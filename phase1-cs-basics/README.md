# Phase 1: CS 기초 보강 (Day 1–30)

## Phase 1이란 / Phase 0과의 차이

- **Phase 0**에서는 변수·리스트·딕셔너리·함수·파일 같은 **문법과 기본 사용법**을 단계별로 익혔다. 각 Day README도 "이걸 한 번 해 보자" 식으로 **할 일 → 완료 조건 → 참고**가 짧게 설명돼 있었다.
- **Phase 1**에서는 **자료구조·알고리즘·복잡도**를 다룬다. 그래서 "용어만 나열"하기보다, **참고**에서 "이 개념이 뭔지, 언제 쓰는지"를 Phase 0처럼 **한두 문장씩 설명**해 두었다. Day별 README를 읽을 때 **목표 → 할 일 → 참고(설명)** 순으로 보면, 생략된 부분 없이 따라가기 쉬울 것이다.
- 일별로 **할 일**과 **완료 조건**은 그대로 두고, **참고**를 "키워드 나열"에서 "설명식 문장"으로 보강했다.

---

## 일별 README (오늘 할 일)

| 주차 | Day | 링크 |
|------|-----|------|
| Week 1 | 1–7 | [day01](week01-python-complexity/day01/README.md) · [day02](week01-python-complexity/day02/README.md) · [day03](week01-python-complexity/day03/README.md) · [day04](week01-python-complexity/day04/README.md) · [day05](week01-python-complexity/day05/README.md) · [day06](week01-python-complexity/day06/README.md) · [day07](week01-python-complexity/day07/README.md) |
| Week 2 | 8–14 | [day08](week02-linkedlist-binarysearch/day08/README.md) … [day14](week02-linkedlist-binarysearch/day14/README.md) |
| Week 3 | 15–21 | [day15](week03-heap-graph/day15/README.md) … [day21](week03-heap-graph/day21/README.md) |
| Week 4 | 22–30 | [day22](week04-dp-backtracking/day22/README.md) … [day30](week04-dp-backtracking/day30/README.md) |

## 폴더 구조

```
phase1-cs-basics/
├── week01-python-complexity/   # Day 1–7
├── week02-linkedlist-binarysearch/  # Day 8–14
├── week03-heap-graph/         # Day 15–21
├── week04-dp-backtracking/    # Day 22–30
├── algorithms/                # NeetCode/LeetCode 풀이 (패턴별 모음)
└── review/                    # 주간 복습, 패턴 카탈로그, Anki 메모
```

## 사용법

- **일별**: 해당 `dayNN/README.md`를 연다. **오늘의 목표**와 **오늘 할 일**을 읽고, **참고**에서 개념 설명을 본 뒤, 코드는 `dayNN/` 안에 작성한다.
- **알고리즘**: `algorithms/<패턴명>/` 에 문제별 파일을 둔다. 커리큘럼 규칙의 코드 템플릿(docstring에 요약·접근법·복잡도·DevOps 연결)을 따른다.
- **복습**: `review/` 에 패턴 정리와 Feynman 메모를 쌓아 둔다. 주간 복습 Day에는 "백지 재현"으로 흐름만 떠올려 보기.
