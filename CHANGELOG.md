## v3.4.0 — 2026-11-13

### MINOR — Universal script-driven, bounded risk-based testing

- Add `PHDK_TEST_AUTOMATION_STANDARD.md`, standard-library Python `scripts/phdk_test_runner.py`, generic project recipe, offline synthetic runner tests and conversational `PHDK test` command. Each repository maps existing native checks to one manifest; the runner records bounded JSON/Markdown reports and redacted logs without consuming agent attention for every case.
- Permit synchronous, short hermetic local unit/contract/in-process integration tests alongside existing static/build checks; retain bans on local application servers, databases, Docker, live API/browser/provider probes and unapproved infrastructure.
- Keep UAT explicitly authorized with existing deployed production, synthetic-owned fixtures, legitimate sessions, cleanup and separate acceptance evidence. No automatic UAT or added lifecycle stage; do not test every conceivable route by default.
- Reconcile scope, production verification, tests/hooks, Plan/Auto/Check, managed native/skill/agent instructions, manifest/help and release metadata. Preserve independent owner controls, security and stop-loss; no auto-upgrade of downstream repos.

## v3.3.0 — 2026-11-12

### MINOR — Delivery stop-loss and WIP-one milestone integration

- New manifest-owned `PHDK_DELIVERY_STOP_LOSS_STANDARD.md`: prioritize one coherent dependency-ready value milestone with verified PR/merge/remote-main evidence before opening other fronts; reconcile contradictory whole-goal versus milestone integration instructions.
- Add additive schema-v1 `AUTO_STATE.json.delivery_watch` and read-only Auto gate dispositions FOCUS_DELIVERY (45 active minutes), RECOVER_DELIVERY (75), DELIVERY_STOP_LOSS (120), plus large-diff, active-WIP, stalled-retry and observed-allowance triggers.
- Carry foreground execution minutes across sessions; preserve stranded product code and exact blocker/recovery action rather than endlessly running reviews. Label unavailable allowance UNKNOWN; never count changed files, open PRs or documents as delivered.
- Add synthetic regression cases and reconcile Plan/PMO/Auto/Continuity/Lifecycle/Check/Delivery/Communication/agent and skill rules/manifest/README. Preserve actual security, owner, hooks, spending/provider boundaries and explicit-only UAT. No background or automatic downstream update.

## v3.2.0 — 2026-11-10

### MINOR — Node.js 26 LTS default and safe migration recommendations

- Set **Node.js 26.x Active LTS (Lithium)** as the named default for new Node projects (entered LTS 2026-10-28; scheduled EOL 2029-04-30). Always select a currently security-patched 26.x release at implementation time.
- Recommend and scope Node 26 migration for existing products without silently changing their major. Continue allowed same-major security patches; prioritize Node 20/EOL. Proven Node 26 incompatibility allows a documented supported Node 24/22 fallback with ADR, support date and revisit checkpoint.
- Reconcile technical stack, Secure, Plan, Auto, Check, coherence, README and managed agent entrypoints; add source-only regression coverage. A PHDK standards release does not modify downstream projects, provider settings, UAT scope or background workflows.

## v3.1.0 — 2026-11-09

### MINOR — Optional Flexible Data Workspace profile

- Introduce vendored `PHDK_FLEXIBLE_DATA_WORKSPACE_STANDARD.md` for evidence-based, owner-chosen, per-resource advanced tabular UX (header sorting, filters, columns, views and opt-in extensions).
- Separate privileged `fields.manage` custom field definitions from normal record editing, preserve server-side role/tenant/field enforcement and typed financial data.
- Link Plan, Design, UX, CRUD, Check, agents and reuse guidance; keep mandatory CRUD and eligible data-exchange contracts independent.
- Public catalog entry remains `SPECIFICATION_ONLY`; no module installation, InmotionTitan implementation, private receipt, UAT, infrastructure or downstream upgrade is implied.

## v3.0.2 — 2026-11-07

### PATCH — Provenance-aware Upgrade and authoritative vendor Force

- Vendor the active project handoff and interview prompts through the official manifest so stale PMO-only text cannot survive a reported current PHDK installation.
- Clarify that bounded subagents are not PMO-exclusive, but a current owner's prohibition always wins.
- Preserve all customized copies during ordinary Upgrade, including committed edits; only published historical PHDK blobs are replaced. Force overwrites every current manifest-owned file and handles previously manifest-owned obsolete paths, preserving owner/project files and unknown extras.
- Diagnose unmanaged active remnants in Preflight/Check and add regression coverage; no downstream projects, UAT, background agents, GitHub remote branches or provider settings are modified.

## v3.0.1 — 2026-11-07

### PATCH — Local-only Git hygiene, with permanent remote-branch retention

- Remove automatic GitHub remote-branch deletion from historical and milestone cleanup in `scripts/phdk_git_history_cleanup.py`. Report read-only remote state as `RETAINED_BY_POLICY` / `ALREADY_ABSENT` and never count retained GitHub branches as incomplete local cleanup.
- Preserve safe local main fast-forward and proven-merged local branch/worktree retirement, including when a remote feature branch advances after merge. A named owner instruction is necessary for any separate remote deletion operation.
- Reconcile Git closeout, delivery, Auto/Force, PMO, Upgrade, Preflight, Check, lifecycle, versioning and agent/skill/native entrypoints; extend mock regression coverage for zero remote-push behavior.
- No GitHub settings changes, automatic downstream upgrade, product UAT or actual local cleanup is implied by this release.

## v3.0.0 — 2026-11-07

### MAJOR — PHDK complies with its own coherence rules

- Break the legacy 947-line monolithic Python coherence checker into a 209-line CLI entrypoint plus 342-line routing and 439-line quality helpers. Continue the same user-facing command with **all three files** vendored atomically.
- Enforce 600 source lines for every manifest-vendored PHDK Python script and canonical PHDK Python test, including the checker itself, in canonical and installed layouts. Treat missing dependencies and oversize scripts as release defects rather than weakening downstream owner hooks.
- Add source-only canonical/installed fixtures and a 601-line negative regression. Repair an obsolete test that pinned the current release to v2.90.0.
- Correct the official Anthropic Security Guidance source and require review of selected skill provenance, host compatibility, permissions, hooks and cost before adoption rather than eagerly checking/installing every reference.
- Verify the independent private PHDK-Modules architecture, scope and **empty** catalog; no real module, private source transfer, downstream adoption or observed time saving is implied.
- Publish the [v3 audit](docs/audits/phdk-v3.0.0-coherence-2026-11-07.md). The audit distinguishes static source checks, GitHub metadata and unexecuted Python/runtime/UAT evidence.

**Migration:** vendor `scripts/phdk_coherence_check.py`, `scripts/phdk_coherence_routing.py` and `scripts/phdk_coherence_quality.py` together. A single-file old checker is not a supported PHDK 3 installation. No new UAT, owner-scope override or product runtime authorization.

## v2.92.1 — 2026-11-07

### Upgrade Force reliability: Git objects, Windows closeout and continuity

- Compare manifest content against published Git blobs using Git-clean semantics and verified attributes; report CRLF-only representation separately, reject actual drift, unsafe paths, altered manifests and custom filters not safe to evaluate. PR/native/product/deployment proofs stay independent.
- Inspect ignored worktree data and Windows long-path risk before cleanup; recheck worktree registration, directory presence and branch SHA after every removal attempt, including failures, and report partial closeout without deleting leftovers.
- Explicit force-only main synchronization preserves recoverable Git-private backups of managed tracked edits, refuses outside owner text, unknown files and divergent history.
- Reject stale Auto COMPLETE with unfinished steps or commitments; the updater accepts --upstream-sha and fetches exactly the pinned snapshot when canonical main moves, reporting later upstream changes rather than creating an endless upgrade cycle.
- Add non-executing discovery of user-installed Windows uv/audit tools and guidance for bounded lockfile/OSV advisory queries with honest runtime/production coverage limits.
- Add synthetic regression test sources and reconcile Upgrade, Auto, Closeout, Secure, README, evolution, manifest, skill and native instructions. No downstream adoption, UAT, unexpected install or background task.

