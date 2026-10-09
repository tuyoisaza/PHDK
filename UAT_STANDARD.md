# PHDK UAT Standard

## Command and purpose

`PHDK uat` runs autonomous user acceptance testing for the identified current product candidate. Match the command case-insensitively after trimming whitespace. Use the current conversation, repository requirements, product documentation, acceptance criteria, current task, code, and existing test evidence to identify the candidate and scope. If no candidate or product goal can be determined, ask only for that missing target.

The command authorizes the assistant to create or refresh UAT artifacts, derive acceptance cases, execute every permitted acceptance check available for those cases, collect evidence, and write the final report without requesting approval between cases. It does not authorize unrelated product development, browser/headless testing, live destructive operations, provider writes, recurring work, or work after the conversation.

## Required artifacts

Use explicit existing equivalents when the repository already defines them. Otherwise create:

- `UAT_CASES.md` — durable catalog of acceptance/use cases.
- `UAT_REPORT.md` — evidence and conclusion for the current candidate/run.

## Build the case catalog

Derive cases from the actual product and changed behavior. Cover applicable primary actors and goals, happy paths, authorization boundaries, invalid input, important empty/error/retry states, state transitions, cross-feature flows, business rules, accessibility/i18n requirements, and regressions materially affected by the candidate.

Every case must contain:

1. Stable ID such as `UAT-001`.
2. Title and actor.
3. Requirement/source traceability.
4. Preconditions and test data/fixtures.
5. User/business actions.
6. Expected observable outcome.
7. Permitted validation channel.
8. Result: NOT RUN, PASS, FAIL, BLOCKED, MANUAL, or NOT APPLICABLE.
9. Evidence reference.
10. Defect/reference when failed.

Keep cases deterministic and repeatable. Do not inflate the catalog with cosmetic permutations that do not represent distinct acceptance risk.

## Execute autonomously

Run the strongest permitted evidence for each case without waiting for approval.

Preferred evidence:

1. Existing automated acceptance/in-process integration tests that exercise the workflow.
2. Repository-local API/service/domain flows using isolated fixtures, test databases, doubles, or existing harnesses.
3. Focused automated test sources added when needed to exercise the acceptance behavior.
4. Static/build/type evidence only for acceptance conditions genuinely established by those checks.
5. Bounded read-only provider metadata/log evidence only when the user asked to include deployment/incident state and `EXECUTION_SCOPE.md` permits it.

Code inspection may establish traceability or explain a blocked case, but it does not make an unexecuted behavioral case PASS.

Do not use browser/headless automation, screenshots, manual UI clicking, production/live app probes, live database writes, destructive migrations, paid calls, provider configuration writes, hosted CI dispatch, recurring monitoring, or background jobs.

## Status semantics

- **PASS** — expected behavior was actually exercised through an appropriate permitted channel and matched.
- **FAIL** — behavior was exercised and did not meet the expected outcome.
- **BLOCKED** — required access, environment, dependency, or permitted tooling was unavailable.
- **MANUAL** — acceptance requires an excluded human/browser/physical/external interaction with no permitted automated equivalent.
- **NOT APPLICABLE** — the traced requirement does not apply to this candidate, with reason.
- **NOT RUN** — temporary state only; final reports resolve it to another status.

Never convert BLOCKED or MANUAL to PASS by inference.

## Defects and autonomous repair

Standalone `PHDK uat` validates and reports the current candidate. It may repair UAT artifacts or the test harness needed to obtain truthful evidence, but it does not silently change unrelated product behavior.

When an active `PHDK auto` goal includes the candidate, an in-scope UAT FAIL is part of that same goal. Diagnose it, make the bounded in-scope repair, rerun the affected case and relevant regression checks, and update the artifacts before final delivery. No additional PHDK approval is required for that repair.

A defect requiring a new material product decision, unavailable access, undisclosed sensitive behavior, or out-of-scope work remains FAIL/BLOCKED with a concrete explanation.

## UAT report

`UAT_REPORT.md` must include:

- candidate repository, branch/PR/commit and product version when available;
- run date/time;
- UAT scope and source requirements;
- environment/harness, distinguishing local/in-process evidence from production;
- summary counts by PASS/FAIL/BLOCKED/MANUAL/NOT APPLICABLE;
- every case ID, result, and evidence;
- commands/tests/harnesses actually executed;
- defects and retest status;
- coverage gaps and excluded channels;
- final conclusion: ACCEPTED, NOT ACCEPTED, or ACCEPTANCE INCOMPLETE.

Use **ACCEPTED** only when all applicable cases PASS and no required acceptance evidence is BLOCKED or MANUAL. Use **NOT ACCEPTED** when any applicable case FAILs. Use **ACCEPTANCE INCOMPLETE** when there are no FAIL cases but required cases remain BLOCKED or MANUAL.

Never claim production, browser, or human acceptance evidence that did not occur.

## Relationship to Auto and delivery

`PHDK uat` is standalone and does not activate `PHDK auto`. Under active Auto, UAT becomes part of the final integrated acceptance boundary when end-user behavior is in scope: finish implementation, run final UAT, repair in-scope failures, rerun affected cases, then complete remaining final verification and delivery.

A standalone UAT run normally leaves product behavior unchanged unless the user separately asks for fixes. If UAT artifact/test-source changes are requested for repository delivery, follow `MAIN_DELIVERY_STANDARD.md` for versioning and delivery.

## Completion report

Do not stop after generating cases. Execute every feasible case and produce the report in the same request. Report the conclusion, totals, candidate revision/version, artifact paths, failures/blocked/manual gaps, and strongest evidence used.
