#!/usr/bin/env python3
"""Larry maintenance dashboard — small Flask app (runs ON Larry).

Tabs: Maintenance (ollama update/restart, pull/remove models, nginx reload),
AL Knowledge (view AL-REFERENCE, anonymise an export), Docs (render the flow docs).

Binds 127.0.0.1 only — exposed via nginx (larry.home.arpa) behind HTTP basic-auth.
Privileged ops use passwordless doas (service runs as a doas-capable user).
"""
import os, re, subprocess, threading, uuid, html, shlex, json, urllib.request
from flask import Flask, request, jsonify, Response

app = Flask(__name__)


@app.before_request
def _same_origin_guard():
    """CSRF mitigation: basic-auth is browser-cached, so a hostile page could POST here
    with credentials attached. Reject state-changing requests whose Origin/Referer names
    a different host. Same-origin fetches and non-browser clients (no Origin) pass."""
    if request.method in ("POST", "PUT", "DELETE"):
        origin = request.headers.get("Origin") or request.headers.get("Referer") or ""
        if origin:
            from urllib.parse import urlparse
            if urlparse(origin).hostname not in (request.host.split(":")[0], "localhost", "127.0.0.1"):
                return jsonify(ok=False, out="cross-origin request rejected"), 403


BASE = os.path.dirname(os.path.abspath(__file__))  # where app.py + vendor/ live
REPO = os.environ.get("LARRY_REPO", "/mnt/rojaws/localDev/setup")
ANON = f"{REPO}/tooling/anonymise.py"
PORT = int(os.environ.get("DASH_PORT", "8090"))

# docs shown in the Docs tab (label -> repo-relative path)
DOCS = {
    "Project Lifecycle": "pipeline/PROJECT-LIFECYCLE.md",
    "alw (AL)": "pipeline/ALW.md",
    "gow (Go)": "pipeline/GOW.md",
    "csw (C#)": "pipeline/CSW.md",
    "bcw (BC analysis)": "pipeline/BCW.md",
    "coms / review": "pipeline/COMS.md",
    "run-build": "pipeline/RUN-BUILD.md",
    "AL Reference": "reference/AL-REFERENCE.md",
    "BCQuality Harvest": "reference/bcquality-harvest-report.md",
    "Build Leaderboard": "reference/build-leaderboard.md",
    "Larry Tower Build": "reference/larry-tower-build-and-architecture.md",
    "BC on Linux (bclinux)": "reference/bc-containers-on-linux-bclinux-bctui.md",
}

MODEL_RE = re.compile(r"^[A-Za-z0-9._:/-]+$")
_jobs = {}   # id -> {"status": running|done|error, "log": str}


def run(cmd, timeout=120):
    """Run a fixed command list; return (ok, combined output)."""
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
        return r.returncode == 0, (r.stdout + r.stderr).strip()
    except subprocess.TimeoutExpired:
        return False, f"timeout after {timeout}s"
    except Exception as e:
        return False, str(e)


def _prune_jobs(keep=20):
    """Drop oldest finished jobs so logs (e.g. ollama pull progress) don't accumulate forever."""
    done = [j for j, v in _jobs.items() if v["status"] != "running"]
    for j in done[:-keep] if len(done) > keep else []:
        _jobs.pop(j, None)


def bg(job_id, cmd, shell=False, kind=None, label=None):
    _prune_jobs()
    _jobs[job_id] = {"status": "running", "kind": kind, "label": label,
                     "log": f"$ {cmd if shell else ' '.join(cmd)}\n"}
    def worker():
        try:
            p = subprocess.Popen(cmd, shell=shell, stdout=subprocess.PIPE,
                                 stderr=subprocess.STDOUT, text=True, bufsize=1)
            for line in p.stdout:
                _jobs[job_id]["log"] += line
            p.wait()
            _jobs[job_id]["status"] = "done" if p.returncode == 0 else "error"
        except Exception as e:
            _jobs[job_id]["log"] += f"\nERROR: {e}"
            _jobs[job_id]["status"] = "error"
    threading.Thread(target=worker, daemon=True).start()


def model_names():
    ok, out = run(["ollama", "ls"])
    names = []
    if ok:
        for ln in out.splitlines()[1:]:
            if ln.strip():
                names.append(ln.split()[0])
    return names


# ─── API: status ──────────────────────────────────────────────────────────
@app.get("/api/status")
def status():
    _, ver = run(["ollama", "--version"])
    _, ps = run(["ollama", "ps"])
    _, ls = run(["ollama", "ls"])
    _, disk = run(["df", "-h", "/mnt/models", "/"])
    return jsonify(version=ver, ps=ps, ls=ls, disk=disk, models=model_names())


# ─── API: quick maintenance actions ────────────────────────────────────────
@app.post("/api/action/<name>")
def action(name):
    cmds = {
        "restart-ollama": ["doas", "systemctl", "restart", "ollama"],
        "reload-nginx":   ["doas", "systemctl", "reload", "nginx"],
        # Bonsai chat server (Mode B time-share). start evicts the coder via the
        # service's ExecStartPre; stop frees VRAM back to it. See tower/bonsai.
        "bonsai-on":      ["doas", "systemctl", "start", "bonsai-llama"],
        "bonsai-off":     ["doas", "systemctl", "stop",  "bonsai-llama"],
        # kb-serve is a USER service (runs as dav); restart via the user manager, not doas.
        "restart-kb-serve": ["env", f"XDG_RUNTIME_DIR=/run/user/{os.getuid()}",
                             "systemctl", "--user", "restart", "kb-serve"],
    }
    if name not in cmds:
        return jsonify(ok=False, out="unknown action"), 400
    ok, out = run(cmds[name])
    return jsonify(ok=ok, out=out or "(done)")


@app.get("/api/kb")
def kb_status():
    """KB hybrid-search health + per-corpus stats, queried over local HTTP (no db access here)."""
    okh, health = run(["curl", "-s", "-m", "5", "http://127.0.0.1:8848/health"], timeout=8)
    up = okh and '"ok"' in health and "true" in health
    token = ""
    try:
        with open(os.path.expanduser("~/.config/kb/serve.env")) as fh:
            for ln in fh:
                if ln.startswith("KB_SERVE_TOKEN="):
                    token = ln.split("=", 1)[1].strip()
                    break
    except OSError:
        pass
    _, stats = run(["curl", "-s", "-m", "8", "-H", f"Authorization: Bearer {token}",
                    "http://127.0.0.1:8848/stats"], timeout=12)
    return jsonify(up=up, stats=stats or "(no stats)")


@app.post("/api/job/kb-reindex")
def job_kb_reindex():
    """Idempotent refresh of the KB index (WAL-safe alongside the live serve). Streams output."""
    jid = uuid.uuid4().hex
    cmd = ("set -a; . \"$HOME/.config/kb/serve.env\"; set +a; "
           "/mnt/rojaws/localDev/setup/tooling/kb index")
    bg(jid, cmd, shell=True, kind="kb", label="kb reindex")
    return jsonify(job=jid)


