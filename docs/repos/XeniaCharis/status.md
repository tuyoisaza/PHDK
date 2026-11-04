---
repository: tuyoisaza/XeniaCharis
repository_url: https://github.com/tuyoisaza/XeniaCharis
default_branch: main
observed_repository_sha: 9d3249b222189ee3da99a059d330a259ecb96fad
observed_at_utc: "2026-11-04T15:00:30Z"
phdk_version: "2.76.0"
phdk_canonical_version: "2.76.0"
phdk_status: CURRENT
tech_stack:
  runtimes:
    - name: node
      declared: "24.22.2 (package.json and railpack.json)"
      resolved: UNVERIFIED
      deployed: UNVERIFIED
    - name: python
      declared: ">=3.12,<3.13; Dockerfile builds 3.12.16 from SHA-256-checked source"
      resolved: UNVERIFIED
      deployed: UNVERIFIED
  frameworks: []
  package_managers:
    - name: pnpm
      declared: "11.25.0"
      resolved: UNVERIFIED
  data_engines:
    - name: PostgreSQL
      deployed: UNVERIFIED
    - name: Redis
      deployed: UNVERIFIED
  images:
    - name: python
      declared: "python:3.12-slim-trixie; digest UNVERIFIED"
stack_review:
  status: PARTIAL
  reviewed_at_utc: "2026-11-04T15:00:30Z"
  evidence: "https://github.com/tuyoisaza/XeniaCharis/blob/main/docs/phdk/2026-11-04-upgrade-276-stack-review.md"
  findings:
    critical: 0
    high: 0
    medium: 0
    low: 0
central_status_source: PHDK
---

PHDK 2.76.0 and the Node patch declaration were merged in XeniaCharis PRs #124 and #125. Source versions are not proof of deployed runtime. The pnpm production audit found no advisories; Python advisory coverage, image/OS, deployment and server versions remain unverified. UAT was not run.

The canonical native PHDK block contains a scoped browser-configuration allowance and an older categorical prohibition; the semantic conflict needs reconciliation.