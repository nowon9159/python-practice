# Day 34: HTTP 서버 직접 구현 (socket → raw HTTP 파싱)

## 🎯 오늘의 목표

- TCP 소켓 위에서 **HTTP 요청**을 파싱하고, **HTTP 응답**을 만들어 **최소 HTTP 서버**를 구현한다.

---

## ✅ 오늘 할 일 (순서대로)

### 1. HTTP 요청 파싱

- **할 일**: `day34/` 안에 `http_server.py`를 만든다. TCP로 **recv**한 바이트를 **utf-8 디코딩**한 뒤, **첫 줄(Request-Line)**을 파싱해 **메서드**(GET/POST)와 **경로**(URL path)를 추출한다. **헤더**는 `\r\n`으로 줄 구분, 빈 줄까지 읽어 (선택) Content-Length 등 필요한 헤더만 파싱. Body는 필요 시 Content-Length만큼 추가 recv.
  - **함수 예**: `parse_request(raw: str) -> dict` with keys `method`, `path`, `headers`, `body`.
- **완료 조건**: "GET /foo HTTP/1.1" 같은 문자열에서 method=`GET`, path=`/foo`가 나온다.

### 2. HTTP 응답 생성 및 전송

- **할 일**: 같은 파일에 **응답 생성**을 넣는다. **Status-Line**(예: `HTTP/1.1 200 OK`), **Headers**(예: `Content-Type: text/plain`, `Content-Length: ...`), **빈 줄**, **Body**를 `\r\n`으로 이어 붙여 바이트로 **send**. 경로에 따라 **200 OK** (예: `/` 또는 `/health`)와 **404 Not Found** (그 외)를 반환하도록 분기.
- **완료 조건**: 브라우저 또는 `curl http://localhost:포트/` 로 요청 시 200과 본문이 보이고, 없는 경로는 404가 나온다.

### 3. 서버 실행·테스트

- **할 일**: 서버를 한 포트에 bind/listen/accept 루프로 띄우고, `curl -v http://127.0.0.1:포트/` 와 `curl -v http://127.0.0.1:포트/unknown` 으로 200/404를 확인한다.
- **완료 조건**: 위 두 요청에 대해 200과 404가 각각 반환된다.

### 4. Anki 카드 추가

- **할 일**: "HTTP 요청 구조: Request-Line, Headers, Body / 응답: Status-Line, Headers, Body" **카드 1장** 추가.
- **완료 조건**: Phase 2 덱에 반영했다.

---

## 📌 참고 (복습할 개념)

- HTTP/1.1 텍스트 프로토콜, \r\n, Content-Length.
- nginx/gunicorn이 소켓 위에서 HTTP를 다룬다는 연결.

---

## ✅ 체크리스트 (할 일 완료 후 표시)

- [ ] **요청 파싱**: 메서드·경로(및 선택적으로 헤더) 파싱 코드를 작성했다.
- [ ] **응답 생성**: 200/404 분기와 Status-Line·Headers·Body를 보내는 코드를 작성했다.
- [ ] **테스트**: curl 또는 브라우저로 200·404를 확인했다.
- [ ] **Anki**: HTTP 요청/응답 구조 카드 추가함.
