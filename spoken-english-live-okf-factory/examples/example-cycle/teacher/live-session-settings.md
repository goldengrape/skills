---
type: Live Session Settings
title: Example Cycle Live Settings
description: Course-specific parameters consumed by the shared Live runtime protocol.
tags: [example, teacher, settings]
timestamp: 2026-07-09T20:10:00-07:00
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
coach_turn_target: "one question, follow-up, or correction cue"
learner_control_cues:
  - more correction
  - less correction
  - explain
  - skip
  - wrap up
fatigue_fallback: minimum_viable_session
pronunciation_target: clear_intelligible_global_english
```

The learner's spoken control cue overrides these correction settings for the current session.
