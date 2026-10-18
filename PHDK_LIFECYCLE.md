## UAT journey handoff extension

`UAT_JOURNEY_STANDARD.md` is mandatory. Stage 50-uat must snapshot `UAT_ROLE_MATRIX.md`, `UAT_ACCESS_REPORT.md`, `UAT_STORIES.md`, `UAT_CASES.md`, `UAT_JOURNEY_MAP.md`, and `UAT_REPORT.md` (plus UX/UI audit when applicable). Stage 60-uat-fix must snapshot `UAT_REMEDIATION.md`, `UAT_RETEST_REPORT.md`, updated UAT_CASES/UAT_REPORT/UAT_JOURNEY_MAP, and relevant UX/UI remediation. Exit gates evaluate every applicable role, safe authenticated switching, step-level evidence and final regression. Every stage transition explicitly ends in `SIGUIENTE PASO` with the immediately actionable owner command or PHDK's next automatic work. Historical initial failures must remain reconstructable.

# PHDK Lifecycle Handoff Standard

## Mandatory commitment tracking at every gate

`PHDK_COMMITMENT_STANDARD.md` is a required downstream vendored contract. Capture must create `PHDK_COMMITMENTS.md`; Plan must produce `PHDK_COMMITMENT_COVERAGE.md`; PMO must keep `PMO_PROGRESS_REPORT.md` and verified `PMO_STATUS.md`; Delivery must produce `PHDK_COMPLETION_AUDIT.md`. Every relevant stage HANDOFF snapshots the ledger and coverage it consumed/produced. No stage may silently omit a confirmed ID. Delivery exit gate cannot pass with open/unmerged in-scope PRs, undelivered confirmed items, missing verification, or an unverified remote target. Report blocked/partially delivered rather than claiming success.

## Purpose

PHDK lifecycle stages must hand off durable, reviewable artifacts to the next stage.

Every stage has:

1. **required inputs** — evidence that must exist before the stage starts;
2. **required outputs** — canonical artifacts the stage must create/update;
3. **exit gate** — conditions that prove the stage is ready to hand off;
4. **handoff record** — an immutable historical snapshot for the current lifecycle run;
5. **next-stage declaration** — a concise user-facing statement of what just completed, what was produced, and what the next stage will consume.

A later stage may reuse prior work only after verifying the required upstream artifacts exist and are coherent for the current project/revision.

## Auto continuity and human-gate policy

Both `PHDK auto` and `PHDK auto force` use `PHDK_AUTO_CONTINUITY.md`. Stage transitions are execution handoffs inside the same authorized goal. Reload the user mandate and next executable action after context compaction and before a terminal response; missing/malformed state is reconstructed internally, never a new approval gate.

In AUTO FORCE, human reviews/sign-offs imposed only by PHDK are `NON_BLOCKING_BY_MODE` from entry. Do not investigate whether they block or seek reviewers/approvals; do not query review/protection configuration preventively. Integration Review remains the assistant's technical diff/source/contract review. Perform applicable mandatory checks and normal versioned branch push → PR → merge → remote-main verification. A mandatory local suite or hook requires no repeated permission within the scoped implementation request.

An actual tool/hook/GitHub rejection is reported, diagnosed, repaired in scope, revalidated and retried while the mandate remains active. Preserve real owner restrictions, security/access controls, hooks and provider boundaries; no evasion or ungrounded repeated writes. A real unresolved blocker affects only dependent work. A non-blocking PHDK human gate must never be copied into the next handoff as a prerequisite or marked as a review that actually occurred.

## Lifecycle run identity

Each explicit full lifecycle execution (especially `PHDK auto` or `PHDK auto force`) should create a stable run ID.

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
PHDK_LIFECYCLE_STATUS.md
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

For Auto variants also maintain `docs/phdk/lifecycle/<run-id>/AUTO_STATE.json` using the schema in `PHDK_AUTO_CONTINUITY.md`: original user-mandate provenance, mode, goal/scope/target, restrictions, current stage, completed/pending actions, blockers and next action. This run-level file is mutable current evidence; stage snapshots remain immutable. Reconcile it with the current conversation and remote facts. It cannot grant authority, resume another conversation, or override a user stop. `scripts/phdk_auto_gate.py` is a supported continuation aid, not an independent permission requirement.

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
45-uat-prep/
50-uat/
60-uat-fix/
65-seo/
67-aeo-geo/
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

