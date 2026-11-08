---
repository: tuyoisaza/XeniaCharis
repository_url: https://github.com/tuyoisaza/XeniaCharis
default_branch: main
observed_repository_sha: 1ee22c5dbd3a8a3b02c9782737d112080fd1575f
observed_at_utc: "2026-11-08T04:32:00Z"
phdk_version: "3.0.2"
phdk_canonical_version: "3.0.2"
phdk_status: CURRENT
tech_stack:
  runtimes:
    - name: node
      declared: "24.22.2"
      resolved: UNVERIFIED
      deployed: UNVERIFIED
    - name: python
      declared: ">=3.12,<3.13; source build 3.12.16"
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
  images:
    - name: python
      declared: "python:3.12-slim-trixie; digest UNVERIFIED"
stack_review:
  status: PARTIAL
  reviewed_at_utc: "2026-11-08T04:32:00Z"
  evidence: "https://github.com/tuyoisaza/XeniaCharis/pull/191"
  findings:
    critical: 0
    high: 0
    medium: 1
    low: 0
central_status_source: PHDK
---

PHDK 3.0.2 is merged in XeniaCharis PR #191. Source-lock advisory checks returned no findings for 59 Python packages and no production npm advisories; one moderate minimatch advisory remains in development dependencies. Coverage is partial: deployed runtimes, image digest, database patch and effective tenant isolation remain unverified. Zero counts apply only to these bounded advisory checks. Deployment of this source revision and UAT were not verified by this record.
