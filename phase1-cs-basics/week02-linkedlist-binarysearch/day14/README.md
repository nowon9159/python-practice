# Day 14: 주간 복습 + 미니 프로젝트 — 파일시스템 트리 탐색기

## 🎯 오늘의 목표

- Week 2 패턴(Linked List, Binary Search, Tree)을 백지로 정리하고, **파일시스템 트리 탐색기**를 구현한 뒤 Anki를 반영한다.

---

## ✅ 오늘 할 일 (순서대로)

### 1. Week 2 패턴 백지 정리

- **할 일**: **아래 4개** 각각에 대해 참고 없이 **의사코드 또는 핵심 로직 3~5줄**을 `day14/review.md`(또는 백지)에 쓴다.
  1. 단방향/이중 연결 리스트: append, delete 시 포인터 갱신 요약
  2. Fast/Slow Pointer: cycle detection 한 문장
  3. 이진 탐색: 기본 / lower bound / 정답 범위(possible) 한 줄씩
  4. BST delete 세 경우, 트리 BFS vs DFS 한 줄
- **완료 조건**: 4개 모두 적었고, 막힌 부분은 노트로 채웠다.

### 2. 파일시스템 트리 탐색기 구현

- **할 일**: `day14/` 안에 `fs_tree.py`를 만든다.
  - **동작**: 주어진 디렉터리 경로를 받아, 그 안의 디렉터리/파일을 **트리 구조**로 표현한다(예: 노드 = 경로, 자식 = 하위 디렉터리/파일). **BFS** 또는 **DFS** 중 하나로 순회하며 각 노드(경로)를 출력한다. (`os.walk` 사용 가능, 또는 `os.listdir` + 재귀)
  - **실행 예**: `uv run python fs_tree.py /path/to/dir` → 트리 형태로 경로들이 출력됨.
- **완료 조건**: 한 디렉터리 경로를 인자로 주면 트리 순회 결과가 출력되고, BFS/DFS 중 사용한 방식을 주석으로 명시했다.

### 3. Anki Week 2 정리

- **할 일**: Week 2에서 빠진 패턴이 있으면 카드 추가. "Linked List / Binary Search / Tree" 요약 카드 1장이라도 보강.
- **완료 조건**: Week 2 덱이 Day 8~13 패턴을 포함하도록 정리했다.

---

## 📌 참고 (복습 범위)

- **Day 8–9**: Linked List — Node(head/tail), append/prepend/delete 시 포인터 갱신. Fast/Slow Pointer로 cycle detection, prev/curr/next로 reverse.
- **Day 10–11**: Binary Search — 기본(인덱스 반환), lower/upper bound(첫/마지막 위치). 정답 범위: possible(x)가 단조일 때 이진 탐색으로 최소/최대 x 찾기.
- **Day 12–13**: BST — insert/search/delete(자식 0/1/2개), 불변식 left < root < right. 순회: inorder(정렬 순), preorder, postorder. 트리 탐색: BFS(큐, 레벨별), DFS(재귀 또는 스택).

---

## ✅ 체크리스트 (할 일 완료 후 표시)

- [ ] **백지 정리**: 4개 패턴 각각 핵심을 참고 없이 적었다.
- [ ] **파일시스템 트리 탐색기**: 디렉터리를 트리로 표현하고 BFS 또는 DFS로 순회하는 코드를 작성·실행했다.
- [ ] **Anki**: Week 2 패턴이 덱에 반영되었다.
