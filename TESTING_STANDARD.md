# TESTING_STANDARD.md

## Purpose

This file defines what "tests" means in a PHDK project — framework, test types, what must be tested, where tests live, and the minimum bar before a working slice can claim `pnpm test` as verification evidence.

Without this file, `pnpm test` in `VERIFICATION_LOOP.md` has no defined content: a project can report "tests pass" while owning zero tests, and that claim is technically honest. This closes that gap.

---

## Status

Read this file when:

- scaffolding the app foundation (`BUILD_APP_FOUNDATION_PROMPT.md` Step 8/14)
- writing any service, repository, auth flow, or LLM-output-validation code
- a working slice's verification evidence includes `pnpm test`
- reviewing whether a slice or merge meets `QA_CHECKLIST.md` Build Quality

---

## Canonical Test Stack

```txt
Unit / integration:  Vitest
Component:           Vitest + Testing Library (React)
End-to-end:          Playwright
```

Do not introduce Jest, Mocha, or another runner without an `ARCHITECTURE_DECISIONS.md` entry — same override rule as every other stack choice in `TECHNICAL_STACK.md`.

Playwright is the canonical e2e tool referenced here, not the optional `SKILLS_REGISTRY.md` entry — that entry is about an AI agent skill for *driving* a browser during a session; this is the project's own committed e2e test suite.

---

## Test Types and Where They Live

```txt
Unit tests            src/**/*.test.ts        next to the file under test
Integration tests      src/**/*.integration.test.ts   next to the feature under test
Component tests        src/**/*.test.tsx        next to the component under test
E2E tests              apps/web/e2e/**/*.spec.ts
```

- Unit test: one function or class, dependencies mocked.
- Integration test: a service against the real Drizzle/Postgres dev database (the Railway dev instance per `TECHNICAL_STACK.md`, never a mocked DB) — exercises the actual query layer, not a stand-in.
- Component test: a single React component's rendering and interaction, no real network calls.
- E2E test: a real user flow through the running app in a browser, per `VERIFICATION_LOOP.md` Browser verification.

---

## What Must Have a Test

A working slice is not complete without unit or integration coverage for:

- Every RBAC/authorization check (a role that should be denied is actually denied — see `DEVSECOPS.md` Authorization Rules)
- Every Zod schema used at an API boundary (valid input accepted, invalid input rejected)
- Every service method containing business logic (not the route handler itself, per `DEVELOPMENT_RULES.md` — business logic lives in services, so that is where the unit test targets)
- Every LLM output-validation path (`DEVSECOPS.md` LLM Integration Safety) — valid schema accepted, malformed/injected output rejected
- Every soft-delete / batch-state filter in the Data Import / Intake Pipeline (`TECHNICAL_STACK.md`) — a `deactivated` batch's rows are actually excluded

An E2E test is required for:

- The Google OAuth login flow (success and failure paths)
- Any flow named as a working slice's user-visible outcome in `TASK.md` — the slice's own acceptance criterion doubles as its E2E test

Not required, by default:

- 100% line coverage — this standard sets a floor of "the risky paths are tested," not a coverage percentage target
- Testing third-party library internals
- Snapshot tests of visual output (no visual-regression tool is standard yet — see `SKILLS_REGISTRY.md` if a project wants one)

---

## CI Enforcement

`pnpm test` in `VERIFICATION_LOOP.md` and `QA_CHECKLIST.md` Required Validation Commands means Vitest for `apps/web` and `apps/api`, plus Playwright for the flows above when they exist. A slice that adds a new RBAC check, Zod schema, service method, or LLM-output path without a corresponding test is not complete — flag it as a gap in `STATUS.md` rather than reporting `pnpm test: pass` on unrelated tests only.

See `ENFORCEMENT.md` for how this is checked mechanically rather than left to self-report.

---

## Never

- Never mark a slice complete with `pnpm test: not run` when the slice touched auth, RBAC, a Zod boundary schema, or an LLM output path
- Never write a test that mocks the database for an integration test — that defeats the purpose of the integration tier; use the real Railway dev database
- Never delete or skip a failing test to make `pnpm test` pass — fix the code or fix the test, or report the failure honestly per `VERIFICATION_LOOP.md` Honest Reporting Rule
- Never commit a test with no assertions ("smoke test" that only checks the function didn't throw) as coverage for a security-relevant path

---

## Verification

- [ ] Vitest is configured for `apps/web` and `apps/api`
- [ ] Playwright is configured for `apps/web/e2e` when any E2E-required flow exists
- [ ] Every RBAC check added or changed this slice has a passing unit or integration test
- [ ] Every Zod boundary schema added or changed this slice has a passing test for both valid and invalid input
- [ ] Every LLM output-validation path has a passing test for both valid and malformed output
- [ ] The Google OAuth login flow has a passing E2E test covering success and failure
- [ ] `pnpm test` output is included in verification evidence, not omitted
