#!/usr/bin/env python3
"""Initialize a local/mounted Archon Shared Workspace run (manifest schema 0.2)."""
from __future__ import annotations
import argparse, json, re
from datetime import datetime, timezone
from pathlib import Path

MODES = {"standard", "fast", "strict"}
BACKENDS = {"github", "google_drive", "filesystem", "other"}
IO_MODES = {"direct_required", "direct_preferred", "return_only_allowed"}


def utcnow() -> str:
    return datetime.now(timezone.utc).isoformat()


def make_run_id() -> str:
    return datetime.now(timezone.utc).strftime("run-%Y%m%d-%H%M%S")


def safe_run_id(value: str) -> str:
    if not re.fullmatch(r"[A-Za-z0-9._-]+", value):
        raise SystemExit("run-id may contain only letters, digits, dot, underscore, and hyphen")
    return value


def policy(mode: str, generators: int | None) -> dict:
    base = {
        "generator_count": 4,
        "minimum_usable_generators": 3,
        "top_k": 2,
        "verifier_mode": "auto",
        "combine_critic_ranker": True,
        "max_extra_evaluators": 1,
        "max_generator_replacements": 1,
        "max_fusion_retries": 1,
        "max_schema_repairs_per_result": 1,
    }
    if mode == "fast":
        base.update({"generator_count": 4, "minimum_usable_generators": 3, "max_extra_evaluators": 0, "max_fusion_retries": 0})
    elif mode == "strict":
        base.update({"generator_count": 4, "minimum_usable_generators": 4, "combine_critic_ranker": False})
    if generators is not None:
        base["generator_count"] = generators
        base["minimum_usable_generators"] = min(base["minimum_usable_generators"], generators)
    return base


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--run-id")
    ap.add_argument("--mode", choices=sorted(MODES), default="standard")
    ap.add_argument("--workspace-backend", choices=sorted(BACKENDS), default="filesystem")
    ap.add_argument("--workspace-io-mode", choices=sorted(IO_MODES))
    ap.add_argument("--allow-return-only-fallback", action="store_true")
    ap.add_argument("--browser-base-url")
    ap.add_argument("--generator-count", type=int)
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()

    if args.generator_count is not None and not (1 <= args.generator_count <= 16):
        raise SystemExit("generator-count must be between 1 and 16")

    root = Path(args.root).resolve()
    run_id = safe_run_id(args.run_id or make_run_id())
    run = root / ".archon" / "runs" / run_id
    if run.exists() and not args.force:
        raise SystemExit(f"run already exists: {run}")

    for rel in ["generation", "verification", "critique", "ranking", "fusion", "final"]:
        (run / rel).mkdir(parents=True, exist_ok=True)

    pol = policy(args.mode, args.generator_count)
    scheduled = [f"G{i}" for i in range(1, pol["generator_count"] + 1)]
    for gid in scheduled:
        (run / "generation" / gid).mkdir(parents=True, exist_ok=True)
    # No result.json placeholders are created here: a Generator is recorded only
    # after it is terminal and its result has been normalized (or failed).

    io_mode = args.workspace_io_mode or ("direct_required" if args.workspace_backend == "github" else "direct_preferred")
    allow_return_only = args.allow_return_only_fallback or io_mode == "return_only_allowed"

    now = utcnow()
    manifest = {
        "schema_version": "0.2",
        "run_id": run_id,
        "created_at": now,
        "updated_at": now,
        "stage": "INIT",
        "outcome": None,
        "mode": args.mode,
        "workspace": {
            "backend": args.workspace_backend,
            "authorized_root": str(root),
            "control_namespace": f".archon/runs/{run_id}",
            "adapter": "",
            "version": None,
            "io_policy": {
                "workspace_io_mode": io_mode,
                "inline_artifact_transport": False,
                "allow_return_only_fallback": allow_return_only,
            },
        },
        "browser_execution": {
            "base_url": args.browser_base_url,
            "fresh_page_per_generator": True,
            "fresh_conversation_per_generator": True,
            "allow_generator_followup_reuse": False,
        },
        "policy": pol,
        "counters": {
            "generator_replacements_used": 0,
            "extra_evaluators_used": 0,
            "fusion_retries_used": 0,
            "schema_repairs_used": 0,
        },
        "scheduled_generators": scheduled,
        "executions": {"generators": {}, "evaluators": [], "fuser": None, "verifiers": []},
        "artifacts": {
            "task": "task.md",
            "executors": "executors.json",
            "generation": {},
            "verification": [],
            "critique": None,
            "ranking": None,
            "fusion": None,
            "final": None,
        },
        "decisions": {
            "generation_barrier": None,
            "top_k": [],
            "preserved_insights_ref": None,
            "winner_adoption": None,
        },
        "reconciliation": {"last_checked_at": None, "notes": []},
        "history": [{"at": now, "event": "initialized", "stage": "INIT"}],
    }
    (run / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    task = "# Frozen Task\n\n## Objective\n\n<TODO>\n\n## Inputs / Base Artifacts\n\n- <TODO>\n\n## Constraints\n\n- <TODO>\n\n## Success Criteria\n\n- <TODO>\n\n## Assumptions\n\n- <none or TODO>\n\n## Open Questions\n\n- <none or TODO>\n"
    (run / "task.md").write_text(task, encoding="utf-8")
    (run / "executors.json").write_text(json.dumps({"schema_version": "0.2", "executors": []}, indent=2) + "\n", encoding="utf-8")
    print(run_id)
    print(run)
    print(f"Workspace I/O: {io_mode}; return-only fallback: {allow_return_only}")
    if args.browser_base_url:
        print(f"Browser base URL: {args.browser_base_url} (fresh page + fresh conversation required per Generator)")
    print("Next: freeze task.md, record executor capabilities, then advance to GENERATING.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
