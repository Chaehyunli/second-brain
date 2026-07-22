# Vault image archive policy

## Scope

- Bulk image archival applies to existing `blog/` notes **except** `blog/STUDYING/`, plus existing `notion/Information/` notes.
- Never bulk-download images for `notion/SKALA/` or `blog/STUDYING/`.
- SKALA and STUDYING visuals are handled only through a separately approved, concept-first pass; a public derivative should reuse its canonical SKALA asset rather than create another copy.

## Selection and storage

- Select at most three visible, non-SVG raster images from a blog article body. Exclude hidden (`0×0`) and small (`<240×100`) images, icons, and duplicate URLs.
- Save the selected image as WebP, resize to at most 1600px wide, and store it beside the note under `assets/<note-slug>/`.
- Add a visible `## 핵심 이미지` section with local relative Markdown paths so both Obsidian and GitHub render the same files.
- Add `SOURCE.txt` beside each asset set. It records source page, context, source-image path without signed query parameters, source SHA-256, and archived dimensions.
- Do not store expiring signed URLs, original high-resolution binaries, or images larger than 10 MiB.

## Verification

- Every Markdown image path must resolve locally.
- `SOURCE.txt` must not contain signed query parameters in `source_image_path` fields.
- Confirm that SKALA and STUDYING have no bulk-imported assets or Markdown changes.
- Run Markdown whitespace checks, relevant unit tests, and GitHub push verification before declaring completion.
