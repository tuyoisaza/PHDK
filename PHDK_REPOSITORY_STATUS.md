# PHDK Repository Status Registry

## Purpose

Provide a small, central, human-readable inventory of PHDK adoption and stack-security posture for repositories owned by `tuyoisaza`. The registry lets maintainers compare downstream repositories against the current PHDK release and current stack recommendations without installing a scheduler, background agent, GitHub Action, webhook, or telemetry service.

This standard is distributable PHDK policy. It does not grant access to any repository, create credentials, or authorize product remediation.

## Applicability

A downstream repository MUST publish or refresh a central status record when all of the following are true:

1. the repository uses PHDK;
2. its canonical GitHub repository is `tuyoisaza/<repo>`;
3. the active agent/session already has write access to `tuyoisaza/PHDK`; and
4. a foreground PHDK operation has current evidence to report.

If ownership cannot be verified, the repository is outside this registry contract. If write access to `tuyoisaza/PHDK` is unavailable, do not request credentials or block the downstream task. Report:

```text
CENTRAL_STATUS: NOT_PUBLISHED
REASON: CANONICAL_PHDK_WRITE_ACCESS_UNAVAILABLE
```

Repositories outside `tuyoisaza/*` MUST NOT publish into this registry unless the owner explicitly expands the scope in a later PHDK standard.

## Canonical location

Each eligible repository owns exactly one current record:

```text
tuyoisaza/PHDK
docs/repos/<repository-name>/status.md
```

Use the exact GitHub repository name as the directory name. The file is a current status snapshot, not an append-only audit log.

Example:

```text
docs/repos/DEBATE/status.md
```

## Required status schema

The record MUST be concise Markdown with this machine-readable front matter followed by an optional short notes section:

```yaml
---
repository: tuyoisaza/<repo>
repository_url: https://github.com/tuyoisaza/<repo>
default_branch: main
observed_repository_sha: <full commit SHA or UNVERIFIED>
observed_at_utc: <ISO-8601 UTC timestamp>
phdk_version: <installed/adopted version or UNVERIFIED>
phdk_canonical_version: <fresh canonical version observed or UNVERIFIED>
phdk_status: CURRENT | BEHIND | AHEAD | UNVERIFIED
tech_stack:
  runtimes:
    - name: node
      declared: ">=22"
      resolved: "22.23.4"
      deployed: "22.23.4"
  frameworks: []
  package_managers: []
  data_engines: []
  images: []
stack_review:
  status: PASS | FINDINGS | PARTIAL | UNVERIFIED
  reviewed_at_utc: <ISO-8601 UTC timestamp or null>
  evidence: <short evidence reference or null>
  findings:
    critical: 0
    high: 0
    medium: 0
    low: 0
central_status_source: PHDK
---
```

Use only values supported by current repository/provider evidence. Unknown build/deployed/runtime values remain `UNVERIFIED`; do not infer them from package constraints. Do not include secrets, tokens, connection strings, private user data, vulnerability exploit details, or copied provider credentials.

## When to refresh

Refresh the central record during the same foreground session after any of these events, when the applicability conditions are satisfied:

- successful `PHDK upgrade` or `PHDK upgrade force`, including no-op standards synchronization after the required Stack Security Review;
- Preflight adoption of a newer canonical PHDK version;
- a completed `PHDK secure` review that materially changes stack-security findings;
- a PHDK-delivered change that materially changes the reported runtime/framework/package-manager/data-engine/image versions.

Do not publish a speculative record before the underlying evidence exists. Do not open a second downstream mission merely to refresh the registry.

## Publication behavior

The downstream repository remains the source of truth for its product code and configuration. The central status file is a reporting artifact in `tuyoisaza/PHDK`.

When publication is applicable:

1. read the existing `docs/repos/<repo>/status.md`, if present;
2. preserve no historical prose that conflicts with the new current snapshot; replace the current snapshot with fresh evidence;
3. use a scoped branch/PR in `tuyoisaza/PHDK` unless an explicitly authorized PHDK delivery mode permits otherwise;
4. write only the status path for that repository plus any required central index metadata;
5. verify the resulting remote PHDK `main` content before reporting `CENTRAL_STATUS: PUBLISHED`.

A failed central write MUST NOT roll back or invalidate an otherwise successful downstream upgrade, security review, or delivery. Report the two outcomes independently.

## Status comparison semantics

`phdk_status` is determined only from version evidence:

- `CURRENT`: installed/adopted version equals the fresh canonical PHDK version;
- `BEHIND`: installed/adopted version is lower than canonical;
- `AHEAD`: installed/adopted version is higher than canonical;
- `UNVERIFIED`: either side cannot be established.

`stack_review.status` is independent of PHDK version. A repository may be CURRENT and still have FINDINGS.

The registry is intended to answer two separate questions:

1. Which repositories are behind the current PHDK standard?
2. Which repositories are below current stack-security recommendations or have incomplete evidence?

Do not collapse those questions into one health flag.

## No background behavior

This standard creates no polling, scheduled scan, recurring job, GitHub Action, webhook, repository crawler, or autonomous maintenance loop. PHDK learns about a repository only when a foreground session is already operating on that repository and has the required access.

A future explicit owner request may authorize a separate central audit across repositories. This status registry alone does not.
