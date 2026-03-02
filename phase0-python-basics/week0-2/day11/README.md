# Day 11: 함수 정의 — def, 인자, return, 호출

## 🎯 오늘의 목표

- **def**로 함수를 만들고, **인자**를 넘기며 **return**으로 결과를 받아 본다.

---

## ✅ 오늘 할 일 (순서대로)

### 1. 인자 하나, return 하나

- **할 일**: `day11/` 안에 `functions.py`를 만든다.
  - `def greet(name):` 다음 줄에 들여쓰기해서 `return "Hello, " + name` 을 넣는다. 아래에서 `result = greet("Python")` 하고 `print(result)` 하면 "Hello, Python"이 나오는지 확인한다.
- **완료 조건**: greet("Python")을 호출해 "Hello, Python"을 받아 출력했다.

### 2. 인자 두 개, 숫자 return

- **할 일**: 같은 파일에 `def add(a, b):` 와 `return a + b` 를 넣는다. `print(add(3, 5))` → 8 이 나오는지 확인한다.
- **완료 조건**: add(3, 5)가 8을 반환한다.

---

## 📌 참고

- **def 함수이름(인자1, 인자2):** 다음 줄부터 들여쓰기된 코드가 함수 몸통.
- **return 값** 으로 결과를 돌려주고 함수를 끝낸다.

---

## ✅ 체크리스트

- [ ] **greet**: 인자 하나 받아 return으로 문자열을 반환했다.
- [ ] **add**: 인자 두 개 받아 합을 return했다.
