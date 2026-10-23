**Encryption standard (v2.64.0):** Apply PHDK_ENCRYPTION_STANDARD.md for TLS, encrypted databases and backups, external key custody, workload identity, secret recovery and bounded encryption-key caching. No unauthorized provider changes or live data migrations.

# PHDK Plan Standard

## Default Node.js runtime selection
For Node.js stacks, follow the mandatory Node.js runtime and npm supply-chain profile in [PHDK_SECURE.md](PHDK_SECURE.md). Default to the latest patched Active LTS compatible with the complete selected stack and Railway deployment. Record version, compatibility evidence, engines pinning and exceptions in the technical architecture; do not assume every framework supports the newest runtime. Re-evaluate at each material stack change.


## Risk-proportionate tenant isolation and encryption

For multi-tenant plans, apply `PHDK_TENANT_RISK_STANDARD.md` and consume `TENANT_RISK_ASSESSMENT.md`. Compare justified shared RLS versus dedicated database/infrastructure architectures and baseline versus additional field-level/per-tenant-key encryption, along with risk reduction, cost and operations. Record risk tier, owner-approved choice or DECISION REQUIRED in `ADMIN_ARCHITECTURE.md`; map selected controls, migration/rollback and UAT verification to `MILESTONE_PLAN.md`. Never silently provision infrastructure or convert live data.

## Mandatory milestone planning and project-management model

Apply `PHDK_PROJECT_MANAGEMENT_STANDARD.md` during Plan. Classify the delivery approach as predictive, adaptive or hybrid from actual requirement stability/uncertainty, then create or refresh `MILESTONE_PLAN.md`.

Milestones are value/acceptance boundaries, not PHDK lifecycle stages. Every in-scope commitment and implementation task/workstream must map to a milestone. Each milestone needs a stable `MS-###` ID, value outcome, linked requirements, included workstreams/tasks, dependencies, material risks/domain impacts, acceptance criteria/evidence, expected SemVer impact, and UAT user-goal intent. Prefer vertical, independently coherent increments; do not reserve an exact version number during planning because current `main` may advance before delivery.

Inside Auto/Auto Force, completing a milestone triggers the milestone publication gate: relevant verification → version reconciliation/bump → version-prefixed commit → scoped PR → merge to `main` → remote SHA/version readback → continue from refreshed `main`. Ending Capture, Plan, Design, PMO, UAT or another lifecycle stage by itself never triggers a version.

When available, prefer the planning/task-breakdown and detailed implementation-plan capabilities registered in `SKILLS_REGISTRY.md`; PHDK's milestone, authorization and delivery rules override any external skill's checkpoint/commit/approval conventions.

## Mandatory product UX/UI planning and Design handoff

For every user-facing interface, implement `PHDK_UX_UI.md` in greenfield or brownfield mode. Plan must produce `UX_RESEARCH_BASELINE.md`, `UX_JOURNEYS.md`, `UI_DESIGN_SYSTEM.md`, and `UX_UI_DECISIONS.md` alongside `UX_ARCHITECTURE.md`, link critical journeys to requirements and implementation tasks, and preserve valid existing workflows in redesigns. Do not declare Plan exit passed with these missing, unless the current scope has no applicable UI and has documented N/A.

Plan fixes the technical stack, content/navigation architecture, existing brand constraints and draft design-system/component boundaries. **Final visual selection belongs to `PHDK design`, stage 25-design, after Plan and before affected UI implementation.** Mark pending aesthetic choices explicitly in the existing design artifacts; do not demand a finished approved style guide as a prerequisite to entering Design. Design refines the same files with references, alternatives, previews, final tokens/component mappings and decision provenance, then updates affected implementation/milestone tasks.

Normal Auto and standalone Design ask one unresolved visual question at a time and wait for the owner's selection/preview approval. Auto Force makes and records the choices as `AGENT_SELECTED_AUTO_FORCE` and continues without a PHDK visual-approval pause. Reuse valid owner decisions; preserve actual owner restrictions and the no-local-runtime/no-Docker/no-new-environment boundary in `PHDK_PRODUCTION_VERIFICATION.md`. A plan, generated mockup or source specification is not runtime verification.

## Mandatory administration architecture

Apply `ADMIN_CONSOLE_STANDARD.md` to every applicable portal. Define `ADMIN_ARCHITECTURE.md`, `ADMIN_CAPABILITY_MATRIX.md`, `ADMIN_SETTINGS_REGISTRY.md`, and `AI_WORKFLOW_CATALOG.md` (only if AI applies) as required Plan/evolving implementation outputs. Fix the authorized tenancy decision, platform vs tenant admin ownership, server-side permissions, isolation boundaries, protected secret storage, UAT profile-switch mechanism, navigable Configuración tabs, localization/themes, backup and audit flow, integration/AI graph input/output contracts, migrations and rollback, and explicit source/API/test traceability. Break missing functions into actual UI+API+DB+test work, never just documentation scaffolding. Document unknown sensitive decisions rather than silently promoting single-tenant to multi-tenant.

## Mandatory resource CRUD architecture

For applicable apps, apply `CRUD_STANDARD.md`: inventory managed entities, role and public exposure, document `CRUD_MATRIX.md` per resource × role × surface, resolve admin detail access and appropriate C/R/U/D policies with backend authorization, and plan exceptions and test coverage. Include the matrix in Plan handoffs. Do not assume all roles get full CRUD.

## Mandatory full-inventory Plan coverage

