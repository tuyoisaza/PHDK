# INTENT_CAPTURE_STANDARD.md

## Purpose

This file defines when and how to capture the *why* behind a feature, bug, or body of work as a durable, git-committed, human-reviewable artifact — before scoping (`TASK.md`) or building starts.

It extends `SPEC_INTERVIEW_PROMPT.md`'s one-time, project-level interview down to individual asks that arrive later, mid-project, from anyone: a stakeholder, a customer bug report, a teammate, a scheduled maintenance trigger, or the AI itself diagnosing an incident.

Its goal is that the reason a piece of work exists survives a context reset, a different AI tool picking up the thread, or months passing — the same way `TASK_TRACKING_STANDARD.md` makes sure the *plan* survives, and `CHANGELOG.md` makes sure the *outcome* survives.

---

## Status

Read this file when:

- a new feature or bug ask arrives that is not already covered by `PROJECT_BRIEF.md`, `PRD.md`, or `FEATURES.md`
- the person asking for the work is not the person who will implement or verify it
- an incident, alert, or scheduled check surfaces something that needs a fix and the reason isn't self-evident from the log line alone
- starting `TASK.md` for a new slice, to decide whether that slice needs an intent file behind it

---

## Core Rule

An intent file captures the problem and the desired outcome, separately from the plan and separately from the code. It is written and reviewed *before* scope is confirmed in `TASK.md`.

This is not a spec. It does not describe files, routes, or implementation. If it starts describing how something will be built, that content belongs in `TASK.md`'s `Slice` section instead.

---

## When to Write One

Write an intent file when:

- A new feature or bug's *why* is not already fully covered by `PROJECT_BRIEF.md` / `PRD.md` / `FEATURES.md`
- The work originates outside the current session — a ticket, a Slack message, a support report, a scheduled or monitoring-triggered check
- The originator of the ask is not the same person who will implement or verify it

Skip it when:

- The slice is purely mechanical execution of something already fully specified in `FEATURES.md` or `PRD.md`
- The change is a one-line trivial fix with an obvious, undisputed reason

When in doubt, write one. A short intent file costs little; a lost "why" costs a rediscovery conversation later.

---

## Format

Create the file at `docs/intents/<short-name>-intent.md`:

```md
# Intent — <short name>

## Originator
[Who is asking for this, and how it arrived — a person's name/role, a ticket link, an incident, etc.]

## Problem
[What pain, gap, or risk this addresses. Not the solution — the problem.]

## Desired Outcome
[What success looks like, in terms of what a person can do, see, or no longer worry about.]

## Constraints / Non-Goals
[What this must not become, any hard constraints, and anything explicitly out of scope.]

## Open Questions
[Anything unresolved that scoping (TASK.md) will need to settle.]

## Linked Slices
[TASK.md / docs/completed-slices/ entries this intent has produced, added to as they happen.]
```

---

## Optional Capture Interview

For an ask that arrives as a short, informal request (a one-line bug report, a vague feature ask), use a short interview instead of writing the file directly:

1. Who is asking for this, and what prompted it right now?
2. What problem or pain does this address — what happens today without it?
3. What does success look like when this is done?
4. Is there anything this must not become, or anything explicitly out of scope?
5. Anything unresolved that needs to be settled before scoping starts?

This is deliberately shorter than `SPEC_INTERVIEW_PROMPT.md`'s 14-question project-level interview — it is scoped to one ask, not a whole product.

---

## File Location and Lifecycle

- Intent files live in `docs/intents/`, one file per intent.
- An intent file is created once and never overwritten. Unlike `TASK.md`, which is replaced when a slice closes, an intent can span multiple slices and multiple `TASK.md` cycles over time — it is a permanent record, not a rotating current-file.
- Never delete an intent file. If the work it describes is abandoned, add a line under `Open Questions` noting that and why, rather than removing the file.
- As slices that implement an intent close, add a pointer to each closed slice's archived `TASK.md` (per `TASK_TRACKING_STANDARD.md`) under the intent's `Linked Slices` section.

---

## Review Step

Intent capture must preserve the originator's meaning, but it is not a mandatory approval pause. If the current user is the originator and their request already clearly states the problem, desired outcome, and relevant constraints, write the intent file from that request and continue into mission scoping without asking them to confirm their own words again.

If the intent was reconstructed from an external source, delegated by someone else, or contains a material ambiguity that could change the mission, get the originator's review before acting on the ambiguous part. Ask only the decision that actually blocks safe scoping.

---

## Relationship to Existing Files

- **`PROJECT_BRIEF.md` / `PRD.md` / `FEATURES.md`** — the project-level equivalent, captured once at project inception via `SPEC_INTERVIEW_PROMPT.md` and `PROJECT_HANDOFF_TO_DEVELOPMENT_KIT_PROMPT.md`. An intent file is not a replacement for these — it is the missing middle layer for asks that arrive *after* project inception and are not already covered by them.
- **`TASK.md`** — reads the reviewed intent file's `Problem` and `Desired Outcome` when defining the slice's user-visible outcome (`AGILE_SLICE_WORKFLOW.md` Step 1) and references it via the `Intent:` field in `TASK.md`'s `Slice` header (`TASK_TRACKING_STANDARD.md`).
- **`STATUS.md`** — does not track intents directly; intents are tracked via the `Linked Slices` section inside each intent file itself, plus the normal `TASK.md`/`STATUS.md` slice lifecycle.

PHDK deliberately does not add a separate `spec.md` artifact on top of this. `PROJECT_BRIEF.md`/`PRD.md`/`FEATURES.md` plus `TASK.md`'s `Slice` header already cover requirements and design scope; a third layer would be exactly the kind of ceremony `AGILE_SLICE_WORKFLOW.md` warns against for small slices.

---

## Anti-Patterns

- Writing an intent file that describes implementation details instead of the problem and desired outcome
- Asking the current originator to reconfirm an intent that already faithfully captures their explicit request
- Acting on a materially ambiguous externally-originated intent without resolving the ambiguity
- Treating a trivial, undisputed one-line fix as requiring an intent file
- Overwriting or deleting an intent file instead of updating its `Linked Slices` and `Open Questions`
- Skipping intent capture for an ask that arrived from outside the current session just because writing the file feels like overhead

---

## Verification

- [ ] An intent file exists for any feature/bug not already covered by `PROJECT_BRIEF.md`/`PRD.md`/`FEATURES.md`
- [ ] The intent file's originator reviewed and confirmed it before scoping began
- [ ] `TASK.md`'s `Slice` header references the intent file via its `Intent:` field, or explicitly states none applies
- [ ] The intent file describes the problem and desired outcome, not implementation
- [ ] Closed slices that implemented the intent are linked back under its `Linked Slices` section
- [ ] No intent file was deleted or overwritten
