# PHDK Lifecycle Handoff Standard

## Purpose

PHDK lifecycle stages must hand off durable, reviewable artifacts to the next stage.

Every stage has:

1. **required inputs** — evidence that must exist before the stage starts;
2. **required outputs** — canonical artifacts the stage must create/update;
3. **exit gate** — conditions that prove the stage is ready to hand off;
4. **handoff record** — an immutable historical snapshot for the current lifecycle run;
5. **next-stage declaration** — a concise user-facing statement of what just completed, what was produced, and what the next stage will consume.

A later stage may reuse prior work only after verifying the required upstream artifacts exist and are coherent for the current project/revision.

## Lifecycle run identity

Each explicit full lifecycle execution (especially `PHDK auto`) should create a stable run ID.

Recommended format:

```text
YYYYMMDD-HHMM-<short-goal-or-branch>
```

Example:

```text
20261010-1518-core-opportunity-radar
```

Do not use random IDs when a deterministic timestamp + goal/branch identifier is available.

## Current-state dashboard

Maintain a current lifecycle index:

```text
PHDK_LIFECYCLE.md
```

It must contain:

- current run ID;
- project/repository;
- current branch/revision;
- current lifecycle goal / confirmed portfolio;
- current stage;
- stage statuses;
- canonical artifact paths;
- historical run folder;
- blockers/decisions;
- next stage.

This file is current state, not reusable authority.

## Historical run archive

Every lifecycle run creates:

```text
docs/phdk/lifecycle/<run-id>/
```

with a run index:

```text
docs/phdk/lifecycle/<run-id>/LIFECYCLE.md
```

and one folder per executed/reused stage:

```text
00-preflight/
10-capture/
20-plan/
30-pmo/
40-integration/
50-uat/
60-uat-fix/
70-check/
80-remediation/
90-delivery/
```

Each stage folder contains:

- `HANDOFF.md` — mandatory;
- copies/snapshots of the stage's canonical outputs that materially define the handoff.

Historical stage folders are immutable after the next stage starts, except for correcting a factual archival error while preserving the original evidence/history.

Do not make downstream stages depend on mutable links alone. If a canonical artifact will be edited later, snapshot the relevant stage output into the historical folder.

## HANDOFF.md schema

Every stage handoff record must contain:

```md
# PHDK Lifecycle Handoff — <stage>

Run ID: ...
Stage: ...
Status: COMPLETED | REUSED | BLOCKED | NOT APPLICABLE
Started from revision: ...
Completed at revision/worktree: ...
Date/time: ...

## Goal / scope
...

## Inputs verified
- ...

## Work performed
- ...

## Deliverables
- canonical path
- historical snapshot path

## Exit gate
- [x] ...
- [x] ...

## Decisions / assumptions
...

## Risks / blockers
...

## Evidence
...

## Next stage
Stage: ...
Required inputs for next stage: ...
What the next stage must verify before starting: ...
```

## Transition declaration

Whenever Auto/PMO moves from one lifecycle stage to the next, tell the user:

1. **Stage completed/reused**
2. **What that stage was responsible for**
3. **What it delivered**
4. **Where the canonical artifacts live**
5. **Where the historical snapshot lives**
6. **What exit gate passed**
7. **What the next stage will do**
8. **What the next stage must verify before starting**

Example:

```text
Plan — COMPLETED

What Plan did:
- reconstructed current architecture;
- defined target solution/repository/UX architecture;
- produced the dependency-ordered implementation plan.

Delivered:
- SOLUTION_ARCHITECTURE.md
- REPOSITORY_ARCHITECTURE.md
- UX_ARCHITECTURE.md
- IMPLEMENTATION_PLAN.md
- ARCHITECTURE_DECISIONS.md

Historical handoff:
docs/phdk/lifecycle/20261010-1518-core-radar/20-plan/

Exit gate:
- P0 requirements mapped to architecture
- data/security boundaries explicit
- workstream decomposition dependency-safe

Next: PMO / Workstreams
PMO will verify the Plan package exists and use IMPLEMENTATION_PLAN.md + architecture ownership boundaries to create/confirm workstreams.
```

This declaration is informational, not an approval gate.

# Stage contracts

## 00 — Preflight

### Purpose

Verify PHDK itself and the execution/tooling environment before lifecycle work.

### Required inputs

- repository root/current request;
- active native instruction context;
- installed PHDK evidence.

### Required canonical outputs

Create/update:

```text
PHDK_PREFLIGHT_REPORT.md
```

It records:

- installed PHDK version;
- canonical PHDK version;
- manifest count/integrity summary;
- managed-rule state;
- relevant skills/capabilities and availability;
- user-disabled capabilities;
- automatic conservative sync performed, if any;
- unresolved installation/capability limitations.

### Historical outputs

Snapshot:

```text
00-preflight/HANDOFF.md
00-preflight/PHDK_PREFLIGHT_REPORT.md
```

### Exit gate

- PHDK installation is coherent enough for the requested command;
- required command standards exist;
- materially relevant capability limitations are known;
- no silently overwritten PHDK-local changes.