@app.post("/api/chat")
def chat():
    """Non-streaming chat with a local ollama model on Larry (localhost:11434)."""
    d = request.json or {}
    model = d.get("model", "")
    messages = d.get("messages", [])
    if not MODEL_RE.match(model) or model not in model_names():
        return jsonify(ok=False, out="unknown model"), 400
    if not isinstance(messages, list) or not messages:
        return jsonify(ok=False, out="no messages"), 400
    payload = json.dumps({"model": model, "messages": messages, "stream": False}).encode()
    req = urllib.request.Request("http://127.0.0.1:11434/api/chat", data=payload,
                                 headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=300) as r:
            data = json.loads(r.read())
        return jsonify(ok=True, reply=(data.get("message") or {}).get("content", ""))
    except Exception as e:
        return jsonify(ok=False, out=f"ollama chat failed: {e}"), 502


@app.post("/api/model/rm")
def model_rm():
    m = (request.json or {}).get("model", "")
    if not MODEL_RE.match(m) or m not in model_names():
        return jsonify(ok=False, out="unknown model"), 400
    ok, out = run(["ollama", "rm", m])
    return jsonify(ok=ok, out=out or f"removed {m}")


# ─── API: long-running jobs (update, pull) ─────────────────────────────────
@app.post("/api/job/update-ollama")
def job_update():
    jid = uuid.uuid4().hex[:8]
    bg(jid, "curl -fsSL https://ollama.com/install.sh | doas sh", shell=True)
    return jsonify(job=jid)


@app.post("/api/job/pull")
def job_pull():
    m = (request.json or {}).get("model", "")
    if not MODEL_RE.match(m):
        return jsonify(ok=False, out="bad model name"), 400
    jid = uuid.uuid4().hex[:8]
    bg(jid, ["ollama", "pull", m])
    return jsonify(job=jid)


@app.post("/api/job/harvest-bcquality")
def job_harvest():
    """Pull BCQuality, resync our custom layer, reindex, and report new/changed rules."""
    jid = uuid.uuid4().hex[:8]
    bg(jid, ["python3", f"{REPO}/pipeline/bcquality_harvest.py"])
    return jsonify(job=jid)


@app.post("/api/job/leaderboard")
def job_leaderboard():
    """Aggregate per-build metrics into the model leaderboard."""
    jid = uuid.uuid4().hex[:8]
    bg(jid, ["python3", f"{REPO}/pipeline/build_leaderboard.py"])
    return jsonify(job=jid)


@app.get("/api/job/<jid>")
def job_status(jid):
    j = _jobs.get(jid)
    return (jsonify(j) if j else (jsonify(status="unknown", log=""), 404))


# ─── API: docs + AL reference ──────────────────────────────────────────────
def render_md(path):
    try:
        import markdown
        txt = open(path, encoding="utf-8").read()
        return markdown.markdown(txt, extensions=["fenced_code", "tables", "toc"])
    except Exception as e:
        return f"<pre>{html.escape(open(path).read())}</pre>" if os.path.exists(path) else f"<em>{e}</em>"


@app.get("/api/docs")
def docs_list():
    return jsonify(list(DOCS.keys()))


@app.get("/api/doc")
def doc():
    label = request.args.get("f", "")
    rel = DOCS.get(label)
    if not rel:
        return "<em>unknown doc</em>", 404
    return render_md(f"{REPO}/{rel}")


# ─── API: anonymise an uploaded export ─────────────────────────────────────
@app.post("/api/al/anonymise")
def al_anon():
    f = request.files.get("file")
    if not f:
        return jsonify(ok=False, out="no file"), 400
    import tempfile
    with tempfile.TemporaryDirectory(prefix="dash-anon-") as td:
        src, dst = os.path.join(td, "in.md"), os.path.join(td, "out.md")
        f.save(src)
        ok, out = run(["python3", ANON, src, dst], timeout=120)
        clean = open(dst, encoding="utf-8").read() if os.path.exists(dst) else ""
    return jsonify(ok=ok, out=out, clean=clean)


# ─── Logs (Larry-local journalctl) ─────────────────────────────────────────
LOG_UNITS = ["ollama", "larry-dashboard", "nginx", "docker"]


@app.get("/api/logs")
def logs():
    unit = request.args.get("unit", "ollama")
    if unit not in LOG_UNITS:
        return "unknown unit", 400
    _, out = run(["doas", "journalctl", "-u", unit, "-n", "250", "--no-pager"], timeout=30)
    return Response(out or "(empty)", mimetype="text/plain")


# ─── Nomad stack (ssh root@nomad — needs Larry's key on nomad) ──────────────
NOMAD_CONTAINERS = ["flatnotes", "kolibri", "kiwix", "cyberchef"]


def nomad_ssh(cmd, timeout=30):
    # cmd is ONE remote-shell command string (ssh joins args → the remote shell
    # would otherwise treat docker --format '|' as pipes).
    return run(["ssh", "-o", "BatchMode=yes", "-o", "ConnectTimeout=6", "root@nomad", cmd], timeout)


@app.get("/api/nomad/status")
def nomad_status():
    ok, out = nomad_ssh("docker ps -a --format '{{.Names}} | {{.Status}} | {{.Image}}'")
    return jsonify(ok=ok, out=out)


@app.post("/api/nomad/restart")
def nomad_restart():
    c = (request.json or {}).get("container", "")
    if c not in NOMAD_CONTAINERS:
        return jsonify(ok=False, out="unknown container"), 400
    ok, out = nomad_ssh(f"docker restart {c}")
    return jsonify(ok=ok, out=out or f"restarted {c}")


# ─── Builds (ssh the build box — needs Larry's key on it) ───────────────────
BUILD_BOX = os.environ.get("BUILD_BOX", "deb")


