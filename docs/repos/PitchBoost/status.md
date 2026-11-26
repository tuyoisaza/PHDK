---
repository: tuyoisaza/PitchBoost
repository_url: https://github.com/tuyoisaza/PitchBoost
default_branch: main
observed_repository_sha: 49aef3d2748122bc9868607df294f42b1d0c8d07
observed_at_utc: "2026-11-26T06:31:10Z"
phdk_version: "4.3.0"
phdk_canonical_version: "4.3.0"
phdk_status: CURRENT
tech_stack:
  runtimes:
    - name: node
      declared: ">=22.23.4 <23 || >=24.22.1 <25"
      resolved: "22.23.4 source pin"
      deployed: UNVERIFIED
  frameworks:
    - name: React
      resolved: "19.2.7"
    - name: Vite
      resolved: "6.4.5"
    - name: Express
      resolved: "4.22.3"
  package_managers:
    - name: npm
      resolved: "lockfile v3; build npm UNVERIFIED"
  data_engines:
    - name: PostgreSQL
      deployed: UNVERIFIED
    - name: Firestore
      deployed: UNVERIFIED
  images:
    - name: application
      declared: "node:22.23.4-bookworm-slim"
      deployed: UNVERIFIED
stack_review:
  status: FINDINGS
  reviewed_at_utc: "2026-11-25"
  evidence: "Partial coverage; repository Node pin precedes security release 22.23.5; one moderate development-only minimatch advisory (GHSA-g3hv-75wg-m249)."
  findings:
    critical: 0
    high: 1
    medium: 1
    low: 0
central_status_source: PHDK
---

PitchBoost 0.3.45 is published via [PR #71](https://github.com/tuyoisaza/PitchBoost/pull/71). All 150 downstream manifest files and its native managed block match the pinned 4.3.0 source. The GitHub integration reported success for this commit. Deployed runtime identity, image digest and database patch remain unverified. [Review evidence](https://github.com/tuyoisaza/PitchBoost/blob/49aef3d2748122bc9868607df294f42b1d0c8d07/docs/evidence/phdk-upgrade.v1.md).
