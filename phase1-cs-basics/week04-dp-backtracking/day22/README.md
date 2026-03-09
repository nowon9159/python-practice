# Day 22: DP 기초 — Memoization vs Tabulation

## 🎯 오늘의 목표

- **Memoization**과 **Tabulation** 차이를 정리하고, **Climbing Stairs**와 **House Robber**를 두 방식 모두로 풀어 본다.

---

## ✅ 오늘 할 일 (순서대로)

### 1. Memo vs Tabulation 차이 정리

- **할 일**: `day22/` 안에 `dp_memo_vs_tab.md`(또는 주석)를 만든다. **2~3문장**으로 적는다.
  - **Memoization**: 재귀 + 캐시(top-down). 처음 호출 시 계산 후 캐시에 저장, 같은 인자면 캐시 반환.
  - **Tabulation**: 반복 + 테이블(bottom-up). 작은 인덱스부터 채워 나가서 목표 인덱스까지.
- **완료 조건**: "overlapping subproblems, optimal substructure"가 DP 조건임을 한 줄이라도 적어 두었다.

### 2. Climbing Stairs — Memo + Tab 둘 다

- **할 일**: `phase1-cs-basics/algorithms/dp/`(또는 `day22/`)에 `climbing_stairs.py`를 만든다.
  - **문제**: n번째 계단까지 오르는 방법 수 (1칸 또는 2칸). **메모이제이션** 버전(재귀 + @lru_cache 또는 dict)과 **Tabulation** 버전(반복, dp[i] = dp[i-1] + dp[i-2]) **둘 다** 구현.
  - **조건**: docstring, 테스트 케이스 n=1, 2, 5 등.
- **완료 조건**: 두 구현이 같은 n에 대해 같은 값을 반환하고, 로컬/제출 통과.

### 3. House Robber — Memo + Tab 둘 다

- **할 일**: 같은 폴더에 `house_robber.py`를 만든다.
  - **문제**: 인접한 집을 털 수 없을 때 최대 금액. **Memo** 버전(재귀 + 캐시)과 **Tab** 버전(반복, dp[i] = max(nums[i]+dp[i-2], dp[i-1]) 등) **둘 다** 구현.
  - **조건**: docstring, 테스트 케이스 3개 이상.
- **완료 조건**: 두 구현 모두 동일 입력에 동일 결과, 로컬/제출 통과.

### 4. Anki 카드 추가

- **할 일**: "DP 조건: overlapping subproblems, optimal substructure" / "Memo vs Tab: top-down vs bottom-up" **카드 1장** 이상 추가.
- **완료 조건**: Week 4 덱에 반영했다.

---

## 📌 참고 (복습할 개념)

- **DP가 적용되는 조건**: (1) **Overlapping subproblems** — 같은 부분 문제가 여러 번 반복해서 나온다(예: fib(n-2)가 여러 경로에서 호출됨). (2) **Optimal substructure** — 큰 문제의 최적해가 작은 부분 문제의 최적해로부터 구해진다. 이 두 가지가 있으면 재귀만 쓰면 중복 계산이 많아지므로, 캐시나 테이블로 한 번만 계산해 두는 DP가 유리하다.
- **Memoization vs Tabulation**: Memo는 **재귀 + 캐시**(top-down). 처음 호출할 때만 계산하고 같은 인자면 캐시에서 반환. Tabulation은 **반복문 + 테이블**(bottom-up). 인덱스 0, 1, … 순서로 채워 나가서 목표 인덱스까지 채운다. 1D DP일 때는 "직전 몇 개만 쓰면 되므로" 변수 몇 개만 두고 공간을 O(1)로 줄일 수 있다.

---

## ✅ 체크리스트 (할 일 완료 후 표시)

- [ ] **Memo vs Tab**: 차이를 문서/주석에 적었다.
- [ ] **Climbing Stairs**: Memo·Tab 둘 다 구현, 테스트 통과함.
- [ ] **House Robber**: Memo·Tab 둘 다 구현, 테스트 통과함.
- [ ] **Anki**: DP 조건·Memo/Tab 카드 추가함.
