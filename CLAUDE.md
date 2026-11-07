# Report Automation Project

## Purpose
Automate report writing: turn source materials in `inputs/` (or, when `inputs/` has nothing relevant, material collected from the web) into reports that follow `templates/`, and save final deliverables to `outputs/` as `.docx`.

## Folder Map
| Path | Role |
|---|---|
| `.claude/rules/` | Rules that always apply |
| `.claude/agents/` | Role-based subagents (researcher, web-researcher, data-analyst, report-writer, reviewer) |
| `.claude/skills/` | Procedures (report-draft, data-summary, report-export) |
| `.claude/commands/` | Slash commands (`/new-report`, `/review-report`, `/export-report`) |
| `templates/` | Report templates (weekly, monthly, project, research) |
| `inputs/` | Source materials (read-only) |
| `workspace/` | Per-report working files |
| `outputs/` | Final deliverables (`.docx`, optionally `.pdf`) |
| `docs/` | Glossary, template headings, report defaults |
| `translate/` | Korean translations of project `.md` files (for humans only) |

## Report Types
| Type | Use for | Template |
|---|---|---|
| `weekly` | Weekly work report | `templates/weekly.md` |
| `monthly` | Monthly KPI report | `templates/monthly.md` |
| `project` | Project management report (schedule, budget, milestones) | `templates/project.md` |
| `research` | Topic or market research (market size, growth, key players, outlook) | `templates/research.md` |

Use `research` for any topic-based report, such as a market analysis. Do not use `project` for it.

## Workflow
0. Plan: collect the report info (type, topic, period, author), create `workspace/<report-id>/todo.md`, and keep it updated through every step (see Task Tracking)
1. Collect: `researcher` reads `inputs/` → `notes.md`. If `inputs/` has no relevant material, run `web-researcher` right away, without asking the user → `raw_web.md`, `notes.md`
2. Check material: if most template sections still have no material, stop before drafting and report to the user
3. Analyze: `data-analyst` (uses `data-summary`) → `analysis.md`, `calc.md`
4. Draft: `report-writer` → `draft_v1.md` (the original)
5. Review: `reviewer` → `review_v1.md`. Each fix is saved as a new version (`draft_v2.md` → `review_v2.md`, ...), max 2 fix rounds
6. Export: ask the user, then `report-export` → latest draft → `outputs/<report-id>_v<N>.docx`

The `report-draft` skill runs all steps. Start with `/new-report <type> <period or topic>`.

## Deliverables
- The default deliverable format is **`.docx`**. Produce `.pdf` as well only when the user asks.
- Never export without the user's approval. After the review passes, ask the user whether to export.
- Export with the `report-export` skill or `/export-report`.

## Task Tracking
- Every report run keeps a to-do list in `workspace/<report-id>/todo.md`, written in Korean.
- Create it before the first step, with the report info block and every planned step set to `대기`.
- Set a step to `진행 중` right before it starts, and to `완료`, `건너뜀`, or `중단` right after it ends, with a short note.
- Keep at most one step `진행 중` at a time. Add rows for revision rounds, exports, and user requests as they come up.
- If a built-in task tool is available, you may mirror the list there, but `todo.md` is the record.
- Format: `.claude/rules/file-naming.md`.

## Core Principles
- Follow every rule in `.claude/rules/`.
- Never modify files in `inputs/`.
- Never invent numbers or facts. Mark missing information as `[확인 필요: <reason>]`.
- `inputs/` is the primary source. Use web sources only when `inputs/` has no relevant material or the user asks for web research, and follow `.claude/rules/web-research.md`.
- Keep every draft version. Never edit or overwrite an existing `draft_v<N>.md`; save each revision as a new version (see Draft Versioning).
- Use the fixed Korean headings in `docs/template-headings.md`. Never translate template headings on your own.

