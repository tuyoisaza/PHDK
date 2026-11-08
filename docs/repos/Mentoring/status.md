---
repository: tuyoisaza/Mentoring
repository_url: https://github.com/tuyoisaza/Mentoring
default_branch: main
observed_repository_sha: e8abdb680b6299e88e1fb833a5fa2a12780279db
observed_at_utc: 2026-11-08T04:32:08Z
phdk_version: 3.0.2
phdk_canonical_version: 3.0.2
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
  reviewed_at_utc: 2026-11-08T04:32:08Z
  evidence: https://github.com/tuyoisaza/Mentoring/pull/150
  findings:
    critical: 0
    high: 0
    medium: 2
    low: 0
central_status_source: PHDK
---

A same-major Fastify static update removed one vulnerable glob/minimatch path. Two moderate production advisory findings remain via Google dependencies that pin gaxios 7.1.3. Deployed runtime, operating system and database coverage remain unverified. UAT was not run for this maintenance.
