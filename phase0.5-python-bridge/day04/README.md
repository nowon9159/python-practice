# Day 4: sys.argv (CLI 인자) + range()

## 🎯 오늘의 목표

- **`sys.argv`** 로 터미널에서 넘겨준 **인자**를 받아 보고, **`range(n)`** 이 0 이상 n 미만의 정수 구간임을 확인한다.

---

## ✅ 오늘 할 일 (순서대로)

### 1. sys.argv로 인자 받기

- **할 일**: `day04/` 안에 **`cli_args.py`** 를 만든다.
  - 파일 맨 위에 **`import sys`** 를 넣는다.
  - **`sys.argv`** 는 **리스트**이고, **`sys.argv[0]`** 은 실행한 스크립트 이름, **`sys.argv[1]`** 부터가 터미널에서 넘겨준 인자다.
  - 예: **`uv run python cli_args.py hello world`** 면 `sys.argv[1]` 은 `"hello"`, `sys.argv[2]` 는 `"world"` 이다.
  - **`if __name__ == "__main__":`** 안에서 **`print(len(sys.argv), sys.argv[1] if len(sys.argv) > 1 else "인자 없음")`** 처럼 한 번 출력해 보면 된다.
- **완료 조건**: **`python cli_args.py 첫번째 두번째`** 로 실행했을 때, 인자 개수와 첫 번째 인자가 출력된다. (Phase 1 Day 1 로그 파서는 "파일 경로"를 **`sys.argv[1]`** 로 받으면 된다.)

### 2. range() 확인하기

- **할 일**: **`range(n)`** 은 "0 이상 n 미만의 정수 구간"을 나타낸다. `range(3)` 이면 0, 1, 2 이다.
  - `day04/` 에 **`range_basics.py`** 를 만들어 **`for i in range(3): print(i)`** 를 실행해 0, 1, 2 가 나오는지 확인해도 된다.
- **완료 조건**: range(n) 이 0..n-1 이라는 걸 알고, 한 번이라도 for와 함께 써 봤다.

---

## 📌 참고

- **sys.argv**: **명령줄 인자**가 들어 있는 **리스트**다. `sys.argv[0]` 은 실행한 스크립트 경로/이름, **`sys.argv[1]`** 부터가 사용자가 넘긴 인자다. 인자가 없을 수 있으니 **`len(sys.argv) > 1`** 인지 확인한 뒤 `sys.argv[1]` 을 쓰는 게 안전하다.
- **range(n)**: **0 이상 n 미만**의 정수 시퀀스다. **`for i in range(5):`** 는 0, 1, 2, 3, 4 로 다섯 번 돈다. "몇 번 반복"할 때 자주 쓴다.

---

## ✅ 체크리스트

- [ ] **sys.argv**: 터미널에서 인자를 넘겨 주었을 때 `sys.argv[1]` 등으로 받아서 출력해 봤다.
- [ ] **range**: `range(n)` 이 0..n-1 이라는 걸 알고, for와 함께 한 번 써 봤다.
