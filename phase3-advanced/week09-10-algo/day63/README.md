# Day 63: Trie 구현 + 응용 문제

## 🎯 오늘의 목표

Trie(접두사 트리)를 구현하고 insert/search/startsWith를 지원한 뒤, 자동완성 엔진 미니 프로젝트로 prefix 검색을 구현한다.

---

## ✅ 오늘 할 일 (순서대로)

### 1. Trie 클래스 구현

- **할 일**: `phase3-advanced/week09-10-algo/day63/` 안에 `trie.py`를 만든다.
  - **클래스**: `Trie` — 노드는 자식 딕셔너리 + 단어 끝 표시(필드 또는 플래그).
  - **메서드**: `insert(word: str)`, `search(word: str) -> bool`, `startsWith(prefix: str) -> bool`.
- **완료 조건**: `if __name__ == "__main__"`에서 단어 여러 개 insert 후 search/startsWith 결과가 기대값과 같다.

### 2. 자동완성 엔진 (미니 프로젝트)

- **할 일**: 같은 폴더에 `autocomplete.py`를 만든다.
  - **동작**: 단어 목록(리스트 또는 파일)을 Trie에 넣고, prefix 문자열을 입력받으면 해당 prefix로 시작하는 후보 단어 리스트를 반환. (kubectl 자동완성처럼 "명령어 prefix → 후보" 연상.)
  - **인터페이스**: `get_candidates(prefix: str) -> list[str]` 또는 CLI로 `uv run python autocomplete.py <prefix>`.
- **완료 조건**: prefix를 주면 후보 목록이 출력되고, Trie의 startsWith/검색 로직을 활용했다.

### 3. Anki 카드

- **할 일**: "Trie를 언제 쓰는가?(prefix 검색, 자동완성)" 카드 추가. (선택) LeetCode Trie 유형 1문제 풀이.
- **완료 조건**: Trie 사용 조건을 Anki 카드로 정리했다.

---

## 📌 참고 (복습할 개념)

- Trie 노드: 자식 딕셔너리, 단어 끝 표시
- 공간 트레이드오프, 문자열 집합 prefix 검색에 유리
- insert O(m), search/startsWith O(m), m=단어 길이

---

## ✅ 체크리스트 (할 일 완료 후 표시)

- [ ] **Trie**: `trie.py`에 insert/search/startsWith 구현·실행 확인함
- [ ] **자동완성**: `autocomplete.py`로 prefix 후보 반환 동작 확인함
- [ ] **Anki**: Trie 사용 조건 카드 추가함
