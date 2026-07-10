---
type: Playbook
title: Rollover Cycle
description: DP-006 evidence-based procedure for completing one cycle and preparing the next without automatic carry-over.
tags: [playbook, rollover, continuity, evidence]
timestamp: 2026-07-09T20:25:00-07:00
---

# DP-006 — Rollover Cycle

## Inputs

- original cycle plan;
- all completed session records;
- explicit skipped or partial-session records;
- canonical learner state;
- phrase deck;
- scenario ledger.

If records are missing, produce a partial-cycle review and name the evidence gap. Do not infer completion.

## Step 1 — Build an Evidence Table

For each planning claim, cite a session or state reference.

| Item | Status | Evidence refs | Confidence |
|---|---|---|---|
| scenario performance | improved / unchanged / mixed / unknown | session IDs | high / medium / low |
| phrase retrieval | learning / stable / not tested | session IDs | high / medium / low |
| recurring pattern | active / improved / uncertain / retired | session IDs | high / medium / low |
| fluency or interaction | improved / unchanged / mixed / unknown | session IDs | high / medium / low |
| fatigue or duration | sustainable / tiring / unknown | session IDs or learner report | high / medium / low |

Skipped days are attendance facts, not evidence of inability.

## Step 2 — Make Four Decisions

State explicitly:

- **continue:** still valuable and not yet stable;
- **change:** useful target, but task, cue, pressure, or explanation should change;
- **retire:** stable enough to leave the active set, with evidence;
- **test next:** uncertain, unobserved, or contradictory.

Default thresholds:

- retire a phrase only after spontaneous appropriate use in at least two sessions or three varied contexts;
- retire an error target only after at least two later opportunities without recurrence, including one transfer context;
- do not declare relapse from one isolated later occurrence;
- do not carry an item forward merely because it appeared in the previous plan.

When evidence is too thin, choose `test next`, not `retire` or `continue` with false certainty.

## Step 3 — Propose the Next Cycle

Recommend:

- 3 or 7 days;
- daily duration;
- one scenario target;
- one fluency/discourse target;
- one language-repair target;
- carry-over phrases and retests;
- one learner interest when it improves task authenticity.

Every target must cite at least one evidence reference or explicit current learner instruction.

## 🔴 CHECKPOINT — Learner Choice Before a Materially New Direction

Stop at the proposal when:

- the primary goal or scenario family changes;
- the recommended duration changes;
- the proposal chooses 3 days instead of 7, or vice versa, for reasons other than the learner's explicit request;
- two next-cycle directions are equally supported.

Present the options and evidence briefly. The next factory run begins only after the learner chooses or explicitly asks the agent to choose.

## Output

Create:

1. `review/cycle-review.md`;
2. `review/next-cycle-proposal.md`;
3. a compact carry-over snapshot compatible with DP-001.

The proposal does not edit the completed cycle's blueprint.

## Failure Rules

| Trigger | Required response |
|---|---|
| Proposal has no evidence references | Reject and add session/state references. |
| More than three primary targets | Reduce scope before presentation. |
| Every old target is carried forward | Re-evaluate stable, low-value, and untested items. |
| Skipped day is described as failed performance | Correct it to skipped or unknown. |
| Stable/retired claim does not meet the threshold | Downgrade to learning, improved, or test next. |
| Next direction materially changes without learner confirmation | Stop at the checkpoint. |
