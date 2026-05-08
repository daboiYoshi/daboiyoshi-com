"""Landing page — the homepage at /"""

CONTENT = """
<section class="hero">
  <div class="container">
    <span class="hero-eyebrow">v1.0 · Final Game · 2026</span>
    <h1>SNAKE <span class="accent">ARCADE</span><span class="cursor" aria-hidden="true"></span></h1>
    <p class="hero-lead">
      A growing collection of browser games, tools, and experiments
      built in HTML by daboiYoshi and the Snake Arcade dev team. No accounts,
      no installs, no tracking — just open a tab and play.
    </p>
    <div class="hero-cta">
      <a class="btn btn-primary" href="https://docs.daboiyoshi.com/game/index.html" rel="noopener">▶ Play Snake 1.0</a>
      <a class="btn" href="tools-experiments/">Browse Tools</a>
      <a class="btn btn-ghost" href="about/">About the project</a>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-head">
      <h2>What's new</h2>
      <a class="section-link" href="about/">View changelog →</a>
    </div>
    <div class="card-grid">
      <a class="card" href="https://snakenet.daboiyoshi.com/" data-external="true" rel="noopener">
        <span class="card-tag">Browser · macOS</span>
        <h3 class="card-title">SnakeNet</h3>
        <p class="card-desc">A simple, customizable web browser for macOS. Enter a URL, pick a color palette, browse. Windows .exe coming.</p>
        <div class="card-meta"><span>NEW</span><span class="arrow">→</span></div>
      </a>

      <a class="card" href="https://define.daboiyoshi.com" data-external="true" rel="noopener">
        <span class="card-tag">Reference</span>
        <h3 class="card-title">Snake Definer</h3>
        <p class="card-desc">Pocket dictionary that defines any English word. Mobile-optimized. Powered by Free Dictionary API.</p>
        <div class="card-meta"><span>NEW</span><span class="arrow">→</span></div>
      </a>

      <a class="card" href="https://void-breach.daboiyoshi.com/" data-external="true" rel="noopener">
        <span class="card-tag">Game · 3D</span>
        <h3 class="card-title">Void Breach</h3>
        <p class="card-desc">Our biggest game yet — now on its own subdomain. Updated and ready to play.</p>
        <div class="card-meta"><span>UPDATED</span><span class="arrow">→</span></div>
      </a>

      <a class="card" href="https://docs.daboiyoshi.com/Snake-Paint/" data-external="true" rel="noopener">
        <span class="card-tag">Creative</span>
        <h3 class="card-title">Snake Paint</h3>
        <p class="card-desc">HTML paint app — pencil, brush, eraser, fill, shapes, text, spray. Refreshed UI.</p>
        <div class="card-meta"><span>UPDATED</span><span class="arrow">→</span></div>
      </a>

      <a class="card" href="https://docs.daboiyoshi.com/Snake-Media-Player/index.html" data-external="true" rel="noopener">
        <span class="card-tag">Media</span>
        <h3 class="card-title">Snake Media Player</h3>
        <p class="card-desc">Drop in MP4, MKV, AVI, MOV, WebM, MP3, FLAC, WAV, OGG. All client-side.</p>
        <div class="card-meta"><span>NEW</span><span class="arrow">→</span></div>
      </a>

      <a class="card" href="https://secure.daboiyoshi.com/" data-external="true" rel="noopener">
        <span class="card-tag">Article</span>
        <h3 class="card-title">HTTP vs HTTPS</h3>
        <p class="card-desc">A short article on what changes when a site upgrades. Coded in XHTML format.</p>
        <div class="card-meta"><span>READ</span><span class="arrow">→</span></div>
      </a>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-head">
      <h2>Featured tools</h2>
      <a class="section-link" href="tools-experiments/">All 22 tools →</a>
    </div>
    <div class="card-grid">
      <a class="card" href="qr-code-generator.html">
        <span class="card-tag">Utility</span>
        <h3 class="card-title">QR Code Generator</h3>
        <p class="card-desc">Generate scannable QR codes for any text or URL — instant, free, in-browser.</p>
        <div class="card-meta"><span>OPEN</span><span class="arrow">→</span></div>
      </a>

      <a class="card" href="zen-timer.html">
        <span class="card-tag">Focus</span>
        <h3 class="card-title">Zen Timer</h3>
        <p class="card-desc">Calm break timer. Set it, breathe, come back when it chimes.</p>
        <div class="card-meta"><span>OPEN</span><span class="arrow">→</span></div>
      </a>

      <a class="card" href="vapordrive.html">
        <span class="card-tag">Aesthetic</span>
        <h3 class="card-title">VaporDrive</h3>
        <p class="card-desc">Synthwave timer — drift through the grid while a session ticks down.</p>
        <div class="card-meta"><span>OPEN</span><span class="arrow">→</span></div>
      </a>

      <a class="card" href="freepassgen.html">
        <span class="card-tag">Security</span>
        <h3 class="card-title">FreePassGen</h3>
        <p class="card-desc">Strong password generator — length, case, symbols, digits, all configurable.</p>
        <div class="card-meta"><span>OPEN</span><span class="arrow">→</span></div>
      </a>

      <a class="card" href="snake-txt-editor.html">
        <span class="card-tag">Editor</span>
        <h3 class="card-title">Snake TXT Editor</h3>
        <p class="card-desc">Lightweight text editor that runs entirely in your browser. Save locally, no signup.</p>
        <div class="card-meta"><span>OPEN</span><span class="arrow">→</span></div>
      </a>

      <a class="card" href="https://docs.daboiyoshi.com/Multi-Convert//multi-convert.html" data-external="true" rel="noopener">
        <span class="card-tag">Files</span>
        <h3 class="card-title">MultiConvert</h3>
        <p class="card-desc">Universal file converter — drop any file, pick a target format, download.</p>
        <div class="card-meta"><span>LAUNCH</span><span class="arrow">→</span></div>
      </a>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="banner">
      Please review our <a href="https://docs.daboiyoshi.com/documents/Terms_Of_Service.pdf" rel="noopener">Terms of Service</a> and <a href="https://docs.daboiyoshi.com/documents/Privacy_Policy.pdf" rel="noopener">Privacy Policy</a>. We don't sell your data — ever.
    </div>
  </div>
</section>
"""

PAGE = {
    "title":       "Snake Arcade — Browser games, tools & experiments by daboiYoshi",
    "description": "Snake Arcade is a free collection of browser games, creative tools, and HTML experiments by daboiYoshi. Play Snake, paint, generate QR codes, run a zen timer — all in your browser, no install required.",
    "og_type":     "website",
    "schema_type": "WebSite",
    "schema_extra": {
        "potentialAction": {
            "@type": "SearchAction",
            "target": "https://www.daboiyoshi.com/?q={search_term_string}",
            "query-input": "required name=search_term_string",
        },
    },
    "content":     CONTENT,
}


def build(render):
    render(PAGE, "index.html")
