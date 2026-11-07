# PHDK Git Workspace Closeout Standard

## Purpose and applicability

This is the **post-merge closeout** for every authorized value milestone, forced-upgrade standards publication, normal implementation delivery, and PMO integration performed from a local Git checkout. It extends MAIN_DELIVERY_STANDARD.md and PHDK_PROJECT_MANAGEMENT_STANDARD.md; it does not create a second merge, second push to main, background janitor, or authorization to delete unrelated work. PHDK auto / PHDK auto force **MUST** execute closeout after each successfully verified milestone publication and before starting the next milestone whenever a usable local Git workspace exists. Workers report their branch/worktree to the coordinator; the coordinator owns closeout. A narrower branch-only, PR-only or local-only request retains its target.

**Independent results:** PUBLISHED means verified remote SHA/version/content. LOCAL_MAIN is SYNCED, BLOCKED or NOT_APPLICABLE_REMOTE_ONLY. LOCAL_CLEANUP is CLEAN, RETAINED_WITH_REASON or NOT_APPLICABLE. REMOTE_BRANCH is RETAINED_BY_POLICY / ALREADY_ABSENT / NOT_CHECKED (read-only); its retention is never a cleanup-completion gate. DEPLOYED is independent. Failed local closeout does not reverse successful remote publication; it forbids claiming the owner's workspace is tidy. Resolve in-scope local drift before creating the next local branch/worktree, or report the blocker.

## Initial historical hygiene (first Auto/Force after adoption)

On the **first explicitly initiated PHDK auto or PHDK auto force** in a local checkout after adopting this revision, perform one bounded repository-specific historical reconciliation before creating new feature branches. A bare PHDK upgrade remains standards-sync/read-only and does **not** authorize deleting historic branches. Do not crawl other repositories or create jobs, schedules or GitHub Actions.

1. **Inventory without deletion.** Inspect live local worktrees, current/locked branches, local-versus-fetched main, and remote branch heads **read-only** using `scripts/phdk_git_history_cleanup.py` (vendored under `phdk-standards/scripts/`). Examine `.git/phdk/git-hygiene-state.json` and continue only unresolved **local** candidates. Never infer an old local branch is disposable merely because it is behind main.
2. **Verify each local candidate in GitHub.** Read merged PR details (repository, base, head SHA, merge SHA/date and other open PRs). Prove the merge SHA belongs to current origin/main and the **local** head equals the PR head. Historical merges must be at least 24 hours old. Retain unverified, protected, dirty, active, divergent and unmerged local branches/worktrees. A remote head advanced after merge is always preserved and does not alone prevent retirement of the unchanged verified local head.
3. **Apply only evidence-backed LOCAL cleanup.** Feed fresh (within 30 minutes) PR observations into the helper's evidence JSON and reuse `phdk_git_closeout.py` for safe local main fast-forward and local branch/worktree retirement. **Never issue a Git push, remote deletion API call or GitHub settings change for cleanup.** Remote refs are read-only evidence. A specific owner request to delete a named remote branch is a separate task, never an implicit Auto/Force/Upgrade/merge side effect.
4. **Evidence and lifetime.** Record inspected/eligible/removed/retained **local** counts, local SHA equality and REMOTE_BRANCH=RETAINED_BY_POLICY / ALREADY_ABSENT / NOT_CHECKED in the lifecycle handoff and `.git/phdk/git-hygiene-state.json`. An exhaustive completed local inventory may be marked complete even with merged remote branches remaining. Retry only unresolved local candidates in a later foreground Auto; no automatic background/remote cleanup.
5. **No local access or no PR metadata.** Without local filesystem access report `NOT_APPLICABLE_REMOTE_ONLY` for local cleanup, never claim the owner's disk changed, and never delete remote GitHub branches. Remote retention is not a blocker. Never ask for passwords or change account/hosting settings.

### Machine-readable GitHub evidence for bounded LOCAL retirement

The agent constructs JSON from **fresh, actual GitHub PR records**, never by inventing a merged state. The helper checks identity, exact SHA, target ancestry and timestamps but cannot authenticate a caller-supplied PR record independently. Remote heads are read-only evidence, **never** deletion candidates under this helper. Save proof under the private Git common directory; markers do not authorize a later session.

