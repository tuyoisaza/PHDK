---
repository: tuyoisaza/ITC
repository_url: https://github.com/tuyoisaza/ITC
default_branch: main
observed_repository_sha: 1a8f39107cd6d21c3c5b6f653e44bd790b357f1e
observed_at_utc: 2026-11-19T10:41:00Z
phdk_version: 4.3.0
phdk_canonical_version: 4.3.0
phdk_status: CURRENT
tech_stack:
  runtimes:
    - name: node
      declared: ">=22.23.5 <23"
      resolved: "22.23.5 (.nvmrc)"
      deployed: UNVERIFIED
  frameworks:
    - name: next
      resolved: 15.5.29
  package_managers:
    - name: npm
      declared: 10.9.2
  data_engines:
    - name: PostgreSQL
      declared: "image tag 18"
      deployed: UNVERIFIED
    - name: Redis
      declared: "image tag 8.10.1"
      deployed: UNVERIFIED
  images: []
stack_review:
  status: FINDINGS
  reviewed_at_utc: 2026-11-19T10:36:00Z
  evidence: https://github.com/tuyoisaza/ITC/blob/1a8f39107cd6d21c3c5b6f653e44bd790b357f1e/docs/phdk/lifecycle/20261119-uleds/SECURITY_REVIEW.md
  findings:
    critical: 0
    high: 0
    medium: 10
    low: 0
central_status_source: PHDK
---

Source review PARTIAL / GAPS_FOUND. Root and web each have 10 moderate npm affected-package entries (overlapping), API/worker/Railway zero; no high/critical. All five lockfiles audited. Compatible Node22/Hono/OTel source fixes applied. Runtime/OS/image patch evidence remains incomplete. ITC0.28.447/ULEDS source delivered via PR27; PHDK4.3.0 via PR26. Static profile7/7 PASS; UAT NOT RUN. Web autodeploy BUILDING at bounded observation; served version UNVERIFIED. No provider settings, DB migration or live application probes.