## v2.92.0 — 2026-11-07

### Read-only PHDK help and context-aware first-run onboarding

- Add `PHDK help`, `PHDK help <command>` and `PHDK help --all` for conversational, non-mutating orientation using a complete 25-command canonical inventory and aliases.
- Show installed version, PHDK's operating purpose, sourced project goal or explicit uncertainty, each command's function and one context-based suggested next step without executing it.
- Add vendored `PHDK_HELP.md`, `PHDK_COMMANDS.json` and optional offline `scripts/phdk_help.py`; route through README, onboarding, agent/skill/native rules, a read-only Help Preflight profile and coherence checks.
- Add synthetic catalog/CLI/no-write regression scenarios. No updater, Stack Security Review, product changes, UAT, provider actions, new permission, scheduler or automatic execution follows from Help.

## v2.91.0 — 2026-11-07

### Evidence-gated post-UAT Export Modules assessment

- Auto/Force retains lightweight reuse signals in its existing retrospective, without scanning modules per milestone or initiating UAT. Upon later explicit owner-authorized UAT, one read-only post-acceptance inventory runs at stage 50 or verified stage 60 UAT Fix closeout for the exact accepted deployed revision.
- Defer inventory for UAT NOT RUN, NOT ACCEPTED, ACCEPTANCE INCOMPLETE, unresolved required defects, incomplete fixes, missing or stale revision evidence. Present one deduplicated candidate batch at acceptance closeout without adding an approval gate to UAT.
- Add vendored `PHDK_POST_UAT_EXPORT_STANDARD.md` and offline `scripts/phdk_post_uat_export.py`; 23 synthetic tests verify gating, evidence limits, read-only inventory and no publication. Preserve private-library ownership, named owner selection and catalog two-consumer acceptance gates.
- Reconcile Auto, continuity, UAT/Fix, lifecycle, reuse/export, agent/skill/native instructions, manifest and release markers; no actual UAT, donor export, private repo write, consumer upgrade, scheduler or provider action is initiated.

## v2.90.0 — 2026-11-07

### PHDK Modules: private library architecture and incremental receiving contract

- Define a private, separately governed implementation library, distinct from public PHDK methodology and the sanitized reuse catalog; modules have stable categorized identities, independently versioned immutable releases and digest-checked history.
- Route owner-selected Export Modules candidates into an authorized private receiving workflow with provenance, rights, security, concurrency and compatibility gates. Public catalog promotion and downstream adoption remain distinct, explicitly approved activities.
- Deliver a complete local private-library starter with offline propose/receive/verify/list CLI, schemas and 20 synthetic regression tests; the private GitHub repository itself remains NOT CREATED until a provider creation capability is available and its visibility is verified.
- Reconcile export/reuse/plan, entrypoints, manifest, standards and static source tests without adding private donor code, GitHub Actions, cross-repository crawler, background execution or implicit upgrades.

## v2.89.0 — 2026-11-07

### PHDK Export Modules: scoped reverse reuse discovery and contribution

- Add explicit `PHDK export modules` to inventory candidate modules in the current project, rank packaging/test-documentation signals, compare optional pinned local Git ancestry and show a bounded read-only Markdown/JSON report.
- Connect qualified candidates to the existing reuse catalog, specifications and Auto retrospective; require named owner selection, rights/security review, evidence and a separate versioned implementation package before an authorized canonical PR. No automatic private-code publication or consumer upgrades.
- Vendor the new policy and read-only Python helper; add 11 synthetic CLI/baseline/symlink/provenance tests and reconcile managed agent/skill/native rules and the manifest.

## v2.88.0 — 2026-11-07