### Next stage must verify

Capture/next stage verifies the Preflight report exists for this run and that no blocking installation defect remains.

---

## 10 — Capture

### Purpose

Define what the product/project is supposed to achieve and why.

### Required inputs

- completed/reused Preflight handoff;
- repository/conversation evidence.

### Required canonical outputs

```text
PROJECT_INTENT.md
PROJECT_BRIEF.md
PRD.md
FEATURES.md
REQUIREMENTS_TRACEABILITY.md
```

### Historical outputs

Snapshot all five canonical Capture artifacts plus `HANDOFF.md`.

### Exit gate

- project intent/ethos coherent;
- all Blocking requirements gaps resolved;
- remaining material unknowns explicit;
- P0 requirements trace to project intent;
- inferred requirements labeled;
- non-goals/constraints explicit.

### Next stage must verify

Plan verifies all five Capture artifacts exist and that the requirements baseline is coherent/current enough for architecture decisions.

---

## 20 — Plan

### Purpose

Translate captured requirements into solution/repository/UX architecture and an executable implementation plan.

### Required inputs

- completed/reused Capture handoff;
- Capture canonical artifacts;
- existing repo architecture for brownfield projects.

### Required canonical outputs

```text
SOLUTION_ARCHITECTURE.md
REPOSITORY_ARCHITECTURE.md
UX_ARCHITECTURE.md
IMPLEMENTATION_PLAN.md
ARCHITECTURE_DECISIONS.md   # when material decisions exist
TASK.md                     # execution-plan integration
```

### Historical outputs

Snapshot all material Plan outputs plus `HANDOFF.md`.

### Exit gate

- P0 requirements mapped to target architecture;
- current/target architecture explicit for brownfield;
- migration/convergence steps exist where needed;
- component/data/security/integration boundaries explicit;
- workstream grouping and dependencies are executable;
- unresolved material architecture decisions explicit.

### Next stage must verify

PMO verifies `IMPLEMENTATION_PLAN.md`, architecture boundaries, dependencies, and any relevant ADRs before creating/confirming workstreams.

---

## 30 — PMO / Workstreams

### Purpose

Turn the implementation plan into an owner-confirmed workstream portfolio and coordinate workstream execution.

### Required inputs

- completed/reused Plan handoff;
- implementation plan;
- architecture ownership/dependency model;
- current git/worktree state.

### Required canonical outputs

```text
PMO.md
PMO_WORKSTREAMS.md
PMO_DEPENDENCIES.md
PMO_STATUS.md
```

### Historical outputs

Snapshot all four PMO artifacts plus `HANDOFF.md`.

When workers produce significant workstream-specific summaries, archive them under:

```text
30-pmo/workstreams/WS-###.md
```

### Exit gate

- active portfolio confirmed or already contained in explicit Auto scope;
- every active workstream has stable ID/outcome/scope;
- dependencies explicit;
- file/component ownership explicit;
- workers completed or residual blockers/deferred state explicit;
- integration queue ready.

### Next stage must verify

Integration Review verifies all expected workstreams have completion evidence and shared/collision surfaces are enumerated.

---

## 40 — Integration Review

### Purpose

Turn completed workstreams into one coherent candidate.

### Required inputs

- completed PMO handoff;
- workstream completion evidence;
- current branches/commits/worktree;
- shared ownership/dependency map.

### Required canonical outputs

Create/update:

```text
INTEGRATION_REPORT.md
```

It must include:

- candidate revision/worktree;
- integrated workstreams;
- changed/shared components;
- conflicts reconciled;
- API/schema/data/navigation contract checks;
- version/changelog reconciliation;
- integrated checks executed;
- unresolved integration risks;
- candidate ready/not-ready decision.

### Historical outputs

```text
40-integration/HANDOFF.md
40-integration/INTEGRATION_REPORT.md
```

Snapshot additional architecture/API/schema evidence only when materially useful.

### Exit gate

- one coherent candidate identified;
- shared-file conflicts resolved or explicitly blocked;
- cross-workstream contracts coherent;
- candidate version/revision identifiable;
- applicable integrated local checks completed;
- no hidden unresolved integration collision.

### Next stage must verify

UAT verifies `INTEGRATION_REPORT.md` says the candidate is ready for acceptance and uses the exact candidate revision/worktree described there.

---

## 50 — UAT

### Purpose

Validate intent-aligned user acceptance on the integrated candidate.

### Required inputs

- completed Integration Review handoff;
- exact candidate revision/worktree;
- Capture/Plan traceability;
- UAT standard.

### Required canonical outputs

```text
UAT_CASES.md
UAT_REPORT.md
```

### Historical outputs

Snapshot both plus `HANDOFF.md`.

### Exit gate

One of:

- ACCEPTED;
- NOT ACCEPTED with actionable FAILs;
- ACCEPTANCE INCOMPLETE with actionable BLOCKED/MANUAL plan.

No unresolved NOT RUN final cases.

### Next stage must verify