# Curated per-run build params exposed on the Builds card. Each maps a client field
# to (ENV_NAME, allowed-values, default). Server validates against the allow-list —
# never trust the client — then prepends KEY=val to the remote command. The default
# value is omitted from the command so unchanged runs stay identical to before.
BUILD_PARAMS = {
    "backend":   ("CODER_BACKEND",   {"pi", "claude", "claude-code"},                         "pi"),
    "model":     ("PI_CODER_MODEL",  {"ollama/qwen3-coder:30b", "ollama/al-coder-qwen3",
                                      "ollama/al-coder-qwen36", "ollama/al-coder-north-mini",
                                      "ollama/north-mini-code-1.0"},              "ollama/qwen3-coder:30b"),
    "strategy":  ("FIX_STRATEGY",    {"auto", "rewrite", "snippet"},                         "auto"),
    "workflow":  ("WORKFLOW",        {"single", "decomposed"},                             "single"),
    "verbatim":  ("VERBATIM_WRITE",  {"0", "1"},                                              "0"),
    "recover":   ("RECOVER_MISSING", {"0", "1"},                                              "1"),
    "escalate":  ("ESCALATE_AFTER",  {"", "1", "2", "3"},                                      ""),
    "maxfix":    ("MAX_FIX_ROUNDS",  {"4", "6", "8", "12"},                                   "8"),
    # --- Advanced (behind the expander); same allow-list mechanism, defaults match run-build.py ---
    "midescalate": ("ESCALATE_MID_AFTER", {"", "1", "2", "3"},                                 ""),
    # Which cheap-cloud model the mid rung uses. Allow-listed like everything else so a
    # dashboard POST can never inject an arbitrary model string. kimi-k2 is the default:
    # 9 runs / 3 fixtures with zero regressions, where both DeepSeek variants took a
    # nearly-passing build backwards (reference/bench-results/mid-tier-evaluation.md).
    "midmodel":  ("MID_MODEL", {"openrouter/moonshotai/kimi-k2",
                                "openrouter/moonshotai/kimi-k3",
                                "openrouter/moonshotai/kimi-k2.7-code",
                                "openrouter/deepseek/deepseek-chat",
                                "openrouter/deepseek/deepseek-v4-flash-0731",
                                "openrouter/z-ai/glm-4.6"},
                  "openrouter/moonshotai/kimi-k2"),
    "injecttopics":("INJECT_TOPICS",      {"auto", "off"},                                 "auto"),
    "injectbudget":("INJECT_BUDGET_K",    {"8", "14", "20", "28"},                          "14"),
    "raginject":   ("RAG_INJECT",         {"0", "1"},                                        "1"),
    "raghits":     ("RAG_HITS",           {"1", "2", "3", "4"},                              "2"),
    "ragfallback": ("RAG_KB_FALLBACK",    {"0", "1"},                                        "0"),
    "numctx":      ("CODER_NUM_CTX",      {"16384", "32768", "65536"},                   "32768"),
    "maxrecovery": ("MAX_RECOVERY_ROUNDS",{"1", "2", "3"},                                   "2"),
    "pitrim":      ("PI_TRIM",            {"0", "1"},                                        "1"),
    "revfix":      ("PI_REVIEW_FIX_ROUNDS",        {"1", "2", "3"},                          "2"),
    "revfixcompile":("PI_REVIEW_FIX_COMPILE_ROUNDS",{"2", "3", "4"},                         "3"),
}
BUILD_REVIEW = {"none", "coms", "claude"}


@app.post("/api/job/build")
def job_build():
    d = request.json or {}
    tool = d.get("tool", "")
    proj = d.get("project", "").strip()
    if tool not in ("alw", "gow", "csw") or not re.match(r"^[\w./-]+$", proj):
        return jsonify(ok=False, out="bad tool/project"), 400
    # collect validated env overrides (skip defaults so an untouched card == old behaviour)
    env = []
    for field, (name, allowed, default) in BUILD_PARAMS.items():
        val = str(d.get(field, default))
        if val not in allowed:
            return jsonify(ok=False, out=f"bad {field}"), 400
        if val != default and val != "":
            env.append(f"{name}={val}")
    # review: none | coms | claude → --review flag (+ REVIEW_BACKEND=claude for the stronger reviewer)
    review = d.get("review", "none")
    if review not in BUILD_REVIEW:
        return jsonify(ok=False, out="bad review"), 400
    review_flag = " --review" if review in ("coms", "claude") else ""
    if review == "claude":
        env.append("REVIEW_BACKEND=claude")
    prefix = (" ".join(env) + " ") if env else ""
    # one remote string; login shell for PATH (~/.local/bin). proj is validated
    # (^[\w./-]+$) and every env value is allow-listed, so all safe inside the quotes.
    remote = f"bash -lc '{prefix}{tool} build {proj}{review_flag}'"
    jid = uuid.uuid4().hex[:8]
    lbl = f"{tool} {proj}" + (f" [{review}]" if review_flag else "") + (f" ({len(env)} opts)" if env else "")
    bg(jid, ["ssh", "-o", "BatchMode=yes", "-o", "ConnectTimeout=6", BUILD_BOX, remote],
       kind="build", label=lbl)
    return jsonify(job=jid)


@app.get("/api/build/jobs")
def build_jobs():
    """Recent build bg-jobs (running first)."""
    js = [{"id": jid, "status": v["status"], "label": v.get("label") or jid}
          for jid, v in _jobs.items() if v.get("kind") == "build"]
    js.sort(key=lambda j: j["status"] != "running")
    return jsonify(jobs=js)


# ─── bclinux (ssh the bcl box=deb → bcl → Nemesis VM101) ────────────────────
# bcl runs on deb and reaches the docker host + KVM guests over ssh. Same chain
# as Builds. status/ports/reprovision/rm are ssh-only; `new` needs BCL_SQL_PASSWORD,
# sourced from a deb-side creds file (~/.config/bclinux/env, chmod 600).
BCL_BOX = os.environ.get("BCL_BOX", "deb")
BCL_NAME_RE = re.compile(r"^[\w-]+$")
BCL_VER_RE = re.compile(r"^[\d.]+$")
_PORT_LABELS = ("web", "dev", "odata", "soap", "mgmt", "ssh", "rdp", "viewer")


def bcl_ssh(remote_cmd, timeout=30):
    # remote_cmd is ONE shell string; login shell so ~/.local/bin (bcl) is on PATH.
    return run(["ssh", "-o", "BatchMode=yes", "-o", "ConnectTimeout=6", BCL_BOX,
                f"bash -lc {shlex.quote(remote_cmd)}"], timeout)


def bcl_env_names():
    """Env names from `bcl ports` (source of truth for validating name args)."""
    ok, out = bcl_ssh("bcl ports")
    names = []
    if ok:
        for ln in out.splitlines():
            tok = ln.split()
            if tok:
                names.append(tok[0])
    return names, out


@app.get("/api/bclinux/status")
def bcl_status():
    ok, raw = bcl_ssh("bcl ports")
    if not ok:
        return jsonify(ok=False, out=raw, envs=[])
    envs = []
    for ln in raw.splitlines():
        tok = ln.split()
        if not tok:
            continue
        name = tok[0]
        e = {"name": name, "slot": None}
        m = re.search(r"slot\s+(\d+)", ln)
        if m:
            e["slot"] = m.group(1)
        # tokens look like  web http://…:14080   dev :14049 …
        for lbl in _PORT_LABELS:
            pm = re.search(rf"\b{lbl}\s+\S*?:(\d+)", ln)
            if pm:
                e[lbl] = pm.group(1)
        # Per-env readiness + uptime. NOTE: bcl's status.txt is a SHARED file
        # (~/bclinux/artifacts/status.txt, one across all guests), so it can't tell
        # envs apart. Probe each env's OWN web port instead — that's the real signal.
        # Uptime still comes from the (per-env) docker container status line.
        if BCL_NAME_RE.match(name) and e.get("web"):
            web = e["web"]
            probe = (f"code=$(curl -s -m4 -o /dev/null -w '%{{http_code}}' "
                     f"http://lxdocker-bc:{web}/BC?tenant=default); "
                     f"up=$(bcl status -name {name} 2>/dev/null | grep '^Up ' | head -1); "
                     f'echo "$code|$up"')
            pok, pout = bcl_ssh(probe, timeout=20)
            code, _, up = pout.strip().partition("|")
            e["uptime"] = up.strip()
            e["http"] = code.strip()
            if code.strip() and code.strip()[0] in ("2", "3") or code.strip() in ("401", "403"):
                e["ready"] = "ready"
            elif e["uptime"]:
                e["ready"] = "starting"
            else:
                e["ready"] = "down"
        envs.append(e)
    return jsonify(ok=True, envs=envs, raw=raw)