### Bundled design selection and interaction motion — one evolution, two independent decisions

- Replace the sequential one-question-per-visual-choice interview with a scope-derived coded decision board: all applicable options, recommendation per decision, one coherent default combination and combined preview. The owner accepts all or overrides selected codes; material changes refresh the preview for one final acceptance. Existing approved visual and motion choices remain independently traceable. Auto Force chooses and continues without a PHDK approval wait.
- Extend the canonical `PHDK_DESIGN_SYSTEM.md` motion interaction contract with shared token timing/presets, CSS/Radix/Motion selection, optional native View Transitions and purposeful button, menu, tab, accordion, modal and route transitions. Specify trigger/state/order/reversibility, focus/ARIA, reduced-motion and fallback behavior.
- Reconcile Plan, Design, Auto/continuity, lifecycle, UX/Designer, Check, explicit-only UAT, agent/skill/native instructions and static coherence guards. No additional animation package, background job, runtime test, new environment, automatic UAT, provider write or downstream project adoption is implied.

## v2.87.0 — 2026-11-07

### Tabular CRUD and self-supplied UAT import files

- Require a useful empty import template, supported file imports and a populated XLSX export for eligible tabular CRUD resources. Declare permissions, per-format schemas, duplicate handling, batch approval, scoped exceptions and cleanup.
- UAT downloads the template, fills a copy with synthetic records and creates independent invalid variants. When a template is missing, record its defect and exercise the importer separately using a known schema. Reopen the actual export and compare records and fields with persisted, authorized values.
- Distribute a local fixture builder and a worked Company Co recipe. Generated inputs do not constitute product acceptance.

## v2.86.0 — 2026-11-07

### A live defect register and bounded UAT repair cycles

- Record defects on discovery in the existing UAT report, preserve original evidence and continue independent cases on the pinned build. Report case coverage separately from actionable defect counts.
- Support a bounded triage worker or an explicitly authorized source repair worker. Keep deployment and retest in a coordinated pass and invalidate in-flight observations if the target changes.
- Add a read-only report checker and linked initial/retest examples. Verified closure requires executed evidence for the affected cases on the selected repaired build. Preserve unresolved issues across handoffs.

## v2.85.0 — 2026-11-07

### Real JWT verification on pre-live synthetic deployments

- Classify the existing release candidate before a pre-live JWT campaign. Alert the operator with the actual target, method, scoped identities and expiry. Keep normal MFA on live, mixed and unknown targets.
- Prefer a supported test factor. Permit an audited, temporary provider-supported MFA exception for exact synthetic accounts and the isolated client when the goal is token or business-flow acceptance. The offline decision helper evaluates supplied evidence and performs no provider writes.
- Require a real provider-issued token, positive and negative verifier/authorization evidence, and separate reporting of JWT, MFA and business outcomes. Verify removal of the exception, restoration of the ordinary policy and invalidation of prior tokens before go-live.

## v2.84.0 — 2026-11-07

### Reproducible UAT identities and admin-led persona switching

- Introduce a vendored synthetic identity standard, linked Company Co café and single-organization rosters, and an offline planner for stable per-run addresses, relationships and expected access decisions.
- Require project-native idempotent provisioning, identity and membership readback, tenant-by-role coverage and verified cleanup. Use the product's audited Test as flow for business journeys after one legitimate elevated sign-in. Prove login-specific cases separately.
- Preserve the explicit Prep/UAT boundary, existing provider controls and the workflow UX verdict. Credentials stay private and unique to each account.

## v2.83.0 — 2026-11-06

### Auto session handoff

- Bound Auto and Auto Force work on a goal to foreground sessions of up to four hours, with earlier handoff when context is at risk or the next slice will not fit. The current session ends after checkpointing. The owner can open a fresh conversation with the supplied resume prompt.
- At session close, present a standard 1920×1080 milestone board with current work, configuration, next steps and independent Git, deployment and acceptance evidence. Record the actual delivery point, including branch-only work and unverified deployment.
- Route the existing Auto advisor and agent instructions through the same boundary. Continue the same goal and run after checking current repository evidence.

