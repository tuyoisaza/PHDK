## v2.74.0 — 2026-10-28

### Official portfolio-first ethos, reuse and cloud-first execution
- Establish PHDK as an opinionated owner-governed system for related projects, focused on compounding shared knowledge/modules, intent-to-verified-value, accountable autonomy and progressive context. Keep existing policy sources instead of adding a competing methodology.
- Make REUSE/ADAPT/BUILD assessment the default for plausibly shared capabilities, preserving fitness, security, license, portability, independent versioning and separate authorization for public/private donor contributions. Starter catalog remains `SPECIFICATION_ONLY`.
- Clarify that the defined but evolvable stack and existing GitHub-connected production (Railway where configured) minimize per-project local infrastructure. Local static review, lint/typechecks, compilation and safe builds remain allowed; Docker, running services/databases and local behavioral tests remain prohibited. Deployed UAT stays explicit-only.
- Align README, Evolution, reuse catalog, Plan, technical stack, starter, hosted verification, Check, progressive context, AGENTS, SKILL, native rules, INANUTSHELL and coherence guard. Remove stale in-process tests, PMO-only delegation and automatic UAT wording from INANUTSHELL.
- This standards release does not implement reusable packages, update downstream projects, change hosting, run local behavioral tests or perform production UAT. Those outcomes remain independently unverified.

## v2.73.0 — 2026-10-28

### Versioned project documentation, hierarchy and traceability
- Introduce vendored `PHDK_DOCUMENTATION_STANDARD.md`: stable `docs/intents/`, `docs/briefs/`, `docs/decisions/`, `docs/plans/`, `docs/images/`, `docs/evidence/` with versioned document baselines and design asset folders. Root `TASK.md` remains authoritative for the current goal; no duplicate task/status system.
- Define `kebab-case.vN.md` names, stable IDs, date/provenance metadata, draft/active/superseded history, permanent ADR supersession, and a generated active-document locator `docs/INDEX.md`. Document versions are independent from PHDK/product SemVer; an active revision does not imply owner approval.
- Add vendored standard-library `scripts/phdk_docs_audit.py` for read-only path, metadata, duplicate-active and index drift detection, with explicit write-only `--sync-index` for authorized changes, plus source regression scenarios. Newly changed unversioned documents are reported while untouched brownfield content is preserved as LEGACY_COMPATIBLE.
- Integrate Capture, Plan, Design/Designer, PMO, Auto/continuity, Check, lifecycle handoffs, intent/task tracking, UAT baseline resolution, agent/native/skill entrypoints, upgrade, main delivery, and coherence routing. No bulk renames, new background automation, local runtime tests, Docker, or automatic UAT.
- Documentation/source consistency and release metadata reviewed; tests and actual downstream deployment/adoption remain independently unverified unless separately evidenced.

## v2.72.0 — 2026-10-27

### Cheap and truthful production revision identification
- Introduce the vendored `PHDK_DEPLOYMENT_VERSION_STANDARD.md`: deployed HTTP products expose public, uncached JSON `GET /health/version` with application version, installed PHDK version, exact built Git SHA and immutable build time. Missing provenance is explicitly UNVERIFIED; the compact UI version widget does not change.
- Permit one tightly scoped, non-UAT, read-only `curl` after an authorized merge/autodeploy or a requested version check; compare the served artifact's revision to the expected release. A successful response proves the answering revision, not all replicas, full application health, acceptance, or Railway deployment success.
- Reconcile source/versioning, production-verification, security boundary, delivery/Auto/Check, diagnostics, managed entrypoints, coherence and manifest rules. No browser, UAT, local behavioral test, new GitHub Action, external provider administration, or downstream project deployment was performed.

## v2.71.1 — 2026-10-27

### Complete forced upgrade publication and workspace closeout
- Publish a changed PHDK upgrade force standards sync as its first scoped value milestone through branch push, PR, permitted merge and independent remote-main manifest/native verification before Auto Force creates more worktrees; an already-published no-op needs no duplicate PR, but local CURRENT does not prove remote publication.
- Fast-forward clean local main and safely retire only the verified integrated owned branch/worktree before new same-goal work. Keep v2.71.0 historical/continuous hygiene, genuine controls and dirty/unmerged data protection; no feature-to-main direct push or redundant post-merge main push.
- Add read-only remote-main manifest gate, explicit copier --force-owned control and honest unpublished-state output, regression test source and vendoring manifest coverage. Reconcile active Upgrade, Auto, agent/skill/native entrypoints, README, VERSION and changelog.
- No local runtime tests, Docker, GitHub Actions, provider administration, unverified branch deletion or downstream automatic upgrades were executed.

