# Day 12: 트리 기초 — BST 구현 + 순회

## 🎯 오늘의 목표

- **BST**를 직접 구현(insert, search, delete)하고, **Inorder / Preorder / Postorder** 순회를 구현한다.

---

## ✅ 오늘 할 일 (순서대로)

### 1. BST 클래스 구현

- **할 일**: `day12/` 안에 `bst.py`를 만든다.
  - **구현 항목**: `TreeNode`(val, left, right), BST 클래스는 **insert**, **search**, **delete**.
  - **delete 세 경우**: (1) 자식 0개 → 노드 제거, (2) 자식 1개 → 부모가 그 자식을 가리키게, (3) 자식 2개 → 오른쪽 서브트리 최소값(또는 왼쪽 최대값)으로 대체 후 그 노드 delete.
  - **불변식**: 모든 노드에 대해 left < root < right (중복은 규칙 하나 정해 두기).
- **완료 조건**: insert 후 search로 존재 여부 확인, delete 후 search·inorder로 트리 상태 확인. 자식 0/1/2개인 노드 삭제 각각 테스트.

### 2. 세 가지 순회 구현

- **할 일**: 같은 파일(또는 별도)에 **inorder**, **preorder**, **postorder**를 구현한다. 재귀 또는 반복(스택) 둘 다 가능.
  - **inorder**: left → root → right (BST면 정렬 순)
  - **preorder**: root → left → right
  - **postorder**: left → right → root
- **완료 조건**: 동일 트리에 대해 세 순회 결과를 출력해 차이를 확인했다.

### 3. Anki 카드 추가

- **할 일**: "BST 순회: Inorder(정렬), Preorder(복사/구조), Postorder(후처리) 각각의 용도" **카드 1장** 추가.
- **완료 조건**: Week 2 덱에 반영했다.

---

## 📌 참고 (복습할 개념)

- BST 불변식: left < root < right
- delete 시 대체 노드: 오른쪽 서브트리 최소 또는 왼쪽 서브트리 최대

---

## ✅ 체크리스트 (할 일 완료 후 표시)

- [ ] **BST**: insert, search, delete 구현 완료, 자식 0/1/2 삭제 모두 확인함.
- [ ] **순회**: inorder, preorder, postorder 구현 완료, 결과 확인함.
- [ ] **Anki**: BST 순회 용도 카드 1장 추가함.
