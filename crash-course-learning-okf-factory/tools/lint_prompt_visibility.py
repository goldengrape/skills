#!/usr/bin/env python3
"""Lint generated Course OKF files for prompt-visibility leaks.

The checker focuses on student-visible prompts. Teacher-private files may contain
rubrics, answer keys, expected answer elements, and internal planning notes.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any, Dict, List, Optional

FORBIDDEN_PATTERNS = [
    r"至少提到",
    r"要求至少",
    r"答案要点",
    r"评分标准",
    r"标准答案",
    r"参考答案",
    r"正确答案",
    r"得分点",
    r"expected[_ -]?points",
    r"model answer",
    r"teacher_thinks",
    r"answer key",
]

STUDENT_VISIBLE_GLOBS = [
    "plan/day-*.md",
    "quizzes/day-*-quiz.md",
]

REQUIRED_RUNTIME_FILES = [
    "teacher/teacher-notebook.md",
    "teacher/visibility-rules.md",
    "teacher/teaching-protocol.md",
    "teacher/engagement-monitor.md",
    "teacher/engagement-intervention-rules.md",
    "teacher/time-policy.md",
    "state/interest-ledger.md",
]


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.exists() else ""


def _student_files(root: Path) -> List[Path]:
    files: List[Path] = []
    for pattern in STUDENT_VISIBLE_GLOBS:
        files.extend(root.glob(pattern))
    return sorted(set(files))


def lint_prompt_visibility(root: Path) -> Dict[str, Any]:
    root = root.resolve()
    failures: List[Dict[str, str]] = []
    warnings: List[Dict[str, str]] = []

    missing_runtime = [path for path in REQUIRED_RUNTIME_FILES if not (root / path).exists()]
    for path in missing_runtime:
        failures.append({"code": "missing_teaching_runtime_file", "path": path, "message": f"Missing teaching runtime file: {path}"})

    for path in _student_files(root):
        rel = str(path.relative_to(root))
        text = _read(path)
        for pattern in FORBIDDEN_PATTERNS:
            if re.search(pattern, text, flags=re.IGNORECASE):
                failures.append({
                    "code": "prompt_visibility_leak",
                    "path": rel,
                    "message": f"Student-visible file contains hidden-answer/rubric marker: {pattern}",
                })

    notebook = _read(root / "teacher/teacher-notebook.md")
    if "teacher_says" not in notebook or "teacher_thinks" not in notebook:
        failures.append({
            "code": "teacher_notebook_schema_missing",
            "path": "teacher/teacher-notebook.md",
            "message": "Teacher notebook must define teacher_says and teacher_thinks fields.",
        })

    visibility = _read(root / "teacher/visibility-rules.md")
    if "Before Learner Answers" not in visibility or "After Learner Answers" not in visibility:
        failures.append({
            "code": "visibility_rules_incomplete",
            "path": "teacher/visibility-rules.md",
            "message": "Visibility rules must separate before-answer and after-answer behavior.",
        })

    time_policy = _read(root / "teacher/time-policy.md") + "\n" + _read(root / "mission.md")
    if "soft" not in time_policy or "strict" not in time_policy:
        failures.append({
            "code": "time_policy_missing_soft_strict",
            "path": "teacher/time-policy.md",
            "message": "Time policy must distinguish soft and strict modes.",
        })

    engagement = _read(root / "teacher/engagement-monitor.md") + "\n" + _read(root / "teacher/engagement-intervention-rules.md")
    if "observable" not in engagement.lower() and "可观察" not in engagement:
        warnings.append({
            "code": "engagement_observability_not_explicit",
            "path": "teacher/engagement-monitor.md",
            "message": "Engagement monitor should state that it uses observable signals rather than mind-reading.",
        })
    if "interest" not in engagement.lower() and "兴趣" not in engagement:
        failures.append({
            "code": "engagement_interest_rules_missing",
            "path": "teacher/engagement-intervention-rules.md",
            "message": "Engagement rules must include interest-preserving behavior.",
        })

    score_history = _read(root / "state/score-history.md")
    if "Score type" not in score_history and "score_type" not in score_history:
        failures.append({
            "code": "score_type_missing",
            "path": "state/score-history.md",
            "message": "Score history must record blind_score, semi_assisted_score, or assisted_score.",
        })
    if "Prompt visibility" not in score_history and "prompt_visibility" not in score_history:
        failures.append({
            "code": "prompt_visibility_field_missing",
            "path": "state/score-history.md",
            "message": "Score history must record whether hints or answer elements were shown before the answer.",
        })

    return {
        "passed": not failures,
        "student_visible_files_checked": [str(p.relative_to(root)) for p in _student_files(root)],
        "forbidden_patterns": FORBIDDEN_PATTERNS,
        "failures": failures,
        "warnings": warnings,
        "quality_dimensions": {
            "prompt_visibility": "checked",
            "teacher_notebook": "checked",
            "score_type": "checked",
            "time_policy": "checked",
            "interest_and_engagement": "checked",
        },
    }


def parse_args(argv: Optional[List[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Lint student-visible prompts for hidden scoring leaks.")
    parser.add_argument("course_okf_dir", type=Path)
    parser.add_argument("--output-json", type=Path)
    return parser.parse_args(argv)


def main(argv: Optional[List[str]] = None) -> int:
    args = parse_args(argv)
    report = lint_prompt_visibility(args.course_okf_dir)
    text = json.dumps(report, ensure_ascii=False, indent=2)
    if args.output_json:
        args.output_json.parent.mkdir(parents=True, exist_ok=True)
        args.output_json.write_text(text, encoding="utf-8")
    print(text)
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
