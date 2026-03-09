# Day 17: 그래프 패턴 — Island (Connected Components)

## 🎯 오늘의 목표

- **Connected Components** 패턴(격자에서 묶음 개수)을 복습하고, **Number of Islands**와 **Clone Graph**를 풀어 본다.

---

## ✅ 오늘 할 일 (순서대로)

### 1. Island 패턴 템플릿 정리

- **할 일**: `day17/` 안에 `island_template.py` 또는 `notes.md`를 만든다. **2D grid**에서 "1"인 칸만 방문해 컴포넌트 개수를 세는 **의사코드 또는 코드**를 적는다.
  - 이중 for로 (r, c) 순회 → 값이 1이고 미방문이면 DFS/BFS 시작, 카운트 +1. 4방(상하좌우) 이동, visited 집합 또는 grid 값 변경으로 방문 표시.
- **완료 조건**: "이중 for + (r,c)에서 DFS/BFS 호출 + 방문 체크"가 한 블록으로 정리되어 있다.

### 2. Number of Islands 풀이

- **할 일**: `phase1-cs-basics/algorithms/graph/`(또는 `day17/`)에 `number_of_islands.py`를 만든다.
  - **문제**: 2D grid에서 '1'이 상하좌우로 연결된 컴포넌트(섬) 개수 반환.
  - **조건**: docstring, 테스트 케이스 3개 이상(빈 grid, 전부 1, 전부 0 등).
- **완료 조건**: 로컬/제출 테스트 통과.

### 3. Clone Graph 풀이

- **할 일**: 같은 폴더에 `clone_graph.py`를 만든다.
  - **문제**: 그래프를 복제하여 반환. 노드마다 이웃 리스트가 있을 때, **방문 맵**(원본 노드 → 새 노드)을 두고 BFS/DFS로 복제.
  - **조건**: docstring, 테스트(작은 그래프로 복제 후 구조 동일 여부).
- **완료 조건**: 로컬/제출 테스트 통과.

### 4. Anki 카드 추가

- **할 일**: "Connected Components / Island 패턴: 이중 for + (r,c)에서 DFS/BFS, 방문 체크" **카드 1장** 추가.
- **완료 조건**: Week 3 덱에 반영했다.

---

## 📌 참고 (복습할 개념)

- **2D grid에서 인접**: 한 칸 (r, c)의 이웃은 **4방** (r±1, c), (r, c±1) 또는 **8방**(대각선 포함). 격자 밖이거나 조건(예: 값이 1만 허용)에 안 맞으면 스킵한다.
- **Connected Components(섬 개수)**: 이중 for로 모든 (r, c)를 돌면서, "조건을 만족하고 아직 방문 안 한 칸"에서 **DFS 또는 BFS**를 한 번 시작한다. 한 번 시작할 때마다 컴포넌트 하나이므로 카운트를 1 올린다. **방문 표시**는 set에 (r,c)를 넣거나, grid 값을 바꿔서 같은 칸을 다시 방문하지 않도록 한다.

---

## ✅ 체크리스트 (할 일 완료 후 표시)

- [ ] **Island 템플릿**: 이중 for + DFS/BFS 패턴을 파일에 적었다.
- [ ] **Number of Islands**: 풀이 파일 작성, 테스트 통과함.
- [ ] **Clone Graph**: 풀이 파일 작성, 테스트 통과함.
- [ ] **Anki**: Connected Components 패턴 카드 1장 추가함.
