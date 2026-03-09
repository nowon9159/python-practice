# Day 27: Sliding Window 심화 + Monotonic Deque

## 🎯 오늘의 목표

- **Monotonic Deque**로 구간 최대/최소를 O(1)에 유지하는 패턴을 정리하고, **Sliding Window Maximum**을 풀어 본다.

---

## ✅ 오늘 할 일 (순서대로)

### 1. Monotonic Deque 유지 조건 정리

- **할 일**: `day27/` 안에 `monotonic_deque_notes.md`(또는 주석)를 만든다. 다음을 적는다.
  - **구간 최대**: deque는 (인덱스 또는 값) **내림차순** 유지. 새 원소가 들어올 때 deque 뒤에서 자신보다 작은 것 제거 후 자신 추가. 윈도우 밖 인덱스는 앞에서 제거. **최대값 = deque 앞**.
  - **유지 조건**: "deque 안에는 현재 윈도우에서 '앞으로 최대가 될 후보'만 남긴다" 한 문장.
- **완료 조건**: "내림차순 유지 + 윈도우 밖 제거"가 말로 설명 가능하다.

### 2. Sliding Window Maximum 풀이

- **할 일**: `phase1-cs-basics/algorithms/sliding-window/`(또는 `day27/`)에 `sliding_window_maximum.py`를 만든다.
  - **문제**: 배열과 윈도우 크기 k가 주어질 때, 각 윈도우에서의 최대값 리스트 반환. **Monotonic Deque**로 O(n).
  - **조건**: docstring에 "Monotonic Deque, 내림차순, 윈도우 밖 인덱스 제거" 명시, 시간/공간복잡도, 테스트 케이스 3개 이상.
- **완료 조건**: 로컬/제출 테스트 통과.

### 3. Anki 카드 추가

- **할 일**: "Monotonic Deque: 구간 최대일 때 내림차순 유지, 앞이 최대, 범위 밖 제거" **카드 1장** 추가.
- **완료 조건**: Week 4 덱에 반영했다.

---

## 📌 참고 (복습할 개념)

- **Monotonic Deque(구간 최대)**: 윈도우를 한 칸씩 밀 때 "현재 윈도우 안에서 최대값"을 O(1)에 알려면, deque를 **값(또는 인덱스) 기준 내림차순**으로 유지한다. 새 원소가 들어오면 deque **뒤**에서 자신보다 **작은 것**을 모두 제거한 뒤 자신을 넣는다. 이렇게 하면 "앞으로 최대가 될 후보"만 남고, **맨 앞**이 현재 윈도우의 최대값이 된다. 윈도우가 밀려서 **범위 밖으로 나간 인덱스**는 deque **앞**에서 제거한다.
- **Sliding Window Maximum**: 길이 k인 윈도우가 배열을 지나갈 때 각 윈도우의 최대값을 구하는 대표 문제다. Monotonic Deque로 O(n)에 풀 수 있다.

---

## ✅ 체크리스트 (할 일 완료 후 표시)

- [ ] **Monotonic Deque**: 유지 조건을 문서에 적었다.
- [ ] **Sliding Window Maximum**: O(n) 풀이 작성, 테스트 통과함.
- [ ] **Anki**: Monotonic Deque 조건 카드 추가함.
