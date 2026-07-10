---
type: Playbook
title: Materialize Cycle Pack
description: DP-003 procedure for converting an interest-aware cycle blueprint into a compact Markdown course pack.
tags: [playbook, generation, markdown, adaptive-topics]
timestamp: 2026-07-09T21:30:00-07:00
---

# DP-003 — Materialize Cycle Pack

## Inputs

- Cycle Evidence Snapshot from DP-001.
- Cycle Blueprint from DP-002.
- Layout from `schemas/course-pack-layout.md`.

## Procedure

1. Create exactly the required directories and files.
2. Write `mission.md` with the confirmed goal, defaults, evidence gaps, cycle targets, and topic policy.
3. Write `plan/cycle-plan.md` with language progression separated from topic slots.
4. Create one `plan/day-N.md` per cycle day.
5. Initialize canonical state from prior evidence without erasing unresolved items.
6. Include structured interest and next-topic state inside `state/learner-state.md`; do not create a duplicate interest file.
7. Generate course-specific Live settings, including topic and current-event settings. Do not copy the global runtime protocol.
8. Initialize review files as structured placeholders with completion criteria.
9. Run DP-007 validation before presenting the pack.

## Daily Plan Contract

Every day file contains:

```markdown
## Language objective
## Topic mode
## Planned topic or evergreen fallback
## Topic adaptation card
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
## Interest evidence to capture
## Language evidence to capture
## Closeout instruction
```

For an anchored day, topic selection rules may simply say `use the planned topic`.

For an adaptive day, the topic adaptation card includes:

- `topic_intent`;
- candidate evidence sources;
- objective-fit, consent, knowledge-load, evidence, recent-topic, and time-fit checks;
- two-choice behavior when selection is ambiguous;
- evergreen fallback;
- load-reduction fallback;
- switch trigger;
- an instruction to preserve the language objective after switching topics.

For a current-event-optional day, include:

- runtime verification requirement;
- preferred and excluded categories;
- 30-second verification budget;
- maximum background length;
- three-part context capsule: what happened, why it fits today, learner question;
- evergreen fallback.

## Canonical Learner-State Sections

`state/learner-state.md` includes:

- progress;
- current language focus;
- active recurring errors;
- **interest and topic state**;
- pronunciation observations;
- fatigue or time notes;
- next action.

Interest and topic state distinguishes:

- explicit/observed confirmed interests;
- possible interests;
- low-engagement candidates;
- avoid/retired topics;
- recommended next topic and evidence basis;
- recent topic history and adaptation hypotheses;
- separate topic-affinity evidence from language, knowledge, prompt, fatigue, or privacy load.

## Compactness Rules

Do not create:

- a separate speaking map,
- a separate scenario map,
- a duplicate phrase bank,
- a separate interest ledger,
- a separate current-events policy file,
- a separate correction policy,
- a teacher notebook,
- separate files for errors, pronunciation notes, or next action.

Add a new file only when an observed retrieval or update failure cannot be solved inside an existing authoritative file.

## Failure Rules

- Missing day file → fail generation.
- Placeholder-only scenario or task → fail generation.
- More than three primary language targets → return to DP-002.
- Adaptive day without selection rule, fallback, or fixed language objective → fail generation.
- Current-event day with a hardcoded future article and no fallback → fail generation.
- Runtime rules copied inconsistently into several files → keep one authoritative protocol and replace duplicates with references.
