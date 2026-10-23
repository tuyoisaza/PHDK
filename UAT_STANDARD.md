## Risk-based tenant isolation acceptance

For multi-tenant UAT, use `TENANT_RISK_ASSESSMENT.md` and `PHDK_TENANT_RISK_STANDARD.md` to select authorization, data separation, storage/cache/search, files/exports, background/AI, backup and cryptographic controls that require evidence. Verify allow/deny journeys only with tagged, uniquely owned synthetic tenant records on the authorized deployed candidate following `PHDK_PRODUCTION_VERIFICATION.md`—never real customer data, local behavioral tests, Docker or new test databases. Cross-tenant leakage is Critical/High; unavailable proof is BLOCKED/UNVERIFIED and requires safe automated fixture cleanup.

## Mandatory UAT Prep handoff

After a fresh explicit `PHDK uat` invocation, inspect `PHDK_UAT_PREP.md` and the **current** `UAT_AUTH_PLAN.md`, `UAT_ROLE_MATRIX.md`, `UAT_FIXTURE_MANIFEST.md`, `UAT_PREP_REPORT.md` for the exact deployed candidate, real seeded/provider-backed synthetic identity, role/tenant readiness and cleanup. That invocation authorizes necessary Prep before acceptance; complete or reuse it within the existing application's authentication and security boundaries, recording truthful per-role blockers when access or a safe mechanism is unavailable. In an explicitly initiated lifecycle run, retain `45-uat-prep/HANDOFF.md`. Auto and Auto Force never run Prep and do not require its handoff to complete development. Standalone `PHDK uat prep` prepares readiness only and does not start UAT. Do not mark Prep's non-browser evidence as acceptance/browser PASS. At stage 50 run `UAT_BROWSER_READINESS_STANDARD.md` independently; Prep does not grant browser access.

## JWT and synthetic authentication gate

Before authenticated UAT/UAT Fix, read `JWT_STANDARD.md` and prepare `UAT_AUTH_PLAN.md`: map Company Co's fiction-only fixture users to **real provider/server-issued test sessions** for each actual application role, elevated admin/super_admin (tenancy-appropriate) included. Do not request passwords or raw bearer tokens from the owner, forge JWTs, add production backdoors or mistake a seed record for a logged-in identity. Use the existing legitimate application/provider mechanisms under `PHDK_PRODUCTION_VERIFICATION.md`; necessary readiness repairs belong to authorized Prep, while acceptance defects require explicitly authorized UAT Fix. Exercise positive/negative API and browser journeys only in the authorized UAT scope. Redact state, revoke grants and report evidence or precise remaining blockers.

## Company Co standard fixture (mandatory evaluation)
Before preparing UAT datasets, read `USE_COMPANY_CO_INFO_FOR_DEMOS.md` and `UAT_JOURNEY_STANDARD.md`. Use synthetic Company Co staff, 17 leaders/departments, buyer/customer and supplier profiles when applicable. Map the records to the actual schema, seed idempotently, provision scoped test accounts, prove Superadmin test-profile switching, and document all resulting UAT actions/evidence. Do not send bulk emails or use live financial transactions as fixture side effects.

## Mandatory persona journeys, test identities and next action

Before executing explicitly authorized UAT, obey `UAT_JOURNEY_STANDARD.md` fully: inspect actual profiles and source-backed permissions, verify access to the existing deployed production candidate, prepare safe run-owned synthetic role accounts when absent, verify Superadmin audited role switching, plan stories by persona, execute observable browser/API journeys, retain per-step evidence and retest authorized repairs. Generate the role/access/stories/journey map and retest artifacts listed there. End every UAT/UAT Fix response with an exact `SIGUIENTE PASO` instruction; do not wait unnecessarily when autonomous work remains. Production URLs do not imply permission to affect real production data or bypass authentication.

## CRUD acceptance gate

