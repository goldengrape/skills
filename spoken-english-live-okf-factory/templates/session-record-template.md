---
type: Template
title: Session Record Template
description: DP-005 Markdown record for one adaptive ChatGPT Live speaking session.
tags: [template, session, state, evidence, interests, current-events]
timestamp: 2026-07-09T21:30:00-07:00
---

# Session Record Template

```markdown
---
type: Session Record
title: Cycle {cycle_id} — Day {day} — {date}
description: Spoken-English ChatGPT Live session evidence and state patch.
tags: [session, english-speaking, chatgpt-live]
timestamp: {timestamp}
---

# Cycle {cycle_id} — Day {day}

## Session Status

- planned_duration:
- actual_shape: full | shortened | minimum_viable
- task_status: completed | partially_completed | skipped
- learner_speaking_share: high | adequate | low | not_observed
- correction_preference_used: live_micro | mostly_delayed | on_request | strict | changed_during_session

## Topic Selection

- language_objective:
- planned_topic_mode: anchored | adaptive | current_event_optional
- topic_intent: anchored_practice | deepen_confirmed | test_possible | refresh_variety | review_transfer | current_event_optional
- actual_topic:
- selection_basis: learner_choice | recommended_next_topic | confirmed_interest | possible_interest_test | verified_current_event | evergreen_fallback | planned_anchor
- topic_switch_occurred: true | false
- recent_topic_balance: repeated_ok | diversify_next | thematic_by_request | unknown
- engagement_cause: topic_affinity | language_load | background_knowledge | prompt_or_task | fatigue_or_time | sensitivity_or_privacy | unknown
- reason_for_switch:

## Current Event

- used: true | false
- event_summary:
- event_date:
- verification_date:
- source_name:
- source_ref:
- relevance_to_language_objective:
- confidence: high | medium | low | not_applicable

## Student Summary

- Speaking task completed:
- What went well:
- Main issue worth repairing:
- Useful expression:

## Evidence

### Strong moments
- claim:
  evidence_class: observed | learner_reported | inferred | uncertain
  evidence:

### Correction events
- learner_form:
  improved_form:
  reason: clarity | naturalness | register | recurring_pattern | grammar | word_choice
  delivery: direct_replacement | naturalness_nudge | self_repair_cue | clarification | delayed
  uptake: repeated | self_repaired | used_later | not_observed
  evidence_class: observed | learner_reported | inferred | uncertain

### Pattern observations
- item:
  status: one_off_slip | candidate_pattern | active_recurring | high_impact_exception | improved | uncertain
  occurrence_evidence:
  prior_evidence_ref:

### Interest and engagement signals
- topic:
  signal: explicit_preference | expanded_answer | learner_initiated_example | learner_question | requested_continuation | repeated_short_answers | requested_switch | sensitive_topic_decline | other
  evidence_class: observed | learner_reported | inferred | uncertain
  context: normal | fatigued | shortened | vocabulary_blocked | background_knowledge_limited | prompt_mismatch | sensitive | unknown
  proposed_status: explicit_confirmed | observed_confirmed | possible | low_engagement_candidate | avoid | retired | no_change
  evidence_ref:

### Pronunciation observations
- item:
  confidence: heard_clearly | likely_issue | uncertain_from_audio_or_transcript
  evidence_class: observed | learner_reported | inferred | uncertain
  note:

## State Patch

### learner-state.md
- current_day:
- completed_sessions:
- recurring_pattern_updates: []
- preference_updates: []
- interest_updates: []
- fatigue_or_time_notes: []
- next_topic_recommendation:
    action: keep_planned | use_confirmed_interest | test_possible_interest | offer_choice | use_current_event_slot | use_fallback | no_change
    topic_or_options: []
    language_objective_to_preserve:
    evidence_refs: []
    confidence:
    topic_intent: deepen_confirmed | test_possible | refresh_variety | review_transfer | no_change
    recent_topic_balance: repeated_ok | diversify_next | thematic_by_request | unknown
- next_action:

### phrase-deck.md
- phrase:
  use_when:
  learner_example:
  evidence_ref:
  status: new | learning | stable
  next_review_condition:

### scenario-ledger.md
- scenario_or_topic:
  topic_mode:
  evidence_ref:
  task_result:
  difficulty:
  engagement:
  next_variant:

## Next Action

- type: continue | repair | retrieve | transfer | diagnose | review_cycle | generate_next_cycle
- focus:
- reason:
- evidence_ref:
```
