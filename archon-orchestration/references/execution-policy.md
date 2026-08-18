# Execution Policy

## Standard mode

```yaml
generators: 4
parallel: true
top_k: 2
verifier: auto
combine_critic_ranker: true
max_extra_evaluators: 1
max_generator_replacements: 1
max_fusion_retries: 1
```

## Latency-aware policy

The expensive stages should normally be:

```text
max(Generator wall-clock) + Fuser wall-clock
```

Evaluation should usually be shorter. Do not add fixed long-running Critic ensembles unless the task justifies the time.

## Evaluation escalation triggers

Use one extra evaluator when one or more are true:

- ranking confidence is below the configured threshold
- top candidates are near-tied on important criteria
- verifier evidence conflicts with language-model judgment
- task is high-risk and failure cost is material
- Critic identifies a critical unresolved assumption

## Fuser policy

Standard mode performs fusion. A low-latency policy may intentionally adopt a clear winner when:

- ranking confidence is high
- verifier evidence strongly separates candidates when applicable
- lower candidates offer no unique useful insight
- user or configured policy prefers lower latency

Record the intentional skip in manifest; do not silently omit the logical decision.

## Executor preference

Default priority for high-value roles:

1. capable Agent Executor with direct Shared Workspace access
2. capable API-backed Agent Executor
3. return-only web/API execution that Orchestrator can normalize

This is a preference, not a hard vendor rule.