@app.post("/api/bclinux/reprovision")
def bcl_reprovision():
    name = (request.json or {}).get("name", "")
    names, _ = bcl_env_names()
    if name not in names:
        return jsonify(ok=False, out="unknown env"), 400
    jid = uuid.uuid4().hex[:8]
    bg(jid, ["ssh", "-o", "BatchMode=yes", "-o", "ConnectTimeout=6", BCL_BOX,
             f"bash -lc {shlex.quote(f'bcl reprovision -name {name}')}"],
       kind="bcl", label=f"reprovision {name}")
    return jsonify(job=jid)


@app.post("/api/bclinux/rm")
def bcl_rm():
    name = (request.json or {}).get("name", "")
    names, _ = bcl_env_names()
    if name not in names:
        return jsonify(ok=False, out="unknown env"), 400
    ok, out = bcl_ssh(f"bcl rm -name {name}", timeout=120)
    return jsonify(ok=ok, out=out or f"removed {name}")


@app.post("/api/bclinux/new")
def bcl_new():
    d = request.json or {}
    name, version = d.get("name", ""), d.get("version", "")
    typ = d.get("type", "onprem")
    if not BCL_NAME_RE.match(name) or not BCL_VER_RE.match(version):
        return jsonify(ok=False, out="bad name/version"), 400
    if typ not in ("onprem", "sandbox"):
        return jsonify(ok=False, out="bad type"), 400
    jid = uuid.uuid4().hex[:8]
    remote = f"set -a; . ~/.config/bclinux/env; bcl new -name {name} -type {typ} -version {version}"
    bg(jid, ["ssh", "-o", "BatchMode=yes", "-o", "ConnectTimeout=6", BCL_BOX,
             f"bash -lc {shlex.quote(remote)}"],
       kind="bcl", label=f"new {name} ({typ} {version})")
    return jsonify(job=jid)


@app.get("/api/bclinux/jobs")
def bcl_jobs():
    """Recent bclinux bg-jobs (running first), newest last-inserted first."""
    js = [{"id": jid, "status": v["status"], "label": v.get("label") or jid}
          for jid, v in _jobs.items() if v.get("kind") == "bcl"]
    js.sort(key=lambda j: j["status"] != "running")  # running on top
    return jsonify(jobs=js)


# ─── vendored assets (mermaid) ─────────────────────────────────────────────
@app.get("/vendor/mermaid.min.js")
def vendor_mermaid():
    p = os.path.join(BASE, "vendor", "mermaid.min.js")
    if not os.path.exists(p):
        return "mermaid not deployed", 404
    return Response(open(p, encoding="utf-8").read(),
                    mimetype="application/javascript",
                    headers={"Cache-Control": "max-age=86400"})


# ─── UI ────────────────────────────────────────────────────────────────────
@app.get("/")
def index():
    return Response(PAGE, mimetype="text/html")


