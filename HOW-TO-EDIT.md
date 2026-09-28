# Git에서 받아 Claude로 수정하기 — 실전 가이드

개발을 잘 몰라도 따라 할 수 있게, **① GitHub에서 내 컴퓨터로 받아 Claude에게 여는 방법**과 **② 페이지 내용을 실제로 수정하는 방법**을 순서대로 정리했습니다.
프로젝트 전체 설명은 [HANDOVER.md](HANDOVER.md), Claude에게 시키는 방법·요청 문구는 [CLAUDE-WORKFLOW.md](CLAUDE-WORKFLOW.md), 이미지 규칙은 [ASSETS.md](ASSETS.md)에 있습니다.

---

# Part 1. Git에서 받아 Claude로 열기

## 1-0. 먼저: 내가 수정하고 올릴 수 있는 권한이 있나

| 하고 싶은 일 | 필요한 것 |
|---|---|
| 받기(clone/pull) | **없음.** 저장소가 public이라 로그인 없이 받을 수 있음 |
| 수정해서 **올리기(push)** | 저장소 **쓰기 권한**. 저장소 주인(`juhyun-bot`)이 저장소 **Settings → Collaborators → Add people**에서 내 GitHub 계정을 **Write** 권한으로 초대해야 함 (초대 메일을 수락) |

권한 없이 push하면 `403` 오류가 납니다. 권한이 없으면 저장소를 **Fork**(내 계정으로 복사)해서 작업하는 방법도 있지만, 그러면 배포 주소도 내 계정 것이 됩니다.

## 1-1. 내 컴퓨터로 받기 (셋 중 하나)

**방법 A. 터미널 (권장)**
```bash
git clone https://github.com/juhyun-bot/special-creator-web.git
cd special-creator-web
```

**방법 B. GitHub Desktop (터미널이 낯설 때)**
저장소 페이지의 초록색 **Code** 버튼 → **Open with GitHub Desktop** → 저장 위치 선택 → Clone. 이후 수정·올리기도 이 앱의 버튼(Commit, Push origin)으로 할 수 있습니다.

**방법 C. ZIP (권장하지 않음)**
**Code → Download ZIP**은 지금 파일만 받는 것이라 **히스토리와 원격 연결이 없어서 push할 수 없습니다.** 코드를 구경만 할 때 쓰세요.

> 🖥️ **서버가 안 켜질 때**: Claude에게 "로컬 서버 켜줘"라고 했는데 `PermissionError`가 나면(폴더 위치에 따라 Claude의 서버 실행 기능이 막히는 경우가 있음), 터미널에서 그 폴더로 이동해 `python3 -m http.server 5173`을 직접 실행하면 됩니다.

## 1-2. 그 폴더를 Claude Code로 열기

1. **Claude 데스크톱 앱의 Code 탭**에서 방금 받은 `special-creator-web` 폴더를 선택해 엽니다. (터미널이라면 그 폴더 안에서 `claude` 실행)
2. 폴더를 열면 [CLAUDE.md](CLAUDE.md)를 **Claude가 자동으로 읽습니다.** (프로젝트 규칙이 들어 있음)
3. 첫 요청으로 이렇게 말하세요:
   > HANDOVER.md, HOW-TO-EDIT.md, ASSETS.md를 읽고 이 프로젝트를 파악해줘. 어떤 파일을 고치면 어떤 화면이 바뀌는지 요약해줘.

## 1-3. 작업을 시작할 때마다 (중요)

**작업 전에 최신 상태로 맞추세요.** 다른 사람이나 다른 컴퓨터에서 바뀐 게 있을 수 있습니다.
- Claude에게: "**git pull 해줘**" (또는 터미널에서 `git pull`)
- 최신인지 확인: "**지금 저장소가 최신이야? 로컬에 커밋 안 된 변경이 있어?**"

같은 줄을 두 사람이 고쳤으면 충돌 표시(`<<<<<<<`)가 생길 수 있습니다. 그럴 땐 직접 고치려 하지 말고 Claude에게 "충돌 해결해줘. 어느 쪽을 남길지 나한테 먼저 물어봐줘"라고 하세요.

## 1-4. 수정한 걸 올리려면

Claude에게 "**커밋하고 push해줘**". 처음 push할 때 GitHub 로그인이 필요하면 **터미널에서 직접** `git push`를 실행해 로그인하세요(비밀번호가 아니라 **개인 액세스 토큰** 사용. 권한은 `Contents: Read and write`). **토큰을 Claude 채팅에 붙여넣지 마세요.** 자세한 내용은 [CLAUDE-WORKFLOW.md](CLAUDE-WORKFLOW.md) "안전 수칙"과 "자주 막히는 곳".

---

# Part 2. 페이지 내용 수정하기

