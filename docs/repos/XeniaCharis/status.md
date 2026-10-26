---
repository: tuyoisaza/XeniaCharis
repository_url: https://github.com/tuyoisaza/XeniaCharis
default_branch: main
observed_repository_sha: 1de5dbcc5dcbcc69bef4224ba6289fe40711cafa
observed_at_utc: "2026-10-26T20:02:15Z"
phdk_version: "2.68.0"
phdk_canonical_version: "2.68.0"
phdk_status: CURRENT
tech_stack:
  runtimes:
    - name: node
      declared: "24.22.1 (railpack.json and package.json engines)"
      resolved: "24.22.1 (source build configuration)"
      deployed: UNVERIFIED
    - name: python
      declared: ">=3.12,<3.13"
      resolved: "3.12.16 (source build recipe with published SHA-256)"
      deployed: UNVERIFIED
  frameworks:
    - name: next
      resolved: "16.4.2"
    - name: react
      resolved: "19.3.1"
    - name: fastapi
      resolved: "0.143.3"
    - name: sqlalchemy
      resolved: "2.1.5"
  package_managers:
    - name: pnpm
      resolved: "11.25.0"
    - name: uv
      resolved: "0.13.5 (API image build source)"
  data_engines:
    - name: PostgreSQL
      resolved: "Exact server patch UNVERIFIED"
      deployed: UNVERIFIED
  images:
    - name: python
      declared: "python:3.12-slim-trixie (tag; digest UNVERIFIED)"
    - name: uv
      declared: "ghcr.io/astral-sh/uv:0.13.5"
stack_review:
  status: PARTIAL
  reviewed_at_utc: null
  evidence: "2026-10-26 bounded source/advisory review; current XeniaCharis main 1de5dbcc5dcbcc69bef4224ba6289fe40711cafa. Node/Python/pypdf source patches are present; complete transitive/PostgreSQL and deployed-runtime coverage are not established."
  findings:
    critical: 0
    high: 0
    medium: 0
    low: 0
central_status_source: PHDK
---

# Current evidence

- Installed and canonical PHDK versions match at 2.68.0; all 79 manifest destinations and the native managed block matched canonical PHDK main commit 5206b417d9575e24d3bf7fe6ff6992b34006d01f.
- XeniaCharis main v0.6.5 is commit 1de5dbcc5dcbcc69bef4224ba6289fe40711cafa. Patched Node.js, Python and pypdf versions are represented in source. Resolved/deployed runtime, exact PostgreSQL patch, complete transitive dependency coverage, and current production deployment identity remain unverified.
- This is a partial stack review, not an application security clearance.