# Day 13: 트리 패턴 — BFS (레벨 순회), DFS

## 🎯 오늘의 목표

- **BFS**와 **DFS** 템플릿을 복습하고, **Invert Binary Tree**와 **Maximum Depth of Binary Tree**를 BFS/DFS로 풀어 본다.

---

## ✅ 오늘 할 일 (순서대로)

### 1. Invert Binary Tree 풀이

- **할 일**: `phase1-cs-basics/algorithms/tree/`(또는 `day13/`)에 `invert_binary_tree.py`를 만든다.
  - **문제**: 이진 트리의 left/right를 모든 노드에서 스왑 (DFS 재귀 또는 BFS 큐).
  - **조건**: docstring(접근법, 시간/공간복잡도), 테스트 케이스(빈 트리, 노드 1개, 여러 노드).
- **완료 조건**: 로컬/제출 테스트 통과.

### 2. Maximum Depth of Binary Tree 풀이 (BFS + DFS)

- **할 일**: 같은 폴더에 `maximum_depth_binary_tree.py`를 만든다.
  - **문제**: 루트에서 leaf까지 최대 깊이 반환. **BFS** 버전(레벨 수 세기)과 **DFS** 버전(재귀: 1 + max(left_depth, right_depth)) **둘 다** 구현해 본다.
  - **조건**: docstring에 두 방법 모두 명시, 테스트 케이스 3개 이상.
- **완료 조건**: 두 구현 모두 같은 입력에 같은 결과를 내고, 로컬/제출 테스트 통과.

### 3. BFS/DFS 템플릿 정리 + Anki

- **할 일**: "트리 BFS 템플릿(큐, 레벨 크기 for level-order)"과 "트리 DFS(재귀 = 암시적 스택)"를 2~3문장 + 의사코드로 `day13/notes.md`에 적거나 Anki 뒷면에 넣는다. **BFS vs DFS 언제 쓰는가** 카드 1장 추가.
- **완료 조건**: 두 템플릿을 말로 설명할 수 있고, Anki에 반영했다.

---

## 📌 참고 (복습할 개념)

- BFS: 큐, 레벨별 탐색
- DFS: 재귀 또는 스택, 전위/중위/후위

---

## ✅ 체크리스트 (할 일 완료 후 표시)

- [ ] **Invert Binary Tree**: 풀이 파일 작성, 테스트 통과함.
- [ ] **Maximum Depth**: BFS·DFS 둘 다 구현하고 테스트 통과함.
- [ ] **Anki**: 트리 BFS vs DFS 카드 1장 추가함.
