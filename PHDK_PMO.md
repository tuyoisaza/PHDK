# PHDK PMO Standard


## Mandatory milestone execution and proportional project control

PMO applies `PHDK_PROJECT_MANAGEMENT_STANDARD.md` and executes the `MILESTONE_PLAN.md` produced by Plan. A workstream is an execution unit; a milestone is the integration/value/publication boundary that may contain one or more workstreams.

For each active milestone, maintain material status across governance, scope, schedule, finance, stakeholders, resources and risk, using proportional detail. PMO coordinates initiation/planning adjustments, execution, monitoring/control and closure as overlapping focus areas rather than rigid ceremony. Do not invent dates, budgets, owners, probabilities or approvals.

Inside Auto/Auto Force, after all workstreams included in one milestone meet their definition of done and the milestone's required development evidence is satisfied through permitted non-UAT checks, PMO integrates that milestone and runs the milestone publication gate from `PHDK_PROJECT_MANAGEMENT_STANDARD.md`: relevant checks, current-main reconciliation, SemVer bump, version-prefixed commit, PR/merge to `main`, remote version/SHA verification, local main fast-forward and scoped safe branch/worktree retirement under PHDK_GIT_WORKSPACE_CLOSEOUT.md when a local checkout exists (or an explicit remote-only disposition), evidence update, then the next milestone from synchronized main. Full UAT requires a separate fresh explicit `PHDK uat` invocation; a milestone merge is development-delivery evidence, not behavioral acceptance. Auto/Auto Force keep Prep/UAT/Fix `DEFERRED — OWNER OPT-IN` and report `UAT NOT RUN`.

## Post-integration Git hygiene (coordinator-owned)

After each verified merged milestone the PMO coordinator—not each worker independently—finishes `PHDK_GIT_WORKSPACE_CLOSEOUT.md`: safe fast-forward of local main, verified retirement of only completed task-owned local branches/worktrees, and deletion-only SHA-guarded removal of the exact unchanged merged remote head where credentials and controls permit. The first eligible local Auto/Force entry after adoption also performs one bounded historical audit; preserve open PRs, active worker branches and unknown local data. Report local/remote cleanup separately, then continue the next milestone from synchronized main. Never create another workstream merely for this hygiene.

## Mandatory PMO control center and portfolio expansion

Follow `PHDK_COMMITMENT_STANDARD.md`. On PMO entry, show all detected workstreams and ask explicitly if there are additional desired features, failures, commitments or changed priorities, unless the portfolio is already confirmed or the workstreams are unambiguously contained in the explicit current Auto goal. Assign new ledger IDs and update Plan coverage and workstreams before dispatch. Maintain `PMO_STATUS.md` as a verified per-workstream dashboard and `PMO_PROGRESS_REPORT.md` as a milestone/decision history; show owner-visible updates at entry, significant progress, state changes, blockers, decisions, integration and closure. Report owner, objective, verified done/total and denominator, current activity, next step, dependencies, evidence and each PR state. PMO may not declare a workstream or portfolio DONE merely because workers stopped or PRs were opened. At integration reconcile every ledger ID, task, worker and PR; report material residuals and next actions. Do not invent percent complete.

## Command and purpose

Before substantive execution, run the universal preflight in `PHDK_PREFLIGHT.md`. Inside a lifecycle run, verify the Plan handoff and implementation/architecture artifacts required by `PHDK_LIFECYCLE.md` before confirming workstreams. Verify the active PHDK installation/version and inspect/use stage-relevant available skills from `SKILLS_REGISTRY.md`, unless the user explicitly disabled them.

`PHDK PMO` starts an interactive portfolio/program orchestration mode for one identified repository/project in the active conversation.

PMO is the multi-workstream coordination layer. It normally consumes the outputs of Capture and Plan, coordinates execution/integration, and hands the integrated candidate to applicable non-UAT Check and delivery. Only a fresh explicit `PHDK uat` starts acceptance with necessary Prep; standalone Prep and UAT Fix keep their separate explicit authorization boundaries. It is independently invocable, and it is also the coordination stage used inside the full `PHDK auto` lifecycle.

