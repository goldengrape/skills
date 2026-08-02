from pathlib import Path

REPOSITORY_ROOT = Path(__file__).resolve().parents[3]
SKILL_ROOT = REPOSITORY_ROOT / "delegate-to-chatgpt-web"


def test_skill_skeleton_exists() -> None:
    assert (SKILL_ROOT / "SKILL.md").is_file()
    assert (SKILL_ROOT / "agents" / "openai.yaml").is_file()
