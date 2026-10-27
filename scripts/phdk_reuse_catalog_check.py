#!/usr/bin/env python3
"""Check the catalog's explicit contract; no downloads or evidence execution.

The JSON Schema covers structure. This stdlib checker mirrors it and adds
cross-record version equality and unique entry/consumer identities. Neither
validator proves that a reference is genuine, safe or independently reviewed.
"""

import argparse
import json
from pathlib import Path
import re
import sys

STATUSES = (
    "SPECIFICATION_ONLY", "CANDIDATE", "REVIEWED",
    "ACCEPTED_VERSIONED", "DEPRECATED",
)
ENTRY_FIELDS = (
    "id", "title", "status", "specification", "capabilities", "implementation",
    "downloadable", "dependencies", "compatibility", "security", "license",
    "evidence", "maintenance",
)


def nonempty(value):
    # Mirror the nonblank text constraint in $defs/text.
    return isinstance(value, str) and re.search(r"\S", value) is not None


def resolved(value):
    return nonempty(value) and value.strip() != "UNASSIGNED"


def expect(condition, path, message, errors):
    if not condition:
        errors.append(f"{path}: {message}")
    return condition


def fields(value, required, path, errors):
    """Validate one known record's keys, not arbitrary JSON Schema."""
    if not expect(isinstance(value, dict), path, "must be an object", errors):
        return False
    missing = set(required) - value.keys()
    extra = value.keys() - set(required)
    if missing:
        errors.append(f"{path}: missing fields {', '.join(sorted(missing))}")
    if extra:
        errors.append(f"{path}: unknown fields {', '.join(sorted(extra))}")
    return not missing and not extra


def string_list(value, path, errors, minimum=0):
    if not expect(isinstance(value, list), path, "must be an array", errors):
        return
    expect(len(value) >= minimum, path, f"requires at least {minimum} items", errors)
    for index, item in enumerate(value):
        expect(nonempty(item), f"{path}[{index}]", "must be nonblank text", errors)


def evidence_records(value, path, errors, consumers=False):
    if not expect(isinstance(value, list), path, "must be an array", errors):
        return
    required = ("consumer", "version", "references") if consumers else (
        "version", "references"
    )
    for index, record in enumerate(value):
        location = f"{path}[{index}]"
        if not fields(record, required, location, errors):
            continue
        expect(resolved(record["version"]), location + ".version",
               "must be a nonblank assigned version", errors)
        string_list(record["references"], location + ".references", errors, 1)
        if consumers:
            expect(nonempty(record["consumer"]), location + ".consumer",
                   "must be nonblank text", errors)
    if consumers:
        # JSON Schema uniqueItems; identity uniqueness is checked separately.
        expect(all(record not in value[:index] for index, record in enumerate(value)),
               path, "duplicate consumer records", errors)


def validate_entry_shape(entry, path):
    errors = []
    if not fields(entry, ENTRY_FIELDS, path, errors):
        return errors
    expect(isinstance(entry["id"], str)
           and re.search(r"^[a-z0-9][a-z0-9._-]+$", entry["id"]) is not None,
           path + ".id", "must match the catalog id pattern", errors)
    for key in ("title", "specification"):
        expect(nonempty(entry[key]), path + "." + key, "must be nonblank text", errors)
    expect(entry["status"] in STATUSES, path + ".status", "invalid status", errors)
    expect(type(entry["downloadable"]) is bool, path + ".downloadable",
           "must be boolean", errors)
    string_list(entry["capabilities"], path + ".capabilities", errors, 1)
    string_list(entry["dependencies"], path + ".dependencies", errors)

    implementation = entry["implementation"]
    if implementation is not None and fields(
        implementation, ("package", "version", "source"), path + ".implementation", errors
    ):
        for key in ("package", "source"):
            expect(nonempty(implementation[key]), path + ".implementation." + key,
                   "must be nonblank text", errors)
        expect(implementation["version"] is None or nonempty(implementation["version"]),
               path + ".implementation.version", "must be null or nonblank text", errors)

    compatibility = entry["compatibility"]
    if fields(compatibility, ("runtimes", "frameworks", "contracts"),
              path + ".compatibility", errors):
        for key in ("runtimes", "frameworks", "contracts"):
            string_list(compatibility[key], path + ".compatibility." + key, errors)
    security = entry["security"]
    if fields(security, ("status", "evidence"), path + ".security", errors):
        expect(security["status"] in ("SPECIFICATION_ONLY", "PENDING", "REVIEWED", "FAILED"),
               path + ".security.status", "invalid status", errors)
        evidence_records(security["evidence"], path + ".security.evidence", errors)
    license_info = entry["license"]
    if fields(license_info, ("status", "identifier", "rights", "evidence"),
              path + ".license", errors):
        expect(license_info["status"] in ("NOT_APPLICABLE", "PENDING", "VERIFIED", "REJECTED"),
               path + ".license.status", "invalid status", errors)
        for key in ("identifier", "rights"):
            expect(license_info[key] is None or nonempty(license_info[key]),
                   path + ".license." + key, "must be null or nonblank text", errors)
        evidence_records(license_info["evidence"], path + ".license.evidence", errors)
    evidence = entry["evidence"]
    if fields(evidence, ("tests_present", "test_status", "test_runs",
                         "portability_consumers", "notes"), path + ".evidence", errors):
        expect(type(evidence["tests_present"]) is bool, path + ".evidence.tests_present",
               "must be boolean", errors)
        expect(evidence["test_status"] in ("NOT_RUN", "PASS", "FAIL", "UNKNOWN"),
               path + ".evidence.test_status", "invalid status", errors)
        evidence_records(evidence["test_runs"], path + ".evidence.test_runs", errors)
        evidence_records(evidence["portability_consumers"],
                         path + ".evidence.portability_consumers", errors, consumers=True)
        string_list(evidence["notes"], path + ".evidence.notes", errors)
    maintenance = entry["maintenance"]
    if fields(maintenance, ("owner", "policy"), path + ".maintenance", errors):
        for key in ("owner", "policy"):
            expect(nonempty(maintenance[key]), path + ".maintenance." + key,
                   "must be nonblank text", errors)
    return errors


