# Web Research Rules

Applies whenever report material comes from the web.

## When to Use the Web
- `inputs/` is the primary source. Use the web only when `inputs/` has no relevant material for the report, or when the user asks for web research.
- Web research is done by the `web-researcher` agent. The `researcher` agent never searches the web.
- When the researcher reports `관련 자료 없음`, run `web-researcher` right away, without asking the user.
- Never save web content into `inputs/`.

## Source Priority
1. Government and statistics agencies, international organizations (e.g., IEA, OECD)
2. Company IR materials and official press releases
3. Established research firms and industry associations
4. Major news outlets

Avoid blogs, forums, social media, unsourced aggregator pages, and AI-generated summaries. Use a lower-priority source only when no higher one covers the fact, and note this in `raw_web.md`.

## Collecting Facts
- Search with several queries, in Korean and in English.
- Take facts only from pages opened with `WebFetch`. Never use a number seen only in a search snippet.
- Prefer the most recent data. Record the reference period of every number, e.g., `2025년 연간`.
- Separate actual figures from forecasts. Label each forecast with its source and target year, e.g., `2030년 전망`.
- Cross-check key numbers with a second independent source when you can. If sources disagree, keep both values with their sources, or mark `[확인 필요: 출처 간 수치 불일치]`.
- Translate non-Korean content into Korean (see the Language Policy in `CLAUDE.md`).
- Use published values as they are. Do not compute new values; derived values follow the Calculations rules in `data-handling.md`.

## Citation
Format: `[출처: <publisher>, "<title>", <URL>, <published date>]`

Example: `[출처: 국제에너지기구(IEA), "Global EV Outlook 2026", https://www.iea.org/..., 2026. 5.]`

- If the published date is unknown, write `게시일 미상`.
- In a draft, a short form with the source number from `raw_web.md` is allowed when the full citation appears in the draft's sources section, e.g., `[출처: S1]`.

## Source Log (`raw_web.md`)
Record every source used, in Korean, in this format:

```
# 웹 자료 원문: <report-id>
접속일: 2026. 11. 7.(토) | 검색어: <queries>

## S1. <publisher> — <title>
- URL: <URL>
- 게시일: 2026. 5. | 신뢰 등급: 1
- 발췌:
  - <fact, translated into Korean> (기준 기간: 2025년 연간)

## 제외한 출처
- <URL>: <reason>
```

- Number sources S1, S2, ... and never renumber them, so notes and drafts can refer to them.
- 신뢰 등급 is the Source Priority number above (1–4).
