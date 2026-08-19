#!/usr/bin/env python3
"""Advance an Archon run manifest through allowed logical stages with lightweight precondition checks (schema 0.2 aware)."""
from __future__ import annotations
import argparse, json
from datetime import datetime, timezone
from pathlib import Path

TERMINAL = {"DONE", "PARTIAL", "FAILED"}
TERMINAL_EXEC = {"completed", "failed", "cancelled", "contaminated"}
ALLOWED = {
    "INIT": {"GENERATING", "FAILED"},
    "GENERATING": {"VERIFYING_GENERATION", "CRITIQUING", "FAILED"},
    "VERIFYING_GENERATION": {"CRITIQUING", "FAILED"},
    "CRITIQUING": {"RANKING", "FAILED"},
    "RANKING": {"FUSING", "FINALIZING", "FAILED"},
    "FUSING": {"FINAL_VERIFY", "FINALIZING", "FAILED"},
    "FINAL_VERIFY": {"FUSING", "FINALIZING", "FAILED"},
    "FINALIZING": {"DONE", "PARTIAL", "FAILED"},
    "DONE": set(), "PARTIAL": set(), "FAILED": set(),
}

def now(): return datetime.now(timezone.utc).isoformat()

def require(condition: bool, message: str, force: bool) -> None:
    if not condition and not force:
        raise SystemExit(message)

def scheduled_ids(data: dict) -> list[str]:
    """Return scheduled Generator IDs, preferring manifest.scheduled_generators (schema 0.2)."""
    sched = data.get("scheduled_generators")
    if isinstance(sched, list) and sched:
        return [str(s) for s in sched]
    n = int(data.get("policy", {}).get("generator_count", 0) or 0)
    return [f"G{i}" for i in range(1, n + 1)]

def check_preconditions(run: Path, data: dict, target: str, force: bool) -> None:
    policy = data.get("policy", {})
    artifacts = data.get("artifacts", {})
    schema = data.get("schema_version", "0.1")
    if target == "GENERATING":
        task = run / "task.md"
        require(task.exists(), "cannot start generation: task.md missing", force)
        if task.exists():
            text = task.read_text(encoding="utf-8", errors="ignore")
            require("<TODO>" not in text, "cannot start generation: task.md still contains <TODO>", force)
    if target in {"VERIFYING_GENERATION", "CRITIQUING"}:
        minimum = int(policy.get("minimum_usable_generators", 3) or 0)
        gens = data.get("executions", {}).get("generators", {})
        ids = scheduled_ids(data)
        require(len(gens) >= len(ids), "cannot pass generation barrier: not all scheduled generators are recorded", force)
        statuses = []
        for gid in ids:
            info = gens.get(gid, {})
            status = info.get("status")
            statuses.append(status)
            require(status in TERMINAL_EXEC, f"cannot pass generation barrier: {gid} non-terminal: {status}", force)
            if status == "completed":
                require(bool(info.get("artifact_ref")), f"cannot pass generation barrier: {gid} completed without artifact_ref", force)
                result_path = run / "generation" / gid / "result.json"
                if schema == "0.2":
                    require(result_path.exists(), f"cannot pass generation barrier: {gid} completed without normalized result.json", force)
                elif not result_path.exists():
                    print(f"WARN schema 0.1 run: {gid} completed without result.json (legacy run; not enforced)")
        usable = 0
        for gid in ids:
            status = gens.get(gid, {}).get("status")
            if status == "completed" and gens.get(gid, {}).get("usable", True) is not False:
                usable += 1
        require(usable >= minimum, f"cannot pass generation barrier: usable generators {usable} < minimum {minimum}", force)
    if target == "RANKING":
        require(bool(artifacts.get("critique")), "cannot rank: critique artifact missing", force)
    if target == "FUSING":
        require(bool(artifacts.get("ranking")), "cannot fuse: ranking artifact missing", force)
    if target in {"FINAL_VERIFY", "FINALIZING"} and data.get("stage") == "FUSING":
        decisions = data.get("decisions", {}) or {}
        fusion_ref = artifacts.get("fusion") or decisions.get("winner_adoption")
        require(bool(fusion_ref), "cannot leave fusion: fusion artifact or decisions.winner_adoption missing", force)
    if target in {"DONE", "PARTIAL"}:
        require(bool(artifacts.get("final")), "cannot finalize successful/partial run: final artifact missing", force)

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--run-id", required=True)
    ap.add_argument("--to", required=True, choices=sorted(ALLOWED))
    ap.add_argument("--note", default="")
    ap.add_argument("--force", action="store_true", help="Allow non-standard transition/precondition override; record forced=true")
    args = ap.parse_args()
    run = Path(args.root).resolve() / ".archon" / "runs" / args.run_id
    path = run / "manifest.json"
    if not path.exists(): raise SystemExit(f"manifest not found: {path}")
    data = json.loads(path.read_text(encoding="utf-8"))
    current = data.get("stage")
    if current not in ALLOWED: raise SystemExit(f"unknown current stage: {current}")
    if args.to not in ALLOWED[current] and not args.force:
        raise SystemExit(f"invalid transition: {current} -> {args.to}")
    check_preconditions(run, data, args.to, args.force)
    ts = now()
    data["stage"] = args.to
    data["updated_at"] = ts
    if args.to in TERMINAL: data["outcome"] = args.to
    entry = {"at": ts, "event": "stage_transition", "from": current, "to": args.to, "note": args.note, "forced": bool(args.force)}
    if args.force:
        entry["precondition_override"] = True
    data.setdefault("history", []).append(entry)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"{current} -> {args.to}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
