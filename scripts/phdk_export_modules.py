#!/usr/bin/env python3
"""Offline, read-only PHDK reusable module discovery. No publishing or code export.

Inspects bounded source directory metadata and an optional catalog. It does not
read application source, access networks, run tests, or promote catalog entries.
"""

import argparse
import json
from pathlib import Path
import re
import subprocess
import sys

SCHEMA_VERSION = 1
SEARCH_PARENTS = (
    "packages", "modules", "components", "lib", "src/modules", "src/features",
    "src/components", "src/lib", "src/utils", "src/hooks", "src/services",
)
EXCLUDED = {
    "node_modules", ".git", ".github", "phdk-standards", "dist", "build",
    "coverage", "vendor", "__pycache__", "data", "uploads", "fixtures",
    "secrets", "private", "credentials", "generated", ".next", ".venv",
}
STOPWORDS = {"starter", "module", "modules", "system", "feature", "features", "service", "services", "component", "components", "common", "shared", "framework", "implementation"}
MAX_CANDIDATES = 80


def tokens(text):
    return {t.removesuffix("s") for t in re.findall(r"[a-z0-9]+", text.lower()) if len(t) > 2 and t not in STOPWORDS}


def safe_directory(path, root):
    """No symlink traversal or cross-root inventory."""
    try:
        relative = path.relative_to(root)
        if not relative.parts or any(part.startswith(".") or part.lower() in EXCLUDED for part in relative.parts):
            return False
        return path.is_dir() and not path.is_symlink() and path.resolve().is_relative_to(root.resolve())
    except (ValueError, OSError):
        return False


def catalog_at(root, supplied):
    if supplied:
        return supplied
    for path in (root / "phdk-standards/PHDK_REUSE_CATALOG.json", root / "PHDK_REUSE_CATALOG.json"):
        if path.is_file():
            return path
    return None


def load_catalog(path):
    if path is None:
        return None
    if path.stat().st_size > 2_000_000:
        raise ValueError("catalog size exceeds bounded inventory limit")
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or not isinstance(data.get("entries"), list):
        raise ValueError("catalog must contain an entries list")
    return [e for e in data["entries"] if isinstance(e, dict) and isinstance(e.get("id"), str)]


def metadata(directory):
    marker = directory / "phdk-module.json"
    if not marker.is_file() or marker.is_symlink():
        return {}, "NOT_DECLARED"
    try:
        if marker.stat().st_size > 16_384:
            return {}, "INVALID_METADATA"
        value = json.loads(marker.read_text(encoding="utf-8"))
        if not isinstance(value, dict) or value.get("schema_version") != 1:
            return {}, "INVALID_METADATA"
        allowed = {"schema_version", "catalog_id", "upstream_commit", "upstream_head_commit", "upstream_version"}
        if set(value) - allowed:
            return {}, "INVALID_METADATA"
        for key in allowed - {"schema_version"}:
            if key in value and (not isinstance(value[key], str) or not value[key].strip()):
                return {}, "INVALID_METADATA"
        for key in ("upstream_commit", "upstream_head_commit"):
            if key in value and not re.fullmatch(r"[a-fA-F0-9]{40}", value[key]):
                return {}, "INVALID_METADATA"
        return value, "DECLARED"
    except (OSError, ValueError, UnicodeError):
        return {}, "INVALID_METADATA"


def changed_paths(root, revision, folder, target=None):
    """Read-only tracked-file diff; excludes module provenance record itself."""
    try:
        check = subprocess.run(
            ["git", "-C", str(root), "cat-file", "-t", revision],
            capture_output=True, text=True, timeout=4, check=False,
        )
        if check.returncode or check.stdout.strip() != "commit":
            return None
        rel = folder.relative_to(root).as_posix()
        command = ["git", "-C", str(root), "diff", "--no-ext-diff", "--name-only", revision]
        if target:
            command.append(target)
        command += ["--", rel, f":(exclude){rel}/phdk-module.json"]
        result = subprocess.run(command, capture_output=True, text=True, timeout=5, check=False)
        return set(result.stdout.splitlines()) if result.returncode == 0 else None
    except (OSError, subprocess.TimeoutExpired):
        return None


