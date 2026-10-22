# TESTING_STANDARD.md

## Purpose

PHDK uses automated tests to control concrete regression risks. Tests are not a default deliverable for every code change.

Creating test sources and executing a suite are separate decisions. Existing repository or hook requirements still apply when no new-test risk trigger exists, including for documentation changes, but they never authorize a prohibited operation. Auto and FORCE authorize required permitted synchronous static checks within the current goal; see `PHDK_AUTO_CONTINUITY.md` and `PHDK_HOOK_COMPATIBILITY.md` for conflicts.

`EXECUTION_SCOPE.md` and `PHDK_PRODUCTION_VERIFICATION.md` govern verification. Permitted local work consists of source/diff review, formatting, lint, static typechecking, safe builds and static security analysis. Do not run local unit, integration, in-process, browser or API tests, even with mocks; do not start servers, Docker or test databases. Runtime acceptance is confined to an explicitly authorized UAT run against the existing deployed production candidate. See `VERIFICATION_LOOP.md` for evidence and reporting requirements and `MAIN_DELIVERY_STANDARD.md` for delivery completion.

The separate permission in `EXECUTION_SCOPE.md` — **Bounded read-only provider diagnostics** — allows requested finite reads of service/deployment status, non-secret source/branch/configuration/watch metadata, and existing logs independently of Developer Mode or unlock. Those observations are diagnostic evidence, not an executed product test.

---

## Authenticated role journeys

In explicitly authorized UAT/UAT Fix, use `JWT_STANDARD.md` to obtain legitimate application/provider sessions for uniquely run-owned synthetic identities; do not introduce a staging-only adapter into production, request people's passwords or paste bearer tokens. For browser cases, isolate a separate secure temporary authenticated browser state per role/tenant and clean it up; source-only fixtures cannot prove login or permissions. JWT-specific negative verification is required only when the application uses JWT. `UAT_STANDARD.md` governs authorization, browser access, safety and evidence.

## UAT Prep — implementation-only verification

Explicit `PHDK uat prep`, or necessary Prep within a fresh explicit `PHDK uat` run, prepares safe readiness under `PHDK_UAT_PREP.md`. It may implement fixture/session support, deliver source changes and perform permitted non-browser provisioning/readiness checks only on the existing deployed production candidate with run-owned synthetic records. Its results are readiness evidence, not UAT acceptance PASS. Standalone Prep does not start acceptance. Browser/Playwright/headless runs and screenshots remain prohibited in Prep and are allowed only within explicitly authorized UAT/UAT Fix. Do not use real accounts, new paid services or local runtime tests. Auto and Auto Force never run Prep.

## Scoped browser exception for UAT and UAT Fix

**Only** during explicitly initiated `PHDK uat`, explicit `PHDK uat fix`, or a retest authorized within that active UAT run, a connected/available browser, browser MCP, Playwright, Cypress or equivalent may be used to exercise user journeys, UI behavior, responsiveness and accessibility and capture timestamped screenshots/evidence. This narrow exception applies **only to those UAT phases**; Auto, Auto Force, PMO and Designer Mode alone do not activate it. It does not activate browser work during Capture, Plan, Prep, implementation, generic verification, Check or Delivery. Delegated work inherits the same scoped authorization and host controls.

Use only the existing versioned production application/database with uniquely run-owned synthetic identities and records under `PHDK_PRODUCTION_VERIFICATION.md`. Confirm the target, exact allowed operations, ownership and cleanup before writes. Never perform real purchases, send real emails, mutate real customer data, bypass authentication, extract secrets, expose personal data, modify provider/repository settings, or call paid services without separate authorization. Do not create local/staging deployments or test databases. No unattended monitoring or background jobs; revoke temporary sessions and verify cleanup on every outcome. Do not open a browser merely to diagnose deployment status.

For each test record the candidate revision, target environment, case ID, steps, expected/actual result and redacted screenshot or trace reference. Stop or mark BLOCKED when browser access, a safe environment or valid test credentials are unavailable; **never** infer PASS from code inspection or claim browser evidence not collected. Close browser sessions after the active UAT execution. UAT Fix may rerun the impacted browser cases after permitted code repairs.

## Core Rule — Tests by Risk, Within Code Scope

Do not write a test merely because code was added. Ask:

1. Can source review and applicable static/build checks adequately assess this change?
2. Would a regression be dangerous, expensive, destructive, security-sensitive, or difficult to diagnose?
3. Can focused test source cover that risk when executed within the permitted deployed acceptance scope?

