# Run Start Checklist

Use before `GENERATING`.

- [ ] User-provided Shared Workspace root is identified.
- [ ] Workspace scope is dedicated or explicitly approved.
- [ ] Backend adapter is selected only after backend is known.
- [ ] Orchestrator can read/write required control state.
- [ ] `manifest.json` exists with valid stage, policy, workspace, counters, scheduled generators, and artifact keys (schema 0.2; see `templates/manifest.json`).
- [ ] `task.md` is frozen, complete, and contains no `<TODO>` placeholders.
- [ ] Material constraints, success criteria, assumptions, and open questions are separated.
- [ ] Available Agent Executors and capabilities are recorded, including direct workspace read/write vs return-only.
- [ ] Generator count, minimum usable quorum, replacement budget, schema-repair budget, evaluator budget, and fusion retry budget are set.
- [ ] Verifier mode is `auto`, `enabled`, or `disabled` with reason.
- [ ] One isolated namespace exists per scheduled Generator.
- [ ] Each Generator has a dispatch package or enough dispatch metadata to reconstruct it.
- [ ] No Generator has access to sibling candidate outputs.
- [ ] For browser-operated independent Generators, `browser_base_url` is recorded or intentionally left at the executor default.
- [ ] A user-provided ChatGPT project/workspace URL is treated only as a base/landing URL, never as permission to reuse an existing conversation.
- [ ] Every browser-operated independent Generator will create a fresh browser page/tab and a fresh conversation from the base URL; no Generator reuses another Generator's page, conversation, follow-up chain, or saved session.
- [ ] The Orchestrator can record a page/conversation handle or equivalent reattachment hint when the executor exposes one.
- [ ] For GitHub backend, `workspace_io_mode` is `direct_required` unless the user explicitly approved a degraded return-only path.
- [ ] For GitHub direct mode, each Generator can read its frozen task/base refs and write its own GitHub branch/namespace without the Orchestrator pasting or uploading substantive artifacts through chat.
- [ ] For GitHub direct mode, browser/file attachment flags are not being used merely to duplicate artifacts that already exist in GitHub.
- [ ] `allow_return_only_fallback` is explicit; it is not silently inferred from executor convenience.
- [ ] Return-only normalization path is available before dispatching any Executor for which fallback was explicitly permitted.
- [ ] Any non-persistent dry run is clearly labeled.
