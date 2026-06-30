#!/usr/bin/env python3
"""Materialize a Course Learning OKF instance from a normalized factory input.

The helper creates the required file tree, initial state files, day plans,
quizzes, and a compact output contract. It also runs a post-generation quality
gate. If a tested local course seed exists, the helper repairs generic skeleton
content once and reruns the quality gate. Unknown courses are still materialized,
but the quality report must fail until a human or AI fills course-specific
content from materials or reconnaissance.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional

try:
    from tools.course_seed_registry import apply_course_seed
    from tools.quality_check_course_okf import quality_check
except ModuleNotFoundError:  # allow running as a script from tools/
    from course_seed_registry import apply_course_seed  # type: ignore
    from quality_check_course_okf import quality_check  # type: ignore

DEFAULT_BASELINE = "zero"
DEFAULT_DAYS = 7
DEFAULT_DAILY_MINUTES = 60
DEFAULT_TARGET_SCORE = 60
DEFAULT_EXAM_FORMAT = "unknown"
DEFAULT_COURSE_TYPE = "concept_heavy"
DEFAULT_MATERIALS_AVAILABLE = "none"

VALID_BASELINES = {"zero", "weak", "partial", "review"}
VALID_NEXT_ACTIONS = {"run_day_1", "continue", "repair", "review", "simulate", "final_review"}

STATE_FILES = [
    "state/current-state.md",
    "state/topic-ledger.md",
    "state/recall-deck.md",
    "state/misconceptions.md",
    "state/score-history.md",
    "state/next-action.md",
    "state/plan-changes.md",
]

FINAL_REVIEW_FILES = [
    "final-review/index.md",
    "final-review/compressed-notes.md",
    "final-review/must-know-list.md",
    "final-review/answer-templates.md",
    "final-review/mock-exam.md",
]

RESUME_RULES = [
    "read state/current-state.md",
    "read state/next-action.md",
    "read state/recall-deck.md",
    "read state/misconceptions.md",
    "read state/score-history.md",
    "read latest sessions/*.md",
    "read relevant plan/day-N.md",
]

STATE_UPDATE_RULES = [
    "read state before teaching",
    "create session record after session",
    "update score history after assessment",
    "update recall deck for missed or high-value items",
    "update misconceptions for wrong distinctions",
    "write next action before ending",
]


@dataclass
class FactoryInput:
    course_name: str
    baseline: str = DEFAULT_BASELINE
    days_available: int = DEFAULT_DAYS
    daily_minutes: int = DEFAULT_DAILY_MINUTES
    target_score: Any = DEFAULT_TARGET_SCORE
    exam_date: Optional[str] = None
    exam_format: str = DEFAULT_EXAM_FORMAT
    course_type: str = DEFAULT_COURSE_TYPE
    materials_available: str = DEFAULT_MATERIALS_AVAILABLE
    materials: List[Dict[str, Any]] = field(default_factory=list)
    constraints: List[str] = field(default_factory=list)
    language: str = "zh"


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def slugify(course_name: str) -> str:
    ascii_name = course_name.encode("ascii", "ignore").decode("ascii").lower()
    slug = re.sub(r"[^a-z0-9]+", "-", ascii_name).strip("-")
    if not slug:
        digest = hashlib.sha1(course_name.encode("utf-8")).hexdigest()[:8]
        slug = f"course-{digest}"
    return f"course-okf-{slug}-pass"


def frontmatter(kind: str, title: str, description: str, tags: Iterable[str]) -> str:
    tag_text = ", ".join(tags)
    return (
        "---\n"
        f"type: {kind}\n"
        f"title: {title}\n"
        f"description: {description}\n"
        f"tags: [{tag_text}]\n"
        f"timestamp: {now_iso()}\n"
        "---\n\n"
    )


def normalize(raw: Dict[str, Any]) -> FactoryInput:
    course_name = str(raw.get("course_name", "")).strip()
    if not course_name:
        raise ValueError("course_name is required")

    baseline = str(raw.get("baseline", DEFAULT_BASELINE)).strip() or DEFAULT_BASELINE
    if baseline not in VALID_BASELINES:
        raise ValueError(f"baseline must be one of {sorted(VALID_BASELINES)}")

    days_available = int(raw.get("days_available", DEFAULT_DAYS))
    if days_available < 1 or days_available > 30:
        raise ValueError("days_available must be between 1 and 30")

    daily_minutes = int(raw.get("daily_minutes", DEFAULT_DAILY_MINUTES))
    if daily_minutes < 20 or daily_minutes > 240:
        raise ValueError("daily_minutes must be between 20 and 240")

    materials = raw.get("materials", []) or []
    if not isinstance(materials, list):
        raise ValueError("materials must be a list")

    constraints = raw.get("constraints", []) or []
    if isinstance(constraints, str):
        constraints = [constraints]
    if not isinstance(constraints, list):
        raise ValueError("constraints must be a list or string")

    return FactoryInput(
        course_name=course_name,
        baseline=baseline,
        days_available=days_available,
        daily_minutes=daily_minutes,
        target_score=raw.get("target_score", DEFAULT_TARGET_SCORE),
        exam_date=raw.get("exam_date"),
        exam_format=str(raw.get("exam_format", DEFAULT_EXAM_FORMAT)),
        course_type=str(raw.get("course_type", DEFAULT_COURSE_TYPE)),
        materials_available=str(raw.get("materials_available", DEFAULT_MATERIALS_AVAILABLE)),
        materials=materials,
        constraints=[str(item) for item in constraints],
        language=str(raw.get("language", "zh")),
    )


def read_input_json(path: Optional[Path]) -> Dict[str, Any]:
    if path is None:
        return {}
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def write(path: Path, content: str, created_files: List[Dict[str, Any]], required: bool = True, template: str = "materializer") -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    created_files.append({"path": str(path), "required": required, "source_template": template})


def index_content(title: str, description: str, links: List[str]) -> str:
    body = frontmatter("Index", title, description, ["index"])
    body += "# " + title + "\n\n" + description + "\n\n"
    if links:
        body += "## Files\n\n" + "\n".join(f"- `{link}`" for link in links) + "\n"
    return body


def daily_plan_content(input_data: FactoryInput, day: int) -> str:
    return frontmatter(
        "Daily Work Package",
        f"{input_data.course_name} Day {day}",
        "One time-boxed crash-course learning session.",
        ["plan", "daily", "crash-course"],
    ) + f"""# Day {day}

