# 📁 폴더 구조 가이드 (python-tutor 커리큘럼)

커리큘럼 진행 시 **어디에 무엇을 둘지** 한눈에 보는 용도입니다.

---

## 1. 루트 구조

```
python-practice/
├── .cursor/
├── docs/                 # 이 가이드, 패턴 카탈로그 등
├── phase0-python-basics/ # Day 1–21 (Python 완전 입문, 선택)
├── phase1-cs-basics/     # Day 22–51 (또는 Phase 0 생략 시 Day 1–30)
├── phase2-systems/       # Day 52–81
├── phase3-advanced/      # Day 82–111
├── templates/            # (선택) 공통 코드 템플릿
├── pyproject.toml        # (선택) uv/pip 공통 의존성·설정
└── README.md
```

- **Phase 0**을 쓰면: phase1의 day01 = **커리큘럼 Day 22**.
- **Phase 0**을 건너뛰면: phase1의 day01 = **커리큘럼 Day 1**로 두고 진행하면 됨.

---

## 2. Phase별 공통 패턴

| 구분 | 넣을 것 | 예시 |
|------|--------|------|
| **일별 학습** | `phaseN/weekXX-테마/dayDD/` | 이론 노트, 실습 스크립트 |
| **알고리즘 풀이** | `phase1,3/.../algorithms/<패턴>/` | `two_sum.py`, `valid_anagram.py` |
| **미니 프로젝트** | `phaseN/.../miniprojects/<이름>/` 또는 `weekXX/.../dayDD/` | 로그 파서, LRU 캐시, HTTP LB |
| **복습·정리** | `phaseN/.../review/` | 패턴 카탈로그, Anki 메모, Feynman 메모 |

---

## 3. 파일 네이밍 (권장)

- **문제 풀이**: `문제명_snake_case.py` (예: `two_sum.py`, `valid_parentheses.py`)
- **일별 메인 실습**: `dayDD/` 안에 `main.py` 또는 주제별 `recursion.py`, `binary_search.py`
- **미니 프로젝트**: `README.md` + `main.py` 또는 `src/` 로 모듈 분리

---

## 4. 규칙과 맞추기

- 코드는 **.cursor/rules/python-tutor.mdc** 의 Python 코드 템플릿 사용 (docstring, 테스트 케이스 포함).
- 풀이 완료 후 체크리스트는 각 파일 주석 또는 `review/` 노트에 정리.
- Anki 카드는 별도 도구 사용 시, `review/anki-notes.md` 같은 형태로 텍스트만 백업해 두면 추적하기 좋음.

이 구조대로 진행하면 Day 번호와 Phase/Week가 대응해서 나중에 “그날 뭘 했지?” 찾기 쉽습니다.
