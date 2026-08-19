# Generation Barrier Checklist

Use before Critique.

- [ ] Every scheduled Generator and replacement is terminal: completed / failed / cancelled / contaminated.
- [ ] No still-running expensive execution is duplicated without policy approval.
- [ ] Failed/cancelled/timed-out executions have reasons recorded (timeout is `failed` with `failure_reason: "timeout"` unless still observable).
- [ ] Every completed Generator has `result.json`.
- [ ] Every completed Generator has a stable `artifact_ref`.
- [ ] Return-only completed Generators have `direct_workspace_write: false` and `return_only_normalized_by_orchestrator: true`, with `raw_return_ref` when safe.
- [ ] Contaminated candidates are marked and excluded from the usable candidate set.
- [ ] No candidate is treated as independent after cross-reading another candidate.
- [ ] Terminal executions are distinguished from usable candidates: usable means completed, uncontaminated, and artifact-backed.
- [ ] Usable candidate count meets policy minimum, or degradation is explicitly approved/recorded.
- [ ] Replacement attempts use distinct IDs (e.g., `G3R1`) and record `replaces`.
- [ ] Replacement budget usage is recorded.
- [ ] Candidate IDs are stable for evaluation.
- [ ] Provider/model identity is removed from evaluation input when practical.
- [ ] Manifest execution records match workspace result files.
