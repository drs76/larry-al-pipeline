#!/usr/bin/env python3
"""board.py — Kanban lifecycle board for the prototype→build→promote flow.

Drives a self-hosted Kanboard (nomad) over JSON-RPC + (on promote) github via `gh`,
egress-gated by egress_policy. Local-first: everything works on the local board; the
github mirror only fires on promote when egress_policy.allowed("github") permits.

Design + rationale: setup/pipeline/scout/kanban-lifecycle/ ; build plan:
setup/pipeline/war-plans/kanban-board/. stdlib only (urllib/json/subprocess).

Verbs (this file grows move by move — see the warplan):
  board project <proto-path>                 create/adopt the board (columns, doc cards, overview)  [Move 3]
  board rfc <proto-path> "<desc>"            mint an RFC card, print its id                          [Move 4]
  board link <proto-path> <sha>             attach a commit external link                           [Move 4]
  board install-hook <proto-path>           drop the post-commit hook                               [Move 4]
  board promote <proto-path>                github mirror (egress-gated) + move overview card       [Move 6]
  board sync <proto-path>                   idempotent reconcile                                     [Move 7]

Config: ~/.config/board/env (KANBOARD_URL, KANBOARD_USER=jsonrpc, KANBOARD_TOKEN), chmod 600.
Env: BOARD_DRY_RUN=1 records intended calls without executing (offline test, Move 8).
"""
import base64
import json
import os
import sys
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import egress_policy   # noqa: E402  (same-dir sibling; the github egress gate)

CONFIG = os.path.expanduser(os.environ.get("BOARD_ENV", "~/.config/board/env"))
DRY_RUN = os.environ.get("BOARD_DRY_RUN") == "1"
OVERVIEW = "Prototypes"                       # the estate overview board
COLUMNS = ["Backlog", "Planning", "Building", "Review", "Promoted", "Done"]
# planning artefacts seeded as Doc cards at `new` (only those that exist)
DOC_ARTEFACTS = [
    "larry-handover.prompt.md", "docs/SPEC.md", "docs/TASKS.md",
    "war-plans", "scout",       # dirs → each *.md inside becomes a doc card
]


class BoardError(Exception):
    pass


# ─── config ────────────────────────────────────────────────────────────────
def load_cfg():
    cfg = {}
    try:
        with open(CONFIG) as f:
            for ln in f:
                ln = ln.strip()
                if ln and not ln.startswith("#") and "=" in ln:
                    k, v = ln.split("=", 1)
                    cfg[k.strip()] = v.strip()
    except OSError as e:
        raise BoardError(f"no board config at {CONFIG} ({e}); the board is unconfigured")
    for k in ("KANBOARD_URL", "KANBOARD_TOKEN"):
        if not cfg.get(k):
            raise BoardError(f"{k} missing from {CONFIG}")
    cfg.setdefault("KANBOARD_USER", "jsonrpc")
    return cfg


# ─── JSON-RPC client ─────────────────────────────────────────────────────────
_id = 0


def rpc(cfg, method, **params):
    """One JSON-RPC call. Returns result, raises BoardError on transport/API error."""
    global _id
    _id += 1
    if DRY_RUN:
        print(f"  [dry-run] {method}({json.dumps(params, sort_keys=True)})")
        # Return method-appropriate fakes so the id-dependent flow can be walked offline.
        if method.startswith("getAll") or method == "getColumns":
            return []
        if method.startswith("create") or method.startswith("add"):
            return _id                      # a fake but unique id
        return True
    body = json.dumps({"jsonrpc": "2.0", "method": method, "id": _id,
                       "params": params or {}}).encode()
    auth = base64.b64encode(f"{cfg['KANBOARD_USER']}:{cfg['KANBOARD_TOKEN']}".encode()).decode()
    req = urllib.request.Request(cfg["KANBOARD_URL"], data=body, headers={
        "Content-Type": "application/json", "Authorization": f"Basic {auth}"})
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            payload = json.loads(r.read().decode())
    except Exception as e:
        raise BoardError(f"kanboard unreachable ({method}): {e}")
    if "error" in payload:
        raise BoardError(f"kanboard API error ({method}): {payload['error']}")
    return payload.get("result")


