#!/usr/bin/env python3
"""Check the defect table in an existing UAT report. No network or product access."""

import argparse
from collections import Counter
import os
from pathlib import Path
import re

COLUMNS = ("ID", "Cases", "Severity", "Observed build", "Initial evidence", "State",
           "Fixed build", "Retest build", "Retest result", "Retest evidence", "Next action")
STATES = ("OPEN", "IN_REPAIR", "AWAITING_RETEST", "REOPENED", "RETEST_BLOCKED",
          "VERIFIED_RESOLVED", "OUT_OF_SCOPE")
CASE_ID = r"[A-Za-z0-9][A-Za-z0-9_.-]*"
RESULTS = {"PASS", "FAIL", "BLOCKED", "MANUAL", "NOT RUN"}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def cells(line):
    return [cell.strip() for cell in line.strip().removeprefix("|").removesuffix("|").split("|")]


def specified(value):
    return value.casefold() not in {"", "-", "unknown", "unverified", "tbd", "tba", "n/a", "none",
                                    "latest", "head", "main"}


def evidence(value):
    # A report anchor, artifact path, URL or stable evidence ID names an item to inspect.
    return specified(value) and re.search(r"[/#]|\b\S+\.(?:md|json|png|jpg|webp|txt|log|pdf)\b|\bEV-[\w.-]+", value, re.I)


def evidence_targets(value, report):
    """Compare Markdown links by destination even when snapshots are in different folders."""
    links = re.findall(r"\[[^\]]*\]\(([^\s()]+)\)", value)
    targets = set()
    for link in links or [item.strip() for item in value.split(",")]:
        if "://" in link or re.fullmatch(r"EV-[\w.-]+", link, re.I):
            targets.add(link)
        else:
            name, marker, anchor = link.partition("#")
            path = report.parent / name if name else report
            targets.add(os.path.abspath(path) + marker + anchor)
    return targets


def check_row(row, report):
    defect = row["ID"]
    require(re.fullmatch(r"DEF-[A-Za-z0-9][A-Za-z0-9_.-]*", defect), "invalid defect ID")
    ids = [item.strip() for item in row["Cases"].split(",")]
    cases = set(ids)
    require(len(ids) == len(cases) and all(re.fullmatch(CASE_ID, item) for item in ids),
            f"{defect}: invalid or duplicate case IDs")
    state = row["State"]
    require(state in STATES and row["Severity"] in ("P0", "P1", "P2", "P3"),
            f"{defect}: invalid state or severity")
    require(specified(row["Observed build"]) and evidence(row["Initial evidence"]),
            f"{defect}: original build and concrete evidence are required")
    require(state == "VERIFIED_RESOLVED" or specified(row["Next action"]),
            f"{defect}: pending action or scope disposition required")
    outcomes = {}
    if row["Retest result"] != "-":
        for entry in row["Retest result"].split(","):
            entry = entry.strip()
            if "=" not in entry and len(cases) == 1:
                case, result = ids[0], entry
            else:
                case, _, result = entry.partition("=")
                case, result = case.strip(), result.strip()
            require(case in cases and case not in outcomes and result in RESULTS,
                    f"{defect}: invalid retest result or case mapping")
            outcomes[case] = result
    if {"PASS", "FAIL"}.intersection(outcomes.values()):
        require(specified(row["Retest build"]) and evidence(row["Retest evidence"]),
                f"{defect}: executed retest requires its build and evidence")
    if state == "VERIFIED_RESOLVED":
        require(specified(row["Fixed build"]) and row["Fixed build"] == row["Retest build"],
                f"{defect}: resolution requires a retest on the selected deployed fix")
        require(set(outcomes) == cases and set(outcomes.values()) == {"PASS"},
                f"{defect}: resolution requires PASS for every affected case")
        require(evidence_targets(row["Retest evidence"], report) - evidence_targets(row["Initial evidence"], report),
                f"{defect}: resolution requires new retest evidence")
    if state == "REOPENED":
        require("FAIL" in outcomes.values(), f"{defect}: reopening requires a failed retest")
    if state == "RETEST_BLOCKED":
        require(set(outcomes) != cases or set(outcomes.values()) != {"PASS"},
                f"{defect}: retest marked blocked despite PASS on every case")
    return cases


def read_register(path):
    lines = path.read_text(encoding="utf-8-sig").splitlines()
    headings = [i for i, line in enumerate(lines) if line.rstrip() == "## Defect register"]
    require(len(headings) == 1, f"{path}: expected one '## Defect register' section")
    start = headings[0] + 1
    while start < len(lines) and not lines[start].strip():
        start += 1
    require(start + 1 < len(lines) and tuple(cells(lines[start])) == COLUMNS,
            f"{path}: expected the standard defect table header")
    separator = cells(lines[start + 1])
    require(len(separator) == len(COLUMNS) and all(re.fullmatch(r":?-{3,}:?", c) for c in separator),
            f"{path}: invalid table separator")
    register = {}
    for i in range(start + 2, len(lines)):
        line = lines[i].strip()
        if re.match(r"^#{1,2}\s", line):
            break
        if "|" not in line:
            continue
        values = cells(line)
        require(len(values) == len(COLUMNS) and all(values), f"{path}:{i+1}: malformed defect row")
        row = dict(zip(COLUMNS, values))
        cases = check_row(row, path)
        require(row["ID"] not in register, f"{path}:{i+1}: duplicate {row['ID']}")
        register[row["ID"]] = (row, cases, evidence_targets(row["Initial evidence"], path))
    return register


def reconcile(current, previous):
    for defect, (before, original_cases, original_evidence) in previous.items():
        if defect not in current:
            require(before["State"] in ("VERIFIED_RESOLVED", "OUT_OF_SCOPE"),
                    f"{defect}: unresolved prior finding missing from current report")
            continue
        after, current_cases, current_evidence = current[defect]
        require(before["Observed build"] == after["Observed build"] and original_evidence == current_evidence,
                f"{defect}: original observation changed")
        require(original_cases <= current_cases, f"{defect}: prior case mapping lost")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("report", type=Path)
    parser.add_argument("--previous", type=Path, help="prior report or retained lifecycle snapshot")
    args = parser.parse_args()
    try:
        register = read_register(args.report)
        if args.previous:
            reconcile(register, read_register(args.previous))
    except (OSError, ValueError) as exc:
        parser.exit(1, f"{exc}\n")
    counts = Counter(row["State"] for row, _, _ in register.values())
    print("Register consistent (static only): " + ", ".join(f"{s}={counts[s]}" for s in STATES))


if __name__ == "__main__":
    main()
