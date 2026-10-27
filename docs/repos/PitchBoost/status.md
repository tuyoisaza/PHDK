---
repository: tuyoisaza/PitchBoost
repository_url: https://github.com/tuyoisaza/PitchBoost
default_branch: main
observed_repository_sha: 44ede596f7f1877ae28626e39a7ac6ce15f87f10
observed_at_utc: "2026-10-27T23:00:00Z"
phdk_version: "2.69.0"
phdk_canonical_version: "2.69.0"
phdk_status: CURRENT
tech_stack:
  runtimes:
    - name: node
      declared: ">=22.23.4 <23 || >=24.22.1 <25"
      resolved: "22.23.4"
      deployed: "UNVERIFIED for observed main SHA"
  frameworks:
    - name: react
      resolved: "19.2.7"
    - name: vite
      resolved: "6.4.5"
    - name: express
      resolved: "4.22.3"
    - name: zod
      resolved: "4.6.7"
    - name: typescript
      resolved: "5.8.3"
  package_managers:
    - name: npm
      resolved: "10.9.9; lockfile v3"
  data_engines:
    - name: postgresql
      declared: "Existing Railway PostgreSQL18 image"
      deployed: "Connection/load observed historically; exact engine patch UNVERIFIED"
  images:
    - name: application
      declared: "node:22.23.4-bookworm-slim"
      deployed: "UNVERIFIED for observed main SHA"
stack_review:
  status: PARTIAL
  reviewed_at_utc: "2026-10-27T22:40:00Z"
  evidence: "PHDK Upgrade Force on PitchBoost main 60e0af75; npm audit reported 0 vulnerabilities; official Node.js 22.23.4 archive SHA256 verified; bounded Railway read observed sleeping app, Railpack runtime/build metadata while repository declares Dockerfile; exact deployed image/runtime unverified. Review covers known dependency advisories, not universal clearance."
  findings:
    critical: 0
    high: 0
    medium: 0
    low: 0
central_status_source: PHDK
---

PitchBoost main is verified at `44ede596f7f1877ae28626e39a7ac6ce15f87f10`, version 0.2.13, after PR #15. PHDK 2.69.0 is installed and current. Static typecheck, lint and build passed; build emitted existing bundle-size and Rollup warnings. No UAT or runtime visual verification was run. Railway was observed sleeping before this release; deployment of this SHA and exact runtime remain unverified.