---
type: Validation Playbook
title: Validate Cycle Pack
description: DP-007 read-only validation gate for inputs, adaptive packs, Live runtime, records, and rollover output.
tags: [validation, quality, gate, adaptive-topics, current-events]
timestamp: 2026-07-09T21:30:00-07:00
---

# DP-007 — Validation Gate

## Rule

Validation is read-only. It reports defects and does not silently rewrite artifacts.

## Input Gate

Fail when:

- cycle duration is unsupported and not approved;
- the primary task is not spoken-English training;
- a blocking conflict is hidden;
- current-event use conflicts with explicit topic exclusions or sensitive-topic settings.

## Blueprint Gate

Fail when:

- there are more than three primary language targets;
- days lack meaningful communicative progression;
- a target has no learner-intent or evidence basis;
- selected activities cannot fit the time budget;
- topic policy is absent;
- an adaptive/current-event slot has no fixed language objective, topic intent, topic-fit check, selection rule, load-reduction fallback, or concrete evergreen fallback;
- a future day depends on a specific unverified news item.

## Course-Pack Gate

Fail when:

- a required file is missing;
- day-file count differs from `cycle_days`;
- a day lacks a language objective, topic mode, usable topic/fallback, speaking task, repair/transfer task, evidence target, or closeout;
- the default day exceeds 15 minutes;
- generic placeholders remain in mission or day plans;
- learner state cannot represent confirmed/possible/low-engagement/avoid topic status;
- current-event settings omit verification budget, context limit, or fallback rules;
- runtime rules are duplicated inconsistently;
- the pack requires Python, hooks, a VM, or hidden database.

## Live-Runtime Gate

Fail when:

- the coach is instructed to dominate speaking time;
- corrections are long, repeated, or lecture-like;
- naturalness feedback is prohibited without reason;
- topic selection becomes a long interview;
- topic choice ignores recent-topic balance or always defaults to the easiest confirmed interest;
- low engagement can be interpreted as dislike without separating affinity from language, knowledge, prompt, fatigue, or privacy load;
- current-event background is expected to dominate the session;
- unverified information may be presented as current fact;
- topic switching is allowed to discard the language objective;
- closeout has no protected time;
- pronunciation certainty is unsupported.

## Session-Record Gate

Fail when:

- completed task is absent;
- actual topic or selection basis is absent;
- high-value correction evidence is absent despite recorded corrections;
- pronunciation notes lack confidence labels;
- a used current event lacks event date, verification date, source name, and confidence;
- interest status is promoted beyond available topic-affinity evidence;
- a non-affinity confound is used to promote or downgrade interest;
- fatigue is treated as topic dislike without separate evidence;
- state patch is missing;
- next action is missing or more than one is active;
- recurring pattern or stable phrase lacks threshold evidence;
- evidence classes are materially blurred;
- automatic persistence is claimed.

## Rollover Gate

Fail when:

- next-cycle proposal does not cite prior evidence;
- continue/change/retire/test-next decisions are missing;
- stable items are retained without reason;
- topic interests are confirmed, downgraded, avoided, or retired without topic-affinity evidence;
- the next cycle repeats one interest excessively without learner request or a changed communicative purpose;
- current-event policy changes without evidence or learner confirmation when required;
- proposed cycle exceeds three primary language targets.

## Output Format

```markdown
# Validation Report

- status: PASS | FAIL
- scope: input | blueprint | course_pack | live_runtime | session_record | rollover

## Defects
- ID:
  severity: blocking | major | minor
  artifact:
  rule:
  evidence:
  required_fix:

## Warnings
-
```

A pack passes only when no blocking or major defects remain.
