# TECHNICAL_STACK.md

## Purpose

This file defines the canonical technical stack for all products built on this standard.

Every agent must treat this file as the source of truth for technology choices. Do not introduce new dependencies outside this stack without explicit approval and a corresponding entry in `ARCHITECTURE_DECISIONS.md`.

---

## Monorepo

```txt
Package manager:    pnpm
Build system:       Turborepo
Language:           TypeScript (strict mode)
Node minimum:       20.x
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

PHDK's stack is fixed — TypeScript strict mode, pnpm workspaces, Turborepo — so language detection is not a per-project decision. The canonical language server is `typescript-language-server` (wrapping `tsserver`), the ecosystem-standard choice, driven by a root `tsconfig.json` with project references across `apps/*` and `packages/*`.

### Required setup

- `typescript-language-server` (or the current tool's built-in TS support, e.g. VS Code/Cursor's bundled TS server) is installed and configured — as a dev tool, not a runtime dependency
- Root `tsconfig.json` uses project references or path mapping that covers every `apps/*` and `packages/*` workspace, so cross-package go-to-definition and find-references work, not just within a single package
- The server resolves Drizzle-generated types from `packages/db` — if it can't, hover and go-to-definition on database queries silently degrade to `any`
- The server resolves Next.js's generated types (`next-env.d.ts`) and NestJS's decorator metadata (`experimentalDecorators`, `emitDecoratorMetadata` in `tsconfig.json`)
- Reuse the existing `tsconfig.json`/`tsconfig.base.json` — never create a second, conflicting TypeScript config to make a tool happy

### Required verification

Before treating LSP setup as done, confirm on at least one real symbol in the project (not a synthetic test file):

- Diagnostics/errors surface correctly
- Go to definition works, including across package boundaries (e.g. from `apps/api` into `packages/db`)
- Find references works
- Symbol rename works
- Hover/type information works
- Workspace symbol search works

### The non-obvious part

A working editor LSP does not mean the AI coding agent has the same capability. Confirm explicitly whether the current AI tool has direct LSP access (a dedicated tool/MCP integration) or only text/grep-based search standing in for it — these are not equivalent. Grep-based "find references" misses re-exports, path aliases, and dynamic access that a real LSP catches, and "no other usages found" claims built on it are weaker than they sound. Report which one is actually available — see `VERIFICATION_LOOP.md` Honest Reporting Rule.

### When to run this

Set up and fully verify once, during the app foundation build (`BUILD_APP_FOUNDATION_PROMPT.md` Quality Gates). After that, a session only needs a quick smoke-check — confirm diagnostics and go-to-definition still work on a real symbol — not the full verification loop every time. Re-run full verification if `tsconfig.json` changes, a new workspace package is added, or the AI tool itself changes.

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

PostgreSQL is the only supported database for this standard, and it only ever runs in the cloud. Do not scaffold, configure, or rely on SQLite in any environment. Do not run PostgreSQL on a developer's machine in any form — no Docker container, no local install, no `localhost` database of any kind. Local development points `DATABASE_URL` at a real, cloud-hosted PostgreSQL instance; the developer's machine is only ever a client.

Configuration is environment-driven:

```env
DATABASE_PROVIDER="postgresql"
DATABASE_URL="..."
```

### Local development connects to a cloud database, never a local one

There is no "local database" in this standard — only one kind of PostgreSQL, running in the cloud, that every environment (including a developer's own machine) connects to over the network.

- Local development uses a dedicated Railway-hosted PostgreSQL instance, separate from the production database — provisioned once per project as part of `First-time Railway setup` below, not per developer machine
- A developer's `.env` sets `DATABASE_URL` to that dev instance's Railway connection string; nothing runs locally to serve it
- Never point local development at the production database
- If `DATABASE_URL` is unset or unreachable, the app must fail loudly (e.g. refuse to start, or return `503` from `/health`) rather than falling back to SQLite or an in-memory store — see `QA_CHECKLIST.md` Database

Rules:

- Never mutate schema without a migration
- Never commit migrations without testing against the Railway dev database first
- Core records include: `id`, `created_at`, `updated_at`, `created_by`, `updated_by`
- Important records include soft delete: `deleted_at`
- Drizzle and PostgreSQL are ready but not implemented unless the project phase requires them

### Data Backup Policy

This is about backing up the live application data (the database), not the code. Code backup is always GitHub — that is separate and non-negotiable. This section is only about the database.

Every project must have an explicit data backup policy. Do not assume one and do not skip asking — it is set during PHDK generation (`PROJECT_HANDOFF_TO_DEVELOPMENT_KIT_PROMPT.md` Question 3) and recorded as a decision in `ARCHITECTURE_DECISIONS.md`.

Recommended default when the developer has no preference — pick one:

```txt
Option A — Weekly email export
Every Monday, a scheduled job exports a full SQL dump of the database
and emails it to the developer's configured address. If the database
holds PII or other sensitive data, the dump is encrypted or
password-protected before it is emailed.

Option B — Weekly git backup branch
Every Monday, a scheduled job exports a full SQL dump and commits it
to a dated backup branch (e.g. backup/2026-08-10) in the same private
repository. Backup branches are never pushed to a public repository.
Old backup branches are pruned per a stated retention window.
```

Both are intentionally minimal. A production system with meaningful data should graduate to managed provider backups (e.g. Railway/PostgreSQL automated backups, point-in-time recovery) as soon as that is available — but nothing here is scaffolded until the database itself exists and the project phase requires it.

Required regardless of which option is chosen:

- Backup job failures are logged and surfaced, never silent
- Minimum retention: last 4 weekly backups, unless the developer specifies otherwise
- The chosen policy is documented in `ARCHITECTURE_DECISIONS.md`
- A restore has been tested at least once before the policy is considered verified — see `QA_CHECKLIST.md` Database

See `DEVSECOPS.md` Data Backup and Recovery Safety for the security requirements around backup exports.

---

## Data Import / Intake Pipeline

Any feature that ingests data from files, spreadsheets, or exports — from multiple source types, or on a recurring cadence (monthly closes, nightly syncs, repeated manual uploads) — uses a stateful intake pipeline, not a direct insert-and-forget import. Do not wire an upload straight into business tables with no batch identity, no review step, and no way to undo a bad import short of a manual `DELETE`.

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

Data Import / Intake Pipeline is not scaffolded unless the project explicitly imports data from multiple sources or on a recurring cadence — see `QA_CHECKLIST.md` Data Import / Intake QA.

---

## Authentication — Custom Google OAuth 2.0

Default authentication method: custom Google OAuth 2.0.

PHDK does not use paid authentication vendors by default.

When login is required, implement Google OAuth 2.0 directly using credentials created in Google Cloud Console.

Do not scaffold WorkOS, Clerk, Supabase Auth, Firebase Auth, Auth.js, or any other managed auth provider unless the project explicitly overrides this standard in `ARCHITECTURE_DECISIONS.md`.

```txt
Provider:           Custom Google OAuth 2.0
Sessions:           database-backed
Authorization:      server-side RBAC when roles exist
```

### Google OAuth credential setup

Before implementing login, create credentials manually:

1. Go to `https://console.cloud.google.com/`
2. Create or select the Google Cloud project for this app
3. Go to `Google Auth Platform` → `Branding`
4. Configure consent screen: app name, support email, authorized domains, developer contact email
5. Go to `Google Auth Platform` → `Clients`
6. Create a new client — Application type: Web application
7. Add Authorized JavaScript origins:
   - Local: `http://localhost:3000`
   - Production: `https://[production-domain]`
8. Add Authorized redirect URIs:
   - Local: `http://localhost:4000/auth/google/callback`
   - Production: `https://[api-production-domain]/auth/google/callback`
9. Save and copy credentials to environment variables
10. Never commit OAuth credentials
11. Add all required variables to Railway for the API service

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
- **Pricing is visible** — the AI management section includes a "refresh model pricing" action that fetches current per-model pricing and shows cost per model currently in use
- **Every call is tracked** — see AI Token & Cost Observability below; this is built into `packages/ai` itself, not something each feature implements separately
- Cost and loop safeguards from `DEVSECOPS.md` Cost and Consumption Safety apply to every LLM call

See `AGENTS.md` Required Routes (`/admin/ai`) and `QA_CHECKLIST.md` AI / LLM Configuration QA.

AI/LLM integration is not scaffolded unless the project explicitly requires it.

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

## Deployment

```txt
Platform:           Railway
Trigger:            GitHub push to main
Services:           two Railway services
  @repo/web         — apps/web
  @repo/api         — apps/api
Root directory:     repository root for both services
```

Rules:

- Never deploy from local CLI
- Both Railway services use the repository root
- Never set Railway root to `apps/web` or `apps/api`
- Environment variables are set in Railway dashboard, never committed
- `apps/mobile` is never deployed unless explicitly tasked

Railway commands:

```bash
# API service
pnpm --filter @repo/api build
pnpm --filter @repo/api start

# Web service
pnpm --filter @repo/web build
pnpm --filter @repo/web start
```

### First-time Railway setup

This is the only supported path to a running deployment. There is no other way to get a first deploy live.

1. Commit the project through the normal branch and commit rules in `DEVELOPMENT_RULES.md`, with the version bumped per `VERSIONING.md`.
2. Push to GitHub. `main` must be current before connecting anything to Railway.
3. In the Railway dashboard, create a new project and choose "Deploy from GitHub repo." Authorize Railway's GitHub App if this is the first time, and select this repository. Do not use `railway up`, the Railway CLI's deploy command, or drag-and-drop a local build/tarball — none of those create the GitHub-connected pipeline this standard requires, and both silently violate "never deploy from local CLI."
4. Inside that Railway project, create two services from the same connected repo — `@repo/api` and `@repo/web`. Both services point at the same repo.
5. For each service, set Root Directory to the repository root (`/`) — never `apps/web` or `apps/api`. Set Build Command and Start Command to the matching pair from Railway commands above (e.g. `pnpm --filter @repo/api build` / `pnpm --filter @repo/api start` for the API service).
6. Set environment variables for each service in the Railway dashboard, from `.env.example` — never commit real values.
7. Railway auto-deploys once the GitHub connection and both services are configured — no manual "deploy" action is needed beyond this setup. Every push to `main` after this point triggers a new deploy on its own.
8. Verify the deploy actually worked: hit the API service's public `/health` endpoint and confirm the response matches `VERIFICATION_LOOP.md` Health Check Standard, then confirm the web service can reach the API through its public URL (`NEXT_PUBLIC_API_URL` pointed at the deployed API, not `localhost`).

After this one-time setup, deployment is fully push-triggered — there is nothing left to do in the Railway dashboard for a normal release.

### First-time Railway database setup

This provisions the cloud PostgreSQL instance that local development connects to — see `Database` above. Do this once per project, not once per developer.

1. In the same Railway project, add a PostgreSQL database service (`+ New` → `Database` → `PostgreSQL`). This is the **dev/staging database** — it is separate from whatever PostgreSQL instance backs the production deploy, and it is the only database any developer's machine is ever allowed to connect to.
2. Copy its connection string from the Railway dashboard (`Postgres` service → `Connect` → `Connection URL`).
3. Set `DATABASE_URL` to that connection string in each developer's local `.env` — never commit it. No local PostgreSQL server, Docker container, or SQLite fallback is scaffolded; the local `.env` is the only local artifact involved.
4. Run migrations against it (`Drizzle Kit`) before any schema change is committed — this is the "test locally" step required elsewhere in this standard, and it means testing against this cloud instance, not a machine-local one.
5. Production gets its own separate PostgreSQL service (or an external managed provider) with its own `DATABASE_URL`, set only in the production service's Railway environment variables — never shared with the dev database and never present in a developer's `.env`.

---

## Deploy Rollback Runbook

Migration rollback notes (`QA_CHECKLIST.md` Migrations and Rollback) cover schema changes. This covers the app deploy itself: what to do when the code just shipped by a push to `main` is bad in production.

Because deployment is fully automatic on every push to `main` (`First-time Railway Setup` above), a bad deploy needs an equally fast, equally well-known way back — not something invented under pressure the first time it happens.

### If a deploy is bad

1. In the Railway dashboard, open the affected service's Deployments tab and redeploy the last known-good deployment — Railway keeps prior build artifacts, so this does not require a new git push or a new build.
2. In parallel, revert the bad commit on `main` (`git revert`, not `git reset` — see `VERSIONING.md` Stop-and-Ask Conditions on rewriting history) so the next automatic deploy from a future push doesn't reintroduce the same bug. The dashboard rollback in step 1 buys time; the revert is what actually fixes `main`.
3. If the bad deploy included a migration that already ran against the production database, the code rollback alone is not sufficient — check whether the migration is backward-compatible with the previous code version before rolling back. A migration that dropped a column the previous code still reads from is not safely reversible by redeploying old code alone; see `QA_CHECKLIST.md` Migrations and Rollback.
4. Confirm recovery against `/health` and `/health/deep` per `VERIFICATION_LOOP.md` before considering the incident resolved.
5. Record what happened in `STATUS.md` — what broke, how it was caught, and what the fix or process gap was, so the next session (or the next AI developer) has the context.

### Never

- Never treat "push a fix forward" as the only option when a dashboard rollback to the last-good build is faster and safer for a production-impacting bug
- Never roll back the app deploy without checking migration compatibility first — a code-only rollback against an incompatible schema state can be worse than the original bug

---

## Preview Environments

Only two Railway environments exist by the standard defaults: the dev/staging database from `First-time Railway database setup` above (used by every developer's local machine and by CI) and production. There is no PR-level preview deploy by default — a human reviewing a slice before merge (`QA_CHECKLIST.md` Human Diff Review) verifies against localhost, per `VERIFICATION_LOOP.md` Browser verification, not against a deployed preview.

This is a deliberate default, not an oversight: a Railway PR-environment service per open branch has a real, ongoing cost, and most PHDK projects do not need it. If a project wants one:

- Enable Railway's PR environments (or an equivalent Railway service configured to deploy feature branches) as an explicit, approved addition — this is an "adding new external services"-adjacent decision per `AI_DEVELOPER_OPERATING_MODEL.md` Stop-and-Ask Conditions, and belongs in `ARCHITECTURE_DECISIONS.md` once approved
- A PR preview environment still points at the same shared dev/staging database from `First-time Railway database setup`, unless the project explicitly provisions a separate ephemeral database per preview — decide and record which, since concurrent previews sharing one dev database can collide on schema/migration state
- A preview environment is never a substitute for the Human Diff Review gate — it makes that review easier (a real deployed URL instead of localhost), it does not replace someone reading the diff

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
    "test": "...",
    "format": "..."
  }
}
```

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
