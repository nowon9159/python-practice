# Day 8: Linked List — 단방향·이중 연결 리스트 구현

## 🎯 오늘의 목표

- **Singly Linked List**와 **Doubly Linked List**를 직접 구현하고, append/prepend/delete/traverse(및 reverse)를 동작시킨다.

---

## ✅ 오늘 할 일 (순서대로)

### 1. 단방향 연결 리스트 구현

- **할 일**: `day08/` 안에 `singly_linked_list.py`를 만든다.
  - **구현 항목**: `Node`(value, next), 리스트는 `head` 유지. **append**, **prepend**, **delete_by_value**(처음 나오는 값 삭제), **traverse**(전체 출력 또는 리스트로 반환).
  - **엣지**: 빈 리스트에서 delete, head/tail이 바뀌는 경우 처리.
- **완료 조건**: append → traverse로 순서 확인, prepend 후 head 변경 확인, delete_by_value 후 traverse로 결과 확인. 빈 리스트·노드 1개인 경우 동작 확인.

### 2. 이중 연결 리스트 구현

- **할 일**: 같은 폴더에 `doubly_linked_list.py`를 만든다.
  - **구현 항목**: `Node`(value, prev, next), **append**, **prepend**, **delete_by_value**, **traverse**. (선택) **reverse** in-place.
  - **엣지**: 빈 리스트, head/tail 갱신, prev/next 쌍 맞추기.
- **완료 조건**: 위 연산들이 모두 동작하고, reverse 구현 시 traverse로 역순 확인.

### 3. Anki 카드 추가

- **할 일**: "Linked List에서 삽입/삭제가 O(?)인 이유(배열과 비교)" 카드 **1장** 추가.
- **완료 조건**: Week 2 덱에 반영했다.

---

## 📌 참고 (복습할 개념)

- Node 구조, head/tail 관리
- 삽입/삭제 시 포인터 갱신 순서 (그리기 권장)
- 배열 vs 연결 리스트 접근/삽입/삭제 복잡도

---

## ✅ 체크리스트 (할 일 완료 후 표시)

- [ ] **단방향**: append, prepend, delete_by_value, traverse 구현 완료, 엣지케이스 확인함.
- [ ] **이중**: 동일 연산 + (선택) reverse 구현 완료, 동작 확인함.
- [ ] **Anki**: Linked List 삽입/삭제 복잡도 카드 1장 추가함.
