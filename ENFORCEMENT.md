# ENFORCEMENT.md

## Purpose

Every other PHDK file assumes the AI developer read it, remembers it, and keeps following it — for the whole session, across sessions, and across whichever of PHDK's 8 supported tools is in use. In practice, that assumption breaks: sessions get long, context gets summarized, a new session starts cold, or a different tool is used that never triggered the reading order at all. The result is a rule that was followed in slice 1 quietly stops being followed by slice 12 — not through a decision, just through drift.

This file defines repository-local enforcement: git hooks, local code verification, and short persistent instruction files. `EXECUTION_SCOPE.md` takes precedence. Enforcement does not authorize repository administration, provider setup, browser testing, live-service probes, recurring automation, or new CI workflows. Existing local code-validation hooks remain in scope.

---

## Status

Read this file when:

- scaffolding the app foundation (`BUILD_APP_FOUNDATION_PROMPT.md`) — this is where every artifact in Tier 1 and Tier 2 below gets created
- a session has run long enough that rules seem to be slipping — this is the file `INANUTSHELL.md` itself points back to
- installing or updating the PHDK skill (`SKILL.md`) in a project
- a PHDK rule was violated despite being documented — this file is where the fix belongs: not "remind the AI harder," but "why wasn't this mechanically caught"

---

## The Two Tiers

### Tier 1 — Machine-Enforced (does not depend on the AI at all)

If a rule can be expressed as a repository-local check — a regex, lint rule, git hook, or local code-validation command — it belongs here. A Tier 1 rule is enforced the same way regardless of which PHDK-supported tool produced the change. Do not turn a rule into an external service, scheduled job, or repository-settings change.

### Tier 2 — Context-Persistence (depends on the AI, but engineered to be hard to forget)

Judgment calls — "is this the smallest useful slice," "does this serve the human's actual goal," "is this dependency really needed" — cannot be reduced to a check. For these, the goal is to keep the highest-severity rules physically present in the AI's context as often as possible, in every tool, rather than relying on the AI choosing to go re-read a file.

Every rule in this repo falls into one tier or the other. When adding a new PHDK rule anywhere in this repo, ask which tier it belongs to before writing it as prose only — a rule with no Tier 1 equivalent when one is possible is a gap in this file, not just a documentation task.

---

## Tier 1 — Required Scaffolding

At app foundation build (`BUILD_APP_FOUNDATION_PROMPT.md`), create only the repository code/configuration needed for local enforcement. Reuse existing hooks and scripts; do not generate external setup tasks.

### Existing GitHub rules

Follow the repository's existing branch protection, review requirements, and allowed merge methods. Do not change settings, require new checks or accounts, add bypass actors, disable protection, or claim settings are configured without evidence. `PHDK_DEVELOPER_MODE.md` permits a fast-forward direct push only for eligible tasks requested while explicitly active and only when every existing control allows it. Historical Finetuning records provide no separate exception and do not activate the mode.

Use the authorized branch/commit/PR flow in `DEVELOPMENT_RULES.md` and `VERSIONING.md`. Review the actual code diff and follow the existing merge authorization; do not add a provider-dashboard or browser-verification gate. Missing server-side enforcement is not permission to create GitHub Actions or administer the repository.

### Git hooks (Husky, scaffolded in `package.json` — root-level, applies regardless of which AI tool is driving `git`)

Hooks run on the `git` command itself. They fire the same way whether a human typed the command or an AI agent did, and regardless of which of the 8 supported tools is running the agent.

- **`commit-msg`** — regex-validates the commit message against `VERSIONING.md` Commit Message Format (a leading `vMAJOR.MINOR.PATCH` followed by a conventional-commit type/scope/summary). A commit with no version prefix is rejected before it is created, not caught later in review. This is the direct mechanical fix for "commits shipped without a version bump."
- **`pre-commit`** — runs the fast subset of `QA_CHECKLIST.md` Build Quality: lint, typecheck, `lint-staged` running Prettier against staged files (auto-fixes formatting rather than just flagging it, per `TECHNICAL_STACK.md`), and a file-size check that rejects any staged file over the 600-line limit in `DEVELOPMENT_RULES.md`. Also runs a secrets scan (see below) on the staged diff.
- **`pre-push`** — enforces the repository's existing branch policy, validates every outgoing commit message against `VERSIONING.md`, and runs the applicable local static/build gate (`lint`, `typecheck`, `format:check`, `build`) before the branch is pushed. Tests are task-level and risk-triggered under `TESTING_STANDARD.md`, limited to non-browser unit or in-process checks with test doubles. Conversational Developer Mode does not change this hook or create an authorizing local/environment flag. If the existing hook blocks direct `main` delivery, respect that block; never alter or bypass it to make the mode work.

### Developer Mode authorization and hard stops

