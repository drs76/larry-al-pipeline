#!/usr/bin/env python3
"""kb_core.py — local hybrid (BM25 + vector) search over the markdown knowledge bases.

No egress: embeddings come from Larry (mxbai-embed-large via the HTTPS proxy), vectors
and BM25 index live in a local sqlite store. Mirrors the hand-rolled-urllib style of the
pipeline scripts (no heavy SDKs). Consumed by the `kb` CLI, the kb-search MCP server, and
the pi kb-search extension.

Commands:
  kb_core.py index  [--corpus NAME] [--rebuild]   build/refresh the index (idempotent)

WARNING: --rebuild is GLOBAL — it clears the whole chunk store, not just --corpus.
`index --corpus X --rebuild` therefore wipes every OTHER corpus and reindexes only X.
To refresh one corpus, omit --rebuild (indexing is idempotent and picks up changes);
use --rebuild alone when you really want to rebuild everything.
  kb_core.py search QUERY [--corpus NAME] [-n N] [--json]
  kb_core.py stats
  kb_core.py corpora
  kb_core.py serve [--host H] [--port P]           HTTP query endpoint for thin clients (Larry)

Thin clients (WSL / ThinkPad): set KB_REMOTE=http://larry.home.arpa:8848 — search/stats/corpora
then go over HTTP to a `kb serve` instance, no local sqlite/corpora needed.
"""
import argparse, hashlib, json, os, re, sqlite3, ssl, sys, time, urllib.request, urllib.error
import yaml

# numpy is needed ONLY for the local-index paths (embedding + vector rerank). Thin
# clients (KB_REMOTE) go over HTTP and never touch it, so a hard top-level import
# made `kb search` die with ModuleNotFoundError on a box that by design has no
# index — import lazily and fail with an actionable message at the point of use.
try:
    import numpy as np
except ModuleNotFoundError:
    np = None

def _need_numpy():
    if np is None:
        sys.exit("numpy required for local indexing/vector search — `apt install python3-numpy` "
                 "(or pip in a venv). Thin clients: set KB_REMOTE=http://larry.home.arpa:8848 instead.")

HERE       = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT  = os.environ.get("KB_REPO_ROOT", os.path.abspath(os.path.join(HERE, "..", "..")))
CORPORA    = os.environ.get("KB_CORPORA", os.path.join(HERE, "kb-corpora.yaml"))
DB_PATH    = os.environ.get("KB_DB", os.path.join(HERE, ".kb-index", "kb.db"))
EMBED_URL  = os.environ.get("KB_EMBED_URL", "https://larry.home.arpa:11443/v1/embeddings")
EMBED_MODEL= os.environ.get("KB_EMBED_MODEL", "mxbai-embed-large")
EMBED_KEY  = os.environ.get("KB_EMBED_KEY", "ollama")
MAX_CHUNK  = int(os.environ.get("KB_MAX_CHUNK", "1600"))   # chars
BATCH      = int(os.environ.get("KB_EMBED_BATCH", "32"))
EMBED_RETRIES = int(os.environ.get("KB_EMBED_RETRIES", "5"))    # transient DNS/network blips
EMBED_BACKOFF = float(os.environ.get("KB_EMBED_BACKOFF", "1.5")) # seconds, exponential
# Thin-client mode: when KB_REMOTE points at a `kb serve` instance (e.g. on Larry), search/stats
# go over HTTP instead of opening the local sqlite store. Lets WSL / ThinkPad clients query the
# shared index without the 24MB db or the corpora. The token must match the server's: env
# KB_REMOTE_TOKEN, else ~/.pi/.kb-token — same contract as al-rag and the kb-search pi
# extension, so a client that already has the token file needs no extra env (without the
# file fallback every thin client got a bare `HTTP Error 401`).
REMOTE      = os.environ.get("KB_REMOTE", "").rstrip("/")

def _remote_token():
    if os.environ.get("KB_REMOTE_TOKEN"):
        return os.environ["KB_REMOTE_TOKEN"]
    try:
        with open(os.path.expanduser("~/.pi/.kb-token")) as f:
            return f.read().strip()
    except OSError:
        return ""

REMOTE_TOKEN= _remote_token()

# ---------------------------------------------------------------- config / paths
def load_corpora():
    with open(CORPORA) as f:
        return (yaml.safe_load(f) or {}).get("corpora", {})

