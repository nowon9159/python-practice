# Day 54: Rate Limiter — Token Bucket, Sliding Window

## 🎯 오늘의 목표

- **Token Bucket**과 **Sliding Window** 알고리즘을 정리하고, **초당 N 요청 제한** Rate limiter를 하나 구현한다.

---

## ✅ 오늘 할 일 (순서대로)

### 1. 두 알고리즘 차이 정리

- **할 일**: `day54/` 안에 `rate_limiter_notes.md`를 만든다. **Token Bucket**: 버킷 크기, 충전 속도, 요청 시 토큰 1개 소비. **Sliding Window**: 구간(예: 1초) 내 요청 타임스탬프를 기록해 N개 초과면 거부. 각각 2문장으로 적는다. API Gateway 레이트리밋 연결 한 줄.
- **완료 조건**: 두 방식의 차이를 말로 설명할 수 있다.

### 2. Rate Limiter 구현

- **할 일**: `day54/` 안에 `rate_limiter.py`를 만든다. **Token Bucket** 또는 **Sliding Window** 중 하나로 **같은 클라이언트(키)**에 대해 **초당 최대 N회** 허용한다. `allow(key) -> bool`: True면 허용(내부 카운트 갱신), False면 거부. `if __name__ == "__main__"`에서 같은 키로 N+1번 연속 호출 시 처음 N번은 True, 그 다음은 False(또는 시간 경과 후 다시 True)인지 확인한다.
- **완료 조건**: 한 키에 대해 초당 제한이 동작한다.

### 3. Anki 카드 추가

- **할 일**: "Token Bucket vs Sliding Window / Rate limiter" **카드 1장** 추가.
- **완료 조건**: Phase 2 덱에 반영했다.

---

## 📌 참고

- 토큰 충전, 구간 내 카운트.

---

## ✅ 체크리스트

- [ ] **정리**: 두 알고리즘 차이를 문서에 적었다.
- [ ] **구현**: Rate limiter 하나를 구현·동작 확인했다.
- [ ] **Anki**: Rate limiter 카드 추가함.
