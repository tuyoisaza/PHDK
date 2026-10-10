# PHDK

**Project Handoff to Development Kit**  
**Version v2.44.2**

PHDK is an operating system for AI-assisted software delivery.

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
human integrated review when requested or required
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
PHDK capture → PHDK plan → implementation/integration → PHDK uat → PHDK uat fix → PHDK check
```

or simply run:

```text
PHDK auto
```

Auto will orchestrate the complete applicable lifecycle and reuse current Capture/Plan artifacts.

Each stage has one job.

| Stage | Purpose |
|---|---|
| **Capture** | Understand the product, its intent, ethos, requirements, users, constraints and success criteria. |
| **Plan** | Design or reconstruct the solution/repository/UX architecture and turn it into an executable implementation plan. |
| **PMO** | Detect and coordinate multiple fronts, dependencies, ownership, workers and integration. |
| **Auto** | Orchestrate the complete lifecycle from Capture through final Check/remediation and delivery. |
| **UAT** | Validate the integrated product against intent-aligned user stories and acceptance criteria. |
| **UAT Fix** | Repair FAILs and removable blockers; guide the owner through manual/external blockers. |
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

When PHDK is stale and its owned standards surface is clean, Preflight may synchronize the standards before continuing. It never silently force-overwrites dirty PHDK files.

When a relevant recommended skill is already available, PHDK should **actually use it**. A URL in the registry is not treated as an installed skill.

Missing optional skills do not block the lifecycle. Important missing capabilities are surfaced when they materially affect quality; installation/connection still follows the host tool's required consent flow.

Full contract: [PHDK_PREFLIGHT.md](PHDK_PREFLIGHT.md). Recommended capability registry: [SKILLS_REGISTRY.md](SKILLS_REGISTRY.md).

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
IMPLEMENTATION_PLAN.md
ARCHITECTURE_DECISIONS.md
TASK.md
```

On an existing repo, Plan **does not reset the project to a default scaffold**. It starts from current reality and recommends the smallest coherent path from current state to target state.

Full procedure: [PHDK_PLAN.md](PHDK_PLAN.md).

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

When the runtime supports workers/subagents, **PMO is the only PHDK mode allowed to delegate workstreams**.

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
→ UAT
→ UAT Fix
→ Check
→ in-scope Check remediation
→ delivery
```

If Capture or Plan is already current, Auto reuses it rather than repeating work.

If the repo already exists, Auto's Plan stage operates in brownfield mode: it understands the current architecture before proposing or executing convergence.

PMO still has a distinct role:

- **PMO** is the workstream coordination engine.
- **Auto** is the end-to-end lifecycle orchestrator that can invoke PMO as one stage.

PMO workers use Auto-style execution semantics for their assigned workstream, but they do not recursively activate the full Auto lifecycle.

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

If a blocker genuinely requires a browser, external account, provider setting, secret, human review or other excluded action, PHDK gives the owner an explicit checklist instead of simply saying “BLOCKED”.

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
- formal approvals required by the repository or organization;
- external/manual actions PHDK cannot perform.

PHDK eliminates repetitive approval loops. It does not eliminate accountability.

---

# Safety and delivery boundaries

PHDK keeps strong execution boundaries.

By default:

- no unattended or overnight execution;
- no scheduled agent loops;
- no recurring autonomous jobs;
- no browser/headless verification;
- no live database mutation;
- no secret-value inspection;
- no provider administration from ordinary development commands;
- no bypass of hooks, protections or formal review requirements.

PMO workers are allowed only inside an explicitly active PMO session and only for owner-confirmed workstreams.

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

Auto will create/reuse the Capture baseline, create/reuse Plan, coordinate workstreams, integrate, validate, repair and check the final candidate. If you invoke Auto without naming one delivery and the repo already reveals several parallel fronts, Auto enters PMO discovery, shows you the detected portfolio and asks you to confirm/add/remove/reprioritize those workstreams instead of forcing you to choose one arbitrary task.

### Existing project

Run:

```text
PHDK upgrade
PHDK capture
PHDK plan
```

Capture reconstructs what the product is supposed to be. Plan reconstructs how it is currently built, then defines the target architecture and an incremental convergence path.

Or run `PHDK auto` and let it orchestrate those stages automatically when they are missing/outdated.

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
| Execution boundaries | [EXECUTION_SCOPE.md](EXECUTION_SCOPE.md) |
| Universal command preflight | [PHDK_PREFLIGHT.md](PHDK_PREFLIGHT.md) |
| Recommended skills/capabilities | [SKILLS_REGISTRY.md](SKILLS_REGISTRY.md) |
| Professional requirements capture | [PHDK_CAPTURE.md](PHDK_CAPTURE.md) |
| Solution architecture & implementation planning | [PHDK_PLAN.md](PHDK_PLAN.md) |
| Multi-workstream orchestration | [PHDK_PMO.md](PHDK_PMO.md) |
| Autonomous single-goal development | [PHDK_AUTO.md](PHDK_AUTO.md) |
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