def resolve(p):
    p = os.path.expanduser(p)
    return p if os.path.isabs(p) else os.path.join(REPO_ROOT, p)

def display_path(p):
    home = os.path.expanduser("~")
    return p.replace(home, "~") if p.startswith(home) else p

def corpus_files(spec):
    files = []
    for raw in spec.get("paths", []):
        ap = resolve(raw)
        if os.path.isdir(ap):
            for root, _, names in os.walk(ap):
                files += [os.path.join(root, n) for n in sorted(names) if n.endswith((".md", ".al"))]
        elif os.path.isfile(ap):
            files.append(ap)
    return files

# ---------------------------------------------------------------- markdown chunking
FM_RE = re.compile(r"\A---\n(.*?)\n---\n", re.S)
H_RE  = re.compile(r"^(#{1,4})\s+(.*)$")

def parse_frontmatter(text):
    m = FM_RE.match(text)
    if not m:
        return {}, text
    try:
        fm = yaml.safe_load(m.group(1)) or {}
        if not isinstance(fm, dict):
            fm = {}
    except Exception:
        fm = {}
    return fm, text[m.end():]

def _split_long(heading, body):
    """Split an over-long section into <=MAX_CHUNK pieces on paragraph boundaries.
    A single paragraph longer than MAX_CHUNK (minified data, unbroken code) is HARD-sliced
    so no chunk can exceed the limit — otherwise the embed request 413s (and mxbai truncates
    at ~512 tokens anyway, so an oversized chunk buys nothing)."""
    paras, out, buf = re.split(r"\n\s*\n", body), [], ""
    for para in paras:
        while len(para) > MAX_CHUNK:            # hard-slice runaway paragraphs
            if buf:
                out.append(buf.strip()); buf = ""
            out.append(para[:MAX_CHUNK]); para = para[MAX_CHUNK:]
        if len(buf) + len(para) + 2 > MAX_CHUNK and buf:
            out.append(buf.strip()); buf = ""
        buf += para + "\n\n"
    if buf.strip():
        out.append(buf.strip())
    return out or [body.strip()]

def chunk_markdown(path, text):
    """Yield (heading_breadcrumb, chunk_text). Splits on headings; large sections subdivide."""
    fm, body = parse_frontmatter(text)
    label = fm.get("name") or fm.get("title")
    tags  = fm.get("tags")
    prefix_bits = []
    if label: prefix_bits.append(str(label))
    if tags:  prefix_bits.append("tags: " + (", ".join(tags) if isinstance(tags, list) else str(tags)))
    fm_prefix = " | ".join(prefix_bits)

    lines = body.splitlines()
    stack, cur_head, cur_lines, sections = [], "", [], []
    def flush():
        if cur_lines and any(l.strip() for l in cur_lines):
            sections.append((cur_head, "\n".join(cur_lines).strip()))
    for ln in lines:
        m = H_RE.match(ln)
        if m:
            flush()
            level = len(m.group(1)); title = m.group(2).strip()
            stack[:] = stack[:level-1] + [title]
            cur_head = " › ".join(stack)
            cur_lines = []
        else:
            cur_lines.append(ln)
    flush()
    if not sections:                       # no headings — whole doc as one section
        sections = [("", body.strip())]

    for head, sect in sections:
        if not sect.strip():
            continue
        pieces = [sect] if len(sect) <= MAX_CHUNK else _split_long(head, sect)
        for i, piece in enumerate(pieces):
            crumb = head + (f" ({i+1}/{len(pieces)})" if len(pieces) > 1 else "")
            emb_text = "\n".join(x for x in (fm_prefix, crumb, piece) if x)
            yield crumb, piece, emb_text

# ---------------------------------------------------------------- AL (.al) chunking
# AL structure: an object is `<type> <id> "<name>" { ... }`. Sub-blocks (fields/keys/
# layout/actions/…) are brace-delimited; procedures/triggers are NOT — their body is
# `begin … end;` and they sit at brace-depth 1 inside the object. So we split the object
# body into brace-depth-1 members (each block, procedure or trigger = one chunk), keeping
# any `[Attribute(...)]` lines attached to the procedure they decorate. One object per file
# is the BC norm; a second object in the same file is folded into the last member's chunk.
AL_OBJECT_RE = re.compile(
    r'^\s*(codeunit|tableextension|table|pageextension|page|reportextension|report|'
    r'enumextension|enum|interface|query|permissionsetextension|permissionset|'
    r'controladdin|pagecustomization|profile|xmlport|entitlement|dotnet)\b', re.I)