PAGE = r"""<!doctype html><html><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Larry Maintenance</title>
<style>
:root{--bg:#0f1115;--panel:#181b22;--fg:#d7dbe0;--acc:#00d787;--dim:#6b7280;--warn:#e5c07b;--bd:#262b36;--bd2:#39404e;--code:#10141b;--btn:#222835}
:root[data-theme="light"]{--bg:#eef1f5;--panel:#ffffff;--fg:#1c2027;--acc:#0a7d4b;--dim:#5b6472;--warn:#9a6a00;--bd:#d4d9e0;--bd2:#c3cad4;--code:#f3f5f8;--btn:#eef1f5}
*{box-sizing:border-box}body{margin:0;font:14px/1.5 system-ui,sans-serif;background:var(--bg);color:var(--fg)}
header{background:var(--panel);padding:12px 18px;font-weight:600;border-bottom:1px solid var(--bd)}
header b{color:var(--acc)}
nav{display:flex;gap:4px;padding:8px 12px;background:var(--panel);border-bottom:1px solid var(--bd)}
nav button{background:transparent;color:var(--fg);border:1px solid var(--bd);padding:6px 14px;border-radius:6px;cursor:pointer}
nav button.on{background:var(--acc);color:#062;border-color:var(--acc);font-weight:600}
main{padding:18px;max-width:1000px;margin:0 auto}
.card{background:var(--panel);border:1px solid var(--bd);border-radius:8px;padding:14px;margin-bottom:14px}
h2{margin:.2em 0 .6em;font-size:15px;color:var(--acc)}
button.act{background:var(--btn);color:var(--fg);border:1px solid var(--bd2);border-radius:6px;padding:7px 12px;cursor:pointer;margin:2px}
button.act:hover{border-color:var(--acc)}
button.danger:hover{border-color:#e06c75}
pre{background:var(--code);border:1px solid var(--bd);border-radius:6px;padding:10px;overflow:auto;max-height:340px;white-space:pre-wrap}
input,select{background:var(--code);color:var(--fg);border:1px solid var(--bd2);border-radius:6px;padding:6px}
.md{background:var(--panel);border:1px solid var(--bd);border-radius:8px;padding:18px}
.md pre{max-height:none}.md table{border-collapse:collapse}.md td,.md th{border:1px solid var(--bd);padding:4px 8px}
.md code{background:var(--code);padding:1px 4px;border-radius:4px}
.row{display:flex;gap:8px;align-items:center;flex-wrap:wrap}
.bgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:10px;margin-top:12px}
.bgrid label{display:flex;flex-direction:column;gap:4px;font-size:12px;color:var(--dim)}
.bgrid select{width:100%}
.adv{margin-top:12px} .adv>summary{cursor:pointer;color:var(--dim);font-size:13px;user-select:none}
.adv[open]>summary{color:var(--fg)}
.dim{color:var(--dim)} .spin{color:var(--warn)}
</style></head><body>
<header style="display:flex;justify-content:space-between;align-items:center">
  <span>🦫 <b>Larry</b> Maintenance</span>
  <button class="act" id="themebtn" onclick="toggleTheme()" title="Toggle light/dark">🌙</button></header>
<nav>
  <button class="on" onclick="tab('maint',this)">Maintenance</button>
  <button onclick="tab('builds',this)">Builds</button>
  <button onclick="tab('bcl',this)">BC Linux</button>
  <button onclick="tab('nomad',this)">Nomad</button>
  <button onclick="tab('chat',this)">Chat</button>
  <button onclick="tab('logs',this)">Logs</button>
  <button onclick="tab('al',this)">AL Knowledge</button>
  <button onclick="tab('docs',this)">Docs</button>
</nav>
<main>
 <section id="maint">
   <div class="card"><h2>Status</h2><div class="row"><button class="act" onclick="loadStatus()">↻ Refresh</button><span id="ver" class="dim"></span></div>
     <pre id="ps">loading…</pre><pre id="ls"></pre><pre id="disk"></pre></div>
   <div class="card"><h2>Ollama</h2>
     <button class="act" onclick="job('update-ollama',{},'Updating ollama…')">⬆ Update ollama</button>
     <button class="act" onclick="post('/api/action/restart-ollama','Restart ollama')">⟳ Restart ollama</button>
     <div class="row" style="margin-top:8px"><input id="pullm" placeholder="model:tag to pull"><button class="act" onclick="pull()">⬇ Pull model</button></div>
     <div class="row" style="margin-top:8px"><select id="rmm"></select><button class="act danger" onclick="rmModel()">🗑 Remove model</button></div>
   </div>
   <div class="card"><h2>KB hybrid-search</h2>
     <div class="row"><button class="act" onclick="loadKb()">↻ Refresh</button>
       <span id="kbstate" class="dim">…</span></div>
     <pre id="kbstats" style="max-height:220px;margin-top:8px">loading…</pre>
     <div class="row" style="margin-top:8px">
       <button class="act" onclick="post('/api/action/restart-kb-serve','Restart kb-serve')">⟳ Restart serve</button>
       <button class="act" onclick="job('kb-reindex',{},'kb reindex (idempotent)…')">⟳ Reindex now</button></div>
     <p class="dim">Store: Larry local disk (WAL), served :8848. Reindex is idempotent + WAL-safe with the live serve.</p></div>
   <div class="card"><h2>Nginx</h2><button class="act" onclick="post('/api/action/reload-nginx','Reload nginx')">⟳ Reload nginx</button></div>
   <div class="card"><h2>Bonsai chat (Mode B)</h2>
     <button class="act" onclick="post('/api/action/bonsai-on','Bonsai ON (evicts coder, ~18s to load)')">▶ Bonsai ON</button>
     <button class="act danger" onclick="post('/api/action/bonsai-off','Bonsai OFF (free VRAM for coder)')">■ Bonsai OFF</button></div>
   <div class="card"><h2>Output</h2><pre id="out">—</pre></div>
 </section>
 <section id="builds" hidden>
   <div class="card"><h2>Run a build (on the build box)</h2>
     <div class="row">
       <select id="btool"><option value="alw">alw (AL)</option><option value="gow">gow (Go)</option><option value="csw">csw (C#)</option></select>
       <input id="bproj" placeholder="project name or path" style="flex:1;min-width:200px">
       <button class="act" onclick="runBuild()">▶ Build</button>
     </div>
     <div class="bgrid">
       <label>Coder backend<select id="bbackend">
         <option value="pi">pi (Larry, local)</option><option value="claude">claude</option><option value="claude-code">claude-code</option></select></label>
       <label>AL model<select id="bmodel">
         <option value="ollama/qwen3-coder:30b">qwen3-coder:30b</option>
         <option value="ollama/al-coder-qwen3">al-coder-qwen3</option>
         <option value="ollama/al-coder-qwen36">al-coder-qwen36</option>
         <option value="ollama/al-coder-north-mini">al-coder-north-mini</option>
         <option value="ollama/north-mini-code-1.0">north-mini-code-1.0</option></select></label>
       <label>Fix strategy<select id="bstrategy">
         <option value="auto">auto</option><option value="rewrite">rewrite</option><option value="snippet">snippet</option></select></label>
       <label>Workflow<select id="bworkflow">
         <option value="single">single</option><option value="decomposed">decomposed</option></select></label>
       <label>Verbatim write<select id="bverbatim">
         <option value="0">off</option><option value="1">on</option></select></label>
       <label>Recover missing<select id="brecover">
         <option value="1">on</option><option value="0">off</option></select></label>
       <label>Review<select id="breview">
         <option value="none">off</option><option value="coms">coms (peer)</option><option value="claude">claude (stronger)</option></select></label>
       <label>Escalate after<select id="bescalate">
         <option value="">manual</option><option value="1">1</option><option value="2">2</option><option value="3">3</option></select></label>
       <label>Max fix rounds<select id="bmaxfix">
         <option value="8">8</option><option value="4">4</option><option value="6">6</option><option value="12">12</option></select></label>
     </div>
     <details class="adv"><summary>Advanced</summary>
     <div class="bgrid">
       <label>Escalate mid after<select id="bmidescalate">
         <option value="">off</option><option value="1">1</option><option value="2">2</option><option value="3">3</option></select></label>
       <label>Mid model<select id="bmidmodel">
         <option value="openrouter/moonshotai/kimi-k2">kimi-k2 (0 regressions/9 runs)</option>
         <option value="openrouter/moonshotai/kimi-k3">kimi-k3 (untested)</option>
         <option value="openrouter/moonshotai/kimi-k2.7-code">kimi-k2.7-code (untested)</option>
         <option value="openrouter/z-ai/glm-4.6">glm-4.6 (untested)</option>
         <option value="openrouter/deepseek/deepseek-v4-flash-0731">deepseek-v4-flash (regressed 1/3)</option>
         <option value="openrouter/deepseek/deepseek-chat">deepseek-chat (regressed, slowest)</option></select></label>
       <label>Inject topics<select id="binjecttopics">
         <option value="auto">auto</option><option value="off">off</option></select></label>
       <label>Inject budget (k)<select id="binjectbudget">
         <option value="14">14</option><option value="8">8</option><option value="20">20</option><option value="28">28</option></select></label>
       <label>RAG inject<select id="braginject">
         <option value="1">on</option><option value="0">off</option></select></label>
       <label>RAG hits<select id="braghits">
         <option value="2">2</option><option value="1">1</option><option value="3">3</option><option value="4">4</option></select></label>
       <label>RAG kb fallback<select id="bragfallback">
         <option value="0">off</option><option value="1">on</option></select></label>
       <label>Coder num_ctx<select id="bnumctx">
         <option value="32768">32768</option><option value="16384">16384</option><option value="65536">65536</option></select></label>
       <label>Max recovery rounds<select id="bmaxrecovery">
         <option value="2">2</option><option value="1">1</option><option value="3">3</option></select></label>
       <label>pi trim<select id="bpitrim">
         <option value="1">on</option><option value="0">off</option></select></label>
       <label>Review fix rounds<select id="brevfix">
         <option value="2">2</option><option value="1">1</option><option value="3">3</option></select></label>
       <label>Review fix (compile)<select id="brevfixcompile">
         <option value="3">3</option><option value="2">2</option><option value="4">4</option></select></label>
     </div>
     <p class="dim">Mid-tier model (<code>MID_MODEL</code>) and bin/URL/timeout paths stay in the build box's env/profile — not per-run choices.</p>
     </details>
     <p class="dim">Runs <code>&lt;env&gt; &lt;tool&gt; build &lt;project&gt; [--review]</code> over SSH on the build box. Defaults match a plain build; changed knobs are passed as env overrides. Output streams below.</p>
   </div>
   <div class="card"><h2>Builds</h2>
     <div class="row"><button class="act" onclick="loadBuildJobs()">↻ Refresh</button>
       <span class="dim">running / recent builds (click to view log)</span></div>
     <div id="buildjobs" style="margin-top:8px" class="dim">none</div></div>
   <div class="card"><h2>Build output</h2><pre id="bout">—</pre></div>
   <div class="card"><h2>Model leaderboard</h2>
     <div class="row"><button class="act" onclick="leaderboard()">🏆 Rebuild leaderboard</button>
       <span class="dim">aggregates per-model metrics from build runs</span></div>
     <pre id="lbout" style="max-height:420px" hidden></pre>
     <div class="dim" id="lbhint" hidden>Open <b>Docs → Build Leaderboard</b> for the rendered table.</div>
   </div>
 </section>
 <section id="bcl" hidden>
   <div class="card"><h2>BC environments (Nemesis VM101)</h2>
     <div class="row"><button class="act" onclick="loadBcl()">↻ Refresh</button>
       <span class="dim">bcl ports + status over ssh (deb → lxdocker-bc)</span></div>
     <div id="bcltbl" style="margin-top:10px">loading…</div></div>
   <div class="card"><h2>New environment</h2>
     <div class="row">
       <input id="bnname" placeholder="env name (e.g. bctest)">
       <select id="bntype"><option value="onprem">onprem</option><option value="sandbox">sandbox</option></select>
       <input id="bnver" placeholder="version (e.g. 28.3 or 28.3.0.0)" value="28.3" style="width:190px">
       <button class="act" onclick="bclNew()">▶ Create</button>
     </div>
     <p class="dim">Version resolves to the closest build and downloads if missing (like bccontainerhelper). Restores db + boots a guest from the golden seed. Long-running; output streams below.</p></div>
   <div class="card"><h2>Jobs</h2>
     <div class="row"><button class="act" onclick="loadBclJobs()">↻ Refresh</button>
       <span class="dim">reprovision / new runs (click to view log)</span></div>
     <div id="bcljobs" style="margin-top:8px" class="dim">none</div></div>
   <div class="card"><h2>Output</h2><pre id="bclout">—</pre></div>
 </section>
 <section id="nomad" hidden>
   <div class="card"><h2>Nomad stack</h2><div class="row"><button class="act" onclick="loadNomad()">↻ Refresh</button></div>
     <pre id="nps">loading…</pre>
     <div class="row" style="margin-top:8px"><select id="nc"><option>flatnotes</option><option>kolibri</option><option>kiwix</option><option>cyberchef</option></select>
       <button class="act" onclick="nomadRestart()">⟳ Restart container</button></div>
     <pre id="nout"></pre></div>
 </section>
 <section id="chat" hidden>
   <div class="card"><h2>Chat with a Larry model</h2>
     <div class="row">
       <select id="chatmodel" style="min-width:220px"></select>
       <input id="chatsys" placeholder="optional system prompt" style="flex:1;min-width:200px">
       <button class="act" onclick="chatClear()">🗑 Clear</button>
       <span id="chatbusy" class="dim"></span>
     </div>
     <div id="chatlog" style="margin-top:10px;max-height:52vh;overflow:auto;display:flex;flex-direction:column;gap:8px"></div>
     <div class="row" style="margin-top:8px">
       <textarea id="chatin" rows="2" placeholder="message… (Enter to send, Shift+Enter = newline)" style="flex:1;resize:vertical"></textarea>
       <button class="act" onclick="chatSend()">▶ Send</button>
     </div>
     <p class="dim">Talks to ollama on Larry (localhost:11434). Loading a model evicts the resident one (VRAM time-share with the coder/Bonsai). History is client-side; Clear resets it.</p>
   </div>
 </section>
 <section id="logs" hidden>
   <div class="card"><div class="row">
     <button class="act" onclick="loadLog('ollama')">ollama</button>
     <button class="act" onclick="loadLog('larry-dashboard')">dashboard</button>
     <button class="act" onclick="loadLog('nginx')">nginx</button>
     <button class="act" onclick="loadLog('docker')">docker</button>
   </div><pre id="logbody" style="max-height:520px">pick a service…</pre></div>
 </section>
 <section id="al" hidden>
   <div class="card"><h2>Anonymise an export</h2>
     <div class="row"><input type="file" id="af"><button class="act" onclick="anon()">Anonymise</button><span id="anos" class="dim"></span></div>
     <pre id="ao" hidden></pre></div>
   <div class="card"><h2>BCQuality</h2>
     <div class="row"><button class="act" onclick="harvest()">⬇ Pull BCQuality &amp; harvest new</button>
       <span class="dim">git pull → resync custom layer → reindex → report new/changed rules</span></div>
     <pre id="hout" style="max-height:360px" hidden></pre>
     <div class="dim" id="hhint" hidden>Report saved — open <b>Docs → BCQuality Harvest</b> to review, then fold into AL Reference.</div>
   </div>
   <div class="card"><h2>AL Reference</h2><div class="md" id="alref">loading…</div></div>
 </section>
 <section id="docs" hidden>
   <div class="card"><div class="row" id="doclist"></div></div>
   <div class="md" id="docbody">pick a doc…</div>
 </section>
</main>
<script src="vendor/mermaid.min.js"></script>
<script>
const $=id=>document.getElementById(id);
function tab(id,btn){for(const s of ['maint','builds','bcl','nomad','chat','logs','al','docs'])$(s).hidden=(s!==id);
 for(const b of document.querySelectorAll('nav button'))b.classList.toggle('on',b===btn);
 if(id==='al')loadRef(); if(id==='docs')loadDocs(); if(id==='nomad')loadNomad(); if(id==='bcl')loadBcl(); if(id==='builds')loadBuildJobs();}
async function runBuild(){const p=$('bproj').value.trim();if(!p)return;
 const body={tool:$('btool').value,project:p,review:$('breview').value,
   backend:$('bbackend').value,model:$('bmodel').value,strategy:$('bstrategy').value,
   workflow:$('bworkflow').value,verbatim:$('bverbatim').value,recover:$('brecover').value,
   escalate:$('bescalate').value,maxfix:$('bmaxfix').value,
   midescalate:$('bmidescalate').value,midmodel:$('bmidmodel').value,injecttopics:$('binjecttopics').value,
   injectbudget:$('binjectbudget').value,raginject:$('braginject').value,raghits:$('braghits').value,
   ragfallback:$('bragfallback').value,numctx:$('bnumctx').value,maxrecovery:$('bmaxrecovery').value,
   pitrim:$('bpitrim').value,revfix:$('brevfix').value,revfixcompile:$('brevfixcompile').value};
 $('bout').textContent='starting build…';
 const r=await fetch('api/job/build',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)});
 const d=await r.json();if(!d.job){$('bout').textContent='failed: '+(d.out||'');return;}pollInto(d.job,'bout');loadBuildJobs();}
async function loadBuildJobs(){const d=await (await fetch('api/build/jobs')).json();
 if(!d.jobs.length){$('buildjobs').textContent='none';return;}
 const ic={running:'⏳',done:'🟢',error:'🔴'};
 $('buildjobs').innerHTML=d.jobs.map(j=>
   `<div class="row" style="margin:2px 0"><button class="act" onclick="pollInto('${j.id}','bout')">${ic[j.status]||''} ${j.label}</button><span class="dim">${j.status}</span></div>`).join('');
 if(d.jobs.some(j=>j.status==='running'))setTimeout(loadBuildJobs,3000);}
async function pollInto(jid,el){const r=await fetch('api/job/'+jid);const d=await r.json();
 $(el).textContent=d.log;if(d.status==='running'){$(el).textContent+='\n⏳ running…';setTimeout(()=>pollInto(jid,el),1500);}}
async function loadNomad(){$('nps').textContent='loading…';const d=await (await fetch('api/nomad/status')).json();
 $('nps').textContent=d.ok?d.out:nomadErr(d.out)+'\n'+d.out;}
function bclErr(o){o=(o||'').toLowerCase();
 if(/no route to host|connection timed out|host is down|could not resolve|name or service not known/.test(o))
   return 'ERROR: build box (deb) or VM101 unreachable';
 if(/connection refused/.test(o))return 'ERROR: sshd not answering';
 if(/permission denied|publickey|host key/.test(o))return "ERROR: SSH auth failed — check Larry's key on deb / deb's key on lxdocker-bc";
 if(/command not found/.test(o))return 'ERROR: bcl not on PATH on deb (symlink ~/.local/bin/bcl)';
 return 'ERROR talking to bcl';}
function bclState(e){const r=e.ready||'down';const c=e.http?' ('+e.http+')':'';
 if(r==='ready')return '🟢 ready';
 if(r==='starting')return '🟡 starting'+c;
 return '🔴 down'+c;}
async function loadBcl(){$('bcltbl').textContent='loading…';
 const d=await (await fetch('api/bclinux/status')).json();
 if(!d.ok){$('bcltbl').innerHTML='<pre>'+bclErr(d.out)+'\n'+(d.out||'')+'</pre>';return;}
 if(!d.envs.length){$('bcltbl').textContent='no environments';return;}
 let h='<table style="border-collapse:collapse;width:100%"><tr>'+
   ['env','slot','state','uptime','web','actions'].map(x=>`<th style="text-align:left;border-bottom:1px solid var(--bd);padding:4px 8px">${x}</th>`).join('')+'</tr>';
 for(const e of d.envs){const web=e.web?`<a href="http://lxdocker-bc:${e.web}/BC?tenant=default" target="_blank">:${e.web}</a>`:'';
   h+=`<tr><td style="padding:4px 8px"><b>${e.name}</b></td><td style="padding:4px 8px">${e.slot??''}</td>`+
      `<td style="padding:4px 8px">${bclState(e)}</td><td style="padding:4px 8px" class="dim">${e.uptime||''}</td>`+
      `<td style="padding:4px 8px">${web}</td>`+
      `<td style="padding:4px 8px"><button class="act" onclick="bclRepro('${e.name}')">⟳ Reprovision</button>`+
      `<button class="act danger" onclick="bclRm('${e.name}')">🗑 Remove</button></td></tr>`;}
 $('bcltbl').innerHTML=h+'</table>';loadBclJobs();}
async function loadBclJobs(){const d=await (await fetch('api/bclinux/jobs')).json();
 if(!d.jobs.length){$('bcljobs').textContent='none';return;}
 const ic={running:'⏳',done:'🟢',error:'🔴'};
 $('bcljobs').innerHTML=d.jobs.map(j=>
   `<div class="row" style="margin:2px 0"><button class="act" onclick="pollInto('${j.id}','bclout')">${ic[j.status]||''} ${j.label}</button><span class="dim">${j.status}</span></div>`).join('');
 if(d.jobs.some(j=>j.status==='running'))setTimeout(loadBclJobs,3000);}
async function bclRepro(n){if(!confirm('Reprovision '+n+'? (reruns provisioning in the guest)'))return;
 $('bclout').textContent='reprovisioning '+n+'…';
 const r=await fetch('api/bclinux/reprovision',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({name:n})});
 const d=await r.json();if(!d.job){$('bclout').textContent='failed: '+(d.out||'');return;}pollInto(d.job,'bclout');loadBclJobs();}
async function bclRm(n){if(!confirm('Remove '+n+'? Destroys the guest (db left in place).'))return;
 $('bclout').textContent='removing '+n+'…';
 const r=await fetch('api/bclinux/rm',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({name:n})});
 const d=await r.json();$('bclout').textContent=d.out;loadBcl();}
async function bclNew(){const n=$('bnname').value.trim(),v=$('bnver').value.trim(),t=$('bntype').value;if(!n||!v)return;
 if(!confirm('Create env '+n+' ('+t+' '+v+')?'))return;$('bclout').textContent='creating '+n+'…';
 const r=await fetch('api/bclinux/new',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({name:n,version:v,type:t})});
 const d=await r.json();if(!d.job){$('bclout').textContent='failed: '+(d.out||'');return;}pollInto(d.job,'bclout');loadBclJobs();}
function nomadErr(o){o=(o||'').toLowerCase();
 if(/no route to host|connection timed out|host is down|could not resolve|name or service not known/.test(o))
   return 'ERROR: nomad host unreachable — is the Proxmox guest booted? (autostart is off, so it needs a manual start)';
 if(/connection refused/.test(o))return 'ERROR: nomad is up but sshd not answering on :22 — check the ssh service on nomad';
 if(/permission denied|publickey|host key/.test(o))return "ERROR: SSH auth to root@nomad failed — check Larry's key in nomad's authorized_keys";
 return 'ERROR talking to nomad';}
async function nomadRestart(){const c=$('nc').value;if(!confirm('Restart '+c+'?'))return;$('nout').textContent='restarting '+c+'…';
 const r=await fetch('api/nomad/restart',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({container:c})});
 const d=await r.json();$('nout').textContent=d.out;loadNomad();}
async function loadLog(u){$('logbody').textContent='loading '+u+'…';$('logbody').textContent=await (await fetch('api/logs?unit='+u)).text();}
function setOut(t){$('out').textContent=t;}
async function loadStatus(){const r=await fetch('api/status');const d=await r.json();
 $('ver').textContent=d.version;$('ps').textContent=d.ps;$('ls').textContent=d.ls;$('disk').textContent=d.disk;
 $('rmm').innerHTML=d.models.map(m=>`<option>${m}</option>`).join('');
 const cm=$('chatmodel');if(cm){const cur=cm.value;cm.innerHTML=d.models.map(m=>`<option>${m}</option>`).join('');if(cur)cm.value=cur;}}
let _chat=[];
function chatClear(){_chat=[];$('chatlog').innerHTML='';}
function chatAdd(role,text){const b=document.createElement('div');
 b.style.cssText='padding:8px 10px;border-radius:8px;max-width:90%;white-space:pre-wrap;'+
  (role==='user'?'align-self:flex-end;background:var(--acc);color:#062':'align-self:flex-start;background:var(--panel);border:1px solid var(--bd)');
 b.textContent=text;$('chatlog').appendChild(b);$('chatlog').scrollTop=$('chatlog').scrollHeight;return b;}
async function chatSend(){const inp=$('chatin');const text=inp.value.trim();if(!text)return;
 const model=$('chatmodel').value;if(!model){$('chatbusy').textContent='pick a model';return;}
 inp.value='';chatAdd('user',text);_chat.push({role:'user',content:text});
 const msgs=[];const sys=$('chatsys').value.trim();if(sys)msgs.push({role:'system',content:sys});
 msgs.push(..._chat);
 $('chatbusy').textContent='… thinking';const ph=chatAdd('assistant','…');
 try{const r=await fetch('api/chat',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({model,messages:msgs})});
  const d=await r.json();
  if(d.ok){ph.textContent=d.reply;_chat.push({role:'assistant',content:d.reply});}
  else{ph.textContent='⚠ '+(d.out||'error');}
 }catch(e){ph.textContent='⚠ '+e;}
 $('chatbusy').textContent='';}
document.addEventListener('keydown',e=>{if(e.target&&e.target.id==='chatin'&&e.key==='Enter'&&!e.shiftKey){e.preventDefault();chatSend();}});
async function post(u,label){setOut(label+' …');const r=await fetch(u,{method:'POST'});const d=await r.json();
 setOut(label+': '+(d.ok?'OK':'FAILED')+'\n'+d.out);loadStatus();}
async function loadKb(){$('kbstate').textContent='checking…';
 try{const d=await (await fetch('api/kb')).json();
  $('kbstate').innerHTML=d.up?'🟢 serve up':'🔴 serve down';
  let s=d.stats;try{const j=JSON.parse(d.stats);s=Array.isArray(j)?j.map(r=>`${r[0].padEnd(18)} ${r[1]} chunks / ${r[2]} files`).join('\n'):JSON.stringify(j,null,1);}catch(e){}
  $('kbstats').textContent=s;
 }catch(e){$('kbstate').textContent='🔴 unreachable';$('kbstats').textContent=String(e);}}
async function pull(){const m=$('pullm').value.trim();if(!m)return;job('pull',{model:m},'Pulling '+m+'…');}
async function rmModel(){const m=$('rmm').value;if(!m||!confirm('Remove '+m+'?'))return;
 setOut('Removing '+m+' …');const r=await fetch('api/model/rm',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({model:m})});
 const d=await r.json();setOut(d.out);loadStatus();}
async function job(name,body,label){setOut(label);
 const r=await fetch('api/job/'+name,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)});
 const d=await r.json();if(!d.job){setOut('failed: '+(d.out||''));return;}poll(d.job);}
async function poll(jid){const r=await fetch('api/job/'+jid);const d=await r.json();
 $('out').textContent=d.log;if(d.status==='running'){$('out').textContent+='\n⏳ running…';setTimeout(()=>poll(jid),1500);}else{loadStatus();}}
async function anon(){const f=$('af').files[0];if(!f)return;$('anos').textContent='working…';
 const fd=new FormData();fd.append('file',f);const r=await fetch('api/al/anonymise',{method:'POST',body:fd});const d=await r.json();
 $('anos').textContent=d.ok?'done':'error';$('ao').hidden=false;$('ao').textContent=(d.out||'')+'\n\n'+(d.clean||'').slice(0,4000);}
async function harvest(){$('hout').hidden=false;$('hhint').hidden=true;$('hout').textContent='starting harvest…';
 const r=await fetch('api/job/harvest-bcquality',{method:'POST',headers:{'Content-Type':'application/json'},body:'{}'});
 const d=await r.json();if(!d.job){$('hout').textContent='failed: '+(d.out||'');return;}harvestPoll(d.job);}
async function harvestPoll(jid){const r=await fetch('api/job/'+jid);const d=await r.json();
 $('hout').textContent=d.log;if(d.status==='running'){$('hout').textContent+='\n⏳ running…';setTimeout(()=>harvestPoll(jid),1500);}
 else{$('hhint').hidden=false;}}
async function leaderboard(){$('lbout').hidden=false;$('lbhint').hidden=true;$('lbout').textContent='aggregating…';
 const r=await fetch('api/job/leaderboard',{method:'POST',headers:{'Content-Type':'application/json'},body:'{}'});
 const d=await r.json();if(!d.job){$('lbout').textContent='failed: '+(d.out||'');return;}lbPoll(d.job);}
async function lbPoll(jid){const r=await fetch('api/job/'+jid);const d=await r.json();
 $('lbout').textContent=d.log;if(d.status==='running'){$('lbout').textContent+='\n⏳ running…';setTimeout(()=>lbPoll(jid),1200);}
 else{$('lbhint').hidden=false;}}
let _mermaidReady=false;
function mermaidInit(){if(_mermaidReady||!window.mermaid)return;
 const dark=document.documentElement.getAttribute('data-theme')!=='light';
 mermaid.initialize({startOnLoad:false,securityLevel:'strict',theme:dark?'dark':'default'});_mermaidReady=true;}
async function renderMermaid(el){if(!window.mermaid){return;}mermaidInit();
 // python-markdown emits <pre><code class="language-mermaid">…</code></pre>
 const blocks=el.querySelectorAll('code.language-mermaid, code.mermaid');const nodes=[];
 blocks.forEach((c,i)=>{const pre=c.closest('pre')||c;const d=document.createElement('pre');
   d.className='mermaid';d.textContent=c.textContent;pre.replaceWith(d);nodes.push(d);});
 if(nodes.length){try{await mermaid.run({nodes});}catch(e){console.error('mermaid',e);}}}
async function loadRef(){$('alref').innerHTML=await (await fetch('api/doc?f=AL Reference')).text();renderMermaid($('alref'));}
async function loadDocs(){const names=await (await fetch('api/docs')).json();
 $('doclist').innerHTML=names.map(n=>`<button class="act" onclick="showDoc('${n.replace(/'/g,"")}')">${n}</button>`).join('');}
async function showDoc(n){$('docbody').innerHTML=await (await fetch('api/doc?f='+encodeURIComponent(n))).text();renderMermaid($('docbody'));}
function applyTheme(t){document.documentElement.setAttribute('data-theme',t);localStorage.setItem('theme',t);$('themebtn').textContent=(t==='light'?'☀':'🌙');}
function toggleTheme(){applyTheme(document.documentElement.getAttribute('data-theme')==='light'?'dark':'light');}
applyTheme(localStorage.getItem('theme')||'dark');
loadStatus();
loadKb();
</script></body></html>"""

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=PORT)
