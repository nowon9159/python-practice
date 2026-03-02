# Day 23: DP 1D → 2D 확장 — LCS, LIS

## 🎯 오늘의 목표

- **2D DP** 패턴을 복습하고, **Longest Common Subsequence**와 **Edit Distance**를 풀어 본다.

---

## ✅ 오늘 할 일 (순서대로)

### 1. LCS 점화식 정리

- **할 일**: `day23/` 안에 `lcs_edit_notes.md`(또는 주석)를 만든다. **LCS**에 대해 다음을 적는다.
  - **정의**: dp[i][j] = text1[0:i], text2[0:j]의 LCS 길이.
  - **전이**: 같으면 dp[i-1][j-1]+1, 다르면 max(dp[i-1][j], dp[i][j-1]). 초기값(한쪽 길이 0)은 0.
- **완료 조건**: 위 점화식이 코드 없이도 말로 설명 가능하다.

### 2. Longest Common Subsequence 풀이

- **할 일**: `phase1-cs-basics/algorithms/dp/`(또는 `day23/`)에 `longest_common_subsequence.py`를 만든다.
  - **문제**: 두 문자열의 LCS 길이 반환. 2D 테이블, (선택) 공간 최적화(이전 행만 유지).
  - **조건**: docstring(점화식 요약, 시간/공간복잡도), 테스트 케이스 3개 이상.
- **완료 조건**: 로컬/제출 테스트 통과.

### 3. Edit Distance (Levenshtein) 풀이

- **할 일**: 같은 폴더에 `edit_distance.py`를 만든다.
  - **문제**: word1 → word2로 바꾸는 최소 연산 수(삽입/삭제/교체). dp[i][j] = word1[0:i]를 word2[0:j]로 만드는 최소 비용. 전이: 같으면 dp[i-1][j-1], 다르면 1 + min(삽입, 삭제, 교체).
  - **조건**: docstring, 테스트 케이스 3개 이상.
- **완료 조건**: 로컬/제출 테스트 통과.

### 4. Anki 카드 추가

- **할 일**: "2D DP: LCS, Edit Distance 전이 패턴(같을 때/다를 때)" **카드 1장** 추가.
- **완료 조건**: Week 4 덱에 반영했다.

---

## 📌 참고 (복습할 개념)

- dp[i][j] 정의, 초기값, 전이 식
- LIS: O(n²) DP 또는 O(n log n) 이진탐색 (다음에 활용)

---

## ✅ 체크리스트 (할 일 완료 후 표시)

- [ ] **LCS 점화식**: 문서/주석에 정리했다.
- [ ] **LCS 풀이**: 2D DP 구현, 테스트 통과함.
- [ ] **Edit Distance**: 풀이 구현, 테스트 통과함.
- [ ] **Anki**: 2D DP 전이 패턴 카드 추가함.