## v2.71.0 — 2026-10-27

### One-time historical and continuous safe Git hygiene
- Extend post-merge PHDK Git workspace closeout with a **bounded historical inventory** on the first explicitly authorized local Auto/Auto Force run after adopting this version. Do not run destructive cleanup from bare Upgrade, passive Preflight, Check, unattended jobs or remote-only sessions.
- Add a vendored, standard-library helper that requires recent merged-PR evidence, checks target ancestry, exact local/remote branch head SHA, open PR count, age for historical records, protected names and tracked/untracked/ignored worktree safety before any branch/worktree retirement. Record detailed retained reasons and local audit state without a new source version bump.
- After each verified milestone merge, coordinate local main fast-forward and verified local branch/worktree retirement with SHA-lease-guarded **deletion-only** remote feature branch cleanup, without rewriting history or changing GitHub/Railway settings. Existing autodelete and inaccessible remotes are reported independently.
- Reconcile Auto, Preflight, PMO, Check, handoffs, versioning, native/agent/skill instructions and vendoring manifest. Add source-only regression scenarios. Local behavioral test runs, user-PC cleanup, provider changes and deployed UAT were not performed in this release.

## v2.70.0 — 2026-10-27

### Verified Git workspace closeout after milestone merge
- Add PHDK_GIT_WORKSPACE_CLOSEOUT.md and a stdlib helper for local origin/main fetch, fast-forward-only main sync, SHA reconciliation, and scoped safe cleanup of independently verified merged milestone branches/worktrees.
- Require Auto/Auto Force and PMO coordinators to run post-merge local closeout at each authorized published value milestone before starting new local work; preserve dirty, locked, active, unmatched and unmerged state and report exact blockers rather than forcing deletion.
- Reconcile entrypoints, delivery/versioning, README and the distribution manifest. Keep remote merge, local sync, remote feature-branch cleanup, Railway deployment and UAT as distinct evidence states; no redundant post-PR main push, server/provider setting changes, background jobs or local product tests.
- Add regression test source for safe branch retirement, SHA mismatch and ignored-data protection. Syntax/static review permitted; runtime/regression execution and deployed UAT not claimed.

## v2.69.0 — 2026-10-27

### Visible milestones and optional reusable-capability catalog
- Tighten milestone contracts around a complete user capability/journey, explicit scope/dependencies, acceptance criteria, honest working/simulated/not-run evidence, delivery target/authorization and next milestone.
- Resolve the agile-slice ambiguity: internal slices do not trigger publication, while a completed coherent authorized milestone is verified/versioned/published before later milestones instead of being held until the whole product is finished.
- Require delivery reporting to distinguish IMPLEMENTED, PUBLISHED, DEPLOYED and ACCEPTED; mocks, shells, fixtures and unexecuted checks cannot be promoted to functional evidence.
- Add optional Plan-time REUSE / ADAPT / BUILD assessment. Only ACCEPTED_VERSIONED catalog entries are eligible for direct reuse; candidate/reviewed implementations require current-project revalidation and specification-only entries have no implementation.
- Add a public reusable-capability catalog contract, JSON schema, standard-library validator and policy scenarios. Accepted reusable packages require explicit license/security/maintenance evidence, observed passing tests and portability in a second independent consumer.
- Define a specification-only starter composition for administration/organizations/multitenancy/roles, synthetic UAT tooling, AI prompt administration, light/dark/corporate themes and internationalization/language selection. Synthetic identities retain explicit UAT opt-in and real authentication/authorization controls.

### Catalog review corrections
- Reject accepted status based on flags alone: require version-linked test, security and license evidence plus evidence for each distinct consumer. Document the license/permission basis and redistribution rights without restricting acceptance to SPDX licenses.
- Align schema/checker required fields, types, unknown-field rejection and assigned version/owner gates; missing implementation is not null. Keep cross-record version and identity checks explicit and clarify that metadata validation is not semantic proof.
- Add shared synthetic negative fixtures for the stdlib checker and optional JSON Schema parity checks. Keep all five canonical starter entries specification-only with empty evidence; do not claim checks ran when execution is unavailable.