# ─── .board marker (per-prototype state) ─────────────────────────────────────
def marker_path(proto):
    return os.path.join(proto, ".board")


def read_marker(proto):
    try:
        with open(marker_path(proto)) as f:
            return json.load(f)
    except (OSError, ValueError):
        return {}


def write_marker(proto, data):
    if DRY_RUN:
        print(f"  [dry-run] write .board {json.dumps(data, sort_keys=True)}")
        return
    with open(marker_path(proto), "w") as f:
        json.dump(data, f, indent=2)
        f.write("\n")


# ─── project helpers ─────────────────────────────────────────────────────────
def find_project(cfg, name):
    """Return the project dict for `name`, or None. Adopt-by-name recovery path."""
    for p in (rpc(cfg, "getAllProjects") or []):
        if p.get("name") == name:
            return p
    return None


def ensure_project(cfg, name):
    """Create-or-adopt a project by name. Returns (project_id, created)."""
    existing = find_project(cfg, name)
    if existing:
        return int(existing["id"]), False
    pid = rpc(cfg, "createProject", name=name)
    if not pid:
        raise BoardError(f"createProject({name}) returned no id")
    return int(pid), True


def reconcile_columns(cfg, pid, created):
    """Make the board's columns exactly COLUMNS. On a freshly-created project remove the
    Kanboard defaults and add ours in order; on adopt, only append any missing (never
    remove — a populated board could lose cards)."""
    have = rpc(cfg, "getColumns", project_id=pid) or []
    have_titles = [c["title"] for c in have]
    if have_titles == COLUMNS:
        return
    if created:
        for c in have:                      # fresh board: no tasks, safe to clear
            rpc(cfg, "removeColumn", column_id=int(c["id"]))
        for title in COLUMNS:
            rpc(cfg, "addColumn", project_id=pid, title=title)
    else:
        for title in COLUMNS:               # adopt: add missing only, preserve order/cards
            if title not in have_titles:
                rpc(cfg, "addColumn", project_id=pid, title=title)


def column_id(cfg, pid, title):
    for c in (rpc(cfg, "getColumns", project_id=pid) or []):
        if c["title"] == title:
            return int(c["id"])
    return None


def tasks_in_project(cfg, pid):
    """All active tasks (title→task) for idempotent upserts."""
    out = {}
    for t in (rpc(cfg, "getAllTasks", project_id=pid, status_id=1) or []):
        out[t["title"]] = t
    return out


def ensure_task(cfg, pid, title, column, color=None):
    """Create the task if a same-titled active one doesn't exist. Returns task id."""
    existing = tasks_in_project(cfg, pid).get(title)
    if existing:
        return int(existing["id"])
    kw = {"title": title, "project_id": pid, "column_id": column_id(cfg, pid, column)}
    if color:
        kw["color_id"] = color
    tid = rpc(cfg, "createTask", **kw)
    return int(tid) if tid else None


def add_link(cfg, task_id, url, title):
    """Attach an external link to a task (idempotent — skip if the url is present).
    Uses type 'auto' so Kanboard picks the provider: file:// → Local File (pre-promote
    doc/commit refs), http(s):// → Web Link (github URLs after promote). The 'weblink'
    provider rejects non-http URLs, so 'auto' is required for the local-first case."""
    for l in (rpc(cfg, "getAllExternalTaskLinks", task_id=task_id) or []):
        if l.get("url") == url:
            return
    rpc(cfg, "createExternalTaskLink", task_id=task_id, type="auto",
        dependency="related", url=url, title=title)


# ─── doc-card discovery ──────────────────────────────────────────────────────
def doc_files(proto):
    """Existing planning artefacts under the prototype (files + *.md in the dirs)."""
    found = []
    for a in DOC_ARTEFACTS:
        p = os.path.join(proto, a)
        if os.path.isfile(p):
            found.append(a)
        elif os.path.isdir(p):
            for root, _, files in os.walk(p):
                for fn in sorted(files):
                    if fn.endswith(".md"):
                        found.append(os.path.relpath(os.path.join(root, fn), proto))
    return found


