# SOP: Migrating www.daboiyoshi.com from Google Sites to GitHub Pages

**Version:** 1.0
**Audience:** Site administrator (daboiYoshi)
**Estimated time:** 45–90 min hands-on, plus DNS propagation wait
**Required downtime:** 0

---

## 1. Purpose & scope

Migrate **www.daboiyoshi.com** from Google Sites to a static GitHub Pages build.

**In scope:** the www subdomain only.
**Out of scope:** docs., sar., define., snakenet., void-breach., secure., about. — these stay on their existing hosts. The new site links out to them.

---

## 2. Pre-flight checklist

Complete every item *before* touching DNS.

- [ ] GitHub account ready (will be the public repo URL)
- [ ] Admin access to the daboiyoshi.com DNS zone (registrar login)
- [ ] Owner access to the existing Google Sites publication
- [ ] Git installed locally
- [ ] **Backup the Google Sites build:** open it in the editor → File → Make a copy → name it `Snake Arcade — pre-migration backup`
- [ ] Screenshot or export the current DNS records for daboiyoshi.com (you need to know what to revert to)
- [ ] Verify the deliverable archive contains: `index.html` at root, `CNAME`, `.nojekyll`, `sitemap.xml`, `robots.txt`, `manifest.webmanifest`, `/assets/`, and 44 HTML pages

> ⚠️ **Critical:** Do not change DNS records until the GitHub Pages site has been verified using a hosts-file override (Section 4). DNS propagation can take 24–48 hours; reverting a misconfigured cutover is slower than testing first.

---

## 3. Create the repo and push the site

### 3.1 Create the repository

1. Sign in to github.com → **+** → **New repository**.
2. Name it `daboiyoshi-com` (any name works — Pages routes by the CNAME file, not the repo name).
3. Visibility: **Public** (required for free Pages).
4. **Do not** initialize with README, .gitignore, or license — you're pushing existing files.
5. Click **Create repository** and copy the clone URL.

### 3.2 Push the files

Open a terminal in the folder that contains `index.html`, `CNAME`, `/assets/`, etc.:

```bash
git init
git add .
git commit -m "Initial commit: Snake Arcade static site"
git branch -M main
git remote add origin https://github.com/<username>/<repo>.git
git push -u origin main
```

Replace `<username>` and `<repo>` with your values.

### 3.3 Enable GitHub Pages

1. On the repo page → **Settings** → **Pages** (left sidebar).
2. Source: **Deploy from a branch**.
3. Branch: **main** / **(root)**. Click **Save**.
4. After 1–2 min, GitHub shows: *"Your site is live at https://<username>.github.io/<repo>/"*. Open it.
5. Verify the dark theme renders, navigation works, mobile menu opens, the launcher button on a tool page loads its iframe, and the 404 page works (visit a fake URL).

> ✅ **Checkpoint:** the site is now live at the github.io URL. The custom domain isn't active yet — that's the next section.

---

## 4. Pre-test the custom domain via /etc/hosts

This proves the site behaves identically under the real hostname *before* you touch DNS. Skipping this is the most common cause of bad cutovers.

### macOS / Linux

```bash
# Find GitHub Pages's IP for your site
dig +short <username>.github.io

# Edit /etc/hosts (sudo)
sudo nano /etc/hosts

# Add this line (use one of the IPs returned above):
185.199.108.153   www.daboiyoshi.com
```

### Windows

1. Run **Notepad as Administrator**.
2. Open `C:\Windows\System32\drivers\etc\hosts` (set "All files" filter).
3. Add the same line as above. Save.

