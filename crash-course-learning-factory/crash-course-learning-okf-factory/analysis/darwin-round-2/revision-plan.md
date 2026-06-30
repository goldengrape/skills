---
type: Darwin Revision Plan
title: Round 2 Revision Plan
description: Minimal revision selected by Darwin-style evaluation.
tags: [darwin, revision-plan, round-2]
timestamp: 2026-06-30T00:00:00-07:00
---
# Round 2 Revision Plan

## Selected Shortfall

D10 MVP executability.

## Change

Add a small standard-library Python helper:

```text
tools/materialize_course_okf.py
```

It must:

1. accept JSON input or CLI flags;
2. normalize the core factory fields;
3. create `course-okf-{slug}-pass/`;
4. create required plan, state, session, record, quiz, and final-review files;
5. initialize `state/current-state.md` and `state/next-action.md`;
6. write `generation-output.json` using the course output contract;
7. report missing files instead of silently passing.

## Non-Changes

- No web app.
- No database.
- No automatic claim of real exam score prediction.
- No replacement of source-grounded course-content generation.

## Expected Impact

| Dimension | Expected effect |
|---|---|
| D3 Layout | Slight improvement because required files can be generated deterministically. |
| D4 State | Slight improvement because initial state files are materialized. |
| D9 Validation | Improvement because output JSON and tests verify file existence. |
| D10 Executability | Major improvement because skeleton generation no longer depends only on manual execution. |
