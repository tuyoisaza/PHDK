**Production-first verification (v2.58.0):** [PHDK_PRODUCTION_VERIFICATION.md](PHDK_PRODUCTION_VERIFICATION.md) governs all modes: local static checks/builds only; no local behavioral tests, Docker, new staging/databases; versioned UAT with uniquely run-owned synthetic fixtures on existing production and verified cleanup.

# PHDK

**Risk-based multi-tenant security (v2.59.0):** [PHDK_TENANT_RISK_STANDARD.md](PHDK_TENANT_RISK_STANDARD.md) requires consultative exposure/impact assessment before choosing a tenant security architecture. Capture/Plan ask only unresolved material questions one at a time; baseline isolation and sensitive-data encryption are mandatory, while per-tenant databases, field-level encryption, managed keys and dedicated infrastructure scale with assessed and owner-approved risk. UAT/Check demand permitted synthetic negative-boundary evidence; this does not authorize infrastructure changes or local behavioral tests.


**Intelligent execution (since v2.57.0):** [PHDK_INTELLIGENT_EXECUTION.md](PHDK_INTELLIGENT_EXECUTION.md) permits bounded in-session delegation in any mode when host-supported, keeps PMO for portfolio governance, and routes context progressively by mode, stage, task and specialist. Worker handoffs do not replace primary-agent integration and delivery.

**Milestone delivery model (v2.56.0):** `PHDK plan` now creates `MILESTONE_PLAN.md`; PMO executes workstreams inside value milestones; Auto/Auto Force version and merge each completed milestone to verified `main` before continuing; final UAT creates milestone-to-user-story acceptance traceability. See [`PHDK_PROJECT_MANAGEMENT_STANDARD.md`](PHDK_PROJECT_MANAGEMENT_STANDARD.md).

**Evolution and maintainer session standard:** [PHDK_EVOLUTION_STANDARD.md](PHDK_EVOLUTION_STANDARD.md) defines consistent PHDK naming, per-session repository refresh, workspace/branch ownership, SemVer, release coherence and verifiable publication. This is a guide for maintaining PHDK itself; it does not activate Auto or authorize unattended changes.

**`PHDK auto force` and durable Auto continuity:** [PHDK_AUTO_CONTINUITY.md](PHDK_AUTO_CONTINUITY.md) makes PHDK-only human reviews non-blocking immediately, without preventive review/protection investigation. Auto keeps the scoped user mandate through context compaction, runs mandatory checks without repeated permission, and repairs/retries actual delivery failures before reporting a remaining blocker.

**New `PHDK uat prep` (v2.53.0):** [`PHDK_UAT_PREP.md`](PHDK_UAT_PREP.md) defines a standalone implementation command and required stage 45 in Auto. It **builds/repairs and provisions permitted non-production synthetic Company Co role accounts**, repeatable seeders, trusted server/provider-issued test sessions and local role/tenant verification; produces fixture/role/auth/prep evidence before UAT. Prep is **not** browser testing or permission for production privileged logins; stage 50 still independently verifies browser access.

**Synthetic UAT identity and JWT policy (v2.52.2):** Read [`JWT_STANDARD.md`](JWT_STANDARD.md) before authenticated UAT, UAT Fix, Auto UAT or Check. Authenticate fictional Company Co roles through a supported **non-production** provider/session/bootstrap; signed, scoped short-lived JWTs are used only by products that actually use JWT. Never ask for people's passwords/bearer tokens, forge production admin access or equate a synthetic role label with authentication. Prove all role and tenant boundaries in actual permitted browser/API journeys, and revoke temporary test sessions.

**Company Co demo/UAT fixture (vendored since v2.50.5):** Before UAT that needs employees, area leaders, role test accounts, customers, buyers, suppliers, products or workflows, read [`USE_COMPANY_CO_INFO_FOR_DEMOS.md`](USE_COMPANY_CO_INFO_FOR_DEMOS.md). Adapt its synthetic 200-person / 17-department company to the real application model, seed idempotently, verify created accounts, and test role-scoped user journeys including auditable Superadmin profile switching. Never perform automatic bulk email to `@tujuisasa.com`; obtain authorization and verify routing first. Record evidence and the next executable action.


**UAT browser readiness (v2.51.6):** The [UAT Browser Readiness and Cost Guard](UAT_BROWSER_READINESS_STANDARD.md) verifies both phase-scoped permission and actual connected browser on every UAT/UAT Fix entry, without inventing paid workarounds or budget requests. Browser-dependent cases remain BLOCKED until real evidence exists; independent acceptance proceeds.

