#!/usr/bin/env python3
"""Read-only, Git-aware remote-main proof for manifest-vendored PHDK objects.

Compares remote Git blobs with the checkout after Git's built-in clean conversion.
Never invokes custom filter drivers or treats a transformed byte stream as
application/runtime, native-rule, PR, or deployment evidence.
"""
import argparse
import json
import re
import subprocess
import sys
from pathlib import Path, PurePosixPath

SAFE = re.compile(r"^[A-Za-z0-9._/-]+$")
OID = re.compile(r"^[0-9a-f]{40,64}$")


def git(repo, *args, input_bytes=None):
    result = subprocess.run(
        ["git", "-C", str(repo), *args], input=input_bytes,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False,
    )
    if result.returncode:
        raise RuntimeError(
            f"git {args[0]} failed: {result.stderr.decode(errors='replace').strip()[-500:]}"
        )
    return result.stdout


def manifest_entries(contents):
    entries, seen = [], set()
    for line in contents.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        fields = line.split("|")
        if len(fields) != 2:
            raise ValueError("invalid manifest entry")
        source, destination = (field.strip() for field in fields)
        for value in (source, destination):
            path = PurePosixPath(value)
            if (not SAFE.fullmatch(value) or "\\" in value or
                    path.is_absolute() or ".." in path.parts or
                    path.as_posix() != value or value.startswith("-")):
                raise ValueError("unsafe manifest path")
        if destination in seen:
            raise ValueError("duplicate manifest destination")
        seen.add(destination)
        entries.append((source, destination))
    if not entries or not {"VERSION", "PHDK_MANIFEST.txt"} <= seen:
        raise ValueError("incomplete manifest")
    return entries


def manifest_paths(contents):
    """Compatibility API used by existing consumers and regression tests."""
    return [destination for _, destination in manifest_entries(contents)]


def attributes(repo, relative, remote_sha=None):
    args = ["check-attr", "-z"]
    if remote_sha:
        args.append(f"--source={remote_sha}")
    args += ["--all", "--", relative]
    fields = git(repo, *args).split(b"\0")
    if fields and fields[-1] == b"":
        fields.pop()
    if len(fields) % 3:
        raise RuntimeError("malformed git check-attr output")
    return {
        fields[i + 1].decode("utf-8", "replace"): fields[i + 2].decode("utf-8", "replace")
        for i in range(0, len(fields), 3)
    }


def remote_blob(repo, remote_sha, relative):
    entries = git(repo, "ls-tree", "-z", remote_sha, "--", relative)
    if not entries or entries.count(b"\0") != 1:
        raise RuntimeError("missing or ambiguous remote Git object")
    info, sep, name = entries.rstrip(b"\0").partition(b"\t")
    tokens = info.split()
    if (not sep or name.decode("utf-8", "replace") != relative or
            len(tokens) != 3 or tokens[0] not in (b"100644", b"100755") or
            tokens[1] != b"blob"):
        raise RuntimeError("remote entry is not a regular file blob")
    oid = tokens[2].decode("ascii")
    if not OID.fullmatch(oid):
        raise RuntimeError("invalid remote blob OID")
    return oid


def read_head(repo, remote, branch):
    ref = f"refs/heads/{branch}"
    fields = git(repo, "ls-remote", "--heads", remote, ref).decode().split()
    if len(fields) != 2 or fields[1] != ref or not OID.fullmatch(fields[0]):
        raise RuntimeError("remote target branch not returned")
    return fields[0]


def verify(project, remote, branch, expected_version):
    if (not SAFE.fullmatch(remote) or not SAFE.fullmatch(branch)
            or remote.startswith("-") or branch.startswith("-")
            or ".." in remote or ".." in branch or "//" in branch):
        raise ValueError("unsafe remote or branch")
    project = project.resolve()
    base = project / "phdk-standards"
    base_resolved = base.resolve()
    manifest = (base / "PHDK_MANIFEST.txt").read_text(encoding="utf-8")
    entries = manifest_entries(manifest)
    version = (base / "VERSION").read_text(encoding="utf-8").strip()
    if expected_version and version != expected_version:
        raise ValueError(f"installed version {version} != expected {expected_version}")

    remote_sha = read_head(project, remote, branch)
    git(project, "fetch", "--no-tags", remote, branch)
    fetched = git(project, "rev-parse", "--verify", "FETCH_HEAD").decode().strip()
    if fetched != remote_sha:
        raise RuntimeError("remote target moved during verification; refresh")

    published_manifest = git(
        project, "show", f"{remote_sha}:phdk-standards/PHDK_MANIFEST.txt"
    ).decode("utf-8")
    if manifest_entries(published_manifest) != entries:
        raise RuntimeError("local and published manifest mappings differ")

    errors, evidence = [], []
    for _, destination in entries:
        relative = f"phdk-standards/{destination}"
        path = base / destination
        entry = {"path": destination}
        try:
            # Do not follow symlinks even if they resolve to files in the repo.
            local = path.resolve()
            if (not local.is_relative_to(base_resolved) or path.is_symlink()
                    or not path.is_file()):
                raise RuntimeError("missing, symlinked or unsafe local file")
            content = path.read_bytes()
            oid = remote_blob(project, remote_sha, relative)
            entry["remote_blob_sha"] = oid
            raw_oid = git(project, "hash-object", "--stdin", input_bytes=content).decode().strip()
            if raw_oid == oid:
                entry["result"] = "RAW_BYTES_IDENTICAL"
            else:
                # A custom filter can execute arbitrary software; never run it as
                # a side effect of this read-only proof.
                actual = attributes(project, relative)
                canonical = attributes(project, relative, remote_sha=remote_sha)
                if actual != canonical:
                    raise RuntimeError("ATTRIBUTE_MISMATCH: checkout and published attributes differ")
                if canonical.get("filter") not in (None, "unset", "unspecified"):
                    raise RuntimeError("CUSTOM_FILTER_UNVERIFIED: raw bytes differ")
                normalized_oid = git(
                    project, "hash-object", f"--path={relative}", "--stdin",
                    input_bytes=content,
                ).decode().strip()
                if normalized_oid != oid:
                    raise RuntimeError("CONTENT_MISMATCH: Git-cleaned blob differs")
                entry["result"] = "LOCAL_REPRESENTATION_ONLY"
                entry["git_attributes"] = canonical
        except (OSError, RuntimeError, UnicodeError) as exc:
            entry["result"] = "BLOCKED"
            entry["reason"] = str(exc)
            errors.append(f"{destination}: {exc}")
        evidence.append(entry)

    if read_head(project, remote, branch) != remote_sha:
        errors.append("remote target moved after verification; retry against a fresh SHA")
    representation = sum(x["result"] == "LOCAL_REPRESENTATION_ONLY" for x in evidence)
    return {
        "status": "PASS" if not errors else "BLOCKED",
        "remote_main_sha": remote_sha,
        "expected_phdk_version": version,
        "manifest_files_checked": len(entries),
        "representation_only_count": representation,
        "file_evidence": evidence,
        "native_managed_block": "VERIFY_SEPARATELY",
        "pull_request_merge": "VERIFY_SEPARATELY",
        "product_version_and_deployment": "VERIFY_SEPARATELY",
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
    except (ValueError, OSError, RuntimeError, UnicodeError) as error:
        result = {"status": "BLOCKED", "reason": str(error)}
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["status"] == "PASS" else 2


if __name__ == "__main__":
    sys.exit(main())
