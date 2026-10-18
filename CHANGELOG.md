## v2.57.0 — 2026-10-18

### Intelligent execution and progressive context
- Add `PHDK_INTELLIGENT_EXECUTION.md`: bounded in-session worker delegation is available across PHDK modes where the host supports it; PMO retains portfolio governance and the primary agent owns integrated delivery.
- Define L0–L4 progressive context routing, compact state recovery, worker task contracts and evidence-based performance measurement.
- Reconcile instruction entrypoints and vendor the new standard. No background agents, recursive worker delegation, provider writes or new spend authorization; downstream updates and speed gains remain unverified.

## v2.56.0 — 2026-10-18

### Milestone planning, PMO execution and incremental Auto delivery
- Add `PHDK_PROJECT_MANAGEMENT_STANDARD.md`, adapting the owner-provided PMI/PMBOK 8 operating model into proportional PHDK governance across value, quality, accountability, seven PMO control domains, five operating focus areas, risk/change discipline and AI-specific controls.
- Require `PHDK plan` to create `MILESTONE_PLAN.md`: coherent value increments mapped to commitments, requirements, workstreams, dependencies, risks, acceptance evidence, expected SemVer impact and UAT intent.
- Change Auto/Auto Force delivery cadence from one terminal version to milestone publication: after a milestone is integrated and technically verified, reconcile SemVer, create version-prefixed commit(s), use the normal PR/merge route to verified remote `main`, then continue from the refreshed main. Lifecycle stages/tasks/slices still do not independently trigger releases.
- Make PMO execute and monitor the milestone roadmap rather than treating workstreams as release boundaries; final cross-milestone Integration Review still precedes UAT.

### Milestone-aware UAT and planning skills
- Require final UAT to read `MILESTONE_PLAN.md`, create `UAT_MILESTONE_MATRIX.md`, and derive at least one intent-linked user-value story for every delivered milestone, with additional role/cross-milestone cases where acceptance needs them.
- Recommend Addy Osmani's Planning and Task Breakdown and Incremental Implementation skills plus Superpowers Writing Plans; external skill file paths, commit cadence and approval conventions never override PHDK artifacts, milestone delivery or execution controls.
- Update lifecycle, agent/native routing, QA, README, manifest, versioning and delivery standards coherently for the new model.

### Source and limits
- The project-management standard operationalizes the owner-supplied knowledge base, which itself states that it is an interpretation based on public PMI material rather than a transcription or PMI certification claim.
- This PHDK release changes standards only; it does not activate Auto/PMO, execute downstream project milestones, run UAT, or deploy applications.

## v2.55.1 — 2026-10-18

### Canonical PHDK evolution and session contract
- Add `PHDK_EVOLUTION_STANDARD.md` as the canonical maintainer-session brief for PHDK identity/spelling, fresh main/version context, workspace boundaries, SemVer decisions, standard reconciliation and verifiable GitHub publication.
- Link the standard from README and route canonical maintenance sessions through AGENTS, SKILL and native managed rules. Distribute the new standard and previously referenced change-management guide through the vendoring manifest.
- Extend the static coherence gate to require the new standard and maintainer entrypoint references. Existing `VERSIONING.md`, `CHANGE_MANAGEMENT.md`, `MAIN_DELIVERY_STANDARD.md` and execution/security controls retain authority.

### Distributed checker compatibility
- Treat `SKILL.md` as an optional canonical entrypoint for static coherence checks: it is present in this standards repository but is not a manifest-vendored file. Validate it when present, without failing an otherwise complete downstream `phdk-standards/` installation.
- The `v2.55.0` commit was a development candidate on this branch, not a separately published main version; `v2.55.1` is the intended first merged version of this standard.

### Scope and adoption
- Standards/routing change only. No downstream repository was upgraded, no agent session was automatically reloaded, and no external deployment, hosted automation or live product verification is implied.
- Run local static coherence and affected tests when supported; report any unexecuted checks and independently verify the GitHub merge/version before claiming publication.

## v2.54.2 — 2026-10-18

