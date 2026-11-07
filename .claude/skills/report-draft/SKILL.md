---
name: report-draft
description: End-to-end report drafting. Use when the user asks to write a report (e.g., "주간보고 작성", "monthly report draft", "보고서 초안", "시장 조사 보고서"). Takes a report type, topic, and period, collects material from inputs/ (or the web right away when inputs/ has nothing relevant), drafts, reviews, keeps every draft version, and offers .docx export.
---
# Report Draft Procedure

## Inputs
| Input | Required for | Example |
|---|---|---|
| type | all | `weekly`, `monthly`, `project`, `research` |
| period | all | `2026-W45`, `2026-10`, `2026. 1.~10.`, `2021~2025년 (전망 2030년)` |
| topic | `project`, `research` | `CRM 개편`, `전기차 시장 성장 추이` |
| author | all | from `docs/report-defaults.md` |

- For `weekly` and `monthly`, the period comes from the report ID.
- For `project` and `research`, the period is separate from the report ID and must be given.
- Read `author` and `department` from `docs/report-defaults.md`. If they are empty, ask the user.
- Ask for all missing inputs in a single question before starting.

## Language
All files this procedure creates in `workspace/` are written entirely in Korean. See the Language Policy in `CLAUDE.md`.

## Versioning
Every draft version is kept. Revisions are saved as new files and existing versions are never changed. See Draft Versioning in `.claude/rules/file-naming.md`.

## Task Tracking
Keep `workspace/<report-id>/todo.md` up to date for the whole run (rules in `CLAUDE.md`, format in `.claude/rules/file-naming.md`):
- Create it in step 1 with the report info block and steps 1–11 as `대기` (step 1 as `완료`).
- Before each step, set it to `진행 중`. After it, set `완료`, `건너뜀`, or `중단` with a short note (e.g., `웹 검색으로 수집`, `데이터 파일 없음`).
- Add a row for each revision round in step 9 when it starts.
- Never mark a step `완료` before its output file exists.

## Steps
1. **Prepare.** Build the report ID per `.claude/rules/file-naming.md` and create `workspace/<report-id>/`. If the folder already has `draft_v*.md` files, stop and ask the user whether to revise the latest version instead of starting over. Then create `todo.md` with the report info block.
2. **Check the template.** Check that `templates/<type>.md` and its section in `docs/template-headings.md` exist. If not, stop and tell the user.
3. **Collect internal material.** Run the `researcher` agent → `notes.md`.
4. **Collect web material.** If the researcher replied `관련 자료 없음`, or the user asked for web research, run the `web-researcher` agent right away, without asking the user → `raw_web.md`, `notes.md`. Otherwise mark this step `건너뜀`.
5. **Check material.** Count the content sections in `notes.md` that have at least one sourced item. If fewer than half do, stop: mark this step `중단`, list the empty sections, and ask the user to add files to `inputs/` or narrow the topic. Do not draft.
6. **Analyze.** If `inputs/data/` has files for the period, run the `data-analyst` agent → `analysis.md`, `calc.md`. Otherwise mark this step `건너뜀`.
7. **Draft.** Run the `report-writer` agent → `draft_v1.md` (the original) and `revisions.md`.
8. **Review.** Run the `reviewer` agent on `draft_v1.md` → `review_v1.md`.
9. **Revise.** While the latest review says `결과: 수정 필요`, at most 2 times:
   - Run `report-writer` with `review_v<N>.md` → `draft_v<N+1>.md` (and working-file corrections)
   - Run `reviewer` on `draft_v<N+1>.md` → `review_v<N+1>.md`

   If a review says `결과: 자료 부족`, stop revising and go to step 10.
10. **Report** to the user in Korean:
    - 3-line summary of the report
    - All remaining `[확인 필요]` items
    - Unresolved review items, if any
    - Version list from `revisions.md` and the path to the latest draft
    - Whether web sources were used, with the list of sources from `raw_web.md`
    - Any `todo.md` steps that are not `완료` or `건너뜀`
11. **Offer export.** Ask the user: "최신 초안(draft_v<N>.md)을 .docx로 내보낼까요? PDF도 필요하시면 말씀해 주세요." If the user approves, run the `report-export` skill. Never export without approval; if the user declines, mark this step `건너뜀`.

## Later Revision Requests
When the user asks for changes to an existing report, add the request as new rows in `todo.md`, run `report-writer` to create the next version from the latest draft, then offer to run `reviewer` on it and to export it.
