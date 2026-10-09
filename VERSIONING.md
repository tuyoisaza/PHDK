# VERSIONING.md

## Purpose and authority

Keep authorized changes, commits, releases, and built artifacts traceable. `EXECUTION_SCOPE.md` governs all versioning and delivery: active conversation and current request, no unattended execution, agents/delegation, background work, GitHub Actions, or external administration. `PHDK_AUTO.md` defines continuous development through the whole identified goal.

Versioning follows the current request's delivery scope. A request to implement, fix, or update repository code or documentation includes the normal versioned branch/PR delivery to verified remote `main` in `MAIN_DELIVERY_STANDARD.md`, unless the user specifies a narrower scope or the user/repository specifies another target. An audit produces a report, not a version bump; a bare `PHDK upgrade` retains its limited scope in `EXECUTION_SCOPE.md`. Versioning alone does not authorize a new task or a release tag.

`PHDK_DEVELOPER_MODE.md` defines a separate, explicit conversational authorization for the version/check/commit/fast-forward-push steps of eligible small tasks requested while the mode is active. The versioning checklist does not activate that mode.

With explicit `PHDK auto`, build the entire goal into one cohesive candidate, run final integrated verification, and reconcile its version for normal branch/PR delivery. Do not bump, release, commit, push, or ask for acceptance merely because a stage ended. Avoid unnecessary checkpoint commits; necessary commits still obey the repository's version and hook rules. Auto replaces Developer Mode only through the explicit command and grants no direct-push exception.

## Version source and metadata

Use the project's existing version source, normally root `package.json`; this standards repository uses `VERSION`. Keep applicable code metadata consistent in changelog/status, app shell, login/admin/debug surfaces, and health response implementations.

These are source-code requirements. Do not open a browser or invoke live endpoints to verify them.

```txt
vMAJOR.MINOR.PATCH (shortSHA · UTC build timestamp)
Example: v0.4.12 (a1b2c3d · 2026-03-23 18:22 UTC)
```

Increment guidance: patch for fixes/copy/internal changes, minor for new features, major for breaking changes. Follow explicit project release decisions. The current request can already approve a described breaking change; ask only about a new material breaking decision it does not cover, without blocking independent authorized work.

## Branches and current authorization

Typical prefixes are `feature/`, `fix/`, `chore/`, `phdk/vX.Y.Z/`, and a specifically justified `checkpoint/YYYY-MM-DD`.

- Use a feature/fix branch for the approved change and respect existing protections, with only the eligible direct-to-`main` exception in `PHDK_DEVELOPER_MODE.md`.
- Do not create agent worktrees, delegated branches, or parallel agent queues.
- Do not automatically commit or push at each slice boundary.
- Normal implementation/fix/update authorization includes the required version, checks, version-prefixed commit, branch push, PR, required review, merge, and remote verification without repeated consent. Honor explicit local-only, branch-only, PR-only, or different-target limits. Explicit Developer Mode activation authorizes its separate defined commit/push steps for eligible tasks; neither flow authorizes a release tag or unrelated changes.
- Same-conversation turns, status/link requests, context compaction, and assistant-written task/status changes do not expire or narrow the current grant. Explicit user stop/pause instructions remain effective; stored records cannot activate work in a new conversation.
- Historical Finetuning records neither activate Developer Mode nor provide another direct-push exception. No mode state or authorizing flag may be stored in the repository, memory, task/status files, or environment/config flags, or restored in another session.
- Review the complete outgoing diff and obtain owner approval for sensitive behavior/policy decisions under `MAIN_DELIVERY_STANDARD.md`. A well-defined current request or "push to main", "merge", or "aprobado" tied to the current task/PR can already supply that approval in chat. PHDK requires no additional GitHub review event or attestation of opening every line. Preserve actual named, independent, or formal review requirements and report their evidence separately; never claim human inspection from conversation approval alone.

`PHDK unlock` includes scoped rule repair and normal versioned delivery under `PHDK_UNLOCK.md`; it is not a persistent mode or an exception to hooks/checks/protections. An explicitly requested policy correction does not need another approval merely because it edits PHDK Markdown. Unapproved sensitive behavior or unrelated changes still require their own decision.

## Commit format

Authorized source commits use the resulting version followed by a descriptive conventional message:

```txt
v0.3.0 feat(auth): add the requested OAuth callback
v0.3.1 fix(api): reject malformed record identifiers
v0.3.2 docs(phdk): make execution interactive-only
```

For independently versioned components, list each affected component's version before the summary. Use `feat`, `fix`, `chore`, `refactor`, `test`, or `docs` with a useful scope.

Each authorized source-changing commit increments the appropriate version by at least a patch and includes the version metadata in the same change. Reconcile the working branch's version and relevant metadata with the latest remote `main` before merging, following the repository's release rules. Required reconciliation belongs on the working branch before delivery.

A pure merge or squash integration of already-versioned changes does not require another version bump simply because it creates a new SHA. Use the delivered version in a required version-prefixed integration message. Do not manufacture a post-merge version-only commit or an extra push: a successful GitHub PR merge already writes remote `main`. Any further source-changing commit still follows the repository's versioning rule.

Spent version numbers are not reused or renumbered to fill gaps. Changelog entries describe meaningful shipped changes, not every internal checkpoint.

