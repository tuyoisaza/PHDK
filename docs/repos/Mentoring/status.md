---
repository: tuyoisaza/Mentoring
repository_url: https://github.com/tuyoisaza/Mentoring
default_branch: main
observed_repository_sha: d18d37620179b8a4358725612a94005933728414
observed_at_utc: 2026-11-19T08:40:51Z
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
  reviewed_at_utc: 2026-11-19T08:40:51Z
  evidence: https://github.com/tuyoisaza/Mentoring/pull/171
  findings:
    critical: 0
    high: 0
    medium: 0
    low: 0
central_status_source: PHDK
---

The production dependency audit reported zero known advisories. Coverage excludes the deployed runtime, OS image and database version. ULEDS source coverage is partial for client and backend, with product support and contextual feedback missing. The single version read returned application 1.44.2, PHDK 4.2.2 and no commit SHA. Deployment of 1.44.3 remains unverified. UAT was not run.