def local_comparison(root, folder, baseline, upstream_head):
    if not baseline:
        return "NOT_DECLARED", None, "NOT_DECLARED", None, None
    local = changed_paths(root, baseline, folder)
    if local is None:
        return "BASELINE_UNAVAILABLE", None, "UNVERIFIED", None, None
    local_state = "LOCAL_CHANGES_DETECTED" if local else "NO_TRACKED_CHANGES"
    if not upstream_head:
        return local_state, len(local), "UPSTREAM_HEAD_NOT_DECLARED", None, None
    upstream = changed_paths(root, baseline, folder, upstream_head)
    if upstream is None:
        return local_state, len(local), "UPSTREAM_HEAD_UNAVAILABLE", None, None
    try:
        ancestor = subprocess.run(
            ["git", "-C", str(root), "merge-base", "--is-ancestor", baseline, upstream_head],
            timeout=4, check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
        ).returncode == 0
    except (OSError, subprocess.TimeoutExpired):
        ancestor = False
    if not ancestor:
        return local_state, len(local), "UPSTREAM_ANCESTRY_UNVERIFIED", None, None
    return local_state, len(local), "THREE_WAY_PATH_COMPARISON", len(upstream), len(local & upstream)


def match_catalog(name, declared_id, entries):
    if entries is None:
        return None, "CATALOG_UNAVAILABLE"
    exact = next((e for e in entries if e["id"] == declared_id), None) if declared_id else None
    if exact:
        return exact, "DECLARED_EXACT"
    if declared_id:
        return None, "DECLARED_ID_NOT_FOUND"
    terms = tokens(name)
    matches = []
    for e in entries:
        searchable = " ".join([str(e.get("title", "")), e["id"], *[str(x) for x in e.get("capabilities", [])]])
        common = len(terms & tokens(searchable))
        if common and common == len(terms) and len(terms) >= 1:
            matches.append((common, e["id"], e))
    if matches:
        matches.sort(key=lambda m: (-m[0], m[1]))
        return matches[0][2], "POSSIBLE_NAME_OVERLAP"
    return None, "NO_OVERLAP_FOUND"


def candidate(root, directory, catalog):
    names = {p.name for p in directory.iterdir() if not p.is_symlink() and p.is_file()}
    manifest = any(n in names for n in ("package.json", "pyproject.toml", "Cargo.toml", "go.mod"))
    docs = any(n.lower().startswith("readme") for n in names)
    test_names = {"tests", "test", "__tests__", "spec"}
    tests = any(p.name.lower() in test_names and p.is_dir() and not p.is_symlink() for p in directory.iterdir()) or any(
        n.endswith((".test.ts", ".test.js", ".spec.ts", "_test.py", ".test.tsx")) for n in names
    )
    info, marker_status = metadata(directory)
    if not (manifest or docs or tests or marker_status != "NOT_DECLARED"):
        return None
    upstream = info.get("upstream_commit")
    diff_status, diff_count, three_way, upstream_count, overlap_count = local_comparison(
        root, directory, upstream, info.get("upstream_head_commit")
    )
    entry, match_kind = match_catalog(directory.name, info.get("catalog_id"), catalog)
    if entry and match_kind == "DECLARED_EXACT":
        kind = "POTENTIAL_EXTENSION" if entry.get("implementation") else "SPECIFICATION_IMPLEMENTATION"
    elif entry:
        kind = "POSSIBLE_OVERLAP"
    elif match_kind == "DECLARED_ID_NOT_FOUND":
        kind = "UNVERIFIED_CATALOG_REFERENCE"
    else:
        kind = "NEW_CANDIDATE" if catalog is not None else "UNCLASSIFIED"
    catalog_version = entry.get("implementation", {}).get("version") if entry and isinstance(entry.get("implementation"), dict) else None
    installed_version = info.get("upstream_version")
    version_alignment = ("MATCH" if catalog_version == installed_version else "POSSIBLE_VERSION_DRIFT") if catalog_version and installed_version else "UNVERIFIED"
    score = int(manifest) * 3 + int(docs) * 2 + int(tests) * 2 + int(marker_status == "DECLARED") * 2
    priority = "HIGH" if score >= 7 else "MEDIUM" if score >= 4 else "LOW"
    return {
        "id": directory.relative_to(root).as_posix(),
        "category": kind,
        "priority": priority,
        "catalog_match": entry["id"] if entry else None,
        "match_evidence": match_kind,
        "catalog_status": entry.get("status") if entry else None,
        "installed_upstream_version": installed_version,
        "catalog_implementation_version": catalog_version,
        "version_alignment": version_alignment,
        "signals": {"package_manifest": manifest, "readme": docs, "tests_present": tests, "provenance": marker_status},
        "baseline_comparison": diff_status,
        "changed_files_count": diff_count,
        "upstream_comparison": three_way,
        "upstream_changed_files_count": upstream_count,
        "changed_path_overlap_count": overlap_count,
        "gates": ["OWNER_SELECTION", "RIGHTS_AND_LICENSE", "SECRETS_AND_DATA_REVIEW", "CONTRACT_AND_PORTABILITY", "OBSERVED_TESTS", "TARGET_REPOSITORY_APPROVAL"],
        "test_result": "NOT_RUN",
        "contribution_state": "PROPOSAL_ONLY",
    }


