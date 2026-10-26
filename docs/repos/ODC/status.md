---
repository: tuyoisaza/ODC
repository_url: https://github.com/tuyoisaza/ODC
default_branch: main
observed_repository_sha: 79a13c47b1994dd397822a55bd982f7e63990673
observed_at_utc: 2026-10-26T15:20:07Z
phdk_version: 2.68.0
phdk_canonical_version: 2.68.0
phdk_status: CURRENT
tech_stack:
  runtimes:
    - name: Python (static asset scripts)
      declared: UNDECLARED
      resolved: "3.14.7 (workstation only; not repository-owned)"
      deployed: UNVERIFIED
  frameworks: []
  package_managers: []
  data_engines: []
  images: []
stack_review:
  status: FINDINGS
  reviewed_at_utc: 2026-10-26T14:55:33Z
  evidence: "ODC Stack Security Review, run 20261026-1455-odc-auto"
  findings:
    critical: 0
    high: 0
    medium: 0
    low: 1
central_status_source: PHDK
---

## Notes

- ODC's repository does not declare a runtime, framework, package manager, data engine or deployed image. The resolved Python version above is only the local execution host and is not a project pin or deployed version.
- Static asset scripts import Pillow, but the dependency is neither declared nor resolved. The review records this as one low-severity reproducibility finding; no version was guessed or installed.
- Deployed/runtime coverage remains unverified.