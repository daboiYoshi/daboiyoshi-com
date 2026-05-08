"""/home/* subpages from the original Google Sites structure."""

DOWNLOADS = {
    "title":       "Downloads — Snake Arcade",
    "description": "Download Snake Arcade builds, the SnakeNet browser, the Chrome extension, and other installable releases.",
    "schema_type": "WebPage",
    "content": """
<div class="container">
  <div class="page-head">
    <nav class="crumbs" aria-label="Breadcrumb">
      <a href="../">Home</a><span>/</span><span aria-current="page">Downloads</span>
    </nav>
    <h1>Downloads</h1>
    <p class="lede">Installable releases and packaged builds from the Snake Arcade project.</p>
  </div>

  <section style="padding-top:0">
    <div class="card-grid">

      <a class="card" href="https://docs.daboiyoshi.com/SnakeNet/SnakeNet.dmg" rel="noopener" data-external="true">
        <span class="card-tag">Browser · macOS</span>
        <h3 class="card-title">SnakeNet</h3>
        <p class="card-desc">Simple custom web browser for macOS. Enter a URL, pick a color palette. Windows .exe coming.</p>
        <div class="card-meta"><span>.DMG</span><span class="arrow">↓</span></div>
      </a>

      <a class="card" href="https://drive.google.com/uc?export=download&id=1rYeRhpZ4vCNG4OjTSn44QdKlycBU3MlZ" rel="noopener" data-external="true">
        <span class="card-tag">Chrome Extension</span>
        <h3 class="card-title">Snake Arcade Extension</h3>
        <p class="card-desc">Pin Snake Arcade to your Chrome toolbar. Unpacked-load install.</p>
        <div class="card-meta"><span>.ZIP</span><span class="arrow">↓</span></div>
      </a>

      <a class="card" href="https://docs.daboiyoshi.com/game/index.html" rel="noopener" data-external="true">
        <span class="card-tag">Game · Web</span>
        <h3 class="card-title">Snake Arcade 1.0</h3>
        <p class="card-desc">The Final Game build. No download — opens straight in your browser.</p>
        <div class="card-meta"><span>PLAY</span><span class="arrow">→</span></div>
      </a>

      <a class="card" href="https://docs.daboiyoshi.com/game/classic-games/snake_arcade_0.5.html" rel="noopener" data-external="true">
        <span class="card-tag">Game · Web</span>
        <h3 class="card-title">Snake Arcade 0.5 (IDP)</h3>
        <p class="card-desc">The Initial Development Phase build. The original solo daboiYoshi version.</p>
        <div class="card-meta"><span>PLAY</span><span class="arrow">→</span></div>
      </a>

      <a class="card" href="https://docs.daboiyoshi.com/game/classic-games/blockade.html" rel="noopener" data-external="true">
        <span class="card-tag">Classic · Web</span>
        <h3 class="card-title">Blockade Clone</h3>
        <p class="card-desc">A clone of the original 1976 Gremlin "Blockade" — the first-ever snake game.</p>
        <div class="card-meta"><span>PLAY</span><span class="arrow">→</span></div>
      </a>

    </div>
  </section>

  <section>
    <div class="prose">
      <h2>How to install the Chrome extension</h2>
      <ol>
        <li>Download the ZIP from the card above and unzip the folder.</li>
        <li>In Chrome, open <code>chrome://extensions</code>.</li>
        <li>Toggle <strong>Developer Mode</strong> on (top right).</li>
        <li>Click <strong>Load Unpacked</strong> and select the unzipped folder.</li>
        <li>Pin the extension to your toolbar.</li>
      </ol>
    </div>
  </section>
</div>
""",
}

