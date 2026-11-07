---
repository: tuyoisaza/Mentoring
repository_url: https://github.com/tuyoisaza/Mentoring
default_branch: main
observed_repository_sha: 52f982f5a7a234170c220702fdf2c363599253e6
observed_at_utc: 2026-11-07T15:18:53.605Z
phdk_version: 3.0.0
phdk_canonical_version: 3.0.0
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
  reviewed_at_utc: 2026-11-07T15:18:53.607Z
  evidence: https://github.com/tuyoisaza/Mentoring/pull/147
  findings:
    critical: 0
    high: 0
    medium: 2
    low: 0
central_status_source: PHDK
---

The production dependency audit cleared the qs advisory after updating to 6.16.1. Two moderate findings remain in glob and minimatch. Deployed runtime and infrastructure coverage are partial. The bounded version read returned Mentoring 1.43.13 and PHDK 2.75.0 with a null commit SHA. UAT was not run.