In an incognito window visit `https://www.daboiyoshi.com`. The site should load. (Expect a TLS warning until step 5 issues a real cert — that's normal during the test.)

When done, **remove the hosts entry**. It was only for verification.

---

## 5. Bind the custom domain in GitHub Pages

1. **Settings** → **Pages** → **Custom domain**.
2. Enter `www.daboiyoshi.com` and click **Save**.
3. The repo's existing `CNAME` file satisfies GitHub's verification — no action needed.
4. Tick **Enforce HTTPS** once it becomes available (greyed out until DNS is configured and the cert is issued — usually 5–60 min after Section 6).

---

## 6. Configure DNS records

Sign into your registrar and update records. Exact UI varies by registrar; record types are universal.

| Record type | Host / Name | Value                          |
|-------------|-------------|--------------------------------|
| CNAME       | www         | `<username>.github.io`         |
| A           | @           | `185.199.108.153`              |
| A           | @           | `185.199.109.153`              |
| A           | @           | `185.199.110.153`              |
| A           | @           | `185.199.111.153`              |
| AAAA        | @           | `2606:50c0:8000::153`          |
| AAAA        | @           | `2606:50c0:8001::153`          |
| AAAA        | @           | `2606:50c0:8002::153`          |
| AAAA        | @           | `2606:50c0:8003::153`          |

> ⚠️ **Important:** If you only need www (and want apex daboiyoshi.com to redirect or stay where it is), skip the A and AAAA records and only update the CNAME for www. The apex records above are only needed if you also want apex (no www) to serve the new site.

**Delete any old records pointing to Google Sites** — typically a CNAME on www → `ghs.googlehosted.com`. Save the zone.

DNS propagation: typically 5–60 min for a CNAME, up to 48 hours globally.

---

## 7. Wait for DNS + TLS, then enforce HTTPS

1. Use **whatsmydns.net** or **dnschecker.org** to look up `www.daboiyoshi.com` (CNAME). Wait until the majority of locations show `<username>.github.io`.
2. Return to **Settings → Pages**. The DNS check should turn green.
3. Tick **Enforce HTTPS**. GitHub issues a Let's Encrypt cert within minutes.

---

## 8. Disable Google Sites publication

> 🔴 **Do not skip.** Leaving Google Sites published means the project still occupies your domain in Google's records. If DNS is briefly reverted, your old site reappears.

1. Open the Google Sites editor for www.daboiyoshi.com.
2. Click the publication settings (gear or "Published" indicator).
3. Click **Unpublish** (or remove the custom-domain binding inside Google Sites).
4. Confirm. The Google Sites copy is preserved in your Drive — you haven't deleted any content, only stopped serving it.

---

## 9. Submit the new sitemap

### Google Search Console

1. Visit **search.google.com/search-console**.
2. Add `daboiyoshi.com` as a property if not already added.
3. Verify ownership (DNS TXT or HTML file — easiest is the HTML file: drop it in the repo root and push).
4. Left nav → **Sitemaps** → submit `https://www.daboiyoshi.com/sitemap.xml`.

### Bing Webmaster Tools

1. Visit **bing.com/webmasters**.
2. Add the property and verify (easiest: **Import from Google Search Console**).
3. Submit the same sitemap URL.

---

## 10. Post-cutover validation

Run every check. Any FAIL triggers the rollback in Section 11.

| Check                | How to validate                                                            | Expected                                       |
|----------------------|----------------------------------------------------------------------------|------------------------------------------------|
| HTTPS works          | Open `https://www.daboiyoshi.com` in incognito                             | Padlock visible, no warning                    |
| HTTP redirects       | Open `http://www.daboiyoshi.com`                                           | Redirects to https                             |
| Mobile rendering     | Open in iOS Safari and Android Chrome                                      | Hamburger menu, no horizontal scroll           |
| Tool launcher        | Open `/qr-code-generator.html` → click "Launch in page"                    | Iframe loads the docs subdomain tool           |
| External links       | Click the SnakeNet card on the home page                                   | Opens snakenet.daboiyoshi.com in a new tab     |
| Sitemap reachable    | Open `/sitemap.xml`                                                        | Valid XML, ~45 URLs                            |
| Robots reachable     | Open `/robots.txt`                                                         | Two-line file, references sitemap              |
| 404 page             | Open `/this-doesnt-exist.html`                                             | Custom 404 with neon design renders            |
| Social preview       | Paste home URL into linkedin.com/post-inspector                            | OG title + description + cover image render   |
| Lighthouse score     | Chrome DevTools → Lighthouse on home page                                  | Performance ≥ 90, A11y ≥ 90, SEO ≥ 95          |
| Search Console index | Wait 24–72 hours, check Coverage report                                    | Pages move into "Indexed" status               |

---

## 11. Rollback (if needed)

If validation fails and can't be fixed forward in your tolerance window:

1. Re-publish the Google Sites backup (Section 2) to www.daboiyoshi.com from inside Google Sites.
2. In your DNS zone, replace the GitHub Pages records with the original Google Sites CNAME (`www → ghs.googlehosted.com`).
3. Wait 5–30 min. Verify in incognito.
4. In the GitHub repo, optionally remove the custom domain in **Settings → Pages** so GitHub stops trying to issue a cert.
5. The new site code is still in the repo — fix it forward and re-attempt the cutover when ready.

---

## 12. Ongoing maintenance

### Adding or editing a page

**Path A — quick edit:** open the `.html` file in the GitHub web UI (pencil icon), edit, commit. Site rebuilds in ~30 seconds.

**Path B — bulk rebuild via the Python script:**

```bash
git clone <repo>
# edit files in /_build/pages/  (or add a new tool to TOOLS in 03_tools.py)
cd _build && python3 build.py
git add . && git commit -m "Update pages" && git push
```

### Adding a new tool

1. In `_build/pages/03_tools.py`, append a new dict to `TOOLS` with `slug`, `title`, `tag`, `blurb`, `url`.
2. Optionally add it to homepage Featured Tools in `01_index.py`.
3. Add a new `<url>` entry to `sitemap.xml`.
4. `python3 build.py`, commit, push.

### Replacing the OG cover image

1. Edit `/assets/images/og-cover.svg`.
2. Re-export to PNG at exactly **1200×630**.
3. Save as `/assets/images/og-cover.png`.
4. Commit and push. The cache may serve the old image to social platforms for up to 7 days — use linkedin.com/post-inspector to force a recrawl.

---

## 13. Reference: GitHub Pages IPs

Verify still current at the time of cutover (GitHub publishes these in their docs):

```
185.199.108.153
185.199.109.153
185.199.110.153
185.199.111.153

2606:50c0:8000::153
2606:50c0:8001::153
2606:50c0:8002::153
2606:50c0:8003::153
```

---

## 14. Page inventory

| Path                              | Title                          | Type     |
|-----------------------------------|--------------------------------|----------|
| `/`                               | Snake Arcade landing           | Hub      |
| `/about/`                         | About index                    | Section  |
| `/about/snake-arcade.html`        | About Snake Arcade             | Article  |
| `/about/daboiyoshi.html`          | About daboiYoshi               | Article  |
| `/about/copyright.html`           | Copyright                      | Article  |
| `/about/honorable-mentions.html`  | Honorable Mentions             | Article  |
| `/tools-experiments/`             | Tools & Experiments hub        | Catalog  |
| `/tools-experiments/*.html` (×22) | Individual tool launchers      | Launcher |
| `/qr-code-generator.html`         | QR Code Generator              | Launcher |
| `/zen-timer.html`                 | Zen Timer                      | Launcher |
| `/vapordrive.html`                | VaporDrive                     | Launcher |
| `/freepassgen.html`               | FreePassGen                    | Launcher |
| `/snake-txt-editor.html`          | Snake TXT Editor               | Launcher |
| `/dictionary.html`                | Dictionary (Snake Definer)     | Launcher |
| `/nimbus-drive.html`              | Nimbus Drive                   | Launcher |
| `/snake-ai.html`                  | Snake AI                       | Launcher |
| `/snake-ai/extra.html`            | Snake AI · Extra               | Article  |
| `/home/`                          | Home (legacy parity)           | Hub      |
| `/home/downloads.html`            | Downloads                      | Catalog  |
| `/home/1-0.html`                  | Snake Arcade 1.0               | Launcher |
| `/home/html-previewer.html`       | HTML Previewer                 | Launcher |
| `/home/ende-crypter.html`         | En/De-crypter                  | Launcher |
| `/404.html`                       | Custom 404                     | System   |
| `/sitemap.xml`                    | Sitemap                        | System   |
| `/robots.txt`                     | Robots                         | System   |
| `/manifest.webmanifest`           | PWA manifest                   | System   |

**Total: 44 HTML pages + 4 system files.**