**UAT profile journeys (v2.50.5):** `UAT_JOURNEY_STANDARD.md` requires code-backed role inventory, safe test users, auditable Superadmin role switching, intent-aligned stories per profile, executable step-by-step journeys, CRUD/UX/auth evidence, UAT Fix + Re-UAT and a concise copy-paste-ready `SIGUIENTE PASO` in every stage/blocker response.


**Project Handoff to Development Kit**  
**Version v2.59.0**

PHDK is an operating system for AI-assisted software delivery.

**Outcome-Driven Operator (v2.50.7):** All PHDK modes follow [PHDK_COMMUNICATION_STANDARD.md](PHDK_COMMUNICATION_STANDARD.md): concise mode/version/progress/git/publication/next-action reporting, end-to-end completion ownership, and suppression of recurring optional external-skill promotions (while preserving required notices and real safety/review gates).

It turns a repository, an idea, or an unfinished product into a structured development process where AI can **understand intent, coordinate work, build autonomously, validate behavior, repair gaps, and check compliance** without losing human control.

PHDK is designed for teams and builders who want more than “vibe coding”: they want AI development that is **traceable, repeatable, governable, and aligned with what the product is actually supposed to do**.

---

## The problem PHDK solves

AI coding tools are powerful, but real software projects break down when:

- requirements live only in chat history;
- different sessions understand the product differently;
- multiple fronts advance without coordination;
- agents stop after partial milestones and wait for another “OK”;
- tests prove code runs but not that the product satisfies its intent;
- UAT reports problems without telling you how to close them;
- standards drift from what the repository actually implements;
- different agents change shared files, versions, schemas, or navigation without integration discipline;
- nobody can answer: **What are we building, why, what is done, what is blocked, and what should happen next?**

PHDK gives AI a shared operating model for answering those questions.

---

# One lifecycle from idea to aligned repository

For a multi-workstream project:

```text
PHDK capture
    ↓
PHDK plan
    ↓
PHDK PMO
    ↓
confirm workstreams
    ↓
PMO workers using Auto execution semantics
    ↓
PMO Integration Review
    ↓
assistant integrated diff review; actual owner/host controls
    ↓
PHDK uat prep
    ↓
PHDK uat
    ↓
PHDK uat fix
    ↓
PHDK check
    ↓
approved remediation
    ↓
Done
```

For a single focused workstream, either run the stages explicitly:

```text
PHDK capture → PHDK plan → implementation/integration → PHDK uat prep → PHDK uat → PHDK uat fix → SEO → AEO/GEO → PHDK check
```

or simply run:

```text
PHDK auto
```

Every Auto invocation revalidates the complete intent/requirements baseline against actual code, then executes the complete authorized lifecycle. It reuses Capture/Plan artifacts only after verifying their currency and coverage, builds missing product code, and completes partial implementations.

Each stage has one job.

| Stage | Purpose |
|---|---|
| **Capture** | Understand the product, its intent, ethos, requirements, users, constraints and success criteria. |
| **Plan** | Design or reconstruct the solution/repository/UX architecture and turn it into an executable implementation plan. |
| **PMO** | Detect and coordinate multiple fronts, dependencies, ownership, workers and integration. |
| **Auto** | Revalidate intent against code, execute the entire authorized development scope, then validate, repair and deliver. |
| **Auto Force** | Execute Auto with PHDK-only human reviews non-blocking from entry; retain the mandate and repair/retry actual delivery failures. |
| **UX/UI** | Plan usable journeys and coherent interfaces for new projects or redesigns; audit real usage and fix critical friction before UAT acceptance. |
| **UAT Prep** | Build and verify the permitted synthetic accounts, fixtures and authentication bootstrap needed for UAT. |
| **UAT** | Validate the integrated product against intent-aligned user stories and acceptance criteria. |
| **UAT Fix** | Repair FAILs and removable blockers; guide the owner through manual/external blockers. |
| **SEO** | After UAT, audit and improve public crawlability, metadata, content, structure and performance with 25 evidence-classified controls. |
| **AEO/GEO** | After SEO, improve factual answer visibility, entity clarity and source credibility without promising AI placement. |
| **CRUD governance** | Inventory mutable resources and enforce role-specific create, list/detail, update and delete capabilities, with justified restrictions and authorization tests. |
| **Check** | Compare the repository against the applicable PHDK standards and produce a remediation backlog. |

