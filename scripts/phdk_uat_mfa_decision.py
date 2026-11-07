#!/usr/bin/env python3
"""Interpret recorded observations offline. The result grants no authority or MFA evidence."""

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


REQUIRED_CHECKS = (
    "phase_authority",
    "prelive_target",
    "isolated_auth_boundary",
    "synthetic_data_and_identities",
    "isolated_side_effects",
    "scoped_provider_policy",
    "revocation_and_launch_guard",
)


def verified(observation):
    if not isinstance(observation, dict) or observation.get("status") != "VERIFIED":
        return False
    ref = observation.get("ref")
    return isinstance(ref, str) and ref.strip().lower() not in (
        "", "-", "unknown", "unverified", "pending", "n/a", "none", "false", "true", "todo",
    )


def unexpired(value, now):
    if not isinstance(value, str):
        return False
    try:
        expiry = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return False
    return expiry.tzinfo is not None and now < expiry


def decide(evidence, now=None):
    """Choose a route from the nonsecret manifest. A source reference is not independently verified."""
    if not isinstance(evidence, dict):
        raise ValueError("expected a JSON object")
    checks = evidence.get("checks")
    checks = checks if isinstance(checks, dict) else {}
    missing = [key for key in REQUIRED_CHECKS if not verified(checks.get(key))]
    if evidence.get("phase") not in ("uat_prep", "uat", "uat_fix"):
        missing.append("phase")
    if evidence.get("target") != "prelive_synthetic":
        missing.append("target")
    if not unexpired(evidence.get("expires_at"), now or datetime.now(timezone.utc)):
        missing.append("expires_at")

    case, factor = evidence.get("case"), evidence.get("factor")
    if case not in ("workflow", "jwt", "mfa"):
        missing.append("case")
    if factor not in ("normal", "provider_automated", "unavailable"):
        missing.append("factor")
    # An already configured provider test factor still requires an isolated
    # pre-live run. Only the two controls specific to an MFA waiver can be absent.
    missing_factor_checks = set(missing) - {"scoped_provider_policy", "revocation_and_launch_guard"}
    decision = "NORMAL_MFA"
    if factor == "provider_automated" and not missing_factor_checks:
        decision = "PROVIDER_AUTOMATED_FACTOR"
    elif case == "mfa" and factor != "normal":
        decision = "MFA_CASE_BLOCKED_OR_MANUAL"
    elif case in ("workflow", "jwt") and factor == "unavailable" and not missing:
        decision = "SCOPED_EXCEPTION_ELIGIBLE"

    return {
        "decision": decision,
        "exception_eligible": decision == "SCOPED_EXCEPTION_ELIGIBLE",
        "missing_checks": missing,
        "mfa_evidence": "NOT_EVALUATED",
        "jwt_evidence": "NOT_EVALUATED",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--evidence", required=True, type=Path, help="local nonsecret JSON manifest")
    args = parser.parse_args()
    try:
        report = decide(json.loads(args.evidence.read_text(encoding="utf-8")))
    except (OSError, ValueError):
        parser.error("cannot read a valid JSON object from the evidence file")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
