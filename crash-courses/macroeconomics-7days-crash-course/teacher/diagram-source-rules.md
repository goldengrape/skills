---
type: Teacher Runtime
title: Diagram Source Rules
description: Rules for external diagram lookup and attribution.
tags: [teacher, diagram, source]
timestamp: 2026-07-03T05:24:06+00:00
---

# Diagram Source Rules

## Use External Sources When

- The diagram is complex or highly standardized.
- A generated image would be misleading or too hard to verify quickly.
- The learner asks for an authoritative reference.
- The concept benefits from an official or open textbook diagram.

## Source Order

1. Official institutions and international organizations.
2. Open textbooks or university open courseware.
3. Wikipedia / Wikimedia Commons.
4. Credible open-source tutorials.

## Required Record

```yaml
source_type: external
source_name:
source_url:
license:
attribution:
retrieved_date:
local_copy_or_link:
used_in:
```
