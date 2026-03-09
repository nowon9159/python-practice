# Day 21: 주간 복습 + 그래프 패턴 정리

## 🎯 오늘의 목표

- Week 3(힙·그래프) 패턴을 백지로 정리하고, **그래프 패턴 카탈로그**를 작성한 뒤 Anki를 반영한다.

---

## ✅ 오늘 할 일 (순서대로)

### 1. 그래프 패턴 카탈로그 작성

- **할 일**: `phase1-cs-basics/review/`(또는 `day21/`)에 `graph_pattern_catalog_week3.md`를 만든다. **아래 6가지** 각각에 대해 "언제 쓰는가, 입력/출력, 시간복잡도 한 줄"을 표로 또는 리스트로 적는다.
  1. Heap (Top K, 스케줄링)
  2. 인접 리스트 vs 인접 행렬
  3. 그래프 BFS/DFS
  4. Island / Connected Components (격자)
  5. 위상정렬 (Kahn, DAG)
  6. Union-Find (연결 요소, 사이클)
  7. Dijkstra (non-negative 최단경로)
- **완료 조건**: 7개 패턴이 "문제 유형 → 이 알고리즘" 형태로 한눈에 보인다.

### 2. 패턴 백지 재현

- **할 일**: **위 7개 중 4개 이상**을 참고 없이 **의사코드 또는 핵심 로직 3~5줄**씩 백지(또는 `day21/review.md`)에 쓴다. (Kahn의 in-degree 0 큐, Union-Find find/union, Dijkstra heap 루프, Island 이중 for + DFS 등)
- **완료 조건**: 4개 이상 적었고, 막힌 부분은 카탈로그/노트로 채웠다.

### 3. Anki Week 3 정리 + 취약 문제 재풀이

- **할 일**: Week 3 패턴 중 빠진 카드 추가. **Day 15~20 중 한 번에 풀지 못했던 문제** 1개를 골라 해설 최소한만 보고 다시 풀어 본다.
- **완료 조건**: Anki 덱에 Week 3가 반영되었고, 재풀이한 문제에 대해 "왜 막혔는지" 1줄 메모해 뒀다.

---

## 📌 참고 (복습 범위)

- **Day 15**: Heap(min-heap, heapq), K번째 큰 원소는 heap 크기 k 유지, Task Scheduler는 빈도·cooldown을 heap으로 스케줄링.
- **Day 16–17**: 인접 리스트(희소)·인접 행렬(has_edge O(1)), 그래프 BFS/DFS·방문 체크. Island 패턴: 2D grid 이중 for + (r,c)에서 DFS/BFS, 방문한 컴포넌트 재방문 안 함.
- **Day 18**: 위상정렬은 DAG에서만. Kahn: in-degree 0인 노드부터 큐에서 꺼내 제거, 이웃 in-degree 감소. 사이클 있으면 결과 길이 < V.
- **Day 19**: Union-Find — find(루트)+path compression, union(두 집합 합침). 연결 요소 개수·사이클 감지에 사용.
- **Day 20**: Dijkstra — non-negative 가중치, heap으로 (거리, 노드), relaxation으로 최단거리 갱신.

---

## ✅ 체크리스트 (할 일 완료 후 표시)

- [ ] **카탈로그**: 7개 패턴을 "언제 쓰는가" 포함해 문서로 작성했다.
- [ ] **백지 재현**: 4개 이상 패턴을 참고 없이 적었다.
- [ ] **Anki + 재풀이**: Week 3 Anki 반영, 취약 문제 1개 재풀이 및 복기했다.
