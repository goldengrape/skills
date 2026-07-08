---
type: Runtime Schema
title: State Event Schema
description: Runtime event schema.
tags: [runtime, state]
timestamp: 2026-07-07T07:38:01+00:00
---

# State Event Schema

```yaml
state_event:
  date: YYYY-MM-DD
  day: 1
  case_id: CASE-DAY1-001
  localization_tag: supratentorial.subcortical.motor
  learner_answer_summary: string
  score_type: blind_score | semi_assisted_score | assisted_score
  prompt_visibility: hidden_until_answer | hinted_before_answer | shown_after_answer
  assistance_mode: guided | semi_guided | blind | barehand
  error_type: side_confusion | level_confusion | evidence_missing | disease_before_location | correct
  remediation_target: string
  next_retest: string
```

## Write Targets

- `state/score-history.md` for scores.
- `state/misconceptions.md` for persistent errors.
- `state/recall-deck.md` for new retrieval cards.
- `state/concept-mastery-state.md` for evidence level.
