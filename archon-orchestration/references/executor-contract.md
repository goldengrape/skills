# Agent Executor Contract

An Agent Executor is any backend the Orchestrator can delegate a bounded task to.

## Conceptual interface

```text
dispatch(task_package) -> execution_id
status(execution_id) -> pending | running | completed | failed | cancelled | contaminated
collect(execution_id) -> result metadata + artifact refs
cancel(execution_id) -> terminal status
```

## Capability declaration

Recommended fields:

```yaml
executor_id: chatgpt-web-1
kind: browser_agent
capabilities:
  browser: true
  workspace_read: true
  workspace_write: true
  shell: true
  long_running: true
  verifier_local: false
cost_class: high
latency_class: high
```

Do not infer missing capabilities from provider branding. Probe or configure them.

## Task package

Each dispatch should contain only what the role needs:

```json
{
  "task_id": "run-017-generator-G3",
  "run_id": "run-017",
  "role": "generator",
  "objective": "...",
  "task_snapshot_ref": "workspace://run-017/task",
  "base_artifact_refs": ["..."],
  "output_namespace": "generation/G3",
  "constraints": {
    "read_other_candidates": false,
    "do_not_modify_final_destination": true
  },
  "expected_result_schema": "executor-result-v0.1"
}
```

## Browser-operated Agents

For web agents:

- Use a distinct page/session per independent Generator.
- Give each page its own output namespace.
- Do not paste another Generator's result into the page before the barrier.
- Revisit the page to collect completion status or artifact reference.
- Treat UI state as transient; persist durable results to Shared Workspace.
- Use only interactions allowed by the service and user authorization; do not bypass usage or access controls.

## Return-only Executors

If an Executor cannot write the Shared Workspace, its result is returned to Orchestrator and normalized into the correct namespace. Mark `direct_workspace_write: false` in metadata.
