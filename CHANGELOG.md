# CHANGELOG.md

All notable changes to the PHDK standards are documented here.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

---

## v2.5.1 — 2026-08-07

### Theme: Post-Update Consistency Review

### Changed

- **Database standard reverted to PostgreSQL-only.** v2.5.0 introduced SQLite for local development; this was reverted. All environments, including local development, use PostgreSQL — no SQLite anywhere. Updated `TECHNICAL_STACK.md`, `DEVELOPMENT_RULES.md`, `README.md`.
- `BUILD_APP_FOUNDATION_PROMPT.md` — fixed leftover `WORKOS_API_KEY`/`CLERK_SECRET_KEY` env var example, replaced with the Google OAuth 2.0 env vars used everywhere else in the standard.
- `QA_CHECKLIST.md` — fixed the auth checklist item that still named WorkOS/Clerk as the approved default provider; now references custom Google OAuth 2.0.
- `PROJECT_HANDOFF_TO_DEVELOPMENT_KIT_PROMPT.md` — fixed version header mismatch (was still v1.5 while CHANGELOG recorded it as bumped to v1.6); filled in the standards repo URL placeholder with `https://github.com/tuyoisaza/PHDK`.
- `README.md` — filled in the standards repo URL placeholder in the "new AI coder session" instructions.

### Notes

This release corrects internal inconsistencies introduced by the v2.5.0 update package that were not caught before merge: a canonical decision that contradicted its own QA gate, stale env var examples from the pre-Google-OAuth auth standard, and unfilled repo URL placeholders.

---

## v2.5.0 — 2026-08-06

### Theme: AI Developer Operating Model

This version upgrades PHDK from a standards repo for AI coding to an AI developer operating system.

### Added

- `AI_DEVELOPER_OPERATING_MODEL.md` — core doctrine for AI developers: ethos, telos, rule levels, autonomous work model, working slice doctrine, stop-and-ask conditions, feedback loop, and final report format
- `SPEC_INTERVIEW_PROMPT.md` — optional pre-brief interview prompt that guides the AI to interview for human context before generating a PHDK kit
- `AGILE_SLICE_WORKFLOW.md` — working slice model to replace waterfall-style AI development; defines slice lifecycle, sizing rules, backlog management, and anti-patterns
- `VERIFICATION_LOOP.md` — defines what counts as proof; required evidence types, health check standard, deep health check standard, verification by slice type, and honest reporting rules
- `DEBUG_DIAGNOSTICS_STANDARD.md` — complete copy diagnostics report specification, debug mode behavior, auth diagnostics requirements, UI controls, and QA checklist
- `DEVSECOPS.md` — security and operational safety baseline covering auth, authorization, sessions, logging, dependencies, environment variables, deployment, and stop-and-ask conditions
- `VERSIONING.md` — version, branch, commit, changelog, release, and visible build metadata standards
- `ONBOARDING_AI_DEVELOPER.md` — required reading order, standards file definitions, session start procedure, rule levels, and what AI developers must never do

### Changed

- `AGENTS.md` — added AI Developer Operating Model section, added autonomous work rules, added public-only project clarification, updated required reading list
- `TECHNICAL_STACK.md` — replaced WorkOS and Clerk with custom Google OAuth 2.0 auth standard, added Google OAuth credential setup instructions, updated environment variables
- `BUILD_APP_FOUNDATION_PROMPT.md` — added new standards files to required reading, updated auth to custom Google OAuth 2.0, added slice completion rule, added diagnostics requirement, updated first task instruction
- `QA_CHECKLIST.md` — added AI Developer Operating Model QA, Working Slice QA, Verification Loop QA, Google OAuth 2.0 QA, Debug Diagnostics QA, Deep Health QA sections
- `PROJECT_HANDOFF_TO_DEVELOPMENT_KIT_PROMPT.md` — updated TASK.md template with working slice section, updated first generated task, updated auth references, added new standards files to reference list, updated to v1.6
- `DEVELOPMENT_RULES.md` — removed WorkOS and Clerk references, updated auth standard
- `README.md` — added v2.5 direction, updated included files list, updated canonical decisions

### Removed

- All references to WorkOS as a default auth provider
- All references to Clerk as a default auth provider
- `BOOTSTRAP_MONOREPO_PROMPT.md` — replaced by `BUILD_APP_FOUNDATION_PROMPT.md` in v2.0

### Canonical Decisions

- Auth: custom Google OAuth 2.0 by default; no paid auth vendor by default
- Working slice model replaces waterfall-style development
- Verification evidence required before every slice is marked complete
- Deep health check standard added as verification requirement

---

## v2.0.0 — 2026-05-07

### Theme: Foundation Prompt and Standards Consolidation

### Added

- `BUILD_APP_FOUNDATION_PROMPT.md` — replaced `BOOTSTRAP_MONOREPO_PROMPT.md` with a project-mode-aware foundation prompt supporting public, authenticated, hybrid, and unclear modes

### Changed

- All references to `BOOTSTRAP_MONOREPO_PROMPT.md` updated to `BUILD_APP_FOUNDATION_PROMPT.md`
- `PROJECT_HANDOFF_TO_DEVELOPMENT_KIT_PROMPT.md` updated to v1.5 with hard mode switch, project name confirmation, canvas mode awareness, and correction loop

### Removed

- `BOOTSTRAP_MONOREPO_PROMPT.md` — replaced by `BUILD_APP_FOUNDATION_PROMPT.md`

---

## v1.0.0 — Initial Release

### Added

- `AGENTS.md`
- `DEVELOPMENT_RULES.md`
- `DESIGN_RULES.md`
- `TECHNICAL_STACK.md`
- `QA_CHECKLIST.md`
- `BOOTSTRAP_MONOREPO_PROMPT.md`
- `PROJECT_HANDOFF_TO_DEVELOPMENT_KIT_PROMPT.md`
- `README.md`
