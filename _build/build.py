#!/usr/bin/env python3
"""
Snake Arcade — static site builder
Renders pages (Python dicts of metadata + HTML) into final HTML files
using a single shell template. Output is plain HTML — works on any
static host (GitHub Pages, Netlify, S3, etc.) with no build step.
"""

import json
import os
import re
import sys
from pathlib import Path

ROOT          = Path(__file__).resolve().parent
TEMPLATE_PATH = ROOT / "templates" / "shell.html"
PAGES_DIR     = ROOT / "pages"
OUTPUT_DIR    = Path("/home/claude/daboiyoshi-site")
SITE_BASE     = "https://www.daboiyoshi.com"

SHELL = TEMPLATE_PATH.read_text(encoding="utf-8")


def relative_root(out_path: Path) -> str:
    """Return '../'-style path from output file back to site root."""
    rel = out_path.relative_to(OUTPUT_DIR)
    depth = len(rel.parts) - 1
    return "../" * depth if depth else "./"


def jsonld_for(page: dict, canonical: str) -> str:
    base = {
        "@context": "https://schema.org",
        "@type":    page.get("schema_type", "WebPage"),
        "name":     page["title"],
        "url":      f"{SITE_BASE}{canonical}",
        "description": page["description"],
        "publisher": {
            "@type": "Organization",
            "name":  "Snake Arcade",
            "url":   SITE_BASE,
        },
    }
    if page.get("schema_type") == "WebApplication":
        base.update({
            "applicationCategory": page.get("schema_category", "UtilityApplication"),
            "operatingSystem":     "Any (web browser)",
            "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
        })
    base.update(page.get("schema_extra", {}))
    return json.dumps(base, separators=(",", ":"))


def render(page: dict, out_subpath: str):
    out_path = OUTPUT_DIR / out_subpath
    out_path.parent.mkdir(parents=True, exist_ok=True)

    canonical = "/" + out_subpath
    canonical = canonical.replace("/index.html", "/")
    root      = relative_root(out_path)

    rendered = SHELL
    rendered = rendered.replace("{title}",       page["title"])
    rendered = rendered.replace("{description}", page["description"])
    rendered = rendered.replace("{canonical}",   canonical)
    rendered = rendered.replace("{og_type}",     page.get("og_type", "website"))
    rendered = rendered.replace("{root}",        root)
    rendered = rendered.replace("{jsonld}",      jsonld_for(page, canonical))
    rendered = rendered.replace("{extra_head}",  page.get("extra_head", ""))
    rendered = rendered.replace("{content}",     page["content"])

    out_path.write_text(rendered, encoding="utf-8")
    print(f"  ✓ {out_subpath}")


def main():
    sys.path.insert(0, str(PAGES_DIR))
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Discover all page modules in /pages and call their build(render) function
    page_files = sorted([p for p in PAGES_DIR.glob("*.py") if not p.name.startswith("_")])
    print(f"Building {len(page_files)} page module(s) ...")
    for pf in page_files:
        mod = __import__(pf.stem)
        if hasattr(mod, "build"):
            mod.build(render)

    print(f"\nDone → {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