AL_MEMBER_RE = re.compile(
    r'^\s*((local\s+|internal\s+|protected\s+)*procedure\b|trigger\b|var\b|fields\b|'
    r'fieldgroups\b|keys\b|layout\b|actions\b|requestpage\b|dataset\b|schema\b|'
    r'elements\b|views\b|labels\b|value\b)', re.I)
AL_ATTR_RE = re.compile(r'^\s*\[')

def _al_label(line):
    s = re.sub(r'\s*[\{\(].*$', '', line.strip())     # drop trailing { or ( and after
    return (s[:70] or "member").strip()

def chunk_al(path, text):
    """Yield (crumb, piece, emb_text) for an AL object, split by brace-depth-1 members."""
    lines = text.splitlines()
    obj_i = next((i for i, l in enumerate(lines)
                  if l.strip() and not l.lstrip().startswith(("//", "/*", "*", "#"))
                  and AL_OBJECT_RE.match(l)), None)
    base = os.path.basename(path)
    if obj_i is None:                                  # not an object file — whole-file chunk(s)
        body = text.strip()
        pieces = [body] if len(body) <= MAX_CHUNK else _split_long(base, body)
        for i, piece in enumerate(pieces):
            crumb = base + (f" ({i+1}/{len(pieces)})" if len(pieces) > 1 else "")
            if piece.strip():
                yield crumb, piece, crumb + "\n" + piece
        return

    objdecl = re.sub(r'\s*\{.*$', '', lines[obj_i].strip())
    depth, buf, unit_open = 0, [], False
    crumb = objdecl + " › (header)"
    out = []
    for l in lines[obj_i:]:
        if depth == 1 and AL_MEMBER_RE.match(l) and unit_open:
            seg = "\n".join(buf).strip()
            if seg:
                out.append((crumb, seg))
            buf, unit_open = [], False
        if depth == 1 and AL_MEMBER_RE.match(l):
            crumb = objdecl + " › " + _al_label(l)
        buf.append(l)
        depth += l.count("{") - l.count("}")
        if l.strip() and not AL_ATTR_RE.match(l) and depth >= 1:
            unit_open = True                           # attribute lines don't open a unit
    seg = "\n".join(buf).strip()
    if seg:
        out.append((crumb, seg))

    for head, sect in out:
        pieces = [sect] if len(sect) <= MAX_CHUNK else _split_long(head, sect)
        for i, piece in enumerate(pieces):
            c = head + (f" ({i+1}/{len(pieces)})" if len(pieces) > 1 else "")
            yield c, piece, c + "\n" + piece

def sha(s):  # content hash for idempotent re-index
    return hashlib.sha256(s.encode("utf-8")).hexdigest()

# ---------------------------------------------------------------- embeddings (Larry)
def _ssl_ctx():
    # Trust the system CA store (HomeLab CA already installed). Python 3.13 turns on
    # VERIFY_X509_STRICT, which rejects the HomeLab CA (no keyUsage extension) — drop just
    # that flag so the chain is still verified but the lenient CA is accepted (as curl does).
    ctx = ssl.create_default_context(cafile=os.environ.get("KB_EMBED_CA") or None)
    ctx.verify_flags &= ~ssl.VERIFY_X509_STRICT
    if os.environ.get("KB_INSECURE") == "1":            # last-resort escape hatch (LAN only)
        ctx.check_hostname = False; ctx.verify_mode = ssl.CERT_NONE
    return ctx

_CTX = _ssl_ctx()

def embed(texts):
    """Return np.float32 [n, dim] embeddings from Larry. Batches; falls back to singles."""
    _need_numpy()
    out = []
    i = 0
    while i < len(texts):
        batch = texts[i:i+BATCH]
        try:
            out.extend(_embed_call(batch))
        except Exception:
            for t in batch:                 # fallback: one at a time
                out.extend(_embed_call([t]))
        i += BATCH
    return np.asarray(out, dtype=np.float32)

