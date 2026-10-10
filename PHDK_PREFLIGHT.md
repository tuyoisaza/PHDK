# PHDK Preflight Standard

## Purpose

Every PHDK command must begin with a fast, bounded preflight before doing substantive work.

Preflight verifies that:

1. PHDK is installed coherently for the current repository/tool.
2. The installed PHDK version is current enough to run the requested command.
3. The manifest-controlled standards are present.
4. The current tool's managed PHDK instruction block is present and recognizable.
5. Relevant recommended skills/capabilities for the requested command are available.
6. The user has not explicitly disabled use of recommended skills.

Preflight is not a separate user command requirement. It is an automatic first step of PHDK commands.

## Commands covered

Run Preflight before:

- `PHDK capture`
- `PHDK plan`
- `PHDK PMO`
- PMO Integration Review / any explicit integration stage
- `PHDK auto`
- `PHDK uat`
- `PHDK uat fix`
- `PHDK check`
- `PHDK unlock`
- Developer Mode tasks
- other future PHDK lifecycle commands

`PHDK upgrade` and `PHDK upgrade force` run the installation/version portions of Preflight as part of their own synchronization contract.

## User override

If the user explicitly says not to use skills, plugins, connectors, MCPs, external references, or a named capability, honor that instruction for the current request.

Examples:

- "PHDK plan, no uses skills externos"
- "PHDK auto without plugins"
- "No uses frontend-design"

In that case:

- still verify the PHDK installation/version itself;
- skip the disabled skill/capability checks;
- do not repeatedly recommend what the user declined;
- use core PHDK standards and available built-in capabilities.

A generic request for a PHDK command is otherwise permission to use already-installed, relevant, read/execute-safe skills within existing PHDK execution boundaries.

## Step 1 — Verify PHDK installation

Identify the active PHDK installation.

Common evidence:

- `phdk-standards/VERSION`
- `phdk-standards/PHDK_MANIFEST.txt`
- the tool-local PHDK skill clone
- a native `PHDK-MANAGED` instruction block
- repository instructions pointing to vendored PHDK standards

Do not infer installation solely from a README mention or historical task file.

Report:

- installed PHDK version;
- installation location/type;
- managed block state;
- manifest presence.

## Step 2 — Verify canonical version

When canonical GitHub access is available, read current PHDK `main` and `VERSION`.

Compare canonical vs installed version.

### Current

If versions match, continue.

### Installed version is older

When the current PHDK-owned surface is clean and synchronization is available, automatically perform conservative PHDK standards synchronization as an internal preflight step, then re-read the updated command/standards before continuing.

Do not require the user to separately type `PHDK upgrade` just because the requested command needs the current standards.

This automatic preflight synchronization:

- changes only the PHDK-owned synchronization surface defined in `PHDK_UPGRADE.md`;
- does not authorize product changes by itself;
- does not push/merge/deploy solely because of the sync;
- must preserve unrelated repository changes.

If dirty local edits in the PHDK-owned surface would be overwritten, do not discard them. Report the paths and continue only when the installed version remains capable of safely executing the command. If current semantics are required, instruct the owner to use `PHDK upgrade force` or explicitly resolve the PHDK-local changes.

Never silently force-upgrade.

### Installed version is newer

Do not downgrade. Record the state and continue using the installed version unless there is a concrete incompatibility.

### Missing/incomplete installation

If manifest-controlled files or the managed block are materially incomplete:

- repair missing PHDK-owned files from canonical upstream when that can be done conservatively without overwriting unrelated/local owner content;
- otherwise report the exact installation gap and the next command/action needed.

Do not continue while pretending a materially incomplete standards installation is valid.

## Step 3 — Verify manifest integrity

Read the installed/canonical `PHDK_MANIFEST.txt`.

At minimum verify:

- all mapped PHDK destination files exist;
- `VERSION` is present;
- command standards needed for the requested command are present;
- `SKILLS_REGISTRY.md` and `PHDK_PREFLIGHT.md` are present in current installations;
- no manifest path escapes `phdk-standards/`.

A complete hash/byte comparison is required during Upgrade; ordinary command Preflight may use a bounded structural check unless drift is suspected.

## Step 4 — Determine recommended skills/capabilities

Read `SKILLS_REGISTRY.md` and select only recommendations relevant to the current command and repository technology.

Do not preload every skill.

Classify each relevant capability:

- **AVAILABLE** — installed/connected and usable now.
- **BUILT-IN EQUIVALENT** — a native capability satisfies the same purpose.
- **MISSING OPTIONAL** — useful but the command can proceed safely without it.
- **MISSING IMPORTANT** — materially lowers quality/evidence for this command.
- **DISABLED BY USER** — user explicitly said not to use it.
- **INCOMPATIBLE / OUT OF SCOPE** — conflicts with PHDK execution limits.

## Step 5 — Inspect actual availability

Inspect only the current tool's real skill/plugin/capability inventory.

Examples:

- local skill directories used by the active coding tool;
- the tool's installed skills index;
- connected plugin/connector inventory;
- built-in capabilities already exposed to the assistant.

Do not claim a skill is installed merely because `SKILLS_REGISTRY.md` contains a URL.

Do not install the same skill repeatedly or create duplicate copies.

## Step 6 — Use relevant installed skills

When a recommended skill/capability is AVAILABLE and compatible with PHDK:

- actually read/use it for the relevant stage;
- apply its useful domain guidance;
- keep PHDK/owner instructions authoritative;
- do not import contradictory delegation/background/browser/provider-write behavior.

Examples:

- Plan/UX work should use an available frontend/design skill when relevant.
- Security-sensitive Plan/Auto/Check work should use an available security-review skill/guidance.
- Code review/Check should use an available code-review skill.
- Framework/library work may use an available current documentation capability.
- PMO may use supported worker/subagent capability only under `PHDK_PMO.md`.

A registry entry that is never checked or used has no operational value.

## Step 7 — Missing recommended skill

A missing skill must not automatically block PHDK when PHDK can safely perform the work itself.

### Optional skill

Proceed using core PHDK/built-in capabilities. Mention the missing optional capability only when it materially affects quality.

### Important skill

When the skill would materially improve the requested task:

- state that it is missing;
- if installation/connection can be offered through the current product/tool, present that option;
- installation/connection that requires user action must not be falsely claimed as completed;
- if the user declines or installation is unavailable, continue with the strongest available PHDK/built-in approach unless the capability is genuinely required.

Do not convert optional ecosystem dependencies into hard project blockers.

## Step 8 — Preflight summary

Keep the summary concise.

Example:

```text
PHDK Preflight
- PHDK: v2.44.0 current
- Installation: complete (35 manifest mappings)
- Managed rules: current
- Plan capabilities:
  - frontend-design: AVAILABLE — will use
  - security guidance: AVAILABLE — will use
  - current-docs capability: MISSING OPTIONAL — proceeding with repo/PHDK evidence
- User skill override: none
```

Do not make Preflight a noisy ritual when everything is healthy.

## Stage recommendation matrix

Use `SKILLS_REGISTRY.md` for the full current mapping. Typical categories:

### Capture
Useful:
- product discovery / requirements-analysis guidance;
- documentation/research readers;
- domain-specific references where applicable.

### Plan
Useful:
- frontend/UX architecture guidance;
- security architecture guidance;
- framework/current-docs capability;
- architecture/code-quality guidance.

### PMO
Useful:
- runtime-supported worker/subagent capability;
- repository/GitHub readers;
- dependency/change-review guidance.

### Auto
Useful:
- relevant framework/domain skills for implementation;
- code-quality guidance;
- security guidance for sensitive changes;
- current-docs capabilities.

### Integration Review
Useful:
- code-review capability;
- dependency/API/schema review guidance;
- security review when boundaries changed.

### UAT / UAT Fix
Useful:
- testing/QA guidance;
- accessibility guidance for source-level/manual checklists;
- domain-specific acceptance guidance.

### Check
Useful:
- code-review capability;
- security review guidance;
- frontend/design review guidance when UI standards apply;
- current-docs capability where framework compliance depends on current APIs.

## Relationship to installation

PHDK Preflight validates and uses the current environment; it is not permission to mutate unrelated personal/global tooling.

Repo-local/tool-local skill installation is allowed only when the current user request or product flow authorizes that installation and it can be done safely without changing unrelated projects.

Third-party plugins/connectors that require user consent/connection must follow the host product's explicit installation/connection flow.

Never claim that a plugin, connector, MCP server, or external credential was installed when the user has not completed the required action.

## Relationship to Auto

`PHDK auto` runs Preflight once at the beginning of the lifecycle and rechecks capabilities only when a later stage needs a materially different capability.

Do not repeat a full Preflight before every internal Auto stage.

If Auto's internal Plan stage needs a design skill that Capture did not, inspect that capability then.

## Completion evidence

Final reports should mention capability limitations only when they materially affected the result.

Do not pad every completion report with the full skill inventory.