## Goal

Use this day to advance pass-level readiness for `{input_data.course_name}` while protecting A-priority topics.

## Time Box

| Minutes | Activity |
|---:|---|
| 0-5 | Due recall cards and previous-session retrieval |
| 5-10 | Today's goal and exam value |
| 10-25 | Core explanation with examples, counterexamples, and contrasts |
| 25-35 | Feynman task by the learner |
| 35-45 | Exam-style question practice |
| 45-55 | Feedback and repair |
| 55-60 | State-update summary |

Configured daily minutes: `{input_data.daily_minutes}`. If the configured time is not 60 minutes, scale lower-priority work first; do not skip state updates.

## Required Evidence

- Feynman explanation result.
- At least one exam-style answer or quiz item.
- Any misconception or weak distinction.
- Next action for the following session.

## State Update

After this session, update `sessions/day-{day}-session.md`, `state/score-history.md`, `state/recall-deck.md`, `state/misconceptions.md`, and `state/next-action.md`.
"""


def quiz_content(input_data: FactoryInput, day: int) -> str:
    return frontmatter(
        "Quiz",
        f"{input_data.course_name} Day {day} Quiz",
        "Short pass-level quiz for a daily session.",
        ["quiz", "assessment"],
    ) + f"""# Day {day} Quiz

