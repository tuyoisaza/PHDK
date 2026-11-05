---
repository: tuyoisaza/InmotionTitan
repository_url: https://github.com/tuyoisaza/InmotionTitan
default_branch: main
observed_repository_sha: 325a92d38c8ce2bda47b767f9c57729d763a1616
observed_at_utc: 2026-11-05T20:07:09.528924+00:00
phdk_version: 2.78.0
phdk_canonical_version: 2.79.0
phdk_status: BEHIND
tech_stack:
  runtimes:
    - name: php
      declared: "8.0.30 (SQL export metadata only)"
      resolved: UNVERIFIED
      deployed: UNVERIFIED
    - name: node
      declared: NOT_IMPLEMENTED
      resolved: UNVERIFIED
      deployed: UNVERIFIED
  frameworks: []
  package_managers: []
  data_engines:
    - name: mariadb
      declared: "10.4.32 (SQL export metadata only)"
      resolved: UNVERIFIED
      deployed: UNVERIFIED
    - name: postgresql
      declared: "OWNER_APPROVED_TARGET; not provisioned"
      resolved: UNVERIFIED
      deployed: UNVERIFIED
  images: []
stack_review:
  status: PARTIAL
  reviewed_at_utc: 2026-11-05T20:07:09.528924+00:00
  evidence: "https://github.com/tuyoisaza/InmotionTitan/blob/325a92d38c8ce2bda47b767f9c57729d763a1616/docs/evidence/stack-security-review.v0.md"
  findings:
    critical: 0
    high: 6
    medium: 2
    low: 1
central_status_source: PHDK
---

Foreground Auto Force adoption of2.78.0 is published in downstream PR4. Static source review found gaps; immutable legacy has not been patched or executed. New application, runtime deployment, provider configuration and acceptance remain unverified/not run. Planned package versions are not installed evidence.

Canonical2.79.0 was observed during this snapshot. Its changelog adds fictional Company Co commercial scenarios; no relevant active migration-policy change was identified in that release note. Current run baseline remains verified2.78.0 until applicable synchronization/preflight; no pinning/updater disablement/UAT activation is introduced.

Reporting only: no methodology release/version change, downstream implementation, provider action or background telemetry.
