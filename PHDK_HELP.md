# PHDK Help — read-only, context-aware command discovery

## Purpose

`PHDK help` is the recommended **first conversational command after installing PHDK in a repository**. It is a **read-only orientation command**, not a new lifecycle stage, shell executable, background agent or permission to start work. Explain what PHDK is for, what the *current product* is for, every available conversational command and the most useful next action **without performing it**.

PHDK means **Project Handoff to Development Kit**. It is an owner-governed operating system for AI-assisted software delivery: intent → requirements/architecture → implementation → applicable quality/security → verifiable GitHub delivery. UAT is a separate explicit owner opt-in. The authoritative command inventory is the vendored `PHDK_COMMANDS.json`; do not hallucinate or use an old memorized command list.

## Invocation and routing

- **`PHDK help`**: display the one-line PHDK purpose, actual installed version (or `sin verificar`), a grounded project objective, the **complete concise catalog grouped by function**, and **one recommended next command** with rationale. State that recommending a command does not invoke it.
- **`PHDK help <command>`**: resolve a canonical command/alias in `PHDK_COMMANDS.json`, return what it does, when to use it, side-effect category, prerequisites/security boundary and the linked canonical standard. Examples: `PHDK help auto force`, `PHDK help browser on`, `PHDK help uat`. Do **not** execute the requested command.
- **`PHDK help --all`**: show all commands plus their aliases and more detail if the owner asks; plain `PHDK help` already enumerates every command.
- Unknown command: say `Comando no encontrado`, suggest the nearest documented name or `PHDK help`; never reinterpret an unrecognized phrase as an execution request.
- Upper/lowercase variants of `PHDK` and command names are lookup-equivalent. Do not expand missing entries into fictional commands. New command releases update this single inventory, this contract, routing and validation together.

For terminal/script consumers the **optional offline helper**, not an installed `phdk` binary, is `python3 phdk-standards/scripts/phdk_help.py --root .` (canonical checkout: `python3 scripts/phdk_help.py --root .`). It supports `--command "auto force"`, `--all` and `--json`; it reads only local documentation. Conversational agents may read the JSON and project artifacts directly to provide a better contextual explanation.

## Bounded read-only entry checks (help-only Preflight profile)

Normal substantive commands follow `PHDK_PREFLIGHT.md`. Help performs a **read-only subset of that Preflight**: identify current project and `phdk-standards/VERSION` (or canonical root `VERSION`), verify local command catalog and recognized installation/managed instructions when visible, and report any missing/stale *local* evidence. **Do not invoke `scripts/phdk_update.py`, auto-synchronize, run a Stack Security Review, install skills, edit TASK/STATUS, create files, spawn an agent, access providers, perform UAT or initiate any other command.** A help request grants no permission for browsing an application, deployments, writes, external spend or task resumption. When installation is incomplete, render the available catalog/next installation diagnosis rather than silently fixing it.

Do not claim remote `main` or newest canonical VERSION was compared unless it was actually inspected through an already-available **read-only** repository connection. It is fine to say `versión instalada: X; upstream: sin verificar` and suggest a separately owner-invoked `PHDK upgrade`.

## Project goal and stage discovery — evidence, not guesswork

Inspect only existing, relevant, nonsensitive, small project documents. Prefer an explicit `PROJECT_INTENT.md` or the **active** intent pointed to by `docs/INDEX.md`; otherwise consult existing project brief, nonsecret README, `MILESTONE_PLAN.md`, `TASK.md`, `STATUS.md` and actual code structure at a bounded level. Distinguish documented objective, implementation evidence, unverified inference and missing information. A project name, folder name or generic template is **not** proof of its objective. When missing, state `Objetivo del proyecto: no documentado / sin verificar` and suggest Capture. In canonical `tuyoisaza/PHDK`, explain the standards repository's own maintenance purpose rather than inventing a downstream product.

Recommendations based on observable facts, one at a time:

| Observed condition | Preferred suggestion |
|---|---|
| No coherent PHDK install / missing catalog | Finish/repair installation first; no silent updater |
| Unclear purpose or no reviewed intent | `PHDK capture` |
| Credible intent, no current architecture/milestone plan | `PHDK plan` |
| Existing visual product with missing design decisions | `PHDK design` (as appropriate) |
| Scoped goal and ready plan; owner wants full implementation | `PHDK auto` (or `PHDK auto force` when the owner deliberately delegates routine design decisions) |
| Existing project with suspected standard drift/unclear gaps | `PHDK check` |
| Verified outdated installed standards and safe owner intention | `PHDK upgrade` |
| Delivered candidate requiring acceptance | Offer **explicit** `PHDK uat` as an optional next action, not an automatic gate |

No unconditional `PHDK upgrade force`, `PHDK auto force`, `PHDK uat`, `PHDK browser on` or `PHDK check --fix` recommendation merely because a repo exists. Honor existing owner restrictions, provider permissions and lack of UAT consent. A suggestion remains a suggestion.

## Response shape (concise by default)

```text
PHDK help · v<installed> (or sin verificar)
PHDK: <why this operating system exists>
Proyecto: <documented goal + source or no documentado>
Situación: <one verifiable sentence, or sin verificar>

Comandos disponibles:
  <group>: <all canonical names> — <one-line purpose each>

Recomendación: PHDK <next> — <reason grounded in this repo>.
No ejecuté otros comandos ni modifiqué archivos.
```

When answering `PHDK help <command>`, show only the targeted detail, its material boundary and the next optional related command if applicable. The final `SIGUIENTE PASO` is the suggested invocation, **not** a pledge to execute it now. Do not print secrets, scan unrelated repos, rely on saved authorizations, or change a downstream repository during help.

## Release consistency and verification

- Vendor `PHDK_HELP.md`, `PHDK_COMMANDS.json` and `scripts/phdk_help.py` in `PHDK_MANIFEST.txt` exactly once.
- Route help through `AGENTS.md`, `SKILL.md`, `PHDK_NATIVE_RULES.md`, `README.md`, onboarding and the help-specific Preflight exception.
- Review every catalog `standard` against the actual source path and every aliases/command collision. Each newly introduced command must be added to the catalog within that release.
- Include offline synthetic tests for all-command output, aliases/detail, project-intent and missing-evidence fallback, and no-write behavior. Static source checks do not prove downstream assistant obedience or actual project readiness.
- No background onboarding ping, automatic command activation, new GitHub Action or project-wide migration is introduced.