# ─── verb: project ───────────────────────────────────────────────────────────
def cmd_project(cfg, proto):
    """Create-or-adopt the prototype's board: columns + doc cards + overview card."""
    proto = os.path.abspath(proto)
    name = os.path.basename(proto.rstrip("/"))
    pid, created = ensure_project(cfg, name)
    reconcile_columns(cfg, pid, created)

    # Doc cards → Planning, one per existing artefact, with a local-path weblink.
    plan_docs = 0
    for rel in doc_files(proto):
        tid = ensure_task(cfg, pid, f"doc: {rel}", "Planning", color="blue")
        if tid:
            add_link(cfg, tid, "file://" + os.path.join(proto, rel), rel)
            plan_docs += 1

    # Overview board: one card per prototype, in the column = current lifecycle stage.
    ovid, _ = ensure_project(cfg, OVERVIEW)
    reconcile_columns(cfg, ovid, _)
    otid = ensure_task(cfg, ovid, name, "Planning", color="green")

    mk = read_marker(proto)
    mk.update({"project_id": pid, "project_name": name, "overview_task_id": otid,
               "linked_shas": mk.get("linked_shas", [])})
    write_marker(proto, mk)
    print(f"board: project '{name}' {'created' if created else 'adopted'} "
          f"(id {pid}, {plan_docs} doc card(s), overview card {otid})")


# ─── git + marker helpers ────────────────────────────────────────────────────
import re
import subprocess


def proto_pid(cfg, proto):
    """The prototype's Kanboard project id — from .board, else adopt-by-name."""
    mk = read_marker(proto)
    if mk.get("project_id"):
        return int(mk["project_id"]), mk
    name = os.path.basename(os.path.abspath(proto).rstrip("/"))
    p = find_project(cfg, name)
    if not p:
        raise BoardError(f"no board for '{name}' — run `board project {proto}` first")
    mk["project_id"] = int(p["id"])
    return int(p["id"]), mk


def git_msg(proto, sha):
    """Full commit message for <sha> in the proto repo, or '' if unavailable."""
    try:
        return subprocess.run(["git", "-C", proto, "show", "-s", "--format=%B", sha],
                              capture_output=True, text=True, timeout=10).stdout
    except Exception:
        return ""


def ticket_of(msg):
    """The task id from a `Ticket: T-<id>` trailer, or None."""
    m = re.search(r"(?mi)^\s*Ticket:\s*T-(\d+)\s*$", msg or "")
    return int(m.group(1)) if m else None


# ─── verb: rfc ───────────────────────────────────────────────────────────────
def cmd_rfc(cfg, proto, *desc_parts):
    """Create an RFC card in Backlog; print its `T-<id>` for the commit trailer."""
    proto = os.path.abspath(proto)
    desc = " ".join(desc_parts).strip() or "RFC"
    pid, mk = proto_pid(cfg, proto)
    tid = ensure_task(cfg, pid, f"RFC: {desc}", "Backlog", color="yellow")
    write_marker(proto, mk)
    print(f"T-{tid}")


# ─── verb: link (commit → RFC card) ──────────────────────────────────────────
def cmd_link(cfg, proto, sha):
    """Attach commit <sha> to the RFC card named by its `Ticket: T-<id>` trailer.
    Best-effort + idempotent. Pre-promote the link is a local placeholder URL
    (file://…#commit=<sha>); `board promote` rewrites it to the github commit URL."""
    proto = os.path.abspath(proto)
    tid = ticket_of(git_msg(proto, sha))
    if not tid:
        return                                       # no trailer → nothing to link
    pid, mk = proto_pid(cfg, proto)
    url = f"file://{proto}#commit={sha}"
    add_link(cfg, tid, url, f"commit {sha[:8]} (local)")
    linked = set(mk.get("linked_shas", []))
    linked.add(sha)
    mk["linked_shas"] = sorted(linked)
    mk["last_sha"] = sha
    write_marker(proto, mk)
    print(f"board: linked commit {sha[:8]} → card T-{tid}")


