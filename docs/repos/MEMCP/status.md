---
repository: tuyoisaza/MEMCP
repository_url: https://github.com/tuyoisaza/MEMCP
default_branch: main
observed_repository_sha: 0c9a0d01b50df22d52ddefb6f64f9dd820d2e7a1
observed_at_utc: 2026-11-17T02:54:00Z
phdk_version: 3.4.0
phdk_canonical_version: 3.4.0
phdk_status: CURRENT
tech_stack:
  runtimes:
    - name: node
      declared: 22.23.5-alpine
      resolved: UNVERIFIED
      deployed: UNVERIFIED
  frameworks:
    - name: MCP client/server
      resolved: 2.4.0
    - name: pg
      resolved: 8.23.1
  package_managers:
    - name: npm
      resolved: UNVERIFIED
  data_engines:
    - name: PostgreSQL
      declared: postgres-ssl:18
      deployed: UNVERIFIED
  images:
    - name: node:22.23.5-alpine
      digest: UNVERIFIED
stack_review:
  status: PARTIAL
  reviewed_at_utc: 2026-11-17T02:54:00Z
  evidence: https://github.com/tuyoisaza/MEMCP/pull/30
  findings:
    critical: 0
    high: 0
    medium: 0
    low: 0
central_status_source: PHDK
---

PHDK snapshot pinned at 9363450b1c8c49061cc5a057c9f9965ea4a7512e. Standards published in PR 29; maintenance v0.21.3 published in PRs 30/31. Node compatible security patch pinned in source; no confirmed deployed patch or complete transitive/OS advisory clearance. Counts describe confirmed findings only, not a clean security verdict. Static checks passed; UAT NOT RUN. Existing local-only decision-service candidate excluded. No provider settings or database writes.
