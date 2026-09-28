# 이미지·에셋 관리 가이드

이미지를 **바꾸거나, 늘리거나, 지울 때** 이 문서만 보면 되도록 정리했습니다. 폴더 규칙, 파일명 규칙, 그리고 "이 사진은 코드 어디에 적혀 있나"까지 한 곳에 있습니다.

> **먼저 이해할 것 — 이 사이트에는 이미지 목록 파일이 없습니다.**
> 사진 경로가 `FindTheKey.html` 등 HTML 안에 **하나하나 직접 적혀 있어요.** (`<img src="assets/…">` 또는 `style="background-image:url('assets/…')"`) 그래서 작업이 두 종류로 나뉩니다.
>
> | 하고 싶은 일 | 난이도 | 방법 |
> |---|---|---|
> | 사진 **내용만 교체** (같은 자리, 같은 장수) | 쉬움 | **같은 파일명·같은 확장자로 덮어쓰기**. 코드 수정 없음 |
> | 사진 **추가/삭제/순서 변경** | HTML 수정 필요 | 아래 "슬롯별 표"의 *코드에서 고칠 곳* 참고 |
> | 파일명·폴더 **이름 변경** | 위험 | 그 파일을 쓰는 모든 HTML/JS도 같이 바꿔야 함 → 반드시 `check-assets.py` 실행 |

## 작업 후 반드시 하는 점검 (1분)

```bash
python3 scripts/check-assets.py
```

- 코드가 가리키는데 **파일이 없는 경우**, **대소문자가 다른 경우**를 잡아줍니다. 종료 코드 0이면 통과.
- **왜 필요한가**: 맥은 `step3-10.JPG`와 `step3-10.jpg`를 같은 파일로 봐서 로컬에서는 잘 보입니다. 그런데 배포 서버(GitHub Pages)는 다른 파일로 봐서 **배포본에서만 이미지가 깨집니다.** 가장 흔한 사고예요.
- 참고로 "어디서도 안 쓰는 파일"과 "2MB 넘는 큰 파일" 목록도 같이 보여줍니다.
- 이 스크립트는 파이썬 3만 있으면 되고, 아무것도 수정하지 않습니다(읽기 전용).

## 폴더 구조 = 페이지 구조

`assets/` 아래는 **화면 위에서 아래로 나오는 섹션 순서대로 번호**를 붙였습니다. 새 이미지는 자기가 들어가는 섹션 폴더에 넣으세요.

```
assets/
├─ 00-hero/            hero-home.html(열쇠구멍 첫 화면) 전용
├─ 01-about/           About 섹션
│   ├─ rolling/        히어로 롤링 5장 + 스크랩북 4장
│   └─ trophy-3d-texture/   3D 트로피 재질
├─ 02-opportunities/   Opportunities 섹션
│   ├─ 01-… ~ 05-…/    카드 5개 각각의 폴더 (썸네일 + 상세 사진)
│   └─ brand-logos/    로고 롤링 21개
├─ 03-program/         Programs 섹션
│   ├─ journey/step1~4/    여정 4단계 롤링 사진
│   ├─ meetup/             "직접 만나 나누는 시간" 갤러리 9장
│   └─ gift/gift1~4/       선물 4종 상세 페이지 사진
├─ 04-voices/story/    Voices 인터뷰 사진 4장
└─ (루트) nav-icon.svg, hero-icon.svg, icon-*.svg, logo-*.svg   여러 섹션이 같이 쓰는 아이콘/로고
```

**규칙 1. 섹션 폴더를 섞지 않는다.** 같은 사진을 두 섹션이 쓰더라도(예: About 롤링 사진 → hero-home 키홀) 파일은 **한 곳에만 두고** 다른 곳은 그 경로를 가리키게 합니다.
**규칙 2. 폴더는 소문자·영문·하이픈.** (`journey`, `meetup`, `gift1` …) 단, 아래 두 폴더는 예외로 이미 대문자/공백이 있어요: `01-93 CUPS, 93 STORIES`(공백·쉼표 포함), `05-Branded-Taste`(대문자). 이름을 바꾸지 말고 그대로 쓰세요. 코드에는 공백이 `%20`, 쉼표가 `%2C`로 적혀 있습니다.

