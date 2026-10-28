# VERSIONING.md

## Product document versions are independent (v2.73.0)

Per [PHDK_DOCUMENTATION_STANDARD.md](PHDK_DOCUMENTATION_STANDARD.md), `docs/<category>/<topic>.vN.md` is a **document baseline revision**, not PHDK `VERSION`, product SemVer, Git SHA or a reason to publish every change as a separate milestone. `docs/INDEX.md` chooses the active baseline by metadata, not highest filename. Minor copy corrections stay in Git history; materially revised intent/plan/decision/visual baselines get a new document version. Actual product release and delivery decisions still follow this file's existing SemVer/milestone rules.


## Purpose and authority

Keep authorized changes, commits, releases, and built artifacts traceable. `EXECUTION_SCOPE.md` governs all versioning and delivery: active conversation and current request, no unattended/background work, GitHub Actions, or external administration. Bounded in-session delegation is allowed in any mode under `PHDK_INTELLIGENT_EXECUTION.md`; PMO separately governs portfolio workstreams. `PHDK_AUTO.md` defines continuous development through one identified goal.

Versioning follows the current request's delivery scope. A request to implement, fix, or update repository code or documentation includes the normal versioned branch/PR delivery to verified remote `main` in `MAIN_DELIVERY_STANDARD.md`, unless the user specifies a narrower scope or the user/repository specifies another target. An audit produces a report, not a version bump; a bare `PHDK upgrade` retains its limited scope in `EXECUTION_SCOPE.md`. Versioning alone does not authorize a new task or a release tag.

`PHDK_DEVELOPER_MODE.md` defines a separate, explicit conversational authorization for the version/check/commit/fast-forward-push steps of eligible small tasks requested while the mode is active. The versioning checklist does not activate that mode.

With explicit `PHDK auto` or `PHDK auto force`, Plan divides the authorized goal into coherent value milestones under `PHDK_PROJECT_MANAGEMENT_STANDARD.md`. Complete and technically verify the internal slices/workstreams that form one milestone, then reconcile its version and deliver that coherent milestone through the normal branch/PR/merge-to-`main` route before continuing from refreshed `main`. Do not bump, release, commit or push merely because a lifecycle stage, task, slice or worker ended; **a completed milestone is the publication boundary**. Do not postpone an already-authorized completed milestone until the whole product is finished. Record IMPLEMENTED, PUBLISHED, DEPLOYED and ACCEPTED independently. Avoid unnecessary checkpoint commits between milestones. Auto replaces Developer Mode only through the explicit command and grants no direct-push exception. In FORCE, `PHDK_AUTO_CONTINUITY.md` takes precedence over PHDK-only human-review wording: skip those gates without investigating them, perform technical diff review/checks and deliver. After a real rejection, report, diagnose, repair, revalidate and retry delivery while preserving the mandate.

## Version source and metadata

Use the project's existing version source, normally root `package.json`; this standards repository uses `VERSION`. Keep the source version consistent across changelog/status, app shell, login/admin and health-response metadata. For deployed HTTP products implement `PHDK_DEPLOYMENT_VERSION_STANDARD.md`: the public `GET /health/version` returns the **application version**, vendored `phdkVersion`, full deployed `commitSha` and immutable `builtAt` (unknowns are `null`). Commit SHA and build timestamp stay in diagnostic metadata and responses, never in the visible version/action widget. Exact widget sizing is defined in `DEBUG_DIAGNOSTICS_STANDARD.md`.

These are source-code requirements, with **one narrow post-release readback exception**: a bounded `GET /health/version` under `EXECUTION_SCOPE.md` and `PHDK_DEPLOYMENT_VERSION_STANDARD.md` may confirm the deployed revision. Do not open a browser or invoke other live endpoints for ordinary development verification.

