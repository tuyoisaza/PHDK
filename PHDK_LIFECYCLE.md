**Hybrid Secure (v2.63.0):** During Auto/Force, perform milestone security deltas and a consolidated `PHDK secure` gate after integration and before final Check/delivery, following [PHDK_SECURE.md](PHDK_SECURE.md). Secure is development validation only: it never initiates UAT Prep/UAT/Fix, forbidden local runtime tests, Docker, new infrastructure or paid scans. Remediate authorized vulnerabilities, preserve real security gates, record evidence and residual risk; Critical/High confirmed issues block clearance absent an explicit permitted owner risk decision.\n\n## v2.62.0 — Explicit-only UAT authorization (overrides legacy automatic-stage wording)

**Binding rule:** `PHDK auto` and `PHDK auto force` MUST NOT invoke, enter, provision, seed, or run UAT Prep (45), UAT (50), or UAT Fix (60), even after milestones, deployment, Check, or a failed prior UAT. Neither FORCE nor a generic full-lifecycle instruction grants UAT authorization. These stages are **DEFERRED — OWNER OPT-IN**, not BLOCKED, FAILED, or a completion prerequisite. This rule takes precedence over any older automatic UAT transitions in this file.

Auto/Force must implement **all authorized milestones first**, perform permitted static checks and integration review, version/commit/push/PR/merge each completed value milestone, finish applicable SEO/AEO and Check/remediation without invoking acceptance tests, deploy through the existing authorized production route, verify remote main and deployment with available non-UAT evidence, and report truthful **DEVELOPMENT COMPLETE / PARTIALLY DELIVERED / BLOCKED** separately from **UAT NOT RUN**. A deployment that cannot be verified must be reported as unverified, not complete. Preserve user stories, acceptance criteria and milestone-to-story mapping as *documentation only*; no synthetic accounts, fixtures, browser journeys, runtime acceptance, or UAT spending in Auto. Do not execute local behavioral tests, Docker, or unauthorized external services.

At the end, offer `PHDK uat` as an optional **future explicit command**, without waiting for an answer as a delivery gate. Only a fresh, explicit owner invocation of `PHDK uat` authorizes UAT and its necessary Prep prerequisite, subject to normal access, safety and spending controls. Standalone `PHDK uat prep` prepares identities only when explicitly requested; it does not authorize running UAT. `PHDK uat fix` requires explicit invocation or authorization within an active explicitly initiated UAT. Prior UAT failures never reopen the completed development goal or prevent subsequent independent development.

## UAT journey handoff extension

For an explicitly initiated UAT run, `UAT_JOURNEY_STANDARD.md` is mandatory. Stage 50-uat must snapshot `UAT_ROLE_MATRIX.md`, `UAT_ACCESS_REPORT.md`, `UAT_MILESTONE_MATRIX.md` when a milestone plan exists, `UAT_STORIES.md`, `UAT_CASES.md`, `UAT_JOURNEY_MAP.md`, and `UAT_REPORT.md` (plus UX/UI audit when applicable). When UAT Fix is explicitly authorized, stage 60-uat-fix must snapshot `UAT_REMEDIATION.md`, `UAT_RETEST_REPORT.md`, updated UAT_CASES/UAT_REPORT/UAT_JOURNEY_MAP, and relevant UX/UI remediation. Exit gates evaluate every applicable role, safe authenticated switching, step-level evidence and final regression. Every stage transition explicitly ends in `SIGUIENTE PASO` with the immediately actionable owner command or PHDK's next automatic work. Historical initial failures must remain reconstructable.

# PHDK Lifecycle Handoff Standard

## Design before UI implementation

For applicable UI scope, `PHDK_DESIGN.md` adds **25-design** after technical/content Plan and before dependent UI implementation. The Auto sequence is Capture → Plan → Design → PMO/implementation → Integration → applicable SEO/AEO → Check → Delivery. UAT Prep → UAT/Fix is a separate, explicitly invoked acceptance sequence. **Auto asks one unresolved visual question at a time and waits for the owner; Auto Force selects, records AGENT_SELECTED_AUTO_FORCE and continues without a PHDK visual-approval pause.** Actual owner restrictions remain binding. Reuse current owner-approved baselines; no forced redesign for non-visual changes or immutable historical runs.

