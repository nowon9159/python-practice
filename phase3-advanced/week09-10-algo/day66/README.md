# Day 66: 비트 연산 — Bitmasking DP

## 🎯 오늘의 목표

비트마스크로 집합을 표현하고 부분집합 순회 등을 연습한 뒤, Bitmasking DP 문제 1~2개를 풀어 "방문한 도시 집합 = mask" 같은 패턴을 익힌다.

---

## ✅ 오늘 할 일 (순서대로)

### 1. 비트마스크 기본 연산 정리

- **할 일**: `phase3-advanced/week09-10-algo/day66/` 안에 `bitmask_notes.py` 또는 `notes.md`를 만든다.
  - **포함 여부**: `(mask >> i) & 1`
  - **부분집합 순회**: `for sub in range(mask)` 또는 `sub = (sub - 1) & mask` 패턴
  - **i번째 추가/제거**: `mask | (1 << i)`, `mask & ~(1 << i)`
  - 위 연산을 사용하는 짧은 예제 코드 또는 의사코드.
- **완료 조건**: mask로 부분집합 표현·순회를 문서 또는 코드로 설명할 수 있다.

### 2. Bitmasking DP 문제 풀이

- **할 일**: 같은 폴더에 `bitmask_dp.py`(또는 풀이 파일)를 만든다.
  - **내용**: Bitmasking DP 문제 1~2개 풀이 (예: Minimum Cost to Visit All Nodes, 외판원 순회 유형). `dp[mask][...]` 형태로 "방문한 집합 = mask" 상태를 쓰는 풀이.
- **완료 조건**: 1문제 이상 풀이가 맞게 동작하고, 상태 정의(mask의 의미)를 주석으로 적었다.

### 3. Anki 카드

- **할 일**: "Bitmasking DP를 쓰는 조건(부분집합/순열, N~20 정도)", "mask로 부분집합 순회" 카드 추가.
- **완료 조건**: Bitmasking DP 조건과 기본 연산을 Anki로 정리했다.

---

## 📌 참고 (복습할 개념)

- 비트마스크: 집합을 정수로 표현, (mask >> i) & 1, 부분집합 순회
- Bitmasking DP: 2^N 상태, TSP 등 "방문한 도시 집합" = mask
- N이 크면 2^N이 폭발하므로 보통 N~20 이하

---

## ✅ 체크리스트 (할 일 완료 후 표시)

- [ ] **비트마스크**: 기본 연산·부분집합 순회를 notes/코드로 정리함
- [ ] **Bitmasking DP**: 1문제 이상 풀이·상태 정의 주석 작성함
- [ ] **Anki**: Bitmasking DP 조건·연산 카드 추가함
