# Day 24: DP 심화 — Knapsack 패턴

## 🎯 오늘의 목표

- **0/1 Knapsack** 점화식을 정리하고 기본 문제를 풀어 본다. (선택) Unbounded Knapsack·Coin Change.

---

## ✅ 오늘 할 일 (순서대로)

### 1. Knapsack 점화식 백지 재현

- **할 일**: `day24/` 안에 `knapsack_notes.md`(또는 주석)를 만든다. **0/1 Knapsack**에 대해 다음을 **코드 없이 문장/수식**으로 적는다.
  - **정의**: dp[i][w] = 0..i번 물건만 쓸 수 있고 용량 w일 때 최대 가치. (또는 dp[w] 1D)
  - **전이**: i번 물건을 넣지 않음 → dp[i-1][w]. 넣음 → (w >= weight[i]일 때) value[i] + dp[i-1][w-weight[i]]. 둘 중 max.
  - **0/1 vs Unbounded**: 0/1은 한 번만 선택, Unbounded는 같은 물건 여러 개 가능 → 전이에서 dp[i][w-w_i] 대신 dp[w-w_i] 사용.
- **완료 조건**: 위를 참고 없이 다시 쓸 수 있는 수준이다.

### 2. 0/1 Knapsack 기본 문제 풀이

- **할 일**: `phase1-cs-basics/algorithms/dp/`(또는 `day24/`)에 `knapsack_01.py`를 만든다.
  - **문제**: weight[], value[], capacity가 주어질 때 최대 가치. 2D 또는 1D(역순 for w) 구현.
  - **조건**: docstring(점화식 한 줄), 테스트 케이스 3개 이상(빈 배열, capacity 0, 일반).
- **완료 조건**: 로컬/제출 테스트 통과.

### 3. (선택) Coin Change 또는 Partition Equal Subset Sum

- **할 일**: Coin Change(동전 개수 무한) 또는 Partition Equal Subset Sum(0/1 변형) 중 **1개** 풀이. 같은 폴더에 파일 추가.
- **완료 조건**: 선택한 1문제 풀이 완료, 테스트 통과.

### 4. Anki 카드 추가

- **할 일**: "Knapsack: 0/1 vs Unbounded 전이 차이" **카드 1장** 추가.
- **완료 조건**: Week 4 덱에 반영했다.

---

## 📌 참고 (복습할 개념)

- dp[용량] 또는 dp[i][용량], 넣는 경우 / 안 넣는 경우
- Coin Change, Subset Sum 변형

---

## ✅ 체크리스트 (할 일 완료 후 표시)

- [ ] **점화식**: 0/1 Knapsack 전이를 문서에 적었다.
- [ ] **0/1 Knapsack**: 기본 문제 풀이, 테스트 통과함.
- [ ] **(선택)** Coin Change 또는 Partition 1문제 풀이함.
- [ ] **Anki**: Knapsack 패턴 카드 추가함.