## 2-1. 화면 ↔ 파일 대응표

| 보이는 화면 | 파일 |
|---|---|
| 첫 열쇠구멍 화면 | `hero-home.html` (+ `.css`, `.js`) |
| **메인 스크롤 페이지 전체** (About / Opportunities / Programs / Voices / FAQ / 푸터) | **`FindTheKey.html`** (글자·구조), **`FindTheKey.css`** (모양) |
| Opportunities 카드를 눌렀을 때 뜨는 상세 팝업 | `OpportunitiesUnlocked-01~05.html` |
| Programs의 선물 "더보기" 상세 페이지 | `BeyondTheDoor-gift1~4.html` |
| 헤더(로고·메뉴·Apply) | 페이지마다 복사돼 있음 (아래 2-3 참고) |

> 글자(문구)는 **`.html`**, 모양(크기·색·간격)은 **`.css`** 입니다. "문구만 바꾸고 싶다"면 거의 항상 `.html`만 열면 됩니다.

## 2-2. 고칠 문구를 코드에서 찾는 법

1. 화면에서 바꾸려는 **문구를 그대로** 복사합니다.
2. 코드 편집기(VS Code 등)에서 `FindTheKey.html`을 열고 **`Cmd+F`** 로 그 문구를 검색합니다. (Claude에게는 "이 문구가 어느 파일 몇 번째 줄에 있어?"라고 물어도 됩니다.)
3. 찾은 줄에서 **글자만** 바꾸고, `<` `>` 로 둘러싸인 부분(태그)은 건드리지 마세요.

**검색이 안 될 때**
- 문장이 `<br>`(줄바꿈)로 나뉘어 있으면 통째로는 검색이 안 됩니다 → 문장 **앞쪽 5~6글자만** 검색하세요.
- 같은 문구가 웹과 모바일에서 다르게 줄바꿈되도록 만들어진 곳이 있습니다(아래 2-4 "줄바꿈").

**바꾸기 전과 후 예시** (FAQ 답변)
```html
<!-- 바꾸기 전 -->
<div class="faq__answer">
  <p>A. 오늘의집 스페셜 크리에이터는 연간 100명 내외로 반기별 선정됩니다.</p>
</div>

<!-- 바꾼 후: 글자만 수정, 태그는 그대로 -->
<div class="faq__answer">
  <p>A. 오늘의집 스페셜 크리에이터는 연간 120명 내외로 반기별 선정됩니다.</p>
</div>
```

## 2-3. 자주 하는 수정 레시피

**① 일반 문구 (About·Programs·Voices 등)**
`FindTheKey.html`에서 문구를 검색해 글자만 수정. 모바일에서 줄이 어색하게 꺾이는지 꼭 확인(2-5).

**② 통계 숫자 (300+ / 674건 / 112명 / 29건)**
`FindTheKey.html`에서 `data-target=`을 검색합니다. 숫자(0에서 올라가는 목표값)는 여기입니다.
```html
<span class="stats__number-value" data-target="300">0</span>   ← 300을 원하는 숫자로
```
라벨(`프리미엄 가구 협찬` 등)은 바로 위 `<p class="stats__label">` 안의 글자입니다.

**③ FAQ 질문/답변 수정·추가**
`faq__question` 검색. 질문은 `<span class="faq__question">`, 답변은 `<div class="faq__answer"><p>` 안입니다.
**추가하려면** 기존 `<div class="faq__item"> … </div>` 한 덩어리를 통째로 복사해 바로 아래 붙이고 글자만 바꾸세요.

**④ 신청(Apply) 링크**
`https://ohou.se/competitions/1155`가 **여러 파일에 복사돼 있습니다**(메인 3곳 + 상세 페이지 9개). 터미널에서 `grep -rn "competitions/1155" *.html`로 전부 찾아 바꾸거나, Claude에게 "이 링크를 ○○으로 전부 바꿔줘"라고 하세요. 하나라도 빠지면 페이지마다 링크가 달라집니다.

**⑤ 헤더 메뉴 라벨/링크**
`About / Opportunities / Programs / Voices / Apply`가 `FindTheKey.html`과 `OpportunitiesUnlocked-01~05.html`, `BeyondTheDoor-gift1~4.html` 총 **10개 파일에 똑같이 복사**돼 있습니다. 바꾸면 10개 다 같이 바꿔야 합니다. (Claude에게 시키는 게 안전)

**⑥ 푸터 (주소·인스타·저작권)**
`FindTheKey.html`에서 `site-footer` 또는 `All rights reserved`를 검색. **이메일 연락처는 아직 미정이라 HTML 주석(`<!-- ... -->`)으로 비워져 있습니다.** 확정되면 그 주석 자리에 `<a href="mailto:주소">주소</a>` 형태로 넣으세요.

