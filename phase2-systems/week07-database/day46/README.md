# Day 46: LSM Tree + SSTable — LevelDB 구조 이해

## 🎯 오늘의 목표

- **LSM Tree**와 **SSTable** 구조를 정리하고, (선택) 단순화 SSTable 쓰기/읽기 시뮬레이션을 한다.

---

## ✅ 오늘 할 일 (순서대로)

### 1. LSM/SSTable 구조 정리

- **할 일**: `day46/` 안에 `lsm_notes.md`를 만든다. **LSM**: 쓰기는 **메모리 버퍼(MemTable)**에, 가득 차면 **디스크의 SSTable**로 flush. **SSTable**: 정렬된 immutable 세그먼트. **Compaction**이 여러 SSTable을 합치는 개념. RocksDB/Cassandra 연결을 한 줄이라도 적는다.
- **완료 조건**: "쓰기 → MemTable → SSTable, SSTable은 정렬된 블록"이 설명되어 있다.

### 2. (선택) SSTable 시뮬레이션

- **할 일**: 메모리 상에서 "정렬된 키-값 블록" 리스트로 SSTable을 흉내 내고, **쓰기**(리스트에 append)와 **읽기**(블록에서 이진 탐색)를 구현해 본다.
- **완료 조건**: 선택. 구현했다면 키 추가·조회가 동작한다.

### 3. Anki 카드 추가

- **할 일**: "LSM: MemTable → SSTable, Compaction / SSTable 정렬" **카드 1장** 추가.
- **완료 조건**: Phase 2 덱에 반영했다.

---

## 📌 참고

- Flush, Compaction. RocksDB, Cassandra.

---

## ✅ 체크리스트

- [ ] **정리**: LSM·SSTable 흐름을 문서에 적었다.
- [ ] **(선택)** SSTable 쓰기/읽기 시뮬레이션을 했다.
- [ ] **Anki**: LSM·SSTable 카드 추가함.
