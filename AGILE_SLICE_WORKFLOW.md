# AGILE_SLICE_WORKFLOW.md

## Purpose

This file defines the working slice model for PHDK projects.

Its goal is to prevent waterfall-style AI development where nothing visible is produced until everything is built.

All steps operate inside `EXECUTION_SCOPE.md`: repository code/documentation and git/GitHub in the active session, with only allowed local code checks and an existing GitHub deployment pipeline.

---

## Core Rule

A working slice implements the smallest useful product outcome that can be reviewed in source, verified locally, and committed.

Every slice must produce something a human can see, use, or test.

Infrastructure alone is not a working slice.

A passing build alone is not a working slice.

A code slice is complete when the approved implementation criteria have source/diff evidence and applicable local checks pass. Browser/UI and live runtime behavior remain unverified; they do not become a required manual testing task for the human.

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

If the human provides a new feature or bug ask that is not already covered by `PROJECT_BRIEF.md`, `FEATURES.md`, or `PRD.md`, capture it first as `docs/intents/<name>-intent.md` per `INTENT_CAPTURE_STANDARD.md`. Request clarification only when that standard requires it for ambiguous intent; do not ask the current originator to reconfirm a clear request. Reference it in `TASK.md`'s `Intent:` field. Do not create work from a scheduled check, bot, monitoring trigger, or a self-assigned maintenance task.

Before writing code, state clearly:

```txt
User-visible outcome: [what the user can do or see when this slice is complete]
Why it matters: [how it moves the product forward]
```

### Step 2 — Confirm mission boundary

Before coding, the mission must have enough information to act:

```txt
Mission goal: [what must be true when all work is done]
Done when: [objective code/documentation completion criteria]
In scope: [features/areas the AI developer may touch]
Out of scope: [what must not be added]
Stop-and-ask conditions: [true human-decision boundaries within EXECUTION_SCOPE.md]
Plan: [ordered working slices]
```

If the user already supplied a brief, accepted plan, or `TASK.md` containing these facts, **do not ask for confirmation again**. Their request is the approval to execute that mission.

Ask only when a missing decision materially prevents safe implementation.

### Step 3 — Work autonomously inside scope

Continue the approved code mission inside the active session and `EXECUTION_SCOPE.md`.

Make reasonable implementation decisions without asking for permission on routine details.

When an allowed local check fails, diagnose, revise, and rerun the affected check autonomously. Do not create background agents, recurring work, or external triggers to continue the mission later.

Stop only at a documented mission boundary or genuine blocker. Ask one precise question there and wait.

### Step 4 — Verify

Do not self-report completion without evidence appropriate to the change. Follow `VERIFICATION_LOOP.md` and `TESTING_STANDARD.md` within `EXECUTION_SCOPE.md`.

Review or run, as applicable:

- Source and diff against the approved acceptance criteria
- Local build, typecheck, lint, and format checks
- Unit or in-process integration tests when required by risk

Do not run browser tests, headless browsers, screenshots, Playwright/Puppeteer/Cypress/Selenium, live HTTP or health/probe checks, or database/cloud operations. Product diagnostic code can be inspected and tested in process without exercising the live product. For documentation-only changes, a source/diff and reference review is sufficient.

### Step 5 — Show proof

Produce evidence:

```txt
Source/diff review result
Allowed local commands run and their output
Risk-triggered unit/in-process integration results, when applicable
Browser/UI/live runtime: not verified; outside execution scope
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

If source review, an allowed local check, or human-supplied evidence identifies a defect, fix it and re-verify locally without handing the work back to the user.

If a revision remains inside mission scope, no new approval is required.

### Step 8 — Commit and push the verified slice

Follow the commit format from `VERSIONING.md`.

Commit and push to the **mission feature branch** once the slice is verified. This does not require a separate approval.

Do not merge to `main` without explicit Human Diff Review approval, and do not treat the AI's own verification evidence as that approval. The merge gate applies once at mission completion, not between slices. See `QA_CHECKLIST.md` Human Diff Review.

A requested deployment uses an approved push through the existing GitHub-connected pipeline. Do not create or modify CI workflows, schedules, repository settings, service configuration, or a replacement deployment mechanism.

### Step 9 — Archive TASK.md and update STATUS.md

Archive the closed slice's `TASK.md` to `docs/completed-slices/<vX.Y.Z>-<slice-name>.md`, per `TASK_TRACKING_STANDARD.md`.

Record in `STATUS.md`:

- What was completed, with a pointer to the archived `TASK.md`
- Current version
- Gaps flagged
- Open questions
- Next step

### Step 10 — Continue or finish the mission

If code completion criteria are not yet satisfied, create the next `TASK.md` slice from the existing mission plan and continue within the active session. If the session ends, save the next step without scheduling a restart.

If they are satisfied, produce the Mission Complete report and present the branch/diff for Human Diff Review before merge.

Recommendations outside the mission remain proposals; do not implement them, schedule maintenance, or launch another agent to work on them after the session.

---

## Slice Sizing Rules

A slice is too big if:

- It takes more than one focused session to complete
- It produces nothing visible until the very end
- It requires building multiple independent systems before anything works
- Its implementation criteria cannot be assessed from a coherent source change and focused local checks

A slice is the right size if:

- It produces one clear user-visible outcome
- Its code can be verified by source/diff review and focused local checks
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
Verification plan: [source/diff review and allowed local checks]
Estimated complexity: [low / medium / high]
```

---

## First Slice Rule

For an approved new-project build, the first slice is:

```txt
Fetch the latest standards from the standards repo.
Read EXECUTION_SCOPE.md, AI_DEVELOPER_OPERATING_MODEL.md, TASK.md, and STATUS.md.
Implement the initial app foundation code using BUILD_APP_FOUNDATION_PROMPT.md.
Review the health-route implementation if required and run applicable allowed local checks.
Record repo structure and code evidence, then continue to the next planned code slice in this session unless the foundation mission is complete or blocked.
```

The foundation slice is complete only when:

- The repo structure matches the standard
- Required route and health-response contracts are implemented in source
- The web app source includes the planned pages and states
- Applicable local build, typecheck, lint, and format checks pass
- The README documents how to run the project locally
- Browser/UI and live runtime verification are explicitly reported as not performed

Foundation work does not create external services, database instances, GitHub Actions workflows, schedules, or deployment integrations. Missing external setup is documented without making the code completion report depend on the human performing browser tests or service setup.

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
- Claiming live UI/runtime behavior was verified when only code checks were performed
- Running browser tests, live probes, or external operations to complete a code slice
- Creating recurring tasks or background agents from the backlog
- Skipping `STATUS.md` updates between sessions
- Expanding the approved mission goal or out-of-scope boundary without approval
- Proposing slices that are not grounded in the PHDK product files
- Stopping after every slice to ask the human to say "continue"
- Treating a planned next slice inside the approved mission as scope expansion
