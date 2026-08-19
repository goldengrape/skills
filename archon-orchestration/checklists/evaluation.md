# Critic and Rank Checklist

Use after the generation barrier and before fusion.

- [ ] Evaluation starts only after the generation barrier is satisfied.
- [ ] Critic input includes every usable candidate artifact.
- [ ] Critic also receives terminal status summaries for unusable candidates.
- [ ] Critic covers every usable candidate.
- [ ] Each usable candidate has strengths and weaknesses, not just a score.
- [ ] Missing assumptions, risks, and operational concerns are explicit.
- [ ] Unique insights and reusable parts are extracted before filtering.
- [ ] Verification evidence is attached with scope and limitations when available.
- [ ] Ranker uses the frozen task rather than post-hoc requirements.
- [ ] Ranking has reasons, confidence, and unresolved disagreements.
- [ ] Rejected candidates have reasons.
- [ ] Top K full candidates are selected.
- [ ] Useful lower-ranked insights are preserved for Fuser.
- [ ] Provider/model identity does not drive ranking.
- [ ] Malformed evaluation output was repaired at most once or rerun within budget.
- [ ] Extra evaluator is used only if escalation criteria are met; at most one by default.
- [ ] Critic and Ranker outputs are persisted as separate logical artifacts even if physically combined.
