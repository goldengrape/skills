# GitHub Shared Workspace Adapter

Use GitHub when code versioning, branches, commits, diffs, PRs, or repository-native artifacts matter.

## Recommended mapping

Control state can live on a dedicated orchestration branch or in a serialized control namespace managed by Orchestrator.

```text
base ref: <frozen task base SHA when relevant>

Generator branches:
  archon/<run_id>/G1
  archon/<run_id>/G2
  archon/<run_id>/G3
  archon/<run_id>/G4

Fuser branch:
  archon/<run_id>/F
```

The control namespace stores small files such as:

```text
.archon/runs/<run_id>/manifest.json
.archon/runs/<run_id>/task.md
.archon/runs/<run_id>/critique/critique.json
.archon/runs/<run_id>/ranking/ranking.json
.archon/runs/<run_id>/final/outcome.json
```

Candidate code should remain in candidate branches; store branch/commit refs in result metadata instead of copying whole diffs into control files.

## Isolation

- All Generator branches start from the same frozen base ref unless the task explicitly needs otherwise.
- A Generator must not inspect sibling `archon/<run_id>/G*` branches before barrier.
- Fuser may inspect candidates only after barrier/evaluation.

## Final integration

Do not merge candidate branches directly into the protected/default branch during generation. Final merge/PR follows user/repo approval policy.
