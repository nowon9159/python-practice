# Phase 0.5: Python 기초 보강 — Phase 1·2·3을 위한 초석

Phase 0에서는 **변수, 리스트, 딕셔너리, 함수, 파일**까지 다뤘다.  
Phase 1부터는 **클래스**, **타입 표기**, **CLI 인자**, **테스트 블록** 같은 걸 쓰는데, Phase 0에서는 한 번도 안 나왔다.  
그래서 **Phase 1로 넘어가기 전에** 이 구간에서 그 개념들을 **설명식으로** 한 번씩 짚고 가자는 게 Phase 0.5다.  
과제를 풀면서 자연스럽게 익히는 건 여기서 굳이 안 해도 되고, **"이걸 모르면 Day 1부터 막힌다"** 수준만 담았다.

---

## 🎯 Phase 0.5의 목표

- **클래스(class)**가 뭔지, **dataclass**로 어떻게 짧게 쓰는지 한 번 해 본다.
- **None**, **if __name__ == "__main__"**, **sys.argv**, **typing**이 뭔지 설명을 읽고, 코드 한 번씩 써 본다.
- (선택) **데코레이터**, **리스트 컴프리헨션**, **enumerate**, **with** 개념을 한 줄씩 알아 두면 Phase 2·3에서 덜 낯설다.

---

## 📂 일별 README (순서대로 진행)

| Day | 주제 | 링크 |
|-----|------|------|
| Day 1 | class 기초 — __init__, self, 속성, 메서드 | [day01/README.md](day01/README.md) |
| Day 2 | dataclass 맛보기 — @dataclass, 필드만 있는 클래스 | [day02/README.md](day02/README.md) |
| Day 3 | None + if __name__ == "__main__" | [day03/README.md](day03/README.md) |
| Day 4 | sys.argv (CLI 인자) + range() | [day04/README.md](day04/README.md) |
| Day 5 | typing 맛보기 — 타입 힌트, List, Optional | [day05/README.md](day05/README.md) |
| Day 6 | (선택) 데코레이터, 리스트 컴프리헨션, enumerate, with | [day06/README.md](day06/README.md) |

- **진행**: 위 표에서 **Day 1**부터 해당 `dayNN/README.md` 를 열고, **할 일** → **참고** → 코드 작성 순으로 진행하면 된다.
- **코드 위치**: 각 Day의 실습 파일은 **해당 Day 폴더 안**에 둔다. 예: Day 1이면 `day01/class_basics.py` .

---

## ✅ Phase 0.5 전체 체크리스트

- [ ] **Day 1**: class — `Person` 같은 클래스를 정의하고, `__init__`, 메서드 하나를 써 봤다.
- [ ] **Day 2**: dataclass — `@dataclass` 로 필드만 있는 클래스를 하나 만들고, 인스턴스를 만들어 봤다.
- [ ] **Day 3**: None + if __name__ — `d.get("없는키")` 가 None인 것, 직접 실행할 때만 실행되는 블록을 확인했다.
- [ ] **Day 4**: sys.argv + range — 터미널 인자 받기, `range(n)` 이 0..n-1 인 것을 확인했다.
- [ ] **Day 5**: typing — 인자·반환값에 타입을 붙인 함수를 최소 하나 만들어 봤다.
- [ ] **Day 6 (선택)**: 데코레이터·리스트 컴프리헨션·enumerate·with 중 하나라도 "뭔지" 알고 있거나, 코드에 한 번 써 봤다.

---

## 다음 단계

위 체크리스트를 끝냈으면 **Phase 1** (`phase1-cs-basics/week01-python-complexity/day01/README.md`) 로 넘어가면 된다.  
Phase 1 Day 1에서는 uv 환경, 타입힌트·dataclass·collections, 로그 파서 CLI를 다룬다.
