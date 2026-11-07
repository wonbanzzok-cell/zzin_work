# 템플릿 제목 대응표 (영어 → 한국어)

모든 템플릿 제목, 머리줄 항목명, 표 머리글, 행 이름의 고정 한국어 표기.
`researcher`, `web-researcher`, `report-writer`는 반드시 이 한국어 표기를 그대로 쓴다. `reviewer`는 이 표와 초안을 대조한다.
제목을 임의로 번역하지 않는다. 여기에 없는 제목이 있으면 멈추고 먼저 이 표에 추가한다.
템플릿을 추가하거나 바꾸면 같은 작업 안에서 이 파일도 고친다.

자리표시자(`{{topic}}`, `{{project_name}}`, `{{period}}`, `{{author}}`, `{{date}}`, `{{source_type}}`)는 `todo.md`의 보고 정보 블록으로 채운다 (`.claude/rules/file-naming.md` 참고).

※ 아래 표의 English 열은 템플릿 원문이므로 번역하지 않고 그대로 둔다.

## 공통
| English | Korean |
|---|---|
| Date | 작성일 |
| Author | 작성자 |
| Period | 기간 |
| Sources | 자료 출처 |
| Issues and Risks | 이슈 및 리스크 |
| Issue / Impact / Response / Owner | 이슈 / 영향 / 대응 / 담당 |
| Status values | 정상, 주의, 지연, 완료 |

## `weekly.md`
| English | Korean |
|---|---|
| Weekly Work Report ({{period}}) | 주간 업무 보고 ({{period}}) |
| 1. Summary | 1. 요약 |
| 2. Key Results | 2. 주요 실적 |
| Item / Target / Actual / Achievement | 항목 / 목표 / 실적 / 달성률 |
| 3. Work in Progress | 3. 진행 중인 업무 |
| Task / Progress / Status / Due | 업무 / 진행률 / 상태 / 마감일 |
| 4. Issues and Risks | 4. 이슈 및 리스크 |
| 5. Next Week's Plan | 5. 다음 주 계획 |

## `monthly.md`
| English | Korean |
|---|---|
| Monthly Report ({{period}}) | 월간 보고 ({{period}}) |
| 1. Executive Summary | 1. 핵심 요약 |
| 2. KPI Performance | 2. KPI 실적 |
| KPI / Target / Actual / Achievement / vs Last Month | KPI / 목표 / 실적 / 달성률 / 전월 대비 |
| 3. Key Achievements | 3. 주요 성과 |
| 4. Analysis | 4. 분석 |
| 5. Issues and Risks | 5. 이슈 및 리스크 |
| 6. Next Month's Plan | 6. 다음 달 계획 |

## `project.md`
| English | Korean |
|---|---|
| Project Report: {{project_name}} | 프로젝트 보고: {{project_name}} |
| 1. Overview | 1. 개요 |
| Goal / Scope / Current Phase | 목표 / 범위 / 현재 단계 |
| 2. Overall Status | 2. 전체 현황 |
| Area / Status / Comment | 구분 / 상태 / 비고 |
| Schedule / Budget / Quality | 일정 / 예산 / 품질 |
| 3. Milestones | 3. 마일스톤 |
| Milestone / Planned / Actual / Forecast / Status | 마일스톤 / 계획 / 실적 / 예상 / 상태 |
| 4. Completed This Period | 4. 이번 기간 완료 사항 |
| 5. Issues and Risks | 5. 이슈 및 리스크 |
| 6. Decisions Needed | 6. 의사결정 필요 사항 |
| 7. Next Steps | 7. 다음 단계 |

## `research.md`
| English | Korean |
|---|---|
| Research Report: {{topic}} | 조사 보고서: {{topic}} |
| 1. Summary | 1. 요약 |
| 2. Market Overview | 2. 시장 개요 |
| 3. Market Size and Growth | 3. 시장 규모 및 성장 추이 |
| Metric / Period / Value / Change / Source | 지표 / 기준 기간 / 값 / 증감 / 출처 |
| 4. Segments and Regions | 4. 세그먼트 및 지역별 현황 |
| Segment / Region / Share or Value / Trend | 세그먼트 / 지역 / 비중 또는 값 / 추세 |
| 5. Key Players | 5. 주요 업체 |
| Company / Position / Recent Moves | 업체 / 시장 지위 / 최근 동향 |
| 6. Growth Drivers and Risks | 6. 성장 요인 및 위험 요인 |
| Factor / Type / Impact | 요인 / 구분 / 영향 |
| Type values (driver / risk) | 성장 요인, 위험 요인 |
| 7. Outlook | 7. 전망 |
| 8. Implications | 8. 시사점 |
| 9. Sources | 9. 출처 |
| No. / Publisher / Title / URL / File / Published / Accessed | 번호 / 발행 기관 / 제목 / URL / 파일 / 게시일 / 접속일 |
| Sources values | 내부 자료, 웹 검색, 내부 자료 + 웹 검색 |
