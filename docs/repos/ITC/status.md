---
repository: tuyoisaza/ITC
repository_url: https://github.com/tuyoisaza/ITC
default_branch: main
observed_repository_sha: 857aeaea6d0159df31221e7f26df6db03ec64977
observed_at_utc: 2026-11-07T15:13:41Z
phdk_version: 3.0.0
phdk_canonical_version: 3.0.0
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
  reviewed_at_utc: 2026-11-07T15:13:41Z
  evidence: https://github.com/tuyoisaza/ITC/blob/857aeaea6d0159df31221e7f26df6db03ec64977/docs/phdk/lifecycle/20261107-upgrade-300/HANDOFF.md
  findings:
    critical: 0
    high: 0
    medium: 2
    low: 0
central_status_source: PHDK
---

Fresh source-only audit: root/web each10 moderate tooling-chain entries (two advisory families), API/worker0; no high/critical. Compatible parent fixes remain unavailable; no major override. Node22.23.4 and Next15.5.29 retained. PHDK3.0.0 delivered through ITC PR24/main0.28.441 with131 mappings and atomic coherence tooling. Coherence and documentation checks passed; canonical trailing blank line preserved. Runtime, OS image and data-engine patch coverage remain UNVERIFIED. UAT NOT RUN.
