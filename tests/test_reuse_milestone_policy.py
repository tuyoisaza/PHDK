"""Static contract fixtures only: no package, consumer or review is real."""

from copy import deepcopy
import importlib.util
import json
from pathlib import Path
import unittest

try:
    from jsonschema import Draft202012Validator
except ImportError:
    Draft202012Validator = None

ROOT = Path(__file__).resolve().parent.parent
SPEC = importlib.util.spec_from_file_location(
    "reuse_catalog_check", ROOT / "scripts" / "phdk_reuse_catalog_check.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)
SCHEMA = json.loads(
    (ROOT / "schemas" / "phdk-reuse-catalog.schema.json").read_text(encoding="utf-8")
)


def canonical_catalog():
    return json.loads((ROOT / "PHDK_REUSE_CATALOG.json").read_text(encoding="utf-8"))


def synthetic_catalog():
    """Structurally accepted fixture, never a canonical entry or real evidence."""
    entry = deepcopy(canonical_catalog()["entries"][0])
    reference = {"version": "1.0.0", "references": ["https://example.invalid/synthetic"]}
    entry.update({
        "id": "synthetic.validator-only",
        "title": "SYNTHETIC validator fixture, not a reusable package",
        "status": "ACCEPTED_VERSIONED",
        "implementation": {
            "package": "synthetic-not-published",
            "version": "1.0.0",
            "source": "https://example.invalid/not-a-package",
        },
        "downloadable": True,
        "security": {"status": "REVIEWED", "evidence": [deepcopy(reference)]},
        "license": {
            "status": "VERIFIED",
            "identifier": "Synthetic custom permission (not a real license)",
            "rights": "Synthetic permission record for validator tests only.",
            "evidence": [deepcopy(reference)],
        },
        "evidence": {
            "tests_present": True,
            "test_status": "PASS",
            "test_runs": [deepcopy(reference)],
            "portability_consumers": [
                {"consumer": "synthetic-a", **deepcopy(reference)},
                {"consumer": "synthetic-b", **deepcopy(reference)},
            ],
            "notes": ["Synthetic fixture; all claims and references are fictional."],
        },
        "maintenance": {
            "owner": "SYNTHETIC fixture maintainer",
            "policy": "No actual implementation or maintenance exists.",
        },
    })
    return {"schema_version": 1, "entries": [entry]}


def locate(data, path):
    for key in path:
        data = data[key]
    return data


def records(value, path=()):
    """All record paths, shared by missing-field and unknown-field fixtures."""
    if isinstance(value, dict):
        yield path, value
        for key, item in value.items():
            yield from records(item, path + (key,))
    elif isinstance(value, list):
        for index, item in enumerate(value):
            yield from records(item, path + (index,))


def shared_negative_fixtures():
    """Each generated case must fail both the schema and stdlib checker."""
    baseline = synthetic_catalog()
    for path, record in records(baseline):
        for key in record:
            changed = deepcopy(baseline)
            del locate(changed, path)[key]
            yield f"missing {path + (key,)}", changed
            changed = deepcopy(baseline)
            locate(changed, path)[key] = {"wrong": "type"}
            yield f"wrong type/shape {path + (key,)}", changed
        changed = deepcopy(baseline)
        locate(changed, path)["unexpected"] = True
        yield f"unknown field {path}", changed

    entry_path = ("entries", 0)
    replacements = [
        (("implementation", "version"), value)
        for value in (None, "", " \t", "\u00a0", "UNASSIGNED", " UNASSIGNED ", 42)
    ] + [
        (("maintenance", "owner"), value) for value in ("", " ", "UNASSIGNED", " UNASSIGNED ")
    ] + [
        (("license", "rights"), value) for value in (None, "", " ")
    ] + [
        (("license", "identifier"), None),
        (("maintenance", "policy"), " "),
        (("downloadable",), 1),
        (("evidence", "tests_present"), 1),
        (("evidence", "test_status"), "NOT_RUN"),
        (("evidence", "tests_present"), False),
        (("security", "status"), "PENDING"),
        (("license", "status"), "PENDING"),
        (("id",), "INVALID ID"),
        (("title",), " "),
        (("capabilities",), []),
        (("dependencies",), [42]),
        (("compatibility", "runtimes"), [""]),
        (("evidence", "notes"), [None]),
        (("evidence", "portability_consumers"), [
            baseline["entries"][0]["evidence"]["portability_consumers"][0]
        ]),
    ]
    evidence_paths = [
        ("security", "evidence"),
        ("license", "evidence"),
        ("evidence", "test_runs"),
        ("evidence", "portability_consumers"),
    ]
    for path in evidence_paths:
        replacements.extend([
            (path, []),
            (path, ["unversioned-reference"]),
            (path + (0, "references"), []),
            (path + (0, "references"), [" \t"]),
            (path + (0, "version"), None),
        ])
    for path, value in replacements:
        changed = deepcopy(baseline)
        locate(changed, entry_path + path[:-1])[path[-1]] = deepcopy(value)
        yield f"invalid {path} = {value!r}", changed
    changed = deepcopy(baseline)
    changed["schema_version"] = True
    yield "boolean schema version", changed
    changed = deepcopy(baseline)
    consumers = changed["entries"][0]["evidence"]["portability_consumers"]
    consumers[1] = deepcopy(consumers[0])
    yield "duplicate whole consumer record", changed
    changed = canonical_catalog()
    del changed["entries"][0]["implementation"]
    yield "missing implementation is not explicit null", changed


class ReuseAndMilestonePolicyTests(unittest.TestCase):
    def test_canonical_catalog_is_valid_and_specification_only(self):
        catalog = canonical_catalog()
        self.assertEqual(MODULE.validate_catalog(catalog), [])
        self.assertEqual(len(catalog["entries"]), 5)
        for entry in catalog["entries"]:
            self.assertEqual(entry["status"], "SPECIFICATION_ONLY")
            self.assertIsNone(entry["implementation"])
            self.assertFalse(entry["downloadable"])
            self.assertEqual(entry["evidence"]["test_status"], "NOT_RUN")

    def test_synthetic_complete_record_and_custom_license_shape(self):
        # A metadata pass does not make this fictional package reusable.
        self.assertEqual(MODULE.validate_catalog(synthetic_catalog()), [])

    def test_shared_negative_fixtures(self):
        for name, catalog in shared_negative_fixtures():
            with self.subTest(case=name):
                self.assertTrue(MODULE.validate_catalog(catalog))

    @unittest.skipUnless(Draft202012Validator, "jsonschema unavailable; schema parity NOT RUN")
    def test_schema_uses_the_same_structural_fixtures(self):
        Draft202012Validator.check_schema(SCHEMA)
        validator = Draft202012Validator(SCHEMA)
        self.assertTrue(validator.is_valid(canonical_catalog()))
        self.assertTrue(validator.is_valid(synthetic_catalog()))
        for name, catalog in shared_negative_fixtures():
            with self.subTest(case=name):
                self.assertFalse(validator.is_valid(catalog))

    def test_version_links_are_additional_semantic_checks(self):
        for path in (("security", "evidence"), ("license", "evidence"),
                     ("evidence", "test_runs"), ("evidence", "portability_consumers")):
            with self.subTest(path=path):
                catalog = synthetic_catalog()
                locate(catalog["entries"][0], path)[0]["version"] = "2.0.0"
                self.assertTrue(any("must equal implementation.version" in error
                                    for error in MODULE.validate_catalog(catalog)))

    def test_identity_uniqueness_is_an_additional_semantic_check(self):
        catalog = synthetic_catalog()
        consumers = catalog["entries"][0]["evidence"]["portability_consumers"]
        consumers[1]["consumer"] = consumers[0]["consumer"]
        consumers[1]["references"] = ["https://example.invalid/different-reference"]
        self.assertTrue(any("identities must be distinct" in error
                            for error in MODULE.validate_catalog(catalog)))
        catalog = synthetic_catalog()
        catalog["entries"].append(deepcopy(catalog["entries"][0]))
        self.assertTrue(any("duplicate id" in error
                            for error in MODULE.validate_catalog(catalog)))

    def test_status_containers_are_reported_without_crashing(self):
        for path in (("status",), ("security", "status"), ("license", "status"),
                     ("evidence", "test_status")):
            for value in ([], {}):
                catalog = synthetic_catalog()
                locate(catalog["entries"][0], path[:-1])[path[-1]] = value
                self.assertTrue(MODULE.validate_catalog(catalog))

    def test_planning_keeps_reuse_optional(self):
        standard = (ROOT / "PHDK_REUSE_CATALOG_STANDARD.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("REUSE", standard)
        self.assertIn("ADAPT", standard)
        self.assertIn("BUILD", standard)
        self.assertIn("Reuse is never mandatory", standard)

    def test_slice_is_not_milestone_publication_boundary(self):
        agile = (ROOT / "AGILE_SLICE_WORKFLOW.md").read_text(encoding="utf-8")
        pm = (ROOT / "PHDK_PROJECT_MANAGEMENT_STANDARD.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("A slice is not a milestone", agile)
        self.assertIn("milestone publication boundary", agile)
        self.assertIn("user capability", pm.lower())
        self.assertIn("next milestone", pm.lower())

    def test_delivery_evidence_distinguishes_states_and_mocks(self):
        delivery = (ROOT / "MAIN_DELIVERY_STANDARD.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("IMPLEMENTED", delivery)
        self.assertIn("PUBLISHED", delivery)
        self.assertIn("DEPLOYED", delivery)
        self.assertIn("ACCEPTED", delivery)
        self.assertIn("mock", delivery.lower())


if __name__ == "__main__":
    unittest.main()
