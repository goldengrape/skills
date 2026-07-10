---
type: Cycle Plan
title: Cycle 1 Language Progression
description: Seven-day blueprint separating language progression from anchored and adaptive topics.
tags: [cycle-plan, speaking, adaptive-topics, week-1]
timestamp: 2026-07-09T22:00:00-07:00
---

# Cycle 1 Language Progression

## Cycle Blueprint

```yaml
cycle_id: 1
cycle_days: 7
daily_minutes: 15
cycle_purpose: establish a daily speaking routine and diagnose transfer needs through explanation, comparison, and recommendation
primary_targets:
  scenario_or_function: explain a process and make an actionable recommendation
  fluency_or_discourse: sustain 45-90 seconds with signposts, examples, and follow-up answers
  language_repair: qualify opinions and comparisons naturally
topic_policy:
  mode: guided_adaptive
  planned_ratio: 0.57
  adaptive_ratio: 0.43
  mid_cycle_adjustment: allowed while preserving each day's language objective
interest_hypotheses:
  - AI may elicit detailed opinions and examples
  - adult continuing education may elicit personally grounded speech
current_events_policy:
  enabled: false
  frequency: none in cycle 1
  preferred_categories: [technology, education]
  excluded_categories: []
  require_current_verification: true if enabled in a later cycle
carry_over_evidence:
  - no prior cycle evidence
  - retrieve phrases introduced earlier in this cycle from day 2 onward
runtime_overrides:
  - optional extension may add up to 5 minutes but does not add a second primary task
validation_risks:
  - self-estimated level has not been confirmed through speech
  - interest affinity may be confused with subject knowledge unless recorded separately
```

## Daily sequence

| Day | Demand | Fixed language objective | Topic mode | Planned topic or fallback | Topic intent | Evidence to capture |
|---|---|---|---|---|---|---|
| 1 | Baseline | Describe a routine in sequence and explain one reason | anchored | current learning routine | anchored practice | speaking length, prompting need, useful baseline repairs |
| 2 | Guided practice | Explain a process clearly enough for another person to follow | anchored | an AI-assisted learning workflow | anchored practice | sequence markers, clarity, AI affinity versus vocabulary load |
| 3 | Variation + repair | Compare two options and state a qualified preference | anchored | AI support versus a human teacher | anchored practice | comparison language, hedging, response to challenge |
| 4 | Interest transfer | Explain benefits, limits, and one example on a selected topic | adaptive | AI tool or adult learning challenge; fallback: a useful app | test possible | explicit choice, spontaneous expansion, learner questions |
| 5 | Higher pressure | Recommend an option after asking for needs and constraints | anchored | recommend a continuing-education course | anchored practice | interaction, conditional recommendation, register |
| 6 | Variety transfer | Diagnose a practical problem and propose two steps | adaptive | underused safe topic; fallback: building a healthy study habit | refresh variety | transfer beyond AI, load versus affinity |
| 7 | Review + diagnosis | Combine explanation, comparison, and recommendation | adaptive | least-repeated suitable topic; fallback: a 30-day learning plan | review transfer | independent reuse, one next-cycle priority, topic preference evidence |

## Progression logic

- Days 1–2 reduce pressure and establish a baseline.
- Day 3 adds comparison and a challenge question.
- Day 4 holds the language task steady while testing topic fit.
- Day 5 adds interaction: the learner must ask questions before recommending.
- Day 6 tests whether the language transfers to a less familiar topic.
- Day 7 removes most scaffolding and gathers evidence for cycle 2.

## Adaptive selection rule

For Days 4, 6, and 7, choose in this order: the learner's explicit choice today; a recorded next-topic recommendation; a suitable possible interest test; the named evergreen fallback. Apply all six checks: objective fit, consent/safety, accessible knowledge, evidence basis, recent-topic balance, and time fit. When two candidates are equally suitable, offer only two concise choices.

## Carry-over rule

From Day 2 onward, retrieve one expression from `state/phrase-deck.md`. From Day 3 onward, retest at most one candidate pattern from the previous session. Do not label a pattern recurring without sufficient repeated evidence.
