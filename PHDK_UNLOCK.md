# PHDK Unlock

## Command and scope

`PHDK unlock` is an explicit interactive instruction to inspect and repair PHDK-related blockers in the current repository. Recognize it case-insensitively after trimming whitespace; an accompanying task or PR identifies the target. It is an instruction to the assistant, not a shell executable, persistent mode, access credential, or background job. Quoted examples and stored files do not invoke it.

Explain the scope briefly: inspect the current blockers, reconcile documentary restrictions with the owner's current instructions, make bounded authorized repairs, and finish the already-authorized delivery through the permitted path. Existing hooks, checks, GitHub protections, access permissions, security controls, and provider-write boundaries remain effective.

The command itself authorizes this repository's scoped PHDK rule repair and its normal versioned branch/PR delivery under `MAIN_DELIVERY_STANDARD.md`; it does not need a separate approval for every file, commit, push, or merge. The owner is explicitly requesting this operating-policy correction. Do not impose a new PHDK-only approval loop merely because the correction edits policy Markdown. An actual required reviewer or unresolved sensitive decision still has to be satisfied.

Continue a product task only when it is identified and currently authorized in this conversation. With no such task, repair the PHDK rules and report readiness; do not select work from old tasks or merge every open PR. Honor narrower instructions such as audit-only, local-only, or PR-only. In a new conversation, files alone cannot restore an old mission. The command does not activate Developer Mode or authorize work after the conversation ends.

## Establish what is really blocking progress

Read the current user instructions before task snapshots. Inspect the existing sources that can affect this task, without creating instruction files for unused tools:

- Root `AGENTS.md`, `TASK.md`, `STATUS.md`, and existing Claude, Cursor, Copilot, Windsurf, or equivalent native instruction files.
- The installed PHDK version, manifest, managed blocks, owner prefaces, and active copied PHDK instructions or skill files inside this repository. Inspect stale supplemental copies as well as manifest destinations; old copies of `SKILL.md`, a README, or a handoff prompt can still issue conflicting instructions.
- Actual applicable hook scripts, version sources, package-manager/toolchain requirements, and the local worktree. Preserve unrelated or uncommitted work.
- Fresh GitHub target/head, PR, check, review, and merge evidence through available read operations. A saved pending checkbox is not evidence that a remote action remains pending.

For each blocker, identify its source, the operation it restricts, its task/conversation scope, and whether anything actually enforces it. Report file paths or concrete GitHub/check evidence, not a generic statement that PHDK forbids the action.

| Blocker | Authorized treatment |
|---|---|
| Assistant-written inactive/paused record conflicting with the live request | Reconcile it with the actual instructions and git evidence; preserve history and real owner stops. |
| PHDK or local instruction asking again for an already approved delivery | Record the current approval and target; remove the redundant documentary stop and continue the permitted delivery. |
| Owner explicitly requests removing local PHDK exceptions | Reconcile those documentary overrides across existing active instruction files. The current owner can replace an earlier owner-authored rule; do not preserve it as immutable merely because it is called an owner override. |
| Missing GitHub review event | Inspect whether a formal submission is actually required. Conversation approval can satisfy PHDK's owner-approval requirement; it cannot satisfy a server rule that requires a GitHub review. |
| Direct-main hook rejects a push | Keep the hook. Use the authorized branch/PR merge route if available; do not convert the rejection into a ban on every route to `main`. |
| Failed or unavailable mandatory check/toolchain | Diagnose it and make clear, bounded in-scope repairs when possible; otherwise report the exact unresolved gate. Never disable the hook or publish through another transport to avoid it. |
| Actual required review, access denial, protection, or material conflict | Preserve the control and prepare everything otherwise permitted. Report the exact remaining decision or access requirement. |
| Provider deployment blocker | Use only requested bounded read-only diagnostics. Record the actual state; do not reconfigure or redeploy through the provider under this command. |

Missing check-runs or an aggregate `pending` state with no posted statuses does not establish a running or failed check. A PR marked mergeable does not prove that all local checks, review requirements, or the eventual combined change are satisfied. An unreadable ruleset endpoint is unknown evidence, not proof of either a prohibition or permission.

If the current owner has authorized the identified PR, all known applicable gates are satisfied, and the existing ordinary merge route preserves server enforcement without a bypass, the assistant may attempt that merge even when rulesets cannot be enumerated. Report that visibility limit and stop at any actual rejection. Do not request repeated approval or new administrative access merely to enumerate rules; never use an override or alternate credential to evade a control.

## Apply the current owner's instructions

