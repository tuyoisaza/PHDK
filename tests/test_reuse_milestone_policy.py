import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parent.parent
SPEC = importlib.util.spec_from_file_location(
    "reuse_catalog_check", ROOT / "scripts" / "phdk_reuse_catalog_check.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class ReuseAndMilestonePolicyTests(unittest.TestCase):
    def test_canonical_catalog_is_valid_and_specification_only(self):
        catalog = json.loads(
            (ROOT / "PHDK_REUSE_CATALOG.json").read_text(encoding="utf-8")
        )
        self.assertEqual(MODULE.validate_catalog(catalog), [])
        self.assertTrue(catalog["entries"])
        for entry in catalog["entries"]:
            self.assertEqual(entry["status"], "SPECIFICATION_ONLY")
            self.assertIsNone(entry["implementation"])
            self.assertFalse(entry["downloadable"])

    def test_unvalidated_candidate_cannot_masquerade_as_accepted_reuse(self):
        candidate = {
            "schema_version": 1,
            "entries": [{
                "id": "example.candidate",
                "title": "Example candidate",
                "status": "ACCEPTED_VERSIONED",
                "specification": "synthetic",
                "capabilities": ["example"],
                "implementation": {
                    "package": "example",
                    "version": "1.0.0",
                    "source": "synthetic",
                },
                "downloadable": True,
                "dependencies": [],
                "compatibility": {
                    "runtimes": [],
                    "frameworks": [],
                    "contracts": [],
                },
                "security": {"status": "PENDING", "evidence": []},
                "license": {
                    "status": "PENDING",
                    "identifier": None,
                    "evidence": [],
                },
                "evidence": {
                    "tests_present": True,
                    "test_status": "UNKNOWN",
                    "portability_consumers": ["consumer-a"],
                    "notes": [],
                },
                "maintenance": {
                    "owner": "UNASSIGNED",
                    "policy": "synthetic",
                },
            }],
        }
        errors = MODULE.validate_catalog(candidate)
        self.assertTrue(any("observed passing tests" in error for error in errors))
        self.assertTrue(any("two portability consumers" in error for error in errors))
        self.assertTrue(any("license VERIFIED" in error for error in errors))

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
