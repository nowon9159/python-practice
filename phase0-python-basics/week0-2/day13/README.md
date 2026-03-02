# Day 13: 문자열 다루기 — split(), strip(), join(), in, 인덱싱

## 🎯 오늘의 목표

- **split()**, **strip()**, **join()**과 문자열 **in**, **인덱싱**을 한 번씩 써 본다.

---

## ✅ 오늘 할 일 (순서대로)

### 1. split()과 strip()

- **할 일**: `day13/` 안에 `string_basics.py`를 만든다.
  - `line = "  apple, banana, orange  "` 를 만든다. `line.strip()` 으로 앞뒤 공백을 없애고, `line.strip().split(", ")` 로 리스트 `["apple", "banana", "orange"]` 가 나오는지 확인한다.
- **완료 조건**: strip() 후 split(", ")으로 단어 리스트가 나온다.

### 2. join()과 in, 인덱싱

- **할 일**: 같은 파일에 `words = ["Hello", "World"]` 를 두고, `" ".join(words)` → "Hello World" 가 나오는지 확인한다.
  - `s = "python"` 일 때 `"p" in s` → True, `s[0]` → "p", `s[-1]` → "n" 이 나오는지 확인한다.
- **완료 조건**: join()으로 리스트를 한 문자열로 붙였고, in과 [0], [-1]을 한 번씩 썼다.

---

## 📌 참고

- **split(구분자)**: 문자열을 구분자로 나눠 **리스트**로 만든다.
- **strip()**: 앞뒤 공백 제거. **join(리스트)**: 리스트를 문자열로 이어 붙인다.
- 문자열도 **인덱스**로 한 글자씩 접근 가능. **-1**은 마지막.

---

## ✅ 체크리스트

- [ ] **split, strip**: strip().split(", ")으로 단어 리스트를 만들었다.
- [ ] **join, in, 인덱싱**: join(), in, [0], [-1]을 사용했다.
