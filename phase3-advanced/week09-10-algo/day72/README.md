# Day 72: Python 심화 — 제너레이터·이터레이터 내부 구조

## 🎯 오늘의 목표

이터레이터 프로토콜(__iter__, __next__, StopIteration)과 제너레이터(yield, lazy evaluation)를 이해하고, 직접 구현한 이터레이터·제너레이터 예제로 동작을 확인한다.

---

## ✅ 오늘 할 일 (순서대로)

### 1. 이터레이터 클래스 구현

- **할 일**: `phase3-advanced/week09-10-algo/day72/` 안에 `iterator_example.py`를 만든다. **__iter__**와 **__next__**를 구현한 이터레이터 클래스를 하나 만든다. (예: range 비슷한 것 — start, stop, step 받아서 next() 시 다음 값 반환, StopIteration 발생.) for 루프로 돌려 보기.
- **완료 조건**: `for x in MyRange(...):` 형태로 동작하고, iter() → next() 호출 순서를 설명할 수 있다.

### 2. 제너레이터 예제

- **할 일**: 같은 폴더에 `generator_example.py`를 만든다. **yield**를 사용한 제너레이터 함수를 하나 이상 만든다. (예: 무한 스트림(무한 수열), 또는 여러 단계를 거치는 파이프라인 — yield로 값 전달.) next() 호출 시 yield까지 진행 후 일시 정지하는지 확인.
- **완료 조건**: 제너레이터로 next()/for로 값을 소비할 수 있고, "일시 정지·재개" 동작을 설명할 수 있다.

### 3. 정리 및 Anki

- **할 일**: `day72/notes.md`에 **이터레이터 vs 제너레이터** 차이를 적는다. (이터레이터: 클래스로 __iter__/__next__, 제너레이터: yield 함수, lazy.) Anki에 "이터레이터 프로토콜", "제너레이터 yield 동작" 카드 추가.
- **완료 조건**: __iter__/__next__ 동작과 yield 동작을 문서로 설명했고, Anki 카드가 추가되어 있다.

---

## 📌 참고 (복습할 개념)

- 이터레이터: __iter__ → self 반환, __next__ → 값 또는 StopIteration
- for 루프: iter() → next() 반복
- 제너레이터: yield로 값 반환·일시 정지, next() 시 yield까지 진행 후 재개

---

## ✅ 체크리스트 (할 일 완료 후 표시)

- [ ] **이터레이터**: `iterator_example.py` 구현·for/next 동작 확인함
- [ ] **제너레이터**: `generator_example.py` 구현·yield 동작 확인함
- [ ] **정리·Anki**: notes.md 이터레이터 vs 제너레이터, Anki 카드 추가함