```txt
VISIBLE UI (all public/login/app/admin surfaces): `vMAJOR.MINOR.PATCH` ONLY
Example visible: `v0.4.12`

DIAGNOSTICS REPORT (copied text, not visible beside the version): version, short Git SHA and UTC build timestamp as separate fields. Never display SHA or build date in the version widget.
```

Increment guidance: patch for fixes/copy/internal changes, minor for new features, major for breaking changes. Follow explicit project release decisions. The current request can already approve a described breaking change; ask only about a new material breaking decision it does not cover, without blocking independent authorized work.

## Post-merge local main and worktree reconciliation

Every published milestone in Auto/Force uses [PHDK_GIT_WORKSPACE_CLOSEOUT.md](PHDK_GIT_WORKSPACE_CLOSEOUT.md) **after** the remote PR/merge SHA has been verified and **before** any new local milestone branch. Synchronize local main with origin/main by safe fast-forward and verify SHA equality; retire only the integrated milestone branch/worktree with a clean and independently proven merge. Never do a second push from local main after a GitHub PR merge. Report local sync/cleanup, remote branch deletion and production deployment as separate results. Connector-only work has no local workspace and must say NOT_APPLICABLE_REMOTE_ONLY.

## One-time historical Git hygiene is not a source release

On the first explicitly initiated local Auto/Force run after adoption, PHDK_GIT_WORKSPACE_CLOSEOUT.md permits a bounded, evidence-backed audit of old branches and safe retirement of verified merged worktrees/heads; subsequent verified milestones retire their own unchanged remote heads as well. These **Git maintenance operations do not create new source commits, SemVer bumps or tags**. Never force-update a remote branch; the SHA lease applies solely to the deletion of an exact, already merged feature ref. Keep source publication, local main synchronization, branch retirement and Railway deployment independently verified. A plain PHDK upgrade remains non-destructive.

## Branches and current authorization

Typical prefixes are `feature/`, `fix/`, `chore/`, `phdk/vX.Y.Z/`, and a specifically justified `checkpoint/YYYY-MM-DD`.

- Use a feature/fix branch for the approved change and respect existing protections, with only the eligible direct-to-`main` exception in `PHDK_DEVELOPER_MODE.md`.
- Do not create uncontrolled agent worktrees, delegated branches, or parallel queues. Bounded in-session workers may use isolated branches/worktrees only when runtime-supported, within the current mandate and with documented ownership/dependencies under `PHDK_INTELLIGENT_EXECUTION.md`; PMO adds portfolio governance. Global version/changelog finalization remains centralized at integration.
- Do not automatically commit or push at each task/slice/stage boundary. Under Auto/Auto Force, do version and publish each completed `MILESTONE_PLAN.md` value milestone after its integration/acceptance gate.
- Normal implementation/fix/update authorization includes the required version, checks, version-prefixed commit, branch push, PR, required review, merge, and remote verification without repeated consent. Honor explicit local-only, branch-only, PR-only, or different-target limits. Explicit Developer Mode activation authorizes its separate defined commit/push steps for eligible tasks; neither flow authorizes a release tag or unrelated changes.
- Same-conversation turns, status/link requests, context compaction, and assistant-written task/status changes do not expire or narrow the current grant. Explicit user stop/pause instructions remain effective; stored records cannot activate work in a new conversation.
- Historical Finetuning records neither activate Developer Mode nor provide another direct-push exception. Never store or restore a standalone authorizing flag. Auto's factual mandate/checkpoint in `AUTO_STATE.json` is permitted under `PHDK_AUTO_CONTINUITY.md`; it records the user's actual instruction and cannot start work from files alone.
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


### Auto milestone version resolution

Plan records only the expected SemVer class for each milestone; it must not pre-reserve exact version numbers. At milestone completion, refresh remote `main`, determine the next unused version from the actual current version and the milestone behavior, update the project version/changelog consistently, and deliver that milestone. Multiple workstreams that form one milestone share one integrated milestone version. A pure lifecycle handoff, final UAT pass or final completion report does not create another version unless source changed after the last delivered milestone.

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
