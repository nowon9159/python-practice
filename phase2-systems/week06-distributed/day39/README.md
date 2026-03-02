# Day 39: 일관성 모델 — Eventual Consistency 시뮬레이터

## 🎯 오늘의 목표

- **Strong vs Eventual consistency** 차이를 정리하고, **Eventual Consistency 시뮬레이터**를 구현한다.

---

## ✅ 오늘 할 일 (순서대로)

### 1. Strong vs Eventual 정리

- **할 일**: `day39/` 안에 `consistency_notes.md`를 만든다. **Strong consistency**(읽기 시 항상 최신)와 **Eventual consistency**(읽기 시 오래된 값이 보일 수 있으나 나중에 수렴)를 2~3문장으로 구분해 적는다.
- **완료 조건**: 두 용어를 말로 구분할 수 있다.

### 2. Eventual Consistency 시뮬레이터 구현

- **할 일**: `day39/` 안에 `eventual_consistency_sim.py`를 만든다. **여러 노드**(예: dict 3개, 각각 키-값 저장소)를 두고, **쓰기**는 한 노드(리더)에만 적용한 뒤 **지연(예: 1초 또는 N스텝) 후** 다른 노드에 복제되도록 시뮬레이션한다. **읽기**는 임의 노드에서 하면 "아직 복제 안 됐으면 오래된 값"이 보이도록 한다. `if __name__ == "__main__"`에서 쓰기 → 즉시 읽기(다른 노드) → 지연 후 읽기로 "eventual" 수렴을 확인한다.
- **완료 조건**: 쓰기 후 다른 노드에서 먼저는 옛값, 지연 후에는 새 값이 보이는 흐름이 한 번이라도 실행된다.

### 3. Anki 카드 추가

- **할 일**: "Strong vs Eventual consistency, 수렴" **카드 1장** 추가.
- **완료 조건**: Phase 2 덱에 반영했다.

---

## 📌 참고 (복습할 개념)

- 복제 지연, 충돌 해결(버전 벡터 등).

---

## ✅ 체크리스트 (할 일 완료 후 표시)

- [ ] **정리**: Strong vs Eventual을 문서에 적었다.
- [ ] **시뮬레이터**: 여러 노드 + 지연 복제로 eventual 수렴을 코드로 확인했다.
- [ ] **Anki**: 일관성 모델 카드 추가함.
