---
repository: tuyoisaza/DomiForecAIst
repository_url: https://github.com/tuyoisaza/DomiForecAIst
default_branch: main
observed_repository_sha: 73bb897ec4e532d7b2582a199b879a5cc136a3c4
observed_at_utc: 2026-10-27T00:18:54.796543+00:00
phdk_version: 2.68.0
phdk_canonical_version: 2.68.0
phdk_status: CURRENT
tech_stack:
  runtimes:
    - name: node
      declared: "22.23.4 (.node-version)"
      resolved: "UNVERIFIED"
      deployed: "UNVERIFIED"
    - name: python
      declared: "3.13.18 (.python-version)"
      resolved: "UNVERIFIED"
      deployed: "UNVERIFIED"
  frameworks:
    - name: next
      resolved: "16.4.1"
    - name: react
      resolved: "19.2.7"
    - name: next-auth
      resolved: "5.0.0-beta.32"
    - name: fastapi
      resolved: "UNVERIFIED"
  package_managers:
    - name: npm
      resolved: "UNVERIFIED"
  data_engines:
    - name: postgresql
      deployed: "UNVERIFIED"
  images: []
stack_review:
  status: PARTIAL
  reviewed_at_utc: 2026-10-27T00:18:54.796543+00:00
  evidence: "DomiForecAIst main73bb897 SECURITY_REPORT.md and docs/phdk/lifecycle/2026-10-26-compliance-security/"
  findings:
    critical: 0
    high: 0
    medium: 0
    low: 0
central_status_source: PHDK
---

Source version0.8.0 delivered through [PR102](https://github.com/tuyoisaza/DomiForecAIst/pull/102). Static source/type/lint/format/theme gates and remote-main completion verifier passed. All19 scoped Check source findings addressed. Original22 pending dual-budget files preserved.

Bounded advisory coverage: npm lock0 findings; OSV64 exact Python pins0 at review time. Counts describe those scans, not universal security clearance. Compatible pins include certifi2026.10.23, mako1.4.3, pypdf6.21.2 and urllib3 2.8.0. Prior builder logs showed Node22.23.3/Python3.13.16; declared patch pins are not deployed-version proof.

Existing GitHub-connected Railway web/API autodeploy observed BUILDING for73bb897. Deployment, rendered fidelity, operational backups, distributed rate behavior and full external automation/cost coverage remain UNVERIFIED. CSP intentionally report-only by owner approval. English business copy may fall back to Spanish. UAT NOT RUN — DEFERRED — OWNER OPT-IN. No provider writes, CI dispatch, runtime tests, browser/DB probes, new infrastructure or spending.
