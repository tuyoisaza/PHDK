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

PostgreSQL is the only supported database for this standard. Do not scaffold, configure, or rely on SQLite in any environment — local development connects to a real PostgreSQL instance (e.g. Docker Compose or a Railway local connection).

Configuration is environment-driven:

```env
DATABASE_PROVIDER="postgresql"
DATABASE_URL="..."
```

Rules:

- Never mutate schema without a migration
- Never commit migrations without testing locally first
- Core records include: `id`, `created_at`, `updated_at`, `created_by`, `updated_by`
- Important records include soft delete: `deleted_at`
- Drizzle and PostgreSQL are ready but not implemented unless the project phase requires them

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