For applicable projects, use `CRUD_STANDARD.md` and `CRUD_MATRIX.md` to exercise permitted Create, Read-list/detail, Update, and Delete/archive in real flows and negative tests for forbidden actions, direct API access, cross-tenant IDs, validation, failure states and persistence. A listed admin record without a working appropriate detail view is FAIL. Record evidence or BLOCKED/MANUAL; never infer PASS from buttons alone.

# PHDK UAT Standard

## Mandatory UX/UI acceptance

On UI-applicable projects, follow `PHDK_UX_UI.md` and deliver `UX_UI_AUDIT_REPORT.md` in the UAT handoff. Exercise critical user journeys and relevant state, responsive, keyboard/focus, contrast and interaction checks in the authorized UAT browser scope when available; classify untested browser evidence BLOCKED/MANUAL. P0/P1 confirmed usability/accessibility failures prevent ACCEPTED. Document in-scope repairs in `UX_UI_REMEDIATION_REPORT.md` and retest affected flows. Brownfield redesigns compare baseline vs target and verify preserved behavior. No browser actions outside permitted UAT/UAT Fix environments.

## Scoped browser exception for UAT and UAT Fix
### Mandatory browser entry and no-new-spend gate

Before browser-dependent cases, follow `UAT_BROWSER_READINESS_STANDARD.md`: explicitly distinguish scoped phase permission from actual tool availability; verify one harmless browser operation against the authorized candidate; log proof/error, safe target and spend disposition in `UAT_ACCESS_REPORT.md` and `UAT_REPORT.md`. No invented budget ceilings, paid browser/API purchases or approval pauses just for an unavailable browser. Continue independent safe UAT cases; BLOCKED/MANUAL is not PASS. Require only genuine host connection/production authorization.


**Only** during an explicitly initiated `PHDK uat` run, explicit `PHDK uat fix`, or a retest authorized within that active UAT run, a connected/available browser, browser MCP, Playwright, Cypress or equivalent may be used to exercise real user journeys, UI behavior, responsiveness and accessibility and capture timestamped screenshots/evidence. This narrow exception applies **only to those UAT phases**; Auto, Auto Force, PMO or Designer Mode alone do not activate it. It does not activate browser work during Capture, Plan, Prep, implementation, generic verification, Check or Delivery. Delegated work inherits the same scoped authorization and host controls.

Use only the existing versioned production application and database with uniquely run-owned synthetic accounts/fixtures under `PHDK_PRODUCTION_VERIFICATION.md`. Confirm the target, allowed operations and cleanup before writes; do not create local/staging deployments or test databases. Never perform real purchases, send real emails, mutate real customer data, bypass authentication, extract secrets, expose personal data, modify provider/repository settings, or call paid services without separate authorization. No unattended monitoring or background jobs; revoke temporary sessions and verify cleanup on every outcome. Do not open a browser merely to diagnose deployment status.

For each test record the candidate revision, target environment, case ID, steps, expected/actual result and redacted screenshot or trace reference. After applying `JWT_STANDARD.md`'s supported synthetic provider/session bootstrap options, stop or mark BLOCKED when browser access, a safe environment or legitimate test identity issuance are still unavailable; **never** infer PASS from code inspection or claim browser evidence not collected. Close browser sessions after the active UAT execution. UAT Fix may rerun the impacted browser cases after permitted code repairs.

## Command and purpose

Before substantive execution, run the universal preflight in `PHDK_PREFLIGHT.md`. Inside a lifecycle run, verify Integration Review and the later `45-uat-prep` handoff with matching candidate, real synthetic role/access readiness or explicit per-role blockers before deriving/executing UAT. Verify the active PHDK installation/version and inspect/use stage-relevant available skills from `SKILLS_REGISTRY.md`, unless the user explicitly disabled them.

`PHDK uat` runs autonomous user acceptance testing for the identified current product candidate. Match the command case-insensitively after trimming whitespace. Use the current conversation, repository requirements, product documentation, acceptance criteria, current task, code, and existing test evidence to identify the candidate and scope. If no candidate or product goal can be determined, ask only for that missing target.

