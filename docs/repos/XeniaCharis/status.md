---
repository: tuyoisaza/XeniaCharis
repository_url: https://github.com/tuyoisaza/XeniaCharis
default_branch: main
observed_repository_sha: 85e8affe0038495e70181625b011a82d1b1a158b
observed_at_utc: "2026-11-14T02:11:54Z"
phdk_version: "3.4.0"
phdk_canonical_version: "3.4.0"
phdk_status: CURRENT
tech_stack:
  runtimes:
    - name: node
      declared: "24.22.3"
      resolved: UNVERIFIED
      deployed: UNVERIFIED
    - name: python
      declared: "3.12.16 source build"
      resolved: UNVERIFIED
      deployed: UNVERIFIED
  frameworks: []
  package_managers:
    - name: pnpm
      declared: "11.25.0"
  data_engines:
    - name: PostgreSQL
      deployed: UNVERIFIED
  images:
    - name: python
      declared: "python:3.12-slim-trixie"
stack_review:
  status: PARTIAL
  reviewed_at_utc: "2026-11-14T02:11:54Z"
  evidence: https://github.com/tuyoisaza/XeniaCharis/pull/194
  findings:
    critical: 0
    high: 0
    medium: 1
    low: 0
central_status_source: PHDK
---

XeniaCharis main is 0.13.82. The compatible Node, dnspython and OpenTelemetry API patches are merged. The moderate minimatch development dependency advisory remains. The web version endpoint served 0.13.79 on the single readback. UAT was not run.
