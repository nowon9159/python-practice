# Day 19: 에러 처리 맛보기 — try / except

## 🎯 오늘의 목표

- **try / except**로 에러가 나도 프로그램이 중단되지 않게 하고, 자주 나오는 **에러 메시지**를 한 번 읽어 본다.

---

## ✅ 오늘 할 일 (순서대로)

### 1. try / except 한 번 쓰기

- **할 일**: `day19/` 안에 `try_except.py`를 만든다.
  - `nums = [1, 2, 3]` 일 때 `print(nums[10])` 은 **IndexError**가 난다. 이걸 `try:` 블록 안에 넣고, 다음에 `except IndexError:` 블록에서 `print("인덱스 범위를 벗어났습니다")` 를 출력하도록 한다. 실행 시 에러 대신 "인덱스 범위를 벗어났습니다"가 나오는지 확인한다.
  - (선택) `d = {"a": 1}` 에서 `d["b"]` 를 하면 **KeyError**. 이걸 try/except로 잡아서 "키가 없습니다"를 출력해 본다.
- **완료 조건**: try/except로 IndexError(또는 KeyError)를 잡아 메시지를 출력했다.

### 2. 에러 메시지 읽기

- **할 일**: 의도적으로 `int("abc")` 를 실행해 **ValueError**가 나게 한다. 터미널에 나오는 에러 메시지(마지막 줄의 ValueError: ...)를 읽고, `day19/notes.md`에 "무슨 에러가 났고, 대략 무슨 뜻인지" 1문장으로 적어 둔다.
- **완료 조건**: ValueError를 한 번 보고, 에러 종류와 의미를 한 줄 메모했다.

---

## 📌 참고

- **try:** 실행할 코드. **except 에러종류:** 에러가 났을 때 실행할 코드.
- **IndexError**: 리스트/문자열 인덱스 범위 초과. **KeyError**: 딕셔너리에 없는 키. **ValueError**: 변환 불가한 값(예: int("abc")).

---

## ✅ 체크리스트

- [ ] **try/except**: IndexError 또는 KeyError를 잡아 메시지를 출력했다.
- [ ] **에러 메시지**: ValueError를 보고 한 줄 메모했다.
