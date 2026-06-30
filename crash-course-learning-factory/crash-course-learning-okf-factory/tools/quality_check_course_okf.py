#!/usr/bin/env python3
"""Quality gate for generated Course Learning OKF instances.

This gate checks more than file existence. It fails course OKFs that still look
like generic skeletons, contain unresolved placeholders in critical learning
files, or lack course-specific exam content.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple

try:
    from tools.course_seed_registry import required_terms_for_course
except ModuleNotFoundError:  # allow running as a script from tools/
    from course_seed_registry import required_terms_for_course  # type: ignore

PLACEHOLDER_PATTERNS = [
    r"\bTBD\b",
    r"Fill this",
    r"placeholder",
    r"Add high-value definitions here",
    r"今日 A 类概念",
    r"今日核心问题",
    r"to be filled",
    r"pending diagnostic",
]

CRITICAL_CONTENT_FILES = [
    "course-map.md",
    "priority-map.md",
    "glossary.md",
    "plan/seven-day-plan.md",
    "plan/day-1.md",
    "quizzes/day-1-quiz.md",
    "final-review/must-know-list.md",
    "final-review/mock-exam.md",
]

STATE_FILES = [
    "state/current-state.md",
    "state/topic-ledger.md",
    "state/recall-deck.md",
    "state/misconceptions.md",
    "state/score-history.md",
    "state/next-action.md",
    "state/plan-changes.md",
]


def _read(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def _count_terms(text: str, terms: Iterable[str]) -> Tuple[int, List[str]]:
    lowered = text.lower()
    found: List[str] = []
    for term in terms:
        if term.lower() in lowered:
            found.append(term)
    return len(found), found


def _placeholder_hits(text: str) -> List[str]:
    hits: List[str] = []
    for pattern in PLACEHOLDER_PATTERNS:
        if re.search(pattern, text, flags=re.IGNORECASE):
            hits.append(pattern)
    return hits


def _score_deduct(score: int, amount: int) -> int:
    return max(0, score - amount)


def quality_check(root: Path, course_name: Optional[str] = None, days_available: Optional[int] = None) -> Dict[str, Any]:
    root = root.resolve()
    output_json = root / "generation-output.json"
    generated: Dict[str, Any] = {}
    if output_json.exists():
        try:
            generated = json.loads(output_json.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            generated = {}

    course = course_name or generated.get("course_okf_name") or root.name
    days = int(days_available or generated.get("initial_state", {}).get("days_remaining", 7))

    failures: List[Dict[str, str]] = []
    warnings: List[Dict[str, str]] = []
    repair_actions: List[str] = []

    # 1. Structural presence for the files that matter to quality.
    missing = [path for path in CRITICAL_CONTENT_FILES + STATE_FILES if not (root / path).exists()]
    for path in missing:
        failures.append({"code": "missing_required_quality_file", "path": path, "message": f"Missing quality-critical file: {path}"})
        repair_actions.append(f"Create `{path}` with course-specific content or state data.")

    # 2. Critical files should not still be placeholders.
    placeholder_files: Dict[str, List[str]] = {}
    for rel_path in CRITICAL_CONTENT_FILES:
        text = _read(root / rel_path)
        hits = _placeholder_hits(text)
        if hits:
            placeholder_files[rel_path] = hits
            failures.append({"code": "placeholder_content", "path": rel_path, "message": f"Unresolved placeholder markers: {', '.join(hits)}"})
            repair_actions.append(f"Rewrite `{rel_path}`; replace placeholders with course-specific topics, examples, questions, and scoring rules.")

    # 3. Known course seeds need visible course terms.
    term_bank = required_terms_for_course(course)
    all_critical_text = "\n".join(_read(root / path) for path in CRITICAL_CONTENT_FILES)
    term_count, found_terms = _count_terms(all_critical_text, term_bank)
    if term_bank:
        min_terms = min(6, max(4, len(term_bank) // 2))
        if term_count < min_terms:
            failures.append({
                "code": "insufficient_course_specific_terms",
                "path": ",".join(CRITICAL_CONTENT_FILES),
                "message": f"Only {term_count} known course terms found; expected at least {min_terms}.",
            })
            repair_actions.append("Populate course-map, priority-map, daily plans, quizzes, and final review with recognized course concepts.")
    else:
        warnings.append({
            "code": "unknown_course_no_seed_terms",
            "path": "course_okf_root",
            "message": "No local course seed term bank is available; require AI or human review using course materials.",
        })
        repair_actions.append("Run reconnaissance using user materials or public sources, then define a course term bank before marking content quality as passed.")

    # 4. Exam-readiness checks.
    priority = _read(root / "priority-map.md")
    if not all(marker in priority for marker in ["A", "B", "C"]):
        failures.append({"code": "abc_priority_missing", "path": "priority-map.md", "message": "A/B/C priority sections are not all visible."})
        repair_actions.append("Rewrite `priority-map.md` with A/B/C sections and exam-value reasons.")
    if priority.count("|") < 12 and "## A" not in priority:
        failures.append({"code": "priority_too_thin", "path": "priority-map.md", "message": "Priority map lacks enough topic-level detail."})
        repair_actions.append("Add at least five A topics with minimum exam answers.")

    day1 = _read(root / "plan/day-1.md")
    required_daily_markers = ["Recall", "Feynman", "Exam", "State"]
    missing_daily_markers = [marker for marker in required_daily_markers if marker.lower() not in day1.lower()]
    if missing_daily_markers:
        failures.append({"code": "day1_not_runnable", "path": "plan/day-1.md", "message": f"Day 1 lacks runnable markers: {', '.join(missing_daily_markers)}"})
        repair_actions.append("Rewrite `plan/day-1.md` with retrieval, map, explanation, Feynman task, exam practice, feedback, and state update.")

    quiz1 = _read(root / "quizzes/day-1-quiz.md")
    if "名词解释" not in quiz1 or "简答" not in quiz1:
        failures.append({"code": "quiz_missing_exam_items", "path": "quizzes/day-1-quiz.md", "message": "Day 1 quiz lacks exam-style term and short-answer items."})
        repair_actions.append("Rewrite `quizzes/day-1-quiz.md` with term explanation, short answer, comparison, and scoring bands.")

    mock_exam = _read(root / "final-review/mock-exam.md")
    if not any(token in mock_exam.lower() for token in ["points", "分", "exam", "mock"]):
        failures.append({"code": "mock_exam_not_exam_like", "path": "final-review/mock-exam.md", "message": "Mock exam does not look like a scored exam."})
        repair_actions.append("Create a scored mock exam near the target-score level.")

    # 5. Recoverability checks.
    next_action = _read(root / "state/next-action.md")
    state_score = _read(root / "state/score-history.md")
    if "next_action" not in next_action:
        failures.append({"code": "next_action_unparseable", "path": "state/next-action.md", "message": "next_action is missing."})
        repair_actions.append("Rewrite `state/next-action.md` with a parseable next_action field.")
    if "Score" not in state_score and "score" not in state_score:
        failures.append({"code": "score_history_unusable", "path": "state/score-history.md", "message": "score-history does not expose score fields."})
        repair_actions.append("Rewrite `state/score-history.md` with assessment-event columns.")

    # 6. Produce a weighted score.
    score = 100
    score = _score_deduct(score, 10 * len(missing))
    score = _score_deduct(score, 8 * len(placeholder_files))
    if term_bank:
        score = _score_deduct(score, max(0, 6 - term_count) * 5)
    else:
        score = _score_deduct(score, 20)
    exam_failure_count = len([f for f in failures if f["code"] in {"abc_priority_missing", "priority_too_thin", "day1_not_runnable", "quiz_missing_exam_items", "mock_exam_not_exam_like"}])
    score = _score_deduct(score, exam_failure_count * 8)
    recover_failure_count = len([f for f in failures if f["code"] in {"next_action_unparseable", "score_history_unusable"}])
    score = _score_deduct(score, recover_failure_count * 8)

    hard_gate_failures = [f for f in failures if f["code"] in {
        "missing_required_quality_file",
        "placeholder_content",
        "insufficient_course_specific_terms",
        "day1_not_runnable",
        "quiz_missing_exam_items",
        "mock_exam_not_exam_like",
    }]
    passed = score >= 75 and not hard_gate_failures

    return {
        "passed": passed,
        "score": score,
        "threshold": 75,
        "course_name": course,
        "known_course_seed_terms": bool(term_bank),
        "found_course_terms": found_terms,
        "term_count": term_count,
        "placeholder_files": placeholder_files,
        "failures": failures,
        "warnings": warnings,
        "repair_actions": list(dict.fromkeys(repair_actions)),
        "quality_dimensions": {
            "structure_presence": "checked",
            "placeholder_absence": "checked",
            "course_specificity": "checked_with_seed_terms" if term_bank else "needs_manual_or_ai_review",
            "exam_readiness": "checked",
            "recoverability": "checked",
        },
    }


def parse_args(argv: Optional[List[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Quality-check a generated Course Learning OKF.")
    parser.add_argument("course_okf_dir", type=Path, help="Generated course OKF directory.")
    parser.add_argument("--course-name", help="Course name override.")
    parser.add_argument("--days-available", type=int, help="Available days override.")
    parser.add_argument("--output-json", type=Path, help="Write quality report JSON to this path.")
    return parser.parse_args(argv)


def main(argv: Optional[List[str]] = None) -> int:
    args = parse_args(argv)
    report = quality_check(args.course_okf_dir, course_name=args.course_name, days_available=args.days_available)
    text = json.dumps(report, ensure_ascii=False, indent=2)
    if args.output_json:
        args.output_json.parent.mkdir(parents=True, exist_ok=True)
        args.output_json.write_text(text, encoding="utf-8")
    print(text)
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
