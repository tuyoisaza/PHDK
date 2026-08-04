# TECHNICAL_STACK.md

## Purpose

This file defines the canonical technical stack for all products built on this standard.

Every agent must treat this file as the source of truth for technology choices. Do not introduce new dependencies outside this stack without explicit approval and a corresponding entry in `ARCHITECTURE_DECISIONS.md`.

---

# Monorepo

## Core Stack

```txt
Package manager:    pnpm
Build system:       Turborepo
Language:           TypeScript (strict mode)
Node minimum:       20.x
Node preferred:     22.x
```

## Structure

```txt
apps/
  web/        — Next.js frontend
  api/        — NestJS + Fastify backend
  mobile/     — Expo placeholder only, do not build unless tasked

packages/
  ui/              — shared UI components and primitives
  types/           — shared TypeScript types
  validators/      — shared Zod schemas
  api-client/      — typed API client used by web and mobile
  design-tokens/   — spacing, colors, typography, radius, shadows, motion
  observability/   — structured logger and diagnostics wrappers
  db/              — Drizzle schema, migrations, database client
  auth/            — shared auth utilities and types
  config/          — shared config actually used by apps/packages
```

## Package Boundary Rules

- `apps/*` may depend on `packages/*`
- `packages/*` must not depend on `apps/*`
- `packages/types` must remain app-agnostic
- `packages/validators` must remain app-agnostic
- shared logic must live in `packages/*`
- never duplicate shared schemas or utilities across apps

---

# Frontend — `apps/web`

## Stack

```txt
Framework:          Next.js (App Router)
Language:           TypeScript
Styling:            Tailwind CSS
Components:         shadcn/ui-compatible
Validation:         Zod (shared from packages/validators)
i18n:               next-intl
State:              React built-ins first, Zustand only if needed
```

## Rules

- Use App Router, not Pages Router
- Server Components by default
- Client Components only when needed
- No business logic inside page components
- No hardcoded user-facing strings
- All strings go through `next-intl`
- Images must use Next.js `Image` where applicable

---

# Backend — `apps/api`

## Stack

```txt
Framework:          NestJS
HTTP adapter:       Fastify
Language:           TypeScript
Validation:         Zod (shared from packages/validators)
API style:          REST
```

GraphQL is allowed only if explicitly required.

## Rules

- Validate all inputs at the API boundary using Zod
- Enforce authorization server-side on every protected endpoint
- Never trust client-supplied data without validation
- Use structured logging on every important action
- Never expose raw error internals to clients

---

# Database — `packages/db`

## Stack

```txt
ORM:                Drizzle
Database:           PostgreSQL (always)
Migration tool:     Drizzle Kit
```

## Rules

- PostgreSQL is the only supported database in every environment
- Development, staging, and production all use PostgreSQL
- SQLite is never used in any environment — local or otherwise
- Drizzle is used as the ORM because it supports multiple database providers, keeping the door open for a future provider switch
- Database provider switching must remain configuration-driven and must never require app-level logic changes
- Never mutate schema without a migration
- Never commit migrations without testing them locally first
- Core records include:
  - `id`
  - `created_at`
  - `updated_at`
  - `created_by`
  - `updated_by`
- Important records should include soft delete:
  - `deleted_at`

## Migration Rules

- Every schema change requires a migration
- Every migration requires rollback notes
- Destructive schema changes require explicit approval
- Migrations must be tested locally before merge

---

# Authentication and Authorization

## Provider

Allowed providers:

- WorkOS
- Clerk
- Auth.js only if explicitly approved

## Provider Selection Rule

Each project must choose exactly one primary auth provider before implementation starts.

Do not scaffold multiple auth providers unless the task explicitly requires migration or comparison support.

## Auth Requirements

```txt
SSO:                Google login required
Sessions:           database-backed where applicable
Authorization:      server-side RBAC
```

## Required Roles

```txt
super_admin
admin
team_leader
member
```

## Rules

- Authentication is handled by the selected provider
- Google SSO must be supported from day one
- Authorization must be enforced server-side on every protected route and endpoint
- Hiding UI is not authorization
- Role escalation must be blocked at the server layer
- Shared auth utilities live in `packages/auth`

---

# Validation — `packages/validators`

## Stack

```txt
Library:    Zod
```

## Rules

