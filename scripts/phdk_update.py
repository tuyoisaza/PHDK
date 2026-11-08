#!/usr/bin/env python3
"""Conservative foreground sync; signal the agent's separate stack review."""

import argparse
import pathlib
import re
import subprocess
import tempfile
import shutil
import json
import sys
import hashlib


def run(*args, cwd=None):
    return subprocess.check_output(args, cwd=cwd, text=True).strip()


def sync_result(status, *, trigger, installed, latest, upstream_sha, files=0, force_owned=False, overwritten=None, removed=None, unmanaged=None):
    adopted = status == "UPDATED" and installed != latest
    required = trigger == "upgrade" or adopted
    return {
        "status": status,
        "standards_sync": "MANIFEST_VERIFIED"
        if status != "NEWER_LOCAL"
        else "SKIPPED_NEWER_LOCAL",
        "version": installed if status == "NEWER_LOCAL" else latest,
        "previous_version": installed,
        "upstream_version": latest,
        "version_adopted": adopted,
        "files": files,
        "upstream_sha": upstream_sha,
        "trigger": trigger,
        "force_owned": force_owned,
        "overwritten_owned_paths": overwritten or [],
        "removed_obsolete_owned_paths": removed or [],
        "unmanaged_active_vendor_paths": unmanaged or [],
        "vendor_integrity": "PARTIAL_UNMANAGED_ACTIVE" if unmanaged else "MANAGED_SNAPSHOT_VERIFIED",
        "remote_main_verification": "UNVERIFIED",
        "forced_upgrade_publication": "PENDING_REMOTE_MAIN_CHECKPOINT" if force_owned else "NOT_AUTHORIZED_BY_COPIER",
        "auto_force_handoff": "PENDING_PUBLICATION" if force_owned else "NOT_TRIGGERED",
        "stack_review_required": required,
        "stack_review_coverage": "PENDING" if required else "NOT_TRIGGERED",
        "stack_security_status": "UNVERIFIED",
        "stack_review_reason": "EXPLICIT_UPGRADE"
        if trigger == "upgrade"
        else ("PREFLIGHT_VERSION_ADOPTION" if adopted else "NO_NEW_VERSION_ADOPTED"),
    }


def select_upstream(upstream, pinned_sha=None):
    """Use a fixed canonical Git commit; fail closed if it cannot be fetched."""
    if pinned_sha is not None and not re.fullmatch(r"[0-9a-fA-F]{40}", pinned_sha):
        raise ValueError("invalid --upstream-sha: expected full 40-character Git SHA")
    observed = run("git", "rev-parse", "HEAD", cwd=upstream)
    if not pinned_sha:
        return observed
    pinned_sha = pinned_sha.lower()
    if observed != pinned_sha:
        # The already-fetched main may have advanced. Fetch ONLY the authorized
        # pinned commit into the temporary clone; do not silently adopt new main.
        run("git", "fetch", "--no-tags", "--depth", "1", "origin", pinned_sha, cwd=upstream)
        if run("git", "rev-parse", "FETCH_HEAD", cwd=upstream) != pinned_sha:
            raise RuntimeError("pinned canonical commit was not fetched")
        run("git", "checkout", "--detach", pinned_sha, cwd=upstream)
    if run("git", "rev-parse", "HEAD", cwd=upstream) != pinned_sha:
        raise RuntimeError("pinned canonical commit identity changed")
    return pinned_sha



def _git_blob_id(data):
    """Calculate an unfiltered Git blob ID; never run project-defined filters."""
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def _content_blob_candidates(data):
    ids = {_git_blob_id(data)}
    if b"\r\n" in data and b"\0" not in data:
        try:
            data.decode("utf-8")
        except UnicodeDecodeError:
            pass
        else:
            ids.add(_git_blob_id(data.replace(b"\r\n", b"\n")))
    return ids


def _historical_blobs(upstream, source, cache):
    """Historical canonical provenance is restricted to the pinned HEAD ancestry."""
    if source in cache:
        return cache[source]
    if not cache.get("_history_loaded"):
        if run("git", "rev-parse", "--is-shallow-repository", cwd=upstream) == "true":
            run("git", "fetch", "--quiet", "--unshallow", "--no-tags",
                "origin", "main", cwd=upstream)
        cache["_history_loaded"] = True
    revisions = run("git", "log", "--format=%H", "HEAD", "--", source,
                    cwd=upstream).splitlines()
    published = set()
    for commit in revisions:
        try:
            published.add(run("git", "rev-parse", "--verify",
                              f"{commit}:{source}", cwd=upstream))
        except subprocess.CalledProcessError:
            continue
    cache[source] = published
    return published


