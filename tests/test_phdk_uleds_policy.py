"""Offline source and synthetic ULEDS/Heal regressions (not deployed UAT)."""
from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
STANDARDS = (
    "PHDK_ULEDS_STANDARD.md",
    "PHDK_CONTINUOUS_IMPROVEMENT_STANDARD.md",
    "PHDK_DEVELOPMENT_LEDGER_STANDARD.md",
    "PHDK_HEAL_STANDARD.md",
)
ROUTES = (
    "AGENTS.md",
    "SKILL.md",
    "PHDK_NATIVE_RULES.md",
    "PHDK_PLAN.md",
    "PHDK_AUTO.md",
    "PHDK_CHECK.md",
    "PHDK_PREFLIGHT.md",
    "PHDK_COHERENCE_STANDARD.md",
    "PHDK_EVOLUTION_STANDARD.md",
    "EXECUTION_SCOPE.md",
    "PHDK_OBSERVABILITY_ANALYTICS.md",
    "README.md",
)
EXAMPLES = sorted((ROOT / "examples" / "uleds").glob("*.json"))
spec = importlib.util.spec_from_file_location(
    "phdk_uleds_validate", ROOT / "scripts" / "phdk_uleds_validate.py"
)
assert spec and spec.loader
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


def read(name):
    return (ROOT / name).read_text(encoding="utf-8")


class ULEDSContractTests(unittest.TestCase):
    def test_release_and_distribution(self):
        version = read("VERSION").strip()
        self.assertEqual(version, "4.2.0")
        self.assertIn(f"**Version v{version}**", read("README.md"))
        self.assertTrue(read("CHANGELOG.md").startswith(f"## v{version}"))
        self.assertTrue(read("PHDK_EVOLUTION_STANDARD.md").startswith(f"## v{version}"))
        manifest = read("PHDK_MANIFEST.txt").splitlines()
        for path in (
            *STANDARDS,
            "schemas/uleds-event.v1.schema.json",
            "scripts/phdk_uleds_validate.py",
            "examples/uleds/client-error.v1.json",
            "examples/uleds/contextual-feedback.v1.json",
            "examples/uleds/support-request.v1.json",
            "examples/uleds/deployment-failed.v1.json",
        ):
            with self.subTest(path=path):
                self.assertEqual(manifest.count(f"{path} | {path}"), 1)
        commands = json.loads(read("PHDK_COMMANDS.json"))["commands"]
        heal = [x for x in commands if x["command"] == "PHDK heal"]
        self.assertEqual(len(heal), 1)
        self.assertEqual(heal[0]["standard"], "PHDK_HEAL_STANDARD.md")
        self.assertEqual(heal[0]["effect"], "READ_ONLY_PLAN")

    def test_agent_routing(self):
        for path in ROUTES:
            with self.subTest(path=path):
                text = read(path)
                self.assertIn("PHDK_ULEDS_STANDARD.md", text)
                self.assertIn("PHDK_HEAL_STANDARD.md", text)

    def test_ui_contract_and_permissions(self):
        debug = read("DEBUG_DIAGNOSTICS_STANDARD.md")
        support = read("PHDK_CONTINUOUS_IMPROVEMENT_STANDARD.md")
        self.assertIn("🤖", debug)
        self.assertIn("🤖", support)
        self.assertIn("clipboard", debug)
        self.assertIn("trash", debug)
        self.assertIn("public", debug.lower())
        self.assertIn("debug OFF", support)
        self.assertIn("data-phdk-component-id", support)
        self.assertIn("RBAC", support)
        self.assertIn("no", read("PHDK_HEAL_STANDARD.md").lower())
        self.assertIn("UAT", read("PHDK_HEAL_STANDARD.md"))
        self.assertIn("no", read("PHDK_ULEDS_STANDARD.md").lower())
        self.assertNotIn("exactly TWO icon-only", debug)
        self.assertNotIn("no third control", debug.lower())

    def test_schema_and_fixtures(self):
        schema = json.loads(read("schemas/uleds-event.v1.schema.json"))
        self.assertEqual(schema["properties"]["specversion"]["const"], "1.0")
        self.assertIn("data", schema["required"])
        self.assertGreaterEqual(len(EXAMPLES), 4)
        for path in EXAMPLES:
            with self.subTest(path=path.name):
                event = json.loads(path.read_text(encoding="utf-8"))
                self.assertEqual(validator.validate(event), [])
                self.assertIn(event["type"], (
                    "phdk.client.error", "phdk.deployment.failed",
                    "phdk.support.request", "phdk.feedback.contextual"
                ))

    def test_negative_privacy_and_provenance(self):
        event = json.loads(EXAMPLES[0].read_text(encoding="utf-8"))
        bad_cases = [
            ("missing project", lambda d: d["data"].pop("project_id")),
            ("query tokens", lambda d: d["data"]["location"].update(
                {"route": "/clientes?access_token=abc"})),
            ("unredacted", lambda d: d["data"]["privacy"].update(
                {"redacted": False})),
            ("fake sha", lambda d: d["data"].update({"git_sha": "abc"})),
            ("bad taxonomy", lambda d: d.update({"type": "arbitrary.run_code"})),
            ("missing event time", lambda d: d.pop("time")),
        ]
        for label, mutate in bad_cases:
            with self.subTest(label=label):
                cloned = copy.deepcopy(event)
                mutate(cloned)
                self.assertTrue(validator.validate(cloned))

    def test_no_background_or_autoexecution_claim(self):
        heal = read("PHDK_HEAL_STANDARD.md")
        self.assertIn("foreground", heal)
        self.assertIn("read-only", heal)
        self.assertIn("explicit", heal)
        self.assertIn("No", heal)
        self.assertIn("PHDK auto", heal)
        self.assertIn("provider", heal.lower())


if __name__ == "__main__":
    unittest.main()