This declaration is informational, not an approval gate. During Auto/AUTO FORCE, append the truthful active-mandate/next-action capsule from `PHDK_COMMUNICATION_STANDARD.md` and execute that next eligible action in the same turn. Do not issue a terminal response just because a stage or handoff completed.

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

## Mandatory administration-console lifecycle overlay

For every applicable administered application, apply `ADMIN_CONSOLE_STANDARD.md` from Capture to delivery. Capture inventories tenancy and admin roles; Plan produces `ADMIN_ARCHITECTURE.md`, `ADMIN_CAPABILITY_MATRIX.md`, `ADMIN_SETTINGS_REGISTRY.md` and (AI only) `AI_WORKFLOW_CATALOG.md`. Include these in material 20-plan and 50-uat/70-check handoff evidence. Implementation must deliver real UI/API/DB enforcement, not only files. UAT tests role-profile switching, tenant isolation and CRUD/configuration/agent flows. Check reports every applicable missing/partial/unverified ability; approved --fix/Auto remediates in scope, with material tenancy/security/production decisions excluded. API-only projects with real admin configuration still require secure administrative capability (API/CLI equivalent) and explicit UI applicability decision; static/no-admin projects may justify N/A.

## Mandatory UX/UI quality overlay

For every UI-applicable lifecycle, apply `PHDK_UX_UI.md` to Plan, Implementation, Integration, UAT/UAT Fix and Check. Plan's UX baseline, journeys, design system and design decisions are required upstream handoff inputs. UAT must perform a user-facing UX/UI audit with evidenced P0/P1 quality gate on the exact candidate, including brownfield before/after regression checks. Required outputs and historical snapshots live in the existing Plan/UAT/UAT Fix stage folders. API-only projects provide an evidence-based NOT APPLICABLE record. No browser activity outside the existing UAT/UAT Fix exception.

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
UX_RESEARCH_BASELINE.md
UX_JOURNEYS.md
UI_DESIGN_SYSTEM.md
UX_UI_DECISIONS.md
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

Inside Auto, a passing Plan handoff immediately starts the next eligible implementation task through stage 30. Missing product code activates required greenfield development; it never turns the Plan handoff into a terminal response or a request for another development command.

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
- each in-scope commitment has concrete implementation/source evidence or an explicit unfinished blocker; coordination artifacts, assignments and scaffolds alone never prove workstream completion;
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
- all required product behavior in the authorized scope is implemented and integrated, or the candidate is explicitly NOT READY with the missing commitment IDs;
- shared-file conflicts resolved or explicitly blocked;
- cross-workstream contracts coherent;
- candidate version/revision identifiable;
- applicable integrated local checks completed;
- no hidden unresolved integration collision.

### Next stage must verify

UAT Prep verifies `INTEGRATION_REPORT.md` and its candidate. If Prep modifies code/schema, it refreshes the current integration candidate and reruns affected integration checks, preserving prior historical evidence. UAT later verifies this revised candidate and the Prep handoff.

---

## 45 — UAT Prep

### Purpose

Build and verify synthetic test identities, secure role sessions and test-only provider/fixture readiness **before** browser UAT. Follow `PHDK_UAT_PREP.md`.

### Inputs

Current integration handoff/candidate, source-backed auth/RBAC/tenancy, Company Co fixture, `JWT_STANDARD.md`, safe isolated target.

### Canonical outputs

`UAT_AUTH_PLAN.md`, `UAT_ROLE_MATRIX.md`, `UAT_FIXTURE_MANIFEST.md`, `UAT_PREP_REPORT.md` and applicable source/test implementation.

### Historical outputs

`45-uat-prep/HANDOFF.md` plus sanitized snapshots of canonical outputs; never tokens, passwords or browser storage state.

### Exit and next-stage gate

Evidence of per-role provisioned test-only identities or exact blockers; valid test bootstrap, local/in-process allow/deny and tenant checks; isolation, expiry and cleanup controls; revision reconciled with Integration after Prep code changes. UAT checks the same candidate plus the Prep handoff and carries precise blockers forward. The browser readiness check begins **only at 50 — UAT**.

---

## 50 — UAT
**Entry gate:** Run `UAT_BROWSER_READINESS_STANDARD.md` after Integration Review and before the first browser-dependent case, verifying scoped phase authorization and technical browser availability independently. Save evidence/safety/no-new-spend disposition in `UAT_ACCESS_REPORT.md`, summarize in `UAT_REPORT.md`, and retain exact BLOCKED cases if not connected. Missing access does not justify paid API/budget approval or a stop of independent safe acceptance checks.


