---
type: Concept Mastery State
title: Concept Mastery State
description: Evidence-based concept state.
tags: [state, learning-control, v3]
timestamp: 2026-07-07T10:05:00-07:00
---

# Concept Mastery State

```yaml
data_status: package_dry_run_not_real_learner
concepts:
  - id: neuroaxis-map
    target_level: L6
    current_evidence_level: L3_partial_dry_run
    assistance_modes_seen: [blind]
    misuse_checks_passed: []
    transfer_checks_passed: []
    note: dry-run only; reset before real learner use
  - id: umn-lmn
    target_level: L6
    current_evidence_level: none
    assistance_modes_seen: []
    misuse_checks_passed: []
    transfer_checks_passed: []
  - id: brainstem-crossed
    target_level: L6
    current_evidence_level: misconception_active_dry_run
    assistance_modes_seen: [blind]
    misuse_checks_passed: []
    transfer_checks_passed: []
    linked_retest: RETEST-MC-002
```

# Rule

No concept is treated as stable without blind or barehand evidence plus a misuse check.
