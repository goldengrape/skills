# delegate-to-chatgpt-web development

This directory contains the design documents, tests, and development environment for the
`delegate-to-chatgpt-web` Codex skill.

Repository layout:

- Installable skill candidate: `../../delegate-to-chatgpt-web/`
- Authoritative design documents: `docs/`
- Derived project wiki: `wiki/`
- Machine-readable document state: `.vibe/`
- Offline tests: `tests/`

Development commands:

```text
uv run pytest -q
uv run ruff check .
```

Do not run tests marked `live` without explicit user authorization. Live tests upload a fixture
and send a real message through the signed-in ChatGPT Web conversation.
