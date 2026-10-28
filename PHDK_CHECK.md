**Hybrid Secure (v2.63.0):** During Auto/Force, perform milestone security deltas and a consolidated `PHDK secure` gate after integration and before final Check/delivery, following [PHDK_SECURE.md](PHDK_SECURE.md). Secure is development validation only: it never initiates UAT Prep/UAT/Fix, forbidden local runtime tests, Docker, new infrastructure or paid scans. Remediate authorized vulnerabilities, preserve real security gates, record evidence and residual risk; Critical/High confirmed issues block clearance absent an explicit permitted owner risk decision.

## Tenant-risk assessment and isolation compliance gate

Apply `PHDK_TENANT_RISK_STANDARD.md` to actual/proposed multi-tenant projects. Check `TENANT_RISK_ASSESSMENT.md`, owner-approved inherent/residual tier, baseline authorization/isolation across database/storage/cache/search/AI/jobs/exports/backups, TLS and at-rest encryption, risk-proportional key/field encryption, evidence-backed negative tenant access and safe UAT cleanup. Do not require a dedicated database for all tenants if the approved risk can be controlled with demonstrably enforced shared isolation. Missing decision is DECISION REQUIRED, missing baseline is GAP, leakage/bypass is Critical/High, and missing evidence within explicitly authorized acceptance is UNVERIFIED. Under Auto, runtime acceptance is deferred and cannot become a delivery blocker. Bare Check stays read-only; `check --fix` does not authorize infrastructure or risk acceptance. Obey `PHDK_PRODUCTION_VERIFICATION.md`.

# PHDK Check Standard

## Portfolio-first consistency (v2.74.0)

When relevant, inspect the project's adopted `TECHNICAL_STACK.md` baseline and ADRs, Plan's REUSE/ADAPT/BUILD reasoning, and `PHDK_REUSE_CATALOG_STANDARD.md`. Flag unjustified duplication, unsupported implementation/reuse claims, and undocumented material stack drift proportionately. Do not block delivery on a separate catalog contribution, imply that specification-only starters are usable, upgrade consumers, run local behavioral tests or administer a host. Local lint, static analysis, typechecks and safe builds remain permitted under `PHDK_PRODUCTION_VERIFICATION.md`.

## Mandatory documentation and nomenclature audit (v2.73.0)

Apply [PHDK_DOCUMENTATION_STANDARD.md](PHDK_DOCUMENTATION_STANDARD.md) to the **current candidate**. For new or materially revised project documents, audit the category paths, `kebab-case.vN.md` names, truthful front-matter version/status/authority/dates, unique active baseline per document ID, stable ADR supersession, matching `docs/INDEX.md`, root `TASK.md` links, milestone/intent/decision/evidence cross-references, and stale duplicate root documents. Prefer the vendored read-only `phdk-standards/scripts/phdk_docs_audit.py --root . --check` plus `--changed` for in-scope paths, and inspect semantic links manually; static filename checks alone are insufficient.

Bare `PHDK check` is read-only: **never** run `--sync-index` or migrate documents during its audit. Classify new mismatches as GAP/PARTIAL, missing access as UNVERIFIED, and untouched brownfield root paths as LEGACY_COMPATIBLE/low-priority debt rather than a blanket deployment blocker. Inside authorized Auto/Auto Force or explicit Check Fix, repair in-scope documents, update the index, rerun the read-only audit and record evidence without expanding the product scope or invoking UAT. The index is a locator, not proof of implemented features or approval.


## Live deployment-version endpoint compliance (non-UAT)

For PHDK-managed HTTP applications or APIs with an existing reachable production hostname, apply `PHDK_DEPLOYMENT_VERSION_STANDARD.md` and inspect the actual `GET /health/version` source route, public safe JSON payload, authoritative application version, exact deployed full SHA provenance, vendored PHDK version, immutable build timestamp, and `Cache-Control: no-store` headers. Require source test coverage for stale/missing provenance and SPA catch-all failures; absence of the route is GAP, incomplete/mocked implementation is PARTIAL, unreachable deployment evidence is UNVERIFIED, and genuinely non-HTTP workloads are NOT_APPLICABLE. In an authorized delivery/version-check task only, permit the single bounded non-UAT GET per `EXECUTION_SCOPE.md`; bare read-only Check never starts application probing, provider writes, UAT or new infrastructure. Separate PUBLISHED, DEPLOYED_REVISION_CONFIRMED, health and ACCEPTED evidence.


