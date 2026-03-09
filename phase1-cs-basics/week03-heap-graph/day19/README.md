# Day 19: Union-Find (Disjoint Set) — Path Compression

## 🎯 오늘의 목표

- **Union-Find**를 **path compression**과 함께 구현하고, **Redundant Connection**과 **Number of Connected Components**를 풀어 본다.

---

## ✅ 오늘 할 일 (순서대로)

### 1. Union-Find 클래스 구현

- **할 일**: `day19/` 안에 `union_find.py`를 만든다.
  - **연산**: **find(x)**: x가 속한 집합의 루트(대표) 반환. **union(x, y)**: x와 y가 속한 집합을 합침. **path compression**: find 시 경로 상 노드들이 루트를 가리키도록 갱신.
  - **(선택) rank 또는 size**로 union 시 작은 트리를 큰 트리에 붙이기.
  - **초기화**: 노드 0..n-1 각각이 자기 자신을 부모로 하는 n개 집합.
- **완료 조건**: find/union 여러 번 호출 후, 같은 집합에 속한 노드들은 find가 같은 값을 반환한다. path compression 적용했는지 주석으로 명시.

### 2. Redundant Connection 풀이

- **할 일**: `phase1-cs-basics/algorithms/graph/`(또는 `day19/`)에 `redundant_connection.py`를 만든다.
  - **문제**: 트리에 엣지 하나를 추가한 그래프에서, 제거하면 트리가 되는 엣지(순환 만드는 엣지) 하나 반환. Union-Find로 엣지 순서대로 union하다가 **이미 같은 루트인 두 노드를 잇는 엣지**가 나오면 그게 정답 후보.
  - **조건**: docstring, 테스트 케이스 3개 이상.
- **완료 조건**: 로컬/제출 테스트 통과.

### 3. Number of Connected Components 풀이

- **할 일**: 같은 폴더에 `number_of_connected_components.py`를 만든다.
  - **문제**: 무방향 그래프에서 연결 요소 개수. 모든 엣지에 대해 union한 뒤, **서로 다른 루트 개수**를 센다 (find(i) for i in range(n) → set 크기).
  - **조건**: docstring, 테스트 케이스 3개 이상.
- **완료 조건**: 로컬/제출 테스트 통과.

### 4. Anki 카드 추가

- **할 일**: "Union-Find 언제 쓰는가? (연결 요소 개수, 사이클 감지)" + "path compression이 뭔가" **카드 1장** 추가.
- **완료 조건**: Week 3 덱에 반영했다.

---

## 📌 참고 (복습할 개념)

- **Union-Find**: 노드들을 "서로소 집합(disjoint set)"으로 관리한다. **find(x)**는 x가 속한 집합의 **대표(루트)**를 반환한다. 구현은 parent 배열에서 부모를 따라 루트까지 올라간다. **path compression**은 find하는 경로 위의 노드들을 **직접 루트를 가리키도록** 바꿔 두어, 다음 find가 빨라지게 한다. **union(x, y)**는 x의 루트와 y의 루트를 하나로 합친다(한 루트가 다른 루트의 부모가 되게 함).
- **rank/size**: union할 때 "작은 트리를 큰 트리 아래에" 붙이면 트리 높이가 잘 커지지 않는다. rank(높이 추정)나 size(노드 수)로 비교해서 붙이는 쪽을 정한다. 이렇게 하면 find가 거의 상수에 가깝게 동작한다.

---

## ✅ 체크리스트 (할 일 완료 후 표시)

- [ ] **Union-Find**: find/union + path compression 구현, 동작 확인함.
- [ ] **Redundant Connection**: 풀이 파일 작성, 테스트 통과함.
- [ ] **Number of Connected Components**: 풀이 파일 작성, 테스트 통과함.
- [ ] **Anki**: Union-Find 용도 카드 1장 추가함.
