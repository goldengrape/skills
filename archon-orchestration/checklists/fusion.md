# Fusion Checklist

Use before final verification or finalization.

- [ ] Fuser has the frozen task.
- [ ] Fuser has full top K candidate artifacts.
- [ ] Fuser has Critic and Ranker outputs.
- [ ] Fuser has preserved unique insights from lower-ranked candidates.
- [ ] Fuser has relevant verification evidence and limitations.
- [ ] Fuser has terminal status notes for excluded candidates when relevant.
- [ ] Fuser writes to a new isolated namespace/artifact.
- [ ] Contradictory candidate assumptions are resolved, not concatenated.
- [ ] Useful preserved insights are either used or explicitly declined.
- [ ] If Fuser intentionally adopts one winner, the rationale is recorded (manifest `decisions.winner_adoption`).
- [ ] Fuser result has a stable `artifact_ref` or adopted candidate reference.
- [ ] Candidate artifacts are not overwritten.
- [ ] Fusion retry budget remains available before any repair retry.
- [ ] Fused result is treated as a new candidate for any final verification.