---

# Before every command: PHDK Preflight

Every lifecycle command starts by checking its own operating environment.

PHDK verifies:

- that PHDK is actually installed for the current repo/tool;
- installed vs canonical PHDK version;
- manifest completeness and managed instruction block;
- which recommended skills/capabilities are relevant to the stage;
- which of those capabilities are actually installed or connected;
- whether the user explicitly asked PHDK not to use skills/plugins/connectors.

When PHDK is stale and its owned standards surface is clean, Preflight automatically synchronizes clean standards from canonical main before continuing. It never silently force-overwrites dirty PHDK files.

When a relevant recommended skill is already available, PHDK should **actually use it**. A URL in the registry is not treated as an installed skill.

Missing optional skills do not block the lifecycle. Important missing capabilities are surfaced when they materially affect quality; installation/connection still follows the host tool's required consent flow.

Full contract: [PHDK_PREFLIGHT.md](PHDK_PREFLIGHT.md). Recommended capability registry: [SKILLS_REGISTRY.md](SKILLS_REGISTRY.md).

---

# Lifecycle deliverables and historical handoffs

PHDK stages do not communicate only through chat. Each stage must leave a durable handoff package in the repository, and the next stage must validate that package before it starts.

Current lifecycle state lives in:

```text
PHDK_LIFECYCLE_STATUS.md
```

Every full run also gets an immutable historical folder:

```text
docs/phdk/lifecycle/<run-id>/
```

Typical structure:

```text
00-preflight/
10-capture/
20-plan/
30-pmo/
40-integration/
50-uat/
60-uat-fix/
65-seo/
67-aeo-geo/
70-check/
80-remediation/
90-delivery/
```

Every stage folder contains a mandatory `HANDOFF.md` plus snapshots of the stage outputs that materially define that handoff.

| Stage | Required canonical deliverables |
|---|---|
| **Preflight** | `PHDK_PREFLIGHT_REPORT.md` |
| **Capture** | `PROJECT_INTENT.md`, `PROJECT_BRIEF.md`, `PRD.md`, `FEATURES.md`, `REQUIREMENTS_TRACEABILITY.md` |
| **Plan** | `SOLUTION_ARCHITECTURE.md`, `REPOSITORY_ARCHITECTURE.md`, `UX_ARCHITECTURE.md`, `UX_RESEARCH_BASELINE.md`, `UX_JOURNEYS.md`, `UI_DESIGN_SYSTEM.md`, `UX_UI_DECISIONS.md`, `IMPLEMENTATION_PLAN.md`, architecture decisions, `TASK.md` integration |
| **PMO / Workstreams** | `PMO.md`, `PMO_WORKSTREAMS.md`, `PMO_DEPENDENCIES.md`, `PMO_STATUS.md` |
| **Integration Review** | `INTEGRATION_REPORT.md` |
| **UAT** | `UAT_CASES.md`, `UAT_REPORT.md`, `UX_UI_AUDIT_REPORT.md` (UI projects) |
| **UAT Fix** | `UAT_REMEDIATION.md`, `UX_UI_REMEDIATION_REPORT.md` (when applicable), plus updated UAT artifacts |
| **SEO** | `SEO_AUDIT_REPORT.md`, `SEO_CHECKLIST.md`, `SEO_REMEDIATION_REPORT.md` (or justified N/A) |
| **AEO/GEO** | `AEO_GEO_AUDIT_REPORT.md`, `AEO_GEO_CHECKLIST.md`, `AEO_GEO_REMEDIATION_REPORT.md` (or justified N/A) |
| **Check** | `PHDK_CHECK_REPORT.md` |
| **Remediation** | `PHDK_REMEDIATION_REPORT.md` plus updated Check report |
| **Delivery** | `DELIVERY_REPORT.md` |

Before moving forward, each stage verifies that the upstream handoff exists, passed its exit gate, and still applies to the current goal/candidate.

If a later stage discovers that an upstream artifact is wrong or stale, PHDK reopens that upstream stage and then revalidates every materially affected downstream stage.

Full contract: [PHDK_LIFECYCLE.md](PHDK_LIFECYCLE.md).

---

# Core commands

## `PHDK capture`

Turn an idea or an existing repository into a professional product baseline.

Capture investigates first and asks only what it still needs to know.

On an existing project, it reads:

