# ENFORCEMENT.md

## Purpose

Every other PHDK file assumes the AI developer read it, remembers it, and keeps following it — for the whole session, across sessions, and across whichever of PHDK's 8 supported tools is in use. In practice, that assumption breaks: sessions get long, context gets summarized, a new session starts cold, or a different tool is used that never triggered the reading order at all. The result is a rule that was followed in slice 1 quietly stops being followed by slice 12 — not through a decision, just through drift.

This file defines how PHDK stops depending on that assumption for as much as possible. The strategy is not "try harder to remember." It is: convert every rule that *can* be mechanically checked into something git, CI, or the AI tool itself enforces automatically — so compliance does not depend on anyone's memory — and for the smaller set of rules that genuinely require judgment and cannot be reduced to a check, maximize how persistently they stay in front of the AI regardless of session length or tool.

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

If a rule can be expressed as a check a computer can run — a regex, a lint rule, a repository setting, a CI status — it belongs here, not in a document someone has to remember to consult. A Tier 1 rule is enforced the same way whether the AI read the docs, forgot them, or was never told about them, and the same way regardless of which of PHDK's 8 supported tools produced the change.

### Tier 2 — Context-Persistence (depends on the AI, but engineered to be hard to forget)

Judgment calls — "is this the smallest useful slice," "does this serve the human's actual goal," "is this dependency really needed" — cannot be reduced to a check. For these, the goal is to keep the highest-severity rules physically present in the AI's context as often as possible, in every tool, rather than relying on the AI choosing to go re-read a file.

Every rule in this repo falls into one tier or the other. When adding a new PHDK rule anywhere in this repo, ask which tier it belongs to before writing it as prose only — a rule with no Tier 1 equivalent when one is possible is a gap in this file, not just a documentation task.

---

## Tier 1 — Required Scaffolding

All of this is created once, at app foundation build (`BUILD_APP_FOUNDATION_PROMPT.md`), the same way `TECHNICAL_STACK.md` First-time Railway Setup is a one-time procedure, not a per-slice task.

### GitHub branch protection (the strongest lever — a repository setting, not code)

This is the single most reliable mechanism in this file because it is enforced by GitHub itself and cannot be bypassed by an agent forgetting a rule, regardless of which AI tool or how many parallel agents are pushing commits.

Configure once, on `main`, in the repository's GitHub settings:

- Require a pull request before merging — direct pushes to `main` are rejected by GitHub, not by an agent's discipline. This is what actually makes `DEVELOPMENT_RULES.md`'s "never commit directly to `main`" true by construction instead of by request.
- Require at least one approving review before merge — this is what makes `QA_CHECKLIST.md` Human Diff Review a hard gate instead of a checklist item that can be skipped under time pressure. GitHub will not merge without a recorded approval; a chat message saying "looks good" does not count and cannot substitute.
- Require status checks to pass before merge — wire in the CI workflow below (lint, typecheck, build, test) as required checks, so a slice cannot merge on the AI's self-reported "tests pass" alone if the actual CI run disagrees.
- Do not allow force-pushes to `main`. Do not allow branch deletion of `main`.
- Finetuning Mode (`DEVELOPMENT_RULES.md`) is the one standing exception to "never push directly to `main`" — implement it as a scoped bypass (e.g. a repo admin temporarily disabling the direct-push restriction, or an allowlisted bypass actor) that is itself visible in the repository's settings audit log, not as something branch protection has no record of.

### Git hooks (Husky, scaffolded in `package.json` — root-level, applies regardless of which AI tool is driving `git`)

Hooks run on the `git` command itself. They fire the same way whether a human typed the command or an AI agent did, and regardless of which of the 8 supported tools is running the agent.

- **`commit-msg`** — regex-validates the commit message against `VERSIONING.md` Commit Message Format (a leading `vMAJOR.MINOR.PATCH` followed by a conventional-commit type/scope/summary). A commit with no version prefix is rejected before it is created, not caught later in review. This is the direct mechanical fix for "commits shipped without a version bump."
- **`pre-commit`** — runs the fast subset of `QA_CHECKLIST.md` Build Quality: lint, typecheck, and a file-size check that rejects any staged file over the 600-line limit in `DEVELOPMENT_RULES.md`. Also runs a secrets scan (see below) on the staged diff.
- **`pre-push`** — blocks a push targeting `main` unless a local `PHDK_FINETUNING_MODE=1` environment variable is set. This is the mechanical form of Finetuning Mode's exception: the human sets the variable to activate it, rather than the AI needing to remember it is active. Branch protection above is the real backstop (a local hook can be bypassed on a local machine); this hook exists so the block happens before a push attempt even reaches GitHub.

### Secrets scanning (mechanical enforcement of "never commit secrets")

- A pre-commit secrets scan (e.g. a `gitleaks`-class tool, or an equivalent pre-commit-hook-compatible scanner) runs on every staged diff, not just on `.env` files by name — a secret pasted into a config file, a test fixture, or a comment is caught the same way.
- A scan finding is a hard block on the commit, not a warning to note and continue past.
- This is in addition to, not instead of, `DEVSECOPS.md` Environment Variable Rules and Secrets Rotation and Compromise Response — the scan catches the accident; that section defines what to do once one gets through anyway.

### CI (GitHub Actions, CI-only per `TASK_TRACKING_STANDARD.md` Local-Only Rule)

- One workflow, triggered on pull request, running `QA_CHECKLIST.md` Required Validation Commands: install, lint, typecheck, build, test.
- Wired into GitHub branch protection above as a required status check.
- This workflow does exactly one job: prove the code is in the state the AI claims. It never tracks tasks, reports status to a dashboard, or gates anything beyond "does the code build and pass its tests" — see `TASK_TRACKING_STANDARD.md` for why task tracking itself must never live here.

