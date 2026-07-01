---
type: Darwin Evaluation
title: Darwin Round 4 Evaluation — Teaching Runtime Quality
description: Evaluation and revision notes after the Day 1 macroeconomics teaching-session review.
tags: [darwin, evaluation, round-4, teaching-runtime]
timestamp: 2026-06-30T00:00:00-07:00
---
# Darwin Round 4 Evaluation

## Trigger

The generated macroeconomics crash course was tested in a real Day 1 learning session. The session showed that the course content was useful, but the teaching runtime leaked answer elements before the learner answered. For example, a student-facing prompt included the expected points for a GDP and welfare question.

## Main Failure Class

Previous factory quality checks handled:

1. file structure;
2. course-specific content;
3. repair and recheck.

They did not check whether the generated teaching interaction was fair and recoverable as a conversation. The new failure class is:

```text
teaching_runtime_quality_failure
```

## Findings

| Finding | Impact | Revision |
|---|---|---|
| Teacher-visible expectations were mixed into student-visible prompts. | Assessment scores can be inflated and state can be overconfident. | Added `teacher/` runtime files and prompt-visibility lint. |
| Score history did not distinguish blind vs assisted scores. | Recovery logic cannot know how reliable a score is. | Added `score_type` and `prompt_visibility`. |
| Daily minutes were treated too much like a hard limit. | Learner interest can be harmed. | Added `time_policy: soft | strict`, default `soft`. |
| Learner-led questions were not separately tracked. | High-interest branches are lost. | Added `state/interest-ledger.md`. |
| Engagement handling was not specified. | Teacher may over-lecture or fail to recover attention. | Added observable-signal engagement monitor and intervention rules. |

## Revision Kept

```text
teaching-runtime-layer
```

This revision is still MVP-sized. It does not build a complex tutor. It only adds the minimal files, rules, and lint checks needed to avoid prompt leakage, preserve interest, and make scores more honest.

## Test Result

```text
python -m pytest -q
7 passed
```

## Macroeconomics Smoke Test

```yaml
course_name: 宏观经济学
baseline: zero
days_available: 7
daily_minutes: 60
time_policy: soft
validation_result.passed: true
structural.passed: true
quality_gate.passed: true
teaching_runtime_quality.passed: true
quality_score: 100
```

## Remaining Limitations

- The local materializer creates runtime files and checks prompt leakage, but it does not actually execute a live session.
- Engagement monitoring is deliberately conservative: it uses observable signals only and does not claim to know learner psychology.
- Teacher notebook privacy is a procedural/runtime rule. In a plain local folder the learner can still open the teacher files; the teaching agent must avoid pasting private sections into the conversation before assessment.