- product documentation;
- code and routes;
- domain models and APIs;
- tests;
- configuration;
- intents;
- architecture decisions;
- current task/status;
- relevant product history.

It separates:

- **stated intent**;
- **implemented behavior**;
- **inferred requirements**;
- **legacy or accidental behavior**;
- **open decisions**.

It produces:

```text
PROJECT_INTENT.md
PROJECT_BRIEF.md
PRD.md
FEATURES.md
REQUIREMENTS_TRACEABILITY.md
```

If Capture has no material questions, it says so. If information is missing, it asks focused questions until the requirements baseline is coherent.

At completion it tells you exactly where everything was captured so you can review it.

---

## Universal administration console (v2.51.4)

`ADMIN_CONSOLE_STANDARD.md` requires an actual, protected **Configuración / Settings** console for every applicable administered portal. First establish `single_tenant` (one elevated admin) vs `multi_tenant` (platform super_admin and tenant-scoped admins), recommending multi-tenancy when justified without silently migrating existing data. Verify and build real user/invitation/role/permission administration, tenant lifecycle where applicable, native locale, safe debug/integrations/secrets-status, backups/audit/security/observability, shared theme templates and auditable administrator role testing. In AI products, **Prompts** must show each agent's business purpose, callsite, approved DB/API inputs, versioned prompts, JSON output schema and destination/next-agent workflow graph. Check demands UI + API + persistence + negative-permission tests, not placeholder tabs.

`PHDK check` remains an evidence-backed read-only audit plus one remediation question. To request a complete authorized audit **and safe implementation in one command**, use `PHDK check --fix`. The authorized `PHDK auto` also repairs applicable in-scope gaps; unknown tenancy, sensitive permissions, live destructive operations and external credentials require their own decision/authorization.

## Automation and cost hygiene (v2.51.5)

Every `PHDK check` and the final Check of `PHDK auto` follows [PHDK_AUTOMATION_HYGIENE.md](PHDK_AUTOMATION_HYGIENE.md): identify leftover PHDK-managed GitHub Actions, agents, schedules, watcher/reload loops, Railway cron/restart storms and CI waiting blocks. Compare source evidence with **actual read-only GitHub/Railway state**, preserve valid required checks and GitHub→Railway autodeploy, and record unavailable provider evidence as UNVERIFIED. The vendored static collector `scripts/phdk_automation_audit.py` helps surface source risks but cannot prove remote workflows are inactive. Provider setting changes are not silently authorized.

## Canonical PHDK Design System

`PHDK_DESIGN_SYSTEM.md` mandates shared shadcn-compatible components, Radix overlay primitives, semantic Tailwind tokens, Motion transitions, consistent Lucide icons, light/dark/corporate color themes and applicable en/es/pt translation catalogs. On entering Designer Mode, inspect the actual stack and document `DESIGN_SYSTEM_READINESS.md`, prepare missing safe prerequisites, then recommend and implement redesigns. The source of truth is vendored to downstream projects.

## Theme tokens and Superadmin template editing

[PHDK_THEME_STANDARD.md](PHDK_THEME_STANDARD.md) requires one canonical semantic CSS token stylesheet for light/dark/corporate, no hardcoded palette colors in UI components, and **Superadmin → Configuración → Edición de templates** with persisted editing, previews and a corporate show/hide switch. [scripts/phdk_theme_audit.py](scripts/phdk_theme_audit.py) supplies a vendorable static check for Designer Mode and PHDK Check; source, permission, persistence and theme-switching tests still supply functional evidence.

## Verified completion gate

After a remote-main delivery, `PHDK_COMPLETION_GATE.md` defines truthful machine-readable QA and remote SHA/version evidence. The vendored `scripts/phdk_completion_gate.py` rejects unsupported completion claims; PR state and task scope remain separately audited.

## `PHDK designer mode`

This explicit mode audits an existing interface, selects a visual direction and implements a redesign, verifying the result through scoped UAT where permitted. See `PHDK_DESIGNER_MODE.md`.

## `PHDK plan`

Turn requirements into architecture and an executable delivery plan.

```text
PHDK plan
```

Plan works in two modes:

- **Greenfield** — design the target architecture from requirements and applicable PHDK standards.
- **Brownfield** — read the architecture that already exists, preserve sound decisions, identify gaps/debt, define a target state and produce an incremental convergence plan.

Plan covers:

- solution/system architecture;
- repository topology (mono/polyrepo and package boundaries);
- web/API/service boundaries;
- PostgreSQL/data ownership when applicable;
- integrations and external dependencies;
- auth/security boundaries;
- AI architecture when applicable;
- testing/observability architecture;
- conceptual UX/information architecture;
- dependency ordering and workstream decomposition.

It creates or updates:

```text
SOLUTION_ARCHITECTURE.md
REPOSITORY_ARCHITECTURE.md
UX_ARCHITECTURE.md
MILESTONE_PLAN.md
IMPLEMENTATION_PLAN.md
ARCHITECTURE_DECISIONS.md
TASK.md
```

On an existing repo, Plan **does not reset the project to a default scaffold**. It starts from current reality and recommends the smallest coherent path from current state to target state.

Full procedure: [PHDK_PLAN.md](PHDK_PLAN.md).


Plan now creates a value-based milestone roadmap under [PHDK_PROJECT_MANAGEMENT_STANDARD.md](PHDK_PROJECT_MANAGEMENT_STANDARD.md). In Auto/Auto Force, a completed milestone is technically verified, versioned, committed with the version prefix, merged through the normal PR route to `main`, remotely verified, and then execution continues from that new main. Lifecycle stage boundaries and internal slices do not trigger releases. Final UAT reads those milestones and builds milestone → user story → acceptance-case evidence.

---

## `PHDK PMO`

Coordinate multiple active fronts of the same project.

PMO reads the Capture baseline, requirements, current plans, code, branches/PRs, UAT and Check evidence, then identifies candidate workstreams.

Example:

```text
WS-001 — Product import reconciliation
WS-002 — Opportunity Radar
WS-003 — Commercial Email Copilot
WS-004 — AI prompt administration
```

It asks you once to confirm, add, remove or reprioritize the active portfolio.

Then it manages:

- dependencies;
- ownership;
- shared files;
- collision risk;
- workstream status;
- branches/worktrees;
- integration readiness;
- blockers;
- cross-workstream decisions.

PMO maintains:

```text
PMO.md
PMO_WORKSTREAMS.md
PMO_DEPENDENCIES.md
PMO_STATUS.md
```

When the runtime supports workers/subagents, **any PHDK mode may delegate bounded in-session tasks under `PHDK_INTELLIGENT_EXECUTION.md`**. PMO remains responsible for portfolio workstreams and their integration.

Workers:

- receive one confirmed workstream;
- use Auto semantics inside that scope;
- cannot recursively delegate;
- cannot choose new work;
- cannot independently finalize global integration.

The PMO orchestrator owns shared integration and the final candidate.

If the runtime does not support workers, PMO coordinates the workstreams sequentially and says so explicitly.

---

## `PHDK auto`

Run the complete PHDK delivery lifecycle for one authorized goal.

```text
PHDK auto
```

Auto now orchestrates:

```text
Capture
→ Plan
→ PMO/workstream execution
→ PMO Integration Review
→ UAT Prep
→ UAT
→ UAT Fix
→ SEO
→ AEO/GEO
→ Check
→ in-scope Check remediation
→ delivery
```

On every invocation, Auto rereads the complete intent and requirements baseline and compares it with actual product code. It reuses Capture/Plan artifacts only after verifying that they are current and cover the authorized goal.

If no product code exists, Auto builds the product. If code is partial, it completes the missing requirements while preserving valid implementation and architecture. Documentation or a scaffold alone does not establish a completed application; unavailable repository access is recorded as UNVERIFIED, never treated as an empty project.

**Plan continues directly into implementation in the same Auto invocation.** Auto executes the entire authorized scope without another development command, a ceremonial approval, or a silent reduction to an MVP. Real blockers remain explicit, and independent authorized work continues. Updating or installing PHDK does not activate Auto.

PMO still has a distinct role:

- **PMO** is the workstream coordination engine.
- **Auto** is the end-to-end lifecycle orchestrator that can invoke PMO as one stage.

PMO workers use Auto-style execution semantics for their assigned workstream, but they do not recursively activate the full Auto lifecycle.

## `PHDK auto force`

Use the same complete lifecycle while explicitly removing human-review stops imposed only by PHDK:

```text
PHDK auto force
```

PHDK records those gates as `NON_BLOCKING_BY_MODE` immediately. It does not investigate whether they block, query review/protection requirements preventively, or seek reviewers/approvals. It reviews the diff itself, runs the applicable mandatory checks, pushes the branch, opens/updates the PR, merges and reads back remote `main`. Mandatory local suites such as `pnpm test` required by a pre-push hook are included in the scoped implementation authorization.