**⑦ Opportunities 카드 문구 / 상세 팝업**
- 카드 제목·부제: `FindTheKey.html`의 `ou-card__title`, `ou-card__sub`
- 상세 팝업의 제목·본문·이전/다음 링크: `OpportunitiesUnlocked-0N.html`의 `detail__category`, `detail__title`, `detail__body`

**⑧ 이미지 교체·추가·삭제**
[ASSETS.md](ASSETS.md)를 보세요. 핵심: **같은 이름·같은 확장자로 덮어쓰면** 코드 수정 없이 바뀝니다. 장수를 늘리거나 줄이면 HTML도 같이 고쳐야 하고, 사진 밑의 `Photo by. 이름` 출처 문구도 직접 바꿔야 합니다.

## 2-4. 수정할 때 조심할 것

- **`<br>`**: 줄바꿈입니다. 지우거나 옮기면 웹/모바일 줄 모양이 바뀝니다. 이 사이트는 모바일에서 손으로 넣은 줄바꿈이 유지되도록 글자 크기를 화면 폭에 맞춰 조절하고 있어서, **문구를 길게 바꾸면 모바일에서 글자가 작아지거나 줄이 꺾일 수 있습니다.**
- **`class="…"` 같은 이름은 바꾸지 마세요.** 글자만 바꾸세요. class는 스타일과 동작이 연결된 이름표입니다.
- **`<br class="mobile-break">`** 는 "모바일에서만 줄바꿈"이라는 뜻입니다. 지우지 마세요.
- **스크롤 연출**(스크롤하다 잠깐 멈추는 곳, 사진 확대 등)은 여러 스크립트가 얽혀 있습니다. **문구·이미지 수정은 안전하지만, 연출·높이·간격을 손대는 요청은 하나씩** 하고 README의 "통합 페이지 구조와 스크롤 동작"을 먼저 읽게 하세요.
- 폰트·색·간격은 임의 값 대신 README "디자인 규칙"의 값만 쓰세요.

## 2-5. 고친 뒤 확인 → 올리기

1. **로컬에서 확인**: 터미널에서 `python3 -m http.server 5173` → 크롬에서 `http://localhost:5173/FindTheKey.html`. (안 바뀌어 보이면 `Cmd+Shift+R`)
2. **모바일 화면 확인**: 크롬에서 `Cmd+Option+I`(개발자 도구) → `Cmd+Shift+M`(모바일 보기) → 폭을 390px 정도로. 모바일에서만 줄이 어색하지 않은지 꼭 보세요. **실제 폰으로도 한 번 보세요.**
3. **이미지를 건드렸다면**: `python3 scripts/check-assets.py` → "오류 없음 ✅"이 나와야 함.
4. **올리기**: Claude에게 "커밋하고 push해줘" (또는 GitHub Desktop의 Commit → Push).
5. **배포본 확인**: 1~2분 뒤 https://juhyun-bot.github.io/special-creator-web/FindTheKey.html 에서 확인. 옛 화면이 보이면 `Cmd+Shift+R` 또는 주소 뒤에 `?v=1`.

## 2-6. 잘못 고쳤을 때 되돌리기

| 상황 | 방법 |
|---|---|
| 아직 **커밋 전**, 한 파일만 원래대로 | `git restore FindTheKey.html` (Claude에게 "이 파일 변경 취소해줘") |
| 커밋 전, 전부 취소 | Claude에게 "지금까지 바꾼 거 전부 원래대로 되돌려줘" (무엇이 사라지는지 먼저 보여달라고 하세요) |
| 이미 **push까지 했음** | Claude에게 "방금 커밋 되돌리는 새 커밋 만들어줘" (`git revert`). 히스토리를 지우지 않고 안전하게 되돌림 |

> 💡 **작은 단위로 자주 커밋하세요.** 문구 하나, 이미지 하나처럼 나눠서 올리면 문제가 생겼을 때 어느 변경 탓인지 찾기 쉽고 되돌리기도 쉽습니다.

## 2-7. 직접 고칠까, Claude에게 시킬까

| | 직접 편집 | Claude에게 |
|---|---|---|
| 잘 맞는 일 | 문구 한두 개, 숫자, 링크 하나 | 여러 파일에 복사된 것(헤더, Apply 링크), 이미지 추가, 모바일 조정, 배포·확인 |
| 주의 | 태그를 실수로 지우기 쉬움 | "웹/모바일 중 어디만"인지 범위를 말할 것 |

Claude에게 시킬 때 좋은 문장 예:
> FindTheKey.html의 FAQ 첫 번째 답변에서 "100명"을 "120명"으로 바꿔줘. 웹과 모바일 모두 줄바꿈이 어색하지 않은지 확인하고, 바꾼 내용은 커밋하지 말고 먼저 보여줘.