```json
{
  "schema_version": 1,
  "repository": "owner/repo",
  "target": "main",
  "remote": "origin",
  "scope": "historical",
  "observed_at_utc": "2026-10-27T23:00:00Z",
  "inventory_exhaustive": false,
  "out_of_scope_count": 0,
  "candidates": [
    {
      "branch": "feature/finished-work",
      "pr_url": "https://github.com/owner/repo/pull/123",
      "state": "closed",
      "merged": true,
      "base": "main",
      "head": "feature/finished-work",
      "head_sha": "FULL_40_HEX_PR_HEAD_SHA",
      "merge_sha": "FULL_40_HEX_MERGE_SHA",
      "merged_at": "2026-10-20T18:00:00Z",
      "open_pr_count": 0
    }
  ]
}
```

The SHAs shown are placeholders, not evidence. For just-merged milestones use `scope: "milestone"` with observed records and no 24-hour age gate. Inventory then apply **local-only** cleanup from the relevant checkout:

```text
python phdk-standards/scripts/phdk_git_history_cleanup.py --record-inventory
python phdk-standards/scripts/phdk_git_history_cleanup.py --apply --evidence .git/phdk/verified-pr-evidence.json
```

In canonical PHDK source checkout use `scripts/` rather than `phdk-standards/scripts/`. Neither command deletes any GitHub branch. No blanket ref pruning, guessed merge SHA or uncontrolled directory removal. Keep the audit bounded to the authorized repository.

## Remote GitHub branch preservation (all automatic modes)

After **each verified milestone PR merge**, close only verified-integrated **local** branches/worktrees and report the remote feature head as `RETAINED_BY_POLICY` when present (or `ALREADY_ABSENT`). **No PHDK Auto/Force, Upgrade, PMO, Check or historical cleanup may delete a GitHub remote branch automatically**, even if already merged. A specific, current owner request naming the remote branch can authorize a separate reviewed deletion under normal controls. General authorization to implement, publish, merge, FORCE or tidy local work never supplies that approval. GitHub's independent delete-on-merge repository setting is not changed by this standard.

## Ordered mandatory closeout

1. **Confirm publication first.** Obtain a real merged PR, base branch, head branch, head SHA, merge/result SHA, and verified remote target SHA/version/content (normally origin/main). Neither open/closed-unmerged PRs, Railway deployments nor feature-branch pushes are publication proof. Squash and rebase merges need not preserve the original branch SHA in main; use GitHub's merged result SHA.
2. **Identify owned workspaces.** Read git status (tracked and untracked), git worktree list --porcelain, local branches and upstream, and identify milestone-owned worktrees/heads. Inspect **ignored** entries before deleting a worktree, including potential secrets and data. Do not infer ownership solely from branch names or delete other agents' work.
3. **Fetch and fast-forward local main.** With verified remote main and a clean appropriate main worktree, fetch the target and update local main via git merge --ff-only origin/main, or equivalent safe fast-forward. If main is checked out in another worktree, operate *in that worktree*, never rewrite an active ref. If main is not checked out, switch a clean appropriate worktree to main first. Verify local main SHA equals fresh origin/main and ahead/behind are both zero. **The remote PR merge already updated origin/main: do not redundantly merge/push local main to origin/main.**
4. **Retire only the proven-integrated worktree and branch.** Confirm the branch tip is a Git ancestor of main, OR obtain independent evidence of the merged GitHub PR's precise head SHA and resulting merge SHA (squash/rebase). Check the local branch tip matches that PR head before deleting non-ancestor history. Remove only clean, unlocked, inactive linked worktrees via ordinary git worktree remove (never --force), then retire only the verified local branch. If the currently executing worktree still holds that branch, safely switch off it or perform closeout from the main worktree. Refuse deletion for dirty tracked files, untracked files, unknown ignored content, locked worktrees, exclusive/unmerged commits, a changed head, or uncertain ownership. Recognized regenerable ignored files may be disposed only after confirming their path/content classification; never treat .env, data, secrets or unspecified files as disposable.
5. **Verify and report.** Re-read local and fetched remote main SHA, branch/worktree presence and any blockers. Record LOCAL_MAIN, LOCAL_CLEANUP, branch/worktree identities and evidence in the milestone delivery handoff, DELIVERY_REPORT.md and applicable AUTO_STATE.json. Preserve unresolved branches/worktrees as explicit active handoff commitments; do not start another branch for the same unfinished delivery. With only a GitHub connector and no local filesystem, report NOT_APPLICABLE_REMOTE_ONLY, never that a user's computer was synchronized.
6. **Remote feature branches and Railway.** Read remote heads only to report `RETAINED_BY_POLICY`, `ALREADY_ABSENT` or `NOT_CHECKED`. **Never delete remote refs as part of cleanup.** Preserve advanced remote heads. Railway autodeploy/branch evidence is separate; never change GitHub or Railway settings as a cleanup side effect.

