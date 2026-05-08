# Snake Arcade — daboiyoshi.com (GitHub Pages build)

This is the static site for **www.daboiyoshi.com**, rebuilt to migrate off Google Sites and onto GitHub Pages.

It serves a sleek, mobile-first landing page plus launcher pages for the games and tools hosted on the existing CDN at **docs.daboiyoshi.com**. Other subdomains (`docs.`, `sar.`, `define.`, `secure.`, `void-breach.`, `snakenet.`, `about.`) keep their own hosting and are linked from this site, not migrated into it.

---

## Quick stats

| Metric | Value |
|---|---|
| Total pages | 44 |
| External tools linked | 22 |
| Stylesheet | 1 file, ~14 KB |
| JavaScript | 1 file, ~2 KB, vanilla, no deps |
| Frameworks | None |
| Build tool | Pure Python, optional |

---

## Repo structure

```
.
├── index.html                  # Landing page (the showpiece)
├── 404.html                    # Custom error page
├── about/                      # /about/ + 4 subpages
├── tools-experiments/          # Tools hub + 22 tool launcher pages
├── home/                       # Legacy /home/* URLs (downloads, html-previewer, etc.)
├── snake-ai/                   # /snake-ai/extra.html
├── *.html                      # Top-level direct nav targets (qr-code-generator, zen-timer, etc.)
├── assets/
│   ├── css/main.css            # Whole design system, 1 file
│   ├── js/main.js              # Mobile nav, year stamp, lazy iframe boot
│   └── images/                 # Favicons, OG cover, app icons
├── sitemap.xml                 # Generated, ~45 URLs
├── robots.txt                  # Allows all crawlers, references sitemap
├── manifest.webmanifest        # PWA manifest, dark theme
├── CNAME                       # Custom domain: www.daboiyoshi.com
└── .nojekyll                   # Disables Jekyll on GitHub Pages
```

---

## Editing content

**Two ways to edit:**

### Option A — Edit HTML directly (simpler)
The compiled HTML files in this repo are plain — open one, edit it, commit. Same as Google Sites was, just in a real text editor.

### Option B — Use the build script (easier for bulk changes)
The site was generated from Python page modules in `/build/pages/`. To change everything in lockstep — for example, adding a new tool that needs both a card on the homepage and its own launcher page — edit the page modules and re-run the build:

```bash
cd build
python3 build.py
```

That re-renders every page with the same shell template (`build/templates/shell.html`) so headers, footers, and meta tags stay consistent across the whole site.

You don't have to use the build script. If you only want to edit one page, just edit the HTML.

---

## Deployment

Full step-by-step lives in `Snake_Arcade_Migration_SOP.docx`. TL;DR:

1. Push this repo to GitHub.
2. **Settings → Pages**: source = `main` branch, root.
3. Add a custom domain: `www.daboiyoshi.com`.
4. Update DNS to point `www` at `<username>.github.io`.
5. Disable Google Sites publishing on `www.daboiyoshi.com` *after* the new site is live.

---

## License & credits

Content © daboiYoshi · Snake Arcade. See `/about/copyright.html` for terms.

Fonts: VT323, Press Start 2P, JetBrains Mono — all open-source, served from Google Fonts.

Build, design, and migration work: prepared as a complete drop-in replacement for the previous Google Sites build.