## Purpose

Check whether the learner can produce exam-usable answers, not merely recognize terms.

## Items

1. 名词解释：写出一个今日 A 类概念的定义、关键词和常见误区。
2. 简答题：用 3-5 个得分点回答一个今日核心问题。
3. 易混对比：区分两个相近概念，写出差异和例子。

## Scoring

| Result | Meaning | Next action |
|---|---|---|
| 0-40% | Not usable yet | repair |
| 41-59% | Unstable | review |
| 60-74% | Pass-like but fragile | continue with retrieval |
| 75%+ | Stable enough for MVP goal | continue or simulate |

Record the result in `state/score-history.md`.
"""


def run_quality_gate_with_repair(root: Path, input_data: FactoryInput) -> Dict[str, Any]:
    """Run post-generation quality check and one deterministic repair attempt.

    This is intentionally a small ratchet: failing skeletons are not returned as
    if they were ready. Known course seeds can repair the most common MVP gap;
    unknown courses return explicit repair actions for the factory agent.
    """
    attempts: List[Dict[str, Any]] = []

    first = quality_check(root, course_name=input_data.course_name, days_available=input_data.days_available)
    attempts.append({"attempt": 1, "action": "initial_quality_check", "passed": first["passed"], "score": first["score"]})
    if first["passed"]:
        return {"passed": True, "attempts": attempts, "repair_result": None, "final_report": first}

    repair_result = apply_course_seed(root, input_data.course_name, input_data.days_available, input_data.daily_minutes)
    attempts.append({"attempt": 2, "action": "course_seed_repair", "applied": repair_result["applied"], "seed_id": repair_result["seed_id"]})

    second = quality_check(root, course_name=input_data.course_name, days_available=input_data.days_available)
    attempts.append({"attempt": 3, "action": "post_repair_quality_check", "passed": second["passed"], "score": second["score"]})

    return {
        "passed": second["passed"],
        "attempts": attempts,
        "repair_result": repair_result,
        "final_report": second,
    }


def materialize(input_data: FactoryInput, output_root: Path) -> Dict[str, Any]:
    slug = slugify(input_data.course_name)
    root = output_root / slug
    created_files: List[Dict[str, Any]] = []

    if root.exists() and any(root.iterdir()):
        raise FileExistsError(f"output directory already exists and is not empty: {root}")

    dirs = ["plan", "state", "sessions", "learning-records", "quizzes", "final-review"]
    for directory in dirs:
        (root / directory).mkdir(parents=True, exist_ok=True)

    write(root / "index.md", index_content(input_data.course_name, "Course Learning OKF entrypoint.", ["mission.md", "plan/day-1.md", "state/current-state.md"]), created_files)
    write(root / "log.md", "# Log\n\n- Created by `tools/materialize_course_okf.py`.\n", created_files)
    write(root / "mission.md", frontmatter("Mission", "Course Mission", "Normalized mission and assumptions.", ["mission"]) + f"""# Mission

course_name: {input_data.course_name}
baseline: {input_data.baseline}
days_available: {input_data.days_available}
daily_minutes: {input_data.daily_minutes}
target_score: {input_data.target_score}
exam_date: {input_data.exam_date or 'unknown'}
exam_format: {input_data.exam_format}
course_type: {input_data.course_type}

## Assumptions

