# AGENTS.md

## Purpose

This file is the entry point and router for AI agents, developers, and automation tools working on this repository. It carries only the rules that apply to every task and a map of where the full standards live — it is not the full standards set.

Every agent must read this file first, then follow the reading order below before making changes.

---

## Required Reading Order

Before starting any task, read the full onboarding stack in this order:

1. `ONBOARDING_AI_DEVELOPER.md`
2. `AI_DEVELOPER_OPERATING_MODEL.md`
3. `AGENTS.md` — this file
4. `DEVELOPMENT_RULES.md` — branching, commits, feature structure, monorepo rules
5. `DESIGN_RULES.md` — UI, UX, accessibility, theming
6. `TECHNICAL_STACK.md` — stack, monorepo layout, auth, database, AI/LLM integration, LSP/code intelligence setup
7. `DEVSECOPS.md` — security, auth, secrets, cost safety, LLM guardrails
8. `VERSIONING.md` — version, branch, commit, changelog, release format
9. `VERIFICATION_LOOP.md` — what counts as proof, health checks
10. `DEBUG_DIAGNOSTICS_STANDARD.md` — debug mode, diagnostics report spec
11. `TASK.md`
12. `STATUS.md`

Work only within the scope defined in `TASK.md`. Do not touch out-of-scope files unless the task explicitly requires it.

---

## AI Developer Operating Model

Agents must work in small, user-visible, verified working slices. Autonomous mode is enabled by default inside the current approved slice. Agents must show verification evidence after each slice, update `STATUS.md` after meaningful progress, and never continue silently after failed verification.

Read `AI_DEVELOPER_OPERATING_MODEL.md` and `AGILE_SLICE_WORKFLOW.md` for the full operating doctrine, including the complete Stop-and-Ask list.

---

## Core Agent Rules

- Work in feature branches. Never commit directly to `main` — unless Finetuning Mode is explicitly active for this conversation, see `DEVELOPMENT_RULES.md` Finetuning Mode.
- Never deploy from local CLI — no `railway up`, no dragging a local build/tarball into Railway. Deployment is triggered by GitHub push to `main`, connected once per `TECHNICAL_STACK.md` First-time Railway Setup.
- Do not create mock dashboards, fake KPIs, random metrics, or demo data in production code.
- Every user-facing feature must have a real route.
- Every feature must enforce RBAC server-side when roles exist.
- Every user-facing string must use the i18n system.
- Every important action must be logged with structured logs.
- No file may exceed 600 lines. Prefer files under 300 lines.
- Business logic must not live inside page components.
- Do not implement infrastructure marked as ready unless the current task explicitly requires it.
- Do not upgrade dependencies unless the task explicitly asks for it.
- Do not change database schema without a migration.
- Do not perform destructive actions unless explicitly approved in `TASK.md`.

---

## Public-Only Project Rule

Public-only websites are not app-style authenticated products unless the PHDK explicitly defines login, private workflows, dashboards, or dynamic user-specific behavior.

If the project is a public marketing site, landing page, or content site: do not add login, dashboards, user accounts, admin panels, role management, or session management. Keep the product focused on public content and public workflows.

---

## Monorepo Structure

Standard layout: `apps/web` (Next.js), `apps/api` (NestJS + Fastify), `apps/mobile` (Expo placeholder only), `packages/*` (shared code). Both `apps/web` and `apps/api` deploy as separate Railway services using the repository root — never set Railway root to `apps/web` or `apps/api`.

Full layout and package list: `TECHNICAL_STACK.md` Monorepo.

---

## Authentication Standard

Default authentication: custom Google OAuth 2.0. No managed auth vendor (WorkOS, Clerk, Supabase Auth, Firebase Auth, Auth.js) unless explicitly overridden in `ARCHITECTURE_DECISIONS.md`.

Full implementation requirements: `DEVSECOPS.md` Authentication Standard.

---

## Required Product Baseline

Every app-style product must include:

- Project name and logo in top-left UI shell
- Visible app version in shell, login page, and admin panel, with copy diagnostics button and clear cache button
- Google OAuth 2.0 login when login is required
- RBAC with server-side enforcement when roles are required
- Admin section when explicitly required by PHDK
- AI management section in the admin panel when the project uses any LLM-powered feature
- Debug mode with copy diagnostics capability
- Structured logging and an audit trail for sensitive actions
- i18n support for configured project languages

---

## Required Roles

Minimum role set when RBAC is required: `super_admin`, `admin`, `team_leader`, `member`.

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
/admin/ai         — when the project uses any LLM-powered feature
```

Every additional feature must have its own route. Avoid hash-fragment navigation for primary features.

---

## Debug Mode Requirements

Debug mode is a developer-support capability, not an end-user feature. Full specification, including the copy diagnostics report and auth/metered-API diagnostics fields: `DEBUG_DIAGNOSTICS_STANDARD.md`.

---

## AI/LLM Feature Requirements

Any feature that calls an LLM requires an AI management section at `/admin/ai` (admin-editable prompt and output schema, configurable provider/model, model pricing lookup) plus provider-agnostic config, prompt-injection guardrails, and output validation in code.

Full specification: `TECHNICAL_STACK.md` AI / LLM Integration and `DEVSECOPS.md` LLM Integration Safety.

---

## Version and Code Organization

Version is displayed in the app shell, login page, and admin panel, in `vMAJOR.MINOR.PATCH (shortSHA · UTC build timestamp)` format. Full standard: `VERSIONING.md`.

Every feature is organized under `src/features/<feature-name>/` with its own components, services, repositories, schemas, permissions, logs, and types. Full rules: `DEVELOPMENT_RULES.md` Feature Structure Rules.

---

## Agent Completion Checklist

Before marking any task complete, verify:

- [ ] Working slice user-visible outcome is confirmed
- [ ] Verification evidence produced — commands, health check, browser
- [ ] Route exists and permissions are enforced server-side
- [ ] i18n strings exist for configured languages
- [ ] Loading, empty, and error states exist
- [ ] Structured logs exist
- [ ] No fake data presented as real
- [ ] No file exceeds 600 lines
- [ ] Build, typecheck, and lint pass
- [ ] `STATUS.md` updated, `TASK.md` final report written, next slice proposed

---

## Things Agents Must Never Do

- Claim a task is complete without verification evidence
- Present fake data as real production data
- Create files over 600 lines
- Put business logic inside page components
- Hardcode user-facing strings
- Commit directly to `main` (unless Finetuning Mode is explicitly active — see `DEVELOPMENT_RULES.md` Finetuning Mode)
- Deploy from local CLI — including `railway up` or uploading a local build/tarball to Railway
- Expose secrets in logs or debug reports
- Install WorkOS, Clerk, or managed auth vendors without explicit approval
- Call a metered or paid external API (image generation, LLM calls, SMS, email sending, etc.) without a hard usage cap, timeout, and loop/retry limit — see `DEVSECOPS.md` Cost and Consumption Safety
- Implement infrastructure marked as ready unless explicitly tasked
- Change database schema without migrations
- Touch files outside the scope defined in `TASK.md`
- Continue silently after failed verification
- Perform destructive actions without explicit approval
