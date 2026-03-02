# Day 65: 고급 DP — DP on Trees, Digit DP

## 🎯 오늘의 목표

DP on Trees(트리 순회와 결합, 서브트리별 상태)와 Digit DP(자릿수별 상태, 수 범위 내 개수/합)를 학습하고, 각각 1문제씩 풀이 또는 개념 정리로 마무리한다.

---

## ✅ 오늘 할 일 (순서대로)

### 1. DP on Trees

- **할 일**: `phase3-advanced/week09-10-algo/day65/` 안에 `dp_on_trees.py` 또는 풀이 파일을 만든다.
  - **내용**: DP on Trees 문제 1개 풀이 (예: Binary Tree Maximum Path Sum, House Robber III 등). 트리 순회(DFS)와 결합해 서브트리 결과를 부모로 모으는 전이 식을 주석으로 적는다.
- **완료 조건**: 선택한 문제의 풀이가 동작하고, "자식 결과를 어떻게 부모에 합칠지" 전이 식을 코드 또는 `day65/notes.md`에 적었다.

### 2. Digit DP

- **할 일**: 같은 폴더에 `digit_dp.py` 또는 `notes.md`를 만든다.
  - **내용**: Digit DP 문제 1개 풀이 (예: 0~N에서 조건 만족 개수) 또는 개념 정리. 상태 정의(tight 여부, 자릿수 인덱스, 메모이제이션)를 문서에 요약한다.
- **완료 조건**: Digit DP의 상태 정의·tight 의미를 설명할 수 있고, 풀이 또는 요약이 문서/코드에 있다.

### 3. Anki 카드

- **할 일**: "DP on Trees 전이 식", "Digit DP 상태 정의(tight, 자릿수)" 카드 추가.
- **완료 조건**: 두 패턴을 Anki 카드로 정리했다.

---

## 📌 참고 (복습할 개념)

- DP on Trees: DFS 순회, 자식 결과 → 부모, 서브트리별 상태
- Digit DP: 자릿수별 상태, tight(상한 따름), 메모이제이션 (pos, tight, ...)

---

## ✅ 체크리스트 (할 일 완료 후 표시)

- [ ] **DP on Trees**: 문제 1개 풀이·전이 식 정리함
- [ ] **Digit DP**: 문제 또는 개념 정리·상태 정의 문서화함
- [ ] **Anki**: DP on Trees, Digit DP 카드 추가함
