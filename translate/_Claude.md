# 보고서 작성 자동화 프로젝트

## 목적
보고서 작성 자동화: `inputs/`의 원본 자료(또는 `inputs/`에 관련 자료가 없을 때 웹에서 수집한 자료)를 `templates/` 양식에 맞춘 보고서로 만들고, 최종 결과물을 `outputs/`에 `.docx`로 저장한다.

## 폴더 구성
| 경로 | 역할 |
|---|---|
| `.claude/rules/` | 항상 적용되는 규칙 |
| `.claude/agents/` | 역할별 서브에이전트 (researcher, web-researcher, data-analyst, report-writer, reviewer) |
| `.claude/skills/` | 작업 절차 (report-draft, data-summary, report-export) |
| `.claude/commands/` | 슬래시 명령 (`/new-report`, `/review-report`, `/export-report`) |
| `templates/` | 보고서 양식 (weekly, monthly, project, research) |
| `inputs/` | 원본 자료 (읽기 전용) |
| `workspace/` | 보고서별 작업 파일 |
| `outputs/` | 최종 결과물 (`.docx`, 필요하면 `.pdf`) |
| `docs/` | 용어집, 템플릿 제목 대응표, 보고서 기본값 |
| `translate/` | 프로젝트 `.md` 파일의 한국어 번역본 (사람이 읽는 용도) |

## 보고서 유형
| 유형 | 용도 | 템플릿 |
|---|---|---|
| `weekly` | 주간 업무 보고 | `templates/weekly.md` |
| `monthly` | 월간 KPI 보고 | `templates/monthly.md` |
| `project` | 프로젝트 관리 보고 (일정, 예산, 마일스톤) | `templates/project.md` |
| `research` | 주제·시장 조사 (시장 규모, 성장 추이, 주요 업체, 전망) | `templates/research.md` |

시장 분석처럼 주제를 다루는 보고서에는 `research`를 쓴다. `project`를 쓰지 않는다.

## 작업 흐름
0. 계획: 보고 정보(유형, 주제, 기간, 작성자)를 받고 `workspace/<report-id>/todo.md`를 만들어 모든 단계에서 계속 갱신한다 (작업 목록 관리 참고)
1. 수집: `researcher`가 `inputs/`를 읽는다 → `notes.md`. `inputs/`에 관련 자료가 없으면 사용자에게 묻지 않고 바로 `web-researcher`를 실행한다 → `raw_web.md`, `notes.md`
2. 자료 확인: 템플릿 섹션 대부분에 여전히 자료가 없으면, 초안 작성 전에 멈추고 사용자에게 보고한다
3. 분석: `data-analyst` (`data-summary` 사용) → `analysis.md`, `calc.md`
4. 작성: `report-writer` → `draft_v1.md` (원문)
5. 검수: `reviewer` → `review_v1.md`. 수정할 때마다 새 버전으로 저장 (`draft_v2.md` → `review_v2.md`, ...), 수정은 최대 2회
6. 내보내기: 사용자에게 물은 뒤 `report-export` → 최신 초안 → `outputs/<report-id>_v<N>.docx`

`report-draft` 스킬이 모든 단계를 실행한다. `/new-report <type> <기간 또는 주제>`로 시작한다.

## 결과물
- 기본 결과물 형식은 **`.docx`**다. `.pdf`는 사용자가 요청할 때만 함께 만든다.
- 사용자 승인 없이 내보내지 않는다. 검수를 통과하면 내보낼지 사용자에게 묻는다.
- 내보내기는 `report-export` 스킬이나 `/export-report`로 한다.

## 작업 목록 관리
- 보고서 작업마다 `workspace/<report-id>/todo.md`에 작업 목록을 한국어로 관리한다.
- 첫 단계 전에 보고 정보 블록과 함께 만들고, 예정된 모든 단계를 `대기`로 둔다.
- 단계를 시작하기 직전에 `진행 중`으로, 끝난 직후에 `완료`, `건너뜀`, `중단` 중 하나로 바꾸고 짧은 비고를 적는다.
- `진행 중`인 단계는 한 번에 하나만 둔다. 수정 라운드, 내보내기, 사용자 요청은 생길 때마다 행을 추가한다.
- 내장 작업 도구가 있으면 같은 목록을 그쪽에도 둘 수 있지만, 기록은 `todo.md`가 기준이다.
- 형식: `.claude/rules/file-naming.md`.

## 핵심 원칙
- `.claude/rules/`의 모든 규칙을 따른다.
- `inputs/`의 파일은 절대 수정하지 않는다.
- 수치나 사실을 지어내지 않는다. 없는 정보는 `[확인 필요: <reason>]`으로 표시한다.
- `inputs/`가 기본 자료다. 웹 자료는 `inputs/`에 관련 자료가 없거나 사용자가 웹 조사를 요청할 때만 쓰고, `.claude/rules/web-research.md`를 따른다.
- 모든 초안 버전을 보관한다. 기존 `draft_v<N>.md`는 수정하거나 덮어쓰지 않고, 수정할 때마다 새 버전으로 저장한다 (초안 버전 관리 참고).
- `docs/template-headings.md`에 정해진 한국어 제목을 쓴다. 템플릿 제목을 임의로 번역하지 않는다.

