# 인수인계 문서 — 스페셜 크리에이터 웹페이지

> 이 문서만 읽으면 **처음 받는 사람이 30분 안에** 사이트를 띄우고, 수정하고, 배포할 수 있게 쓰였습니다.
> 세부 이력·디자인 수치는 [README.md](README.md), 이미지 규칙은 [ASSETS.md](ASSETS.md)에 있습니다.

## 1. 이 프로젝트는 무엇인가

오늘의집 **"스페셜 크리에이터"** 소개·모집 페이지입니다. Figma 디자인을 **정적 HTML/CSS/JS**로 옮겼고, **빌드 도구가 없습니다**(`npm install`도 필요 없음). 파일을 고치고 push하면 GitHub Pages가 그대로 배포합니다.

| | |
|---|---|
| 배포 주소 (메인) | https://sarahkim-bucketplace.github.io/special-creator/FindTheKey.html |
| 배포 주소 (첫 화면) | https://sarahkim-bucketplace.github.io/special-creator/hero-home.html — 루트 주소도 여기로 이동 |
| 저장소 | https://github.com/sarahkim-bucketplace/special-creator (public, 브랜치 `main`) |
| 디자인 원본 | Figma 파일 키 `NoZZ6mYgg5AZpr5MxwhzOw` (주요 노드 ID는 README "Figma 소스") |
| 신청 링크 | https://ohou.se/competitions/1155 |
| 인스타그램 | https://www.instagram.com/ohouse_creator/ |

방문자 흐름: **`index.html`(리다이렉트) → `hero-home.html`(열쇠구멍 스크롤 첫 화면) → 열쇠 클릭 → `FindTheKey.html`** (About → Opportunities → Programs → Voices 4개 섹션이 한 장으로 이어진 스크롤 페이지).

## 2. 5분 안에 시작하기

**준비물**: git, 파이썬 3(맥에 기본 설치), 크롬. (Claude Code 사용 시 아래 4번 참고)

```bash
git clone https://github.com/sarahkim-bucketplace/special-creator.git
cd special-creator
python3 -m http.server 5173
```

브라우저에서 `http://localhost:5173/` 접속. (`file://`로 직접 열면 일부가 깨지니 꼭 서버로 여세요.)

**수정 → 확인 → 배포**

```bash
python3 scripts/check-assets.py     # 이미지 경로 점검 (아래 5번)
git add -A && git commit -m "무엇을 바꿨는지"
git push                             # 1~2분 뒤 배포본에 반영
```

수정이 안 보이면 브라우저 캐시입니다 → `Cmd+Shift+R`.

## 3. 어디를 고치면 되나 (자주 하는 작업)

| 하고 싶은 일 | 고칠 곳 |
|---|---|
| **문구** 바꾸기 (섹션별) | `FindTheKey.html` — 섹션 id로 찾기: `#find-the-key`(About) / `#opportunities-unlocked` / `#beyond-the-door` / `#creator-voices`(+FAQ, 푸터) |
| **통계 숫자** (300+ / 674건 / 112명 / 29건) | `FindTheKey.html`의 `.stats__number-value`의 `data-target="숫자"` (0에서 카운트업되는 목표값) |
| **FAQ** 질문/답변 | `FindTheKey.html`의 `.faq__question` 주변 |
| **신청(Apply) 링크** 변경 | `grep -rn "competitions/1155" *.html` 로 전부 찾아 바꾸기 — **10개 파일에 흩어져 있음**(메인 3곳 + 상세 페이지 9개의 헤더) |
| **헤더 메뉴** 라벨/링크 | 헤더가 페이지마다 **복사돼 있음** — `FindTheKey.html` + `OpportunitiesUnlocked-01~05.html` + `BeyondTheDoor-gift1~4.html` 전부 같이 수정 |
| **Opportunities 카드** 제목·부제 | `FindTheKey.html`의 `.ou-card__title` / `.ou-card__sub` |
| **OU 상세 팝업** 제목·본문·이전/다음 | `OpportunitiesUnlocked-0N.html` (`.detail__title`, `.detail__body`). 05번만 사진마다 링크가 바뀜 → ASSETS.md |
| **선물 상세 페이지** | `BeyondTheDoor-gift1~4.html` — 사진 그리드와 모바일 뒤로가기 버튼(`#giftBackBtn`) 마크업이 **4개 파일에 똑같이 복사**돼 있으니 바꿀 땐 4개 다. 스타일은 `BeyondTheDoor-gift.css`, 버튼 동작은 `gift-detail-reveal.js` |
| **푸터** (주소·인스타·저작권) | `FindTheKey.html`의 `.site-footer`. **이메일 연락처는 아직 미정이라 HTML 주석으로 비워둠** — 확정되면 주석 자리에 `mailto:` 링크로 |
| **이미지** 교체/추가/삭제 | **[ASSETS.md](ASSETS.md)** (폴더·파일명 규칙 + 사진별 코드 위치) |
| **글자 크기·색·간격** | `FindTheKey.css` — 기준값은 README "디자인 규칙"(폰트 5단계·색 2종·간격 340px 등). **임의 값 대신 그 값만 쓰기** |
| **모바일** 전용 스타일 | `FindTheKey.css` **맨 끝**의 `@media (max-width: 900px)` 블록. 모바일 큰 글자는 화면 폭에 비례해 커지고 줄어듦(`clamp()`), 손으로 넣은 `<br>` 줄바꿈은 유지됨 |
| **스크롤 연출** | 아래 "건드릴 때 조심할 곳" 참고 |

