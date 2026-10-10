# PHDK Check Standard

## Command and purpose

`PHDK check` audits the current repository against the active PHDK standards and produces a concrete remediation backlog. The command is intentionally two-phase:

1. **Audit phase — read-only:** inspect PHDK and the repository, classify gaps, write or refresh `PHDK_CHECK_REPORT.md`, present the results, and ask once whether the user wants the listed remediation executed.
2. **Remediation phase — only after explicit yes:** execute the approved, enumerated gaps through the normal PHDK development and delivery rules, then rerun the check and report the residual gap.

The first `PHDK check` command does not authorize product-code changes, version bumps, commits, pushes, merges, provider writes, or settings changes in the audited project. It authorizes the audit artifact itself when the user asked to persist the report; otherwise report in chat and keep the repository unchanged. A later clear `yes`, `sí`, `ejecuta`, `hazlo`, or equivalent answer to the presented remediation question authorizes the enumerated remediation scope in the same conversation.

## What PHDK to read

Read the repository's active PHDK installation completely enough to evaluate compliance:

- `VERSION` and `PHDK_MANIFEST.txt`;
- every active manifest-controlled PHDK standard that exists in the project;
- root/native instruction files and owner prefaces that govern the repository;
- `PROJECT_INTENT.md`, `REQUIREMENTS_TRACEABILITY.md`, project brief/PRD/features, feature intents, requirements, and architecture decisions needed to determine applicability;
- `TASK.md` / `STATUS.md` as state evidence, not authority;
- repository hooks, package scripts, source layout, tests, configuration, version sources, and relevant code.

Do not treat `ORIGINALS/`, archived changelogs, completed-task archives, examples, or historical superseded instructions as current standards.

If canonical upstream PHDK is reachable, compare the installed version/manifest to canonical `main`. Version drift is itself a gap. Do not silently upgrade during the audit. If remediation is later approved and the installed standards are stale, synchronize PHDK first, then rerun the audit before applying product changes because the compliance target may have changed.

## Applicability before compliance

PHDK contains conditional standards. Do not mark a repository noncompliant merely because it lacks something the project does not need.

For every requirement, classify applicability first using project intent, PRD/features, architecture decisions, current product type, and code reality.

Examples:

- A public marketing site is not missing RBAC merely because PHDK defines RBAC defaults for role-bearing apps.
- A repository without AI features is not missing `packages/ai`.
- A repository with actual AI provider usage must satisfy `AI_ADMIN_STANDARD.md`. Detect provider/config evidence without reading secret values. If only an unused key placeholder exists and no AI feature can be established, use UNKNOWN / DECISION NEEDED rather than inventing AI product scope.
- A project with no schema change is not missing a migration.
- A project whose intent explicitly excludes authentication is not noncompliant for lacking login.

When applicability is ambiguous, classify the item **UNKNOWN / DECISION NEEDED** rather than inventing scope.

## Compliance model

Every evaluated requirement receives one status:

- **COMPLIANT** — repository evidence satisfies the applicable PHDK requirement.
- **GAP** — applicable requirement is not satisfied.
- **PARTIAL** — some required behavior/evidence exists but is incomplete.
- **NOT APPLICABLE** — requirement does not apply, with reason.
- **UNKNOWN / DECISION NEEDED** — applicability or intended behavior cannot be established from current evidence.
- **UNVERIFIED** — the requirement may be implemented but the permitted audit channels cannot establish compliance.

Never mark COMPLIANT from filenames alone when the standard requires behavior. Inspect the relevant source/configuration/test evidence.

## Gap severity and remediation type

For each GAP/PARTIAL item, assign:

- **Critical** — security, authorization, privacy, destructive-data, or release-integrity violation with material impact.
- **High** — required product behavior, data integrity, authentication, architecture boundary, or mandatory delivery control is materially missing.
- **Medium** — important maintainability, observability, testing, accessibility, i18n, or standards requirement is incomplete.
- **Low** — documentation, consistency, naming, or low-risk hygiene gap.

Also classify the remediation:

- **AUTO-FIXABLE** — requirements and desired end state are unambiguous; the assistant can implement it under current standards.
- **FIXABLE WITH VALIDATION** — implementable, but requires tests/checks to prove the result.
- **DECISION REQUIRED** — fixing it would choose new product behavior, architecture, security policy, data policy, paid service, or infrastructure not already established by project intent.
- **EXTERNAL / MANUAL** — requires an external provider setting, secret, access grant, browser/manual process, live migration, or other excluded operation.

The user's later `yes` authorizes AUTO-FIXABLE and FIXABLE WITH VALIDATION gaps in the published report, plus ordinary supporting changes necessary to implement them. It does not answer DECISION REQUIRED items or authorize EXTERNAL / MANUAL operations.

## Required report

Use `PHDK_CHECK_REPORT.md` unless the repository already defines an explicit equivalent.

The report must include:

### Header
- repository and audited branch/commit;
- installed PHDK version;
- canonical PHDK version when checked;
- audit date/time;
- project intent sources used;
- files/standards inspected.

