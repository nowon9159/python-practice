# Day 15: 파일 읽기 — open(), read(), readline(), for line in f

## 🎯 오늘의 목표

- **파일을 열고** 내용을 **read()**, **readline()**, **for line in f** 로 읽어 본다.

---

## ✅ 오늘 할 일 (순서대로)

### 1. 텍스트 파일 하나 만들기

- **할 일**: `day15/` 안에 `sample.txt` 파일을 만든다. 안에 아무 문장 3줄을 적고 저장한다 (예: "첫 줄", "둘째 줄", "셋째 줄").
- **완료 조건**: sample.txt가 있고, 2줄 이상 들어 있다.

### 2. open과 read / for line in f

- **할 일**: `day15/` 안에 `read_file.py`를 만든다.
  - `f = open("sample.txt")` 또는 `open("sample.txt", encoding="utf-8")` 로 연다. `content = f.read()` 후 `print(content)` 로 전체가 출력되는지 확인한다. `f.close()` 로 닫는다.
  - 다시 파일을 열고, `for line in f: print(line.strip())` 로 한 줄씩 출력되는지 확인한다. 끝나면 `f.close()`.
  - (권장) `with open("sample.txt") as f:` 안에서 read() 또는 for line in f 를 쓰면, with 블록을 나갈 때 자동으로 닫힌다. 이 방식으로 한 번 더 실행해 본다.
- **완료 조건**: read()로 전체, for line in f로 한 줄씩 출력했다. (선택) with open을 썼다.

---

## 📌 참고

- **open(경로)**: 파일 객체 반환. **read()**: 전체 내용을 한 문자열로. **readline()**: 한 줄씩.
- **for line in f:** 파일을 한 줄씩 반복. **with open(...) as f:** 쓰면 끝날 때 자동 close.

---

## ✅ 체크리스트

- [ ] **sample.txt**: 2줄 이상 있는 텍스트 파일을 만들었다.
- [ ] **read/for line**: read()와 for line in f 를 각각 실행했다.
