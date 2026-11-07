#!/usr/bin/env python3
"""Bounded read-only discovery of already-installed security/package tools.

No installs, subprocess invocations, package imports, network traffic or PATH edits.
A found executable path is not proof of its version, safety or successful audit.
"""
import argparse
import json
import os
import shutil
from pathlib import Path

TOOLS = ("uv", "pip-audit", "osv-scanner", "node", "npm", "pnpm", "poetry")


def discover(name, project=None, env=None, windows=None):
    if name not in TOOLS:
        raise ValueError("unsupported tool")
    env = os.environ if env is None else env
    windows = os.name == "nt" if windows is None else windows
    suffix = ".exe" if windows else ""
    home = Path(env.get("USERPROFILE" if windows else "HOME", "~")).expanduser()
    local = Path(env.get("LOCALAPPDATA", str(home / "AppData" / "Local")))
    roaming = Path(env.get("APPDATA", str(home / "AppData" / "Roaming")))
    locations = []
    if project:
        root = Path(project).resolve()
        locations += [root / ".venv" / ("Scripts" if windows else "bin")]
    locations += [home / ".local" / "bin", home / ".cargo" / "bin", home / ".rye" / "shims"]
    if windows:
        locations += [
            local / "Microsoft" / "WinGet" / "Links",
            local / "Programs" / "uv",
            roaming / "Python" / "Scripts",
            home / "scoop" / "shims",
        ]
        python_root = local / "Programs" / "Python"
        # One known installation directory; bounded discovery, never recursive.
        if python_root.is_dir():
            locations += [p / "Scripts" for p in list(sorted(python_root.glob("Python*")))[:12]]
    found = []
    path_hit = shutil.which(name + suffix, path=env.get("PATH", ""))
    if path_hit:
        found.append({"path": str(Path(path_hit).resolve()), "source": "PATH"})
    for folder in locations:
        candidate = folder / (name + suffix)
        if candidate.is_file() and not any(x["path"] == str(candidate.resolve()) for x in found):
            found.append({"path": str(candidate.resolve()), "source": "KNOWN_LOCATION"})
    return {
        "tool": name,
        "status": "FOUND_PATH" if found else "NOT_LOCATED_IN_BOUNDED_SEARCH",
        "candidates": found,
        "executed": False,
        "installed_or_usable": "UNVERIFIED",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", default=".")
    parser.add_argument("--tool", choices=TOOLS, action="append")
    args = parser.parse_args()
    results = [discover(name, args.project) for name in (args.tool or list(TOOLS))]
    print(json.dumps({"results": results, "changed_environment": False,
                      "advisory_coverage": "NOT_ASSESSED"}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
