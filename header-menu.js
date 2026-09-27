(function () {
  // shared by all 9 pages that use the .header component — toggles the
  // mobile dropdown nav (<=900px) via the hamburger button
  const header = document.querySelector('.header');
  const btn = document.getElementById('header-menu-btn');
  const links = document.getElementById('header-links');
  if (!header || !btn || !links) return;

  function closeMenu() {
    header.classList.remove('header--menu-open');
    btn.setAttribute('aria-expanded', 'false');
    document.body.style.overflow = '';
  }

  btn.addEventListener('click', () => {
    const isOpen = header.classList.toggle('header--menu-open');
    btn.setAttribute('aria-expanded', String(isOpen));
    // the menu is now a fullscreen panel (see FindTheKey.css/OpportunitiesUnlocked-0N.css
    // etc.'s mobile .header__links redesign) — lock body scroll behind it while open,
    // otherwise the page's own scroll-snap can jump sections underneath
    document.body.style.overflow = isOpen ? 'hidden' : '';
  });

  links.querySelectorAll('a').forEach((a) => {
    a.addEventListener('click', closeMenu);
  });

  window.addEventListener('resize', () => {
    if (window.innerWidth > 900) closeMenu();
  });
})();
