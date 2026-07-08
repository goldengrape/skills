# Darwin Round 7 Test Report

## Unit tests

```text
python -m pytest -q
14 passed
```

## Macro smoke test

Command:

```bash
python tools/materialize_course_okf.py \
  --course-name '宏观经济学' \
  --baseline zero \
  --days-available 7 \
  --daily-minutes 60 \
  --target-score 60 \
  --time-policy soft \
  --target-learning-level L6 \
  --output-dir /mnt/data/r7_macro_test
```

Result:

```yaml
validation_result.passed: true
quality_gate.passed: true
quality_score: 100
learning_control_quality.passed: true
learning_control_quality.minimal_contract_files:
  - learning-contract/index.md
  - teacher/learning-control-policy.md
  - state/concept-mastery-state.md
  - state/assessment-evidence-ledger.md
visual_teaching_quality.passed: true
diagram_assets_found: 7
```

## Regression checks

- Old split learning-control files are not generated.
- Compact learning-control files are generated.
- L6 default remains recorded.
- L7 override remains recorded.
- Removing `learning-contract/index.md` fails the learning-control gate.
- Macro course seed still repairs generic skeletons and produces diagram assets.
