"""Source-only optional Data Workspace contract guards; no product or runtime UAT."""
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
STANDARD = "PHDK_FLEXIBLE_DATA_WORKSPACE_STANDARD.md"


class FlexibleDataWorkspaceTests(unittest.TestCase):
    def test_spec_in_manifest_once_and_not_package(self):
        lines = (ROOT / "PHDK_MANIFEST.txt").read_text(encoding="utf-8").splitlines()
        mapping = f"{STANDARD} | {STANDARD}"
        self.assertEqual(lines.count(mapping), 1)
        data = json.loads((ROOT / "PHDK_REUSE_CATALOG.json").read_text(encoding="utf-8"))
        entries = [item for item in data["entries"]
                   if item["id"] == "starter.flexible-data-workspace"]
        self.assertEqual(len(entries), 1)
        entry = entries[0]
        self.assertEqual(entry["specification"], STANDARD)
        self.assertEqual(entry["status"], "SPECIFICATION_ONLY")
        self.assertIsNone(entry["implementation"])
        self.assertFalse(entry["downloadable"])
        self.assertEqual(entry["evidence"]["test_status"], "NOT_RUN")

    def test_no_silent_opt_in_or_schema_mutation(self):
        content = (ROOT / STANDARD).read_text(encoding="utf-8")
        for required in ("OWNER_ENABLED", "OWNER_DECLINED", "NOT_SELECTED_AUTO_FORCE",
                         "fields.manage", "tenant", "server", "custom fields",
                         "never automatically ALTER", "UAT NOT RUN",
                         "PHDK-Modules", "SPECIFICATION_ONLY"):
            with self.subTest(required=required):
                self.assertIn(required.lower(), content.lower())

    def test_reconciled_route(self):
        for name in ("README.md", "PHDK_PLAN.md", "PHDK_DESIGN.md",
                     "PHDK_UX_UI.md", "CRUD_STANDARD.md",
                     "TABULAR_DATA_EXCHANGE_STANDARD.md", "PHDK_CHECK.md",
                     "PHDK_REUSE_CATALOG_STANDARD.md", "PHDK_COHERENCE_STANDARD.md",
                     "AGENTS.md", "SKILL.md", "PHDK_NATIVE_RULES.md"):
            with self.subTest(name=name):
                self.assertIn(STANDARD, (ROOT / name).read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
