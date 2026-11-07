#!/usr/bin/env python3
"""Safely synchronize local main and retire one verified merged milestone branch.

No provider writes, force pushes, garbage collection, or broad branch deletion.
The caller independently verifies the PR merge and supplies its merge SHA.
For squash/rebase retirement the verified PR head SHA is also required.
"""
import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath

SHA = re.compile(r"^[0-9a-fA-F]{40}$")
SENSITIVE = {".env", ".ssh", ".aws", ".azure", ".kube", "secrets", "credentials",
             "uploads", "customer-data", "private", "id_rsa", "id_ed25519"}
WINDOWS_SAFE_PATH_LENGTH = 240
MAX_WALK_ENTRIES = 10000

GENERATED = {
    "node_modules", ".next", ".nuxt", "dist", "build", "coverage",
    ".cache", ".turbo", ".vite", "__pycache__", ".pytest_cache",
    "target", "out", ".gradle", ".parcel-cache",
}

def git(*args, cwd=None, required=True):
    command = ["git", *(["-C", str(cwd)] if cwd else []), *args]
    result = subprocess.run(command, capture_output=True, text=True, check=False)
    if required and result.returncode:
        raise RuntimeError(
            f"{' '.join(command)}: {result.stderr.strip() or result.stdout.strip()}"
        )
    return result

def sha(ref, cwd):
    return git("rev-parse", "--verify", ref, cwd=cwd, required=False).stdout.strip()

def worktrees(cwd):
    entries, current = [], None
    for line in git("worktree", "list", "--porcelain", cwd=cwd).stdout.splitlines():
        if not line:
            if current:
                entries.append(current)
            current = None
        elif line.startswith("worktree "):
            current = {"path": line[9:]}
        elif current is not None:
            key, _, value = line.partition(" ")
            current[key] = value or True
    if current:
        entries.append(current)
    return entries

def is_ancestor(older, newer, cwd):
    return git("merge-base", "--is-ancestor", older, newer,
               cwd=cwd, required=False).returncode == 0

def local_changes(path, ignored=False):
    args = ["status", "--porcelain=v1", "--untracked-files=all"]
    if ignored:
        args.append("--ignored")
    return git(*args, cwd=path).stdout.splitlines()

def sensitive(relative):
    parts = PurePosixPath(relative.replace("\\", "/")).parts
    return any(
        part.lower() in SENSITIVE or part.lower().startswith(".env.") or
        part.lower().endswith((".pem", ".key", ".p12", ".pfx", ".sqlite", ".sqlite3"))
        for part in parts
    )


def safe_generated_ignored(changes):
    """Conservative path-level screening; a full walk is required before deletion."""
    for line in changes:
        if not line.startswith("!! "):
            return False
        relative = line[3:].strip().strip('"').replace("\\", "/")
        parts = PurePosixPath(relative).parts
        if (not parts or not any(part in GENERATED for part in parts) or
                sensitive(relative) or ".." in parts):
            return False
    return True


def inspect_payload(path, changes, windows=None):
    """Bounded non-mutating preflight of ignored content, links and long paths."""
    windows = (os.name == "nt") if windows is None else windows
    report = {
        "ignored_entries": sum(x.startswith("!! ") for x in changes),
        "inspected_entries": 0, "windows_long_paths": 0,
        "unsafe_content": bool(changes and not safe_generated_ignored(changes)),
        "inspection_errors": [],
    }
    def check(item):
        report["inspected_entries"] += 1
        if windows and len(str(item)) >= WINDOWS_SAFE_PATH_LENGTH:
            report["windows_long_paths"] += 1
        if report["inspected_entries"] > MAX_WALK_ENTRIES:
            report["inspection_errors"].append("payload exceeds bounded inspection")
        if (item.is_symlink() or (hasattr(item, "is_junction") and item.is_junction())
                or sensitive(str(item.relative_to(path)))):
            report["unsafe_content"] = True
    try:
        for folder, dirs, files in os.walk(
            path, followlinks=False,
            onerror=lambda error: report["inspection_errors"].append(
                f"filesystem traversal failed: {type(error).__name__}"
            ),
        ):
            here = Path(folder)
            check(here)
            for name in dirs + files:
                check(here / name)
            if report["inspection_errors"]:
                break
    except (OSError, ValueError) as exc:
        report["inspection_errors"].append(f"inspection failed: {type(exc).__name__}")
    return report