## v2.82.0 — 2026-11-06

### Workflow and visual acceptance in UAT
- Explicit UAT follows the role from its normal entry point to a recognizable outcome. Reviewers inspect rendered frames before critical decisions for required information, reading order, competing controls and next-step cues. Ordered procedures and role-appropriate CRUD have concrete walkthrough criteria.
- Each case records functional and workflow UX results with evidence. A required UX failure can reject a functionally successful journey. Missing required visual evidence leaves acceptance incomplete in the absence of a confirmed failure. The existing case catalog, journey map and UX audit carry the evidence through remediation and retest.

## v2.81.0 — 2026-11-06

### Company Co knowledge examples
- Expand the fictional Company Co catalog to six knowledge documents, including detailed reception, after-sales and FAQ examples. Keep them as drafts for review; no provider calls or publication are implied.
- Include the readable knowledge collection in the vendoring manifest and retain the structured catalog.

## v2.80.0 — 2026-11-06

### Company Co campaign examples
- Expand the synthetic commercial catalog with three draft email campaigns, including message content and references to example conversations. Preserve the original campaign entry for compatibility. No sending or provider authorization is implied.

## v2.79.0 — 2026-11-05

### Company Co commercial scenarios
- Add a fictional, structured commercial scenario with opportunities, draft campaigns, knowledge, agent configuration and example usage, linked to the existing Company Co service cases.
- Include the readable and JSON catalogs in the manifest. No external dispatch, actual billing, production seed or UAT is implied.

## v2.78.0 — 2026-11-05

### Auto learning closeout and risk-based critical-change assurance
- Add vendored `PHDK_RETROSPECTIVE_STANDARD.md`: every Auto/Force run prepares an evidence-based process review with the final authorized change and reports actual publication before learning/proposals. Distinguish canonical candidates, local-only actions, already-supported behavior, rejected proposals and missing evidence; zero findings and partial closeouts are valid. No new approval gate, automatic upstream issue/PR, cross-project write or report-only release loop.
- Add vendored `PHDK_CRITICAL_CHANGE_STANDARD.md`: conditional invariants, characterization/equivalence planning, material-decision provenance, idempotent transitions, checkpoints, reconciliation and recovery including post-cutover writes. Apply by integrity/value/access/continuity risk, not only to legacy or financial systems. Reuse existing plans and continuity records.
- Keep technical delivery, actual acceptance, cutover authorization and executed transition independently evidenced. Prevent a source merge/autodeploy from silently triggering an unauthorized critical operation. Preserve the existing machine-readable completion schema and source/requirement reconciliation.
- Wire the contracts through Auto, Plan, completion reporting, README, coherence review and the vendoring manifest; add `scripts/phdk_learning_risk_check.py` and bounded source-review scenarios. Existing agent/skill/native routes still load Auto/Plan/completion; no command or persistent authority flag is added.
- Preserve prior release history byte-for-byte in linked `CHANGELOG-through-v2.77.0.md`.

### Verification and limitations
- The two new policy texts passed the read-only contracts-only source check; three intentional document-marker omissions were correctly rejected. Python syntax compilation passed. These are static document checks, not application or agent-behavior tests.
- Full canonical/vendored coherence execution and the networked completion-gate CLI were not run in this connector-only workspace; no runtime, UAT, sandbox, migration or downstream-adoption PASS is claimed. Remote PR/main evidence is verified and reported separately during publication.
- The proposed local isolated-test exception is NOT activated. Local behavioral-test restrictions, explicit-only UAT, real controls, security Preflight, owner exclusions and spending boundaries remain unchanged. No downstream repository, infrastructure, model selection or background agent is changed by this release.

## Earlier releases

The complete preceding changelog is preserved in [CHANGELOG-through-v2.77.0.md](CHANGELOG-through-v2.77.0.md), including its links to older archives. Historical release notes are not current execution authority.
