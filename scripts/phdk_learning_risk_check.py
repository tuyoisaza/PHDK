#!/usr/bin/env python3
"""Read-only source checks for PHDK learning/risk contracts, never runtime proof."""
from __future__ import annotations

import argparse
from pathlib import Path
import re
import sys

CONTRACTS: dict[str, tuple[str, ...]] = {
    "PHDK_RETROSPECTIVE_STANDARD.md": (
        "Every Auto/Auto Force run", "before its normal version/PR delivery",
        "After the final publication attempt", "RETROSPECTIVE_PARTIAL",
        "NO_GENERALIZABLE_FINDINGS", "docs/decisions/phdk-process-review.vN.md",
        "PHDK_GAP", "PROJECT_SPECIFIC", "HOST_OR_PROVIDER_LIMIT",
        "MISINTERPRETATION", "EXISTING_SAFEGUARD", "PROPOSE_CANONICAL",
        "APPLY_LOCALLY_IF_AUTHORIZED", "ALREADY_SUPPORTED", "REJECT_WITH_REASON",
        "NEEDS_EVIDENCE", "negative scenario", "does not automatically open an issue/PR",
        "do not reopen a delivered milestone", "post-merge delivery artifact",
        "private source link", "UNKNOWN",
    ),
    "PHDK_CRITICAL_CHANGE_STANDARD.md": (
        "because of the risk", "NOT_APPLICABLE", "PHDK_PRODUCTION_VERIFICATION.md",
        "prohibition on local behavioral tests", "explicit-only UAT",
        "This release does not activate a local-test exception",
        "not automatically correct", "NOT RUN", "OWNER_APPROVED", "AGENT_PROPOSED",
        "UNRESOLVED", "Idempotent", "after cutover", "startup/release migration hooks",
        "TECHNICALLY_DELIVERED", "ACCEPTED", "CUTOVER_AUTHORIZED", "CUTOVER_EXECUTED",
        "NOT_AUTHORIZED", "do not replace mandatory machine-gate fields",
        "not automatic version pinning", "AUTO_STATE.json", "current coordinator",
    ),
}
ROUTES: dict[str, tuple[str, ...]] = {
    "PHDK_AUTO.md": tuple(CONTRACTS),
    "PHDK_PLAN.md": ("PHDK_CRITICAL_CHANGE_STANDARD.md",),
    "PHDK_COMPLETION_GATE.md": tuple(CONTRACTS),
    "PHDK_COHERENCE_STANDARD.md": (
        *CONTRACTS, "scripts/phdk_learning_risk_check.py",
    ),
    "README.md": tuple(CONTRACTS),
}
DISTRIBUTED = (*CONTRACTS, "scripts/phdk_learning_risk_check.py")


def read(root: Path, name: str, errors: list[str]) -> str:
    try:
        return (root / name).read_text(encoding="utf-8-sig")
    except (OSError, UnicodeError) as exc:
        errors.append(f"{name}: unreadable ({exc})")
        return ""


def inspect_sources(root: Path, contracts_only: bool = False) -> list[str]:
    """Check policy markers; never import or evaluate a project's source."""
    errors: list[str] = []
    for name, markers in CONTRACTS.items():
        source = read(root, name, errors).casefold()
        for marker in markers:
            if marker.casefold() not in source:
                errors.append(f"{name}: missing contract marker {marker!r}")
    if contracts_only:
        return errors
    for name, markers in ROUTES.items():
        source = read(root, name, errors)
        for marker in markers:
            if marker not in source:
                errors.append(f"{name}: missing routing marker {marker!r}")
    manifest = read(root, "PHDK_MANIFEST.txt", errors)
    sources: set[str] = set()
    destinations: set[str] = set()
    pairs: list[tuple[str, str]] = []
    for line_number, line in enumerate(manifest.splitlines(), 1):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = [part.strip() for part in line.split("|")]
        if len(parts) != 2 or not all(parts):
            errors.append(f"PHDK_MANIFEST.txt:{line_number}: malformed mapping")
            continue
        source, destination = parts
        for value in parts:
            if (value.startswith(("/", "\\")) or "\\" in value
                    or ":" in value or ".." in value.split("/")):
                errors.append(f"PHDK_MANIFEST.txt:{line_number}: unsafe path {value!r}")
        if source in sources or destination in destinations:
            errors.append(f"PHDK_MANIFEST.txt:{line_number}: duplicate mapping")
        sources.add(source)
        destinations.add(destination)
        pairs.append((source, destination))
    for name in DISTRIBUTED:
        if pairs.count((name, name)) != 1:
            errors.append(f"PHDK_MANIFEST.txt: require exactly one {name} mapping")
        if not (root / name).is_file():
            errors.append(f"{name}: distributable dependency missing")
    version = read(root, "VERSION", errors).strip()
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        errors.append("VERSION: expected a numeric MAJOR.MINOR.PATCH version")
    if f"**Version v{version}**" not in read(root, "README.md", errors):
        errors.append("README.md: version marker mismatch")
    changelog = read(root, "CHANGELOG.md", errors)
    release = re.search(r"^## v(\d+\.\d+\.\d+)\b", changelog, re.MULTILINE)
    if release is None or release.group(1) != version:
        errors.append("CHANGELOG.md: newest release mismatch")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--contracts-only", action="store_true",
                        help="Only check the two policy texts; excludes routing, manifest and release.")
    args = parser.parse_args()
    root = args.root.resolve()
    if not root.is_dir():
        parser.error(f"not a directory: {root}")
    errors = inspect_sources(root, args.contracts_only)
    scope = "CONTRACTS_ONLY (routing/manifest/release NOT CHECKED)" if args.contracts_only else "CONTRACTS_AND_ROUTING"
    print(f"SCOPE: {scope}")
    for error in errors:
        print(f"FAIL: {error}")
    print("SOURCE CHECK: FAIL" if errors else "SOURCE CHECK: PASS")
    print("No proof of runtime behavior, sandboxing, acceptance, cutover, publication or adoption.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
