# Agent Executor Contract

Load this file before dispatching, collecting, normalizing, or resuming Agent Executor work.

An Agent Executor is any backend the Orchestrator can delegate a bounded task to. Executors may be browser-operated agents, API-backed agents, local agents, deterministic programs, verifiers, or future compatible backends.

## Conceptual interface

```text
dispatch(task_package) -> execution_id
status(execution_id) -> pending | running | completed | failed | cancelled | contaminated
collect(execution_id) -> result metadata + artifact refs or returned content
cancel(execution_id) -> terminal status
```

The Orchestrator may implement this through browser control, APIs, local processes, files, or another authorized mechanism.

## Capability declaration

Recommended fields:

```yaml
executor_id: executor-1
kind: browser_agent | api_agent | local_agent | deterministic_program | other
capabilities:
  browser: true
  workspace_read: true
  workspace_write: false
  shell: false
  long_running: true
  verifier_local: false
  return_only: true
cost_class: high
latency_class: high
isolation_unit: session
```

Do not infer missing capabilities from provider branding. Probe, configure, or mark unknown.

## Task package

Each dispatch should contain only what the role needs:

```json
{
  "task_id": "run-017-generator-G3",
  "run_id": "run-017",
  "role": "generator",
  "candidate_id": "G3",
  "objective": "...",
  "task_snapshot_ref": "workspace://run-017/task.md",
  "base_artifact_refs": [],
  "output_namespace": "generation/G3",
  "constraints": {
    "read_other_current_run_candidates": false,
    "do_not_modify_final_destination": true
  },
  "approved_tools": [],
  "expected_result_schema": "executor-result-v0.2"
}
```

Do not include sibling candidate artifacts in Generator packages before the barrier. The Orchestrator should persist the dispatch package or a stable reference to it before or immediately after dispatch.

## Dispatch record

Record each dispatch in manifest or executor metadata with:

```json
{
  "execution_id": "",
  "role": "generator",
  "candidate_id": "G1",
  "executor_id": "",
  "status": "running",
  "output_namespace": "generation/G1",
  "direct_workspace_write": false,
  "started_at": "",
  "last_observed_at": "",
  "artifact_ref": null,
  "limitations": []
}
```

## Terminal statuses

Use these execution statuses:

* `completed`: Executor returned or wrote a normalizable result with a stable artifact reference.
* `failed`: Executor could not complete, timed out, returned unusable content, or normalization failed.
* `cancelled`: Orchestrator or user stopped the execution before usable completion.
* `contaminated`: Executor saw prohibited current-run candidate/evaluation/fusion content.

A timed-out execution is usually `failed` with `failure_reason: "timeout"` unless it can still be observed and recovered. Use `contaminated` only when independence or input isolation was materially violated; do not reuse it for ordinary low quality.

## Browser-operated Executors

For browser-operated Executors:

* Use a distinct page/session/context per independent Generator.
* Give each context only the frozen task, base inputs, role instructions, approved tools, and its own namespace.
* Do not paste another Generator's output or evaluation content before the barrier.
* Record the page/session handle or other reattachment hint in manifest when allowed.
* Treat UI state as transient. Persist durable results to the Shared Workspace.
* Use only interactions allowed by user authorization and the service; do not bypass access controls.

A single browser page may be reused for later non-independent roles only after the role no longer claims Generator independence.

## Return-only Executors

A return-only Executor cannot write directly to the Shared Workspace. Its output is still valid if the Orchestrator can observe it and normalize it.

Required Orchestrator normalization steps:

1. Collect the returned text or structured data.
2. Store safe raw return content at `generation/<ID>/raw-return.md` or equivalent.
3. Create or reference the durable candidate artifact in the assigned namespace.
4. Write `generation/<ID>/result.json` using `templates/executor-result.json`.
5. Set `direct_workspace_write: false`.
6. Set `return_only_normalized_by_orchestrator: true`.
7. Record `raw_return_ref`, `artifact_ref`, and `normalization_notes`.

If the return contains a complete final artifact but no artifact reference, the Orchestrator writes that artifact into the namespace and uses the new stable reference. If the return is ambiguous, incomplete, unsafe to persist, or cannot be mapped to the schema, attempt one schema repair if policy permits; if repair fails, mark `failed`.

Do not claim completion until the normalized artifact or stable external reference is observable.

## Result contract

Every terminal execution should have a normalized result object per `templates/executor-result.json` (schema 0.2). Required core fields:

```json
{
  "schema_version": "0.2",
  "execution_id": "",
  "run_id": "",
  "role": "generator",
  "candidate_id": "G1",
  "status": "completed",
  "usable": true,
  "artifact_ref": "",
  "output_namespace": "generation/G1",
  "direct_workspace_write": false,
  "return_only_normalized_by_orchestrator": true,
  "started_at": "",
  "completed_at": ""
}
```

Rules:

* Do not mark `completed` without a usable `artifact_ref`.
* `usable` is true only when terminal `completed`, uncontaminated, and artifact-backed; a contaminated Generator may still contain useful ideas but must not be counted as an independent candidate.
* Persist failed, cancelled, timed-out, malformed, and contaminated results with reasons.
* If output is malformed but recoverable, repair the schema once without changing substantive content.
* If output is missing or inaccessible, mark failure with reason instead of fabricating a result.
