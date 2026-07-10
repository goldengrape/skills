---
type: Validation Playbook
title: Validate Cycle Pack
description: DP-007 read-only validation gate for factory inputs, generated packs, session records, and rollover output.
tags: [validation, quality, gate]
timestamp: 2026-07-09T18:10:00-07:00
---

# DP-007 — Validation Gate

## Rule

Validation is read-only. It reports defects. It does not silently rewrite inputs or artifacts.

## Input Gate

Fail when:

- cycle duration is unsupported and not explicitly approved,
- the primary task is not spoken-English training,
- a blocking conflict is hidden rather than recorded.

## Blueprint Gate

Fail when:

- there are more than three primary targets,
- days lack a meaningful progression,
- a target has no learner-intent or evidence basis,
- the selected activities cannot fit the time budget.

## Course-Pack Gate

Fail when:

- a required file is missing,
- the number of day files differs from `cycle_days`,
- a day lacks a named scenario, speaking task, repair or transfer task, evidence target, or closeout,
- the default day exceeds 15 minutes,
- generic placeholders remain in mission or day plans; structured `pending` review fields are allowed before the cycle is completed,
- runtime rules are duplicated inconsistently,
- the pack requires Python, hooks, a virtual machine, or a hidden database.

## Live-Runtime Gate

Fail when:

- the coach is instructed to dominate speaking time,
- corrections are long, repeated, or lecture-like,
- naturalness feedback is prohibited without reason,
- the closeout has no protected time,
- pronunciation certainty is unsupported.

## Session-Record Gate

Fail when:

- the completed task is absent,
- high-value correction evidence is absent despite recorded corrections,
- pronunciation notes lack confidence labels,
- the state patch is missing,
- the next action is missing or more than one next action is active,
- a recurring pattern or stable phrase is asserted without sufficient evidence or an explicit exception,
- observed, reported, inferred, and uncertain claims are materially blurred,
- the record claims automatic persistence.

## Rollover Gate

Fail when:

- the next-cycle proposal does not cite prior evidence,
- continue/change/retire/test-next decisions are missing,
- stable items are retained without reason,
- stable or retired status is asserted without evidence references or threshold support,
- the proposed cycle exceeds three primary targets.

## Output Format

```markdown
# Validation Report

- status: PASS | FAIL
- scope: input | blueprint | course_pack | live_runtime | session_record | rollover

## Defects
- ID:
  severity: blocking | major | minor
  artifact:
  rule:
  evidence:
  required_fix:

## Warnings
- 
```

A pack passes only when no blocking or major defects remain.
