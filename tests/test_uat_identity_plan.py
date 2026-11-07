"""Static checks on rendered catalog data. No product, identities or sessions."""

import json
import subprocess
import tempfile
import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from phdk_uat_identity_plan import DEFAULT_CATALOG, render


class UatIdentityPlanTests(unittest.TestCase):
    def setUp(self):
        self.catalog = json.loads(DEFAULT_CATALOG.read_text(encoding="utf-8"))

    def plan(self, run="r7k2", mode="multi"):
        return render(self.catalog, "pos", run, mode)

    def test_multi_aliases_ownership_and_delegated_journey(self):
        plan = self.plan()
        self.assertEqual(plan, self.plan())
        self.assertEqual(plan["status"], "PLAN_ONLY")
        self.assertEqual(plan["entry_actor"], "platform.owner.01")
        users = {u["key"]: u for u in plan["subjects"]}
        self.assertEqual(len(users), 7)
        self.assertEqual(users["bruma.member.01"]["email"], self.catalog["email_example"])
        self.assertEqual(users["bruma.member.01"]["reports_to"], "bruma.lead.01")
        self.assertEqual(users["nube.member.01"]["reports_to"], "nube.lead.01")
        self.assertTrue(any(j.get("assignee") == "nube.member.01" and j["expect"] == "DENY"
                            for j in plan["journeys"]))
        other = self.plan(run="r7k3")
        self.assertTrue({u["email"] for u in users.values()}.isdisjoint(
            u["email"] for u in other["subjects"]))

    def test_single_scope_resolves_its_own_admin_and_roster(self):
        plan = self.plan(mode="single")
        self.assertEqual(plan["entry_actor"], "companyco.admin.01")
        self.assertEqual({s["scope"] for s in plan["subjects"]}, {"companyco"})
        self.assertEqual(len(plan["subjects"]), 3)

    def test_duplicate_or_unowned_subjects_are_rejected(self):
        ops = self.catalog["rosters"]["operations"]
        ops.append(dict(ops[0]))
        with self.assertRaisesRegex(ValueError, "duplicate subject"):
            self.plan()
        ops.pop()
        ops[-1]["reports_to"] = "other.01"
        with self.assertRaisesRegex(ValueError, "reports_to"):
            self.plan()

    def test_unresolved_journey_is_rejected(self):
        self.catalog["multi_tenant"]["journeys"][0]["assignee"] = "other.member.01"
        with self.assertRaisesRegex(ValueError, "unresolved journey assignee"):
            self.plan()

    def test_reject_oversize_names_and_live_domain(self):
        with self.assertRaisesRegex(ValueError, "64 bytes"):
            self.plan(run="x" * 64)
        self.catalog["email_template"] = self.catalog["email_template"].replace(".test", ".com")
        with self.assertRaisesRegex(ValueError, "reserved email template"):
            self.plan()

    def test_cli_rejects_nested_metadata_without_echoing_it(self):
        topology = self.catalog["multi_tenant"]
        for row, field in ((topology["scopes"][0], "name"), (topology["records"][0], "label"),
                           (self.catalog["rosters"]["operations"][1], "area")):
            with self.subTest(field=field), tempfile.TemporaryDirectory() as temp:
                original = row[field]
                row[field] = {"unexpected": "content-must-stay-private"}
                path = Path(temp) / "catalog.json"
                path.write_text(json.dumps(self.catalog), encoding="utf-8")
                result = subprocess.run(
                    [sys.executable, str(ROOT / "scripts/phdk_uat_identity_plan.py"), "--catalog",
                     str(path), "--project", "pos", "--run", "r7k2", "--mode", "multi"],
                    capture_output=True, text=True, check=False)
                self.assertEqual(result.returncode, 2)
                self.assertEqual(result.stdout, "")
                self.assertIn(f"invalid {field}", result.stderr)
                self.assertNotIn("Traceback", result.stderr)
                self.assertNotIn("content-must-stay-private", result.stderr)
                row[field] = original
