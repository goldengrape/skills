#!/usr/bin/env python3
"""Advance an Archon run manifest through allowed logical stages with lightweight precondition checks."""
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

def check_preconditions(run: Path, data: dict, target: str, force: bool) -> None:
    policy = data.get("policy", {})
    artifacts = data.get("artifacts", {})
    if target == "GENERATING":
        task = run / "task.md"
        require(task.exists(), "cannot start generation: task.md missing", force)
        if task.exists():
            text = task.read_text(encoding="utf-8", errors="ignore")
            require("<TODO>" not in text, "cannot start generation: task.md still contains <TODO>", force)
    if target in {"VERIFYING_GENERATION", "CRITIQUING"}:
        n = int(policy.get("generator_count", 0) or 0)
        minimum = int(policy.get("minimum_usable_generators", min(3, n)) or 0)
        gens = data.get("executions", {}).get("generators", {})
        require(len(gens) >= n, "cannot pass generation barrier: not all scheduled generators are recorded", force)
        statuses = [gens.get(f"G{i}", {}).get("status") for i in range(1, n + 1)]
        require(all(s in TERMINAL_EXEC for s in statuses), f"cannot pass generation barrier: non-terminal statuses {statuses}", force)
        usable = sum(1 for s in statuses if s == "completed")
        require(usable >= minimum, f"cannot pass generation barrier: usable generators {usable} < minimum {minimum}", force)
    if target == "RANKING":
        require(bool(artifacts.get("critique")), "cannot rank: critique artifact missing", force)
    if target == "FUSING":
        require(bool(artifacts.get("ranking")), "cannot fuse: ranking artifact missing", force)
    if target in {"FINAL_VERIFY", "FINALIZING"} and data.get("stage") == "FUSING":
        require(bool(artifacts.get("fusion")), "cannot leave fusion: fusion artifact missing", force)
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
    data.setdefault("history", []).append({"at": ts, "event": "stage_transition", "from": current, "to": args.to, "note": args.note, "forced": bool(args.force)})
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"{current} -> {args.to}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
