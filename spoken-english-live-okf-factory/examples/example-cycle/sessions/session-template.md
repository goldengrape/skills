---
type: Template
title: Session Record Template
description: DP-005 copyable Markdown record for one ChatGPT Live speaking session.
tags: [template, session, state, evidence]
timestamp: 2026-07-09T20:25:00-07:00
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

## Student Summary

- Scenario:
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
- next_action:

### phrase-deck.md
- phrase:
  use_when:
  learner_example:
  evidence_ref:
  status: new | learning | stable
  next_review_condition:

### scenario-ledger.md
- scenario:
  evidence_ref:
  task_result:
  difficulty:
  next_variant:

## Next Action

- type: continue | repair | retrieve | transfer | diagnose | review_cycle | generate_next_cycle
- focus:
- reason:
- evidence_ref:
```