### Google OAuth: explicit Railway Variables handoff
- Require a copyable `KEY=value` block for owner-supplied OAuth deployment values, with the consuming Railway service/environment, exact application variable names, full public callback/origin and known non-secret URLs.
- Preserve each project's actual environment contract, identify all missing required values and optional keys, explain their source, and request secret entry directly in the provider.
- Reinforce the handoff in the agent entrypoint and authentication QA checklist. Continue independent implementation while runtime configuration is pending; a setup block does not prove live login.

## v2.54.1 — 2026-10-17

### Auto Force: remember, propose and execute
- Require a visible operative reminder at start/resume, in substantive progress, after partial delivery and before proposed questions/blockers: reload current relevant rules, reconcile inherited blockers, find solutions, propose what is missing and execute the next authorized action. The user does not need an additional continuation or proposal command.
- For each ordinary definition missing from an authorized capability, propose the behavior, justified default, explicit assumptions, meaningful configuration and implementation/acceptance action. Resolve supported reversible choices and continue; do not ask the owner to design everything or recommend excluding confirmed gaps to close the run.
- Align Check, Plan and commitment classification: ordinary missing detail is development work; a genuinely new indispensable decision includes a concrete recommendation and impact while independent work continues.
- Specify supported routine browser recovery in an already-authorized phase, preferring isolation when shared session/cache state could be affected. A blocked test does not stop independent implementation or preparation.
- Keep the change in the operating instructions and native entrypoints. No new executor, hook, state schema or advisor behavior is introduced; downstream session behavior remains subject to actual adoption and execution.

## v2.54.0 — 2026-10-17

### Auto Force and continuous delivery
- Add `PHDK auto force`: PHDK-imposed human/manual/formal reviews are nonblocking immediately, without investigating approval queues or searching for reviewers. Perform substantive technical diff review, required checks, versioned branch push/PR/merge and remote-main verification.
- An actual rejected operation starts report → investigate its cause → repair → revalidate → retry delivery. Preserve the current authorization through this cycle and continue independent work when one operation remains unavailable.
- Both Auto variants record the factual user mandate and progress in run-local `AUTO_STATE.json`, recover it after context loss and continue without another grant. A missing or malformed record is repaired internally; it is neither a permission token nor a new delivery gate.
- Explicitly preauthorize existing mandatory finite isolated suites, including `pnpm test`/Vitest and composition when required. Avoiding optional tests does not prohibit a required hook.
- Align native entrypoints, lifecycle, task tracking, communication, enforcement and delivery rules. The continuation cue reports the current goal/next action and is followed by actual work in the same invocation.

### Verification and adoption
- Add an offline state advisor and behavioral regressions for nonblocking reviews, required checks, real rejection/repair/retry, context recovery, independent work, stop preservation and delivery targets. See `PHDK_COHERENCE_REPORT.md` for executed verification and its limits.
- Distribute the continuity contract and advisor through the managed manifest. Downstream projects adopt v2.54.0 through the existing authorized upgrade/preflight; publishing this source does not imply every active session or installed project has reloaded.
- FORCE changes PHDK's review policy; it does not weaken actual hooks/platform enforcement, erase genuine user restrictions, force-push, administer providers or create background execution.

## v2.53.1 — 2026-10-17

### Auto executes missing implementation after planning
- Require every explicit Auto invocation to reread the complete current intent/requirements baseline and reconcile actual source, coverage and acceptance evidence before reusing artifacts. Preserve valid code and the current authorized scope.
- Classify requirements-only/scaffold-only repositories as unimplemented products when the intent requires software; plan and immediately execute complete greenfield development in the same invocation. Complete partial implementations without reducing the goal to an MVP or interpreting missing code as NOT APPLICABLE. Unavailable source remains UNVERIFIED.
- Make Plan-to-implementation continuation mandatory; reconcile Capture, PMO, Check and commitment wording that could stop Auto or demand redundant approval for already-confirmed requirements. Keep standalone planning/audit scopes and material external decisions intact.
- Align AGENTS, SKILL, native rules, lifecycle/closure contracts and README. Preserve UAT Prep and the subsequent UAT, repair, Check and normal delivery gates.

