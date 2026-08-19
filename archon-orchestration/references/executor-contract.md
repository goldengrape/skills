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
  workspace_write: true
  shell: false
  long_running: true
  verifier_local: false
  return_only: false
cost_class: high
latency_class: high
isolation_unit: browser_page_and_conversation
workspace_transport: direct
```

Do not infer missing capabilities from provider branding. Probe, configure, or mark unknown. For a `direct_required` workspace, an Executor without both required workspace read and write capabilities is incompatible unless the user explicitly permits degraded return-only transport.

## Task package

Each dispatch should contain only what the role needs. Prefer references to durable workspace inputs over copied artifact contents.

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
  "input_delivery": "workspace_refs_only",
  "output_delivery": "workspace_direct",
  "constraints": {
    "read_other_current_run_candidates": false,
    "do_not_modify_final_destination": true,
    "inline_artifact_transport": false,
    "fresh_browser_page": true,
    "fresh_browser_conversation": true
  },
  "approved_tools": [],
  "expected_result_schema": "executor-result-v0.2"
}
```

Do not include sibling candidate artifacts in Generator packages before the barrier. Do not paste or upload substantive workspace artifacts merely because the browser transport makes that convenient. The Orchestrator should persist the dispatch package or a stable reference to it before or immediately after dispatch.

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
  "direct_workspace_write": true,
  "browser_page_ref": null,
  "conversation_ref": null,
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
* `contaminated`: Executor saw prohibited current-run candidate/evaluation/fusion content or reused a browser conversation whose prior context could contain such content.

A timed-out execution is usually `failed` with `failure_reason: "timeout"` unless it can still be observed and recovered. Use `contaminated` only when independence or input isolation was materially violated; do not reuse it for ordinary low quality.

## Browser-operated Executors

For every browser-operated independent Generator, both page isolation and conversation isolation are mandatory.

Required behavior:

1. Start one distinct browser execution/invocation per Generator.
2. Create a fresh browser page/tab/target for that Generator.
3. From the configured `browser_base_url`, create a fresh conversation for that Generator.
4. A user-provided ChatGPT project/workspace URL may be used as the base URL so shared project instructions/sources are available, but it is only a landing scope. Do not reuse an existing project conversation.
5. Never reuse another Generator's page, conversation, follow-up chain, saved session, or reattached thread as a new independent Generator.
6. Give the new conversation only the frozen task ref, allowed shared base refs, role instructions, approved tools, and its own output namespace.
7. Record the page/target and conversation/session reference when the executor exposes them.
8. Treat browser UI state as transient. The durable result must exist in the Shared Workspace before completion is accepted.

Sharing a browser process or signed-in profile is acceptable when the underlying browser controller creates a distinct page and distinct conversation per Generator and no cross-conversation content is injected. A fresh tab alone is insufficient if it reopens or continues an existing conversation.

A single browser page may be reused for later non-independent roles only after that role no longer claims Generator independence.

### Oracle / ChatGPT browser mapping

When `steipete/oracle` is the browser controller, map the generic contract as follows:

- Launch one Oracle browser invocation per independent Generator.
- `--chatgpt-url <URL>` may point to `https://chatgpt.com/`, Temporary Chat, or a user-provided ChatGPT project/workspace URL. Treat it as `browser_base_url` only.
- In attach-running mode, Oracle opening a fresh Oracle-owned tab satisfies the page requirement; each Generator still must start a fresh conversation from the base URL.
- Do not use `--browser-follow-up`, `--followup`, `oracle session`, or an existing conversation URL to manufacture another independent Generator.
- Do not pass repository files with `--file` or browser attachments when the active workspace policy says the Executor should read those artifacts from GitHub directly. Send compact refs/URLs and instructions instead.
- A completed Oracle response should normally be a compact receipt pointing to the durable workspace artifact, not the full artifact body, when `workspace_io_mode` is `direct_required`.

If the browser Executor cannot access the required GitHub refs/tools from the new conversation, fail capability negotiation before dispatch rather than silently turning the Orchestrator prompt into a file-transfer mechanism.

## Direct workspace Executors

When `output_delivery` is `workspace_direct`:

1. Executor reads task/base artifacts from stable workspace refs.
2. Executor writes only to its assigned namespace/branch.
3. Executor versions/commits the result when supported by the backend.
4. Executor returns a compact receipt with `artifact_ref`, version identity, summary, evidence/tests, and limitations.
5. Orchestrator independently reads or verifies the referenced artifact.
6. Only then may Orchestrator mark the execution `completed` and write normalized result metadata.

Do not require a duplicate inline artifact body in the receipt.

## Return-only Executors

A return-only Executor cannot write directly to the Shared Workspace. This is a compatibility path, not the preferred transport when the selected adapter requires direct workspace I/O.

Before using it, confirm that workspace policy allows `allow_return_only_fallback: true`. For GitHub `direct_required` runs this must be an explicit user-approved downgrade, not an automatic fallback.

Required Orchestrator normalization steps when fallback is allowed:

1. Collect the returned text or structured data.
2. Store safe raw return content at `generation/<ID>/raw-return.md` or equivalent.
3. Create or reference the durable candidate artifact in the assigned namespace.
4. Write `generation/<ID>/result.json` using `templates/executor-result.json`.
5. Set `direct_workspace_write: false`.
6. Set `return_only_normalized_by_orchestrator: true`.
7. Record `raw_return_ref`, `artifact_ref`, `normalization_notes`, and that transport was degraded.

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
  "direct_workspace_write": true,
  "return_only_normalized_by_orchestrator": false,
  "started_at": "",
  "completed_at": ""
}
```

Rules:

* Do not mark `completed` without a usable `artifact_ref`.
* For a browser Generator, do not count it as independent unless fresh page and fresh conversation isolation were satisfied or equivalently proven.
* `usable` is true only when terminal `completed`, uncontaminated, and artifact-backed; a contaminated Generator may still contain useful ideas but must not be counted as an independent candidate.
* Persist failed, cancelled, timed-out, malformed, and contaminated results with reasons.
* If output is malformed but recoverable, repair the schema once without changing substantive content.
* If output is missing or inaccessible, mark failure with reason instead of fabricating a result.
