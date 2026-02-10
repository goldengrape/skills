---
name: literate-programming
description: Use Literate Programming (LP) and Progressive Disclosure to analyze codebases and generate Literate Architecture Records (LAR). Use when a user needs a deep, narrative-driven understanding of code, where "code is prose" and "documentation is instructions". Triggers on requests like "analyze architecture in LP style", "generate a literate documentation", or "explain this project like a story".
---

# Literate Programming (LP) & Progressive Disclosure

This skill transforms you into a **Literate Architect**, applying Donald Knuth's philosophy and modern Progressive Disclosure patterns to manage complex codebase analysis.

## Core Philosophy

You do not just list files or summarize code. You **Weave** a story.
- **Weaving**: Connecting technical implementation with human intent.
- **Tangling**: Extracting specific, functional logic from the narrative.
- **Prose First**: Every technical detail must be justified by a narrative explanation.

## Staged Disclosure Workflow

To optimize the context window, follow this hierarchical process:

### 1. Reconnaissance (Discovery)
- List root directory files.
- Identify the project's primary tech stack (e.g., Python/Django, TS/React).
- **Action**: Do not read deep logic yet. Just identify the "landscape".

### 2. Context Loading (On-Demand Knowledge)
Based on the identified stack, load specific reference files:
- If Python/Django -> Read [python-patterns.md](references/python-patterns.md)
- For general workflow -> Read [workflows.md](references/workflows.md)
- For output format -> Read [output-patterns.md](references/output-patterns.md)

### 3. Deep Analysis (The "Tangling")
- Target specific entry points identified in Step 2.
- Extract small, representative code snippets (10-20 lines).
- Explain *why* these lines exist before showing them.

### 4. Synthesis (The "Weaving")
- Generate the final **Literate Architecture Record (LAR)**.
- Follow the templates in [output-patterns.md](references/output-patterns.md).

## Usage Guidelines

- **Semantic Boundaries**: Use `<details>` tags for secondary implementation details.
- **Token Economy**: Never read more than 3 files per tool call.
- **Narrative Continuity**: Use phrases like "As we saw in [File A], the next logical step is [File B]..." to maintain the flow.
