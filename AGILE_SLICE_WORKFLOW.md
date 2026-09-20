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

Every working slice follows this lifecycle inside the active mission. Slices are execution checkpoints, not approval gates.

### Step 1 — Define the user-visible outcome

If this slice originates from a new feature or bug ask that is not already covered by `PROJECT_BRIEF.md`, `FEATURES.md`, or `PRD.md`, capture it first as `docs/intents/<name>-intent.md` per `INTENT_CAPTURE_STANDARD.md`, and have its originator review it before continuing. Reference it in `TASK.md`'s `Intent:` field. This is conditional, not a new mandatory step for every slice — see `INTENT_CAPTURE_STANDARD.md` for when it applies.

Before writing code, state clearly:

```txt
User-visible outcome: [what the user can do or see when this slice is complete]
Why it matters: [how it moves the product forward]
```

### Step 2 — Confirm mission boundary

Before coding, the mission must have enough information to act:

```txt
Mission goal: [what must be true when all work is done]
Done when: [objective completion criteria]
In scope: [features/areas the AI developer may touch]
Out of scope: [what must not be added]
Stop-and-ask conditions: [true human-decision boundaries]
Plan: [ordered working slices]
```

If the user already supplied a brief, accepted plan, or `TASK.md` containing these facts, **do not ask for confirmation again**. Their request is the approval to execute that mission.

Ask only when a missing decision materially prevents safe implementation.

### Step 3 — Work autonomously inside scope

Move fast inside the approved mission.

Make reasonable implementation decisions without asking for permission on routine details.

When verification fails, diagnose, revise, and rerun the affected checks autonomously.

Stop only at a documented mission boundary or genuine blocker. Ask one precise question there and wait.

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

### Step 6 — Progress checkpoint, not approval gate

Record the evidence and update continuity files.

If useful, send a concise progress update such as:

```txt
Slice complete: <outcome>
Verification: <key evidence>
Continuing: <next planned slice>
```

Do not ask the user to say "continue." If the human sends feedback, incorporate it into the remaining mission plan.

### Step 7 — Self-revise when needed

If verification or diagnostics find a defect, fix it and re-verify without handing the work back to the user.

If a revision remains inside mission scope, no new approval is required.

### Step 8 — Commit and push the verified slice

Follow the commit format from `VERSIONING.md`.

Commit and push to the **mission feature branch** once the slice is verified. This does not require a separate approval.

Do not merge to `main` without explicit Human Diff Review approval, and do not treat the AI's own verification evidence as that approval. The merge gate applies once at mission completion, not between slices. See `QA_CHECKLIST.md` Human Diff Review.

### Step 9 — Archive TASK.md and update STATUS.md

Archive the closed slice's `TASK.md` to `docs/completed-slices/<vX.Y.Z>-<slice-name>.md`, per `TASK_TRACKING_STANDARD.md`.

Record in `STATUS.md`:

- What was completed, with a pointer to the archived `TASK.md`
- Current version
- Gaps flagged
- Open questions
- Next step

### Step 10 — Continue or finish the mission

If mission completion criteria are not yet satisfied, create the next `TASK.md` slice from the existing mission plan and continue immediately.

If they are satisfied, produce the Mission Complete report and present the branch/diff for Human Diff Review before merge.

Recommendations outside the mission become follow-up proposals; do not silently expand scope to implement them.

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
Record repo structure and verification evidence, then continue to the next planned foundation slice automatically unless the foundation mission is complete or blocked.
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
- Expanding the approved mission goal or out-of-scope boundary without approval
- Proposing slices that are not grounded in the PHDK product files
- Stopping after every slice to ask the human to say "continue"
- Treating a planned next slice inside the approved mission as scope expansion