## 파일명 규칙

기본 패턴은 **`<주제>-<번호 두 자리>.<확장자>`** — 예: `step2-03.jpg`, `gift1-07.jpg`, `atelier-02.jpg`.

| 규칙 | 설명 |
|---|---|
| 번호는 **두 자리** (`01`, `02` … `10`) | 정렬이 맞고, 다른 폴더와 모양이 같음 |
| 확장자는 **소문자 `.jpg`** 권장 | 대문자(`.JPG`)는 코드도 똑같이 대문자로 적어야 해서 사고가 잦음 |
| **새 파일은 영문+숫자+하이픈**만 | 한글 파일명은 맥(NFD)↔서버(NFC) 표기 차이로 깨질 수 있음 |
| 번호가 **빈 채로 남아도 괜찮음** | 사진을 지우면 번호가 비는데(예: `step3-09` 없음) 억지로 당겨서 다시 번호 매기지 말 것 — 코드 경로를 전부 바꿔야 해서 오히려 위험 |

**예외로 이미 한글 이름을 쓰는 곳** (지금은 잘 동작 중 — 건드리지 말고, 새로 추가할 때만 영문으로):
- `01-about/rolling/about-roll-<인스타ID>.jpg`, `about-scrapbook-<이름>.jpg` — 파일명 = 출처(크레딧) 이름
- `02-opportunities/brand-logos/<반기>_<브랜드>.png` — 예: `25상반기_LG.png`, `26상반기_데스커.png` (몇 년 몇 반기에 들어온 브랜드인지 기록)
- `02-opportunities/05-Branded-Taste/01-… ~ 06-….png` — `<번호>-<프로그램명>_<채널>` 형식
- `03-program/meetup/공간_<장소>_<번호>.jpg`

> 참고: 스크랩북 파일명은 `about-scrapbook-라료하우스.jpg`(하이픈)와 `about-scrapbook_리디홈.jpg`(밑줄)이 섞여 있습니다. 이미 코드가 그 이름으로 연결돼 있어서 그대로 뒀어요. **새 파일은 하이픈 하나로 통일**하세요.

## 슬롯별 표 — 어떤 사진이 어디에 어떻게 쓰이나

**"코드에서 고칠 곳"이 비어 있으면 = 같은 이름으로 덮어쓰기만 하면 끝**이라는 뜻입니다.
(별도 표기가 없으면 파일은 모두 `FindTheKey.html`에 적혀 있습니다.)

### 00-hero — 열쇠구멍 첫 화면 (`hero-home.html`)

| 파일 | 용도 | 권장 크기 | 비고 |
|---|---|---|---|
| `key-photo.png` | 첫 화면 아래 3D 열쇠 이미지 | 현재 1023×1537, 배경 투명 PNG | About의 키 사진(`about-key-photo.jpg`)과 **별개 파일**. 서로 안 건드림 |
| `key-shadow-1/2.svg`, `logo-*.svg` | 그림자·로고 | SVG | 교체 시 같은 이름으로 |

### 01-about — About 섹션

