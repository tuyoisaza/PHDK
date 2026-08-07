# AGENTS.md

## Purpose

This file defines the operating rules for AI agents, developers, and automation tools working on this repository.

Every agent must read this file before making changes. The goal is simple: every agent understands the product architecture, coding standards, release process, debug expectations, and quality rules before touching a file.

---

## Required Reading Order

Before starting any task, read the full onboarding stack in this order:

1. `ONBOARDING_AI_DEVELOPER.md`
2. `AI_DEVELOPER_OPERATING_MODEL.md`
3. `AGENTS.md` — this file
4. `DEVELOPMENT_RULES.md`
5. `DESIGN_RULES.md`
6. `TECHNICAL_STACK.md`
7. `DEVSECOPS.md`
8. `VERSIONING.md`
9. `VERIFICATION_LOOP.md`
10. `DEBUG_DIAGNOSTICS_STANDARD.md`
11. `TASK.md`
12. `STATUS.md`

Work only within the scope defined in `TASK.md`.

Do not touch out-of-scope files unless the task explicitly requires it.

---

## AI Developer Operating Model

Agents must work in small, user-visible, verified working slices.

Autonomous mode is enabled by default inside the current approved slice.

Agents must show verification evidence after each slice.

Agents must update `STATUS.md` after meaningful progress.

Agents must not continue silently after failed verification.

Agents must stop and ask before destructive data actions, auth-provider changes, payment behavior changes, tenant-model changes, deployment-architecture changes, or scope expansion.

Read `AI_DEVELOPER_OPERATING_MODEL.md` and `AGILE_SLICE_WORKFLOW.md` for the full operating doctrine.

---

## Core Agent Rules

- Work in feature branches. Never commit directly to `main`.
- Never deploy from local CLI. Deployment is triggered by GitHub push to `main`.
- Do not create mock dashboards, fake KPIs, random metrics, or demo data in production code.
- Every user-facing feature must have a real route.
- Every feature must enforce RBAC server-side when roles exist.
- Every user-facing string must use the i18n system.
- Every important action must be logged with structured logs.
- Debug-aware functions must become more verbose when debug mode is active.
- No file may exceed 600 lines. Prefer files under 300 lines.
- Business logic must not live inside page components.
- Version must be visible in app shell, login page, and admin panel.
- Version must include a copy diagnostics button and clear cache button.
- Do not implement infrastructure marked as ready unless the current task explicitly requires it.
- Do not upgrade dependencies unless the task explicitly asks for it.
- Do not change database schema without a migration.
- Do not perform destructive actions unless explicitly approved in `TASK.md`.

---

## Public-Only Project Rule

Public-only websites are not app-style authenticated products unless the PHDK explicitly defines login, private workflows, dashboards, or dynamic user-specific behavior.

If the project is a public marketing site, landing page, or content site:

- Do not add login
- Do not add dashboards
- Do not add user accounts or CRUD
- Do not add admin panels
- Do not add role management
- Do not add session management
- Keep the product focused on public content and public workflows

---

## Monorepo Structure

```txt
apps/
  web/          — Next.js frontend
  api/          — NestJS + Fastify backend
  mobile/       — Expo placeholder only, do not build unless tasked
packages/
  ui/           — shared UI components
  types/        — shared TypeScript types
  validators/   — shared Zod schemas
  api-client/   — typed API client
  design-tokens/ — spacing, colors, typography, radius, shadows, motion
  observability/ — logger and diagnostics wrappers
  db/           — Drizzle schema, migrations, database client
  config/       — shared config
```

Both `apps/web` and `apps/api` deploy as separate Railway services using the repository root.

Never set Railway root directory to `apps/web` or `apps/api`.

---

## Authentication Standard

Default authentication: custom Google OAuth 2.0.

Do not use WorkOS, Clerk, Supabase Auth, Firebase Auth, Auth.js, or any managed auth provider unless the project explicitly overrides this in `ARCHITECTURE_DECISIONS.md`.

When login is required:
- Implement Google OAuth 2.0 directly
- Use database-backed sessions
- Enforce RBAC server-side

Read `DEVSECOPS.md` for the full auth implementation requirements.

---

## Required Product Baseline

Every app-style product must include:

- Project name and logo in top-left UI shell
- Visible app version in shell, login page, and admin panel
- Version badge with copy diagnostics button and clear cache button
- Google OAuth 2.0 login when login is required
- RBAC with server-side enforcement when roles are required
- Admin section when explicitly required by PHDK
- Debug mode with copy diagnostics capability
- Structured logging
- Audit trail for sensitive actions
- i18n support for configured project languages

---

## Required Roles

Minimum role set when RBAC is required:

```txt
super_admin
admin
team_leader
member
```

Authorization must be enforced server-side. Hiding UI elements is not security.

---

## Required Routes

Minimum routes for app-style projects with login:

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

## Debug Mode Requirements

Debug mode is a developer-support capability, not an end-user feature.

When debug mode is active:
- Functions emit verbose structured logs
- Floating panel appears top-left with version number
- Copy diagnostics button copies sanitized diagnostics report
- Clear cache button clears cache, forces logout, reloads page

Read `DEBUG_DIAGNOSTICS_STANDARD.md` for the full specification.

---

## Version Requirements

Version must be displayed in:
- Login page
- Main app shell
- Admin panel

Required format:

```txt
vMAJOR.MINOR.PATCH (shortSHA · UTC build timestamp)
```

Version increments on merge to `main`. Read `VERSIONING.md` for the full standard.

---

## Code Organization Rules

Feature structure:

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

Each feature owns its route, UI, service layer, repository, schemas, permissions, logs, and tests.

---

## Agent Completion Checklist

Before marking any task complete, verify:

- [ ] Working slice user-visible outcome is confirmed
- [ ] Verification evidence produced — commands, health check, browser
- [ ] Route exists
- [ ] Permissions enforced server-side
- [ ] i18n strings exist for configured languages
- [ ] Loading state exists
- [ ] Empty state exists
- [ ] Error state exists
- [ ] Structured logs exist
- [ ] Debug mode behavior considered
- [ ] No fake data presented as real
- [ ] No file exceeds 600 lines
- [ ] Build, typecheck, and lint pass
- [ ] `STATUS.md` updated
- [ ] `TASK.md` expected final report written
- [ ] Next slice proposed

---

## Things Agents Must Never Do

- Claim a task is complete without verification evidence
- Present fake data as real production data
- Create files over 600 lines
- Put business logic inside page components
- Hardcode user-facing strings
- Commit directly to `main`
- Deploy from local CLI
- Expose secrets in logs or debug reports
- Install WorkOS, Clerk, or managed auth vendors without explicit approval
- Implement infrastructure marked as ready unless explicitly tasked
- Change database schema without migrations
- Touch files outside the scope defined in `TASK.md`
- Continue silently after failed verification
- Perform destructive actions without explicit approval
