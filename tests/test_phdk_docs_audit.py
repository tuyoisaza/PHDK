"""Source regression scenarios for the PHDK documentation audit.

PHDK production-first policy disallows local behavioral test execution in
ordinary Auto. Retain these as test source for an explicitly permitted runner.
"""
import importlib.util
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "phdk_docs_audit.py"
SPEC = importlib.util.spec_from_file_location("phdk_docs_audit", SCRIPT)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class DocumentationAuditTest(unittest.TestCase):
    def setUp(self):
        self.folder = tempfile.TemporaryDirectory()
        self.addCleanup(self.folder.cleanup)
        self.root = Path(self.folder.name)

    def add(self, path, doc_id, version, status="draft", authority="owner-request"):
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(
            f"---\ndoc_id: {doc_id}\nversion: {version}\nstatus: {status}\n"
            f"created_at: 2026-10-28\nupdated_at: 2026-10-28\n"
            f"authority: {authority}\n---\n\n# Test\n",
            encoding="utf-8",
        )
        return target

    def test_valid_active_and_newer_draft(self):
        self.add("docs/intents/project-intent.v1.md", "project-intent", "v1", "active")
        self.add("docs/intents/project-intent.v2.md", "project-intent", "v2", "draft")
        errors, _, docs = MODULE.audit(self.root, set())
        self.assertEqual(errors, [])
        index = MODULE.make_index(docs)
        self.assertIn("[v1](intents/project-intent.v1.md)", index)
        self.assertIn("[v2](intents/project-intent.v2.md)", index)

    def test_duplicate_active_is_error(self):
        self.add("docs/plans/technical-plan.v1.md", "technical-plan", "v1", "active")
        self.add("docs/plans/technical-plan.v2.md", "technical-plan", "v2", "active")
        errors, _, _ = MODULE.audit(self.root, set())
        self.assertTrue(any("multiple active" in x for x in errors))

    def test_changed_unversioned_fails_untouched_legacy_warns(self):
        path = "docs/intents/legacy-intent.md"
        p = self.root / path
        p.parent.mkdir(parents=True)
        p.write_text("legacy\n", encoding="utf-8")
        errors, warnings, _ = MODULE.audit(self.root, set())
        self.assertFalse(errors)
        self.assertTrue(warnings)
        errors, _, _ = MODULE.audit(self.root, {path})
        self.assertTrue(any("kebab-case.vN.md" in x for x in errors))

    def test_wrong_version_and_authority(self):
        self.add("docs/briefs/project-brief.v1.md", "project-brief", "v2",
                 "active", "owner-not-proven")
        errors, _, _ = MODULE.audit(self.root, set())
        self.assertTrue(any("version mismatch" in x for x in errors))
        self.assertTrue(any("invalid authority" in x for x in errors))

    def test_changed_design_asset_requires_version_subfolder(self):
        p = self.root / "docs/images/login/screen.png"
        p.parent.mkdir(parents=True)
        p.write_bytes(b"fake")
        errors, _, _ = MODULE.audit(self.root, {"docs/images/login/screen.png"})
        self.assertTrue(any("design asset" in x for x in errors))


if __name__ == "__main__":
    unittest.main()
