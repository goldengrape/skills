---
type: Darwin Evaluation
title: Round 2 Post-Revision Evaluation
description: Evaluation after adding the minimal materializer and tests.
tags: [darwin, evaluation, post-revision, round-2]
timestamp: 2026-06-30T00:00:00-07:00
---
# Round 2 Post-Revision Evaluation

Evaluation mode: **dry_run + local_tests**.

Local tests:

```text
python -m pytest -q
3 passed
```

| Dimension | Weight | Before | After | Reason |
|---|---:|---:|---:|---|
| D1 Meta-factory identity | 10 | 9 | 9 | No change. |
| D2 Input/output contract | 10 | 9 | 9 | Output contract now has a concrete JSON producer. |
| D3 Generated layout completeness | 12 | 9 | 10 | Materializer creates the required file tree for variable day counts. |
| D4 State persistence | 14 | 9 | 10 | Initial state files are created deterministically. |
| D5 Resume behavior | 10 | 9 | 9 | Resume playbook unchanged. |
| D6 Adaptive planning | 10 | 8 | 8 | Adaptation playbook unchanged. |
| D7 Daily package fit | 8 | 9 | 9 | Daily plan generated with the 60-minute structure. |
| D8 Source grounding | 8 | 8 | 8 | Source gaps are initialized; course quality still depends on materials. |
| D9 Validation and tests | 10 | 8 | 9 | Tests and `generation-output.json` added. |
| D10 MVP executability | 8 | 3 | 8 | Minimal executable skeleton generator added without exceeding MVP. |

Before: **82.4 / 100** under the round-2 rubric.  
After: **91.8 / 100** under the round-2 rubric.

Hard gates: passed.

## Kept Revision

The materializer was kept because it improves executable reliability and does not introduce a heavy runtime dependency.

## Remaining Risks

| Risk | Status | Next check |
|---|---|---|
| No real course trial yet | Still open | Generate and resume three course instances. |
| Teaching content still depends on materials | Accepted | Keep source gaps visible and require reconnaissance. |
| CLI only creates skeleton | Intended MVP boundary | Do not expand into a full app unless user asks. |
