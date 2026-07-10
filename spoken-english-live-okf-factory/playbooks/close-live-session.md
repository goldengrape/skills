---
type: Playbook
title: Close Live Session
description: DP-005 procedure for converting one Live session into trustworthy Markdown evidence, state updates, and one next action.
tags: [playbook, closeout, state, evidence]
timestamp: 2026-07-09T20:25:00-07:00
---

# DP-005 — Close Live Session

## Completion Rule

A session is incomplete until it returns:

1. one session record,
2. one state patch,
3. exactly one next action.

The output is copyable Markdown. Do not claim that any file was written, uploaded, or committed.

## Evidence Classes

Every recorded claim uses one class:

| Class | Meaning | May update canonical state? |
|---|---|---|
| `observed` | Directly supported by the Live interaction or supplied turn-by-turn record. | Yes, subject to thresholds below. |
| `learner_reported` | Stated by the learner but not observed in this session. | Yes, as a preference, interest, fatigue note, or hypothesis—not as performance proof. |
| `inferred` | A cautious interpretation from observed behavior. | Only as a test-next hypothesis. |
| `uncertain` | Audio, transcript, or context is insufficient. | Only in uncertainty or diagnostic fields. |

Do not rewrite an inference as an observation.

## Pattern Thresholds

Use these operational labels:

- **one-off slip:** one observed occurrence with no prior pattern and no repeat;
- **candidate pattern:** two similar occurrences in one session, or one occurrence matching an active prior record;
- **active recurring pattern:** supported across two sessions, or at least three separated speaking turns in one session;
- **high-impact exception:** one occurrence may become active when it repeatedly blocks meaning or task completion, but the reason must be stated;
- **stable phrase:** used spontaneously and appropriately in at least two sessions or three varied contexts;
- **learning phrase:** corrected or prompted use with incomplete spontaneous retrieval.

These are defaults, not fake precision. When evidence is incomplete, use the weaker label.

## Evidence Selection

Record:

- the task actually completed;
- strong moments supported by the interaction;
- high-value correction events;
- learner uptake: repeated, self-repaired, used later, or not yet demonstrated;
- one-off slips separately from candidate or recurring patterns;
- pronunciation only with an evidence label;
- fatigue, duration, or correction-preference changes when they affected the session.

Do not copy the lesson plan as if it were performance evidence.

## State Patch Order

Apply the patch conceptually in this order:

1. update cycle/day and completion status;
2. update recurring-pattern status using the thresholds above;
3. update phrase status and next retrieval condition;
4. update scenario evidence, difficulty, and next variation;
5. update interests, preferences, fatigue, or duration notes;
6. write exactly one next action.

## Next-Action Selection

Choose the smallest action that most improves the next session:

- `continue`
- `repair`
- `retrieve`
- `transfer`
- `diagnose`
- `review_cycle`
- `generate_next_cycle`

When several actions are useful, select one primary action and place the others in evidence notes, not as competing next actions.

## Failure Recovery

| Trigger | First response | If unresolved |
|---|---|---|
| Transcript and remembered audio conflict | Prefer the clearly observed interaction and label the conflict. | Mark uncertain; do not create a pronunciation diagnosis. |
| A correction occurred but learner uptake is unknown | Record the correction with `uptake: not_observed`. | Keep it learning/candidate rather than stable/solved. |
| Only one occurrence supports a new error | Record it as a one-off slip. | Promote only when prior evidence or high-impact blocking evidence exists. |
| State patch contradicts session evidence | Preserve the session evidence and flag the conflicting state field. | Do not overwrite canonical state until reviewed. |
| Closeout time is very short | Produce the minimum record: task, one strength, one repair, state patch, one next action. | Omit optional prose, never the persistence chain. |

## Validation Conditions

Fail the closeout when:

- no task completion status is recorded;
- observed, reported, inferred, and uncertain claims are blurred in a consequential way;
- an active recurring pattern is created without meeting a threshold or stating a high-impact exception;
- pronunciation lacks an evidence label;
- the state patch is absent;
- there is zero or more than one next action;
- the output claims automatic persistence.
