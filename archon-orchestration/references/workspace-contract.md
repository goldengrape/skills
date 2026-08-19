# Shared Workspace Contract

Load this file when initializing, resuming, repairing, or finalizing a run.

The Shared Workspace is the durable source of run state **and the primary transport for substantive run artifacts**. The user should create or approve it before substantive orchestration. Orchestrator conversation memory is not sufficient for a resumable run and should not become a substitute file-transfer channel.

## Control plane vs artifact plane

Keep these responsibilities separate:

```text
Orchestrator conversation / browser prompt:
  compact control instructions, IDs, refs, constraints, status receipts

Shared Workspace:
  frozen task, base inputs, candidate artifacts, diffs/files, critique, ranking,
  fusion output, verification evidence, manifest and final outcome
```

When an Executor can read/write the Shared Workspace directly, pass stable refs instead of copying artifact bodies into prompts or responses. Prefer a small receipt pointing to a durable artifact over a long returned artifact body.

Adapters may tighten this rule. In particular, the GitHub adapter defaults to `direct_required`: GitHub is the data plane, and return-only/chat-mediated artifact transport is disabled unless the user explicitly accepts a degraded path.

## Minimum logical operations

A backend should support, directly or through the Orchestrator:

```text
read_artifact(ref)
write_artifact(namespace, content_or_ref)
list_namespace(namespace)
create_namespace(namespace)
read_manifest(run_id)
write_manifest(run_id, manifest)
identify_version(artifact)
```

Version identity may be a commit SHA, Drive revision ID, immutable file ID, timestamped snapshot, content hash, or another stable backend identifier.

## Workspace I/O policy

Record the active policy in manifest or equivalent run metadata:

```yaml
workspace_io_mode: direct_required | direct_preferred | return_only_allowed
inline_artifact_transport: false
allow_return_only_fallback: false
```

Meaning:

- `direct_required`: selected Executors must read/write substantive artifacts in the workspace themselves. Capability mismatch is a dispatch failure unless the user explicitly changes policy.
- `direct_preferred`: use direct workspace I/O whenever supported; a permitted fallback may normalize returned artifacts.
- `return_only_allowed`: Executor output may travel through its return channel and be normalized by Orchestrator.
- `inline_artifact_transport: false`: do not duplicate durable workspace artifacts into chat/file-upload channels unless required by an explicitly allowed fallback.

Never silently change `direct_required` to return-only merely because a browser executor lacks workspace access.

## Logical namespace

Default logical layout:

```text
.archon/
  runs/
    <run_id>/
      manifest.json
      task.md
      executors.json
      generation/
        G1/
          dispatch.json (optional)
          raw-return.md (return-only executors, when explicitly allowed and safe)
          candidate.*
          result.json
        G2/
        G3/
        G4/
        G3R1/
      verification/
      critique/
        critique.json
      ranking/
        ranking.json
      fusion/
        result.json
        artifact.*
      final/
        outcome.json
```

A backend may map these logical namespaces differently (GitHub Generator namespaces as branches; Drive Generator namespaces as subfolders). The mapping must be recorded clearly enough that another Orchestrator can resume the run.

## Manifest authority

`manifest.json` is the control-plane source of truth for:

* run ID
* stage and outcome
* workspace root and backend
* workspace I/O and browser-execution policy
* policy and budget counters
* scheduled Generators and execution records
* artifact references
* orchestration decisions
* history

A manifest entry that claims completion without an observable result or artifact is invalid. If manifest and artifacts disagree materially, STOP and reconcile before dispatching new work.

## Controlled multi-writer rule

* Orchestrator owns control state: manifest, policy, stage transitions, ranking, final outcome.
* Each active Generator owns exactly one isolated generation namespace.
* Fuser owns a separate fusion namespace.
* Verifier writes only verification artifacts or records.
* No two active Executors may write the same isolated namespace concurrently.

## Required control files

| File | Purpose |
| --- | --- |
| `manifest.json` | Run state, policy, execution records, artifact refs, counters, decisions, history |
| `task.md` | Frozen task snapshot |
| `executors.json` | Optional capability inventory |
| `generation/<ID>/dispatch.json` | Optional durable dispatch package or reference |
| `generation/<ID>/result.json` | Normalized terminal execution result |
| `generation/<ID>/raw-return.md` | Safe raw return from explicitly allowed return-only Executor, when applicable |
| `critique/critique.json` | Logical Critic output |
| `ranking/ranking.json` | Logical Ranker output |
| `fusion/result.json` | Fuser result metadata |
| `final/outcome.json` | Final outcome summary |

## Artifact references

Prefer small stable references over duplicated large outputs.

Example:

```json
{
  "backend": "github",
  "ref": "branch:archon/run-017/G3@91fa3",
  "kind": "candidate",
  "version": "91fa3",
  "summary": "Alternative implementation using event queue"
}
```

For direct-write Executors, the receipt should point to the workspace artifact and version; the Orchestrator verifies that ref rather than asking for a duplicate body.

For explicitly allowed return-only Executors, the Orchestrator may create the artifact from returned content and then assign the stable `artifact_ref`. Return-only content is not durable until the Orchestrator writes it into the Shared Workspace or stores a stable external reference.

## Return-only normalization

When an Executor cannot write directly to the Shared Workspace **and the active workspace policy allows fallback**, the Orchestrator writes the returned output into the assigned namespace and records `direct_workspace_write: false` with `return_only_normalized_by_orchestrator: true`. The normalized artifact becomes the candidate of record.

Record the transport downgrade in manifest/history. Do not treat return-only normalization as equivalent to direct-write capability during executor selection for a `direct_required` run.

## Reconciliation rule

When resuming:

1. Treat manifest as the index, not as unquestionable proof.
2. Validate manifest claims against workspace artifacts.
3. Import valid orphaned result files into manifest when safe.
4. Roll back or stop when manifest stage is ahead of artifacts.
5. Record every repair in manifest history.

See `references/failure-recovery.md` for the full deterministic reconciliation order.

## Privacy and scope

* Use a dedicated root when possible.
* Do not recursively inspect unrelated user files.
* Record the authorized root in manifest.
* Treat credentials and secrets as out of scope unless explicitly required and safely handled.
* Do not persist sensitive raw returns unless necessary and approved.
