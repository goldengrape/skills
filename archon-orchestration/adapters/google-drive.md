# Google Drive Shared Workspace Adapter

Use Google Drive for document-centric, research, planning, writing, spreadsheet, presentation, or mixed-artifact tasks.

## Recommended mapping

```text
<user-provided-folder>/
  .archon/
    runs/
      <run_id>/
        manifest.json
        task.md
        generation/
          G1/
          G2/
          G3/
          G4/
        verification/
        critique/
        ranking/
        fusion/
        final/
```

Each Generator writes only inside its own subfolder until the generation barrier.

## Artifact types

Candidate artifacts may be:

- Google Docs
- Sheets
- Slides
- uploaded Markdown/text/PDF files
- folders containing multiple artifacts

Store stable file/folder identifiers or URLs in result metadata when available.

## Isolation

A Generator should be given direct links only to frozen base materials and its own output folder. Do not provide sibling Generator folders before the barrier.

## Finalization

Fuser creates a new artifact in `fusion/` or `final/`; do not overwrite original candidates. If the final artifact will replace or publish over an existing shared document, treat that as a CHECKPOINT.
