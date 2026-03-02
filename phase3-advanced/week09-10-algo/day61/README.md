# Day 61: Advanced Graph — Bellman-Ford, Floyd-Warshall

## 🎯 오늘의 목표

Bellman-Ford(음수 간선 허용, 단일 출발 최단경로, V-1번 relaxation)와 Floyd-Warshall(모든 쌍 최단경로, O(V³))을 이해하고 구현한다.

---

## ✅ 오늘 할 일 (순서대로)

### 1. Bellman-Ford 구현

- **할 일**: `phase3-advanced/week09-10-algo/day61/` 안에 `bellman_ford.py`를 만든다.
  - **함수**: `bellman_ford(n: int, edges: list[tuple[int,int,int]], start: int) -> list[int]` — `n` 정점, `edges`는 (u, v, w), `start`에서의 최단 거리 리스트 반환.
  - **음수 사이클 감지**: V번째 relaxation에서도 갱신되면 음수 사이클 존재 → 예외 또는 별도 플래그 반환.
- **완료 조건**: `if __name__ == "__main__"`에서 예제 그래프(음수 간선 포함 1개, 음수 사이클 없는 예 1개)로 실행해 거리 배열이 올바르게 나온다. 음수 사이클이 있는 입력에 대해 감지 결과가 출력된다.

### 2. Floyd-Warshall 구현

- **할 일**: 같은 폴더에 `floyd_warshall.py`를 만든다.
  - **함수**: `floyd_warshall(n: int, edges: list[tuple[int,int,int]]) -> list[list[int]]` — n×n 최단 거리 행렬 반환. 간선 없으면 inf.
  - 중간 노드 k를 거치는 경로로 dp 갱신 (3중 루프).
- **완료 조건**: 예제 그래프(정점 4개 이상)로 실행해 모든 쌍 최단거리 행렬이 맞게 출력된다.

### 3. 차이 정리 및 Anki

- **할 일**: `day61/` 안에 `notes.md`를 만들고 **Bellman-Ford vs Floyd-Warshall** 비교를 적는다. (적용 조건, 시간복잡도, 음수 간선/사이클 처리.) NeetCode/LeetCode에서 각 알고리즘에 맞는 문제 1개씩 풀이(선택). Anki에 "Bellman-Ford", "Floyd-Warshall" 카드 추가.
- **완료 조건**: 두 알고리즘의 차이·적용 조건을 문서에 적었고, Anki 카드가 추가되어 있다.

---

## 📌 참고 (복습할 개념)

- Bellman-Ford: V-1번 relaxation, V번째에도 갱신되면 음수 사이클
- Floyd-Warshall: dp[k][i][j] = min(기존, i→k→j), O(V³)
- 단일 출발 vs 모든 쌍, 음수 간선 허용 시 Bellman-Ford/Floyd-Warshall 사용

---

## ✅ 체크리스트 (할 일 완료 후 표시)

- [ ] **Bellman-Ford**: `bellman_ford.py` 구현·실행 확인, 음수 사이클 감지 동작함
- [ ] **Floyd-Warshall**: `floyd_warshall.py` 구현·실행으로 모든 쌍 거리 확인함
- [ ] **정리·Anki**: `notes.md` 비교 정리, Anki 카드 추가함
