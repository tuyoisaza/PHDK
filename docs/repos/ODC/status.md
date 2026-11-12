---
repository: tuyoisaza/ODC
repository_url: https://github.com/tuyoisaza/ODC
default_branch: main
observed_repository_sha: 54bcaf55235f8eafcab8499459ae93548d748dc7
observed_at_utc: 2026-11-12T16:29:49Z
phdk_version: 3.2.0
phdk_canonical_version: 3.2.0
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
      resolved: UNVERIFIED
  data_engines: []
  images:
    - name: Pillow
      declared: 13.0.0
      resolved: UNVERIFIED
stack_review:
  status: PARTIAL_UNVERIFIED
  reviewed_at_utc: 2026-11-12T16:29:49Z
  evidence: "ODC Stack Security Review, run 20261112-1018-odc-upgrade-force"
  findings:
    critical: 0
    high: 0
    medium: 0
    low: 0
central_status_source: PHDK
---

## Notes

- ODC main at `54bcaf55235f8eafcab8499459ae93548d748dc7` declares Python 3.14.10 and Pillow 13.0.0. These source declarations do not establish installed or deployed versions.
- The assistant workstation resolved Python 3.14.7; this is local evidence only and was not upgraded. Pillow was not installed on that host. No project generator was run.
- Compatible security maintenance was applied based on the official Python 3.14.10 and Pillow 13.0.0 releases. Installed dependency and deployment coverage remain unverified.