| 파일 | 장수 | 용도 | 권장 비율/크기 | 코드에서 고칠 곳 (장수·순서 바꿀 때) |
|---|---|---|---|---|
| `rolling/about-roll-*.jpg` | 5 | 히어로 롤링(스크롤로 넘어가며 마지막 장은 풀스크린) | 세로 3:4 (현재 약 1080×1440) | ① `FindTheKey.html`의 `.about-roll__item` ② **`about-hero-roll.js` 상단(47행 부근)의 `CREDITS` 배열** — 사진 순서와 **같은 순서**로 출처 이름을 넣어야 함 ③ 첫 장의 출처는 HTML의 `.about-photo__credit`에도 적혀 있음 ④ **`hero-home.html`의 `.hero-pin__photos` 안 앞 3장**이 같은 파일을 가리킴 |
| `rolling/about-scrapbook-*.jpg` | 4 | 스크랩북(2열 × 2장) | 세로 3:4 (약 1080×1440) | `FindTheKey.html`의 `.about-scrapbook` — 사진마다 `.about-photo__credit` 문구가 옆에 있음 |
| `about-key-photo.jpg` | 1 | 키 사진 프레임(중앙 정지→풀스크린 확대→디졸브) | 세로 2:3 (현재 2000×3000) | 출처 표기 없음 |
| `SC_01_Blk.gif` | 1 | 스페셜 크리에이터 배지 모션 | 정사각 (1080×1080) | |
| `trophy.glb`, `trophy-3d-texture/*` | — | 3D 트로피 (`trophy.js`) | — | **`trophy-texture-org.png`(원본 사진)는 절대 덮어쓰지 말 것** — README 참고 |

⚠️ **About 롤링 사진을 바꿀 때 가장 자주 빠뜨리는 것**: `about-hero-roll.js`의 `CREDITS`와 `hero-home.html`의 3줄. 사진만 바꾸면 **출처 이름이 옛날 사진 것으로 남거나** 첫 화면 키홀 속 사진만 안 바뀝니다.

### 02-opportunities — Opportunities 섹션

카드 5개 = 폴더 5개. 카드를 누르면 상세 페이지(`OpportunitiesUnlocked-0N.html`)가 팝업으로 뜹니다.

| 폴더 | 썸네일 | 상세 사진 | 상세 페이지 |
|---|---|---|---|
| `01-93 CUPS, 93 STORIES` | `thumb-yido.jpg` | `yido-01-poster.png`(첫 장, 포스터라 잘리지 않게 `contain`) + `yido-01~05.jpg` = 6장 | `OpportunitiesUnlocked-01.html` |
| `02-space-airbnb` | `thumb.jpg` | `image-01~04.jpg` = 4장 | `-02.html` |
| `03-space-storymarket` | `thumb-storymarket.jpg` | `storymarket-01~06.jpg` = 6장 | `-03.html` |
| `04-space-atelier` | `thumb.jpg` | `atelier-01~05.jpg` = 5장 | `-04.html` |
| `05-Branded-Taste` | `thumb.png` | `01-…myfavehobby.png` ~ `06-…MOPO.png` = 6장 | `-05.html` |

- **썸네일**: `FindTheKey.html`의 `.ou-card__photo` (카드 크기 291×430, 마우스 올리면 394×520 — 위아래가 `cover`로 잘림). 카드 제목·부제도 같은 위치의 `.ou-card__title` / `.ou-card__sub`.
- **상세 사진**: 화면 오른쪽 절반(폭 약 49%, 높이는 화면 전체)을 `cover`로 채움 → **세로로 긴 사진이 잘 어울림**. 가로 사진은 좌우가 잘리니, 잘리면 안 되는 사진(포스터·글자 있는 이미지·16:9 영상 썸네일)에는 `detail__photo-img--contain` 클래스를 붙임(예: 01번 첫 장, 05번의 2·3번째).
- 상세 사진 장수를 바꾸면 `OpportunitiesUnlocked-0N.html`의 `.detail__photo-slide` 줄을 추가/삭제. 캐러셀(`detail-photo-carousel.js`)은 장수를 **자동으로 셈**.
- ⭐ **05번만 특별**: 사진 1장마다 본문에 **링크가 하나씩 짝**으로 붙습니다. 사진을 추가/삭제/순서 변경하면 링크도 같이 맞춰야 해요. 한 사진당 손볼 곳이 **3군데**입니다 — ① `.detail__photo-slide`(사진) ② `#detailLinks`의 `.detail__link`(데스크톱용 링크) ③ `.detail__photo-link`(모바일용 링크, 사진 바로 아래). 셋 다 **같은 순서**여야 함. 현재 링크(사진 순서대로): myfavehobby(YouTube) / 88like(YouTube) / 원삼집(YouTube) / tovhaus(Instagram 릴스) / 제니홈무드(Instagram 릴스) / MOPO(Instagram 릴스).

