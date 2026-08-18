# Shared Workspace Contract

The Shared Workspace is the external source of run state. The user should create and authorize it before substantive orchestration.

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

Versioning can be a Git commit SHA, Drive revision ID, timestamped immutable file, or another stable backend identifier.

## Logical namespace

```text
.archon/
  runs/
    <run_id>/
      manifest.json
      task.md
      executors.json
      generation/
        G1/
        G2/
        G3/
        G4/
      verification/
      critique/
      ranking/
      fusion/
      final/
```

A backend may map these logical namespaces differently. For example, GitHub Generator namespaces may be branches; Google Drive Generator namespaces may be subfolders.

## Controlled multi-writer rule

- Orchestrator owns control state (`manifest`, ranking, run policy) or serializes writes to it.
- Each Generator owns exactly one isolated output namespace.
- Fuser owns a separate fusion namespace.
- No two active Executors may write the same isolated namespace concurrently.

## Artifact references

Prefer small stable references over duplicated large outputs.

Example:

```json
{
  "backend": "github",
  "ref": "branch:archon/run-017/g3@91fa3",
  "kind": "candidate",
  "summary": "Alternative implementation using event queue"
}
```

A return-only Executor that cannot write Workspace may return content to Orchestrator, which normalizes and writes the artifact.

## Privacy and scope

- Use a dedicated repo/folder when possible.
- Do not recursively inspect unrelated user files.
- Record the authorized root in manifest.
- Treat credentials and secrets as out of scope unless explicitly required and safely handled.
