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