## 4. Claude로 이어서 작업하기

이 저장소에는 [CLAUDE.md](CLAUDE.md)가 있어서, **Claude Code로 이 폴더를 열면 프로젝트 규칙과 문서 위치를 자동으로 읽습니다.**

1. 위 `git clone` 후, 그 폴더를 Claude Code(데스크톱 앱 Code 탭 또는 터미널 `claude`)에서 엽니다.
2. 처음엔 이렇게 말하면 됩니다:
   > "HANDOVER.md, README.md, ASSETS.md 읽고 이 프로젝트 파악해줘. 그다음 ○○ 부분을 이렇게 바꿔줘."
3. 작업이 끝나면 "커밋하고 push해줘", 이어서 "배포본에서 확인해줘"라고 하면 됩니다.

**Claude가 대화 맥락은 못 가져옵니다.** git에는 코드만 넘어가고 예전 대화는 안 넘어가요. 그래서 "왜 이렇게 만들었는지"를 README에 계속 적어 왔습니다. **새로 큰 결정을 하면 README에 적어두세요**(Claude에게 "README에도 반영해줘"라고 하면 됩니다).

**Figma를 읽게 하려면** Figma 연결(MCP)이 있는 환경이어야 하고, Figma 파일에 본인 계정 접근 권한이 있어야 합니다(아래 6번).

## 5. 배포와 점검

- **배포 방식**: `main` 브랜치에 push하면 GitHub Pages가 자동 배포합니다. 반영에 1~2분, 브라우저 캐시는 최대 약 10분.
- **push 전에**: `python3 scripts/check-assets.py` — 이미지 경로 오류를 잡아줍니다. 맥은 대소문자를 무시하기 때문에 **로컬에선 멀쩡한데 배포본에서만 이미지가 깨지는 사고**를 이 스크립트가 미리 막아줍니다.
- **push 후에**: 배포 주소를 열어 확인(스크롤 끝까지, 모바일 폭도). 캐시 때문에 안 바뀌어 보이면 `주소?v=1` 처럼 뒤에 아무 글자를 붙여 열어보세요.
- 이 컴퓨터에 `gh` CLI는 없고, 인증은 맥 키체인의 **GitHub 개인 액세스 토큰(PAT)** 을 씁니다. 새 컴퓨터에서는 처음 push할 때 GitHub 로그인/토큰이 필요합니다(권한: 이 저장소의 `Contents` Read and write). **토큰은 채팅·문서·스크린샷에 절대 붙여넣지 마세요.**

## 6. 계정·권한 체크리스트 (담당자가 바뀔 때 꼭 확인)

