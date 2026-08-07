# SPEC_INTERVIEW_PROMPT.md

## Purpose

This file contains the prompt to use when you want to brief an AI on a new project idea before generating a PHDK kit.

Use this prompt when you have an idea but have not yet done a full project brief. It guides the AI to interview you for the human context and goals that the PHDK generation prompt needs.

This is an optional pre-step. If you have already done a deep brief through conversation, skip this file and go directly to the PHDK generation prompt.

---

## When to Use This File

Use this prompt when:

- You have a new project idea but have not briefed the AI yet
- You want a structured interview before generating the PHDK kit
- You want to make sure the brief covers human context, not just technical requirements
- You are starting from scratch and want to think through the project before committing to a spec

Skip this file when:

- You have already briefed the AI through conversation, refinement, and research
- You are ready to go directly to PHDK generation

---

## Prompt

---

⛔ STOP ANY PREVIOUS TASK.

You are now in **SPEC INTERVIEW MODE**.

Your only job is to interview me about a new project so we can build a clear brief before generating a Project Handoff to Development Kit.

Do not generate code.
Do not generate a spec yet.
Do not suggest technical solutions yet.
Do not ask about databases, routes, or frameworks.

First respond exactly:

```txt
Understood. I am now in SPEC INTERVIEW MODE.
I will ask you questions one at a time to understand your project.
I will not suggest technical solutions until the brief is complete.
Let's start.
```

Then ask the questions below one at a time.

Wait for each answer before asking the next question.

Do not ask multiple questions at once.

Do not skip questions unless the answer was already clearly given.

---

## Interview Questions

### Human Context

**Question 1:**
Who is this project for? Describe the person who will use it. Not a demographic — a real person with a real situation.

**Question 2:**
What is that person trying to do or decide? What action does this product help them take?

**Question 3:**
What pain are they experiencing right now? What is the problem they are trying to solve or avoid?

**Question 4:**
What do they use today instead? What is the current workaround, if any?

---

### Goals and Outcomes

**Question 5:**
What does success look like in real life for this person? Not in the app — in their actual life or work.

**Question 6:**
What is the smallest useful outcome this product could deliver? What would make someone say "this is already worth it"?

**Question 7:**
What is your goal with this project? Personal, commercial, service, or creative — be honest about what you want from it.

---

### Product Shape

**Question 8:**
Does this project require users to create accounts and log in? Yes or no, and why.

**Question 9:**
Is any of the data or content sensitive? Does it involve private user information, payments, health data, or anything that requires extra care?

**Question 10:**
Are there workflows that happen before login and workflows that happen after login, or is it all one or the other?

---

### Scope and Vision

**Question 11:**
What is the one thing this product must do well above everything else? If it only did one thing perfectly, what would that be?

**Question 12:**
What should this product never do or become? What would make you consider it a failure?

**Question 13:**
What does the first useful working version look like? What can a user do on day one that makes it real?

**Question 14:**
Is there anything else I should know before we turn this into a spec? Any constraints, inspirations, non-obvious requirements, or strong opinions about how this should feel?

---

## After the Interview

When all questions are answered, produce a short project brief using this format:

```md
# Project Brief

## One-Line Description
[What this is in one sentence]

## The Person
[Who this is for and their situation]

## The Problem
[What pain they are experiencing]

## The Current Workaround
[What they do today]

## The Solution
[What this product does differently]

## Success in Real Life
[What success looks like for the user outside the app]

## The Goal
[What you want from this project — personal, commercial, service, creative]

## Login Required
[yes / no / reason]

## Data Sensitivity
[notes or none]

## The One Thing
[What this must do better than anything else]

## What It Must Never Be
[Constraints or failure conditions]

## First Working Version
[What the user can do on day one]

## MVP Scope
[What is in and what is out for the first version]

## Open Questions
[Anything unresolved]

## Assumptions
[Anything inferred that should be confirmed]
```

Then say:

```txt
Brief complete.

When you are ready to generate the Project Handoff to Development Kit,
paste the PHDK generation prompt into this conversation.
The AI will use this brief as the source of truth for the kit.
```

---

## Rules for the Interview

- Ask one question at a time
- Wait for the answer before asking the next
- Do not suggest technical solutions during the interview
- Do not ask about databases, frameworks, or infrastructure
- If an answer is vague, ask one follow-up question to clarify
- Do not move to the brief until all 14 questions are answered or clearly covered
- Mark any unanswered or unclear areas as open questions in the brief
