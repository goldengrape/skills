---
type: Live Session Settings
title: Example Cycle Live Settings
description: Course-specific runtime and adaptive-topic parameters consumed by the shared Live protocol.
tags: [example, teacher, settings, adaptive-topics]
timestamp: 2026-07-09T21:30:00-07:00
---

# Live Session Settings

```yaml
daily_minutes: 15
practice_language: mostly_english
feedback_language: Chinese
interruption_style: live_micro
naturalness_nudges: true
self_repair_prompts: true
repeat_after_high_value_correction: true
micro_correction_target_seconds: 3-8
learner_speaking_share_target: ">= two_thirds"
coach_turn_target: "one question, follow-up, correction cue, or brief context sentence"
learner_control_cues:
  - more correction
  - less correction
  - explain
  - skip
  - wrap up
fatigue_fallback: minimum_viable_session
pronunciation_target: clear_intelligible_global_english
topic_policy:
  mode: guided_adaptive
  planned_ratio: 0.67
  adaptive_ratio: 0.33
  allow_mid_cycle_topic_adjustment: true
interest_discovery:
  enabled: true
  confirmation_rule: explicit_or_repeated_evidence
  separate_affinity_from_load: true
  recent_topic_window: 3
  default_max_same_topic_sessions_per_7_day_cycle: 3
current_events:
  enabled: false
  frequency: none_this_cycle
  require_current_verification: true
  max_context_sentences: 3
  verification_budget_seconds: 30
```

The learner's spoken control cue or explicit topic choice overrides these settings for the current session, while the language objective remains fixed.
