#!/usr/bin/env python3
"""Conservative foreground sync; signal the agent's separate stack review."""
import argparse, pathlib, subprocess, tempfile, shutil, json, sys

def run(*args, cwd=None):
    return subprocess.check_output(args, cwd=cwd, text=True).strip()

def sync_result(status, *, trigger, installed, latest, upstream_sha, files=0):
    adopted = status == "UPDATED" and installed != latest
    required = trigger == "upgrade" or adopted
    return {
        "status": status,
        "standards_sync": "MANIFEST_VERIFIED" if status != "NEWER_LOCAL" else "SKIPPED_NEWER_LOCAL",
        "version": installed if status == "NEWER_LOCAL" else latest,
        "previous_version": installed,
        "upstream_version": latest,
        "version_adopted": adopted,
        "files": files,
        "upstream_sha": upstream_sha,
        "trigger": trigger,
        "stack_review_required": required,
        "stack_review_coverage": "PENDING" if required else "NOT_TRIGGERED",
        "stack_security_status": "UNVERIFIED",
        "stack_review_reason": "EXPLICIT_UPGRADE" if trigger == "upgrade" else (
            "PREFLIGHT_VERSION_ADOPTION" if adopted else "NO_NEW_VERSION_ADOPTED"
        ),
    }


def sync(project, trigger="preflight"):
    if trigger not in {"preflight", "upgrade"}:
        raise ValueError("Invalid trigger")
    target = project / "phdk-standards"
    if not (target / "VERSION").exists():
        raise ValueError("PHDK is not installed")
    with tempfile.TemporaryDirectory() as temp:
        run("git", "clone", "--quiet", "--depth", "1", "--branch", "main",
            "https://github.com/tuyoisaza/PHDK.git", temp)
        upstream = pathlib.Path(temp)
        latest = (upstream / "VERSION").read_text().strip()
        installed = (target / "VERSION").read_text().strip()
        upstream_sha = run("git", "rev-parse", "HEAD", cwd=upstream)
        def semver(v):
            parts = v.split(".")
            if len(parts) != 3 or not all(p.isdecimal() for p in parts):
                raise ValueError("Invalid version")
            return tuple(map(int, parts))
        if semver(latest) < semver(installed):
            return sync_result("NEWER_LOCAL", trigger=trigger, installed=installed,
                               latest=latest, upstream_sha=upstream_sha)
        changes = []
        seen = set()
        for line in (upstream / "PHDK_MANIFEST.txt").read_text().splitlines():
            if not line.strip() or line.startswith("#"):
                continue
            src, dst = map(str.strip, line.split("|"))
            for name in (src, dst):
                if pathlib.PurePosixPath(name).is_absolute() or ".." in pathlib.PurePosixPath(name).parts:
                    raise ValueError("Unsafe manifest path")
            if dst in seen:
                raise ValueError("Duplicate destination")
            seen.add(dst)
            source = (upstream / src).resolve()
            dest = (target / dst).resolve()
            if not source.is_relative_to(upstream) or not dest.is_relative_to(target) or not source.is_file():
                raise ValueError("Invalid source/destination")
            if not dest.is_file() or source.read_bytes() != dest.read_bytes():
                status = run("git", "status", "--porcelain", "--", str(dest.relative_to(project)), cwd=project)
                if status:
                    raise ValueError("Local edits: " + str(dest))
                changes.append((source, dest))
        snapshots = [(dst, dst.read_bytes() if dst.is_file() else None) for _, dst in changes]
        try:
            for src, dst in changes:
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(src, dst)
                if src.read_bytes() != dst.read_bytes():
                    raise ValueError("Verification failed")
        except Exception:
            for dst, old in snapshots:
                if old is None:
                    dst.unlink(missing_ok=True)
                else:
                    dst.write_bytes(old)
            raise
        return sync_result("UPDATED" if changes else "CURRENT", trigger=trigger,
                           installed=installed, latest=latest, upstream_sha=upstream_sha,
                           files=len(changes))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project", nargs="?", default=".")
    parser.add_argument("--trigger", choices=("preflight", "upgrade"), default="preflight",
                        help="Upgrade requires an agent stack review even when standards are current.")
    args = parser.parse_args()
    try:
        print(json.dumps(sync(pathlib.Path(args.project).resolve(), trigger=args.trigger)))
    except Exception as e:
        print(json.dumps({"status": "BLOCKED", "standards_sync": "BLOCKED", "reason": str(e),
                          "trigger": args.trigger, "stack_review_required": args.trigger == "upgrade",
                          "stack_review_coverage": "PENDING" if args.trigger == "upgrade" else "NOT_TRIGGERED",
                          "stack_security_status": "UNVERIFIED"}), file=sys.stderr)
        sys.exit(2)
