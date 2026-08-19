# Finalize Checklist

Use before reporting `DONE`, `PARTIAL`, or `FAILED`.

- [ ] Final artifact reference is stable and accessible.
- [ ] Candidate terminal statuses are recorded, including failed/cancelled/contaminated.
- [ ] Return-only normalization status is recorded for affected candidates.
- [ ] Ranking/top K decision is recorded.
- [ ] Fusion or intentional winner adoption is recorded.
- [ ] Evaluation confidence and any extra evaluator are recorded.
- [ ] Verification claims match tools/commands that actually ran.
- [ ] Verifier limitations or unavailability are stated.
- [ ] Generator replacements, schema repairs, evaluator escalations, and fusion retries stayed within policy or have approval.
- [ ] Known limitations are written down.
- [ ] Any merge/delete/overwrite/publish action has required approval.
- [ ] `final/outcome.json` exists for DONE/PARTIAL with `final_artifact_ref`.
- [ ] Manifest outcome is DONE / PARTIAL / FAILED and matches artifacts.
- [ ] Manifest history includes reconciliation actions, if any.
- [ ] Local `check_archon_run.py`, when applicable, reports no errors.
- [ ] User-facing response can point to the final artifact without duplicating the whole run log.
