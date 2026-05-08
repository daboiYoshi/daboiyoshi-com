"""404 page + a /home/ shim that mirrors the old Google Sites URL."""

NOT_FOUND = {
    "title":       "404 · Page not found — Snake Arcade",
    "description": "That page doesn't exist on Snake Arcade. Try the homepage or browse our tools.",
    "schema_type": "WebPage",
    "extra_head": '<meta name="robots" content="noindex">',
    "content": """
<div class="container">
  <section class="hero">
    <span class="hero-eyebrow">Error · 404</span>
    <h1><span class="accent">404</span><span class="cursor" aria-hidden="true"></span></h1>
    <p class="hero-lead">The page you tried to load isn't here. It may have moved when we migrated off Google Sites — or the URL is just wrong.</p>
    <div class="hero-cta">
      <a class="btn btn-primary" href="/">▶ Back home</a>
      <a class="btn" href="/tools-experiments/">Browse tools</a>
      <a class="btn btn-ghost" href="https://docs.daboiyoshi.com" rel="noopener">CDN Docs ↗</a>
    </div>
  </section>
</div>
""",
}

HOME_INDEX = {
    "title":       "Home — Snake Arcade",
    "description": "Snake Arcade home — games, tools, downloads, and project notes by daboiYoshi.",
    "schema_type": "WebPage",
    "extra_head": '<link rel="canonical" href="https://www.daboiyoshi.com/">',
    "content": """
<div class="container">
  <div class="page-head">
    <h1>Home</h1>
    <p class="lede">Welcome to Snake Arcade. The main landing page now lives at the site root — this page mirrors it for legacy links.</p>
  </div>

  <section style="padding-top:0">
    <div class="card-grid">
      <a class="card" href="../"><span class="card-tag">Main</span><h3 class="card-title">Snake Arcade Home</h3><p class="card-desc">Featured projects and what's new.</p><div class="card-meta"><span>OPEN</span><span class="arrow">→</span></div></a>
      <a class="card" href="downloads.html"><span class="card-tag">Files</span><h3 class="card-title">Downloads</h3><p class="card-desc">Installable builds and offline copies.</p><div class="card-meta"><span>OPEN</span><span class="arrow">→</span></div></a>
      <a class="card" href="1-0.html"><span class="card-tag">Game</span><h3 class="card-title">Snake Arcade 1.0</h3><p class="card-desc">Play the Final Game build.</p><div class="card-meta"><span>OPEN</span><span class="arrow">→</span></div></a>
      <a class="card" href="html-previewer.html"><span class="card-tag">Tool</span><h3 class="card-title">HTML Previewer</h3><p class="card-desc">Paste HTML, see a live preview.</p><div class="card-meta"><span>OPEN</span><span class="arrow">→</span></div></a>
      <a class="card" href="ende-crypter.html"><span class="card-tag">Tool</span><h3 class="card-title">En/De-crypter</h3><p class="card-desc">Encode and decode short strings.</p><div class="card-meta"><span>OPEN</span><span class="arrow">→</span></div></a>
    </div>
  </section>
</div>
""",
}


def build(render):
    render(NOT_FOUND,  "404.html")
    render(HOME_INDEX, "home/index.html")