- All Zod schemas live in `packages/validators`
- Schemas are shared between `apps/web` and `apps/api`
- Never duplicate schemas across apps
- Validate at API boundaries, not only in UI
- Use Zod for environment variable validation
- Applications must fail fast on startup when required environment variables are missing or invalid

---

# Logging — `packages/observability`

## Style

```txt
structured JSON logs
```

## Required Fields

Every important log entry must include where applicable:

```txt
event
timestamp
environment
version
correlation_id
user_id
user_role
route
result
```

## Never Log

- passwords
- tokens
- cookies
- API keys
- authorization headers
- sensitive PII unless explicitly approved and redacted

---

# Observability

## Status

```txt
Error tracking:     Sentry-ready
Tracing:            OpenTelemetry-ready
Health checks:      /health endpoint required on apps/api
```

## Meaning of “Ready”

“Ready” means the architecture and environment variable slots are reserved.

Do not install, initialize, or scaffold Sentry or OpenTelemetry until explicitly tasked.

## Rules

- Every API service must expose `/health`
- Correlation IDs must flow through every request
- Version-aware and environment-aware logs are required

---

# API Contracts

- API contracts must be typed and validated with shared Zod schemas
- Breaking API changes require migration notes or versioning strategy
- Shared request/response schemas should live in `packages/validators`

---

# Payments

## Status

```txt
Provider:   Stripe-ready
```

Stripe must not be scaffolded unless the project explicitly requires payments.

---

# Deployment

## Platform

```txt
Platform:           Railway
Trigger:            Hosting provider detects GitHub push to main
Services:           two Railway services
  @repo/web         — apps/web
  @repo/api         — apps/api
Root directory:     repository root by default
```

## Rules

- Never deploy from local CLI
- Default Railway root is repository root for both services
- Only change Railway root if deployment architecture is explicitly changed and documented
- Environment variables are set in Railway dashboard, never committed to the repository
- `apps/mobile` is never deployed unless explicitly tasked

---

# Environment Variables

## Required `.env.example`

```env
# App
APP_NAME=""
APP_ENV=""
APP_VERSION=""
APP_GIT_SHA=""
APP_BUILD_TIME=""

# Database
DATABASE_URL="postgresql://..."

# Auth — WorkOS
WORKOS_API_KEY=""
WORKOS_CLIENT_ID=""

# Auth — Clerk alternative
NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY=""
CLERK_SECRET_KEY=""

# Auth shared
AUTH_SECRET=""
AUTH_REDIRECT_URI=""

# Observability
SENTRY_DSN=""
OTEL_EXPORTER_OTLP_ENDPOINT=""
```

## Optional — Only If Payments Are In Scope

```env
STRIPE_SECRET_KEY=""
STRIPE_WEBHOOK_SECRET=""
NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY=""
```

---

# Package Scripts

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

# Versioning

## Required Format

```txt
vMAJOR.MINOR.PATCH (shortSHA · UTC build timestamp)
```

Example:

```txt
v0.4.12 (a1b2c3d · 2026-03-23 18:22 UTC)
```

## Required Visibility

Version must be visible in:

- login page
- app shell
- admin panel

## Rules

- Version increments on merge to `main`
- Version does not increment on every feature-branch commit
- Commit messages always start with the current version
- Optional: an auto-bump pre-commit hook can map version to git 1:1. See `VERSIONING.md`. Recommendation, not a rule.

---

# DevSecOps

Security tooling and practices for CI/CD, secrets, supply chain, runtime, and monitoring live in `DEVSECOPS.md`.

Baseline requirements:

- Never commit or log secrets
- Dependency audit, SAST, and secret scanning on pull requests and before release
- Branch protection on `main` with required reviews and status checks
- HTTPS-only production with security headers
- Rate limiting on sensitive endpoints
- Security event auditing
- Rollback path for every release

See `DEVSECOPS.md` for the full baseline.

---

# Technology Introduction Rules

Do not introduce any technology outside this stack without:

- explicit approval from the project owner
- a corresponding `ARCHITECTURE_DECISIONS.md` entry
- a clear reason why the standard stack cannot solve the problem

---

# Final Rule

PostgreSQL is the only supported database for this standard.

SQLite is never allowed in any environment. Do not scaffold, configure, or rely on SQLite anywhere in the repository.

Drizzle is the required ORM because it keeps database-provider switching possible without app-level rewrites. Even though only PostgreSQL is supported today, all database access must go through Drizzle so a future provider change stays configuration-driven.