Follow `PHDK_COMMITMENT_STANDARD.md`. Consume `PHDK_COMMITMENTS.md`, and generate `PHDK_COMMITMENT_COVERAGE.md` retaining visibility of every confirmed ID. Map **every confirmed ID in the current authorized goal** to requirements, design decisions, implementation tasks/workstreams, dependencies and acceptance evidence; fail the Plan exit gate if any such ID is unowned or omitted without a documented blocker. Mark other commitments outside this run's scope without executing, cancelling or silently deferring them. Missing implementation of a confirmed in-scope requirement stays linked to that commitment and is executed by Auto. Return genuinely new outcomes outside the goal or indispensable material decisions unresolved by current rules/decisions to Capture for owner scope confirmation; preserve original plan and ledger history.

Under active AUTO FORCE, [Propose missing definitions and solutions](PHDK_AUTO_CONTINUITY.md#propose-missing-definitions-and-solutions) takes precedence over generic requests for missing specifications. The assistant supplies concrete behavior and acceptance criteria for gaps already implied by the authorized outcome: recover relevant current standards and product decisions, choose reasonable safe reversible defaults, identify useful configuration, and record assumptions and rationale in the existing Plan/decision artifacts. Then implement the inferable authorized work; do not ask the owner to design every detail or recommend dropping required capabilities to finish. For visual choices, first complete the applicable Design baseline under `PHDK_DESIGN.md` without a FORCE owner-selection wait.

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

Do not invent branding or visual art direction unsupported by intent. Standalone Plan records constraints and unresolved aesthetic choices; the explicit `PHDK design` command or the Design stage included in an authorized Auto goal supplies the graphical design scope. Final visual choices follow that stage's mode policy before dependent UI coding.

### 4. MILESTONE_PLAN.md

Define the ordered value-delivery roadmap required by `PHDK_PROJECT_MANAGEMENT_STANDARD.md`. Map milestones to commitments, requirements, workstreams/tasks, dependencies, risks, acceptance evidence, expected SemVer impact and UAT user-goal intent. Record actual version/PR/main evidence only after execution. Include the selected Design baseline as a dependency for applicable UI work, not as a mandatory separate release milestone.

### 5. IMPLEMENTATION_PLAN.md

The executable delivery plan.

Every step must contain:

- stable Plan ID, e.g. `PLAN-001`;
- intent/requirement/feature links;
- inspected implementation state, existing source/evidence, and the exact missing behavior, with routine definitions supplied by the assistant under the FORCE rule above when applicable;
- outcome;
- prerequisites/dependencies, including the applicable selected Design baseline for UI tasks;
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

### 7. TASK.md integration

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
- applicable Design inputs and unresolved visual choices are ready for stage 25;
- unresolved material decisions are explicit.

## Relationship to PMO

Plan supplies PMO with the architecture and executable decomposition; Design supplies the selected visual baseline for applicable UI workstreams.

Recommended chain:

```text
Capture → Plan → Design → PMO / implementation
```

PMO should derive workstreams primarily from `IMPLEMENTATION_PLAN.md`, requirements/features, architecture ownership boundaries, the selected Design baseline and current repo state.

Plan proposes workstream groupings but does not activate them. PMO owns portfolio confirmation and coordination. It may organize or execute genuinely independent authorized non-UI work while an ordinary Auto design choice is pending, but cannot bypass the affected UI design dependency.

## Relationship to Auto

Standalone `PHDK plan` produces architecture/planning artifacts and stops unless a parent request includes execution. Its completion response identifies `PHDK design` as the next applicable step without silently activating it.

Full `PHDK auto` uses Plan as an internal lifecycle stage after Capture. After Plan, immediately execute/reuse applicable `PHDK design` before UI workstream implementation. **Auto asks the unresolved visual choices and waits for the owner; Auto Force chooses, records AGENT_SELECTED_AUTO_FORCE and continues.** No second development command is needed after the applicable decision. Continue the complete authorized scope, including greenfield construction when code is absent, while preserving valid code and independent permitted work. A completed plan or design package proves readiness to execute, not implemented or accepted behavior.

## Lifecycle handoff

When Plan completes or is reused inside a lifecycle run:

- create `docs/phdk/lifecycle/<run-id>/20-plan/HANDOFF.md`;
- snapshot the material Plan outputs, including `SOLUTION_ARCHITECTURE.md`, `REPOSITORY_ARCHITECTURE.md`, `UX_ARCHITECTURE.md`, draft design artifacts, `MILESTONE_PLAN.md`, `IMPLEMENTATION_PLAN.md`, relevant architecture decisions, and TASK integration;
- record the architecture quality/exit gate;
- declare what Design must verify before visual selection, or why Design is NOT APPLICABLE for this scope;
- retain the architecture/dependency inputs that PMO will consume after the Design gate.

Design verifies the technical/content baseline, existing decisions and components; it refines only affected planning outputs. PMO must validate `IMPLEMENTATION_PLAN.md`, ownership/dependency boundaries, relevant ADRs and the applicable `25-design/HANDOFF.md` before dependent UI execution.

## Completion response

At completion, explain:

- whether Plan operated greenfield or brownfield;
- current architecture summary when applicable;
- target architecture;
- major decisions/tradeoffs;
- recommended repo topology;
- workstream decomposition;
- migration/convergence plan;
- unresolved decisions and the next applicable Design choice.

Then list/link:

- `SOLUTION_ARCHITECTURE.md`
- `REPOSITORY_ARCHITECTURE.md`
- `UX_ARCHITECTURE.md`
- `IMPLEMENTATION_PLAN.md`
- `UI_DESIGN_SYSTEM.md` and `UX_UI_DECISIONS.md` when UI applies
- `ARCHITECTURE_DECISIONS.md` when created/updated
- `TASK.md` when updated

State clearly that Design and PMO/Auto execution use these artifacts as the architectural source of truth; the selected visual baseline is finalized in Design.