- [ ] **GitHub 저장소 소유권** — 지금 저장소는 개인 성격 계정(`sarahkim-bucketplace`) 아래에 있습니다. **이 계정이 사라지면 저장소도 배포도 같이 사라집니다.** 새 담당자/회사 계정으로 옮기세요(아래 "저장소 옮기기" 참고).
- [ ] **GitHub Pages 설정** — 옮긴 저장소의 Settings → Pages에서 배포 소스가 `main` 브랜치 루트인지 확인(옮긴 뒤 새로 켜야 할 수 있음). **저장소 주소가 바뀌면 배포 주소도 바뀝니다**(`<새 계정>.github.io/<저장소명>/`). 예전 주소는 자동으로 넘어가지 않으니 이 주소를 공유한 곳(사내 문서·슬랙·메일 등)은 새 주소로 교체해야 합니다.
- [ ] **원본 사진 폴더 (⚠️ 저장소에 없음)** — 웹에 올린 사진의 **원본·정리본은 git에 없고 담당자 iCloud Drive에만 있습니다**(`오늘의집/스페셜 클래스 웹페이지/assets/` 아래 `01. About`, `02. oppotunities`, `03. program` 등). 이 폴더를 **사내 공유 드라이브로 옮겨 새 담당자에게 공유**하세요. 저장소 안 사진 중 상당수는 줄여서 올린 것이라 원본이 없으면 화질을 다시 살릴 수 없고, 사진 교체 작업의 출발점(예: 선물 사진은 `번호-크리에이터이름.jpg`로 정리해 둔 폴더가 곧 소스였고 그 이름이 `Photo by.` 출처가 됨)도 이 폴더입니다.
- [ ] **Figma** — 파일 `NoZZ6mYgg5AZpr5MxwhzOw`에 새 담당자를 초대(편집 또는 보기 권한). 사진·디자인 확정은 Figma 기준입니다.
- [ ] **신청 링크** `ohou.se/competitions/1155`가 이번 모집에 유효한지. 모집 회차가 바뀌면 3번 표대로 10개 파일을 같이 교체.
- [ ] **공개 저장소 주의** — 저장소가 **public**이라 코드·이미지·크리에이터 출처 표기가 전부 공개됩니다. 공개하면 안 되는 자료가 생기면 private로 전환해야 하는데, 무료 GitHub 계정은 private로 바꾸면 Pages도 꺼집니다.
- [ ] **저작권·초상 사용 확인** — 페이지에 쓰인 사진은 크리에이터 개인 작업물입니다(출처 `Photo by.` 표기됨). 새 담당자는 사진 사용 동의 범위가 어디까지인지 확인하세요.
- [ ] **커밋 작성자 정보** — 히스토리(커밋 353개)에 작성자 이름·이메일이 남아 있습니다(회사 이메일 형식 1종, 개인 PC 이름이 들어간 로컬 이메일 형식 1종). 그대로 옮겨도 동작엔 문제 없지만, 이런 정보가 새 저장소에 따라가는 게 싫으면 아래 "저장소 옮기기 B안"(히스토리 없이 시작)을 쓰세요.

## 7. 저장소 옮기기 (다른 git으로)

**A안 — 히스토리 그대로 옮기기 (권장)**: 커밋 기록·"누가 언제 뭘 바꿨나"가 그대로 이어집니다.

```bash
# 1) 옮길 곳에 '빈' 저장소를 먼저 만든다 (README/라이선스 추가 체크 해제)
# 2) 이 폴더에서:
git remote rename origin old-origin
git remote add origin <새 저장소 주소>
git push -u origin --all
git push origin --tags
```

- 히스토리를 통째로 복사하는 **미러 방식**도 가능: `git clone --mirror <옛 주소>` 후 `git push --mirror <새 주소>` (모든 브랜치·태그 포함).
- GitHub 안에서 소유자만 바꾸는 방법도 있습니다: 저장소 Settings → Danger Zone → **Transfer ownership** (받는 사람이 수락). 이 경우 이슈·설정이 그대로 이동하고 옛 저장소 주소는 새 주소로 자동 연결되지만, **Pages 주소는 자동으로 안 넘어갑니다.**

**B안 — 깨끗하게 새로 시작 (히스토리 없이)**: 커밋 기록·과거 작성자 정보가 필요 없고, 저장소를 가볍게 시작하고 싶을 때.

```bash
git checkout --orphan clean-main
git add -A && git commit -m "Initial commit (handover from special-creator)"
git branch -M main
git remote add origin <새 저장소 주소>
git push -u origin main
```

**크기 참고**: 지금 `.git`이 약 490MB(과거에 커밋된 큰 원본 이미지가 히스토리에 남아 있음)라서 A안은 처음 push가 오래 걸리고, 일부 회사 Git 서버는 용량 제한에 걸릴 수 있습니다. 현재 `assets/`는 약 230MB입니다. 제한이 있으면 B안이 낫습니다.

**옮긴 뒤 할 일**: ① `README.md`/이 문서의 저장소·배포 주소 교체 ② Pages 켜기 ③ 새 배포 주소에서 이미지가 다 뜨는지 확인 ④ 옛 주소를 공유했던 곳 갱신 ⑤ 옛 저장소는 바로 지우지 말고 새 곳이 안정된 뒤에 정리.

## 8. 건드릴 때 조심할 곳

이 사이트에서 가장 까다로운 부분은 **스크롤 연출**입니다. 겉으로 단순해 보여도 여러 스크립트가 서로 맞물려 있어요.

