# Failure and Recovery

Load this file when a stage is non-ideal: failure, cancellation, timeout, contamination, malformed output, normalization failure, inaccessible artifact, verification error, or Orchestrator restart.

## Principles

- Persist what happened before repairing it.
- Prefer reconciliation over rerunning expensive completed work.
- Never hide failed, cancelled, contaminated, schema-invalid, or normalization-failed executions.
- Do not advance a stage while required artifacts for that stage are missing.
- Do not exceed retry/replacement/schema-repair/escalation budgets without a CHECKPOINT.

## Generator failure

When a Generator fails, is cancelled, or times out:

1. Record terminal status and reason (timeout is `failed` with `failure_reason: "timeout"` unless still observable).
2. Persist any safe raw return or diagnostic reference.
3. Mark whether the candidate is usable.
4. Continue with 3/4 usable candidates if policy allows and coverage remains adequate.
5. Replace once by default when usable candidates fall below policy minimum or coverage is materially missing.

Do not rerun all Generators because one failed.

## Generator contamination

Contamination means a Generator saw or may have used another current-run candidate, critique, ranking, or fusion artifact before the generation barrier.

Required handling:

1. Mark candidate status `contaminated`.
2. Preserve its namespace for audit.
3. Exclude it from the independent usable candidate set.
4. Replace it once if policy and budget allow, using a distinct ID such as `G3R1` with `replaces: "G3"`.
5. Record the contamination source when known.
6. After the barrier, Critic may extract useful ideas from it only if clearly labeled non-independent.

Never treat a contaminated candidate as independent.

## Return-only normalization failure

If a return-only Executor gives malformed or incomplete output:

1. Save safe raw return content if allowed.
2. Attempt one schema repair if policy permits.
3. If repair creates a stable candidate artifact and result object, mark completed with `return_only_normalized_by_orchestrator: true`.
4. If repair fails, mark `failed` with `failure_reason: "normalization_failed"`.

Do not evaluate transient text that has not been normalized into the Shared Workspace.

## Nonterminal or stale execution

At a barrier, if an execution is still `pending` or `running`:

1. Recheck actual status through the available handle.
2. Reattach if possible.
3. Cancel only if policy/user intent supports cancellation.
4. If no handle exists and no result artifact exists, stop for reconciliation or mark `failed` with reason if policy permits.
5. Do not launch a duplicate expensive execution unless replacement policy permits it.

## Evaluation failure

If Critic/Ranker output is malformed:

1. Attempt one schema repair if policy permits.
2. If repair fails, rerun with another fast evaluator if budget permits.
3. If ranking confidence is low or evidence conflicts remain, use one extra evaluator by default.
4. Persist both the original malformed output reference and the repaired/replacement output reference when practical.

Do not fabricate rankings from partial evaluator text.

## Verification failure

Distinguish:

- candidate `fail`
- verifier/infrastructure `error`
- verifier `unavailable`

A verifier error or unavailability is not a candidate failure. Record scope and limitations.

## Fuser failure

- Retry once if failure is execution/infrastructure related and budget remains.
- If the fused artifact fails verification, perform one evidence-guided repair/fusion if budget remains.
- If fusion remains worse than a verified top candidate, finalization may adopt the earlier candidate and record why.
- Do not overwrite candidate artifacts while repairing fusion.

## Orchestrator restart (deterministic reconciliation order)

Recovery starts from the Shared Workspace, in this order:

1. Read `manifest.json`.
2. Read `task.md`.
3. List all run namespaces.
4. Inspect `generation/<ID>/result.json` files, raw returns, and artifact refs.
5. Inspect `verification/`, `critique/`, `ranking/`, `fusion/`, and `final/`.
6. Reattach to known running executions when possible.
7. Compare manifest stage with artifacts actually present.
8. If manifest is ahead of artifacts, move back to the last validated stage or stop for repair.
9. If artifacts are ahead of manifest, validate them before advancing the manifest.
10. Resume at the first incomplete logical stage.

Do not repeat completed generation, critique, ranking, or fusion solely because conversational memory is gone.

## Manifest/artifact disagreement

Examples and repairs:

| Disagreement | Repair |
| --- | --- |
| Manifest says `CRITIQUING`, but a Generator is nonterminal | Return to `GENERATING` or mark/replace execution before barrier |
| Manifest says Generator completed, but no `artifact_ref` exists | Re-normalize the result or mark failed |
| Result file exists but manifest lacks execution record | Validate the result, then import it into manifest history |
| Ranking exists but critique missing | Stop; rebuild critique or mark ranking invalid |
| Final outcome exists but manifest stage is earlier | Validate outcome and either advance manifest or stop for user approval |

Record reconciliation actions in manifest history.

## Partial finalization

Use `PARTIAL` when the run produced a useful artifact but did not satisfy all operational requirements, such as degraded candidate quorum, unavailable verifier, or unresolved approval.

Use `FAILED` when no useful final artifact can be supported.

Use `DONE` only when required gates passed or approved limitations are recorded.
