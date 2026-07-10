---
type: Playbook
title: Derive Cycle Blueprint
description: DP-002 procedure for turning normalized evidence into one bounded, interest-aware course-cycle design.
tags: [playbook, blueprint, cycle, adaptive-topics]
timestamp: 2026-07-09T21:30:00-07:00
---

# DP-002 — Derive Cycle Blueprint

## Input

One Cycle Evidence Snapshot produced by DP-001.

## Step 1 — Select at most three primary language targets

Choose no more than:

1. one scenario or communicative-function target,
2. one fluency or discourse target,
3. one language-repair target.

A target must be supported by learner intent, recent evidence, or an evidence gap that needs diagnosis.

Do not count conversation topics as extra language targets. Topics are vehicles for practice.

## Step 2 — Set cycle type and topic policy

- **7 days:** normal continuity and gradual transfer.
- **3 days:** one focused scenario, repair sprint, or short diagnostic cycle.

Topic policy:

- `fixed` — all daily topics are named in advance;
- `guided_adaptive` — default; core language progression is fixed and some topic slots adapt from evidence;
- `open_adaptive` — most topics adapt, but every day still has a fixed language objective and fallback.

Do not inflate a three-day need into seven days merely to fill a template.

## Step 3 — Build the language progression

For a seven-day cycle, use this default progression:

1. baseline or low-pressure entry,
2. guided practice,
3. variation with repair,
4. interest-based transfer,
5. higher-pressure or less scripted version,
6. adaptive transfer or optional current-event discussion,
7. review conversation and next-cycle diagnosis.

For a three-day cycle:

1. baseline and guided use,
2. variation or adaptive-interest transfer,
3. transfer and review.

The sequence is about increasing communicative demand, not merely changing subject matter.

## Step 4 — Assign topic slots

Each day uses one mode and one topic intent:

- `anchored` — the topic is fixed because it serves a specific scenario or diagnostic need;
- `adaptive` — the session chooses from confirmed/possible interests or offers two options;
- `current_event_optional` — the session may use one freshly verified event, otherwise it uses a named fallback.

Adaptive topic intents:

- `deepen_confirmed` — reuse a confirmed interest with a new language function, pressure, or perspective;
- `test_possible` — gather one bounded piece of evidence about a possible interest;
- `refresh_variety` — use a safe new or underused topic to prevent a narrow topic loop;
- `review_transfer` — revisit a prior topic only to test transfer of a language target.

Recommended seven-day `guided_adaptive` mix:

- three or four anchored days,
- two adaptive days,
- zero or one current-event-optional day,
- one review/diagnostic day, which may overlap with the categories above.

A three-day cycle normally includes at least one adaptive-capable day when interest evidence exists.

Every adaptive or current-event-optional day must declare:

- fixed language objective;
- topic function, such as explanation, comparison, opinion, storytelling, negotiation, or follow-up interaction;
- selection inputs;
- concrete evergreen fallback;
- excluded categories;
- rule for preserving the language objective after a topic switch;
- one topic intent;
- recent-topic limit;
- load-reduction fallback when the topic is suitable but the task is too difficult.

## Step 4A — Apply the Topic-Fit Check

A candidate topic is eligible only when all six checks pass:

1. **objective fit** — it naturally elicits the day's language function;
2. **consent and safety** — it respects explicit preferences, exclusions, and privacy;
3. **knowledge accessibility** — the learner can speak from experience or from a very short context capsule;
4. **evidence basis** — it is a confirmed interest, a bounded possible-interest test, a deliberate variety refresh, or a named fallback;
5. **recent-topic balance** — it does not create unnecessary repetition inside the recent three-session window;
6. **time fit** — setup does not consume the speaking budget.

When several candidates pass, prefer the one that advances the assigned topic intent. Do not always choose the strongest confirmed interest.

## Step 5 — Current-event suitability

A current-event slot is optional, never required for course completion.

Use it only when:

- current-events use is enabled;
- the event can be verified at session time;
- it aligns with a confirmed or plausible interest;
- it can be verified within 30 seconds and explained in two or three short sentences;
- it creates a useful speaking task rather than a comprehension lecture;
- it does not violate exclusions or sensitive-topic policy.

Do not hardcode a future news item into a multi-day plan. Store a selection rule and fallback instead.

## Step 6 — Fit the time budget

Default 15-minute day:

- one topic/scenario,
- one main speaking task,
- one short repair loop,
- one closeout.

Current-event background is included inside this budget and should normally take less than one minute.

Twenty-minute days may add one variation. Thirty-minute days may add a second role-play only when explicitly selected.

## Step 7 — Define carry-over evidence

The blueprint must name, when available:

- one prior phrase to retrieve;
- one prior error or uncertainty to retest;
- one scenario or interest to reuse, vary, or test;
- the previous next action;
- one topic hypothesis that still needs evidence.

## Output: Cycle Blueprint

```yaml
cycle_id:
cycle_days:
daily_minutes:
cycle_purpose:
primary_targets:
  scenario_or_function:
  fluency_or_discourse:
  language_repair:
topic_policy:
  mode:
  planned_ratio:
  adaptive_ratio:
  mid_cycle_adjustment:
interest_hypotheses: []
current_events_policy:
  enabled:
  frequency:
  preferred_categories: []
  excluded_categories: []
  require_current_verification:
carry_over_evidence: []
daily_sequence:
  - day:
    language_objective:
    topic_mode: anchored | adaptive | current_event_optional
    topic_intent: anchored_practice | deepen_confirmed | test_possible | refresh_variety | review_transfer | current_event_optional
    planned_or_fallback_topic:
    topic_function:
    selection_inputs: []
    topic_fit_checks: []
    load_reduction_fallback:
    switch_trigger:
    opening_question:
    speaking_task:
    target_expressions: []
    repair_or_transfer_task:
    evidence_to_capture: []
runtime_overrides: []
validation_risks: []
```

## Failure Rules

- More than three language targets → reduce scope.
- Topics change but communicative demand does not progress → redesign progression.
- An adaptive slot lacks a named fallback or fixed language objective → fail blueprint.
- A future day depends on a particular unverified news event → replace it with a selection rule and fallback.
- The same broad topic appears more than three times in a seven-day guided-adaptive cycle without learner request → diversify or mark the cycle thematic.
- Topic selection has no load-reduction fallback → add one before treating difficulty as low interest.
- Two days repeat the same task without a deliberate difficulty change → redesign the later day.
- A day contains only explanation, reading, or written exercises → replace it with spoken production.
- The plan exceeds the selected duration → remove tasks before extending time.
