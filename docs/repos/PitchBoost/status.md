---
repository: tuyoisaza/PitchBoost
repository_url: https://github.com/tuyoisaza/PitchBoost
default_branch: main
observed_repository_sha: 82c9d1b2d57643ea7a93a23ed4ff1404985e7514
observed_at_utc: "2026-10-27T23:44:00Z"
phdk_version: "2.70.0"
phdk_canonical_version: "2.70.0"
phdk_status: CURRENT
tech_stack:
  runtimes:
    - name: node
      declared: ">=22.23.4 <23 || >=24.22.1 <25"
      resolved: "22.23.4"
      deployed: "22.23.4 (Railway deployment d520220d-9489-4769-9527-0d4e39078bf0)"
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
      declared: "Railway image ghcr.io/railwayapp-templates/postgres-ssl:18"
      deployed: "Image tag 18 observed; exact PostgreSQL patch UNVERIFIED"
  images:
    - name: application
      declared: "node:22.23.4-bookworm-slim"
      resolved: "Build log base image digest sha256:de170b39439eb0e5a3444ad7d60b015614a381e10fecae2e30ec9e735122f38d"
      deployed: "Runtime log confirms Node 22.23.4; final application image digest UNVERIFIED"
stack_review:
  status: PARTIAL
  reviewed_at_utc: "2026-10-27T23:44:00Z"
  evidence: "PHDK Upgrade Force, canonical 2.70.0 at e3e48d86f6834c876a9d57777811047380248f0f. package-lock npm audit: 0 vulnerabilities. Official Node.js 2026-10-21 security release identifies 22.23.4 as current patched 22.x; Railway deployment d520220d runs observed main SHA 82c9d1b2d57643ea7a93a23ed4ff1404985e7514 and logs Node 22.23.4. Build logs show node:22.23.4-bookworm-slim base digest above. PostgreSQL patch and final application image digest remain unknown; Railway config reports RAILPACK while deployment build logs show Dockerfile, so effective builder configuration is unresolved."
  findings:
    critical: 0
    high: 0
    medium: 0
    low: 0
central_status_source: PHDK
---

PitchBoost main is verified at `82c9d1b2d57643ea7a93a23ed4ff1404985e7514`, version 0.2.16, after PR #17. PHDK 2.70.0 is installed and current. Dependency audit reported zero known vulnerabilities. The Oct. 27 Railway read observed deployment `d520220d-9489-4769-9527-0d4e39078bf0` on that exact SHA, successful status, and Node 22.23.4. Build logs record the pinned Node base image digest. Railway's current service configuration reports Railpack, while the deployment build log shows Dockerfile; exact builder reconciliation, final app image digest, and PostgreSQL patch are unverified. This review is partial and does not claim universal security clearance. UAT and application behavioral verification were not run.