- **`*-pause.js` 계열**(배지·키 사진·트로피·통계·선물 앞에서 스크롤이 잠깐 멈췄다 가는 지점): 한 스크립트가 스크롤을 움직이면 다음 스크립트가 연달아 실행되는 문제를 `viewport.js`의 `markPauseUnlock()`/`pauseSafeToTrigger()`로 막고 있습니다. **새 멈춤 지점을 만들거나 순서를 바꾸면 이 규칙을 따라야** 합니다(README "멈춤 스크립트 간 연쇄 방지").
- **화면 높이 `viewport.js`**: 맥북 14"/16"/외부 모니터에서 같은 구도가 나오도록 화면 높이를 760~960px로 제한해서 씁니다. About 섹션의 위치 계산에 `window.innerHeight` 대신 `window.effVH()`를 쓰세요.
- **높이가 서로 묶인 값**: `hero-home.css`의 `.hero-pin` 높이와 `hero-home.js`의 `REVEAL_VH`(=2.2)는 **항상 같이** 바꿔야 합니다.
- **모바일 줄바꿈**: About 등 큰 글자는 화면 폭에 비례해 줄어들고(`clamp()`), 손으로 넣은 `<br>` 줄이 어느 폭에서도 다시 꺾이지 않게 각 그룹의 **가장 긴 줄** 기준으로 비율을 잡았습니다. **문구를 바꾸면 가장 긴 줄이 여전히 들어가는지 320px 폭에서 다시 확인**하세요.
- **폰트·색·간격은 README 표의 값만** 씁니다(폰트 5단계, 글자색 `#2d2828`/`#7b7b7b`, 사진 모서리 5px, 섹션 간격 340px …).
- **이미 검증 안 된 것**: 스크롤 연출·"Click me" 힌트가 **실제 폰에서** 어떻게 보이는지는 에뮬레이션/측정으로만 확인했습니다. 3D 트로피의 커서 추적/드래그도 실제 화면 검증이 덜 됐습니다(README "남은 할 일").

## 9. 외부 의존 (인터넷 필요)

- **Pretendard 폰트** — `cdn.jsdelivr.net` (버전 1.3.9)
- **Three.js** (3D 트로피) — `cdn.jsdelivr.net` (버전 0.170.0). `FindTheKey.html`의 `importmap`에 고정돼 있음
- 그 외 서버·DB·API·환경변수·비밀키는 **없습니다.** (히스토리 전체에서 GitHub 토큰·AWS 키·개인키 형태의 문자열을 검색해 없음을 확인했습니다. 다만 패턴 검색이라 100% 보증은 아니니, 회사 저장소로 옮기기 전에 사내 보안 도구가 있으면 한 번 더 돌리세요.)

## 10. 파일 지도 (요약)

```
index.html                리다이렉트 → hero-home.html
hero-home.html/.css/.js   열쇠구멍 첫 화면
FindTheKey.html/.css      ★ 메인 통합 페이지 (문구·스타일 대부분이 여기)
OpportunitiesUnlocked-01~05.html/.css   카드 클릭 시 뜨는 상세 (메인이 fetch해서 팝업에 넣음 — 삭제 금지)
BeyondTheDoor-gift1~4.html/.css         선물 상세 페이지
*.js                      기능별 스크립트 (파일별 역할: README "파일 구조")
assets/                   이미지 (구조·규칙: ASSETS.md)
scripts/check-assets.py   이미지 경로 점검
CLAUDE.md                 Claude용 프로젝트 규칙 (자동으로 읽힘)
README.md                 상세 기록 (디자인 규칙·스크롤 동작·이력)
```

## 11. 남은 일 (인수인계 시점)

- 푸터 **이메일 연락처** — 확정 대기(주석 처리됨)
- **모바일 실기기 확인** — 스크롤 연출, 히어로의 "Click me" 자동 힌트, 큰 글자 비례 크기
- **이미지 용량 줄이기** — 2MB 넘는 파일이 30여 개(최대 25MB). 로딩을 빠르게 하려면 ASSETS.md "새 이미지 준비 방법"대로 줄여서 교체
- 선물 상세(`BeyondTheDoor-gift1~4.html`)의 모바일은 뒤로가기 화살표만 OU 상세처럼 추가했고, 나머지 레이아웃은 사진 그리드 그대로임(2열→600px 이하 1열)
- 푸터가 메인(`FindTheKey.html`)에만 있고 상세 페이지에는 없음(디자인 확정 후 결정)
