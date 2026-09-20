# AGENTS.md

## Purpose

This file is the entry point and router for AI agents, developers, and automation tools working on this repository. It carries only the rules that apply to every task and a map of where the full standards live — it is not the full standards set.

Every agent must read this file first, then read the project's `TASK.md` and `STATUS.md`. Load deeper standards only when the current task needs them.

If a session runs long and rules start slipping, re-read `INANUTSHELL.md` — it is the one-line-per-rule condensed version of everything below. It is a memory aid, not a replacement for the task-relevant standards. `ENFORCEMENT.md` is the deeper fix: git hooks, local verification gates, and repository settings reduce dependence on memory.

---

## Universal PHDK Command

When the developer says exactly:

```txt
PHDK upgrade
```

read `PHDK_UPGRADE.md` and execute it immediately. This exact command is explicit approval to fetch the canonical upstream and synchronize PHDK-managed files. Do not ask for a second confirmation. Do not continue into feature work afterward unless separately requested.

---

## Minimum Session Context

For every task, load only this minimum set first:

1. `AGENTS.md` — this file; router and hard rules
2. `TASK.md` — the current slice and allowed scope
3. `STATUS.md` — persistent project state, gaps, and next slices

Do **not** preload the full standards stack on every session. Extra context costs attention and tokens and increases the chance of conflicting instructions. Load the smallest relevant standard set for the task.

Read `ONBOARDING_AI_DEVELOPER.md` when joining a PHDK project for the first time, when the project has materially changed, or when orientation is needed — not as a mandatory per-task read.

### Progressive Standards Router

| When the current task touches | Load |
|---|---|
| slice planning, scope, backlog, or a new ask | `AI_DEVELOPER_OPERATING_MODEL.md`, `AGILE_SLICE_WORKFLOW.md`, `TASK_TRACKING_STANDARD.md`; add `INTENT_CAPTURE_STANDARD.md` when the why is not already captured |
| branching, code organization, dependencies, or general implementation | `DEVELOPMENT_RULES.md` |
| UI, UX, accessibility, responsive behavior | `DESIGN_RULES.md` |
| stack, architecture, database, deployment, AI/LLM integration, LSP | `TECHNICAL_STACK.md` |
| auth, secrets, security, privacy, metered APIs | `DEVSECOPS.md` |
| versions, commits, changelog, release/merge behavior | `VERSIONING.md` |
| verification, health, probes, or tests | `VERIFICATION_LOOP.md`, `DEBUG_DIAGNOSTICS_STANDARD.md`, `TESTING_STANDARD.md` |
| debug mode or diagnostics UI | `DEBUG_DIAGNOSTICS_STANDARD.md` |
| foundation scaffolding, hooks, repository protection, rule enforcement | `ENFORCEMENT.md` |

A task may require more than one row. Load only the rows that apply.

Work only within the scope defined in `TASK.md`. Do not touch out-of-scope files unless the task explicitly requires it.

---

## AI Developer Operating Model

Agents must work in small, user-visible, verified working slices. Autonomous mode is enabled by default inside the current approved slice. Agents must show verification evidence after each slice, update `STATUS.md` after meaningful progress, and never continue silently after failed verification.

When planning or scoping a slice, load `AI_DEVELOPER_OPERATING_MODEL.md` and `AGILE_SLICE_WORKFLOW.md`. When a slice originates from a new feature/bug ask not already covered by the project's brief/PRD/features docs, also load `INTENT_CAPTURE_STANDARD.md` first — it defines when to capture the why in a durable `docs/intents/` file before scoping in `TASK.md`.

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
- Protected `/health/deep` plus endpoint diagnostic registry and authorized safe-probe controls for app-style products
- Structured high-signal logging at important execution boundaries and an audit trail for sensitive actions
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

Any feature that calls an LLM requires an AI management section at `/admin/ai` (admin-editable prompt and output schema, configurable provider/model, model pricing lookup, token/cost usage view) plus provider-agnostic config, prompt-injection guardrails, and output validation in code. Every LLM call is made through `packages/ai`, never a provider SDK called directly from feature code, so token/cost tracking is automatic — see `TECHNICAL_STACK.md` AI Token & Cost Observability.

Full specification: `TECHNICAL_STACK.md` AI / LLM Integration and `DEVSECOPS.md` LLM Integration Safety.

---

## Version and Code Organization

Version is displayed in the app shell, login page, and admin panel, in `vMAJOR.MINOR.PATCH (shortSHA · UTC build timestamp)` format. Full standard: `VERSIONING.md`.

Every feature is organized under `src/features/<feature-name>/` with its own components, services, repositories, schemas, permissions, logs, and types. Full rules: `DEVELOPMENT_RULES.md` Feature Structure Rules.

---

## Agent Completion Checklist

Before marking any task complete, verify:

- [ ] Working slice user-visible outcome is confirmed
- [ ] Verification evidence produced — static/build gate, health/deep health, affected safe probes, browser when applicable, and risk-triggered tests only when required
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
- Create speculative Python/Node/browser test harnesses before using existing health/probe diagnostics, unless the diagnostics cannot isolate the problem
- Perform destructive actions without explicit approval