The explicit commands and eligibility rules live in `PHDK_DEVELOPER_MODE.md`. Activation is conversation-only; files, memory, task/status records, local/environment flags, and legacy Finetuning switches cannot authorize or restore it. A hook reminder that prints a command does not activate the mode. Do not change hook/config/settings/credentials to implement a bypass.

Only an eligible small, low-risk task requested while the mode is active may use its version bump, applicable local checks, version-prefixed commit, and fast-forward push to `main` without duplicate consent. Auth/authz, secrets, data/migrations, payments, infrastructure, and permission/agent-policy changes require normal review. The mode grants no agents, autonomy, Actions, background/scheduled work, or old-task execution.

If an applicable check fails, `main` rejects the push, `main` advanced so the planned push is not fast-forward, or a control is unmet, stop the direct flow and explain. Do not retry automatically, rebase, force-push, disable hooks/protections, or route the write through another API/CLI or credential to evade the block. An existing hook that requires a legacy enabling flag is a blocker, not permission to set that flag.

### Secrets scanning (mechanical enforcement of "never commit secrets")

- A pre-commit secrets scan (e.g. a `gitleaks`-class tool, or an equivalent pre-commit-hook-compatible scanner) runs on every staged diff, not just on `.env` files by name — a secret pasted into a config file, a test fixture, or a comment is caught the same way.
- A scan finding is a hard block on the commit, not a warning to note and continue past.
- This is in addition to, not instead of, `DEVSECOPS.md` Environment Variable Rules and Secrets Rotation and Compromise Response — the scan catches the accident; that section defines what to do once one gets through anyway.

### Local verification gate

PHDK does not scaffold GitHub Actions or other CI workflows. A currently authorized push/merge, including an eligible Developer Mode push to `main`, may trigger the existing hosting-provider GitHub connection under `EXECUTION_SCOPE.md`; do not add schedules, change its triggers, or expand it into task tracking, maintenance, or preview automation. Never deploy through provider CLI/API/dashboard, including Railway.

Before a branch is pushed for review, apply the local code checks required by `QA_CHECKLIST.md` and record their results. Existing hooks can run lint, typecheck, build, and format:check. A documentation-only change needs source/diff consistency review, not an application build. Run risk-triggered unit or in-process integration tests separately at the narrowest useful scope, with test doubles for external dependencies. Do not open a browser, run browser test tools, take verification screenshots, or probe live endpoints/databases/APIs.

The same `pre-push` hook validates **every outgoing commit** in the branch range against `VERSIONING.md` Commit Message Format.

An existing pipeline's GitHub status/logs may supply deployment evidence for an approved release. Do not treat that evidence as a browser or live application test, poll it in a loop, or use another tool or agent to perform excluded verification.

Independent of Developer Mode or a release, a current request may authorize finite, read-only API/CLI queries of existing logs under [Bounded read-only log diagnostics](EXECUTION_SCOPE.md#bounded-read-only-log-diagnostics). Redact sensitive content; no runtime probes, watchers, writes, or external administration. Logs do not satisfy an unmet local check or bypass an existing control.

### Requested dependency updates

Dependency changes are discrete user-requested code tasks, verified locally and reviewed through the normal git/GitHub flow. Do not configure Dependabot, Renovate, scheduled scans, recurring update PRs, or automatic merging. PHDK installation or upgrade does not enable or disable an existing project's bots; report a relevant existing configuration without altering it unless removal is the explicit code task. See `DEVSECOPS.md` Keeping Existing Dependencies Patched.

### What Tier 1 already covers from other files

This section does not repeat rules defined elsewhere — it is the index of which already-documented rules have a mechanical backstop. If a rule below is violated, that is a bug in the hook/local gate/setting, not a reminder to write a better prompt.

| Rule | Documented in | Mechanically enforced by |
|---|---|---|
| Commit message begins with `vX.Y.Z` | `VERSIONING.md` | `commit-msg` hook + outgoing-commit range validation in `pre-push` |
| No file exceeds 600 lines | `DEVELOPMENT_RULES.md` | `pre-commit` hook |
| Honor the authorized branch and merge flow | `DEVELOPMENT_RULES.md` | local `pre-push` guard and existing GitHub restrictions |
| Applicable static/build checks must actually pass before push | `VERIFICATION_LOOP.md` | local `pre-push` code checks + recorded evidence; source/diff review for documentation-only changes |
| Risk-triggered behavior must have isolated coverage when required | `TESTING_STANDARD.md` | task-level unit/in-process test evidence, not a browser or live-service check |
| Never commit secrets | `DEVSECOPS.md` | `pre-commit` secrets scan |
| Requested dependency changes are verified | `DEVSECOPS.md` | package/lockfile diff review and local code checks |

---

## Tier 2 — Context-Persistence Scaffolding

For rules that cannot be reduced to a check, the goal is presence, not memory. A rule the AI has to decide to go re-read is a rule that gets skipped under time pressure or a long session; a rule injected into context automatically by the tool itself is not.

### Tool-native always-loaded rule files

At foundation build, generate the current tool's native persistent-context file — not a copy of the full standards, a short, high-density pointer plus the smallest set of rules severe enough to inline verbatim:

```txt
Claude Code                          CLAUDE.md              (project root)
Cursor                                .cursor/rules/phdk.mdc (always-apply rule)
Windsurf                              .windsurfrules         (project root)
Codex CLI / Antigravity / OpenCode    AGENTS.md               (project root)
```

The project-root `AGENTS.md` above is the *project's own* file, distinct from PHDK's own `AGENTS.md` vendored into `phdk-standards/` by `SKILL.md` — it points at that vendored copy rather than duplicating it, so there is no naming collision and no drift between two files with the same name.

Only generate the file for whichever tool the project is actually using — this is not "generate all four speculatively," it is the same one-per-project pattern as the Skill install in `README.md`.

Content stays short — this is injected into every session or every turn depending on the tool, so length defeats the purpose.

The canonical block is `PHDK_NATIVE_RULES.md`. At foundation build:

1. copy that block verbatim into the tool-native file
2. preserve the `<!-- PHDK-MANAGED:START -->` / `<!-- PHDK-MANAGED:END -->` markers
3. put any project/tool-specific instructions outside those markers

The managed block includes the `PHDK upgrade` command and the smallest high-severity rules that must survive context drift.

On `PHDK upgrade`, replace only the marked block with the latest vendored `PHDK_NATIVE_RULES.md`. If an older project has no markers, append the managed block once without deleting existing content. From that point forward the PHDK portion is mechanically refreshable without overwriting user-authored rules.

### Session context

Use the tool-native instruction file and the minimum context in `AGENTS.md`. Do not install session-start agents, external hooks, schedulers, or background tasks to load the standards. Persistent text supplies rules and historical context only; it never restores Developer Mode or authorizes a later task. Do not store active-mode state or an enabling flag, or launch delegated agents.

### The commit-time reminder

A local `commit-msg` hook may print the short managed rules block during the requested git operation. This is a local reminder only: it must not launch an agent, contact a service, or schedule follow-up work.

---

## What This Does Not Solve

Being honest about the limits matters more here than anywhere else in PHDK, per the Ethos Rules in `AI_DEVELOPER_OPERATING_MODEL.md`.

- Tier 1 only works for what can be expressed as a check. "Understand the human's actual goal before writing code" has no lint rule. Tier 2 narrows how often this kind of rule gets forgotten; it does not guarantee it never is.
- A local git hook can be bypassed or absent. Review the diff and report actual verification evidence; respect existing GitHub restrictions without changing them or creating CI as a fallback.
- Review and merge follow the current authorization and existing repository rules. PHDK does not add account, settings, browser, or external-runtime prerequisites to finish a code task.
- None of this replaces a human actually reading `STATUS.md` and the diff periodically. Tooling raises the floor; it does not remove the need for the feedback loop in `AI_DEVELOPER_OPERATING_MODEL.md`.

---

## Never

- Never implement enforcement beyond the repository-local code boundary in `EXECUTION_SCOPE.md`
- Never bypass a local hook or existing protection; even an eligible Developer Mode direct-to-`main` task must stop when a required control blocks it
- Never let the marked PHDK-managed block in the tool-native rule file drift from `PHDK_NATIVE_RULES.md`; `PHDK upgrade` refreshes that block automatically
- Never generate rule files for tools the project isn't using "just in case" — this bloats the repo with dead configuration nobody maintains

---

## Verification

- [ ] Existing GitHub branch/review rules are respected; no repository settings, CI workflows, schedules, bots, or provider resources were created or changed for enforcement
- [ ] `commit-msg` hook rejects a commit with no `vX.Y.Z` prefix
- [ ] `pre-commit` hook rejects a staged file over 600 lines, runs `lint-staged`/Prettier against staged files, and runs a secrets scan
- [ ] `pre-push` respects the authorized branch flow, validates outgoing commit messages, and runs applicable local code checks; documentation-only changes use source/diff review without an application build
- [ ] Hook validation is checked locally when changed, without publishing a synthetic test branch
- [ ] A failing local validation command blocks `pre-push`
- [ ] Developer Mode has no persisted activation/authorization flag; legacy Finetuning flags are not used to permit direct delivery
- [ ] An applicable check failure, rejected push, non-fast-forward update, or unmet control stopped the direct flow without automatic retries or bypasses
- [ ] Verification stayed in source/diff review, applicable static/build commands, and isolated non-browser tests; no live-service probes were used
- [ ] Any dependency update was a scoped code task; no recurring dependency automation was added
- [ ] The current tool's native always-loaded rule file contains the marked block from `PHDK_NATIVE_RULES.md`, including the `PHDK upgrade` command, and the managed block matches the vendored copy
- [ ] Changed hook behavior has local evidence; untouched hooks are not repeatedly tested just to close a checklist