**로고 롤링** `brand-logos/` — 21개, 파일명 `<반기>_<브랜드>.png`
- 박스 **152×59, `contain`** → 로고를 **304×118(2배 해상도), 배경 투명 PNG**로 만들면 박스에 딱 맞음.
- 로고 1개는 HTML에 **두 번** 적혀 있음(무한 롤링용 복제 세트). 내용만 교체 → 덮어쓰기. **추가하려면 `.brand-rolling__track` 안 앞 세트 끝과 복제 세트 끝, 총 2줄**을 넣기. `alt`에는 브랜드 이름.
- 롤링 속도는 `FindTheKey.css`의 `brand-rolling-scroll 30s`(개수를 크게 바꾸면 비례해서 조정).

### 03-program — Programs 섹션

| 폴더 | 장수(현재) | 용도 | 크기 | 코드에서 고칠 곳 |
|---|---|---|---|---|
| `journey/step1~4/` | 6 / 8 / 11 / 7 | 여정 4단계 각각의 가로 롤링 | 박스 **244×320**(세로형, `cover`). 현재 약 720×900 | `FindTheKey.html`의 `.btd-journey__rolling-item` — 사진 1장이 **두 번**(복제 세트) 적혀 있음. **표시 순서는 파일 번호 순이 아님**(코드에 적힌 순서). 사진마다 `Photo by.` 출처 문구가 같이 있음(step3만 없음) |
| `meetup/` | 9 | "직접 만나 나누는 시간" 코버플로 갤러리 | 현재 가로형(3:2, 약 3120×2080)이 많음 | `.btd-gallery__stack-item` 1개 = 사진 1장(복제 없음). 스크립트가 장수를 자동으로 셈 |
| `gift/gift1~4/` | 13 / 32 / 12 / 17 | 선물 4종 "더보기" 상세 페이지 사진 그리드 | 세로 3:4 (약 750×1000) | `BeyondTheDoor-gift1~4.html`의 `.gift-detail__item` 1개 = 사진 1장 + `Photo by.` 출처. (`gift2-19.avif`만 avif 형식) |
| (메인의 선물 카드 썸네일) | 카드당 3장 | 카드 위 부채꼴로 펼쳐지는 사진 3장 | — | `FindTheKey.html`의 `.btd-gift__stack-photo--left/right/front` 3줄. **어떤 번호를 쓸지가 여기에 적혀 있음**(예: gift2는 `04/05/06`, 나머지는 `01/02/03`) — 그 번호 파일을 지우면 여기가 깨짐 |

- **롤링 사진을 추가할 때 (journey)**: 새 사진을 `stepN-XX.jpg`로 넣고 → 같은 `.btd-journey__rolling-item` 줄을 **앞 세트 끝 + 복제 세트 끝, 2군데**에 추가 → 사진이 늘어난 만큼 롤링이 빨라져 보이므로 `FindTheKey.css`의 `btd-journey-rolling-scroll 25s`를 장수 비율만큼 늘림.
- **출처(크레딧)**: 모든 사진 위의 `Photo by. 이름` 문구는 **코드에 직접 적힌 글자**입니다(파일명과 자동 연동 아님). 사진을 바꾸면 출처도 같이 바꿔주세요. 지금까지는 **출처를 알 수 없는 사진은 넣지 않는 방식**으로 진행해 왔습니다(선물 상세·About·journey 사진 모두 출처가 표기돼 있음. journey의 step3만 표기 없음).

### 04-voices — Creator Voices

| 파일 | 용도 | 권장 |
|---|---|---|
| `story/cv-<이름>.jpg` × 4 | 인터뷰 행 사진(495×340 박스, `cover`) | 세로/가로 무관, 폭 900~1080px 정도면 충분 |

`FindTheKey.html`의 `.cv-row__photo` 4곳. 이름·본문 글자도 같은 행 안에 있음.

### 루트 공용 아이콘

