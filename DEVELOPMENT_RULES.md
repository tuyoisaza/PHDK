# DEVELOPMENT_RULES.md

## Purpose

This file defines the development principles, workflow rules, and coding standards for this repository.

Every agent and developer must follow these rules on every task, every branch, every commit.

`EXECUTION_SCOPE.md` governs every action: work on repository code/documentation, use git/GitHub, verify code locally, and use only an existing GitHub-connected deployment pipeline. Product architecture requirements below are source-code requirements; they do not authorize external setup, live verification, or recurring automation. Local code-check hooks remain permitted by `ENFORCEMENT.md`.

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

- Never commit directly to `main`; respect existing GitHub branch protection without changing repository settings — see `ENFORCEMENT.md`
- Every mission starts in a feature branch; planned slices for that mission stay on the same branch
- Every concurrent agent/subagent works on its own branch unless explicitly coordinating through the same mission queue
- Locally verified slice commits may be pushed to the mission branch during the active session
- Merge to `main` only after mission verification and Human Diff Review approval
- Every major update creates a checkpoint branch named `checkpoint/YYYY-MM-DD` as a recoverable backup
- Version increments on every commit, on every branch — see `VERSIONING.md` Version Bump on Every Commit
- A requested deployment is triggered by an approved GitHub push to `main` through the existing connected pipeline — never from local CLI, a local build/tarball upload, a new Actions workflow, or external dashboard configuration
- Do not create schedules, recurring tasks, background agents, dependency bots, or future triggers from a code task
- Update existing dependencies only for a specifically requested update; do not add maintenance bots or scheduled dependency work

See Finetuning Mode below for the one narrow, explicit exception to "never commit directly to `main`."

---

## Finetuning Mode

Finetuning Mode is a narrow, explicit exception to "never commit directly to `main`" above — nothing else changes. It exists for the short window after core development is functionally complete but before the project is in production: rapid, verified, low-ceremony iteration without a branch and review per tweak.

### When it applies

- The project is not yet in production — no real users, no live production traffic. If the project already has a live production deployment serving real users, refuse to activate Finetuning Mode and recommend a sandbox/staging environment instead; production changes always go through the normal branch-plus-review flow, no exceptions.
- Core development is functionally complete. This is for polish, fixes, and small adjustments requested one at a time — not for building new features from scratch.

### How it is activated

- Verbal only, in the current conversation. The developer says something like "activate finetuning mode," or clearly equivalent intent.
- Never assume it is active. It does not persist in `TASK.md`, `STATUS.md`, or any other file, and it is not carried over between sessions or conversations.
- If a new conversation starts and the developer wants it again, they say so again.
- Confirm activation explicitly back to the developer, and if there is any doubt about whether the project might already be in production, ask before proceeding.

### What changes while it is active

- Every other rule in this file and in `AGENTS.md`, `DEVSECOPS.md`, `DESIGN_RULES.md`, `TECHNICAL_STACK.md`, and `QA_CHECKLIST.md` still applies in full. Finetuning Mode relaxes exactly one thing: the branch-per-change and merge-approval requirement.
- `EXECUTION_SCOPE.md` still applies in full. Do not change branch protection or other repository settings to activate this mode, and do not imply that Human Diff Review occurred when it did not.
- For each requested code change: make the change, run the applicable allowed local checks, and only if they pass and existing repository permissions allow it, commit and push directly to `main` through the existing deployment pipeline.
- If tests or checks fail, do not commit or push. Report the failure and fix it, or ask, before touching `main`.
- Still bump version and update `CHANGELOG.md`/`STATUS.md` per `VERSIONING.md` on each push, same as any other merge to `main`.
- Still stop and ask on every condition listed in `DEVSECOPS.md` Stop-and-Ask Conditions and `AI_DEVELOPER_OPERATING_MODEL.md` Stop-and-Ask Conditions — Finetuning Mode does not waive those.

### Ending it