def _embed_call(batch):
    body = json.dumps({"model": EMBED_MODEL, "input": batch}).encode()
    # Retry transient network/DNS blips (deb→Larry resolver hiccups under sustained load
    # surface as "Temporary failure in name resolution" and would otherwise abort a whole
    # corpus mid-index). Exponential backoff; re-raise only after EMBED_RETRIES attempts.
    last = None
    for attempt in range(EMBED_RETRIES):
        try:
            req = urllib.request.Request(EMBED_URL, data=body, headers={
                "Content-Type": "application/json", "Authorization": f"Bearer {EMBED_KEY}"})
            with urllib.request.urlopen(req, context=_CTX, timeout=120) as r:
                data = json.loads(r.read())
            rows = sorted(data["data"], key=lambda d: d.get("index", 0))
            return [d["embedding"] for d in rows]
        except Exception as e:                       # noqa: BLE001 — retry any transient failure
            last = e
            if attempt < EMBED_RETRIES - 1:
                time.sleep(EMBED_BACKOFF * (2 ** attempt))
    raise last

# ---------------------------------------------------------------- store
def db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    con = sqlite3.connect(DB_PATH, timeout=30)
    # WAL lets `serve` (reader) and `index` (writer) coexist without corrupting each other.
    # REQUIRES a local-disk DB — WAL over NFS is unsafe (that combo corrupted the old deb index
    # 2026-08-06). Keep KB_DB on the serving host's own disk.
    con.execute("PRAGMA journal_mode=WAL")
    con.execute("PRAGMA synchronous=NORMAL")
    con.execute("PRAGMA busy_timeout=30000")
    con.execute("""CREATE TABLE IF NOT EXISTS chunks(
        id INTEGER PRIMARY KEY, corpus TEXT, path TEXT, heading TEXT,
        text TEXT, sha TEXT, dim INTEGER, emb BLOB)""")
    con.execute("CREATE INDEX IF NOT EXISTS ix_chunks_cp ON chunks(corpus, path)")
    # self-contained (not contentless) so per-row DELETE works on incremental re-index
    con.execute("CREATE VIRTUAL TABLE IF NOT EXISTS chunks_fts USING fts5(text)")
    con.commit()
    return con

def _fts_set(con, rowid, text):
    con.execute("INSERT INTO chunks_fts(rowid, text) VALUES(?,?)", (rowid, text))

def _fts_del(con, rowid):
    con.execute("DELETE FROM chunks_fts WHERE rowid=?", (rowid,))

# ---------------------------------------------------------------- indexing
def index(only=None, rebuild=False):
    corpora = load_corpora()
    con = db()
    if rebuild:
        con.execute("DELETE FROM chunks"); con.execute("DELETE FROM chunks_fts"); con.commit()
    total_add = total_del = 0
    for name, spec in corpora.items():
        if only and name != only:
            continue
        files = corpus_files(spec)
        seen_paths = set()
        for fp in files:
            dp = display_path(fp)
            seen_paths.add(dp)
            with open(fp, encoding="utf-8", errors="replace") as f:
                text = f.read()
            cur = {}   # (heading, sha) -> (piece, emb_text)
            chunker = chunk_al if fp.endswith(".al") else chunk_markdown
            for crumb, piece, emb_text in chunker(fp, text):
                cur[(crumb, sha(piece))] = (piece, emb_text)
            rows = con.execute("SELECT id, heading, sha FROM chunks WHERE corpus=? AND path=?",
                               (name, dp)).fetchall()
            existing = {(h, s): rid for rid, h, s in rows}
            to_del = [rid for k, rid in existing.items() if k not in cur]
            to_add = [(k, v) for k, v in cur.items() if k not in existing]
            for rid in to_del:
                con.execute("DELETE FROM chunks WHERE id=?", (rid,)); _fts_del(con, rid)
            if to_add:
                embs = embed([v[1] for _, v in to_add])
                for (k, v), e in zip(to_add, embs):
                    crumb, s = k; piece, _ = v
                    cur_ = con.execute(
                        "INSERT INTO chunks(corpus,path,heading,text,sha,dim,emb) VALUES(?,?,?,?,?,?,?)",
                        (name, dp, crumb, piece, s, len(e), e.tobytes()))
                    _fts_set(con, cur_.lastrowid, (crumb + "\n" + piece))
            total_add += len(to_add); total_del += len(to_del)
            if to_add or to_del:
                print(f"  {name}: {display_path(fp)}  +{len(to_add)} -{len(to_del)}", file=sys.stderr)
        # drop chunks for files that vanished from the corpus
        placeholders = ",".join("?" * len(seen_paths)) or "''"
        stale = con.execute(
            f"SELECT id FROM chunks WHERE corpus=? AND path NOT IN ({placeholders})",
            [name, *seen_paths]).fetchall()
        for (rid,) in stale:
            con.execute("DELETE FROM chunks WHERE id=?", (rid,)); _fts_del(con, rid); total_del += 1
        con.commit()
    print(f"index done: +{total_add} chunks, -{total_del} removed", file=sys.stderr)
    con.close()

