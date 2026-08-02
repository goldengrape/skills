---
name: delegate-to-chatgpt-web
description: Delegate bounded tasks to a signed-in ChatGPT Web conversation by exchanging authorized local files as ZIP archives. Use when the user explicitly asks Codex to send a task or files through the in-app Browser and retrieve a result ZIP; do not use for API calls, credential handling, or unapproved uploads.
---

# Delegate to ChatGPT Web

## Development status

This source directory is a valid RMD-TASK-001 skeleton, not a release candidate. Follow the
authoritative development documents and tests before installing it into the active Codex skills
directory.

## Intended workflow

1. Validate the request, authorized paths, file count, size limits, and sensitive-file rules.
2. Build a deterministic task ZIP containing `TASK.md`, `manifest.json`, and `input/`.
3. Use only the Codex in-app Browser and its existing signed-in ChatGPT Web session.
4. Confirm the target conversation and attached ZIP before sending a task-ID-bearing message.
5. Observe page evidence until the task completes, needs user input, or fails.
6. Download only the matching result ZIP, record its size and SHA-256, and validate it as
   untrusted input before extraction. Do not click previewable result files such as `.md`, `.txt`,
   `.html`, or `.py`; those controls can open a preview instead of a reliable download path.
7. Return a structured `completed`, `needs_input`, or `failed` result.

## Safety boundaries

- Never read, store, or bypass passwords, cookies, tokens, or verification codes.
- Never upload paths that the user did not authorize.
- Never execute code, macros, installers, or other active content from a downloaded ZIP.
- Exchange task data only through ZIP archives. If ChatGPT Web provides only previewable files,
  leave them unopened and return `needs_input` or `RESULT_ZIP_NOT_FOUND`.
- Stop for login prompts, verification challenges, new permission requests, ambiguous page state,
  or material changes to task scope.
- Do not run a live ChatGPT Web test without explicit user authorization for that test.
