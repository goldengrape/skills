#!/usr/bin/env python3
"""Minimal learning-control quality gate for generated Course OKF instances.

Round 7 applies Occam's razor: one learning contract, one teacher policy,
and one evidence ledger are enough to enforce L1-L9, AI diet, productive
friction, verifiability, feedback anchoring, and barehand checks.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any, Dict, List, Optional

REQUIRED_LEARNING_FILES = [
    "learning-contract/index.md",
    "teacher/learning-control-policy.md",
    "state/concept-mastery-state.md",
    "state/assessment-evidence-ledger.md",
]

FORBIDDEN_PSEUDO_MASTERY = [
    r"mastered\s*:\s*true",
    r"status\s*:\s*mastered",
    r"完全掌握",
    r"掌握度\s*[:：]?\s*\d+%",
]

LOW_VALUE_GAMIFICATION = [r"徽章", r"badge", r"streak", r"连续打卡", r"排名", r"leaderboard"]


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.exists() else ""


def check_learning_stage_evidence(root: Path) -> Dict[str, Any]:
    root = root.resolve()
    failures: List[Dict[str, str]] = []
    warnings: List[Dict[str, str]] = []

    for rel in REQUIRED_LEARNING_FILES:
        if not (root / rel).exists():
            failures.append({"code": "missing_learning_control_file", "path": rel, "message": f"Missing learning-control file: {rel}"})

    contract = _read(root / "learning-contract/index.md")
    policy = _read(root / "teacher/learning-control-policy.md")
    concept_state = _read(root / "state/concept-mastery-state.md")
    evidence_ledger = _read(root / "state/assessment-evidence-ledger.md")
    combined = "\n".join([contract, policy, concept_state, evidence_ledger])

    for level in [f"L{i}" for i in range(1, 10)]:
        if level not in contract:
            failures.append({"code": "learning_stage_rubric_incomplete", "path": "learning-contract/index.md", "message": f"Missing {level} definition."})

    if "default_core_target: L6" not in contract and "default core target is L6" not in contract:
        failures.append({"code": "default_core_target_not_L6", "path": "learning-contract/index.md", "message": "Learning contract must declare L6 as the default core target unless user override is explicit."})

    for mode in ["guided", "semi_guided", "blind", "barehand"]:
        if mode not in combined:
            failures.append({"code": "assistance_mode_missing", "path": "learning-contract/index.md", "message": f"Missing assistance mode: {mode}"})

    if "misuse" not in combined.lower() and "误用" not in combined:
        failures.append({"code": "l6_misuse_check_missing", "path": "teacher/learning-control-policy.md", "message": "L6 concepts must require misuse discrimination or flawed-answer checks."})
    if "transfer" not in combined.lower() and "迁移" not in combined:
        failures.append({"code": "l7_transfer_check_missing", "path": "teacher/learning-control-policy.md", "message": "L7 targets must require transfer checks."})
    if "barehand" not in combined.lower() or "2-3" not in combined:
        failures.append({"code": "barehand_checkpoint_not_scheduled", "path": "state/assessment-evidence-ledger.md", "message": "Barehand checkpoint schedule is missing."})
    if "independent recall" not in combined.lower() and "独立" not in combined:
        failures.append({"code": "productive_friction_missing", "path": "teacher/learning-control-policy.md", "message": "Productive friction policy must preserve independent recall or equivalent."})
    if "source" not in combined.lower() and "资料" not in combined:
        failures.append({"code": "feedback_anchor_missing", "path": "teacher/learning-control-policy.md", "message": "Feedback policy must anchor feedback to source/rubric/output evidence."})
    if "textbook" not in combined.lower() and "考试" not in combined:
        failures.append({"code": "model_vs_reality_missing", "path": "teacher/learning-control-policy.md", "message": "Model-vs-reality protocol must distinguish exam/textbook model from real-world complexity."})
    if "badge" not in combined.lower() and "徽章" not in combined:
        failures.append({"code": "negative_feature_list_missing", "path": "teacher/learning-control-policy.md", "message": "Negative feature list must mention badges/streaks/rankings or equivalent low-value gamification."})

    checked_text = "\n".join(_read(path) for path in root.glob("**/*.md") if "teacher/answer-keys" not in str(path))
    for pattern in FORBIDDEN_PSEUDO_MASTERY:
        if re.search(pattern, checked_text, flags=re.IGNORECASE):
            failures.append({"code": "unsupported_mastery_claim", "path": "course_okf_root", "message": f"Potential unsupported mastery claim detected: {pattern}"})
            break

    for pattern in LOW_VALUE_GAMIFICATION:
        if re.search(pattern, checked_text, flags=re.IGNORECASE):
            # The negative-feature section is expected to mention these terms. Warn only when they appear elsewhere.
            matches = [str(p.relative_to(root)) for p in root.glob("**/*.md") if re.search(pattern, _read(p), flags=re.IGNORECASE) and p.name not in {"index.md", "learning-control-policy.md"}]
            if matches:
                warnings.append({"code": "possible_low_value_gamification", "path": ", ".join(matches[:5]), "message": f"Possible low-value gamification term detected: {pattern}"})

    return {
        "passed": not failures,
        "learning_contract_present": (root / "learning-contract/index.md").exists(),
        "default_core_target": "L6" if "L6" in contract else "unknown",
        "assistance_modes_checked": True,
        "productive_friction_policy_present": (root / "teacher/learning-control-policy.md").exists(),
        "barehand_checkpoints_present": "barehand" in evidence_ledger.lower(),
        "minimal_contract_files": REQUIRED_LEARNING_FILES,
        "failures": failures,
        "warnings": warnings,
        "quality_dimensions": {
            "learning_contract": "checked_compact",
            "assistance_modes": "checked_compact",
            "productive_friction": "checked_compact",
            "feedback_anchor": "checked_compact",
            "model_vs_reality": "checked_compact",
            "negative_features": "checked_compact",
        },
    }


def parse_args(argv: Optional[List[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check learning-stage / AI-diet quality for a generated Course OKF.")
    parser.add_argument("course_okf_dir", type=Path)
    parser.add_argument("--output-json", type=Path)
    return parser.parse_args(argv)


def main(argv: Optional[List[str]] = None) -> int:
    args = parse_args(argv)
    report = check_learning_stage_evidence(args.course_okf_dir)
    text = json.dumps(report, ensure_ascii=False, indent=2)
    if args.output_json:
        args.output_json.parent.mkdir(parents=True, exist_ok=True)
        args.output_json.write_text(text, encoding="utf-8")
    print(text)
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
