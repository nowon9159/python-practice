# Day 2: 변수·기본 타입 (int, float, str, bool)

## 🎯 오늘의 목표

- **변수**에 값을 넣고, **int, float, str, bool** 네 가지 타입을 쓰며, **type()**으로 타입을 확인해 본다.

---

## ✅ 오늘 할 일 (순서대로)

### 1. 변수에 숫자·문자 넣기

- **할 일**: `day02/` 안에 `variables.py`를 만든다. 아래를 **한 줄씩** 넣고 실행해 본다.
  - `name = "내이름"`  (문자열)
  - `age = 20`  (정수)
  - `height = 175.5`  (실수)
  - `is_student = True`  (참/거짓)
  - `print(name, age, height, is_student)`  → 실행 시 네 값이 한 줄에 출력되는지 확인한다.
- **완료 조건**: 위 네 변수를 넣고 `uv run python variables.py`로 실행했을 때 값이 출력된다.

### 2. type()으로 타입 확인

- **할 일**: 같은 파일 아래에 `print(type(age))`, `print(type(name))`, `print(type(height))`, `print(type(is_student))` 를 넣고 다시 실행한다. 각각 `<class 'int'>`, `<class 'str'>`, `<class 'float'>`, `<class 'bool'>` 같은 결과가 나오는지 확인한다.
- **완료 조건**: type() 출력으로 int, str, float, bool이 구분된다.

---

## 📌 참고

- **int**: 정수. **float**: 소수 있는 수. **str**: 문자열(따옴표). **bool**: True / False.

---

## ✅ 체크리스트

- [ ] **변수 4개**: name, age, height, is_student를 넣고 print로 출력했다.
- [ ] **type()**: 네 변수의 타입을 type()으로 출력해 확인했다.
