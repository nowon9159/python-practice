# Day 52: 메시지 큐 — Python으로 Pub/Sub 브로커 구현

## 🎯 오늘의 목표

- **Pub/Sub** 개념을 정리하고, **subscribe(topic)** / **publish(topic, msg)** 로 구독자에게 push하는 **메시지 브로커**를 구현한다.

---

## ✅ 오늘 할 일 (순서대로)

### 1. Pub/Sub·Kafka 용어 정리

- **할 일**: `day52/` 안에 `pubsub_notes.md`를 만든다. **발행자-토픽-구독자**, **토픽별 구독자 목록**, 메시지 전달 흐름을 2~3문장으로 적는다. **Kafka**의 파티션·오프셋을 한 줄씩 메모해 둔다.
- **완료 조건**: "subscribe로 토픽 구독, publish로 토픽에 메시지 보내면 구독자에게 전달"이 설명되어 있다.

### 2. Pub/Sub 브로커 구현

- **할 일**: `day52/` 안에 `pubsub_broker.py`를 만든다. **subscribe(topic, callback)** 또는 **subscribe(topic) -> queue**: 토픽별로 구독자(콜백 또는 큐) 목록 유지. **publish(topic, msg)**: 해당 토픽 구독자에게 msg를 **push**(콜백 호출 또는 큐에 put). in-process로 동작하면 됨. `if __name__ == "__main__"`에서 subscribe 2개, publish 1번으로 두 구독자 모두가 메시지를 받는지 확인한다.
- **완료 조건**: subscribe 후 publish 시 구독자에게 메시지가 전달된다.

### 3. Anki 카드 추가

- **할 일**: "Pub/Sub: 토픽, 구독자, push / Kafka 파티션·오프셋" **카드 1장** 추가.
- **완료 조건**: Phase 2 덱에 반영했다.

---

## 📌 참고

- 토픽별 구독자, 메시지 전달.

---

## ✅ 체크리스트

- [ ] **정리**: Pub/Sub·Kafka 용어를 문서에 적었다.
- [ ] **브로커**: subscribe/publish가 동작하고, 구독자가 메시지를 받는다.
- [ ] **Anki**: Pub/Sub·메시지 브로커 카드 추가함.
