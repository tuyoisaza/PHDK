# TECHNICAL_STACK.md

For explicit `PHDK auto`, `PHDK_AUTO.md` governs the whole goal's cadence: implement all agreed features and cross-package wiring before final integrated verification and versioned branch/PR delivery. Stack and build contracts below remain applicable; they do not impose a QA/release/approval cycle after each internal stage. Preserve actual mandatory controls and the provider/browser boundaries in `EXECUTION_SCOPE.md`.

## Purpose

This file defines the canonical technical stack for all products built on this standard.

Every agent must treat this file as the source of truth for technology choices. A dependency outside this stack needs current scope authorization and a corresponding entry in `ARCHITECTURE_DECISIONS.md`. Under `PHDK_AUTO.md`, necessary bounded implementation dependencies can be routine choices within the agreed goal; do not ask again solely because a package name was not listed. Prefer the existing stack. A new runtime platform, auth provider, paid service, or material architecture/security change is not a routine dependency choice unless that decision is already part of the authorized goal.

`EXECUTION_SCOPE.md` defines what the PHDK agent may do. This file specifies application code and repository configuration; it does not authorize provisioning or administering external services. Work stays in repository files, local code verification, git/GitHub, authorized pushes to an existing GitHub-connected deployment pipeline, and requested diagnostics under its **Bounded read-only provider diagnostics** section. Browser testing, application HTTP/database/API probes, provider administration, recurring jobs, and infrastructure setup remain outside scope. Requested bounded provider metadata/status/log reads need no extra approval phrase, PHDK Developer Mode, or unlock.

---

## Monorepo

```txt
Package manager:    pnpm
Build system:       Turborepo
Language:           TypeScript (strict mode)
Node minimum:       20.x
Formatter:          Prettier
```

Structure:

```txt
apps/
  web/              — Next.js frontend
  api/              — NestJS + Fastify backend
  mobile/           — Expo placeholder only, do not build unless tasked
packages/
  ui/               — shared UI components
  types/            — shared TypeScript types
  validators/       — shared Zod schemas
  api-client/       — typed API client
  design-tokens/    — spacing, colors, typography, radius, shadows, motion
  observability/    — logger and diagnostics wrappers
  db/               — Drizzle schema, migrations, database client
  config/           — shared config
```

---

## LSP / Code Intelligence Setup

Use the TypeScript code intelligence already available in the current coding tool. `typescript-language-server`/`tsserver` is the reference implementation, but PHDK does not install editor plugins, MCP integrations, or language servers as a foundation or session-completion gate.

### Repository configuration

- Keep strict TypeScript settings and root project references/path mappings across `apps/*` and `packages/*`.
- Preserve Drizzle-generated types, Next.js generated types (`next-env.d.ts`), and NestJS decorator metadata (`experimentalDecorators`, `emitDecoratorMetadata`) in the relevant code configuration.
- Reuse `tsconfig.json`/`tsconfig.base.json`; do not create a conflicting config solely for a tool.

### Available capability and evidence

When direct local LSP access is available and relevant to the change, use diagnostics, definitions, references, and type information to inspect real project symbols. Otherwise use repository text search and applicable TypeScript checks. Report which capability was actually used; an editor having an LSP does not prove the agent can access it.

Do not perform a synthetic rename, mandatory setup exercise, or per-session smoke check just to satisfy PHDK. When a requested code change affects TypeScript configuration or workspace boundaries, validate that code locally without expanding the task into environment setup or external integration installation.

---

## Frontend — apps/web

```txt
Framework:          Next.js (App Router)
Language:           TypeScript strict
Styling:            Tailwind CSS
Components:         shadcn/ui-compatible
Validation:         Zod (shared from packages/validators)
i18n:               next-intl
State:              React built-ins first, Zustand if needed
```

Rules:

- Use App Router, not Pages Router
- Server components by default, client components only when needed
- No business logic inside page components
- No hardcoded user-facing strings
- Images use Next.js Image component

---

## Backend — apps/api

```txt
Framework:          NestJS
HTTP adapter:       Fastify
Language:           TypeScript strict
Validation:         Zod (shared from packages/validators)
API style:          REST (GraphQL only if explicitly required)
```

Rules:

