# CHANGELOG.md

## Purpose

Tracks the version of this standards repository. The version in `VERSION` increments on merge to `main`, matching the versioning rules in `AGENTS.md` and `VERSIONING.md`.

---

## v2.4.0

- Add explicit test framework to `TECHNICAL_STACK.md`: Vitest (+ React Testing Library, Supertest for the API) and Playwright for E2E
- Add `Testing Foundation` step to `BUILD_APP_FOUNDATION_PROMPT.md` and renumber subsequent steps
- Update Node version in `TECHNICAL_STACK.md`: minimum 22.x, preferred 24.x (24 is Active LTS, 22 is Maintenance LTS)
- Unify the copy-debug-report payload and redaction lists across `AGENTS.md` and `BUILD_APP_FOUNDATION_PROMPT.md`
- Add `VERSION` file and this changelog to track standards-repo versions
- Add `ONBOARDING_AI_DEVELOPER.md` so AI IDE coders can receive the knowledge in the right order
- Update `README.md` entrypoint with the new files

## v2.3.0

- Add `DEVSECOPS.md`: secrets, supply chain, SAST/DAST, CI/CD, runtime security headers, monitoring, incident response, vulnerability SLA, checklist
- Add `VERSIONING.md`: merge-based default model plus optional auto-bump pre-commit hook, wiring notes, gotchas
- Add optional tooling: `scripts/bump-version.mjs`, `scripts/prepend-version.mjs`, `scripts/generate-version.mjs`, `.husky/pre-commit`, `.husky/prepare-commit-msg`
- Frame everything beyond the core rules as recommendations in `AGENTS.md`
- Add DevSecOps section to `QA_CHECKLIST.md`

## v2.2.1

- Embed the version into branch names: `feature/<version>/<feature-name>`, `fix/<version>/<issue-name>`, `chore/<version>/<task-name>`, `checkpoint/<version>-YYYY-MM-DD`
- Fill the standards repository URL placeholder in `handoff_prompt.md`

## v2.2.0

- Align the canonical package model to 9 packages, adding `packages/auth` and renaming shared packages (`@repo/*`)
- Move Zod schemas to `packages/validators` and the logger to `packages/observability` across all files
- Remove SQLite references everywhere and standardize PostgreSQL-only + Drizzle portability language
- Update `handoff_prompt.md` to the current structure and add standards fetch lists

## Before v2.2.0

Versions were tracked informally in commit messages (`Initial commit`, `v0`, `v1`, `2.1`, `2.1.1`, `handoff`). This changelog starts at v2.2.0.
