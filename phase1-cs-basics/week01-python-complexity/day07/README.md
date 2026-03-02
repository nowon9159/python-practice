# Day 7: 미니 프로젝트 — LRU Cache

## 🎯 오늘의 목표

- **LRU Cache**를 직접 구현해 get/put O(1)을 만족시키고, Redis LRU와 연결해서 이해한다.

---

## ✅ 오늘 할 일 (순서대로)

### 1. LRU Cache 클래스 구현

- **할 일**: `day07/` 안에 `lru_cache.py`를 만든다.
  - **API**: `get(key) -> value` (없으면 -1 등 규칙대로), `put(key, value)`. capacity 초과 시 **LRU** 항목 한 개 제거 후 삽입.
  - **조건**: `get`, `put` 모두 **평균 O(1)**. `OrderedDict` 또는 **Doubly Linked List + dict** 중 하나로 구현.
  - **조건**: docstring에 "LRU 정책", 시간/공간복잡도 적기.
- **완료 조건**: LeetCode 146 LRU Cache 테스트 케이스(또는 동일한 시나리오)를 통과한다.

### 2. 엣지케이스 테스트

- **할 일**: `if __name__ == "__main__"`에 아래를 포함한 테스트를 넣는다.
  - capacity 1인 경우 (한 개 넣고 다른 키 put 시 기존 제거)
  - 같은 키로 put 두 번 (갱신 후 순서만 바뀌고 개수 유지)
  - get으로 접근한 키는 "가장 최근 사용"이 되어, capacity 초과 시 제거되지 않아야 함
- **완료 조건**: 위 시나리오를 코드로 돌려서 기대대로 동작함을 확인했다.

### 3. Anki + (선택) Redis LRU 메모

- **할 일**: Anki에 "LRU Cache: 언제 쓰는가, get/put O(1) 방법(OrderedDict 또는 DLL+dict)" 카드 **1장** 추가. (선택) Redis 문서에서 LRU/approx LRU 설명을 읽고, "Redis는 근사 LRU를 쓰는 이유" 등을 1~2줄 메모.
- **완료 조건**: LRU 조건과 구현 방법을 말로 설명할 수 있고, Anki에 반영했다.

---

## 📌 참고 (복습할 개념)

- **LRU**: Least Recently Used, 캐시 용량 초과 시 가장 오래 사용하지 않은 항목 제거
- **구현**: OrderedDict (move_to_end) 또는 Doubly Linked List + HashMap으로 접근 순서 유지

---

## ✅ 체크리스트 (할 일 완료 후 표시)

- [ ] **LRU Cache**: get/put O(1) 구현을 한 파일에 완성하고, 공식/동일 시나리오 테스트 통과함.
- [ ] **엣지케이스**: capacity 1, 동일 키 재삽입, get 후 eviction 순서 테스트를 추가하고 통과함.
- [ ] **Anki**: LRU 조건·구현 카드 1장 이상 추가함.
