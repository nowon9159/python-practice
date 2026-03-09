# Day 10: Binary Search — 기본 → Left/Right bound 변형

## 🎯 오늘의 목표

- 이진 탐색 **기본**과 **Lower/Upper bound** 변형을 복습하고, **Search in Rotated Sorted Array**와 **Koko Eating Bananas**를 풀어 본다.

---

## ✅ 오늘 할 일 (순서대로)

### 1. 이진 탐색 템플릿 정리

- **할 일**: `day10/` 안에 `binary_search_templates.py`(또는 `notes.md`)를 만든다. **세 가지**를 코드 또는 의사코드로 적는다.
  - **기본**: 정렬된 배열에서 target의 (아무) 인덱스 반환, 없으면 -1.
  - **Lower bound**: target 이상인 **첫 번째** 인덱스.
  - **Upper bound**: target **초과**인 첫 번째 인덱스(또는 target인 마지막 인덱스+1).
- **완료 조건**: mid 계산(left+right)//2, left/right 갱신 조건이 명확히 적혀 있고, 나중에 백지로 다시 쓸 수 있는 수준이다.

### 2. Search in Rotated Sorted Array 풀이

- **할 일**: `phase1-cs-basics/algorithms/binary-search/`(또는 `day10/`)에 `search_rotated_sorted_array.py`를 만든다.
  - **문제**: 회전된 정렬 배열에서 target 인덱스 찾기. (한 쪽 절반은 항상 정렬되어 있음을 이용)
  - **조건**: docstring, 테스트 케이스 3개 이상(회전 없음, 회전 있음, 없음).
- **완료 조건**: 로컬/제출 테스트 통과.

### 3. Koko Eating Bananas 풀이

- **할 일**: 같은 폴더에 `koko_eating_bananas.py`를 만든다.
  - **문제**: 바나나 더미 배열과 제한 시간 h가 주어질 때, k(시간당 먹는 개수) 최소값. **정답 범위에 대한 이진 탐색**: possible(k)로 h 시간 안에 다 먹을 수 있는지 판별.
  - **조건**: docstring에 "정답 범위 BS" 명시, 테스트 케이스 3개 이상.
- **완료 조건**: 로컬/제출 테스트 통과.

### 4. Anki 카드 추가

- **할 일**: "이진 탐색: 기본 vs Lower bound vs Upper bound, 언제 어떤 걸 쓰는가" **카드 1장** 추가.
- **완료 조건**: Week 2 덱에 반영했다.

---

## 📌 참고 (복습할 개념)

- **mid 계산·left/right 갱신**: mid는 `(left + right) // 2`로 두고, overflow가 걱정되면 `left + (right - left) // 2`를 쓴다. target이 mid보다 크면 left = mid+1, 작으면 right = mid-1(기본형). **lower/upper bound**에서는 "같을 때" left를 옮길지 right를 옮길지에 따라 "첫 번째" 또는 "마지막" 위치가 정해지므로, 템플릿을 정해 두고 외우는 편이 안전하다.
- **Lower bound / Upper bound**: "target **이상**인 **첫 번째** 인덱스"가 필요하면 lower bound(왼쪽을 줄일 때 조건을 조정). "target **초과**인 첫 번째" 또는 "target인 **마지막** 인덱스 + 1"이 필요하면 upper bound. "몇 개 있는지"는 upper - lower로 구할 수 있다.

---

## ✅ 체크리스트 (할 일 완료 후 표시)

- [ ] **템플릿**: 기본/Lower/Upper bound 코드(또는 의사코드)를 파일에 정리했다.
- [ ] **Search in Rotated**: 풀이 파일 작성, 테스트 통과함.
- [ ] **Koko Eating Bananas**: 정답 범위 BS 풀이 파일 작성, 테스트 통과함.
- [ ] **Anki**: Binary Search 변형 카드 1장 추가함.