### Publication, privacy and verification limits
- Keep PHDK as methodology/contracts/catalog; reusable implementations belong in separately versioned packages. The canonical public catalog uses generic contracts and synthetic starter examples.
- This release does not publish private donor source, inventory or evidence, and does not modify donor projects or consumers automatically.
- Add static test scenarios for optional module selection, rejection of unvalidated accepted status, milestone/slice separation and truthful delivery evidence. Local repository test execution, UAT, deployment and provider operations are not implied by the standards change and must be reported separately when not run.

## v2.68.0 — 2026-10-25

### One-command forced upgrade and Auto Force
- Redefine exact `PHDK upgrade force` as a composite foreground command: complete forced PHDK synchronization, Stack Security Review, eligible central-status publication and verification, then transition immediately into `PHDK auto force` without asking the owner for a second command.
- Continue an already identified authorized development goal when present. When none exists, use a bounded repository-maintenance goal: reconcile current code/configuration with current PHDK and recorded product intent, remediate compatible in-repository security/standards gaps, complete applicable Check/remediation and normal delivery, and do not invent new product features.
- Reuse the upgrade phase's fresh stack-review evidence as the Auto baseline when inputs and advisory freshness are unchanged. Do not duplicate the same review immediately.
- Preserve Auto Force boundaries: no automatic UAT, no major/material migration decision, no provider/new-infrastructure write, spending, secret/account operation or bypass of actual controls.

### Verification and adoption
- Reconcile Upgrade, Auto, native managed rules, AGENTS, SKILL and README so the chained transition is visible from active entrypoints.
- Bare `PHDK upgrade` remains sync/review-only. Publishing this release does not start Auto in dormant repositories; the composite behavior activates only when the owner explicitly invokes `PHDK upgrade force`.

## v2.67.0 — 2026-10-25

### Auto owns compatible stack security maintenance
- Make every new `PHDK auto` and `PHDK auto force` run perform one fresh Stack Security Review during Preflight, even when canonical PHDK is already current. Reuse the resulting evidence at unchanged later stages instead of requiring a separate Upgrade command.
- Treat compatible repository-owned security maintenance discovered by Auto as part of the existing development mandate: supported same-major runtime security patches such as Node.js patch releases, compatible dependency security fixes, and aligned repo-owned runtime/build declarations, lockfiles and pins.
- Revalidate affected static/security evidence and continue normal Auto versioning and delivery without asking the owner for a second security-remediation command.
- Preserve boundaries for major runtime migrations, material breaking dependency migrations, provider administration/new infrastructure, spending, secrets/account operations, UAT and explicit owner exclusions. Standalone Upgrade remains read-only with respect to product remediation unless separately authorized.

### Verification and adoption
- Reconcile Auto, Preflight, Secure, native managed rules, AGENTS, SKILL and README so the same behavior is visible from all active entrypoints.
- Publishing this release does not retroactively execute Auto in dormant repositories. Downstream repositories adopt the behavior when they next synchronize PHDK or run a clean Preflight that adopts this version.

## v2.66.0 — 2026-10-25

### Central downstream repository status registry
- Add `PHDK_REPOSITORY_STATUS.md` as a vendored contract for eligible PHDK repositories under `tuyoisaza/*`. During foreground PHDK work, repositories that already have canonical-PHDK write access publish or refresh `docs/repos/<repo>/status.md`.
- Record installed versus canonical PHDK version, observed repository SHA, evidence-backed tech-stack versions and an independent Stack Security Review status so maintainers can identify both standards drift and security/version drift without conflating them.
- Route Upgrade/Force, Preflight adoption and native managed instructions through the registry. Missing canonical write access is non-blocking and never triggers a credential request.
- Keep the registry explicitly foreground-only: no telemetry, repository crawler, scheduler, GitHub Action, webhook, background retry or autonomous cross-repository maintenance is introduced.

### Verification and adoption
- Add the registry standard to the vendoring manifest and document the canonical `docs/repos/<repository-name>/status.md` location.
- Publishing this PHDK release does not populate every downstream status record. Each eligible repository reports itself when a foreground PHDK session runs with sufficient evidence and existing access.

## v2.65.3 — 2026-10-23

### Publish the optional Company Co document importer corpus
- Publish the existing fictional 2025 quality-management dossier as 35 logical documents covering 17 processes, with individual PDF and Word files, consolidated alternatives, completed records and blank forms.
- Include an obsolete revision, an image-only PDF for OCR, ten documented extraction cases, machine-readable expectations and integrity metadata. Preserve the canonical Company Co people, departments and commercial baseline.
- Add an English corpus index and discoverable links from README and the Company Co reference. Keep the business documents in Spanish and the optional corpus outside the standards vendoring manifest.
- Treat the ISO 9001:2015 / Amendment 1:2024 reference as historical simulation, with no actual certification claim or new execution policy, command, provisioning or automatic UAT behavior.

