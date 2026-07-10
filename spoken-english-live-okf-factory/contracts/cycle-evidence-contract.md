---
type: Contract
title: Cycle Evidence Contract
description: DP-001 contract for normalizing learner input and prior evidence before planning.
tags: [contract, evidence, learner-state]
timestamp: 2026-07-09T18:10:00-07:00
---

# DP-001 — Cycle Evidence Contract

## Input

The factory accepts four groups of information.

### Learner brief

```yaml
learner_name: optional
native_language: Chinese
estimated_speaking_level: A2|B1|B2|C1|unknown
speaking_confidence: low|medium|high|unknown
target_english: global|american|british|custom|unspecified
primary_goal: daily|workplace|interview|academic|travel|social|custom
target_scenarios: []
learner_interests: []
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

### Prior evidence

Accept pasted text or readable files containing:

- previous cycle review,
- latest session records,
- canonical learner state,
- phrase deck,
- scenario ledger,
- new learner constraints or interests.

## Evidence Classes

Normalize every claim as one of:

- `current_instruction` — the learner's explicit present request;
- `observed` — supported by a session record or supplied interaction;
- `learner_reported` — stated by the learner but not directly observed;
- `inferred` — a cautious planning hypothesis;
- `uncertain` — evidence is insufficient or conflicting.

A lower-confidence class must not be promoted silently. Keep an evidence reference when available.

## Evidence Priority

When records disagree, prefer:

1. learner’s explicit current instruction,
2. most recent completed session record,
3. most recent cycle review,
4. canonical learner state,
5. older records.

Record conflicts instead of silently choosing when the conflict changes the course design.

## Defaults

- `cycle_days`: 7
- `daily_minutes`: 15
- `target_english`: clear global English
- `interruption_style`: live micro-correction
- `practice_language`: mostly English
- `feedback_language`: Chinese

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
observed_evidence:
  strengths: []
  active_errors: []
  unstable_phrases: []
  scenario_history: []
  interests: []
  fatigue_or_time_notes: []
carry_over:
  previous_next_action:
  required_retests: []
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

- `daily_minutes` is outside the supported values and the learner has not approved a custom duration;
- two current instructions conflict in a way that changes cycle purpose;
- the requested task is not spoken-English training.

Do not stop for non-critical missing data. Use defaults and record them.
