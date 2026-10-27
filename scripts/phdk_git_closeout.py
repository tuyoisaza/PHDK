#!/usr/bin/env python3
"""Safely synchronize local main and retire one verified merged milestone branch.

No provider writes, force pushes, garbage collection, or broad branch deletion.
The caller independently verifies the PR merge and supplies its merge SHA.
For squash/rebase retirement the verified PR head SHA is also required.
"""
import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

SHA = re.compile(r"^[0-9a-fA-F]{40}$")
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

def safe_generated_ignored(changes):
    """Only known disposable ignored paths, never .env or unknown user data."""
    for line in changes:
        if not line.startswith("!! "):
            return False
        relative = line[3:].strip().strip('"').replace("\\", "/")
        if not any(part in GENERATED for part in relative.split("/")):
            return False
    return True

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
        if changes and not (args.allow_generated_ignored and safe_generated_ignored(changes)):
            result["branch_cleanup"] = "RETAINED_UNTRACKED_OR_IGNORED_CONTENT"
            result["retained_entries"] = len(changes)
            return result
        removal = git("worktree", "remove", str(owner_path),
                      cwd=root, required=False)
        if removal.returncode:
            result["branch_cleanup"] = "RETAINED_WORKTREE_REMOVE_REJECTED"
            result["reason"] = (removal.stderr or removal.stdout).strip()[-1200:]
            return result
        result["actions"].append("remove_verified_worktree")
    deletion = git("branch", "-d" if ancestor else "-D",
                   args.branch, cwd=root, required=False)
    if deletion.returncode:
        result["branch_cleanup"] = "RETAINED_BRANCH_DELETE_REJECTED"
        result["reason"] = (deletion.stderr or deletion.stdout).strip()[-1200:]
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
                        help="permit only known disposable ignored build/dependency files")
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