### Verification scope
- Review policy scenarios and run applicable existing local checks before publication. This standards change does not prove adoption or application-level execution in downstream projects.
- Repair a pre-existing UAT policy test pinned to v2.51.6: retain the minimum supported version and verify current VERSION/README/newest-CHANGELOG agreement so subsequent compatible releases can pass.

## v2.53.0 — 2026-10-17

### PHDK uat prep: implement synthetic test identities before acceptance
- Introduce standalone `PHDK uat prep` and mandatory Auto stage `45-uat-prep` after Integration Review, before browser UAT. Prep explicitly builds/reuses idempotent Company Co synthetic user seeders, supported isolated auth/session bootstrap and role/tenant test support; validates allowed non-browser cases and documents actual account provisioning and cleanup.
- Add vendored `PHDK_UAT_PREP.md`, required `UAT_AUTH_PLAN.md`, `UAT_ROLE_MATRIX.md`, `UAT_FIXTURE_MANIFEST.md`, `UAT_PREP_REPORT.md`, stage snapshots, fresh-candidate reconciliation and Prep-ready/blocked role gates.
- Integrate lifecycle, Auto, standalone UAT, Check, agent/native routing, JWT, Company Co, testing, execution scope and manifest. Preserve UAT-only browser permission and independent connection/no-new-spend verification at stage 50.
- Standards-only release: this repository does not create accounts in downstream applications, deploy staging resources, run browsers or alter authentication providers.

## v2.52.2 — 2026-10-17

### Reconcile JWT authenticated UAT with UAT browser readiness
- Preserve v2.51.6 UAT browser permission/connection/cost gates while adding a separate real synthetic role-authentication gate, rather than treating browser access or fixture data as logged-in identities.
- Reconcile manifest, UAT, Auto and AGENTS standards, test-evidence obligations, and version metadata without dropping concurrent changes.

## v2.52.1 — 2026-10-17

### Standards clarification
- Clarify Company Co as the fixture authority, correct DEVSECOPS heading order and reconcile documentation version metadata after the synthetic JWT/UAT release.

## v2.52.0 — 2026-10-17

### Synthetic identities, authorized JWT UAT and role-complete testing
- Introduce vendored `JWT_STANDARD.md`: test-only identity bootstrap via existing auth provider/session, controlled synthetic Company Co profiles, short-lived validated JWT **only where JWT is used**, and real Playwright/browser sessions per role without asking for human passwords or bearer secrets.
- Separate JWT (JSON Web Token) from UAT (User Acceptance Testing); define authenticated super_admin (multi-tenant) versus admin (single-tenant), audited Test as, tenant-negative testing, production prohibitions, cleanup and concrete evidence gates.
- Integrate bootstrap/negative tests with UAT, Auto, Check, DEVSECOPS, testing, admin console, Company Co, skill entry points and vendoring. Documentation/policy change only; no downstream deployment, new login endpoint, token issuance or live application UAT performed.

## v2.51.6 — 2026-10-17

### Browser readiness and no-unplanned-spend UAT gate
- Vendor `UAT_BROWSER_READINESS_STANDARD.md` and require a real browser connection check at Auto, UAT/UAT Fix and Designer UAT transitions; distinguish phase permission from connected runtime capability.
- Require timestamped access proof/blocked cases/safe-target and cost disposition in UAT access and acceptance reports.
- Prevent improvised paid browser APIs, test-service subscriptions and arbitrary spending caps as substitutes for missing browser access; preserve host consent and data/production constraints.
- Continue independently runnable acceptance cases; never infer browser PASS or stall the entire lifecycle for a hypothetical budget.

### Verification scope
- Standards and manifest consistency only; no actual downstream product browsers or paid services exercised.

## v2.51.5 — 2026-10-16

### Mandatory automation and cost hygiene in Check and Auto
- Add `PHDK_AUTOMATION_HYGIENE.md` and a vendored read-only static scanner for residual GitHub Actions, recurring agents/bots, production watchers, Railway cron and restart-loop risks; add unit regressions.
- Make Check and Auto verify **live** GitHub Actions state/runs/checks and Railway Wait for CI, deployment triggers, cron/restarts and usage when provider metadata is available. Unverified remote state blocks an unsupported ALIGNED claim.
- Preserve justified security checks and GitHub-connected Railway autodeploy; automatic cleanup applies only to provably obsolete PHDK-owned source. No implicit provider setting changes.