- Validate all inputs at the API boundary using Zod
- Enforce authorization server-side on every protected endpoint
- Never trust client-supplied data without validation
- Use structured logging on every important action
- Never expose raw error internals to clients
- Bind to `0.0.0.0` and read `process.env.PORT`

---

## Database — packages/db

```txt
ORM:                Drizzle
Database:           PostgreSQL — all environments
Migration tool:     Drizzle Kit
```

PostgreSQL is the application's supported runtime database. Runtime database infrastructure is an external prerequisite; PHDK implements its schema, migrations, queries, and configuration validation in the repository even when the runtime is not yet available. Do not provision a cloud database, start a local database/container, or replace the runtime database with SQLite. Local verification uses isolated test doubles or in-process adapters and never connects to a real database.

Configuration is environment-driven:

```env
DATABASE_PROVIDER="postgresql"
DATABASE_URL="..."
```

### Database code and isolated verification

- Runtime connection values belong to the existing deployment environment; PHDK documents variable names in `.env.example` without retrieving or setting real credentials
- Never run migrations, queries, seeds, or verification probes against a real dev, staging, or production database from the PHDK agent
- Review migration SQL and compatibility locally; test query and migration-related application logic with explicit test doubles when risk-triggered coverage is needed
- Test doubles are confined to verification and must never become a silent production fallback
- If runtime `DATABASE_URL` is unset or unreachable, application code must fail clearly rather than fall back to SQLite or an in-memory store — see `QA_CHECKLIST.md` Database

Rules:

- Never mutate schema without a migration
- Include migration compatibility and recovery notes with schema changes; report that live migration execution is outside PHDK rather than claiming it was tested
- Core records include: `id`, `created_at`, `updated_at`, `created_by`, `updated_by`
- Important records include soft delete: `deleted_at`
- Drizzle and PostgreSQL are ready but not implemented unless the project phase requires them

### Data Backup Policy

Live database backup and recovery operations are outside PHDK under `EXECUTION_SCOPE.md`. PHDK does not create backup jobs, email exports, git backup branches, retention schedules, restore tasks, or backup product features as part of a foundation or database slice.

Keep source code and migration files in GitHub. Never put live database dumps, credentials, or private application data into source control. If the user supplies existing recovery constraints, record only the relevant requirements and migration dependencies in `ARCHITECTURE_DECISIONS.md`; do not invent a policy or claim a backup/restore was verified. External backup setup is not a PHDK code-completion gate.

See `DEVSECOPS.md` Data Backup and Recovery Safety for the corresponding boundary.

---

## Data Import / Intake Pipeline

Any requested feature that ingests data from multiple file, spreadsheet, or export types, supports repeated manual uploads, or explicitly requires recurring import code uses a stateful intake pipeline. Do not wire an upload straight into business tables with no batch identity, no review step, and no way to undo a bad import short of a manual `DELETE`. This specifies import code; it does not authorize scheduled syncs, polling, background maintenance, or execution against live data.

This does not apply to a one-off seed script or a single admin-only CSV import with no repeat cadence — those can insert directly. The pipeline is for imports that recur or come from more than one source.

### The core principle

Never trust an uploaded file directly into production tables as final, and never hard-delete imported data to "undo" a bad import. Instead:

- Every import batch has an explicit lifecycle state.
- Every business-data row carries a reference to the batch that created it.
- Whether a row "counts" in business queries depends on its batch's current state — not on whether the row physically exists.

Approving or deactivating a batch never moves or deletes a single row. It flips one status field, and a shared query filter does the rest. This means undoing an approval, or reactivating a deactivated batch, is trivial and fully auditable — nothing was destroyed.

### Two control tables

Separate from the business tables the import populates:

```txt
import_batches        one row per uploaded package (e.g. "June 2026 close")
  - status:             pending | processed | approved | deactivated
  - cutoff_date:         derived from file content, never asked of the user
  - deactivated_at, deactivated_by, deactivation_reason
  - superseded_by_batch_id

import_file_checks    one row per file within a batch — the checklist
  - status:             pending | parsed | errored | duplicate | approved
  - source_type:         which requirement this file satisfies
  - records_imported, warnings (json), errors (json), meta (json)
```

Every business table populated by an import (invoices, orders, inventory snapshots, forecast rows, etc.) carries a nullable `batch_id` referencing `import_batches`. `NULL` means the row predates the pipeline (legacy data) and is always live.

### Lifecycle

