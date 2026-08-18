# Architecture Reference

## Layer model

```text
Archon logical workflow
        ↓
Orchestrator
        ↓
Agent Executors
        ↕
Shared Workspace
```

Optional capabilities such as Verifier, Search, Browser, Solver, shell scripts, or platform tools are attached at execution time.

## Role / Executor separation

Roles define *why* a step exists:

- Generator: search solution space.
- Critic: expose strengths, weaknesses, assumptions, and reusable insights.
- Ranker: choose/trim candidates using task fit and evidence.
- Fuser: synthesize a new result from strong parts.

Executors define *how* a role is performed:

- browser-operated web agent
- API-backed agent
- local agent
- local deterministic program

Do not encode provider names into the logical workflow.

## Why 4 Generators by default

The main ROI of multiple Generators is search-space expansion. Independent candidates can discover different architectures, interpretations, proof paths, or rhetorical structures. Four parallel Generators normally cost roughly one Generator wall-clock stage when the Orchestrator can run them concurrently.

## Why not 3 expensive Critics by default

Additional Critic votes mostly reduce evaluation error rather than create new solution paths. When Critic executions are long-running agents, a fixed 3C stage can add substantial wall-clock for smaller marginal gain. The default policy therefore uses one evaluation pass and escalates by one additional evaluator only when confidence/evidence requires it.