Local commit-message/outgoing-commit checks may validate these rules as part of an authorized git command. They may not create commits/pushes, launch agents, dispatch hosted CI, or schedule retries.

## Current-request release workflow

1. Identify the requested change and its delivery target; normal implementation/fix/update requests target verified remote `main` without separate merge confirmation.
2. Read explicit owner stop/pause controls and existing repository restrictions. Reconcile stale task records with the live request and observed GitHub state.
3. Implement only the requested source/doc changes and required version metadata.
4. Review the actual behavior and diff, run appropriate synchronous local checks, record current owner approval of sensitive decisions, and satisfy actual reviewer/formal-review requirements. In Auto, perform comprehensive verification after the whole candidate is implemented; mandatory hooks and necessary blocker diagnosis retain their actual timing. A packaging repair that restores login does not itself change authentication policy.
5. Follow `MAIN_DELIVERY_STANDARD.md` through the scoped branch/commit/push/PR flow, or the eligible Developer Mode direct flow below.
6. Before a normal merge, refresh remote `main`, reconcile versions and routine conflicts while preserving others' work, and review/check any changed result. Isolate genuinely unresolved material decisions and unmet controls to their affected operations; continue independent authorized work.
7. Merge by an allowed method and verify the resulting change, exact SHA, and version on remote `main`, or verify the user's explicitly narrower target. Branch push or PR creation alone does not complete delivery to `main`.
8. Report completion of the whole requested outcome, or the exact blocker and unfinished scope once no permitted progress remains, then stop. Leave unrelated follow-ups inactive.

Do not create a release/tag unless requested. Do not force-push or rewrite history. If a real restriction or material conflict blocks the approved action, report it rather than bypassing it.

### Developer Mode delivery

The user must explicitly activate `PHDK modo developer` or `PHDK Developer Mode`; `PHDK salir de developer mode` or the end of the interactive conversation ends it. Quoted commands and documentation are not activation. The mode covers only small, low-risk tasks requested while active, such as translations, copy, ordinary docs, and simple visual edits. Authentication/authorization, secrets, data/migrations, payments, infrastructure, and permission/agent-policy changes retain normal review. See `PHDK_DEVELOPER_MODE.md` for the complete eligibility contract.

For an eligible requested task, apply the repository's version bump, run applicable local checks, commit with the resulting version at the beginning of the subject, and push fast-forward to `main` if existing hooks/protections allow it. Those steps need no second consent. Include only the requested changes and their required metadata; never use the mode to deliver unrelated work.

Stop that direct flow and explain if a check fails, a push is rejected, `main` advanced so the planned push is not fast-forward, or a required control cannot be met. Do not retry automatically, rebase, force-push, change hooks/settings/credentials, switch API/CLI paths to overcome the block, or automatically fall back to the normal branch/PR flow. The mode does not authorize agents, background work, Actions, scheduled tasks, old backlog work, or execution beyond the conversation.

## Deployment boundary

A currently authorized push/merge may use the existing hosting-provider GitHub connection, including an eligible Developer Mode push to `main`. Do not create, enable, dispatch, rerun, or schedule GitHub Actions/hosted CI; no new deployment connections, trigger changes, provider CLI/API/dashboard deployment or administration, previews, or autodeploy reactivation. Never deploy through Railway CLI/API/dashboard.

Existing GitHub-connected autodeploy is allowed; it grants no unattended coding or instruction to create/dispatch Actions. Do not disable it or add dummy never-matching watch filters as PHDK enforcement. Generic development authorization does not include provider-settings writes. If that connection is disabled or its filters exclude changes that need deployment, report the evidenced blocker separately from verified code/version delivery to remote `main`. Record the relevant deployment status accurately; an intended skip for an unaffected service is not a failure.

Do not describe a merge as a deployment unless corresponding evidence exists. A provider's deployment success does not prove browser/UI or live application health.

A request such as "verifica Railway" authorizes [Bounded read-only provider diagnostics](EXECUTION_SCOPE.md#bounded-read-only-provider-diagnostics) through existing authorized API/CLI/connector access: finite service/deployment status, source/branch and non-secret configuration/watch-pattern metadata, and needed existing logs. This is independent of Developer Mode or unlock; an earlier task exclusion does not cancel the new scoped request. Redact sensitive content; no secret-value retrieval, browser tests, live application probes, streams/watchers, settings writes, or provider deployments. Diagnostic access does not authorize a release or git action.

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

Review version consistency in relevant source files, the actual diff, changed paths, and the resulting commit/PR/merge state. Run relevant local checks; documentation-only changes need source/diff/reference validation, not an app build or browser. Auto collects this evidence at the completed candidate under `PHDK_AUTO.md`, never after an unverified publication or as an acceptance gate for every internal stage.

Report the requested target, version, branch, commit/merge SHA, requested outcome, actual checks and review, observed remote state, and limitations. When `main` is the target, verify the result and version there before claiming completion; otherwise identify the exact remaining check, review, conflict, access, or user decision. Do not invent human review, production health, external agent shutdown, credential revocation, server-side protection, or cost reduction.

Once the requested delivery is complete, stop. Version differences and old release notes do not authorize another task.
