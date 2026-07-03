#!/usr/bin/env python3
"""Render small reusable teaching diagrams for generated Course OKF instances.

The tool intentionally covers only stable MVP diagram templates. More complex
figures should be sourced from authoritative open materials and recorded in the
diagram index rather than improvised.
"""
from __future__ import annotations

import argparse
from pathlib import Path
from typing import Dict, Iterable, List, Tuple


def _ensure_matplotlib():
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    return plt


def _setup_axes(ax, title: str) -> None:
    ax.set_title(title)
    ax.set_xlabel("Real output Y")
    ax.set_ylabel("Price level P")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(True, alpha=0.2)


def _line(ax, xs: Iterable[float], ys: Iterable[float], label: str, linestyle: str = "-") -> None:
    ax.plot(list(xs), list(ys), linestyle=linestyle, linewidth=2, label=label)


def render_ad_curve(path: Path) -> None:
    plt = _ensure_matplotlib()
    fig, ax = plt.subplots(figsize=(6, 4), dpi=160)
    _setup_axes(ax, "AD curve and shifts")
    xs = [1, 9]
    _line(ax, xs, [8, 2], "AD₀")
    _line(ax, xs, [6.8, 0.8], "AD left", "--")
    _line(ax, xs, [9.2, 3.2], "AD right", "--")
    ax.annotate("left shift", xy=(3.1, 4.2), xytext=(2.0, 5.1), arrowprops={"arrowstyle": "->"})
    ax.annotate("right shift", xy=(7.0, 5.2), xytext=(6.1, 6.4), arrowprops={"arrowstyle": "->"})
    ax.legend(loc="upper right")
    fig.tight_layout()
    fig.savefig(path)
    plt.close(fig)


def render_sras_curve(path: Path) -> None:
    plt = _ensure_matplotlib()
    fig, ax = plt.subplots(figsize=(6, 4), dpi=160)
    _setup_axes(ax, "SRAS curve and shifts")
    xs = [1, 9]
    _line(ax, xs, [2, 8], "SRAS₀")
    _line(ax, xs, [3.4, 9.4], "SRAS left/up", "--")
    _line(ax, xs, [0.6, 6.6], "SRAS right/down", "--")
    ax.annotate("costs rise", xy=(4.1, 5.7), xytext=(2.4, 7.3), arrowprops={"arrowstyle": "->"})
    ax.annotate("costs fall", xy=(6.1, 4.4), xytext=(6.8, 2.6), arrowprops={"arrowstyle": "->"})
    ax.legend(loc="upper left")
    fig.tight_layout()
    fig.savefig(path)
    plt.close(fig)


def render_lras_curve(path: Path) -> None:
    plt = _ensure_matplotlib()
    fig, ax = plt.subplots(figsize=(6, 4), dpi=160)
    _setup_axes(ax, "LRAS and potential output")
    ax.axvline(5, linewidth=2, label="LRAS₀ / Y*")
    ax.axvline(3.5, linewidth=2, linestyle="--", label="LRAS left")
    ax.axvline(6.5, linewidth=2, linestyle="--", label="LRAS right")
    ax.annotate("Y* falls", xy=(3.5, 6.8), xytext=(2.0, 8.0), arrowprops={"arrowstyle": "->"})
    ax.annotate("Y* rises", xy=(6.5, 6.8), xytext=(7.0, 8.0), arrowprops={"arrowstyle": "->"})
    ax.legend(loc="upper right")
    fig.tight_layout()
    fig.savefig(path)
    plt.close(fig)


def render_ad_sras_equilibrium(path: Path) -> None:
    plt = _ensure_matplotlib()
    fig, ax = plt.subplots(figsize=(6, 4), dpi=160)
    _setup_axes(ax, "AD-SRAS short-run equilibrium")
    xs = [1, 9]
    _line(ax, xs, [8, 2], "AD")
    _line(ax, xs, [2, 8], "SRAS")
    ax.scatter([5], [5])
    ax.annotate("E₀", xy=(5, 5), xytext=(5.3, 5.4))
    ax.axvline(5, linestyle=":", linewidth=1)
    ax.axhline(5, linestyle=":", linewidth=1)
    ax.text(5.1, 0.3, "Y₀")
    ax.text(0.25, 5.1, "P₀")
    ax.legend(loc="upper right")
    fig.tight_layout()
    fig.savefig(path)
    plt.close(fig)


def render_four_shocks(path: Path) -> None:
    plt = _ensure_matplotlib()
    fig, axes = plt.subplots(2, 2, figsize=(9, 7), dpi=150)
    cases = [
        ("AD left: Y↓ P↓", [8, 2], [6.8, 0.8], [2, 8], "AD₀", "AD₁"),
        ("AD right: Y↑ P↑", [8, 2], [9.2, 3.2], [2, 8], "AD₀", "AD₂"),
        ("SRAS left: Y↓ P↑", [8, 2], [8, 2], [3.4, 9.4], "AD", "SRAS₁"),
        ("SRAS right: Y↑ P↓", [8, 2], [8, 2], [0.6, 6.6], "AD", "SRAS₂"),
    ]
    for ax, (title, ad0, ad1, sras, label0, label1) in zip(axes.flat, cases):
        _setup_axes(ax, title)
        xs = [1, 9]
        if "AD" in title and ("left" in title or "right" in title):
            _line(ax, xs, ad0, "AD₀")
            _line(ax, xs, ad1, label1, "--")
            _line(ax, xs, [2, 8], "SRAS")
        else:
            _line(ax, xs, ad0, "AD")
            _line(ax, xs, [2, 8], "SRAS₀")
            _line(ax, xs, sras, label1, "--")
        ax.legend(fontsize=8, loc="upper right")
    fig.tight_layout()
    fig.savefig(path)
    plt.close(fig)