## Windows closeout and force-owned main recovery (v2.92.1)

Before ordinary linked-worktree removal, inspect tracked, untracked and ignored data, bounded filesystem entries, symlinks/junctions and Windows path lengths. Recognized cache/dependency folders may be considered disposable only after all contained data is classified and the explicit --allow-generated-ignored option is used; any secret, unknown item, uncertain ownership, long path or inspection failure retains the worktree. Never enable force deletion or change Git path settings to bypass a blocker.

After a rejected *or successful* Git worktree removal, reread Git registration, physical directory and branch SHA separately. PARTIAL_CLOSEOUT means Git altered some state but left residual data. Do not delete that branch or the remaining directory blindly; preserve exact evidence and safe recovery instructions. Local cleanup status is independent from already-verified remote publication.

During exact Upgrade Force only, --reconcile-force-owned can back up and resolve dirty local main after validating the old and new manifest and any native managed marker. Original tracked files and diff are preserved under the private Git common directory (phdk/closeout-recovery). Refuse untracked/unknown or owner text outside markers. Fast-forward only by ordinary --ff-only and verify final local/remote SHA; no history rewrite, second main push or cleanup of unrelated work.

## Safe local closeout command

From the relevant local Git checkout, run a non-mutating inspection. In the canonical PHDK repository use scripts/phdk_git_closeout.py instead of the vendored phdk-standards/scripts path:

    python phdk-standards/scripts/phdk_git_closeout.py

After independently verifying the merged GitHub PR, use the actual **full** merge SHA and only the identified branch:

    python phdk-standards/scripts/phdk_git_closeout.py --apply --merged-sha <MERGED_40_CHAR_SHA> --branch <OWNED_BRANCH>

For a squash/rebase branch that is not an ancestor of main, add --pr-head-sha <VERIFIED_40_CHAR_PR_HEAD_SHA> only after checking the merged PR targets the expected branch and its head SHA matches. This is external evidence supplied by the agent; the helper **does not query or independently verify GitHub PR state**. Use --allow-generated-ignored only after examining ignored content and confirming it consists solely of the helper's recognized disposable build/dependency paths. Preserve worktree contents whenever uncertain.

The script never pushes, merges unmerged feature work, changes GitHub/Railway settings, runs garbage collection, deletes remote branches, deletes unrelated worktrees or launches product tests. Verified squash/rebase local branch retirement uses an exact expected-head compare-and-delete, not a forced branch deletion. --apply fetches, fast-forwards and attempts targeted safe local retirement; inspection uses the locally cached remote-tracking ref and can therefore be stale. Exit 0 indicates successful requested **local** closeout; exit 2 indicates main sync/verification blocked; exit 3 indicates main synced but selected cleanup retained. JSON evidence is not a substitute for independent GitHub/production verification.

## Disk-space and regression guidance

A branch ref alone generally occupies negligible disk. The one-time historical scan is not an instruction to run an automatic garbage-collection or mass-delete pass. Linked worktrees, separate clones and per-worktree ignored dependencies/build directories can consume substantial space. Merging does not itself free this space. Do not run broad git clean -fdx, git worktree prune, git gc --prune=now, forced deletion of unverified branches or removal of unknown paths. Measure actual reclaimed bytes before claiming a disk saving.

Author regression scenarios for clean merge, verified squash, dirty/ignored/locked worktrees, diverged main, missing/mismatched SHAs, concurrent branches, current worktree protection, and remote-only delivery. Run local static checks only under PHDK_PRODUCTION_VERIFICATION.md; local product/runtime tests remain excluded.
