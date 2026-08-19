#!/usr/bin/env python3
"""Health check for a local/mounted Archon run, plus package-level consistency checks.

Run-level checks: manifest schema (0.1 accepted with warnings, 0.2 fully validated),
stage validity, frozen task, generator namespaces, generation barrier (terminal
statuses, usable count, normalized result.json consistency), stage-gated artifact
refs, budget counters, and final outcome consistency.

Package-level checks (auto-enabled when the workspace root also contains
manifest.txt, i.e. the root is the skill package): manifest.txt matches the file
tree, no .archon run-state paths are listed, and SKILL.md references resolve.
Inline code examples are ignored via fenced-code scanning to avoid false positives.
"""
from __future__ import annotations
import argparse, json, re
from dataclasses import dataclass
from pathlib import Path

VALID_STAGES = {"INIT","GENERATING","VERIFYING_GENERATION","CRITIQUING","RANKING","FUSING","FINAL_VERIFY","FINALIZING","DONE","PARTIAL","FAILED"}
TERMINAL_EXEC = {"completed","failed","cancelled","contaminated"}
BARRIER_STAGES = {"VERIFYING_GENERATION","CRITIQUING","RANKING","FUSING","FINAL_VERIFY","FINALIZING","DONE","PARTIAL"}
EXTERNAL_REF = re.compile(r"(?:^|://|[A-Za-z0-9_-]+://)")

@dataclass
class Finding:
    level: str
    path: str
    message: str

def load_json(path: Path, findings: list[Finding]):
    try: return json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:
        findings.append(Finding("error", str(path), f"invalid JSON: {e}"))
        return None

def ref_exists(root: Path, run: Path, ref: str | None) -> bool:
    """External refs (http(s) or any '://') are recorded as-is and never flagged missing."""
    if not ref:
        return False
    if "://" in ref:
        return True
    p = Path(ref)
    if p.is_absolute():
        return p.exists()
    return (run / p).exists() or (root / p).exists()

def scheduled_ids(data: dict, n: int) -> list[str]:
    sched = data.get("scheduled_generators")
    if isinstance(sched, list) and sched:
        return [str(s) for s in sched]
    return [f"G{i}" for i in range(1, n + 1)]

# ---------------------------------------------------------------- package checks

def check_package(pkg: Path, findings: list[Finding]) -> None:
    """manifest.txt vs file tree, plus fence-aware SKILL.md reference scan."""
    manifest_file = pkg / "manifest.txt"
    if not manifest_file.exists():
        findings.append(Finding("info", "manifest.txt", "no manifest.txt at root; package-level checks skipped"))
        return
    listed: list[str] = []
    for line in manifest_file.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith(".archon"):
            findings.append(Finding("error", "manifest.txt", f"run-state path must not be listed: {line}"))
            continue
        listed.append(line)
    for rel in listed:
        p = pkg / rel
        if not p.exists():
            findings.append(Finding("error", "manifest.txt", f"listed file missing from package: {rel}"))
        elif not p.is_file():
            findings.append(Finding("error", "manifest.txt", f"listed entry is not a file: {rel}"))
    # Unlisted package files (excluding run state and VCS/cache dirs).
    listed_set = {Path(l).as_posix() for l in listed}
    for p in sorted(pkg.rglob("*")):
        if not p.is_file():
            continue
        rel = p.relative_to(pkg).as_posix()
        if rel == "manifest.txt":
            continue
        if rel.startswith((".archon/", ".git/", "__pycache__/")):
            continue
        if rel not in listed_set:
            findings.append(Finding("warn", "manifest.txt", f"package file not listed in manifest.txt: {rel}"))
    # SKILL.md reference scan, ignoring fenced code blocks.
    skill = pkg / "SKILL.md"
    if not skill.exists():
        findings.append(Finding("error", "SKILL.md", "SKILL.md missing from package root"))
        return
    ref_re = re.compile(r"(references|adapters|checklists|scripts|templates)/([A-Za-z0-9._-]+\.(?:md|py|json))")
    in_fence = False
    for lineno, line in enumerate(skill.read_text(encoding="utf-8").splitlines(), start=1):
        stripped = line.strip()
        if stripped.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        for m in ref_re.finditer(line):
            rel = f"{m.group(1)}/{m.group(2)}"
            if not (pkg / rel).exists():
                findings.append(Finding("error", f"SKILL.md:{lineno}", f"reference to missing package file: {rel}"))

