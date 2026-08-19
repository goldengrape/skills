# Generation Barrier Checklist

Use before Critique.

- [ ] Every scheduled Generator and replacement is terminal: completed / failed / cancelled / contaminated.
- [ ] No still-running expensive execution is duplicated without policy approval.
- [ ] Failed/cancelled/timed-out/capability-mismatched executions have reasons recorded (timeout is `failed` with `failure_reason: "timeout"` unless still observable).
- [ ] Every completed Generator has `result.json` or backend-equivalent normalized terminal metadata.
- [ ] Every completed Generator has a stable `artifact_ref`.
- [ ] Every browser-operated independent Generator used a fresh page/tab and a fresh conversation; project/workspace base URLs were not reused as existing conversations.
- [ ] No browser Generator was created by reusing another Generator's follow-up chain, saved session, reattached conversation, or prior-turn context.
- [ ] For `direct_required` workspace mode, every usable Generator wrote the substantive candidate directly to its assigned workspace namespace/branch and the referenced artifact was independently verified.
- [ ] For `direct_required` workspace mode, no usable Generator was silently downgraded to long inline response/file-transfer transport.
- [ ] Return-only completed Generators exist only when fallback was explicitly permitted and have `direct_workspace_write: false` and `return_only_normalized_by_orchestrator: true`, with `raw_return_ref` when safe.
- [ ] Contaminated candidates are marked and excluded from the usable candidate set.
- [ ] No candidate is treated as independent after cross-reading another candidate or reusing contaminated browser context.
- [ ] Terminal executions are distinguished from usable candidates: usable means completed, independently isolated when required, policy-compliant, uncontaminated, and artifact-backed.
- [ ] Usable candidate count meets policy minimum, or degradation is explicitly approved/recorded.
- [ ] Replacement attempts use distinct IDs (e.g., `G3R1`) and record `replaces`.
- [ ] Replacement budget usage is recorded.
- [ ] Candidate IDs are stable for evaluation.
- [ ] Provider/model identity is removed from evaluation input when practical.
- [ ] Manifest execution records match workspace result files/artifact refs.
