# Failure and Recovery

## Generator failure

- Mark terminal status and reason.
- Continue with 3/4 if policy allows and coverage is still adequate.
- With fewer than 3 usable candidates, replace failed Generator once by default.
- Never treat a contaminated candidate as independent.

## Executor timeout / long-running page

- Check actual execution status before declaring failure.
- Do not duplicate a still-running expensive task unless policy permits.
- Persist any known execution ID/page reference in manifest.

## Evaluation failure

- If Critic/Ranker output is malformed, retry once with schema repair or use another fast evaluator.
- If ranking confidence is low, use one extra evaluator by default.

## Fuser failure

- Retry once if failure is execution/infrastructure related.
- If Fuser artifact fails verification, perform one evidence-guided repair/fusion if budget remains.
- If fusion remains worse than a verified top candidate, finalization may adopt the earlier candidate and record why.

## Orchestrator restart

1. Read manifest.
2. Inspect workspace namespaces and terminal result files.
3. Reconcile stage with artifacts.
4. Reattach to known running executions when possible.
5. Resume at the first incomplete logical stage.

Do not repeat completed generation just because conversational memory is gone.
