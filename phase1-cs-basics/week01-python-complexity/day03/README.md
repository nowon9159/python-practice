# Day 3: Array & String — Two Pointers, Sliding Window

## 🎯 오늘의 목표

- Two Pointers와 Sliding Window 패턴을 복습하고, **Valid Anagram**과 **Best Time to Buy and Sell Stock**을 풀어 본다.

---

## ✅ 오늘 할 일 (순서대로)

### 1. Valid Anagram 풀이

- **할 일**: `phase1-cs-basics/algorithms/two-pointers/`(또는 `day03/`)에 `valid_anagram.py`를 만든다.
  - **문제**: 두 문자열이 애너그램인지 판별 (NeetCode: Valid Anagram)
  - **조건**: 코드 템플릿 규칙 준수 (docstring에 문제 요약, 접근법, 시간/공간복잡도, DevOps 연결), `if __name__ == "__main__"`에 테스트 케이스 최소 3개(엣지 포함).
- **완료 조건**: 제출/로컬 테스트 통과, docstring에 복잡도가 적혀 있다.

### 2. Best Time to Buy and Sell Stock 풀이

- **할 일**: 같은 폴더(또는 `day03/`)에 `best_time_buy_sell_stock.py`를 만든다.
  - **문제**: 한 번 사고 한 번 팔 때 최대 이익 (Sliding Window 또는 one-pass 관점)
  - **조건**: 위와 동일 (docstring, 테스트 케이스 3개 이상).
- **완료 조건**: 제출/로컬 테스트 통과, 시간/공간복잡도 docstring에 명시.

### 3. 패턴 정리 + Anki

- **할 일**: "언제 Two Pointers vs Sliding Window를 쓰는가?"를 2~3문장으로 정리해 `day03/notes.md`에 적거나 Anki 뒷면에 넣는다. Two Pointers / Sliding Window 각각 **카드 1장** 이상 추가.
- **완료 조건**: 두 패턴의 차이를 말로 설명할 수 있고, Anki에 반영했다.

---

## 📌 참고 (복습할 개념)

- **Two Pointers**: left/right 이동 조건, 정렬된 배열·펠린드롬·pair 찾기, O(n)
- **Sliding Window**: 고정/가변 구간, 부분배열·부분문자열, 조건 만족 시 shrink

---

## ✅ 체크리스트 (할 일 완료 후 표시)

- [ ] **Valid Anagram**: 풀이 파일 작성, docstring·테스트 케이스 포함, 통과 확인함.
- [ ] **Best Time to Buy and Sell Stock**: 풀이 파일 작성, docstring·테스트 케이스 포함, 통과 확인함.
- [ ] **패턴 정리**: Two Pointers vs Sliding Window 차이를 정리했고, Anki 카드 1장 이상 추가함.
