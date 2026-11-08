---
repository: tuyoisaza/ITC
repository_url: https://github.com/tuyoisaza/ITC
default_branch: main
observed_repository_sha: 5acaa041a29a8a57d482ccda64ce96fde287464b
observed_at_utc: 2026-11-08T04:22:07Z
phdk_version: 3.0.2
phdk_canonical_version: 3.0.2
phdk_status: CURRENT
tech_stack:
  runtimes:
    - name: node
      declared: ">=22.23.4 <23"
      resolved: "22.23.4 (.nvmrc)"
      deployed: UNVERIFIED
  frameworks:
    - name: next
      resolved: 15.5.29
    - name: fastify
      resolved: 5.12.8
  package_managers:
    - name: npm
      declared: 10.9.2
  data_engines:
    - name: PostgreSQL
      deployed: UNVERIFIED
    - name: Redis
      deployed: UNVERIFIED
  images: []
stack_review:
  status: FINDINGS
  reviewed_at_utc: 2026-11-08T04:22:07Z
  evidence: https://github.com/tuyoisaza/ITC/blob/5acaa041a29a8a57d482ccda64ce96fde287464b/docs/phdk/lifecycle/20261107-upgrade-302/HANDOFF.md
  findings:
    critical: 0
    high: 0
    medium: 2
    low: 0
central_status_source: PHDK
---

Fresh source-only audits: root/web each 10 moderate tooling-chain entries (two advisory families), API/worker zero; no high/critical. Compatible parent fixes remain unavailable; no major override. Node 22.23.4 and Next 15.5.29 retained. PHDK 3.0.2 delivered through ITC PR25/main 0.28.445; 133 mappings, coherence and documentation checks passed. Coverage PARTIAL: runtime, OS image and data-engine patches remain UNVERIFIED. UAT NOT RUN.
