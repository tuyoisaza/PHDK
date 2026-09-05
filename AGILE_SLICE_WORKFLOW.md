# AGILE_SLICE_WORKFLOW.md

## Purpose

This file defines the working slice model for PHDK projects.

Its goal is to prevent waterfall-style AI development where nothing visible is produced until everything is built.

---

## Core Rule

A working slice is the smallest useful product outcome that can be built, verified, shown, and committed.

Every slice must produce something a human can see, use, or test.

Infrastructure alone is not a working slice.

A passing build alone is not a working slice.

A working slice is complete only when a human can observe the outcome.

---

## Good Slice Examples

```txt
User can log in with Google and land on a useful first page
User can create one record and see it in a list
User can edit and delete their own record
Admin can invite one user by email
Dashboard shows one real metric pulled from real data
Failed login produces useful and safe debug diagnostics
Public homepage renders with correct content and structure
Contact form submits and user sees a confirmation message
Search returns real results from real data
```

## Bad Slice Examples

```txt
Build the database layer
Build all routes
Build the UI shell
Set up all services
Implement the backend architecture
Scaffold the entire auth system
Create all models
Set up the full API structure
Install and configure all packages
```

Bad slices produce nothing visible or verifiable. They feel productive but deliver nothing the human can confirm or use.

---

## Slice Lifecycle

Every working slice follows this lifecycle in order. Do not skip steps.

### Step 1 — Define the user-visible outcome

Before writing code, state clearly:

```txt
User-visible outcome: [what the user can do or see when this slice is complete]
Why it matters: [how it moves the product forward]
```

### Step 2 — Confirm scope

State what is in scope and what is not:

```txt
In scope: [files, features, areas the AI developer may touch]
Out of scope: [what must not be touched]
Stop-and-ask conditions: [what will trigger a pause]
```

Wait for confirmation before coding.

### Step 3 — Work autonomously inside scope

Move fast inside the confirmed scope.

Make reasonable decisions without asking for permission on every detail.

Stop at boundaries. Ask one question. Wait for the answer.

### Step 4 — Verify

Do not self-report completion without running verification.

Run:

- Build commands
- Type check
- Lint
- `/health` endpoint check
- Browser or test runner check
- Debug diagnostics check if applicable

### Step 5 — Show proof

Produce evidence:

```txt
Commands run and their output
/health result
Browser verification note or screenshot
Debug diagnostics result
Changed files list
Known failures or gaps
```

### Step 6 — Collect feedback

Present the evidence to the user.

Wait for confirmation, correction, or approval.

Do not move to the next slice without feedback.

### Step 7 — Revise if needed

If the user requests changes, revise only what is needed.

Show the updated result.

Wait for approval again.

### Step 8 — Commit and push if approved

Follow the commit format from `VERSIONING.md`.

Push to the feature branch.

Do not merge to `main` without explicit approval, and do not treat the AI's own verification evidence as that approval — a human reading the actual diff is a separate, required gate. See `QA_CHECKLIST.md` Human Diff Review.

### Step 9 — Archive TASK.md and update STATUS.md

Archive the closed slice's `TASK.md` to `docs/completed-slices/<vX.Y.Z>-<slice-name>.md`, per `TASK_TRACKING_STANDARD.md`.

Record in `STATUS.md`:

- What was completed, with a pointer to the archived `TASK.md`
- Current version
- Gaps flagged
- Open questions
- Next step

### Step 10 — Propose next slice

Propose the next user-visible outcome.

Keep proposals small and concrete.

---

## Slice Sizing Rules

A slice is too big if:

- It takes more than one focused session to complete
- It produces nothing visible until the very end
- It requires building multiple independent systems before anything works
- The user cannot verify the outcome without running code themselves

A slice is the right size if:

- It produces one clear user-visible outcome
- It can be verified in the browser or via a health check
- It can be committed as a coherent unit
- The next slice is obvious from the outcome of this one

---

## Slice Planning Format

When proposing a slice, use this format:

```txt
Proposed slice: [name]
User-visible outcome: [what the user can do or see]
Why now: [why this slice comes before others]
In scope: [what will be built]
Out of scope: [what will not be touched]
Depends on: [previous slices or conditions]
Verification plan: [how completion will be proven]
Estimated complexity: [low / medium / high]
```

---

## First Slice Rule

The first slice of every project is always:

```txt
Fetch the latest standards from the standards repo.
Read AI_DEVELOPER_OPERATING_MODEL.md, TASK.md, and STATUS.md.
Build the initial scalable app foundation using BUILD_APP_FOUNDATION_PROMPT.md.
Verify /health responds correctly.
Report back with repo structure, verification evidence, and next slice proposal.
```

The foundation slice is complete only when:

- The repo structure matches the standard
- `/health` responds correctly
- The web app renders without errors
- The build passes
- The README documents how to run the project locally

---

## Backlog Management

After each slice, update the backlog in `STATUS.md`:

```txt
## Completed Slices
- [slice name] vX.Y.Z [date]

## Current Slice
- [slice name] — in progress

## Next Slices
- [slice name] — proposed
- [slice name] — proposed

## Blocked Slices
- [slice name] — blocked by [reason]
```

Keep the backlog honest. Do not add slices that are not confirmed by the PHDK files.

The format of `TASK.md`, `STATUS.md`, and the completed-slice archive is defined in `TASK_TRACKING_STANDARD.md` — including the rule that none of this ever depends on GitHub Issues, GitHub Projects, or GitHub Actions.

---

## Anti-Patterns to Avoid

- Building everything before showing anything
- Claiming a slice is complete without browser or health verification
- Skipping `STATUS.md` updates between sessions
- Expanding scope mid-slice without approval
- Proposing slices that are not grounded in the PHDK product files
- Moving to the next slice without collecting feedback on the current one
