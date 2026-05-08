"""About section — main page + child pages."""

ABOUT_INDEX = {
    "title":       "About — Snake Arcade",
    "description": "About Snake Arcade and daboiYoshi — the story behind the project, why it exists, and where it came from.",
    "og_type":     "website",
    "schema_type": "AboutPage",
    "content": """
<div class="container">
  <div class="page-head">
    <nav class="crumbs" aria-label="Breadcrumb">
      <a href="../">Home</a><span>/</span><span aria-current="page">About</span>
    </nav>
    <h1>About Snake Arcade</h1>
    <p class="lede">A long-running personal project by daboiYoshi: a place to ship browser games, HTML experiments, and useful little tools — without paywalls, accounts, or surveillance.</p>
  </div>

  <div class="prose">
    <p>Snake Arcade started with one HTML snake game and grew, project by project, into a small library of browser-only games and tools. Everything here runs in the browser. Nothing requires an install. We don't sell your data, and we don't run ads.</p>
    <p>For more, contact our administration at <a href="mailto:info@daboiyoshi.com">info@daboiyoshi.com</a>.</p>

    <h2>Sub-pages</h2>
    <ul>
      <li><a href="snake-arcade.html">About Snake Arcade</a> — the platform itself</li>
      <li><a href="daboiyoshi.html">About daboiYoshi</a> — the developer</li>
      <li><a href="copyright.html">Copyright</a> — licensing notes</li>
      <li><a href="honorable-mentions.html">Honorable Mentions</a> — credits and inspirations</li>
    </ul>
  </div>
</div>
""",
}

SNAKE_ARCADE = {
    "title":       "About Snake Arcade — the platform",
    "description": "Why Snake Arcade exists, how it started, and what we build here. A look at the platform behind the games.",
    "og_type":     "article",
    "schema_type": "AboutPage",
    "content": """
<div class="container">
  <div class="page-head">
    <nav class="crumbs" aria-label="Breadcrumb">
      <a href="../">Home</a><span>/</span><a href="./">About</a><span>/</span><span aria-current="page">Snake Arcade</span>
    </nav>
    <h1>About Snake Arcade</h1>
    <p class="lede">A platform for browser-only games and HTML experiments.</p>
  </div>

  <div class="prose">
    <p>Snake Arcade started because daboiYoshi coded a snake game in HTML and built a website around it. Then more changes, more projects, more tools. Now every game, project, or tool here is published under the Snake Arcade banner.</p>

    <h2>Why the focus on HTML?</h2>
    <p>Learning Unity and the deeper game-dev stack is a long road. HTML is much easier to pick up, immediately runs anywhere, and produces things measured in kilobytes — not gigabytes. That trade-off is what makes shipping fast and keeps everything playable in seconds, not after a download.</p>

    <h2>How it works</h2>
    <p>Snake Arcade is a static collection of HTML/CSS/JS projects. Most heavy assets and individual games live on our CDN at <a href="https://docs.daboiyoshi.com" rel="noopener">docs.daboiyoshi.com</a>. The main site links them together and surfaces what's new.</p>

    <blockquote>
      Of course we are not charging you to use our games and tools. We are not taking or selling your personal information.
    </blockquote>

    <h2>The team</h2>
    <p>When the site says "we", "us", or "our", that means daboiYoshi together with the administration / dev team that supports the project.</p>
  </div>
</div>
""",
}

DABOIYOSHI = {
    "title":       "About daboiYoshi — the developer",
    "description": "About daboiYoshi, creator of Snake Arcade. Coding habits, the YouTube channel, and the project's roots.",
    "og_type":     "profile",
    "schema_type": "Person",
    "schema_extra": {
        "givenName": "daboiYoshi",
        "url":       "https://www.daboiyoshi.com/about/daboiyoshi.html",
        "sameAs": [
            "https://www.youtube.com/@daboiYoshi_tfsaviation",
            "https://github.com/daboiYoshi",
        ],
    },
    "content": """
<div class="container">
  <div class="page-head">
    <nav class="crumbs" aria-label="Breadcrumb">
      <a href="../">Home</a><span>/</span><a href="./">About</a><span>/</span><span aria-current="page">daboiYoshi</span>
    </nav>
    <h1>daboiYoshi</h1>
    <p class="lede">Solo developer. Snake Arcade founder. YouTube channel: <a href="https://www.youtube.com/@daboiYoshi_tfsaviation" rel="noopener">@daboiYoshi_tfsaviation</a>.</p>
  </div>

  <div class="prose">
    <p>I'm daboiYoshi. I run a YouTube channel — link is in the footer or in the About menu. I've been wanting to make games for a long time, but learning Unity and the heavier coding stacks is hard. HTML is much easier to learn and ship, and it lets me put things online instantly without bloated downloads.</p>

    <h2>Why this project?</h2>
    <p>Coding is fun. You get to learn new things and build cool things and put them somewhere people can actually use them. After a while of making HTML games, projects, and tools, I just decided to give the creator of every one of them the same name: Snake Arcade. That's basically what this whole site is — Snake Arcade HTML projects.</p>

    <h2>What's been shipped</h2>
    <p>As of January 2026, this site includes an HTML-based operating system, a snake game, and a long list of HTML projects ranging from creative tools to small games. The list keeps growing.</p>

    <h2>A note on Blockade</h2>
    <p>50 years ago, in 1976, Gremlin released "Blockade" — the original "snake" game, where two players each control a continuously moving arrow that leaves a solid trail. The goal isn't growth or score; it's spatial denial. Force your opponent into a wall or a trail before they force you. The "eat food to grow" version came later, with games like Bigfoot Bonkers and eventually Nibbler in 1982. There's a Blockade clone on this site at <a href="https://docs.daboiyoshi.com/game/classic-games/blockade.html" rel="noopener">docs.daboiyoshi.com/game/classic-games/blockade.html</a>.</p>
  </div>
</div>
""",
}

