---
repository: tuyoisaza/InmotionTitan
repository_url: https://github.com/tuyoisaza/InmotionTitan
default_branch: main
observed_repository_sha: 70ceb058147366efdb8687fa2cbf68568d289192
observed_at_utc: 2026-11-25T12:34:00Z
phdk_version: 4.3.0
phdk_canonical_version: 4.3.0
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
  reviewed_at_utc: 2026-11-25T12:34:00Z
  evidence: "https://github.com/tuyoisaza/InmotionTitan/blob/70ceb058147366efdb8687fa2cbf68568d289192/docs/phdk/lifecycle/2026-11-19-uleds-auto/MS004.md"
  findings:
    critical: 0
    high: 6
    medium: 2
    low: 1
central_status_source: PHDK
---

Application 0.103.0 and PHDK 4.3.0 merged through InmotionTitan PR184. ULEDS milestones1–4 implemented in source: client/backend capture, support/contextual intake and triage/development ledger with draft-only XLSX. Milestones5–6 remain outstanding. Feature activation and migrations were not executed. Manifest/coherence, version, types, compile, hermetic tests and immutable legacy checks passed. Audit:321 dependencies, zero current modern-package advisories. Node26.13.1 security floor verified against the official release notice.

Coverage remains PARTIAL: deployed runtime, image/OS and PostgreSQL patch unknown. Severity counters preserve prior immutable-legacy findings (6 high/2 medium/1 low), not new modern-package advisories or reverified exploitability. No data/provider changes or UAT. Deployed revision UNVERIFIED; source merge is independently verified.