```txt
upload → pending → [parse each file, insert rows tagged with batch_id] → processed
                                                                              │
                                                              manual review ─┤
                                                                              ▼
                                                         approved  |  deactivated
```

- Rows are inserted as soon as a file parses successfully — while the batch is still `pending`/`processed`. There is no separate staging table to promote from; the state filter (below) is what makes a batch's data count or not.
- `processed` means every file in the batch parsed; it is not yet official. A human approves it explicitly.
- `approved` is a status flip only — no data moves.
- `deactivated` is the undo path. It is not a delete: rows stay in place, the file stays in storage, and the deactivation is audited (`deactivated_at`, `deactivated_by`, `deactivation_reason`, optionally `superseded_by_batch_id`). Route any "delete this import" UI action to deactivate, never to a physical `DELETE`.
- Reactivating a batch is just clearing its `deactivated` status — the history stays intact either way.

### The shared filter — this is what makes deactivation work

Every business query filters through one reusable predicate, not a hand-rolled `WHERE` per query:

```ts
// packages/db (or equivalent shared query layer)
function activeSource(table) {
  return or(
    isNull(table.batchId),                 // legacy rows with no batch are always live
    notExists(
      db.select().from(importBatches)
        .where(and(
          eq(importBatches.id, table.batchId),
          eq(importBatches.status, "deactivated"),
        ))
    ),
  )
}
```

Apply it in every dashboard, report, forecast, or business query that reads from an import-populated table. Do not filter by `status = 'approved'` only — `pending`/`processed` rows should generally still be visible as "not yet final" rather than invisible, unless the project's business rules say otherwise; the one status that must always be excluded is `deactivated`.

### Deduplication — two levels, before insert

- **Exact duplicate**: hash the raw file content (e.g. SHA-256). If that hash already exists on a non-deactivated batch, mark the file `duplicate` in `import_file_checks` and skip the insert.
- **Semantic duplicate**: each parser derives a content fingerprint (e.g. same source type + same detected period + same key dimension) independent of file bytes. Catches "same data, re-exported, different file." Skip the insert and mark `duplicate` if a matching fingerprint already exists on a non-deactivated batch.

Both checks run before rows are inserted, not after.

### Required behavior for every intake feature

- Parsing never fails silently — every file gets a recorded outcome (`parsed`, `errored`, `duplicate`) with counts and a `warnings`/`errors` payload, even on partial success.
- Cutoff/period date is derived from file content (e.g. latest date found across the batch), never a field the user has to fill in.
- Manual approval is a distinct, explicit action — a batch does not become official just because it finished parsing.
- Deactivation always asks for a reason and records who/when.
- `DELETE` on an import batch (API or UI) is wired to deactivate, never to a physical row delete.

Data Import / Intake Pipeline is not scaffolded unless the project explicitly requires imports from multiple sources or repeated uploads. If the user explicitly requests recurring import code, deliver only that code and its isolated tests under `EXECUTION_SCOPE.md`; do not configure a schedule or enable external execution. See `QA_CHECKLIST.md` Data Import / Intake QA.

---

## Authentication — Custom Google OAuth 2.0

Default authentication method: custom Google OAuth 2.0.

PHDK does not use paid authentication vendors by default.

When login is required, implement Google OAuth 2.0 directly with environment-driven credential references. Creating credentials or configuring Google Cloud is outside PHDK.

Do not scaffold WorkOS, Clerk, Supabase Auth, Firebase Auth, Auth.js, or any other managed auth provider unless the project explicitly overrides this standard in `ARCHITECTURE_DECISIONS.md`.

```txt
Provider:           Custom Google OAuth 2.0
Sessions:           database-backed
Authorization:      server-side RBAC when roles exist
```

### Google OAuth code contract

Document the required variable names and exact callback path in repository configuration. Validate the configured redirect URI, OAuth state, token exchange result, and session behavior in code. Use mocked provider responses and session adapters for local verification; do not open a browser, complete a real login, or contact the provider.

Existing credential and allowed-origin configuration is an external runtime prerequisite. If it is unavailable, report that limitation while completing the code that can be implemented and verified locally. Do not create cloud projects, OAuth clients, consent screens, external secrets, or provider settings.

### Required env vars for auth

