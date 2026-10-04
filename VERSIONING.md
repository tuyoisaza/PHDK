# VERSIONING.md

## Purpose

This file defines how PHDK projects track versions, commits, branches, changelogs, visible build metadata, and release progress.

Its goal is to make AI development traceable across sessions and recoverable at any point.

`EXECUTION_SCOPE.md` applies to versioning and release work. Update repository metadata and use git/GitHub; verify source and local output. Do not inspect a live UI, call health endpoints, create release automation, or operate deployment services.

---

## Status

This file is enforced for working slices, commits, releases, and deployed builds.

Read this file when:

- starting a working slice
- finishing a working slice
- committing changes
- bumping app version
- preparing a release
- updating `STATUS.md`
- updating `CHANGELOG.md`
- showing version information in the UI
- reporting deployed build information

---

## Version Source of Truth

Product code must expose a consistent version in the applicable locations below. These are implementation requirements, not permission for the agent to open the UI or call live endpoints:

- `package.json` at the workspace root
- `CHANGELOG.md`
- `STATUS.md`
- App shell UI
- Login page if login exists
- Admin or system page if admin exists
- Debug diagnostics report
- `/health` endpoint response
- Protected `/health/deep` endpoint if available

---

## Version Format

```txt
vMAJOR.MINOR.PATCH (shortSHA · UTC build timestamp)
```

Example:

```txt
v0.4.12 (a1b2c3d · 2026-03-23 18:22 UTC)
```

### Version bump guidance

- **patch** — fixes, small internal changes, copy updates, dependency patches
- **minor** — new working slice, new user-visible feature, new route
- **major** — breaking changes, architecture changes, data model changes, auth model changes

---

## Branch Naming

```txt
feature/<feature-name>
fix/<issue-name>
chore/<task-name>
checkpoint/YYYY-MM-DD
phdk/vX.Y.Z/short-slice-name
```

Examples:

```txt
feature/google-oauth-login
fix/auth-callback-failure
checkpoint/2026-03-23
phdk/v0.3.0/login-google-oauth
```

Rules:

- Never commit directly to `main` (unless Finetuning Mode is explicitly active — see `DEVELOPMENT_RULES.md` Finetuning Mode)
- Every **mission** starts on its own feature branch; planned slices inside that mission stay on the same branch
- Checkpoint branches are created before major updates as recoverable backups
- Locally verified slices may commit and push to the mission branch during the active session
- Merge the completed mission to `main` only after verification and Human Diff Review approval

---

## Commit Message Format

Every commit begins with the version that commit produces — not only release commits, and not only commits that land on `main`.

```txt
v0.3.0 feat(slice): add Google OAuth login
v0.3.1 fix(auth): handle OAuth callback failure
v0.3.2 docs(phdk): update status after dashboard slice
v0.3.3 refactor(api): extract auth service
v0.3.4 test(auth): add OAuth callback tests
```

For projects with multiple independently versioned components (e.g. a `server` and a `plugin` in the same repo), list each affected component's version, comma-separated, before the conventional-commit message:

```txt
server v0.2.16, plugin v0.4.11 - feat(prompt): show installed plugin version
```

Rules:

- Every commit message must begin with the version that commit produces (`vX.Y.Z`), or with each affected component's version for multi-component projects — the conventional-commit type/scope/summary follows it
- This applies to every commit on every branch — feature branches, fixes, chores, and docs included. There is no such thing as an unversioned commit
- Every commit bumps the version by at least a patch — see Version Bump on Every Commit below
- This rule is enforced by a local `commit-msg` hook when each commit is created and by an outgoing-commit range check in `pre-push` before pushing — see `ENFORCEMENT.md`. These code checks may be scaffolded and run locally; do not create Actions workflows, scheduled jobs, or bots to enforce the rule
- Use `feat`, `fix`, `chore`, `refactor`, `test`, `docs` prefixes
- Scope to the feature or area changed
- Keep messages short and specific

---

## Version Bump on Every Commit

Every commit increments the version by at least a patch. No two commits share a version number.

For each commit:

1. Choose the increment using Version bump guidance above — patch is the floor, minor or major when the change warrants it.
2. Update the version in `package.json` at the workspace root as part of that same commit, never as a separate follow-up.
3. Write the commit message with the resulting version as its prefix.

Why this is absolute:

- A requested deployment uses an approved GitHub push to `main` and the existing pipeline (see `DEVSECOPS.md` Deployment Safety Rules). A distinct version and commit identifier in the generated metadata make the built artifact traceable to its source.
- A fix that ships without a bump is indistinguishable in version metadata from the build before it. Verify the source/build metadata locally; this does not establish that the live deployment is healthy or authorize checking the running site.

Version numbers consumed on a feature branch that never merges are spent. Gaps in the sequence are expected and correct — never reuse, renumber, or backfill a version to close a gap.

`CHANGELOG.md` is not written once per commit. It is written per user-facing change, under the version that shipped it (see Changelog Format).

---

## Working Slice Version Rule

Each completed working slice inside an approved mission results in:

- Implemented product outcome with source/diff and applicable local code evidence
- Updated `STATUS.md`
- Updated `CHANGELOG.md` when user-facing behavior changed
- Version bumped on every commit in the slice, per Version Bump on Every Commit
- Commit with descriptive message
- Push to the mission feature branch without requiring a separate slice-level approval
- Continue to the next planned code slice in the active session until the mission is done; never schedule a restart or follow-up job
- Merge the completed mission to `main` only after explicit Human Diff Review approval

---

## Changelog Format

```md
## vX.Y.Z — YYYY-MM-DD

### Added
-

### Changed
-

### Fixed
-

### Verification
-

### Known Issues
-
```

---

## Slice Release Report Format

At the end of every working slice, report exactly:

```txt
Slice: [slice name]
Version: [vX.Y.Z]
Branch: [branch name]
Commit: [short SHA]
Mission branch: [branch]
Code verification: [pass/fail/partial + source/local evidence]
Browser/UI/live runtime: not verified; outside execution scope
Deployment: [not requested / existing GitHub pipeline triggered / unavailable]
Known issues: [list or none]
Next planned code slice: [inside the active mission or none]
```

---

## Version Metadata in the App

When these product surfaces exist, their source must expose version metadata as specified below. Inspect the implementation and local build output; do not exercise a browser, live endpoint, or database to verify it.

### UI locations

- App shell — version badge near logo
- Login page — version number in footer or corner
- Admin panel — version with full metadata

### API locations

```json
GET /health
{
  "status": "ok",
  "service": "api",
  "version": "v0.4.12",
  "environment": "production"
}
```

```json
GET /health/deep (protected)
{
  "status": "ok",
  "version": "v0.4.12",
  "gitSha": "a1b2c3d",
  "buildTime": "2026-03-23T18:22:00Z",
  "environment": "production",
  "database": "connected",
  "migrations": "current",
  "uptime": 3600
}
```

---

## Stop-and-Ask Conditions

Stop before:

- Force-pushing to any branch
- Deleting branches that have not been merged
- Rewriting git history
- Tagging a release without approval
- Pushing directly to `main` without approval (Finetuning Mode, explicitly activated for the current conversation per `DEVELOPMENT_RULES.md`, is the one standing exception)
- Bumping a major version without approval
- Changing the release or versioning strategy

---

## Verification

Versioning work is complete when:

- [ ] Applicable UI source binds the correct version in the app shell, login page, and admin panel
- [ ] Health/diagnostics response code uses the same version source when those features exist
- [ ] Local metadata and applicable code checks were reviewed; browser/UI/live runtime behavior was not verified
- [ ] `CHANGELOG.md` is updated for user-facing changes
- [ ] `STATUS.md` reflects current state
- [ ] Every commit message begins with the version it produces
- [ ] Every commit bumped the version by at least a patch, with `package.json` updated in the same commit
- [ ] Commit message follows the format
- [ ] Branch name follows the format
- [ ] No direct commits to `main` without approval
- [ ] No Actions workflows, schedules, bots, external deployment configuration, or manual browser-testing gates were added; local git hooks remain code checks only