def discover(root, entries):
    found = []
    seen = set()
    for parent_name in SEARCH_PARENTS:
        parent = root / parent_name
        if not safe_directory(parent, root):
            continue
        for directory in sorted(parent.iterdir(), key=lambda p: p.name.lower()):
            if len(found) >= MAX_CANDIDATES:
                break
            if not safe_directory(directory, root):
                continue
            rel = directory.relative_to(root).as_posix()
            if rel in seen:
                continue
            seen.add(rel)
            record = candidate(root, directory, entries)
            if record:
                found.append(record)
    found.sort(key=lambda x: ({"HIGH": 0, "MEDIUM": 1, "LOW": 2}[x["priority"]], x["id"]))
    return found


def report(root, entries):
    items = discover(root, entries)
    return {
        "schema_version": SCHEMA_VERSION,
        "mode": "READ_ONLY_LOCAL_INVENTORY",
        "scope": "CURRENT_REPOSITORY_ONLY",
        "catalog_status": "AVAILABLE" if entries is not None else "UNAVAILABLE",
        "publication": "NOT_AUTHORIZED_BY_SCAN",
        "limitations": ["STATIC_METADATA_ONLY", "NO_SOURCE_REVIEW", "NO_RUNTIME_TESTS", "NO_LICENSE_OR_SECURITY_VERIFICATION", "NO_UPSTREAM_NETWORK_FETCH", "UNTRACKED_CHANGES_NOT_COMPARED", "THREE_WAY_IS_PATH_LEVEL_NOT_SEMANTIC"],
        "count": len(items),
        "candidates": items,
    }


def markdown(data):
    lines = ["# PHDK Export Modules — local proposal", "", "**Status:** analysis only; nothing exported or published.",
             f"**Candidates:** {data['count']} | **Catalog:** {data['catalog_status']}", "",
             "| Local candidate | Classification | Priority | Catalog | Baseline |", "|---|---|---|---|---|"]
    for entry in data["candidates"]:
        # Only local, bounded folder identifiers appear; never file contents.
        cols = [entry["id"], entry["category"], entry["priority"], entry["catalog_match"] or "—", entry["baseline_comparison"]]
        lines.append("| " + " | ".join(c.replace("|", "\\|").replace("`", "") for c in cols) + " |")
    lines += ["", "Review each candidate's code, actual diff, ownership, licenses, secrets, test evidence and portability before requesting an explicit publication decision.",
              "A changed module is not automatically a better module. One donor is never ACCEPTED_VERSIONED evidence."]
    return "\n".join(lines) + "\n"


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="currently authorized donor repository")
    parser.add_argument("--catalog", type=Path, default=None, help="optional local PHDK reuse catalog")
    parser.add_argument("--json", action="store_true", help="machine-readable private local report")
    args = parser.parse_args(argv)
    root = args.root.resolve()
    if not root.is_dir():
        parser.error("--root must be an existing directory")
    try:
        entries = load_catalog(catalog_at(root, args.catalog))
        result = report(root, entries)
    except (OSError, ValueError, UnicodeError) as exc:
        print(f"PHDK export modules: invalid catalog or source ({type(exc).__name__})", file=sys.stderr)
        return 2
    print(json.dumps(result, indent=2, ensure_ascii=False) if args.json else markdown(result), end="\n" if args.json else "")
    return 0


if __name__ == "__main__":
    sys.exit(main())
