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
checkpoint/YYYY-MM-DD
phdk/vX.Y.Z/short-slice-name
```

Rules:

- Never commit directly to `main`
- Every feature starts in a feature branch
- Every agent and subagent works on its own branch
- Merge only after verification passes and approval is given
- Every major update creates a checkpoint branch named `checkpoint/YYYY-MM-DD` as a recoverable backup
- Version increments on merge to `main`, not on every feature branch commit
- Deployment is triggered by GitHub push to `main` — never from local CLI

---

## Commit Rules

Commit message format:

```txt
feat(auth): add Google OAuth login
fix(api): handle OAuth callback failure
chore(version): bump to v0.3.0
refactor(auth): extract session service
test(auth): add OAuth callback tests
docs(phdk): update status after login slice
```

Rules:

- Use `feat`, `fix`, `chore`, `refactor`, `test`, `docs` prefixes
- Scope to the feature or area changed
- Keep messages short and specific
- Include version in release commits
- Do not create noisy version bumps for every minor feature branch commit

---

## Working Slice Rule

Use `BUILD_APP_FOUNDATION_PROMPT.md` for the initial scalable app foundation.

After the foundation, work in small user-visible verified slices.

Read `AGILE_SLICE_WORKFLOW.md` for the full slice lifecycle.

A working slice is not complete until verification evidence exists.

Read `VERIFICATION_LOOP.md` for what counts as proof.

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
  web/              — Next.js frontend
  api/              — NestJS + Fastify backend
  mobile/           — Expo placeholder only
packages/
  ui/               — shared UI components
  types/            — shared TypeScript types
  validators/       — shared Zod schemas
  api-client/       — typed API client
  design-tokens/    — design tokens
  observability/    — logger and diagnostics
  db/               — Drizzle schema and client
  config/           — shared config
```

Rules:

- Use pnpm workspaces
- Use Turborepo for build orchestration
- Both `apps/web` and `apps/api` deploy as separate Railway services
- Both services use the repository root
- Never set Railway root to `apps/web` or `apps/api`
- `apps/mobile` is a placeholder only
- Shared code lives in `packages/*` — never duplicate across apps

---

## Feature Structure Rules

Every feature must be organized as:

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

A feature is not complete unless it includes:

- Route
- UI with all states
- Server-side permissions
- Validation with Zod
- i18n keys for configured languages
- Structured logging
- Empty, loading, error, and success states

---

## Route Rules

Every meaningful feature gets a dedicated route.

Good:

```txt
/admin/users
/admin/roles
/settings/profile
/reports/sales
```

Avoid:

```txt
/admin#users
/admin?tab=roles
```

---

## Authentication Rules

Default auth: custom Google OAuth 2.0.

Do not use WorkOS, Clerk, Supabase Auth, Firebase Auth, Auth.js, or any managed auth provider unless explicitly approved in `ARCHITECTURE_DECISIONS.md`.

Read `DEVSECOPS.md` for the full auth implementation requirements.

---

## Database Rules

- ORM: Drizzle — required because it keeps a future provider switch configuration-driven
- PostgreSQL only — all environments, including local development, connect to a real PostgreSQL instance
- Do not scaffold, configure, or rely on SQLite in any environment
- Never manually mutate production schema without a migration

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

## Validation Rules

- Use Zod for all input validation
- Validate at the API boundary, not only in the UI
- Never trust client-supplied data without server-side validation
- Share Zod schemas via `packages/validators`

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

Never log passwords, tokens, cookies, API keys, authorization headers, or sensitive PII.

Read `DEBUG_DIAGNOSTICS_STANDARD.md` for copy diagnostics requirements.

---

## Error Rules

Errors must include:

- Stable error code
- Human-readable message
- Technical message where safe to expose
- Correlation ID
- Severity level

---

## i18n Rules

- No hardcoded user-facing strings anywhere in the codebase
- All strings use the i18n system
- Supported languages are defined per project in the PHDK kit
- Fallback order: user locale → app default → English
- Use locale-aware formatting for dates, numbers, currency, and pluralization

---

## Data Rules

Production must never show fake data as real.

Allowed states:

- Empty state
- Setup required state
- Loading state
- Error state
- Success state with real data

Never allowed:

- Fake KPIs
- Random numbers
- Demo analytics presented as real
- Placeholder totals without clear disclosure

---

## Definition of Done

A working slice is done only when:

- [ ] User-visible outcome confirmed in browser or test runner
- [ ] Verification evidence produced
- [ ] Route exists
- [ ] Permissions enforced server-side
- [ ] i18n keys present for all configured languages
- [ ] Logs are structured
- [ ] Debug behavior considered
- [ ] Accessibility basics covered
- [ ] Zod validation exists at API boundary
- [ ] All states handled: loading, empty, error, success
- [ ] No file exceeds 600 lines
- [ ] Build, typecheck, and lint pass
- [ ] `STATUS.md` updated
- [ ] `TASK.md` expected final report completed
- [ ] Next slice proposed
