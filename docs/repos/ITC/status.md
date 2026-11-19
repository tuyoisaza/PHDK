---
repository: tuyoisaza/ITC
repository_url: https://github.com/tuyoisaza/ITC
default_branch: main
observed_repository_sha: 4e036a19ff980984ae12b7877e46c4d169db27c7
observed_at_utc: 2026-11-19T10:13:00Z
phdk_version: 4.3.0
phdk_canonical_version: 4.3.0
phdk_status: CURRENT
tech_stack:
  runtimes:
    - name: node
      declared: ">=22.23.4 <23"
      resolved: "22.23.4 (.nvmrc)"
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
  reviewed_at_utc: 2026-11-19T10:10:00Z
  evidence: https://github.com/tuyoisaza/ITC/blob/4e036a19ff980984ae12b7877e46c4d169db27c7/docs/phdk/lifecycle/20261119-upgrade-430/STACK_SECURITY_REVIEW.md
  findings:
    critical: 0
    high: 0
    medium: 14
    low: 0
central_status_source: PHDK
---

Source review PARTIAL / GAPS_FOUND. Counts are root npm affected-package entries, not independent vulnerabilities; web 12 and API/worker 4 overlap. All five lockfiles audited. Runtime/OS/image patch evidence incomplete. No product remediation or UAT claimed. PHDK standards published in ITC PR26, application metadata 0.28.446. ULEDS adoption separately requested, not yet implemented.
