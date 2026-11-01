#!/usr/bin/env python3
"""Synchronous, read-only human-equivalent development effort projection."""
import argparse
import json
import math
from pathlib import Path


def hours(value, label):
    if isinstance(value, bool) or not isinstance(value, (float, int)):
        raise ValueError(f"{label}: expected numeric hours")
    if not math.isfinite(value) or value < 0:
        raise ValueError(f"{label}: expected finite nonnegative hours")
    return float(value)


def summarize(data):
    if not isinstance(data, dict) or data.get("schema_version") != 1:
        raise ValueError("Unsupported effort state schema")
    day = hours(data.get("human_day_hours"), "human_day_hours")
    if not day:
        raise ValueError("human_day_hours must exceed zero")
    baseline = hours(data.get("baseline_total_hours"), "baseline_total_hours")
    milestones = data.get("milestones")
    if not isinstance(milestones, list) or not milestones:
        raise ValueError("A nonempty milestones list is required")
    earned_sum = remaining_sum = 0.0
    ids = set()
    all_done = True
    for item in milestones:
        if not isinstance(item, dict):
            raise ValueError("Each milestone must be an object")
        key = item.get("id")
        if not isinstance(key, str) or not key.strip() or key in ids:
            raise ValueError("Milestone ids must be unique nonempty strings")
        ids.add(key)
        hours(item.get("baseline_hours"), f"{key}.baseline_hours")
        earned = hours(item.get("verified_equivalent_hours"), f"{key}.verified_equivalent_hours")
        left = hours(item.get("remaining_hours"), f"{key}.remaining_hours")
        state = item.get("status")
        if state not in ("DONE", "PENDING", "IN_PROGRESS", "BLOCKED"):
            raise ValueError(f"{key}.status invalid")
        if earned and not str(item.get("evidence_ref") or "").strip():
            raise ValueError(f"{key}: verified work needs evidence_ref")
        if state == "PENDING" and earned:
            raise ValueError(f"{key}: pending work cannot be credited")
        if state == "DONE" and left:
            raise ValueError(f"{key}: DONE milestone has pending effort")
        if state == "DONE" and (not earned or not str(item.get("evidence_ref") or "").strip()):
            raise ValueError(f"{key}: DONE requires verified delivery evidence")
        all_done = all_done and state == "DONE"
        earned_sum += earned
        remaining_sum += left
    total = earned_sum + remaining_sum
    complete = all_done and remaining_sum == 0 and earned_sum > 0
    # An unfinished milestone with zero forecast is not evidence of 100% completion.
    progress = (earned_sum / total * 100) if total else (100.0 if complete else None)
    if not complete and progress is not None and progress >= 100.0:
        progress = None
    return {
        "initial_days": round(baseline / day, 1),
        "remaining_days": round(remaining_sum / day, 1),
        "progress_percent": round(progress, 1) if progress is not None else None,
        "confidence": data.get("confidence", "UNVERIFIED"),
        "day_hours": day,
        "complete_with_evidence": complete,
    }


def render(data):
    p = data["progress_percent"]
    n = min(10, max(0, int(p / 10 + 0.5))) if p is not None else 0
    bar = "#" * n + "-" * (10 - n) if p is not None else "?" * 10
    label = f"{p:.1f}%" if p is not None else "UNVERIFIED"
    return "\n".join([
        "PHDK Development ETA — esfuerzo humano equivalente",
        f"Base: {data['initial_days']:.1f} jornadas de {data['day_hours']:g} h",
        f"[{bar}] {label} verificable | Restante: {data['remaining_days']:.1f} jornadas",
        f"Confianza: {data['confidence']}",
        "No es ETA real de la IA, fecha de entrega ni UAT.",
    ])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--state", type=Path, required=True)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    try:
        data = summarize(json.loads(args.state.read_text(encoding="utf-8")))
    except (OSError, ValueError, TypeError) as exc:
        parser.error(str(exc))
    print(json.dumps(data, ensure_ascii=False, indent=2) if args.json else render(data))


if __name__ == "__main__":
    main()