def is_published_copy(data, upstream, source, cache):
    """Proven published PHDK text is not a downstream customization."""
    return bool(_content_blob_candidates(data) &
                _historical_blobs(upstream, source, cache))


def _manifest_pairs(path):
    if not path.is_file():
        return []
    entries = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        pair = [value.strip() for value in line.split("|")]
        if len(pair) != 2 or not all(pair):
            raise ValueError("Invalid manifest entry")
        entries.append(tuple(pair))
    return entries


def _vendor_path(root, name):
    path = pathlib.PurePosixPath(name)
    if (path.is_absolute() or not path.parts or name == "."
            or ".." in path.parts or "\\" in name or "\0" in name):
        raise ValueError("Unsafe vendored path: " + name)
    if (root / name).is_symlink():
        raise ValueError("Symlink not supported for vendored path: " + name)
    dest = (root / name).resolve()
    if not dest.is_relative_to(root.resolve()):
        raise ValueError("Vendored path escapes root: " + name)
    return dest


def _unmanaged_active(root, destinations):
    """Unknown active extras are reported, not deleted or overwritten."""
    extras = []
    for path in [*root.glob("*.md"), *root.glob("scripts/phdk_*.py")]:
        relative = path.relative_to(root).as_posix()
        if (path.is_file() and not path.is_symlink()
                and relative not in destinations
                and not path.name.endswith("_REPORT.md")):
            extras.append(relative)
    return sorted(set(extras))


