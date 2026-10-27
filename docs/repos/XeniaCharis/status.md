---
repository: tuyoisaza/XeniaCharis
repository_url: https://github.com/tuyoisaza/XeniaCharis
default_branch: main
observed_repository_sha: d0039bf56fe8094ace825b11e804d192b94f1d75
observed_at_utc: "2026-10-27T21:38:00Z"
phdk_version: "2.69.0"
phdk_canonical_version: "2.69.0"
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
  reviewed_at_utc: "2026-10-27T21:30:00Z"
  evidence: "Fresh Auto Preflight source/lock review: https://github.com/tuyoisaza/XeniaCharis/blob/main/docs/phdk/lifecycle/20261026-auto-portfolio/00-preflight/STACK_SECURITY_REVIEW.md. Canonical PHDK 2.69.0 was adopted; coherence passed 84 mappings. Reviewed key pinned runtimes/frameworks/security-sensitive dependencies against current official sources. Full transitive advisory coverage, base-image digest/OS package inventory, deployed service versions/SHA/runtime, tenant isolation and effective deployment controls remain UNVERIFIED."
  findings:
    critical: 0
    high: 0
    medium: 0
    low: 0
central_status_source: PHDK
---

# Current evidence

- XeniaCharis main is v0.13.14 at d0039bf56fe8094ace825b11e804d192b94f1d75 (PR #118). GitHub commit metadata currently reports both API and web deployment contexts as PENDING, with “Railway is deploying the service”; this does not prove deployed SHA, runtime, or application health.
- Adopted and canonical PHDK are both 2.69.0. The official updater verified 21 manifest destinations; the static coherence checker passed 84 mappings.
- Current source/runtime declarations remain: Node 24.22.1, Python 3.12.16 build recipe, Next 16.4.2, React 19.3.1, FastAPI 0.143.3, SQLAlchemy 2.1.5, pypdf 6.21.2, pnpm 11.25.0 and uv 0.13.5. Deployed versions remain UNVERIFIED.
- Static tenant RLS inventory reports 92/92 lexical declarations across 85 migration sources; it does not prove policy semantics, applied schema or effective tenant denial. Provisional tenant risk remains R3 High; the intended commercial/contact-only data scope does not establish technical enforcement or residual-risk acceptance. The dependency inventory's third-party exact-release declarations remain DECLARED_UNREVIEWED for legal/commercial suitability.
- Stack security review is PARTIAL and overall deployed security status remains UNVERIFIED. No Critical/High issue was confirmed in the reviewed pinned versions, but transitive, image/OS, deployment and host-control coverage remain incomplete.
- UAT Prep/UAT/UAT Fix remain DEFERRED — OWNER OPT-IN; UAT NOT RUN. No Railway diagnostics/logs, provider/database write, manual deployment, behavioral test or application probe was performed.
