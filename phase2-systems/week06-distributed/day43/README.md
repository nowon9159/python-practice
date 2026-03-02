# Day 43: MapReduce — Python으로 Word Count

## 🎯 오늘의 목표

- **MapReduce**(Map → Shuffle → Reduce) 개념을 정리하고, **Word Count**를 Python으로 구현한다.

---

## ✅ 오늘 할 일 (순서대로)

### 1. MapReduce 단계 정리

- **할 일**: `day43/` 안에 `mapreduce_notes.md`를 만든다. **Map**(입력 → (키, 값) 리스트), **Shuffle**(같은 키끼리 묶기), **Reduce**(같은 키에 대해 집계)를 각각 1~2문장으로 적는다. Hadoop/Spark와의 연결을 한 줄이라도 적어 둔다.
- **완료 조건**: Map/Reduce 역할을 말로 설명할 수 있다.

### 2. Word Count MapReduce 구현

- **할 일**: `day43/` 안에 `word_count_mapreduce.py`를 만든다. **입력**: 문자열 또는 파일 내용(여러 줄). **Map**: 각 줄을 단어로 쪼개 (단어, 1) 리스트 생성. **Shuffle**: 같은 단어끼리 그룹(딕셔너리 또는 defaultdict). **Reduce**: 그룹별로 개수 합산. 단일 프로세스로 구현해도 됨. `if __name__ == "__main__"`에서 예시 문자열로 실행해 단어별 개수가 출력되면 됨.
- **완료 조건**: Map → Shuffle → Reduce 단계가 코드에 드러나고, Word Count 결과가 출력된다.

### 3. Anki 카드 추가

- **할 일**: "MapReduce: Map, Shuffle, Reduce / Word Count" **카드 1장** 추가.
- **완료 조건**: Phase 2 덱에 반영했다.

---

## 📌 참고 (복습할 개념)

- Map: (키, 값) 생성. Reduce: 같은 키 집계.

---

## ✅ 체크리스트 (할 일 완료 후 표시)

- [ ] **정리**: Map/Reduce 단계를 문서에 적었다.
- [ ] **Word Count**: MapReduce 흐름으로 구현·실행했다.
- [ ] **Anki**: MapReduce 카드 추가함.
