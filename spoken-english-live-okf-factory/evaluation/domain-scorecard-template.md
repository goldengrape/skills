---
type: Domain Scorecard Template
title: Spoken English Live OKF Factory Domain Scorecard
description: Reusable evidence sheet for one baseline or comparison evaluation.
tags: [darwin, scorecard, evaluation]
timestamp: 2026-07-09T19:15:00-07:00
---

# Domain Scorecard

## Evaluation Metadata

```yaml
evaluation_id:
version_under_test:
evaluator:
evaluation_date:
evidence_modes_used: []
full_live_sessions_observed: 0
static_review_weight_percent:
score_status: final|provisional
```

## Hard Gates

| Gate | PASS/FAIL | Evidence |
|---|---|---|
| HG-01 Speaking-first interaction |  |  |
| HG-02 Pronunciation and accent integrity |  |  |
| HG-03 Timebox and closeout |  |  |
| HG-04 Persistence chain |  |  |
| HG-05 Evidence truthfulness |  |  |
| HG-06 Continuity |  |  |
| HG-07 Runtime compatibility |  |  |
| HG-08 Validation integrity |  |  |

Any `FAIL` makes the domain result fail regardless of numeric score.

## Dimension Scores

| Dimension | Weight | Score 1–10 | Weighted points | Evidence and reasoning |
|---|---:|---:|---:|---|
| D1 Evidence fidelity and personalization | 12 |  |  |  |
| D2 Cycle focus, scope, and progression | 12 |  |  |  |
| D3 Authentic spoken tasks and learner output | 14 |  |  |  |
| D4 Live conversational orchestration | 14 |  |  |  |
| D5 Corrective feedback and idiomatic coaching | 15 |  |  |  |
| D6 Timebox, fatigue, and session economy | 8 |  |  |  |
| D7 Session evidence and state integrity | 10 |  |  |  |
| D8 Cross-cycle adaptation and retrieval | 10 |  |  |  |
| D9 Runtime truthfulness and Markdown usability | 5 |  |  |  |
| **Domain total** | **100** |  | **/100** |  |

## Test-Prompt Results

| Prompt ID | Mode | Result | Main defects | Dimensions affected |
|---|---|---|---|---|
| DOMAIN-001 | full_generation |  |  |  |
| DOMAIN-002 | full_generation |  |  |  |
| DOMAIN-003 | full_live |  |  |  |
| DOMAIN-004 | full_live |  |  |  |
| DOMAIN-005 | interaction_simulation |  |  |  |
| DOMAIN-006 | full_generation |  |  |  |
| DOMAIN-007 | full_generation |  |  |  |
| DOMAIN-008 | interaction_simulation |  |  |  |

## Composite Result

```yaml
common_score:
domain_score:
common_weight: 0.35
domain_weight: 0.65
composite_score:
hard_gate_status:
final_decision: retain|revise|reject
```

## Improvement Decision

- What improved against baseline:
- What regressed:
- Whether a hard gate regressed:
- Independent reviewer judgment:
- Retain or roll back:
