# PHDK Delivery Stop-Loss Standard — v3.3.0

## Delivery, not activity
Auto and Auto Force must optimize **verified milestone delivery**, not changed-file counts, documents, revisions, tool calls, or continued agent activity. ODC demonstrated the hazard of nine open milestones, a large unpublished diff, and no PR/remote integration despite heavy allowance use. This standard applies at entry, milestone planning/dispatch, after material development or failures, before each new work slice, and at session handoff.

## Executable milestone contract
Plan and PMO use the existing \`MILESTONE_PLAN.md\`: milestone ID, concrete user/business capability or complete enabling foundation, in-scope/out-of-scope work, commitment IDs, dependency order, owner restrictions, critical safety invariants, permitted non-UAT technical evidence, remote target, and verified PR/merge/target SHA/version required for PUBLISHED. Prefer dependency-correct vertical increments. Do **not** create fake micro-milestones, publish mock-only stubs or arbitrarily split inseparable schema/auth/migration changes.

**Work in progress: one active value milestone by default.** Bounded workers may handle disjoint parts within that milestone, with PMO owning shared integration/version. Multiple concurrent milestones require a current explicit owner-approved exception, recorded with \`wip_override_ref\`. Publish a safe coherent milestone to the agreed branch using normal checked PR/merge and actual remote readback **before expanding** to unrelated work. Final cross-portfolio integration, final Check/SEO and deferred UAT are not prerequisites for eligible earlier milestone code delivery.

## Hard intervention thresholds without invented telemetry
The existing read-only \`scripts/phdk_auto_gate.py\` reads the additive schema-v1 \`AUTO_STATE.json.delivery_watch\`. Check it before each new slice, after a material finding/rejection and at handoff. No result automatically executes code or overrides protections.

- **FOCUS_DELIVERY** at **45 foreground active minutes without a verified merged milestone**, **100 unintegrated product files**, **more than one active milestone without owner exception**, or **20% actual observed allowance**. Freeze new fronts; finish current value milestone.
- **RECOVER_DELIVERY** at **75 active minutes**, **four nonprogress repair cycles**, or **35% observed allowance**. Freeze speculative features and unrelated PHDK/stack upgrades; inventory actual source/dependencies and integrate the smallest *safe, coherent existing* increment with required gates, PR/merge and target verification.
- **DELIVERY_STOP_LOSS** at **120 active minutes**, **six nonprogress cycles**, or **50% observed allowance**. No more new development or repeated diagnostics. Publish an already-safe increment if possible; otherwise preserve work, identify exact actual blocker and recovery action, create a verifiable branch/portable handoff, and **end the current invocation**. No automatic rerun. A stalled subsequent session remains delivery/recovery-only until proof of integration or explicit owner rescoping.

The clock is cumulative active foreground session time, **not** human-effort estimates or calendar idle time. Actual host allowance use may be recorded only when exposed by the host and attributed to its source; otherwise state \`ALLOWANCE=UNKNOWN\`. Never infer token, allowance, dollars or percentages from wall clock, code, or activity. Diff counts are risk signals, not value delivered. Preserve all real security/hook/owner/access/spending controls. Critical security defects can block publication; UAT remains \`DEFERRED — OWNER OPT-IN\` and cannot block eligible source delivery.

## Additive state, stable across sessions

\`\`\`json
"delivery_watch": {
  "window_started_at": "2026-11-12T15:00:00-06:00",
  "active_minutes_before_session": 0,
  "active_milestones": ["MS-001"],
  "product_files_pending": 0,
  "standards_files_pending": 0,
  "nonprogress_cycles": 0,
  "observed_source": "git status, PR list and current target SHA"
}
\`\`\`

Maintain \`session.started_at\` separately. At session close, carry forward the foreground minutes since the later of session start or last verified delivery by updating \`active_minutes_before_session\`. On next actual foreground session, update session start but **do not reset** delivery window or carry. Only after an **independently verified target merge** may the coordinator record actual PR/remote SHA/version evidence, zero carry and nonprogress count, and reset \`window_started_at\`. An open/draft PR, push, commit, handoff or new chat cannot reset it. Distinguish changed product files from vendored PHDK updates; record actual source for observations. Optional \`allowance_pct_since_delivery\` must be 0–100 with \`allowance_source\`; optional \`wip_override_ref\` must cite current owner authority. Recover missing legacy fields internally as \`REPAIR_STATE\`, not another ceremony.

This advisor is read-only and cannot independently prove telemetry or a GitHub merge. The agent MUST reconcile its state with actual git/GitHub results; a self-reported SHA is not publication proof.

## Recover large stranded changes safely
Inspect owner commitments, current branches/worktrees, diff, target and open PRs, auth/schema dependencies and permitted gates. Classify findings: **A: unsafe/mandatory blocker**; **B: in-scope delivery still missing**; **C: improvement/backlog**. Repair A, integrate a safe coherent subset of existing B, defer C and unrelated standards maintenance. Do not discard code, mass-format, or split inseparable changes just to create artificial progress. If one larger integration is unavoidable, state the exact dependencies, evidence and bounded release plan. If an actual control rejects the operation, report the real rejection, attempted bounded fix, preserved work and one precise owner/next action. Do not simply continue exploring.

## Mandatory delivery pulse
Status and handoff: **verified merged milestones/total**, current milestone/WIP, last merged PR and target SHA or NONE, open PR count, unintegrated product/PHDK file counts, watchdog disposition/foreground minutes, observed allowance or UNKNOWN, exact blocker, next executable delivery action. No completion claim from reports, changed files, an open PR or static PASS. Final whole-goal completion still follows \`PHDK_COMPLETION_GATE.md\`.

No automatic downstream upgrades, new Actions, agents, scheduled monitors, provider writes, unauthorized runtime/UAT tests, expenses or unsafe merges.