# ─── verb: install-hook ──────────────────────────────────────────────────────
HOOK = """#!/bin/sh
# board post-commit hook — link this commit to its Ticket: RFC card (best-effort).
# Reads the commit's `Ticket: T-<id>` trailer; a board/network outage never blocks a commit.
sha=$(git rev-parse HEAD)
python3 {board_py} link {proto} "$sha" >/dev/null 2>>{proto}/.board.log || true
exit 0
"""


def cmd_install_hook(cfg, proto):
    """Drop a post-commit hook into the prototype's .git/hooks (idempotent). git-inits the
    prototype if it isn't a repo yet — the hook's whole purpose is commit-linking, so a repo
    is implied; this makes pre-promote RFC↔commit linking work (ledger PROTO_GIT_INIT)."""
    proto = os.path.abspath(proto)
    if not os.path.isdir(os.path.join(proto, ".git")):
        if DRY_RUN:
            print(f"  [dry-run] git init {proto}")
        else:
            subprocess.run(["git", "-C", proto, "init", "-q", "-b", "main"], check=False)
    hooks = os.path.join(proto, ".git", "hooks")
    if not os.path.isdir(hooks):
        print(f"board: could not git-init {proto} — skipping hook install")
        return
    path = os.path.join(hooks, "post-commit")
    body = HOOK.format(board_py=os.path.abspath(__file__), proto=proto)
    if DRY_RUN:
        print(f"  [dry-run] write {path}")
        return
    with open(path, "w") as f:
        f.write(body)
    os.chmod(path, 0o755)
    print(f"board: post-commit hook installed → {path}")


# ─── github + promote (Move 6 — the risky 20%) ───────────────────────────────
GH_OWNER = os.environ.get("BOARD_GH_OWNER", "drs76")
# minimal secret patterns — block the github push on a hit (never the local promote)
SECRET_RE = re.compile(
    r"(sk-[A-Za-z0-9]{20,}|gh[posru]_[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|"
    r"-----BEGIN [A-Z ]*PRIVATE KEY-----|OPENROUTER_API_KEY\s*=\s*\S+)")


def gh(*args, check=True):
    """Run `gh …`; honour BOARD_DRY_RUN. Returns (rc, stdout)."""
    if DRY_RUN:
        print(f"  [dry-run] gh {' '.join(args)}")
        return 0, ""
    r = subprocess.run(["gh", *args], capture_output=True, text=True)
    if check and r.returncode != 0:
        raise BoardError(f"gh {args[0]} failed: {(r.stderr or r.stdout).strip()}")
    return r.returncode, r.stdout.strip()


def gh_has_project_scope():
    if DRY_RUN:
        return True
    r = subprocess.run(["gh", "auth", "status"], capture_output=True, text=True)
    return "'project'" in (r.stdout + r.stderr)


def ensure_git(proto, name):
    """Guarantee a git repo with at least one commit (gh repo create --source needs it)."""
    if DRY_RUN:
        return "main"
    if not os.path.isdir(os.path.join(proto, ".git")):
        subprocess.run(["git", "-C", proto, "init", "-q", "-b", "main"], check=True)
    # a commit if the tree has none yet
    has = subprocess.run(["git", "-C", proto, "rev-parse", "HEAD"],
                         capture_output=True, text=True).returncode == 0
    if not has:
        subprocess.run(["git", "-C", proto, "add", "-A"], check=True)
        subprocess.run(["git", "-C", proto, "-c", "user.email=board@local",
                        "-c", "user.name=board", "commit", "-q", "-m",
                        f"promote {name}"], check=True)
    br = subprocess.run(["git", "-C", proto, "branch", "--show-current"],
                        capture_output=True, text=True).stdout.strip()
    return br or "main"


