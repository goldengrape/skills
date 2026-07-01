---
type: Template
title: Resources
description: Template for resources.md in a generated Course Learning OKF.
tags: [template, resources, provenance]
timestamp: 2026-06-30T00:00:00-07:00
---
# Resources Template

````markdown
---
type: Resource Registry
title: {Course Name} Resources
description: Sources, confidence, and gaps used to generate this course OKF.
tags: [resources, provenance]
timestamp: {timestamp}
---

# Resources

```yaml
resources:
  - id: resource-001
    type:
    title:
    path_or_url:
    priority: primary
    confidence: unknown
    used_for: []
    notes:
source_gaps:
  - missing_item:
    effect:
    fallback:
```

# Rule

User-provided course materials outrank generic public or model-memory fallback knowledge.
````
