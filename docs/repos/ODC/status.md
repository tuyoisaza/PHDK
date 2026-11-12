---
repository: tuyoisaza/ODC
repository_url: https://github.com/tuyoisaza/ODC
default_branch: main
observed_repository_sha: 1401bf9034367f7b30a8d54783b1eec38eb9b7d4
observed_at_utc: 2026-11-12T23:34:12Z
phdk_version: 3.3.0
phdk_canonical_version: 3.3.0
phdk_status: CURRENT
tech_stack:
  runtimes:
    - name: Python (static asset scripts)
      declared: "3.14.10 (.python-version)"
      resolved: "3.14.7 (assistant workstation only; not repository-owned runtime)"
      deployed: UNVERIFIED
  frameworks: []
  package_managers:
    - name: pip requirements
      declared: "Pillow==13.0.0 (requirements.txt)"
      resolved: "NOT INSTALLED on assistant workstation; project resolution UNVERIFIED"
  data_engines: []
  images:
    - name: Pillow
      declared: 13.0.0
      resolved: "NOT INSTALLED on assistant workstation; project resolution UNVERIFIED"
stack_review:
  status: PARTIAL
  reviewed_at_utc: 2026-11-12T23:17:53Z
  evidence: "ODC Stack Security Review, run 20261112-1644-odc-upgrade-force-330; declared Python/Pillow and official advisories reviewed; full package scan not available"
  findings:
    critical: 0
    high: 0
    medium: 0
    low: 0
central_status_source: PHDK
---

## Notes

- ODC main is verified at 1401bf9034367f7b30a8d54783b1eec38eb9b7d4, VERSION 0.1.7, PHDK 3.3.0. Canonical PHDK main was independently observed at a214ffd39c6bc6bb5695cb80df149ff49e39c11f, version 3.3.0.
- The ODC repository is a documentation bundle with Python graphic-generation scripts. It does not declare a deployed application runtime. Assistant workstation Python 3.14.7 was observed; Pillow is not installed on that workstation. Project dependency resolution and deployment remain unverified.
- Official Python 3.14.10 and Pillow 13.0.0 release/advisory sources were reviewed. Automated package audit tools were not available in the bounded search, so PARTIAL reflects incomplete advisory coverage; zero counts mean no findings confirmed in the scoped review, not a complete scan result.
