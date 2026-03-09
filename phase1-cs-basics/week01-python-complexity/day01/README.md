# Day 1: Python 환경 + 타입힌트·dataclass·collections

## 🎯 오늘의 목표

- uv로 Python 환경을 세팅하고, 타입힌트·dataclass·collections를 복습한 뒤 **예제 코드**와 **로그 파서 CLI**를 만든다.

---

## ✅ 오늘 할 일 (순서대로)

### 1. 환경 세팅

- **할 일**: 이 레포(또는 `day01/` 상위)에서 아래를 실행한다.
  - `uv venv` → 가상환경 생성
  - `uv init` → `pyproject.toml` 생성 (이미 있으면 생략)
  - `uv add --dev ruff` → 린터/포매터 추가
  - `uv run python --version` → 정상 실행 확인
- **완료 조건**: `uv sync` 후 `uv run python --version`이 에러 없이 나온다.

### 2. 예제 코드 작성

- **할 일**: `day01/` 안에 예제 파일 하나(예: `examples.py`)를 만들고 **아래 세 가지를 모두** 넣는다.
  1. **타입힌트**: `List`, `Dict`, `Optional` 등이 붙은 함수를 **최소 2개** (예: `def parse(s: str) -> list[str]:`).
  2. **dataclass**: `@dataclass`로 필드가 3개 이상인 클래스 **1개** (필요하면 `__post_init__` 사용).
  3. **collections**: `defaultdict`, `Counter`, `deque`를 **각각 최소 1번씩** 사용하는 코드.
- **완료 조건**: 위 세 가지가 한 파일에 들어 있고, `uv run python examples.py`로 실행해도 오류가 없다.

### 3. 로그 파서 CLI (미니프로젝트)

- **할 일**: `day01/` 안에 `log_parser.py`(이름 변경 가능)를 만든다.
  - **동작**: 파일 경로를 인자로 받아, 그 로그 파일을 읽고 **레벨 / 타임스탬프 / 메시지** 등을 파싱한 뒤, 터미널에 요약 또는 필터 결과를 출력한다.
  - **실행 예**: `uv run python log_parser.py path/to/logfile.log`
- **완료 조건**: 위처럼 실행했을 때 파싱 결과가 터미널에 출력된다.

---

## 📌 참고 (복습할 개념)

- **uv**: Python 패키지·가상환경 도구. `uv venv`로 가상환경을 만들고, `uv init`으로 프로젝트 초기화(pyproject.toml 생성), `uv add`로 의존성 추가, `uv run python ...`으로 해당 환경에서 스크립트를 실행한다. `uv sync`로 lock 파일 기준으로 의존성을 맞춘다.
- **타입힌트**: 함수 인자와 반환값에 타입을 적어 두는 것. `typing` 모듈의 `List`, `Dict`, `Optional`, `Union` 등을 쓰고, 함수 시그니처에 일관되게 붙이면 나중에 읽기와 자동완성이 수월해진다.
- **dataclass**: `@dataclass`를 붙이면 `__init__`, `__repr__` 등을 자동 생성해 준다. 필드에 기본값을 줄 수 있고, 초기화 직후 처리가 필요하면 `__post_init__`에 넣는다.
- **collections**: `defaultdict`는 키가 없을 때 기본값을 쓰고, `Counter`는 요소 개수를 세기 좋고, `deque`는 앞뒤 삽입/삭제가 O(1)인 큐·스택에 적합하다. 로그 파싱에서는 레벨별 카운트·빈도·최근 N줄 버퍼 등에 쓸 수 있다.

---

## ✅ 체크리스트 (할 일 완료 후 표시)

- [ ] **환경**: `uv venv` + `uv sync` 완료, `uv run python --version` 확인함
- [ ] **예제**: 타입힌트 함수 2개 + dataclass 1개 + defaultdict/Counter/deque 각 1회 이상 포함한 파일 작성함
- [ ] **로그 파서**: `uv run python log_parser.py <경로>` 로 실행 시 파싱 결과가 출력됨