Finetuning Mode ends when the developer says so, or implicitly when the conversation ends. Do not carry it into a new conversation or infer it from `STATUS.md` history.

---

## Commit Rules

Every commit message begins with the version that commit produces. `VERSIONING.md` Commit Message Format is the authoritative definition; this is the short form.

```txt
v0.3.0 feat(auth): add Google OAuth login
v0.3.1 fix(api): handle OAuth callback failure
v0.3.2 refactor(auth): extract session service
v0.3.3 test(auth): add OAuth callback tests
v0.3.4 docs(phdk): update status after login slice
```

Rules:

- Every commit message must begin with `vX.Y.Z` — every commit, on every branch, not only releases or merges to `main`
- Every commit bumps the version by at least a patch, with `package.json` updated in the same commit
- Use `feat`, `fix`, `chore`, `refactor`, `test`, `docs` prefixes
- Scope to the feature or area changed
- Keep messages short and specific

---

## Working Slice Rule

Use `BUILD_APP_FOUNDATION_PROMPT.md` for the initial scalable app foundation.

After the foundation, work in small user-visible verified slices.

Read `AGILE_SLICE_WORKFLOW.md` for the full slice lifecycle.

A working slice is not complete until verification evidence exists.

Read `VERIFICATION_LOOP.md` for source/diff evidence and allowed local lint, typecheck, build, format, and risk-triggered unit/in-process integration checks. Browser testing and live UI/runtime verification are outside scope; state that limitation without turning it into a manual testing gate for the human.

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
- By default, app code targets separate Railway services for `apps/web` and `apps/api` through the project's existing GitHub-connected pipeline
- Both service build configurations target the repository root; do not change live service settings
- Do not create or reconfigure Railway services or connect a repository to a deployment provider
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
- Cloud-hosted PostgreSQL remains the product's database target; implement repository schema, query, and migration code against that contract without connecting to it
- Agent verification does not connect to a database, provision a cloud database, run a database container, or retrieve live credentials. Use pure logic or in-process dependency substitutes for local checks
- Do not start PostgreSQL on a developer's machine or replace the product database with a local test database
- Do not scaffold, configure, or rely on SQLite in any environment
- Author reviewed migrations when the schema changes; do not execute migrations or mutate a live database

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

### User-initiated or multi-source data imports

If an approved feature imports data from multiple source types, supports repeated user-initiated imports, or explicitly requires recurring import code, its code uses the stateful intake pipeline in `TECHNICAL_STACK.md` Data Import / Intake Pipeline. This is a product data model, not an instruction to schedule imports, run maintenance, or execute an import against a live system.

- Never hard-delete imported data to undo a bad import — deactivate the owning batch and let the shared query filter exclude it; rows and files stay in place, deactivation is audited
- Every row a batch import creates carries a reference to that batch
- The product requires explicit user approval of a batch before treating its data as official
- A one-off seed script or single admin-only CSV import with no repeated or recurring execution is exempt from the batch pattern; authoring that code does not authorize running it against a live database

---

## Definition of Done

A working slice is done only when:

- [ ] Approved product outcome is implemented and reviewed in source/diff
- [ ] Applicable local code verification evidence produced
- [ ] Route exists
- [ ] Permissions enforced server-side
- [ ] i18n keys present for all configured languages
- [ ] Logs are structured
- [ ] Debug behavior considered
- [ ] Accessibility basics covered
- [ ] Zod validation exists at API boundary
- [ ] All states handled: loading, empty, error, success
- [ ] No file exceeds 600 lines
- [ ] Applicable local build, typecheck, lint, and format checks pass; risk-triggered unit/in-process integration tests pass when required
- [ ] Browser/UI and live runtime behavior are reported as not verified, without requiring manual tests from the human
- [ ] `STATUS.md` updated
- [ ] `TASK.md` expected final report completed
- [ ] Code mission criteria satisfied, or the next planned code slice is active within this session
- [ ] No recurring work, background agents, CI workflows, external setup, or live service operations were created or performed
