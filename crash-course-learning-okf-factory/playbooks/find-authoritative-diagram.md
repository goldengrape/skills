---
type: Playbook
title: Find Authoritative Diagram
description: Locate and record external open teaching images when a generated diagram would be insufficient.
tags: [playbook, visual, diagram, external-source]
timestamp: 2026-07-03T00:00:00-07:00
---
# Find Authoritative Diagram

Use this playbook when a required image is complex, standard, detailed, or better handled by a trusted existing source.

## Source Priority

1. Official or institutional sources.
2. Open textbooks or university open courseware.
3. Wikipedia / Wikimedia Commons.
4. Credible open-source tutorials.

## Required Source Record

Every external image must record:

```yaml
source_url:
source_name:
license:
attribution:
retrieved_date:
local_copy_or_link:
used_in:
```

## Guardrails

- Do not copy images with unclear rights into the generated bundle.
- Prefer generated diagrams for simple teaching curves so labels can match the lesson.
- Use external diagrams when the image would otherwise be misleading or too complex to generate quickly.
