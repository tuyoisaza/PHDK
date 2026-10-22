"""Policy regression source for explicit-only PHDK UAT preparation."""
import re
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

    def test_auto_defers_acceptance_and_preserves_explicit_handoff_order(self):
        auto = read("PHDK_AUTO.md")
        rows = re.findall(r"^\s*(UAT Prep|UAT Fix|UAT)\s*\.{2,}\s*(.*?)\s*$", auto, re.M)
        self.assertEqual({stage for stage, _ in rows}, {"UAT Prep", "UAT", "UAT Fix"})
        for stage, status in rows:
            with self.subTest(stage=stage, status=status):
                self.assertEqual(status, "DEFERRED — OWNER OPT-IN")
        self.assertIn("UAT NOT RUN", auto)
        self.assertNotIn("### 5. UAT Prep", auto)
        self.assertNotIn("### 6. UAT and repair", auto)
        lifecycle = read("PHDK_LIFECYCLE.md")
        self.assertIn("45-uat-prep/", lifecycle)
        self.assertLess(lifecycle.index("## 45 — UAT Prep"), lifecycle.index("## 50 — UAT"))

    def test_installed_managed_rules_keep_explicit_authorization(self):
        native = read("PHDK_NATIVE_RULES.md")
        managed = native.split("<!-- PHDK-MANAGED:START -->", 1)[1].split("<!-- PHDK-MANAGED:END -->", 1)[0]
        for marker in ("PHDK auto force", "PHDK uat", "PHDK uat prep", "PHDK uat fix",
                       "DEFERRED — OWNER OPT-IN", "UAT NOT RUN"):
            with self.subTest(marker=marker):
                self.assertIn(marker, managed)
        self.assertNotIn("In Auto it is stage 45", managed)

    def test_required_artifacts_and_no_browser_in_prep(self):
        prep = read("PHDK_UAT_PREP.md")
        for artifact in ("UAT_AUTH_PLAN.md", "UAT_ROLE_MATRIX.md", "UAT_FIXTURE_MANIFEST.md", "UAT_PREP_REPORT.md"):
            with self.subTest(artifact=artifact):
                self.assertIn(artifact, prep)
        self.assertIn("idempotent", prep)
        self.assertIn("PHDK_PRODUCTION_VERIFICATION.md", prep)
        self.assertIn("run-owned", prep)
        self.assertIn("must not", prep.lower())
        self.assertIn("browser", prep.lower())
        self.assertIn("UAT_BROWSER_READINESS_STANDARD.md", prep)
        self.assertIn("UAT_PREP_REPORT.md", read("UAT_STANDARD.md"))
        self.assertIn("PHDK_UAT_PREP.md", read("PHDK_CHECK.md"))

    def test_phase_preserves_browser_exception(self):
        scope = read("EXECUTION_SCOPE.md")
        self.assertIn("## PHDK UAT Prep — explicit preparation", scope)
        self.assertIn("## Scoped browser exception for UAT and UAT Fix", scope)
        self.assertNotIn("UAT Prep phases of an authorized", scope)
        browser = read("UAT_BROWSER_READINESS_STANDARD.md")
        self.assertIn("only inside those UAT phases", browser)

if __name__ == "__main__":
    unittest.main()
