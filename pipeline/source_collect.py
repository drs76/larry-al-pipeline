#!/usr/bin/env python3
"""
source_collect — deterministic half of the source→AL-knowledge pipeline. No model.

Handles two source kinds behind one interface: YouTube (caption track) and web
(RSS/Atom feed or a single article). A feed is the exact analogue of a channel
listing, an article the analogue of a transcript, so everything downstream —
triage, distillation, merging — is source-agnostic.

Three jobs, all re-runnable (idempotent — an already-archived video is skipped, so
you can point it at the same channel monthly and it only picks up what's new):

  scan <url>            list a channel's videos / a feed's articles as JSON
  fetch <id|url> [...]  pull captions or article text, clean, archive
  list                  what's already in the archive

Captions only — never downloads video/audio (--skip-download). Uses YouTube's own
caption track, so no whisper/ffmpeg transcription step is needed.

Env:
  TRANSCRIPTS   archive dir (default setup/reference/transcripts)
  YTDLP         yt-dlp binary (default: PATH)
  FETCH_SLEEP   seconds between fetches (default 4 — YouTube 429s below ~this)
"""
import os, sys, re, json, html, subprocess, shutil, time, datetime, glob

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.environ.get("LARRY_REPO", os.path.dirname(HERE))
TRANSCRIPTS = os.environ.get("TRANSCRIPTS", os.path.join(REPO, "reference", "transcripts"))
YTDLP = os.environ.get("YTDLP") or shutil.which("yt-dlp") or os.path.expanduser("~/.local/bin/yt-dlp")
FETCH_SLEEP = float(os.environ.get("FETCH_SLEEP", "4"))

# --js-runtimes node is REQUIRED: without a JS runtime yt-dlp's extractor fails.
BASE = [YTDLP, "--js-runtimes", "node", "--no-warnings"]


def slugify(title):
    s = re.sub(r"[^\w\s-]", "", (title or "").lower()).strip()
    return re.sub(r"[\s_-]+", "-", s)[:60].strip("-") or "untitled"


def archive_path(vid, title):
    return os.path.join(TRANSCRIPTS, f"{slugify(title)}.md")


_archived_ids = None


def _archived_id_index():
    """Video IDs already present in the archive, read once per process. Scanning a
    channel checks every video, so re-reading the archive per video would be O(n*m)."""
    global _archived_ids
    if _archived_ids is None:
        _archived_ids = set()
        for f in glob.glob(os.path.join(TRANSCRIPTS, "*.md")):
            try:
                with open(f, encoding="utf-8", errors="replace") as fh:
                    head = fh.read(2000)
                m = re.search(r"\*\*Video ID:\*\*\s*(\S+)", head)
                if m:
                    _archived_ids.add(m.group(1))
                else:   # transcripts archived by hand, before the header existed
                    for u in re.findall(r"(?:v=|youtu\.be/)([\w-]{11})", head):
                        _archived_ids.add(u)
            except OSError:
                pass
    return _archived_ids


def already_archived(vid, title):
    """Ingested if the video ID is in the archive index, or a file with its slug
    exists. ID match is authoritative — titles get edited after publication."""
    if vid and vid in _archived_id_index():
        return True
    return os.path.exists(archive_path(vid, title))


def find_archived(vid, title=""):
    """Path of the archived transcript for this id/url, or None.

    Must not be derived from the title alone: an ingest plan truncates titles to
    keep its table readable, and a truncated title slugifies to a DIFFERENT
    filename than the archived one (…locking-in-t vs …locking-in-the). That made
    run() miss transcripts it already had and skip them as "already archived".
    Search by ID first — that is stable — and only fall back to the slug.
    """
    if vid:
        for f in glob.glob(os.path.join(TRANSCRIPTS, "*.md")):
            try:
                with open(f, encoding="utf-8", errors="replace") as fh:
                    if vid in fh.read(2000):
                        return f
            except OSError:
                pass
    p = archive_path(vid, title)
    return p if os.path.exists(p) else None