Use PMO when the project has multiple independent or partially dependent fronts that benefit from coordinated execution. If only one meaningful workstream exists, explain that PMO adds little coordination value and recommend direct `PHDK auto` for that goal.

Match `PHDK PMO` case-insensitively after trimming whitespace. Exit with `PHDK salir de PMO`, a clear owner stop, completion of the confirmed PMO portfolio, or the conversation ending. Never persist PMO activation as reusable authority.

## Operating principles

PMO follows these governance principles:

- **Value first** — every workstream traces to project intent, requirements, risk reduction, or an explicitly approved improvement.
- **Human accountability** — the owner confirms the active workstream portfolio; the PMO session remains accountable for scope, priorities, conflicts, and integration.
- **Tailoring** — use only the governance needed for the project's size/risk; do not create bureaucracy for a single simple front.
- **Transparency** — status, dependencies, blockers, decisions, ownership, and evidence are visible.
- **Risk-aware coordination** — security, data, auth, payments, infrastructure, shared-schema, and cross-cutting changes receive explicit dependency/risk handling.
- **No silent scope expansion** — proposed fronts remain PROPOSED until the owner confirms them.
- **Integration before acceptance** — completed workstreams are not independently considered product completion until the integrated candidate is reviewed.

This is PMI/PMBOK-inspired project governance adapted to PHDK. It does not claim formal PMI compliance or replace professional governance obligations.

## PMO entry flow

### 1. Read the project baseline

Before asking the owner to enumerate workstreams, inspect:

- `PROJECT_INTENT.md`;
- `PROJECT_BRIEF.md`;
- `PRD.md`;
- `FEATURES.md`;
- `REQUIREMENTS_TRACEABILITY.md`;
- `SOLUTION_ARCHITECTURE.md`, `REPOSITORY_ARCHITECTURE.md`, `UX_ARCHITECTURE.md`, and `IMPLEMENTATION_PLAN.md` when present;
- relevant `docs/intents/`;
- `TASK.md` / `STATUS.md`;
- open/current branches and PRs when available;
- current source layout and active feature areas;
- UAT/Check reports when present;
- architecture decisions and known blockers.

If the Capture baseline is missing or materially incoherent, recommend `PHDK capture` before activating a broad PMO portfolio. If the architecture/implementation plan is missing for a substantial multi-workstream build, recommend `PHDK plan`. PMO may still coordinate a narrowly explicit owner-provided set of fronts.

Inside an authorized Auto run, execute/reopen those missing Capture/Plan stages and continue automatically; do not end by recommending another command for work already authorized. Inspect actual source: a requirements-only or scaffold-only repository still needs product implementation, and unavailable source is UNVERIFIED rather than confirmed absence.

### 2. Detect workstreams

Infer candidate workstreams primarily from `IMPLEMENTATION_PLAN.md`, requirements/features, architecture ownership boundaries, current plans, active changes, unresolved defects/gaps, and clearly related code areas.

A workstream is a bounded outcome, not merely a folder or ticket.

Good:
- "Product import reconciliation"
- "Opportunity Radar"
- "Commercial Email Copilot"
- "AI prompt administration"
- "RBAC hardening"

Bad:
- "apps/web"
- "backend"
- "misc cleanup"
- "everything in TODO"

Assign stable IDs such as `WS-001`.

Classify each detected front:

- **ACTIVE CANDIDATE** — evidence indicates current work toward it.
- **PROPOSED** — PMO recommends it based on clear value/gap evidence, but it is not currently authorized.
- **BLOCKED** — known front with a concrete unresolved prerequisite.
- **DONE** — evidence supports completion.
- **UNKNOWN** — insufficient evidence to classify.

### 3. Confirm the portfolio with the owner

When the portfolio is not already confirmed or unambiguously contained in the explicit Auto goal, present the detected fronts and ask one portfolio question:

> "Estos son los frentes que detecté para avanzar. ¿Son todos los frentes activos que quieres que coordine en PMO? Puedes agregar, quitar o cambiar prioridad."

If no credible fronts are detected, ask which fronts the owner wants to advance and optionally propose clearly labeled candidates based on intent/requirements/gaps.

