# Day 1: 환경 세팅(uv) + Python 실행·print·주석

## 🎯 오늘의 목표

- **uv**로 Python 환경을 만들고, 터미널에서 **Python을 실행**해 보며 **print**와 **주석**을 써 본다.

---

## ✅ 오늘 할 일 (순서대로)

### 1. uv 설치 확인

- **할 일**: 터미널에서 `uv --version`을 입력해 uv가 설치되어 있는지 확인한다. 없으면 [uv 공식 문서](https://docs.astral.sh/uv/)에서 설치 방법을 따라 설치한다.
- **완료 조건**: `uv --version`이 에러 없이 버전을 출력한다.

### 2. 가상환경 만들고 Python 실행

- **할 일**: `day01/` 폴더로 이동한 뒤 `uv venv`를 실행해 가상환경을 만든다. 그다음 `uv run python --version`으로 Python 버전이 나오는지 확인한다.
- **완료 조건**: `uv run python --version`이 예를 들어 `Python 3.12.x`처럼 출력된다.

### 3. 첫 번째 .py 파일 작성

- **할 일**: `day01/` 안에 `hello.py` 파일을 만든다. 안에 **한 줄**: `print("Hello, Python")` 을 넣고 저장한다. **주석**으로 `# 이건 출력하는 코드입니다` 같은 문장을 한 줄 넣어도 된다. 터미널에서 `uv run python hello.py`로 실행한다.
- **완료 조건**: `uv run python hello.py`를 실행했을 때 `Hello, Python`이 터미널에 출력된다.

---

## 📌 참고

- **print( ... )**: 괄호 안의 내용을 터미널에 출력한다.
- **#**: 그 줄의 뒤쪽은 주석(실행되지 않음).

---

## ✅ 체크리스트 (할 일 완료 후 표시)

- [ ] **uv**: `uv --version` 확인했고, `uv venv` 후 `uv run python --version`이 동작한다.
- [ ] **hello.py**: `print("Hello, Python")`이 들어 있고, 실행 시 문구가 출력된다.