def managed_manifest_destinations(path, remote_ref):
    allowed = set()
    for ref in ("HEAD", remote_ref):
        content = git("show", f"{ref}:phdk-standards/PHDK_MANIFEST.txt",
                      cwd=path, required=False)
        if content.returncode:
            return None
        for line in content.stdout.splitlines():
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            fields = line.split("|")
            if len(fields) != 2:
                return None
            relative = fields[1].strip()
            checked = PurePosixPath(relative)
            if (not relative or "\\" in relative or checked.is_absolute() or
                    checked.as_posix() != relative or ".." in checked.parts):
                return None
            allowed.add(f"phdk-standards/{relative}")
    return allowed


def managed_segments(contents):
    start, end = b"<!-- PHDK-MANAGED:START -->", b"<!-- PHDK-MANAGED:END -->"
    if contents.count(start) != 1 or contents.count(end) != 1:
        raise ValueError("missing or duplicate native managed block")
    prefix, _, remainder = contents.partition(start)
    managed, _, suffix = remainder.partition(end)
    return prefix, managed, suffix


def normalized_eol(data):
    return data.replace(b"\r\n", b"\n")


def restore_native_managed_only(local_path, baseline):
    original = local_path.read_bytes()
    local_before, _, local_after = managed_segments(original)
    _, baseline_managed, _ = managed_segments(baseline)
    # Keep all project-owned bytes, including their exact checkout line endings.
    existing_crlf = original.count(b"\r\n") > original.count(b"\n") // 2
    if existing_crlf:
        baseline_managed = baseline_managed.replace(b"\r\n", b"\n").replace(b"\n", b"\r\n")
    replacement = (local_before + b"<!-- PHDK-MANAGED:START -->" +
                   baseline_managed + b"<!-- PHDK-MANAGED:END -->" + local_after)
    local_path.write_bytes(replacement)