def sync(project, trigger="preflight", force_owned=False, upstream_sha=None):
    project = pathlib.Path(project).resolve()
    if trigger not in {"preflight", "upgrade"}:
        raise ValueError("Invalid trigger")
    if force_owned and trigger != "upgrade":
        raise ValueError("--force-owned requires --trigger upgrade")
    target = project / "phdk-standards"
    if not (target / "VERSION").exists():
        raise ValueError("PHDK is not installed")
    with tempfile.TemporaryDirectory() as temp:
        run(
            "git",
            "clone",
            "--quiet",
            "--depth",
            "1",
            "--branch",
            "main",
            "https://github.com/tuyoisaza/PHDK.git",
            temp,
        )
        upstream = pathlib.Path(temp)
        upstream_sha = select_upstream(upstream, upstream_sha)
        latest = (upstream / "VERSION").read_text().strip()
        installed = (target / "VERSION").read_text().strip()

        def semver(v):
            parts = v.split(".")
            if len(parts) != 3 or not all(p.isdecimal() for p in parts):
                raise ValueError("Invalid version")
            return tuple(map(int, parts))

        if semver(latest) < semver(installed):
            return sync_result(
                "NEWER_LOCAL",
                trigger=trigger,
                installed=installed,
                latest=latest,
                upstream_sha=upstream_sha,
                force_owned=force_owned,
            )
        changes, overwritten, conflicts, removals = [], [], [], []
        seen, history_cache = set(), {}
        previous_manifest = target / "PHDK_MANIFEST.txt"
        new_mappings = _manifest_pairs(upstream / "PHDK_MANIFEST.txt")
        # A locally edited manifest cannot prove that extras are PHDK-owned.
        old_manifest_trusted = False
        if previous_manifest.is_file():
            old_bytes = previous_manifest.read_bytes()
            old_manifest_trusted = (
                old_bytes == (upstream / "PHDK_MANIFEST.txt").read_bytes()
            )
            if not old_manifest_trusted:
                try:
                    old_manifest_trusted = is_published_copy(
                        old_bytes, upstream, "PHDK_MANIFEST.txt", history_cache)
                except subprocess.CalledProcessError:
                    old_manifest_trusted = False
        old_mappings = (_manifest_pairs(previous_manifest)
                        if old_manifest_trusted else [])
        for src, dst in new_mappings:
            source = _vendor_path(upstream, src)
            dest = _vendor_path(target, dst)
            if dst in seen:
                raise ValueError("Duplicate destination: " + dst)
            seen.add(dst)
            if not source.is_file():
                raise ValueError("Invalid manifest source: " + src)
            if dest.is_file() and source.read_bytes() == dest.read_bytes():
                continue
            status = run("git", "status", "--porcelain", "--",
                         str(dest.relative_to(project)), cwd=project)
            if status and not force_owned:
                conflicts.append(dst + " (uncommitted edit/deletion)")
                continue
            if dest.is_file() and not force_owned:
                try:
                    canonical = is_published_copy(
                        dest.read_bytes(), upstream, src, history_cache)
                except subprocess.CalledProcessError:
                    canonical = False
                if not canonical:
                    conflicts.append(dst + " (customized or unverified origin)")
                    continue
            if dest.is_file() and (status or force_owned):
                overwritten.append(str(dest.relative_to(project)))
            changes.append((source, dest))

        for src, dst in old_mappings:
            if dst in seen:
                continue
            dest = _vendor_path(target, dst)
            if not dest.exists():
                continue
            if not dest.is_file():
                conflicts.append(dst + " (obsolete non-file path)")
                continue
            status = run("git", "status", "--porcelain", "--",
                         str(dest.relative_to(project)), cwd=project)
            if not force_owned:
                if status:
                    conflicts.append(dst + " (obsolete customization)")
                    continue
                try:
                    canonical = is_published_copy(
                        dest.read_bytes(), upstream, src, history_cache)
                except subprocess.CalledProcessError:
                    canonical = False
                if not canonical:
                    conflicts.append(dst + " (obsolete origin unverified)")
                    continue
            removals.append(dest)

        if force_owned:
            # Extra PHDK files may predate the manifest: remove only a source
            # copied verbatim from canonical history, never an unknown add-on.
            for relative in _unmanaged_active(target, seen):
                dest = _vendor_path(target, relative)
                if dest in removals:
                    continue
                try:
                    canonical = is_published_copy(
                        dest.read_bytes(), upstream, relative, history_cache)
                except subprocess.CalledProcessError:
                    canonical = False
                if canonical:
                    removals.append(dest)

        if conflicts:
            raise ValueError("PHDK customization preserved; no files changed: "
                             + "; ".join(conflicts))
        snapshots = [
            (dst, dst.read_bytes() if dst.is_file() else None)
            for _, dst in changes
        ] + [(dst, dst.read_bytes()) for dst in removals]
        try:
            for source, dest in changes:
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(source, dest)
                if source.read_bytes() != dest.read_bytes():
                    raise ValueError("Vendor file verification failed")
            for dest in removals:
                dest.unlink()
                if dest.exists():
                    raise ValueError("Obsolete vendor file not removed")
        except Exception:
            for dest, old in snapshots:
                if old is None:
                    dest.unlink(missing_ok=True)
                else:
                    dest.parent.mkdir(parents=True, exist_ok=True)
                    dest.write_bytes(old)
            raise
        unmanaged = _unmanaged_active(target, seen)
        if not old_manifest_trusted:
            unmanaged.append("PHDK_MANIFEST.txt:PREVIOUS_ORIGIN_UNVERIFIED")
        return sync_result(
            "UPDATED" if changes or removals else "CURRENT",
            trigger=trigger,
            installed=installed,
            latest=latest,
            upstream_sha=upstream_sha,
            files=len(changes),
            force_owned=force_owned,
            overwritten=overwritten,
            removed=[str(p.relative_to(project)) for p in removals],
            unmanaged=unmanaged,
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project", nargs="?", default=".")
    parser.add_argument(
        "--trigger",
        choices=("preflight", "upgrade"),
        default="preflight",
        help="Upgrade requires an agent stack review even when standards are current.",
    )
    parser.add_argument(
        "--force-owned", action="store_true",
        help="Only for exact owner-invoked PHDK upgrade force; replace dirty manifest-owned files.",
    )
    parser.add_argument(
        "--upstream-sha", help="optional full canonical commit SHA pinned for this invocation",
    )
    args = parser.parse_args()
    try:
        print(
            json.dumps(sync(pathlib.Path(args.project).resolve(), trigger=args.trigger,
                            force_owned=args.force_owned, upstream_sha=args.upstream_sha))
        )
    except Exception as e:
        print(
            json.dumps(
                {
                    "status": "BLOCKED",
                    "standards_sync": "BLOCKED",
                    "reason": str(e),
                    "trigger": args.trigger,
                    "force_owned": args.force_owned,
                    "remote_main_verification": "UNVERIFIED",
                    "stack_review_required": args.trigger == "upgrade",
                    "stack_review_coverage": "PENDING"
                    if args.trigger == "upgrade"
                    else "NOT_TRIGGERED",
                    "stack_security_status": "UNVERIFIED",
                }
            ),
            file=sys.stderr,
        )
        sys.exit(2)
