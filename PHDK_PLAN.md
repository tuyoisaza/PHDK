# PHDK Plan Standard

## Command and purpose

`PHDK plan` turns the captured product intent and requirements into a professional solution architecture and executable delivery plan.

It runs after `PHDK capture` when a project needs architectural definition, architectural reconstruction, or a concrete implementation plan.

Plan has two operating modes:

1. **Greenfield** — design the target architecture from the requirements and PHDK standards.
2. **Brownfield** — inspect the architecture that already exists, preserve valid decisions, identify gaps/debt/inconsistencies, define a target architecture, and create an incremental convergence plan from the current state.

Plan does not blindly scaffold or rewrite an existing repository. Existing code and architecture are first-class evidence.

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

When the repo already exists, Plan must first document **Current State** before proposing change.

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

### 4. IMPLEMENTATION_PLAN.md

The executable delivery plan.

Every step must contain:

- stable Plan ID, e.g. `PLAN-001`;
- intent/requirement/feature links;
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

### 5. ARCHITECTURE_DECISIONS.md

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

Full `PHDK auto` uses Plan as an internal lifecycle stage after Capture and before PMO. Auto may proceed without a redundant Plan approval when the architecture choices are already within the authorized product goal and standards. It asks only for genuinely material unresolved architecture/product decisions.

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
