# PHDK coherence report — v2.50.9 candidate

Baseline: `b7a14623fdaef0db6f0becd856f812c6652efcc3` (`origin/main`, v2.50.8).
Scope: completion-gate version-source behavior, its standard, manifest and release metadata. Review timestamp: 2026-10-13.

## Findings

| Class | Severity | Evidence | Owner | Remediation / next action |
|---|---|---|---|---|
| VERIFIED | — | `scripts/phdk_completion_gate.py` reads plain-text versions and an explicit JSON property; six regression tests pass, including a temporary bare remote whose `main` ref and commit version are checked. | PHDK | Preserve fail-closed path/property validation and verify vendored KELEDON evidence after installation. |
| VERIFIED | — | `PHDK_COMPLETION_GATE.md` documents evidence and CLI forms; `VERSION`, README and newest changelog agree at v2.50.9. | PHDK | Run release coherence and delivery checks before merge. |
| VERIFIED | — | `scripts/phdk_coherence_check.py` passes for 50 manifest mappings. Baseline v2.50.8 includes README and CHANGELOG in the manifest, resolving the previously observed installed-input mismatch after synchronization. | PHDK | Downstream projects must sync the published manifest through the current PHDK Auto delivery. |
| RISK | Low | Completion evidence can name arbitrary version paths/properties. The verifier now rejects absolute/traversal paths and malformed property paths; actual lookup is confined to the selected Git commit tree. | PHDK | Retain rejection tests and report the selected source in delivery evidence. |
| UNVERIFIED | — | The updated checker has not yet been run from KELEDON's vendored installation because v2.50.9 is not published. | KELEDON delivery | Install after the PHDK merge, rerun KELEDON's actual evidence gate, and record its result. |
| N/A | — | No runtime dependency, provider call, database, browser, hosted CI, or external service is required by this parser change. | PHDK | None. |

## Release decision

The baseline checker compared the entire remote version file with the expected semantic version. That conflicts with the completion standard's support for a project's canonical version source when it is a JSON package manifest. The smallest correction adds an explicit JSON property selector, optional CLI overrides, input validation, and regression coverage while preserving plain-text `VERSION` support. Release remains pending normal branch/PR review, local checks, and independent remote-main readback.
