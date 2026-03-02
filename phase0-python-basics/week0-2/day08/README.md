# Day 8: 딕셔너리(dict) — {}, key-value, d[key], d.get(), in

## 🎯 오늘의 목표

- **딕셔너리**를 만들고, **키로 값**을 찾으며, **get()**과 **in**을 써 본다.

---

## ✅ 오늘 할 일 (순서대로)

### 1. 딕셔너리 만들고 키로 접근

- **할 일**: `day08/` 안에 `dict_basics.py`를 만든다.
  - `person = {"name": "홍길동", "age": 20, "city": "서울"}` 로 만든다.
  - `print(person["name"])` → "홍길동", `print(person["age"])` → 20 이 나오는지 확인한다.
  - `person["email"] = "hong@example.com"` 으로 새 키-값을 추가한 뒤 `print(person)` 으로 네 개가 다 나오는지 확인한다.
- **완료 조건**: person에서 키로 값을 꺼내고, 새 키를 추가해 출력했다.

### 2. get()과 in

- **할 일**: 같은 파일에 `print(person.get("name"))` → "홍길동", `print(person.get("phone"))` → None(또는 아무것도 안 나옴)을 확인한다. `get("phone", "없음")` 처럼 기본값을 주면 "없음"이 나오는지 확인한다.
  - `if "city" in person: print(person["city"])` 로 "city" 키가 있을 때만 출력되게 한다.
- **완료 조건**: get()으로 있으면 값, 없으면 None(또는 기본값)이 나오고, in으로 키 존재 여부를 썼다.

---

## 📌 참고

- **딕셔너리**: 키-값 쌍. `d[key]` 로 값 조회, 없으면 에러. `d.get(key)` 는 없으면 None(또는 기본값).
- **키 in 딕셔너리**: 그 키가 있으면 True.

---

## ✅ 체크리스트

- [ ] **d[key], 추가**: person에서 값 조회하고, email 키를 추가했다.
- [ ] **get(), in**: get()과 in을 한 번씩 사용했다.
