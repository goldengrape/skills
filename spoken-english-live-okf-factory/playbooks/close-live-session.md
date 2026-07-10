---
type: Playbook
title: Close Live Session
description: DP-005 procedure for converting one Live session into trustworthy evidence, interest state, and one next action.
tags: [playbook, closeout, state, evidence, interests, current-events]
timestamp: 2026-07-09T21:30:00-07:00
---

# DP-005 — Close Live Session

## Completion Rule

A session is incomplete until it returns:

1. one session record;
2. one state patch;
3. exactly one next action.

When topic adaptation is enabled, the state patch also includes one next-topic recommendation or `no_change`.

The output is copyable Markdown. Do not claim that any file was written, uploaded, or committed.

## Evidence Classes

| Class | Meaning | May update canonical state? |
|---|---|---|
| `observed` | Directly supported by the Live interaction or supplied turn-by-turn record. | Yes, subject to thresholds. |
| `learner_reported` | Stated by the learner but not observed in this session. | Yes, as a preference, interest, fatigue note, or hypothesis—not as performance proof. |
| `inferred` | A cautious interpretation from observed behavior. | Only as a test-next hypothesis. |
| `uncertain` | Audio, transcript, context, or current-event verification is insufficient. | Only in uncertainty or diagnostic fields. |

Do not rewrite an inference as an observation.

## Pattern and Phrase Thresholds

- **one-off slip:** one observed occurrence with no prior pattern and no repeat;
- **candidate pattern:** two similar occurrences in one session, or one occurrence matching an active prior record;
- **active recurring pattern:** supported across two sessions, or at least three separated speaking turns in one session;
- **high-impact exception:** one occurrence may become active when it repeatedly blocks meaning or task completion, but the reason must be stated;
- **stable phrase:** used spontaneously and appropriately in at least two sessions or three varied contexts;
- **learning phrase:** corrected or prompted use with incomplete spontaneous retrieval.

When evidence is incomplete, use the weaker label.

## Engagement Cause Classification

Before proposing an interest update, record the most plausible cause of the observed response:

- `topic_affinity`;
- `language_load`;
- `background_knowledge`;
- `prompt_or_task`;
- `fatigue_or_time`;
- `sensitivity_or_privacy`;
- `unknown`.

Only `topic_affinity` evidence may directly promote or downgrade an interest. If another cause is plausible, preserve the current interest status and record a task-design or support adjustment instead.

## Interest Thresholds

- An explicit learner statement can create `explicit_confirmed` immediately.
- A single observed positive signal creates `possible`, not confirmed.
- Repeated positive signals across two sessions may create `observed_confirmed`.
- An explicit request to revisit the topic may also create `observed_confirmed` after one trial.
- Low engagement becomes `low_engagement_candidate` only after repeated signals across two non-fatigued sessions.
- One tired, shortened, difficult, or sensitive-topic session does not lower interest status.
- `retired` requires an explicit learner choice or repeated evidence that the topic no longer supports engagement or learning value.

Interest is not a personality judgment. Record only what is useful for topic selection.

## Evidence Selection

Record:

- the task actually completed;
- actual topic and topic mode;
- topic-selection basis;
- strong moments supported by interaction;
- high-value correction events;
- learner uptake;
- language patterns and pronunciation with evidence labels;
- engagement signals relevant to later topic selection;
- fatigue, duration, or preference changes that affected the session;
- current-event provenance when used;
- topic intent, recent-topic balance, and engagement-cause classification.

Do not copy the lesson plan as if it were performance evidence.

## Current-Event Provenance

When a current event was used, record:

```yaml
current_event:
  used: true
  event_summary:
  event_date:
  verification_date:
  source_name:
  source_ref: optional
  relevance_to_language_objective:
  confidence: high|medium|low
```

If no reliable verification was available, record `used: false` and the fallback topic. Do not reconstruct citations from memory at closeout.

## State Patch Order

Apply the patch conceptually in this order:

1. update cycle/day and completion status;
2. update recurring-pattern status;
3. update phrase status and next retrieval condition;
4. update scenario/topic evidence, difficulty, engagement, engagement-cause classification, and next variation;
5. update interest status only from topic-affinity evidence using thresholds;
6. update preferences, fatigue, or duration notes;
7. recommend the next adaptive topic or `no_change`;
8. write exactly one next action.

The next-topic recommendation may contain:

```yaml
next_topic_recommendation:
  action: keep_planned | use_confirmed_interest | test_possible_interest | offer_choice | use_current_event_slot | use_fallback | no_change
  topic_or_options: []
  language_objective_to_preserve:
  evidence_refs: []
  confidence: high | medium | low
  topic_intent: deepen_confirmed | test_possible | refresh_variety | review_transfer | no_change
  recent_topic_balance: repeated_ok | diversify_next | thematic_by_request | unknown
```

This recommendation does not silently rewrite a future day file.

## Next-Action Selection

Choose the smallest action that most improves the next session:

- `continue`;
- `repair`;
- `retrieve`;
- `transfer`;
- `diagnose`;
- `review_cycle`;
- `generate_next_cycle`.

When several actions are useful, select one primary action and place the others in evidence notes.

## Failure Recovery

| Trigger | First response | If unresolved |
|---|---|---|
| Transcript and remembered audio conflict | Prefer clearly observed interaction and label the conflict. | Mark uncertain; do not create pronunciation diagnosis. |
| A correction occurred but uptake is unknown | Record `uptake: not_observed`. | Keep it learning/candidate rather than stable/solved. |
| Only one occurrence supports a new error | Record one-off slip. | Promote only with prior or high-impact evidence. |
| One positive topic-affinity signal occurs | Record `possible`. | Do not confirm unless explicit or repeated. |
| Low engagement may be caused by language, knowledge, prompt, fatigue, or privacy load | Keep interest state unchanged and record the confound. | Test later with a better-matched task only if useful. |
| A confirmed interest has dominated the recent topic window | Keep the interest confirmed. | Recommend `refresh_variety` unless the learner requested a thematic cycle. |
| Topic engagement is low during fatigue | Record fatigue and keep interest status unchanged. | Test later only if useful. |
| Current-event source/date is unavailable | Mark current event unverified and do not assert facts. | Record the fallback topic instead. |
| State patch contradicts session evidence | Preserve session evidence and flag conflict. | Do not overwrite canonical state until reviewed. |
| Closeout time is very short | Produce minimum record: task, topic basis, one strength, one repair, patch, one next action. | Omit optional prose, never the persistence chain. |

## Validation Conditions

Fail the closeout when:

- no task completion status is recorded;
- actual topic or topic-selection basis is absent;
- observed, reported, inferred, and uncertain claims are blurred consequentially;
- a recurring pattern, stable phrase, or confirmed observed interest is created without threshold evidence;
- pronunciation lacks an evidence label;
- a used current event lacks source/date/verification information;
- the state patch is absent;
- there is zero or more than one next action;
- the output claims automatic persistence.
