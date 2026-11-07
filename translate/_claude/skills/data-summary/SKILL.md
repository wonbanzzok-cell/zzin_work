---
name: data-summary
description: inputs/data/의 Excel/CSV 파일을 Markdown 표로 요약한다 (합계, 평균, 최소, 최대, 이상치 표시가 포함된 전기 대비 증감). 보고서 수치가 스프레드시트에서 나올 때마다 사용한다.
---
# 데이터 요약

## 사전 준비
`pip install pandas openpyxl`

## 사용법
```
python .claude/skills/data-summary/scripts/summarize.py <file> [--sheet NAME] [--date-col COL] [--period PERIOD] [--out PATH]
```
- `--date-col`과 `--period`를 함께 주면 해당 기간과 직전 기간을 비교한다.
- `--period`는 `2026-10` (월) 또는 `2026-W45` (ISO 주차) 형식을 받는다.
- `--out`이 없으면 결과를 화면에 출력한다.

## 단계
1. 파일을 한 번 열어 날짜 열과 숫자 열을 확인한다.
2. `--out workspace/<report-id>/raw_<file-stem>.md`로 스크립트를 실행한다.
3. 결과를 검토한다. 30% 이상 변동은 `이상치`로 표시된다.
4. 필요한 표를 원본 파일 이름과 함께 `workspace/<report-id>/analysis.md`에 합친다. 영어 열 이름은 한국어로 바꾼다 (예: `revenue` → `매출`).

## 출력 언어
스크립트가 제목과 표 머리글을 한국어로 출력하므로, 결과를 보고서 작업 파일에 그대로 넣을 수 있다.

## 참고
- CSV 파일은 UTF-8로 읽고, 실패하면 CP949로 읽는다.
- 스크립트가 실패하면 오류 메시지를 그대로 보고한다. 대신 손으로 계산하지 않는다.