### Verification limits
- Review the corpus inventory, document hashes, internal references, rendered pages and publication diff. Run the existing static PHDK coherence check and verify release metadata and remote publication separately.
- The importer itself and runtime UAT were not executed. This documentation publication does not upgrade downstream projects or deploy an application.

## v2.65.2 — 2026-10-23

### Resolve build and hook ambiguity before asking
- Add an ordered decision procedure to the existing hook standard and route native managed instructions, agent/skill entrypoints, Auto, verification and delivery through it before execution, BLOCKED or a user question.
- Distinguish permitted compiler/static tooling from import/require load checks of compiled application/API modules, including checks with networking/listeners disabled. Classify mixed command chains and provenance before choosing a correction.
- Repair only authorized proven PHDK-managed local invocations, retain runtime source and disclose NOT RUN coverage. Preserve independent owner/external/unknown controls and their required ordering; prepare concrete unresolved decisions without local-runtime exception prompts or duplicate approvals.
- Reconcile older local-suite instructions in enforcement and verification with production-first policy. No automatic UAT, new CI, provider change or infrastructure route is introduced.
- Add bounded static guards for on-demand routing, the installed managed block, manifest dependencies and six decision scenarios. Keep VERSION, README and CHANGELOG synchronized. Integrate on v2.65.1 while preserving Stack Security Review and canonical/vendored static-check compatibility.

### Verification limits
- Static source checks and independent review are recorded in the release checkpoint. The scenarios document expected decisions; no local behavioral tests, downstream agent execution, UAT or project upgrade is claimed.

## v2.65.1 — 2026-10-23

### Preserve downstream static-hook compatibility
- Format the six manifest-owned Python helpers with Ruff 0.7.0 and split the updater's grouped import into identical-order individual imports. This is a mechanical source correction: command contracts, review obligations, permissions and runtime behavior are unchanged.
- Preserve the README hard line break using Markdown backslash syntax, remove one redundant EOF newline from each of the design guide and the oldest changelog archive, and retain the historical text.
- Keep the 78 source/destination manifest mappings and exact-copy distribution contract unchanged. Existing downstream Ruff and source-hygiene checks remain enabled; no hook, configuration or vendored exception is introduced.

### Static verification and limits
- Formatting preserves the exact AST for all six helpers. The subsequent updater import split is the only structural AST difference; import order and the rest of its AST are identical. Static compilation with normalized source positions produces equivalent code for all six helpers; no helper behavior or application tests are executed for this comparison.
- Record pinned Ruff/source-hygiene, canonical and installed-layout coherence, manifest, version and outgoing-source checks in `PHDK_COHERENCE_REPORT.md`. Source publication and downstream adoption require separate verification.

## v2.65.0 — 2026-10-23

### Stack security review on upgrade
- Require a bounded read-only Stack Security Review for every explicit Upgrade/Force, including no-op synchronization, and once when foreground Preflight actually adopts a new canonical version.
- Reuse Secure as the canonical evidence contract for all workspace/service roles: distinguish declared, resolved, build and observed deployed versions; review current official advisories, support/EOL, dependency/native compatibility, images and data engines.
- Report standards synchronization, review coverage and security findings independently. A successful vendor update cannot clear product vulnerabilities; findings do not prevent safer standards from being delivered.
- Replace the stale Node 20 minimum with supported, security-patched LTS selection. Prefer compatible Active LTS for new projects, allow a documented supported Maintenance LTS fallback, and recommend patches within existing supported majors before migration.
- Route Upgrade, Preflight, Plan, Check, execution/delivery and native agent entrypoints coherently. The foreground updater exposes pending review obligations without pretending to execute a security scan. Static coherence checks understand canonical and vendored manifest destinations.
- Reconcile touched legacy local-test instructions with production-first verification. Preserve owner customizations, actual controls, explicit-only UAT and separately authorized remediation/delivery.

### Verification and adoption
- Source/diff, Python syntax, manifest/native-block and static coherence verification are required; no local behavioral tests, Docker, UAT, new scanners, hosted workflow dispatch or provider mutations are introduced.
- This release does not claim every project is updated or its application dependencies patched. Downstream adoption and security evidence must be verified per repository.
- v2.64.0 was already proposed by the independent encryption/KMS PR when this release was prepared; its unmerged changes are not included.

