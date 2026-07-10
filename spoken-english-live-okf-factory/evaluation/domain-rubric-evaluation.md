---
type: Domain Rubric Evaluation
title: Spoken English Live OKF Factory Rubric Quality Evaluation
description: Darwin RQ1–RQ9 quality review of the proposed domain scoring scheme.
tags: [darwin, rubric-quality, evaluation]
timestamp: 2026-07-09T21:30:00-07:00
---

# Domain Rubric Quality Evaluation

## Result

- **Overall quality score:** 95/100
- **Decision:** `accept`
- **Hard-gate review:** passed
- **Research confidence:** medium
- **Rubric freeze status:** frozen for the v0.8 optimization run

The rubric is sufficiently grounded and operational for the v0.8 optimization run. The user explicitly requested Darwin optimization after reviewing the earlier policy, so the 35/65 weighting and clear intelligible global-English target are frozen for this run. A real Live session is still mandatory before the package score becomes non-provisional.

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

The boundaries are sufficiently clean for operational scoring:

- D3 evaluates the task's speaking opportunity;
- D4 evaluates how the coach conducts the interaction;
- D5 evaluates feedback events;
- D6 evaluates time and fatigue control.

Topic affinity, task difficulty, and Live orchestration now have explicit evidence fields, reducing the earlier overlap. A long correction is scored primarily under D5, with secondary D4 or D6 effects only when interaction or time is observably damaged.

## RQ5 — Observability and Scoreability

**Score: 14/15**

Each dimension includes 1/5/10 anchors, common failures, and concrete evidence to inspect. The three evidence modes prevent static review from pretending to validate Live behavior. The score is reduced only because learner/coach speaking share lacks objective telemetry and pronunciation reliability requires direct audio observation. Interest adaptation is now observable through topic intent, engagement-cause classification, recent-topic balance, and hard gate HG-10.

## RQ6 — Weight Reasonableness

**Score: 9/10**

The highest weights go to authentic speaking, Live orchestration, and corrective feedback because these are the main value and risk areas. Continuity and evidence integrity receive meaningful weight. Runtime compactness receives a smaller numeric weight because its severe failures are also protected by hard gates. The 35/65 common/domain composite is frozen for this optimization run; later longitudinal evidence may justify revisiting it.

## RQ7 — Hard-Gate Reasonableness

**Score: 10/10**

The hard gates target failures that invalidate the workflow regardless of polished writing or high scores elsewhere: non-speaking sessions, unsafe pronunciation certainty, broken timebox/closeout, missing persistence chain, fabricated evidence, continuity failure, unavailable runtime dependencies, and silent validation repair. None is merely a stylistic preference.

## RQ8 — Test-Prompt Match

**Score: 10/10**

The twelve prompts cover:

- cold-start generation;
- conflicting evidence;
- real Live correction;
- fatigue adaptation;
- evidence-sensitive closeout;
- mixed-completion rollover;
- adversarial runtime requests;
- naturalness coaching without grammar errors;
- adaptive interest discovery and current-event fallback;
- expertise versus interest confounds;
- topic monoculture prevention;
- slow current-event verification fallback.

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

None for this optimization run. Full Live observation remains required before treating the package score as non-provisional.

## Decision Rationale

The quality threshold is exceeded and all critical RQ minimums pass:

- RQ1: 15/15, above the 10/15 minimum;
- RQ5: 14/15, above the 10/15 minimum;
- RQ7: 10/10, above the 6/10 minimum.

The user explicitly requested this optimization after the scoring policy was established. The decision is therefore `accept` for this run, while the resulting package score remains provisional until Live observation.
