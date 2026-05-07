# AGENTS.md

## Purpose

This file defines the operating rules for AI agents, developers, and automation tools working on this repository.

Every agent must read this file before making changes. The goal is simple: every agent understands the product architecture, coding standards, release process, debug expectations, and quality rules before touching a file.

---

# Required Reading Order

Before starting any task, read:

1. `AGENTS.md`
2. `DEVELOPMENT_RULES.md`
3. `DESIGN_RULES.md`
4. `TECHNICAL_STACK.md`
5. `TASK.md`
6. `STATUS.md`

Work only within the scope defined in `TASK.md`.

Do not touch out-of-scope files unless the task explicitly requires it.

---

# Core Agent Rules

- Work in feature branches.
- Never commit directly to `main`.
- Do not deploy from local CLI.
- Deployment must be triggered by the hosting provider detecting a GitHub push to `main`.
- Do not create mock dashboards, fake KPIs, random metrics, or demo data in production code.
- Every user-facing feature must have a real route.
- Every feature must enforce RBAC server-side.
- Every user-facing string must use the i18n system.
- Every important action must be logged with structured logs.
- Debug-aware functions must become more verbose when debug mode is active.
- No file may exceed 600 lines.
- Prefer files under 300 lines.
- Business logic must not live inside page components.
- Version must be visible in app shell, login page, and admin panel.
- Version must include a copy-debug-report action.
- Do not implement infrastructure marked as “ready” unless the current task explicitly requires it.
- Do not upgrade dependencies unless the task explicitly asks for it.
- Do not change database schema without a migration and rollback note.
- Do not perform destructive actions unless explicitly requested in `TASK.md`.

---

# Monorepo Structure

```txt
apps/
  web/          — Next.js frontend
  api/          — NestJS + Fastify backend
  mobile/       — Expo placeholder only; do not build unless tasked

packages/
  core/         — shared types, schemas, utilities
  db/           — Drizzle schema, migrations, database client
  auth/         — shared auth utilities
  logger/       — structured logger
  ui/           — shared UI components
```

`apps/web` and `apps/api` deploy as separate Railway services.

Railway service root should remain the repository root.

Each Railway service must use build/start commands that target the correct app.

Do not set Railway root directory to `apps/web` or `apps/api` unless the project explicitly changes deployment architecture.

---

# Required Product Baseline

Every app-style product must include:

- project name and logo in top-left UI shell
- visible app version in shell, login page, and admin panel
- Google login through the selected auth provider
- RBAC with server-side enforcement
- admin section
- debug mode with copy-debug-report action
- structured logging
- audit trail for sensitive actions
- i18n support for configured project languages

Accepted auth providers must be defined in `TECHNICAL_STACK.md`.

---

# Required Roles

Minimum role set:

- `super_admin`
- `admin`
- `team_leader`
- `member`

Authorization must be enforced server-side.

Hiding UI elements is not security.

---

# Required Routes

Minimum routes for app-style projects:

```txt
/login
/dashboard
/admin
/admin/users
/admin/roles
/admin/debug
/admin/system
/admin/audit
```

Every additional feature must have its own route.

Avoid hash-fragment navigation for primary features.

---

# Debug Mode Requirements

Debug mode must support:

- persistent debug state
- activation scoped to global, tenant, user, or session where applicable
- structured verbose logs when active
- audit trail when debug mode is enabled or disabled
- auto-expiry where possible

The copy-debug-report action must copy sanitized diagnostics including:

- project name
- environment
- version and git SHA
- build timestamp
- client timestamp
- current route
- locale and timezone
- browser info and viewport
- user ID and role if authenticated
- feature flags
- debug mode state
- DB provider
- recent frontend logs
- safe backend diagnostics if available
- errors and correlation ID

Never copy unrestricted raw server logs.

Always redact:

- passwords
- tokens
- cookies
- API keys
- authorization headers
- secrets

---

# Version Requirements

Version must be displayed in:

- login page
- main app shell
- admin panel

Required format:

```txt
vMAJOR.MINOR.PATCH (shortSHA · UTC build timestamp)
```

Example:

```txt
v0.4.12 (a1b2c3d · 2026-03-23 18:22 UTC)
```

Version increments on merge to `main`, not on every feature branch commit.

---

# Code Organization Rules

Feature structure:

```txt
src/features/<feature-name>/
  components/
  services/
  repositories/
  schemas/
  permissions/
  logs/
  tests/
  types.ts
```

Each feature owns:

- route
- UI
- service layer
- repository/data access layer
- schemas
- permissions
- logs
- tests where appropriate

---

# TASK.md Requirements

`TASK.md` must define:

- current objective
- allowed files/folders
- forbidden files/folders
- acceptance criteria
- expected final report format

Agents must not exceed this scope.

---

# STATUS.md Requirements

`STATUS.md` must track:

- current branch
- current version
- completed work
- pending work
- known blockers
- files changed
- validation performed

Agents must update `STATUS.md` when the task requires persistent status tracking.

---

# Agent Completion Checklist

Before marking any task complete, verify:

- [ ] Route exists
- [ ] Permissions are enforced server-side
- [ ] i18n strings exist for configured languages
- [ ] Loading state exists
- [ ] Empty state exists
- [ ] Error state exists
- [ ] Structured logs exist
- [ ] Debug mode behavior was considered
- [ ] No fake data is presented as real
- [ ] No file exceeds 600 lines
- [ ] Build, typecheck, and lint pass or failures are documented
- [ ] Database migrations exist if schema changed
- [ ] Rollback note exists if schema changed
- [ ] `TASK.md` expected final report is written

---

# Final Report Format

Every agent final report must include:

```txt
Summary:
- ...

Files changed:
- ...

Validation:
- ...

Known issues:
- ...

Next recommended step:
- ...
```

---

# Things Agents Must Never Do

- Present fake data as real production data
- Create files over 600 lines
- Put business logic inside page components
- Hardcode user-facing strings
- Commit directly to `main`
- Deploy from local CLI
- Expose secrets in logs or debug reports
- Implement infrastructure marked as “ready” unless explicitly tasked
- Change database schema without migrations
- Touch files outside the scope defined in `TASK.md`
- Upgrade dependencies without explicit task scope
- Perform destructive actions without explicit task scope

