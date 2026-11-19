---
repository: tuyoisaza/Mentoring
repository_url: https://github.com/tuyoisaza/Mentoring
default_branch: main
observed_repository_sha: a6b6d590d9e75498c417030d41d8af1668d9c7c1
observed_at_utc: 2026-11-19T09:10:23Z
phdk_version: 4.3.0
phdk_canonical_version: 4.3.0
phdk_status: CURRENT
tech_stack:
  runtimes:
    - name: node
      declared: ">=24.22.3 <25"
      resolved: "24.22.3"
      deployed: UNVERIFIED
  frameworks:
    - name: Next.js
      resolved: "15.5.28"
      deployed: UNVERIFIED
  package_managers:
    - name: pnpm
      resolved: "11.0.9"
  data_engines: []
  images: []
stack_review:
  status: PARTIAL
  reviewed_at_utc: 2026-11-19T09:10:23Z
  evidence: https://github.com/tuyoisaza/Mentoring/pull/173
  findings:
    critical: 0
    high: 0
    medium: 0
    low: 0
uleds_status: IMPLEMENTED_SOURCE
central_status_source: PHDK
---

Mentoring 1.46.0 includes tenant-scoped ULEDS intake, expiration and the support and contextual-feedback panel. Seventeen hermetic tests and four application-generated envelope validations passed. The production dependency audit returned no known advisories. Build/deployment ingestion is unconfigured. The bounded web version read returned 1.45.0 without a SHA. Version 1.46.0 deployment, live Redis durability and UAT remain unverified.
