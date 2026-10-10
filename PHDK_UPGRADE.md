# PHDK_UPGRADE.md

## Purpose and command contract

Synchronize an existing PHDK project to the current published standards in response to the user's request in this conversation.

The canonical commands are:

- `PHDK upgrade` — conservative standards synchronization.
- `PHDK upgrade force` — authoritative replacement of the PHDK-owned surface from canonical upstream `main`, even when that PHDK-owned surface has local edits.

Match both case-insensitively after trimming whitespace.

A bare `PHDK upgrade` authorizes the conservative standards sync now, without a second confirmation in the clean case. `PHDK upgrade force` additionally authorizes discarding local modifications only inside the explicitly PHDK-owned surface defined below. It does not authorize product implementation, a commit/push/merge/release, deployment, workflow execution, an agent, or a future run. A current request that explicitly includes git delivery provides that additional authorization.

Follow `EXECUTION_SCOPE.md`: interactive-only, no GitHub Actions, no scheduled/background work, no browsers, live application probes, or provider writes. Delegation is prohibited except inside an explicitly active PMO session under `PHDK_PMO.md`. Bounded read-only provider diagnostics are available for a current requested check/diagnosis; a bare sync does not start that investigation. Report and stop after the requested sync and any authorized git delivery.

An upgrade copies `MAIN_DELIVERY_STANDARD.md`, `PHDK_UNLOCK.md`, `PHDK_AUTO.md`, `PHDK_PLAN.md`, `PHDK_PMO.md`, and the definition of `PHDK_DEVELOPER_MODE.md`; copying them activates no command or mode. Execution/authorization policy changes use the normal branch flow, even if Developer Mode is active. Review their actual diff and apply the approval rules in `MAIN_DELIVERY_STANDARD.md`: a well-defined owner request can already approve the policy decision, and a current instruction to deliver the identified update supplies delivery approval. Do not add a PHDK-only demand to open the diff or submit a GitHub review; actual formal review requirements remain binding.

When the owner explicitly includes this synchronization in an Auto development goal, use `PHDK_AUTO.md` for the whole goal's final verification and delivery cadence; copying standards or finishing a foundation does not complete that larger goal. A bare `PHDK upgrade` still authorizes only its sync, not product work or publication.

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

When versions match, check the managed block and file hashes before saying already current. Do not create a no-op commit.

For an authorized update on a default/protected branch, use a dedicated working branch such as `chore/phdk-upgrade-vX.Y.Z`; keep unrelated work untouched. Branch creation is part of the requested file-sync safety workflow, not permission to push it.

### 5. Synchronize the manifest

Read the fetched `PHDK_MANIFEST.txt`; never use a handwritten file list or cached model memory. Each non-comment line maps an upstream source to its destination inside `phdk-standards/`.

Validate that every source exists, destinations are unique and safe relative paths, and no path escapes the standards directory. Copy exactly those mappings, including `EXECUTION_SCOPE.md`, `MAIN_DELIVERY_STANDARD.md`, `PHDK_UNLOCK.md`, `PHDK_AUTO.md`, `PHDK_PLAN.md`, `PHDK_PMO.md`, `PHDK_DEVELOPER_MODE.md`, and `PHDK_NATIVE_RULES.md`.

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
- Interactive-only rules are present; delegation remains prohibited except for explicit PMO's bounded in-session worker model; no-Actions, no-scheduling, and owner-control rules remain present.
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

### 10. Commit or deliver only when authorized

A bare `PHDK upgrade` or `PHDK upgrade force` leaves the verified sync available for review unless the current request separately authorizes git delivery. Force changes overwrite authority, not delivery authority. It does not automatically commit, push, merge, tag, deploy, or delete branches.

When the current request also authorizes git delivery, stage only the synced standards, the changed native managed block, safe continuity changes, and minimal required version metadata. Use normal project version rules and an authorized feature/maintenance branch. A clear instruction to merge includes necessary commit/push/PR steps, without bypassing existing restrictions.

Do not create, enable, dispatch, rerun, or schedule GitHub Actions/hosted CI to validate or deliver the upgrade.

## Report and stop

Report the command used, old/new versions, upstream SHA, vendored-file count, native-block state, branch/commit/merge state where applicable, checks, conflicts, and limitations. For force mode, explicitly list the PHDK-owned dirty paths that were overwritten/removed and state that non-PHDK repository files were preserved. Then stop.

An upgrade does not activate Developer Mode, remove installed application automation, terminate a process, revoke a credential, disable an external scheduler, or change GitHub/hosting settings. Removing existing automation files is a separate explicit repository-code request; external administration remains outside PHDK. Never report those operations as completed merely because standards were updated.
