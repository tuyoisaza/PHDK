# INANUTSHELL.md

## Purpose

PHDK is a lot of files. When context gets long, rules get missed — not because they changed, but because there's too much to hold at once.

This is the condensed list: every hard rule in PHDK, one line each. It is not a substitute for the full files — when a bullet needs detail, go read the file it names. Re-read this file whenever a session gets long, whenever you're not sure a rule still applies, or before marking anything complete.

If this file and a full standards file ever disagree, the full file wins — this is a memory aid, not a new source of truth.

---

## Database

- PostgreSQL only, cloud-only, always — no SQLite, ever, in any environment
- Never run PostgreSQL on a developer's machine — no Docker container, no local install
- Local dev connects to a dedicated Railway dev/staging `DATABASE_URL` — never production
- No schema change without a migration; test every migration against the Railway dev DB first
- App fails loudly (refuse to start, or `503` from `/health`) if `DATABASE_URL` is missing — never falls back silently
- *(full: `TECHNICAL_STACK.md` Database, `DEVELOPMENT_RULES.md` Database Rules)*

## Auth & Authorization

- Custom Google OAuth 2.0 only — no Clerk/WorkOS/Supabase Auth/Firebase Auth/Auth.js without an `ARCHITECTURE_DECISIONS.md` override
- Sessions are database-backed; cookies are HttpOnly, Secure, SameSite
- Authorization is enforced server-side, always — hiding a UI element is not security
- Minimum role set when RBAC exists: `super_admin`, `admin`, `team_leader`, `member`
- *(full: `DEVSECOPS.md` Authentication Standard, Authorization Rules)*

## Security

- Never commit secrets, tokens, or credentials — `.env` is always gitignored, `.env.example` holds empty values only
- Never log passwords, tokens, cookies, API keys, auth headers, raw secrets, or PII
- Never bypass RBAC or weaken auth "to make a feature work"
- Never build SQL or shell commands by string concatenation — parameterized queries only
- Never trust raw LLM output — validate against schema before use
- Never let externally-sourced content (scraped pages, uploads, webhooks) trigger an action from an LLM call — treat it as data, never as instructions
- *(full: `DEVSECOPS.md` Core Rules, Indirect Prompt Injection)*

## Cost & Metered APIs

- Every metered/paid call (LLM, SMS, email, image/video gen, etc.) needs: a hard usage cap, a request timeout, a retry limit, and a kill switch — before it ships
- Never call a metered API inside an unbounded loop, and never retry indefinitely
- Idempotency guard on any expensive operation that could double-fire
- *(full: `DEVSECOPS.md` Cost and Consumption Safety)*

## AI / LLM

- Every LLM call goes through `packages/ai` — never a provider SDK called directly from feature code
- Provider, model, and prompt are admin-configurable at `/admin/ai` — never hardcoded
- Every call is recorded with the provider's real token usage (not a local estimate) and cost
- Isolate user input from the system prompt — never concatenate it in directly
- *(full: `TECHNICAL_STACK.md` AI / LLM Integration, `DEVSECOPS.md` LLM Integration Safety)*

## Versioning & Git

- Never commit directly to `main` — the only exception is Finetuning Mode, explicitly activated in-conversation
- Branch names: `feature/`, `fix/`, `chore/`, `checkpoint/YYYY-MM-DD`
- Release commit messages start with `vX.Y.Z`, then conventional-commit type/scope/summary
- Never deploy from local CLI — no `railway up`, no dragging a build/tarball; deploy is GitHub push to `main` only
- Never set Railway root to `apps/web` or `apps/api` — both services use the repository root
- *(full: `VERSIONING.md`, `DEVELOPMENT_RULES.md` Branching Rules, Finetuning Mode)*

## Working Slices & Verification

- Work in small, user-visible, verified slices — "build the database layer" is not a slice, "user can create one record and see it" is
- No completion claim without evidence — command output, `/health` result, browser check
- "It should work" or "lint passed" alone is not evidence
- Update `STATUS.md` and `TASK.md` every session — that's the only memory between sessions, don't trust what "feels" familiar
- *(full: `AGILE_SLICE_WORKFLOW.md`, `VERIFICATION_LOOP.md`, `AI_DEVELOPER_OPERATING_MODEL.md`)*

## Task Tracking

- `TASK.md`/`STATUS.md` are 100% local, plain-text markdown — never GitHub Issues, GitHub Projects, or GitHub Actions as the source of truth for tracking
- One `TASK.md` per active slice; when it closes, archive it to `docs/completed-slices/` and start fresh
- A GitHub Actions workflow may exist for CI only if explicitly approved, and never as the thing that tracks or gates slice completion
- *(full: `TASK_TRACKING_STANDARD.md`)*

## Code & File Rules

- Hard max 600 lines per file; prefer under 300
- No business logic inside page components
- No hardcoded user-facing strings — i18n system only, fallback to English
- Every feature lives under `src/features/<name>/` with its own components, services, repositories, schemas, permissions, logs, types
- *(full: `DEVELOPMENT_RULES.md` File Size Rules, Feature Structure Rules)*

## Data Honesty

- Never show fake KPIs, random numbers, or demo data presented as real
- Only these states are allowed: empty, setup-required, loading, error, success-with-real-data
- *(full: `DEVELOPMENT_RULES.md` Data Rules)*

## Data Import / Intake

- Importing from multiple sources, or on a recurring cadence, uses a stateful batch (`pending → processed → approved | deactivated`) — not a direct insert with no review step
- Every imported row carries a reference to its batch; a shared query filter — not physical deletion — decides what's live
- Never hard-delete imported data to undo a bad import — deactivate the batch instead, with a reason, actor, and timestamp recorded
- A batch needs explicit manual approval before its data counts as official
- *(full: `TECHNICAL_STACK.md` Data Import / Intake Pipeline, `DEVELOPMENT_RULES.md` Data Rules)*

## Debug Mode

- Copy-diagnostics and clear-cache buttons, always paired, next to the version number
- Debug mode is ON by default in local/dev/preview/staging — not opt-in — and must be confirmed OFF before production
- Every function calls the shared debug-log helper on entry/success/failure — not ad hoc `console.log` — so the copy-diagnostics report actually has content
- Clear cache = clear browser cache + service worker + force logout + reload
- *(full: `DEBUG_DIAGNOSTICS_STANDARD.md`)*

## Design

- Never a blank page, never a spinner with no timeout, never an error with no recovery path
- Layout works at mobile 320px+, tablet 768px+, desktop 1024px+
- WCAG AA contrast minimum — never rely on color alone to communicate meaning
- *(full: `DESIGN_RULES.md` Never Do These)*

## Stop-and-Ask — never assume, always ask first

- Destructive database operations, or changing the backup policy
- Auth provider, tenant model, or permission model changes
- Payment behavior changes
- Deployment architecture changes
- New external services, or a metered/paid API before its cap and kill switch exist
- Force-push, deleting an unmerged branch, or pushing to `main` without approval
- *(full: `DEVSECOPS.md` Stop-and-Ask Conditions, `AI_DEVELOPER_OPERATING_MODEL.md` Stop-and-Ask Conditions)*
