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
    "PHDK_UX_UI.md",
    "PHDK_DESIGN_SYSTEM.md",
    "PHDK_DESIGN.md",
    "PHDK_SECURE.md",
    "PHDK_TENANT_RISK_STANDARD.md",
    "PHDK_STARTER_PROFILE.md",
    "PHDK_PMO.md",
    "PHDK_COMMITMENT_STANDARD.md",
    "PHDK_PROJECT_MANAGEMENT_STANDARD.md",
    "PHDK_RETROSPECTIVE_STANDARD.md",
    "PHDK_REUSE_CATALOG_STANDARD.md",
    "PHDK_DESIGNER_MODE.md",
    "PHDK_THEME_STANDARD.md",
    "UAT_DEFECT_WORKFLOW.md",
    "PHDK_REPOSITORY_STATUS.md",
    "PHDK_COMMUNICATION_STANDARD.md",
    "ONBOARDING_AI_DEVELOPER.md",
    "INANUTSHELL.md",
    "VERIFICATION_LOOP.md",
    "qa_checklist.md",
    "technical_stack.md",
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
        self.assertGreaterEqual(tuple(int(v) for v in version.split(".")), (4, 2, 0))
        self.assertIn(f"**Version v{version}**", read("README.md"))
        self.assertTrue(read("CHANGELOG.md").startswith(f"## v{version}"))
        self.assertTrue(read("PHDK_EVOLUTION_STANDARD.md").startswith(f"## v{version}"))
        manifest = read("PHDK_MANIFEST.txt").splitlines()
        for path in (
            *STANDARDS,
            "schemas/uleds-event.v1.schema.json",
            "scripts/phdk_uleds_validate.py",
            "PHDK_OBSERVABILITY_ANALYTICS.md",
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
        catalog = json.loads(read("PHDK_REUSE_CATALOG.json"))
        selected = [x for x in catalog["entries"]
                    if x["id"] == "starter.uleds-continuous-improvement"]
        self.assertEqual(len(selected), 1)
        self.assertEqual(selected[0]["status"], "SPECIFICATION_ONLY")
        self.assertIsNone(selected[0]["implementation"])
        self.assertFalse(selected[0]["downloadable"])

        self.assertEqual(len(commands), len({c["command"] for c in commands}))

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
        self.assertRegex(support, r"debug (?:mode is )?OFF")
        self.assertIn("data-phdk-component-id", support)
        self.assertIn("RBAC", support)
        self.assertIn("no", read("PHDK_HEAL_STANDARD.md").lower())
        self.assertIn("UAT", read("PHDK_HEAL_STANDARD.md"))
        self.assertIn("no", read("PHDK_ULEDS_STANDARD.md").lower())
        self.assertNotIn("exactly TWO icon-only", debug)
        self.assertNotIn("no third control", debug.lower())
        self.assertIn("ADOPTION_NOT_AUTHORIZED", read("PHDK_CHECK.md"))
        self.assertIn("🤖", read("PHDK_DESIGNER_MODE.md"))
        self.assertIn("SOURCE_UNAVAILABLE", read("PHDK_ULEDS_STANDARD.md"))


    def test_juleth_mandatory_microphone_dictation(self):
        support = read("PHDK_CONTINUOUS_IMPROVEMENT_STANDARD.md")
        required = (
            "microphone dictation",
            "SpeechRecognition",
            "webkitSpeechRecognition",
            "secure context",
            "**explicit user gesture**",
            "editable transcript",
            "Never auto-submit",
            "raw audio",
            "unsupported browser",
            "microphone denied",
            "browser speech provider",
        )
        self.assertEqual([item for item in required if item not in support], [])
        # Negative regression: removal of mandatory owner-gesture guard must fail.
        damaged = support.replace("**explicit user gesture**", "", 1)
        self.assertIn("**explicit user gesture**", [item for item in required if item not in damaged])
        for path in (
            "PHDK_ULEDS_STANDARD.md",
            "PHDK_UX_UI.md",
            "PHDK_DESIGN_SYSTEM.md",
            "PHDK_DESIGN.md",
            "PHDK_CHECK.md",
            "UAT_STANDARD.md",
            "PHDK_STARTER_PROFILE.md",
        ):
            with self.subTest(path=path):
                self.assertIn("dictation", read(path).lower())
        debug = read("DEBUG_DIAGNOSTICS_STANDARD.md")
        self.assertIn("only inside", debug)
        catalog = json.loads(read("PHDK_REUSE_CATALOG.json"))
        starter = next(item for item in catalog["entries"]
                       if item["id"] == "starter.uleds-continuous-improvement")
        self.assertTrue(any("microphone dictation" in item.lower()
                            for item in starter["capabilities"]))
        self.assertEqual(starter["status"], "SPECIFICATION_ONLY")

    def test_schema_and_fixtures(self):
        schema = json.loads(read("schemas/uleds-event.v1.schema.json"))
        self.assertEqual(schema["properties"]["specversion"]["const"], "1.0")
        self.assertIn("data", schema["required"])
        self.assertFalse(schema["additionalProperties"])
        self.assertGreaterEqual(len(schema.get("allOf", [])), 6)
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
            ("unexpected top-level field", lambda d: d.update({"password": "hidden"})),
            ("unexpected data field", lambda d: d["data"].update({"password": "hidden"})),
            ("unexpected actor field", lambda d: d["data"]["actor"].update({"password": "hidden"})),
            ("mismatched channel", lambda d: d["data"].update({"channel": "support"})),
            ("unhashable channel", lambda d: d["data"].update({"channel": {"role": "admin"}})),
            ("unhashable severity", lambda d: d["data"].update({"severity": ["ERROR"]})),
            ("unhashable privacy class", lambda d: d["data"]["privacy"].update({"classification": ["public"]})),
            ("missing error payload", lambda d: d["data"].pop("error")),
            ("bad product version", lambda d: d["data"].update({"product_version": "release"})),
            ("malformed extension", lambda d: d["data"].update({"extensions": {"nested": {"bad": 1}}})),
        ]
        for label, mutate in bad_cases:
            with self.subTest(label=label):
                cloned = copy.deepcopy(event)
                mutate(cloned)
                self.assertTrue(validator.validate(cloned))

    def test_streaming_timing_is_not_implicit(self):
        policy = read("PHDK_ULEDS_STANDARD.md")
        self.assertIn("SOURCE_UNAVAILABLE", policy)
        self.assertIn("30 days", policy)
        self.assertIn("no", read("PHDK_HEAL_STANDARD.md").lower())
        self.assertIn("NOT RUN", read("PHDK_COHERENCE_STANDARD.md"))
        self.assertIn("No", read("PHDK_CONTINUOUS_IMPROVEMENT_STANDARD.md"))

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