# ---------------------------------------------------------------- remote client
def _remote_call(path, payload=None):
    """GET (payload=None) or POST JSON to the KB_REMOTE server; return parsed JSON."""
    url = REMOTE + path
    data = json.dumps(payload).encode() if payload is not None else None
    headers = {"Content-Type": "application/json"}
    if REMOTE_TOKEN:
        headers["Authorization"] = f"Bearer {REMOTE_TOKEN}"
    req = urllib.request.Request(url, data=data, headers=headers, method="POST" if data else "GET")
    with urllib.request.urlopen(req, timeout=30) as r:   # plain HTTP, LAN only
        return json.loads(r.read())

def corpora_list():
    """[(name, desc)] — remote-aware so thin clients need no local yaml."""
    if REMOTE:
        return [(c["name"], c.get("desc", "")) for c in _remote_call("/corpora")]
    return [(name, spec.get("desc", "")) for name, spec in load_corpora().items()]

# ---------------------------------------------------------------- search
def _fts_query(q):
    terms = re.findall(r"[A-Za-z0-9_]+", q)
    return " OR ".join(f'"{t}"' for t in terms) if terms else ""

def search(query, corpus=None, n=8, pool=40):
    if REMOTE:
        return _remote_call("/search", {"query": query, "corpus": corpus, "n": n})
    con = db()
    where = "WHERE corpus=?" if corpus else ""
    args  = (corpus,) if corpus else ()
    rows = con.execute(f"SELECT id, corpus, path, heading, text, dim, emb FROM chunks {where}", args).fetchall()
    if not rows:
        con.close(); return []
    by_id = {r[0]: r for r in rows}

    # dense
    qv = embed([query])[0]
    qn = qv / (np.linalg.norm(qv) + 1e-9)
    mat = np.stack([np.frombuffer(r[6], dtype=np.float32) for r in rows])
    mat = mat / (np.linalg.norm(mat, axis=1, keepdims=True) + 1e-9)
    sims = mat @ qn
    order = np.argsort(-sims)[:pool]
    dense_rank = {rows[i][0]: k for k, i in enumerate(order)}

    # keyword (BM25 via FTS5)
    kw_rank = {}
    fq = _fts_query(query)
    if fq:
        cond = " AND corpus=?" if corpus else ""
        cargs = (fq, corpus) if corpus else (fq,)
        try:
            frows = con.execute(
                f"SELECT c.id FROM chunks_fts f JOIN chunks c ON c.id=f.rowid "
                f"WHERE f.text MATCH ?{cond} ORDER BY bm25(f) LIMIT ?", (*cargs, pool)).fetchall()
            kw_rank = {rid: k for k, (rid,) in enumerate(frows)}
        except sqlite3.OperationalError:
            kw_rank = {}
    con.close()

    # reciprocal rank fusion
    K = 60
    scores = {}
    for rid, rk in dense_rank.items(): scores[rid] = scores.get(rid, 0) + 1.0/(K+rk)
    for rid, rk in kw_rank.items():    scores[rid] = scores.get(rid, 0) + 1.0/(K+rk)
    ranked = sorted(scores, key=lambda r: -scores[r])[:n]
    out = []
    for rid in ranked:
        _, corp, path, head, text, _, _ = by_id[rid]
        snip = re.sub(r"\s+", " ", text).strip()[:280]
        out.append({"corpus": corp, "path": path, "heading": head,
                    "score": round(scores[rid], 5), "snippet": snip})
    return out