def secret_scan(proto):
    """Return a list of (relpath) files that trip SECRET_RE among git-tracked files."""
    if DRY_RUN:
        return []
    files = subprocess.run(["git", "-C", proto, "ls-files"], capture_output=True,
                           text=True).stdout.split()
    hits = []
    for rel in files:
        try:
            with open(os.path.join(proto, rel), encoding="utf-8", errors="ignore") as f:
                if SECRET_RE.search(f.read()):
                    hits.append(rel)
        except OSError:
            pass
    return hits


def _rewrite_url(old, proto, repo_url, branch):
    """Pure mapping: a local file:// doc/commit URL → its github URL, else None.
    Kept pure (no I/O) so it is unit-testable (test_board.py)."""
    pc, pd = f"file://{proto}#commit=", f"file://{proto}/"
    if old.startswith(pc):
        return f"{repo_url}/commit/{old[len(pc):]}"
    if old.startswith(pd):
        return f"{repo_url}/blob/{branch}/{old[len(pd):]}"
    return None


def rewrite_links(cfg, pid, proto, repo_url, branch):
    """Rewrite every local file:// external link to its github URL (idempotent)."""
    for t in (rpc(cfg, "getAllTasks", project_id=pid, status_id=1) or []):
        for l in (rpc(cfg, "getAllExternalTaskLinks", task_id=int(t["id"])) or []):
            old = l.get("url", "")
            new = _rewrite_url(old, proto, repo_url, branch)
            if new and new != old:
                rpc(cfg, "removeExternalTaskLink", task_id=int(t["id"]), link_id=int(l["id"]))
                add_link(cfg, int(t["id"]), new, l.get("title", "link"))


def move_overview(cfg, name, column):
    """Move the prototype's overview card to `column` (best-effort)."""
    ov = find_project(cfg, OVERVIEW)
    if not ov:
        return
    ovid = int(ov["id"])
    cid = column_id(cfg, ovid, column)
    for t in (rpc(cfg, "getAllTasks", project_id=ovid, status_id=1) or []):
        if t["title"] == name and cid:
            rpc(cfg, "moveTaskPosition", project_id=ovid, task_id=int(t["id"]),
                column_id=cid, position=1, swimlane_id=int(t.get("swimlane_id", 0)))
            return


def cmd_promote(cfg, proto):
    """Move the overview card to Promoted; mirror to github ONLY when egress permits.
    Gate-first, idempotent, resumable; a local-only prototype takes the log-skip branch
    (no gh call at all) and still 'succeeds'."""
    proto = os.path.abspath(proto)
    name = os.path.basename(proto.rstrip("/"))
    pid, mk = proto_pid(cfg, proto)

    egress_policy.set_policy_for(proto)                     # resolve .anon/config.yml / env
    ok, reason = egress_policy.allowed("github")            # GATE FIRST — before any gh
    if not ok:
        move_overview(cfg, name, "Promoted")
        mk["github"] = False
        write_marker(proto, mk)
        print(f"board: promoted '{name}' locally — github mirror SKIPPED ({reason})")
        return

    if not gh_has_project_scope():
        move_overview(cfg, name, "Promoted")
        print(f"board: promoted '{name}' locally — github mirror SKIPPED: gh token lacks the "
              f"'project' scope (run: gh auth refresh -s project). Re-run `board sync {proto}` after.")
        return

    hits = secret_scan(proto)
    if hits:
        move_overview(cfg, name, "Promoted")
        print(f"board: promoted '{name}' locally — github mirror BLOCKED: possible secret(s) in "
              f"{', '.join(hits[:5])}. Remove them, then `board sync {proto}`.")
        return

    branch = ensure_git(proto, name)
    repo = f"{GH_OWNER}/{name}"
    repo_url = f"https://github.com/{repo}"

    # 1. repo (idempotent: create if absent, else ensure origin + push)
    exists = gh("repo", "view", repo, check=False)[0] == 0
    if not exists:
        gh("repo", "create", repo, "--private", "--source", proto, "--remote", "origin", "--push")
    elif not DRY_RUN:
        subprocess.run(["git", "-C", proto, "remote", "add", "origin",
                        f"https://github.com/{repo}.git"], capture_output=True)
        subprocess.run(["git", "-C", proto, "push", "-u", "origin", branch], capture_output=True)

    # tag the repo so pipeline repos are findable on github (idempotent; best-effort)
    gh("repo", "edit", repo, "--add-topic", "prototype", "--add-topic", "promoted", check=False)

    # 2. Project v2 (idempotent via .board), then link the repo
    proj_url = mk.get("github_project_url")
    if not proj_url:
        _, out = gh("project", "create", "--owner", "@me", "--title", name, "--format", "json")
        try:
            proj_url = json.loads(out).get("url") if out else None
            num = str(json.loads(out).get("number")) if out else None
        except ValueError:
            proj_url, num = None, None
        if num:
            gh("project", "link", num, "--owner", "@me", "--repo", repo, check=False)

    # 3. rewrite local links → github URLs
    rewrite_links(cfg, pid, proto, repo_url, branch)

    # 4. record repo/project on the overview card + move it to Promoted
    ov = find_project(cfg, OVERVIEW)
    if ov and mk.get("overview_task_id"):
        add_link(cfg, int(mk["overview_task_id"]), repo_url, f"{name} repo")
        if proj_url:
            add_link(cfg, int(mk["overview_task_id"]), proj_url, f"{name} project")
    move_overview(cfg, name, "Promoted")

    mk.update({"github": True, "repo_url": repo_url, "github_project_url": proj_url,
               "default_branch": branch})
    write_marker(proto, mk)
    print(f"board: promoted '{name}' → {repo_url}" + (f" + project {proj_url}" if proj_url else ""))


