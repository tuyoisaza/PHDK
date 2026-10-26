# PHDK Secure Standard

## Contract
`PHDK secure` is an explicit standalone security audit-and-authorized-remediation command. In `PHDK auto` and `PHDK auto force`, Secure is mandatory **development work**, not UAT or UAT Prep. Hybrid operation means lightweight security checks at each completed value milestone and a consolidated security gate after integration and before final Check/delivery. Security findings may require reopening implementation. Never interpret Secure as permission for UAT, penetration testing, paid scanning, external provider mutations, local behavioral tests, Docker, new environments or bypassing controls.

## Milestone checks
For each completed value milestone inspect changed source/configuration and relevant threat boundaries: secrets, dependencies, authentication/session management, server-side authorization and least privilege, tenant isolation across data/storage/jobs/exports/AI, encryption and TLS configuration, input validation and injection, SSRF/XSS/CSRF, rate limiting, logging/PII, backup exposure, supply chain and GitHub/Railway configuration. Run permitted static checks only, preserve existing independent security gates, and document applicability and evidence. Do not claim behavioral assurance from source inspection.

## Consolidated gate
After integration, assess OWASP Top 10 and relevant ASVS controls using a risk-based threat model; reconcile with `PHDK_TENANT_RISK_STANDARD.md`, `PHDK_PRODUCTION_VERIFICATION.md`, current owner decisions and actual hosting architecture. Record each finding with severity, affected asset/tenant boundary, reproducible static evidence, remediation, verification status and residual risk. Fix authorized source/config defects, repeat permitted static checks, and document unverified runtime controls for later explicitly authorized UAT. No fabricated passing tests or acceptance evidence.

## Release decisions
Critical/High confirmed security vulnerabilities block Secure clearance and final delivery until fixed or subject to an explicit, documented owner risk decision consistent with non-waivable host/security controls. An owner waiver cannot bypass technical enforcement or assert a vulnerability is resolved. Unknown/unverified is not PASS: classify its risk and report limits; absent UAT is not itself a Secure failure. Medium/Low findings require documented prioritization and ownership. Do not request routine approval in Auto Force; sensitive architecture, spending and risk acceptance still require owner authority.

## Outputs
At each milestone, record a concise security delta in the milestone handoff. For the consolidated gate, create `docs/phdk/lifecycle/<run-id>/68-secure/HANDOFF.md` and `SECURITY_REPORT.md` with scope, controls matrix, findings, remediation commits, static verification, residual risk, release decision and explicit `RUNTIME SECURITY VALIDATION NOT RUN` where applicable. Record stage in lifecycle status. Standalone Secure audits current state and fixes only within the owner's authorization; read-only invocation must not mutate code.

## Precedence and integration
Secure runs after implementation/integration, before final Check and delivery; it never enters stages 45/50/60. This standard supplements existing tenant, production-verification, Check, delivery, Auto and milestone rules. Existing owner/host controls take precedence. Load this file at a relevant security stage, stack-review trigger or milestone; reuse its compact evidence in later unchanged stages.

## Mandatory Node.js runtime and npm supply-chain profile

For a new Node.js project, Plan MUST prefer the newest security-patched **Active LTS** compatible with the framework, package manager, native addons, database drivers, build tooling and hosting platform. If no Active LTS exists or none is compatible, use the newest compatible, supported **Maintenance LTS** and record why, its support deadline and migration implications. This supported fallback is an ordinary technical choice, not unresolved risk requiring an extra approval. If no supported LTS is compatible at all, recommend the concrete stack changes needed and record `DECISION_REQUIRED` for a genuinely new material decision; never silently substitute Current or EOL. Do not select Current solely because its version number is higher, or silently select an EOL runtime. Verify official release/security notices and the support schedule at review time; never freeze a supposedly latest patch in PHDK.

For an existing supported major, use its current compatible security-patched release first. In a standalone review, report/recommend the patch. **In Auto/Force, implement a compatible same-major security patch as ordinary in-scope security maintenance without asking for a second command**, updating applicable repository-owned runtime declarations and build pins and reconciling compatible dependency/lockfile evidence. A security fix does not itself authorize a major migration. An EOL line requires a concrete supported migration target and compatibility assessment; material architecture/provider decisions and acceptance of unresolved security risk retain existing owner controls. Keep the declared constraint, exact resolved build version and observed deployed version distinct. Do not claim hosting compatibility or a running patch from a manifest alone.

