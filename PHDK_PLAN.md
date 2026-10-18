# PHDK Plan Standard


## Mandatory milestone planning and project-management model

Apply `PHDK_PROJECT_MANAGEMENT_STANDARD.md` during Plan. Classify the delivery approach as predictive, adaptive or hybrid from actual requirement stability/uncertainty, then create or refresh `MILESTONE_PLAN.md`.

Milestones are value/acceptance boundaries, not PHDK lifecycle stages. Every in-scope commitment and implementation task/workstream must map to a milestone. Each milestone needs a stable `MS-###` ID, value outcome, linked requirements, included workstreams/tasks, dependencies, material risks/domain impacts, acceptance criteria/evidence, expected SemVer impact, and UAT user-goal intent. Prefer vertical, independently coherent increments; do not reserve an exact version number during planning because current `main` may advance before delivery.

Inside Auto/Auto Force, completing a milestone triggers the milestone publication gate: relevant verification → version reconciliation/bump → version-prefixed commit → scoped PR → merge to `main` → remote SHA/version readback → continue from refreshed `main`. Ending Capture, Plan, PMO, UAT or another lifecycle stage by itself never triggers a version.

When available, prefer the planning/task-breakdown and detailed implementation-plan capabilities registered in `SKILLS_REGISTRY.md`; PHDK's milestone, authorization and delivery rules override any external skill's checkpoint/commit/approval conventions.

## Mandatory product UX/UI planning

For every user-facing interface, implement `PHDK_UX_UI.md` in greenfield or brownfield mode. Plan must produce `UX_RESEARCH_BASELINE.md`, `UX_JOURNEYS.md`, `UI_DESIGN_SYSTEM.md`, and `UX_UI_DECISIONS.md` alongside `UX_ARCHITECTURE.md`, link critical journeys to requirements and implementation tasks, and preserve valid existing workflows in redesigns. Do not declare Plan exit passed with these missing, unless the project has no UI and has documented N/A.


## Mandatory administration architecture

Apply `ADMIN_CONSOLE_STANDARD.md` to every applicable portal. Define `ADMIN_ARCHITECTURE.md`, `ADMIN_CAPABILITY_MATRIX.md`, `ADMIN_SETTINGS_REGISTRY.md`, and `AI_WORKFLOW_CATALOG.md` (only if AI applies) as required Plan/evolving implementation outputs. Fix the authorized tenancy decision, platform vs tenant admin ownership, server-side permissions, isolation boundaries, protected secret storage, UAT profile-switch mechanism, navigable Configuración tabs, localization/themes, backup and audit flow, integration/AI graph input/output contracts, migrations and rollback, and explicit source/API/test traceability. Break missing functions into actual UI+API+DB+test work, never just documentation scaffolding. Document unknown sensitive decisions rather than silently promoting single-tenant to multi-tenant.

## Mandatory resource CRUD architecture

For applicable apps, apply `CRUD_STANDARD.md`: inventory managed entities, role and public exposure, document `CRUD_MATRIX.md` per resource × role × surface, resolve admin detail access and appropriate C/R/U/D policies with backend authorization, and plan exceptions and test coverage. Include the matrix in Plan handoffs. Do not assume all roles get full CRUD.

## Mandatory full-inventory Plan coverage

Follow `PHDK_COMMITMENT_STANDARD.md`. Consume `PHDK_COMMITMENTS.md`, and generate `PHDK_COMMITMENT_COVERAGE.md` retaining visibility of every confirmed ID. Map **every confirmed ID in the current authorized goal** to requirements, design decisions, implementation tasks/workstreams, dependencies and acceptance evidence; fail the Plan exit gate if any such ID is unowned or omitted without a documented blocker. Mark other commitments outside this run's scope without executing, cancelling or silently deferring them. Missing implementation of a confirmed in-scope requirement stays linked to that commitment and is executed by Auto. Return genuinely new outcomes outside the goal or indispensable material decisions unresolved by current rules/decisions to Capture for owner scope confirmation; preserve original plan and ledger history.