```env
GOOGLE_OAUTH_CLIENT_ID=""
GOOGLE_OAUTH_CLIENT_SECRET=""
GOOGLE_OAUTH_REDIRECT_URI="http://localhost:4000/auth/google/callback"
GOOGLE_OAUTH_ALLOWED_DOMAIN=""
AUTH_SESSION_SECRET=""
```

---

## Authorization

Required role model when RBAC is needed:

```txt
super_admin
admin
team_leader
member
```

Rules:

- Authorization enforced server-side on every protected route and endpoint
- Hiding UI is not authorization
- Role escalation blocked at server layer

---

## Validation — packages/validators

```txt
Library:    Zod
```

Rules:

- All Zod schemas live in `packages/validators`
- Shared between `apps/web` and `apps/api` — never duplicate schemas
- Validate at API boundary, not only in UI
- Use Zod for environment variable validation

---

## Observability — packages/observability

```txt
Style:              structured JSON logs
Error tracking:     Sentry-ready — not implemented until relevant phase
Tracing:            OpenTelemetry-ready — not implemented until relevant phase
```

Rules:

- Sentry and OpenTelemetry are ready in configuration but not scaffolded until explicitly tasked
- Every API service exposes a `/health` endpoint
- Correlation IDs must flow through every request
- Read `DEBUG_DIAGNOSTICS_STANDARD.md` for copy diagnostics spec

For a current request to check provider deployment/service/status/non-secret configuration metadata, consult existing logs, or diagnose an incident, use `EXECUTION_SCOPE.md` — **Bounded read-only provider diagnostics**. This permits only the defined bounded metadata/log reads through existing access, not a new observability integration or monitoring process. A later scoped read request is not canceled by an earlier code-task exclusion.

---

## Payments

```txt
Provider:   Stripe-ready — not implemented until required
```

Stripe is not scaffolded unless the project explicitly requires payments.

---

## AI / LLM Integration — packages/ai

Any feature that calls an LLM (chat, generation, extraction, classification, agents, etc.) must be built provider-agnostic and admin-manageable. Do not hardcode a provider, a model, or a prompt string directly in application code.

```txt
Provider:  configuration-driven — Anthropic, OpenAI, Google, or other, selected via env var
Model:     configuration-driven — selected via env var, never hardcoded
```

```env
AI_PROVIDER="anthropic"          — anthropic | openai | google | other
AI_MODEL="claude-sonnet-5"
AI_API_KEY=""
```

`packages/ai` is the only path to a model provider. No app code, feature, or route calls a provider SDK (`openai`, `@anthropic-ai/sdk`, `@google/generative-ai`, etc.) directly — every call goes `feature → packages/ai → provider`. This is what makes provider-swapping a config change instead of a code change, and what makes token/cost tracking below automatic instead of something each developer has to remember to add.

### Required for every LLM-powered feature

- **Provider is configurable** — switching provider is a config change, not a code change
- **Model is configurable** — switching model is a config change, not a code change
- **Prompt is admin-manageable** — an authorized admin can view and edit the prompt template from an AI management section in the admin panel, without a code deploy
- **Expected output is defined and admin-manageable** — the expected output shape/schema is visible and editable by an authorized admin alongside the prompt
- **Guardrails against prompt injection** — user-supplied content is never concatenated directly into the system prompt; user input is isolated/delimited, and the system prompt cannot be overridden by user input
- **Guardrails against indirect prompt injection** — if the feature feeds externally-sourced content (scraped pages, CMS fields, uploaded files, third-party API responses) into an LLM call, that content is treated as data, credentials are scoped per resource/tenant, and destructive actions require a confirmation gate — see `DEVSECOPS.md` LLM Integration Safety, Indirect Prompt Injection
- **Output validation** — LLM output is validated against the expected schema (e.g. with Zod) before it is used or displayed; invalid output is rejected, not trusted
- **Prompt/config changes are audited** — every edit to a prompt template or output schema logs actor, timestamp, and diff
- **Pricing is visible** — the AI management section includes an admin-initiated "refresh model pricing" action and shows cost per model currently in use; this standard does not add scheduled refreshes or polling
- **Every call is tracked** — see AI Token & Cost Observability below; this is built into `packages/ai` itself, not something each feature implements separately
- Cost and loop safeguards from `DEVSECOPS.md` Cost and Consumption Safety apply to every LLM call

