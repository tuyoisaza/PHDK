# DEVELOPMENT_RULES.md

## Purpose

This file defines the development principles, workflow rules, and coding standards for this repository.

Every agent and developer must follow these rules on every task, every branch, every commit.

---

## Development Principles

Priorities in order:

1. Correctness
2. Security
3. Maintainability
4. Observability
5. User experience
6. Performance

Do not optimize for performance at the cost of correctness or security.

---

## Branching Rules

Branch naming:

```txt
feature/<feature-name>
fix/<issue-name>
chore/<task-name>
checkpoint/<date>
```

Rules:

- Never commit directly to `main`
- Every feature starts in a feature branch
- Every agent and subagent works on its own branch
- Merge only after validation passes
- Every major update creates a checkpoint branch named `checkpoint/YYYY-MM-DD` as a recoverable backup
- Version increments on merge to `main`, not on every feature branch commit
- Deployment is triggered by GitHub push to `main` — never from local CLI

---

## Commit Rules

Commit message format:

```txt
v0.4.12 feat(admin): add debug report panel
v0.4.13 fix(auth): enforce role check on admin users route
v0.4.14 chore(i18n): add language translations
```

Rules:

- Include the current version in every commit message
- Use `feat`, `fix`, `chore`, `refactor`, `test`, `docs` prefixes
- Scope to the feature or area changed
- Keep messages short and specific
- Do not create noisy version bumps for every minor feature branch commit

---

## File Size Rules

- Hard maximum: 600 lines
- Preferred maximum: 300 lines
- Split large files by responsibility
- Keep functions small and purposeful
- Do not create junk-drawer utility files

---

## Monorepo Rules

Structure:

```txt
apps/
  web/             — Next.js frontend
  api/             — NestJS + Fastify backend
  mobile/          — Expo placeholder only
packages/
  ui/              — shared UI components
  types/           — shared TypeScript types
  validators/      — shared Zod schemas
  api-client/      — typed API client
  design-tokens/   — shared design tokens
  observability/   — logging and diagnostics wrappers
  db/              — Drizzle schema, migrations, database client when needed
  auth/            — shared auth utilities and types
  config/          — shared config actually used by apps/packages
```

Rules:

- Use pnpm workspaces
- Use Turborepo for build orchestration
- Both `apps/web` and `apps/api` deploy as separate Railway services
- Both services use the repository root — never set Railway root to `apps/web` or `apps/api`
- `apps/mobile` is a placeholder only — do not build unless explicitly tasked
- Shared code lives in `packages/*` — never duplicate across apps
- Use `BUILD_APP_FOUNDATION_PROMPT.md` for the initial scalable app foundation

---

## Feature Structure Rules

Every substantial feature should be organized as:

```txt
src/features/<feature-name>/
  components/
  services/
  repositories/
  schemas/
  permissions/
  logs/
  types.ts
```

A feature is not complete unless relevant required parts are included:

- Route
- UI with all states
- Server-side permissions when protected
- Validation with Zod where input exists
- i18n keys if i18n is enabled
- Structured logging for important actions
- Empty, loading, error, and success states

---

## Route Rules

Every meaningful feature gets a dedicated route.

Good:

```txt
/admin/users
/admin/roles
/admin/debug
/settings/profile
/reports/sales
```

Avoid:

```txt
/admin#users
/admin?tab=roles
```

Tabs are acceptable only when the parent route is accessible and the tab content is secondary.

---

## Database Rules

ORM: Drizzle.

PostgreSQL is the only supported database in every environment — development, staging, and production.

SQLite is never allowed in any environment. Do not scaffold, configure, or rely on it.

Drizzle is required because it supports multiple database providers, so a future provider switch stays configuration-driven.

Switching database provider must be configuration-driven and must never require app-level logic changes.

Never manually mutate production schema without a migration.

Never commit migration files without testing them locally first.

Core record fields where appropriate:

```txt
id
created_at
updated_at
created_by
updated_by
deleted_at     — for soft delete on important records
```

---

## Authentication and Authorization Rules

- Authentication: WorkOS or Clerk when login is required
- Google SSO should be supported when login is required
- Sessions must be secure, provider-compatible, and validated server-side
- Database-backed sessions are required only when the chosen auth provider or product requirements require them
- Authorization must be enforced server-side on every protected route and API endpoint
- Hiding UI elements is not authorization
- Role escalation must be blocked at the server layer

---

## Validation Rules

- Use Zod for input validation
- Validate at the API boundary, not only in the UI
- Never trust client-supplied data without server-side validation
- Share Zod schemas between `apps/web` and `apps/api` via `packages/validators`

---

## Logging Rules

Use structured logs for every important action.

Every log entry must include where applicable:

```txt
event name
timestamp
environment
version
correlation ID
user ID
user role
route or operation
result
```

Never log:

```txt
passwords
tokens
cookies
API keys
authorization headers
sensitive PII unless explicitly approved and redacted
```

---

## Error Rules

Errors must include:

- Stable error code
- Human-readable message
- Technical message where safe to expose
- Correlation ID
- Severity level
- Remediation hint where useful

---

## Debug Rules

When debug mode is active:

- Functions emit more verbose structured logs
- Diagnostic payloads include more context
- Sensitive values are still redacted
- Debug mode activation is always audited when auth/admin exists
- Debug mode never activates in production by default

---

## i18n Rules

If i18n is enabled for the project:

- No hardcoded user-facing strings are allowed
- All strings use the i18n system
- Supported languages are defined per project in the PHDK kit
- Fallback order: user locale → app default → English
- Use locale-aware formatting for dates, numbers, currency, and pluralization
- Design must accommodate longer translated strings without breaking layout

If i18n is not enabled yet:

- User-facing strings must be centralized and easy to extract later

---

## Data Rules

Production must never show fake data as real.

Allowed states:

- Empty state
- Setup required state
- Missing integration state
- Loading state
- Error state

Never allowed:

- Fake KPIs
- Random numbers
- Demo analytics
- Placeholder totals without clear disclosure

---

## Definition of Done

A task is done only when:

- It works with real data or honest empty states
- Route exists when the task requires one
- Permissions are enforced server-side when protected
- i18n keys are present if i18n is enabled
- Logs are structured for important actions
- Debug behavior is considered
- Accessibility basics are covered
- Zod validation exists at API boundary where inputs exist
- All states are handled: loading, empty, error, success
- No file exceeds 600 lines
- Build, typecheck, and lint pass, or failures are reported honestly
- Tests are added where useful
- `TASK.md` expected final report is completed