## v2.63.2 — 2026-10-23

### Reconcile phase limits with current owner authorization
- Require Plan to load and record the verified applicable PHDK baseline before deriving briefs, plans and tasks; distinguish adopted and verified canonical versions.
- Classify restrictions by lifetime and provenance in the existing task record. Retain source, known date, scope, closure condition and superseding instruction; never attribute assistant-created restrictions to the owner or treat phase completion as a permission grant.
- Reconcile TASK, plan, STATUS, Auto mandate and affected worker context before construction-to-publication transitions. Keep owner authorization, technical permission, costs and explicit-only UAT separate; do not duplicate an approval already granted or claim that a document edit clears an executor denial.
- Align delivery, execution, planning, delegation and agent entrypoints; add bounded static coherence guards without changing executor permissions or introducing a new runtime authority mechanism.
- Preserve the concurrently published v2.63.1 manifest repair and release history. Normalize escaped newlines at the touched agent/native entrypoint boundaries without changing policy.

### Verification limits
- Static/source verification is recorded in the delivery checkpoint; no local behavioral tests, Docker, UAT, provider operations or downstream project changes are part of this correction. Publishing PHDK does not resolve DEBATE's executor permission or prove its deployment.

## v2.63.1 — 2026-10-23

### Repair canonical manifest vendoring
- Remove literal escaped newline delimiters from the PHDK_SECURE.md manifest mapping so all sources resolve inside the canonical repository and downstream upgrades can validate the distribution.
- Normalize the escaped line breaks in the previous release note; align VERSION and the README release marker.
- Static distribution repair only. No downstream product implementation, UAT, provider operations, or policy changes are authorized by this patch.

## v2.63.0 — 2026-10-22

### Hybrid PHDK Secure
- Add standalone `PHDK secure` and milestone security deltas plus consolidated pre-Check security gate in Auto/Force.
- Add `PHDK_SECURE.md` to the vendoring manifest; align Plan, lifecycle, Check, native agent entrypoints and README. Require patched Active LTS Node.js compatibility and npm supply-chain checks for Node.js projects. Preserve explicit-only UAT and production-first static verification.
- This standards release does not assert downstream adoption, runtime security validation or application deployment.

## v2.62.1 — 2026-10-22

### Reconcile explicit-only UAT throughout active guidance
- Replace obsolete automatic UAT transitions in acceptance, Auto/Force, lifecycle, PMO, milestone delivery, Check/remediation, SEO/AEO and completion guidance. Auto keeps stages 45/50/60 `DEFERRED — OWNER OPT-IN` and reports development/delivery separately from `UAT NOT RUN`; absent acceptance artifacts and historical UAT failures do not reopen completed development.
- Preserve the existing command boundaries: fresh explicit `PHDK uat` includes necessary Prep; standalone `PHDK uat prep` prepares only; UAT Fix requires explicit invocation or repair authorization within an explicitly initiated UAT run. Designer and source remediation do not implicitly authorize acceptance.
- Put the binding rule inside the distributed native `PHDK-MANAGED` block, restore SKILL YAML front matter to the start of the file, and align entrypoints, boards, examples, commitment criteria and optional acceptance evidence without weakening actual owner, host, security or required-check controls.
- Align affected acceptance/security guidance with the existing production-only verification policy: legitimate application/provider sessions, uniquely run-owned synthetic records, server-side role/tenant enforcement, expiry/revocation and verified cleanup. No new test issuer, staging/database or authentication bypass is authorized.
- Add bounded static coherence guards for deferred stages, explicit entrypoints, native managed rules, SKILL distribution/front matter and known obsolete affirmative transitions. Keep archived history outside the active-policy scan and reject unsafe scan paths. Update UAT Prep regression source to the current policy; behavioral tests and UAT were not run.
- Record source/static verification and its limits in `PHDK_COHERENCE_REPORT.md` and the prepublication delivery checkpoint. Publishing canonical PHDK does not upgrade downstream projects or reload existing agent sessions.

## v2.62.0 — 2026-10-21

### Explicit-only UAT authorization
- Auto and Auto Force finish all development, milestone publication, non-UAT checks and deployment before offering optional acceptance.
- UAT Prep, UAT and UAT Fix are never automatic Auto stages; only an explicit `PHDK uat` invocation authorizes acceptance and its required preparation.
- Retain milestone acceptance stories without synthetic provisioning; report development completion separately from UAT NOT RUN.
- Preserve standalone `PHDK uat prep` as a separate explicit command.

