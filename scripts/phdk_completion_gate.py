#!/usr/bin/env python3
"""Fail-closed remote delivery evidence verifier. Python standard library only."""

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path, PureWindowsPath


def git(*args):
    p = subprocess.run(
        ["git", *args], capture_output=True, text=True, timeout=25, check=False
    )
    if p.returncode:
        raise RuntimeError(f"git {' '.join(args)} failed: {p.stderr.strip()}")
    return p.stdout.strip()


def extract_version(content, property_path=None):
    """Read a plain-text version or an explicitly selected JSON property."""
    if property_path is None:
        return content.strip()
    if not isinstance(property_path, str) or not re.fullmatch(
        r"[A-Za-z_][A-Za-z0-9_-]*(?:\.[A-Za-z_][A-Za-z0-9_-]*)*",
        property_path,
    ):
        raise ValueError("unsafe version_property")
    value = json.loads(content)
    for key in property_path.split("."):
        if not isinstance(value, dict) or key not in value:
            raise ValueError(f"JSON version property {property_path!r} not found")
        value = value[key]
    if not isinstance(value, str) or not value.strip():
        raise ValueError(
            f"JSON version property {property_path!r} must be a non-empty string"
        )
    return value.strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--evidence", default="PHDK_DELIVERY_EVIDENCE.json")
    ap.add_argument("--remote", default="origin")
    ap.add_argument("--version-file", help="Override the evidence version_file")
    ap.add_argument(
        "--version-property", help="Dot-separated JSON property in version_file"
    )
    args = ap.parse_args()
    errors = []
    try:
        data = json.loads(Path(args.evidence).read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise ValueError("root must be object")
    except (OSError, ValueError) as exc:
        print(f"BLOCKED: invalid evidence: {exc}")
        return 1

    for key in (
        "goal",
        "target_branch",
        "expected_version",
        "merged_commit_sha",
        "pr_url",
    ):
        if not isinstance(data.get(key), str) or not data[key].strip():
            errors.append(f"missing {key}")
    sha = data.get("merged_commit_sha", "")
    if not re.fullmatch(r"[a-fA-F0-9]{40}", sha):
        errors.append("merged_commit_sha must be a full 40-character SHA")
    pr = data.get("pr_url", "")
    if not re.fullmatch(r"https://github\.com/[^/\s]+/[^/\s]+/pull/[0-9]+/?", pr):
        errors.append("pr_url must be a concrete GitHub pull request URL")
    checks = data.get("checks")
    if not isinstance(checks, dict) or not checks:
        errors.append("checks must be a nonempty object")
    else:
        for name, entry in checks.items():
            if not isinstance(entry, dict):
                errors.append(f"{name}: invalid check record")
                continue
            status = entry.get("status")
            if status not in ("PASS", "NOT_APPLICABLE"):
                errors.append(f"{name}: status {status!r} prevents COMPLETED")
            if (
                not isinstance(entry.get("evidence"), str)
                or not entry["evidence"].strip()
            ):
                errors.append(f"{name}: missing evidence/rationale")
        if not any(
            x.get("status") == "PASS" for x in checks.values() if isinstance(x, dict)
        ):
            errors.append("at least one actual PASS check required")

    branch = data.get("target_branch", "main")
    version_file = args.version_file or data.get("version_file", "VERSION")
    version_property = (
        args.version_property
        if args.version_property is not None
        else data.get("version_property")
    )
    version_file_path = Path(version_file) if isinstance(version_file, str) else None
    if (
        version_file_path is None
        or version_file_path.is_absolute()
        or PureWindowsPath(version_file).is_absolute()
        or ".." in version_file.replace("\\", "/").split("/")
        or not re.fullmatch(r"[A-Za-z0-9._/-]+", version_file)
    ):
        errors.append("unsafe version_file")
    if version_property is not None and (
        not isinstance(version_property, str)
        or not re.fullmatch(
            r"[A-Za-z_][A-Za-z0-9_-]*(?:\.[A-Za-z_][A-Za-z0-9_-]*)*",
            version_property,
        )
    ):
        errors.append("unsafe version_property")
    if not re.fullmatch(r"[A-Za-z0-9._/-]+", branch):
        errors.append("unsafe branch")
    if not errors:
        try:
            ls = git(
                "ls-remote", "--heads", args.remote, "refs/heads/" + branch
            ).split()
            if len(ls) < 2 or ls[1] != "refs/heads/" + branch:
                raise RuntimeError("remote ref not returned")
            remote_sha = ls[0]
            if remote_sha.lower() != sha.lower():
                errors.append(f"remote {branch} is {remote_sha}, expected {sha}")
            else:
                # Fetch a specific SHA read-only into object database if necessary.
                try:
                    git("cat-file", "-e", sha + "^{commit}")
                except RuntimeError:
                    git("fetch", "--no-tags", args.remote, branch)
                source = git("show", sha + ":" + version_file)
                observed_version = extract_version(source, version_property)
                if observed_version.lstrip("v") != data.get(
                    "expected_version", ""
                ).lstrip("v"):
                    errors.append(
                        f"remote version source {observed_version!r} != expected {data.get('expected_version')!r}"
                    )
        except Exception as exc:
            errors.append(f"remote verification unavailable: {exc}")
    if errors:
        print("BLOCKED: completion proof failed")
        for error in errors:
            print(" - " + error)
        return 1
    print(
        f"PASS: remote {args.remote}/{branch} SHA={sha} VERSION={data['expected_version']}"
    )
    print(
        "Note: PR merge/reviews and product acceptance must also be independently verified."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
