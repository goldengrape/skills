---
type: Contract
title: Cycle Evidence Contract
description: DP-001 contract for normalizing learner input, topic preferences, and prior evidence before planning.
tags: [contract, evidence, learner-state, interests, current-events]
timestamp: 2026-07-09T21:30:00-07:00
---

# DP-001 — Cycle Evidence Contract

## Input

The factory accepts five groups of information.

### Learner brief

```yaml
learner_name: optional
native_language: Chinese
estimated_speaking_level: A2|B1|B2|C1|unknown
speaking_confidence: low|medium|high|unknown
target_english: global|american|british|custom|unspecified
primary_goal: daily|workplace|interview|academic|travel|social|custom
target_scenarios: []
explicit_interests: []
avoid_topics: []
```

### Cycle preferences

```yaml
cycle_id: 1
cycle_days: 7
daily_minutes: 15
supported_minutes: [10, 15, 20, 30]
practice_language: mostly_english
feedback_language: Chinese
```

### Correction preferences

```yaml
interruption_style: live_micro|mostly_delayed|on_request|strict
allow_naturalness_nudges: true
micro_correction_target_seconds: 3-8
repeat_after_high_value_correction: true
learner_control_cues: [more correction, less correction, explain, skip, wrap up]
```

### Topic and current-event preferences

```yaml
topic_policy:
  mode: fixed|guided_adaptive|open_adaptive
  planned_ratio: 0.6
  adaptive_ratio: 0.4
  allow_mid_cycle_topic_adjustment: true
interest_discovery:
  enabled: true
  ask_directly_when_uncertain: false
  separate_affinity_from_load: true
  recent_topic_window: 3
  default_max_same_topic_sessions_per_7_day_cycle: 3
current_events:
  enabled: false
  frequency: up_to_one_slot_per_cycle
  preferred_categories: [technology, science, culture, lifestyle]
  excluded_categories: []
  require_current_verification: true
  sensitive_topics_require_opt_in: true
  verification_budget_seconds: 30
  max_context_sentences: 3
```

### Prior evidence

Accept pasted text or readable files containing:

- previous cycle review,
- latest session records,
- canonical learner state,
- phrase deck,
- scenario ledger,
- explicit new interests or topic exclusions,
- observed engagement signals,
- fatigue or duration notes,
- prior current-event outcomes.

## Evidence Classes

Normalize every claim as one of:

- `current_instruction` — the learner's explicit present request;
- `observed` — supported by a session record or supplied interaction;
- `learner_reported` — stated by the learner but not directly observed;
- `inferred` — a cautious planning hypothesis;
- `uncertain` — evidence is insufficient or conflicting.

A lower-confidence class must not be promoted silently. Keep an evidence reference when available.

## Interest Evidence Rules

Use these operational states:

- `explicit_confirmed` — the learner directly says they want or enjoy the topic;
- `observed_confirmed` — repeated engagement across at least two sessions, or the learner explicitly asks to continue after trying it;
- `possible` — one observed positive signal or one inferred match;
- `low_engagement_candidate` — repeated low-engagement signals across at least two non-fatigued sessions;
- `avoid` — explicitly excluded or unsuitable under the current policy;
- `retired` — previously useful but no longer worth active use, with evidence.

Positive engagement signals may include:

- longer spontaneous answers than the session baseline;
- learner-initiated examples or related questions;
- explicit request to continue or revisit;
- lower prompting needs while maintaining useful language challenge.

Do not treat these alone as disinterest:

- one short answer;
- one tired or shortened session;
- difficulty caused by unfamiliar vocabulary;
- a sensitive topic the learner chooses not to discuss.

## Topic-Affinity and Load Separation

Before changing interest status, classify the most plausible explanation for the learner's response:

- `topic_affinity` — the learner explicitly chooses, expands, asks questions, or requests continuation;
- `language_load` — the learner has ideas but lacks vocabulary, grammar, or fluency to express them;
- `background_knowledge` — the subject requires facts or context the learner does not have;
- `prompt_or_task` — the question is vague, overly broad, repetitive, or poorly matched to the language objective;
- `fatigue_or_time` — the learner is tired, distracted, or in a shortened session;
- `sensitivity_or_privacy` — the learner does not want to discuss the topic;
- `unknown`.

Only `topic_affinity` evidence may directly raise or lower an interest status. The other classes may change task design, support level, or topic suitability, but they do not by themselves prove liking or disliking.

When low engagement is observed and the cause is not explicit, keep the interest state unchanged and create a small diagnostic note or future test.

## Topic Portfolio Evidence

Track the last three actual topics and their language functions. In a normal seven-day guided-adaptive cycle, do not plan the same broad topic for more than three sessions unless the learner explicitly requests a thematic cycle. Reuse is valuable only when the language function, pressure, or perspective changes.

## Evidence Priority

When records disagree, prefer:

1. learner’s explicit current instruction,
2. most recent completed session record,
3. most recent cycle review,
4. canonical learner state,
5. older records.

Record conflicts instead of silently choosing when the conflict changes course purpose, topic safety, or current-event policy.

## Defaults

- `cycle_days`: 7
- `daily_minutes`: 15
- `target_english`: clear global English
- `interruption_style`: live micro-correction
- `practice_language`: mostly English
- `feedback_language`: Chinese
- `topic_policy.mode`: guided_adaptive
- `topic_policy.planned_ratio`: 0.6
- `topic_policy.adaptive_ratio`: 0.4
- `interest_discovery.enabled`: true
- `current_events.enabled`: false
- `current_events.require_current_verification`: true

A 20-minute session is the normal longer option. Ten and thirty minutes require explicit learner choice.

## Output: Cycle Evidence Snapshot

Produce one normalized snapshot with:

```yaml
confirmed:
  learner_goal:
  target_scenarios: []
  daily_minutes:
  cycle_days:
  correction_preference:
  topic_policy:
  current_events_policy:
  topic_portfolio_policy:
observed_evidence:
  strengths: []
  active_errors: []
  unstable_phrases: []
  scenario_history: []
  fatigue_or_time_notes: []
interest_state:
  recent_topic_history: []
  explicit_confirmed: []
  observed_confirmed: []
  possible: []
  low_engagement_candidate: []
  avoid: []
  retired: []
carry_over:
  previous_next_action:
  required_retests: []
  recommended_next_topic:
  adaptation_hypotheses: []
defaults_used: []
conflicts: []
evidence_gaps: []
evidence_register:
  - claim:
    class: current_instruction | observed | learner_reported | inferred | uncertain
    source_ref:
    confidence: high | medium | low
```

## Stop Conditions

Stop before blueprint derivation when:

- `daily_minutes` is outside supported values and the learner has not approved a custom duration;
- two current instructions conflict in a way that changes cycle purpose;
- current-event categories conflict with explicit exclusions or sensitive-topic preferences;
- the requested task is not spoken-English training.

Do not stop for non-critical missing data. Use defaults and record them.