Only a fresh explicit owner invocation of `PHDK uat` starts acceptance and its necessary Prep prerequisite. The command authorizes the assistant to create or refresh UAT artifacts, derive acceptance cases, execute every permitted acceptance check available for those cases, collect evidence, and write the final report without requesting approval between cases. It does not authorize unrelated product development, browser testing outside the narrowly scoped UAT exception, live destructive operations, provider configuration writes, recurring work, or work after the conversation. Product-code remediation requires explicit `PHDK uat fix` or specific repair authorization within the active explicitly initiated UAT run.

## Required artifacts

Use explicit existing equivalents when the repository already defines them. Otherwise create:

- `UAT_MILESTONE_MATRIX.md` — milestone → user story → requirement/criterion → UAT case → evidence traceability for projects with a milestone plan.
- `UAT_CASES.md` — durable catalog of acceptance/use cases.
- `UAT_REPORT.md` — evidence and conclusion for the current candidate/run.

## Intent-first user stories and case catalog

Before deriving UAT cases, identify the project's current intent from the strongest available source in this order: `PROJECT_INTENT.md`, `REQUIREMENTS_TRACEABILITY.md`, `PROJECT_BRIEF.md`, `PRD.md`, `FEATURES.md`, relevant `docs/intents/*-intent.md`, the current authorized request, and the current `TASK.md`. Use `PHDK_CAPTURE.md` when the project-level why/requirements baseline is missing or incoherent; use `INTENT_CAPTURE_STANDARD.md` for later feature/change-level intent.

Every UAT user story must align with that intent. Express each story in user-value form such as "As <actor>, I want <goal>, so that <intent-linked outcome>." The "so that" outcome must point to a stated project problem, desired outcome, business/user objective, or explicit constraint. Do not create stories merely because the code contains a route, component, API, database field, or implementation detail.


When `MILESTONE_PLAN.md` exists, read it before authoring stories and create/update `UAT_MILESTONE_MATRIX.md`. Every delivered milestone must have **at least one user-value story** that validates why that milestone exists; a milestone with multiple actors or materially independent acceptance outcomes requires multiple stories/cases. UAT executes against the final integrated candidate, so also add cross-milestone stories where value depends on several increments. A technical/enabling milestone still needs an observable consumer/operator outcome or explicit acceptance story; do not fabricate a persona that has no real stake.

Maintain an explicit traceability chain:

**Project Intent → Milestone → User Story → Requirement / Acceptance Criterion → UAT Case → Evidence**

A user story is invalid for UAT when its value cannot be traced to the current project intent. Mark it **OUT OF INTENT** and exclude it from acceptance counts rather than silently expanding project scope. If an apparently necessary story contradicts the recorded intent, report the conflict as a product-scope decision; do not rewrite project intent from implementation evidence.

Derive cases from the actual product and changed behavior. Cover applicable primary actors and goals, happy paths, authorization boundaries, invalid input, important empty/error/retry states, state transitions, cross-feature flows, business rules, accessibility/i18n requirements, and regressions materially affected by the candidate.

Every user story must contain a stable story ID such as `US-001`, actor, user goal, intent-linked outcome, source intent reference, and linked milestone ID(s) when a milestone plan exists.

Every case must contain:

1. Stable ID such as `UAT-001`.
2. Linked user story ID and actor.
3. Intent source and requirement/acceptance-criterion traceability.
4. Preconditions and test data/fixtures.
5. User/business actions.
6. Expected observable outcome.
7. Permitted validation channel.
8. Result: NOT RUN, PASS, FAIL, BLOCKED, MANUAL, or NOT APPLICABLE.
9. Evidence reference.
10. Defect/reference when failed.

Keep cases deterministic and repeatable. Do not inflate the catalog with cosmetic permutations that do not represent distinct acceptance risk.

Before execution, perform an **Intent Alignment Gate**:

