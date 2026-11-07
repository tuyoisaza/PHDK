"""Synthetic offline source scenarios for the read-only PHDK help catalog renderer.

Not a product/UAT test. Safe only where repo policy permits executing standards helpers.
"""

from __future__ import annotations

import contextlib
import importlib.util
import io
import json
import shutil
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "phdk_help.py"
SPEC = importlib.util.spec_from_file_location("phdk_help", SCRIPT)
assert SPEC and SPEC.loader
phdk_help = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(phdk_help)


class PHDKHelpTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.vendored = self.root / "phdk-standards"
        self.vendored.mkdir()
        shutil.copyfile(ROOT / "PHDK_COMMANDS.json", self.vendored / "PHDK_COMMANDS.json")
        (self.vendored / "VERSION").write_text("2.92.0\n", encoding="utf-8")

    def tearDown(self):
        self.temp.cleanup()

    def invoke(self, *args):
        stdout, stderr = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
            rc = phdk_help.main(["--root", str(self.root), *args])
        return rc, stdout.getvalue(), stderr.getvalue()

    def test_catalog_has_unique_names_and_real_canonical_standards(self):
        catalog = json.loads((ROOT / "PHDK_COMMANDS.json").read_text(encoding="utf-8"))
        names = set()
        for command in catalog["commands"]:
            for name in [command["command"], *command.get("aliases", [])]:
                key = phdk_help.normalize(name)
                self.assertNotIn(key, names)
                names.add(key)
            self.assertTrue((ROOT / command["standard"]).is_file(), command)
        self.assertGreaterEqual(len(catalog["commands"]), 20)
        for expected in ("PHDK help", "PHDK auto", "PHDK auto force", "PHDK uat", "PHDK upgrade force", "PHDK export modules"):
            self.assertIn(phdk_help.normalize(expected), names)

    def test_every_command_listed_with_context_and_no_writes(self):
        (self.root / "PROJECT_INTENT.md").write_text("# Intent\n\n## Objetivo\nConstruir un catálogo de productos para usuarios reales.\n", encoding="utf-8")
        (self.root / "MILESTONE_PLAN.md").write_text("# Plan\n", encoding="utf-8")
        before = sorted(p.relative_to(self.root).as_posix() for p in self.root.rglob("*"))
        rc, text, error = self.invoke()
        after = sorted(p.relative_to(self.root).as_posix() for p in self.root.rglob("*"))
        self.assertEqual(rc, 0, error)
        self.assertIn("v2.92.0", text)
        self.assertIn("Construir un catálogo", text)
        catalog = json.loads((ROOT / "PHDK_COMMANDS.json").read_text(encoding="utf-8"))
        for entry in catalog["commands"]:
            self.assertIn(entry["command"] + " — ", text)
        self.assertIn("Recomendación: PHDK auto", text)
        self.assertEqual(before, after)

    def test_capture_when_goal_not_documented(self):
        rc, out, err = self.invoke("--json")
        self.assertEqual(rc, 0, err)
        data = json.loads(out)
        self.assertEqual(data["project_goal"], "no documentado / sin verificar")
        self.assertEqual(data["recommendation"], "PHDK capture")
        self.assertTrue(data["read_only"])

    def test_plan_when_intent_exists_without_plan(self):
        (self.root / "PROJECT_INTENT.md").write_text("## Purpose\nImprove customer support quality via transparent workflows.\n", encoding="utf-8")
        rc, out, err = self.invoke("--json")
        self.assertEqual(rc, 0, err)
        self.assertEqual(json.loads(out)["recommendation"], "PHDK plan")

    def test_alias_and_command_detail_do_not_activate_mode(self):
        rc, out, err = self.invoke("--command", "browser allow", "--json")
        self.assertEqual(rc, 0, err)
        data = json.loads(out)
        self.assertEqual(data["selected_command"]["command"], "PHDK browser on")
        self.assertEqual(data["commands"], [])
        self.assertTrue(data["read_only"])
        rc, out, err = self.invoke("--command", "auto force")
        self.assertEqual(rc, 0, err)
        self.assertIn("Comando: PHDK auto force", out)

    def test_unknown_command_and_missing_install_do_not_mutate(self):
        rc, out, err = self.invoke("--command", "invented deploy")
        self.assertEqual(rc, 2)
        self.assertIn("Comando no encontrado", err)
        (self.vendored / "PHDK_COMMANDS.json").unlink()
        rc, out, err = self.invoke()
        self.assertEqual(rc, 2)
        self.assertIn("instalación/catálogo", err)


if __name__ == "__main__":
    unittest.main()
