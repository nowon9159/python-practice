# Day 50: SQLite 클론 미니 프로젝트 (Day 1)

## 🎯 오늘의 목표

- **SQLite 스타일** 최소 DB 엔진의 **파서·실행기 뼈대**를 설계하고, CREATE TABLE / INSERT / SELECT 중 일부를 처리하는 구조를 만든다.

---

## ✅ 오늘 할 일 (순서대로)

### 1. SQLite 아키텍처 파악

- **할 일**: SQLite 공식 문서 또는 요약 글을 읽고, `day50/` 안에 `sqlite_clone_notes.md`를 만든다. **파서 → 실행기 → 스토리지** 흐름을 2~3문장으로 적는다.
- **완료 조건**: "SQL이 파싱되어 실행 계획으로 바뀌고, 스토리지에 접근한다"가 정리되어 있다.

### 2. 최소 명령 파서·실행 구조

- **할 일**: `day50/` 안에 `minidb.py`를 만든다. **입력**: 간단한 명령 문자열(예: "CREATE TABLE users (id INT, name TEXT);", "INSERT INTO users VALUES (1, 'a');", "SELECT * FROM users;"). **파서**(정규식 또는 split으로 키워드·테이블명·컬럼·값 추출)와 **실행기**(CREATE면 메모리 dict에 테이블 스키마 저장, INSERT면 행 추가, SELECT면 행 목록 반환)를 **최소한** 구현한다. 한 테이블, 고정 컬럼만 있어도 됨.
- **완료 조건**: 위 세 가지 명령 중 **최소 2가지**(예: CREATE + INSERT, 또는 INSERT + SELECT)가 동작한다. Day 51에서 확장할 부분을 주석으로 적어 둔다.

---

## 📌 참고

- 파서 → 실행기. 테이블 = 메모리 구조 또는 파일.

---

## ✅ 체크리스트

- [ ] **아키텍처**: SQLite 흐름을 문서에 적었다.
- [ ] **뼈대**: 파서·실행기로 CREATE/INSERT/SELECT 중 2가지 이상이 동작한다.
