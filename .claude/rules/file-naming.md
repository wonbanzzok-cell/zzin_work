# File Naming Rules

## Report ID
| Type | Format | Example |
|---|---|---|
| `weekly` | `weekly_<YYYY>-W<ww>` (ISO week) | `weekly_2026-W45` |
| `monthly` | `monthly_<YYYY>-<MM>` | `monthly_2026-10` |
| `project` | `project_<project-slug>_<YYYYMMDD>` | `project_crm-renewal_20261107` |
| `research` | `research_<topic-slug>_<YYYYMMDD>` | `research_ev-market-growth_20261107` |

- The slug is a short English name in lowercase with hyphens. It is used only in file and folder names.
- `<YYYYMMDD>` is the date the report run starts, not the reporting period.
- The Korean topic and the reporting period are stored in the report info block of `todo.md`, not in the ID.

## Locations
| Content | Path |
|---|---|
| Source materials | `inputs/data/`, `inputs/documents/`, `inputs/references/` |
| Working files | `workspace/<report-id>/` |
| Final deliverables | `outputs/<report-id>_v<N>.docx` (and `.pdf` on request) |
| Report defaults (author, department) | `docs/report-defaults.md` |
| Korean translations of project `.md` files | `translate/` (see `CLAUDE.md`) |

## Working Files in `workspace/<report-id>/`
| File | Created by |
|---|---|
| `todo.md` | the main session running `report-draft` (report info and to-do list) |
| `notes.md` | researcher; replaced by web-researcher when web sources are used |
| `raw_web.md` | web-researcher (web sources, only when `inputs/` has no relevant material or the user asks) |
| `analysis.md`, `calc.md` | data-analyst |
| `draft_v1.md` | report-writer (original draft) |
| `draft_v2.md`, `draft_v3.md`, ... | report-writer (one file per revision) |
| `review_v<N>.md` | reviewer (review of `draft_v<N>.md`) |
| `revisions.md` | report-writer, report-export (revision, correction, and export log) |

## Draft Versioning
- `draft_v1.md` is always the original draft.
- Every revision, whether from reviewer feedback or a user request, is saved as a new file `draft_v<N+1>.md`, where N is the highest existing version.
- Never edit, overwrite, rename, or delete an existing `draft_v<N>.md`. Create the next version by copying the latest one and editing only the copy.
- The review of `draft_v<N>.md` is saved as `review_v<N>.md`, so each review stays paired with the version it checked.
- The latest draft is the one with the highest N.

## Working-File Corrections
- `notes.md`, `raw_web.md`, `analysis.md`, and `calc.md` are not versioned. When a review finds an error that started in one of them, correct it in place.
- Never remove a source entry from `raw_web.md`; mark a wrong entry `(정정: <reason>)` instead, so source numbers S1, S2, ... stay stable.
- Log every correction in the `작업 파일 수정` section of `revisions.md`.

## Revision Log (`revisions.md`)
Add a row every time a draft version is created, a working file is corrected, or a draft is exported. Write it in Korean, in this format:

```
# 수정 이력: <report-id>

## 초안 버전
| 버전 | 작성일 | 수정 근거 | 주요 수정 내용 |
|---|---|---|---|
| v1 | 2026. 11. 7. | 최초 작성 | - |
| v2 | 2026. 11. 7. | review_v1.md | 10월 매출 수치 정정 외 2건 |
| v3 | 2026. 11. 8. | 사용자 요청 | 요약을 3줄로 축약 |

## 작업 파일 수정
| 파일 | 수정일 | 수정 근거 | 수정 내용 |
|---|---|---|---|
| notes.md | 2026. 11. 7. | review_v1.md | 섹션 제목 오역 정정 ('금기 완료 사항' → '이번 기간 완료 사항') |

## 내보내기 기록
| 결과물 | 원본 초안 | 내보낸 날짜 |
|---|---|---|
| outputs/weekly_2026-W45_v1.docx | draft_v3.md | 2026. 11. 8. |
```

## To-Do List (`todo.md`)
Created at the start of every report run and updated before and after each step. Write it in Korean, in this format:

```
# 작업 목록: <report-id>

## 보고 정보
- 유형: research
- 주제: 전기차 시장 성장 추이
- 기간: 2021~2025년 (전망 2030년)
- 작성자: <author> (<department>)
- 작성일: 2026. 11. 7.(토)
- 자료 출처: 웹 검색

## 작업
| 순서 | 작업 | 담당 | 상태 | 비고 |
|---|---|---|---|---|
| 1 | 준비(보고서 ID·폴더·보고 정보) | 주 세션 | 완료 | - |
| 2 | 템플릿 확인 | 주 세션 | 완료 | templates/research.md |
| 3 | 내부 자료 수집 | researcher | 완료 | 관련 자료 없음 |
| 4 | 웹 자료 수집 | web-researcher | 진행 중 | 내부 자료 없음 → 즉시 웹 검색 |
| 5 | 자료 충분성 확인 | 주 세션 | 대기 | - |
| 6 | 데이터 분석 | data-analyst | 대기 | - |
| 7 | 초안 작성(v1) | report-writer | 대기 | - |
| 8 | 검수(v1) | reviewer | 대기 | - |
| 9 | 수정·재검수 | report-writer, reviewer | 대기 | - |
| 10 | 결과 보고 | 주 세션 | 대기 | - |
| 11 | 내보내기(docx) | report-export | 대기 | 사용자 승인 후 |
```

- The report info block is the single source for the template header placeholders: `{{topic}}` / `{{project_name}}` ← 주제, `{{period}}` ← 기간, `{{author}}` ← 작성자, `{{date}}` ← 작성일, `{{source_type}}` ← 자료 출처.
- 자료 출처 is one of: `내부 자료`, `웹 검색`, `내부 자료 + 웹 검색`.
- 상태 is one of: `대기`, `진행 중`, `완료`, `건너뜀`, `중단`.
- Keep at most one row `진행 중`. Append rows (e.g., `수정(v2)`, `검수(v2)`, `사용자 요청: 요약 축약`); never delete rows.

## Deliverable Versioning
- Never overwrite an existing deliverable. Increment the version: `_v1` → `_v2`.
- Deliverable versions (`outputs/..._v<N>`) are numbered separately from draft versions. `revisions.md` records which draft each deliverable came from.

## General
- Use only lowercase letters, digits, hyphens, and underscores in file names. No spaces.
