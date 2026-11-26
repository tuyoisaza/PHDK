---
repository: tuyoisaza/PitchBoost
repository_url: https://github.com/tuyoisaza/PitchBoost
default_branch: main
observed_repository_sha: bff042ec9ff3e7767851b10f8486b3c221828b48
observed_at_utc: "2026-11-26T06:37:13Z"
phdk_version: "4.3.0"
phdk_canonical_version: "4.3.0"
phdk_status: CURRENT
tech_stack:
  runtimes:
    - name: node
      declared: ">=22.23.5 <23 || >=24.22.3 <25"
      resolved: "22.23.5 source pin"
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
      declared: "node:22.23.5-bookworm-slim"
      deployed: UNVERIFIED
stack_review:
  status: PARTIAL
  reviewed_at_utc: "2026-11-26"
  evidence: "Source pins use patched Node lines and minimatch 11.0.9; the final npm lock registry query returned zero advisories for 736 named packages. Runtime coverage remains partial."
  findings:
    critical: 0
    high: 0
    medium: 0
    low: 0
central_status_source: PHDK
---

PitchBoost 0.3.46 is published via [PR #72](https://github.com/tuyoisaza/PitchBoost/pull/72). All 150 downstream manifest files and its native managed block match the pinned 4.3.0 source. GitHub recorded a production deployment for this commit. Deployed runtime identity, image digest and database patch remain unverified. [Review evidence](https://github.com/tuyoisaza/PitchBoost/blob/bff042ec9ff3e7767851b10f8486b3c221828b48/docs/phdk/lifecycle/20261126-security-check/CHECK_REPORT.md).