- Goal is pass-level readiness, not full mastery.
- User-provided materials outrank generic knowledge.
- Missing source evidence must be recorded in `resources.md`.
""", created_files)
    write(root / "course-map.md", frontmatter("Course Map", "Course Map", "Minimal course map to be filled after reconnaissance.", ["course-map"]) + "# Course Map\n\n## A/B/C Topic Outline\n\nFill this from course materials before running Day 1.\n", created_files)
    write(root / "resources.md", frontmatter("Resource Registry", "Resources", "Sources, confidence, and gaps.", ["resources", "provenance"]) + resources_body(input_data), created_files)
    write(root / "priority-map.md", frontmatter("Priority Map", "Priority Map", "A/B/C exam-value classification.", ["priority", "exam"]) + "# Priority Map\n\n## A — Must know\n\n- TBD from resources.\n\n## B — Stabilizers\n\n- TBD from resources.\n\n## C — Short-term low value\n\n- TBD from resources.\n", created_files)
    write(root / "glossary.md", frontmatter("Glossary", "Glossary", "Terms and concise exam definitions.", ["glossary"]) + "# Glossary\n\nAdd high-value definitions here.\n", created_files)

    write(root / "plan/index.md", index_content("Plan", "Daily plan index.", ["seven-day-plan.md"] + [f"day-{day}.md" for day in range(1, input_data.days_available + 1)]), created_files)
    write(root / "plan/seven-day-plan.md", frontmatter("Plan", "Crash-Course Plan", "Configured-day plan for pass-level readiness.", ["plan"]) + seven_day_body(input_data), created_files)
    for day in range(1, input_data.days_available + 1):
        write(root / f"plan/day-{day}.md", daily_plan_content(input_data, day), created_files)

    write(root / "state/index.md", index_content("State", "Canonical learner memory files.", [Path(f).name for f in STATE_FILES]), created_files)
    write(root / "state/current-state.md", state_current_body(input_data), created_files)
    write(root / "state/topic-ledger.md", frontmatter("State", "Topic Ledger", "Per-topic mastery and evidence.", ["state", "topics"]) + "# Topic Ledger\n\n| Topic | Priority | Status | Mastery 0-4 | Evidence | Next review |\n|---|---|---|---:|---|---|\n", created_files)
    write(root / "state/recall-deck.md", frontmatter("State", "Recall Deck", "Active recall cards.", ["state", "recall"]) + "# Recall Deck\n\n| Card ID | Topic | Prompt | Expected answer | Due | Result |\n|---|---|---|---|---|---|\n", created_files)
    write(root / "state/misconceptions.md", frontmatter("State", "Misconceptions", "Open and resolved misconception tracker.", ["state", "misconceptions"]) + "# Misconceptions\n\n| ID | Topic | Error | Severity | Repair task | Status | Retest evidence |\n|---|---|---|---|---|---|---|\n", created_files)
    write(root / "state/score-history.md", frontmatter("State", "Score History", "Assessment events and pass-readiness estimates.", ["state", "scores"]) + "# Score History\n\n| Date | Event | Score | Pass readiness | Risk | Evidence | Next action |\n|---|---|---:|---|---|---|---|\n", created_files)
    write(root / "state/next-action.md", next_action_body(), created_files)
    write(root / "state/plan-changes.md", frontmatter("State", "Plan Changes", "Adaptation log for future daily plans.", ["state", "adaptation"]) + "# Plan Changes\n\n| Date | Trigger evidence | Changed files | Reason |\n|---|---|---|---|\n", created_files)

    write(root / "sessions/index.md", index_content("Sessions", "Session records.", ["day-1-session.md"]), created_files)
    write(root / "sessions/day-1-session.md", session_body(1, pending=True), created_files)
    write(root / "learning-records/index.md", index_content("Learning Records", "Longer learning records and baselines.", ["0001-initial-baseline.md"]), created_files)
    write(root / "learning-records/0001-initial-baseline.md", frontmatter("Learning Record", "Initial Baseline", "Initial baseline before Day 1.", ["baseline", "record"]) + "# Initial Baseline\n\n- Baseline: pending diagnostic.\n- Known constraints: see `mission.md`.\n", created_files)

    write(root / "quizzes/index.md", index_content("Quizzes", "Daily quizzes.", [f"day-{day}-quiz.md" for day in range(1, input_data.days_available + 1)]), created_files)
    for day in range(1, input_data.days_available + 1):
        write(root / f"quizzes/day-{day}-quiz.md", quiz_content(input_data, day), created_files)

    for file_name in FINAL_REVIEW_FILES:
        path = root / file_name
        if path.name == "index.md":
            content = index_content("Final Review", "Compressed review and mock exam.", ["compressed-notes.md", "must-know-list.md", "answer-templates.md", "mock-exam.md"])
        else:
            title = path.stem.replace("-", " ").title()
            content = frontmatter("Final Review", title, "Final review placeholder.", ["final-review"]) + f"# {title}\n\nFill this during the final review playbook.\n"
        write(path, content, created_files)

    for entry in created_files:
        entry_path = Path(entry["path"])
        try:
            entry["path"] = str(entry_path.relative_to(root))
        except ValueError:
            entry["path"] = str(entry_path)

    structural_validation = validate(root, input_data.days_available)
    quality_gate = run_quality_gate_with_repair(root, input_data)

    output = {
        "course_okf_name": input_data.course_name,
        "course_slug": slug,
        "created_files": created_files,
        "initial_state": {
            "current_day": 1,
            "days_remaining": input_data.days_available,
            "completed_sessions": 0,
            "pass_readiness": "very_low",
            "risk_level": "high",
            "next_action": "run_day_1",
        },
        "seven_day_plan": "plan/seven-day-plan.md",
        "day_1_entrypoint": "plan/day-1.md",
        "state_update_rules": STATE_UPDATE_RULES,
        "resume_rules": RESUME_RULES,
        "validation_result": {
            "passed": structural_validation["passed"] and quality_gate["passed"],
            "structural": structural_validation,
            "quality_gate": quality_gate,
        },
    }
    (root / "quality-report.json").write_text(json.dumps(quality_gate["final_report"], ensure_ascii=False, indent=2), encoding="utf-8")
    (root / "generation-output.json").write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")
    return output


def resources_body(input_data: FactoryInput) -> str:
    lines = ["# Resources", "", "## Source Register", "", "| Type | Location | Priority | Confidence | Notes |", "|---|---|---|---|---|"]
    if input_data.materials:
        for item in input_data.materials:
            lines.append(
                "| {type} | {path} | {priority} | {confidence} | {notes} |".format(
                    type=item.get("type", "other"),
                    path=item.get("path_or_url", item.get("path", "unknown")),
                    priority=item.get("priority", "primary"),
                    confidence=item.get("confidence", "unknown"),
                    notes=item.get("notes", ""),
                )
            )
    else:
        lines.append("| none | none | primary | unknown | No user material provided yet. |")
    lines.extend(["", "## Source Gaps", "", "- Confirm teacher emphasis, exam format, and past-question style.", ""])
    return "\n".join(lines)


def seven_day_body(input_data: FactoryInput) -> str:
    lines = ["# Crash-Course Plan", "", f"Configured days: `{input_data.days_available}`", f"Daily minutes: `{input_data.daily_minutes}`", "", "| Day | Main use | State requirement |", "|---:|---|---|"]
    for day in range(1, input_data.days_available + 1):
        if day == input_data.days_available:
            use = "final review, must-know list, answer templates, mock exam"
        elif day == 1:
            use = "baseline, course map, first A-topics"
        else:
            use = "A-topic progress, retrieval, exam practice, repair if needed"
        lines.append(f"| {day} | {use} | update session, score history, recall deck, next action |")
    lines.append("")
    return "\n".join(lines)


def state_current_body(input_data: FactoryInput) -> str:
    return frontmatter("State", "Current State", "Canonical learner position.", ["state", "current"]) + f"""# Current State

