"""Offline decision-table checks using fictional observations."""

import sys
import unittest
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from phdk_uat_mfa_decision import REQUIRED_CHECKS, decide


NOW = datetime(2026, 11, 7, tzinfo=timezone.utc)


class UatMfaDecisionTests(unittest.TestCase):
    def setUp(self):
        self.evidence = {
            "phase": "uat", "case": "workflow", "factor": "unavailable",
            "target": "prelive_synthetic", "expires_at": "2026-11-07T00:15:00Z",
            "checks": {key: {"status": "VERIFIED", "ref": f"run.md#{key}"} for key in REQUIRED_CHECKS},
        }

    def decision(self, **changes):
        return decide({**self.evidence, **changes}, NOW)

    def test_bounded_exception_is_advice_only(self):
        report = self.decision()
        self.assertEqual(report["decision"], "SCOPED_EXCEPTION_ELIGIBLE")
        self.assertTrue(report["exception_eligible"])
        self.assertEqual(report["mfa_evidence"], "NOT_EVALUATED")
        self.assertEqual(report["jwt_evidence"], "NOT_EVALUATED")

    def test_missing_unverified_or_unreferenced_observation_closes_exception(self):
        for key in REQUIRED_CHECKS:
            for observation in (None, True, {"status": "UNKNOWN", "ref": "audit.md"},
                                {"status": "VERIFIED", "ref": "unknown"}):
                with self.subTest(key=key, observation=observation):
                    checks = {**self.evidence["checks"], key: observation}
                    report = self.decision(checks=checks)
                    self.assertEqual(report["decision"], "NORMAL_MFA")
                    self.assertIn(key, report["missing_checks"])

    def test_unknown_live_mixed_unauthorized_and_expired_targets(self):
        for field, values in {
            "target": ("live", "mixed", None), "phase": ("auto", "check", None),
            "case": (None, "unexpected"), "factor": ("unknown", None),
            "expires_at": ("2026-11-07T00:00:00Z", "2026-11-07T00:15:00", None),
        }.items():
            for value in values:
                with self.subTest(field=field, value=value):
                    report = self.decision(**{field: value})
                    self.assertFalse(report["exception_eligible"])
                    self.assertIn(field, report["missing_checks"])

    def test_real_factors_take_precedence_and_mfa_cases_require_one(self):
        for kind in ("workflow", "jwt", "mfa"):
            self.assertEqual(self.decision(case=kind, factor="normal")["decision"], "NORMAL_MFA")
            self.assertEqual(self.decision(case=kind, factor="provider_automated")["decision"],
                             "PROVIDER_AUTOMATED_FACTOR")
        for factor in ("unknown", "unavailable"):
            self.assertEqual(self.decision(case="mfa", factor=factor)["decision"],
                             "MFA_CASE_BLOCKED_OR_MANUAL")
        self.assertEqual(self.decision(case="jwt")["mfa_evidence"], "NOT_EVALUATED")

    def test_source_values_are_never_echoed(self):
        self.evidence["checks"]["phase_authority"]["ref"] = "unique-private-source-reference"
        self.assertNotIn("unique-private-source-reference", repr(self.decision()))

    def test_provider_test_factor_requires_verified_prelive_target_and_run(self):
        controls = ("phase_authority", "prelive_target", "isolated_auth_boundary",
                    "synthetic_data_and_identities", "isolated_side_effects")
        missing_controls = [
            {"checks": {**self.evidence["checks"], key: None}} for key in controls
        ]
        for changes in [{"target": target} for target in ("live", "mixed", "unknown")] + [
            {"phase": "auto"}, {"expires_at": "2026-11-07T00:00:00Z"}, *missing_controls,
        ]:
            with self.subTest(changes=changes):
                self.assertEqual(self.decision(factor="provider_automated", **changes)["decision"],
                                 "NORMAL_MFA")
                self.assertEqual(self.decision(case="mfa", factor="provider_automated", **changes)["decision"],
                                 "MFA_CASE_BLOCKED_OR_MANUAL")