def render_output_gaps(path: Path) -> None:
    plt = _ensure_matplotlib()
    fig, axes = plt.subplots(1, 2, figsize=(9, 4), dpi=150)
    for ax, title, ad_y, gap_label in [
        (axes[0], "Recessionary gap: Y < Y*", [7, 1], "Y < Y*"),
        (axes[1], "Expansionary gap: Y > Y*", [9, 3], "Y > Y*"),
    ]:
        _setup_axes(ax, title)
        xs = [1, 9]
        _line(ax, xs, ad_y, "AD")
        _line(ax, xs, [2, 8], "SRAS")
        ax.axvline(5, linewidth=2, label="LRAS / Y*")
        ax.text(1.2 if "<" in gap_label else 6.3, 1.2, gap_label)
        ax.legend(fontsize=8, loc="upper right")
    fig.tight_layout()
    fig.savefig(path)
    plt.close(fig)


def render_policy_gap(path: Path) -> None:
    plt = _ensure_matplotlib()
    fig, axes = plt.subplots(1, 2, figsize=(9, 4), dpi=150)
    for ax, title, ad0, ad1 in [
        (axes[0], "Expansionary policy closes recessionary gap", [7, 1], [8, 2]),
        (axes[1], "Contractionary policy cools overheating", [9, 3], [8, 2]),
    ]:
        _setup_axes(ax, title)
        xs = [1, 9]
        _line(ax, xs, ad0, "AD₀")
        _line(ax, xs, ad1, "AD policy", "--")
        _line(ax, xs, [2, 8], "SRAS")
        ax.axvline(5, linewidth=2, label="LRAS / Y*")
        ax.legend(fontsize=8, loc="upper right")
    fig.tight_layout()
    fig.savefig(path)
    plt.close(fig)


RENDERERS = {
    "ad_curve": render_ad_curve,
    "sras_curve": render_sras_curve,
    "lras_curve": render_lras_curve,
    "ad_sras_equilibrium": render_ad_sras_equilibrium,
    "ad_sras_four_shocks": render_four_shocks,
    "output_gaps": render_output_gaps,
    "policy_closing_output_gaps": render_policy_gap,
}

METADATA: Dict[str, Dict[str, str]] = {
    "ad_curve": {"title": "AD curve and shifts", "topic": "aggregate demand", "notes": "Axes, downward slope, left and right shifts."},
    "sras_curve": {"title": "SRAS curve and shifts", "topic": "short-run aggregate supply", "notes": "Cost shocks and short-run supply shifts."},
    "lras_curve": {"title": "LRAS and potential output", "topic": "long-run aggregate supply", "notes": "Potential output and LRAS left/right shifts."},
    "ad_sras_equilibrium": {"title": "AD-SRAS short-run equilibrium", "topic": "short-run equilibrium", "notes": "AD and SRAS intersection determines Y and P."},
    "ad_sras_four_shocks": {"title": "Four AD-SRAS short-run shocks", "topic": "AD-AS short-run shocks", "notes": "AD left/right and SRAS left/right baseline outcomes."},
    "output_gaps": {"title": "Recessionary and expansionary gaps", "topic": "output gaps", "notes": "Y relative to potential output Y*."},
    "policy_closing_output_gaps": {"title": "Policy closing output gaps", "topic": "policy response", "notes": "Expansionary and contractionary policy as AD shifts."},
}


def render(diagram: str, output_dir: Path, prefix: str = "") -> Path:
    if diagram not in RENDERERS:
        raise ValueError(f"unknown diagram {diagram!r}; expected one of {sorted(RENDERERS)}")
    output_dir.mkdir(parents=True, exist_ok=True)
    stem = f"{prefix}{diagram}".replace("_", "-")
    path = output_dir / f"{stem}.png"
    RENDERERS[diagram](path)
    return path


def render_many(diagrams: Iterable[str], output_dir: Path, prefix: str = "") -> List[Path]:
    return [render(diagram, output_dir, prefix=prefix) for diagram in diagrams]


def write_index(output_dir: Path, course_root: Path, rows: List[Tuple[str, Path, str, str, str]]) -> None:
    index = output_dir / "index.md"
    lines = [
        "---",
        "type: Diagram Index",
        "title: Diagram Index",
        "description: Reusable teaching diagrams for this Course OKF instance.",
        "tags: [diagram, visual, asset]",
        "---",
        "",
        "# Diagram Index",
        "",
        "| Diagram ID | File | Topic | Source | Used in | Notes |",
        "|---|---|---|---|---|---|",
    ]
    for diagram_id, file_path, topic, used_in, notes in rows:
        rel = file_path.relative_to(course_root).as_posix()
        lines.append(f"| {diagram_id} | `{rel}` | {topic} | generated: python/matplotlib | {used_in} | {notes} |")
    lines.append("")
    index.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Render reusable Course OKF teaching diagrams.")
    parser.add_argument("--diagram", choices=sorted(RENDERERS), action="append", required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--prefix", default="")
    parser.add_argument("--write-index", action="store_true")
    parser.add_argument("--course-root", type=Path, help="Course root for relative index paths.")
    parser.add_argument("--used-in", default="plan/day-3.md")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    paths = render_many(args.diagram, args.output_dir, prefix=args.prefix)
    if args.write_index:
        course_root = args.course_root or args.output_dir.parent.parent
        rows = []
        for diagram, path in zip(args.diagram, paths):
            meta = METADATA[diagram]
            diagram_id = path.stem
            rows.append((diagram_id, path, meta["topic"], args.used_in, meta["notes"]))
        write_index(args.output_dir, course_root, rows)
    for path in paths:
        print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