## 초안 버전 관리
- `draft_v1.md`가 원문이다. 검수 의견이나 사용자 요청에 따른 모든 수정은 `draft_v<N+1>.md`가 된다.
- 기존 버전은 읽기 전용이다: 절대 수정, 덮어쓰기, 이름 변경, 삭제하지 않는다.
- `review_v<N>.md`는 `draft_v<N>.md`의 검수 결과다.
- 그 밖의 작업 파일(`notes.md`, `raw_web.md`, `analysis.md`, `calc.md`)은 검수에서 그 파일에서 시작된 오류가 발견되면 직접 고칠 수 있다. 고칠 때마다 기록한다.
- 모든 버전, 작업 파일 수정, 내보내기는 `workspace/<report-id>/revisions.md`에 기록한다.
- 자세한 규칙과 형식: `.claude/rules/file-naming.md`.

## 언어 정책

### 프로젝트 파일: 영어
- 프로젝트의 모든 `.md` 파일은 **영어**로 작성한다. 대상은 다음과 같다.
  - `CLAUDE.md`
  - `.claude/` 아래 전체 (rules, agents, skills, commands)
  - `templates/`와 `docs/`
  - 이후 위 위치에 새로 추가되는 모든 `.md` 파일
- 만들어야 할 문구를 정확히 보여 주는 경우에는 영어 파일 안에 한국어 예시(예: `~함`, `[확인 필요]`)를 넣을 수 있다.

### 보고서 내용: 예외 없이 한국어
- **모든 보고서 내용은 한국어로** 작성한다. 대상은 다음과 같다.
  - 초안 원문(`draft_v1.md`)과 **모든 수정본** (`draft_v2.md`, `draft_v3.md`, ...)
  - `workspace/`의 모든 작업 파일 (`todo.md`, `notes.md`, `raw_web.md`, `analysis.md`, `calc.md`, `review_v<N>.md`, `revisions.md`, `raw_*.md`)
  - `outputs/`의 모든 최종 결과물
- "모든"에는 제목, 표 머리글, 항목명, 상태값, 캡션, `[확인 필요: ...]`의 사유가 포함된다. 영어 섹션 이름이나 영어 상태값을 쓰지 않는다.
- 템플릿 제목은 `docs/template-headings.md`에 있는 그대로 쓴다.
- 원본 자료가 영어나 다른 언어이면 내용을 한국어로 번역한다. 고유명사, 제품명, 코드는 원문 그대로 두고, 필요하면 처음 나올 때 한국어 설명을 붙인다.
- 사용자가 수정을 요청하면, 요청이 다른 언어로 되어 있어도 수정본은 한국어로 쓴다.
- 보고서에 관해 사용자와 이야기할 때는 한국어를 쓴다.

### 보고서 내용에서 허용되는 영어
아래만 영어로 쓸 수 있다.

| 허용 대상 | 위치 |
|---|---|
| 고유명사와 제품명 (예: `Tesla`, `BYD`) | 어디든 |
| `docs/glossary.md`에 있는 약어 (예: `KPI`, `EV`) | 어디든, 처음 나올 때 풀어 씀 |
| 원어로 된 출처 제목 | 출처 표시와 출처 섹션 |
| URL과 파일 이름 | 출처 표시와 출처 섹션에서만 |
| 코드 | 코드 블록에서만 |

초안과 결과물에서 허용되지 않는 것:
- 보고서 ID와 슬러그 (예: `ev-market-growth`). 제목에는 보고 정보의 한국어 주제를 쓴다. 예: `조사 보고서: 전기차 시장 성장 추이`.
- 본문의 폴더 이름과 경로 (예: `inputs/`). 대신 `내부 자료` 또는 `웹 자료`라고 쓴다.
- 영어 섹션 이름, 항목명, 상태값.

작업 파일(`todo.md`, `notes.md`, `revisions.md`)에는 파일 경로와 보고서 ID를 써도 된다.

## 번역 정책
- "프로젝트 파일: 영어" 정책 대상인 `.md` 파일을 만들거나 고칠 때마다, **같은 작업 안에서** `translate/`의 한국어 번역본도 만들거나 고친다.
- `translate/` 아래에 원본과 같은 경로로 두되, 다음 이름은 바꾼다.

  | 원본 | 번역본 |
  |---|---|
  | `CLAUDE.md` | `translate/_Claude.md` |
  | `.claude/...` | `translate/_claude/...` |
  | 그 외 | `translate/<같은 경로>` |

  예: `.claude/agents/reviewer.md` → `translate/_claude/agents/reviewer.md`, `templates/weekly.md` → `translate/templates/weekly.md`
- 원본을 삭제하거나 이름을 바꾸면 번역본도 똑같이 삭제하거나 이름을 바꾼다.
- 번역 규칙:
  - 본문, 제목, 표 내용, frontmatter의 `description` 값을 번역한다.
  - frontmatter 키, `name` 값, 도구 이름, 파일 경로, 명령어, 코드, 자리표시자(`{{...}}`, `$ARGUMENTS`)는 그대로 둔다.
  - 섹션 순서와 구조는 원본과 같게 유지한다.
- `translate/`는 사람이 읽는 용도로만 쓴다. 지침으로 불러오거나 따르지 않는다. 기준은 항상 영어 원본이며, 둘이 다르면 번역본을 고친다.
- `workspace/`와 `outputs/`의 보고서 내용은 이미 한국어이므로 번역하지 않는다.
- `.md`가 아닌 파일(`settings.json`, `.py`)은 번역하지 않는다.
