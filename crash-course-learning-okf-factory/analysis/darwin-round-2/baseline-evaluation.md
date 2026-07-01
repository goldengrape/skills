---
type: Darwin Evaluation
title: Round 2 Baseline Evaluation
description: Evaluation of the lower-triangular version before round 2 revision.
tags: [darwin, evaluation, baseline, round-2]
timestamp: 2026-06-30T00:00:00-07:00
---
# Round 2 Baseline Evaluation

Evaluation mode: **dry_run**.

| Dimension | Weight | Score / 10 | Weighted |
|---|---:|---:|---:|
| D1 Meta-factory identity | 10 | 9 | 9.0 |
| D2 Input/output contract | 10 | 9 | 9.0 |
| D3 Generated layout completeness | 12 | 9 | 10.8 |
| D4 State persistence | 14 | 9 | 12.6 |
| D5 Resume behavior | 10 | 9 | 9.0 |
| D6 Adaptive planning | 10 | 8 | 8.0 |
| D7 Daily package fit | 8 | 9 | 7.2 |
| D8 Source grounding | 8 | 8 | 6.4 |
| D9 Validation and tests | 10 | 8 | 8.0 |
| D10 MVP executability | 8 | 3 | 2.4 |

Total: **82.4 / 100** under the round-2 rubric.

The score differs from the previous 89 because this rubric adds MVP executability as an explicit dimension. The lower-triangular ADD is preserved, but the package still depends on manual or AI execution to materialize the instance.

## Weakest Point

D10 MVP executability. The factory can describe what to create, but there is no minimal local helper to create the required skeleton and initial state.

## Revision Decision

Revise only the skeleton-materialization gap. Do not build a full app, UI, database, or grading engine.
