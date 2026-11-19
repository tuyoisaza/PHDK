---
repository: tuyoisaza/Mentoring
repository_url: https://github.com/tuyoisaza/Mentoring
default_branch: main
observed_repository_sha: 1686ed30f34f4b7d2c410c67784dae3c4b0369d9
observed_at_utc: 2026-11-19T08:31:10Z
phdk_version: 4.2.2
phdk_canonical_version: 4.2.2
phdk_status: CURRENT
tech_stack:
  runtimes:
    - name: node
      declared: ">=24.22.1 <25"
      resolved: "24.22.1"
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
  status: FINDINGS
  reviewed_at_utc: 2026-11-19T08:31:10Z
  evidence: https://github.com/tuyoisaza/Mentoring/pull/170
  findings:
    critical: 0
    high: 0
    medium: 2
    low: 1
central_status_source: PHDK
---

The production dependency audit identified two moderate advisories (glob and minimatch) and one low advisory (fast-xml-parser). Node 24.22.3 is a newer same-major security release than the project pin. Live runtime, image and database versions remain unverified. UAT was not run.
