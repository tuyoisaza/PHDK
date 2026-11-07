---
repository: tuyoisaza/ITC
repository_url: https://github.com/tuyoisaza/ITC
default_branch: main
observed_repository_sha: a72840f11edcb939d4c5d38d85e9aeb896c8fcd0
observed_at_utc: 2026-11-07T12:17:05Z
phdk_version: 2.88.0
phdk_canonical_version: 2.88.0
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
  reviewed_at_utc: 2026-11-07T12:17:05Z
  evidence: https://github.com/tuyoisaza/ITC/blob/a72840f11edcb939d4c5d38d85e9aeb896c8fcd0/docs/phdk/lifecycle/20261107-upgrade-force/90-delivery/HANDOFF.md
  findings:
    critical: 0
    high: 0
    medium: 2
    low: 0
central_status_source: PHDK
---

Source-only review: two npm tooling advisory families yield ten root/web dependency-chain entries. Three Next advisories were patched at15.5.29; compatible Sentry/TypeScript-ESLint parents still depend on affected glob/minimatch majors. API/worker initial audits have no reported findings. No high/critical in scoped audit; this is not deployed-stack clearance. Standards and patch delivered via ITC PR23/main0.28.434. Static lint/types/service closures, docs and canonical remote content checks passed. Deployed runtime, OS images and data-engine patches remain unverified. UAT NOT RUN.
