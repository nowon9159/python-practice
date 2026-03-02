# Day 32: GIL 이해 + multiprocessing

## 🎯 오늘의 목표

- **GIL**이 무엇인지 한 문장으로 설명하고, **CPU-bound vs I/O-bound**에 threading vs multiprocessing을 적용한 **실험 스크립트**를 작성·실행한다.

---

## ✅ 오늘 할 일 (순서대로)

### 1. GIL 한 문장 정리

- **할 일**: `day32/` 안에 `gil_notes.md`를 만든다. **"GIL이란?"**을 **한 문장**으로 적는다 (예: "한 시점에 한 스레드만 Python 바이트코드를 실행하게 하는 락"). 그리고 **"CPU-bound일 때 threading이 왜 불리한가?"**를 1~2문장으로 적는다.
- **완료 조건**: 위 한 문장을 참고 없이 말할 수 있다.

### 2. CPU-bound vs I/O-bound 실험 스크립트

- **할 일**: `day32/` 안에 `cpu_io_experiment.py`를 만든다.
  - **내용**: (1) **CPU-bound** 작업 하나 정의 (예: 큰 수 반복 곱셈 또는 소수 세기). 이를 **순차 1회**, **threading으로 2~4스레드**, **multiprocessing으로 2~4프로세스**로 각각 실행하고 **걸린 시간**을 출력. (2) **I/O-bound** 작업 하나 정의 (예: `time.sleep(1)` 여러 번). 동일하게 순차/threading/multiprocessing으로 실행하고 시간 출력.
  - **조건**: `if __name__ == "__main__"`에서 위 실험을 돌리고, 결과를 print로 확인.
- **완료 조건**: 스크립트를 실행했고, CPU-bound에서는 multiprocessing이 유리하고, I/O-bound에서는 threading도 유리할 수 있음을 결과로 확인했다. **결과 요약 2~3줄**을 `day32/result.md` 또는 주석에 적어 둔다.

### 3. Anki 카드 추가

- **할 일**: "GIL 한 문장" / "CPU-bound → multiprocessing, I/O-bound → threading/asyncio" **카드 1장** 추가.
- **완료 조건**: Phase 2 덱에 반영했다.

---

## 📌 참고 (복습할 개념)

- GIL: 한 시점에 한 스레드만 실행. CPU-bound 시 threading은 효과 제한적.
- multiprocessing: 별도 프로세스 → GIL 우회.

---

## ✅ 체크리스트 (할 일 완료 후 표시)

- [ ] **GIL**: 한 문장 설명을 문서에 적었다.
- [ ] **실험**: CPU-bound·I/O-bound에 대한 threading/multiprocessing 실험 스크립트를 작성·실행하고 결과를 메모했다.
- [ ] **Anki**: GIL·multiprocessing 언제 쓰는가 카드 추가함.
