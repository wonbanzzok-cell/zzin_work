# Data Handling Rules

## Source Integrity
- Never modify files in `inputs/`. Treat them as read-only.
- Never invent numbers or facts. If information is missing, write `[확인 필요: <reason in Korean>]` in the report.

## Citation
- Every number in a report must cite its source file, e.g., `[출처: sales_2026-10.xlsx]`.
- Quotations from documents must cite the file and the section or page, e.g., `[출처: 회의록_1105.docx, 2쪽]`.
- When quoting a non-Korean source, give the Korean translation and keep the citation.

## Web Sources
- Use web sources only when `inputs/` has no relevant material or the user asks for web research. The `web-researcher` agent collects them, following `.claude/rules/web-research.md`.
- Cite web facts with publisher, title, URL, and published date, e.g., `[출처: 국제에너지기구(IEA), "Global EV Outlook 2026", https://www.iea.org/..., 2026. 5.]`.
- Take facts only from pages actually opened with `WebFetch`, never from search snippets.
- State the reference period of every web number, e.g., `2025년 연간 판매량`.
- Record every web source in `workspace/<report-id>/raw_web.md` with its accessed date.
- If sources disagree, show both values with their sources, or mark `[확인 필요: 출처 간 수치 불일치]`.
- Use published values as they are. If a derived value is needed, compute it with a script and record it in `calc.md`; otherwise mark `[확인 필요]`.

## Calculations
- Record every derived value with its formula in `workspace/<report-id>/calc.md`, in Korean.
  Example: `달성률 = 실적 1,230 / 목표 1,500 × 100 = 82.0%`
- Use script output (the `data-summary` skill) for totals and rates. Do not compute them mentally.

## Privacy
- Do not include personal information in reports: names of individuals (except report owners), phone numbers, emails, resident registration numbers.
- Refer to customers or employees by role or anonymized ID.
