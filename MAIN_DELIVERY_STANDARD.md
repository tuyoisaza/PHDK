# Main Delivery Standard

## Purpose and authority

Finish the user's current implementation request with the requested change integrated into remote `main`. `EXECUTION_SCOPE.md` governs authorization and exclusions; stricter owner instructions, existing hooks, review requirements, and access controls remain binding. This standard defines the normal branch/PR flow, independently of Developer Mode's narrow direct-main exception.

## The requested outcome includes delivery

A current request to implement, fix, or update repository code or documentation includes the necessary scoped branch, version bump, applicable local checks, version-prefixed commit, branch push, pull request, required review, merge, and verification on remote `main`. Do not require the user to repeat "merge and push to main" after the development work. Use another delivery target when the user or the repository explicitly specifies it; do not create or retarget a default branch merely to apply this standard.

Honor narrower requests such as inspect, audit, plan, edit locally, leave on a branch, or open a PR without merging. Their stated limit remains the deliverable. The exact `PHDK upgrade` command retains its synchronization-only contract unless the user also requests git delivery. No instruction here authorizes release tags, unrelated changes, a new task, or work after the active conversation ends.

An existing hosting connection may deploy automatically after the authorized update to `main`. PHDK's limits on autonomous coding, schedules, and Actions do not require disabling this GitHub-connected autodeploy or introducing dummy never-matching watch filters. Preserve valid service-specific watch paths. Report an observed disabled connection, a filter shown to exclude changes that need deployment, or an actual skipped/failed status for the relevant commit separately from code integration; an intended skip for an unaffected service is not a failure. Merge and deployment are separate facts; verify and report only the available evidence. Do not deploy or administer provider resources through a CLI/API/dashboard or change hosting/GitHub settings to finish delivery; a requested configuration intervention is a separate scope and cannot be inferred from a generic development request. The separately requested bounded read-only log exception in `EXECUTION_SCOPE.md` remains available.

## Keep current authorization and task records consistent

- Preserve the authorization and target of the same unfinished request across turns in the active conversation. A status question, request for a link, clarification, context compaction, checkpoint, or assistant-written task summary does not cancel that request or remove its delivery steps.
- `TASK.md`, `STATUS.md`, summaries, and managed instruction files record the user's decisions; they do not independently grant, withdraw, expire, or narrow authorization. Do not mark an authorized unfinished delivery inactive merely because coding is finished or a newer message asks about progress.
- A real user stop, pause, cancellation, narrower target, or newer incompatible instruction takes precedence. Preserve its scope and provenance. An actual technical or review blocker pauses execution without pretending the user withdrew authorization. Never erase an owner's real restriction by relabeling it stale.
- When records conflict, compare the actual user instructions, their scope, and current git/PR evidence. Correct an assistant-generated bookkeeping error within the authorized task. Ask only if a material owner decision remains ambiguous; do not ask for a second grant already present in the active conversation.
- Never embed temporary task state such as "TASK remains paused" in permanent agent/routing instructions. Keep dated task facts in tracking records and verify them before relying on them. An unchecked commit/push/merge box is not proof that the remote operation is still pending.
- In a new conversation, do not resume an old task or restore Developer Mode from records alone. A new current request can explicitly resume the named work, including its stated delivery target. This continuity rule permits no background, scheduled, or post-conversation execution.

## Review according to risk and existing requirements

Review the complete outgoing diff and the changes needed for integration. Ordinary in-scope changes use the assistant's source/diff review and applicable local checks; PHDK adds no universal human-review gate to them. Their normal path still uses a feature/fix branch and PR unless an explicitly active, eligible Developer Mode task uses its direct-main flow.

Require human review for authentication, authorization, roles or permissions, secrets, personal/sensitive data or data integrity, schema/migrations, payments, infrastructure, deployment configuration, and agent execution/authorization policy. Also require every review mandated by the project's owner, repository rules, or existing protections. Mixed or uncertain risk follows that reviewed path; do not split a sensitive change into small commits to avoid it.

Delivery authorization and actual human diff review are distinct. Never report that a person examined the diff without evidence. When required review is genuinely missing, prepare all otherwise permitted work, present the concrete PR/diff and reason, and report delivery awaiting that review. When the required review is satisfied and current delivery authorization remains valid, complete the merge without asking separately whether to perform the already-authorized delivery.

## Normal branch-to-main procedure

