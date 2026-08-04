# VERSIONING.md

## Purpose

This file documents how versioning works in projects built on this standard, including the optional auto version-bump hook.

Like all tooling in this repo, the scripts here are **recommendations**. Adopt them when they fit the project. Skip or adapt them when they do not — the core versioning rules below still apply.

---

# Version Format

Required format, visible in the login page, app shell, and admin panel:

```txt
vMAJOR.MINOR.PATCH (shortSHA · UTC build timestamp)
```

Example:

```txt
v0.4.12 (a1b2c3d · 2026-03-23 18:22 UTC)
```

---

# Versioning Models

## Model 1 — Merge-based (default)

- Version increments on merge to `main`, not on every feature branch commit.
- Noisy per-commit bumps are avoided.
- The version at any point in `main` history maps to a release.

## Model 2 — Auto-bump on every commit (optional)

- A pre-commit hook increments the patch version on every commit.
- Version history maps 1:1 to git history with zero manual effort.
- Bump major/minor manually via `npm version major|minor`; the hook only patches patch.

Choose one model per project and document it in `STATUS.md` or `ARCHITECTURE_DECISIONS.md`. Do not mix them silently.

---

# Files

Optional tooling, generic and copyable into any project that uses a root `package.json`:

```txt
scripts/bump-version.mjs         — pre-commit hook logic: patch+1, write back, git add, print
scripts/prepend-version.mjs      — prepare-commit-msg hook logic: prefix the commit message with the version
scripts/generate-version.mjs     — build-time metadata: writes { version, gitSha, buildTime }
.husky/pre-commit                — one line: node scripts/bump-version.mjs
.husky/prepare-commit-msg        — one line: node scripts/prepend-version.mjs "$1" "$2"
```

---

# Wiring Notes

## One-time setup

```bash
pnpm add -D husky
pnpm exec husky init
```

Add the `prepare` script to the root `package.json` so hooks are regenerated on fresh clones:

```json
{
  "scripts": {
    "prepare": "husky || exit 0"
  }
}
```

Copy the scripts and hook files, then commit them.

## Commit message version

`scripts/prepend-version.mjs` ensures every commit message starts with the current version. It reads `package.json` with `new URL("../package.json", import.meta.url)`, which is cwd-independent and works from any directory.

## Build-time metadata

Wire `scripts/generate-version.mjs` into the `dev` and `prebuild` scripts:

```json
{
  "scripts": {
    "dev": "node scripts/generate-version.mjs && <dev command>",
    "prebuild": "node scripts/generate-version.mjs"
  }
}
```

It writes `{ version, gitSha, buildTime }` to `src/version-generated.json` (dev) and `dist/version.json` (prod).

---

# Gotchas

- The bump runs in `pre-commit`, before the commit is created, so the updated `package.json` lands in the same commit. That is the whole trick.
- `bump-version.mjs` only patches the patch segment. Bump major/minor manually via `npm version`.
- `generate-version.mjs` wraps `git rev-parse` in `try/catch` and returns `"unknown"` when there is no HEAD yet (fresh scaffold).
- `git commit --amend` re-runs `pre-commit` and bumps patch again. Accept this or use `--no-verify` when you do not want the version counted.
- The scripts assume a root `package.json`. In a monorepo, keep the scripts at the repository root and read the root `package.json`.
- The prepare-commit-msg hook skips merge and squash messages so auto-merged history does not get garbled prefixes.

---

# Manual Fallback

Without the hooks, developers write the version manually at the start of every commit message:

```txt
v0.4.12 feat(admin): add debug report panel
```
