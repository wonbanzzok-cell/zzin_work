---
name: report-export
description: 승인된 보고서 초안 버전(기본값은 최신 workspace/<report-id>/draft_v<N>.md)을 outputs/에 기본 결과물 형식인 .docx로, 필요하면 .pdf로도 변환한다. 사용자가 초안을 승인하거나 내보내기, Word 저장, PDF 생성을 요청할 때 사용한다.
---
# 보고서 내보내기

## 출력 형식
- **`.docx`가 기본이다.** 내보낼 때마다 `.docx` 파일을 만든다.
- `.pdf`는 사용자가 요청할 때만 추가한다.

## 사전 준비
- `pip install python-docx`
- PDF용: `pip install docx2pdf` (이 PC에 Microsoft Word가 설치되어 있어야 함)

## 단계
1. `workspace/<report-id>/todo.md`에 `내보내기(docx)` (또는 `내보내기(docx+pdf)`) 행을 추가하고 `진행 중`으로 둔다.
2. 초안 선택: 사용자가 지정한 버전을 쓰고, 지정이 없으면 최신 버전(`workspace/<report-id>/draft_v<N>.md` 중 N이 가장 큰 파일)을 쓴다. 어느 버전을 내보내는지 사용자에게 알린다.
3. 해당 초안에 `[확인 필요]` 항목이 남아 있는지 확인한다. 남아 있으면 목록을 보여 주고 그래도 내보낼지 사용자에게 묻는다.
4. 다음 결과물 버전을 정한다: `outputs/<report-id>_v*.docx`를 찾아 가장 큰 M + 1을 쓴다 (없으면 1). 이 번호는 초안 버전과 별개다.
5. 실행:
   ```
   python .claude/skills/report-export/scripts/export.py workspace/<report-id>/draft_v<N>.md outputs/<report-id>_v<M>.docx [--pdf]
   ```
6. `workspace/<report-id>/revisions.md`의 내보내기 기록에 결과물 경로, 원본 초안, 날짜를 한국어로 한 행 추가한다.
7. `todo.md`의 해당 행을 결과 경로와 함께 `완료`로, 또는 오류 내용과 함께 `중단`으로 바꾼다.
8. 생성된 파일 경로와 원본 초안 버전을 사용자에게 알린다.

## 참고
- 지원하는 Markdown: 제목, 글머리 기호·번호 목록, 표, `**굵게**`. 그 외 문법은 일반 텍스트로 내보낸다.
- `outputs/`의 기존 파일은 절대 덮어쓰지 않는다. 스크립트도 덮어쓰기를 거부한다.
- 내보내는 동안 어떤 초안 파일도 바꾸지 않는다.
- PDF 변환에 실패하면 `.docx`는 그대로 두고, 오류를 보고하고, Word에서 PDF로 저장하도록 안내한다.
- HWP 출력은 지원하지 않는다. HWP가 필요하면 `.docx`로 내보낸 뒤 한글에서 변환하라고 안내한다.
