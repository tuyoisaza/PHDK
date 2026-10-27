#!/usr/bin/env python3
"""Validate PHDK_REUSE_CATALOG.json semantics using only the Python standard library."""

import argparse
import json
from pathlib import Path
import sys

STATUSES = {
    "SPECIFICATION_ONLY",
    "CANDIDATE",
    "REVIEWED",
    "ACCEPTED_VERSIONED",
    "DEPRECATED",
}


def nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def validate_catalog(data):
    errors = []
    if not isinstance(data, dict):
        return ["catalog must be an object"]
    if data.get("schema_version") != 1:
        errors.append("schema_version must be 1")
    entries = data.get("entries")
    if not isinstance(entries, list):
        return errors + ["entries must be a list"]

    seen = set()
    for index, entry in enumerate(entries):
        prefix = f"entries[{index}]"
        if not isinstance(entry, dict):
            errors.append(f"{prefix}: entry must be an object")
            continue
        entry_id = entry.get("id")
        if not nonempty(entry_id):
            errors.append(f"{prefix}: missing id")
            entry_id = prefix
        elif entry_id in seen:
            errors.append(f"{entry_id}: duplicate id")
        seen.add(entry_id)

        status = entry.get("status")
        if status not in STATUSES:
            errors.append(f"{entry_id}: invalid status {status!r}")
            continue

        if not nonempty(entry.get("title")):
            errors.append(f"{entry_id}: missing title")
        if not nonempty(entry.get("specification")):
            errors.append(f"{entry_id}: missing specification")
        capabilities = entry.get("capabilities")
        if not isinstance(capabilities, list) or not capabilities or not all(
            nonempty(item) for item in capabilities
        ):
            errors.append(f"{entry_id}: capabilities must be a nonempty string list")

        implementation = entry.get("implementation")
        downloadable = entry.get("downloadable")
        evidence = entry.get("evidence")
        security = entry.get("security")
        license_info = entry.get("license")
        maintenance = entry.get("maintenance")

        if status == "SPECIFICATION_ONLY":
            if implementation is not None:
                errors.append(f"{entry_id}: SPECIFICATION_ONLY requires implementation null")
            if downloadable is not False:
                errors.append(f"{entry_id}: SPECIFICATION_ONLY cannot be downloadable")
        elif status in {"CANDIDATE", "REVIEWED", "ACCEPTED_VERSIONED"}:
            if not isinstance(implementation, dict):
                errors.append(f"{entry_id}: {status} requires implementation metadata")
            if status != "ACCEPTED_VERSIONED" and downloadable is not False:
                errors.append(
                    f"{entry_id}: {status} must not be presented as accepted/downloadable"
                )

        if isinstance(implementation, dict):
            if not nonempty(implementation.get("package")):
                errors.append(f"{entry_id}: implementation missing package")
            if not nonempty(implementation.get("source")):
                errors.append(f"{entry_id}: implementation missing source")

        if not isinstance(evidence, dict):
            errors.append(f"{entry_id}: missing evidence")
            evidence = {}
        test_status = evidence.get("test_status")
        if test_status not in {"NOT_RUN", "PASS", "FAIL", "UNKNOWN"}:
            errors.append(f"{entry_id}: invalid test_status")
        portability = evidence.get("portability_consumers")
        if not isinstance(portability, list) or not all(nonempty(x) for x in portability):
            errors.append(f"{entry_id}: portability_consumers must be a string list")
            portability = []

        if status == "ACCEPTED_VERSIONED":
            version = (
                implementation.get("version") if isinstance(implementation, dict) else None
            )
            if not nonempty(version):
                errors.append(
                    f"{entry_id}: ACCEPTED_VERSIONED requires an implementation version"
                )
            if downloadable is not True:
                errors.append(
                    f"{entry_id}: ACCEPTED_VERSIONED must be marked downloadable"
                )
            if evidence.get("tests_present") is not True or test_status != "PASS":
                errors.append(
                    f"{entry_id}: ACCEPTED_VERSIONED requires observed passing tests"
                )
            if len(set(portability)) < 2:
                errors.append(
                    f"{entry_id}: ACCEPTED_VERSIONED requires two portability consumers"
                )
            if not isinstance(security, dict) or security.get("status") != "REVIEWED":
                errors.append(
                    f"{entry_id}: ACCEPTED_VERSIONED requires security REVIEWED"
                )
            if not isinstance(license_info, dict) or license_info.get("status") != "VERIFIED":
                errors.append(
                    f"{entry_id}: ACCEPTED_VERSIONED requires license VERIFIED"
                )
            if (
                not isinstance(maintenance, dict)
                or not nonempty(maintenance.get("owner"))
                or maintenance.get("owner") == "UNASSIGNED"
            ):
                errors.append(
                    f"{entry_id}: ACCEPTED_VERSIONED requires a maintenance owner"
                )
    return errors


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "catalog",
        nargs="?",
        default=str(
            Path(__file__).resolve().parent.parent / "PHDK_REUSE_CATALOG.json"
        ),
    )
    args = parser.parse_args()
    path = Path(args.catalog)
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    errors = validate_catalog(data)
    if errors:
        print("\n".join("FAIL: " + item for item in errors), file=sys.stderr)
        return 1
    print(f"PASS: {len(data['entries'])} reuse catalog entries (static semantics only)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
