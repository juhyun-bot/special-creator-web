// fades/rises each photo in .gift-detail__grid into view as it's scrolled
// to, reusing the same initReveal helper (scroll-reveal.js) as the rest
// of the site (.cv-row, .btd-journey__row, etc.)
initReveal('.gift-detail__item', { stagger: 60 });

// mobile-only 뒤로가기 화살표 (.gift-detail__back-btn, see BeyondTheDoor-gift.css) —
// this page is reached by a real navigation from FindTheKey.html's "더보기" button, so
// it's plain browser-back; if there's no history (page opened directly / shared link)
// fall back to the Programs section of the main page
const giftBackBtn = document.getElementById('giftBackBtn');
if (giftBackBtn) {
  giftBackBtn.addEventListener('click', () => {
    if (history.length > 1) {
      history.back();
    } else {
      location.href = 'FindTheKey.html#beyond-the-door';
    }
  });
}
