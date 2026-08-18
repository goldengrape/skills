# References

## Primary design inputs

1. **Archon: An Architecture Search Framework for Inference-Time Techniques** — arXiv:2409.15254. The Skill adopts the general inference-time composition idea around generation, critique, ranking/filtering, fusion, and optional verification.
2. **goldengrape/vibe-coding-skill** — used as a Skill-engineering reference for explicit guardrails, CHECKPOINT/STOP conditions, mode-oriented behavior, templates, machine-readable state, progressive disclosure, lightweight helper scripts, package manifest, and test prompts.

## Design note

This package does not copy the Vibe Coding Skill's URD/ADD/MDD/TDD/RMD methodology. It borrows its *Skill packaging and operational discipline* while implementing an independent Archon orchestration workflow.