## Historical and remote Git cleanup evidence check (read-only)

Inspect one-time historical inventory, local .git/phdk/git-hygiene-state.json state where accessible, actual merged-PR/head SHA proofs, preserved blocked worktrees, and observed remote branch disappearance after each milestone. A skipped remote deletion or unverified local checkout is reported separately; an open PR or dirty branch never becomes an auto-cleanable source. Bare PHDK check does not run --apply, delete remote refs, change provider settings or start historical cleanup. Apply current repository controls and keep UAT deferred.

## Local Git closeout evidence check (read-only)

For each previously published value milestone with a local checkout, inspect the actual `PHDK_GIT_WORKSPACE_CLOSEOUT.md` LOCAL_MAIN and LOCAL_CLEANUP evidence, local-vs-fetched-origin/main SHA and any retained active worktrees/branches. Bare `PHDK check` is read-only: never delete branches, run remote/provider writes or trigger cleanup from a stored task. Auto/Force perform actual closeout at the post-merge boundary before the next local milestone, then Check audits its evidence. If only a GitHub connector exists, record NOT_APPLICABLE_REMOTE_ONLY, never infer that the owner's computer was synchronized. Railway branch/deploy evidence is separate.

## Acceptance scope during Check

Check and Check remediation do not invoke UAT Prep, UAT or UAT Fix. Under Auto/Auto Force, report these phases `DEFERRED — OWNER OPT-IN` and `UAT NOT RUN`; evaluate source, static checks and delivery evidence without requiring acceptance handoffs, synthetic provisioning or runtime journeys. Keep actual missing product behavior and security defects as development findings, while optional acceptance execution remains deferred. Only a fresh explicit `PHDK uat` initiates acceptance and necessary Prep; standalone `PHDK uat prep` is prep-only, and UAT Fix needs explicit authorization. Old UAT failures do not automatically reopen completed development.

## UAT Prep implementation/evidence review

For an authenticated application with explicitly authorized Prep evidence to audit, apply `PHDK_UAT_PREP.md` and inspect actual idempotent run-owned synthetic provisioning, role/tenant matrix, legitimate provider/server-issued sessions, negative authorization evidence from the permitted deployed target, logout/revocation and verified cleanup. Review current `UAT_AUTH_PLAN.md`, `UAT_ROLE_MATRIX.md`, `UAT_FIXTURE_MANIFEST.md`, `UAT_PREP_REPORT.md` and any executed `45-uat-prep/HANDOFF.md` for the exact candidate. Fictional names or plans never prove READY; missing evidence within that authorized Prep scope remains UNVERIFIED or precisely BLOCKED. In Auto, Prep-only infrastructure, execution and handoffs are deferred and cannot become an auto-fixable provisioning task or a development-completion gate. Keep bare Check read-only and distinguish Prep readiness from browser acceptance. Production scope and safety follow `PHDK_PRODUCTION_VERIFICATION.md`.

## Synthetic UAT authentication and JWT evidence review

For each authenticated app, apply `JWT_STANDARD.md` to actual provider/session source and security configuration. Inspect role/tenant authorization, elevated admin versus multi-tenant super_admin, scoped Test as when a product requirement, expiry/revocation and cleanup controls. Review Company Co role coverage, `UAT_AUTH_PLAN.md`, `UAT_ACCESS_REPORT.md` and redacted runtime evidence only when available from an explicitly authorized acceptance run; never provision or issue sessions from Check. JWT-specific signature/issuer/audience/expiry/key checks apply only to apps using JWT; OAuth/cookie apps must not be forced to adopt JWT. Missing required product functionality or a source-backed security defect is GAP. UAT-only bootstrap and unexecuted acceptance remain `DEFERRED — OWNER OPT-IN` in Auto, with no behavioral PASS inferred from source. Bare Check stays read-only.

## Mandatory automation and provider-cost hygiene gate

