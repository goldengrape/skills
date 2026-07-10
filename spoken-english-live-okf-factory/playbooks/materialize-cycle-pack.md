---
type: Playbook
title: Materialize Cycle Pack
description: DP-003 procedure for converting a cycle blueprint into a compact Markdown course pack.
tags: [playbook, generation, markdown]
timestamp: 2026-07-09T18:10:00-07:00
---

# DP-003 — Materialize Cycle Pack

## Inputs

- Cycle Evidence Snapshot from DP-001.
- Cycle Blueprint from DP-002.
- Layout from `schemas/course-pack-layout.md`.

## Procedure

1. Create exactly the required directories and files.
2. Write `mission.md` with the confirmed goal, defaults, evidence gaps, and cycle targets.
3. Write `plan/cycle-plan.md` from the blueprint.
4. Create one `plan/day-N.md` per cycle day.
5. Initialize canonical state from prior evidence without erasing unresolved items.
6. Generate course-specific Live settings. Do not copy or redefine the global runtime protocol.
7. Initialize review files as structured placeholders with completion criteria.
8. Run DP-007 validation before presenting the pack.

## Daily Plan Contract

Every day file contains:

```markdown
## Goal
## Scenario and roles
## Time budget
## Recall cue
## Opening question
## Main speaking task
## Optional live micro-correction targets
## Learner-output target and coach-turn limit
## Fatigue or short-time fallback
## Repair and repetition
## Transfer question
## Evidence to capture
## Closeout instruction
```

## Compactness Rules

Do not create:

- a separate speaking map,
- a separate scenario map,
- a duplicate phrase bank,
- a separate correction policy,
- a teacher notebook,
- separate files for errors, interests, pronunciation notes, or next action.

Add a new file only when an observed retrieval or update failure cannot be solved inside an existing authoritative file.

## Failure Rules

- Missing day file → fail generation.
- Placeholder-only scenario or task → fail generation.
- More than three primary targets → return to DP-002.
- Runtime rules copied inconsistently into several files → keep one authoritative protocol and replace duplicates with references.
