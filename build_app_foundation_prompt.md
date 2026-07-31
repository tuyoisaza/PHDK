# BUILD_APP_FOUNDATION_PROMPT.md

## Purpose

This file contains the prompt to give to an AI coding agent after a Project Handoff to Development Kit (PHDK) has been generated.

Its job is to build the initial scalable app foundation for a project using the standard PHDK stack.

This is not a folder-only scaffold.
This is not a fake demo app.
This is not random feature development.

This prompt builds the reusable technical foundation that future product features will be built on.

---

## How to Use This File

1. Create or open the project GitHub repository.
2. Add the PHDK project-specific files to the repository.
3. Fetch the latest standards files from the PHDK standards repo.
4. Open your AI coding agent, such as Claude Code, Cursor, Windsurf, or equivalent.
5. Paste the prompt below as the first build task.
6. The AI coding agent must build the app foundation according to the PHDK project mode.
7. Review the result against `QA_CHECKLIST.md` before starting feature work.

---

# Prompt

## Hard Mode Switch

STOP ANY PREVIOUS TASK.

You are now in **BUILD APP FOUNDATION MODE**.

Your only job is to build the initial scalable app foundation for this project using the PHDK files and standards.

Do not continue any previous task.
Do not build project-specific product features unless explicitly required by `TASK.md`.
Do not create fake dashboards, fake data, fake analytics, fake users, fake payments, fake integrations, or fake business logic.
Do not skip validation.
Do not mark the task complete until the quality gates are checked.

First respond exactly:

```txt
Understood. I am now in BUILD APP FOUNDATION MODE.
Previous tasks are paused.
I will read the PHDK files and standards before making changes.
```

---

## Step 1 — Read Required Files

Before writing or changing code, read these files:

### Project-specific PHDK files

- `README.md`
- `STATUS.md`
- `TASK.md`
- `PROJECT_BRIEF.md`
- `PRD.md`
- `FEATURES.md`
- `NAVTREE.md`
- `PUBLIC_CONTENT.md`
- `PRIVATE_CONTENT.md` if it exists
- `ARCHITECTURE_DECISIONS.md`

### Standards files

- `AGENTS.md`
- `DEVELOPMENT_RULES.md`
- `DESIGN_RULES.md`
- `TECHNICAL_STACK.md`
- `QA_CHECKLIST.md`
- `BUILD_APP_FOUNDATION_PROMPT.md`

After reading, respond with:

```txt
PHDK and standards read.
Project mode identified: [public / authenticated / hybrid / unclear]
Login required: [yes / no / unclear]
Foundation scope understood.
Proceeding with implementation plan.
```

If the project mode or login requirement is unclear, stop and ask one clarifying question before coding.

---

## Step 2 — Identify Project Mode

Use the PHDK files to classify the foundation mode.

### Public mode

Use this when login is not required.

Build a public-facing scalable web app foundation.

Do not build:

- login
- dashboard
- account area
- user CRUD
- roles
- admin panel
- private routes
- session tables
- fake authenticated states

### Authenticated mode

Use this when login and accounts are required.

Build a web app foundation with authentication-ready and role-aware structure.

Build only the auth/account/admin pieces required by the PHDK.

Do not assume every authenticated app needs full SaaS admin CRUD unless the PHDK requires it.

### Hybrid mode

Use this when the project has both public marketing pages and a logged-in app area.

Build:

- public marketing/content shell
- login/account foundation
- private app shell
- role-aware navigation only where required

### Unclear mode

If the PHDK does not clearly identify whether the app is public, authenticated, or hybrid, stop and ask one question before coding.

---

## Step 3 — Standard Technical Architecture

Use the PHDK standard stack:

- pnpm
- Turborepo
- TypeScript monorepo
- `apps/web` — Next.js web app
- `apps/api` — NestJS + Fastify API
- `apps/mobile` — future Expo placeholder only
- `packages/*` — shared core packages
- Tailwind CSS
- shadcn/ui-compatible structure
- Zod validation
- Drizzle/PostgreSQL-ready when persistence is needed
- Redis-ready when jobs/cache are needed
- Stripe-ready only when payments are needed
- WorkOS or Clerk-ready only when login is needed
- OpenTelemetry-ready and Sentry-ready, but not implemented until the relevant task
- Railway deployment from GitHub push to `main`
- Two Railway services:
  - `@repo/web`
  - `@repo/api`

