#!/usr/bin/env python3
"""PHDK conservative foreground update. Invoked only during authorized Preflight."""
import pathlib, subprocess, tempfile, shutil, json, sys

def run(*args, cwd=None):
    return subprocess.check_output(args, cwd=cwd, text=True).strip()

def sync(project):
    target = project / "phdk-standards"
    if not (target / "VERSION").exists():
        raise ValueError("PHDK is not installed")
    with tempfile.TemporaryDirectory() as temp:
        run("git", "clone", "--quiet", "--depth", "1", "--branch", "main",
            "https://github.com/tuyoisaza/PHDK.git", temp)
        upstream = pathlib.Path(temp)
        latest = (upstream / "VERSION").read_text().strip()
        installed = (target / "VERSION").read_text().strip()
        def semver(v):
            parts = v.split(".")
            if len(parts) != 3 or not all(p.isdecimal() for p in parts):
                raise ValueError("Invalid version")
            return tuple(map(int, parts))
        if semver(latest) < semver(installed):
            return {"status": "NEWER_LOCAL"}
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
        return {"status": "UPDATED" if changes else "CURRENT", "version": latest,
                "files": len(changes), "upstream_sha": run("git", "rev-parse", "HEAD", cwd=upstream)}

if __name__ == "__main__":
    try:
        print(json.dumps(sync(pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve())))
    except Exception as e:
        print(json.dumps({"status": "BLOCKED", "reason": str(e)}), file=sys.stderr)
        sys.exit(2)
