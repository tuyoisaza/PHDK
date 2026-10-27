---
repository: tuyoisaza/XeniaCharis
repository_url: https://github.com/tuyoisaza/XeniaCharis
default_branch: main
observed_repository_sha: 8136ef3dd34e3190b05be9805842120b6a17e681
observed_at_utc: "2026-10-27T04:59:57Z"
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
  reviewed_at_utc: "2026-10-27T04:55:56Z"
  evidence: "Same-run review: https://github.com/tuyoisaza/XeniaCharis/blob/main/docs/phdk/lifecycle/20261026-auto-portfolio/68-secure/SECURITY_REPORT.md. Reviewed v0.13.0 managed-secret lifecycle delta and current tenant/data-boundary evidence. No confirmed Critical/High exploitable source vulnerability; source coverage remains PARTIAL. Tenant isolation and applied RLS, host secret scope/revocation, enforceability of the owner-confirmed commercial/contact data boundary, exact PostgreSQL patch, image digest and deployed revision are UNVERIFIED. Node/Python/framework/package versions remain source-evidenced and unchanged by docs-only v0.13.1."
  findings:
    critical: 0
    high: 3
    medium: 2
    low: 0
central_status_source: PHDK
---

# Current evidence

- XeniaCharis main is v0.13.1 at 8136ef3dd34e3190b05be9805842120b6a17e681, independently verified after PR #103 merged. PHDK is current at 2.68.0, matching canonical main; the run verified 79 manifest mappings.
- Source declares Node 24.22.1 and CPython 3.12.16; framework/package-manager versions above remain source-evidenced. The repository inventory has 631 third-party exact-release declarations marked DECLARED_UNREVIEWED; this is not legal/commercial approval.
- Stack review remains PARTIAL, not security clearance. Provisional tenant risk remains R3 High; source and effective controls do not establish residual-risk acceptance. Production runtime, effective RLS, managed-host identity/token scope, migration/worker execution, PostgreSQL patch, image digest and deployed SHA remain UNVERIFIED.
- UAT Prep/UAT/UAT Fix remain DEFERRED — OWNER OPT-IN; UAT NOT RUN. No Railway diagnostics, provider/database write, deployment, behavioral test or application probe was performed for v0.13.1.
