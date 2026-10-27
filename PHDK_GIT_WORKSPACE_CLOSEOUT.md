# PHDK Git Workspace Closeout Standard

## Purpose and applicability

This is the **post-merge closeout** for every authorized value milestone, normal implementation delivery, and PMO integration performed from a local Git checkout. It extends MAIN_DELIVERY_STANDARD.md and PHDK_PROJECT_MANAGEMENT_STANDARD.md; it does not create a second merge, second push to main, background janitor, or authorization to delete unrelated work. PHDK auto / PHDK auto force **MUST** execute closeout after each successfully verified milestone publication and before starting the next milestone whenever a usable local Git workspace exists. Workers report their branch/worktree to the coordinator; the coordinator owns closeout. A narrower branch-only, PR-only or local-only request retains its target.

**Independent results:** PUBLISHED means verified remote SHA/version/content. LOCAL_MAIN is SYNCED, BLOCKED or NOT_APPLICABLE_REMOTE_ONLY. LOCAL_CLEANUP is CLEAN, RETAINED_WITH_REASON or NOT_APPLICABLE. REMOTE_BRANCH and DEPLOYED are independent. Failed local closeout does not reverse successful remote publication; it forbids claiming the owner's workspace is tidy. Resolve in-scope local drift before creating the next branch/worktree, or record the precise blocker.

## Initial historical hygiene (first Auto/Force after adoption)

On the **first explicitly initiated PHDK auto or PHDK auto force** in a local checkout after adopting this revision, perform one bounded repository-specific historical reconciliation before creating new feature branches. A bare PHDK upgrade remains standards-sync/read-only and does **not** authorize deleting historic branches. Do not crawl other repositories or create jobs, schedules or GitHub Actions.

1. **Inventory without deletion.** Inspect live local worktrees, current/locked branches, local-versus-fetched main, and remote branch heads using `scripts/phdk_git_history_cleanup.py` (vendored path under `phdk-standards/scripts/`). Examine the existing `.git/phdk/git-hygiene-state.json` if present, distinguish a previously completed historical pass from pending candidates, and continue only the bounded unresolved work. Never infer that an old branch is disposable just because it is behind main or not checked out.
2. **Verify every candidate in GitHub.** Read merged PR details including exact repository, base, head name/SHA, merge SHA, merged_at, and the absence of other open PRs for the same branch. Require proof that the merge SHA is in current origin/main and the live remote head still matches the PR head. For historical cleanup, the merge must be at least 24 hours old; more recent branches follow the current-milestone workflow. A retained branch without a verified PR is `RETAINED_UNVERIFIED`, not a cleanup failure that justifies deleting it. Do not remove default/protected/release/staging branches, branches with active workers or open PRs, branches that have advanced after merge, or any branch with unmerged/dirty/unknown ignored work.
3. **Apply only evidence-backed safe cleanup.** Feed fresh (within 30 minutes) GitHub PR observations into the helper's JSON evidence file. Reuse `phdk_git_closeout.py` for safe local main fast-forward and local branch/worktree retirement. When a remote feature branch still exists, perform a **deletion-only SHA-lease guarded push** for that exact branch and head, then check remote absence. This is a conditional deletion, **not** a force update of any branch. If actual server controls or tools reject it, retain the branch and report the observed error; never use an admin override or modify GitHub settings to bypass enforcement.
4. **Evidence and lifetime.** Record inspected/eligible/removed/retained counts, branch-level reasons, actual local SHA equality and independent remote deletion status in the existing lifecycle handoff plus local `.git/phdk/git-hygiene-state.json` (not a source commit). Only mark an entire historical inventory complete when it was exhaustive and no unresolved in-scope candidate remains. Bounded batches are not proof that every old branch was reviewed. A pending marker may be revisited in a later foreground Auto, but no automatic background retries occur. Historical cleanup is local-repository hygiene, not a new product milestone or extra SemVer bump.
5. **No local access or no PR metadata.** If the executing agent has only a GitHub connector and no filesystem, record `NOT_APPLICABLE_REMOTE_ONLY` for local cleanup; it cannot claim to clean the owner's computer. If it lacks a safe remote deletion capability, record `REMOTE_BRANCH_RETAINED_TOOL_UNAVAILABLE`, not DONE. Never ask for passwords or silently change account/hosting settings.

### Machine-readable GitHub evidence for bounded deletion

The agent constructs the JSON from **fresh, actual GitHub PR records**, never by inventing a merged state. The helper checks identity, exact SHA, target ancestry, timestamps, and live refs; it cannot independently authenticate the origin of a caller-supplied PR record. The inventory includes the local and remote branch-head names/SHAs so the agent can fetch associated PR evidence automatically. Save any temporary proof JSON under the repo's private Git common directory, not among source files. A saved audit marker never authorizes work in a new conversation.

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

The SHA strings shown are placeholders, not valid execution evidence. For the current just-merged milestone use `scope: "milestone"` and the actual observed records without the 24-hour historical age gate. Run the inventory first, then apply from the relevant local checkout with validated real evidence:

```text
python phdk-standards/scripts/phdk_git_history_cleanup.py --record-inventory
python phdk-standards/scripts/phdk_git_history_cleanup.py --apply --evidence .git/phdk/verified-pr-evidence.json
```

In canonical PHDK source checkout use `scripts/` rather than `phdk-standards/scripts/`. No fallback to blanket `git push --delete`, broad ref pruning, guessed merge SHA or uncontrolled directory removal. Keep the entire audit bounded to the current authorized repository.

## Continuous remote branch closeout

