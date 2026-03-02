# Day 18: 모듈 맛보기 — import, 다른 .py에서 함수 가져오기

## 🎯 오늘의 목표

- **다른 .py 파일**에 함수를 적어 두고, **import**해서 사용해 본다.

---

## ✅ 오늘 할 일 (순서대로)

### 1. 함수가 들어 있는 모듈 파일

- **할 일**: `day18/` 안에 `mymodule.py`를 만든다. 안에 `def hello(): return "Hello from module"` 같은 함수를 하나 넣고 저장한다.
- **완료 조건**: mymodule.py에 함수가 최소 1개 있다.

### 2. import해서 사용

- **할 일**: `day18/` 안에 `main.py`를 만든다. `import mymodule` 을 넣고, `print(mymodule.hello())` 로 위 함수를 호출한다. 실행 시 "Hello from module"이 나오는지 확인한다.
  - (선택) `from mymodule import hello` 하고 `print(hello())` 로도 호출해 본다.
- **완료 조건**: import mymodule 후 함수를 호출해 결과가 출력된다.

---

## 📌 참고

- **import 모듈이름**: 그 파일(.py)의 코드를 불러온다. **모듈이름.함수()** 로 호출.
- **from 모듈이름 import 함수**: 함수만 가져와서 이름만으로 호출 가능.

---

## ✅ 체크리스트

- [ ] **mymodule.py**: 함수 1개를 넣었다.
- [ ] **main.py**: import 후 함수를 호출해 출력했다.
