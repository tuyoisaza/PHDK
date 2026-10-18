#!/usr/bin/env python3
"""Suggest the next Auto action from factual state; never grant authority or execute it.

Local standard-library only: no network, shell, GitHub review lookup or state writes.
Missing bookkeeping calls for internal repair, not a new owner approval.
"""
import argparse
import json
import sys
from pathlib import Path


MODES = {"auto", "auto_force"}
KINDS = {"work", "review_diff", "required_check", "delivery", "verify_delivery"}
STATES = {"pending", "running", "blocked", "done"}
BLOCKERS = {"phdk_human_review", "real_failure", "external_dependency", "owner_decision", "owner_stop"}


def nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def choice(value, options):
    return isinstance(value, str) and value in options


def string_list(value, required=False):
    return isinstance(value, list) and (bool(value) or not required) and all(nonempty(x) for x in value)


def result(disposition, actions=None, **details):
    return {"disposition": disposition, "actions": actions or [], **details,
            "authority": "Advisory only; reconcile with the current user instruction. No action executed."}


def validate(state, mode):
    errors = []
    if not isinstance(state, dict):
        return ["state must be an object"]
    if not choice(mode, MODES):
        errors.append("current mode must be auto or auto_force")
    if type(state.get("schema_version")) is not int or state["schema_version"] != 1:
        errors.append("schema_version must be 1")
    if state.get("mode") != mode:
        errors.append("recorded mode must be reconciled with the current invocation")
    for key in ("run_id", "repository", "goal", "target_branch", "candidate_ref"):
        if not nonempty(state.get(key)):
            errors.append(f"missing {key}")
    if not string_list(state.get("completion_criteria"), required=True):
        errors.append("completion_criteria must be a nonempty string list")
    grant = state.get("authorization")
    if not isinstance(grant, dict):
        errors.append("authorization must record the actual user mandate")
    else:
        for key in ("source_ref", "instruction"):
            if not nonempty(grant.get(key)):
                errors.append(f"authorization missing {key}")
        if not choice(grant.get("status"), {"active", "paused", "revoked", "completed"}):
            errors.append("invalid authorization status")
        if not string_list(grant.get("scope"), required=True):
            errors.append("authorization scope must be a nonempty string list")
        if not string_list(grant.get("restrictions")):
            errors.append("authorization restrictions must be a string list")
    steps, blockers = state.get("steps"), state.get("blockers")
    if not isinstance(steps, list) or not steps:
        errors.append("steps must be a nonempty list")
    if not isinstance(blockers, list):
        errors.append("blockers must be a list")
    if errors:
        return errors

    step_ids, blocker_ids = set(), set()
    for item in blockers:
        if not isinstance(item, dict) or not nonempty(item.get("id")):
            errors.append("each blocker needs an id")
            continue
        bid = item["id"]
        if bid in blocker_ids:
            errors.append(f"duplicate blocker {bid}")
        blocker_ids.add(bid)
        if not choice(item.get("kind"), BLOCKERS):
            errors.append(f"{bid}: invalid blocker kind")
        if not nonempty(item.get("reason")):
            errors.append(f"{bid}: missing reason")
        if item.get("kind") == "phdk_human_review":
            # FORCE never demands provenance research to waive a PHDK-only review.
            continue
        for key in ("evidence", "observed_at"):
            if not nonempty(item.get(key)):
                errors.append(f"{bid}: missing actual {key}")
        if item.get("kind") == "real_failure":
            if not nonempty(item.get("failed_operation")):
                errors.append(f"{bid}: missing failed_operation")
            if "repair_action" in item and not nonempty(item["repair_action"]):
                errors.append(f"{bid}: repair_action must describe a concrete action")
        else:
            for key in ("source_ref", "next_action"):
                if not nonempty(item.get(key)):
                    errors.append(f"{bid}: missing {key}")
            if not string_list(item.get("resolution_attempts"), required=True):
                errors.append(f"{bid}: record attempted resolution before waiting")
    for item in steps:
        if not isinstance(item, dict) or not nonempty(item.get("id")):
            errors.append("each step needs an id")
            continue
        sid = item["id"]
        if sid in step_ids:
            errors.append(f"duplicate step {sid}")
        step_ids.add(sid)
        if not choice(item.get("kind"), KINDS) or not choice(item.get("status"), STATES):
            errors.append(f"{sid}: invalid kind/status")
        if not nonempty(item.get("action")):
            errors.append(f"{sid}: missing executable action")
        for key in ("depends_on", "blocked_by"):
            if not string_list(item.get(key)):
                errors.append(f"{sid}: {key} must be a string list")
        if item.get("status") == "done" and not nonempty(item.get("evidence")):
            errors.append(f"{sid}: completed step needs observed evidence")
    if errors:
        return errors
    graph = {}
    done = {item["id"] for item in steps if item["status"] == "done"}
    for item in steps:
        sid = item["id"]
        for dep in item["depends_on"]:
            if dep not in step_ids:
                errors.append(f"{sid}: unknown dependency {dep}")
        for bid in item["blocked_by"]:
            if bid not in blocker_ids:
                errors.append(f"{sid}: unknown blocker {bid}")
        if sid in done and any(dep not in done for dep in item["depends_on"]):
            errors.append(f"{sid}: completed evidence has an unfinished prerequisite; reconcile and revalidate")
        graph[sid] = set(item["depends_on"])
    # A dependency-cycle is bookkeeping to repair, not a request for approval.
    while graph:
        ready = {sid for sid, deps in graph.items() if not deps}
        if not ready:
            errors.append("dependency graph contains a cycle or unknown dependency")
            break
        graph = {sid: deps - ready for sid, deps in graph.items() if sid not in ready}
    return errors


