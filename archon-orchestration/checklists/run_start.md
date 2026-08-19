# Run Start Checklist

Use before `GENERATING`.

- [ ] User-provided Shared Workspace root is identified.
- [ ] Workspace scope is dedicated or explicitly approved.
- [ ] Backend adapter is selected only after backend is known.
- [ ] Orchestrator can read/write required control state.
- [ ] `manifest.json` exists with valid stage, policy, workspace, counters, scheduled generators, and artifact keys (schema 0.2; see `templates/manifest.json`).
- [ ] `task.md` is frozen, complete, and contains no `<TODO>` placeholders.
- [ ] Material constraints, success criteria, assumptions, and open questions are separated.
- [ ] Available Agent Executors and capabilities are recorded, including direct-write vs return-only.
- [ ] Generator count, minimum usable quorum, replacement budget, schema-repair budget, evaluator budget, and fusion retry budget are set.
- [ ] Verifier mode is `auto`, `enabled`, or `disabled` with reason.
- [ ] One isolated namespace exists per scheduled Generator.
- [ ] Each Generator has a dispatch package or enough dispatch metadata to reconstruct it.
- [ ] No Generator has access to sibling candidate outputs.
- [ ] Browser-operated independent Generators have distinct pages/sessions or equivalent isolation.
- [ ] Return-only normalization path is available before dispatching return-only Executors.
- [ ] Any non-persistent dry run is clearly labeled.
