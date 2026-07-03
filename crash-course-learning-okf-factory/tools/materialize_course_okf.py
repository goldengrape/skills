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
DEFAULT_TIME_POLICY = "soft"

VALID_BASELINES = {"zero", "weak", "partial", "review"}
VALID_NEXT_ACTIONS = {"run_day_1", "continue", "repair", "review", "simulate", "final_review"}
VALID_TIME_POLICIES = {"soft", "strict"}

STATE_FILES = [
    "state/current-state.md",
    "state/topic-ledger.md",
    "state/recall-deck.md",
    "state/misconceptions.md",
    "state/score-history.md",
    "state/next-action.md",
    "state/plan-changes.md",
    "state/interest-ledger.md",
]

FINAL_REVIEW_FILES = [
    "final-review/index.md",
    "final-review/compressed-notes.md",
    "final-review/must-know-list.md",
    "final-review/answer-templates.md",
    "final-review/mock-exam.md",
]

TEACHER_RUNTIME_FILES = [
    "teacher/index.md",
    "teacher/teaching-protocol.md",
    "teacher/visibility-rules.md",
    "teacher/teacher-notebook.md",
    "teacher/engagement-monitor.md",
    "teacher/engagement-intervention-rules.md",
    "teacher/time-policy.md",
    "teacher/visual-teaching-policy.md",
    "teacher/diagram-quality-rules.md",
    "teacher/diagram-source-rules.md",
]

VISUAL_ASSET_FILES = [
    "assets/diagrams/index.md",
]

RESUME_RULES = [
    "read state/current-state.md",
    "read state/next-action.md",
    "read state/recall-deck.md",
    "read state/misconceptions.md",
    "read state/score-history.md",
    "read latest sessions/*.md",
    "read relevant plan/day-N.md",
    "read teacher/teacher-notebook.md without displaying teacher_thinks",
    "read state/interest-ledger.md",
    "read assets/diagrams/index.md when a topic uses diagrams",
]

