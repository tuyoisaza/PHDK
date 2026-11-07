# PHDK 3.0 coherence and private modules audit

- Date: 2026-11-07
- Source version: PHDK v2.92.1 at canonical GitHub `main` SHA `dc4c5d290ad4df8961488f06cd68e7947aad25f6`.
- Scope: public PHDK standards and GitHub metadata/source of PRIVATE the independently verified **private PHDK-Modules repository**; does not modify donors or consumers.
- Evidence type: source inspection and verified provider metadata. Tests must be reported as NOT RUN unless actually executed.

## Verified findings and changes

1. **P0 — self-contradictory line rule:** `scripts/phdk_coherence_check.py` contained **947 physical lines**, exceeding the consumer's 600-line Python hook. The refactor preserves the command in a small CLI entrypoint and separately vendored routing/quality helpers. Add source-budget checks over all vendored scripts and canonical tests, including canonical/installed synthetic regression fixtures. **No hook exemption.**
2. **P1 — stale SemVer test:** `tests/test_phdk_module_library_policy.py` asserted the current version was exactly 2.90.0, false for current 2.92.1 and every later release. Changed to current VERSION/README/CHANGELOG alignment rather than a historical constant.
3. **P1 — external skill path drift:** `SKILLS_REGISTRY.md` pointed Anthropic Security Guidance at a missing old Claude Code path. The official available source is `anthropics/claude-plugins-official/plugins/security-guidance`. This is a plugin reference, not evidence of installation or authorized hooks. Other selected external sources (Anthropic frontend-design, skill-creator; Addy Osmani; Superpowers; Context7; MCP) resolved at audit time, but existence alone does not prove compatibility.
4. **P1 — distribution closure:** the three Python checker files must be mapped in the manifest, installed atomically and checked in the installed destination layout. An old single-file install cannot reliably run the modular checker.
5. **P1 — private modules readiness:** the separate the independently verified **private PHDK-Modules repository** provider repo is independently confirmed PRIVATE. Its catalog is `{"schema_version":1,"entries":[]}`, and its offline `propose/receive/verify/list` script and synthetic tests exist. There is no accepted module, independently verified two-consumer implementation, measured time saving, published package or authority to copy a donor.
6. **P2 — process overhead:** discover/install only selected skills when relevant; lack of third-party skills should not block default PHDK work. Distinguish applicable reusable capability from generalized abstraction that adds maintenance cost.

## Technical evidence and limits

- Inspected root PHDK 2.92.1 VERSION, README, CHANGELOG, Evolution, Coherence, Upgrade, hook compatibility, manifest, agent/skill/native routes, selected Python scripts/tests, public-private module standards and private receiver/manifest tests.
- Checked PHDK-Modules provider private visibility and the actual empty registry; no library mutation.
- Added tests `tests/test_phdk_coherence_checker.py` to exercise canonical/installed manifest layouts, current command and >600 failure. **Added tests are NOT RUN** under remote GitHub connector access; no runtime PASS is claimed.
- No local checkout Git hooks or Mentoring Upgrade Force run here; their observed compatibility and user-specific customizations remain **UNVERIFIED**.
- No UAT, security advisories scan, running app, browser acceptance or customer data source transfer was performed. Static marker checks do not prove semantic policy coherence.
- Source publication, PR/merge and remote MAIN must be confirmed after actual GitHub actions.

## Architecture conclusion and migration

Maintain PHDK public standards/contracts/disclosure-safe catalog separate from the PRIVATE versioned module library. A donor scan/post-UAT review is read-only. A real transfer requires named owner approval, rights/licensing, sanitization, security, target visibility and verified tests. A module is `ACCEPTED_VERSIONED` only with the independent consumer evidence required by the canonical contract.

Upgrade PHDK as a pinned manifest set with all three checker scripts; check canonical and reconstructed installed layouts. Mentoring does not adopt changes merely because PHDK public `main` advances. This release remains subject to executable validation in a permitted checked-out environment and any actual repo PR gates.
