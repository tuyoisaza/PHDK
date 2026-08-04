# PHDK Standards Repository

This repository contains the reusable PHDK standards set. AI coding agents fetch these files before coding so every project follows the same best practices and the same best-of-breed stack, repeatedly.

## Included files

- `AGENTS.md` — operating rules every AI agent must read before making changes
- `DEVELOPMENT_RULES.md` — development principles, workflow, coding standards
- `DESIGN_RULES.md` — UI, UX, design-system, and accessibility standards
- `TECHNICAL_STACK.md` — canonical technical stack for all PHDK projects
- `DEVSECOPS.md` — DevSecOps best practices: secrets, supply chain, CI/CD, runtime security
- `VERSIONING.md` — versioning models, including the optional auto-bump pre-commit hook
- `QA_CHECKLIST.md` — quality gates for task, merge, and release scopes
- `BUILD_APP_FOUNDATION_PROMPT.md` — prompt for building the initial scalable app foundation
- `handoff_prompt.md` — PHDK generation prompt (v1.6) used to produce project-specific kits
- `scripts/` — optional helper scripts: version bump, version metadata generation, commit message prefixing
- `.husky/` — optional git hook templates wired to the scripts above

## How to use this repo

1. Point an AI coding agent at this repository.
2. Instruct the agent to fetch the latest versions of these files before coding:
   - `AGENTS.md`
   - `DEVELOPMENT_RULES.md`
   - `DESIGN_RULES.md`
   - `TECHNICAL_STACK.md`
   - `DEVSECOPS.md`
   - `VERSIONING.md`
   - `QA_CHECKLIST.md`
   - `BUILD_APP_FOUNDATION_PROMPT.md`
3. Use `handoff_prompt.md` to generate a project-specific PHDK kit.
4. Use `BUILD_APP_FOUNDATION_PROMPT.md` as the first build prompt after the kit is generated.
5. Continue feature development against the project's `TASK.md` and `STATUS.md`.

## Enforced rules vs recommendations

This kit draws a clear line:

- **Enforced rules** — security, correctness, server-side RBAC, no fake data, i18n, structured logs, file limits, git discipline. These apply to every task unless `TASK.md` overrides them.
- **Recommendations** — the scripts, hooks, and optional tooling. Adopt them when they fit the project; skip or adapt them when they do not. Never force a script into a project it does not belong in.

## Canonical decisions

- Stack: pnpm + Turborepo + TypeScript monorepo; `apps/web` (Next.js), `apps/api` (NestJS + Fastify), `apps/mobile` (Expo placeholder only)
- Shared packages: `ui`, `types`, `validators`, `api-client`, `design-tokens`, `observability`, `db`, `auth`, `config`
- Database: PostgreSQL only — SQLite is never used in any environment. Drizzle is the required ORM because it keeps a future provider switch configuration-driven.
- Auth: WorkOS or Clerk with Google SSO; server-side RBAC (`super_admin`, `admin`, `team_leader`, `member`)
- Deployment: Railway, two services (`@repo/web`, `@repo/api`), repository-root based, triggered by GitHub push to `main`
- Security: DevSecOps baseline in `DEVSECOPS.md` — secrets never committed, dependency audit + SAST + secret scanning on PRs, branch protection, HTTPS-only, rate limiting, security event audit, rollback path

## Versioning

- The handoff prompt is maintained as `handoff_prompt.md` (currently v1.6).
- Standards files evolve independently; README is updated when the set changes.
