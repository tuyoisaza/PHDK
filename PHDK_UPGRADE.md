# PHDK_UPGRADE.md

## Purpose and command contract

Synchronize an existing PHDK project to the current published standards in response to the user's request in this conversation.

The canonical command is `PHDK upgrade` (case-insensitive after trimming whitespace). It authorizes the standards sync now, without a second confirmation in the clean case. It does not authorize product implementation, a commit/push/merge/release, deployment, workflow execution, an agent, or a future run. A current request that explicitly includes git delivery provides that additional authorization.

Follow `EXECUTION_SCOPE.md`: one assistant, interactive-only, no delegation, no GitHub Actions, no scheduled/background work, no browsers, live application probes, or provider writes. Bounded read-only log retrieval is available only for a current requested diagnosis; it is not a standards-sync check. Report and stop after the requested sync and any authorized git delivery.

An upgrade copies `MAIN_DELIVERY_STANDARD.md` and the definition of `PHDK_DEVELOPER_MODE.md`; it never activates that mode. A sync that changes execution or authorization policy, including this release's delivery permissions, requires the normal branch/human-review flow even if Developer Mode is already active. Do not classify permission changes as low-risk merely because they are Markdown.

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

Inspect git status. Stop before overwriting any uncommitted change in `phdk-standards/`. Preserve unrelated files and changes without staging, discarding, stashing, or rewriting them.

Preserve stricter owner controls wherever they are stored, including committed overrides. If syncing a managed file would overwrite a stricter stop/pause/interactive-only rule, stop and report that exact path. Do not silently move, delete, or weaken it in order to obtain a clean upstream mirror.

Distinguish an actual owner restriction from an assistant-written snapshot of a past task. Do not introduce permanent routing claims such as "TASK remains paused" or use a generated summary to revoke an already-authorized current delivery. When the current request includes reconciling such records, verify the owner's instructions and live git/PR facts, correct the stale record, and preserve every genuine remaining control. A bare standards sync never silently removes a stricter owner rule.

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

Validate that every source exists, destinations are unique and safe relative paths, and no path escapes the standards directory. Copy exactly those mappings, including `EXECUTION_SCOPE.md`, `MAIN_DELIVERY_STANDARD.md`, `PHDK_DEVELOPER_MODE.md`, and `PHDK_NATIVE_RULES.md`.

Remove an obsolete vendored file only when the previous manifest lists it, the new manifest omits it, it is clean, and it contains no stricter owner override. For pre-manifest projects, do not delete unknown extra files. Never delete unrelated project files.

### 6. Refresh the current tool's managed block

Use the exact latest `PHDK_NATIVE_RULES.md` block with its `PHDK-MANAGED:START` and `PHDK-MANAGED:END` markers.

Known project-native locations include `CLAUDE.md`, `.cursor/rules/phdk.mdc`, `.windsurfrules`, and root `AGENTS.md`. Use only the current tool's applicable file.

- Replace only the marked managed block when it exists.
- When the file exists without markers, append the block without deleting existing project instructions.
- When the applicable file is absent, create it only as part of the requested install/sync.
- Preserve stricter owner rules outside or inside the block; stop on an overwrite conflict rather than weakening them.

Do not install a plugin, spawn an assistant, register a hook that runs tasks, or create a scheduler. Loading a rule file never starts work.

### 7. Record continuity

When safe to edit without absorbing unrelated work, record old/new PHDK versions, canonical repository, upstream commit SHA, date, and any conflicts in `STATUS.md`. Otherwise put that information only in the report.

Do not make an old product task active or create a next mission merely to record the sync.

Record the sync as its own scoped change; do not cancel an unfinished currently authorized delivery because a status/link question or the sync produced a new tracking entry. Verify observed git/PR completion before repeating an operation listed as pending in an older checkpoint. A report can record post-merge evidence without manufacturing another version-only commit.

Do not store or restore Developer Mode activation in the continuity record. Historical evidence that the mode was used does not authorize a new conversation or task.

### 8. Verify using repository evidence

- Vendored `VERSION` matches the chosen upstream version.
- Every manifest destination exists and matches its mapped source byte-for-byte.
- The current native managed block matches the source block.
- Interactive-only, single-assistant, no-delegation, no-Actions, no-scheduling, and owner-control rules are present.
- Developer Mode's explicit activation/exit, temporary lifetime, risk limits, and no-bypass rules match upstream; the upgrade itself did not activate it.
- Normal delivery's verified remote-target completion, risk-based review, authorization continuity, version reconciliation, and no-redundant-push rules match upstream; narrower requests and existing controls remain effective.
- Existing provider GitHub autodeploy and watch paths were not disabled or replaced with dummy filters as a PHDK restriction. Report observed deployment blockers/statuses separately without inferring permission for provider writes. Valid service-specific filters and intended skips for unaffected services are not configuration errors.
- The bounded read-only log-diagnostics permission is present without adding provider writes, live probes, streams, or monitoring.
- No owner control or unrelated edit was overwritten or staged.
- No product source changed except minimal version metadata when a currently authorized commit requires it.
- No agents, background tasks, workflow runs, browser sessions, live probes, or external configuration changes occurred.

Documentation-only verification is source/diff and reference checking. Do not run an application build or live check merely to satisfy an old checklist.

### 9. Commit or deliver only when authorized

A bare `PHDK upgrade` leaves the verified sync available for review. It does not automatically commit, push, merge, tag, deploy, or delete branches.

When the current request also authorizes git delivery, stage only the synced standards, the changed native managed block, safe continuity changes, and minimal required version metadata. Use normal project version rules and an authorized feature/maintenance branch. A clear instruction to merge includes necessary commit/push/PR steps, without bypassing existing restrictions.

Do not create, enable, dispatch, rerun, or schedule GitHub Actions/hosted CI to validate or deliver the upgrade.

## Report and stop

Report old/new versions, upstream SHA, vendored-file count, native-block state, branch/commit/merge state where applicable, checks, conflicts, and limitations. Then stop.

An upgrade does not activate Developer Mode, remove installed application automation, terminate a process, revoke a credential, disable an external scheduler, or change GitHub/hosting settings. Removing existing automation files is a separate explicit repository-code request; external administration remains outside PHDK. Never report those operations as completed merely because standards were updated.