`MAIN_DELIVERY_STANDARD.md` defines approval evidence. A clear instruction such as "push to main", "merge", or "aprobado" for the identified current change is owner approval in the conversation. Do not require the owner to repeat it in a special phrase or press a GitHub review button unless an applicable control specifically requires that recorded action. Record approval truthfully; do not claim that a person inspected every line of the diff.

Classify the actual diff and behavior. A package-format fix that restores login is not automatically a change to authentication policy. PHDK synchronization and local-exception removal explicitly requested by the owner already have authorization for that described policy decision. Undisclosed sensitive behavior, unrelated changes, a new material risk, or another task cannot borrow that approval.

Use current instructions to resolve an older task-specific exclusion. For example, "no Railway CLI operations" in a previous code-sync task does not cancel a later request to check Railway through an available read-only connector. An active explicit owner stop remains binding within its scope; a targeted unlock request permits only the intervention it identifies.

Natural-language authorization remains valid without this command. Do not tell the user to run `PHDK unlock` merely to make an already clear approval or read-only diagnosis request count.

## Repair documentary conflicts without removing controls

1. Pin fresh canonical PHDK `main`, read its version and manifest, and compare it with the installed sources. Use `PHDK_UPGRADE.md` for synchronization mechanics, with this command's explicit rule-reconciliation and delivery scope. Do not downgrade a newer installation. If upstream is unavailable, do not invent a successful sync; complete any independent, verifiable task-record/rule repairs already authorized and report the unavailable portion.
2. Reconcile the actual blocker across all existing active native files and copied PHDK sources that govern the task. Remove obsolete PHDK gates, duplicate per-step approval demands, and temporary task state embedded as permanent instructions. When the owner requests removing local PHDK exceptions, remove those documentary exceptions within the requested scope. Preserve product requirements, unrelated guidance, real security requirements, and historical records.
3. Treat a modified file, project-specific customization, or unknown legacy copy as evidence to inspect, not permission to overwrite it blindly. Compare with the canonical source and retain unrelated local work. Archive old release history when a canonical replacement requires it; keep referenced history available.
4. Do not remove or weaken hook commands, required checks, branch protections, code-owner review rules, permissions, secrets handling, application auth, data validation, or infrastructure safeguards to make the audit appear clean. Their presence requires the appropriate permitted route or a concrete blocker report. Do not add skip flags, force-push, manufacture review/check results, change settings, or create a new credential/transport to evade them.
5. Update task evidence only as a dated record of the current owner instructions, corrected rules, remaining controls, and observed delivery state. Do not write an `unlocked=true` permission flag or delete prior approvals/stops/history to erase their provenance.

The instruction to repair PHDK documentation is not authorization to edit CI/workflow behavior, do unrelated repository-wide cleanup, install new product dependencies, or change provider settings. A separately explicit request for such a change retains its own scope and applicable controls.

## Finish the permitted delivery

Use a suitable existing task branch when possible. Reconcile version metadata against current remote `main`, review the outgoing diff, run applicable local checks and hooks, create a version-prefixed commit, publish the branch/PR, satisfy actual remaining controls, merge, and verify remote content and version. An approved PR merge already updates remote `main`; no extra push or ceremonial version bump is needed.

Inspect overlapping PRs before integration. Two PRs that independently use the same next version may contain different fixes and may conflict after the first merge. Do not assume a standards PR contains a product fix, merge unrelated PRs, overwrite another contributor's work, or reuse a released version. Resolve only the currently authorized integration and rerun affected checks.

Developer Mode keeps its own immediate stop conditions. Unlock is a new explicit diagnostic/rule-repair instruction, not an automatic retry of a rejected direct push. It does not waive the failed check or silently reactivate/switch a stopped product delivery; identify the permitted route for the currently requested follow-up.

For a requested Railway or other provider check, use `EXECUTION_SCOPE.md` — **Bounded read-only provider diagnostics**. Read only the service/deployment status, non-secret configuration metadata, or existing logs needed for that question, through existing authorized access with finite bounds. This permission is independent of Developer Mode and unlock. No browser tests, application probes, streams, settings writes, manual provider deployments, or recurring monitoring.

## Report and stop

Report the removed documentary blockers with their sources, the current approval/target, the actual version/commit/PR/main state, and any real remaining check/review/access/configuration blocker. Say which observations came from source review, local checks, GitHub, or a requested provider read. Do not call the repository fully unblocked or deployed when a required control or deployment remains unresolved.

Complete all currently authorized, feasible work before asking for a genuinely missing decision. Do not ask for permission already present in the conversation. Then stop; do not schedule another unlock, a later retry, or the next product task.