def validate_entry_semantics(entry, path):
    """Called only after every required record, field and type is valid."""
    errors = []
    status = entry["status"]
    implementation = entry["implementation"]
    evidence = entry["evidence"]
    security = entry["security"]
    license_info = entry["license"]
    if status == "SPECIFICATION_ONLY":
        expect(implementation is None, path, "SPECIFICATION_ONLY requires implementation null", errors)
        expect(entry["downloadable"] is False, path, "SPECIFICATION_ONLY cannot be downloadable", errors)
    elif status in ("CANDIDATE", "REVIEWED", "ACCEPTED_VERSIONED"):
        expect(implementation is not None, path, f"{status} requires implementation metadata", errors)
        if status != "ACCEPTED_VERSIONED":
            expect(entry["downloadable"] is False, path, f"{status} cannot be downloadable", errors)

    version = implementation["version"] if implementation is not None else None
    groups = (
        ("security.evidence", security["evidence"]),
        ("license.evidence", license_info["evidence"]),
        ("evidence.test_runs", evidence["test_runs"]),
        ("evidence.portability_consumers", evidence["portability_consumers"]),
    )
    for name, records in groups:
        for index, record in enumerate(records):
            expect(record["version"] == version, f"{path}.{name}[{index}].version",
                   "must equal implementation.version", errors)
    consumers = [record["consumer"] for record in evidence["portability_consumers"]]
    expect(len(consumers) == len(set(consumers)), path + ".evidence.portability_consumers",
           "consumer identities must be distinct", errors)

    if status == "ACCEPTED_VERSIONED":
        expect(resolved(version), path, "ACCEPTED_VERSIONED requires an assigned implementation version", errors)
        expect(entry["downloadable"] is True, path, "ACCEPTED_VERSIONED must be downloadable", errors)
        expect(evidence["tests_present"] is True and evidence["test_status"] == "PASS",
               path, "ACCEPTED_VERSIONED requires observed passing tests", errors)
        expect(len(consumers) >= 2, path, "ACCEPTED_VERSIONED requires two portability consumers", errors)
        expect(security["status"] == "REVIEWED", path, "ACCEPTED_VERSIONED requires security REVIEWED", errors)
        expect(license_info["status"] == "VERIFIED", path, "ACCEPTED_VERSIONED requires license VERIFIED", errors)
        for key in ("identifier", "rights"):
            expect(nonempty(license_info[key]), path + ".license." + key,
                   "ACCEPTED_VERSIONED requires documented license and redistribution rights", errors)
        expect(resolved(entry["maintenance"]["owner"]), path,
               "ACCEPTED_VERSIONED requires an assigned maintenance owner", errors)
        for name, records in groups:
            expect(bool(records), path + "." + name,
                   "ACCEPTED_VERSIONED requires version-linked evidence references", errors)
    return errors


def validate_catalog(data):
    errors = []
    if not fields(data, ("schema_version", "entries"), "catalog", errors):
        return errors
    # bool is an int subclass in Python, but not a JSON Schema integer.
    expect(type(data["schema_version"]) in (int, float) and data["schema_version"] == 1,
           "schema_version", "must be integer 1", errors)
    if not expect(isinstance(data["entries"], list), "entries", "must be an array", errors):
        return errors
    seen = set()
    for index, entry in enumerate(data["entries"]):
        path = f"entries[{index}]"
        shape_errors = validate_entry_shape(entry, path)
        errors.extend(shape_errors)
        if shape_errors:
            continue
        expect(entry["id"] not in seen, path + ".id", "duplicate id", errors)
        seen.add(entry["id"])
        errors.extend(validate_entry_semantics(entry, path))
    return errors


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "catalog", nargs="?",
        default=str(Path(__file__).resolve().parent.parent / "PHDK_REUSE_CATALOG.json"),
    )
    args = parser.parse_args()
    try:
        data = json.loads(Path(args.catalog).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    errors = validate_catalog(data)
    if errors:
        print("\n".join("FAIL: " + item for item in errors), file=sys.stderr)
        return 1
    print(f"PASS: {len(data['entries'])} reuse catalog entries (static metadata only)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