Railway rule:

- both Railway services use the repository root
- never set Railway root directory to `apps/web` or `apps/api`

---

## Step 4 — Required Monorepo Foundation

Create or verify this structure:

```txt
apps/
  web/
  api/
  mobile/
packages/
  ui/
  types/
  validators/
  api-client/
  design-tokens/
  observability/
  db/
  auth/
  config/
.env.example
.gitignore
package.json
pnpm-workspace.yaml
turbo.json
tsconfig.base.json
README.md
```

### Package responsibilities

- `packages/ui` — reusable UI primitives and app-shell components
- `packages/types` — shared TypeScript types
- `packages/validators` — shared Zod schemas
- `packages/api-client` — typed API client used by web now and mobile later
- `packages/design-tokens` — spacing, colors, typography, radius, shadows, motion
- `packages/observability` — logger and diagnostics wrappers
- `packages/db` — database package; implementation only when persistence is required
- `packages/auth` — shared auth utilities and types; implementation only when login is required
- `packages/config` — shared config actually used by apps/packages

Do not create unused placeholder config files.
Do not duplicate shared logic across apps.

---

## Step 5 — Root Workspace Requirements

Use pnpm only.

Do not generate:

- `package-lock.json`
- `npm-shrinkwrap.json`
- `yarn.lock`

Root scripts must include:

```json
{
  "scripts": {
    "dev": "turbo dev",
    "build": "turbo build",
    "start": "turbo start",
    "lint": "turbo lint",
    "typecheck": "turbo typecheck",
    "test": "turbo test",
    "format": "turbo format"
  }
}
```

Use workspace protocol imports for internal packages where appropriate:

```json
{
  "dependencies": {
    "@repo/types": "workspace:*",
    "@repo/validators": "workspace:*",
    "@repo/api-client": "workspace:*"
  }
}
```

Required package names:

- `apps/web` package name: `@repo/web`
- `apps/api` package name: `@repo/api`
- `packages/ui` package name: `@repo/ui`
- `packages/types` package name: `@repo/types`
- `packages/validators` package name: `@repo/validators`
- `packages/api-client` package name: `@repo/api-client`
- `packages/design-tokens` package name: `@repo/design-tokens`
- `packages/observability` package name: `@repo/observability`
- `packages/db` package name: `@repo/db`
- `packages/auth` package name: `@repo/auth`
- `packages/config` package name: `@repo/config`

---

## Step 6 — Build `apps/api`

Build a NestJS + Fastify API foundation.

Required behavior:

- bind to `0.0.0.0`
- read `process.env.PORT`
- default to `4000` locally
- expose public `GET /health`
- return exactly:

```json
{ "status": "ok", "service": "api" }
```

Required API structure:

```txt
apps/api/src/
  main.ts
  app.module.ts
  modules/
    health/
  common/
    guards/
    pipes/
    interceptors/
    filters/
    decorators/
  config/
  observability/
```

Rules:

- use Zod validation at API boundaries where inputs exist
- return structured errors with stable error codes
- log important actions through `@repo/observability`
- do not expose raw error internals to clients
- do not add database/auth/payment/job integrations unless required by the project mode and PHDK task

### If login = yes

Add auth-ready API structure only as required by PHDK.

Allowed:

- current user endpoint if needed
- protected-route guard structure
- role-check utility structure if roles are required
- server-side authorization boundaries

Do not create fake users or fake roles.
Do not create full user CRUD unless required by the PHDK.

### If login = no

Do not create auth endpoints, session endpoints, user management endpoints, role endpoints, or private API routes.

---

## Step 7 — Build `apps/web`

Build a Next.js web foundation.

Required:

- Next.js App Router
- React
- TypeScript strict
- Tailwind CSS
- shadcn/ui-compatible structure
- centralized design tokens from `@repo/design-tokens`
- shared UI primitives from `@repo/ui`
- typed API calls through `@repo/api-client`
- responsive mobile-first layout
- accessibility-ready structure
- light/dark mode readiness
- app version visible in a developer-safe location
- client-side API health check that does not require the API during build

Required route behavior:

- public routes come from `NAVTREE.md`
- do not invent routes not supported by the PHDK
- every meaningful route must handle loading, empty, error, and success states where relevant
- browser zoom must not break layout
- no tiny tap targets
- no inaccessible color contrast

