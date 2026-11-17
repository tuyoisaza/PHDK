"""Source-contract regressions: Upgrade Force must request opt-in before Auto Force.

This standard is conversational; these tests check routed source policy, not a
product command runtime or an agent's actual future behavior.
"""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

ROUTES = (
    "PHDK_UPGRADE.md",
    "PHDK_AUTO.md",
    "PHDK_AUTO_CONTINUITY.md",
    "AGENTS.md",
    "SKILL.md",
    "PHDK_NATIVE_RULES.md",
    "README.md",
    "PHDK_PREFLIGHT.md",
    "PHDK_COMMUNICATION_STANDARD.md",
    "PHDK_SECURE.md",
)


class UpgradeForceOwnerConfirmationPolicyTests(unittest.TestCase):
    def text(self, path):
        return (ROOT / path).read_text(encoding="utf-8")

    def test_each_active_entrypoint_requires_separate_owner_reply(self):
        for path in ROUTES:
            with self.subTest(path=path):
                value = self.text(path).lower()
                self.assertIn("upgrade force", value)
                self.assertIn("auto force", value)
                self.assertTrue("sí/no" in value or "yes/no" in value
                                or "affirmative" in value, path)
                self.assertTrue("owner" in value or "propietario" in value, path)

    def test_upgrade_has_explicit_yes_no_declined_silence_and_blocker(self):
        upgrade = self.text("PHDK_UPGRADE.md")
        for required in (
            "¿Quieres ejecutar PHDK auto force ahora? (Sí/No)",
            "AUTO_FORCE=DECLINED",
            "AUTO_FORCE=AWAITING_OWNER",
            "AUTO_FORCE=NOT_OFFERED",
            "UPGRADE_REMOTE_MAIN=BLOCKED/UNVERIFIED",
            "Do not start product investigation",
        ):
            self.assertIn(required, upgrade)

    def test_no_obsolete_unconditional_chain_in_main_routes(self):
        for path in ("PHDK_UPGRADE.md", "PHDK_AUTO.md", "SKILL.md", "README.md"):
            with self.subTest(path=path):
                value = self.text(path)
                self.assertNotIn("transition immediately into `PHDK auto force`", value)
                self.assertNotIn("immediately continues as `PHDK auto force`", value)
                self.assertNotIn("continues here without another command", value)

    def test_command_catalog_describes_only_conditional_auto(self):
        catalog = json.loads(self.text("PHDK_COMMANDS.json"))
        command = next(x for x in catalog["commands"]
                       if x["command"] == "PHDK upgrade force")
        self.assertEqual(command["effect"], "FORCED_SYNC_THEN_OWNER_CONFIRMATION")
        self.assertIn("Sí/No", command["summary"])
        self.assertIn("confirmación", command["when"])

    def test_release_markers_and_standalone_auto_remain_independent(self):
        self.assertEqual(self.text("VERSION").strip(), "4.0.0")
        self.assertIn("**Version v4.0.0**", self.text("README.md"))
        self.assertIn("MAJOR", self.text("CHANGELOG.md").splitlines()[2])
        self.assertIn("A standalone explicit Auto invocation", self.text("PHDK_AUTO.md"))


if __name__ == "__main__":
    unittest.main()