- every applicable user story has a valid intent source;
- every applicable UAT case links to a user story;
- every applicable user story has at least one UAT case unless explicitly justified;
- no UAT case validates behavior that is outside or contrary to the current intent;
- non-goals and constraints from the intent are represented where they materially affect acceptance.

If this gate fails, acceptance is incomplete until the traceability defect is repaired or reported.

## Execute autonomously

Run the strongest permitted evidence for each case without waiting for approval.

Preferred evidence:

1. Existing permitted acceptance/API/browser checks exercising the exact deployed production revision with run-owned synthetic fixtures.
2. Focused automated test sources added when needed, delivered through the authorized source workflow and executed only against that permitted deployed candidate.
3. Direct user journeys and API evidence in the scoped UAT environment, with actual role/tenant isolation and cleanup evidence.
4. Static/build/type evidence only for acceptance conditions genuinely established by those checks.
5. Bounded read-only provider metadata/log evidence only when the user asked to include deployment/incident state and `EXECUTION_SCOPE.md` permits it.

Code inspection may establish traceability or explain a blocked case, but it does not make an unexecuted behavioral case PASS.

Use browser/headless automation, screenshots and UI clicking only within the scoped UAT exception above. Do not perform unauthorized production/live app probes, unscoped or real-data database writes, destructive migrations, paid calls, provider configuration writes, hosted CI dispatch, recurring monitoring or background jobs. Any permitted synthetic write requires exact run ownership and verified cleanup.

## Status semantics

- **PASS** — expected behavior was actually exercised through an appropriate permitted channel and matched.
- **FAIL** — behavior was exercised and did not meet the expected outcome.
- **BLOCKED** — required access, environment, dependency, or permitted tooling was unavailable.
- **MANUAL** — acceptance requires an unavailable or excluded human/physical/external interaction with no permitted automated equivalent.
- **NOT APPLICABLE** — the traced requirement does not apply to this candidate, with reason.
- **NOT RUN** — temporary case status inside an authorized UAT run; final UAT reports resolve required unexecuted cases to BLOCKED/MANUAL as appropriate. Auto's separate **UAT NOT RUN** delivery statement is valid and does not imply a failed or blocked development goal.

Never convert BLOCKED or MANUAL to PASS by inference.

## Defects and autonomous repair

Explicit `PHDK uat` prepares the necessary safe readiness, validates and reports the current candidate. It may repair UAT artifacts or in-scope preparation needed to obtain truthful evidence, but it does not silently change unrelated product behavior or authorize product defect remediation.

After explicit `PHDK uat fix` or repair authorization within the active explicitly initiated UAT run, diagnose in-scope failures, make bounded repairs, deliver the changed candidate, rerun affected permitted cases and update the evidence without per-defect approval. Auto and Auto Force do not enter UAT Fix, rerun acceptance or reopen completed development because an earlier UAT report contains FAIL cases.

A defect requiring a new material product decision, unavailable access, undisclosed sensitive behavior, or out-of-scope work remains FAIL/BLOCKED with a concrete explanation.

## UAT report

`UAT_REPORT.md` must include:

- candidate repository, branch/PR/commit and product version when available;
- run date/time;
- project intent sources and intent-alignment summary;
- user-story coverage and any OUT OF INTENT items;
- UAT scope and source requirements;
- exact deployed production environment/revision and permitted harness, distinguishing static source evidence from executed acceptance;
- summary counts by PASS/FAIL/BLOCKED/MANUAL/NOT APPLICABLE;
- every case ID, result, and evidence;
- commands/tests/harnesses actually executed;
- defects and retest status;
- for every FAIL: observed failure, expected behavior, probable root cause, affected requirement/story/case, affected component/files when identifiable, proposed repair, repair risk/scope, and exact retest needed;
- coverage gaps and excluded channels;
- an **Action Plan** for every FAIL, BLOCKED, and MANUAL case that prevents ACCEPTED status;
- final conclusion: ACCEPTED, NOT ACCEPTED, or ACCEPTANCE INCOMPLETE.

