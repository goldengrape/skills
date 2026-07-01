---
type: Darwin Domain Rubric
title: Round 2 Domain Rubric
description: Domain scoring standard for the Crash Course Learning OKF Factory.
tags: [darwin, rubric, round-2]
timestamp: 2026-06-30T00:00:00-07:00
---
# Round 2 Domain Rubric

## Goal

Score whether the factory can generate a stateful, resumable, short-term pass-oriented Course Learning OKF instance.

## Dimensions

| ID | Dimension | Weight | 10-point anchor |
|---|---|---:|---|
| D1 | Meta-factory identity | 10 | Clearly reusable across courses; no fixed-course leakage. |
| D2 | Input/output contract | 10 | Normalized input, output object, defaults, and validation fields are explicit. |
| D3 | Generated layout completeness | 12 | Required file tree covers mission, maps, resources, plan, state, sessions, records, quizzes, and final review. |
| D4 | State persistence | 14 | Current state, topic ledger, recall deck, misconceptions, score history, next action, and plan changes are all concrete. |
| D5 | Resume behavior | 10 | Resume reads saved state and evidence before deciding whether to continue, repair, review, simulate, or final-review. |
| D6 | Adaptive planning | 10 | Evidence triggers plan repair and records changed files and reasons. |
| D7 | Daily package fit | 8 | Daily sessions fit the configured minute budget and protect state updates. |
| D8 | Source grounding | 8 | Resources track source priority, confidence, and gaps; user materials outrank generic knowledge. |
| D9 | Validation and tests | 10 | Generated output can be checked structurally and failures are reported, not hidden. |
| D10 | MVP executability | 8 | A minimal helper or equivalent procedure can materialize the skeleton without requiring manual file creation. |

## Hard Gates

| Gate | Failure condition |
|---|---|
| HG1 | No required state directory or no `state/next-action.md`. |
| HG2 | Generated course is only a plan, not an OKF instance. |
| HG3 | Resume flow ignores saved state. |
| HG4 | No validation result or missing files are silently accepted. |
| HG5 | Revision introduces a heavy app that exceeds MVP scope. |

## Scoring Note

This round uses dry-run scoring plus local tests. Scores must say `dry_run` unless a real course instance is generated, resumed, and updated with learner evidence.