### Dependency automation

- Dependabot or Renovate, per `DEVSECOPS.md` Keeping Existing Dependencies Patched — already a Tier 1 mechanism by nature (it opens PRs on a schedule; it does not require anyone to remember to check for updates).

### What Tier 1 already covers from other files

This section does not repeat rules defined elsewhere — it is the index of which already-documented rules have a mechanical backstop. If a rule below is violated, that is a bug in the hook/CI/setting, not a reminder to write a better prompt.

| Rule | Documented in | Mechanically enforced by |
|---|---|---|
| Commit message begins with `vX.Y.Z` | `VERSIONING.md` | `commit-msg` hook |
| No file exceeds 600 lines | `DEVELOPMENT_RULES.md` | `pre-commit` hook |
| Never commit directly to `main` | `DEVELOPMENT_RULES.md` | GitHub branch protection |
| Human reviews the diff before merge | `QA_CHECKLIST.md` Human Diff Review | GitHub required PR approval |
| Build/lint/typecheck/test must actually pass | `VERIFICATION_LOOP.md` | CI required status check |
| Never commit secrets | `DEVSECOPS.md` | `pre-commit` secrets scan |
| Dependencies stay patched | `DEVSECOPS.md` | Dependabot/Renovate |

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

Content stays short — this is injected into every session or every turn depending on the tool, so length defeats the purpose:

- A pointer: read `phdk-standards/AGENTS.md` first, then `phdk-standards/INANUTSHELL.md` if the session has been running a while.
- The smallest set of rules severe enough to inline verbatim so they survive even if the pointer above is never followed: never commit directly to `main`, never force-push, never weaken auth/RBAC/validation to make something work; every commit message starts with `vX.Y.Z`; a working slice needs verification evidence, not "should work"; stop and ask before destructive DB operations, auth/payment/tenant changes, new external services, or a metered API with no cost cap; read `TASK.md` and `STATUS.md` before doing anything else this session.

This file is generated once, then kept in sync by the same update flow `SKILL.md` already uses for `phdk-standards/` — when `phdk-standards/INANUTSHELL.md` changes upstream, the inlined block above is diffed against it and the developer is told to confirm the update, same as any other vendored-standards change.

### Session-start ritual, made mechanical where the tool allows it

- Where the current tool supports a session-start or first-prompt hook (a hook that runs before the first response in a session), wire it to print `phdk-standards/INANUTSHELL.md` into context automatically — this replaces "the AI is instructed to read it" with "the AI cannot start without having seen it."
- Where no such hook exists, the tool-native always-loaded rule file above is the fallback — it is present without requiring a hook mechanism, because the tool loads it unconditionally by convention.

### The commit-time reminder

Every `commit-msg` hook invocation (Tier 1, above) also prints the Tier 2 hard-rules block from the tool-native rule file to stdout after a successful commit. This is deliberate, low-cost redundancy: it re-surfaces the highest-severity rules at the single most frequent, most mechanically-guaranteed touchpoint in the entire workflow — a commit happens every few minutes in an active session, far more often than a human would think to say "hey, re-read the standards." A long session that has drifted from the rules gets re-exposed to them dozens of times before it ends, without anyone having to notice the drift first.

---

## What This Does Not Solve

Being honest about the limits matters more here than anywhere else in PHDK, per the Ethos Rules in `AI_DEVELOPER_OPERATING_MODEL.md`.

- Tier 1 only works for what can be expressed as a check. "Understand the human's actual goal before writing code" has no lint rule. Tier 2 narrows how often this kind of rule gets forgotten; it does not guarantee it never is.
- A local git hook can be bypassed, or is simply absent if a developer's machine never ran the setup step. GitHub branch protection is the real backstop for anything security-critical for exactly this reason — never rely on a local hook alone for something that must never happen.
- None of this replaces a human actually reading `STATUS.md` and the diff periodically. Tooling raises the floor; it does not remove the need for the feedback loop in `AI_DEVELOPER_OPERATING_MODEL.md`.

---

## Never

- Never write a new PHDK rule that has an obvious Tier 1 equivalent (a regex, a repo setting, a CI check) as prose only, without also adding the mechanical version here
- Never treat a bypassed local hook as routine — it is the same class of action as force-pushing or pushing directly to `main`, and belongs in `VERSIONING.md` Stop-and-Ask Conditions
- Never let the tool-native rule file (Tier 2) drift out of sync with `INANUTSHELL.md` — a stale inlined rule block is worse than none, because it creates false confidence that the AI is current
- Never generate rule files for tools the project isn't using "just in case" — this bloats the repo with dead configuration nobody maintains

---

## Verification

- [ ] GitHub branch protection on `main` requires a PR, at least one approval, and passing status checks, and disallows force-push
- [ ] `commit-msg` hook rejects a commit with no `vX.Y.Z` prefix
- [ ] `pre-commit` hook rejects a staged file over 600 lines and runs a secrets scan
- [ ] `pre-push` hook blocks a push to `main` unless `PHDK_FINETUNING_MODE=1` is set locally
- [ ] CI workflow runs install/lint/typecheck/build/test on every PR and is a required status check
- [ ] Dependabot or Renovate is configured
- [ ] The current tool's native always-loaded rule file exists at the correct path for that tool and is not a stale copy of an old `INANUTSHELL.md`
- [ ] A test commit with an intentionally malformed message was actually rejected by the hook, not just assumed to work
