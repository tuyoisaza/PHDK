# AGENTS.md

## Purpose

This file is the entry point and router for AI agents, developers, and automation tools working on this repository. It carries only the rules that apply to every task and a map of where the full standards live — it is not the full standards set.

Every agent must read this file first, then read the project's `TASK.md` and `STATUS.md`. Load deeper standards only when the current task needs them.

If a session runs long and rules start slipping, re-read `INANUTSHELL.md` — it is the one-line-per-rule condensed version of everything below. It is a memory aid, not a replacement for the task-relevant standards. `ENFORCEMENT.md` defines code-oriented local hooks and verification gates.

## Execution Boundary

PHDK is limited to repository code/documentation, local code validation, git/GitHub, and delivery through an existing GitHub-connected deployment pipeline. Read `EXECUTION_SCOPE.md` before acting; this boundary applies to every mode, delegated agent, and external skill.

Do not operate or test in a browser, including headless tools and screenshots. Do not create dependency bots, scheduled agents, cron jobs, recurring backups, maintenance workflows, or preview deployments. Do not administer hosting, databases, OAuth accounts, secrets, repository settings, or other external services. Product requirements describe code to implement, not permission to operate that code against a live environment.

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
2. `EXECUTION_SCOPE.md` — allowed code work, delivery, and exclusions
3. `TASK.md` — the current slice and allowed scope
4. `STATUS.md` — persistent project state, gaps, and next slices

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
| local code verification or tests; health/diagnostic implementation | `VERIFICATION_LOOP.md`, `DEBUG_DIAGNOSTICS_STANDARD.md`, `TESTING_STANDARD.md` |
| debug mode or diagnostics UI | `DEBUG_DIAGNOSTICS_STANDARD.md` |
| foundation scaffolding, local hooks, rule enforcement | `ENFORCEMENT.md` |

A task may require more than one row. Load only the rows that apply.

Work only within the scope defined in `TASK.md`. Do not touch out-of-scope files unless the task explicitly requires it.

---

## AI Developer Operating Model

Agents run in **Mission Autopilot for the active code task**. Once the mission goal/scope is clear, plan the required working slices and execute them within `EXECUTION_SCOPE.md` until complete or blocked. Slice boundaries are checkpoints, not approval gates. Verify locally, self-correct, commit/push to the mission feature branch, and update continuity. This does not authorize scheduled agents, future runs, or ongoing maintenance after the mission ends.

When planning or scoping a slice, load `AI_DEVELOPER_OPERATING_MODEL.md` and `AGILE_SLICE_WORKFLOW.md`. When a slice originates from a new feature/bug ask not already covered by the project's brief/PRD/features docs, also load `INTENT_CAPTURE_STANDARD.md` first — it defines when to capture the why in a durable `docs/intents/` file before scoping in `TASK.md`.

---

## Core Agent Rules

- Work in feature branches. Never commit directly to `main` — unless Finetuning Mode is explicitly active for this conversation, see `DEVELOPMENT_RULES.md` Finetuning Mode.
- Delivery uses an approved push/merge to the branch of the existing GitHub-connected pipeline. Never deploy through a provider CLI/API/dashboard or create the connection as a PHDK task; see `TECHNICAL_STACK.md` Deployment.
- Do not create mock dashboards, fake KPIs, random metrics, or demo data in production code.
- Every user-facing feature must have a real route.
- Every feature must enforce RBAC server-side when roles exist.
- Every user-facing string must use the i18n system.
- Every important action must be logged with structured logs.
- No file may exceed 600 lines. Prefer files under 300 lines.
- Business logic must not live inside page components.
- Implement only the repository code/configuration required by the task. Provisioning and external administration remain outside `EXECUTION_SCOPE.md`.
- Do not upgrade dependencies unless the task explicitly asks for it.
- Do not change database schema without a migration.
- Do not perform destructive operations on live data or external services. Destructive repository changes require explicit task scope.

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

- [ ] Requested behavior is implemented and reviewed in code; visual/live-runtime outcomes are not claimed without evidence
- [ ] Local code verification evidence produced: appropriate source/diff checks, static/build commands, and non-browser risk-triggered tests
- [ ] Route exists and permissions are enforced server-side
- [ ] i18n strings exist for configured languages
- [ ] Loading, empty, and error states exist
- [ ] Structured logs exist
- [ ] No fake data presented as real
- [ ] No file exceeds 600 lines
- [ ] Applicable local code checks pass; documentation-only work has a source/diff and reference review
- [ ] `STATUS.md` updated and `TASK.md` reflects mission completion or the next active slice
- [ ] No unnecessary approval pause occurred between planned slices

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
- Call a metered or paid external API to validate a change; implement and locally test the product's usage caps, timeouts, and retry limits instead
- Provision infrastructure or administer external services
- Change database schema without migrations
- Touch files outside the scope defined in `TASK.md`
- Hand a verification failure back to the human before attempting safe diagnosis and repair
- Ask "continue?", "proceed?", or equivalent between planned slices inside the approved mission
- Open or automate a browser for verification, including headless runners, screenshots, plugins, and delegated browser work
- Create scheduled agents, dependency bots, cron jobs, recurring backups, or maintenance workflows
- Probe live endpoints, execute live database operations, or send notifications to validate code
- Perform destructive repository changes without explicit task scope