COPYRIGHT = {
    "title":       "Copyright — Snake Arcade",
    "description": "Copyright information for Snake Arcade and daboiYoshi.com — what's covered and how to credit.",
    "schema_type": "AboutPage",
    "content": """
<div class="container">
  <div class="page-head">
    <nav class="crumbs" aria-label="Breadcrumb">
      <a href="../">Home</a><span>/</span><a href="./">About</a><span>/</span><span aria-current="page">Copyright</span>
    </nav>
    <h1>Copyright</h1>
    <p class="lede">Copyright © daboiYoshi · Snake Arcade.</p>
  </div>

  <div class="prose">
    <p>All games, tools, art, code, and written content on Snake Arcade and daboiyoshi.com are the work of daboiYoshi and the Snake Arcade dev team unless otherwise credited.</p>

    <h2>Use</h2>
    <p>You can play, share, and link to anything on this site. Embedding individual tools in your own page is fine if you keep the original credit visible.</p>

    <h2>Re-publishing</h2>
    <p>Don't republish complete projects under a different name without asking first. Forks of open-source projects on our <a href="https://github.com/daboiYoshi" rel="noopener">GitHub</a> follow the license attached to that specific repository.</p>

    <h2>Third-party assets</h2>
    <p>Where we use third-party libraries, fonts, or APIs, those keep their original licenses. See <a href="honorable-mentions.html">Honorable Mentions</a> for credits and links.</p>

    <h2>Reporting an issue</h2>
    <p>If you believe something on this site infringes a copyright, email <a href="mailto:info@daboiyoshi.com">info@daboiyoshi.com</a> with details and we'll look into it.</p>
  </div>
</div>
""",
}

HONORABLE_MENTIONS = {
    "title":       "Honorable Mentions — Snake Arcade",
    "description": "Credits and inspirations: APIs, dictionaries, libraries, and projects that influenced Snake Arcade.",
    "schema_type": "AboutPage",
    "content": """
<div class="container">
  <div class="page-head">
    <nav class="crumbs" aria-label="Breadcrumb">
      <a href="../">Home</a><span>/</span><a href="./">About</a><span>/</span><span aria-current="page">Honorable Mentions</span>
    </nav>
    <h1>Honorable Mentions</h1>
    <p class="lede">A short list of the people, projects, and APIs that helped shape Snake Arcade.</p>
  </div>

  <div class="prose">
    <h2>APIs &amp; dictionaries</h2>
    <ul>
      <li><a href="https://www.merriam-webster.com/" rel="noopener">Merriam-Webster</a> — reference dictionary used while building Snake Definer.</li>
      <li><a href="https://www.dictionaryapi.dev" rel="noopener">Free Dictionary API</a> — powers the <a href="https://define.daboiyoshi.com" rel="noopener">Snake Definer</a> lookups.</li>
      <li><a href="https://letsencrypt.org" rel="noopener">Let's Encrypt</a> — free TLS certificates that keep the site on HTTPS.</li>
    </ul>

    <h2>Inspirations</h2>
    <ul>
      <li><strong>Blockade (Gremlin, 1976)</strong> — the original "snake" arcade game that inspired everything that came after, including this project's name.</li>
      <li><strong>Nibbler (1982)</strong> — the version that introduced the now-classic "eat food to grow" mechanic.</li>
    </ul>

    <h2>Tooling</h2>
    <ul>
      <li>The browsers, editors, and operating systems that made it possible to build everything here in plain HTML, CSS, and JavaScript.</li>
    </ul>

    <p>If you contributed something we should credit here, email <a href="mailto:info@daboiyoshi.com">info@daboiyoshi.com</a>.</p>
  </div>
</div>
""",
}


def build(render):
    render(ABOUT_INDEX,         "about/index.html")
    render(SNAKE_ARCADE,         "about/snake-arcade.html")
    render(DABOIYOSHI,           "about/daboiyoshi.html")
    render(COPYRIGHT,            "about/copyright.html")
    render(HONORABLE_MENTIONS,   "about/honorable-mentions.html")
