---
type: Darwin Domain Research
title: Round 2 Domain Research
description: Research basis for evaluating the Crash Course Learning OKF Factory.
tags: [darwin, domain-research, round-2]
timestamp: 2026-06-30T00:00:00-07:00
---
# Round 2 Domain Research

## Research Scope

Evaluate whether the Crash Course Learning OKF Factory can reliably produce and maintain a stateful course-learning OKF instance for short pass-level exam preparation.

## Research Method

- user_provided_requirements: the user's twelve-point requirement statement in the conversation.
- project_documents: `docs/URD.md`, `docs/ADD.md`, `factory/`, `schemas/`, `playbooks/`, `templates/`, and prior `analysis/` reports.
- dry_run_validation: local structural inspection and minimal executable tests.

No external web research or independent sub-agent execution was used in this round.

## Key Findings

1. The factory identity is now clear: it generates course-specific OKF instances rather than one fixed learning plan.
2. URD and ADD now match the user's main requirements, and the ADD matrix is formally lower triangular.
3. State files, resume rules, score history, misconceptions, recall deck, and plan adaptation are represented in schemas, templates, and playbooks.
4. The main remaining implementation gap was materialization: a user or AI still had to manually create the full file tree from the contract.
5. A minimal deterministic skeleton generator would reduce missing-file risk without turning the MVP into a heavy application.

## Candidate Evaluation Concerns

| Concern | Risk |
|---|---|
| Pure document contract with no executable skeleton | Generated instances may omit files despite strong docs. |
| Content generation from weak sources | Course-specific quality remains limited by available materials. |
| Dry-run scoring | Scores may be optimistic without real course trials. |
| Over-expansion | Adding a full app would exceed MVP scope. |

## Evidence Gaps

- No full real-course trial on management, macroeconomics, or religious philosophy.
- No independent judge/sub-agent comparison.
- No grading calibration against an actual teacher's exam rubric.

## Confidence Level

Medium. The file-level evidence is strong, but effect quality is still dry-run only.