Under active AUTO FORCE, [Propose missing definitions and solutions](PHDK_AUTO_CONTINUITY.md#propose-missing-definitions-and-solutions) takes precedence over generic requests for missing specifications. The assistant supplies concrete behavior and acceptance criteria for gaps already implied by the authorized outcome: recover relevant current standards and product decisions, choose reasonable safe reversible defaults, identify useful configuration, and record assumptions and rationale in the existing Plan/decision artifacts. Then implement the inferable authorized work; do not ask the owner to design every detail or recommend dropping required capabilities to finish.

For a genuinely new indispensable material decision that cannot be resolved within that mandate, present the recommended definition and its impact, ask only for the specific remaining choice, and continue independent work. Existing user decisions and non-goals remain binding. Standalone Plan and audit-only requests retain their planning/read-only boundaries; this rule does not activate implementation outside an authorized parent goal.

## Command and purpose

Before substantive execution, run the universal preflight in `PHDK_PREFLIGHT.md`. Inside a lifecycle run, verify the Capture handoff and required Capture artifacts from `PHDK_LIFECYCLE.md` before making architecture decisions. Verify the active PHDK installation/version and inspect/use stage-relevant available skills from `SKILLS_REGISTRY.md`, unless the user explicitly disabled them.

`PHDK plan` turns the captured product intent and requirements into a professional solution architecture and executable delivery plan.

It runs after `PHDK capture` when a project needs architectural definition, architectural reconstruction, or a concrete implementation plan.

Plan has two operating modes:

1. **Greenfield** — design the target architecture from the requirements and PHDK standards.
2. **Brownfield** — inspect the architecture that already exists, preserve valid decisions, identify gaps/debt/inconsistencies, define a target architecture, and create an incremental convergence plan from the current state.

Plan does not blindly scaffold or rewrite an existing repository. Existing code and architecture are first-class evidence.

Choose the mode from actual product implementation. A readable repository containing only requirements, PHDK files or a scaffold is greenfield for the required product development, even though the repository already exists. Reuse its established intent and decisions. An unreadable/incompletely inspected source tree is UNVERIFIED, not evidence of absence. For a partial product, preserve working parts and plan the missing behavior.

## Inputs

Use the strongest available sources:

- `PROJECT_INTENT.md`
- `PROJECT_BRIEF.md`
- `PRD.md`
- `FEATURES.md`
- `REQUIREMENTS_TRACEABILITY.md`
- `docs/intents/*-intent.md`
- `ARCHITECTURE_DECISIONS.md` / ADRs
- current source/repository layout
- package/workspace configuration
- routes/API boundaries
- schema/models/migrations
- auth/RBAC
- integrations
- deployment/build configuration
- design system/UI structure
- current TASK/STATUS
- applicable PHDK standards

If Capture artifacts are missing or materially incoherent, recommend or run `PHDK capture` first when the parent command authorizes the full lifecycle.

## Greenfield: design the target architecture

For a new project, derive an architecture that satisfies the captured intent and requirements while conforming to applicable PHDK standards.

Do not mechanically choose complexity. Tailor the architecture to the product.

Where the PHDK default stack applies, prefer the standard monorepo architecture unless project constraints/decisions justify another shape:

```text
repo/
├── apps/
│   ├── web/
│   └── api/
├── packages/
│   ├── db/
│   ├── ui/
│   ├── validators/
│   ├── config/
│   └── ai/        # only when AI applies
└── ...
```

Typical default responsibilities:

- web: Next.js application/UI
- api: NestJS/Fastify application services/API
- database: PostgreSQL via the PHDK data layer conventions
- shared packages: reusable contracts/UI/config/validation/domain utilities
- AI: centralized provider-agnostic package only when AI actually applies

A different architecture is valid when product requirements, constraints, scale, existing platform, deployment model, or documented ADRs justify it.

## Brownfield: architecture reconstruction and convergence

When meaningful product implementation already exists, Plan must first document **Current State** before proposing change.

Inspect:

- workspace/repo topology;
- apps/services/packages;
- runtime boundaries;
- database and data ownership;
- APIs/events/integration contracts;
- auth and permission boundaries;
- deployment boundaries;
- shared libraries and coupling;
- UX/navigation/information architecture;
- testing/observability/security architecture;
- AI architecture when applicable;
- known technical debt and migration constraints.

Classify each important existing architectural element:

- **KEEP** — aligned and healthy;
- **EVOLVE** — valid direction but needs improvement;
- **REPLACE** — materially conflicts with requirements/standards;
- **UNKNOWN** — evidence insufficient;
- **LEGACY** — retained temporarily for compatibility/migration.

Never replace working architecture merely because a PHDK default is different.

Produce a gap map:

```text
Current State → Gap / Risk → Target State → Migration Step → Validation
```

The target architecture must be reachable incrementally from the current repository without requiring an unnecessary rewrite.

## Canonical Plan artifacts

Create or refresh:

### 1. SOLUTION_ARCHITECTURE.md

The system-level architecture.

Required sections:

- architecture goals and intent links;
- current-state summary (brownfield);
- target-state overview;
- system/context boundaries;
- major components/services;
- responsibility boundaries;
- runtime/deployment topology;
- data architecture;
- integration architecture;
- auth/security boundaries;
- AI architecture when applicable;
- observability/diagnostics;
- reliability/performance expectations;
- architecture risks/tradeoffs;
- migration/convergence strategy;
- diagrams (Mermaid preferred when useful);
- open architecture decisions.

### 2. REPOSITORY_ARCHITECTURE.md

Defines how the codebase should be organized.

Include:

- mono/polyrepo decision and rationale;
- apps/services/packages;
- package responsibilities;
- dependency-direction rules;
- shared contracts/types;
- database package/schema ownership;
- route/API organization;
- test layout;
- configuration/env ownership;
- generated-code policy;
- shared/global files;
- build/release boundaries.

For brownfield projects, include current vs target layout and migration steps.

### 3. UX_ARCHITECTURE.md

Conceptual UX/UI architecture, not merely visual styling.

Include:

- actor/role entry points;
- information architecture;
- navigation model;
- route hierarchy;
- primary flows;
- admin vs user surfaces;
- responsive strategy;
- loading/empty/error/success/permission states;
- accessibility assumptions;
- design-system/component boundaries;
- conceptual screen/page inventory;
- optional low-fidelity Mermaid/ASCII flow diagrams.

Do not invent branding or visual art direction unsupported by intent. Detailed graphical design may be produced only when the request includes it.

### 4. MILESTONE_PLAN.md

Define the ordered value-delivery roadmap required by `PHDK_PROJECT_MANAGEMENT_STANDARD.md`. Map milestones to commitments, requirements, workstreams/tasks, dependencies, risks, acceptance evidence, expected SemVer impact and UAT user-goal intent. Record actual version/PR/main evidence only after execution.

### 5. IMPLEMENTATION_PLAN.md

The executable delivery plan.

Every step must contain:

- stable Plan ID, e.g. `PLAN-001`;
- intent/requirement/feature links;
- inspected implementation state, existing source/evidence, and the exact missing behavior, with routine definitions supplied by the assistant under the FORCE rule above when applicable;
- outcome;
- prerequisites/dependencies;
- exact components/files/packages likely affected;
- implementation steps;
- data/schema/API implications;
- security/risk notes;
- validation;
- UAT impact;
- rollback/migration considerations;
- recommended workstream grouping;
- done criteria.

Order the plan by dependencies, not by document order.

### 6. ARCHITECTURE_DECISIONS.md

Create or update the project architecture-decision ledger when material decisions exist.

For each decision:

- ADR/decision ID;
- context;
- options considered;
- decision;
- rationale;
- consequences;
- requirement/intent links;
- status;
- migration impact.

Do not overwrite historical decisions silently. Supersede them explicitly.

### 6. TASK.md integration

Plan translates the approved architecture/implementation sequence into actionable task structure.

`TASK.md` should identify:
- current project goal;
- workstream-ready tasks;
- dependencies;
- sequence;
- shared integration points;
- completion criteria;
- planned verification.

TASK remains execution context, not permanent product requirements or reusable authorization.

## Architecture dimensions Plan must evaluate

Use only applicable dimensions:

- system context and external actors;
- frontend/web/mobile;
- backend/API/services;
- data/storage;
- domain boundaries;
- auth/authz;
- tenancy;
- integrations;
- event/async flows;
- caching/queues where justified;
- AI/LLM architecture;
- imports/ETL;
- payments;
- notifications;
- content/CMS;
- security/privacy;
- audit/observability;
- performance/scalability;
- resilience/recovery;
- internationalization;
- accessibility;
- deployment/runtime boundaries;
- repository/build architecture;
- testing architecture;
- migration/backward compatibility;
- UX/information architecture.

Do not introduce infrastructure/services merely because they are common architectural patterns.

## Architecture quality gate

Before Plan is complete:

- every P0 requirement maps to a target architecture capability;
- all major components have clear responsibilities;
- dependency direction is explicit;
- data ownership is explicit;
- auth/security boundaries are explicit where applicable;
- external dependencies are explicit;
- shared/global surfaces are identified for PMO;
- major architecture decisions are recorded;
- migration steps exist for brownfield gaps;
- implementation ordering is dependency-safe;
- UX route/flow architecture covers all P0 workflows;
- unresolved material decisions are explicit.

## Relationship to PMO

Plan supplies PMO with the architecture and executable decomposition.

Recommended chain:

```text
Capture → Plan → PMO
```

PMO should derive workstreams primarily from `IMPLEMENTATION_PLAN.md`, requirements/features, architecture ownership boundaries, and current repo state.

Plan proposes workstream groupings but does not activate them. PMO owns portfolio confirmation and coordination.

## Relationship to Auto

Standalone `PHDK plan` produces architecture/planning artifacts and stops unless a parent request includes execution.

Full `PHDK auto` uses Plan as an internal lifecycle stage after Capture and before PMO/workstream execution. After the Plan exit gate passes, Auto must immediately execute the next eligible implementation task and continue the complete authorized development in the same invocation, including greenfield construction when code is absent. It must not ask whether to start development or require another mode command. Ask only for genuinely material unresolved architecture/product decisions and continue independent permitted work. A completed plan proves readiness to execute; it does not prove implemented or accepted behavior.

## Lifecycle handoff

When Plan completes or is reused inside a lifecycle run:

- create `docs/phdk/lifecycle/<run-id>/20-plan/HANDOFF.md`;
- snapshot the material Plan outputs, including `SOLUTION_ARCHITECTURE.md`, `REPOSITORY_ARCHITECTURE.md`, `UX_ARCHITECTURE.md`, `IMPLEMENTATION_PLAN.md`, relevant architecture decisions, and TASK integration;
- record the architecture quality/exit gate;
- declare what PMO must verify before it creates/confirms workstreams.

PMO must validate `IMPLEMENTATION_PLAN.md`, ownership/dependency boundaries, and relevant ADRs before workstream execution.

## Completion response

At completion, explain:

- whether Plan operated greenfield or brownfield;
- current architecture summary when applicable;
- target architecture;
- major decisions/tradeoffs;
- recommended repo topology;
- workstream decomposition;
- migration/convergence plan;
- unresolved decisions.

Then list/link:

- `SOLUTION_ARCHITECTURE.md`
- `REPOSITORY_ARCHITECTURE.md`
- `UX_ARCHITECTURE.md`
- `IMPLEMENTATION_PLAN.md`
- `ARCHITECTURE_DECISIONS.md` when created/updated
- `TASK.md` when updated

State clearly that PMO/Auto execution should use these artifacts as the architectural source of truth.