def scan(channel_url):
    """Flat-list a channel/playlist. Cheap: metadata only, no per-video extraction."""
    cmd = BASE + ["--flat-playlist", "-J", channel_url]
    out = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
    if out.returncode != 0:
        print(f"ERROR: yt-dlp scan failed: {out.stderr.strip()[:400]}", file=sys.stderr)
        return []
    try:
        data = json.loads(out.stdout)
    except json.JSONDecodeError as e:
        print(f"ERROR: could not parse yt-dlp JSON ({e})", file=sys.stderr)
        return []
    # A channel/playlist has "entries"; a single-video URL (or a bare 11-char ID)
    # has none -- yt-dlp returns the video object itself. Fall back to [data] so a
    # lone video still scans (youtu.be/<id>, watch?v=<id>, or the bare ID).
    entries = data.get("entries")
    if not entries and data.get("id"):
        entries = [data]
    vids = []
    for e in (entries or []):
        if not e:
            continue
        # nested playlists (a channel's tabs) -> flatten one level
        for sub in (e.get("entries") or [e]):
            if not sub or not sub.get("id"):
                continue
            vids.append({
                "id": sub.get("id"),
                "title": (sub.get("title") or "").strip(),
                "duration": sub.get("duration") or 0,
                "upload_date": sub.get("upload_date") or "",
                "url": sub.get("url") or f"https://www.youtube.com/watch?v={sub.get('id')}",
                "channel": (sub.get("channel") or data.get("title") or "").strip(),
                "description": (sub.get("description") or "")[:400],
                "archived": already_archived(sub.get("id"), sub.get("title") or ""),
            })
    return vids


def clean_vtt(text):
    """VTT -> plain prose. Strips cue timings, positioning, inline karaoke tags and
    the rolling-duplicate lines auto-captions emit."""
    lines, seen_last = [], None
    for raw in text.splitlines():
        ln = raw.strip()
        if (not ln or ln.startswith(("WEBVTT", "Kind:", "Language:", "NOTE", "STYLE"))
                or "-->" in ln or ln.isdigit()):
            continue
        ln = re.sub(r"<[^>]+>", "", ln)          # <c>, <00:00:00.000> karaoke tags
        ln = re.sub(r"align:\S+|position:\S+", "", ln)
        ln = html.unescape(ln).strip()
        if not ln or ln == seen_last:            # auto-caption rolling repeats
            continue
        lines.append(ln)
        seen_last = ln
    # collapse the word-level overlap auto-captions leave between consecutive cues
    out = []
    for ln in lines:
        if out and (ln.startswith(out[-1]) or out[-1].endswith(ln)):
            if len(ln) > len(out[-1]):
                out[-1] = ln
            continue
        out.append(ln)
    return "\n".join(out)