## Tenant-risk handoff

For multi-tenant scope, apply `PHDK_TENANT_RISK_STANDARD.md` from Capture to Check. Capture creates a provisional `TENANT_RISK_ASSESSMENT.md`; Plan confirms or escalates the owner decision; Integration records implemented controls; separately authorized UAT Prep/UAT use safe synthetic tenant identities and Check records evidence, gaps and residual risk without initiating acceptance. Auto records deferred runtime evidence separately from its non-UAT checks. Reference or snapshot the sanitized assessment in relevant HANDOFF records; reopen on changed exposure, sensitive data, contract, incident or blast radius. No new tenant-risk stage or approval ceremony is implied. `PHDK_PRODUCTION_VERIFICATION.md` remains authoritative for where and how behavioral verification may occur throughout this lifecycle: local static checks only, no local runtime tests/Docker/new staging, and bounded production UAT with safe synthetic ownership and cleanup.

## Milestone roadmap and acceptance traceability

Apply `PHDK_PROJECT_MANAGEMENT_STANDARD.md` across Plan, Design, PMO/implementation, Integration and UAT.

- Plan must create/snapshot `MILESTONE_PLAN.md` with every in-scope commitment/task/workstream mapped to a value milestone.
- Design updates only affected tasks/acceptance criteria and links the selected baseline; its exit is not an automatic release milestone.
- PMO tracks milestone execution and records actual version/PR/main evidence after each completed Auto/Auto Force milestone publication.
- A milestone delivery does not close the lifecycle run; Auto continues from verified `main`.
- Only after explicit `PHDK uat`, acceptance must create/snapshot `UAT_MILESTONE_MATRIX.md` and cover every delivered milestone with at least one intent-linked user-value story plus additional role/cross-milestone cases where required.
- Lifecycle stage transitions themselves do not imply version bumps.

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

A later authorized stage may reuse prior work only after verifying its required upstream artifacts exist and are coherent for the current project/revision. Auto/Auto Force leave stages 45/50/60 `DEFERRED — OWNER OPT-IN`, report `UAT NOT RUN`, and do not require their artifacts to enter SEO, AEO/GEO, Check or Delivery. Deferred acceptance is not a failed or missing development handoff.

## Auto continuity and human-gate policy

Both `PHDK auto` and `PHDK auto force` use `PHDK_AUTO_CONTINUITY.md`. Transitions among their authorized development stages are execution handoffs inside the same goal; they do not activate optional acceptance. Reload the user mandate and next executable action after context compaction and before a terminal response; missing/malformed state is reconstructed internally, never a new approval gate.

Normal Auto's Design selection/preview approval is the specific product-input exception in `PHDK_DESIGN.md`, not a ceremonial delivery review. While waiting, record stage 25 as BLOCKED with reason `DESIGN_AWAITING_OWNER`, retain the exact unanswered question and existing mandate, and continue genuinely independent authorized work. Resume from the answer without repeating already resolved choices or asking for another development command.

In AUTO FORCE, human reviews/sign-offs imposed only by PHDK are `NON_BLOCKING_BY_MODE` from entry, including Design's owner-selection wait. Complete the Design work, select and record the baseline, then continue. Do not investigate whether PHDK reviews block or seek reviewers/approvals; do not query review/protection configuration preventively. Integration Review remains the assistant's technical diff/source/contract review. Perform applicable permitted checks and normal versioned branch push → PR → merge → remote-main verification. Preserve the production-first local boundary and never bypass an incompatible required hook.

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
- stage statuses, including Design between Plan and UI implementation;
- canonical artifact paths;
- historical run folder;
- blockers/decisions;
- next stage.

This file is current state, not reusable authority.

