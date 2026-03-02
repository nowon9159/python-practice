# Day 64: Segment Tree + Binary Indexed Tree (Fenwick)

## 🎯 오늘의 목표

Segment Tree(구간 쿼리 + point update, O(log n))와 Fenwick Tree(구간 합 특화)를 구현하고, Range Sum Query 등 관련 문제 1~2개를 푼다.

---

## ✅ 오늘 할 일 (순서대로)

### 1. Segment Tree 구현

- **할 일**: `phase3-advanced/week09-10-algo/day64/` 안에 `segment_tree.py`를 만든다.
  - **기능**: 구간 합 또는 구간 최소 중 하나 이상. `build(arr)`, `query(left, right)`, `update(index, value)`.
  - 이진 분할, 리프 = 원소, O(log n) per operation.
- **완료 조건**: 예제 배열로 build 후 query/update 여러 번 수행해 결과가 맞다 (직접 계산 또는 예제와 일치).

### 2. Fenwick Tree (BIT) 구현

- **할 일**: 같은 폴더에 `fenwick.py`를 만든다.
  - **기능**: 구간 합. prefix sum을 LSB 비트로 구간 관리. `add(i, delta)`, `prefix_sum(i)` 또는 `range_sum(l, r)`.
- **완료 조건**: Segment Tree와 동일한 배열·쿼리에 대해 구간 합 결과가 일치한다.

### 3. 차이 정리 및 문제·Anki

- **할 일**: `day64/notes.md`에 Segment Tree vs Fenwick 차이(연산 종류, 복잡도, 구현 난이도) 정리. LeetCode 등에서 Range Sum Query 유형 1~2개 풀이. Anki에 "Segment Tree", "Fenwick" 카드 추가.
- **완료 조건**: 두 구조의 차이·연산 복잡도를 설명할 수 있고, 구현·문제 풀이가 완료되었으며 Anki에 반영했다.

---

## 📌 참고 (복습할 개념)

- Segment Tree: 이진 분할, 리프 = 원소, 구간 합/최소/최대 등
- Fenwick: LSB로 구간 관리, 구간 합에 특화, 구현 간단
- 둘 다 point update + range query O(log n)

---

## ✅ 체크리스트 (할 일 완료 후 표시)

- [ ] **Segment Tree**: `segment_tree.py` 구현·query/update 실행 확인함
- [ ] **Fenwick**: `fenwick.py` 구현·구간 합 결과 확인함
- [ ] **정리·문제·Anki**: notes.md 작성, 관련 문제 1~2개 풀이, Anki 카드 추가함
