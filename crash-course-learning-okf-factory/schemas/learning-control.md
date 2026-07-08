---
type: Schema
title: Learning Control Schema
description: Compact schema for learning stages, target levels, AI assistance, verifiability, productive friction, and evidence ledgers.
tags: [schema, learning-control, learning-stage, ai-diet]
---

# Learning Control Schema

## Learning stages

`learning_stage` is one of `L1` through `L9`.

| Level | Meaning | Minimum evidence |
|---|---|---|
| L1 | heard of | no longer unfamiliar |
| L2 | can follow | follows an explanation |
| L3 | can recognize | identifies concept in context |
| L4 | can retrieve | recalls definition/formula/diagram without notes |
| L5 | standard use | solves same-type tasks |
| L6 | misuse discrimination | detects common confusions and flawed answers |
| L7 | transfer | uses concept in new or cross-day contexts |
| L8 | fluency | low-hint, mixed, or timed use |
| L9 | critique / teach / create | teaches, critiques, designs examples, or creates |

## Assistance modes

```yaml
assistance_mode: guided | semi_guided | blind | barehand
score_type: assisted_score | semi_assisted_score | blind_score | barehand_score
```

Rules:

- guided evidence cannot prove L6.
- L6 needs blind misuse-discrimination evidence.
- L7 needs transfer evidence, preferably blind or barehand.
- barehand means no notes, no hints, and usually cross-day mixed scope.

## Concept state row

```yaml
concept:
priority: A | B | C | interest_extension
target_level: L1-L9
current_evidence_level: L1-L9
latest_assistance_mode: guided | semi_guided | blind | barehand
evidence:
next_required_check:
```

## Evidence event row

```yaml
date:
concept:
event_type: recall | standard_application | misuse_discrimination | transfer | barehand | flawed_answer_review | fluency
assistance_mode:
score_type:
result:
evidence_level_candidate:
notes:
```

## Verifiability

```yaml
verifiability: high | medium | low
```

- high: exact scoring and repair tests are allowed.
- medium: use rubric plus model-vs-reality distinction.
- low: avoid pseudo-precise mastery claims.