# ------------------------------------------------------------------ run checks

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--run-id", required=True)
    args = ap.parse_args()
    root = Path(args.root).resolve()
    run = root / ".archon" / "runs" / args.run_id
    findings: list[Finding] = []

    if (root / "manifest.txt").exists():
        check_package(root, findings)

    manifest_path = run / "manifest.json"
    if not manifest_path.exists():
        print("ERROR manifest.json missing")
        return 2
    m = load_json(manifest_path, findings) or {}
    if m.get("run_id") != args.run_id:
        findings.append(Finding("error", "manifest.json", "run_id mismatch"))
    stage = m.get("stage")
    if stage not in VALID_STAGES:
        findings.append(Finding("error", "manifest.json", f"invalid stage: {stage}"))
    schema = m.get("schema_version", "0.1")
    if schema not in {"0.1", "0.2"}:
        findings.append(Finding("warn", "manifest.json", f"unknown schema_version: {schema}"))
    elif schema == "0.1":
        findings.append(Finding("warn", "manifest.json", "legacy schema 0.1 manifest; result.json/counter checks limited"))
    if not (run / "task.md").exists():
        findings.append(Finding("error", "task.md", "frozen task missing"))
    else:
        task = (run / "task.md").read_text(encoding="utf-8", errors="ignore")
        if "<TODO>" in task and stage not in {"INIT", "FAILED"}:
            findings.append(Finding("error", "task.md", "task still contains TODO after INIT"))

    policy = m.get("policy", {})
    n = int(policy.get("generator_count", 0) or 0)
    if n < 1:
        findings.append(Finding("error", "manifest.json", "generator_count must be >= 1"))
    ids = scheduled_ids(m, n)
    for gid in ids:
        d = run / "generation" / gid
        if not d.exists():
            findings.append(Finding("error", str(d.relative_to(root)), "generator namespace missing"))

    gen_exec = m.get("executions", {}).get("generators", {})
    outcome = m.get("outcome")
    barrier_reached = stage in BARRIER_STAGES
    if barrier_reached:
        if len(gen_exec) < len(ids):
            findings.append(Finding("error", "manifest.json", "generation barrier passed before all scheduled generators were recorded"))
        usable = 0
        for gid in ids:
            info = gen_exec.get(gid)
            if not isinstance(info, dict):
                continue
            status = info.get("status")
            if status not in TERMINAL_EXEC:
                findings.append(Finding("error", "manifest.json", f"{gid} not terminal at/after barrier: {status}"))
                continue
            result_path = run / "generation" / gid / "result.json"
            result = load_json(result_path, findings) if result_path.exists() else None
            if result is None and status == "completed":
                findings.append(Finding("warn", str(result_path.relative_to(root)), f"terminal {gid} lacks normalized result.json"))
            if result is not None:
                if result.get("candidate_id") not in {None, gid}:
                    findings.append(Finding("error", str(result_path.relative_to(root)), f"candidate_id mismatch for {gid}"))
                if result.get("status") not in {None, status}:
                    findings.append(Finding("error", str(result_path.relative_to(root)), f"status mismatch for {gid}"))
                expected_ns = f"generation/{gid}"
                if result.get("output_namespace") not in {None, expected_ns}:
                    findings.append(Finding("error", str(result_path.relative_to(root)), f"unexpected output_namespace for {gid}"))
                for key in ("direct_workspace_write", "return_only_normalized_by_orchestrator", "usable"):
                    if key in result and not isinstance(result.get(key), bool):
                        findings.append(Finding("error", str(result_path.relative_to(root)), f"{key} must be boolean"))
                if status == "completed" and not result.get("artifact_ref"):
                    findings.append(Finding("error", str(result_path.relative_to(root)), f"{gid} completed without artifact_ref in result.json"))
            if status == "completed":
                if not info.get("artifact_ref"):
                    findings.append(Finding("error", "manifest.json", f"{gid} completed without artifact_ref"))
                elif not ref_exists(root, run, info.get("artifact_ref")):
                    findings.append(Finding("warn", "manifest.json", f"{gid} artifact_ref is not locally resolvable: {info.get('artifact_ref')}"))
                if info.get("usable", True) is not False:
                    usable += 1
                if info.get("return_only_normalized_by_orchestrator") is False and info.get("direct_workspace_write") is False:
                    findings.append(Finding("warn", "manifest.json", f"{gid} is return-only but not marked return_only_normalized_by_orchestrator"))
            if status == "contaminated":
                findings.append(Finding("warn", "manifest.json", f"{gid} contaminated; excluded from usable set (reason: {info.get('status_reason') or info.get('failure_reason') or 'not recorded'})"))
        minimum = int(policy.get("minimum_usable_generators", min(3, n)) or 0)
        if usable < minimum and outcome not in {"PARTIAL", "FAILED"}:
            findings.append(Finding("error", "manifest.json", f"usable generators {usable} below policy minimum {minimum}"))
        elif usable < minimum:
            findings.append(Finding("warn", "manifest.json", f"usable generators {usable} below policy minimum {minimum} (declared {outcome})"))

    if stage in {"RANKING","FUSING","FINAL_VERIFY","FINALIZING","DONE","PARTIAL"}:
        critique = m.get("artifacts", {}).get("critique")
        if not critique:
            findings.append(Finding("error", "manifest.json", "critique artifact missing after CRITIQUING"))
    if stage in {"FUSING","FINAL_VERIFY","FINALIZING","DONE","PARTIAL"}:
        ranking = m.get("artifacts", {}).get("ranking")
        if not ranking:
            findings.append(Finding("error", "manifest.json", "ranking artifact missing after RANKING"))
    if stage in {"FINAL_VERIFY","DONE","PARTIAL"}:
        fusion = m.get("artifacts", {}).get("fusion")
        winner = (m.get("decisions", {}) or {}).get("winner_adoption")
        if not fusion and not winner:
            findings.append(Finding("warn", "manifest.json", "fusion artifact missing; ensure winner-adoption/skip is explicitly recorded"))
    if stage in {"DONE","PARTIAL"} and not m.get("artifacts", {}).get("final"):
        findings.append(Finding("error", "manifest.json", "final artifact missing for terminal successful/partial outcome"))

    if schema == "0.2":
        counters = m.get("counters", {}) or {}
        for key, max_key in (("generator_replacements_used","max_generator_replacements"),
                             ("extra_evaluators_used","max_extra_evaluators"),
                             ("fusion_retries_used","max_fusion_retries"),
                             ("schema_repairs_used","max_schema_repairs_per_result")):
            used = counters.get(key, 0)
            cap = policy.get(max_key)
            if isinstance(cap, int) and isinstance(used, int) and used > cap:
                findings.append(Finding("error", "manifest.json", f"counter {key} {used} exceeds policy max {cap}"))
        rec = m.get("reconciliation", {}) or {}
        if not rec.get("last_checked_at") and stage not in {"INIT"}:
            findings.append(Finding("info", "manifest.json", "reconciliation.last_checked_at not recorded"))

    if stage in {"DONE","PARTIAL","FAILED"}:
        final_ref = m.get("artifacts", {}).get("final")
        if final_ref:
            if ref_exists(root, run, final_ref):
                final_path = Path(final_ref)
                if not final_path.is_absolute():
                    final_path = (run / final_path) if (run / final_path).exists() else (root / final_path)
                if final_path.name.endswith(".json"):
                    outcome_rec = load_json(final_path, findings) or {}
                    if outcome_rec.get("run_id") not in {None, args.run_id}:
                        findings.append(Finding("error", str(final_path.relative_to(root)), "outcome run_id mismatch"))
                    if outcome_rec.get("outcome") not in {"DONE","PARTIAL","FAILED"}:
                        findings.append(Finding("error", str(final_path.relative_to(root)), "invalid outcome value"))
                    if stage in {"DONE","PARTIAL"} and not outcome_rec.get("final_artifact_ref"):
                        findings.append(Finding("error", str(final_path.relative_to(root)), "final_artifact_ref missing in outcome"))
            else:
                findings.append(Finding("warn", "manifest.json", f"final artifact is not locally resolvable: {final_ref}"))

    for f in findings:
        print(f"{f.level.upper():5} {f.path}: {f.message}")
    errors = sum(f.level == "error" for f in findings)
    warns = sum(f.level == "warn" for f in findings)
    infos = sum(f.level == "info" for f in findings)
    print(f"Summary: {errors} error(s), {warns} warning(s), {infos} info")
    return 2 if errors else 0

if __name__ == "__main__":
    raise SystemExit(main())
