# Day 15: Heap (우선순위 큐) — heapq, Min/Max Heap

## 🎯 오늘의 목표

- **heapq** 사용법과 Min/Max Heap 트릭을 정리하고, **Kth Largest Element**와 **Task Scheduler**를 풀어 본다.

---

## ✅ 오늘 할 일 (순서대로)

### 1. heapq 사용법 정리

- **할 일**: `day15/` 안에 `heap_notes.py` 또는 `heap_notes.md`를 만든다. 다음을 **코드 또는 문장**으로 적는다.
  - **heappush**, **heappop**, **heapify** 사용 예 (리스트 하나로 min-heap)
  - **Max Heap 흉내**: 값을 음수로 넣어서 heappop 시 다시 양수로 되돌리기 (또는 (우선순위, 값) 튜플로 역순)
- **완료 조건**: "K번째 큰 원소"를 구할 때 heap 크기를 k로 유지하는 패턴이 적혀 있다.

### 2. Kth Largest Element in an Array 풀이

- **할 일**: `phase1-cs-basics/algorithms/heap/`(또는 `day15/`)에 `kth_largest.py`를 만든다.
  - **문제**: 배열에서 k번째로 큰 원소 반환. **Min heap 크기 k** 유지: k개 넘으면 pop해서 작은 것 제거 → 마지막에 heap[0]이 k번째 큰 값.
  - **조건**: docstring(접근법, 시간/공간복잡도), 테스트 케이스 3개 이상.
- **완료 조건**: 로컬/제출 테스트 통과.

### 3. Task Scheduler 풀이

- **할 일**: 같은 폴더에 `task_scheduler.py`를 만든다.
  - **문제**: 같은 태스크 사이에 cooldown n이 있을 때, 전체 완료까지 최소 시간. (최대 빈도 작업을 기준으로 슬롯 계산하거나, heap으로 매 턴 가장 많이 남은 작업 선택)
  - **조건**: docstring, 테스트 케이스 3개 이상.
- **완료 조건**: 로컬/제출 테스트 통과.

### 4. Anki 카드 추가

- **할 일**: "Heap 언제 쓰는가? (Top K, 스케줄링 등)" **카드 1장** 추가. (선택) Max Heap 트릭 한 줄.
- **완료 조건**: Week 3 덱에 반영했다.

---

## 📌 참고 (복습할 개념)

- **Heap 불변식**: 부모 노드 값이 자식보다 작거나 같으면(min-heap) 루트가 최소값이다. 배열로 구현할 때 인덱스 i의 자식은 2i+1, 2i+2, 부모는 (i-1)//2이다. **heappush**는 맨 끝에 넣고 위로 올리며, **heappop**은 루트를 반환하고 맨 끝 원소를 루트로 내려서 아래로 내리며 자리 맞춘다.
- **K번째 큰/작은 원소**: "**Min heap 크기 k**"를 유지하면서 원소를 넣고, k개를 넘기면 pop해서 가장 작은 것을 버린다. 끝나면 heap[0]이 "k번째로 큰 값"이 된다. Top K 문제에서 공간을 O(k)로 줄일 때 자주 쓴다.

---

## ✅ 체크리스트 (할 일 완료 후 표시)

- [ ] **heapq 정리**: Min/Max Heap 사용법을 파일에 적었다.
- [ ] **Kth Largest**: 풀이 파일 작성, 테스트 통과함.
- [ ] **Task Scheduler**: 풀이 파일 작성, 테스트 통과함.
- [ ] **Anki**: Heap 용도 카드 1장 추가함.