When a real hook/tool/GitHub operation rejects delivery, PHDK reports the rejection, investigates that concrete cause, repairs it within scope, revalidates and retries the affected push/PR/merge. It keeps the mandate and completes independent work. It does not repeat unchanged rejected writes or evade controls with force-pushes, disabled hooks, alternate credentials/transports or provider-setting changes. Real current owner/host restrictions remain effective.

Both Auto variants preserve mandate provenance, scope/target/restrictions, progress and next action in `docs/phdk/lifecycle/<run-id>/AUTO_STATE.json`. Context recovery reloads that evidence with the current user instructions; missing/malformed state is reconstructed internally. The file is no new permission and does not activate another conversation. Every Auto update states the true mandate and next action, then executes the eligible action in the same turn. Completion, a user stop or a real remaining blocker is reported as its actual state.

The canonical contract and supported continuation aid are [PHDK_AUTO_CONTINUITY.md](PHDK_AUTO_CONTINUITY.md) and [scripts/phdk_auto_gate.py](scripts/phdk_auto_gate.py). Updating or discussing these standards does not activate Auto or AUTO FORCE.

---

## `PHDK uat`

Run intent-aligned user acceptance testing.

UAT starts from the product’s captured intent and requirements.

Its traceability chain is:

```text
Project Intent
    ↓
User Story
    ↓
Requirement / Acceptance Criterion
    ↓
UAT Case
    ↓
Evidence
```

It creates:

```text
UAT_CASES.md
UAT_REPORT.md
```

Results are classified as:

- **PASS**
- **FAIL**
- **BLOCKED**
- **MANUAL**
- **NOT APPLICABLE**

The final conclusion is one of:

- **ACCEPTED**
- **NOT ACCEPTED**
- **ACCEPTANCE INCOMPLETE**

UAT never converts code inspection into a behavioral PASS.

---

## `PHDK uat fix`

Turn an incomplete UAT report into an action plan and repair loop.

```text
PHDK uat fix
```

For every unresolved FAIL, BLOCKED or MANUAL case, PHDK explains:

- what prevents acceptance;
- why it matters;
- who or what must act;
- where;
- how;
- in what order;
- what evidence closes the case;
- what to rerun next;
- whether PHDK can solve it now.

If a blocker is repository-local — for example a missing fixture, fake adapter, auth stub or in-process harness — PHDK should build the smallest permitted harness and rerun the case.

If a blocker genuinely requires an unavailable browser environment, external account, provider setting, secret, actual current-owner/host review or other excluded action, PHDK gives the owner an explicit checklist instead of simply saying “BLOCKED”.

---

## SEO and AEO/GEO — after UAT

On relevant public sites, Auto executes `PHDK_SEO.md` to audit and implement safe SEO corrections, then `PHDK_AEO_GEO.md` to improve factual answer clarity and citation-readiness. Both stages record evidence and historical handoffs; entirely private projects are marked NOT APPLICABLE with justification. Neither stage grants unapproved production/browser/provider access or guarantees rankings or AI citations.

---

## `PHDK check`

Measure the gap between the repository and the applicable PHDK standards.

```text
PHDK check
```

Check reads the standards and first determines **which ones actually apply** based on product intent.

It produces a compliance/remediation report with findings such as:

- **COMPLIANT**
- **GAP**
- **PARTIAL**
- **NOT APPLICABLE**
- **UNKNOWN / DECISION NEEDED**
- **UNVERIFIED**

It also classifies remediation as:

- **AUTO-FIXABLE**
- **FIXABLE WITH VALIDATION**
- **DECISION REQUIRED**
- **EXTERNAL / MANUAL**

The first Check pass is an audit.

After presenting the gap list, PHDK asks whether you want the fixable items executed.

A yes authorizes only the enumerated remediation backlog.

---

# Standards that activate only when relevant

PHDK is conditional, not bureaucratic.

It does not add features simply because a standard exists.

Examples:

- no RBAC requirement for a product that genuinely has no roles;
- no AI infrastructure for a project that does not use AI;
- no migration requirement when there is no schema change;
- no PMO overhead for a single simple workstream.

The project’s **intent and requirements determine applicability**.

---

# AI-native project support

