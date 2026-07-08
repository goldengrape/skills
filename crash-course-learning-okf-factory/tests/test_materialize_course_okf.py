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


def test_teaching_runtime_layer_and_soft_time_policy(tmp_path: Path):
    factory_input = normalize({"course_name": "Macroeconomics", "baseline": "zero", "time_policy": "soft"})
    output = materialize(factory_input, tmp_path)
    root = tmp_path / output["course_slug"]

    assert output["initial_state"]["time_policy"] == "soft"
    assert output["validation_result"]["quality_gate"]["final_report"]["teaching_runtime_quality"]["passed"] is True
    assert (root / "teacher/teacher-notebook.md").exists()
    assert (root / "teacher/visibility-rules.md").exists()
    assert (root / "teacher/engagement-monitor.md").exists()
    assert (root / "teacher/time-policy.md").exists()
    assert (root / "state/interest-ledger.md").exists()

    day1_prompt = (root / "quizzes/day-1-quiz.md").read_text(encoding="utf-8")
    assert "至少提到" not in day1_prompt
    assert "答案要点" not in day1_prompt
    assert "teacher_thinks" not in day1_prompt

    notebook = (root / "teacher/teacher-notebook.md").read_text(encoding="utf-8")
    assert "teacher_says" in notebook
    assert "teacher_thinks" in notebook


def test_strict_time_policy_is_recorded(tmp_path: Path):
    factory_input = normalize({"course_name": "Management", "baseline": "zero", "time_policy": "strict"})
    output = materialize(factory_input, tmp_path)
    root = tmp_path / output["course_slug"]

    assert output["initial_state"]["time_policy"] == "strict"
    mission = (root / "mission.md").read_text(encoding="utf-8")
    time_policy = (root / "teacher/time-policy.md").read_text(encoding="utf-8")
    assert "time_policy: strict" in mission
    assert "current_time_policy: strict" in time_policy

from tools.check_diagram_quality import check_diagram_quality
from tools.render_diagram_asset import render


def test_visual_teaching_layer_exists_for_generated_courses(tmp_path: Path):
    factory_input = normalize({"course_name": "Management", "baseline": "zero"})
    output = materialize(factory_input, tmp_path)
    root = tmp_path / output["course_slug"]

    assert (root / "teacher/visual-teaching-policy.md").exists()
    assert (root / "teacher/diagram-quality-rules.md").exists()
    assert (root / "teacher/diagram-source-rules.md").exists()
    assert (root / "assets/diagrams/index.md").exists()

    report = output["validation_result"]["quality_gate"]["final_report"]
    assert report["visual_teaching_quality"]["passed"] is True


def test_macroeconomics_seed_generates_reusable_diagram_assets(tmp_path: Path):
    factory_input = normalize({"course_name": "宏观经济学", "baseline": "zero", "days_available": 7})
    output = materialize(factory_input, tmp_path)
    root = tmp_path / output["course_slug"]

    diagram_dir = root / "assets/diagrams"
    assert (diagram_dir / "index.md").exists()
    expected = [
        "day3-ad-curve.png",
        "day3-sras-curve.png",
        "day3-lras-curve.png",
        "day3-ad-sras-four-shocks.png",
        "day3-output-gaps.png",
    ]
    for filename in expected:
        assert (diagram_dir / filename).exists(), filename
        assert (diagram_dir / filename).stat().st_size > 1000

    visual = check_diagram_quality(root)
    assert visual["passed"] is True
    assert visual["curve_lessons_detected"] is True
    assert len(visual["diagram_assets_found"]) >= 5


def test_visual_quality_gate_detects_complex_ascii_curve(tmp_path: Path):
    factory_input = normalize({"course_name": "Management", "baseline": "zero"})
    output = materialize(factory_input, tmp_path)
    root = tmp_path / output["course_slug"]
    (root / "plan/day-1.md").write_text(
        "# Day 1\n\n价格水平 P\n```text\nP |   / SRAS\n  |  /\n  | /____ 真实产出 Y\n```\n", encoding="utf-8"
    )
    visual = check_diagram_quality(root)
    assert visual["passed"] is False
    assert any(f["code"] == "complex_ascii_diagram_detected" for f in visual["failures"])


def test_render_diagram_asset_writes_png(tmp_path: Path):
    path = render("ad_sras_four_shocks", tmp_path)
    assert path.exists()
    assert path.suffix == ".png"
    assert path.stat().st_size > 1000

from tools.check_learning_stage_evidence import check_learning_stage_evidence


def test_learning_contract_defaults_to_l6_and_quality_gate_passes(tmp_path: Path):
    factory_input = normalize({"course_name": "Management", "baseline": "zero"})
    output = materialize(factory_input, tmp_path)
    root = tmp_path / output["course_slug"]

    assert output["initial_state"]["target_learning_level"] == "L6"
    assert (root / "learning-contract/index.md").exists()
    assert (root / "teacher/learning-control-policy.md").exists()
    assert (root / "state/concept-mastery-state.md").exists()
    assert (root / "state/assessment-evidence-ledger.md").exists()
    assert not (root / "teacher/ai-diet-policy.md").exists()

    report = output["validation_result"]["quality_gate"]["final_report"]
    assert report["learning_control_quality"]["passed"] is True
    assert report["learning_control_quality"]["default_core_target"] == "L6"


def test_target_learning_level_override_is_recorded(tmp_path: Path):
    factory_input = normalize({"course_name": "Management", "baseline": "zero", "target_learning_level": "L7"})
    output = materialize(factory_input, tmp_path)
    root = tmp_path / output["course_slug"]

    assert output["initial_state"]["target_learning_level"] == "L7"
    contract = (root / "learning-contract/index.md").read_text(encoding="utf-8")
    concept_state = (root / "state/concept-mastery-state.md").read_text(encoding="utf-8")
    assert "target_learning_level: L7" in contract
    assert "default_target_level: L7" in concept_state


def test_learning_stage_quality_detects_missing_contract(tmp_path: Path):
    factory_input = normalize({"course_name": "Management", "baseline": "zero"})
    output = materialize(factory_input, tmp_path)
    root = tmp_path / output["course_slug"]
    (root / "learning-contract/index.md").unlink()

    report = check_learning_stage_evidence(root)
    assert report["passed"] is False
    assert any(f["code"] == "missing_learning_control_file" for f in report["failures"])
