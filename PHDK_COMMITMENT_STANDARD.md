# PHDK Commitment Ledger and Completion Gate

## Authority and applicability

This standard governs Capture, Plan, PMO, Auto, Integration, UAT and Delivery for every PHDK lifecycle. It is a governance and evidence contract, **not** authorization to work beyond the owner-confirmed scope, bypass review, run agents in the background, or perform provider writes. All work remains in-session under `EXECUTION_SCOPE.md`.

## Canonical record: PHDK_COMMITMENTS.md

Capture creates and maintains `PHDK_COMMITMENTS.md` as the single durable inventory of proposed, confirmed, completed, blocked and explicitly excluded commitments. A stable ID (`CMT-001`, etc.) is never reused or silently deleted. Each row must include:

| Field | Requirement |
|---|---|
| ID / title | Stable identity and testable outcome |
| Origin | Owner statement, Capture, PRD, existing plan, defect, UAT, PR or inferred discovery; link evidence |
| Category / priority | Feature, defect, technical, security or operational; P0/P1/P2 |
| Scope decision | PROPOSED, CONFIRMED, DEFERRED or CANCELLED, with dated owner decision/evidence for latter two |
| Acceptance criteria | Observable conditions, linked requirement/story and case IDs |
| Plan / workstream | Task ID, WS ID, dependency and owner |
| Execution status | NOT STARTED, IN PROGRESS, BLOCKED or IMPLEMENTED; distinguish implementation from delivery |
| Verification | Tests/UAT cases, PASS/FAIL/BLOCKED/MANUAL and evidence reference |
| Git delivery | Branch, commit(s), PR URL/number, PR state, merge SHA and verified target branch |
| Final disposition | DONE, BLOCKED, DEFERRED or CANCELLED, with reason and next owner action if unresolved |
| Last update | Revision/time of the last verified change |

Never calculate progress from narrative optimism. Report percentages only when a weighted/denominator methodology is specified; default to `verified DONE confirmed commitments / all confirmed non-cancelled commitments` and separately show blocked/deferred, so a deferral does not inflate completion. Show counts and denominator. An implemented-but-unmerged change is **not DONE** when delivery to the target branch is in scope.

## Capture inventory confirmation

Before closing Capture, discover requirements from owner input, prior plans, code, known defects, unfinished tasks, UAT, open PRs and current repo evidence. Present the proposed inventory in a legible summary with stable IDs and explicit exclusions; ask one scope-completion question: “These are the items found. Are they all, or do you want to add defects, features or other commitments?” Accept additions and iterate **only when the owner adds something material**. When the owner explicitly already confirmed the scope in the current conversation, reuse that confirmation without another ritual question. If the owner cannot answer, mark unknowns and do not treat silence as confirmation for a material scope choice. Capture delivers a reconciled ledger, baseline traceability, and a concise end-of-stage accounting: included, excluded/deferred, uncertain, and what Plan must consume.

## Plan accounting

Plan maps every CONFIRMED commitment to at least one actionable task/workstream and acceptance criteria. Produce `PHDK_COMMITMENT_COVERAGE.md` with one row per ledger ID, architecture decision, task, workstream, dependency, acceptance case and gap. Fail the Plan exit gate when a confirmed commitment lacks execution ownership or an explicit blocker. Do not quietly drop an item because it is inconvenient or already partly implemented.

## PMO portfolio confirmation and visibility

Before activating workstreams, PMO shows the complete detected portfolio AND asks: “Is this the complete portfolio, or should I add other features, failures or priorities?” Accept additions and update ledger, Plan coverage, owners, dependencies and workstreams before execution. Skip repeat questioning when the owner already confirmed exactly this portfolio. No new commitment becomes active from inference alone.

Maintain `PMO_STATUS.md` as a current control-center dashboard plus `PMO_PROGRESS_REPORT.md` as a dated append-only milestone/decision journal. Show overall confirmed/done/active/blocked/deferred counts, computed completion fraction, then per workstream: objective, accountable owner/worker, status, verified done/total commitments, evidence and last milestone, current activity, next action, blockers/dependencies, PR state and owner decision needed. Never fabricate a 30% estimate; label any non-verifiable percentage as an estimate and give method.

Publish a compact, user-visible PMO board (not just files) at entry, portfolio confirmation, meaningful workstream milestone, state change, blocker, decision request, integration transition and final handoff. Every entry includes timestamp/revision, changed statuses, what closed with evidence, what is running, what is next, and any decision requested. If no material change occurred, do not spam updates. PMO remains responsible for workers, dependencies, integration and delivery reconciliation; delegation alone is not PMO progress.

## No-silent-drop reconciliation

At every handoff, reconcile ledger IDs against the initial confirmed baseline, Plan tasks, PMO workstreams, implementation/evidence, UAT and target-branch delivery. Newly discovered gaps get new IDs and owner scope decisions. Missing IDs, unowned confirmed work, stale statuses or inconsistent PR states fail the next-stage entry gate until resolved. Snapshots of ledger and coverage are included with Capture, Plan, PMO and Delivery historical HANDOFFs; preserve superseded state in history.

## Terminal gate: fail closed

Before saying Auto or Delivery is COMPLETED, generate `PHDK_COMPLETION_AUDIT.md`:

1. Enumerate every CONFIRMED commitment, its acceptance evidence and final disposition; compare initial inventory and planned tasks against delivered work.
2. Reconcile every in-scope branch and PR (including those created by workers): OPEN, DRAFT, MERGED or CLOSED WITHOUT MERGE; confirm real merge SHA and exact remote target revision when available.
3. Identify all unmerged PRs, unfinished tasks, unresolved tests, unresolved blockers, and missing historical handoffs. An open PR is never evidence of completed target-branch delivery.
4. For each unresolved item, either complete the authorized action through normal controls or record its exact blocker, owner, next action and affected commitment. Do not silently defer/cancel or treat missing permissions as success.
5. Declare **COMPLETED** only if all confirmed in-scope commitments are verified DONE, the intended target is verified, required reviews/checks have passed, no in-scope PR remains open/unmerged, and the archive is complete. Otherwise terminal status is **BLOCKED** or **PARTIALLY DELIVERED**, never successful completion. An explicitly owner-approved scope reduction is recorded as a decision and audited against the revised baseline; do not rewrite history to manufacture 100%.

Show a final user-facing reconciliation table with confirmed/done/blocked/deferred/cancelled, each outstanding ID and its reason, PR states and merge SHAs, version/target SHA, validation and next owner action. The end of a conversation never turns unfinished work into DONE.

## Regression scenarios required for PHDK standards review

- Seven confirmed features, five implemented: completion gate rejects DONE and lists two missing IDs.
- Two PRs remain OPEN even with UAT PASS: completion gate rejects DONE and lists both PRs.
- Four workstreams, one blocked: PMO dashboard reports verified denominators, blocker and decision, not invented percentages.
- Owner adds a defect after initial portfolio discovery: new ID flows Capture/Plan/PMO and cannot disappear.
- Owner explicitly defers an item: retain original ID, owner decision and revised baseline, distinguish deferred from delivered.
- A stage reuses a snapshot while requirements change: reject stale upstream handoff and reopen affected stages.

For documentation-only edits, review these scenarios against the normative contracts; do not claim automated tests ran unless a harness actually executed.