All Node.js projects, including existing products, apply the Stack Security Review below during relevant milestones and the consolidated gate. Inspect reproducible install configuration such as `npm ci` or the lockfile-equivalent without executing installs as part of the review. Evaluate publisher MFA and provenance/trusted publishing where applicable without requesting account secrets. Prefer an evidence-backed dependency cooldown with documented exceptions for urgent security fixes. Do not blanket-disable legitimate native install scripts; review necessary script permissions and isolation. A compromised package or exposed credential requires incident classification and containment/rotation through separately authorized channels, never unapproved provider changes.

## Stack Security Review

This is the shared, bounded review contract for the actual project stack, including non-Node components. It reuses Secure and Check findings; it does not create another lifecycle mode or a background scanner.

### Triggers and reuse

- Every explicit `PHDK upgrade` and `PHDK upgrade force` MUST review the current project, **including a no-op standards synchronization** or a newer local version that cannot be downgraded. A blocked sync does not prevent independent permitted reads; report the sync conflict separately.
- Foreground Preflight MUST perform the review once when it actually adopts a new canonical PHDK version, including a first installation or pre-versioned installation. A version comparison, failed sync or same-version integrity repair alone does not trigger a repeated full review. Re-read adopted instructions before continuing.
- **Every new `PHDK auto` and `PHDK auto force` run MUST perform one fresh Stack Security Review during Preflight even when PHDK is already current.** This is the run's baseline security inventory; later milestones reuse it only while inputs and advisory freshness remain valid. Do not repeat the same full review at every unchanged stage.
- Plan performs or refreshes the applicable review when selecting the initial architecture. Refresh affected evidence on material changes to runtimes, manifests/locks, frameworks, native dependencies, builders/base images, deployment roles or database/cache/search engines. Secure milestones and the consolidated gate reuse the same evidence contract.
- Review all applicable workspace packages and service roles, including workers, within the identified project. A multi-project rollout requires the current owner's identified scope; no dormant-project scan, recurring job, webhook or post-conversation work follows from this rule.
- Within one command/run, reuse evidence only after checking its repository/input hashes, deployment identifiers, source retrieval dates and advisory/support freshness. An explicit later Upgrade still checks for new advisories even with unchanged files. New relevant advisories or changed evidence invalidate the affected result. Do not repeat the whole review at every unchanged Auto/PMO stage.

### Read scope and execution boundary

