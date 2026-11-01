# PHDK Human-Equivalent Development Effort Standard

## Objective and point in the lifecycle

After PMO has reconciled the confirmed workstreams/dependencies and \`MILESTONE_PLAN.md\`, **before executing the first implementation milestone**, show the owner an estimate in uninterrupted **human-equivalent focused workdays**. When PMO is unnecessary for a single workstream, the same checkpoint happens after the Plan milestone breakdown is confirmed. A standalone PMO may show it after portfolio confirmation. This is the requested **informational pause**: tell the owner, then **continue authorized Auto/Auto Force immediately without waiting for a reply**.

Human-equivalent days measure the effort a competent human contributor would need to deliver the specified work, **not** AI execution speed, wall-clock time to completion, a delivery date or team calendar duration. Parallel workers do not make human-equivalent person-days shrink. Do not invent velocity history, estimate from elapsed chat time, or imply a three-day estimate makes Auto run three days. Default **8 hours of focused work per human day**, document any justified local alternative.

## Planning and source of truth

Estimate each value milestone in human-hours, covering required planning/design still pending, implementation, integration, defect repair, non-UAT technical checks, security work, documentation and authorized Git publication **once**, without double-counting shared work. The baseline is the sum of milestone hours. If there are unresolved architectural/design dependencies, describe the assumptions; give a low–high range when materially uncertain and identify confidence \`LOW\`, \`MEDIUM\` or \`HIGH\`. If insufficient source/scope evidence exists, state **INSUFFICIENT BASIS**, explain the missing facts and give no made-up number.

The original estimate, assumptions, per-milestone forecast, excluded work and confidence belong in the existing \`MILESTONE_PLAN.md\` (Effort / human-equivalent section). During implementation PMO updates the existing \`PMO_STATUS.md\` / \`PMO_PROGRESS_REPORT.md\` from actual verified evidence. Keep the first baseline immutable in the historical record and document scope change and re-estimation rather than silently rewriting the forecast. This standard is not a new task authority, approval ledger, stage, Git release boundary or UAT authorization.

## Current-run numeric projection (optional helper input)

Keep a lightweight, factual, non-authorizing projection in \`docs/phdk/lifecycle/<run-id>/EFFORT_STATE.json\`, linked from existing lifecycle / \`AUTO_STATE.json\` by path when helpful. The authoritative task remains root \`TASK.md\`, milestone plan and workstream delivery evidence. This projection does not grant continued execution after a conversation ends.

The minimal schema version 1 is shown with **synthetic example figures**, not a project estimate:

\`\`\`json
{
  "schema_version": 1,
  "human_day_hours": 8,
  "baseline_total_hours": 24,
  "confidence": "MEDIUM",
  "milestones": [
    {"id": "MS-001", "baseline_hours": 8, "verified_equivalent_hours": 8, "remaining_hours": 0, "status": "DONE", "evidence_ref": "synthetic publication evidence"},
    {"id": "MS-002", "baseline_hours": 10, "verified_equivalent_hours": 6.4, "remaining_hours": 3.6, "status": "IN_PROGRESS", "evidence_ref": "synthetic verified slice evidence"},
    {"id": "MS-003", "baseline_hours": 6, "verified_equivalent_hours": 0, "remaining_hours": 6, "status": "PENDING", "evidence_ref": ""}
  ]
}
\`\`\`

All hour values must be nonnegative finite numbers, all IDs unique. \`baseline_total_hours\` is **never rewritten just to make progress look good**. \`verified_equivalent_hours\` is the human-equivalent estimate embodied in independently evidenced, non-overlapping completed product work — not actual human or AI time consumed. Give partial credit only for real completed functional slices with source evidence; if the partial completion is unverifiable, leave effort pending and mark \`IN_PROGRESS\`. A milestone is \`DONE\` only with its required technical integration/publication evidence; an unmerged PR, a mock or an unexecuted check is not sufficient. Keep \`DEPLOYED\`, \`ACCEPTED\` and \`UAT NOT RUN\` separate.

Calculate:
- Initial human workdays = baseline_total_hours / human_day_hours.
- Remaining human workdays = sum(remaining_hours) / human_day_hours.
- Evidence-weighted development progress = 100 × sum(verified_equivalent_hours) / (sum(verified_equivalent_hours) + sum(remaining_hours)).
- If that denominator is zero, report **UNVERIFIED** except where all milestones have credible completed evidence and the development scope is truly finished. Rounding is for display only, one decimal day.
- New complexity, scope additions, rework or actual blockers may increase remaining hours and reduce progress. Explain \`+X h\` variance, source and confidence change. **Elapsed time alone never decrements the balance.**

## Owner-facing display and cadence

At baseline, show an easily scanned checkpoint **before implementation**:

\`\`\`text
PHDK Development ETA · ESFUERZO HUMANO EQUIVALENTE
Plan original: 3.0 jornadas de 8 h (confianza media)
[----------] 0% verificable · Restante: 3.0 jornadas
No es tiempo real de la IA ni una fecha de entrega.
SIGUIENTE PASO: ejecutar MS-001. Continúo.
\`\`\`

At each **meaningful verified milestone**, and when evidence-backed partial progress or scope variance materially changes the forecast, update the bar and remaining days with the same baseline, evidence reference, confidence and next action. Do not spam unchanged statistics or invent a percentage per file, PR opening, worker start, or wall-clock hour. A blocked or in-progress milestone retains its honest remaining effort. At closure, zero remaining work and 100% require verified development completion; report any not-done scope and its remaining or unknown estimate. Final delivery state is independently \`DEVELOPMENT COMPLETE\`, \`PARTIALLY DELIVERED\` or \`BLOCKED\`; Auto still reports optional \`UAT NOT RUN\`.

Read-only manual/synchronous helper: \`python phdk-standards/scripts/phdk_effort_status.py --state docs/phdk/lifecycle/<run-id>/EFFORT_STATE.json\` (source repo: \`scripts/phdk_effort_status.py\`). The helper only reads the JSON and renders the bar/summary; no timers, network, provider calls, background jobs, UAT, approvals or writes. If unavailable, calculate directly from verified PMO evidence and say the helper was not run.

Regression scenarios: initial 24 h = 3.0 workdays; after independently verified 14.4 equivalent hours completed and 9.6 h remaining, show 60% and 1.2 workdays left; scope growth may increase remaining work; elapsed time cannot change numbers; missing evidence, invalid hours and unexplained zero-progress claims fail; a report does not create an approval gate.
