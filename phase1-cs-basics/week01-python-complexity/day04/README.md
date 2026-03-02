# Day 4: Hashing — HashMap, HashSet 내부 동작

## 🎯 오늘의 목표

- 해시(HashMap/HashSet) 동작을 복습하고, **Two Sum**, **Group Anagrams**, **Top K Frequent Elements**를 해시를 활용해 푼다.

---

## ✅ 오늘 할 일 (순서대로)

### 1. Two Sum 풀이

- **할 일**: `phase1-cs-basics/algorithms/hashing/`(또는 `day04/`)에 `two_sum.py`를 만든다.
  - **문제**: 배열에서 합이 target이 되는 두 수의 인덱스 반환 (해시로 O(n) 풀이)
  - **조건**: docstring(문제 요약, 접근법, 시간/공간복잡도), `if __name__ == "__main__"`에 테스트 케이스 최소 3개(엣지 포함).
- **완료 조건**: 로컬/제출 테스트 통과.

### 2. Group Anagrams 풀이

- **할 일**: 같은 폴더에 `group_anagrams.py`를 만든다.
  - **문제**: 애너그램끼리 그룹으로 묶어 반환 (해시 키 설계: 정렬된 문자열 또는 카운트 튜플 등).
  - **조건**: docstring, 테스트 케이스 3개 이상.
- **완료 조건**: 로컬/제출 테스트 통과.

### 3. Top K Frequent Elements 풀이

- **할 일**: 같은 폴더에 `top_k_frequent.py`를 만든다.
  - **문제**: 빈도 상위 k개 원소 반환 (Counter + heap 또는 Counter만으로).
  - **조건**: docstring, 테스트 케이스 3개 이상(빈 배열, k=1 등 엣지 포함).
- **완료 조건**: 로컬/제출 테스트 통과.

### 4. Anki 카드 추가

- **할 일**: "해시를 언제 쓰는가?(카운팅, 존재 여부, 그룹핑)" 또는 "DevOps에서 해시 구조가 쓰이는 예"를 **카드 1장** 이상 추가한다.
- **완료 조건**: Week 1 Anki 덱에 반영했다.

---

## 📌 참고 (복습할 개념)

- 해시 함수, bucket, collision(chaining 등), 평균 O(1)
- 카운팅, 존재 여부, 그룹핑에 dict/set 활용

---

## ✅ 체크리스트 (할 일 완료 후 표시)

- [ ] **Two Sum**: 해시 활용 풀이 파일 작성, 테스트 통과함.
- [ ] **Group Anagrams**: 풀이 파일 작성, 테스트 통과함.
- [ ] **Top K Frequent**: 풀이 파일 작성, 테스트 통과함.
- [ ] **Anki**: 해시 관련 카드 1장 이상 추가함.
