/* ============================================================
   Snake Arcade — daboiyoshi.com
   Site script | vanilla, defer-loaded, no deps
   ============================================================ */
(function () {
  'use strict';

  // ---- Mobile nav toggle ----
  const toggle = document.querySelector('[data-nav-toggle]');
  const nav    = document.querySelector('[data-primary-nav]');

  if (toggle && nav) {
    toggle.addEventListener('click', () => {
      const open = nav.getAttribute('data-open') === 'true';
      nav.setAttribute('data-open', String(!open));
      toggle.setAttribute('aria-expanded', String(!open));
    });

    // Close on nav link tap (mobile)
    nav.addEventListener('click', (e) => {
      if (e.target.tagName === 'A') {
        nav.setAttribute('data-open', 'false');
        toggle.setAttribute('aria-expanded', 'false');
      }
    });

    // Close on Esc
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && nav.getAttribute('data-open') === 'true') {
        nav.setAttribute('data-open', 'false');
        toggle.setAttribute('aria-expanded', 'false');
        toggle.focus();
      }
    });
  }

  // ---- Year stamp in footer ----
  document.querySelectorAll('[data-year]').forEach((el) => {
    el.textContent = String(new Date().getFullYear());
  });

  // ---- Mark current page in nav ----
  const here = location.pathname.replace(/\/index\.html$/, '/').replace(/\.html$/, '');
  document.querySelectorAll('.primary-nav a').forEach((a) => {
    const href = a.getAttribute('href') || '';
    const norm = href.replace(/\/index\.html$/, '/').replace(/\.html$/, '');
    if (norm && (norm === here || (norm !== '/' && here.startsWith(norm)))) {
      a.setAttribute('aria-current', 'page');
    }
  });

  // ---- Optional iframe lazy boot for embedded tool pages ----
  // Pages that contain a launcher with [data-iframe-src] only mount the iframe
  // when the user clicks the "Launch in page" button — keeps initial paint fast.
  document.querySelectorAll('[data-launch-inline]').forEach((btn) => {
    btn.addEventListener('click', () => {
      const target = document.querySelector(btn.dataset.launchInline);
      const src    = btn.dataset.iframeSrc;
      if (!target || !src) return;
      target.innerHTML =
        '<iframe src="' + src + '" loading="lazy" title="Tool" ' +
        'style="width:100%;height:80vh;border:1px solid var(--border-bright);' +
        'border-radius:8px;background:#000" allow="fullscreen"></iframe>';
      btn.disabled = true;
      btn.textContent = 'LOADED';
    });
  });
})();
