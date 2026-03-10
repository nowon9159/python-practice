# Day 2: dataclass 맛보기 — @dataclass, 필드만 있는 클래스

## 🎯 오늘의 목표

- **`@dataclass`** 로 **필드만 있는 클래스**를 짧게 만드는 법을 한 번 써 본다.

---

## ✅ 오늘 할 일 (순서대로)

### 1. dataclass로 로그 한 줄 표현하기

- **할 일**: `day02/` 안에 `dataclass_basics.py`를 만든다.
  - 파일 맨 위에 **`from dataclasses import dataclass`** 를 넣는다.
  - **`@dataclass`** 아래에 **`class LogEntry:`** 를 정의한다.
  - 필드로 **`level: str`**, **`message: str`**, **`timestamp: str`** (또는 원하는 이름) 세 개를 적는다.
  - **`e = LogEntry("INFO", "서버 시작", "2024-01-01 10:00:00")`** 처럼 만들고 **`print(e.level, e.message)`** 가 나오는지 확인한다.
- **완료 조건**: `@dataclass` 로 필드만 있는 클래스를 하나 만들고, 인스턴스를 만들어 필드에 접근했다.

---

## 📌 참고

- **dataclass**: **필드만 있는 클래스**를 짧게 쓰려고 쓰는 문법이다. `@dataclass` 를 붙이면 **`__init__`**, **`__repr__`** 같은 걸 자동으로 만들어 준다. Day 1에서 직접 썼던 `__init__` 을 필드 이름만 적으면 자동으로 해 준다고 보면 된다.
- **Phase 1 Day 1**에서 로그 한 줄을 "레벨, 메시지, 타임스탬프"로 묶을 때 이걸 쓰면 편하다.

---

## ✅ 체크리스트

- [ ] **LogEntry**: `@dataclass` 로 level, message, timestamp 필드를 넣었다.
- [ ] **실행**: `LogEntry("INFO", "서버 시작", "2024-01-01 10:00:00")` 로 만들고 `e.level`, `e.message` 를 출력했다.
