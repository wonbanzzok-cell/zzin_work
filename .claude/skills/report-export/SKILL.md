---
name: report-export
description: Converts an approved report draft version (by default the latest workspace/<report-id>/draft_v<N>.md) to .docx, the default deliverable format, and optionally .pdf, in outputs/. Use when the user approves a draft or asks to export it, save it as Word, or make a PDF.
---
# Report Export

## Output Format
- **`.docx` is the default.** Every export produces a `.docx` file.
- Add `.pdf` only when the user asks for it.

## Prerequisites
- `pip install python-docx`
- For PDF: `pip install docx2pdf` (requires Microsoft Word on this PC)

## Steps
1. Add a row `내보내기(docx)` (or `내보내기(docx+pdf)`) to `workspace/<report-id>/todo.md` and set it to `진행 중`.
2. Choose the draft: use the version the user names; otherwise use the latest one (the highest N among `workspace/<report-id>/draft_v<N>.md`). Tell the user which version you are exporting.
3. Check that draft for remaining `[확인 필요]` items. If any remain, list them and ask the user whether to export anyway.
4. Find the next deliverable version: look for `outputs/<report-id>_v*.docx` and use the highest M + 1 (start at 1). This number is separate from the draft version.
5. Run:
   ```
   python .claude/skills/report-export/scripts/export.py workspace/<report-id>/draft_v<N>.md outputs/<report-id>_v<M>.docx [--pdf]
   ```
6. Add a row to the export section of `workspace/<report-id>/revisions.md`: deliverable path, source draft, and date, in Korean.
7. Set the `todo.md` row to `완료` with the output path, or to `중단` with the error.
8. Report the output path(s) and the source draft version to the user.

## Notes
- Supported Markdown: headings, bullet and numbered lists, tables, `**bold**`. Other syntax is exported as plain text.
- Never overwrite an existing file in `outputs/`. The script refuses to do so.
- Never change any draft file while exporting.
- If PDF conversion fails, keep the `.docx`, report the error, and suggest saving as PDF from Word.
- HWP output is not supported. If the user needs HWP, export `.docx` and tell them to convert it in Hangul.
