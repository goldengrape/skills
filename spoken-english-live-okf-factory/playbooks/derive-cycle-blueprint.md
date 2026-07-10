---
type: Playbook
title: Derive Cycle Blueprint
description: DP-002 procedure for turning normalized evidence into one bounded course-cycle design.
tags: [playbook, blueprint, cycle]
timestamp: 2026-07-09T18:10:00-07:00
---

# DP-002 — Derive Cycle Blueprint

## Input

One Cycle Evidence Snapshot produced by DP-001.

## Step 1 — Select at most three primary targets

Choose no more than:

1. one scenario target,
2. one fluency or discourse target,
3. one language-repair target.

A target must be supported by learner intent, recent evidence, or a recorded evidence gap that needs diagnosis.

## Step 2 — Set the cycle type

- **7 days:** normal continuity and gradual transfer.
- **3 days:** one focused scenario, one repair sprint, or a short diagnostic cycle.

Do not inflate a three-day need into seven days merely to fill a template.

## Step 3 — Build the progression

For a seven-day cycle, use this default progression:

1. baseline or low-pressure entry,
2. guided practice,
3. variation with repair,
4. interest-based transfer,
5. higher-pressure or less scripted version,
6. mixed transfer,
7. review conversation and next-cycle diagnosis.

For a three-day cycle:

1. baseline and guided use,
2. variation and repair,
3. transfer and review.

## Step 4 — Fit the time budget

Default 15-minute day:

- one scenario,
- one main speaking task,
- one short repair loop,
- one closeout.

Twenty-minute days may add one variation. Thirty-minute days may add a second role-play only when explicitly selected.

## Step 5 — Define carry-over evidence

The blueprint must name:

- at least one prior phrase to retrieve when available,
- at least one prior error or uncertainty to retest when available,
- one scenario or interest to reuse or vary,
- the previous next action.

## Output: Cycle Blueprint

```yaml
cycle_id:
cycle_days:
daily_minutes:
cycle_purpose:
primary_targets:
  scenario:
  fluency_or_discourse:
  language_repair:
carry_over_evidence: []
daily_sequence:
  - day:
    scenario:
    speaking_task:
    target_expressions: []
    repair_or_transfer_task:
    evidence_to_capture:
runtime_overrides: []
validation_risks: []
```

## Failure Rules

- More than three targets → reduce scope.
- Two days repeat the same task without a deliberate difficulty change → redesign the later day.
- A day contains only explanation, reading, or written exercises → replace it with spoken production.
- The plan exceeds the selected duration → remove tasks before extending time.
