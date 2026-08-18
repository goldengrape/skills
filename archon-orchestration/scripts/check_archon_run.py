#!/usr/bin/env python3
"""Lightweight health check for a local/mounted Archon run."""
from __future__ import annotations
import argparse, json
from dataclasses import dataclass
from pathlib import Path

VALID_STAGES = {"INIT","GENERATING","VERIFYING_GENERATION","CRITIQUING","RANKING","FUSING","FINAL_VERIFY","FINALIZING","DONE","PARTIAL","FAILED"}
TERMINAL_EXEC = {"completed","failed","cancelled","contaminated"}

@dataclass
class Finding:
    level: str
    path: str
    message: str


def load_json(path: Path, findings: list[Finding]):
    try: return json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:
        findings.append(Finding("error", str(path), f"invalid JSON: {e}")); return None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--run-id", required=True)
    args = ap.parse_args()
    root = Path(args.root).resolve()
    run = root / ".archon" / "runs" / args.run_id
    findings: list[Finding] = []
    manifest_path = run / "manifest.json"
    if not manifest_path.exists():
        print("ERROR manifest.json missing"); return 2
    m = load_json(manifest_path, findings) or {}
    if m.get("run_id") != args.run_id: findings.append(Finding("error", "manifest.json", "run_id mismatch"))
    stage = m.get("stage")
    if stage not in VALID_STAGES: findings.append(Finding("error", "manifest.json", f"invalid stage: {stage}"))
    if not (run / "task.md").exists(): findings.append(Finding("error", "task.md", "frozen task missing"))
    else:
        task = (run / "task.md").read_text(encoding="utf-8", errors="ignore")
        if "<TODO>" in task and stage not in {"INIT","FAILED"}: findings.append(Finding("error", "task.md", "task still contains TODO after INIT"))

    policy = m.get("policy", {})
    n = int(policy.get("generator_count", 0) or 0)
    if n < 1: findings.append(Finding("error", "manifest.json", "generator_count must be >= 1"))
    for i in range(1, n + 1):
        d = run / "generation" / f"G{i}"
        if not d.exists(): findings.append(Finding("error", str(d.relative_to(root)), "generator namespace missing"))

    gen_exec = m.get("executions", {}).get("generators", {})
    barrier_reached = stage in {"VERIFYING_GENERATION","CRITIQUING","RANKING","FUSING","FINAL_VERIFY","FINALIZING","DONE","PARTIAL"}
    if barrier_reached:
        if len(gen_exec) < n: findings.append(Finding("error", "manifest.json", "generation barrier passed before all scheduled generators were recorded"))
        usable = 0
        for gid in [f"G{i}" for i in range(1, n + 1)]:
            info = gen_exec.get(gid)
            if not isinstance(info, dict): continue
            status = info.get("status")
            if status not in TERMINAL_EXEC: findings.append(Finding("error", "manifest.json", f"{gid} not terminal at/after barrier: {status}"))
            if status == "completed":
                usable += 1
                if not info.get("artifact_ref"): findings.append(Finding("error", "manifest.json", f"{gid} completed without artifact_ref"))
        minimum = int(policy.get("minimum_usable_generators", min(3,n)) or 0)
        if usable < minimum: findings.append(Finding("warn", "manifest.json", f"usable generators {usable} below policy minimum {minimum}"))

    if stage in {"RANKING","FUSING","FINAL_VERIFY","FINALIZING","DONE","PARTIAL"}:
        critique = m.get("artifacts", {}).get("critique")
        if not critique: findings.append(Finding("error", "manifest.json", "critique artifact missing after CRITIQUING"))
    if stage in {"FUSING","FINAL_VERIFY","FINALIZING","DONE","PARTIAL"}:
        ranking = m.get("artifacts", {}).get("ranking")
        if not ranking: findings.append(Finding("error", "manifest.json", "ranking artifact missing after RANKING"))
    if stage in {"FINAL_VERIFY","FINALIZING","DONE","PARTIAL"} and stage != "FINALIZING":
        if stage in {"FINAL_VERIFY","DONE","PARTIAL"} and not m.get("artifacts", {}).get("fusion"):
            findings.append(Finding("warn", "manifest.json", "fusion artifact missing; ensure winner-adoption/skip is explicitly recorded"))
    if stage in {"DONE","PARTIAL"} and not m.get("artifacts", {}).get("final"):
        findings.append(Finding("error", "manifest.json", "final artifact missing for terminal successful/partial outcome"))

    for f in findings:
        print(f"{f.level.upper():5} {f.path}: {f.message}")
    errors = sum(f.level == "error" for f in findings)
    warns = sum(f.level == "warn" for f in findings)
    print(f"Summary: {errors} error(s), {warns} warning(s)")
    return 2 if errors else 0

if __name__ == "__main__":
    raise SystemExit(main())
