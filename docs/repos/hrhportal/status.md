---
repository: tuyoisaza/hrhportal
repository_url: https://github.com/tuyoisaza/hrhportal
default_branch: main
observed_repository_sha: UNVERIFIED
observed_at_utc: 2026-10-26T14:09:18Z
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
      resolved: 15.5.28-candidate
    - name: Fastify
      resolved: 5.12.6-candidate
    - name: Zod
      resolved: 3.25.76
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
  status: FINDINGS
  reviewed_at_utc: 2026-10-26T14:09:18Z
  evidence: docs/phdk/lifecycle/20261026-phdk-upgrade-force/00-preflight/STACK_SECURITY_REVIEW.md in active candidate
  findings:
    critical: 0
    high: 1
    medium: 0
    low: 0
central_status_source: PHDK
---

Notes: The candidate is uncommitted on codex/security-maintenance-2026-10-26 and based on remote main SHA 636f32066fbaebd59ef9c4d3d048b223e983ace7 (v0.10.1 / PHDK 2.65.1). Candidate PHDK 2.68.0 and compatible dependency patches are not yet on main or deployed. The candidate audit has one High Zod finding; application release clearance is held. Exact Node build/deployed version and live database state are UNVERIFIED.
