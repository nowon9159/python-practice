# Day 83: 최종 프로젝트 — Python 분산 태스크 큐 (Celery 클론 미니)

## 🎯 오늘의 목표

Celery 스타일의 분산 태스크 큐 미니 버전을 구현한다. Producer가 태스크를 넣고, Worker가 꺼내 실행하며, Broker(큐)로 연결되는 구조가 동작하도록 만든다.

---

## ✅ 오늘 할 일 (순서대로)

### 1. 프로젝트 뼈대 생성

- **할 일**: `phase3-advanced/final-project/`(또는 `phase3-advanced/week11-12-final/day83/task_queue/`) 폴더를 만들고 프로젝트 뼈대를 잡는다. `pyproject.toml` 또는 `requirements.txt`, 필요한 경우 패키지 구조(예: `broker.py`, `worker.py`, `client.py`)를 정한다.
- **완료 조건**: 지정 폴더에 프로젝트가 있고, `uv run` 또는 `python`으로 실행 환경이 동작한다.

### 2. 태스크 정의·enqueue·Broker

- **할 일**: **태스크** = 함수 + 인자를 직렬화 가능한 형태로 정의한다. (예: 함수 이름 문자열 + 인자 리스트.) **Broker**는 큐를 제공한다. (메모리: `queue.Queue`, 또는 Redis list 등.) **enqueue(task)** 로 태스크를 넣는 API를 구현한다.
- **완료 조건**: 태스크를 enqueue하면 Broker(큐)에 들어가고, 형식이 정의되어 있다.

### 3. Worker 루프 구현

- **할 일**: **Worker**는 루프로 Broker에서 `get` → 태스크 역직렬화 → 해당 함수 실행 → (선택) 결과 저장한다. 최소 1가지 태스크 타입(예: add, echo)으로 실행해 본다.
- **완료 조건**: Producer가 태스크를 넣고, Worker가 꺼내서 실행하는 것이 한 번 이상 성공했다. Day 84에서 에러 처리·재시도·정리를 이어간다.

---

## 📌 참고 (복습할 개념)

- 태스크 = 함수 + 인자 직렬화
- Broker: queue.Queue, Redis list 등
- Worker: get → 실행 → (선택) result 저장

---

## ✅ 체크리스트 (할 일 완료 후 표시)

- [ ] **프로젝트 뼈대**: final-project/ 또는 day83/ 폴더에 구조·실행 환경 갖춤
- [ ] **태스크·Broker·enqueue**: 태스크 정의·enqueue·Broker 동작 확인함
- [ ] **Worker**: Worker 루프로 최소 1가지 태스크 실행 성공함
