# VERSIONING.md

## Purpose and authority

Keep authorized changes, commits, releases, and built artifacts traceable. `EXECUTION_SCOPE.md` governs all versioning and delivery: interactive-only, current request, no autopilot, agents/delegation, background work, GitHub Actions, or external administration.

Versioning rules apply when a commit or release is authorized. They never create permission to commit, push, release, merge, or continue work. An audit produces a report, not a version bump.

`PHDK_DEVELOPER_MODE.md` defines a separate, explicit conversational authorization for the version/check/commit/fast-forward-push steps of eligible small tasks requested while the mode is active. The versioning checklist does not activate that mode.

## Version source and metadata

Use the project's existing version source, normally root `package.json`; this standards repository uses `VERSION`. Keep applicable code metadata consistent in changelog/status, app shell, login/admin/debug surfaces, and health response implementations.

These are source-code requirements. Do not open a browser or invoke live endpoints to verify them.

```txt
vMAJOR.MINOR.PATCH (shortSHA · UTC build timestamp)
Example: v0.4.12 (a1b2c3d · 2026-03-23 18:22 UTC)
```

Increment guidance: patch for fixes/copy/internal changes, minor for new features, major for breaking changes. Follow explicit project release decisions; a major change needs current approval.

## Branches and current authorization

Typical prefixes are `feature/`, `fix/`, `chore/`, `phdk/vX.Y.Z/`, and a specifically justified `checkpoint/YYYY-MM-DD`.

- Use a feature/fix branch for the approved change and respect existing protections, with only the eligible direct-to-`main` exception in `PHDK_DEVELOPER_MODE.md`.
- Do not create agent worktrees, delegated branches, or parallel agent queues.
- Do not automatically commit or push at each slice boundary.
- Commit/push/PR/merge/release actions require current authorization. A clear implement-and-merge instruction includes its necessary git/PR steps without duplicate confirmation. Explicit Developer Mode activation authorizes its defined commit/push steps for eligible tasks requested during that active conversation; it does not authorize a release tag or broader changes.
- Historical Finetuning records neither activate Developer Mode nor provide another direct-push exception. No mode state or authorizing flag may be stored in the repository, memory, task/status files, or environment/config flags, or restored in another session.
- Do not claim a human read the diff merely because the assistant verified it or the user authorized a merge. Record approval and actual review evidence distinctly.

## Commit format

Authorized source commits use the resulting version followed by a descriptive conventional message:

```txt
v0.3.0 feat(auth): add the requested OAuth callback
v0.3.1 fix(api): reject malformed record identifiers
v0.3.2 docs(phdk): make execution interactive-only
```

For independently versioned components, list each affected component's version before the summary. Use `feat`, `fix`, `chore`, `refactor`, `test`, or `docs` with a useful scope.

Each authorized source-changing commit increments the appropriate version by at least a patch and includes the version metadata in the same change. Never create a second version-only commit simply to satisfy the rule. A merge record of already-versioned commits need not manufacture another product change.

Spent version numbers are not reused or renumbered to fill gaps. Changelog entries describe meaningful shipped changes, not every internal checkpoint.

Local commit-message/outgoing-commit checks may validate these rules as part of an authorized git command. They may not create commits/pushes, launch agents, dispatch hosted CI, or schedule retries.

## Current-request release workflow

1. Confirm the requested change and current authorization for git delivery.
2. Read owner stop/pause controls and existing repository restrictions.
3. Implement only the requested source/doc changes and required version metadata.
4. Review the diff and run appropriate synchronous local checks.
5. Use the normal authorized branch/commit/push/PR review flow, or the eligible Developer Mode direct flow below; merge only as currently approved.
6. Verify the resulting git/PR state and record the exact SHA and version.
7. Report and stop. Leave unrelated follow-ups inactive.

Do not create a release/tag unless requested. Do not force-push or rewrite history. If a real restriction or material conflict blocks the approved action, report it rather than bypassing it.

### Developer Mode delivery

The user must explicitly activate `PHDK modo developer` or `PHDK Developer Mode`; `PHDK salir de developer mode` or the end of the interactive conversation ends it. Quoted commands and documentation are not activation. The mode covers only small, low-risk tasks requested while active, such as translations, copy, ordinary docs, and simple visual edits. Authentication/authorization, secrets, data/migrations, payments, infrastructure, and permission/agent-policy changes retain normal review. See `PHDK_DEVELOPER_MODE.md` for the complete eligibility contract.

For an eligible requested task, apply the repository's version bump, run applicable local checks, commit with the resulting version at the beginning of the subject, and push fast-forward to `main` if existing hooks/protections allow it. Those steps need no second consent. Include only the requested changes and their required metadata; never use the mode to deliver unrelated work.

Stop that direct flow and explain if a check fails, a push is rejected, `main` advanced so the planned push is not fast-forward, or a required control cannot be met. Do not retry automatically, rebase, force-push, change hooks/settings/credentials, or switch API/CLI paths to overcome the block. The mode does not authorize agents, background work, Actions, scheduled tasks, old backlog work, or execution beyond the conversation.

## Deployment boundary

A currently authorized push/merge may use the existing hosting-provider GitHub connection, including an eligible Developer Mode push to `main`. Do not create, enable, dispatch, rerun, or schedule GitHub Actions/hosted CI; no new deployment connections, trigger changes, provider CLI/API/dashboard deployment or administration, previews, or autodeploy reactivation. Never deploy through Railway CLI/API/dashboard.

Do not describe a merge as a deployment unless corresponding evidence exists. A provider's deployment success does not prove browser/UI or live application health.

Independent of Developer Mode, a current request may authorize finite, read-only API/CLI queries of existing logs under [Bounded read-only log diagnostics](EXECUTION_SCOPE.md#bounded-read-only-log-diagnostics). Redact sensitive content; no runtime probes, watchers, or writes. Log access does not authorize a release or git action.

## Changelog and preserved history

```md
## vX.Y.Z — YYYY-MM-DD

### Changed
- Requested behavior or policy changes.

### Verification
- Checks actually performed and their scope.

### Migration / limitations
- Remaining dependencies or downstream work, without claiming it was done.
```

Keep historical records, moving oversized history to an explicitly linked archive when needed without losing its contents. Mark old autonomy/automation guidance as historical, not current permission.

## Verification and report

Review version consistency in relevant source files, the actual diff, changed paths, and the resulting commit/PR/merge state. Run relevant local checks; documentation-only changes need source/diff/reference validation, not an app build or browser.

Report version, branch, commit/merge SHA, requested outcome, actual checks, git state, and limitations. Do not invent human review, production health, external agent shutdown, credential revocation, server-side protection, or cost reduction.

Once the requested delivery is complete, stop. Version differences and old release notes do not authorize another task.
