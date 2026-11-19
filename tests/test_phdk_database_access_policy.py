"""Source-only regressions for optional, bounded live DB diagnostics (v4.1.0).

These tests validate policy coherence, not agent behavior, real credentials,
Railway connectivity, SQL safety, or production/UAT execution.
"""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

ROUTES = (
    "EXECUTION_SCOPE.md",
    "technical_stack.md",
    "PHDK_PRODUCTION_VERIFICATION.md",
    "PHDK_TEST_AUTOMATION_STANDARD.md",
    "PHDK_PLAN.md",
    "PHDK_AUTO.md",
    "PHDK_CHECK.md",
    "PHDK_PREFLIGHT.md",
    "PHDK_COHERENCE_STANDARD.md",
    "AGENTS.md",
    "SKILL.md",
    "PHDK_NATIVE_RULES.md",
    "README.md",
)


def text(path):
    return (ROOT / path).read_text(encoding="utf-8")


class ScopedDatabaseAccessPolicyTests(unittest.TestCase):
    def test_standard_is_vendored_and_routed(self):
        entry = "PHDK_DATABASE_ACCESS_STANDARD.md | PHDK_DATABASE_ACCESS_STANDARD.md"
        manifest = text("PHDK_MANIFEST.txt").splitlines()
        self.assertEqual(manifest.count(entry), 1)
        for path in ROUTES:
            with self.subTest(path=path):
                self.assertIn("PHDK_DATABASE_ACCESS_STANDARD.md", text(path))

    def test_read_only_non_uat_permission_is_narrow(self):
        policy = text("PHDK_DATABASE_ACCESS_STANDARD.md")
        for required in (
            "not a PHDK command", "read-only diagnostics", "legitimate",
            "production", "tenant", "read-only role", "BEGIN READ ONLY",
            "statement_timeout", "ROLLBACK", "TLS",
            "DIAGNOSTIC_BLOCKED", "ACCESS_CLEANUP_BLOCKED",
            "separately", "explicitly", "Railway",
            "ELEVATED_DIAGNOSTIC", "migration metadata",
            "aggregate counts only",
        ):
            with self.subTest(required=required):
                self.assertIn(required.lower(), policy.lower())
        scope = text("EXECUTION_SCOPE.md")
        self.assertIn("## Scoped read-only live database diagnostics (non-UAT)", scope)
        self.assertIn("PHDK_DATABASE_ACCESS_STANDARD.md", scope)
        self.assertIn("read-only diagnostics", text("technical_stack.md").lower())
        self.assertNotIn(
            "Never run migrations, queries, seeds, or verification probes against a real dev",
            text("technical_stack.md")
        )

    def test_test_runner_and_uat_are_not_weakened(self):
        test = text("PHDK_TEST_AUTOMATION_STANDARD.md")
        production = text("PHDK_PRODUCTION_VERIFICATION.md")
        policy = text("PHDK_DATABASE_ACCESS_STANDARD.md")
        self.assertIn("hermetic", test)
        self.assertIn("no real DB", test)
        self.assertIn("explicit", production)
        self.assertIn("synthetic", production)
        self.assertIn("not a local test-runner check", policy)
        self.assertIn("do not", policy.lower())
        self.assertIn("provider-setting write", policy)
        self.assertIn("no new", text("README.md").lower())

    def test_no_new_database_command_or_catalog_change(self):
        catalog = json.loads(text("PHDK_COMMANDS.json"))
        commands = [x["command"].lower() for x in catalog["commands"]]
        self.assertFalse(any(x.startswith("phdk db") for x in commands))
        self.assertNotIn("PHDK db", text("PHDK_DATABASE_ACCESS_STANDARD.md"))

    def test_release_markers(self):
        version = text("VERSION").strip()
        self.assertGreaterEqual(tuple(map(int, version.split("."))), (4, 1, 0))
        self.assertIn(f"**Version v{version}**", text("README.md"))
        self.assertTrue(text("CHANGELOG.md").startswith(f"## v{version}"))
        self.assertTrue(text("PHDK_EVOLUTION_STANDARD.md").startswith(f"## v{version}"))


if __name__ == "__main__":
    unittest.main()
