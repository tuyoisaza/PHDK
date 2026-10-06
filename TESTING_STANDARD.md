# TESTING_STANDARD.md

## Purpose

PHDK uses automated tests to control concrete regression risks. Tests are not a default deliverable for every code change.

`EXECUTION_SCOPE.md` is authoritative. Permitted code checks consist of source/diff review, static checks, local builds, and local unit or in-process integration tests with external dependencies replaced by deterministic test doubles. See `VERIFICATION_LOOP.md` for evidence and reporting requirements.

The separate permission in `EXECUTION_SCOPE.md` — **Bounded read-only log diagnostics** — allows requested retrieval of existing logs independently of PHDK Developer Mode. Those logs are diagnostic evidence, not an executed product test.

---

## Core Rule — Tests by Risk, Within Code Scope

Do not write a test merely because code was added. Ask:

1. Can source review and applicable static/build checks adequately assess this change?
2. Would a regression be dangerous, expensive, destructive, security-sensitive, or difficult to diagnose?
3. Can a small deterministic local test catch that risk without a browser, network service, or database?

If no risk trigger applies, source review and the applicable static/build gate are sufficient for code completion. If a risk trigger applies, add the smallest useful permitted test. A remaining runtime uncertainty must be reported; it never authorizes broader execution by itself.

---

## Mandatory Automated-Test Triggers

A slice requires local automated coverage when it adds or materially changes:

- authorization/RBAC/security boundaries where an unauthorized actor must be denied
- payment, billing, money, credits, quotas, or other financially consequential calculations or state transitions
- destructive data logic, irreversible state transitions, or migration transformations with meaningful data-loss risk
- complex deterministic business rules or calculations whose subtle regressions are difficult to spot in review
- security-sensitive parsing or validation, including LLM output validation that can trigger actions
- a previously observed production bug when a small deterministic local regression test can reproduce the risky rule

Target the risky code rather than creating a broad suite around unrelated behavior. If a risk cannot be fully covered locally, test the deterministic part and report the remaining gap. Do not mark unsupported runtime behavior as verified.

---

## Tests Are Not Required by Default For

- simple CRUD without a specific regression risk
- every service method or API-boundary Zod schema
- every UI component or working slice
- ordinary route wiring and response contracts adequately reviewed in source
- documentation, formatting, or other reversible low-impact changes
- third-party library internals

Do not manufacture tests to satisfy a percentage or checklist count. PHDK has no coverage-percentage target. Visual snapshots and browser-based tests are outside scope regardless of risk.

---

## Choose the Smallest Permitted Test Layer

When a test trigger exists:

- **Unit test** — a pure or nearly pure rule, calculation, parser, authorization decision, or transformation.
- **In-process integration test** — application modules or handlers composed inside the test process, with fake persistence, OAuth, clocks, filesystem boundaries where needed, and provider/network adapters. No HTTP listener, live endpoint, or database connection is allowed.

Vitest in a Node environment is the default when a project needs a runner. Prefer the project's existing permitted runner. Add a runner or `test` script only when the first justified test requires it; do not scaffold test tooling at foundation time just because PHDK exists.

In-memory test doubles belong in test code. They must never become a silent production fallback for a missing database or external dependency.

### Browser and external test execution are prohibited

Do not create or run browser-based E2E, headed/headless browser tests, visual snapshots, screenshot comparisons, or browser-mode test runners. This includes Playwright, Puppeteer, Cypress, Selenium, chrome-devtools, browser MCP, UI interaction through another skill, and delegation to another agent. Renaming a browser check as a smoke test, accessibility scan, preview, or manual confirmation does not make it permitted.

Do not call an application health/probe endpoint, start a preview server, connect to local or cloud databases, use customer accounts, complete OAuth sign-in, call paid providers, or provision services to make tests pass. Existing test scripts must be inspected for these behaviors before execution. An existing browser suite may remain in a repository, but the PHDK agent must neither run nor expand it.

A human may independently test the product. That is not a mandatory PHDK completion gate and must not be reported as an agent-performed check or assigned to the human merely to close a checklist.

---

## Product Diagnostics Are Implementation Requirements

Health endpoints, protected probes, debug panels, redaction, correlation IDs, and copyable reports remain product features where specified by `VERIFICATION_LOOP.md` and `DEBUG_DIAGNOSTICS_STANDARD.md`.

Review their implementation and use local tests for risky logic such as authorization, probe-mode enforcement, redaction, timeouts, quotas, and retry bounds. Stub the dependency boundary; do not execute a real probe or provider request as a test.

Human-supplied redacted diagnostics and logs retrieved under **Bounded read-only log diagnostics** in `EXECUTION_SCOPE.md` can inform a code fix. Retrieval requires a current human request and stays within that section's limits; it does not authorize diagnostic UI operation or live product tests/probes.

---

## No Speculative Test Harnesses

Do not create ad hoc Python, Node, shell, or other scripts just to make a checklist green. Prefer existing static commands and local test infrastructure.

A temporary local diagnostic script is permitted only when:

- it addresses a specific code-level uncertainty that existing checks cannot isolate
- it is the smallest useful approach and its purpose is stated before creation
- it remains within `EXECUTION_SCOPE.md`, without browser or external runtime access
- it is deleted afterward unless retained as a justified project tool

Do not repeatedly run full test/build loops while iterating on a narrow issue. Run targeted checks during iteration and the applicable gate once before push/release. Do not create CI, scheduled agents, dependency bots, or recurring test workflows to replace local evidence.

---

## Verification Record

For each slice, report one of:

```txt
Automated tests: not required — no risk trigger; source review and applicable static/build checks completed
```

or:

```txt
Automated tests: required — <risk trigger>
Local tests run: <command/result>
Coverage limit: <external/runtime behavior not exercised, if relevant>
```

For UI or deployment changes, also state:

```txt
Visual/runtime: visual/runtime unverified — no browser or live product test/probe executed
```

When bounded log diagnostics were requested, report the source, query bounds, redacted findings, and limits separately from test results. Existing log events do not prove that the agent executed or retested the product.

Missing coverage of an applicable risky rule is a gap. A prohibited browser or external runtime check is a scope limit, not a task to delegate or a reason to require a human browser check before continuing code work.

---

## Never

- Never create tests solely to make a checklist green.
- Never execute product tests through a browser or external service; permitted read-only log diagnostics remain separate evidence under `EXECUTION_SCOPE.md`.
- Never weaken security or alter production behavior merely to make local tests pass.
- Never delete or skip a failing risk-required local test just to merge.
- Never claim a local test establishes live health, visual correctness, or a successful real provider integration.
- Never expose secrets or real private data in fixtures, examples, reports, or logs.
- Never add recurring automation, deployment workflows, or cloud/database operations as a test prerequisite.

---

## Verification

- [ ] The slice was assessed against the mandatory risk triggers.
- [ ] Source review and applicable static/build checks have actual recorded results.
- [ ] If a trigger applies, the smallest useful local test exists and passes or its failure/gap is reported.
- [ ] Test scripts and dependencies do not launch browsers or access services/databases.
- [ ] No speculative harness or unnecessary runner was added.
- [ ] Remaining visual/runtime uncertainty is stated accurately.
- [ ] If log diagnostics were requested, retrieval followed `EXECUTION_SCOPE.md` and findings are reported separately from product-test evidence.
