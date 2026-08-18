# Verifier Policy

Verifier is an optional evidence module, not part of the universal Archon Core.

## Enable when

- the check is cheaper than another full Agent pass
- the result meaningfully distinguishes candidates
- the oracle is sufficiently clear
- the check can actually be run in the current environment

## Examples

### Programming

- compile/build
- unit/integration tests
- typecheck
- lint/static analysis
- targeted regression tests

### Mathematics

- numerical substitution
- CAS simplification
- constraint solver
- proof checker/formal verifier

### Research / analysis

- citation existence
- publication/date verification
- numeric/source consistency
- quote verification

These usually provide partial evidence, not a complete quality oracle.

## Evidence schema

```json
{
  "candidate_id": "G1",
  "verifier": "pytest",
  "status": "pass | fail | error | unavailable",
  "scope": "unit tests for package X",
  "command_or_tool": "uv run pytest tests/...",
  "summary": "184 passed",
  "artifact_ref": "...",
  "limitations": ["does not cover external API failure mode"]
}
```

## Rules

- Distinguish `fail` (candidate failed) from `error` (verifier/infrastructure failed).
- Never convert `unavailable` into a negative score.
- Never claim a command/tool ran if it did not.
- Feed evidence to Critic/Ranker rather than replacing them wholesale.
- Re-run relevant verification on fused output because fusion creates a new candidate.