For **every** project, apply `PHDK_AUTOMATION_HYGIENE.md` before marking Check aligned. Inventory locally checked-in GitHub Actions, scheduled agents/bots, repository watchers, Railway cron/restart/redeploy configuration, and also verify **live enabled workflow/runs and GitHub checks plus Railway Wait for CI, deployment triggers, restarts and usage** through authorized read-only provider metadata. Use vendored `scripts/phdk_automation_audit.py` as static evidence when available; its clean result never proves remote compliance. Preserve justified security CI, branch rules and GitHub-connected Railway autodeploy. Put findings in a dedicated **Automation and Cost Hygiene** section of `PHDK_CHECK_REPORT.md`, including owner/provenance, active state, dependency, cost/blockage risk, severity, remediation type and provider access gaps. For bare Check no mutations; within `check --fix` or Auto remove unambiguous obsolete PHDK-owned repository triggers only, never change provider settings or disable required checks. Unverifiable live state remains UNVERIFIED, not COMPLIANT.


## Mandatory UX/UI audit checks

For a UI-applicable project, apply `PHDK_UX_UI.md`: verify Plan design artifacts and historical snapshots, trace critical user journeys to requirements/tasks/UAT, inspect source fidelity and any current `UX_UI_AUDIT_REPORT.md`/`UX_UI_REMEDIATION_REPORT.md` evidence from explicitly authorized acceptance. Repair current in-scope source-backed P0/P1 defects under the active remediation authorization; missing or historical UAT evidence does not start acceptance or reopen completed development. In Auto, report runtime usability/fidelity as deferred. Do not assume an attractive screenshot proves usability. Audit phase remains read-only except permitted report artifact.


## Mandatory three-theme governance audit
For UI-applicable projects, inspect PHDK_THEME_STANDARD.md and run the vendored scripts/phdk_theme_audit.py from the audited project root when available. In PHDK_CHECK_REPORT.md record the actual CSS token file/import graph, light/dark/corporate token parity, duplicate palette sources, hardcoded component colors (with file:line), real platform-administrator Configuración → Edición de templates implementation (super_admin multi / admin single), editable/persisted values, corporate-theme show/hide flag and fallback, server-side authorization/validation, route coverage and executable test evidence. Missing phdk-theme.config.json, missing editor/flag, or hardcoded palette literals are GAP/PARTIAL, not COMPLIANT; a self-declared config or static scan pass is insufficient proof. For deferred Auto acceptance use `DEFERRED — OWNER OPT-IN` with `UAT NOT RUN`; for missing evidence inside an explicitly authorized acceptance audit use UNVERIFIED; distinguish API-only NOT APPLICABLE and projects without an authorized administrative surface (DECISION REQUIRED). Standalone bare Check stays read-only until remediation is authorized; explicit check --fix and in-scope Auto remediation continue under their existing authorization.

## Mandatory CRUD completeness audit

For applications with managed records, apply `CRUD_STANDARD.md`. Verify every listed administration record has an appropriate detail path; audit Create/Read-list/Read-detail/Update/Delete capabilities against the authorized per-role and public matrix, API enforcement, tenancy and UAT tests. Missing operations are GAP unless a documented legitimate exception applies. Missing development evidence is UNVERIFIED; acceptance not explicitly initiated remains deferred in Auto and is not a delivery blocker. Do not demand unsafe public mutations or deletion of immutable records.

## Mandatory administration-console contract

For every applicable stateful/administered portal, apply `ADMIN_CONSOLE_STANDARD.md` to the **actual code and authorization behavior**, regardless of vertical (CRM/ERP/LMS etc.). First detect/document single_tenant vs multi_tenant; recommend multi-tenancy when justified, but report an unresolved conversion as DECISION REQUIRED rather than silently applying schema/security changes. Verify the platform Settings navigation and working tabs, correct super_admin (multi) vs admin (single), tenant admin scope, tenant/member/role/permission CRUD, invitations, default locale, default tenant and user permissions, feature flags/debug/integrations, masked secret status, audited security, backups/recovery, role-test sessions, semantic theme templates, AI agent graph/catalog if AI is present, and role- and tenant-negative tests. Pin paths to UI, API, DB and test evidence in `ADMIN_CAPABILITY_MATRIX.md`, `ADMIN_ARCHITECTURE.md` and `ADMIN_SETTINGS_REGISTRY.md`. Absent required UI/API implementation is GAP/PARTIAL. In Auto, runtime acceptance evidence remains `DEFERRED — OWNER OPT-IN`; within an explicitly authorized acceptance audit, missing behavioral evidence is UNVERIFIED. Documentation alone never proves functioning behavior. An authenticated administrative app cannot classify the whole console NOT APPLICABLE solely for industry or complexity.