def reconcile_force_owned_main(main_path, remote_ref):
    """Only with the explicit upgrade-force flag: scoped, backed-up reconciliation."""
    if not is_ancestor(sha("HEAD", main_path), remote_ref, main_path):
        return False, {"reason": "local main is not a fast-forward ancestor"}
    if git("rev-parse", "-q", "--verify", "MERGE_HEAD",
           cwd=main_path, required=False).returncode == 0:
        return False, {"reason": "main has a merge already in progress"}
    changed = local_changes(main_path)
    if not changed:
        return True, {"result": "NO_DIRTY_MANAGED_PATHS"}
    manifest_owned = managed_manifest_destinations(main_path, remote_ref)
    if manifest_owned is None:
        return False, {"reason": "cannot validate both old and new manifest ownership"}
    native = {"AGENTS.md", "CLAUDE.md", ".windsurfrules", ".cursor/rules/phdk.mdc"}
    paths, baselines = [], {}
    for entry in changed:
        if len(entry) < 4 or entry[:2] in ("??", "!!") or " -> " in entry:
            return False, {"reason": "unknown, renamed or untracked main content"}
        relative = entry[3:]
        file = main_path / relative
        if (relative not in manifest_owned | native or not file.is_file() or
                file.is_symlink() or not file.resolve().is_relative_to(main_path.resolve())):
            return False, {"reason": f"non-managed or unsafe dirty path: {relative}"}
        baseline = git("show", f"HEAD:{relative}", cwd=main_path, required=False)
        index = git("show", f":{relative}", cwd=main_path, required=False)
        if baseline.returncode or index.returncode:
            return False, {"reason": f"untracked, missing or newly staged: {relative}"}
        if relative in native:
            try:
                original_before, _, original_after = managed_segments(file.read_bytes())
                head_before, _, head_after = managed_segments(baseline.stdout.encode("utf-8"))
                index_before, _, index_after = managed_segments(index.stdout.encode("utf-8"))
            except ValueError:
                return False, {"reason": f"native markers ambiguous: {relative}"}
            if ((normalized_eol(original_before), normalized_eol(original_after)) !=
                (normalized_eol(head_before), normalized_eol(head_after)) or
                (normalized_eol(index_before), normalized_eol(index_after)) !=
                (normalized_eol(head_before), normalized_eol(head_after))):
                return False, {"reason": f"owner text outside managed block changed: {relative}"}
        paths.append(relative)
        baselines[relative] = baseline.stdout.encode("utf-8")

    common = Path(git("rev-parse", "--git-common-dir", cwd=main_path).stdout.strip())
    if not common.is_absolute():
        common = (main_path / common).resolve()
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ") + "-" + uuid.uuid4().hex[:10]
    folder = common / "phdk" / "closeout-recovery" / stamp
    folder.mkdir(mode=0o700, parents=True, exist_ok=False)
    record = []
    for number, relative in enumerate(paths):
        data = (main_path / relative).read_bytes()
        name = f"{number:03d}.backup"
        saved = folder / name
        saved.write_bytes(data)
        saved.chmod(0o600)
        record.append({"path": relative, "backup": name,
                       "sha256": hashlib.sha256(data).hexdigest()})
    (folder / "changes.diff").write_text(
        git("diff", "--binary", "HEAD", "--", *paths, cwd=main_path).stdout,
        encoding="utf-8",
    )
    (folder / "staged.diff").write_text(
        git("diff", "--cached", "--binary", "--", *paths, cwd=main_path).stdout,
        encoding="utf-8",
    )
    (folder / "working.diff").write_text(
        git("diff", "--binary", "--", *paths, cwd=main_path).stdout,
        encoding="utf-8",
    )
    (folder / "manifest.json").write_text(
        json.dumps({"local_main_sha": sha("HEAD", main_path),
                    "remote_main_sha": sha(remote_ref, main_path),
                    "files": record}, indent=2),
        encoding="utf-8",
    )
    evidence = {"result": "RECONCILED_MANAGED_ONLY", "paths": paths,
                "backup_path": str(folder)}
    try:
        for relative in paths:
            if relative in native:
                # Clear the staged managed edit; replace only the working block.
                git("restore", "--source=HEAD", "--staged", "--", relative, cwd=main_path)
                restore_native_managed_only(main_path / relative, baselines[relative])
            else:
                git("restore", "--source=HEAD", "--staged", "--worktree",
                    "--", relative, cwd=main_path)
    except (OSError, RuntimeError, ValueError) as exc:
        return False, {**evidence, "reason": f"managed restore failed: {exc}"}
    if local_changes(main_path):
        return False, {**evidence, "reason": "main still dirty after managed restoration"}
    return True, evidence


