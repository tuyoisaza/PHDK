"""Static regression checks for UAT scoped-browser readiness policy."""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class UATBrowserReadinessTests(unittest.TestCase):
    def load(self, path):
        return (ROOT / path).read_text(encoding="utf-8")

    def test_manifest_and_entrypoints(self):
        self.assertIn("UAT_BROWSER_READINESS_STANDARD.md | UAT_BROWSER_READINESS_STANDARD.md", self.load("PHDK_MANIFEST.txt"))
        for path in ("UAT_STANDARD.md", "UAT_JOURNEY_STANDARD.md", "PHDK_AUTO.md", "PHDK_LIFECYCLE.md", "EXECUTION_SCOPE.md", "PHDK_NATIVE_RULES.md", "AGENTS.md"):
            with self.subTest(path=path):
                self.assertIn("UAT_BROWSER_READINESS_STANDARD.md", self.load(path))

    def test_capability_separate_from_permission(self):
        p = self.load("UAT_BROWSER_READINESS_STANDARD.md")
        for x in ("Permission is not connectivity", "ACTIVE_UAT_EXCEPTION", "AVAILABLE_VERIFIED", "HOST_CONNECTION_REQUIRED", "UAT_ACCESS_REPORT.md"):
            self.assertIn(x, p)

    def test_no_unplanned_cost_or_fake_pass(self):
        p = self.load("UAT_BROWSER_READINESS_STANDARD.md")
        for x in ("budget ceiling", "approval for new spending", "BLOCKED", "never PASS", "continue"):
            self.assertIn(x, p)

    def test_release_version(self):
        self.assertEqual(self.load("VERSION").strip(), "2.51.6")
        self.assertIn("**Version v2.51.6**", self.load("README.md"))
        self.assertTrue(self.load("CHANGELOG.md").startswith("## v2.51.6"))


if __name__ == "__main__":
    unittest.main()