**One-command authorized repair:** An explicit `PHDK check --fix` or `PHDK check fix` invocation authorizes audit plus *enumerated* unambiguous AUTO-FIXABLE/FIXABLE WITH VALIDATION remediation in the same run. The assistant records the frozen gap IDs in the report, implements stack-specific UI/API/auth/migrations/tests, reruns validation and Check, and follows version/PR/merge/remote verification; it must still pause on material multi-tenant conversion, unapproved permissions/policies, live destructive actions, provider writes or external credentials. This is not the behavior of a bare `PHDK check`, which remains read-only until the user approves remediation. Under an authorized `PHDK auto`, already-in-scope fixes require no second permission.

## Command and purpose

Before substantive execution, run the universal preflight in `PHDK_PREFLIGHT.md`. Inside a lifecycle run, verify the latest authorized Integration/SEO/AEO-GEO handoffs (or justified N/A records); inspect UAT/UAT Fix handoffs only when explicitly authorized and actually executed, otherwise record acceptance as deferred under `PHDK_LIFECYCLE.md`. Audit the exact current candidate rather than an older revision. Verify the active PHDK installation/version and inspect/use stage-relevant available skills from `SKILLS_REGISTRY.md`, unless the user explicitly disabled them.

`PHDK check` audits the current repository against the active PHDK standards and produces a concrete remediation backlog. The bare command is intentionally two-phase (unless explicitly invoked as one-command `PHDK check --fix`):

1. **Audit phase — read-only:** inspect PHDK and the repository, classify gaps, write or refresh `PHDK_CHECK_REPORT.md`, present the results, and ask once whether the user wants the listed remediation executed.
2. **Remediation phase — only after explicit yes:** execute the approved, enumerated gaps through the normal PHDK development and delivery rules, then rerun the check and report the residual gap.

The first **bare** `PHDK check` command does not authorize product-code changes, version bumps, commits, pushes, merges, provider writes, or settings changes in the audited project. It authorizes the audit artifact itself when the user asked to persist the report; otherwise report in chat and keep the repository unchanged. A later clear `yes`, `sí`, `ejecuta`, `hazlo`, or equivalent answer to the presented remediation question authorizes the enumerated remediation scope in the same conversation.

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

Required behavior remains applicable before its code exists. A readable empty/scaffold-only project with confirmed product requirements has implementation GAPs; a partially implemented requirement is PARTIAL. Unavailable source/evidence is UNVERIFIED, not proof that the repository is empty. Never classify implementation or acceptance NOT APPLICABLE solely because it has not been developed. Under Auto, implement these already-in-scope gaps and reconcile affected upstream handoffs; a plan alone cannot close them.

Examples:

- A public marketing site is not missing RBAC merely because PHDK defines RBAC defaults for role-bearing apps.
- A project whose confirmed intent does not require AI features is not missing `packages/ai`; an authorized AI feature that has not been built is an implementation gap.
- A repository with actual AI provider usage must satisfy `AI_ADMIN_STANDARD.md`. Detect provider/config evidence without reading secret values. If only an unused key placeholder exists and no AI feature can be established, use UNKNOWN / DECISION NEEDED rather than inventing AI product scope.
- A project with no schema change is not missing a migration.
- A project whose intent explicitly excludes authentication is not noncompliant for lacking login.

When applicability is ambiguous, classify the item **UNKNOWN / DECISION NEEDED** rather than inventing scope.

