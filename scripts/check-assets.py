#!/usr/bin/env python3
"""이미지/에셋 점검 — push 전에 실행하세요.

    python3 scripts/check-assets.py

무엇을 검사하나
  1) 코드(HTML/CSS/JS)가 가리키는 assets/ 파일이 실제로 있는지 (없으면 배포본에서 404)
  2) 대소문자가 정확히 같은지 — macOS는 대소문자를 무시해서 로컬에선 멀쩡하지만
     GitHub Pages(리눅스)에서는 404가 납니다. 예: step3-10.JPG 를 step3-10.jpg 로 적으면 사고
  3) 아무 데서도 안 쓰는 assets/ 파일 (지워도 되는 후보)
  4) 용량이 큰 이미지 (첫 로딩이 느려지는 원인)

오류(1, 2)가 있으면 종료 코드 1, 없으면 0. (3, 4)는 참고용 목록이라 종료 코드에 영향 없음.
빌드 도구 없이 파이썬 3만 있으면 됩니다.
"""
import glob
import os
import re
import sys
import unicodedata
import urllib.parse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

BIG_KB = 2048  # 이 이상이면 "큰 이미지"로 알림
IGNORE_NAMES = {".DS_Store"}

# assets/ 로 시작하고 파일 확장자로 끝나는 경로 (HTML src/href, CSS url(), JS 문자열 모두 잡음).
# - 파일명에 공백이 있어도 됨 ("02-전국 내집자랑_88like.jpeg")
# - 확장자로 끝나야 하므로 주석 속 폴더 언급("assets/03-program/gift/")은 무시됨
EXTS = "jpe?g|png|gif|svg|webp|avif|glb|gltf|obj|fbx|mp4|webm|woff2?|json"
REF_RE = re.compile(
    r"""assets/[^"'()<>]*?\.(?:%s)(?=["'()<>?#\s]|$)""" % EXTS, re.IGNORECASE
)


def nfc(s):
    return unicodedata.normalize("NFC", s)


def exact_case_exists(path):
    """경로의 각 단계가 대소문자까지 정확히 있는지 (한글 NFC/NFD 차이는 같은 것으로 봄)."""
    cur = "."
    for part in path.split("/"):
        try:
            names = os.listdir(cur)
        except OSError:
            return False
        if not any(nfc(n) == nfc(part) for n in names):
            return False
        # 실제 이름으로 이어서 내려감 (NFD 이름이어도 열리도록)
        cur = os.path.join(cur, next(n for n in names if nfc(n) == nfc(part)))
    return True


def main():
    sources = sorted(glob.glob("*.html") + glob.glob("*.css") + glob.glob("*.js"))
    refs = {}  # 디코딩한 경로 -> 그걸 쓰는 파일들
    for f in sources:
        text = open(f, encoding="utf-8").read()
        for m in REF_RE.findall(text):
            p = urllib.parse.unquote(m.split("?")[0].split("#")[0])
            refs.setdefault(p, set()).add(f)

    missing, wrong_case = [], []
    for p, users in sorted(refs.items()):
        if os.path.exists(p) and not exact_case_exists(p):
            wrong_case.append((p, users))
        elif not os.path.exists(p):
            missing.append((p, users))

    on_disk = []
    for dirpath, _, files in os.walk("assets"):
        for name in files:
            if name not in IGNORE_NAMES:
                on_disk.append(nfc(os.path.join(dirpath, name)))
    used = {nfc(p) for p in refs}
    unused = sorted(p for p in on_disk if p not in used)
    big = sorted(
        ((os.path.getsize(p) // 1024, p) for p in on_disk if os.path.getsize(p) // 1024 >= BIG_KB),
        reverse=True,
    )

    def show(title, rows):
        print(f"\n{title}")
        for p, users in rows:
            print(f"  - {p}\n      쓰는 곳: {', '.join(sorted(users))}")

    print(f"코드에서 찾은 assets 참조 {len(refs)}개 / assets 폴더 실제 파일 {len(on_disk)}개")
    if missing:
        show("❌ 파일이 없음 (배포하면 404) — 파일명·폴더·확장자 확인", missing)
    if wrong_case:
        show("❌ 대소문자가 달라서 GitHub Pages에서 404 — 코드의 경로를 실제 파일명과 똑같이", wrong_case)
    if unused:
        print(f"\nℹ️ 어디서도 안 쓰는 파일 {len(unused)}개 (지워도 되는 후보 — 지우기 전에 확인)")
        for p in unused:
            print(f"  - {p}")
    if big:
        print(f"\nℹ️ {BIG_KB // 1024}MB 이상 큰 파일 {len(big)}개 (줄이면 로딩이 빨라짐)")
        for kb, p in big:
            print(f"  - {kb / 1024:.1f}MB  {p}")

    if missing or wrong_case:
        print("\n결과: 고쳐야 할 오류가 있습니다.")
        return 1
    print("\n결과: 오류 없음 ✅ (참조된 모든 파일이 있고 대소문자도 일치)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