## v2.61.0 — 2026-10-21

### Automatic PHDK-managed hook compatibility remediation
- Add `PHDK_HOOK_COMPATIBILITY.md`: scan effective Git hooks and nested scripts against production-first verification before publication; identify provenance before editing.
- Authorize Auto/Auto Force and Check Fix to repair only proven legacy/PHDK-owned runtime-test hook conflicts while preserving versioning, secret scans, security and independent checks.
- Require bare Check to report findings and preserve owner/external/unknown hooks, never bypass or run prohibited local tests to make a push pass.
- Update active execution, agent, testing and enforcement guidance and vendor the standard. Documentation-only checks; downstream adoption and runtime behavior unverified.

## v2.60.1 — 2026-10-21

### Publish the historical intelligent-development architecture audit
- Publish the previously delivered v2.56.0 read-only architecture audit as an optional repository report, including measured inventory, evidence references, context estimates, delegation analysis, target architecture, alternatives, migration and benchmark proposal.
- Add publication provenance and an explicit addendum: general bounded delegation and progressive context guidance already shipped in v2.57.x; historical findings must not be treated as current rules.
- Link the report from README without adding it to mandatory instructions or the vendoring manifest. No execution-policy change, runtime benchmark, downstream upgrade or deployment is performed.

## v2.60.0 — 2026-10-21

### Pre-implementation visual Design
- Add `PHDK_DESIGN.md`, the standalone `PHDK design` command and conditional lifecycle stage `25-design` after technical/content Plan and before dependent UI implementation.
- Establish four guided decision groups: visual identity, composition, graphic system and experience in context. Recover references, show meaningful alternatives and representative previews, then retain the selected style guide and actual design assets in the repository.
- Reuse `UI_DESIGN_SYSTEM.md`, `UX_UI_DECISIONS.md`, the single shared token/component source and `docs/design/`; preserve owner-approved brands, existing interfaces and immutable historical runs. Designer Mode remains separate implementation/redesign work.

### Auto asks; Auto Force decides
- Normal Auto and standalone Design ask one unresolved visual question at a time and wait for the owner's selection and selected-preview approval before dependent UI coding. Independent authorized work may continue.
- Auto Force performs the same Design responsibilities, selects a direction, records `AGENT_SELECTED_AUTO_FORCE` with rationale and continues without a PHDK visual-approval wait. Actual owner restrictions, sensitive scope/security decisions and external spending/access controls remain binding; agent selection is never represented as owner approval.
- Extend the continuity advisor with an additive `design_choice` blocker, `DESIGN_AWAITING_OWNER` reporting, explicit FORCE selection before dependent implementation, and rejection of completed steps retaining unresolved visual choices. Preserve actual owner stops and the existing advisory-only authority boundary.

### Coherent lifecycle and verification
- Reconcile Plan, UX/UI, lifecycle, Auto/continuity, native instructions, AGENTS, SKILL and README. Integration compares source to the selected baseline; UAT compares the permitted deployed interface; Check evaluates decision provenance, real retained artifacts, component/token usage and current evidence.
- Extend the static coherence guard and add ten behavioral regression cases as source. AST syntax checks passed for the modified advisor, coherence checker and new test source. Behavioral tests were NOT RUN locally under the production-first policy; the complete repository coherence script was NOT RUN because a full local checkout was unavailable.
- Preserve the concurrently published v2.59.0 tenant-risk standard and controls. Keep all previous changelog bytes in the linked `CHANGELOG-through-v2.59.0.md` archive, included in the manifest.
- Design creates no local application server, Docker, staging/database, browser-test or paid-service exception. Static/generated concepts and specification-only choices are not runtime verification. Missing visual capability stays explicit; normal Auto needs an informed specification-only owner choice, while FORCE selects with visual evidence UNVERIFIED and continues permitted work.
- This release changes standards and a local state advisor. It does not prove downstream adoption, actual visual-agent execution, runtime behavior, application deployment or acceptance.

### Verification record
See [docs/verification/v2.60.0-design.md](docs/verification/v2.60.0-design.md) for the source-review scope and execution limits. Publication evidence is established by the actual PR/merge and independent remote-main readback, not this release note.

## Earlier release history

The complete previous changelog, unchanged through v2.59.0, is retained in [CHANGELOG-through-v2.59.0.md](CHANGELOG-through-v2.59.0.md), including its links to older archives.
