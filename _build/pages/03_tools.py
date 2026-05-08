"""Tools & Experiments — hub page plus 22 launcher pages.

Each tool either:
  - links to an external URL (typically docs.daboiyoshi.com), OR
  - is a stub for a tool that should be ported into the new repo later.

The launcher page surfaces a clean intro card AND offers an in-page launch
(lazy iframe) for tools that work well embedded.
"""

# ---- Tool registry (single source of truth) ----
# slug, title, tag, blurb, target_url, embed_ok
TOOLS = [
    {
        "slug": "base64-converter",
        "title": "Base64 Converter",
        "tag":   "Encoding",
        "blurb": "Encode and decode Base64 strings — paste in plain text or Base64 and get the other side.",
        "url":   "https://docs.daboiyoshi.com/Base64-Converter/index.html",
        "embed_ok": True,
    },
    {
        "slug": "multi-convert",
        "title": "Multi Convert",
        "tag":   "Files",
        "blurb": "Universal file converter. Drop in a file, pick a target format, download. Works on most common file types.",
        "url":   "https://docs.daboiyoshi.com/Multi-Convert//multi-convert.html",
        "embed_ok": True,
    },
    {
        "slug": "qr-code-generator",
        "title": "QR Code Generator",
        "tag":   "Utility",
        "blurb": "Turn any text or URL into a scannable QR code in your browser. No upload, nothing leaves the device.",
        "url":   "https://docs.daboiyoshi.com/QR-Code-Generator/index.html",
        "embed_ok": True,
    },
    {
        "slug": "z-dos",
        "title": "Z-DOS",
        "tag":   "OS · Experiment",
        "blurb": "An operating system written in HTML — files, terminal, windows, the whole bit. Boot it in a tab.",
        "url":   "https://docs.daboiyoshi.com/Z-DOS/index.html",
        "embed_ok": True,
    },
    {
        "slug": "snake-media-player",
        "title": "Snake Media Player",
        "tag":   "Media",
        "blurb": "Drop-in media player for video (MP4, MKV, AVI, MOV, WebM) and audio (MP3, FLAC, WAV, OGG). All client-side.",
        "url":   "https://docs.daboiyoshi.com/Snake-Media-Player/index.html",
        "embed_ok": True,
    },
    {
        "slug": "3d-viewer",
        "title": "3D Viewer",
        "tag":   "3D",
        "blurb": "Browser-based 3D model viewer for OBJ / GLTF style files. Pan, rotate, zoom.",
        "url":   "https://docs.daboiyoshi.com/3d-Viewer/index.html",
        "embed_ok": True,
    },
    {
        "slug": "password-generator",
        "title": "Password Generator",
        "tag":   "Security",
        "blurb": "Generate strong passwords with configurable length, case, digits, and symbols.",
        "url":   "https://docs.daboiyoshi.com/Password-Generator/index.html",
        "embed_ok": True,
    },
    {
        "slug": "sa-paint",
        "title": "SA Paint",
        "tag":   "Creative",
        "blurb": "HTML paint app — pencil, brush, eraser, fill, line, rectangles, ellipses, polygons, arrows, spray, and text.",
        "url":   "https://docs.daboiyoshi.com/Snake-Paint/",
        "embed_ok": True,
    },
    {
        "slug": "neon-dash",
        "title": "Neon Dash",
        "tag":   "Game",
        "blurb": "Fast-paced neon arcade dash. Reflex-driven, mobile-friendly.",
        "url":   "https://docs.daboiyoshi.com/Neon-Dash/index.html",
        "embed_ok": True,
    },
    {
        "slug": "4d-tessellation",
        "title": "4D Tessellation",
        "tag":   "Math · Visual",
        "blurb": "Visualize 4D geometric tessellations projected into 3D space. Twist the projection, watch shapes reform.",
        "url":   "https://docs.daboiyoshi.com/4d-Tessellation/index.html",
        "embed_ok": True,
    },
    {
        "slug": "compliment-generator",
        "title": "Compliment Generator",
        "tag":   "Fun",
        "blurb": "Click for a kind word. Click again. As many as you need.",
        "url":   "https://docs.daboiyoshi.com/Compliment-Generator/index.html",
        "embed_ok": True,
    },
    {
        "slug": "inflation",
        "title": "Inflation",
        "tag":   "Calculator",
        "blurb": "Calculate inflation-adjusted values across years. Useful for cost comparisons and planning.",
        "url":   "https://docs.daboiyoshi.com/Inflation/index.html",
        "embed_ok": True,
    },
    {
        "slug": "music-player",
        "title": "Music Player",
        "tag":   "Media",
        "blurb": "Lightweight in-browser music player. Drop in audio files and listen — no uploads.",
        "url":   "https://docs.daboiyoshi.com/Music-Player/index.html",
        "embed_ok": True,
    },
    {
        "slug": "3d-shading",
        "title": "3D Shading",
        "tag":   "3D · Visual",
        "blurb": "Real-time shading and lighting playground for 3D primitives. Experiment with materials and light angles.",
        "url":   "https://docs.daboiyoshi.com/3d-Shading/index.html",
        "embed_ok": True,
    },
    {
        "slug": "neon-skyrunner",
        "title": "Neon Skyrunner",
        "tag":   "Game",
        "blurb": "Dodge red obstacles across three lanes. Collect green gems. Survive as long as you can. ← → to switch lanes, Space / ↑ to jump.",
        "url":   "https://docs.daboiyoshi.com/Neon-skyrunner/",
        "embed_ok": True,
    },
    {
        "slug": "3d-world-generator",
        "title": "3D World Generator",
        "tag":   "3D · Tool",
        "blurb": "Procedurally generate small 3D worlds you can wander through, all in the browser.",
        "url":   "https://docs.daboiyoshi.com/3d-World-Generator/index.html",
        "embed_ok": True,
    },
    {
        "slug": "snake-txt-editor",
        "title": "Snake TXT Editor",
        "tag":   "Editor",
        "blurb": "Lightweight text editor that runs entirely in your browser. Save locally, no signup.",
        "url":   "https://docs.daboiyoshi.com/Snake-TXT-Editor/index.html",
        "embed_ok": True,
    },
    {
        "slug": "json-insight-hub",
        "title": "JSON Insight Hub",
        "tag":   "Developer",
        "blurb": "Inspect, format, and explore JSON. Pretty-print, collapse, search — for debugging and data work.",
        "url":   "https://docs.daboiyoshi.com/JSON-Insight-Hub/index.html",
        "embed_ok": True,
    },
    {
        "slug": "zen-timer",
        "title": "Zen Timer",
        "tag":   "Focus",
        "blurb": "Calm break timer. Set it, breathe, come back when it chimes.",
        "url":   "https://docs.daboiyoshi.com/Zen-Timer/index.html",
        "embed_ok": True,
    },
    {
        "slug": "vapordrive",
        "title": "VaporDrive",
        "tag":   "Aesthetic",
        "blurb": "Synthwave timer — drift through the grid while a session ticks down.",
        "url":   "https://docs.daboiyoshi.com/VaporDrive/index.html",
        "embed_ok": True,
    },
    {
        "slug": "screen-saver",
        "title": "Screen Saver",
        "tag":   "Aesthetic",
        "blurb": "DVD-bouncing-logo style screen saver, Snake Arcade edition. Fullscreen-friendly.",
        "url":   "https://docs.daboiyoshi.com/Dvd-bouncing-logo-snake-arcade/index.html",
        "embed_ok": True,
    },
    {
        "slug": "snake-paint",
        "title": "Snake Paint (alt)",
        "tag":   "Creative",
        "blurb": "Same paint app as SA Paint, listed under its newer name. Pencil, brush, eraser, fill, shapes, text, spray.",
        "url":   "https://docs.daboiyoshi.com/Snake-Paint/",
        "embed_ok": True,
    },
]


