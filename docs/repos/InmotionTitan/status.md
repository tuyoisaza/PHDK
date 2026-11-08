---
repository: tuyoisaza/InmotionTitan
repository_url: https://github.com/tuyoisaza/InmotionTitan
default_branch: main
observed_repository_sha: 947993b28e3e08155e982c215f5d0bd4a5e6e21f
observed_at_utc: 2026-11-08T04:23:02Z
phdk_version: 3.0.2
phdk_canonical_version: 3.0.2
phdk_status: CURRENT
tech_stack:
  runtimes:
    - name: node
      declared: ">=24.22.2 <25 || >=26.13.0 <27"
      resolved: "26.13.0 (local build runtime)"
      deployed: UNVERIFIED
  frameworks:
    - name: next
      declared: "16.4.5"
      resolved: "16.4.5"
      deployed: UNVERIFIED
    - name: react
      declared: "19.3.1"
      resolved: "19.3.1"
      deployed: UNVERIFIED
    - name: nestjs
      declared: "12.3.3"
      resolved: "12.3.3"
      deployed: UNVERIFIED
    - name: fastify
      declared: "5.12.8"
      resolved: "5.12.8"
      deployed: UNVERIFIED
  package_managers:
    - name: pnpm
      declared: "11.25.0"
      resolved: "11.25.0"
      deployed: UNVERIFIED
  data_engines:
    - name: postgresql
      declared: "PostgreSQL target; current engine patch unverified"
      resolved: UNVERIFIED
      deployed: UNVERIFIED
  images: []
stack_review:
  status: PARTIAL
  reviewed_at_utc: 2026-11-08T04:23:02Z
  evidence: "https://github.com/tuyoisaza/InmotionTitan/blob/947993b28e3e08155e982c215f5d0bd4a5e6e21f/docs/phdk/lifecycle/2026-11-07-phdk-302-maintenance/HANDOFF.md"
  findings:
    critical: 0
    high: 6
    medium: 2
    low: 1
central_status_source: PHDK
---

App0.38.2 / PHDK3.0.2 published in PR68; pinned standards862c7246716aabc77099ac0aa74b478545334d35, remote gate PASS133. Bounded maintenance only; M7 pause and foreign INDEX/brief preserved. Fresh pnpm audit321 dependencies, zero advisories. Node source pin24.22.2 and local26.13.0 checked against official current release/security sources. No compatible patch identified in reviewed scope.

PARTIAL: deployed runtime/OS/image digest/PostgreSQL/provenance remain UNVERIFIED. Finding counts retain historical immutable legacy findings (6 high,2 medium,1 low), not modern-package findings or newly verified exploitability. Legacy unchanged. One postmerge version GET returned app0.38.1, PHDK3.0.1, bb317026b6833ace50c6cd0873f8cb1573b78181: STALE_OR_DIFFERENT_REVISION. No polling, provider write, SQL or UAT. UAT NOT RUN.
