---
repository: tuyoisaza/LetsWork
repository_url: https://github.com/tuyoisaza/LetsWork
default_branch: main
observed_repository_sha: a44b27b73e7251d1a35e3c1484d984b4d17bfbc5
observed_at_utc: 2026-10-28T18:45:46Z
phdk_version: 2.73.0
phdk_canonical_version: 2.73.0
phdk_status: CURRENT
tech_stack:
  runtimes:
    - name: Node.js
      declared: ">=24.22.1"
      resolved: "24.20.0 (local static-check runtime)"
      deployed: UNVERIFIED
  frameworks:
    - name: Next.js
      version: 16.4.1
      scope: web
    - name: NestJS
      version: 12.1.2
      scope: api
  package_managers:
    - name: pnpm
      declared: "11.25.0"
      resolved: "11.25.0"
  data_engines:
    - name: PostgreSQL
      declared_image: "ghcr.io/railwayapp-templates/postgres-ssl:18"
      provider_deployment: "candidate deployment UNVERIFIED"
      server_version: "UNVERIFIED (not queried)"
  images:
    - name: Node.js API/web build base
      declared: "node:24.22.1-bookworm-slim@sha256:55fb5f5a527ea2c5c4a95f963e48ef90aa38c7b346054fdc8ee9957a2b55d205"
      deployed: UNVERIFIED
    - name: Node.js scanner build base
      declared: "node:24.22.1-bookworm-slim (same pinned digest)"
      provider_builder: RAILPACK
      deployed: UNVERIFIED
stack_review:
  status: PARTIAL
  reviewed_at_utc: 2026-10-28T18:30:00Z
  evidence: "PHDK Auto Force 20261028-upgrade-force; pnpm audit reported zero known advisories; source review found Node patch aligned; Railway read-only metadata did not show v0.59.1 candidate deployed and reports scanner builder RAILPACK."
  findings:
    critical: 0
    high: 0
    medium: 0
    low: 0
central_status_source: PHDK
---

## Notes

- PHDK 2.73.0 matches canonical `tuyoisaza/PHDK` main; all 91 vendored mappings pass the coherence check.
- LetsWork v0.59.1 is published at main SHA `a44b27b73e7251d1a35e3c1484d984b4d17bfbc5` via [PR #241](https://github.com/tuyoisaza/LetsWork/pull/241). The bounded Railway read still showed prior-SHA deployments queued; it did not confirm this candidate. API/web/scanner runtime and the public version endpoint response remain unverified.
- The local static-check runtime is Node 24.20.0 while the project requires `>=24.22.1`; the repository image declarations use 24.22.1. The scanner's effective image remains unknown because Railway reports RAILPACK.
- PostgreSQL exact patch and current backup are unverified. No migration was run; it remains gated on candidate deployment verification and a current pre-migration backup.
- UAT remains DEFERRED — OWNER OPT-IN; UAT NOT RUN.