def closeout(args):
    root = Path(git("rev-parse", "--show-toplevel").stdout.strip()).resolve()
    target, remote = args.target, args.remote
    local_ref = f"refs/heads/{target}"
    remote_ref = f"refs/remotes/{remote}/{target}"
    result = {
        "repository": str(root), "target": target, "remote": remote,
        "mode": "APPLY" if args.apply else "INSPECT", "actions": [],
        "local_main": "UNVERIFIED", "branch_cleanup": "NOT_REQUESTED",
    }
    for name in (target, args.branch):
        if name and git("check-ref-format", "--branch", name, cwd=root,
                        required=False).returncode:
            raise RuntimeError("invalid branch name")
    if args.branch == target:
        raise RuntimeError("cleanup branch cannot be target")
    if args.apply and not args.merged_sha:
        raise RuntimeError("--apply requires --merged-sha from independently verified PR merge")
    for value in (args.merged_sha, args.pr_head_sha):
        if value and not SHA.fullmatch(value):
            raise RuntimeError("merge/head SHA must be a full 40-character SHA")
    if args.pr_head_sha and not args.branch:
        raise RuntimeError("--pr-head-sha requires --branch")

    if args.apply:
        git("fetch", "--no-tags", remote, target, cwd=root)
        result["actions"].append("fetch_target")
        fetched = sha("FETCH_HEAD", root)
        tracked = sha(remote_ref, root)
        if not fetched or fetched != tracked:
            raise RuntimeError("fetched target and remote-tracking ref differ")
    remote_head = sha(remote_ref, root)
    result["remote_main_sha"] = remote_head or None
    if not remote_head:
        raise RuntimeError("remote-tracking target unavailable")
    if args.merged_sha and not is_ancestor(args.merged_sha, remote_ref, root):
        raise RuntimeError("supplied merged PR SHA is not contained in remote target")

    trees = worktrees(root)
    result["worktrees"] = [
        {"path": w["path"], "branch": w.get("branch"),
         "locked": bool(w.get("locked")), "prunable": bool(w.get("prunable"))}
        for w in trees
    ]
    main_tree = next((w for w in trees if w.get("branch") == local_ref), None)
    local_head = sha(local_ref, root)
    result["local_main_sha_before"] = local_head or None
    if not args.apply:
        if local_head:
            counts = git("rev-list", "--left-right", "--count",
                         f"{local_ref}...{remote_ref}", cwd=root).stdout.split()
            result["ahead_by"], result["behind_by"] = [int(v) for v in counts]
            result["local_main"] = (
                "SYNCED" if local_head == remote_head else "DIVERGED_OR_BEHIND"
            )
        else:
            result["local_main"] = "MISSING"
        return result

    if not main_tree:
        # Do not rewrite a checked-out main ref; use normal Git worktree operations.
        if local_changes(root):
            result["local_main"] = "BLOCKED_DIRTY_CURRENT_WORKTREE"
            return result
        if not local_head:
            git("switch", "--create", target, "--track", f"{remote}/{target}", cwd=root)
            result["actions"].append("create_tracking_main")
        else:
            git("switch", target, cwd=root)
            result["actions"].append("switch_to_main")
        main_tree = {"path": str(root), "branch": local_ref}

    main_path = Path(main_tree["path"])
    if local_changes(main_path):
        if args.reconcile_force_owned:
            safe, evidence = reconcile_force_owned_main(main_path, remote_ref)
            result["managed_reconciliation"] = evidence
            if not safe:
                result["local_main"] = "BLOCKED_MANAGED_RECONCILIATION"
                return result
        else:
            result["local_main"] = "BLOCKED_DIRTY_MAIN_WORKTREE"
            return result
    ff = git("merge", "--ff-only", remote_ref, cwd=main_path, required=False)
    if ff.returncode:
        result["local_main"] = "BLOCKED_NON_FAST_FORWARD_OR_CONFLICT"
        result["reason"] = (ff.stderr or ff.stdout).strip()[-1200:]
        return result
    result["actions"].append("fast_forward_local_main")
    local_head = sha(local_ref, root)
    result["local_main_sha_after"] = local_head
    if local_head != remote_head:
        result["local_main"] = "BLOCKED_SHA_MISMATCH"
        return result
    result["local_main"] = "SYNCED"

    if not args.branch:
        return result
    branch_ref = f"refs/heads/{args.branch}"
    head = sha(branch_ref, root)
    if not head:
        result["branch_cleanup"] = "ALREADY_ABSENT"
        return result
    if args.pr_head_sha and args.pr_head_sha.lower() != head.lower():
        result["branch_cleanup"] = "BLOCKED_PR_HEAD_SHA_MISMATCH"
        return result
    ancestor = is_ancestor(head, local_ref, root)
    # For squash/rebase, require independently verified merged PR head + merge.
    verified_pr = bool(args.pr_head_sha and args.merged_sha)
    if not ancestor and not verified_pr:
        result["branch_cleanup"] = "RETAINED_UNMERGED_OR_SQUASH_UNVERIFIED"
        return result
    owner_tree = next(
        (w for w in worktrees(root) if w.get("branch") == branch_ref), None
    )
    if owner_tree:
        owner_path = Path(owner_tree["path"]).resolve()
        if owner_tree.get("locked") or owner_tree.get("prunable") or owner_path == root:
            result["branch_cleanup"] = "RETAINED_LOCKED_OR_ACTIVE_WORKTREE"
            return result
        changes = local_changes(owner_path, ignored=True)
        payload = inspect_payload(owner_path, changes)
        result["worktree_payload"] = payload
        if payload["inspection_errors"] or payload["windows_long_paths"]:
            result["branch_cleanup"] = (
                "RETAINED_WINDOWS_LONG_PATH_RISK" if payload["windows_long_paths"]
                else "RETAINED_INSPECTION_UNVERIFIED"
            )
            return result
        if changes and not (args.allow_generated_ignored and
                            safe_generated_ignored(changes) and
                            not payload["unsafe_content"]):
            result["branch_cleanup"] = "RETAINED_UNTRACKED_OR_IGNORED_CONTENT"
            result["retained_entries"] = len(changes)
            return result
        removal = git("worktree", "remove", str(owner_path),
                      cwd=root, required=False)
        registry_error = None
        try:
            registered = any(
                Path(w["path"]).resolve() == owner_path for w in worktrees(root)
            )
        except (RuntimeError, OSError) as exc:
            registered, registry_error = None, str(exc)
        exists = os.path.lexists(owner_path)
        residual = inspect_payload(owner_path, []) if exists else None
        result["worktree_postcondition"] = {
            "registered": registered, "directory_exists": exists,
            "residual_inventory": residual,
            "registration_error": registry_error,
            "branch_sha": sha(branch_ref, root) or None,
        }
        if removal.returncode or registered is not False or exists:
            result["branch_cleanup"] = (
                "PARTIAL_CLOSEOUT" if (registered is False and exists) or
                (registered is True and not exists) else
                "RETAINED_WORKTREE_REMOVE_REJECTED"
            )
            result["reason"] = (removal.stderr or removal.stdout).strip()[-1200:]
            return result
        result["actions"].append("remove_verified_worktree")
    if ancestor:
        deletion = git("branch", "-d", args.branch, cwd=root, required=False)
    else:
        # Verified squash/rebase only: atomic SHA-guarded deletion, not a forced delete.
        deletion = git("update-ref", "-d", branch_ref, head, cwd=root, required=False)
    if deletion.returncode:
        result["branch_cleanup"] = "RETAINED_BRANCH_DELETE_REJECTED"
        result["reason"] = (deletion.stderr or deletion.stdout).strip()[-1200:]
    elif sha(branch_ref, root):
        result["branch_cleanup"] = "PARTIAL_BRANCH_CLOSEOUT"
    else:
        result["branch_cleanup"] = "REMOVED_VERIFIED_BRANCH"
        result["actions"].append("delete_verified_local_branch")
    return result

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--remote", default="origin")
    parser.add_argument("--target", default="main")
    parser.add_argument("--merged-sha", help="40-character verified merged PR SHA")
    parser.add_argument("--branch", help="only this milestone-owned local branch")
    parser.add_argument("--pr-head-sha", help="40-character verified PR head SHA")
    parser.add_argument("--allow-generated-ignored", action="store_true",
                        help="permit only inspected generated ignored build/dependency files")
    parser.add_argument("--reconcile-force-owned", action="store_true",
                        help="upgrade force only: back up and replace tracked PHDK-owned main edits")
    args = parser.parse_args()
    try:
        report = closeout(args)
        print(json.dumps(report, indent=2, sort_keys=True))
        if args.apply and report["local_main"] != "SYNCED":
            return 2
        if args.apply and args.branch and report["branch_cleanup"] not in (
            "REMOVED_VERIFIED_BRANCH", "ALREADY_ABSENT"
        ):
            return 3
        return 0
    except (RuntimeError, OSError) as exc:
        print(json.dumps({"status": "BLOCKED", "error": str(exc)}),
              file=sys.stderr)
        return 2

if __name__ == "__main__":
    sys.exit(main())