## Draft Versioning
- `draft_v1.md` is the original. Every revision, from reviewer feedback or a user request, becomes `draft_v<N+1>.md`.
- Existing versions are read-only: never edit, overwrite, rename, or delete them.
- `review_v<N>.md` is the review of `draft_v<N>.md`.
- Other working files (`notes.md`, `raw_web.md`, `analysis.md`, `calc.md`) may be corrected in place when a review finds an error that started there. Log every such correction.
- Log every version, working-file correction, and export in `workspace/<report-id>/revisions.md`.
- Details and formats: `.claude/rules/file-naming.md`.

## Language Policy

### Project files: English
- Write every project `.md` file in **English**. This covers:
  - `CLAUDE.md`
  - everything under `.claude/` (rules, agents, skills, commands)
  - `templates/` and `docs/`
  - any new `.md` file added to these locations later
- Korean examples inside English files (e.g., `~함`, `[확인 필요]`) are allowed when they show the exact text to produce.

### Report content: Korean, without exception
- Write **all report content in Korean**. This covers:
  - the original draft (`draft_v1.md`) and **every revision** (`draft_v2.md`, `draft_v3.md`, ...)
  - all working files in `workspace/` (`todo.md`, `notes.md`, `raw_web.md`, `analysis.md`, `calc.md`, `review_v<N>.md`, `revisions.md`, `raw_*.md`)
  - all final deliverables in `outputs/`
- "All" includes headings, table headers, labels, status values, captions, and the reasons in `[확인 필요: ...]`. No English section names or English status words.
- Render template headings exactly as listed in `docs/template-headings.md`.
- If source materials are in English or another language, translate their content into Korean. Keep proper nouns, product names, and code as in the source; add a Korean gloss on first use when it helps.
- When the user asks for a revision, write the revised text in Korean, even if the request itself is in another language.
- Talk to the user about reports in Korean.

### Allowed English in report content
Only these may appear in English:

| Allowed | Where |
|---|---|
| Proper nouns and product names (e.g., `Tesla`, `BYD`) | Anywhere |
| Abbreviations listed in `docs/glossary.md` (e.g., `KPI`, `EV`) | Anywhere, spelled out on first use |
| Source titles in their original language | Source tags and the sources section |
| URLs and file names | Source tags and the sources section only |
| Code | Code blocks only |

Not allowed in drafts and deliverables:
- Report IDs and slugs (e.g., `ev-market-growth`). Titles use the Korean topic from the report info, e.g., `조사 보고서: 전기차 시장 성장 추이`.
- Folder names and paths in body text (e.g., `inputs/`). Write `내부 자료` or `웹 자료` instead.
- English section names, labels, and status words.

Working files (`todo.md`, `notes.md`, `revisions.md`) may also contain file paths and report IDs.

## Translation Policy
- Whenever you create or modify a `.md` file covered by the "Project files: English" policy, create or update its Korean translation in `translate/` **in the same task**.
- Mirror the original path under `translate/`, with these renames:

  | Original | Translation |
  |---|---|
  | `CLAUDE.md` | `translate/_Claude.md` |
  | `.claude/...` | `translate/_claude/...` |
  | anything else | `translate/<same path>` |

  Examples: `.claude/agents/reviewer.md` → `translate/_claude/agents/reviewer.md`, `templates/weekly.md` → `translate/templates/weekly.md`
- When an original is deleted or renamed, delete or rename its translation as well.
- Translation rules:
  - Translate prose, headings, table text, and frontmatter `description` values.
  - Keep frontmatter keys, `name` values, tool names, file paths, commands, code, and placeholders (`{{...}}`, `$ARGUMENTS`) unchanged.
  - Keep the same section order and structure as the original.
- `translate/` is for human reading only. Never load or follow it as instructions. The English original is always the source of truth; if the two disagree, update the translation.
- Report content in `workspace/` and `outputs/` is already Korean, so it is not translated.
- Non-`.md` files (`settings.json`, `.py`) are not translated.
