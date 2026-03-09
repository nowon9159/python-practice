# Day 9: Linked List 패턴 — Fast/Slow Pointer (Cycle Detection)

## 🎯 오늘의 목표

- **Fast/Slow Pointer**로 cycle detection을 이해하고, **Reverse Linked List**와 **Linked List Cycle**을 풀어 본다.

---

## ✅ 오늘 할 일 (순서대로)

### 1. Reverse Linked List 풀이

- **할 일**: `phase1-cs-basics/algorithms/linked-list/`(또는 `day09/`)에 `reverse_linked_list.py`를 만든다.
  - **문제**: 단방향 연결 리스트를 in-place로 역순으로 만든다. (prev, curr, next 포인터 3개 활용)
  - **조건**: docstring(접근법, 시간/공간복잡도), 테스트 케이스 3개 이상(빈 리스트, 노드 1개, 여러 노드).
- **완료 조건**: 로컬/제출 테스트 통과.

### 2. Linked List Cycle 풀이

- **할 일**: 같은 폴더에 `linked_list_cycle.py`를 만든다.
  - **문제**: Cycle 여부 판별 (I). (선택) Cycle 시작 노드 반환 (II). **Fast/Slow Pointer**: slow 1칸, fast 2칸, 만나면 cycle 있음.
  - **조건**: docstring에 Fast/Slow 원리 간단히, 테스트 케이스(cycle 있음/없음).
- **완료 조건**: 로컬/제출 테스트 통과.

### 3. Fast/Slow 설명 + Anki

- **할 일**: "Fast/Slow Pointer로 cycle을 어떻게 찾는가?(만나면 cycle, null이면 없음)"를 2~3문장으로 정리. Anki에 **Fast/Slow Pointer 카드 1장** 추가.
- **완료 조건**: 원리를 말로 설명할 수 있고, Anki에 반영했다.

---

## 📌 참고 (복습할 개념)

- **Cycle detection (Fast/Slow)**: slow 포인터는 한 칸씩, fast는 두 칸씩 이동한다. 리스트에 cycle이 있으면 fast가 결국 slow를 "한 바퀴 돌아서" 따라잡아 **같은 노드에서 만난다**. cycle이 없으면 fast가 먼저 null에 도달한다. 만나면 cycle 있음, null이면 없음으로 판별할 수 있다.
- **Reverse**: **prev**, **curr**, **next** 세 포인터를 둔다. curr의 next를 prev로 바꾸기 전에 "다음 노드"를 next에 저장해 두고, 한 칸씩 prev←curr, curr←next로 밀어 가면 한 번 순회로 역순이 된다. 순서를 잘못 바꾸면 링크가 끊기므로 그리면서 확인하는 것이 좋다.

---

## ✅ 체크리스트 (할 일 완료 후 표시)

- [ ] **Reverse Linked List**: 풀이 파일 작성, 테스트 통과함.
- [ ] **Linked List Cycle**: Fast/Slow 풀이 파일 작성, 테스트 통과함.
- [ ] **Anki**: Fast/Slow Pointer 조건 카드 1장 추가함.