1. Identify the repository, remote, target, current task, owner instructions, review requirements, and local state. Inspect the relevant hooks, version scripts, package-manager requirements, and applicable gates early enough to disclose a delivery blocker before calling development complete. Preserve unrelated edits and other contributors' commits.
2. Start or continue the task's existing suitable feature/fix branch from a known target state. A new message or checkpoint does not require another branch for the same unfinished delivery. Keep the outgoing range limited to the approved task and necessary version metadata.
3. Implement the requested change. Run applicable synchronous local checks, with no browser tests, live probes, hosted CI dispatch, or provider operations. Source/diff/reference checks suffice for ordinary documentation work unless the repository has a stricter applicable requirement.
4. If a check fails, keep publication blocked while diagnosing it. Repair a clear, bounded defect within the approved scope and rerun affected checks. A failing baseline does not authorize unrelated repository-wide cleanup, workflow edits, new dependencies, or weaker gates. If scope, review, toolchain, or access prevents resolution, report the specific blocker and preserve the work.
5. Refresh the remote target before final integration. Resolve routine same-task integration conflicts when the intended result is clear, retaining other contributors' work and the requested behavior. Use the repository's allowed method without force-pushes or history rewriting. Material ambiguity or a sensitive decision requires the appropriate review/decision, not an arbitrary choice of one side.
6. Reconcile the final version and changelog on the working branch against the current target and the repository's version standard. Review the integration result, rerun the affected local checks, and obtain any review required for that result. A materially changed diff cannot reuse approval of a different diff.
7. Create the necessary scoped commit(s) with the resulting version at the start of each source-changing commit subject. Use existing hooks and required checks. Never disable a hook, ignore a failure, or choose an API/transport/credential to evade a control. If the current environment cannot satisfy an applicable mandatory gate, stop before publishing.
8. Push the working branch through the permitted path, open or update its PR, and complete the required review. A ban on direct pushes to `main` still permits the repository's authorized reviewed-PR route; it is not a prohibition on integrating through that route.
9. Recheck the requested scope, target/head revisions, checks, and review before merging through the allowed method. Handle a new target change within this same bounded normal flow and revalidate the resulting change; do not blindly retry a stale or rejected write. Never bypass a protection or pretend a rejected merge succeeded.
10. Verify the resulting commit/content and version on the remote target. Accommodate the repository's merge or squash method rather than assuming a feature-branch SHA must appear unchanged in `main`. Report the PR, resulting remote SHA/version, actual checks, and delivery state; then stop at the requested outcome.

## Version once for each required source change, not again for integration

Use the repository's actual version source, including `VERSION` where applicable. Account for existing bump hooks so they do not produce a duplicate bump. Additional source-changing commits follow the repository standard; do not promise a single version increment for an arbitrarily long task.

A merge or squash record that only integrates already-versioned changes does not require another version bump. Reconcile a version collision or changed source before integration, without reusing spent versions. Do not manufacture a post-merge version-only commit or empty commit to make a completed task look released.

A GitHub PR merge already updates remote `main`. After that operation, read back the resulting state; do not perform a redundant local merge and second push to `main`. When a repository explicitly permits local integration instead, only its required ordinary fast-forward push publishes that local result, with all controls intact.

## Completion and blocked delivery

For a request targeting `main`, local implementation, a versioned commit, a pushed feature branch, and an open PR are intermediate states. Mark the delivery complete only after verifying the requested change and consistent version on remote `main`.

When blocked, state the unfinished delivery step, the exact failed check/conflict/review/access requirement, what was actually committed or pushed, and the concrete next decision. Keep it part of the same request; do not call it an optional future task or rewrite the user's permission as inactive. Do not create a job to resume later.

Keep task records and final reporting honest. A record written before publication is a dated checkpoint; compare it with live git/PR evidence before claiming an operation remains pending or repeating it. Do not create a second release solely to stamp a post-merge checklist. A requested application URL should be an observed appropriate URL with the known delivery state; a local source-file link is not evidence of a deployed change. Missing deployment evidence is reported as such, without browser tests or provider writes.

## Developer Mode remains a separate direct-main flow

`PHDK_DEVELOPER_MODE.md` still requires explicit activation, an eligible small low-risk request, and the active conversation. Its failed-check, rejected/non-fast-forward push, and unmet-control conditions stop the direct flow immediately. The normal repair/integration steps above do not authorize automatic repair, rebase, merge, retry, or switching delivery paths to get around that stop. Report the blocker and wait for the user's next instruction.
