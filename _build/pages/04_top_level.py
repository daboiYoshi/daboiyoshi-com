"""Top-level standalone pages.
These were direct nav items in the old Google Sites structure, separate
from the /tools-experiments/ catalog. Several point to subdomain tools.
"""

PAGES = [
    {
        "slug": "qr-code-generator",
        "title": "QR Code Generator",
        "tag": "Utility",
        "blurb": "Turn any text or URL into a scannable QR code. Free, instant, in-browser — nothing leaves your device.",
        "url": "https://docs.daboiyoshi.com/QR-Code-Generator/index.html",
    },
    {
        "slug": "zen-timer",
        "title": "Zen Timer",
        "tag": "Focus",
        "blurb": "Calm break timer. Set it, breathe, come back when it chimes.",
        "url": "https://docs.daboiyoshi.com/Zen-Timer/index.html",
    },
    {
        "slug": "vapordrive",
        "title": "VaporDrive",
        "tag": "Aesthetic Timer",
        "blurb": "Synthwave drift timer — sit back while a neon grid runs your session out.",
        "url": "https://docs.daboiyoshi.com/VaporDrive/index.html",
    },
    {
        "slug": "freepassgen",
        "title": "FreePassGen",
        "tag": "Security",
        "blurb": "Strong password generator with configurable length, character classes, and symbol sets. Generated in your browser.",
        "url": "https://docs.daboiyoshi.com/Password-Generator/index.html",
    },
    {
        "slug": "snake-txt-editor",
        "title": "Snake TXT Editor",
        "tag": "Editor",
        "blurb": "Lightweight in-browser text editor. Save locally, no signup.",
        "url": "https://docs.daboiyoshi.com/Snake-TXT-Editor/index.html",
    },
    {
        "slug": "dictionary",
        "title": "Dictionary",
        "tag": "Reference",
        "blurb": "Snake Definer — pocket dictionary that defines any English word. Mobile-optimized.",
        "url": "https://define.daboiyoshi.com",
    },
    {
        "slug": "nimbus-drive",
        "title": "Nimbus Drive",
        "tag": "Storage",
        "blurb": "Browser-based file area for working with files locally — no cloud account needed.",
        "url": "https://docs.daboiyoshi.com/Nimbus-Drive/index.html",
    },
    {
        "slug": "snake-ai",
        "title": "Snake AI",
        "tag": "AI",
        "blurb": "An AI-powered helper assembled from the Snake Arcade toolkit. Ask, get answers.",
        "url": "https://docs.daboiyoshi.com/Snake-AI/index.html",
    },
]


def page_content(p):
    return f"""
<div class="container">
  <div class="page-head">
    <nav class="crumbs" aria-label="Breadcrumb">
      <a href="./">Home</a><span>/</span><span aria-current="page">{p['title']}</span>
    </nav>
    <h1>{p['title']}</h1>
    <p class="lede">{p['blurb']}</p>
  </div>

  <section style="padding-top:0">
    <div class="launcher">
      <div class="launcher-meta">
        <span><strong>Type:</strong> {p['tag']}</span>
        <span><strong>Cost:</strong> Free</span>
        <span><strong>Account:</strong> None required</span>
      </div>
      <div class="hero-cta">
        <a class="btn btn-primary" href="{p['url']}" rel="noopener">▶ Open in new tab</a>
        <button class="btn" data-launch-inline="#embed-mount" data-iframe-src="{p['url']}">Launch in page</button>
        <a class="btn btn-ghost" href="tools-experiments/">All tools</a>
      </div>
      <div id="embed-mount" aria-live="polite"></div>
    </div>
  </section>

  <section>
    <div class="prose">
      <h2>About</h2>
      <p>{p['blurb']} Runs entirely in your browser — nothing is uploaded.</p>
      <h2>Need help?</h2>
      <p>If something doesn't work, drop a note to <a href="mailto:info@daboiyoshi.com">info@daboiyoshi.com</a>. Include your browser and OS so we can repro.</p>
    </div>
  </section>
</div>
"""


# Snake AI extra subpage
SNAKE_AI_EXTRA = {
    "title":       "Snake AI · Extra — Snake Arcade",
    "description": "Additional notes, settings, and experiments around the Snake AI helper.",
    "schema_type": "WebPage",
    "content": """
<div class="container">
  <div class="page-head">
    <nav class="crumbs" aria-label="Breadcrumb">
      <a href="../">Home</a><span>/</span><a href="../snake-ai.html">Snake AI</a><span>/</span><span aria-current="page">Extra</span>
    </nav>
    <h1>Snake AI · Extra</h1>
    <p class="lede">Bonus material and experiments around Snake AI.</p>
  </div>

  <div class="prose">
    <p>This page collects extra notes, in-progress experiments, and behaviors related to the Snake AI helper. Content here is exploratory and may change frequently.</p>

    <h2>Want to suggest something?</h2>
    <p>Email <a href="mailto:info@daboiyoshi.com">info@daboiyoshi.com</a> or open an issue on <a href="https://github.com/daboiYoshi" rel="noopener">GitHub</a>.</p>

    <h2>Back to Snake AI</h2>
    <p><a href="../snake-ai.html">Return to the main Snake AI page</a>.</p>
  </div>
</div>
""",
}


def build(render):
    for p in PAGES:
        render({
            "title":       f"{p['title']} — Snake Arcade",
            "description": p["blurb"],
            "og_type":     "website",
            "schema_type": "WebApplication",
            "schema_category": "UtilityApplication",
            "content":     page_content(p),
        }, f"{p['slug']}.html")

    render(SNAKE_AI_EXTRA, "snake-ai/extra.html")