# ---------------------------------------------------------------- stats
def stats():
    if REMOTE:
        return [tuple(r) for r in _remote_call("/stats")]
    con = db()
    rows = con.execute("SELECT corpus, COUNT(*), COUNT(DISTINCT path) FROM chunks GROUP BY corpus").fetchall()
    con.close()
    return rows

# ---------------------------------------------------------------- serve (remote-query wrapper)
def serve(host, port, token):
    """Expose read-only search/stats/corpora over HTTP for thin clients. LAN only, no TLS.
    Runs on Larry (owns the sqlite index); WSL/ThinkPad point KB_REMOTE here."""
    from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

    class H(BaseHTTPRequestHandler):
        protocol_version = "HTTP/1.1"
        def log_message(self, *a): pass                       # quiet; systemd journals stderr
        def _authed(self):
            if not token:
                return True
            return self.headers.get("Authorization", "") == f"Bearer {token}"
        def _send(self, code, obj):
            body = json.dumps(obj).encode()
            self.send_response(code)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        def do_GET(self):
            if self.path == "/health":
                return self._send(200, {"ok": True})
            if not self._authed():
                return self._send(401, {"error": "unauthorized"})
            if self.path == "/stats":
                return self._send(200, [list(r) for r in stats()])
            if self.path == "/corpora":
                return self._send(200, [{"name": n, "desc": d} for n, d in corpora_list()])
            self._send(404, {"error": "not found"})
        def do_POST(self):
            if not self._authed():
                return self._send(401, {"error": "unauthorized"})
            if self.path != "/search":
                return self._send(404, {"error": "not found"})
            n = int(self.headers.get("Content-Length", 0))
            try:
                req = json.loads(self.rfile.read(n) or b"{}")
            except Exception:
                return self._send(400, {"error": "bad json"})
            q = (req.get("query") or "").strip()
            if not q:
                return self._send(400, {"error": "query required"})
            res = search(q, corpus=req.get("corpus"), n=int(req.get("n") or 8))
            self._send(200, res)

    srv = ThreadingHTTPServer((host, port), H)
    print(f"kb serve on http://{host}:{port}  (auth: {'token' if token else 'none'})", file=sys.stderr)
    srv.serve_forever()

# ---------------------------------------------------------------- cli
def main():
    ap = argparse.ArgumentParser(prog="kb", description="local hybrid search over markdown KBs")
    sub = ap.add_subparsers(dest="cmd", required=True)
    pi = sub.add_parser("index"); pi.add_argument("--corpus"); pi.add_argument("--rebuild", action="store_true")
    ps = sub.add_parser("search"); ps.add_argument("query"); ps.add_argument("--corpus")
    ps.add_argument("-n", type=int, default=8); ps.add_argument("--json", action="store_true")
    sub.add_parser("stats"); sub.add_parser("corpora")
    pv = sub.add_parser("serve")
    pv.add_argument("--host", default=os.environ.get("KB_SERVE_HOST", "0.0.0.0"))
    pv.add_argument("--port", type=int, default=int(os.environ.get("KB_SERVE_PORT", "8848")))
    a = ap.parse_args()

    if a.cmd == "index":
        if REMOTE:
            sys.exit("refusing to index in KB_REMOTE (thin-client) mode — index on the server (Larry)")
        index(only=a.corpus, rebuild=a.rebuild)
    elif a.cmd == "serve":
        if REMOTE:
            sys.exit("refusing to serve while KB_REMOTE is set (would proxy to itself) — unset KB_REMOTE")
        serve(a.host, a.port, os.environ.get("KB_SERVE_TOKEN", ""))
    elif a.cmd == "search":
        res = search(a.query, corpus=a.corpus, n=a.n)
        if a.json:
            print(json.dumps(res, indent=2))
        elif not res:
            print("(no results — is the index built? run `kb index`)", file=sys.stderr)
        else:
            for r in res:
                print(f"[{r['score']}] {r['corpus']}  {r['path']}")
                print(f"      {r['heading']}")
                print(f"      {r['snippet']}\n")
    elif a.cmd == "stats":
        for corp, c, p in stats():
            print(f"{corp:16} {c:6} chunks  {p:4} files")
    elif a.cmd == "corpora":
        for name, desc in corpora_list():
            print(f"{name:16} {desc}")

if __name__ == "__main__":
    main()
