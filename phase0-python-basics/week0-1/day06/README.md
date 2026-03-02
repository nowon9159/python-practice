# Day 6: while 루프, break, continue + 리스트와 조합

## 🎯 오늘의 목표

- **while** 루프를 쓰고, **break**(중단), **continue**(다음 반복으로)를 한 번씩 써 본다. **리스트**와 **for/while**을 같이 써 본다.

---

## ✅ 오늘 할 일 (순서대로)

### 1. while과 break

- **할 일**: `day06/` 안에 `while_loop.py`를 만든다.
  - `count = 0` 으로 두고, `while count < 5:` 안에서 `print(count)`, `count = count + 1` 을 넣어 0, 1, 2, 3, 4가 출력되는지 확인한다.
  - 새로 `n = 0` 으로 두고, `while True:` 안에서 `n += 1`, `print(n)` 후 `if n >= 3: break` 를 넣어 1, 2, 3만 출력되고 멈추는지 확인한다.
- **완료 조건**: while로 0~4 출력, while True + break로 1,2,3 후 종료가 된다.

### 2. 리스트와 for/while 조합

- **할 일**: 같은 파일에 `numbers = [1, 2, 3, 4, 5]` 를 만든다. **for**로 numbers를 돌면서 "값을 2배로 출력"하는 코드를 적는다 (예: `for x in numbers: print(x * 2)`). 실행 시 2, 4, 6, 8, 10이 나오는지 확인한다.
  - (선택) **while**과 인덱스로 같은 리스트를 돌며 `numbers[i]` 를 출력해 본다.
- **완료 조건**: for로 리스트를 돌아 2배 값이 출력된다.

---

## 📌 참고

- **while 조건:** 조건이 True인 동안 반복. **break**: 루프를 바로 빠져나감. **continue**: 아래 코드를 건너뛰고 다음 반복으로.

---

## ✅ 체크리스트

- [ ] **while, break**: count 0~4 출력, n 1,2,3 후 break 동작을 확인했다.
- [ ] **리스트+for**: 리스트를 for로 돌아 값(또는 2배)을 출력했다.
