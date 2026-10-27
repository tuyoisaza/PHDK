# PHDK Git Workspace Closeout Standard

## Purpose and applicability

This is the **post-merge closeout** for every authorized value milestone, normal implementation delivery, and PMO integration performed from a local Git checkout. It extends MAIN_DELIVERY_STANDARD.md and PHDK_PROJECT_MANAGEMENT_STANDARD.md; it does not create a second merge, second push to main, background janitor, or authorization to delete unrelated work. PHDK auto / PHDK auto force **MUST** execute closeout after each successfully verified milestone publication and before starting the next milestone whenever a usable local Git workspace exists. Workers report their branch/worktree to the coordinator; the coordinator owns closeout. A narrower branch-only, PR-only or local-only request retains its target.

**Independent results:** PUBLISHED means verified remote SHA/version/content. LOCAL_MAIN is SYNCED, BLOCKED or NOT_APPLICABLE_REMOTE_ONLY. LOCAL_CLEANUP is CLEAN, RETAINED_WITH_REASON or NOT_APPLICABLE. REMOTE_BRANCH and DEPLOYED are independent. Failed local closeout does not reverse successful remote publication; it forbids claiming the owner's workspace is tidy. Resolve in-scope local drift before creating the next branch/worktree, or record the precise blocker.

## Ordered mandatory closeout

1. **Confirm publication first.** Obtain a real merged PR, base branch, head branch, head SHA, merge/result SHA, and verified remote target SHA/version/content (normally origin/main). Neither open/closed-unmerged PRs, Railway deployments nor feature-branch pushes are publication proof. Squash and rebase merges need not preserve the original branch SHA in main; use GitHub's merged result SHA.
2. **Identify owned workspaces.** Read git status (tracked and untracked), git worktree list --porcelain, local branches and upstream, and identify milestone-owned worktrees/heads. Inspect **ignored** entries before deleting a worktree, including potential secrets and data. Do not infer ownership solely from branch names or delete other agents' work.
3. **Fetch and fast-forward local main.** With verified remote main and a clean appropriate main worktree, fetch the target and update local main via git merge --ff-only origin/main, or equivalent safe fast-forward. If main is checked out in another worktree, operate *in that worktree*, never rewrite an active ref. If main is not checked out, switch a clean appropriate worktree to main first. Verify local main SHA equals fresh origin/main and ahead/behind are both zero. **The remote PR merge already updated origin/main: do not redundantly merge/push local main to origin/main.**
4. **Retire only the proven-integrated worktree and branch.** Confirm the branch tip is a Git ancestor of main, OR obtain independent evidence of the merged GitHub PR's precise head SHA and resulting merge SHA (squash/rebase). Check the local branch tip matches that PR head before deleting non-ancestor history. Remove only clean, unlocked, inactive linked worktrees via ordinary git worktree remove (never --force), then retire only the verified local branch. If the currently executing worktree still holds that branch, safely switch off it or perform closeout from the main worktree. Refuse deletion for dirty tracked files, untracked files, unknown ignored content, locked worktrees, exclusive/unmerged commits, a changed head, or uncertain ownership. Recognized regenerable ignored files may be disposed only after confirming their path/content classification; never treat .env, data, secrets or unspecified files as disposable.
5. **Verify and report.** Re-read local and fetched remote main SHA, branch/worktree presence and any blockers. Record LOCAL_MAIN, LOCAL_CLEANUP, branch/worktree identities and evidence in the milestone delivery handoff, DELIVERY_REPORT.md and applicable AUTO_STATE.json. Preserve unresolved branches/worktrees as explicit active handoff commitments; do not start another branch for the same unfinished delivery. With only a GitHub connector and no local filesystem, report NOT_APPLICABLE_REMOTE_ONLY, never that a user's computer was synchronized.
6. **Remote feature branches and Railway.** Read whether GitHub automatically deletes merged head branches. Without such a setting, delete only independently verified merged, unchanged, task-owned remote branches using an authorized safe mechanism if available; otherwise report REMOTE_BRANCH_RETAINED with the exact limitation. Never indiscriminately delete historic remote branches. Check whether existing Railway GitHub autodeploy targets the authorized production branch (normally main) via bounded permitted metadata when available, without changing provider settings or confusing deployment with source merge.

## Safe local closeout command

From the relevant local Git checkout, run a non-mutating inspection. In the canonical PHDK repository use scripts/phdk_git_closeout.py instead of the vendored phdk-standards/scripts path:

    python phdk-standards/scripts/phdk_git_closeout.py

After independently verifying the merged GitHub PR, use the actual **full** merge SHA and only the identified branch:

    python phdk-standards/scripts/phdk_git_closeout.py --apply --merged-sha <MERGED_40_CHAR_SHA> --branch <OWNED_BRANCH>

For a squash/rebase branch that is not an ancestor of main, add --pr-head-sha <VERIFIED_40_CHAR_PR_HEAD_SHA> only after checking the merged PR targets the expected branch and its head SHA matches. This is external evidence supplied by the agent; the helper **does not query or independently verify GitHub PR state**. Use --allow-generated-ignored only after examining ignored content and confirming it consists solely of the helper's recognized disposable build/dependency paths. Preserve worktree contents whenever uncertain.

The script never pushes, merges unmerged feature work, changes GitHub/Railway settings, runs garbage collection, deletes remote branches, deletes unrelated worktrees or launches product tests. --apply fetches, fast-forwards and attempts targeted safe local retirement; inspection uses the locally cached remote-tracking ref and can therefore be stale. Exit 0 indicates successful requested **local** closeout; exit 2 indicates main sync/verification blocked; exit 3 indicates main synced but selected cleanup retained. JSON evidence is not a substitute for independent GitHub/production verification.

## Disk-space and regression guidance

A branch ref alone generally occupies negligible disk. Linked worktrees, separate clones and per-worktree ignored dependencies/build directories can consume substantial space. Merging does not itself free this space. Do not run broad git clean -fdx, git worktree prune, git gc --prune=now, forced deletion of unverified branches or removal of unknown paths. Measure actual reclaimed bytes before claiming a disk saving.

Author regression scenarios for clean merge, verified squash, dirty/ignored/locked worktrees, diverged main, missing/mismatched SHAs, concurrent branches, current worktree protection, and remote-only delivery. Run local static checks only under PHDK_PRODUCTION_VERIFICATION.md; local product/runtime tests remain excluded.