When a project actually uses an LLM provider such as Anthropic, OpenAI, Gemini/Google or another configured model provider, PHDK activates additional AI standards.

AI integrations are expected to have:

- centralized provider access through `packages/ai` or equivalent;
- configurable provider/model;
- prompt injection defenses;
- structured output validation;
- token and cost observability;
- usage attribution;
- rate/cost safeguards;
- kill switches;
- admin-manageable prompts.

For AI-bearing products, the super-admin area includes:

### Prompts

A dedicated Prompts interface with:

- left-side prompt/agent list;
- editable **Name**;
- editable **Personality prompt**;
- editable **Execution prompt**;
- editable **Output JSON schema**;
- revisions and audit history;
- stable prompt/agent identity.

### AI consumption

Usage and cost evidence attributable to:

- provider;
- model;
- feature/workflow;
- prompt/agent;
- prompt revision;
- tokens;
- cost;
- latency;
- error state.

Projects without AI do not receive these requirements.

---

# Human control remains central

PHDK is designed for autonomous execution **inside explicit human direction**.

Humans remain responsible for:

- product intent;
- portfolio/workstream selection;
- material product decisions;
- sensitive policy choices;
- actual current-owner/host formal approval requirements;
- external/manual actions PHDK cannot perform.

PHDK eliminates repetitive approval loops. It does not eliminate accountability.

In AUTO FORCE, PHDK-only human-review requirements are non-blocking from entry; no preventive review/protection investigation is added. The assistant still reviews its diff and performs required checks, handles actual delivery rejections and reports verified results.

---

# Safety and delivery boundaries

PHDK keeps strong execution boundaries.

By default:

- no unattended or overnight execution;
- no scheduled agent loops;
- no recurring autonomous jobs;
- no browser/headless verification outside scoped UAT/UAT Fix in local/staging environments by default;
- no live database mutation;
- no secret-value inspection;
- no provider administration from ordinary development commands;
- no bypass of hooks, protections or actual current-owner/host review requirements; AUTO FORCE skips only PHDK-imposed human gates.

PMO portfolio workers operate only in an active PMO session on confirmed workstreams. Other PHDK modes may use bounded in-session task workers under `PHDK_INTELLIGENT_EXECUTION.md` without activating PMO.

---

# Keep PHDK synchronized

## Conservative upgrade

```text
PHDK upgrade
```

Updates PHDK standards conservatively.

If PHDK-owned files have local edits, it reports the conflict instead of overwriting them.

## Authoritative standards refresh

```text
PHDK upgrade force
```

Replaces only the PHDK-owned surface with canonical upstream:

- manifest-owned files under `phdk-standards/`;
- exact `PHDK-MANAGED` blocks;
- obsolete files proven to have been PHDK-owned by the previous manifest.

It does **not** overwrite product code, project requirements, intents, TASK/STATUS, ADRs, hooks, package files, provider settings or owner instructions outside managed markers.

---

# Other operational commands

## `PHDK unlock`

Diagnose and reconcile documentary PHDK blockers while preserving real hooks, protections, reviews, access and security controls.

## `PHDK Developer Mode`

A narrow temporary direct-main workflow for eligible small, low-risk tasks when explicitly activated.

It is separate from Auto and PMO.

---

# How to start

### New project

For maximum control, run the stages explicitly:

```text
PHDK capture
PHDK plan
PHDK PMO
```

Then continue through UAT/Check as needed.

For end-to-end execution, simply run:

```text
PHDK auto
```

Auto will revalidate the complete intent/requirements baseline against code, create or reuse verified Capture/Plan outputs, execute the required development, coordinate workstreams, integrate, prepare synthetic UAT access, validate, repair and deliver the final candidate.

Auto also tells you **where it is in the lifecycle**. At startup it shows a status board for:

```text
Preflight
Capture
Plan
PMO / Workstreams
Integration Review
UAT Prep
UAT
UAT Fix
SEO
AEO/GEO
Check
Remediation
Delivery
```

Each stage is marked `PENDING`, `RUNNING`, `REUSED`, `COMPLETED`, `BLOCKED`, or `NOT APPLICABLE`. When Auto moves to another stage, it reports what just closed, the strongest artifact/evidence, what is running now, and what comes next. If you invoke Auto without naming one delivery and the repo already reveals several parallel fronts, Auto enters PMO discovery, shows you the detected portfolio and asks you to confirm/add/remove/reprioritize those workstreams instead of forcing you to choose one arbitrary task.

### Existing project

