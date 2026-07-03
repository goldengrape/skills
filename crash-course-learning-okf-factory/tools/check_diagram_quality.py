#!/usr/bin/env python3
"""Visual teaching quality gate for generated Course OKF instances."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any, Dict, List, Optional

REQUIRED_VISUAL_RUNTIME_FILES = [
    "teacher/visual-teaching-policy.md",
    "teacher/diagram-quality-rules.md",
    "assets/diagrams/index.md",
]

COMPLEX_ASCII_HINTS = [
    r"```text[\s\S]{0,300}(AD|SRAS|LRAS|curve|曲线)[\s\S]{0,300}[\\/|_]{4,}",
    r"价格水平[\s\S]{0,300}真实产出[\s\S]{0,300}[\\/|_]{4,}",
]

CURVE_PATTERNS = [
    r"\bAD\b",
    r"\bSRAS\b",
    r"\bLRAS\b",
    r"aggregate demand",
    r"aggregate supply",
    r"曲线",
    r"总需求",
    r"总供给",
    r"产出缺口",
    r"output gap",
]


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.exists() else ""


def _student_files(root: Path) -> List[Path]:
    files: List[Path] = []
    for pattern in ["plan/day-*.md", "quizzes/day-*-quiz.md", "learning-records/*.md"]:
        files.extend(root.glob(pattern))
    return sorted(set(files))


def _detect_curve_lessons(root: Path) -> bool:
    text = "\n".join(_read(path) for path in _student_files(root))
    return any(re.search(pattern, text, flags=re.IGNORECASE) for pattern in CURVE_PATTERNS)


def check_diagram_quality(root: Path) -> Dict[str, Any]:
    root = root.resolve()
    failures: List[Dict[str, str]] = []
    warnings: List[Dict[str, str]] = []

    missing = [path for path in REQUIRED_VISUAL_RUNTIME_FILES if not (root / path).exists()]
    for path in missing:
        failures.append({"code": "missing_visual_runtime_file", "path": path, "message": f"Missing visual teaching file: {path}"})

    policy = _read(root / "teacher/visual-teaching-policy.md")
    quality_rules = _read(root / "teacher/diagram-quality-rules.md")
    index = _read(root / "assets/diagrams/index.md")

    if "matplotlib" not in policy.lower() and "python" not in policy.lower():
        failures.append({"code": "visual_policy_missing_generated_priority", "path": "teacher/visual-teaching-policy.md", "message": "Visual policy must prefer Python/matplotlib when available."})
    if "authoritative" not in policy.lower() and "权威" not in policy:
        failures.append({"code": "visual_policy_missing_external_source_rule", "path": "teacher/visual-teaching-policy.md", "message": "Visual policy must allow authoritative external/open-source diagrams for complex images."})
    if "ASCII" not in policy and "ascii" not in policy.lower():
        failures.append({"code": "visual_policy_missing_ascii_limit", "path": "teacher/visual-teaching-policy.md", "message": "Visual policy must restrict ASCII diagrams."})
    if "axis" not in quality_rules.lower() and "坐标轴" not in quality_rules:
        failures.append({"code": "diagram_quality_missing_axis_check", "path": "teacher/diagram-quality-rules.md", "message": "Diagram quality rules must check axes."})
    if "| Diagram ID |" not in index:
        failures.append({"code": "diagram_index_schema_missing", "path": "assets/diagrams/index.md", "message": "Diagram index must use the required table schema."})

    curve_lessons_detected = _detect_curve_lessons(root)
    pngs = sorted((root / "assets/diagrams").glob("*.png")) if (root / "assets/diagrams").exists() else []
    if curve_lessons_detected and not pngs:
        failures.append({"code": "curve_lesson_without_diagram_asset", "path": "assets/diagrams", "message": "Curve/model lessons were detected but no generated or sourced diagram assets exist."})

    for path in _student_files(root):
        rel = str(path.relative_to(root))
        text = _read(path)
        for pattern in COMPLEX_ASCII_HINTS:
            if re.search(pattern, text, flags=re.IGNORECASE):
                failures.append({"code": "complex_ascii_diagram_detected", "path": rel, "message": "Complex curve/model explanation appears to rely on ASCII art."})

    indexed_png_count = 0
    for png in pngs:
        rel = png.relative_to(root).as_posix()
        if rel in index or png.name in index:
            indexed_png_count += 1
        else:
            failures.append({"code": "diagram_asset_not_indexed", "path": rel, "message": "Diagram PNG exists but is not listed in assets/diagrams/index.md."})

    if not curve_lessons_detected and not pngs:
        warnings.append({"code": "no_visual_triggers_detected", "path": "course_okf_root", "message": "No curve/model visual trigger detected; diagrams are optional for this instance."})

    return {
        "passed": not failures,
        "curve_lessons_detected": curve_lessons_detected,
        "diagram_assets_found": [str(path.relative_to(root)) for path in pngs],
        "indexed_png_count": indexed_png_count,
        "failures": failures,
        "warnings": warnings,
        "quality_dimensions": {
            "visual_policy": "checked",
            "diagram_index": "checked",
            "diagram_assets": "checked",
            "ascii_complex_graphs": "checked",
        },
    }


def parse_args(argv: Optional[List[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check generated Course OKF diagram and visual-teaching quality.")
    parser.add_argument("course_okf_dir", type=Path)
    parser.add_argument("--output-json", type=Path)
    return parser.parse_args(argv)


def main(argv: Optional[List[str]] = None) -> int:
    args = parse_args(argv)
    report = check_diagram_quality(args.course_okf_dir)
    text = json.dumps(report, ensure_ascii=False, indent=2)
    if args.output_json:
        args.output_json.parent.mkdir(parents=True, exist_ok=True)
        args.output_json.write_text(text, encoding="utf-8")
    print(text)
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
