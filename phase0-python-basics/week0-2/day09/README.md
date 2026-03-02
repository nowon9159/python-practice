# Day 9: 딕셔너리 순회 — for k in d, items(), keys(), values()

## 🎯 오늘의 목표

- 딕셔너리를 **for**로 돌면서 **키**, **값**, **키와 값 쌍**을 한 번씩 출력해 본다.

---

## ✅ 오늘 할 일 (순서대로)

### 1. for k in d, keys(), values()

- **할 일**: `day09/` 안에 `dict_loop.py`를 만든다.
  - `d = {"a": 1, "b": 2, "c": 3}` 을 만든다.
  - `for k in d: print(k)` 로 키만 출력된다 (a, b, c). `for k in d.keys():` 도 같은 결과인지 확인한다.
  - `for v in d.values(): print(v)` 로 1, 2, 3이 나오는지 확인한다.
- **완료 조건**: for로 키만, values()로 값만 출력했다.

### 2. items()로 키와 값 함께

- **할 일**: 같은 파일에 `for k, v in d.items(): print(k, v)` 를 넣어 (a 1), (b 2), (c 3)처럼 키와 값이 쌍으로 출력되는지 확인한다.
- **완료 조건**: items()로 키-값 쌍을 한 번씩 출력했다.

---

## 📌 참고

- **d.keys()**: 키들. **d.values()**: 값들. **d.items()**: (키, 값) 쌍들.
- **for k, v in d.items():** → k에 키, v에 값이 들어간다.

---

## ✅ 체크리스트

- [ ] **키·값 순회**: for k in d, for v in d.values() 를 실행했다.
- [ ] **items()**: for k, v in d.items() 로 쌍을 출력했다.