Run:

```text
PHDK upgrade
PHDK capture
PHDK plan
```

Capture reconstructs what the product is supposed to be. Plan reconstructs how it is currently built, then defines the target architecture and an incremental convergence path.

Or run `PHDK auto`: it revalidates the complete baseline on every invocation, refreshes missing/outdated artifacts, and continues through all authorized implementation and delivery.

### Existing project with unclear standards drift

Run:

```text
PHDK check
```

to understand the compliance gap.

---

# The PHDK philosophy

PHDK is built around a few simple ideas:

1. **Intent before implementation.**
2. **Requirements should survive chat sessions.**
3. **AI should finish authorized work instead of repeatedly asking to continue.**
4. **Parallel work needs ownership, dependencies and integration discipline.**
5. **Acceptance should test what users need, not merely what code exists.**
6. **A failed or blocked UAT case should always have a next action.**
7. **Standards should adapt to the product, not force irrelevant features.**
8. **Autonomy should increase execution speed without reducing accountability.**
9. **Every important result should be traceable to evidence.**
10. **The repository should become the durable memory of the project.**

---

# Documentation map

| Need | Read |
|---|---|
| PHDK maintainer sessions and evolution | [PHDK_EVOLUTION_STANDARD.md](PHDK_EVOLUTION_STANDARD.md) |
| Execution boundaries | [EXECUTION_SCOPE.md](EXECUTION_SCOPE.md) |
| Universal command preflight | [PHDK_PREFLIGHT.md](PHDK_PREFLIGHT.md) |
| Lifecycle stage contracts & historical handoffs | [PHDK_LIFECYCLE.md](PHDK_LIFECYCLE.md) |
| Recommended skills/capabilities | [SKILLS_REGISTRY.md](SKILLS_REGISTRY.md) |
| Professional requirements capture | [PHDK_CAPTURE.md](PHDK_CAPTURE.md) |
| Solution architecture & implementation planning | [PHDK_PLAN.md](PHDK_PLAN.md) |
| Multi-workstream orchestration | [PHDK_PMO.md](PHDK_PMO.md) |
| Autonomous single-goal development | [PHDK_AUTO.md](PHDK_AUTO.md) |
| Auto Force, mandate continuity and delivery repair/retry | [PHDK_AUTO_CONTINUITY.md](PHDK_AUTO_CONTINUITY.md) |
| UAT and UAT repair | [UAT_STANDARD.md](UAT_STANDARD.md) |
| Standards compliance | [PHDK_CHECK.md](PHDK_CHECK.md) |
| Normal delivery to main | [MAIN_DELIVERY_STANDARD.md](MAIN_DELIVERY_STANDARD.md) |
| AI administration | [AI_ADMIN_STANDARD.md](AI_ADMIN_STANDARD.md) |
| Testing | [TESTING_STANDARD.md](TESTING_STANDARD.md) |
| Security | [DEVSECOPS.md](DEVSECOPS.md) |
| Versioning | [VERSIONING.md](VERSIONING.md) |
| Upgrade | [PHDK_UPGRADE.md](PHDK_UPGRADE.md) |
| Change management & releases | [CHANGE_MANAGEMENT.md](CHANGE_MANAGEMENT.md) |
| Technical release history | [CHANGELOG.md](CHANGELOG.md) |

---

# Installation

PHDK can be vendored into an existing repository under `phdk-standards/` using the mappings in `PHDK_MANIFEST.txt`, with the appropriate `PHDK-MANAGED` block added to the active coding tool’s native instruction file.

Common project-local locations include:

| Tool | PHDK skill location |
|---|---|
| Claude Code | `.claude/skills/phdk` |
| Cursor | `.cursor/skills/phdk` |
| Codex CLI / Antigravity | `.agents/skills/phdk` |
| Windsurf | `.windsurf/skills/phdk` |
| VS Code / GitHub Copilot | `.github/skills/phdk` |
| OpenCode | `.opencode/skills/phdk` |
| Pi | `.pi/skills/phdk` |

Use the installation path for the tool you actually use. PHDK does not require background updaters, schedulers or CI agents.

---

# Project status

PHDK is actively evolving.

The README intentionally describes **what PHDK is and how to use it**, not the release-by-release history.

For release notes, migrations and historical changes, see:

- [CHANGE_MANAGEMENT.md](CHANGE_MANAGEMENT.md)
- [CHANGELOG.md](CHANGELOG.md)