An explicit Upgrade/Force or a Preflight adoption trigger includes repository/source reads, current official advisory/support lookups and bounded reads of already connected provider metadata/logs for the identified project under [EXECUTION_SCOPE.md](EXECUTION_SCOPE.md#bounded-read-only-provider-diagnostics). Define finite targets, request/result bounds and log windows before retrieval. Existing owner restrictions and host access controls remain binding. Missing access becomes `UNVERIFIED`; do not ask for credentials, create an account or infer a runtime from a successful deployment.

A **standalone review trigger** (for example bare Upgrade/Force or adoption-only Preflight) does not itself authorize product edits, dependency installation, lifecycle scripts, lockfile regeneration, application builds/execution, local behavioral tests, Docker, UAT, live probes, provider/configuration writes, paid scanners, commits, pushes, merges or deployment. **Inside an explicitly invoked `PHDK auto` / `PHDK auto force`, the existing Auto development mandate does authorize compatible repository-owned security remediation discovered by this review:** supported same-major runtime security patches; compatible dependency security updates that do not require a material breaking migration; and aligned repo-owned runtime/build declarations, lockfiles and pins using the project's permitted dependency workflow. Perform permitted static/security verification and normal Auto version/delivery. Do not extend that authority to major runtime migrations, material breaking dependency migrations, new infrastructure, provider administration/writes, spending, secrets/account operations or explicit owner exclusions. Preserve actual controls.

### Inventory and evidence

For each applicable component, retain separate evidence fields:

| Field | Required evidence |
|---|---|
| Declared | Manifest/engine/package-manager range, runtime file, image tag or deployment configuration and source path. |
| Resolved | Exact lockfile/package/image version and integrity/provenance where available; identify direct versus transitive dependencies. |
| Build | Builder/runtime/base-OS image and digest, build timestamp and deployment/artifact identifier. Mark build-only tooling explicitly. |
| Deployed | Actually observed runtime/engine version, service, environment, deployed source SHA/image and observation source/time. Missing exact evidence remains `UNKNOWN` or `UNVERIFIED`. |

Record review date, repository SHA, relevant input hashes, service/environment, deployment/image identifier, evidence references and bounded coverage. Inspect workspace manifests and all relevant lockfiles; `packageManager`, `engines`, runtime-version files, Dockerfiles and builder/deployment configuration; frameworks, ORMs/drivers and native addons; operating-system images and database/cache/search engines. Never read secret values or customer data to build this inventory.

A range, floating major tag, `@types/node`, build log or successful deployment is not proof of the running Node patch. A package-manager audit with no findings does not cover Node itself, OS images or data engines. Source/main and deployed commits may differ; assess them separately and identify unreviewed deployed dependencies instead of presenting a source lockfile as live evidence.

### Current security and compatibility baseline

Use primary vendor security/release notices, official support/EOL schedules and applicable package advisories. Record advisory IDs, affected ranges, fixed versions **per supported major**, publication/retrieval dates, exploit prerequisites and compatibility requirements. Evaluate each actual major against its own dated floor; a numerically higher EOL major is not a substitute. Verify official current sources at review time rather than relying on the previous report or model memory.

Distinguish version applicability from verified application exploitability. An affected version warrants a finding; unknown reachability is not proof of safety. A workaround must match the resolved component and be evaluated only for the advisory it mitigates. Keep unaffected packages distinct from similarly named vulnerable transports or plugins.

Review direct/transitive runtime and build dependencies, lockfile consistency/integrity, registry/source origins, known advisories, suspicious release/maintainer changes, install-script exceptions, native binaries and framework/driver/runtime compatibility. Use already available safe static tools and existing vendor evidence; do not install scanners or execute dependency code. Record incomplete coverage rather than inventing a complete supply-chain clearance.

### Results, recording and remediation

Report these independent outcomes in the existing Upgrade, Preflight, Check or security report:

- **STANDARDS_SYNC:** `VERIFIED`, `CURRENT`, `SKIPPED_NEWER_LOCAL`, `BLOCKED` or `NOT_APPLICABLE`, with version, upstream SHA, manifest/native-block evidence and conflicts. A helper's manifest-only success is not proof of native-block verification.
- **STACK_REVIEW_COVERAGE:** `COMPLETE`, `PARTIAL`, `PENDING` or `NOT_APPLICABLE`, with enumerated components, environments, advisory sources and missing evidence. COMPLETE describes the stated review scope, never universal security assurance.
- **STACK_SECURITY_STATUS:** `NO_KNOWN_FINDINGS_IN_REVIEWED_SCOPE`, `GAPS_FOUND`, `UNVERIFIED` or `NOT_APPLICABLE`. Use GAPS_FOUND when findings exist, retaining any additional unknowns. An incomplete or pending review cannot receive a clean status; a source-only assessment can have COMPLETE source coverage while deployed runtime remains UNVERIFIED.

A verified standards sync may coexist with stack gaps or incomplete evidence. Findings MUST NOT prevent delivery of safer standards or be reported as repaired by vendoring. This separation does not waive Secure's application-release clearance rule for confirmed Critical/High vulnerabilities. A standards-only delivery is not application security clearance, even if an existing connection rebuilds the unchanged application.

Use existing Check severity/remediation categories. Each finding identifies component/service scope, evidence, affected/fixed range, recommended compatible change, verification limits and owner/action. Reuse `SECURITY_REPORT.md`, `PHDK_CHECK_REPORT.md` or `PHDK_PREFLIGHT_REPORT.md` when that report belongs to the current task; otherwise include the structured review in the Upgrade report. An authorized rollout may retain a scoped report under `docs/phdk/`. Such evidence files are project documentation, not new PHDK-owned force-replacement surfaces.

Continue already-authorized remediation without duplicate consent. Otherwise present the concrete patch/migration action within the current review/sync scope. Do not silently change a major version, provider or live service, accept residual risk, activate Auto or initiate UAT. Missing optional UAT remains `DEFERRED — OWNER OPT-IN`, not a stack defect. A sync helper reporting PENDING/UNVERIFIED means the assistant still owes the review; never relabel that helper output as a completed audit.
