---
repository: tuyoisaza/DomiForecAIst
repository_url: https://github.com/tuyoisaza/DomiForecAIst
default_branch: main
observed_repository_sha: 101ba882cce9bf7cf36e189d8b8bd4841b9e55c2
observed_at_utc: 2026-10-29T18:16:00Z
phdk_version: 2.74.0
phdk_canonical_version: 2.74.0
phdk_status: CURRENT
tech_stack:
  runtimes:
    - name: node
      declared: "22.23.4 (.node-version)"
      resolved: "22.23.2 (local)"
      deployed: "UNVERIFIED; observed web /health/version commit 92a8eb4818c7c9b5fae223c38a00ffe152a715a7, before current main 101ba882cce9bf7cf36e189d8b8bd4841b9e55c2"
    - name: python
      declared: "3.13.18 (.python-version); API Docker builder pinned to 3.14.10-slim-bookworm"
      resolved: "UNVERIFIED (API image not built)"
      deployed: "UNVERIFIED; observed API /health/version commit 92a8eb4818c7c9b5fae223c38a00ffe152a715a7, before current main 101ba882cce9bf7cf36e189d8b8bd4841b9e55c2"
  frameworks:
    - name: next
      resolved: "16.4.1"
    - name: react
      resolved: "19.2.9"
    - name: next-auth
      resolved: "5.0.0-beta.31"
    - name: fastapi
      resolved: "0.140.0"
  package_managers:
    - name: npm
      resolved: "npm ci from lock; 404 packages installed with lifecycle scripts disabled"
  data_engines:
    - name: postgresql
      deployed: "UNVERIFIED"
  images:
    - "apps/api/Dockerfile: python:3.14.10-slim-bookworm (source pin; build/deployed digest UNVERIFIED)"
stack_review:
  status: PARTIAL
  reviewed_at_utc: 2026-10-29T18:16:00Z
  evidence: "DomiForecAIst main 101ba882cce9bf7cf36e189d8b8bd4841b9e55c2; docs/phdk/lifecycle/2026-10-27-phdk-upgrade-force/STACK_SECURITY_REVIEW.md"
  findings:
    critical: 0
    high: 0
    medium: 0
    low: 0
central_status_source: PHDK
---

DomiForecAIst main was independently read after PR [#181](https://github.com/tuyoisaza/DomiForecAIst/pull/181), merge commit `101ba882cce9bf7cf36e189d8b8bd4841b9e55c2`, web version 0.10.19. Vendored PHDK 2.74.0 is current against canonical PHDK main `4016187e11da14e1d9b75b8ef8f709c2d204a3be`; coherence check passed for 91 manifest mappings.

Source security maintenance: Node declaration 22.23.4; React/React DOM 19.2.9; API builder Python image declaration 3.14.10. Local Node resolved as 22.23.2. The API `.python-version` remains 3.13.18. npm lock audit reported 0 advisories in 513 resolved package records. These results do not establish universal supply-chain, Python dependency, OS-image or deployed-runtime clearance.

Bounded one-time GETs to both existing `/health/version` hosts returned HTTP 200 JSON with `no-store`; both reported versioned web/API artifacts at commit `92a8eb4818c7c9b5fae223c38a00ffe152a715a7`, which is an ancestor of but not the current main merge commit. The merged revision's deployment is therefore NOT VERIFIED. Railway/provider state, deployed runtimes/image digest, PostgreSQL and operational backup evidence remain UNVERIFIED. No provider writes or deployments were performed.

Scoped source review found no confirmed critical/high finding in reviewed sources; stack coverage remains PARTIAL and security status is not universal clearance. Static verification passed (source gate, TypeScript, ESLint), as did PHDK coherence, reuse catalog, docs audit and npm audit. No Docker, local application/runtime or behavioral tests were run. UAT Prep/UAT/UAT Fix: DEFERRED — OWNER OPT-IN. UAT NOT RUN.
