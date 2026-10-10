# PHDK PMO Standard

## Command and purpose

Before substantive execution, run the universal preflight in `PHDK_PREFLIGHT.md`. Verify the active PHDK installation/version and inspect/use stage-relevant available skills from `SKILLS_REGISTRY.md`, unless the user explicitly disabled them.

`PHDK PMO` starts an interactive portfolio/program orchestration mode for one identified repository/project in the active conversation.

PMO is the multi-workstream coordination layer. It normally consumes the outputs of Capture and Plan, coordinates execution/integration, and hands the integrated candidate to UAT/UAT Fix/Check. It is independently invocable, and it is also the coordination stage used inside the full `PHDK auto` lifecycle.

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

Present the detected fronts and ask one portfolio question:

> "Estos son los frentes que detecté para avanzar. ¿Son todos los frentes activos que quieres que coordine en PMO? Puedes agregar, quitar o cambiar prioridad."

If no credible fronts are detected, ask which fronts the owner wants to advance and optionally propose clearly labeled candidates based on intent/requirements/gaps.

Do not activate proposed fronts without owner confirmation.

The confirmation establishes the PMO portfolio for this active conversation. It does not authorize unrelated future fronts.

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
- current PMO session evidence.

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
- UAT coverage;
- assigned worker/agent identity when delegation exists;
- branch/worktree;
- shared-file claims;
- blockers;
- integration state.

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

PMO is the only PHDK mode that may delegate coding/review tasks to subagents/worker agents, and only when the current runtime/tool explicitly supports such agents.

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

## Integration review

After all confirmed workstreams are DONE or have explicit residual blockers, PMO performs a central integration review before UAT.

Integration review must:

1. Refresh the target branch/revision.
2. Collect each worker's changed files, commits, tests, assumptions, and unresolved risks.
3. Reconcile shared-file changes and version collisions.
4. Verify cross-workstream API/schema/data/navigation contracts.
5. Resolve ordinary integration conflicts while preserving intended outcomes.
6. Recheck requirement traceability across the combined candidate.
7. Run applicable integrated static/build/test gates.
8. Produce one coherent integrated candidate.
9. Finalize project version/changelog according to repository standards.
10. Record integration evidence in `PMO_STATUS.md`.

A workstream's local success is not proof the integrated candidate is acceptable.

## Lifecycle after integration

Default lifecycle for a multi-workstream project:

```txt
PHDK capture
    ↓
PHDK plan
    ↓
PHDK PMO
    ↓
owner confirms workstreams
    ↓
workers using Auto execution semantics
    ↓
PMO Integration Review
    ↓
PHDK uat
    ↓
PHDK uat fix (when needed)
    ↓
PHDK check
    ↓
approved check remediation (when needed)
    ↓
Done
```

For a single workstream, PMO may recommend leaving standalone PMO and using the full `PHDK auto` lifecycle instead. Explicit Auto will reuse current Capture/Plan outputs and tailor PMO down to one sequential workstream.

Capture may already be complete; do not force rerunning it when the requirements baseline is coherent.

## UAT and Check handoff

PMO owns the integrated candidate handed to UAT.

UAT validates the integrated candidate against intent-aligned user stories and requirements, not each worker in isolation.

If UAT finds fixable failures/removable blockers, `PHDK uat fix` repairs the integrated candidate. PMO should update affected workstream/integration evidence but need not reactivate unrelated workers.

After UAT reaches ACCEPTED or the owner explicitly accepts remaining external/manual limits, `PHDK check` audits repository conformance.

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

PMO must present a readable integrated summary before UAT:
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
- required downstream UAT/UAT Fix/Check stages requested by the PMO goal are complete;
- residual blockers/decisions are explicit;
- no worker remains active.

Then exit PMO and stop. Do not automatically invent the next portfolio.