For Auto variants also maintain `docs/phdk/lifecycle/<run-id>/AUTO_STATE.json` using the schema in `PHDK_AUTO_CONTINUITY.md`: original user-mandate provenance, mode, goal/scope/target, restrictions, current stage, completed/pending actions, blockers and next action. This run-level file is mutable current evidence; stage snapshots remain immutable. Reconcile it with the current conversation and remote facts. It cannot grant authority, resume another conversation, or override a user stop. `scripts/phdk_auto_gate.py` is a supported continuation aid, not an independent permission requirement. A generic continuation suggestion never overrides the explicit mode-specific Design decision rule.

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
25-design/
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

Create folders only for executed/reused stages. In Auto, record stages 45/50/60 as `DEFERRED — OWNER OPT-IN` in the run index and current dashboard; no fabricated Prep/UAT/Fix folders, reports or completion snapshots are required. An explicitly initiated later acceptance run records its own actual handoffs and links the delivered candidate.

Each executed/reused stage folder contains:

- `HANDOFF.md` — mandatory;
- copies/snapshots of the stage's canonical outputs that materially define the handoff.

Historical stage folders are immutable after the next stage starts, except for correcting a factual archival error while preserving the original evidence/history.

Do not make downstream stages depend on mutable links alone. If a canonical artifact will be edited later, snapshot the relevant stage output into the historical folder. New Design handoffs do not require retroactively rewriting completed pre-Design runs.

## HANDOFF.md schema

Every stage handoff record must contain:

```md
# PHDK Lifecycle Handoff — <stage>

Run ID: ...
Stage: ...
Status: COMPLETED | REUSED | BLOCKED | NOT APPLICABLE
# Deferred acceptance is recorded in the run index as DEFERRED — OWNER OPT-IN; no execution handoff is created.
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
- produced the dependency-ordered implementation plan and draft design constraints.

Delivered:
- SOLUTION_ARCHITECTURE.md
- REPOSITORY_ARCHITECTURE.md
- UX_ARCHITECTURE.md
- UI_DESIGN_SYSTEM.md
- UX_UI_DECISIONS.md
- IMPLEMENTATION_PLAN.md
- ARCHITECTURE_DECISIONS.md

Historical handoff:
docs/phdk/lifecycle/20261010-1518-core-radar/20-plan/

Exit gate:
- P0 requirements mapped to architecture
- data/security boundaries explicit
- workstream decomposition dependency-safe
- Design inputs ready

Next: Design
Design verifies the technical/content baseline and prepares the selected visual style guide and previews.
Auto asks for the unresolved visual choice; Auto Force selects and continues.
```

The transition declaration itself is informational, not an approval gate. The actual ordinary Auto Design choice is governed separately by `PHDK_DESIGN.md`. During Auto/AUTO FORCE, append the truthful active-mandate/next-action capsule from `PHDK_COMMUNICATION_STANDARD.md` and execute the next eligible action in the same turn. Do not issue a terminal response merely because a stage/handoff completed; when a genuine ordinary Auto design answer is needed and independent work is exhausted, ask that one question and preserve the mandate.

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

For every applicable administered application, apply `ADMIN_CONSOLE_STANDARD.md` from Capture to delivery. Capture inventories tenancy and admin roles; Plan produces `ADMIN_ARCHITECTURE.md`, `ADMIN_CAPABILITY_MATRIX.md`, `ADMIN_SETTINGS_REGISTRY.md` and (AI only) `AI_WORKFLOW_CATALOG.md`. Include these in material 20-plan/70-check evidence and in 50-uat only when acceptance was explicitly initiated. Implementation must deliver real UI/API/DB enforcement, not only files. Explicitly initiated UAT tests role-profile switching, tenant isolation and CRUD/configuration/agent flows; Auto retains those cases as documentation and defers execution. Check reports every applicable missing/partial/unverified ability; approved --fix/Auto remediates in scope, with material tenancy/security/production decisions excluded. API-only projects with real admin configuration still require secure administrative capability (API/CLI equivalent) and explicit UI applicability decision; static/no-admin projects may justify N/A.

## Mandatory UX/UI quality overlay

