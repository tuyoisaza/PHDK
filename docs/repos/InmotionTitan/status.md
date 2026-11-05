---
repository: tuyoisaza/InmotionTitan
repository_url: https://github.com/tuyoisaza/InmotionTitan
default_branch: main
observed_repository_sha: 2eac3fbacd9d05b499cfd13c0920f4d4ba2cbb8b
observed_at_utc: 2026-11-05T23:48:14.068602+00:00
phdk_version: 2.79.0
phdk_canonical_version: 2.79.0
phdk_status: CURRENT
tech_stack:
  runtimes:
    - name: node
      declared: ">=24.22.1 <27"
      resolved: "26.13.0 (local build runtime)"
      deployed: UNVERIFIED
  frameworks:
    - name: next
      declared: "16.4.5"
      resolved: "16.4.5"
      deployed: UNVERIFIED
    - name: react
      declared: "19.3.1"
      resolved: "19.3.1"
      deployed: UNVERIFIED
    - name: nestjs
      declared: "12.3.3"
      resolved: "12.3.3"
      deployed: UNVERIFIED
    - name: fastify
      declared: "5.12.8"
      resolved: "5.12.8"
      deployed: UNVERIFIED
  package_managers:
    - name: pnpm
      declared: "11.25.0"
      resolved: "11.25.0"
      deployed: UNVERIFIED
  data_engines:
    - name: postgresql
      declared: "Owner-approved target; repository migrations prepared, not executed"
      resolved: UNVERIFIED
      deployed: UNVERIFIED
  images: []
stack_review:
  status: PARTIAL
  reviewed_at_utc: 2026-11-05T23:48:14.068602+00:00
  evidence: "https://github.com/tuyoisaza/InmotionTitan/blob/2eac3fbacd9d05b499cfd13c0920f4d4ba2cbb8b/docs/evidence/migration2-progress.md"
  findings:
    critical: 0
    high: 6
    medium: 2
    low: 1
central_status_source: PHDK
---

M4 source delivered in PR7/main2eac3fb, application0.2.0; PHDK2.79.0 adoption is published. Clean API/web build and static packaging passed; fresh pnpm audit reported zero known dependency advisories. Official Node/Next security notices reviewed. This does not establish complete runtime, OS, provider or database security coverage.

Finding counts retain the earlier immutable legacy source review (six high, two medium, one low); they are not findings newly attributed to the modern application. Legacy was neither modified nor executed. Source findings and runtime assurance remain separate. Modern permission/history/data boundaries are reviewed in m4-read-coverage.md.

One bounded deployed-version GET returned403; deployment remains UNVERIFIED. UAT NOT RUN, no real-data import, SQL execution or cutover. M5-M7 are ongoing in the current foreground migration goal. No provider changes, scheduler, telemetry or methodology release is part of this status refresh.