```yaml
current_day: 1
days_remaining: {input_data.days_available}
completed_sessions: 0
pass_readiness: very_low
risk_level: high
last_session_date: null
next_action: run_day_1
source_gaps:
  - teacher emphasis unknown unless provided
  - past exam style unknown unless provided
latest_summary: initialized, no learning evidence yet
```
"""


def next_action_body() -> str:
    return frontmatter("State", "Next Action", "Canonical next learning step.", ["state", "next-action"]) + """# Next Action

```yaml
next_action: run_day_1
reason: initialized course OKF; no session has run yet
blocking_items: []
read_before_start:
  - state/current-state.md
  - state/recall-deck.md
  - state/misconceptions.md
  - state/score-history.md
  - sessions/day-1-session.md
  - plan/day-1.md
```
"""


def session_body(day: int, pending: bool = False) -> str:
    status = "pending" if pending else "completed"
    return frontmatter("Session Record", f"Day {day} Session", "Daily session evidence record.", ["session", "evidence"]) + f"""# Day {day} Session

```yaml
day: {day}
status: {status}
started_at: null
completed_at: null
score_estimate: null
next_action: run_day_1
```

## Evidence

- Retrieval:
- Feynman explanation:
- Exam-style answer:
- Misconceptions:
- State updates made:
"""


def required_paths(days_available: int) -> List[str]:
    base = [
        "index.md", "log.md", "mission.md", "course-map.md", "resources.md", "priority-map.md", "glossary.md",
        "plan/index.md", "plan/seven-day-plan.md",
        "state/index.md", "sessions/index.md", "sessions/day-1-session.md",
        "learning-records/index.md", "learning-records/0001-initial-baseline.md",
        "quizzes/index.md",
    ]
    base.extend(f"plan/day-{day}.md" for day in range(1, days_available + 1))
    base.extend(STATE_FILES)
    base.extend(f"quizzes/day-{day}-quiz.md" for day in range(1, days_available + 1))
    base.extend(FINAL_REVIEW_FILES)
    return base


def validate(root: Path, days_available: int) -> Dict[str, Any]:
    missing = [path for path in required_paths(days_available) if not (root / path).exists()]
    warnings: List[str] = []
    source_gaps: List[str] = []
    resources = root / "resources.md"
    if resources.exists() and "Source Gaps" in resources.read_text(encoding="utf-8"):
        source_gaps.append("source gaps recorded in resources.md")
    else:
        warnings.append("resources.md does not include Source Gaps")
    return {
        "passed": not missing,
        "missing_files": missing,
        "warnings": warnings,
        "source_gaps": source_gaps,
    }


def parse_args(argv: Optional[List[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Materialize and quality-check a Course Learning OKF.")
    parser.add_argument("--input-json", type=Path, help="Path to a JSON factory input file.")
    parser.add_argument("--output-dir", type=Path, default=Path.cwd(), help="Directory where the course OKF folder will be created.")
    parser.add_argument("--course-name", help="Course name. Overrides input JSON when provided.")
    parser.add_argument("--baseline", choices=sorted(VALID_BASELINES), help="Learner baseline.")
    parser.add_argument("--days-available", type=int, help="Available study days.")
    parser.add_argument("--daily-minutes", type=int, help="Minutes available per day.")
    parser.add_argument("--target-score", help="Target score or pass target.")
    parser.add_argument("--exam-format", help="Exam format.")
    parser.add_argument("--course-type", help="Course type.")
    parser.add_argument("--materials-available", help="Material availability.")
    return parser.parse_args(argv)


def main(argv: Optional[List[str]] = None) -> int:
    args = parse_args(argv)
    raw = read_input_json(args.input_json)
    overrides = {
        "course_name": args.course_name,
        "baseline": args.baseline,
        "days_available": args.days_available,
        "daily_minutes": args.daily_minutes,
        "target_score": args.target_score,
        "exam_format": args.exam_format,
        "course_type": args.course_type,
        "materials_available": args.materials_available,
    }
    for key, value in overrides.items():
        if value is not None:
            raw[key] = value
    try:
        input_data = normalize(raw)
        output = materialize(input_data, args.output_dir)
    except Exception as exc:  # keep CLI user-friendly
        print(f"error: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(output, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
