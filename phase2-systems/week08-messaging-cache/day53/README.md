# Day 53: 캐싱 전략 — Write-Through, Write-Behind, Cache-Aside

## 🎯 오늘의 목표

- **Write-Through / Write-Behind / Cache-Aside** 차이를 정리하고, **Redis 호환 인메모리 캐시 서버**(GET/SET)를 구현한다.

---

## ✅ 오늘 할 일 (순서대로)

### 1. 캐싱 전략 비교표

- **할 일**: `day53/` 안에 `caching_strategies.md`를 만든다. **Cache-Aside**(앱이 캐시·DB 읽기/쓰기 제어), **Write-Through**(쓰기 시 캐시+DB 동시), **Write-Behind**(캐시에만 쓰고 나중에 DB 반영)를 표로 비교한다. 각각 "쓰기 시 동작" 한 줄.
- **완료 조건**: 세 전략의 차이가 표로 구분되어 있다.

### 2. Redis 호환 인메모리 캐시 서버

- **할 일**: `day53/` 안에 `cache_server.py`를 만든다. **TCP 서버** 한 포트에서 accept. **GET key** / **SET key value** 를 (간단한 텍스트 프로토콜 또는 RESP 일부) 파싱해, **in-memory dict**로 get/set 한다. 응답을 클라이언트에 보낸다. `redis-cli` 또는 `nc`로 GET/SET 요청을 보내 응답이 오는지 확인한다.
- **완료 조건**: 서버 실행 후 GET/SET 요청으로 값을 넣고 꺼낼 수 있다.

### 3. Anki 카드 추가

- **할 일**: "캐싱 전략: Cache-Aside, Write-Through, Write-Behind" **카드 1장** 추가.
- **완료 조건**: Phase 2 덱에 반영했다.

---

## 📌 참고

- 각 전략의 쓰기·일관성 트레이드오프.

---

## ✅ 체크리스트

- [ ] **비교표**: 세 전략을 문서에 적었다.
- [ ] **캐시 서버**: GET/SET 지원 서버를 구현·테스트했다.
- [ ] **Anki**: 캐싱 전략 카드 추가함.
