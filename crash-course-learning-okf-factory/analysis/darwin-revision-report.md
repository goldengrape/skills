---
type: Darwin Revision Report
title: Darwin-Style Revision Report
description: Evaluation, revision actions, and validation result after applying Darwin-style optimization.
tags: [darwin, revision, evaluation]
timestamp: 2026-06-30T00:00:00-07:00
---

# Darwin-Style Revision Report

## Method

This revision used the Darwin loop in a local, document-focused form:

1. Read the current OKF factory files.
2. Freeze the user's requirement as the domain standard.
3. Build URD and ADD using the vibe coding skill process.
4. Dry-run evaluate the implementation against ADD.
5. Revise the weakest contract and state-persistence points.
6. Validate the revised bundle with a structural check.

No independent sub-agent execution was available in this environment, so the effect evaluation is marked as **dry_run**.

## Domain Rubric Used

| Dimension | Weight | What was checked |
|---|---:|---|
| R1 Meta-factory identity | 12 | It generates course OKF instances, not one fixed learning plan. |
| R2 Short-term pass orientation | 10 | It optimizes for pass-level readiness under time limits. |
| R3 Generated layout completeness | 15 | It requires the full course instance tree. |
| R4 State persistence | 15 | It stores current state, topics, recall cards, misconceptions, score history, next action, and plan changes. |
| R5 Resume behavior | 12 | It reads state and evidence before choosing the next session. |
| R6 Adaptive planning | 12 | It repairs weak topics and rewrites future plans when evidence requires it. |
| R7 Daily package fit | 8 | It keeps daily work near the configured minute budget. |
| R8 Source grounding | 8 | It records materials, source confidence, and gaps. |
| R9 Validation and output contract | 8 | It returns created files, initial state, entrypoints, rules, and validation result. |

## Scores

| Version | Score | Evaluation mode | Notes |
|---|---:|---|---|
| Uploaded baseline | 73 | dry_run | Good structure, incomplete contracts and state templates. |
| Revised version | 89 | dry_run | Input/output contracts, generated layout, state templates, and validation were strengthened. |

## Kept Revisions

| Area | Revision |
|---|---|
| Requirements | Added `docs/URD.md` with roles, goals, requirements, constraints, out-of-scope items, and acceptance criteria. |
| Design | Added `docs/ADD.md` with FR/DP mapping, design matrix, execution order, coupling notes, and failure-mode responses. |
| Input contract | Revised baseline, target score, course type, materials, constraints, and preferences. |
| Output contract | Added `schemas/course-okf-output.md` and required validation output fields. |
| Generated layout | Required daily plans, quiz files, initial learning record, session placeholder, final-review files, and `state/plan-changes.md`. |
| State memory | Added score-history, next-action, and plan-change templates/schemas. |
| Resume and adaptation | Strengthened read order and repair/review/simulate decision rules. |
| Source grounding | Added resource registry template and confidence fields. |
| Validation | Added validation playbook and stricter checklist. |
| Markdown reliability | Replaced nested triple-fence template blocks with four-backtick outer fences. |

## Remaining Risks

| Risk | Status | Recommended next step |
|---|---|---|
| No executable generator code exists yet. | Accepted for current OKF-document version. | If needed, create a small CLI that materializes a course instance from these templates. |
| Actual course quality still depends on available materials. | Accepted. | Keep `resources.md` and source gaps visible in every generated instance. |
| Dry-run evaluation may overestimate quality. | Accepted with disclosure. | Test with three real courses: management, macroeconomics, and religious philosophy. |


## ADD Matrix Follow-up Revision

A follow-up revision made the ADD matrix formally lower triangular. DP11 validation was moved out of FR1-FR10 and kept only as ADD-FR-011. The layout/state and state/update dependencies were also separated so earlier FRs do not depend on later DPs. See `analysis/add-lower-triangular-revision.md`.

---

# Darwin Round 2 — Evaluation and Revision

## Method

This round followed Darwin-style evaluation in a local-document + local-test form:

1. Read the lower-triangular version.
2. Created a project-specific round-2 domain research note and rubric.
3. Re-scored the package with an added MVP executability dimension.
4. Chose the weakest dimension: deterministic skeleton materialization.
5. Added the smallest implementation that addresses that weakness.
6. Ran local pytest checks.

Evaluation mode: **dry_run + local_tests**. No independent sub-agent execution was available.

## Baseline Under Round-2 Rubric

Score: **82.4 / 100**.

The lower-triangular ADD and stateful OKF design were solid, but the package still relied on manual or AI execution to create the required file tree.

## Revision Kept

Added:

```text
tools/materialize_course_okf.py
tools/README.md
tests/test_materialize_course_okf.py
examples/management-factory-input.json
analysis/darwin-round-2/
```

The helper creates a required Course Learning OKF skeleton, initializes state, creates daily plans and quizzes for variable day counts, creates final-review placeholders, and writes `generation-output.json` with `validation_result`.

## Test Result

```text
python -m pytest -q
3 passed
```

## Post-Revision Score

Score: **91.8 / 100** under the round-2 rubric.

| Area | Before | After |
|---|---:|---:|
| Round-2 score | 82.4 | 91.8 |
| MVP executability | 3/10 | 8/10 |
| Local tests | none | 3 passed |

## Remaining Risks

| Risk | Status | Recommended next step |
|---|---|---|
| No real-course trial yet. | Still open. | Generate and resume management, macroeconomics, and religious philosophy instances. |
| Materializer creates skeletons, not full course content. | Intended MVP boundary. | Fill course content through reconnaissance and playbooks. |
| Dry-run evaluation can overestimate quality. | Disclosed. | Use real prompts and learner evidence in the next evaluation round. |
