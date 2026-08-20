# VERSIONING.md

## Purpose

This file defines how PHDK projects track versions, commits, branches, changelogs, visible build metadata, and release progress.

Its goal is to make AI development traceable across sessions and recoverable at any point.

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

Every project maintains a visible version in these locations:

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
- Every working slice starts on its own branch
- Checkpoint branches are created before major updates as recoverable backups
- Merge only after verification passes and approval is given

---

## Commit Message Format

```txt
v0.3.0 feat(slice): add Google OAuth login
v0.3.1 fix(auth): handle OAuth callback failure
v0.3.1 docs(phdk): update status after dashboard slice
v0.3.0 chore(version): bump to v0.3.0
v0.3.2 refactor(api): extract auth service
v0.3.2 test(auth): add OAuth callback tests
```

For projects with multiple independently versioned components (e.g. a `server` and a `plugin` in the same repo), list each affected component's version, comma-separated, before the conventional-commit message:

```txt
server v0.2.16, plugin v0.4.11 - feat(prompt): show installed plugin version
```

Rules:

- For release commits, the commit message must begin with the current version (`vX.Y.Z`), or with each affected component's version for multi-component projects — the conventional-commit type/scope/summary follows it
- Use `feat`, `fix`, `chore`, `refactor`, `test`, `docs` prefixes
- Scope to the feature or area changed
- Keep messages short and specific
- Do not create noisy version bumps for every minor feature branch commit — the version prefix applies to release commits, not every intermediate commit on a feature branch

---

## Working Slice Version Rule

Each completed and approved working slice results in:

- Verified user-visible outcome
- Updated `STATUS.md`
- Updated `CHANGELOG.md` when user-facing behavior changed
- Version bump when appropriate
- Commit with descriptive message
- Push to feature branch
- Merge to `main` only after explicit approval

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
Commit: [short SHA or pending]
Verification: [pass/fail/partial]
Health: [/health result]
Deep health: [result or not applicable]
Debug diagnostics: [safe/not tested/not applicable]
Known issues: [list or none]
Next suggested slice: [proposal]
```

---

## Version Metadata in the App

The app must expose version metadata in these locations:

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

- [ ] Version is visible in app shell, login page, and admin panel
- [ ] `/health` returns correct version
- [ ] `CHANGELOG.md` is updated for user-facing changes
- [ ] `STATUS.md` reflects current state
- [ ] Commit message follows the format
- [ ] Branch name follows the format
- [ ] No direct commits to `main` without approval