def evaluate(state, mode):
    # A documented stop remains visible even while unrelated state needs repair.
    grant = state.get("authorization") if isinstance(state, dict) else None
    status = grant.get("status") if isinstance(grant, dict) else None
    if choice(status, {"paused", "revoked", "completed"}):
        action = "Honor the recorded user stop while reconciling it with the live instruction; repair bookkeeping only."
        if status == "completed":
            action = "The recorded goal ended; do not reactivate it from a file."
        return result("STOPPED", [action], status=status, state_errors=validate(state, mode))
    errors = validate(state, mode)
    if errors:
        return result("REPAIR_STATE", ["Repair the record from current task facts and continue; do not ask for renewed permission."], errors=errors)
    steps = state["steps"]
    by_id = {item["id"]: item for item in state["blockers"]}
    done = {item["id"] for item in steps if item["status"] == "done"}
    pending = [item for item in steps if item["status"] != "done"]
    ignored = sorted({bid for item in pending for bid in item["blocked_by"]
                      if mode == "auto_force" and by_id[bid]["kind"] == "phdk_human_review"})
    notes = {"non_blocking_reviews": ignored, "review_disposition": "NON_BLOCKING_BY_MODE" if ignored else "NONE"}
    if not pending:
        return result("VERIFY_DELIVERY", ["Verify the actual target content/version and completion evidence before reporting complete."], **notes)
    waiting, ready, repairs = [], [], []
    verification = {item["id"] for item in pending if item["kind"] in {"review_diff", "required_check"}}
    for item in pending:
        if any(dep not in done for dep in item["depends_on"]):
            continue
        if item["kind"] in {"delivery", "verify_delivery"} and verification:
            continue
        real = [by_id[bid] for bid in item["blocked_by"] if bid not in ignored]
        external = [b for b in real if b["kind"] in {"external_dependency", "owner_decision", "owner_stop"}]
        if external:
            waiting.extend({"step_id": item["id"], "blocker_id": b["id"], "action": b["next_action"]} for b in external)
            continue
        failures = [b for b in real if b["kind"] == "real_failure"]
        if failures:
            for b in failures:
                repair = b.get("repair_action") or "Diagnose the observed rejection and repair its cause within the current scope."
                repairs.append({"step_id": item["id"], "blocker_id": b["id"], "action": repair,
                                "then": f"Revalidate affected checks, retry the failed delivery operation, and verify remote {state['target_branch']}."})
            continue
        reviews = [b for b in real if b["kind"] == "phdk_human_review"]
        action = item["action"] if not reviews else "Perform the pending PHDK technical diff review within current permissions, then continue delivery."
        ready.append({"step_id": item["id"], "action": action})
    if repairs:
        return result("REPAIR_AND_RETRY", repairs, independent_actions=ready, waiting=waiting, **notes)
    if ready:
        return result("CONTINUE", ready, waiting=waiting, **notes)
    if waiting:
        return result("WAITING_EXTERNAL", waiting, **notes)
    return result("REPAIR_STATE", ["Reconcile step dependencies and missing prerequisites internally; do not turn a stale status into a human gate."], **notes)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--state", required=True, help="Run-local AUTO_STATE.json")
    parser.add_argument("--mode", required=True, choices=sorted(MODES), help="Mode from the current user instruction, not authority restored from a file")
    args = parser.parse_args()
    try:
        state = json.loads(Path(args.state).read_text(encoding="utf-8"))
        outcome = evaluate(state, args.mode)
    except (OSError, ValueError) as exc:
        outcome = result("REPAIR_STATE", ["Reconstruct the record from the current authorized request and observed progress."], errors=[str(exc)])
    print(json.dumps(outcome, ensure_ascii=False, indent=2))
    # An absent/stale record is not a publication control or approval rejection.
    return 0


if __name__ == "__main__":
    sys.exit(main())
