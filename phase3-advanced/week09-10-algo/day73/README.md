# Day 73: Python 심화 — functools, itertools 완전 정복

## 🎯 오늘의 목표

functools(reduce, lru_cache, partial, wraps)와 itertools(chain, combinations, permutations, groupby, islice 등)를 예제로 다루고, 자주 쓰는 함수 목록과 사용처를 정리해 Day 74 복습 시 참고할 수 있게 한다.

---

## ✅ 오늘 할 일 (순서대로)

### 1. functools 예제

- **할 일**: `phase3-advanced/week09-10-algo/day73/` 안에 `functools_demo.py`를 만든다. **reduce**, **partial**, **lru_cache**를 각각 사용하는 예제를 넣는다. (예: reduce로 fold/합·곱, partial로 인자 고정, lru_cache로 메모이제이션.) 필요하면 **wraps** 사용 예(데코레이터 보존)도 한 줄.
- **완료 조건**: 세 함수(또는 네 개)가 한 파일에서 실행 가능하고, 각각의 역할이 주석으로 적혀 있다.

### 2. itertools 예제

- **할 일**: 같은 폴더에 `itertools_demo.py`를 만든다. **chain**, **combinations**, **permutations**, **groupby**, **islice** 중 최소 4개를 사용하는 예제를 넣는다. (중첩 루프 대신 조합/순열/그룹핑 등.)
- **완료 조건**: 각 함수별로 입력·출력 예가 한 번씩 실행되어 결과가 확인 가능하다.

### 3. 정리·선택 문제·Anki

- **할 일**: `day73/notes.md`에 **자주 쓰는 함수 목록 + 사용처**를 표로 정리한다. (선택) 알고리즘 문제 1개를 itertools/functools로 풀어 본 뒤 풀이를 같은 폴더에 저장. Anki에 "functools 요약", "itertools 요약" 카드 추가.
- **완료 조건**: notes.md가 Day 74 복습 시 참고용으로 읽을 수 있고, Anki 카드가 추가되어 있다.

---

## 📌 참고 (복습할 개념)

- functools: reduce(fold), lru_cache(메모이제이션), partial(인자 고정), wraps(메타데이터 보존)
- itertools: chain, combinations, permutations, groupby, islice — 중첩 루프 대체

---

## ✅ 체크리스트 (할 일 완료 후 표시)

- [ ] **functools**: `functools_demo.py`에 reduce/partial/lru_cache 예제 작성·실행함
- [ ] **itertools**: `itertools_demo.py`에 4개 이상 함수 예제 작성·실행함
- [ ] **정리·Anki**: notes.md 함수 목록·사용처 정리, Anki 카드 추가함
