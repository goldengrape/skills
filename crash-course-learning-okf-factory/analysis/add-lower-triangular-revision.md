---
type: ADD Revision Report
title: Lower Triangular ADD Revision
description: Records the matrix cleanup that makes the ADD explicitly lower triangular.
tags: [add, axiomatic-design, matrix, revision]
timestamp: 2026-06-30T00:00:00-07:00
---

# Lower Triangular ADD Revision

## Reason

The previous ADD matrix was directionally correct but not formally lower triangular because validation was marked as a dependency for FR1-FR10. That represented an acceptance check as if it were a design parameter needed by earlier functions.

## Changes Made

| Area | Change |
|---|---|
| Validation dependency | Removed DP11 marks from FR1-FR10. |
| Layout dependency | Removed FR2 -> DP6. Layout now depends on DP1 and DP2 only. |
| State dependency | Removed FR6 -> DP8. State update now depends on persisted state, not the reverse. |
| Matrix interpretation | Changed from "decoupled with execution order" to "decoupled / lower triangular". |
| Trace note | Added a trace note clarifying that validation is ADD-FR-011. |

## Revised Matrix Status

The revised matrix satisfies the lower-triangular condition under the chosen FR/DP ordering:

```text
FR1  -> DP1
FR2  -> DP1, DP2
FR3  -> DP1, DP3
FR4  -> DP3, DP4
FR5  -> DP1, DP4, DP5
FR6  -> DP2, DP4, DP6
FR7  -> DP5, DP6, DP7
FR8  -> DP6, DP8
FR9  -> DP4, DP5, DP6, DP8, DP9
FR10 -> DP4, DP6, DP10
FR11 -> DP1, DP2, DP3, DP4, DP5, DP6, DP7, DP8, DP9, DP10, DP11
```

There are no dependencies from an earlier FR to a later DP.

## Result

Design matrix type: **Decoupled / Lower Triangular**.