### Verification scope
- PHDK policy/source/static checks only. This release does not inspect or modify downstream GitHub Actions or Railway accounts.

## v2.51.4 — 2026-10-16

### Universal tenancy-aware administration console
- Introduce vendored `ADMIN_CONSOLE_STANDARD.md`: deliberate single/multi tenancy, appropriate elevated admin vs platform super_admin/tenant admins, tenant/role/user/invite administration, native language, safe system/integration/secret metadata, protected backups/security/audit/operations, semantic light/dark/corporate theme editing and scoped role testing.
- Extend the conditional AI Admin Standard from prompt text editor to an auditable agent/workflow catalog: input-source mappings, typed JSON output schemas, next-hop graph, validation, publishing, costs and runtime/tenant scope.
- Integrate administration requirements into Capture, Plan, Lifecycle, Auto, UAT, CRUD, Check, the vendored manifest and native/agent instructions; demand actual implementation and negative authorization evidence.
- Add explicit `PHDK check --fix` / `PHDK check fix` as a single user-authorized audit-and-remediate invocation. Bare Check remains nonmutating; never auto-convert tenancy or perform unapproved live destructive/security/provider changes.

### Verification limits
- Standards-source and manifest integration verified through the GitHub connector; no downstream product code, application browser/UAT or production deployment is implied.

## v2.51.3 — 2026-10-16

### Three-theme governance and Superadmin template editing
- Introduce PHDK_THEME_STANDARD.md: one authoritative CSS palette token source, identical light/dark/corporate token contracts, semantic component consumption and precisely documented exceptions.
- Require a real Superadmin Configuración → Edición de templates editor with saved presets, preview/reset, role enforcement and a separate corporate show/hide setting with safe fallback.
- Add vendorable static scanner scripts/phdk_theme_audit.py and local unit tests; Designer Mode must remediate hardcoded palettes and PHDK Check must audit source, behavior and test evidence.
- Integrate the rule into Design System, Designer Mode, Check, UX/UI, agent/skill entrypoints, README and vendoring manifest.

### Verification and limitations
- Static scanner and repo consistency checks do not prove that any downstream app editor exists or works. Product permissions, persistence, theme propagation and UAT must be verified per candidate.
- No downstream repository, live product, GitHub Actions, or hosting deployment is changed by this PHDK standards release.

## v2.51.2 — 2026-10-15

### Designer Mode: exhaustive internal-content review
- Require `DESIGNER_COVERAGE.md` before implementation, with stable review units for screens, internal sections, hidden contents, roles, states and relevant viewports.
- Execute the complete per-unit loop: expose, read, critique, correct, reinspect, verify and continue without ceremonial per-section approvals.
- Separate source review, visual verification and repository delivery; incomplete children and stale shared-component evidence prevent premature completion.
- Explicitly include Designer's bounded per-unit and final UAT/UAT Fix subphases in `EXECUTION_SCOPE.md`, preserving production, access, privacy and provider restrictions.
- Reconcile VERSION and README after the unmerged v2.51.1 candidate. No version number is reused.

### History and adoption
- Preserve the previous changelog byte-for-byte in [CHANGELOG-through-v2.51.0.md](CHANGELOG-through-v2.51.0.md), retaining its relative links.
- Vendor that archive and the existing [history through v2.31.0](ORIGINALS/CHANGELOG-through-v2.31.0.md) so installed changelogs retain their history.
- Preserve the v2.51.0 centralized updater. No downstream product was redesigned, upgraded or deployed by this standards change.

### Verification scope
- Documentation, release metadata, manifest mappings, source/diff review and remote GitHub delivery evidence; no application browser/UAT or production claims.

## Historical releases

[Complete previous changelog through v2.51.0](CHANGELOG-through-v2.51.0.md).

Historical instructions are release records, not current execution authority.
