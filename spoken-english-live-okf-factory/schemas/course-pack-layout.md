---
type: Schema
title: Course Pack Layout
description: DP-003 compact Markdown layout for a generated, interest-aware spoken-English cycle.
tags: [schema, course-pack, markdown, adaptive-topics]
timestamp: 2026-07-09T21:30:00-07:00
---

# DP-003 — Generated Course Pack Layout

```text
spoken-english-live-{learner-slug}-cycle-{N}/
├── index.md
├── mission.md
├── plan/
│   ├── cycle-plan.md
│   └── day-01.md ... day-N.md
├── state/
│   ├── learner-state.md
│   ├── phrase-deck.md
│   └── scenario-ledger.md
├── sessions/
│   ├── index.md
│   └── session-template.md
├── teacher/
│   └── live-session-settings.md
└── review/
    ├── cycle-review.md
    └── next-cycle-proposal.md
```

## File Responsibilities

| File | Responsibility |
|---|---|
| `index.md` | Reading order and current cycle status. |
| `mission.md` | Learner goal, assumptions, evidence basis, bounded language focus, and topic policy. |
| `plan/cycle-plan.md` | Whole-cycle language progression, anchored/adaptive topic slots, and carry-over evidence. |
| `plan/day-N.md` | One time-bounded Live session with a fixed language objective and usable topic plan or fallback. |
| `state/learner-state.md` | Canonical current state, active errors, interest/topic state, pronunciation observations, fatigue notes, and next action. |
| `state/phrase-deck.md` | Reusable expressions and recall status. |
| `state/scenario-ledger.md` | Practiced scenarios/topics, evidence, difficulty, engagement, and next variants. |
| `sessions/index.md` | Session record index. |
| `sessions/session-template.md` | Copyable closeout format. |
| `teacher/live-session-settings.md` | Course-specific runtime, topic-policy, and current-event parameters consumed by the factory runtime protocol. |
| `review/cycle-review.md` | Completed-cycle language and topic evidence summary. |
| `review/next-cycle-proposal.md` | Evidence-backed next-cycle recommendation and carry-over snapshot. |

## Canonical State Rule

`state/learner-state.md` is the single authority for:

- current cycle and day;
- current language focus;
- active recurring errors;
- confirmed, possible, low-engagement, avoided, and retired topic interests;
- recommended next adaptive topic and evidence basis;
- recent topic window and topic-diversity state;
- adaptation hypotheses with affinity/load separation;
- pronunciation observations;
- fatigue or time notes;
- next action.

Do not recreate separate files for these sections unless a future retrieval problem is demonstrated.

## Frontmatter

Every Markdown file uses:

```yaml
---
type:
title:
description:
tags: []
timestamp:
---
```
