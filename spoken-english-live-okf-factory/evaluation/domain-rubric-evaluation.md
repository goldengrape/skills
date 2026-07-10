---
type: Domain Rubric Evaluation
title: Spoken English Live OKF Factory Rubric Quality Evaluation
description: Darwin RQ1–RQ9 quality review of the proposed domain scoring scheme.
tags: [darwin, rubric-quality, evaluation]
timestamp: 2026-07-09T19:20:00-07:00
---

# Domain Rubric Quality Evaluation

## Result

- **Overall quality score:** 94/100
- **Decision:** `needs_user_confirmation`
- **Hard-gate review:** passed
- **Research confidence:** medium
- **Rubric freeze status:** not frozen

The rubric is sufficiently grounded and operational to enter Darwin Phase 0.35. It should not yet be frozen because three policy choices remain for the user: the common/domain weighting, whether a real Live session is mandatory for a non-provisional baseline, and the default pronunciation target.

## RQ1 — Goal Match

**Score: 15/15**

The rubric directly evaluates the complete intended workflow: evidence intake, cycle generation, speaking-first Live delivery, concise correction, 15-minute time discipline, Markdown closeout, and cross-cycle adaptation. It does not drift into grading the learner's general intelligence or treating the bundle as a conventional exam-preparation course.

## RQ2 — Research Sufficiency

**Score: 13/15**

The research combines user-confirmed requirements, direct project inspection, current official OpenAI documentation, official CEFR and ACTFL frameworks, and corrective-feedback research. The score is reduced because no longitudinal learner deployment, independent teacher calibration, or audio benchmark exists yet. The recent GenAI study is preliminary and is correctly assigned low evidentiary weight.

## RQ3 — Dimension Completeness

**Score: 10/10**

The nine dimensions cover all material outcomes and failure surfaces:

- personalization;
- cycle design;
- spoken-task authenticity;
- real-time orchestration;
- correction and naturalness;
- time/fatigue;
- closeout evidence;
- rollover;
- runtime truthfulness.

No major project responsibility is left unscored.

## RQ4 — Dimension Independence

**Score: 9/10**

The boundaries are mostly clean:

- D3 evaluates the task's speaking opportunity;
- D4 evaluates how the coach conducts the interaction;
- D5 evaluates feedback events;
- D6 evaluates time and fatigue control.

Some natural overlap remains because a long correction also affects speaking share and time. The rubric resolves this by scoring the correction defect primarily under D5 and recording its secondary effects under D4 or D6 only when the interaction or timebox is observably damaged.

## RQ5 — Observability and Scoreability

**Score: 13/15**

Each dimension includes 1/5/10 anchors, common failures, and concrete evidence to inspect. The three evidence modes prevent static review from pretending to validate Live behavior. The score is reduced because learner/coach speaking share lacks objective telemetry and pronunciation reliability requires direct audio observation.

## RQ6 — Weight Reasonableness

**Score: 9/10**

The highest weights go to authentic speaking, Live orchestration, and corrective feedback because these are the main value and risk areas. Continuity and evidence integrity receive meaningful weight. Runtime compactness receives a smaller numeric weight because its severe failures are also protected by hard gates. The 35/65 common/domain composite is reasonable but requires user confirmation.

## RQ7 — Hard-Gate Reasonableness

**Score: 10/10**

The hard gates target failures that invalidate the workflow regardless of polished writing or high scores elsewhere: non-speaking sessions, unsafe pronunciation certainty, broken timebox/closeout, missing persistence chain, fabricated evidence, continuity failure, unavailable runtime dependencies, and silent validation repair. None is merely a stylistic preference.

## RQ8 — Test-Prompt Match

**Score: 10/10**

The eight prompts cover:

- cold-start generation;
- conflicting evidence;
- real Live correction;
- fatigue adaptation;
- evidence-sensitive closeout;
- mixed-completion rollover;
- adversarial runtime requests;
- naturalness coaching without grammar errors.

Every dimension and hard gate is exercised by at least one prompt. The suite includes both normal and adversarial cases and clearly labels full-Live versus proxy evidence.

## RQ9 — Resistance to Template Contamination

**Score: 5/5**

The rubric is not a renamed copy of Darwin's common structural rubric. Its dimensions use domain-specific constructs, user decisions, Live runtime constraints, language-assessment frameworks, and corrective-feedback risks. Generic qualities such as “workflow clarity” are left to the common rubric.

## Hard-Gate Review

| Check | Result | Note |
|---|---|---|
| Gates correspond to high-risk domain failures | PASS | Each gate can invalidate the learning workflow or evidence integrity. |
| Gates are externally observable | PASS | Each can be checked in files, interaction, closeout, or rollover evidence. |
| Gates do not duplicate ordinary quality preferences | PASS | Minor style and polish remain numeric dimensions. |
| Gates do not require unavailable telemetry | PASS | Speaking-share is a scored dimension, not a strict numeric gate. |
| Pronunciation gate avoids native-speaker bias | PASS | It requires evidence and prioritizes intelligibility. |

## Required Revisions Before Freezing

No structural rewrite is required. The user must confirm or revise:

1. `common_weight = 0.35`, `domain_weight = 0.65`;
2. whether at least one `full_live` test is mandatory for a non-provisional baseline;
3. whether “clear, intelligible global English” is the default pronunciation target;
4. whether the first baseline uses the included example learner or the user's real profile.

After any modification, rerun this RQ1–RQ9 evaluation before freezing.

## Decision Rationale

The quality threshold is exceeded and all critical RQ minimums pass:

- RQ1: 15/15, above the 10/15 minimum;
- RQ5: 13/15, above the 10/15 minimum;
- RQ7: 10/10, above the 6/10 minimum.

Because research confidence is medium and Darwin requires human confirmation before freezing, the decision is `needs_user_confirmation`, not automatic acceptance.
