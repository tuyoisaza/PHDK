"""Policy regression tests for standalone/Auto PHDK UAT Prep."""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def read(path):
    return (ROOT / path).read_text(encoding="utf-8")

class UatPrepPolicyTests(unittest.TestCase):
    def test_command_is_vendored_and_routed(self):
        self.assertIn("PHDK_UAT_PREP.md | PHDK_UAT_PREP.md", read("PHDK_MANIFEST.txt"))
        for path in ("SKILL.md", "AGENTS.md", "PHDK_NATIVE_RULES.md", "EXECUTION_SCOPE.md"):
            with self.subTest(path=path):
                self.assertIn("phdk uat prep", read(path).lower())

    def test_auto_and_handoff_order(self):
        auto = read("PHDK_AUTO.md")
        self.assertLess(auto.index("### 5. UAT Prep"), auto.index("### 6. UAT and repair"))
        self.assertIn("UAT Prep ............. PENDING", auto)
        self.assertIn("UAT Prep ............. COMPLETED / REUSED / BLOCKED", auto)
        lifecycle = read("PHDK_LIFECYCLE.md")
        self.assertIn("45-uat-prep/", lifecycle)
        self.assertLess(lifecycle.index("## 45 — UAT Prep"), lifecycle.index("## 50 — UAT"))

    def test_required_artifacts_and_no_browser_in_prep(self):
        prep = read("PHDK_UAT_PREP.md")
        for artifact in ("UAT_AUTH_PLAN.md", "UAT_ROLE_MATRIX.md", "UAT_FIXTURE_MANIFEST.md", "UAT_PREP_REPORT.md"):
            with self.subTest(artifact=artifact):
                self.assertIn(artifact, prep)
        self.assertIn("idempotent", prep)
        self.assertIn("non-production", prep)
        self.assertIn("must not", prep.lower())
        self.assertIn("browser", prep.lower())
        self.assertIn("UAT_BROWSER_READINESS_STANDARD.md", prep)
        self.assertIn("UAT_PREP_REPORT.md", read("UAT_STANDARD.md"))
        self.assertIn("PHDK_UAT_PREP.md", read("PHDK_CHECK.md"))

    def test_phase_preserves_browser_exception(self):
        scope = read("EXECUTION_SCOPE.md")
        self.assertIn("## PHDK UAT Prep — source development only", scope)
        self.assertIn("## Scoped browser exception for UAT and UAT Fix", scope)
        self.assertNotIn("UAT Prep phases of an authorized", scope)
        browser = read("UAT_BROWSER_READINESS_STANDARD.md")
        self.assertIn("only inside those UAT phases", browser)

if __name__ == "__main__":
    unittest.main()
