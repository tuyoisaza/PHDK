"""Static integrity checks for the fictional identity topology."""

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = json.loads((ROOT / "COMPANY_CO_UAT_IDENTITIES.json").read_text(encoding="utf-8"))


class UatIdentityFixtureTests(unittest.TestCase):
    def test_tenancy_and_entry_actor(self):
        multi = FIXTURE["multi_tenant"]
        single = FIXTURE["single_tenant"]
        cafes = {s["name"]: s for s in multi["scopes"] if s["kind"] == "tenant"}
        self.assertEqual(set(cafes), {"Café Bruma", "Café Nube Andina"})
        catalog = (ROOT / "COMPANY_CO_SERVICE_SCENARIOS.md").read_text(encoding="utf-8")
        for name, cafe in cafes.items():
            self.assertIn(f'| {cafe["source_customer"]} | {name} |', catalog)
            self.assertEqual(cafe["roster"], "operations")
        self.assertEqual(multi["entry_actor"], "platform.owner.01")
        self.assertEqual([s["kind"] for s in single["scopes"]], ["organization"])
        self.assertEqual(single["scopes"][0]["roster"], "operations")
        self.assertEqual(single["entry_actor"], "companyco.admin.01")

    def test_run_scoped_addresses_and_memberships(self):
        self.assertIs(FIXTURE["external_dispatch"], False)
        addresses = set()
        for mode in ("multi_tenant", "single_tenant"):
            for scope in FIXTURE[mode]["scopes"]:
                roster = FIXTURE["rosters"][scope["roster"]]
                members = {f'{row["role"]}.{row["slot"]}' for row in roster}
                self.assertEqual(len(roster), len(members))
                if scope["kind"] != "platform":
                    self.assertTrue({"admin.01", "lead.01", "member.01"} <= members)
                for row in roster:
                    if "reports_to" in row:
                        self.assertIn(row["reports_to"], members)
                    for run in ("r7k2", "r7k3"):
                        address = FIXTURE["email_template"].format(
                            project="pos", run=run, scope=scope["key"],
                            role=row["role"], slot=row["slot"],
                        )
                        self.assertRegex(address, r"^uat-[a-z0-9-]+@companyco\.example\.test$")
                        self.assertNotIn(address, addresses)
                        addresses.add(address)
        self.assertIn(FIXTURE["email_example"], addresses)

    def test_handoffs_and_denials_resolve_to_owned_records_and_subjects(self):
        for mode in ("multi_tenant", "single_tenant"):
            example = FIXTURE[mode]
            subjects = {
                f'{scope["key"]}.{person["role"]}.{person["slot"]}': scope["key"]
                for scope in example["scopes"] for person in FIXTURE["rosters"][scope["roster"]]
            }
            self.assertIn(example["entry_actor"], subjects)
            records = {r["key"]: r["scope"] for r in example["records"]}
            assignments = set()
            readbacks = set()
            denial_actions = set()
            for step in example["journeys"]:
                actor_scope = subjects[step["subject"]]
                if "target" in step:
                    self.assertIn(step["target"], subjects)
                if "assignee" in step:
                    self.assertIn(step["assignee"], subjects)
                if step["expect"] == "DENY":
                    denial_actions.add(step["action"])
                    if "record" in step:
                        target_scope = subjects[step["assignee"]] if "assignee" in step else actor_scope
                        self.assertNotEqual(target_scope, records[step["record"]])
                    continue
                self.assertEqual(step["expect"], "ALLOW")
                self.assertEqual(actor_scope, records[step["record"]])
                if step["action"] == "assign":
                    self.assertEqual(actor_scope, subjects[step["assignee"]])
                    assignments.add((step["record"], step["assignee"]))
                elif step["action"] == "read_assigned":
                    self.assertIn((step["record"], step["subject"]), assignments)
                    readbacks.add((step["record"], step["subject"]))
            self.assertTrue(assignments)
            self.assertEqual(readbacks, assignments)
            expected_denials = {"read_by_id", "assign"} if mode == "multi_tenant" else {"change_role"}
            self.assertEqual(denial_actions, expected_denials)