Use **ACCEPTED** only when the Intent Alignment Gate passes, all applicable stories are covered, all applicable cases PASS, and no required acceptance evidence is BLOCKED or MANUAL.

## Mandatory action guidance for incomplete UAT

When the conclusion is NOT ACCEPTED or ACCEPTANCE INCOMPLETE, the report must never stop at status labels. It must tell the owner what to do next.

For every unresolved FAIL, BLOCKED, or MANUAL case include an actionable card with:

- **Case / defect ID**
- **What is preventing acceptance**
- **Why it matters** — requirement, intent, risk, or acceptance criterion affected
- **What must happen**
- **Who/what must act** — assistant/code change, repository owner, provider/admin, human reviewer, or other dependency
- **Where** — repository file/component, environment, provider, account, browser/manual flow, or external system
- **How** — concrete repair/verification steps in order
- **When** — prerequisite/order relative to other actions
- **Evidence needed to close it**
- **After that** — exact retest/UAT command or next PHDK command
- **Can PHDK do it now?** — YES / PARTIAL / NO, with reason

Then add a top-level **Recommended next actions** section ordered by dependency and impact. It must be concrete enough that the owner can follow it without reverse-engineering the UAT files.

Examples:

- If a case is BLOCKED because a safe browser environment or manual flow is unavailable, say exactly which flow a human must exercise, what result to record, and what command/report to rerun afterward.
- If a case is BLOCKED because an external secret/access/provider setting is missing, identify the missing prerequisite without exposing secrets, identify where it must be configured, and state what evidence should be supplied back.
- If a case is MANUAL because visual/UX acceptance is required, provide a human review checklist and expected acceptance evidence.
- If no FAIL exists but BLOCKED/MANUAL cases remain, explicitly say: **"No hay defectos de código reparables automáticamente; la aceptación está incompleta por estos prerequisitos/validaciones pendientes."**

Never answer only "no hay FAIL" when acceptance is incomplete. Use **NOT ACCEPTED** when any applicable case FAILs. Use **ACCEPTANCE INCOMPLETE** when there are no FAIL cases but required cases remain BLOCKED or MANUAL.

Never claim production, browser, or human acceptance evidence that did not occur.

## UAT lifecycle handoff

At the end of UAT, create `docs/phdk/lifecycle/<run-id>/50-uat/HANDOFF.md` and snapshot `UAT_CASES.md` + `UAT_REPORT.md`. Record the acceptance conclusion and the exact inputs required by UAT Fix or Check.

If the conclusion is ACCEPTED and no UAT remediation is required, record UAT Fix as NOT APPLICABLE for this run before Check starts.

## Repair command — PHDK uat fix

`PHDK uat fix` takes the current `UAT_REPORT.md` and `UAT_CASES.md` as its repair backlog.

For every FAIL, first normalize it into an actionable defect with:

- defect ID;
- UAT case/story/requirement links;
- observed vs expected behavior;
- evidence;
- likely root cause and confidence;
- affected source/component;
- proposed repair;
- scope/risk classification;
- retest command/case.

Then execute all repairs that are clearly within the current product intent and do not require a new material product/security/infrastructure decision.

Treat a BLOCKED case as potentially repairable when the blocker is a source-level defect within the authorized repair scope. Examples include a missing safely scoped fixture seeder, legitimate session integration or cleanup/revocation support. In those cases, `PHDK uat fix` should repair the smallest appropriate support, deliver the changed candidate, rerun the case only in the permitted deployed environment and update the evidence. Do not add authentication bypasses, local runtime harnesses or new test databases to make a case pass.

A BLOCKED case is non-removable only when the missing prerequisite is genuinely external or excluded, such as a unavailable/unauthorized browser environment, provider/account access, real secret, live environment, manual approval, or external system state. Do not ask for approval per failure. Repair autonomously, run the affected tests/UAT cases, update the report, and continue until all fixable FAILs are resolved or only concrete blockers/decisions remain.

