---
repository: tuyoisaza/InmotionTitan
repository_url: https://github.com/tuyoisaza/InmotionTitan
default_branch: main
observed_repository_sha: 9e6fd06a99dbaa30638aba6bff1ced39345f16b2
observed_at_utc: 2026-11-15T13:14:00Z
phdk_version: 3.4.0
phdk_canonical_version: 3.4.0
phdk_status: CURRENT
tech_stack:
  runtimes:
    - name: node
      declared: ">=24.22.3 <25 || >=26.13.1 <27"
      resolved: "host pnpm: 24.22.1; host node: 26.13.0"
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
      declared: "PostgreSQL; current server patch unverified"
      resolved: UNVERIFIED
      deployed: UNVERIFIED
  images: []
stack_review:
  status: PARTIAL
  reviewed_at_utc: 2026-11-15T13:14:00Z
  evidence: "https://github.com/tuyoisaza/InmotionTitan/blob/9e6fd06a99dbaa30638aba6bff1ced39345f16b2/docs/phdk/lifecycle/2026-11-15-integrated-evolution/CHECK_REPORT.md"
  findings:
    critical: 0
    high: 6
    medium: 2
    low: 1
central_status_source: PHDK
---

Application 0.53.0 merged through PR102. PHDK 3.4.0 conservatively synchronized from canonical 7324ed6a1af9e30610862a27bd7a120eb0b444d6. EV00-F1 source milestone only; EV-00 remainder and EV-01–EV-07 are unfinished.

Production dependency audit reported zero advisories. Declared Node floors already include the reviewed same-major security patches; actual host runtimes are below those floors. Deployment runtime, OS/image and PostgreSQL patches remain unverified. Severity counters retain the prior immutable-legacy inventory (6 high/2 medium/1 low), not new modern-package advisories or reverified exploitability; host drift is recorded separately without inventing a severity count.

Typecheck, server/web compile, seven hermetic policy contracts, i18n, version/docs/coherence and legacy-tree checks passed. Local tests do not verify PostgreSQL, tenant behavior in deployment or acceptance. UAT NOT RUN; migration 0111 NOT RUN.

One bounded GET to the established /health/version returned HTTP200/no-store, application0.52.2/PHDK3.3.0 at b97f057ccedd6f50b5e587e1b18f63c94dd44d15: STALE relative to source0.53.0. No polling, provider writes or real-data operations.
