---
repository: tuyoisaza/ITC
repository_url: https://github.com/tuyoisaza/ITC
default_branch: main
observed_repository_sha: dd01c4631c86c78c5dcb0fe93f857d3a935bd21d
observed_at_utc: 2026-11-07T11:56:01Z
phdk_version: 2.87.0
phdk_canonical_version: 2.87.0
phdk_status: CURRENT
tech_stack:
  runtimes:
    - name: node
      declared: ">=22.23.4 <23"
      resolved: "22.23.4 (.nvmrc)"
      deployed: UNVERIFIED
  frameworks:
    - name: next
      resolved: 15.5.28
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
  reviewed_at_utc: 2026-11-07T11:56:01Z
  evidence: https://github.com/tuyoisaza/ITC/blob/dd01c4631c86c78c5dcb0fe93f857d3a935bd21d/docs/phdk/lifecycle/20261107-upgrade-force/00-preflight/STACK_SECURITY_REVIEW.md
  findings:
    critical: 0
    high: 0
    medium: 5
    low: 0
central_status_source: PHDK
---

Source-only review: two npm advisory families yield ten root/web dependency-chain entries; three primary Next advisories additionally apply. API/worker npm audits have no reported findings. Counts describe reviewed source, not deployed security. Compatible Next 15.5.29 maintenance is pending; deployed runtimes, images and engine patches remain unverified. Standards delivered via ITC PR 22 with 120 remote manifest entries verified. UAT NOT RUN.