See `AI_ADMIN_STANDARD.md` for conditional super-admin Prompts/consumption requirements and `QA_CHECKLIST.md` AI / LLM Configuration QA.

AI/LLM integration is not scaffolded unless the project explicitly requires it.

When AI applies, `AI_ADMIN_STANDARD.md` is mandatory. Provider/API-key evidence plus actual AI feature usage requires the protected super-admin **Prompts** capability and AI consumption administration. The Prompts editor separates editable name, personality prompt, execution prompt, and output JSON schema, with revision/audit and usage attribution.

These are product-code requirements. The PHDK agent verifies provider adapters, pricing, and usage handling with test doubles; it does not invoke a live model, operate the admin controls, or configure an external provider.

### AI Token & Cost Observability

`packages/ai` wraps every provider call and automatically records its usage. A feature is not done if its LLM calls don't show up in this tracking — see `QA_CHECKLIST.md` AI / LLM Configuration QA.

**Source of truth** — use the `usage` object returned by the provider on every response. Never estimate token counts locally (e.g. with a tokenizer library) when the provider reports actual consumption; local estimation is a fallback only for a provider that genuinely omits usage data.

**Field naming** — align with [OpenTelemetry GenAI semantic conventions](https://opentelemetry.io/docs/specs/semconv/gen-ai/) (`gen_ai.*`) where practical, so field names carry over cleanly if real OTel export is scaffolded later per `DEVSECOPS.md` Observability. This is a naming convention, not a requirement to stand up an OTel collector now — structured JSON logs are sufficient until tracing is explicitly tasked.

Record per call:

```txt
timestamp, environment, service/app, feature or workflow name
provider, requested_model, response_model
input_tokens, output_tokens, cached_input_tokens
cache_write_tokens, reasoning_tokens        — when the provider reports them
total_tokens, estimated_cost_usd, latency_ms
correlation/request ID, conversation ID     — when applicable
customer/account/project ID                 — when the project attributes cost per tenant
status, error_type                          — on failure
```

**Cost calculation** — `estimated_cost_usd = (input_tokens × input rate) + (output_tokens × output rate) + applicable cache/reasoning rates`. Store which version/date of the pricing table was used for each calculation so historical costs stay auditable after prices change — this is the same pricing table the "refresh model pricing" action above keeps current.

**Minimum queries the data must support** — tokens and cost by day/month, by model, by feature, by customer/account where attribution applies, by conversation/request; input/output ratio; cache savings; latency by model; error rate by model. Structured logs plus a query/aggregation path (SQL view, log query, or a simple report endpoint) satisfy this for most projects — a dedicated dashboard is only required if the project already has one for other metrics.

**Privacy default** — do not store full prompts or responses as part of this tracking. It records metrics and operational metadata only. Capturing actual prompt/response content is opt-in, explicit, and separate from token/cost tracking, and must follow the project's data retention and privacy handling.

---

## Deployment Through GitHub

PHDK releases code through an authorized push or merge to the existing GitHub-connected deployment pipeline, as defined in `EXECUTION_SCOPE.md`. Use the project's established release branch and target; `main` is the default only when the existing pipeline uses it. Do not change its triggers or create/connect a pipeline when none exists.

Repository build/start configuration may be maintained for that existing path. For an already connected Railway monorepo, both app builds use the repository root and the matching package commands:

```bash
# API service
pnpm --filter @repo/api build
pnpm --filter @repo/api start

# Web service
pnpm --filter @repo/web build
pnpm --filter @repo/web start
```

These commands describe the pipeline's application contract. Do not start an app locally if doing so would contact real services. Local build checks must stay within the verification boundary.

### Release procedure

1. Review the code diff and run the applicable local static/build checks and risk-triggered unit or in-process tests, without a browser or real services.
2. Commit and push through the authorized git/GitHub branch and review flow in `DEVELOPMENT_RULES.md` and `VERSIONING.md`.
3. Let the already connected pipeline respond to that push. Report the commit SHA and any deployment status already available through GitHub; do not poll repeatedly or claim runtime health from a successful push alone.
4. If the pipeline or required external configuration is missing, report the deployment limitation. Do not create infrastructure to remove it.

Do not use a provider dashboard, provider deployment/administration API or CLI commands, `railway up`, local upload, manual provider redeploy, or live `/health` probe. Requested bounded provider metadata/status/log reads through an authorized API/CLI/connector are governed by `EXECUTION_SCOPE.md` — **Bounded read-only provider diagnostics**. Do not provision projects, services, databases, secrets, domains, preview environments, or monitoring. PHDK does not add CI/task workflows, cron triggers, scheduled deployments, or maintenance agents. Product endpoints and diagnostics remain application code, verified locally as described in `VERIFICATION_LOOP.md`.

---

## Deploy Rollback Runbook

Rollback stays in the repository and existing GitHub deployment path. PHDK does not perform provider-side rollback or mutate the production database. Requested reads of existing incident deployment metadata/logs remain subject to `EXECUTION_SCOPE.md` — **Bounded read-only provider diagnostics**.

### If a deploy is bad

1. Inspect the relevant commits and migration files. Identify a code revert or corrective patch and flag any schema-compatibility uncertainty; do not infer the live database state.
2. Prepare a reviewable `git revert` or corrective change on the appropriate branch, following the existing authorization and review flow. Do not rewrite history.
3. Verify the change locally with static/build checks and applicable isolated tests, then use the authorized GitHub push/merge path so the existing pipeline deploys it.
4. Report the available GitHub evidence, any separately requested bounded log findings, and their limits. Neither proves the agent ran a product test or confirmed recovery. Do not contact `/health`, `/health/deep`, the database, or a provider dashboard to claim recovery.
5. Record the incident, code change, migration caveats, and any unverified external recovery state in `STATUS.md`.

### Never

- Never use a provider rollback or CLI deployment as a shortcut around the authorized GitHub path
- Never represent a code rollback as a database rollback or confirmed runtime recovery

---

## Preview Environments

PHDK does not create, enable, or require preview environments. It does not run browser-based or screenshot-based verification on localhost, previews, or production. A person's optional visual review is external feedback, not a mandatory PHDK gate or evidence the agent may claim as its own.

---

## Environment Variables

Required `.env.example`:

```env
# App
APP_NAME=""
APP_ENV="development"
APP_VERSION="0.0.1"
APP_GIT_SHA=""
APP_BUILD_TIME=""

# Web
NEXT_PUBLIC_API_URL="http://localhost:4000"

# API
PORT="4000"
NODE_ENV="development"

# Database
DATABASE_PROVIDER="postgresql"
DATABASE_URL="postgresql://..."

# Auth — Google OAuth 2.0
GOOGLE_OAUTH_CLIENT_ID=""
GOOGLE_OAUTH_CLIENT_SECRET=""
GOOGLE_OAUTH_REDIRECT_URI="http://localhost:4000/auth/google/callback"
GOOGLE_OAUTH_ALLOWED_DOMAIN=""
AUTH_SESSION_SECRET=""

# Debug
DEBUG_MODE="false"

# Observability (future)
SENTRY_DSN=""
OTEL_EXPORTER_OTLP_ENDPOINT=""

# Payments (future)
STRIPE_SECRET_KEY=""
STRIPE_WEBHOOK_SECRET=""
NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY=""

# Cache/Jobs (future)
REDIS_URL=""
```

---

## Package Scripts

Every app must include:

```json
{
  "scripts": {
    "dev": "...",
    "build": "...",
    "start": "...",
    "lint": "...",
    "typecheck": "...",
    "format": "prettier --write .",
    "format:check": "prettier --check ."
  }
}
```

Root-level Prettier config (`.prettierrc`, `.prettierignore`) lives at the repository root, not duplicated per app. Wire it into the `pre-commit` hook via `lint-staged` per `ENFORCEMENT.md` Git Hooks — formatting is fixed automatically on staged files, not just checked.

Add a `test` script only when `TESTING_STANDARD.md` identifies a concrete need. Tests are local unit or in-process integration checks with test doubles; do not install or run Playwright, Puppeteer, Cypress, Selenium, browser/UI automation, screenshots, or real-service probes for verification.

---

## Versioning

Required format:

```txt
vMAJOR.MINOR.PATCH (shortSHA · UTC build timestamp)
```

Version must be visible in login page, app shell, and admin panel.

Read `VERSIONING.md` for the full versioning standard.

---

## Technology Introduction Rules

Do not introduce any technology outside this stack without:

1. Explicit approval from the project owner
2. A corresponding `ARCHITECTURE_DECISIONS.md` entry
3. A clear reason why the standard stack cannot solve the problem