def fetch(video, outdir=None):
    """Fetch + clean + archive one video's captions. Returns the archive path or None."""
    outdir = outdir or TRANSCRIPTS
    os.makedirs(outdir, exist_ok=True)
    vid, title = video["id"], video.get("title") or video["id"]
    dest = archive_path(vid, title)
    if already_archived(vid, title):
        print(f"  skip (already archived): {title}")
        return None

    import tempfile
    with tempfile.TemporaryDirectory() as tmp:
        cmd = BASE + [
            "--skip-download", "--write-auto-sub", "--write-sub",
            "--sub-lang", "en.*,en", "--sub-format", "vtt",
            "-o", os.path.join(tmp, "%(id)s.%(ext)s"),
            video.get("url") or f"https://www.youtube.com/watch?v={vid}",
        ]
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=900)
        vtts = sorted(glob.glob(os.path.join(tmp, "*.vtt")))
        if not vtts:
            err = (r.stderr or "").strip()[:200]
            print(f"  NO CAPTIONS: {title}" + (f" ({err})" if err else ""))
            return None
        with open(vtts[0], encoding="utf-8", errors="replace") as fh:
            body = clean_vtt(fh.read())

    if len(body) < 200:
        print(f"  TOO SHORT after cleaning, skipped: {title}")
        return None

    dur = video.get("duration") or 0
    ud = video.get("upload_date") or ""
    ud_fmt = f"{ud[:4]}-{ud[4:6]}-{ud[6:]}" if len(ud) == 8 else ud
    header = (
        f"# {title}\n\n"
        f"- **Source:** {video.get('url')}\n"
        f"- **Video ID:** {vid}\n"
        f"- **Channel:** {video.get('channel') or 'unknown'}\n"
        f"- **Published:** {ud_fmt or 'unknown'}\n"
        f"- **Duration:** {int(dur)//60}m{int(dur)%60:02d}s\n"
        f"- **Ingested:** {datetime.date.today().isoformat()}\n"
        f"- **Source of text:** YouTube caption track (auto-generated captions are "
        f"unreliable for API/identifier names — verify against Microsoft Learn or the "
        f"compiler before trusting a signature).\n\n"
        f"---\n\n"
    )
    with open(dest, "w", encoding="utf-8") as fh:
        fh.write(header + body + "\n")
    print(f"  archived: {os.path.relpath(dest, REPO)} ({len(body)} chars)")
    return dest


# ---------------------------------------------------------------------------
# Web / blog sources
#
# Same pipeline as video, only fetch+clean differ: an RSS/Atom feed is the exact
# analogue of a channel listing, and an article is the analogue of a transcript.
# Deliberately distil-only by default: we archive a metadata stub (URL, title,
# date) for idempotency and keep the distilled notes, rather than mirroring other
# people's full articles into the repo. ARCHIVE_FULLTEXT=1 opts in.
# ---------------------------------------------------------------------------

ARCHIVE_FULLTEXT = os.environ.get("ARCHIVE_FULLTEXT", "0") == "1"
UA = {"User-Agent": "Mozilla/5.0 (compatible; larry-ingest/1.0)"}


def detect_source(url):
    u = (url or "").strip()
    # A bare 11-char video ID is what the ingest plan's ID column holds for videos —
    # it has no scheme or host, so match it before anything tries to HTTP GET it.
    if re.fullmatch(r"[\w-]{11}", u) and "." not in u:
        return "youtube"
    u = u.lower()
    if "youtube.com" in u or "youtu.be" in u:
        return "youtube"
    if re.search(r"(/feed/?$|/rss/?$|\.xml$|/atom/?$|feeds?\.)", u):
        return "feed"
    return "page"


def _http_get(url, timeout=60):
    import urllib.request
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        raw = r.read()
    enc = "utf-8"
    m = re.search(rb'charset=["\']?([\w-]+)', raw[:4000], re.I)
    if m:
        enc = m.group(1).decode("ascii", "replace")
    return raw.decode(enc, errors="replace")


