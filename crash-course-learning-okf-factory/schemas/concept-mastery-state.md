# Concept Mastery State Schema

```yaml
concept: string
priority: A | B | C | extension
target_level: L1-L9
current_evidence_level: L1-L9
assistance_mode: guided | semi_guided | blind | barehand
evidence:
  - date: string
    event: string
    result: passed | failed | partial
    score_type: assisted_score | semi_assisted_score | blind_score | barehand_score
    notes: string
next_required_check: string
```

Rule: do not claim mastery without evidence level and assistance mode.
