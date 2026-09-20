# PHDK_UPGRADE.md

## Purpose

This file defines the cross-tool command for synchronizing an existing PHDK project to the latest published PHDK standards.

The canonical command is:

```txt
PHDK upgrade
```

It is intentionally plain language so it works in Claude Code, Cursor, Codex, Windsurf, VS Code/Copilot, OpenCode, Pi, Antigravity, and other coding agents without depending on an IDE-specific slash-command system.

---

## Command Contract

When the developer says exactly `PHDK upgrade` (case-insensitive after trimming whitespace):

- Treat it as an imperative command, not a question.
- The command itself is explicit approval to fetch the latest PHDK and overwrite **PHDK-managed** vendored standards with the upstream copy.
- Do **not** ask "Proceed?" or request a second confirmation in the normal clean case.
- Do not run the project's normal feature task first. Upgrade PHDK first, then stop and report.
- Do not regenerate the project brief, PRD, features, navigation, or other project-specific kit files.
- Do not change application code, dependencies, database schema, deployment settings, secrets, or infrastructure merely because PHDK was upgraded.
- Do not deploy or merge to `main` solely because this command was issued.

The one safety exception: if there are uncommitted changes inside `phdk-standards/`, do not overwrite them. Stop and report the conflicting paths. PHDK-owned files are supposed to be a clean mirror; silent destruction is not acceptable.

---

## Canonical Upstream

The only canonical source for this command is:

```txt
https://github.com/tuyoisaza/PHDK.git
branch: main
```

The upstream root `VERSION` file defines the latest PHDK version.

Do not use a cached model memory of the latest version. Fetch it.

---

## Upgrade Procedure

### 1. Identify the project

Find the current git repository root.

A project is considered PHDK-enabled when at least one of these is true:

- `phdk-standards/` exists
- the project-root tool rule file points to `phdk-standards/AGENTS.md`
- `TASK.md` and `STATUS.md` exist and the project identifies itself as PHDK

If none apply, do not silently convert an unrelated repository into PHDK. Report that PHDK is not installed in this repo.

### 2. Safety preflight

Before fetching or overwriting:

- inspect git status for `phdk-standards/`
- if any uncommitted change exists inside that folder, stop and report it
- unrelated uncommitted project files must not be staged, discarded, stashed, or rewritten by the upgrade

If the current branch is the repository's default/protected branch and an upgrade will be needed, create a dedicated branch such as:

```txt
chore/phdk-upgrade-vX.Y.Z
```

If already on a non-default working branch, stay on it unless the project's own workflow requires a dedicated maintenance branch.

### 3. Fetch a fresh upstream copy

Use a platform-appropriate temporary directory outside the project and fetch a fresh shallow clone of `main`.

Equivalent intent:

```txt
git clone --depth 1 https://github.com/tuyoisaza/PHDK.git <temporary-directory>
```

If the fetch fails, make no project changes. Report the failure.

If the current IDE is using an installed PHDK skill clone and that clone is discoverable, it may also be fast-forwarded with `git pull --ff-only` after the project sync succeeds. A dirty skill clone must never be force-reset.

### 4. Compare versions

Read:

```txt
project:  phdk-standards/VERSION
latest:   <fresh-upstream>/VERSION
```

If the project has no vendored `VERSION`, treat it as pre-versioned/older and allow the standards folder to be created or normalized.

If project version equals latest version:

- verify the managed native-rules block is current
- report "already current"
- do not create a no-op commit

If the project version is newer than upstream, do not downgrade. Report the mismatch.

### 5. Read the upstream manifest

Read the **latest upstream** `PHDK_MANIFEST.txt`.

Each non-comment line is:

```txt
source path | destination path inside phdk-standards/
```

Copy exactly those files from the fresh upstream clone into the listed destination paths.

Do not guess the file list from memory.

If the existing vendored copy has an older `PHDK_MANIFEST.txt`, remove files that were listed in the old manifest but are no longer listed in the new manifest. Never delete files outside `phdk-standards/`.

For pre-manifest projects, do not delete unknown extra files during the first upgrade; only write the new manifest set.

### 6. Refresh the tool-native PHDK block

The latest vendored `phdk-standards/PHDK_NATIVE_RULES.md` is the canonical managed block for tool-native persistent instructions.

Known locations include:

```txt
Claude Code                          CLAUDE.md
Cursor                               .cursor/rules/phdk.mdc
Windsurf                             .windsurfrules
Codex / Antigravity / OpenCode       AGENTS.md
```

For the tool currently in use:

- if the file contains `<!-- PHDK-MANAGED:START -->` and `<!-- PHDK-MANAGED:END -->`, replace only that block with the latest `PHDK_NATIVE_RULES.md`
- if the file exists but has no managed markers, append the managed block without deleting existing user/project instructions
- if the tool's native file does not exist and the current tool is known, create it with the managed block
- do not create rule files for tools that are not in use

This makes future `PHDK upgrade` commands self-updating without overwriting unrelated IDE instructions.

### 7. Record continuity

If `STATUS.md` is clean enough to edit without absorbing unrelated uncommitted work, record:

```txt
PHDK standards: vOLD → vNEW
Upstream: https://github.com/tuyoisaza/PHDK
Upstream commit: <sha>
Date: <current date>
```

If `STATUS.md` already has unrelated uncommitted edits, leave it untouched and include the same information in the upgrade report instead. Do not let continuity logging cause unrelated work to be staged accidentally.

### 8. Verify the sync

Before committing, verify:

- `phdk-standards/VERSION` equals upstream `VERSION`
- every destination in the latest `PHDK_MANIFEST.txt` exists
- every vendored file byte-for-byte matches its mapped upstream source
- the current tool-native managed block matches `phdk-standards/PHDK_NATIVE_RULES.md`
- no application/source files changed unless the project's own versioning rule requires minimal version metadata for the upgrade commit
- no unrelated working-tree changes were staged

### 9. Commit safely

Stage only:

- `phdk-standards/`
- the current tool-native rule file if its PHDK-managed block changed
- `STATUS.md` only when the upgrade itself changed it
- minimum project version metadata only if the project's `VERSIONING.md` requires it for every commit

Commit through the project's normal version/commit rules. The commit summary should clearly include the PHDK transition, for example:

```txt
chore(phdk): upgrade standards vOLD to vNEW
```

If PHDK project rules require a leading product version, add that required prefix.

Push the maintenance/working branch when the project's normal workflow authorizes pushes. Never merge, deploy, or delete branches solely because of `PHDK upgrade`.

---

## Required Final Report

Return a compact report:

```txt
PHDK upgrade
from: vOLD
to: vNEW
upstream commit: <sha>
vendored files: <count>
native rules: updated / already current / not applicable
status: updated / already current / blocked
branch: <name>
commit: <sha or not created>
conflicts: none / <paths>
```

Do not turn the upgrade into a general project review. The command has one job: synchronize PHDK safely and stop.