If a FAIL requires a new material product decision, unavailable access, external/manual action, unavailable/unsafe browser evidence, provider write, or out-of-scope behavior, do not guess. Leave it unresolved with the exact blocker and required decision.

`PHDK uat` authorizes acceptance and necessary Prep; product-code repairs from its failure backlog require explicit `PHDK uat fix` or specific repair authorization within that active explicitly initiated UAT run. Auto and Auto Force provide neither UAT execution nor UAT Fix authority. A prior failure report is evidence for a later authorized repair, not a command to resume one.

Create/update `UAT_REMEDIATION.md` during UAT Fix. It must list each defect/blocker, root cause, repair/action, affected components, retest evidence, resolution state, and remaining manual/external action.

After repair, rerun affected UAT cases and necessary regression checks, then regenerate `UAT_REPORT.md` with:
- RESOLVED / STILL FAILING / BLOCKED status per defect;
- repair commit/revision when available;
- retest evidence;
- updated final acceptance conclusion.

Inside a lifecycle run, create `docs/phdk/lifecycle/<run-id>/60-uat-fix/HANDOFF.md` and snapshot `UAT_REMEDIATION.md`, `UAT_REPORT.md`, and `UAT_CASES.md`. Check must verify this latest handoff/status rather than assuming acceptance from an older report.

If the user also requested normal repository delivery, follow `MAIN_DELIVERY_STANDARD.md`.

## Relationship to Auto and delivery

`PHDK uat` is an explicit acceptance command and does not activate `PHDK auto` or PMO. Auto and Auto Force complete authorized implementation, permitted static checks, integration, applicable SEO/AEO, Check/remediation and verified delivery without entering, provisioning, seeding or running UAT Prep, UAT or UAT Fix. These stages remain **DEFERRED — OWNER OPT-IN**. Report the actual **DEVELOPMENT COMPLETE / PARTIALLY DELIVERED / BLOCKED** outcome separately from **UAT NOT RUN**; absent UAT is not a development completion prerequisite. Offer `PHDK uat` as an optional future command without waiting for acceptance authorization as a delivery gate.

When the owner later explicitly invokes `PHDK uat`, use the final integrated and deployed candidate, including PMO integration evidence when applicable; worker-level passes do not replace integrated acceptance. Preserve milestone-to-story/criterion mapping as documentation during development without provisioning UAT fixtures. Explicit `PHDK uat prep` alone does not start acceptance, and historical UAT failures never reopen the completed development goal. Deliver authorized preparation or repair source changes through `MAIN_DELIVERY_STANDARD.md` before testing the revised deployed candidate.

## Completion report

Do not stop after generating cases. Execute every feasible case and produce the report in the same request. Report the conclusion, totals, candidate revision/version, artifact paths, failures/blocked/manual gaps, strongest evidence used, and a prioritized next-action plan whenever the conclusion is not ACCEPTED. When FAILs exist, include the recommended next command `PHDK uat fix`. When only BLOCKED/MANUAL items remain, explain exactly how to unblock/perform them and what to rerun afterward.


## Production-first verification override (v2.58.0)

**Mandatory:** Apply [PHDK_PRODUCTION_VERIFICATION.md](PHDK_PRODUCTION_VERIFICATION.md). Owner-authorized production-only UAT supersedes earlier local unit/in-process/runtime testing, staging-only identity, and blanket production-test prohibitions. Local operations are limited to static analysis, lint, typecheck and safe builds; Docker, local runtime tests and separate staging/databases are prohibited. UAT must use existing versioned production deployment and existing database, strictly scoped run-owned synthetic identities/records, audit, automated cleanup and verified revocation on success, failure and interruption. Never touch real data or bypass existing security hooks; apply the [hook decision procedure](PHDK_HOOK_COMPATIBILITY.md#decision-procedure) before reporting an unresolved verification gate BLOCKED.
