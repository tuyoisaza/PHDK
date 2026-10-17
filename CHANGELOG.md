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
