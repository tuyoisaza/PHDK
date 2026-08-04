# ONBOARDING_AI_DEVELOPER.md

## Purpose

This file tells an AI IDE coder (Claude Code, Cursor, Windsurf, Copilot, or equivalent) how to receive the PHDK knowledge correctly before touching a project.

This repository is a **public standards reference**. AI agents point at it, fetch the files in order, and then apply the same best stack and the same best practices to every project.

Read this file before reading any standards file.

---

## What This Repo Contains

```txt
AGENTS.md                       — operating rules every agent reads first
DEVELOPMENT_RULES.md            — workflow, git discipline, coding standards
DESIGN_RULES.md                 — UI, UX, accessibility, debug UI rules
TECHNICAL_STACK.md              — the canonical stack (source of truth for tooling)
DEVSECOPS.md                    — DevSecOps baseline: secrets, supply chain, CI/CD, runtime
VERSIONING.md                   — versioning models and optional auto-bump tooling
QA_CHECKLIST.md                 — quality gates for task, merge, and release
BUILD_APP_FOUNDATION_PROMPT.md  — prompt to build the initial app foundation
handoff_prompt.md               — prompt to generate a project-specific kit
ONBOARDING_AI_DEVELOPER.md      — this file
VERSION                         — current standards-repo version
CHANGELOG.md                    — history of standards changes
scripts/                        — optional helper scripts (version bump, prefix, metadata)
.husky/                         — optional git hook templates
```

---

## Enforced Rules vs Recommendations

This is the most important distinction in the kit.

### Enforced rules

Apply to every task unless `TASK.md` explicitly overrides them:

- security and correctness
- server-side RBAC on every protected route and endpoint
- no fake data presented as real
- i18n for every user-facing string
- structured logging on important actions
- file limits (600 lines max, prefer under 300)
- PostgreSQL only — SQLite is never used in any environment
- git discipline (feature branches, versioned commit messages)
- no deployment from a local CLI

### Recommendations

Optional tooling. Adopt when it fits the project; skip or adapt when it does not:

- the version-bump and commit-prefix hooks in `scripts/` and `.husky/`
- any DevSecOps tooling that does not fit the project's stack

Never force a recommended script into a project it does not belong in.

---

## Reading Order

When starting work on a project built from this standard, fetch and read in this order:

1. `AGENTS.md`
2. `DEVELOPMENT_RULES.md`
3. `DESIGN_RULES.md`
4. `TECHNICAL_STACK.md`
5. `DEVSECOPS.md`
6. `VERSIONING.md`
7. `TASK.md`
8. `STATUS.md`

Then the project-specific files:

- `README.md`, `PROJECT_BRIEF.md`, `PRD.md`, `FEATURES.md`, `NAVTREE.md`, `PUBLIC_CONTENT.md`, `PRIVATE_CONTENT.md` (if present), `ARCHITECTURE_DECISIONS.md`

Work only within the scope defined in `TASK.md`. Do not touch out-of-scope files.

---

## The Two Prompts

### `handoff_prompt.md`

Use this to generate a project-specific PHDK kit from a project brief. It produces the project files (`README.md`, `TASK.md`, `STATUS.md`, `PRD.md`, `FEATURES.md`, and the rest) that describe what to build.

### `BUILD_APP_FOUNDATION_PROMPT.md`

Use this as the first build prompt after the kit is generated. It builds the reusable technical foundation (monorepo, `apps/api`, `apps/web`, shared packages, debug foundation, testing foundation, quality gates) — not product features.

Do not use the foundation prompt to build project features.
Do not use `handoff_prompt.md` to build code directly.

---

## Working Rules for AI Agents

- Identify the project mode first: public, authenticated, hybrid, or unclear
- If the mode is unclear, ask one clarifying question before coding
- Do not invent features, routes, or integrations the PHDK does not list
- Do not present fake data, fake users, fake KPIs, or demo analytics as real
- Do not add auth/admin/dashboard code when the project is public-only
- Keep `apps/mobile` as an Expo placeholder; do not build it unless tasked
- Put business logic in the service layer, never in page components
- Enforce authorization server-side; hiding UI is not security
- Validate all inputs at API boundaries with the shared Zod schemas
- Log important actions with structured logs through `@repo/observability`
- Run the quality gates in `QA_CHECKLIST.md` before declaring work complete
- Use the final report format defined in `AGENTS.md`

---

## Versioning Awareness

- The standards repo itself is versioned via `VERSION` and `CHANGELOG.md`; always fetch the latest versions of the standards files from `main`
- Projects built from this standard must show their own version as `vMAJOR.MINOR.PATCH (shortSHA · UTC build timestamp)` in the login page, app shell, and admin panel
- Project commit messages always start with the current project version
- Project version increments on merge to `main`, not on every feature-branch commit

---

## First Task Checklist

- [ ] This onboarding file was read
- [ ] Standards files were fetched from the latest `main`
- [ ] `AGENTS.md` reading order was followed
- [ ] Project mode is identified (public / authenticated / hybrid)
- [ ] Enforced vs recommended rules are distinguished
- [ ] Scope from `TASK.md` is understood
- [ ] Build prompt (if applicable) was used in the right order