HTML_PREVIEWER = {
    "title":       "HTML Previewer — Snake Arcade",
    "description": "Paste HTML, see a live preview side-by-side. Useful for testing snippets and small layouts.",
    "schema_type": "WebApplication",
    "schema_category": "DeveloperApplication",
    "content": """
<div class="container">
  <div class="page-head">
    <nav class="crumbs" aria-label="Breadcrumb">
      <a href="../">Home</a><span>/</span><span aria-current="page">HTML Previewer</span>
    </nav>
    <h1>HTML Previewer</h1>
    <p class="lede">Paste HTML, see a live preview. Quick way to test a snippet without setting up a sandbox.</p>
  </div>

  <section style="padding-top:0">
    <div class="launcher">
      <div class="hero-cta">
        <a class="btn btn-primary" href="https://docs.daboiyoshi.com/HTML-Previewer/index.html" rel="noopener">▶ Open the previewer</a>
        <button class="btn" data-launch-inline="#embed-mount" data-iframe-src="https://docs.daboiyoshi.com/HTML-Previewer/index.html">Launch in page</button>
      </div>
      <div id="embed-mount"></div>
    </div>
  </section>
</div>
""",
}

ENDE_CRYPTER = {
    "title":       "En/De-crypter — Snake Arcade",
    "description": "Encode and decode short strings using common reversible encodings. Browser-only — nothing leaves your device.",
    "schema_type": "WebApplication",
    "schema_category": "SecurityApplication",
    "content": """
<div class="container">
  <div class="page-head">
    <nav class="crumbs" aria-label="Breadcrumb">
      <a href="../">Home</a><span>/</span><span aria-current="page">En/De-crypter</span>
    </nav>
    <h1>En/De-crypter</h1>
    <p class="lede">Encode and decode short strings with common reversible encodings. Useful for quick lookups and debugging.</p>
  </div>

  <section style="padding-top:0">
    <div class="launcher">
      <div class="launcher-meta">
        <span><strong>Note:</strong> not for high-security use — encoding is not encryption.</span>
      </div>
      <div class="hero-cta">
        <a class="btn btn-primary" href="https://docs.daboiyoshi.com/En-De-Crypter/index.html" rel="noopener">▶ Open the tool</a>
        <button class="btn" data-launch-inline="#embed-mount" data-iframe-src="https://docs.daboiyoshi.com/En-De-Crypter/index.html">Launch in page</button>
      </div>
      <div id="embed-mount"></div>
    </div>
  </section>
</div>
""",
}

ONE_O = {
    "title":       "Snake Arcade 1.0 — the Final Game build",
    "description": "Snake Arcade 1.0 — Final Game (FG) build. Fixed and polished by the Snake Arcade dev team. Plays in your browser.",
    "schema_type": "VideoGame",
    "schema_extra": {
        "genre": "Arcade",
        "playMode": "SinglePlayer",
        "applicationCategory": "Game",
    },
    "content": """
<div class="container">
  <div class="page-head">
    <nav class="crumbs" aria-label="Breadcrumb">
      <a href="../">Home</a><span>/</span><span aria-current="page">Snake Arcade 1.0</span>
    </nav>
    <h1>Snake Arcade 1.0</h1>
    <p class="lede">The FG (Final Game) build. Fixed and polished by the Snake Arcade dev team.</p>
  </div>

  <section style="padding-top:0">
    <div class="launcher">
      <div class="launcher-meta">
        <span><strong>Version:</strong> 1.0 (FG)</span>
        <span><strong>Type:</strong> Browser game</span>
        <span><strong>Cost:</strong> Free</span>
      </div>
      <div class="hero-cta">
        <a class="btn btn-primary" href="https://docs.daboiyoshi.com/game/index.html" rel="noopener">▶ Play 1.0</a>
        <a class="btn" href="https://docs.daboiyoshi.com/game/classic-games/snake_arcade_0.5.html" rel="noopener">Play 0.5 (IDP)</a>
        <a class="btn btn-ghost" href="downloads.html">Downloads</a>
      </div>
    </div>
  </section>

  <section>
    <div class="prose">
      <h2>Want the Scratch edition?</h2>
      <p><a href="https://scratch.mit.edu/projects/1285720576" rel="noopener">Snake Arcade on Scratch →</a></p>
    </div>
  </section>
</div>
""",
}


def build(render):
    render(DOWNLOADS,       "home/downloads.html")
    render(HTML_PREVIEWER,  "home/html-previewer.html")
    render(ENDE_CRYPTER,    "home/ende-crypter.html")
    render(ONE_O,           "home/1-0.html")