class _Extract(__import__("html.parser", fromlist=["HTMLParser"]).HTMLParser):
    """Minimal readability: keep text inside <article>/<main> when present, drop
    script/style/nav/header/footer/aside/form. Used when trafilatura isn't installed
    (PEP 668 makes a system pip install awkward, and this keeps the tool portable)."""
    DROP = {"script", "style", "nav", "header", "footer", "aside", "form", "noscript", "svg"}
    MAIN = {"article", "main"}
    BLOCK = {"p", "div", "section", "br", "li", "tr", "h1", "h2", "h3", "h4", "h5", "h6",
             "pre", "blockquote"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts, self.main_parts = [], []
        self.depth_drop, self.depth_main = 0, 0

    def handle_starttag(self, tag, attrs):
        if tag in self.DROP:
            self.depth_drop += 1
        elif tag in self.MAIN:
            self.depth_main += 1
        elif tag in self.BLOCK:
            self._emit("\n")

    def handle_endtag(self, tag):
        if tag in self.DROP and self.depth_drop:
            self.depth_drop -= 1
        elif tag in self.MAIN and self.depth_main:
            self.depth_main -= 1
        elif tag in self.BLOCK:
            self._emit("\n")

    def handle_data(self, data):
        if self.depth_drop:
            return
        self._emit(data)

    def _emit(self, s):
        self.parts.append(s)
        if self.depth_main:
            self.main_parts.append(s)

    def text(self):
        chosen = self.main_parts if len("".join(self.main_parts).strip()) > 400 else self.parts
        out = "".join(chosen)
        out = re.sub(r"[ \t\r\f\v]+", " ", out)
        out = re.sub(r"\n\s*\n\s*\n+", "\n\n", out)
        return "\n".join(ln.strip() for ln in out.splitlines()).strip()


def html_to_text(html_doc, url=None):
    """Prefer trafilatura (better boilerplate removal) when installed; else stdlib."""
    try:
        import trafilatura
        got = trafilatura.extract(html_doc, url=url, include_comments=False,
                                  include_tables=True)
        if got and len(got) > 300:
            return got.strip()
    except ImportError:
        pass
    p = _Extract()
    p.feed(html_doc)
    return p.text()


def _page_title(html_doc, fallback):
    m = re.search(r"<title[^>]*>(.*?)</title>", html_doc, re.S | re.I)
    return html.unescape(re.sub(r"\s+", " ", m.group(1))).strip() if m else fallback


def scan_web(url):
    """List candidate articles: an RSS/Atom feed (or a page's discoverable feed)
    expands to its entries; a bare article URL is a one-item list."""
    kind = detect_source(url)
    items = []
    if kind == "page":
        try:                       # a blog root often advertises its feed
            doc = _http_get(url)
            m = re.search(r'<link[^>]+type=["\']application/(?:rss|atom)\+xml["\'][^>]*>', doc, re.I)
            href = re.search(r'href=["\']([^"\']+)', m.group(0), re.I) if m else None
            if href:
                feed_url = href.group(1)
                if feed_url.startswith("/"):
                    from urllib.parse import urljoin
                    feed_url = urljoin(url, feed_url)
                print(f"  discovered feed: {feed_url}")
                return scan_web(feed_url)
        except Exception:
            pass
        return [{"id": url, "title": "", "url": url, "source": "page",
                 "upload_date": "", "duration": 0, "channel": "",
                 "archived": already_archived(url, "")}]

    import feedparser
    f = feedparser.parse(url)
    site = (f.feed.get("title") or "") if getattr(f, "feed", None) else ""
    for e in (f.entries or []):
        link = e.get("link") or ""
        if not link:
            continue
        d = e.get("published_parsed") or e.get("updated_parsed")
        items.append({
            "id": link, "title": (e.get("title") or "").strip(), "url": link,
            "source": "page", "channel": site,
            "upload_date": time.strftime("%Y%m%d", d) if d else "",
            "duration": 0,
            "description": re.sub(r"<[^>]+>", "", (e.get("summary") or ""))[:400],
            "archived": already_archived(link, (e.get("title") or "")),
        })
    return items


def fetch_web(item):
    """Fetch + clean one article. Returns {'path','text'} — path is a metadata stub
    unless ARCHIVE_FULLTEXT=1, so re-runs skip it without mirroring the article."""
    url = item.get("url") or item.get("id")
    doc = _http_get(url)
    title = item.get("title") or _page_title(doc, url)
    body = html_to_text(doc, url=url)
    if len(body) < 300:
        print(f"  TOO SHORT after extraction, skipped: {title}")
        return None
    dest = archive_path(url, title)
    ud = item.get("upload_date") or ""
    header = (
        f"# {title}\n\n"
        f"- **Source:** {url}\n"
        f"- **Site:** {item.get('channel') or 'unknown'}\n"
        f"- **Published:** {f'{ud[:4]}-{ud[4:6]}-{ud[6:]}' if len(ud) == 8 else (ud or 'unknown')}\n"
        f"- **Ingested:** {datetime.date.today().isoformat()}\n"
    )
    if ARCHIVE_FULLTEXT:
        payload = header + "\n---\n\n" + body + "\n"
    else:
        payload = (header + f"- **Full text:** not archived (third-party article) — "
                   f"knowledge distilled into the AL reference; read the original at "
                   f"the source link above.\n")
    with open(dest, "w", encoding="utf-8") as fh:
        fh.write(payload)
    print(f"  {'archived' if ARCHIVE_FULLTEXT else 'recorded'}: "
          f"{os.path.relpath(dest, REPO)} ({len(body)} chars extracted)")
    return {"path": dest, "text": body, "title": title}


def scan_any(url):
    """Front door: dispatch on the URL's shape."""
    return scan(url) if detect_source(url) == "youtube" else scan_web(url)


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    cmd = sys.argv[1]

    if cmd == "scan":
        if len(sys.argv) < 3:
            print("usage: source_collect.py scan <url>", file=sys.stderr)
            return 2
        print(json.dumps(scan_any(sys.argv[2]), indent=2))
        return 0

    if cmd == "fetch":
        ids = sys.argv[2:]
        if not ids:
            print("usage: source_collect.py fetch <video_id|url> [...]", file=sys.stderr)
            return 2
        ok = 0
        for i, v in enumerate(ids):
            if detect_source(v) != "youtube":
                if fetch_web({"url": v, "id": v}):
                    ok += 1
                if i < len(ids) - 1:
                    time.sleep(FETCH_SLEEP)
                continue
            vid = v.rsplit("/", 1)[-1].replace("watch?v=", "")
            info = subprocess.run(BASE + ["-J", "--skip-download", v],
                                  capture_output=True, text=True, timeout=300)
            try:
                meta = json.loads(info.stdout)
            except json.JSONDecodeError:
                print(f"  metadata failed: {v}")
                continue
            if fetch({"id": meta.get("id", vid), "title": meta.get("title", vid),
                      "duration": meta.get("duration", 0),
                      "upload_date": meta.get("upload_date", ""),
                      "channel": meta.get("channel", ""),
                      "url": meta.get("webpage_url", v)}):
                ok += 1
            if i < len(ids) - 1:
                time.sleep(FETCH_SLEEP)   # YouTube 429s if you go faster
        print(f"\nFetched {ok}/{len(ids)}.")
        return 0

    if cmd == "collect":
        # scan + fetch everything not yet archived. Wholly deterministic (no model,
        # no egress beyond the source itself) — this is what Larry's dashboard runs,
        # since Larry has no Claude. Distil/merge then happens on a dev box.
        if len(sys.argv) < 3:
            print("usage: source_collect.py collect <url> [limit]", file=sys.stderr)
            return 2
        items = scan_any(sys.argv[2])
        limit = int(sys.argv[3]) if len(sys.argv) > 3 and sys.argv[3].isdigit() else None
        fresh = [i for i in items if not i["archived"]][:limit]
        print(f"{len(items)} found, {len(items)-len([i for i in items if not i['archived']])} "
              f"already archived, {len(fresh)} to collect.")
        ok = 0
        for i, it in enumerate(fresh, 1):
            print(f"[{i}/{len(fresh)}] {it.get('title') or it['id']}")
            got = fetch_web(it) if it.get("source") == "page" else fetch(it)
            ok += bool(got)
            if i < len(fresh):
                time.sleep(FETCH_SLEEP)
        print(f"\nCollected {ok}/{len(fresh)}. Distil + merge on a dev box: ingw scan/run")
        return 0

    if cmd == "list":
        files = sorted(glob.glob(os.path.join(TRANSCRIPTS, "*.md")))
        for f in files:
            print(f"  {os.path.basename(f)}")
        print(f"\n{len(files)} transcript(s) in {TRANSCRIPTS}")
        return 0

    print(f"unknown command: {cmd}", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
