# PHDK cross-agent canonical policy

Project-root `AGENTS.md` is the single canonical PHDK policy entry point regardless of coding agent. Vendored `phdk-standards/AGENTS.md` is the versioned reference, not a competing root policy.

## Tool adapters

- **Codex:** reads root `AGENTS.md` directly.
- **OpenCode:** reads root `AGENTS.md` directly when supported; if an alternative instruction path is configured, point it at `AGENTS.md` without duplicating policy.
- **Claude Code:** uses root `CLAUDE.md` containing an `@AGENTS.md` import.
- **Other tools:** use their existing native entrypoints as minimal references, with syntax the tool actually supports. Do not create files for unused tools.

Canonical newly generated Claude adapter:

```md
<!-- PHDK-ADAPTER:CLAUDE:START -->
@AGENTS.md
<!-- PHDK-ADAPTER:CLAUDE:END -->
```

## Force migration contract

1. Inventory root `AGENTS.md`, existing native files (including `CLAUDE.md`), managed markers, owner text, and actual GitHub protections.
2. Install/refresh the exact canonical `PHDK_NATIVE_RULES.md` block only in root `AGENTS.md`. Preserve root content outside PHDK markers.
3. Replace duplicate PHDK-managed blocks in native files with a minimal reference to root `AGENTS.md`. Replace an entire native file only if it is provably an exact PHDK-generated adapter or the owner expressly authorizes replacement.
4. Preserve unmarked owner instructions, including an explicit human-review rule, unless a **current explicit owner instruction** supersedes that documentary rule. Such owner-authorized reconciliation must record what changed. Generic `upgrade force` alone does not authorize deletion of owner rules.
5. Never remove an actual GitHub-enforced review, CODEOWNERS control, branch protection, hook, permission requirement, or applicable check. A conversation instruction does not impersonate a formal GitHub approval.
6. Verify active adapters refer to root `AGENTS.md`, no duplicate PHDK managed policy remains, and preserved owner rules are reported. If conflicting unmarked owner instructions remain, report them as a migration blocker, not as canonicalization success.

Do not add redundant approval prompts in tool adapters. Under `PHDK auto`, stage transitions and ordinary PR delivery proceed automatically within the authorized goal, subject to actual project-owner controls and enforced requirements.
