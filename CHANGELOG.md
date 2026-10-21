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