For every UI-applicable lifecycle, apply `PHDK_UX_UI.md` and `PHDK_DESIGN.md` to Plan, Design, Implementation, Integration, UAT/UAT Fix and Check. Plan's UX baseline, journeys and draft design constraints are Design inputs; the selected Design style guide/previews/decision record are required before dependent UI implementation. Explicitly initiated UAT performs an evidenced UX/UI and selected-baseline fidelity audit on the exact deployed candidate, including brownfield regression checks and the P0/P1 quality gate. Snapshot material outputs in 20-plan/25-design/50-uat/60-uat-fix as applicable. Non-visual scope provides evidence-based NOT APPLICABLE. Static concept creation does not grant browser activity outside scoped UAT/UAT Fix.

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
UI_DESIGN_SYSTEM.md         # draft constraints; finalized in Design
UX_UI_DECISIONS.md          # known choices and pending visual decisions
MILESTONE_PLAN.md
IMPLEMENTATION_PLAN.md
ARCHITECTURE_DECISIONS.md   # when material decisions exist
TASK.md                    # execution-plan integration
```

### Historical outputs

Snapshot all material Plan outputs plus `HANDOFF.md`.

### Exit gate

- P0 requirements mapped to target architecture;
- current/target architecture explicit for brownfield;
- migration/convergence steps exist where needed;
- component/data/security/integration boundaries explicit;
- workstream grouping and dependencies are executable;
- unresolved material architecture decisions explicit;
- applicable Design inputs are ready, without pretending a pending visual choice is approved.

### Next stage must verify

Design verifies selected technical stack, content/navigation architecture, audience/tasks, existing brand decisions and draft shared-component/theme constraints. If Design is NOT APPLICABLE, record the reason and proceed to eligible implementation.

Inside Auto, a passing Plan handoff immediately starts/reuses Design for affected UI scope. Normal Auto asks its unresolved visual choices; FORCE selects and continues to stage 30. Missing product code remains required greenfield development, not a reason to stop after planning or request another development command.

---

## 25 — Design

### Purpose

Establish a visible, durable visual style guide and selected interface baseline before affected UI implementation. Follow `PHDK_DESIGN.md`; this is not Designer Mode or UAT.

### Required inputs

- completed/reused Plan handoff and current scope/applicability;
- technical stack, content/navigation architecture, audience/roles and primary journeys;
- existing/draft `UI_DESIGN_SYSTEM.md` and `UX_UI_DECISIONS.md`;
- supplied references, actual existing assets/components and constraints where available.

### Required canonical outputs

- refined `UI_DESIGN_SYSTEM.md` and `UX_UI_DECISIONS.md`, not duplicate design truth documents;
- actual permitted references, concepts and representative previews/editable sources under `docs/design/`;
- mode-correct design gate record with baseline/revision, alternatives, chosen direction, decision provenance, asset paths and visual limitations;
- affected `IMPLEMENTATION_PLAN.md` / `MILESTONE_PLAN.md` and traceability updates.

### Historical outputs

`25-design/HANDOFF.md` plus snapshots of the selected style guide, decisions and material assets or immutable commit-addressed artifact references. Historic completed runs remain untouched. A mutable external preview link alone is insufficient.

### Exit gate

- identity, composition, graphic system and in-context experience have relevant recorded decisions;
- representative screens/critical flow, responsive composition and key states are covered proportionately;
- Auto/standalone Design has actual owner approval or a disclosed owner-accepted specification-only decision;
- Auto Force has `AGENT_SELECTED_AUTO_FORCE` and rationale, with no PHDK owner-approval wait;
- reused authority and exact baseline are current and traceable;
- shared component/token mappings preserve the single palette source and theme contract;
- actual preview visibility/limitations are truthful; concepts are not app/runtime PASS evidence;
- material planning consequences are reconciled; actual owner restrictions remain effective.

### Next stage must verify

PMO/implementation checks the selected baseline, mode-correct decision, applicable assets/components/tokens and linked tasks before affected UI coding. In normal Auto, `DESIGN_AWAITING_OWNER` holds only dependent work; FORCE resolves that PHDK-only wait by choosing and recording. Backend/non-visual work may continue only when genuinely independent and already authorized. Missing visual tooling follows PHDK_DESIGN.md's disclosed specification-only policy, never a fabricated screenshot or approval.

---

## 30 — PMO / Workstreams

### Purpose

Turn the implementation plan into an owner-confirmed workstream portfolio and coordinate workstream execution.

### Required inputs

- completed/reused Plan handoff;
- applicable Design handoff/selected baseline, or evidence-based NOT APPLICABLE;
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
- dependencies explicit, including selected Design baseline for UI work;
- file/component ownership explicit;
- workers completed or residual blockers/deferred state explicit;
- each in-scope commitment has concrete implementation/source evidence or an explicit unfinished blocker; coordination artifacts, assignments and scaffolds alone never prove workstream completion;
- integration queue ready.

### Next stage must verify

Integration Review verifies all expected workstreams have completion evidence and shared/collision surfaces are enumerated. Workers receive only the relevant selected Design slices, not the entire rejected-concept history.

---

## 40 — Integration Review

### Purpose

Turn completed workstreams into one coherent candidate.

### Required inputs

- completed PMO handoff;
- workstream completion evidence;
- current branches/commits/worktree;
- shared ownership/dependency map;
- applicable selected Design baseline and shared-component/token mappings.

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
- selected Design baseline source-fidelity review and explicit deviations, without invented render evidence;
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
- applicable permitted static checks completed; runtime acceptance is deferred until explicit `PHDK uat` on the authorized deployed candidate;
- no hidden unresolved integration collision or unrecorded material design drift.

### Next stage must verify

In Auto/Auto Force, the next applicable SEO/AEO/Check stage verifies `INTEGRATION_REPORT.md` and its candidate; stages 45/50/60 stay deferred. A later explicit `PHDK uat` or `PHDK uat prep` makes this integration evidence an input to Prep. If authorized Prep modifies code/schema, reconcile and deliver the revised candidate with affected permitted static checks, preserving prior historical evidence. Explicit UAT then verifies the deployed revision and required Prep handoff under `PHDK_PRODUCTION_VERIFICATION.md`.

---

## 45 — UAT Prep

**Authorization:** Enter only on explicit `PHDK uat prep` or as the necessary prerequisite of a fresh explicit `PHDK uat`. Auto/Auto Force keep this stage `DEFERRED — OWNER OPT-IN`.

### Purpose

Build and verify synthetic test identities, secure role sessions and fixture readiness **before** browser UAT. Follow `PHDK_UAT_PREP.md` and the governing `PHDK_PRODUCTION_VERIFICATION.md`.

### Inputs

Current integration handoff/candidate, source-backed auth/RBAC/tenancy, Company Co fixture, `JWT_STANDARD.md`, and the existing authorized production target with safe run-owned synthetic isolation.

### Canonical outputs

`UAT_AUTH_PLAN.md`, `UAT_ROLE_MATRIX.md`, `UAT_FIXTURE_MANIFEST.md`, `UAT_PREP_REPORT.md` and applicable source/test implementation.

### Historical outputs

`45-uat-prep/HANDOFF.md` plus sanitized snapshots of canonical outputs; never tokens, passwords or browser storage state.

### Exit and next-stage gate

Evidence of per-role provisioned synthetic identities or exact blockers; legitimate authentication, allow/deny and tenant-boundary verification only in the permitted deployed environment; isolation, expiry and cleanup controls; revision reconciled with Integration after Prep code changes. No local/in-process runtime tests or new environment. UAT checks the same candidate plus the Prep handoff and carries precise blockers forward. The browser readiness check begins **only at explicitly initiated 50 — UAT**. A standalone Prep command stops after its own authorized preparation/delivery outcome; it does not transition into UAT.

---

## 50 — UAT
**Authorization:** Only a fresh explicit owner invocation of `PHDK uat` starts acceptance. Auto/Auto Force keep this stage `DEFERRED — OWNER OPT-IN` and report `UAT NOT RUN`.

**Entry gate:** Within that explicitly initiated UAT, run `UAT_BROWSER_READINESS_STANDARD.md` after required Prep and Integration Review and before the first browser-dependent case, verifying scoped phase authorization and technical browser availability independently. Save evidence/safety/no-new-spend disposition in `UAT_ACCESS_REPORT.md`, summarize in `UAT_REPORT.md`, and retain exact BLOCKED cases if not connected. Missing access does not justify paid API/budget approval or a stop of independent safe acceptance checks.

### Purpose

Validate intent-aligned user acceptance and applicable selected-design fidelity on the integrated deployed candidate.

### Required inputs

- current explicit `PHDK uat` invocation and completed Integration Review handoff;
- verified `45-uat-prep` handoff/role fixtures or documented source-backed N/A, with outstanding per-role blockers;
- exact deployed candidate revision reconciled after Prep changes;
- Capture/Plan/Design traceability and selected previews or disclosed specification-only limitations;
- UAT standard and production-first verification/cleanup controls.

### Required canonical outputs

```text
UAT_CASES.md
UAT_REPORT.md
UX_UI_AUDIT_REPORT.md  # when UI applies
```

### Historical outputs

Snapshot all applicable outputs plus `HANDOFF.md`.

### Exit gate

One of:

- ACCEPTED;
- NOT ACCEPTED with actionable FAILs;
- ACCEPTANCE INCOMPLETE with actionable BLOCKED/MANUAL plan.

No unresolved NOT RUN final cases. A generated concept, owner design approval or agent selection is not evidence of actual rendered behavior, accessibility or successful production cleanup.

### Next stage must verify

Report the acceptance outcome and required next action. UAT Fix enters only on explicit `PHDK uat fix` or authorization within this active explicitly initiated UAT, and verifies the exact report/cases for the same candidate. A report alone does not authorize repair. If no repair is needed, record UAT Fix NOT APPLICABLE in this explicit acceptance run. Subsequent SEO/AEO/Check work follows its own current scope; acceptance failure never reopens a completed Auto development goal.

---

## 60 — UAT Fix

**Authorization:** Enter only on explicit `PHDK uat fix` or authorization within an active explicitly initiated UAT. Auto/Auto Force keep this stage `DEFERRED — OWNER OPT-IN`; old failed reports do not activate it.

### Purpose

Repair UAT failures/removable blockers and provide explicit closure actions for non-removable acceptance gaps.

### Required inputs

- completed UAT handoff;
- UAT report/cases;
- exact candidate/worktree;
- affected selected Design baseline when repairing visual fidelity.

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
- permitted deployed retests executed;
- remaining blockers/manual actions are explicit;
- current UAT conclusion is known.

### Next stage must verify

Any separately authorized downstream work records the latest UAT status without assuming ACCEPTED when acceptance remains incomplete. That status does not retroactively block or reopen completed development. Material new visual direction reopens only affected Design decisions under the current mode; routine fixes to match the selected baseline do not trigger another style interview.

---

## 65 — SEO

### Purpose
After Integration Review in Auto, improve applicable public-site technical SEO and content discoverability on the integrated candidate. No UAT result is a prerequisite.

### Required inputs
- Integration handoff, current candidate, Capture audience/intent, current route map and `PHDK_SEO.md`; include UAT/UAT Fix evidence only when separately authorized and actually available. In Auto, record acceptance `DEFERRED — OWNER OPT-IN`.

### Required canonical outputs
- `SEO_AUDIT_REPORT.md`, `SEO_CHECKLIST.md`, `SEO_REMEDIATION_REPORT.md` (or evidence-based NOT APPLICABLE record).

### Historical outputs
- `65-seo/HANDOFF.md` and snapshots of applicable reports, changes and regression evidence.

### Exit gate
- 25 controls classified with evidence or applicability justified; in-scope fixes and permitted non-UAT checks recorded; critical indexability blockers unresolved only with BLOCKED status. Update acceptance traceability without executing UAT; when a separate active UAT authorizes retests, record those actual results separately.

### Next stage must verify
- AEO/GEO consumes the SEO handoff, public-route indexability baseline and current integrated candidate; no UAT handoff is required in Auto.

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
- 15 controls evidenced/classified; supported corrections checked through permitted non-UAT verification; blocked external measurements not mislabeled PASS. Acceptance remains deferred in Auto; only separately authorized UAT may retest behavioral effects.

### Next stage must verify
- Check validates SEO and AEO/GEO exit gates, or their documented NOT APPLICABLE reasons.

---

## 70 — Check

### Purpose

Audit the resulting repository against all applicable PHDK standards.

### Required inputs

- latest integrated/remediated candidate;
- authorized Capture + Plan + Design + PMO + Integration + SEO + AEO/GEO handoffs or grounded NOT APPLICABLE records;
- acceptance status separately: stages 45/50/60 `DEFERRED — OWNER OPT-IN` in Auto, or real UAT handoffs when explicitly authorized and executed;
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
- applicable Design decision provenance, asset availability, implementation fidelity and current visual evidence distinguished;
- development gaps classified; deferred optional acceptance evidence does not become a development blocker or an implicit UAT task;
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

After verifying remote main, close the local milestone workspace under `PHDK_GIT_WORKSPACE_CLOSEOUT.md`: safe main fast-forward, SHA equality and scoped clean worktree/branch retirement, or explicit BLOCKED / NOT_APPLICABLE_REMOTE_ONLY evidence. Record LOCAL_MAIN/LOCAL_CLEANUP independently of PUBLISHED/DEPLOYED/ACCEPTED; no redundant push to main or deletion of unrelated work.

### Purpose

Complete versioned integration to the requested target and record exactly what shipped.

### Required inputs

- completed/reused authorized development handoffs; deferred stages 45/50/60 require no execution artifacts;
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
- applicable selected Design baseline, decision provenance and residual visual limitations;
- real delivery rejections and their diagnosis, scoped repair, revalidation and retry outcomes when applicable;
- deployment evidence if actually observed, otherwise deployment UNVERIFIED;
- development outcome separately from `UAT NOT RUN` and `DEFERRED — OWNER OPT-IN` in Auto;
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

At every explicit Auto invocation, reread the complete current intent/requirements baseline and reconcile it with actual product source under `PHDK_AUTO.md`. Reuse is the result of this review, not a reason to omit it. Preserve valid code/documents and honor the current authorized scope. Missing required product implementation is pending work, never grounds to mark implementation or Integration NOT APPLICABLE; only intent/scope-based irrelevance justifies N/A. Auto acceptance is `DEFERRED — OWNER OPT-IN`, not REUSED, NOT APPLICABLE or an unfinished prerequisite.

A stage may be marked REUSED only when the next stage verifies:

- required canonical artifacts exist;
- they are coherent with current intent/goal;
- no material upstream change invalidated them;
- historical origin/revision is identifiable;
- claimed implementation and validation have current evidence; a plan or old completion label alone cannot satisfy an implementation/acceptance gate;
- for Design, original decision authority is known and valid for the current mode: normal Auto does not silently treat an agent-only selection as owner approval.

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
5. re-run every authorized downstream development exit gate materially affected by the change. In Auto, keep UAT Prep/UAT/Fix deferred; mark historical acceptance evidence stale without rerunning it or reopening a completed development goal.

Do not silently patch architecture during UAT, replace the selected visual direction during implementation, or rewrite requirements during Check without restoring lifecycle traceability. Apply the current mode's Design decision policy to material visual changes, not a repeated approval for routine fidelity repairs.

# Minimum historical principle

PHDK should preserve enough history that a future assistant/human can answer:

- What did Capture understand at that time?
- What architecture did Plan choose?
- What visual direction did Design select, from which previews, and who actually decided?
- Which workstreams did PMO execute?
- What exactly was integrated?
- Was acceptance deferred, or explicitly invoked with actual UAT accept/fail/block evidence?
- Was UAT Fix explicitly authorized, and what did it repair?
- What did SEO audit, improve and validate?
- What did AEO/GEO verify and improve without fabricating AI visibility?
- What standards gaps did Check find?
- What remediation happened?
- What version/commit/PR was finally delivered?

If the repo cannot answer those questions from versioned artifacts, the lifecycle handoff is incomplete.
