# PHDK Universal Test Automation Standard (v3.4.0)

## Purpose
All current and future PHDK-managed projects should **reuse one lightweight, vendored Python orchestrator**, not invent per-project test infrastructure. The common runner executes each repository's existing native tools (TypeScript, Python, Go, Java, Rust, PHP, etc.) through a small project-owned test manifest, captures bounded evidence and returns one exit code plus JSON/Markdown reports. It does not discover test cases automatically, replace native test frameworks, act as a sandbox or create a background job.

This standard **supersedes earlier blanket prohibitions on all local runtime tests** only for the narrowly permitted **hermetic, code-level** checks below. Other project runtime, hosted/provider and UAT boundaries remain in force. A previous prohibition in a distributed PHDK copy does not authorize executing a new workflow until that copy is intentionally upgraded and its owner restrictions reconciled.

## Two profiles and their permissions

| Profile | Applicable tests | Execution boundary |
|---|---|---|
| `local` | Existing lint, formatting, typecheck, safe builds, static security; short, deterministic unit/contract/in-process integration tests with mocks/doubles | Foreground, offline, repository-scoped, no real DB, server, network, application HTTP, Docker, browser, paid provider, external writes or credentials. Existing hooks/owner restrictions still apply. |
| `uat` | Project-defined API, browser, end-to-end, permissions, integration, migration and recovery cases justified by risk | **Only** inside a fresh explicit owner `PHDK uat`/authorized `PHDK uat fix` run, targeting the existing deployed production candidate with uniquely run-owned synthetic fixtures, legitimate sessions and verified cleanup per UAT standards. `--uat-authorized` is a CLI assertion, **not proof** of permission. |

Local code-level tests do not exercise a deployed URL, authenticate users, probe JWT flows, test a database or verify real browser behavior. In-process tests must avoid opening listeners, creating application databases or contacting providers. When this cannot be guaranteed, classify the check as UAT/deferred rather than lying about local hermeticity. UAT may require authenticated synthetic sessions; never inject bypasses or test real users.

## Per-project manifest

A project opts in to a minimal `tests/phdk-tests.json` with `schema_version: 1` and a `checks` array; each check declares a unique `id`, `profile`, `kind`, argument-array `argv`, and bounded `timeout_sec` (1–600). Optional `cwd` is repository-relative. This is a list of existing trusted project commands, **not** a new framework. Start from `examples/test-automation/suite.example.json` and substitute actual available scripts; never copy JavaScript commands blindly into another language stack. Avoid speculative checks or artificial percentage/route-count targets.

The runner refuses shells, known provider/database/container commands, local HTTP URLs, duplicate IDs, unsafe paths, absent profiles and invalid manifests; it executes using subprocess with `shell=False`. **That is best-effort command validation, not process/network isolation**: a package-manager script or test source may do anything permitted by the host. An agent must inspect package scripts, hooks, transitive command graphs and fixtures before first execution and whenever changed. Owner/host rules still prevail.

For a UAT check with `mutates: true`, declare `run_owned_data: true` and a bounded `cleanup_argv`; check test-owned identity, tenant, record IDs and rollback evidence independently. The runner invokes cleanup even after that check fails, but abrupt host termination, inaccessible providers or an untrusted child process can still leave state. Report cleanup failures as incidents, never a passed test.

## How to run

Read-only validation of a project's profile:

```sh
python phdk-standards/scripts/phdk_test_runner.py --root . --profile local --validate
```

Run local code-level checks during a current authorized implementation goal or explicit `PHDK test`:

```sh
python phdk-standards/scripts/phdk_test_runner.py --root . --profile local --max-seconds 300
```

During a **separately explicit** PHDK UAT run only, pass its real existing production HTTPS target and the active synthetic run ID:

```sh
python phdk-standards/scripts/phdk_test_runner.py --root . --profile uat --uat-authorized --uat-run-id RUN-20261113-01 --uat-target https://existing-production.example
```

Use `python scripts/phdk_test_runner.py` when running inside the canonical PHDK checkout. The example domain and run ID are placeholders; never test them. Python >=3.10 and the standard library suffice for the orchestrator; actual per-project test tools must already be installed and permitted. No new service, GitHub Actions, background worker, scheduler, Docker instance, test server or local database.

The default synchronous budget is 300 seconds, each command has a bounded timeout, and failure stops later cases by default. A deliberate diagnostic invocation may use `--continue-on-failure` within the same overall budget, but may not produce repeated speculative loops. Material time/allowance pressure follows `PHDK_DELIVERY_STOP_LOSS_STANDARD.md` and never delays an otherwise deliverable milestone.

## Outputs and truthful coverage

One execution writes `.phdk-test-results/<UTC>-<profile>-<pid>/report.json`, `report.md`, and one bounded redacted log per attempted check. Add `.phdk-test-results/` to the project's `.gitignore` when adopting. Never commit raw logs, secrets, customer data, JWTs or private traffic captures. Built-in redaction is best effort, so validate evidence before sharing. The runner reports git SHA when locally verifiable, selected profile, duration, counts, and **PASS / FAIL / BLOCKED / NOT_RUN**. Missing manifest or missing selected checks is not PASS. The other profile is explicitly excluded, not implicitly accepted. Source tests and UAT results are **separate**.

## Lifecycle: a checkpoint, not another bureaucracy stage

- **Capture/Plan:** identify real high-risk behavior and existing test commands. Declare only justified unit/contract, integration and acceptance cases; select a local hermetic path or defer to explicit deployed UAT.
- **Implementation/Auto:** write focused test code alongside changed behavior. Reuse native scripts and run the bounded `local` profile at milestone integration, with targeted reruns after fixes. No forced test percentage, 585-case combinatorial expansion, or gratuitous test harness.
- **40 Integration / Check / Delivery:** collect the latest relevant local report for the candidate SHA and permitted build/security results, publish independently valuable milestones on time. `local PASS` establishes only the scripted code-level checks; report deployment and `UAT NOT RUN` separately.
- **Explicit UAT / UAT Fix:** execute the configured `uat` profile only if applicable and under existing authorization, fixtures, browsers, evidence, cleanup, and cutover boundaries. If a project cannot safely test a special recovery/replication case, mark it NOT_RUN/decision-required, not an assumed FAIL or a new infrastructure mandate.
- **Documentation-only, non-applicable or absent safe runner:** report `NOT_APPLICABLE`, `NOT_CONFIGURED` or precise `BLOCKED`; do not fabricate a successful green suite.

The runner is an **execution consolidation mechanism**, not a promise to test an arbitrary website without project-specific tests. It lowers repeated agent/tool interaction by collecting diagnostics from one finite command; the agent reads a concise report and only opens failed logs for repair. Fix the application, not the evidence, and never weaken hooks or bypass authorization to make a check green.