### If login = yes

Build the login/account/private foundation required by the PHDK.

Allowed if required:

- login route
- protected app shell
- account route
- dashboard route
- admin/config route
- role-aware navigation
- private route guards

Do not create full admin modules unless explicitly required.
Do not create fake account data.
Do not create user CRUD unless required.

### If login = no

Build only public routes and public workflows.

Do not create:

- login page
- dashboard
- account area
- admin panel
- role navigation
- user profile pages

---

## Step 8 — Shared Packages

### `packages/types`

Include shared TypeScript types used by both web and API.

Must include `HealthResponse` matching:

```ts
export type HealthResponse = {
  status: "ok";
  service: "api";
};
```

### `packages/validators`

Include shared Zod schemas.

Must include health schema matching:

```ts
{ "status": "ok", "service": "api" }
```

### `packages/api-client`

Build a typed API client consumed by `apps/web`.

Must include a health request helper.

Use `NEXT_PUBLIC_API_URL` as the API base URL.

The web build must not require the API to be reachable.

### `packages/design-tokens`

Define tokens for:

- colors
- spacing
- typography
- radius
- shadows
- motion
- light mode
- dark mode

### `packages/ui`

Build reusable UI primitives only.

Allowed:

- Button
- Card
- AppShell
- VersionBadge
- DebugPanel shell if debug mode is required
- CopyDiagnosticsButton if debug mode is required

Do not build project-specific product UI inside `packages/ui`.

### `packages/observability`

Build a minimal logger and diagnostics wrapper.

Use a tiny wrapper around `console` unless the PHDK explicitly requires a real logging package.

Methods:

- `info`
- `warn`
- `error`
- optional `debug` when debug mode is enabled

Never log:

- passwords
- tokens
- cookies
- API keys
- authorization headers
- secrets
- sensitive PII unless explicitly approved and redacted

### `packages/db`

If persistence is not required yet, keep this documentation-only or minimal.

If persistence is required by the PHDK, implement according to `TECHNICAL_STACK.md` and `DEVELOPMENT_RULES.md`.

PostgreSQL is the only supported database. SQLite is never used in any environment.

Do not add database code just to satisfy a checklist.

### `packages/auth`

Build only when login = yes.

Include shared auth utilities and types consumed by `apps/web` and `apps/api`.

Do not create fake users, fake roles, or fake sessions.

Do not build auth scaffolding when login = no.

### `packages/config`

Include only config files that are actually imported or extended.

Do not create unused placeholder configs.

---

## Step 9 — Debug Foundation

Debug mode is a developer-support capability, not an end-user feature.

### App-style projects

If the project has interactive features, user flows, login, dashboards, forms, workflows, or dynamic behavior, include debug mode foundation.

### Static or public-only projects

If the project is a public marketing site, landing page, or simple content site, include debug mode as a recommended technical note or environment-gated developer utility, not as visible product UI.

### Required behavior when implemented

- debug mode is off by default in production
- debug mode can be enabled only through safe developer/admin control
- functions emit more verbose structured logs when active
- diagnostic payloads include useful context
- diagnostic payloads redact sensitive values
- activation is auditable when login/admin exists

### Copy diagnostics report

If debug diagnostics are implemented, the report must include this sanitized payload:

```txt
project name
environment
version
git SHA
build timestamp
client timestamp
current route
locale and timezone
browser info and viewport
screen size and viewport size
user ID if authenticated
user role if authenticated
auth state if applicable
feature flags
debug mode state
API base URL hostname only
DB provider if available
recent frontend logs
safe backend diagnostics if available
recent client errors
recent API errors with correlation IDs
correlation ID
```

Always redact:

```txt
passwords
tokens
cookies
API keys
authorization headers
secrets
private user data
payment data
sensitive environment variables
full connection strings
raw server logs
```

Never copy unrestricted raw server logs.
Never include full URLs containing tokens or private query parameters.
Never include request or response bodies unless explicitly sanitized.

---

## Step 10 — Environment Setup

Create `.env.example` at repository root.

Minimum:

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

# Debug
DEBUG_MODE="false"
```

Add only relevant future placeholders based on PHDK scope.

Examples:

```env
# Future database
DATABASE_URL=""

