---
repository: tuyoisaza/hrhportal
repository_url: https://github.com/tuyoisaza/hrhportal
default_branch: main
observed_repository_sha: d8b8b8817b129a30445fd30eed863b4abbbcfaeb
observed_at_utc: 2026-10-27T22:37:15Z
phdk_version: 2.69.0
phdk_canonical_version: 2.69.0
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
      declared: "ghcr.io/railwayapp-templates/postgres-ssl:18"
      deployed: UNVERIFIED
  images:
    - name: postgres-ssl
      tag: "18"
stack_review:
  status: PARTIAL
  reviewed_at_utc: 2026-10-27T22:37:15Z
  evidence: docs/phdk/lifecycle/20261027-phdk-upgrade-force/68-secure/SECURITY_REPORT.md and 00-preflight/STACK_SECURITY_REVIEW.md at observed main SHA
  findings:
    critical: 0
    high: 0
    medium: 2
    low: 1
central_status_source: PHDK
---

Notes: HRH PR #50 delivered v0.10.3 to main at the observed repository SHA. The pinned pnpm 10.0.0 full and production lockfile audits report no known vulnerabilities after same-major Vite/Vitest remediation. The broader review remains partial: the Node range admits EOL Node 20; Railway build/runtime Node and deployed artifact lockfile are unverified; runtime cross-tenant denial is unverified; and the PostgreSQL image is pinned only to major tag 18, with exact patch, digest and provenance unverified. A bounded Railway read at 2026-10-27T22:35:02Z observed @repo/web and @repo/api BUILDING from the same main SHA; successful rollout and deployed source remain unverified. Postgres was SLEEPING. Canonical PHDK main was observed at version 2.69.0, commit ea94b7905c2259761da1125a79571068f309ad1a. UAT NOT RUN; no live application probe was performed.