`nav-icon.svg`(헤더 로고) · `hero-icon.svg` · `icon-go.svg`(카드 화살표) · `icon-close.svg`(팝업 닫기 X) · `icon-back.svg`(모바일 뒤로가기) · `icon-instagram.svg`(푸터) · `logo-ohouse-special-creator.svg`(푸터 로고). 여러 페이지가 같이 쓰니 **덮어쓰기만** 하세요.

## 새 이미지 준비 방법 (권장)

1. **원본을 그대로 넣지 마세요.** 지금도 원본급 큰 파일(수 MB~25MB)이 남아 있어서 첫 로딩이 느립니다(`check-assets.py`가 목록을 보여줌). 한 번 커밋되면 깃 히스토리에 **영구히** 남아 저장소가 무거워집니다.
2. 맥에서 한 줄로 줄이기 (긴 변 1200px, JPEG 품질 80):
   ```bash
   sips -Z 1200 -s format jpeg -s formatOptions 80 원본.jpg --out assets/03-program/journey/step2/step2-09.jpg
   ```
   (여러 장은 `for f in *.jpg; do …; done`) — 상세 사진은 1200~1600px, 작은 롤링 사진은 720~1000px이면 충분.
3. **목표 용량**: 사진 1장 **500KB 이하**(어쩔 수 없어도 1MB).
4. 파일을 넣고 → HTML 수정(필요한 경우) → `python3 scripts/check-assets.py` → 브라우저에서 확인(강력 새로고침 `Cmd+Shift+R`) → 커밋/푸시.

## 작업별 체크리스트

**사진 내용만 교체**: 같은 이름·같은 확장자로 덮어쓰기 → (출처가 다르면 `Photo by.` 문구 수정) → 점검 스크립트.

**사진 한 장 추가**: ① 규칙대로 파일명 짓기 ② 해당 폴더에 넣기 ③ 위 슬롯 표의 *코드에서 고칠 곳* 수정(복제 세트가 있는 곳은 **2군데**) ④ 출처 문구 ⑤ 점검 스크립트.

**사진 한 장 삭제**: ① HTML에서 그 줄 제거(복제 세트가 있으면 **2군데**) ② 파일 삭제 ③ 점검 스크립트(다른 곳에서 안 쓰는지 확인됨). 번호는 당기지 말 것.

**섹션 폴더 이름을 바꾸고 싶을 때**: 하지 마세요. 꼭 필요하면 `git mv`로 옮기고, 모든 참조를 일괄 치환한 뒤 점검 스크립트가 통과하는지 확인하고, **push 후 배포본에서 이미지가 뜨는지 직접 열어볼 것**(로컬이 멀쩡해도 배포본이 깨질 수 있음).

## 알려진 함정 모음

- **`.JPG` 대문자**: `step3-10/11/12.JPG` 세 개가 대문자입니다. 코드도 대문자로 적혀 있으니 지금은 정상. 이름을 바꾸거나 새로 만들 땐 소문자 `.jpg`로 통일해서, 코드와 파일이 같은지 점검 스크립트로 확인하세요.
- **공백/쉼표 폴더**: `01-93 CUPS, 93 STORIES` — 코드에서 `01-93%20CUPS%2C%2093%20STORIES`로 적혀 있는 게 정상(브라우저 주소용 표기). 점검 스크립트는 이 표기를 알아서 풀어서 비교합니다.
- **캐시**: 이미지를 덮어썼는데 안 바뀌어 보이면 브라우저 캐시입니다. 강력 새로고침(`Cmd+Shift+R`). 배포본은 GitHub Pages 캐시(약 10분)도 있어서 push 직후엔 옛 이미지가 보일 수 있음.
- **한 파일을 두 곳에서 쓸 때**: About 롤링 앞 3장은 hero-home도 씀. 새로 이런 공유를 만들지 말 것(지우거나 바꿀 때 한쪽이 깨짐).
- **`.DS_Store`**: 맥이 폴더마다 만드는 파일. 깃에는 안 올라가도록 `.gitignore`에 들어 있음.
