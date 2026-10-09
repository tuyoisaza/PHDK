# TESTING_STANDARD.md

## Purpose

PHDK uses automated tests to control concrete regression risks. Tests are not a default deliverable for every code change.

`EXECUTION_SCOPE.md` is authoritative. Permitted code checks consist of source/diff review, static checks, local builds, and local unit or in-process integration tests with external dependencies replaced by deterministic test doubles. See `VERIFICATION_LOOP.md` for evidence and reporting requirements and `MAIN_DELIVERY_STANDARD.md` for normal delivery completion.

The separate permission in `EXECUTION_SCOPE.md` — **Bounded read-only provider diagnostics** — allows requested finite reads of service/deployment status, non-secret source/branch/configuration/watch metadata, and existing logs independently of Developer Mode or unlock. Those observations are diagnostic evidence, not an executed product test.

---

## Core Rule — Tests by Risk, Within Code Scope

Do not write a test merely because code was added. Ask:

1. Can source review and applicable static/build checks adequately assess this change?
2. Would a regression be dangerous, expensive, destructive, security-sensitive, or difficult to diagnose?
3. Can a small deterministic local test catch that risk without a browser, network service, or database?

If no risk trigger applies, source review and the applicable static/build gate are sufficient for code completion. If a risk trigger applies, add the smallest useful permitted test. A remaining runtime uncertainty must be reported; it never authorizes broader execution by itself.

Passing local verification alone does not finish a normal development request. Continue its authorized branch/PR delivery through review, integration, and fresh verification of the remote target and version under `MAIN_DELIVERY_STANDARD.md`, unless the user explicitly narrowed the scope. Review the complete actual diff; owner approval of sensitive decisions may already be present in the current request. Preserve actual named, independent, or formal review requirements without adding a universal human-diff or GitHub-review-event gate. Classify the changed behavior: restoring login through a packaging fix does not itself change authentication policy.

### Auto cadence

When `PHDK auto` is explicitly active, follow `PHDK_AUTO.md`: implement the entire identified goal and write necessary coverage with its code, then execute the applicable integrated verification at the end. Slice checklists collect coverage for that boundary; they do not require intermediate test suites, human acceptance, or a release per feature. Run an intermediate check only to resolve an actual implementation blocker or satisfy a mandatory hook/control at the operation it governs.

At the final boundary, review the whole candidate, run all applicable local gates and risk-triggered tests, repair in-scope failures, and rerun affected checks before normal branch/PR delivery. Do not require another PHDK-only approval or assign routine local testing to the owner. Final verification happens before publication to `main`; Auto neither skips required checks nor authorizes browser/live-service tests.

---

## Mandatory Automated-Test Triggers

A change requires local automated coverage when it adds or materially changes the behavior below. In Auto, write that coverage with the implementation and execute it in final whole-goal verification, except for a genuine implementation blocker or mandatory intermediate control:

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

Human-supplied redacted diagnostics and observations retrieved under **Bounded read-only provider diagnostics** in `EXECUTION_SCOPE.md` can inform a code fix. A current request such as "verifica Railway" authorizes the relevant finite reads through existing access; an older code-sync task exclusion cannot veto that newer read request. Retrieval does not authorize diagnostic UI operation, live product tests/probes, secret-value reads, or provider writes.

---

## No Speculative Test Harnesses

Do not create ad hoc Python, Node, shell, or other scripts just to make a checklist green. Prefer existing static commands and local test infrastructure.

A temporary local diagnostic script is permitted only when:

- it addresses a specific code-level uncertainty that existing checks cannot isolate
- it is the smallest useful approach and its purpose is stated before creation
- it remains within `EXECUTION_SCOPE.md`, without browser or external runtime access
- it is deleted afterward unless retained as a justified project tool

Do not repeatedly run full test/build loops while iterating on a narrow issue. Outside Auto, use targeted checks during iteration and the applicable gate before push/release. In Auto, execute risk-triggered tests and other applicable verification on the completed whole candidate; only a real blocker or mandatory control justifies an intermediate check. Rerun affected checks after a final-verification repair or integration change. Normal delivery permits bounded in-scope repairs and conflict resolution. Developer Mode retains its direct-main hard stops while it is active; an explicit Auto activation replaces that mode for the identified goal under `PHDK_AUTO.md`. Never bypass a failed check or hook. Do not create CI, scheduled agents, dependency bots, or recurring test workflows to replace local evidence.

---

## Verification Record

Report the relevant risk coverage for the requested deliverable. During Auto implementation, record pending final checks factually and continue; do not emit a completion report or mark checks passed at each slice. At the final integrated boundary, report one of:

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

When bounded provider diagnostics were requested, report the service/deployment, source, query bounds, non-secret metadata or redacted logs, and limits separately from test results. Provider status and existing log events do not prove that the agent executed or retested the product.

Missing coverage of an applicable risky rule is a gap. A prohibited browser or external runtime check is a scope limit, not a task to delegate or a reason to require a human browser check before continuing code work.

---

## Never

- Never create tests solely to make a checklist green.
- Never execute product tests through a browser or external service; permitted read-only provider diagnostics remain separate evidence under `EXECUTION_SCOPE.md`.
- Never weaken security or alter production behavior merely to make local tests pass.
- Never delete or skip a failing risk-required local test just to merge.
- Never claim a local test establishes live health, visual correctness, or a successful real provider integration.
- Never expose secrets or real private data in fixtures, examples, reports, or logs.
- Never add recurring automation, deployment workflows, or cloud/database operations as a test prerequisite.

---

## Verification

- [ ] The entire requested goal was assessed against the mandatory risk triggers; Auto coverage includes all implemented features and their relevant interactions.
- [ ] Source review and applicable static/build checks have actual recorded results.
- [ ] If a trigger applies, the smallest useful local test exists and passes or its failure/gap is reported.
- [ ] Test scripts and dependencies do not launch browsers or access services/databases.
- [ ] No speculative harness or unnecessary runner was added.
- [ ] Remaining visual/runtime uncertainty is stated accurately.
- [ ] If provider diagnostics were requested, retrieval followed `EXECUTION_SCOPE.md` and findings are reported separately from product-test evidence.


## User acceptance testing

`PHDK uat` is governed by `UAT_STANDARD.md`. UAT is the requirements-to-observable-behavior acceptance layer above implementation-focused tests.

- Derive cases from actual actors, goals, requirements, acceptance criteria, workflows, errors, permissions, and materially changed behavior.
- Give every case a stable ID and requirement/source traceability.
- Exercise behavior through the strongest permitted channel available: existing automated acceptance/integration tests, in-process API/service/domain flows, isolated fixtures, or focused test sources added to exercise acceptance behavior.
- Build/type/static evidence counts only when it genuinely establishes the acceptance condition.
- Code inspection alone cannot make an unexecuted behavioral case PASS.
- Browser/headless UI execution, screenshots, live app/database probes, destructive writes, paid calls, provider administration, hosted CI dispatch, and background monitoring remain excluded.
- Cases requiring unavailable/excluded evidence are BLOCKED or MANUAL with the missing evidence stated explicitly.
- Store the catalog in `UAT_CASES.md` and the current run in `UAT_REPORT.md`, unless the repository already defines equivalent canonical paths.
