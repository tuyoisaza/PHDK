---
repository: tuyoisaza/InmotionTitan
repository_url: https://github.com/tuyoisaza/InmotionTitan
default_branch: main
observed_repository_sha: 738833782a92f771a4d2254e0135f0f105920ea2
observed_at_utc: 2026-11-19T07:19:30Z
phdk_version: 4.2.2
phdk_canonical_version: 4.2.2
phdk_status: CURRENT
tech_stack:
  runtimes:
    - name: node
      declared: ">=26.13.1 <27"
      resolved: "verification Node 26.13.1; ambient host versions not deployment evidence"
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
      declared: "PostgreSQL; current server patch unverified"
      resolved: UNVERIFIED
      deployed: UNVERIFIED
  images: []
stack_review:
  status: PARTIAL
  reviewed_at_utc: 2026-11-19T07:19:30Z
  evidence: "https://github.com/tuyoisaza/InmotionTitan/blob/738833782a92f771a4d2254e0135f0f105920ea2/docs/phdk/lifecycle/2026-11-19-phdk-421-upgrade/UPGRADE_REPORT.md"
  findings:
    critical: 0
    high: 6
    medium: 2
    low: 1
central_status_source: PHDK
---

Application 0.99.9 and PHDK 4.2.2 merged through InmotionTitan PR179. Canonical correction published through PHDK PR163 at 684c79780627bdf72adff641fd663cc54997a91b. Coherence, 150 manifest mappings, native owner-text preservation, immutable legacy baseline, application version and documentation checks passed. Audit: 321 dependencies, zero advisories. No functional product change or ULEDS implementation is claimed.

Coverage remains PARTIAL: deployed runtime, image/OS and PostgreSQL patch unknown. Severity counters preserve prior immutable-legacy findings (6 high/2 medium/1 low), not new modern-package advisories or reverified exploitability. No data/provider changes or UAT. Deployed revision UNVERIFIED; source merge is independently verified.
