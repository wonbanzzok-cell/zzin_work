# 파일 이름 규칙

## 보고서 ID
| 유형 | 형식 | 예 |
|---|---|---|
| `weekly` | `weekly_<YYYY>-W<ww>` (ISO 주차) | `weekly_2026-W45` |
| `monthly` | `monthly_<YYYY>-<MM>` | `monthly_2026-10` |
| `project` | `project_<project-slug>_<YYYYMMDD>` | `project_crm-renewal_20261107` |
| `research` | `research_<topic-slug>_<YYYYMMDD>` | `research_ev-market-growth_20261107` |

- 슬러그는 영문 소문자와 하이픈으로 된 짧은 이름이다. 파일·폴더 이름에만 쓴다.
- `<YYYYMMDD>`는 보고 대상 기간이 아니라 보고서 작업을 시작한 날짜다.
- 한국어 주제와 보고 기간은 ID가 아니라 `todo.md`의 보고 정보 블록에 저장한다.

## 저장 위치
| 내용 | 경로 |
|---|---|
| 원본 자료 | `inputs/data/`, `inputs/documents/`, `inputs/references/` |
| 작업 파일 | `workspace/<report-id>/` |
| 최종 결과물 | `outputs/<report-id>_v<N>.docx` (요청 시 `.pdf`도) |
| 보고서 기본값 (작성자, 부서) | `docs/report-defaults.md` |
| 프로젝트 `.md` 파일의 한국어 번역본 | `translate/` (`CLAUDE.md` 참고) |

## `workspace/<report-id>/`의 작업 파일
| 파일 | 작성 주체 |
|---|---|
| `todo.md` | `report-draft`를 실행하는 주 세션 (보고 정보와 작업 목록) |
| `notes.md` | researcher. 웹 자료를 쓰면 web-researcher가 새로 씀 |
| `raw_web.md` | web-researcher (웹 출처, `inputs/`에 관련 자료가 없거나 사용자가 요청할 때만) |
| `analysis.md`, `calc.md` | data-analyst |
| `draft_v1.md` | report-writer (초안 원문) |
| `draft_v2.md`, `draft_v3.md`, ... | report-writer (수정할 때마다 한 파일씩) |
| `review_v<N>.md` | reviewer (`draft_v<N>.md`의 검수 결과) |
| `revisions.md` | report-writer, report-export (수정·작업 파일 정정·내보내기 이력) |

## 초안 버전 관리
- `draft_v1.md`는 항상 초안 원문이다.
- 검수 의견이든 사용자 요청이든, 모든 수정은 새 파일 `draft_v<N+1>.md`로 저장한다. N은 현재 가장 큰 버전 번호다.
- 기존 `draft_v<N>.md`는 절대 수정, 덮어쓰기, 이름 변경, 삭제하지 않는다. 최신 버전을 복사해 다음 버전을 만들고 복사본만 고친다.
- `draft_v<N>.md`의 검수 결과는 `review_v<N>.md`로 저장해, 검수 결과가 해당 버전과 짝을 이루게 한다.
- 최신 초안은 N이 가장 큰 파일이다.

## 작업 파일 수정
- `notes.md`, `raw_web.md`, `analysis.md`, `calc.md`는 버전을 나누지 않는다. 검수에서 이 파일에서 시작된 오류가 발견되면 직접 고친다.
- `raw_web.md`의 출처 항목은 삭제하지 않는다. 잘못된 항목은 `(정정: <reason>)`으로 표시해 출처 번호 S1, S2, ...가 바뀌지 않게 한다.
- 고칠 때마다 `revisions.md`의 `작업 파일 수정` 섹션에 기록한다.

## 수정 이력 (`revisions.md`)
초안 버전을 만들거나, 작업 파일을 고치거나, 초안을 내보낼 때마다 한 행을 추가한다. 한국어로 아래 형식에 맞춰 쓴다.

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

## 작업 목록 (`todo.md`)
보고서 작업을 시작할 때 만들고, 각 단계 전후로 갱신한다. 한국어로 아래 형식에 맞춰 쓴다.

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

- 보고 정보 블록은 템플릿 머리줄 자리표시자의 유일한 출처다: `{{topic}}` / `{{project_name}}` ← 주제, `{{period}}` ← 기간, `{{author}}` ← 작성자, `{{date}}` ← 작성일, `{{source_type}}` ← 자료 출처.
- 자료 출처는 `내부 자료`, `웹 검색`, `내부 자료 + 웹 검색` 중 하나다.
- 상태는 `대기`, `진행 중`, `완료`, `건너뜀`, `중단` 중 하나다.
- `진행 중`인 행은 하나만 둔다. 행은 추가만 하고 (예: `수정(v2)`, `검수(v2)`, `사용자 요청: 요약 축약`) 삭제하지 않는다.

## 결과물 버전 관리
- 기존 결과물은 절대 덮어쓰지 않는다. 버전을 올린다: `_v1` → `_v2`.
- 결과물 버전(`outputs/..._v<N>`)은 초안 버전과 따로 매긴다. 각 결과물이 어느 초안에서 나왔는지는 `revisions.md`에 기록한다.

## 공통
- 파일 이름에는 영문 소문자, 숫자, 하이픈, 밑줄만 쓴다. 공백은 쓰지 않는다.
