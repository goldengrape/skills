---
type: Schema
title: External Image Source
description: Source and attribution schema for externally sourced teaching images.
tags: [schema, external-source, image, attribution]
timestamp: 2026-07-03T00:00:00-07:00
---
# External Image Source

Use an external source when a required teaching image is complex, standard, or better explained by an authoritative open source.

```yaml
source_type: external
source_name: Wikimedia Commons
source_url: https://...
license: CC BY-SA 4.0
attribution: "Author / Project, license, URL"
retrieved_date: 2026-07-03
local_copy_path: assets/diagrams/external/...
used_in:
  - plan/day-5.md
  - teacher/teacher-notebook.md
```

## Preferred Source Order

1. Official institutions, government agencies, or international organizations.
2. Open textbooks and university open courseware.
3. Wikipedia / Wikimedia Commons.
4. Credible open-source tutorials.

Do not use unlicensed or unclear images as course assets unless they are linked for reference only and not copied into the course bundle.