If no risk trigger applies, source review and applicable permitted repository gates are sufficient for code verification; no new test is needed. If a risk trigger applies, author the smallest useful coverage and record the permitted execution prerequisites. Existing mandatory controls remain effective, but a runtime-test requirement does not override the execution boundary. A remaining runtime uncertainty must be reported; it never authorizes acceptance or broader execution by itself.

Passing local verification alone does not finish a normal development request. Continue its authorized branch/PR delivery through review, integration, and fresh verification of the remote target and version under `MAIN_DELIVERY_STANDARD.md`, unless the user explicitly narrowed the scope. Review the complete actual diff; owner approval of sensitive decisions may already be present in the current request. Preserve actual named, independent, or formal review requirements without adding a universal human-diff or GitHub-review-event gate. Classify the changed behavior: restoring login through a packaging fix does not itself change authentication policy.

### Auto cadence

When `PHDK auto` is explicitly active, follow `PHDK_AUTO.md`: implement the entire identified goal and author necessary coverage with its code, then perform permitted integrated source/static verification. Preserve user stories, acceptance criteria and milestone-to-story mapping as documentation without provisioning fixtures or running acceptance. Slice checklists do not require intermediate test suites, human acceptance or a release per feature. Run an intermediate permitted static check only to resolve an actual implementation blocker or satisfy a mandatory control.

At the final development boundary, review the whole candidate, run applicable permitted static gates, repair in-scope development/Check failures and rerun affected checks before normal branch/PR delivery. Verify remote `main` and available non-UAT deployment evidence. Report the actual **DEVELOPMENT COMPLETE / PARTIALLY DELIVERED / BLOCKED** state separately from **UAT NOT RUN**; Prep/UAT/Fix remain **DEFERRED — OWNER OPT-IN**, not a delivery prerequisite. Offer optional future `PHDK uat` without waiting as a delivery gate. Prior UAT failures do not reopen development or authorize retests.

### Required permitted checks are already authorized

For both `PHDK auto` and `PHDK auto force`, inspect actual scripts and execute required permitted checks such as lint, typecheck, format and safe builds. A command name is not evidence of safety: a build/lint command that starts runtime tests, an application, database, browser or live service is outside this boundary. Use finite execution; do not leave watchers running, weaken controls or treat `pnpm test`/Vitest as an automatic exception.

Avoid unnecessary verification while preserving mandatory controls. A hook that requires prohibited runtime execution is a concrete policy conflict. Apply `PHDK_HOOK_COMPATIBILITY.md`: repair only proven PHDK-owned legacy conflicts within authorized scope, preserving independent security/version gates; otherwise report the exact blocked publication operation and continue independent work. Never bypass a hook, silently claim a required test passed or ask for a ceremonial approval to run forbidden local tests.

FORCE also makes PHDK-only human/manual/formal review waits nonblocking without a preventive review/protection investigation. Perform technical source/diff/security review and mandatory checks, then continue the permitted delivery. An actual hook/tool/GitHub rejection starts a repair-and-retry cycle under `PHDK_AUTO_CONTINUITY.md`: report, diagnose the observed cause, repair within scope, revalidate affected checks, retry delivery and verify `main`. A first rejection is not a terminal condition. Preserve genuine current owner restrictions, keep the mandate, and continue while permitted progress remains without bypass or identical rejected retries.

---

## Mandatory Automated-Test Triggers

A change requires focused automated test source when it adds or materially changes the behavior below. In Auto, author coverage with the implementation, statically review it and record runtime execution as deferred to explicitly authorized UAT against the existing deployed candidate:

- authorization/RBAC/security boundaries where an unauthorized actor must be denied
- payment, billing, money, credits, quotas, or other financially consequential calculations or state transitions
- destructive data logic, irreversible state transitions, or migration transformations with meaningful data-loss risk
- complex deterministic business rules or calculations whose subtle regressions are difficult to spot in review
- security-sensitive parsing or validation, including LLM output validation that can trigger actions
- a previously observed production bug when focused permitted regression coverage can reproduce the risky rule

Target the risky code rather than creating a broad suite around unrelated behavior. If a risk cannot be exercised through the permitted deployed scope, retain its source coverage or specification and report the execution gap. Do not run a local harness as a substitute or mark unsupported runtime behavior verified.

---

## New Tests Are Not Required by Default For

- simple CRUD without a specific regression risk
- every service method or API-boundary Zod schema
- every UI component or working slice
- ordinary route wiring and response contracts adequately reviewed in source
- documentation, formatting, or other reversible low-impact changes
- third-party library internals