In active AUTO FORCE, apply [Propose missing definitions and solutions](PHDK_AUTO_CONTINUITY.md#propose-missing-definitions-and-solutions) before treating missing detail as UNKNOWN or DECISION REQUIRED. For a capability already within the authorized goal, recover the relevant current rules and existing product decisions, define the missing behavior with reasonable safe reversible defaults, identify configuration that is useful and consistent with those rules, and record the rationale and acceptance criteria. Implement the inferable authorized result as AUTO-FIXABLE or FIXABLE WITH VALIDATION; do not ask the owner to define the entire behavior or recommend excluding the capability to close the report.

Only a genuinely new indispensable material decision that those rules and the current mandate cannot resolve needs owner input. Present a concrete recommendation and its impact, ask only for that specific decision, and continue independent authorized gaps. Respect actual user decisions and exclusions. This precedence does not authorize remediation for standalone bare Check or an audit-only request.

## Compliance model

Every evaluated requirement receives one status:

- **COMPLIANT** — repository evidence satisfies the applicable PHDK requirement.
- **GAP** — applicable requirement is not satisfied.
- **PARTIAL** — some required behavior/evidence exists but is incomplete.
- **NOT APPLICABLE** — requirement does not apply, with reason.
- **UNKNOWN / DECISION NEEDED** — applicability or intended behavior cannot be established from current evidence.
- **UNVERIFIED** — the requirement may be implemented but the permitted audit channels cannot establish compliance.
- **DEFERRED — OWNER OPT-IN** — acceptance execution/Prep/UAT Fix is outside the current Auto scope; record `UAT NOT RUN`, never COMPLIANT, GAP, BLOCKED or a new execution task solely for that absence.

Never mark COMPLIANT from filenames alone when the standard requires behavior. Inspect the relevant source/configuration/test evidence.

## Gap severity and remediation type

For each GAP/PARTIAL item, assign:

- **Critical** — security, authorization, privacy, destructive-data, or release-integrity violation with material impact.
- **High** — required product behavior, data integrity, authentication, architecture boundary, or mandatory delivery control is materially missing.
- **Medium** — important maintainability, observability, testing, accessibility, i18n, or standards requirement is incomplete.
- **Low** — documentation, consistency, naming, or low-risk hygiene gap.

Also classify the remediation:

- **AUTO-FIXABLE** — the required outcome is established by the authorized scope and current standards, including routine definitions the assistant can resolve under the FORCE rule above.
- **FIXABLE WITH VALIDATION** — implementable, but requires tests/checks to prove the result.
- **DECISION REQUIRED** — fixing it requires a genuinely new material product, architecture, security, data, paid-service or infrastructure decision outside what the current intent/rules/mandate resolve; missing routine implementation detail alone does not establish this category.
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
Summarize important COMPLIANT and NOT APPLICABLE findings so the report is auditable and not merely a to-do list. Show deferred acceptance separately; a non-UAT conformance conclusion does not claim runtime acceptance.

### Decisions and external blockers
List UNKNOWN / DECISION NEEDED, UNVERIFIED, and EXTERNAL / MANUAL items separately. Do not hide them inside the fixable backlog.

### Proposed execution order
Order fixable gaps by dependency and risk. Combine duplicate root causes instead of proposing repeated edits.

## Audit procedure

1. Pin the repository revision being audited.
2. Read the Capture requirements package and current Plan architecture artifacts first when present (`PROJECT_INTENT.md`, `PROJECT_BRIEF.md`, `PRD.md`, `FEATURES.md`, `REQUIREMENTS_TRACEABILITY.md`) so standards applicability is grounded in what the product is meant to be. If those artifacts are missing/incoherent, record a requirements-baseline gap and recommend `PHDK capture` for standalone Check; inside Auto, reopen/repair the upstream baseline and continue authorized execution. Do not fabricate applicability from code alone.
3. Identify the active PHDK version/manifest and current governing instructions.
4. Check canonical PHDK version when accessible; record drift without mutating the repository.
5. Read all applicable active standards; build an internal requirement matrix.
6. Inspect repository source, configuration, scripts, tests, docs, versioning, hooks, and delivery metadata needed to evaluate each requirement.
7. For every applicable app-style repository, inspect `DEBUG_DIAGNOSTICS_STANDARD.md` and the concrete mounted component/handlers/tests, not just a version string. Verify the canonical compact inline row (`vX.Y.Z` only → clipboard → trash) with no visible SHA/date/parentheses, 12px version label, two 28×28px visible icon buttons, 14×14px icons and 4px gap (no wrapping/truncation or oversized tiles), always-visible anonymous and debug-OFF presentation across public home, login, app and admin; safe sanitized copy with privileged diagnostics protected, green success checkmark and timed revert for both actions, cache safety, and absence of extra visible text/toasts. Record each missing or unverified requirement as GAP/PARTIAL/UNVERIFIED, with source/test evidence; NOT APPLICABLE only for non-app projects with rationale.
8. For AI-bearing repositories, evaluate `AI_ADMIN_STANDARD.md`: centralized provider access, token/cost tracking, super-admin consumption, Prompts navigation/route, prompt list/editor fields, output-schema validation, audit/revisions, and prompt/revision attribution.
9. Distinguish implementation absence from verification absence.
10. Deduplicate findings by root cause.
11. Produce the report and a concise prioritized summary.
12. For standalone bare Check, ask exactly one execution question: **"¿Quieres que ejecute los gaps AUTO-FIXABLE y FIXABLE WITH VALIDATION de este reporte?"** An explicit `--fix` / `fix` skips this question. Inside Auto, enumerate and execute only the already-authorized in-scope gap IDs; record out-of-scope findings separately without activating them or requesting generic approval for the whole mixed report. Ask only for a genuinely necessary unresolved material decision after independent permitted work.
13. Stop for standalone bare Check; for the explicit same-command fix variant or authorized in-scope Auto findings, continue directly with the enumerated fixable remediation under the limits above. Apply the FORCE missing-definition rule before preserving an initial DECISION REQUIRED label; do not auto-decide a genuinely unresolved material decision.

Do not manufacture exhaustive certainty when access is incomplete. Prefer UNKNOWN/UNVERIFIED over speculation.

## Remediation after yes

After explicit approval in the same conversation, an explicit fix variant, or for enumerated gaps already within the authorized Auto goal:

1. Freeze the approved gap IDs and report revision so scope is clear.
2. If PHDK itself is stale and that gap is approved, run the standards synchronization first, then regenerate the gap report before product remediation. Explain any new/removed gaps caused by the standards update; do not silently expand to newly discovered material decisions.
3. Build one coherent remediation plan from the approved AUTO-FIXABLE / FIXABLE WITH VALIDATION items.
4. Follow project intent. Closing a PHDK gap must not create features that conflict with the product's intent or non-goals.
5. Implement autonomously without asking for approval per file or gap.
6. Run applicable permitted non-UAT checks. User-facing changes, approved remediation and `check --fix` do not themselves authorize UAT Prep/UAT/Fix; retain affected acceptance criteria and offer a separate explicit `PHDK uat` after delivery. If remediation touches multiple PMO workstreams/shared surfaces, update PMO integration evidence rather than creating an untracked parallel portfolio. Use `PHDK auto` cadence for the remediation batch only when the approved gap set forms a development goal; the `yes` itself is enough authorization for the listed fixes.
7. Preserve actual hooks, protections, required reviews, access controls, and execution boundaries.
8. Version, commit, push, PR, and merge under `MAIN_DELIVERY_STANDARD.md` when the approved remediation request targets repository delivery.
9. Rerun `PHDK check` against the resulting candidate/main.
10. Update `PHDK_CHECK_REPORT.md` with resolved gap IDs, residual gaps, evidence, and final alignment status.

Do not fix genuine DECISION REQUIRED or EXTERNAL / MANUAL items merely because they appeared in the same report. In FORCE, first resolve routine missing definitions under the rule above; for a remaining indispensable decision, present the concrete recommendation and impact rather than a blank request to define behavior, after continuing independent work.

## Stack review evidence

Consume and revalidate the [Stack Security Review](PHDK_SECURE.md#stack-security-review) from Upgrade, Preflight adoption, Plan or Secure. Check its repository/input hashes, deployment identifiers, advisory/support dates and scope; refresh affected stale evidence, not every unchanged component. Reuse STANDARDS_SYNC, STACK_REVIEW_COVERAGE and STACK_SECURITY_STATUS and classify findings with this Check report's existing severities/remediation categories. A sync success or zero package advisories cannot prove runtime/image/data-engine security. Record missing access and deployed-version evidence as UNVERIFIED. Bare Check remains audit-only; Check Fix and existing current remediation authorization keep their stated write/delivery limits.

## Relationship to other commands

- **`PHDK PMO`** coordinates owner-confirmed workstreams and integrated delivery; Check is not a workstream detector or PMO replacement.
- **`PHDK check`** audits standards compliance and asks before remediation.
- **`PHDK plan`** defines/reconstructs target architecture and implementation planning; Check verifies whether the resulting repository conforms to applicable standards and recorded architecture.
- **`PHDK auto`** runs the authorized development/delivery lifecycle and includes final non-UAT Check plus automatic remediation of in-scope AUTO-FIXABLE / FIXABLE WITH VALIDATION findings. It excludes Prep/UAT/Fix.
- **`PHDK uat`** validates intent-aligned user acceptance behavior; it can provide evidence for check findings but does not replace the broader standards audit.
- **`PHDK unlock`** reconciles PHDK-related blockers; it is not a general compliance audit.
- **`PHDK upgrade`** synchronizes PHDK standards and performs the bounded read-only Stack Security Review; it does not by itself remediate the repository or patch product vulnerabilities.
- **Developer Mode** remains a narrow direct-main mode for eligible small changes and does not bypass the check audit/approval split.

## Lifecycle handoff

At Check completion, create `docs/phdk/lifecycle/<run-id>/70-check/HANDOFF.md` and snapshot `PHDK_CHECK_REPORT.md`. Record the exact report revision, overall conclusion, and gap IDs/types.

When Check remediation executes, create/update:

```text
PHDK_REMEDIATION_REPORT.md
```

with each gap ID, repair, changed components, validation, final status, and residual decision/external gaps. After rerunning Check, create `docs/phdk/lifecycle/<run-id>/80-remediation/HANDOFF.md` and snapshot both remediation and updated Check reports.

Delivery must verify the latest Check/remediation handoff and identify any accepted residual limitation before publication.

## Completion semantics

The audit phase is complete only when the report exists (when persistence was requested or expected by the repository workflow) and the prioritized gap list is presented. Standalone bare Check then asks whether to execute fixable gaps. An explicit `check --fix` / `check fix` or an authorized Auto goal already supplies in-scope remediation approval: record the enumerated gap IDs and continue without asking again.

The remediation phase is complete only after approved fixable gaps are implemented, verified, delivered to the requested target, and the check is rerun. Report residual DECISION REQUIRED, EXTERNAL / MANUAL, UNKNOWN, or UNVERIFIED items explicitly. Never call the repository fully aligned while unresolved applicable development gaps remain. State the scope of any non-UAT ALIGNED conclusion and report `UAT NOT RUN` separately; deferred acceptance does not block development completion or imply runtime verification.


## Functional debug widget evidence gate

For applicable interactive apps, explicitly read `DEBUG_WIDGET_READINESS.md` and inspect the actual implementation. Require top-left placement directly below app name; only version with no parenthesized SHA/date; compact pair of actions. Insist on **verified clipboard text**, event/history/error collection, and **verified cache/session/cookie clearing** through origin-scoped adapters and app logout. A green check animation with no awaited successful operation MUST be a HIGH severity GAP. A static report with no captured events, or a trash button that only changes state/reloads, is a GAP. No behavioral PASS without evidence from explicitly authorized deployed acceptance exercising the handlers and observing real adapter calls/effects. Link source paths, test source/results and unsupported capabilities in Check. In Auto, perform source/static checks, report runtime evidence `DEFERRED — OWNER OPT-IN` and `UAT NOT RUN`, and continue development delivery; never execute acceptance to satisfy this Check item. Within an explicitly initiated acceptance run, missing evidence is UNVERIFIED, not PASS.


## Hook compatibility (v2.61.0)

Apply the [hook decision procedure](PHDK_HOOK_COMPATIBILITY.md#decision-procedure) before executing an ambiguous build/packaging/hook command, declaring its conflict BLOCKED, or asking the owner. Inspect the command chain and provenance, automatically repair only proven PHDK-owned incompatibilities within authorized remediation, and preserve independent security/version/branch/commit gates. Owner-owned, external and unknown controls retain their authorization boundary; prepare a concrete proposal for any unresolved gate. Never request a prohibited local-runtime exception, execute excluded tests, use --no-verify or start UAT to satisfy a hook. Bare `PHDK check` remains audit-only: report the classification and proposed correction; only `check --fix`, approved remediation or an active authorized implementation goal permits repairs.