# ─── verb: sync (Move 7 — the reconcile net) ─────────────────────────────────
def git_shas(proto):
    """All commit shas in the proto repo (newest first), or [] if not a repo."""
    r = subprocess.run(["git", "-C", proto, "log", "--format=%H"],
                       capture_output=True, text=True)
    return r.stdout.split() if r.returncode == 0 else []


def cmd_sync(cfg, proto):
    """Idempotently reconcile a prototype to the board: create/adopt the board + cards,
    attach any unlinked `Ticket:` commits, and (if already github-mirrored) rewrite links
    to their github URLs. Safe to re-run — the net under every best-effort gap."""
    proto = os.path.abspath(proto)
    name = os.path.basename(proto.rstrip("/"))

    cmd_project(cfg, proto)                              # create/adopt board + columns + doc cards + overview

    mk = read_marker(proto)
    linked_before = set(mk.get("linked_shas", []))
    relinked = 0
    for sha in git_shas(proto):                          # attach unlinked trailer'd commits
        if sha in linked_before:
            continue
        if ticket_of(git_msg(proto, sha)):
            cmd_link(cfg, proto, sha)
            relinked += 1

    mk = read_marker(proto)
    if mk.get("github") and mk.get("repo_url"):          # already promoted → keep github links fresh
        rewrite_links(cfg, int(mk["project_id"]), proto, mk["repo_url"],
                      mk.get("default_branch", "main"))

    print(f"board: synced '{name}' ({relinked} commit(s) re-linked"
          + (", github links refreshed" if mk.get("github") else "") + ")")


VERBS = {
    "project": cmd_project,
    "rfc": cmd_rfc,
    "link": cmd_link,
    "install-hook": cmd_install_hook,
    "promote": cmd_promote,
    "sync": cmd_sync,
}


def main(argv):
    if len(argv) < 2 or argv[1] not in VERBS:
        print("usage: board <" + "|".join(VERBS) + "> <proto-path> [args]", file=sys.stderr)
        return 2
    try:
        cfg = load_cfg()
    except BoardError as e:
        print(f"board: {e}", file=sys.stderr)
        return 2
    try:
        VERBS[argv[1]](cfg, *argv[2:])
    except BoardError as e:
        print(f"board: {e}", file=sys.stderr)
        return 2
    except TypeError:
        print(f"usage: board {argv[1]} <proto-path> [args]", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
