#!/usr/bin/env python3
"""Render a synthetic identity plan from a local catalog. No provider access."""

import argparse
import json
import re
from pathlib import Path

DEFAULT_CATALOG = Path(__file__).resolve().parents[1] / "COMPANY_CO_UAT_IDENTITIES.json"
EMAIL = "uat-{project}-{run}-{scope}-{role}-{slot}@companyco.example.test"
SLUG = r"[a-z0-9]+(?:-[a-z0-9]+)*"


def require(condition, message):
    if not condition:
        raise ValueError(message)


def component(value, pattern, field):
    require(isinstance(value, str) and re.fullmatch(pattern, value), f"invalid {field}")
    return value


def text_field(row, field):
    value = row[field]
    require(isinstance(value, str) and value.strip(), f"invalid {field}")
    return value


def rows(value, field):
    require(isinstance(value, list) and all(isinstance(row, dict) for row in value),
            f"{field} must be an array of objects")
    return value


def render(catalog, project, run, mode):
    # Alphanumeric project and run keys keep these two ownership fields unambiguous.
    for key, value in (("project", project), ("run", run)):
        component(value, r"[a-z0-9]+", key)
    require(isinstance(catalog, dict) and catalog.get("schema_version") == 1,
            "expected identity catalog schema_version 1")
    require(catalog.get("classification") == "fictional_synthetic"
            and catalog.get("external_dispatch") is False and catalog.get("email_template") == EMAIL,
            "expected synthetic, no-dispatch catalog with the reserved email template")
    require(mode in ("single", "multi"), "invalid mode")
    topology = catalog[f"{mode}_tenant"]
    rosters = catalog["rosters"]
    require(isinstance(topology, dict) and isinstance(rosters, dict), "expected topology and roster objects")
    scopes, subjects, records = {}, {}, {}
    emails = set()
    for scope in rows(topology["scopes"], "scopes"):
        key = component(scope["key"], SLUG, "scope")
        require(key not in scopes, "duplicate scope")
        require(scope["kind"] in ("organization", "platform", "tenant"), "invalid scope kind")
        scopes[key] = {"key": key, "kind": scope["kind"], "name": text_field(scope, "name")}
        roster_name = text_field(scope, "roster")
        require(roster_name in rosters, "unresolved roster")
        roster = rows(rosters[roster_name], "roster")
        require(roster, "empty roster")
        for row in roster:
            role = component(row["role"], SLUG, "role")
            slot = component(row["slot"], r"0[1-9]|[1-9][0-9]+", "slot")
            subject = f"{key}.{role}.{slot}"
            email = EMAIL.format(project=project, run=run, scope=key, role=role, slot=slot)
            require(subject not in subjects and email not in emails, "duplicate subject key or email")
            require(len(email.split("@")[0]) <= 64, "email local part exceeds 64 bytes; shorten keys")
            emails.add(email)
            account = {"key": subject, "scope": key, "role": role, "slot": slot, "email": email}
            for field in ("area", "native_role", "persona_ref"):
                if field in row:
                    account[field] = text_field(row, field)
            if "reports_to" in row:
                account["reports_to"] = f"{key}.{text_field(row, 'reports_to')}"
            subjects[subject] = account

    kinds = [scope["kind"] for scope in scopes.values()]
    if mode == "single":
        require(kinds == ["organization"], "single mode requires one organization")
    else:
        require("tenant" in kinds and "organization" not in kinds and kinds.count("platform") <= 1,
                "multi mode requires tenant scopes and at most one platform")
    require(topology["entry_actor"] in subjects, "unresolved entry_actor")
    for account in subjects.values():
        if "reports_to" in account:
            require(account["reports_to"] in subjects and account["reports_to"] != account["key"],
                    "unresolved or self-referencing reports_to")

    for record in rows(topology["records"], "records"):
        key = component(record["key"], SLUG, "record")
        require(key not in records and record["scope"] in scopes, "duplicate record or unknown scope")
        records[key] = {"key": key, "scope": record["scope"], "label": text_field(record, "label")}
    journeys = []
    for row in rows(topology["journeys"], "journeys"):
        require(row["subject"] in subjects and row["expect"] in ("ALLOW", "DENY"),
                "unresolved journey subject or invalid expectation")
        action = component(row["action"], r"[a-z][a-z0-9_-]*", "action")
        journey = {"subject": row["subject"], "action": action, "expect": row["expect"]}
        for field, targets in (("record", records), ("assignee", subjects), ("target", subjects)):
            if field in row:
                require(row[field] in targets, f"unresolved journey {field}")
                journey[field] = row[field]
        journeys.append(journey)
    return {"status": "PLAN_ONLY", "project": project, "run": run, "mode": mode,
            "entry_actor": topology["entry_actor"], "scopes": list(scopes.values()),
            "subjects": list(subjects.values()), "records": list(records.values()), "journeys": journeys}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--catalog", type=Path, default=DEFAULT_CATALOG)
    parser.add_argument("--project", required=True, help="short lowercase alphanumeric project key")
    parser.add_argument("--run", required=True, help="short lowercase alphanumeric run key")
    parser.add_argument("--mode", choices=("multi", "single"), required=True)
    args = parser.parse_args()
    try:
        catalog = json.loads(args.catalog.read_text(encoding="utf-8"))
        plan = render(catalog, args.project, args.run, args.mode)
    except (KeyError, TypeError, ValueError, OSError) as exc:
        parser.error(f"invalid identity plan: {exc}")
    print(json.dumps(plan, ensure_ascii=True, indent=2))


if __name__ == "__main__":
    main()