### Purpose

Validate intent-aligned user acceptance on the integrated candidate.

### Required inputs

- completed Integration Review handoff;
- verified `45-uat-prep` handoff/role fixtures or documented source-backed N/A, with outstanding per-role blockers;
- exact candidate revision/worktree reconciled after Prep changes;
- Capture/Plan traceability;
- UAT standard.

### Required canonical outputs

```text
UAT_CASES.md
UAT_REPORT.md
UX_UI_AUDIT_REPORT.md  # when UI applies
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
UX_UI_REMEDIATION_REPORT.md  # when UX/UI defects exist
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

## 65 — SEO

### Purpose
After UAT/UAT Fix, improve applicable public-site technical SEO and content discoverability on the validated candidate.

### Required inputs
- UAT/UAT Fix handoff (or documented NOT APPLICABLE), verified candidate, Capture audience/intent, current route map and `PHDK_SEO.md`.

### Required canonical outputs
- `SEO_AUDIT_REPORT.md`, `SEO_CHECKLIST.md`, `SEO_REMEDIATION_REPORT.md` (or evidence-based NOT APPLICABLE record).

### Historical outputs
- `65-seo/HANDOFF.md` and snapshots of applicable reports, changes and regression evidence.

### Exit gate
- 25 controls classified with evidence or applicability justified; in-scope fixes and retests recorded; critical indexability blockers unresolved only with BLOCKED status; affected UAT evidence revalidated.

### Next stage must verify
- AEO/GEO consumes SEO handoff, public-route indexability baseline and current UAT candidate.

---

## 67 — AEO/GEO

### Purpose
After SEO, improve credible public answers and citation-readiness for answer/generative search, without promises of model placement.

### Required inputs
- SEO handoff/applicability, current candidate, Capture intent and `PHDK_AEO_GEO.md`.

### Required canonical outputs
- `AEO_GEO_AUDIT_REPORT.md`, `AEO_GEO_CHECKLIST.md`, `AEO_GEO_REMEDIATION_REPORT.md` (or evidence-based NOT APPLICABLE record).

### Historical outputs
- `67-aeo-geo/HANDOFF.md` and material snapshots.

### Exit gate
- 15 controls evidenced/classified; supported corrections retested; blocked external measurements not mislabeled PASS; affected UAT revalidated.

### Next stage must verify
- Check validates SEO and AEO/GEO exit gates, or their documented NOT APPLICABLE reasons.

---

## 70 — Check

### Purpose

Audit the resulting repository against all applicable PHDK standards.

### Required inputs

- latest integrated/remediated candidate;
- Capture + Plan + PMO + Integration + UAT + SEO + AEO/GEO handoffs or grounded NOT APPLICABLE records;
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
- Auto mode and mandate evidence; under AUTO FORCE, PHDK-only human gates recorded as `NON_BLOCKING_BY_MODE`, never fabricated human approval;
- real delivery rejections and their diagnosis, scoped repair, revalidation and retry outcomes when applicable;
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
- no stage falsely marked completed;
- for Auto/AUTO FORCE, no remaining executable in-scope action is hidden behind a terminal response; finalize actual completed/stopped/blocked state in `AUTO_STATE.json` under the continuity contract.

# Reuse of existing stage artifacts

At every explicit Auto invocation, reread the complete current intent/requirements baseline and reconcile it with actual product source under `PHDK_AUTO.md`. Reuse is the result of this review, not a reason to omit it. Preserve valid code/documents and honor the current authorized scope. Missing required product implementation is pending work, never grounds to mark implementation, Integration or UAT NOT APPLICABLE; only intent/scope-based irrelevance justifies N/A.

A stage may be marked REUSED only when the next stage verifies:

- required canonical artifacts exist;
- they are coherent with current intent/goal;
- no material upstream change invalidated them;
- historical origin/revision is identifiable.
- claimed implementation and validation have current evidence; a plan or old completion label alone cannot satisfy an implementation/acceptance gate.

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
- What did SEO audit, improve and validate?
- What did AEO/GEO verify and improve without fabricating AI visibility?
- What standards gaps did Check find?
- What remediation happened?
- What version/commit/PR was finally delivered?

If the repo cannot answer those questions from versioned artifacts, the lifecycle handoff is incomplete.
