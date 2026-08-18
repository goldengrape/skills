# Run Start Checklist

Use before `GENERATING`.

- [ ] User-provided Shared Workspace root is identified.
- [ ] Workspace scope is dedicated or explicitly approved.
- [ ] Orchestrator can read/write required control state.
- [ ] Task snapshot is frozen and stored.
- [ ] Material constraints and assumptions are separated.
- [ ] Available Agent Executors and capabilities are known.
- [ ] Generator count and budget policy are set.
- [ ] Verifier mode is `auto`, `enabled`, or `disabled` with reason.
- [ ] One isolated output namespace exists per Generator.
- [ ] No Generator has access to sibling candidate outputs.
- [ ] Run manifest is valid before dispatch.
