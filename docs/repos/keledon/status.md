---
repository: tuyoisaza/keledon
repository_url: https://github.com/tuyoisaza/keledon
default_branch: main
observed_repository_sha: 48378830abc56e10c67b45a1f6ca30a43e8fa68a
observed_at_utc: 2026-10-26T19:12:00Z
phdk_version: 2.68.0
phdk_canonical_version: 2.68.0
phdk_status: CURRENT
tech_stack:
  runtimes:
    - name: node
      declared: ">=24.22.1 <25"
      resolved: "Docker source tags 24.22.1; registry manifests verified"
      deployed: UNVERIFIED
  frameworks:
    - "NestJS 11, Prisma 5.22, React 19, Vite 7; package constraints, not deployed readback"
    - "Electron 44.9.3 in Browser lock; installer not rebuilt/accepted"
  package_managers:
    - "npm 10.9.8 used for lock-only metadata; host Node22.23.2"
  data_engines:
    - "Railway Postgres image major18; exact running patch UNVERIFIED"
    - "Qdrant running version UNVERIFIED"
  images:
    - "node:24.22.1-slim/alpine/bookworm source pins"
    - "nginx:alpine source, digest/security coverage UNVERIFIED"
stack_review:
  status: PARTIAL
  reviewed_at_utc: 2026-10-26T19:12:00Z
  evidence: "https://github.com/tuyoisaza/keledon/blob/48378830abc56e10c67b45a1f6ca30a43e8fa68a/docs/phdk/lifecycle/20261026-auto-force/SECURITY_REVIEW.md"
  findings:
    critical: 0
    high: 0
    medium: 0
    low: 0
central_status_source: PHDK
---

KELEDON5.8.0 merged through PR296. Counts cover only known npm advisories for seven reviewed lockfiles after compatible remediation; zero counts do not clear unreviewed native/OS/engine/deployed components. Node24 major migration explicitly owner-approved; native audio/Prisma compatibility not behaviorally accepted. Existing production GitHub autodeploy building this SHA at observation; no runtime success inferred. UAT NOT RUN, owner opt-in. No local application tests/build/lint or provider administration.
