---
repository: tuyoisaza/MEMCP
repository_url: https://github.com/tuyoisaza/MEMCP
default_branch: main
observed_repository_sha: db1eee3d6e2970847e52a4b578d004cd902b1472
observed_at_utc: 2026-11-17T06:35:00Z
phdk_version: 4.0.0
phdk_canonical_version: 4.0.0
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
  reviewed_at_utc: 2026-11-17T06:35:00Z
  evidence: https://github.com/tuyoisaza/MEMCP/pull/51
  findings:
    critical: 0
    high: 0
    medium: 0
    low: 0
central_status_source: PHDK
---

PHDK4.0.0 adopted from5ab95cfc346cd2d77024e3cd8adc359ca8e64ee8; current canonical VERSION rechecked. A downstream canonical-command security-routing link repair is disclosed in MEMCP's run evidence. Source v0.38.0 published through PR51; full production goal remains open. Node22.23.5-alpine pinned, supported major retained with Node26 migration proposal; deployed patch/image digest unverified. Root/web lockfile audits reported zero known advisories at06:09UTC; installed third-party versions are source/lock evidence, not OS/database clearance. PHDK coherence and bounded hermetic profile pass. Counts cover confirmed findings only; overall stack review remains PARTIAL. Pilot, PostgreSQL verification, tenant/customer activation, full recovery and payments are not operationally verified. UAT is explicitly OUT OF SCOPE. No secrets, customer records, provider settings or database writes are included in this status publication.
