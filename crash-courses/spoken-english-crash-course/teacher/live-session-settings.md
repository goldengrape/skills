---
type: Live Session Settings
title: Cycle 1 ChatGPT Live Settings
description: Course-specific runtime, correction, topic, and current-event parameters.
tags: [teacher, live-session, settings, cycle-1]
timestamp: 2026-07-09T22:00:00-07:00
---

# Cycle 1 ChatGPT Live Settings

Use the factory's `runtime/live-session-protocol.md` as the authoritative runtime protocol. This file contains only course-specific values.

```yaml
cycle_id: 1
planned_duration_minutes: 15
optional_extension_minutes: 5
target_english: clear_global_english
practice_language: mostly_english
feedback_language: Chinese
learner_speaking_share_target: at_least_two_thirds
coach_turn_limit: normally_one_question_or_two_short_sentences
correction:
  interruption_style: live_micro
  allow_naturalness_nudges: true
  micro_correction_target_seconds: 3-8
  repeat_after_high_value_correction: true
  learner_control_cues: [more correction, less correction, explain, skip, wrap up]
topic_policy:
  mode: guided_adaptive
  planned_ratio: 0.57
  adaptive_ratio: 0.43
  allow_mid_cycle_topic_adjustment: true
  recent_topic_window: 3
  max_same_broad_topic_sessions: 3
  preserve_language_objective_on_switch: true
  separate_affinity_from_load: true
current_events:
  enabled: false
  frequency: none
  preferred_categories: [technology, education]
  excluded_categories: []
  require_current_verification: true
  verification_budget_seconds: 30
  max_context_sentences: 3
  fallback_rule: use_the_daily_evergreen_fallback
closeout:
  protected_minutes: 2
  require_session_record: true
  require_state_patch: true
  require_exactly_one_next_action: true
```

## First-session note

The B1–B2 level is self-reported. Adjust prompt length and scaffolding from observed speech, but do not silently change the cycle's language objectives. Pronunciation feedback requires clear audio evidence.

## Minimum viable session

When tired or short on time: one speaking prompt, one useful repair if needed, one learner restatement, and closeout. Record `shortened` or `minimum_viable` accurately.
