---
repository: tuyoisaza/XeniaCharis
repository_url: https://github.com/tuyoisaza/XeniaCharis
default_branch: main
observed_repository_sha: 54140e38dac27a468b5e701f480028d8859ed3c7
observed_at_utc: "2026-10-27T00:27:01Z"
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
    - name: pypdf
      resolved: "6.21.2"
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
  reviewed_at_utc: "2026-10-27"
  evidence: "Same-run bounded source security review is recorded at https://github.com/tuyoisaza/XeniaCharis/blob/main/docs/phdk/lifecycle/20261026-auto-portfolio/68-secure/SECURITY_REPORT.md. Its functional-source review is pinned to v0.12.0; dependency/runtime versions remain unchanged through v0.12.8. The v0.12.8 final diff review covered the new read-only license metadata auditor and evidence; no package versions or application behavior changed. No Critical/High exploitable source vulnerability was confirmed by the bounded review. Overall stack status remains PARTIAL because runtime, effective RLS, host secret scope, exact PostgreSQL patch, image digest and deployed revision are unverified."
  findings:
    critical: 0
    high: 0
    medium: 0
    low: 0
central_status_source: PHDK
---

# Current evidence

- Installed and canonical PHDK versions match at 2.68.0. All 79 manifest destinations and the native managed block were verified against canonical PHDK main during the current run.
- XeniaCharis main v0.12.8 is commit 54140e38dac27a468b5e701f480028d8859ed3c7. Source declares Node 24.22.1 and CPython 3.12.16; lock entries include pypdf 6.21.2. The dependency inventory contains 631 third-party exact-release declarations marked DECLARED_UNREVIEWED; publisher metadata is not legal/commercial approval.
- The stack review is PARTIAL, not an application security clearance. Effective PostgreSQL RLS, host identity/token scope, exact database patch, image digest, deployed runtime/revision and production behavior remain UNVERIFIED. Candidate deployment was not queried or observed.