### Executive summary
- counts: COMPLIANT, GAP, PARTIAL, NOT APPLICABLE, UNKNOWN, UNVERIFIED;
- gaps by severity;
- whether PHDK version drift exists;
- overall status: **ALIGNED**, **GAPS FOUND**, or **ALIGNMENT INCOMPLETE**.

### Gap table
For every GAP/PARTIAL item:
- stable ID, e.g. `CHK-001`;
- severity;
- PHDK standard + section/rule;
- applicability rationale;
- repository evidence;
- exact missing behavior/evidence;
- remediation type;
- proposed remediation;
- files/components likely affected;
- validation required;
- dependencies on other gaps.

### Non-gap evidence
Summarize important COMPLIANT and NOT APPLICABLE findings so the report is auditable and not merely a to-do list.

### Decisions and external blockers
List UNKNOWN / DECISION NEEDED, UNVERIFIED, and EXTERNAL / MANUAL items separately. Do not hide them inside the fixable backlog.

### Proposed execution order
Order fixable gaps by dependency and risk. Combine duplicate root causes instead of proposing repeated edits.

## Audit procedure

1. Pin the repository revision being audited.
2. Read the Capture requirements package first when present (`PROJECT_INTENT.md`, `PROJECT_BRIEF.md`, `PRD.md`, `FEATURES.md`, `REQUIREMENTS_TRACEABILITY.md`) so standards applicability is grounded in what the product is meant to be. If those artifacts are missing/incoherent, record a requirements-baseline gap and recommend `PHDK capture`; do not fabricate applicability from code alone.
3. Identify the active PHDK version/manifest and current governing instructions.
4. Check canonical PHDK version when accessible; record drift without mutating the repository.
5. Read all applicable active standards; build an internal requirement matrix.
6. Inspect repository source, configuration, scripts, tests, docs, versioning, hooks, and delivery metadata needed to evaluate each requirement.
7. For AI-bearing repositories, evaluate `AI_ADMIN_STANDARD.md`: centralized provider access, token/cost tracking, super-admin consumption, Prompts navigation/route, prompt list/editor fields, output-schema validation, audit/revisions, and prompt/revision attribution.
8. Distinguish implementation absence from verification absence.
9. Deduplicate findings by root cause.
10. Produce the report and a concise prioritized summary.
11. Ask exactly one execution question: **"¿Quieres que ejecute los gaps AUTO-FIXABLE y FIXABLE WITH VALIDATION de este reporte?"**
12. Stop. Do not begin remediation until the user answers.

Do not manufacture exhaustive certainty when access is incomplete. Prefer UNKNOWN/UNVERIFIED over speculation.

## Remediation after yes

After explicit approval in the same conversation:

1. Freeze the approved gap IDs and report revision so scope is clear.
2. If PHDK itself is stale and that gap is approved, run the standards synchronization first, then regenerate the gap report before product remediation. Explain any new/removed gaps caused by the standards update; do not silently expand to newly discovered material decisions.
3. Build one coherent remediation plan from the approved AUTO-FIXABLE / FIXABLE WITH VALIDATION items.
4. Follow project intent. Closing a PHDK gap must not create features that conflict with the product's intent or non-goals.
5. Implement autonomously without asking for approval per file or gap.
6. Run the applicable checks and UAT where user-facing behavior changes. Use `PHDK auto` cadence for the remediation batch only when the approved gap set forms a development goal; the `yes` itself is enough authorization for the listed fixes.
7. Preserve actual hooks, protections, required reviews, access controls, and execution boundaries.
8. Version, commit, push, PR, and merge under `MAIN_DELIVERY_STANDARD.md` when the approved remediation request targets repository delivery.
9. Rerun `PHDK check` against the resulting candidate/main.
10. Update `PHDK_CHECK_REPORT.md` with resolved gap IDs, residual gaps, evidence, and final alignment status.

Do not fix DECISION REQUIRED or EXTERNAL / MANUAL items merely because they appeared in the same report. Ask only for the specific decision or external action when it is the remaining blocker.

## Relationship to other commands

- **`PHDK check`** audits standards compliance and asks before remediation.
- **`PHDK auto`** continuously develops an already-authorized product goal; it does not automatically trigger a full standards compliance sweep.
- **`PHDK uat`** validates intent-aligned user acceptance behavior; it can provide evidence for check findings but does not replace the broader standards audit.
- **`PHDK unlock`** reconciles PHDK-related blockers; it is not a general compliance audit.
- **`PHDK upgrade`** synchronizes PHDK standards; it does not by itself remediate the repository to match them.
- **Developer Mode** remains a narrow direct-main mode for eligible small changes and does not bypass the check audit/approval split.

## Completion semantics

The audit phase is complete only when the report exists (when persistence was requested or expected by the repository workflow), the prioritized gap list is presented, and the user has been asked whether to execute the fixable gaps.

The remediation phase is complete only after approved fixable gaps are implemented, verified, delivered to the requested target, and the check is rerun. Report residual DECISION REQUIRED, EXTERNAL / MANUAL, UNKNOWN, or UNVERIFIED items explicitly. Never call the repository fully aligned while unresolved applicable gaps remain.
