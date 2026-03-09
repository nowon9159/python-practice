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

- **Node 구조**: 단방향은 (value, next), 이중은 (value, prev, next). 리스트는 **head**(그리고 tail 있으면 tail)만 들고 있으면 된다. 새 노드 추가·삭제 시 head/tail이 바뀌는 경우(빈 리스트에서 첫 삽입, 마지막 노드 삭제 등)를 꼭 처리해야 한다.
- **삽입/삭제 시 포인터 갱신**: "어떤 노드의 next(또는 prev)를 먼저 바꿀지" 순서가 중요하다. 잘못하면 기존 링크를 잃어버린다. 종이에 화살표 그려 가며 한 단계씩 따라가 보면 실수하기 쉽다.
- **배열 vs 연결 리스트**: 배열은 인덱스로 **접근 O(1)**, 중간 삽입/삭제는 요소를 밀어야 해서 **O(n)**. 연결 리스트는 **접근**하려면 head부터 따라가야 해서 O(n), 하지만 **삽입/삭제**할 위치만 알면 포인터만 바꿔서 **O(1)**(단, 그 위치까지 가는 비용은 별도).

---

## ✅ 체크리스트 (할 일 완료 후 표시)

- [ ] **단방향**: append, prepend, delete_by_value, traverse 구현 완료, 엣지케이스 확인함.
- [ ] **이중**: 동일 연산 + (선택) reverse 구현 완료, 동작 확인함.
- [ ] **Anki**: Linked List 삽입/삭제 복잡도 카드 1장 추가함.