# ---- Hub page ----
def hub_content():
    # Cards link to INTERNAL launcher pages, so no data-external flag.
    cards = []
    for t in TOOLS:
        cards.append(f"""
      <a class="card" href="{t['slug']}.html">
        <span class="card-tag">{t['tag']}</span>
        <h3 class="card-title">{t['title']}</h3>
        <p class="card-desc">{t['blurb']}</p>
        <div class="card-meta"><span>OPEN</span><span class="arrow">→</span></div>
      </a>""")

    grid = "\n".join(cards)
    return f"""
<div class="container">
  <div class="page-head">
    <nav class="crumbs" aria-label="Breadcrumb">
      <a href="../">Home</a><span>/</span><span aria-current="page">Tools &amp; Experiments</span>
    </nav>
    <h1>Tools &amp; Experiments</h1>
    <p class="lede">Every browser-only utility, toy, and experiment we've built. Click any card to open its launcher.</p>
  </div>

  <section style="padding-top:0">
    <div class="card-grid">{grid}
    </div>
  </section>
</div>
"""


# ---- Per-tool launcher page ----
def tool_content(t):
    return f"""
<div class="container">
  <div class="page-head">
    <nav class="crumbs" aria-label="Breadcrumb">
      <a href="../">Home</a><span>/</span><a href="./">Tools</a><span>/</span><span aria-current="page">{t['title']}</span>
    </nav>
    <h1>{t['title']}</h1>
    <p class="lede">{t['blurb']}</p>
  </div>

  <section style="padding-top:0">
    <div class="launcher">
      <div>
        <div class="launcher-meta">
          <span><strong>Type:</strong> {t['tag']}</span>
          <span><strong>Hosted on:</strong> docs.daboiyoshi.com (CDN)</span>
          <span><strong>Cost:</strong> Free</span>
        </div>
      </div>
      <div class="hero-cta">
        <a class="btn btn-primary" href="{t['url']}" rel="noopener">▶ Open in new tab</a>
        <button class="btn" data-launch-inline="#embed-mount" data-iframe-src="{t['url']}">Launch in page</button>
        <a class="btn btn-ghost" href="./">All tools</a>
      </div>
      <div id="embed-mount" aria-live="polite"></div>
    </div>
  </section>

  <section>
    <div class="prose">
      <h2>About this tool</h2>
      <p>{t['blurb']} It runs entirely in the browser — nothing is uploaded to a server. Open it in a new tab for the cleanest experience, or click <em>Launch in page</em> to embed it inline.</p>

      <h2>Privacy</h2>
      <p>Snake Arcade tools don't collect personal data. Anything you paste, draw, type, or generate stays on your device unless you explicitly download or share it. See our <a href="https://docs.daboiyoshi.com/documents/Privacy_Policy.pdf" rel="noopener">Privacy Policy</a> for the full statement.</p>
    </div>
  </section>
</div>
"""


def build(render):
    # Hub
    render({
        "title":       "Tools & Experiments — Snake Arcade",
        "description": "Browse every Snake Arcade browser tool: paint, media player, QR generator, password tools, 3D viewers, calculators, focus timers, and more. All run in your browser — free, no install.",
        "og_type":     "website",
        "schema_type": "CollectionPage",
        "content":     hub_content(),
    }, "tools-experiments/index.html")

    # Each tool
    for t in TOOLS:
        render({
            "title":       f"{t['title']} — Snake Arcade",
            "description": t["blurb"],
            "og_type":     "website",
            "schema_type": "WebApplication",
            "schema_category": "UtilityApplication",
            "content":     tool_content(t),
        }, f"tools-experiments/{t['slug']}.html")
