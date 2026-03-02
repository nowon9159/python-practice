# Day 5: Stack & Queue — 단조 스택(Monotonic Stack)

## 🎯 오늘의 목표

- Stack과 Monotonic Stack을 복습하고, **Valid Parentheses**와 **Daily Temperatures**를 풀어 본다.

---

## ✅ 오늘 할 일 (순서대로)

### 1. Valid Parentheses 풀이

- **할 일**: `phase1-cs-basics/algorithms/stack-queue/`(또는 `day05/`)에 `valid_parentheses.py`를 만든다.
  - **문제**: 괄호 문자열이 유효한지 (스택으로 매칭)
  - **조건**: docstring(문제 요약, 접근법, 시간/공간복잡도), `if __name__ == "__main__"`에 테스트 케이스 최소 3개(빈 문자열, 짝 안 맞음, 올바른 경우 등).
- **완료 조건**: 로컬/제출 테스트 통과.

### 2. Daily Temperatures 풀이 (Monotonic Stack)

- **할 일**: 같은 폴더에 `daily_temperatures.py`를 만든다.
  - **문제**: 각 날짜에서 더 따뜻한 날까지의 일수 배열 반환 (Monotonic Stack으로 "다음에 더 큰 원소" 찾기).
  - **조건**: docstring에 "Monotonic Stack" 접근법과 시간/공간복잡도 명시, 테스트 케이스 3개 이상.
- **완료 조건**: 로컬/제출 테스트 통과.

### 3. Monotonic Stack 설명 + Anki

- **할 일**: "Monotonic Stack을 언제 쓰는가?(다음/이전 더 큰·작은 원소)"와 "유지 조건(오름/내림), 인덱스 vs 값 저장"을 2~3문장으로 정리한다. Anki에 **Monotonic Stack 카드 1장** 이상 추가.
- **완료 조건**: Daily Temperatures 풀이에서 스택 유지 조건을 말로 설명할 수 있고, Anki에 반영했다.

---

## 📌 참고 (복습할 개념)

- **Stack**: LIFO, 괄호 매칭
- **Monotonic Stack**: 오름/내림 유지, 다음/이전 더 큰(작은) 원소, 인덱스 vs 값

---

## ✅ 체크리스트 (할 일 완료 후 표시)

- [ ] **Valid Parentheses**: 스택 풀이 파일 작성, 테스트 통과함.
- [ ] **Daily Temperatures**: Monotonic Stack 풀이 파일 작성, 테스트 통과함.
- [ ] **Anki**: Monotonic Stack 조건·핵심 코드 카드 1장 이상 추가함.
