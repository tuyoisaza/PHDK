---
repository: tuyoisaza/LetsWork
repository_url: https://github.com/tuyoisaza/LetsWork
default_branch: main
observed_repository_sha: 8b341c0d1d9a674daed0eebad32d3fc078ec39a0
observed_at_utc: 2026-10-26T15:39:02Z
phdk_version: 2.68.0
phdk_canonical_version: 2.68.0
phdk_status: CURRENT
tech_stack:
  runtimes:
    - name: Node.js
      declared: ">=24.22.1"
      resolved: "24.22.1 (portable static-check runtime)"
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
      provider_deployment: SUCCESS
      server_version: UNVERIFIED (not queried)
  images:
    - name: Node.js API/web build base
      declared: "public.ecr.aws/docker/library/node:24.22.1-bookworm-slim@sha256:55fb5f5a527ea2c5c4a95f963e48ef90aa38c7b346054fdc8ee9957a2b55d205"
      deployed: UNVERIFIED
stack_review:
  status: PARTIAL
  reviewed_at_utc: 2026-10-26T15:39:02Z
  evidence: "PHDK Auto Force 20261022-0753-check; pnpm audit reported zero advisories; Railway deployment metadata read-only"
  findings:
    critical: 0
    high: 0
    medium: 0
    low: 0
central_status_source: PHDK
---

## Notes

- PHDK 2.68.0 matches the canonical tuyoisaza/PHDK main version; all 79 vendored manifest mappings pass the coherence checker.
- Repository runtime/image declarations and the locally resolved Node version are not evidence of the runtime currently deployed. Railway showed the LetsWork API, web and scanner services on main with successful deployments; application runtime versions and behavior remain unverified.
- Candidate v0.52.0 was not included in the observed repository SHA above. No deployment of that candidate is claimed.