UAT Fix verifies the exact UAT report/cases for the same candidate. If UAT is ACCEPTED with no remediation needed, UAT Fix may be NOT APPLICABLE and Check can proceed.

---

## 60 — UAT Fix

### Purpose

Repair UAT failures/removable blockers and provide explicit closure actions for non-removable acceptance gaps.

### Required inputs

- completed UAT handoff;
- UAT report/cases;
- exact candidate/worktree.

### Required canonical outputs

Create/update:

```text
UAT_REMEDIATION.md
UAT_REPORT.md
UAT_CASES.md
```

`UAT_REMEDIATION.md` records:

- defect/blocker IDs;
- root cause;
- repair/action;
- changed components;
- retest;
- RESOLVED / STILL FAILING / BLOCKED / MANUAL;
- remaining owner/external actions.

### Historical outputs

Snapshot all remediation outputs plus `HANDOFF.md`.

### Exit gate

- every fixable in-scope FAIL/removable blocker was attempted;
- retests executed;
- remaining blockers/manual actions are explicit;
- current UAT conclusion is known.

### Next stage must verify

Check verifies the latest UAT status and does not assume ACCEPTED when acceptance remains incomplete.

---

## 70 — Check

### Purpose

Audit the resulting repository against all applicable PHDK standards.

### Required inputs

- latest integrated/remediated candidate;
- Capture + Plan + PMO + Integration + UAT handoffs;
- active PHDK standards.

### Required canonical outputs

```text
PHDK_CHECK_REPORT.md
```

### Historical outputs

```text
70-check/HANDOFF.md
70-check/PHDK_CHECK_REPORT.md
```

### Exit gate

- applicability evaluated;
- all material standards evaluated;
- gaps classified;
- remediation categories assigned;
- overall ALIGNED / GAPS FOUND / ALIGNMENT INCOMPLETE conclusion explicit.

### Next stage must verify

Remediation verifies the exact Check report revision and approved/in-scope gap IDs.

---

## 80 — Remediation

### Purpose

Close in-scope Check gaps.

### Required inputs

- completed Check handoff;
- exact Check report revision;
- authorized/in-scope gap IDs.

### Required canonical outputs

Create/update:

```text
PHDK_REMEDIATION_REPORT.md
PHDK_CHECK_REPORT.md
```

The remediation report records:

- gap ID;
- repair;
- changed components;
- validation;
- final status;
- residual decision/external gaps.

### Historical outputs

Snapshot both plus `HANDOFF.md`.

### Exit gate

- all in-scope fixable gaps attempted;
- Check rerun;
- residual gap explicit;
- repository readiness for delivery known.

### Next stage must verify

Delivery verifies the latest Check/remediation result and identifies any accepted residual limitation.

---

## 90 — Delivery

### Purpose

Complete versioned integration to the requested target and record exactly what shipped.

### Required inputs

- completed/reused prior lifecycle handoffs;
- final candidate;
- final verification evidence;
- delivery target/controls.

### Required canonical outputs

Create/update:

```text
DELIVERY_REPORT.md
```

It records:

- goal/portfolio;
- final version;
- branch;
- source commit(s);
- PR;
- merge method;
- remote target SHA;
- checks/reviews;
- deployment evidence if actually observed;
- residual blockers/limitations;
- links to all lifecycle handoff folders.

### Historical outputs

```text
90-delivery/HANDOFF.md
90-delivery/DELIVERY_REPORT.md
```

The run-level `LIFECYCLE.md` must then be finalized.

### Exit gate

- requested delivery target satisfied or exact blocker recorded;
- resulting version/revision verified;
- lifecycle artifact index complete;
- no stage falsely marked completed.

# Reuse of existing stage artifacts

A stage may be marked REUSED only when the next stage verifies:

- required canonical artifacts exist;
- they are coherent with current intent/goal;
- no material upstream change invalidated them;
- historical origin/revision is identifiable.

When reusing a stage in a new lifecycle run:

- create a new stage `HANDOFF.md` for this run;
- record which canonical/historical artifacts were reused;
- snapshot the reused canonical artifacts into the new run when they are necessary to reconstruct this run historically;
- do not modify the old historical run folder.

# Upstream invalidation

If a later stage discovers that an upstream artifact is materially wrong/outdated:

1. mark the affected current stage BLOCKED;
2. identify the upstream stage/artifact that must be revisited;
3. reopen that stage within the current lifecycle run;
4. create a new revision/snapshot;
5. re-run every downstream exit gate materially affected by the change.

Do not silently patch architecture during UAT or silently rewrite requirements during Check without restoring lifecycle traceability.

# Minimum historical principle

PHDK should preserve enough history that a future assistant/human can answer:

- What did Capture understand at that time?
- What architecture did Plan choose?
- Which workstreams did PMO execute?
- What exactly was integrated?
- What did UAT accept/fail/block?
- What did UAT Fix repair?
- What standards gaps did Check find?
- What remediation happened?
- What version/commit/PR was finally delivered?

If the repo cannot answer those questions from versioned artifacts, the lifecycle handoff is incomplete.
