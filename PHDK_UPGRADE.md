# PHDK_UPGRADE.md

## Purpose and command contract

**Adoption is not deletion:** installing or syncing PHDK never itself deletes historical Git branches/worktrees. The first subsequent explicitly initiated local PHDK auto/auto force (including the Auto Force phase of upgrade force) runs the bounded historical inventory and safe cleanup in PHDK_GIT_WORKSPACE_CLOSEOUT.md if it has local Git access and fresh PR evidence. A bare PHDK upgrade remains limited to its established sync/read-only review scope, and a remote-only agent must not claim the owner's local disk changed.


Synchronize an existing PHDK project to the current published standards, perform its bounded, read-only [Stack Security Review](PHDK_SECURE.md#stack-security-review), and, when eligible, publish the repository's current central status under [PHDK_REPOSITORY_STATUS.md](PHDK_REPOSITORY_STATUS.md) in response to the user's request in this conversation.

The canonical commands are:

- `PHDK upgrade` — conservative standards synchronization plus Stack Security Review, including a no-op sync.
- `PHDK upgrade force` — authoritative replacement of the PHDK-owned surface from canonical upstream `main`, even when that PHDK-owned surface has local edits, plus the same Stack Security Review, **then an immediate handoff into `PHDK auto force` in the same foreground session when the upgrade phase finishes without a real blocking boundary**.

Match both case-insensitively after trimming whitespace.

A bare `PHDK upgrade` authorizes only the conservative standards sync and bounded stack review now, without a second confirmation in the clean case. **`PHDK upgrade force` is a composite foreground command:** it authorizes discarding local modifications only inside the explicitly PHDK-owned surface defined below, completing the forced standards sync/review, and then continuing immediately under `PHDK auto force` for the current repository without another user command. The Auto Force phase carries its normal implementation, compatible security remediation, versioning and delivery authority and its normal exclusions. The composite command still does not authorize unrelated new features, background/future execution, UAT, provider administration, new infrastructure, spending, secrets/account operations, or bypassing real controls.

Follow `EXECUTION_SCOPE.md`: interactive-only, no GitHub Actions, no scheduled/background work, no browsers, live application probes, or provider writes. Bounded in-session delegation is permitted in any mode under `PHDK_INTELLIGENT_EXECUTION.md`, with PMO portfolio workstreams governed by `PHDK_PMO.md`. The review includes official advisory/support lookups and bounded reads of already connected provider metadata/logs for the identified project under EXECUTION_SCOPE.md. Record missing access as UNVERIFIED; no credentials, new access or live probes are implied. For bare `PHDK upgrade`, report and stop after the sync/review. For `PHDK upgrade force`, do **not** stop merely because the upgrade phase completed: perform the transition contract below and continue into Auto Force unless a real boundary prevents the handoff.

An upgrade copies the complete canonical manifest, including `PHDK_PREFLIGHT.md`, `SKILLS_REGISTRY.md`, `MAIN_DELIVERY_STANDARD.md`, `PHDK_UNLOCK.md`, `PHDK_AUTO.md`, `PHDK_PLAN.md`, `PHDK_PMO.md`, and the definition of `PHDK_DEVELOPER_MODE.md`; copying them activates no command or mode. Execution/authorization policy changes use the normal branch flow, even if Developer Mode is active. Review their actual diff and apply the approval rules in `MAIN_DELIVERY_STANDARD.md`: a well-defined owner request can already approve the policy decision, and a current instruction to deliver the identified update supplies delivery approval. Do not add a PHDK-only demand to open the diff or submit a GitHub review; actual formal review requirements remain binding.

When the owner explicitly includes this synchronization in an Auto development goal, use `PHDK_AUTO.md` for the whole goal's final verification and delivery cadence; copying standards or finishing a foundation does not complete that larger goal. A bare `PHDK upgrade` still authorizes only standards synchronization and read-only review, not product remediation or publication.

## PHDK-owned surface

Force mode may overwrite or remove only content whose ownership is unambiguous:

1. **Vendored standards destinations** under `phdk-standards/` that are listed by the current or fetched canonical `PHDK_MANIFEST.txt`.
2. **Obsolete vendored standards files** under `phdk-standards/` that were listed by the previously installed manifest but are absent from the new canonical manifest.
3. **Marked native managed blocks** delimited by exact `PHDK-MANAGED:START` / `PHDK-MANAGED:END` markers in the current tool's native instruction file.

Force mode must not overwrite:

- product/application source;
- project requirements, PRD, Capture artifacts, TASK/STATUS, intents, ADRs, changelog, README, or other project documentation merely because they mention PHDK;
- owner instructions outside a PHDK-managed marker block;
- hooks, workflow files, package manifests, provider settings, secrets, infrastructure, or repository settings;
- unknown files inside `phdk-standards/` that were never listed by an installed/canonical manifest.

A filename, directory name, example, or PHDK-related prose does not establish PHDK ownership by itself.

## Canonical upstream

```txt
https://github.com/tuyoisaza/PHDK.git
branch: main
version source: VERSION
```

Fetch the source rather than trusting cached version knowledge. A fix on an unmerged branch is not the published `main` version.

## Procedure

### 1. Identify the project and current request

Read the current user request and repository root. Confirm PHDK is present through `phdk-standards/`, an existing native rule-file reference, or project task/status documentation. Do not convert an unrelated project silently.

Read owner pause/stop instructions. A specifically requested standards sync may operate only within that narrow scope; it never reactivates an old task or broadly removes the pause.

### 2. Protect local work and owner controls

Inspect git status and determine whether the command is conservative or force mode.

For bare `PHDK upgrade`, stop before overwriting any uncommitted change in the PHDK-owned surface and report the conflicting paths.

For `PHDK upgrade force`, do **not** stop merely because PHDK-owned files/managed blocks are dirty. Record those paths, then replace that owned content from canonical upstream. This explicit command is the owner's authorization to discard local PHDK-standard edits in those owned locations. Preserve unrelated files and changes without staging, discarding, stashing, or rewriting them.

For a bare standards sync, preserve genuine owner controls wherever they are stored, including committed overrides; report an actual overwrite conflict. In force mode, owner text outside managed markers remains preserved exactly. Owner text placed inside a PHDK-managed marker block is replaced because that block is explicitly PHDK-owned; move durable project-specific owner rules outside the markers rather than preserving local edits inside canonical managed content. When the current owner also requests removing local PHDK exceptions or reconciling blockers, follow `PHDK_UNLOCK.md` to replace those documentary rules within that scope. Their owner-override label does not make them immutable. Preserve unrelated requirements and actual hooks, checks, security/access controls, and server protections.

Distinguish an actual current owner restriction from an older task-specific exclusion or assistant-written snapshot. Do not introduce permanent routing claims such as "TASK remains paused" or use a generated summary to revoke an already-authorized current delivery or a newer provider-read request. Verify instructions and git/PR facts when reconciling records. A bare sync does not silently remove a genuine owner rule, while an explicit current request to replace it supplies that documentary authority.

Do not create instruction files for tools that are not in use. Respect all existing repository access/review controls.

### 3. Obtain the current upstream

Fetch a fresh copy of canonical `main` into a temporary location outside the project, using the available repository tools. A shallow clone is one possible implementation:

```sh
git clone --depth 1 https://github.com/tuyoisaza/PHDK.git <temporary-directory>
```

If the fetch fails, make no project changes and report it. Do not register a retry job, scheduled sync, session-start hook, or background updater. Do not force-reset a dirty installed skill clone.

### 4. Compare versions and choose the working branch

Read upstream `VERSION` and project `phdk-standards/VERSION`. Do not downgrade a newer local version. Missing local version metadata identifies an older/pre-versioned installation, not authority for product changes.

When versions match, check the managed block and file hashes before saying already current. Still perform the Stack Security Review and refresh advisory/support evidence; the no-op only applies to standards copying. A newer local version is not downgraded and still receives the explicit-command review. Do not create a no-op commit.

For an authorized update on a default/protected branch, use a dedicated working branch such as `chore/phdk-upgrade-vX.Y.Z`; keep unrelated work untouched. Branch creation is part of the requested file-sync safety workflow, not permission to push it. In force mode inspect existing branches, PRs and `git worktree list --porcelain` first; reuse the suitable unfinished upgrade branch/worktree. Do not create another worktree for the same goal. Only use an isolated worktree when needed to protect unrelated work, and record ownership and a post-merge closeout obligation.

### 5. Synchronize the manifest

Read the fetched `PHDK_MANIFEST.txt`; never use a handwritten file list or cached model memory. Each non-comment line maps an upstream source to its destination inside `phdk-standards/`.

Validate that every source exists, destinations are unique and safe relative paths, and no path escapes the standards directory. Copy exactly those mappings, including `EXECUTION_SCOPE.md`, `PHDK_PREFLIGHT.md`, `SKILLS_REGISTRY.md`, `MAIN_DELIVERY_STANDARD.md`, `PHDK_UNLOCK.md`, `PHDK_AUTO.md`, `PHDK_PLAN.md`, `PHDK_PMO.md`, `PHDK_DEVELOPER_MODE.md`, and `PHDK_NATIVE_RULES.md`.

Remove an obsolete vendored file in conservative mode only when the previous manifest lists it, the new manifest omits it, it is clean, and removal respects the current owner's scope. In force mode, if the previous installed manifest proves the obsolete path was PHDK-owned, remove it even when locally modified; never remove an unknown extra file that was not manifest-owned. For pre-manifest projects, do not delete unknown extra files. An explicitly requested complete PHDK reconciliation or unlock also inspects active supplemental copies such as in-repository `SKILL.md`, README, and handoff instructions; compare their source and customizations before replacing stale generic PHDK content. Keep required history references and unrelated project files.

### 6. Refresh the current tool's managed block

Use the exact latest `PHDK_NATIVE_RULES.md` block with its `PHDK-MANAGED:START` and `PHDK-MANAGED:END` markers.

Known project-native locations include `CLAUDE.md`, `.cursor/rules/phdk.mdc`, `.windsurfrules`, and root `AGENTS.md`. Use only the current tool's applicable file.

- Replace only the marked managed block when it exists. In force mode replace that entire marked block byte-for-byte from canonical upstream, regardless of local edits inside the block.
- When the file exists without markers, append the block without deleting existing project instructions.
- When the applicable file is absent, create it only as part of the requested install/sync.
- Preserve genuine owner rules outside or inside the block during a bare sync. Apply a current explicit request to remove/reconcile documentary exceptions through `PHDK_UNLOCK.md`, across the existing active native files that could retain the blocker. Do not change enforced hooks, checks, or protections.

Do not install a plugin, spawn an assistant, register a hook that runs tasks, or create a scheduler. Loading a rule file never starts work.

### 7. Record continuity

When safe to edit without absorbing unrelated work, record old/new PHDK versions, canonical repository, upstream commit SHA, date, and any conflicts in `STATUS.md`. Otherwise put that information only in the report.

Do not make an old product task active or create a next mission merely to record the sync.

Record the sync as its own scoped change; do not cancel an unfinished currently authorized delivery because a status/link question or the sync produced a new tracking entry. Verify observed git/PR completion before repeating an operation listed as pending in an older checkpoint. A report can record post-merge evidence without manufacturing another version-only commit.

Do not store or restore Developer Mode activation in the continuity record. Historical evidence that the mode was used does not authorize a new conversation or task.

### 8. Force-mode verification

When `PHDK upgrade force` was used, additionally verify:

- every canonical manifest destination matches upstream byte-for-byte;
- every obsolete previously manifest-owned vendored file omitted by the new manifest is gone;
- every current native PHDK managed block matches upstream exactly;
- no file outside the PHDK-owned surface changed as part of the force replacement;
- every unrelated dirty file remains dirty with identical content;
- owner/native text outside managed markers remains byte-for-byte unchanged;
- the report lists which PHDK-owned local edits were discarded.

If any non-PHDK file changed, restore it before reporting success.

### 9. Verify using repository evidence

- Vendored `VERSION` matches the chosen upstream version.
- Every manifest destination exists and matches its mapped source byte-for-byte.
- The current native managed block matches the source block.
- Interactive-only rules are present; delegation is bounded to supported in-session workers under `PHDK_INTELLIGENT_EXECUTION.md`; PMO portfolio coordination remains separate; no-Actions, no-scheduling, and owner-control rules remain present.
- Developer Mode's explicit activation/exit, temporary lifetime, risk limits, and no-bypass rules match upstream; the upgrade itself did not activate it.
- Normal delivery's verified remote-target completion, risk-based review, authorization continuity, version reconciliation, and no-redundant-push rules match upstream; narrower requests and existing controls remain effective.
- Existing provider GitHub autodeploy and watch paths were not disabled or replaced with dummy filters as a PHDK restriction. Report observed deployment blockers/statuses separately without inferring permission for provider writes. Valid service-specific filters and intended skips for unaffected services are not configuration errors.
- `PHDK unlock` is routed without persistent activation, bypasses, or old-task resumption; approvals in the current conversation and actual formal review requirements are distinguished.
- `PHDK auto` and `PHDK salir de auto` are routed, with whole-goal continuous development, final integrated verification before publication, and actual controls preserved. No copied instruction, upgrade, or saved flag activated the mode.
- Bounded read-only provider diagnostics cover requested metadata/status/log reads without extra consent, provider writes, secret values, live probes, streams, or monitoring.
- Any documentary owner exceptions changed were explicitly included in the current request; actual enforced controls and unrelated edits were preserved.
- No product source changed except minimal version metadata when a currently authorized commit requires it.
- No agents, background tasks, workflow runs, browser sessions, live probes, or external configuration changes occurred.

Documentation-only verification is source/diff and reference checking. Do not run an application build or live check merely to satisfy an old checklist.

### 9a. Review the actual project stack

Perform the shared [Stack Security Review](PHDK_SECURE.md#stack-security-review) for all applicable packages/service roles, regardless of whether standards changed. Reuse the audit already performed for the same adoption/command only after validating its input hashes, deployment identifiers and advisory freshness. A standards-copy helper is not a security scanner; `scripts/phdk_update.py --trigger upgrade <project>` (add `--force-owned` only when the owner explicitly invoked force mode) reports pending work but does not perform the review, refresh native blocks, commit, push, open a PR or merge.

Inspect runtimes/package managers, direct and transitive dependencies, frameworks/native addons, builder/base-OS images/digests and data engines. Preserve the distinction between declared constraints, resolved locks, build versions and actually observed deployed runtime. Record source/main versus deployed SHA differences. Use current primary vendor advisories, support schedules and compatible per-major patch floors; a reviewed affected version is not proof of reachable exploitation.

Report STANDARDS_SYNC, STACK_REVIEW_COVERAGE and STACK_SECURITY_STATUS independently, with concrete fixes/migration recommendations and missing evidence. Sync success cannot mark the stack safe, and findings do not block delivery of safer standards. Preserve Secure's application-release rule and existing controls. Do not install/update dependencies or run applications, tests, Docker, UAT, scanners, deployments or provider mutations from this review alone. Continue separately authorized remediation; otherwise leave its concrete findings for the owner's decision.

### 9b. Publish eligible central repository status

After the Stack Security Review has current evidence, apply [PHDK_REPOSITORY_STATUS.md](PHDK_REPOSITORY_STATUS.md).

For a verified `tuyoisaza/<repo>` downstream repository, when the active session already has write access to `tuyoisaza/PHDK`, refresh `docs/repos/<repo>/status.md` in the canonical PHDK repository with the installed/canonical PHDK versions, observed repository SHA, concise tech-stack versions and independent stack-review status. Use only evidence already established by this foreground operation. Do not include secrets or infer deployed versions.

Treat central publication as a separate reporting outcome. Failure or unavailable write access does not invalidate the downstream standards sync or stack review and must not trigger a credential request, scheduler, background retry or new monitoring process. Report `CENTRAL_STATUS: PUBLISHED | NOT_PUBLISHED | UNVERIFIED` with the reason.

### 9c. Mandatory forced-upgrade publication checkpoint

An exact PHDK upgrade force command authorizes **delivery of its changed standards to remote main as the first scoped milestone**. The copier's UPDATED/CURRENT status, a local main commit, a branch push, a Railway branch deployment or an open PR do not prove delivery. A locally CURRENT sync can still be absent on remote main.

1. **Recover instead of multiplying workspaces.** Inspect current branch, worktrees, uncommitted edits, existing upgrade PRs and remote main. Reuse an in-scope unfinished branch/PR rather than opening another. An already-published no-op means the expected canonical manifest files **and** applicable native managed block are verified on fresh remote main; in that case do not create a dummy commit, branch or PR.
2. **Publish the actual change.** If main differs, stage only the synced PHDK-owned surface, required project version/changelog and authorized continuity evidence. Preserve other work. Apply permitted static/source checks and reviews, version-prefixed commit, push to **the feature branch**, create/update the PR targeting main, reconcile fresh target changes and merge using the permitted GitHub method. Never push feature:main directly or bypass GitHub rules. A PR merge itself updates remote main; do not add a redundant main-to-main push. Railway autodeploy is independent and may follow the existing main connection.
3. **Read back remote main.** Independently verify the merged PR result/SHA, expected project version, all synced manifest files and the applicable native managed block on remote main. With local Git, use `python phdk-standards/scripts/phdk_upgrade_remote_gate.py --expected-version <UPSTREAM_VERSION>` for the read-only **vendored-content** comparison; PR merge, native block, application and deployment still need separate evidence. With connector-only access use equivalent source comparisons. A missing or failed readback means UPGRADE_REMOTE_MAIN=BLOCKED/UNVERIFIED, never PUBLISHED. Apply the normal PHDK completion gate for versioned deliveries; a proven already-published no-op does not require a fictitious PR.
4. **Close the local workspace before the next one.** After verified merge, fetch and fast-forward clean local main to the newly observed origin/main, checking both SHA and ahead/behind=0. Run PHDK_GIT_WORKSPACE_CLOSEOUT.md using the verified merge SHA and owned branch. If the completed branch is checked out in the current linked worktree, move the coordinator into an existing safe main worktree first; do not delete its own running worktree. Retire only clean, unlocked, independently integrated owned branches/worktrees; use v2.71.0 evidence-backed remote branch cleanup where available. Never discard dirty, active, divergent, unknown or unrelated work.

Record UPGRADE_REMOTE_MAIN=PUBLISHED | ALREADY_PUBLISHED | BLOCKED | UNVERIFIED, final remote SHA, version, PR/merge (or verified no-op), LOCAL_MAIN, LOCAL_CLEANUP and retained worktree reasons. If an actual hook, access or server control prevents publication, preserve the unfinished branch and report the precise blocker. Continue genuinely independent authorized work where safe, but do not call the upgrade delivered or open another worktree for the same unfinished delivery.

### 9d. Transition `PHDK upgrade force` → `PHDK auto force`

After forced standards synchronization, Stack Security Review, eligible central-status publication, the mandatory remote-main publication checkpoint above, and upgrade-phase verification complete, `PHDK upgrade force` MUST transition immediately into `PHDK auto force` in the same conversation/session. Do not ask the owner to type a second command and do not emit a terminal upgrade-only response first.

Determine the Auto Force goal in this order:

1. If the current conversation or repository state already identifies an unfinished authorized product/development goal, continue that goal.
2. Otherwise use the bounded maintenance goal: **reconcile this repository with current PHDK and current recorded product intent; remediate compatible in-repository security/standards gaps; complete applicable Check/remediation and normal delivery; do not invent new product features or broaden scope.**
3. If multiple active fronts are already evidenced, let Auto Force use its PMO/portfolio rules rather than selecting an unrelated feature.

The handoff reuses the just-completed upgrade review as the Auto run's fresh Preflight Stack Security Review when evidence/input hashes and advisory freshness are unchanged; do not immediately repeat identical work. Initialize/recover Auto state and lifecycle under `PHDK_AUTO.md` / `PHDK_AUTO_CONTINUITY.md`, then continue through the eligible lifecycle.

A real blocker in the upgrade phase may prevent the transition only when Auto Force cannot safely proceed around it. Finish independent permitted work and report the exact boundary. Missing optional tooling, PHDK-only review waits, or the mere absence of a pre-existing product task are not reasons to ask for another command.

### 10. Commit or deliver only when authorized

A bare `PHDK upgrade` leaves the verified sync and stack-review findings available and does not authorize product delivery. **`PHDK upgrade force` is the explicit exception:** after its upgrade phase it enters Auto Force, whose normal scoped development/version/branch/PR/merge/delivery authority applies to the resulting maintenance/current goal. The upgrade phase itself still does not bypass controls, force-push, create tags/releases, administer providers, or execute UAT.

For a bare `PHDK upgrade`, when the current request separately authorizes git delivery, stage only the synced standards, the changed native managed block, authorized review/continuity evidence, and minimal required version metadata. Use normal project version rules and an authorized feature/maintenance branch. For `PHDK upgrade force`, step 9c publishes changed standards as the first scoped milestone before the Auto Force handoff. Auto Force owns additional authorized product milestones. If remote main already has the exact standards, do not invent an upgrade-only commit, version bump or PR.

Do not create, enable, dispatch, rerun, or schedule GitHub Actions/hosted CI to validate or deliver the upgrade.

## Report, stop, or transition

Report the command used, old/new versions, upstream SHA, vendored-file count, native-block state, branch/commit/merge state where applicable, checks, conflicts, limitations, and CENTRAL_STATUS. Include STANDARDS_SYNC, STACK_REVIEW_COVERAGE and STACK_SECURITY_STATUS with dated evidence, missing coverage, findings and exact next actions under Secure; a copied manifest or helper PENDING result is not a completed audit. For force mode, explicitly list the PHDK-owned dirty paths that were overwritten/removed and state that non-PHDK repository files were preserved. For bare Upgrade, then stop. For Upgrade Force, continue through the mandatory Auto Force handoff and report only the final composite outcome.

An upgrade does not activate Developer Mode, remove installed application automation, terminate a process, revoke a credential, disable an external scheduler, or change GitHub/hosting settings. Removing existing automation files is a separate explicit repository-code request; external administration remains outside PHDK. Never report those operations as completed merely because standards were updated.


## Post-force standards acceptance note

After `PHDK upgrade force`, keep verified standards synchronization, stack-review coverage/security findings and product validation as separate evidence, **then continue automatically into the required Auto Force phase**. The upgrade phase alone does not validate or repair product behavior; the chained Auto Force phase performs its applicable implementation, security remediation, Check and delivery work under its own contract. Never report vendoring itself as proof that application behavior works or that vulnerabilities were patched; report those outcomes only from the subsequent Auto Force evidence.