Do not manufacture tests to satisfy a percentage or checklist count. PHDK has no coverage-percentage target. This list does not waive an existing mandatory test suite. Visual snapshots and browser-based tests are outside ordinary development verification; UAT/UAT Fix may use the scoped browser exception.

---

## Choose the Smallest Useful Coverage

When a test trigger exists, preserve or author focused coverage for the relevant rule, authorization boundary, parser, transformation or integrated user outcome. Prefer existing project test source and a supported acceptance channel. Locally inspect source, syntax/types and build compatibility only; writing unit or integration test source does not authorize executing it locally, including against mocks.

Execute runtime acceptance only after explicit UAT authorization against the existing deployed candidate with run-owned synthetic records and safe cleanup. Do not install a local runner, create test infrastructure or expose an internal test endpoint merely to obtain execution evidence. A coverage gap stays explicit when no permitted channel exists.

Test doubles must never become a silent production fallback for a missing database or external dependency.

### Browser tests prohibited outside UAT/UAT Fix

Outside the scoped UAT/UAT Fix exception, do not create or run browser-based E2E, headed/headless browser tests, visual snapshots, screenshot comparisons, or browser-mode test runners. This includes Playwright, Puppeteer, Cypress, Selenium, chrome-devtools, browser MCP, UI interaction through another skill, and delegation to another agent. Renaming a browser check as a smoke test, accessibility scan, preview, or manual confirmation does not make it permitted.

Do not call an application health/probe endpoint, start a preview server, connect to local or cloud databases, use customer accounts, complete OAuth sign-in, call paid providers, or provision services to make tests pass. Existing test scripts must be inspected for these behaviors before execution. An existing browser suite may remain in a repository, but the PHDK agent must neither run nor expand it outside authorized UAT/UAT Fix.

A human may independently test the product. That is not a mandatory PHDK completion gate and must not be reported as an agent-performed check or assigned to the human merely to close a checklist.

---

## Product Diagnostics Are Implementation Requirements

Health endpoints, protected probes, debug panels, redaction, correlation IDs, and copyable reports remain product features where specified by `VERIFICATION_LOOP.md` and `DEBUG_DIAGNOSTICS_STANDARD.md`.

Review their implementation and author focused coverage for risky logic such as authorization, probe-mode enforcement, redaction, timeouts, quotas and retry bounds. Perform only permitted static checks during development; do not execute a real probe, local runtime harness or provider request as a substitute for separately authorized acceptance.

Human-supplied redacted diagnostics and observations retrieved under **Bounded read-only provider diagnostics** in `EXECUTION_SCOPE.md` can inform a code fix. A current request such as "verifica Railway" authorizes the relevant finite reads through existing access; an older code-sync task exclusion cannot veto that newer read request. Retrieval does not authorize diagnostic UI operation, live product tests/probes, secret-value reads, or provider writes.

---

## No Speculative Test Harnesses

Do not create ad hoc Python, Node, shell or other scripts just to make a checklist green. Prefer existing permitted static commands.

A temporary local diagnostic script is permitted only when:

- it addresses a specific code-level uncertainty that existing checks cannot isolate
- it is the smallest useful approach and its purpose is stated before creation
- it performs source/static analysis within `EXECUTION_SCOPE.md` and `PHDK_PRODUCTION_VERIFICATION.md`, without product execution, local runtime tests, browser or external runtime access
- it is deleted afterward unless retained as a justified project tool

Do not repeatedly run full build loops while iterating on a narrow issue. Outside Auto, use targeted permitted static checks during iteration and the applicable gate before push/release. In Auto, perform permitted whole-candidate verification; only a real blocker or mandatory control justifies an intermediate check. Rerun affected permitted checks after a final-verification repair or integration change. Normal delivery permits bounded in-scope repairs and conflict resolution. Developer Mode retains its direct-main hard stops while active; an explicit Auto activation replaces that mode for the identified goal under `PHDK_AUTO.md`. Never bypass a failed check or hook. Do not create CI, scheduled agents, dependency bots or recurring test workflows as an execution workaround.

---

## Verification Record

Report the relevant risk coverage for the requested deliverable. During Auto implementation, record pending final checks factually and continue; do not emit a completion report or mark checks passed at each slice. At the final integrated boundary, report one of:

```txt
New tests: not required — no risk trigger
Existing required controls: <permitted command/result or exact policy conflict>
Source review and applicable static/build checks: <actual results>
```

or:

```txt
Automated test source: required — <risk trigger and authored/existing coverage>
Local runtime tests: NOT RUN — prohibited by production-first policy
UAT: NOT RUN — DEFERRED — OWNER OPT-IN (unless separately explicitly invoked)
Coverage limit: <behavior not exercised or authorized deployed evidence reference>
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
- Never execute product tests through a browser outside authorized UAT/UAT Fix or through an unauthorized external service; permitted read-only provider diagnostics remain separate evidence under `EXECUTION_SCOPE.md`.
- Never weaken security or alter production behavior merely to make tests pass.
- Never delete meaningful failing test source, bypass a gate or claim an unexecuted check passed just to merge.
- Never claim static source/build evidence establishes live health, visual correctness or a successful real provider integration.
- Never expose secrets or real private data in fixtures, examples, reports, or logs.
- Never add recurring automation, deployment workflows, or cloud/database operations as a test prerequisite.

---

## Verification

- [ ] The entire requested goal was assessed against the mandatory risk triggers; Auto coverage includes all implemented features and their relevant interactions.
- [ ] Source review and applicable static/build checks have actual recorded results.
- [ ] Existing required controls were assessed against the permitted execution boundary; no hook was bypassed and any conflict is reported or legitimately reconciled.
- [ ] If a trigger applies, focused test source exists and runtime execution/evidence limits are reported accurately.
- [ ] Executed development scripts remain static and do not start applications, tests, browsers, services or databases.
- [ ] No speculative harness or unnecessary runner was added.
- [ ] Remaining visual/runtime uncertainty is stated accurately.
- [ ] If provider diagnostics were requested, retrieval followed `EXECUTION_SCOPE.md` and findings are reported separately from product-test evidence.


## User acceptance testing

Only a fresh explicit `PHDK uat` invocation begins acceptance and necessary Prep under `UAT_STANDARD.md`. UAT is the requirements-to-observable-behavior acceptance layer above implementation-focused source checks. Standalone `PHDK uat prep` does not start acceptance; UAT Fix requires explicit invocation or repair authorization within the active explicitly initiated UAT run. Auto and Auto Force never enter these stages or reopen them from historical failures.

- Derive cases from actual actors, goals, requirements, acceptance criteria, workflows, errors, permissions, and materially changed behavior.
- Give every case a stable ID and requirement/source traceability.
- Exercise behavior through the strongest permitted acceptance/API/browser channel on the exact existing deployed production revision, using only run-owned synthetic fixtures with verified cleanup; never use local/in-process tests or new test databases.
- Build/type/static evidence counts only when it genuinely establishes the acceptance condition.
- Code inspection alone cannot make an unexecuted behavioral case PASS.
- Browser/headless UI execution and screenshots outside explicitly authorized UAT/UAT Fix, unscoped live app/database probes, real-data/destructive writes, paid calls, provider administration, hosted CI dispatch and background monitoring remain excluded.
- Cases requiring unavailable/excluded evidence are BLOCKED or MANUAL with the missing evidence stated explicitly.
- Store the catalog in `UAT_CASES.md` and the current run in `UAT_REPORT.md`, unless the repository already defines equivalent canonical paths.


## Production-first verification override (v2.58.0)

**Mandatory:** Apply [PHDK_PRODUCTION_VERIFICATION.md](PHDK_PRODUCTION_VERIFICATION.md). Owner-authorized production-only UAT supersedes earlier local unit/in-process/runtime testing, staging-only identity, and blanket production-test prohibitions. Local operations are limited to static analysis, lint, typecheck and safe builds; Docker, local runtime tests and separate staging/databases are prohibited. UAT must use existing versioned production deployment and existing database, strictly scoped run-owned synthetic identities/records, audit, automated cleanup and verified revocation on success, failure and interruption. Never touch real data or bypass existing security hooks; a conflicting gate is BLOCKED.


## Hook compatibility (v2.61.0)

Apply [PHDK_HOOK_COMPATIBILITY.md](PHDK_HOOK_COMPATIBILITY.md). Inspect effective Git hooks and nested package scripts before push; a local behavioral test required by a legacy PHDK hook is an AUTO-FIXABLE policy violation, not a reason to request a local-testing exception. Within authorized Auto/Auto Force/Check Fix, replace **only proven PHDK-owned** prohibited test invocations with permitted static checks while preserving security/version/branch/commit gates. Owner-owned, external, or unknown hooks remain unchanged absent explicit authorization; report BLOCKED if they prevent push. Never execute prohibited tests or use --no-verify.
