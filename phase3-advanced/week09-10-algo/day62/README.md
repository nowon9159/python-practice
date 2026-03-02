# Day 62: Advanced Graph — MST (Kruskal, Prim)

## 🎯 오늘의 목표

MST(최소 신장 트리) 개념을 복습하고, Kruskal(엣지 정렬 + Union-Find)과 Prim(힙 사용)을 구현한 뒤 MST 문제 1~2개를 푼다.

---

## ✅ 오늘 할 일 (순서대로)

### 1. Kruskal 구현

- **할 일**: `phase3-advanced/week09-10-algo/day62/` 안에 `kruskal.py`를 만든다.
  - **Union-Find**: 사이클 감지용 `UnionFind` 클래스 (또는 별도 파일에서 import).
  - **함수**: `kruskal(n: int, edges: list[tuple[int,int,int]]) -> int` — 가중치 합 반환. 엣지를 가중치 오름차순 정렬 후 Union-Find로 사이클 없이 추가.
- **완료 조건**: 예제 그래프(정점 4개 이상)로 실행해 MST 가중치 합이 올바르게 나온다.

### 2. Prim 구현

- **할 일**: 같은 폴더에 `prim.py`를 만든다.
  - **함수**: `prim(n: int, adj: list[list[tuple[int,int]]]) -> int` — 인접 리스트(정점, 가중치), MST 가중치 합 반환. heapq로 최소 가중치 간선 확장.
- **완료 조건**: Kruskal과 동일 입력에 대해 같은 MST 비용이 나온다.

### 3. 문제 풀이 및 Anki

- **할 일**: LeetCode/NeetCode MST 유형 문제 1~2개 풀이. `day62/`에 풀이 파일 또는 링크 정리. Anki에 "MST", "Kruskal vs Prim", "O(E log E) vs O(E log V)" 카드 추가.
- **완료 조건**: Kruskal vs Prim 차이를 설명할 수 있고, 두 구현이 완료되었으며 Anki 카드가 추가되어 있다.

---

## 📌 참고 (복습할 개념)

- MST: 모든 정점 연결, 가중치 합 최소, 트리이므로 사이클 없음
- Kruskal: O(E log E), 엣지 정렬 + Union-Find
- Prim: O(E log V), 한 정점에서 시작해 가장 가까운 정점 확장(힙)

---

## ✅ 체크리스트 (할 일 완료 후 표시)

- [ ] **Kruskal**: `kruskal.py` 구현·실행으로 MST 비용 확인함
- [ ] **Prim**: `prim.py` 구현·동일 입력에 Kruskal과 같은 결과 확인함
- [ ] **문제·Anki**: MST 문제 1~2개 풀이, Anki 카드 추가함