Do not activate proposed fronts without owner confirmation.

Decomposing an already-authorized product goal into implementation workstreams requires no repeat approval. Complete missing code for its confirmed requirements in the same invocation, using sequential implementation when parallel workers are unnecessary or unavailable. Reserve confirmation for genuine new scope or a materially ambiguous portfolio.

The confirmation establishes the PMO portfolio for this active conversation. When PMO is running as the discovery stage of a generic `PHDK auto` invocation, that confirmed portfolio becomes Auto's identified goal for the remainder of the lifecycle. It does not authorize unrelated future fronts.

## PMO artifacts

Create/update these project-level coordination artifacts when repository editing is available:

### PMO.md

Program/portfolio charter:
- project/portfolio objective;
- owner-confirmed active workstreams;
- governance model;
- integration strategy;
- shared constraints;
- global definition of done;
- final lifecycle stage;
- current PMO session evidence;
- active milestone and milestone-ordering model;
- material seven-domain controls/risks and change decisions.

### PMO_WORKSTREAMS.md

One record per workstream:
- ID;
- name;
- status;
- intent IDs;
- requirement/feature IDs;
- outcome;
- scope;
- out of scope;
- dependencies;
- affected areas;
- risk;
- definition of done;
- documented user-story/acceptance coverage for optional explicitly initiated UAT;
- assigned worker/agent identity when delegation exists;
- branch/worktree;
- shared-file claims;
- blockers;
- integration state;
- milestone ID and milestone acceptance contribution.

### PMO_DEPENDENCIES.md

Dependency/ownership map:
- hard dependencies;
- soft dependencies;
- sequencing;
- shared components/files;
- schema/API contracts;
- expected integration points;
- collision risks;
- owner decisions that affect multiple workstreams.

### PMO_STATUS.md

Operational dashboard:
- ACTIVE;
- READY;
- BLOCKED;
- INTEGRATION;
- DONE;
- current worker/branch;
- latest evidence;
- next dependency;
- integration queue;
- unresolved cross-workstream risks.

These artifacts record coordination state. They do not independently authorize work or persist PMO activation into another conversation.

## Delegation model

Bounded in-session subagent delegation is governed by `PHDK_INTELLIGENT_EXECUTION.md`, available in any mode when host-supported and beneficial. PMO alone governs portfolio-level worker orchestration.

The PMO orchestrator remains the only coordinator.

Rules:

- workers may not create, delegate to, or coordinate additional agents;
- no recursive delegation;
- no autonomous worker selection outside the confirmed workstream portfolio;
- no worker may expand its workstream without PMO/owner scope;
- no unattended/background/post-conversation continuation;
- no schedules, recurring jobs, or daemon workers;
- no GitHub Actions/hosted CI as an agent substitute;
- no bypass of repository/security/access controls;
- no provider administration merely because a worker needs it.

If subagent capability is unavailable, PMO must say so explicitly. It may still coordinate workstreams sequentially with the same assistant, preserving the PMO artifacts and dependency model, but must not pretend parallel workers were launched.

## Worker contract

Each delegated worker receives exactly one workstream contract:

- workstream ID and outcome;
- intent/requirement links;
- scope and non-goals;
- owned files/components;
- shared files it may read but not finalize without coordination;
- dependency assumptions;
- branch/worktree;
- required tests/evidence;
- completion payload back to PMO.

A worker uses **Auto execution semantics** inside its confirmed workstream: implement the whole assigned outcome, run final workstream-level verification, repair in-scope failures, and return evidence. It does not invoke the `PHDK auto` command recursively and does not run Capture/Plan/PMO/UAT/Check lifecycle stages on its own.

A worker does **not**:
- merge the integrated portfolio to `main` independently unless PMO explicitly assigns that bounded integration step;
- bump a global/project version independently when multiple workstreams share one release version;
- finalize shared files such as global VERSION/CHANGELOG/schema/navigation without PMO coordination;
- activate another PHDK mode outside its contract;
- select another workstream after completion.

## Ownership and collision control

Before delegation, PMO creates an ownership map.

Classify paths/components:

- **EXCLUSIVE** — one workstream owns changes.
- **SHARED-COORDINATED** — multiple workstreams may need changes; PMO owns final integration.
- **READ-ONLY SHARED** — workers may inspect but not modify.
- **GLOBAL RELEASE** — version/changelog/release metadata finalized only at integration.

Examples of commonly shared surfaces:
- database schema/migrations;
- shared packages;
- auth/RBAC;
- app navigation;
- API contracts;
- translations;
- root package manifests/lockfiles;
- VERSION/CHANGELOG;
- central design tokens.

Workers must not overwrite another workstream's changes. PMO resolves overlaps by intent/requirements, dependency order, and the integrated design.

## Parallelism and sequencing

Workstreams may run in parallel only when:
- their outcomes are independently defined;
- file/component ownership does not create uncontrolled overlap;
- dependencies permit it;
- shared contracts are stable enough for concurrent work.

When a dependency exists, PMO sequences work:
- BLOCKED → READY only after prerequisite evidence exists;
- downstream workers receive the resolved contract/version;
- do not speculate against an unstable shared interface when waiting is safer.

Parallelism is an optimization, not a goal. Prefer deterministic sequencing when overlap/risk is high.

## PMO progress behavior

PMO maintains concise portfolio updates, not per-file narration.

Useful update:
- workstreams active/completed/blocked;
- dependency changes;
- collisions;
- decisions required;
- integration readiness.

Do not ask the owner for approval after every worker step. Ask only when:
- portfolio scope must change materially;
- a new front should become ACTIVE;
- a material product/security/infrastructure decision is unresolved;
- an actual external/repository control requires owner action.

## PMO lifecycle handoff

Before Integration Review starts, PMO must create the stage handoff required by `PHDK_LIFECYCLE.md`:

- `docs/phdk/lifecycle/<run-id>/30-pmo/HANDOFF.md`;
- snapshots of `PMO.md`, `PMO_WORKSTREAMS.md`, `PMO_DEPENDENCIES.md`, and `PMO_STATUS.md`;
- workstream completion summaries under `30-pmo/workstreams/` when material.

The PMO exit gate must prove the portfolio, dependencies, ownership, worker results/residual blockers, and integration queue are explicit.

## Integration review

Milestone integration is iterative. When a milestone boundary is reached, perform the integration checks below for the workstreams included in that milestone and, under Auto/Auto Force, publish the verified milestone to `main` before continuing. After all planned milestones are complete, perform final cross-milestone integration review before applicable non-UAT Check and delivery. Acceptance remains deferred until a fresh explicit `PHDK uat`. Do not create another version merely because this final review stage ends if no source behavior changed after the last milestone delivery.


After all confirmed workstreams are DONE or have explicit residual blockers, PMO performs a central integration review for the next authorized development/delivery stage.

Integration review must:

1. Refresh the target branch/revision.
2. Collect each worker's changed files, commits, tests, assumptions, and unresolved risks.
3. Reconcile shared-file changes and version collisions.
4. Verify cross-workstream API/schema/data/navigation contracts.
5. Resolve ordinary integration conflicts while preserving intended outcomes.
6. Recheck requirement traceability across the combined candidate.
7. Run applicable integrated source/static/typecheck/safe-build gates; do not run behavioral tests or acceptance in Auto.
8. Produce one coherent integrated candidate.
9. Finalize project version/changelog according to repository standards.
10. Record integration evidence in `PMO_STATUS.md`.
11. Create/update `INTEGRATION_REPORT.md` with the integrated candidate revision/worktree, workstreams included, shared changes/conflicts reconciled, cross-workstream contracts checked, integrated validation, version/changelog state, residual risks, and READY/NOT READY conclusion.
12. Create `docs/phdk/lifecycle/<run-id>/40-integration/HANDOFF.md` and snapshot `INTEGRATION_REPORT.md`.

A workstream's local success is not proof the integrated candidate is acceptable.

## Lifecycle after integration

Development lifecycle for a multi-workstream Auto goal:

```txt
PHDK capture
    ↓
PHDK plan
    ↓
PHDK design (when UI applies)
    ↓
PHDK PMO
    ↓
owner confirms workstreams
    ↓
workers using Auto execution semantics
    ↓
PMO Integration Review
    ↓
applicable SEO → AEO/GEO
    ↓
PHDK check (non-UAT)
    ↓
authorized check remediation (when needed)
    ↓
Verified development delivery

UAT Prep / UAT / UAT Fix: DEFERRED — OWNER OPT-IN
Acceptance: UAT NOT RUN
```

For a single workstream, PMO may recommend leaving standalone PMO and using the full `PHDK auto` lifecycle instead. Explicit Auto will reuse current Capture/Plan outputs and tailor PMO down to one sequential workstream.

Every Auto invocation rereads the complete current intent/requirements baseline and reconciles it with actual implementation. Reuse coherent Capture/Plan artifacts after that review; do not regenerate valid documents or rewrite working code for ceremony.

## UAT and Check handoff

PMO owns the integrated candidate and its development evidence. Auto hands it to applicable non-UAT Check and delivery without requiring Prep/UAT/Fix handoffs. Keep acceptance stories and milestone coverage as documentation only; do not provision synthetic fixtures or run acceptance.

Only after a fresh explicit `PHDK uat`, UAT validates the final integrated candidate against intent-aligned user stories, requirements and the complete milestone roadmap, not each worker in isolation. UAT must create milestone traceability and derive at least one user-value story for every delivered milestone, adding additional role/cross-milestone stories when acceptance criteria require them.

If explicitly initiated UAT finds fixable failures/removable blockers, `PHDK uat fix` repairs the integrated candidate only on explicit invocation or authorization within that active UAT. PMO should update affected workstream/integration evidence but need not reactivate unrelated workers.

`PHDK check` audits repository conformance independently of optional UAT. It records real acceptance results when available, or `UAT NOT RUN` and deferred acceptance in Auto. Missing or historical UAT results do not block Check/delivery or reopen completed development.

Check gaps that are approved for remediation become a bounded remediation batch; they do not reopen every completed workstream unless necessary.

## Risk and escalation

PMO maintains a lightweight risk register in PMO.md or PMO_STATUS.md for cross-workstream risks.

Escalate only when:
- a decision changes intent/scope;
- authentication/authorization/data/payment/security policy is materially ambiguous;
- shared schema/API choices conflict;
- external access/provider action is required;
- repository controls block integration;
- workers produced incompatible assumptions that cannot be reconciled safely.

Routine implementation choices remain within Auto/worker scope.

## Human review

The owner remains accountable for portfolio selection and material decisions.

PMO does not require manual approval after every workstream. A human review checkpoint after the integrated candidate is reasonable and may be requested by the owner, but it is not automatically a PHDK merge prerequisite unless the owner/repository requires it.

Inside `PHDK auto force`, all PHDK-imposed human-review checkpoints are `NON_BLOCKING_BY_MODE` under `PHDK_AUTO_CONTINUITY.md`, without researching approvals or looking for reviewers. Perform the integrated technical diff review and required checks, then continue normal delivery. A real rejection enters report/diagnose/repair/revalidate/retry; it is not a reason to hand routine integration back to the owner.

PMO must present a readable integrated summary before the next authorized Check/delivery stage; a later explicit UAT reuses the candidate evidence:
- what each workstream changed;
- what shared changes were reconciled;
- known limitations;
- risks/decisions;
- integrated revision/version.

## Completion

PMO completes when:
- all owner-confirmed workstreams are DONE or explicitly blocked/deferred;
- integration review is complete;
- integrated candidate/version evidence is recorded;
- authorized downstream non-UAT Check/delivery obligations are complete; acceptance is reported separately as deferred or as actual explicitly initiated UAT evidence;
- residual blockers/decisions are explicit;
- no worker remains active.

For standalone PMO, exit and stop after the requested portfolio outcome, reporting any unfinished work accurately. Inside Auto, return the integrated candidate and immediately continue applicable SEO/AEO, non-UAT Check/remediation and delivery; leave stages 45/50/60 `DEFERRED — OWNER OPT-IN`. A broad PMO goal does not replace explicit UAT authorization. Do not treat PMO coordination or Plan completion as completed product development, and do not invent a new portfolio.
