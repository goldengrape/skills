# Shared Workspace Contract

Load this file when initializing, resuming, repairing, or finalizing a run.

The Shared Workspace is the durable source of run state. The user should create or approve it before substantive orchestration. Orchestrator conversation memory is not sufficient for a resumable run.

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
          raw-return.md (return-only executors, when safe)
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
| `generation/<ID>/raw-return.md` | Safe raw return from return-only Executor, when applicable |
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

For return-only Executors, the Orchestrator may create the artifact from returned content and then assign the stable `artifact_ref`. Return-only content is not durable until the Orchestrator writes it into the Shared Workspace or stores a stable external reference.

## Return-only normalization

When an Executor cannot write directly to the Shared Workspace, the Orchestrator writes the returned output into the assigned namespace and records `direct_workspace_write: false` with `return_only_normalized_by_orchestrator: true`. The normalized artifact becomes the candidate of record.

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
