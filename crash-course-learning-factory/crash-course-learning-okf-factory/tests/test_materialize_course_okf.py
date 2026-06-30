from pathlib import Path
import json

from tools.materialize_course_okf import normalize, materialize, required_paths, slugify
from tools.quality_check_course_okf import quality_check


def test_slugify_falls_back_for_non_ascii_course_name():
    slug = slugify("管理学")
    assert slug.startswith("course-okf-course-")
    assert slug.endswith("-pass")


def test_materialize_default_seven_day_layout(tmp_path: Path):
    factory_input = normalize({"course_name": "Management", "baseline": "zero"})
    output = materialize(factory_input, tmp_path)
    root = tmp_path / output["course_slug"]

    assert output["validation_result"]["passed"] is True
    assert output["validation_result"]["structural"]["passed"] is True
    assert output["validation_result"]["quality_gate"]["passed"] is True
    assert (root / "state/current-state.md").exists()
    assert (root / "state/next-action.md").exists()
    assert (root / "plan/day-7.md").exists()
    assert (root / "quizzes/day-7-quiz.md").exists()
    assert (root / "final-review/mock-exam.md").exists()
    assert (root / "quality-report.json").exists()
    assert (root / "generation-output.json").exists()

    saved = json.loads((root / "generation-output.json").read_text(encoding="utf-8"))
    assert saved["initial_state"]["next_action"] == "run_day_1"
    assert "read state/current-state.md" in saved["resume_rules"]


def test_materialize_variable_day_layout(tmp_path: Path):
    factory_input = normalize({"course_name": "Macro Economics", "days_available": 3, "daily_minutes": 60})
    output = materialize(factory_input, tmp_path)
    root = tmp_path / output["course_slug"]

    assert output["validation_result"]["passed"] is True
    assert (root / "plan/day-3.md").exists()
    assert not (root / "plan/day-4.md").exists()
    assert (root / "quizzes/day-3-quiz.md").exists()
    assert not (root / "quizzes/day-4-quiz.md").exists()

    for path in required_paths(3):
        assert (root / path).exists(), path


def test_macroeconomics_quality_gate_repairs_generic_skeleton(tmp_path: Path):
    factory_input = normalize({"course_name": "宏观经济学", "baseline": "zero", "days_available": 7, "daily_minutes": 60})
    output = materialize(factory_input, tmp_path)
    root = tmp_path / output["course_slug"]
    report = quality_check(root, course_name="宏观经济学", days_available=7)

    assert output["validation_result"]["quality_gate"]["repair_result"]["applied"] is True
    assert output["validation_result"]["quality_gate"]["repair_result"]["seed_id"] == "macroeconomics-v1"
    assert report["passed"] is True
    assert report["score"] >= 75

    combined = "\n".join((root / p).read_text(encoding="utf-8") for p in ["course-map.md", "priority-map.md", "plan/day-1.md", "quizzes/day-1-quiz.md", "final-review/mock-exam.md"])
    for term in ["GDP", "inflation", "unemployment", "aggregate demand", "fiscal policy", "monetary policy"]:
        assert term.lower() in combined.lower()
    assert "Fill this" not in combined
    assert "TBD" not in combined


def test_unknown_course_quality_gate_fails_with_repair_actions(tmp_path: Path):
    factory_input = normalize({"course_name": "Imaginary Concept Studies", "baseline": "zero"})
    output = materialize(factory_input, tmp_path)
    root = tmp_path / output["course_slug"]
    report = output["validation_result"]["quality_gate"]["final_report"]

    assert output["validation_result"]["structural"]["passed"] is True
    assert output["validation_result"]["passed"] is False
    assert report["passed"] is False
    assert report["repair_actions"]
    assert any("course term bank" in action or "Rewrite" in action for action in report["repair_actions"])
