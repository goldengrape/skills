# SETUP — Confirmed Repository Layout

## Metadata

- document_id: SETUP-0001
- decision_id: DEC-005
- status: confirmed
- source_ids: URD-Q-006, RMD-SETUP-003–005, RMD-TASK-001
- confirmed_by: user
- confirmed_at: 2026-08-02

## Decision

For this repository, the following confirmed layout replaces the generic project layout example
in RMD-0001:

```text
C:\Users\golde\code\skills\
├── delegate-to-chatgpt-web\
│   ├── SKILL.md
│   ├── agents\openai.yaml
│   ├── scripts\
│   └── references\
└── development\delegate-to-chatgpt-web\
    ├── pyproject.toml
    ├── uv.lock
    ├── tests\
    ├── docs\
    ├── wiki\
    └── .vibe\
```

`delegate-to-chatgpt-web\` is the lean installable candidate. Design documents, tests, and
development-only files stay under `development\delegate-to-chatgpt-web\` and are not copied into
an active Codex installation.

The repository root is the operational working directory. Commands that target the uv project
use `development\delegate-to-chatgpt-web` as their working directory.

## Installation boundary

The candidate exists in the user-specified skills repository. Copying it into the active
`$CODEX_HOME/skills` directory is deferred until RMD-TASK-011 passes and the user confirms that
final installation location.
