# TESTING_STANDARD.md

## Purpose

PHDK uses automated tests as a **risk-control tool**, not as the default proof that every slice works.

The primary proof for normal product development is the running system itself: typecheck/lint/build where relevant, `/health`, protected `/health/deep`, endpoint probes, browser verification, structured logs, and a copyable diagnostics report.

Automated tests are required only when the cost of a regression is high enough to justify maintaining them.

---

## Core Rule — Diagnostics First, Tests by Risk

Do not write a test merely because code was added.

First ask:

1. Can the affected behavior be verified directly through the live app, `/health/deep`, or a safe endpoint probe?
2. If it regresses later, would the failure be dangerous, expensive, destructive, security-sensitive, or difficult to diagnose?
3. Is there a small deterministic automated test that catches that risk more cheaply than repeated manual diagnosis?

If the answer to 1 is yes and 2 is no, diagnostics are normally sufficient.

If 2 and 3 are yes, add the smallest useful automated test.

---

## Mandatory Automated-Test Triggers

A slice requires automated coverage when it adds or materially changes:

- authorization/RBAC/security boundaries where an unauthorized actor must be denied
- payment, billing, money, credits, quotas, or other financially consequential calculations or state transitions
- destructive data operations, irreversible state transitions, or migration logic with meaningful data-loss risk
- complex deterministic business rules or calculations where subtle regressions are hard to see from a health probe
- security-sensitive parsing or validation, including LLM output validation that can trigger actions
- a previously observed production bug when a small deterministic regression test can reproduce it

The test should target the risky rule, not create a broad suite around unrelated code.

---

## Tests Are Not Required by Default For

- simple CRUD that is covered by endpoint probes and diagnostics
- every service method
- every API-boundary Zod schema
- every UI component
- every working slice
- route wiring and ordinary response-shape checks that the endpoint diagnostic registry already verifies
- visual snapshots
- third-party library internals
- happy-path browser automation for flows that are cheaper and clearer to verify live

Do not manufacture tests to satisfy a percentage or checklist count. PHDK has no coverage-percentage target.

---

## Choose the Smallest Test Layer

When a test trigger exists:

- **Unit test** — pure or nearly pure business rule/calculation.
- **Integration test** — persistence, authorization, or boundary behavior whose correctness depends on the real application integration.
- **E2E test** — only for a high-risk cross-system user flow that cannot be verified adequately by protected diagnostics and targeted probes.

Vitest is the default unit/integration runner when a project needs one. Playwright is the default E2E runner when a project genuinely needs E2E automation.

Do **not** scaffold Vitest, Playwright, Testing Library, or a `test` script at foundation time merely because PHDK exists. Add the minimum test tooling when the first risk-triggered test appears.

A project may use another runner only when there is a concrete project reason recorded in `ARCHITECTURE_DECISIONS.md`.

---

## Diagnostic Verification Is Not a Fake Test

A safe endpoint probe against the running application is valid verification when it proves the actual path under change.

Use the endpoint diagnostic registry defined in `VERIFICATION_LOOP.md` and `DEBUG_DIAGNOSTICS_STANDARD.md` to capture:

- method and route
- required auth/role
- probe mode
- sanitized request example
- expected status and response shape
- actual status and latency
- correlation ID
- related safe logs

This is often more useful than a synthetic test because it exercises the real runtime path and produces evidence the IDE can consume immediately.

---

## No Speculative Test Harnesses

Do not create ad hoc Python, Node, shell, or browser scripts simply to prove that code "probably works" when the application already exposes a health/probe path that can verify it directly.

A temporary diagnostic script is allowed only when:

- the existing diagnostics cannot reproduce or isolate the failure
- the script is the cheapest way to narrow the problem
- its purpose is stated before it is created
- it is deleted afterward unless it graduates into a justified permanent tool

Do not repeatedly run full test/build loops while iterating on a narrow issue. Use targeted diagnostics during iteration; run the relevant full gate once before push/release.

---

## Verification Record

For each slice, report one of:

```txt
Automated tests: not required — diagnostics cover the affected path; no risk trigger
```

or:

```txt
Automated tests: required — <risk trigger>
Tests run: <command/result>
```

A missing test is a gap only when a mandatory test trigger applies.

---

## Never

- Never create tests solely to make a checklist green.
- Never require an E2E test for every user-visible slice.
- Never replace a direct live-system probe with a mock when the real safe path is available.
- Never delete or skip a failing risk-required test just to merge.
- Never let a test suite become a substitute for `/health/deep`, diagnostics, or Human Diff Review.
- Never expose secrets or real private data in test fixtures, probe examples, or diagnostics.

---

## Verification

- [ ] The slice was checked against the mandatory automated-test triggers.
- [ ] If no trigger applies, the affected runtime path has direct diagnostic/probe evidence.
- [ ] If a trigger applies, the smallest useful automated test exists and passes or its failure is honestly reported.
- [ ] No speculative one-off test harness was created when existing diagnostics were sufficient.
- [ ] Test tooling was not scaffolded without a real test need.
