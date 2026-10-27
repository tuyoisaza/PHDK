#!/usr/bin/env python3
"""Read-only remote-main check for vendored PHDK content; not PR/UAT proof."""
import argparse
import json
import re
import subprocess
import sys
from pathlib import Path, PurePosixPath

SAFE = re.compile(r"^[A-Za-z0-9._/-]+$")


def git(repo, *args):
    result = subprocess.run(
        ["git", "-C", str(repo), *args],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False,
    )
    if result.returncode:
        raise RuntimeError(
            f"git {args[0]} failed: {result.stderr.decode(errors='replace').strip()[-500:]}"
        )
    return result.stdout


def manifest_paths(contents):
    destinations, seen = [], set()
    for line in contents.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        fields = line.split("|")
        if len(fields) != 2:
            raise ValueError("invalid manifest entry")
        destination = fields[1].strip()
        path = PurePosixPath(destination)
        if (not destination or "\\" in destination or path.is_absolute()
                or ".." in path.parts or path.as_posix() != destination):
            raise ValueError("unsafe manifest destination")
        if destination in seen:
            raise ValueError("duplicate manifest destination")
        seen.add(destination)
        destinations.append(destination)
    if not destinations or "VERSION" not in seen or "PHDK_MANIFEST.txt" not in seen:
        raise ValueError("incomplete manifest")
    return destinations


def verify(project, remote, branch, expected_version):
    if (not SAFE.fullmatch(remote) or not SAFE.fullmatch(branch)
            or remote.startswith("-") or branch.startswith("-")
            or ".." in remote or ".." in branch or "//" in branch):
        raise ValueError("unsafe remote or branch")
    project = project.resolve()
    base = project / "phdk-standards"
    manifest = (base / "PHDK_MANIFEST.txt").read_text(encoding="utf-8")
    paths = manifest_paths(manifest)
    version = (base / "VERSION").read_text(encoding="utf-8").strip()
    if expected_version and version != expected_version:
        raise ValueError(f"installed version {version} != expected {expected_version}")
    ref = f"refs/heads/{branch}"
    ls = git(project, "ls-remote", "--heads", remote, ref).decode().strip().split()
    if len(ls) != 2 or ls[1] != ref or not re.fullmatch(r"[0-9a-f]{40}", ls[0]):
        raise RuntimeError("remote target branch not returned")
    remote_sha = ls[0]
    # This fetch reads the remote; it never pushes, merges or deletes.
    git(project, "fetch", "--no-tags", remote, branch)
    fetched = git(project, "rev-parse", "--verify", "FETCH_HEAD").decode().strip()
    if fetched != remote_sha:
        raise RuntimeError("remote target moved during verification; refresh")
    errors = []
    for destination in paths:
        local_path = (base / destination).resolve()
        if not local_path.is_relative_to(base.resolve()) or not local_path.is_file():
            errors.append(f"missing/unsafe local: {destination}")
            continue
        try:
            published = git(project, "show", f"{remote_sha}:phdk-standards/{destination}")
        except RuntimeError:
            errors.append(f"missing remote main: {destination}")
            continue
        if published != local_path.read_bytes():
            errors.append(f"mismatch remote main: {destination}")
    return {
        "status": "PASS" if not errors else "BLOCKED",
        "remote_main_sha": remote_sha,
        "expected_phdk_version": version,
        "manifest_files_checked": len(paths),
        "native_managed_block": "VERIFY_SEPARATELY",
        "pull_request_merge": "VERIFY_SEPARATELY",
        "local_main_and_worktree_closeout": "VERIFY_SEPARATELY",
        "mismatches": errors[:30],
        "mismatch_count": len(errors),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", default=".")
    parser.add_argument("--remote", default="origin")
    parser.add_argument("--branch", default="main")
    parser.add_argument("--expected-version")
    args = parser.parse_args()
    try:
        result = verify(Path(args.project), args.remote, args.branch, args.expected_version)
    except (ValueError, OSError, RuntimeError) as error:
        result = {"status": "BLOCKED", "reason": str(error)}
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["status"] == "PASS" else 2


if __name__ == "__main__":
    sys.exit(main())
