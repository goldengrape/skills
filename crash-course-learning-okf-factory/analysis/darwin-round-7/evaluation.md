# Darwin Round 7 Evaluation — Occam Learning Control

## Goal

Apply Darwin-style optimization to round6 with an Occam constraint: preserve learning-control behavior while removing unnecessary runtime file proliferation and duplicated policy fragments.

## Baseline observation

Round6 correctly introduced:

- L1-L9 learning stages.
- Default core target L6.
- AI assistance modes.
- Productive friction and AI diet.
- Verifiability policy.
- Feedback anchoring.
- Model-vs-reality separation.
- Barehand and transfer evidence.

However, the same control logic was split across many tiny runtime artifacts:

- `learning-contract/user-goal.md`, `assumptions.md`, `target-levels.md`, `learning-stage-rubric.md`, `verifiability-map.md`, `stage-to-assessment-map.md`
- `teacher/stage-aligned-assessment-policy.md`, `ai-diet-policy.md`, `productive-friction-policy.md`, `verifiability-policy.md`, `feedback-anchor-policy.md`, `model-vs-reality-protocol.md`, `negative-feature-list.md`
- `state/concept-stage-history.md`, `barehand-checkpoints.md`, `transfer-checks.md`, `ai-assistance-log.md`

This made the generated Course OKF more verbose without adding independent runtime decisions.

## Round7 change

Collapse the learning-control layer into four generated artifacts:

```text
learning-contract/index.md
teacher/learning-control-policy.md
state/concept-mastery-state.md
state/assessment-evidence-ledger.md
```

Source-side consolidation:

```text
schemas/learning-control.md
playbooks/manage-learning-control.md
```

Removed redundant source playbooks and schemas that only repeated these rules.

## Capability preservation

The compact layer still enforces:

- L1-L9 stages.
- Default core L6.
- guided / semi_guided / blind / barehand modes.
- L6 misuse-discrimination requirement.
- L7 transfer requirement.
- 2-3 day barehand checkpoint recommendation.
- verifiability-sensitive scoring.
- productive friction preservation.
- product/source anchored feedback.
- model-vs-reality separation.
- negative feature blacklist.

## Quantitative result

Macro smoke generated Course OKF:

| Metric | Round6 | Round7 |
|---|---:|---:|
| materializer created files | 86 | 71 |
| generated course files | 95 | 80 |
| learning-control runtime artifacts | 17 | 4 |
| quality score | 100 | 100 |
| pytest | 14 passed | 14 passed |

## Darwin decision

Keep the round7 revision. It reduces surface area while preserving hard gates and passing the same macro smoke test. This is a strict improvement under Occam's razor: fewer artifacts, same behavior, same validation score.