# Future cache / jobs
REDIS_URL=""

# Future auth
AUTH_PROVIDER=""
WORKOS_API_KEY=""
CLERK_SECRET_KEY=""

# Future payments
STRIPE_SECRET_KEY=""
STRIPE_WEBHOOK_SECRET=""

# Future observability
SENTRY_DSN=""
OTEL_EXPORTER_OTLP_ENDPOINT=""
```

Do not wire unused services yet.

Create `.gitignore` including:

```txt
.env
.env.local
.env.*.local
node_modules
.next
dist
.turbo
*.db
```

---

## Step 11 — i18n Readiness

Do not hardcode user-facing text in a way that makes future translation difficult.

If the PHDK defines supported languages or requires i18n:

- configure the selected i18n system
- create locale files
- route all user-facing strings through the i18n system
- use locale-aware formatting for dates, numbers, currency, and pluralization

If i18n is not required yet:

- keep user-facing strings centralized and easy to extract later
- do not overbuild full translation infrastructure unless requested

---

## Step 12 — Data Honesty Rules

Production must never show fake data as real.

Allowed states:

- empty state
- setup required state
- missing integration state
- loading state
- error state
- success state with real data

Never allowed:

- fake KPIs
- random numbers
- demo analytics presented as real
- placeholder totals without clear disclosure
- fake users
- fake payments
- fake database records

---

## Step 13 — Documentation Output

Update or create project README documentation explaining:

- how to install
- how to run locally
- how to run web and API together
- how to run typecheck, lint, build, and tests
- app mode: public/authenticated/hybrid
- Railway two-service deployment model
- Railway build/start commands
- required environment variables
- how to use the PHDK files
- how to continue with `TASK.md`

Railway commands must be documented as:

API service:

```bash
pnpm --filter @repo/api build
pnpm --filter @repo/api start
```

Web service:

```bash
pnpm --filter @repo/web build
pnpm --filter @repo/web start
```

Both services must use the repository root.

Do not require GitHub Actions for Railway deployment.

---

## Step 14 — Quality Gates

Before declaring foundation complete, check:

- `pnpm install` runs cleanly from repository root
- `pnpm typecheck` passes or failures are reported honestly
- `pnpm lint` passes or failures are reported honestly
- `pnpm build` passes or failures are reported honestly
- `pnpm dev` runs web and API together through Turborepo
- API binds to `0.0.0.0`
- API uses `process.env.PORT`, defaulting to `4000` locally
- `GET /health` returns exactly `{ "status": "ok", "service": "api" }`
- web can call health endpoint through `@repo/api-client`
- web build does not require the API to be running
- shared types and validators are actually imported and used
- package names use the `@repo/*` names
- internal package dependencies use `workspace:*` where appropriate
- public/private routes match the PHDK login branching rule
- no unauthorized auth/dashboard/admin code exists in public-only mode
- debug mode is off by default in production
- diagnostic reports redact sensitive data
- no fake data is presented as real
- no file exceeds the line limit defined in `DEVELOPMENT_RULES.md`
- no secrets are committed
- README documents Railway repo-root deployment

If a quality gate cannot be run, explain why.

Do not claim success if validation failed or was not run.

---

## Final Report Format

When the app foundation task is complete, respond exactly in this format:

```txt
APP FOUNDATION COMPLETE

Project mode:
[public / authenticated / hybrid]

Repository structure:
[list of created directories and key files]

Routes created:
[list]

API endpoints created:
[list]

Shared packages created:
[list]

Debug foundation:
[implemented / documented only / not applicable + reason]

Quality gates:
[pass/fail/not run for each item]

Warnings or gaps:
[list or "none"]

Next step:
Continue feature development using TASK.md from the PHDK kit.
```

---

## Non-Negotiable Rules

- Build the app foundation, not random product features.
- Respect the PHDK files as the product source of truth.
- Respect the standards files as the technical source of truth.
- Do not invent features.
- Do not fake integrations.
- Do not add auth if login = no.
- Do not add admin/dashboard/user CRUD unless required.
- Do not build mobile app features now.
- Keep `apps/mobile` as a future placeholder only.
- Use pnpm only.
- Use Railway repo-root deployment model.
- Do not set Railway root to `apps/web` or `apps/api`.
- Do not claim success without validation.

