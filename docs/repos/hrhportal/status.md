---
repository: tuyoisaza/hrhportal
repository_url: https://github.com/tuyoisaza/hrhportal
default_branch: main
observed_repository_sha: 431a564be5c1432ca216d50b286f63e3cb25f8c6
observed_at_utc: 2026-10-26T15:05:05Z
phdk_version: 2.68.0
phdk_canonical_version: 2.68.0
phdk_status: CURRENT
tech_stack:
  runtimes:
    - name: node
      declared: ">=20"
      resolved: UNVERIFIED
      deployed: UNVERIFIED
  frameworks:
    - name: Next.js
      resolved: 15.5.28
      deployed: UNVERIFIED
    - name: Fastify
      resolved: 5.12.6
      deployed: UNVERIFIED
    - name: Zod
      declared: "^4.6.6"
      resolved: 4.6.7
      deployed: UNVERIFIED
  package_managers:
    - name: pnpm
      resolved: 10.0.0
  data_engines:
    - name: PostgreSQL
      declared: postgres-ssl:18
      deployed: UNVERIFIED
  images:
    - name: postgres-ssl
      tag: "18"
stack_review:
  status: PARTIAL
  reviewed_at_utc: 2026-10-26T15:05:05Z
  evidence: docs/phdk/lifecycle/20261026-phdk-upgrade-force/68-secure/SECURITY_REPORT.md and 00-preflight/STACK_SECURITY_REVIEW.md at observed main SHA
  findings:
    critical: 0
    high: 0
    medium: 2
    low: 0
central_status_source: PHDK
---

Notes: HRH PR #49 merged v0.10.2 to main at the observed repository SHA. The pinned production dependency audit reports no known vulnerabilities after the owner-authorized Zod migration. Medium evidence gaps remain: the declared Node range permits EOL Node 20 while the exact Railway runtime is UNVERIFIED, and runtime tenant-denial evidence was not exercised. A bounded Railway production read at 2026-10-26T15:05:05Z observed @repo/api and @repo/web BUILDING with pending deployments; Postgres was SLEEPING. Deployed source SHA and successful rollout are UNVERIFIED. UAT NOT RUN; no live application probe was performed.