STATE_UPDATE_RULES = [
    "read state before teaching",
    "create session record after session",
    "append teacher_says and teacher_thinks to teacher/teacher-notebook.md",
    "update score history after assessment with score_type and prompt_visibility",
    "update recall deck for missed or high-value items",
    "update misconceptions for wrong distinctions",
    "record interest-led branches when learner asks deeper questions",
    "record generated or sourced diagrams in assets/diagrams/index.md",
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
    time_policy: str = DEFAULT_TIME_POLICY
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

    time_policy = str(raw.get("time_policy", DEFAULT_TIME_POLICY)).strip() or DEFAULT_TIME_POLICY
    if time_policy not in VALID_TIME_POLICIES:
        raise ValueError(f"time_policy must be one of {sorted(VALID_TIME_POLICIES)}")

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
        time_policy=time_policy,
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
    time_note = "soft planning target" if input_data.time_policy == "soft" else "strict session limit"
    return frontmatter(
        "Daily Work Package",
        f"{input_data.course_name} Day {day}",
        "One crash-course learning session with explicit student-visible tasks.",
        ["plan", "daily", "crash-course"],
    ) + f"""# Day {day}

## Goal

Use this day to advance pass-level readiness for `{input_data.course_name}` while protecting A-priority topics.

## Time Policy

Configured daily minutes: `{input_data.daily_minutes}`.

Current time policy: `{input_data.time_policy}` ({time_note}).

- If `time_policy: soft`, learner questions may continue when they show useful interest or clarify core concepts. Record the branch in `state/interest-ledger.md`.
- If `time_policy: strict`, answer extension questions briefly, record them in `state/interest-ledger.md`, and return to the planned exam path.
- State updates must not be skipped in either mode.

## Suggested Flow

| Minutes | Activity |
|---:|---|
| 0-5 | Due recall cards and previous-session retrieval |
| 5-10 | Today's goal and exam value |
| 10-25 | Core explanation with examples, counterexamples, and contrasts |
| 25-35 | Feynman task by the learner |
| 35-45 | Exam-style question practice |
| 45-55 | Feedback and repair |
| 55-60 | State-update summary |

## Required Evidence

- Feynman explanation result.
- At least one exam-style answer or quiz item.
- Any misconception or weak distinction.
- Any interest-led branch that should influence future examples or review.
- Next action for the following session.

## Teacher Runtime Rule

Before showing a quiz or exam prompt, write the hidden goal, expected answer elements, and scoring rule in `teacher/teacher-notebook.md`. Show the learner only the student prompt. Do not reveal hidden answer elements before the learner answers.

## State Update

After this session, update `sessions/day-{day}-session.md`, `teacher/teacher-notebook.md`, `state/score-history.md`, `state/interest-ledger.md`, `state/recall-deck.md`, `state/misconceptions.md`, and `state/next-action.md`.
"""

def quiz_content(input_data: FactoryInput, day: int) -> str:
    return frontmatter(
        "Quiz",
        f"{input_data.course_name} Day {day} Quiz",
        "Short pass-level quiz for a daily session. Student prompt only; answer keys live under teacher/.",
        ["quiz", "assessment", "student-visible"],
    ) + f"""# Day {day} Quiz

```yaml
visibility: student_prompt
assessment_mode: blind_quiz
score_type_if_unprompted: blind_score
hidden_teacher_files:
  - teacher/rubrics/day-{day}-rubric.md
  - teacher/answer-keys/day-{day}-answer-key.md
```

## Purpose

Check whether the learner can produce exam-usable answers, not merely recognize terms.

## Items

1. 名词解释：写出一个今日核心概念的定义，并补充一个容易混淆的地方。
2. 简答题：回答一个今日核心问题。请按自己的理解作答，先不要看笔记。
3. 易混对比：区分两个相近概念，写出差异和例子。

## After the Learner Answers

The teacher may then show missing points, corrected wording, and a compact reference answer. Record the assessment in `state/score-history.md` with `score_type`, `prompt_visibility`, and whether any hints were shown before the answer.
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


def teacher_index_content(input_data: FactoryInput) -> str:
    return index_content(
        "Teacher Runtime",
        "Private teacher-side runtime files. Show paths to the learner when useful, but do not paste hidden teacher_thinks content into the conversation before assessment.",
        [
            "teaching-protocol.md",
            "visibility-rules.md",
            "teacher-notebook.md",
            "engagement-monitor.md",
            "engagement-intervention-rules.md",
            "time-policy.md",
            "visual-teaching-policy.md",
            "diagram-quality-rules.md",
            "diagram-source-rules.md",
            "rubrics/",
            "answer-keys/",
        ],
    )


def teaching_protocol_content(input_data: FactoryInput) -> str:
    return frontmatter("Teacher Runtime", "Teaching Protocol", "Runtime protocol for student-visible teaching and private teacher notes.", ["teacher", "protocol"]) + f"""# Teaching Protocol

## Core Split

Each teaching turn has two layers:

```yaml
teacher_says:
  - shown to learner
teacher_thinks:
  - private planning, expected answer elements, scoring rule, next intervention
```

Show only `teacher_says` in the conversation before the learner answers. Keep `teacher_thinks` in `teacher/teacher-notebook.md`.

## Assessment Flow

1. Write the task goal and expected answer elements to `teacher/teacher-notebook.md`.
2. Render only the student prompt.
3. Wait for the learner answer.
4. Score the answer and show feedback.
5. Update `state/score-history.md` with score type and prompt visibility.

## Score Types

| score_type | Meaning |
|---|---|
| blind_score | No answer elements or scoring hints were shown before the learner answered. |
| semi_assisted_score | The format was scaffolded, but specific answer elements were hidden. |
| assisted_score | Specific answer elements or substantial hints were shown before the learner answered. |

## Visual Teaching

When a lesson explains curves, axes, graph shifts, equilibrium models, flow diagrams, or spatial structures, use the visual teaching protocol:

1. Prefer generated Python/matplotlib diagrams when available.
2. Use authoritative open-source diagrams for complex images and record source/license.
3. Avoid complex ASCII diagrams.
4. Insert diagrams near the explanation.
5. Record each diagram in `assets/diagrams/index.md`.

## Interest-Led Branches

When the learner asks a deeper question, default to continuing under `time_policy: soft`. Connect the answer back to exam relevance and record the branch in `state/interest-ledger.md`.
"""


def visibility_rules_content(input_data: FactoryInput) -> str:
    return frontmatter("Teacher Runtime", "Visibility Rules", "Rules for separating student-visible prompts from hidden scoring materials.", ["teacher", "visibility"]) + """# Visibility Rules

## Before Learner Answers: Allowed

- The question.
- Time or length limit.
- Output format.
- Whether notes are allowed.
- A neutral reminder to answer from memory.

## Before Learner Answers: Not Allowed

- Expected answer elements.
- Hidden scoring criteria.
- Standard or reference answers.
- Phrases such as “at least mention these points”.
- Teacher internal judgments.

## After Learner Answers: Allowed

- Missing points.
- Corrected wording.
- Compact reference answer.
- Scoring explanation.
- Recall cards and misconception repairs.

## Exception

Guided practice may show scaffolds, but the assessment must then be recorded as `assisted_score` or `semi_assisted_score`, not as `blind_score`.
"""


def teacher_notebook_content(input_data: FactoryInput) -> str:
    return frontmatter("Teacher Notebook", "Teacher Notebook", "Private runtime notebook for teacher-side planning and hidden scoring materials.", ["teacher", "notebook", "private-runtime"]) + f"""# Teacher Notebook

```yaml
course: {input_data.course_name}
visibility: teacher_private_runtime_file
time_policy: {input_data.time_policy}
status: initialized
```

## Append-Only Turn Log

Use this structure for each teaching turn:

```yaml
turn_id: dayN-tXX
phase: explanation | guided_practice | blind_quiz | feedback | interest_branch | state_update
teacher_says:
  - "student-visible message"
teacher_thinks:
  task_goal: "hidden teaching goal"
  expected_answer_elements: []
  do_not_reveal_before_answer: []
  scoring_rule: "hidden until after answer"
engagement_observation:
  interest_level: high | normal | uncertain
  attention_signal: stable | maybe_dropping | unknown
  evidence: []
teaching_decision:
  action: continue_core | continue_branch | offer_choice | short_check | pause_and_summarize
  reason: ""
state_updates: []
```
"""


def engagement_monitor_content() -> str:
    return frontmatter("Teacher Runtime", "Engagement Monitor", "Observable learning signals and cautious engagement interpretation.", ["teacher", "engagement"]) + """# Engagement Monitor

Do not claim to know the learner's inner mental state. Only record observable signals.

## Positive Interest Signals

- Learner asks why or how.
- Learner gives their own example.
- Learner asks for a practice problem.
- Learner says the topic is interesting.
- Learner creates a table, derivation, or analogy.
- Learner answers beyond the minimum requirement.

## Possible Attention-Drop Signals

- Repeated very short answers.
- Repeated “I do not understand” without a specific question.
- Skipping the requested task.
- Repeating the same error after repair.
- Saying they are tired, annoyed, or short on time.

## Response Rule

High interest: continue when useful and connect back to the exam spine.
Possible attention drop: shorten explanation, use a small question, offer a choice, or summarize and pause.
"""


def engagement_intervention_rules_content() -> str:
    return frontmatter("Teacher Runtime", "Engagement Intervention Rules", "Small teaching moves for preserving interest and restoring attention.", ["teacher", "engagement", "intervention"]) + """# Engagement Intervention Rules

## If Interest Is High

- Continue the branch under soft time policy.
- Make the branch exam-relevant if possible.
- Offer one small exercise when the learner asks for depth.
- Record the topic in `state/interest-ledger.md`.

## If Attention May Be Dropping

Use one of these moves without accusing the learner of being inattentive:

- “我们先做一个 30 秒判断题，把这个点钉住。”
- “这里有两条路：继续深入原理，或者先做考试题。你选一个。”
- “我先把这段压成三句话，再继续。”
- “这个点可以暂存，我们先完成今天最低合格输出。”

## Guard

Do not force time limits unless `time_policy: strict` or the learner explicitly asks to keep the session within the configured minutes.
"""


def time_policy_content(input_data: FactoryInput) -> str:
    return frontmatter("Teacher Runtime", "Time Policy", "Soft and strict time policies for crash-course sessions.", ["teacher", "time-policy"]) + f"""# Time Policy

```yaml
default_time_policy: soft
current_time_policy: {input_data.time_policy}
configured_daily_minutes: {input_data.daily_minutes}
```

## Soft Policy

Daily minutes are a planning target. If the learner shows high interest or asks a concept-repair question, continue naturally when it helps learning. Record actual time and extra topics.

## Strict Policy

Daily minutes are a hard limit. Use brief answers for extension questions, record them in `state/interest-ledger.md`, and return to the planned exam path.

## Switching Rule

Use strict mode only when the learner requests it, the exam is imminent, or the input explicitly sets `time_policy: strict`.
"""



def visual_teaching_policy_content() -> str:
    return frontmatter("Teacher Runtime", "Visual Teaching Policy", "Rules for when and how to use diagrams in course teaching.", ["teacher", "visual", "diagram"]) + """# Visual Teaching Policy

## Trigger

If a lesson explains curves, coordinate axes, graph shifts, equilibrium models, geometric relations, flow/process structures, system diagrams, or spatial layouts, use a visual explanation.

## Source Priority

1. **Generate with Python/matplotlib when available.** Use this for stable teaching diagrams such as AD/SRAS/LRAS, supply-demand curves, simple functions, before/after shifts, and simple flow diagrams.
2. **Use authoritative open images when the diagram is complex.** Prefer official institutions, open textbooks, university open courseware, Wikipedia/Wikimedia Commons, or credible open-source tutorials. Record source URL, license, and attribution.
3. **Use ASCII only as a temporary tiny sketch.** Do not rely on ASCII for complex curves, multi-curve models, equilibrium shifts, or mobile-sensitive layouts.

## Teaching Rule

For a new curve or graph, explain:

- horizontal axis and vertical axis;
- why the axes are chosen;
- what each curve means;
- why the slope has that direction;
- movement along the curve vs whole-curve shift;
- old and new equilibrium points when relevant.

## Display Rule

Insert the image near the matching explanation, not only as a detached link. Record every generated or sourced image in `assets/diagrams/index.md`.
"""


def diagram_quality_rules_content() -> str:
    return frontmatter("Teacher Runtime", "Diagram Quality Rules", "Quality checklist for generated or sourced course diagrams.", ["teacher", "diagram", "quality"]) + """# Diagram Quality Rules

A diagram passes only if it is useful for learning and recoverable by later sessions.

## Required Checks

- Diagram exists and is listed in `assets/diagrams/index.md`.
- Axis labels are present when there are axes.
- Variables are explained in nearby text.
- Curves are labeled.
- Shift direction is labeled when shift is taught.
- New and old equilibrium points are labeled when equilibrium is taught.
- Source or generator is recorded.
- Complex curve/model diagrams do not rely on ASCII.

## External Image Checks

- Source URL recorded.
- Source name recorded.
- License or usage status recorded.
- Attribution recorded when required.
"""


def diagram_source_rules_content() -> str:
    return frontmatter("Teacher Runtime", "Diagram Source Rules", "Rules for external diagram lookup and attribution.", ["teacher", "diagram", "source"]) + """# Diagram Source Rules

## Use External Sources When

- The diagram is complex or highly standardized.
- A generated image would be misleading or too hard to verify quickly.
- The learner asks for an authoritative reference.
- The concept benefits from an official or open textbook diagram.

## Source Order

1. Official institutions and international organizations.
2. Open textbooks or university open courseware.
3. Wikipedia / Wikimedia Commons.
4. Credible open-source tutorials.

## Required Record

```yaml
source_type: external
source_name:
source_url:
license:
attribution:
retrieved_date:
local_copy_or_link:
used_in:
```
"""


def diagram_index_content() -> str:
    return frontmatter("Diagram Index", "Diagram Index", "Reusable teaching diagrams for this Course OKF instance.", ["diagram", "visual", "asset"]) + """# Diagram Index

| Diagram ID | File | Topic | Source | Used in | Notes |
|---|---|---|---|---|---|

## Rules

- Add every generated or externally sourced diagram here.
- Use generated diagrams for simple curve/model teaching when possible.
- Use authoritative open images for complex diagrams and record license/attribution.
- Do not use complex ASCII diagrams as formal course assets.
"""

def rubric_content(input_data: FactoryInput, day: int) -> str:
    return frontmatter("Teacher Rubric", f"Day {day} Rubric", "Private rubric for scoring after the learner answers.", ["teacher", "rubric"]) + f"""# Day {day} Rubric

```yaml
visibility: teacher_private
show_before_answer: false
```

## Generic Scoring Rule

- Definition accuracy.
- Correct causal mechanism or distinction.
- Course-specific example.
- Clear exam-ready wording.
- No serious misconception.

## Prompt Visibility Rule

If any specific answer element is shown before the learner answers, record the result as `assisted_score` or `semi_assisted_score`.
"""


def answer_key_content(input_data: FactoryInput, day: int) -> str:
    return frontmatter("Teacher Answer Key", f"Day {day} Answer Key", "Private answer key to use only after learner response.", ["teacher", "answer-key"]) + f"""# Day {day} Answer Key

```yaml
visibility: teacher_private
show_before_answer: false
```

Use this file to store compact reference answers after course-specific content is known. Do not paste this section into the conversation before the learner answers.
"""


def interest_ledger_body(input_data: FactoryInput) -> str:
    return frontmatter("State", "Interest Ledger", "Learner-led questions and interest branches that may shape future teaching.", ["state", "interest"]) + """# Interest Ledger

| Date | Branch ID | Trigger | Topic | Relation to exam | Interest evidence | Teacher decision | Time policy | Impact on plan |
|---|---|---|---|---|---|---|---|---|

## Rules

- Default: learner-led questions are valuable learning evidence, not a problem.
- In soft mode, continue when the branch clarifies concepts or sustains interest.
- In strict mode, answer briefly and return to the planned path.
"""


def materialize(input_data: FactoryInput, output_root: Path) -> Dict[str, Any]:
    slug = slugify(input_data.course_name)
    root = output_root / slug
    created_files: List[Dict[str, Any]] = []

    if root.exists() and any(root.iterdir()):
        raise FileExistsError(f"output directory already exists and is not empty: {root}")

    dirs = ["plan", "state", "sessions", "learning-records", "quizzes", "final-review", "teacher", "teacher/rubrics", "teacher/answer-keys", "assets", "assets/diagrams", "assets/diagrams/external"]
    for directory in dirs:
        (root / directory).mkdir(parents=True, exist_ok=True)

    write(root / "index.md", index_content(input_data.course_name, "Course Learning OKF entrypoint.", ["mission.md", "plan/day-1.md", "state/current-state.md"]), created_files)
    write(root / "log.md", "# Log\n\n- Created by `tools/materialize_course_okf.py`.\n", created_files)
    write(root / "mission.md", frontmatter("Mission", "Course Mission", "Normalized mission and assumptions.", ["mission"]) + f"""# Mission

course_name: {input_data.course_name}
baseline: {input_data.baseline}
days_available: {input_data.days_available}
daily_minutes: {input_data.daily_minutes}
time_policy: {input_data.time_policy}
target_score: {input_data.target_score}
exam_date: {input_data.exam_date or 'unknown'}
exam_format: {input_data.exam_format}
course_type: {input_data.course_type}

## Assumptions

- Goal is pass-level readiness, not full mastery.
- Daily minutes are a soft planning target unless `time_policy: strict`.
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
    write(root / "state/score-history.md", frontmatter("State", "Score History", "Assessment events and pass-readiness estimates.", ["state", "scores"]) + "# Score History\n\n| Date | Event | Score | Score type | Prompt visibility | Pass readiness | Risk | Evidence | Next action |\n|---|---|---:|---|---|---|---|---|---|\n", created_files)
    write(root / "state/next-action.md", next_action_body(), created_files)
    write(root / "state/plan-changes.md", frontmatter("State", "Plan Changes", "Adaptation log for future daily plans.", ["state", "adaptation"]) + "# Plan Changes\n\n| Date | Trigger evidence | Changed files | Reason |\n|---|---|---|---|\n", created_files)
    write(root / "state/interest-ledger.md", interest_ledger_body(input_data), created_files)

    write(root / "teacher/index.md", teacher_index_content(input_data), created_files)
    write(root / "teacher/teaching-protocol.md", teaching_protocol_content(input_data), created_files)
    write(root / "teacher/visibility-rules.md", visibility_rules_content(input_data), created_files)
    write(root / "teacher/teacher-notebook.md", teacher_notebook_content(input_data), created_files)
    write(root / "teacher/engagement-monitor.md", engagement_monitor_content(), created_files)
    write(root / "teacher/engagement-intervention-rules.md", engagement_intervention_rules_content(), created_files)
    write(root / "teacher/time-policy.md", time_policy_content(input_data), created_files)
    write(root / "teacher/visual-teaching-policy.md", visual_teaching_policy_content(), created_files)
    write(root / "teacher/diagram-quality-rules.md", diagram_quality_rules_content(), created_files)
    write(root / "teacher/diagram-source-rules.md", diagram_source_rules_content(), created_files)
    write(root / "assets/diagrams/index.md", diagram_index_content(), created_files)
    for day in range(1, input_data.days_available + 1):
        write(root / f"teacher/rubrics/day-{day}-rubric.md", rubric_content(input_data, day), created_files)
        write(root / f"teacher/answer-keys/day-{day}-answer-key.md", answer_key_content(input_data, day), created_files)

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
            "time_policy": input_data.time_policy,
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
time_policy: {input_data.time_policy}
last_session_date: null
next_action: run_day_1
interest_profile:
  high_interest_topics: []
  possible_attention_drop_signals: []
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
  - state/interest-ledger.md
  - sessions/day-1-session.md
  - teacher/teacher-notebook.md
  - teacher/visual-teaching-policy.md
  - assets/diagrams/index.md
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
- Interest-led branches:
- Teacher notebook entries:
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
    base.extend(TEACHER_RUNTIME_FILES)
    base.extend(VISUAL_ASSET_FILES)
    base.extend(f"teacher/rubrics/day-{day}-rubric.md" for day in range(1, days_available + 1))
    base.extend(f"teacher/answer-keys/day-{day}-answer-key.md" for day in range(1, days_available + 1))
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
    parser.add_argument("--time-policy", choices=sorted(VALID_TIME_POLICIES), help="soft allows interest-led extensions; strict treats daily minutes as a hard limit.")
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
        "time_policy": args.time_policy,
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
