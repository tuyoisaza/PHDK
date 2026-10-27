---
repository: tuyoisaza/XeniaCharis
repository_url: https://github.com/tuyoisaza/XeniaCharis
default_branch: main
observed_repository_sha: 80f1c87cc82c3ea3d3718dfe9130b3463d0e2688
observed_at_utc: "2026-10-27T21:22:12Z"
phdk_version: "2.68.0"
phdk_canonical_version: "2.69.0"
phdk_status: BEHIND
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
  evidence: "Same-run review: https://github.com/tuyoisaza/XeniaCharis/blob/main/docs/phdk/lifecycle/20261026-auto-portfolio/68-secure/SECURITY_REPORT.md. Current application/dependency source baseline remains v0.13.7; later releases through v0.13.13 changed evidence/release metadata only. Source coverage remains PARTIAL. Tenant isolation/applied RLS, host secret scope/revocation, enforceability of the owner-confirmed commercial/contact data boundary, exact PostgreSQL patch, image digest, and deployed revision are UNVERIFIED."
  findings:
    critical: 0
    high: 3
    medium: 2
    low: 0
central_status_source: PHDK
---

# Current evidence

- XeniaCharis main is v0.13.13 at 80f1c87cc82c3ea3d3718dfe9130b3463d0e2688 (PR #117). GitHub API/web deployment-status contexts are PENDING for this SHA; they do not prove deployed SHA, runtime, or application health.
- The vendored/adopted PHDK version is 2.68.0; canonical PHDK main is 2.69.0. Status is BEHIND by one minor release. Runtime and framework versions above remain source-evidenced; deployment values remain UNVERIFIED.
- The latest source audit baseline remains v0.13.7; PR #117 and later updates contain no product/dependency source change. Static tenant RLS inventory reports 92/92 lexical declarations across 85 migration sources, not semantic or deployed isolation evidence.
- Stack review remains PARTIAL, not security clearance. Provisional tenant risk remains R3 High; source and effective controls do not establish residual-risk acceptance. The dependency inventory's 631 third-party exact-release declarations remain DECLARED_UNREVIEWED, not legal/commercial approval.
- UAT Prep/UAT/UAT Fix remain DEFERRED — OWNER OPT-IN; UAT NOT RUN. No Railway diagnostics, provider/database write, deployment, behavioral test, or application probe was performed.