After **each verified milestone PR merge**, run the existing local closeout and then apply the evidence-backed remote-branch retirement for that **same milestone** using the helper above. This does not require enabling GitHub's `delete_branch_on_merge` setting. If that setting already removed the branch, record `REMOTE_BRANCH=ALREADY_ABSENT`. Check the live branch SHA and any open PRs immediately before a deletion-only leased push; do not delete a branch advanced since merge, even if its original PR was merged. Keep the cleanup result distinct from PUBLISHED, DEPLOYED and ACCEPTED. Do not postpone the next authorized milestone for an unrelated historical branch that is safely retained.

## Ordered mandatory closeout

1. **Confirm publication first.** Obtain a real merged PR, base branch, head branch, head SHA, merge/result SHA, and verified remote target SHA/version/content (normally origin/main). Neither open/closed-unmerged PRs, Railway deployments nor feature-branch pushes are publication proof. Squash and rebase merges need not preserve the original branch SHA in main; use GitHub's merged result SHA.
2. **Identify owned workspaces.** Read git status (tracked and untracked), git worktree list --porcelain, local branches and upstream, and identify milestone-owned worktrees/heads. Inspect **ignored** entries before deleting a worktree, including potential secrets and data. Do not infer ownership solely from branch names or delete other agents' work.
3. **Fetch and fast-forward local main.** With verified remote main and a clean appropriate main worktree, fetch the target and update local main via git merge --ff-only origin/main, or equivalent safe fast-forward. If main is checked out in another worktree, operate *in that worktree*, never rewrite an active ref. If main is not checked out, switch a clean appropriate worktree to main first. Verify local main SHA equals fresh origin/main and ahead/behind are both zero. **The remote PR merge already updated origin/main: do not redundantly merge/push local main to origin/main.**
4. **Retire only the proven-integrated worktree and branch.** Confirm the branch tip is a Git ancestor of main, OR obtain independent evidence of the merged GitHub PR's precise head SHA and resulting merge SHA (squash/rebase). Check the local branch tip matches that PR head before deleting non-ancestor history. Remove only clean, unlocked, inactive linked worktrees via ordinary git worktree remove (never --force), then retire only the verified local branch. If the currently executing worktree still holds that branch, safely switch off it or perform closeout from the main worktree. Refuse deletion for dirty tracked files, untracked files, unknown ignored content, locked worktrees, exclusive/unmerged commits, a changed head, or uncertain ownership. Recognized regenerable ignored files may be disposed only after confirming their path/content classification; never treat .env, data, secrets or unspecified files as disposable.
5. **Verify and report.** Re-read local and fetched remote main SHA, branch/worktree presence and any blockers. Record LOCAL_MAIN, LOCAL_CLEANUP, branch/worktree identities and evidence in the milestone delivery handoff, DELIVERY_REPORT.md and applicable AUTO_STATE.json. Preserve unresolved branches/worktrees as explicit active handoff commitments; do not start another branch for the same unfinished delivery. With only a GitHub connector and no local filesystem, report NOT_APPLICABLE_REMOTE_ONLY, never that a user's computer was synchronized.
6. **Remote feature branches and Railway.** Use the evidence-backed continuous remote branch closeout above. Delete only the exact unchanged merged milestone remote head with a deletion-only SHA lease after verifying no open PR; otherwise report the retained reason. Never indiscriminately delete historic remote branches. Check whether existing Railway GitHub autodeploy targets the authorized production branch (normally main) via bounded permitted metadata when available, without changing provider settings or confusing deployment with source merge.

## Safe local closeout command

From the relevant local Git checkout, run a non-mutating inspection. In the canonical PHDK repository use scripts/phdk_git_closeout.py instead of the vendored phdk-standards/scripts path:

    python phdk-standards/scripts/phdk_git_closeout.py

After independently verifying the merged GitHub PR, use the actual **full** merge SHA and only the identified branch:

    python phdk-standards/scripts/phdk_git_closeout.py --apply --merged-sha <MERGED_40_CHAR_SHA> --branch <OWNED_BRANCH>

For a squash/rebase branch that is not an ancestor of main, add --pr-head-sha <VERIFIED_40_CHAR_PR_HEAD_SHA> only after checking the merged PR targets the expected branch and its head SHA matches. This is external evidence supplied by the agent; the helper **does not query or independently verify GitHub PR state**. Use --allow-generated-ignored only after examining ignored content and confirming it consists solely of the helper's recognized disposable build/dependency paths. Preserve worktree contents whenever uncertain.

The script never pushes, merges unmerged feature work, changes GitHub/Railway settings, runs garbage collection, deletes remote branches, deletes unrelated worktrees or launches product tests. --apply fetches, fast-forwards and attempts targeted safe local retirement; inspection uses the locally cached remote-tracking ref and can therefore be stale. Exit 0 indicates successful requested **local** closeout; exit 2 indicates main sync/verification blocked; exit 3 indicates main synced but selected cleanup retained. JSON evidence is not a substitute for independent GitHub/production verification.

## Disk-space and regression guidance

A branch ref alone generally occupies negligible disk. The one-time historical scan is not an instruction to run an automatic garbage-collection or mass-delete pass. Linked worktrees, separate clones and per-worktree ignored dependencies/build directories can consume substantial space. Merging does not itself free this space. Do not run broad git clean -fdx, git worktree prune, git gc --prune=now, forced deletion of unverified branches or removal of unknown paths. Measure actual reclaimed bytes before claiming a disk saving.

Author regression scenarios for clean merge, verified squash, dirty/ignored/locked worktrees, diverged main, missing/mismatched SHAs, concurrent branches, current worktree protection, and remote-only delivery. Run local static checks only under PHDK_PRODUCTION_VERIFICATION.md; local product/runtime tests remain excluded.
