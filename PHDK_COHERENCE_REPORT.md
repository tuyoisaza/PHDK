# PHDK coherence report — v2.50.10 candidate

Baseline: `f012f0cf7ac7c749dee269285d4ef5bd2218f7eb` (`origin/main`, v2.50.9).
Scope: vendored release metadata inputs and the downstream coherence check. Review timestamp: 2026-10-13.

## Findings

| Class | Severity | Evidence | Owner | Remediation / next action |
|---|---|---|---|---|
| GAP | Medium | The v2.50.8/v2.50.9 manifest omitted README.md and CHANGELOG.md, although the vendored coherence checker requires both in its root. A KELEDON manifest comparison confirmed those inputs were missing. | PHDK | Add both release metadata files to the manifest and enforce their presence in the coherence checker. |
| VERIFIED | — | Six completion-gate tests pass, covering text and JSON versions, nested/missing/unsafe properties, CLI override, exact remote SHA verification, and fail-closed mismatch behavior. | PHDK | Preserve the regression coverage in future releases. |
| VERIFIED | — | Candidate coherence checker now requires VERSION, README.md and CHANGELOG.md to be both valid release metadata and vendored inputs. It passes against all 52 manifest mappings. | PHDK | Install the candidate in KELEDON, verify byte-for-byte mappings, and run its vendored coherence checker. |
| VERIFIED | — | `PHDK_COHERENCE_STANDARD.md` now states the same distribution invariant as the checker. The completion-gate standard documents text and JSON version sources. | PHDK | Keep standard, implementation and manifest aligned. |
| N/A | — | No runtime dependency, provider call, database, browser, hosted CI, or external service is needed for these deterministic static checks. | PHDK | None. |
| UNVERIFIED | — | KELEDON's installed standards have not yet been synchronized to v2.50.10; the merged downstream coherence run is pending. | KELEDON delivery | After merge, sync the full manifest and run the actual installed checker plus remote completion gate. |

## Release decision

The upstream pull fixed the completion verifier's JSON-version handling but did not distribute the coherence checker's README/CHANGELOG inputs. This release closes the full downstream path: manifest inclusion, a static guard against omission, and an explicit standard. Publication remains pending normal PR review, release checks and independent remote-main readback.
