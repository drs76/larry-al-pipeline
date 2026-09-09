"""anon_workspace.py — Mode B workspace-mirror for agentic coders (anon hook, phase 4).

Claude Code is agentic: it reads/edits real files with its own tools, so scrubbing a
single prompt is not enough. This presents the coder a SCRUBBED MIRROR of the tracked
tree, lets it edit there, then reverse-maps the resulting diff back to real tokens and
applies it to the real repo:

    tracked files ─forward(scrub)→ mirror ─git baseline→ coder edits ─git diff→
        scrubbed patch ─reverse(map)→ real patch ─git apply→ real repo

Only git-tracked TEXT files are mirrored (respects .gitignore; binaries skipped). HIGH
secrets fail the whole run closed (§6). Reversibility (phase 2) is what lets the reversed
context lines match the real files so the patch applies. See anon-claude-hook.spec.md §4.
"""
import os
import shutil
import subprocess
import tempfile

import anon_map
import pathguard
import secret_gate


class SymlinkAbort(Exception):
    """A tracked symlink was found while building the enterprise mirror. Fail closed —
    following it can copy an out-of-repo file into the scrubbed workspace."""

    def __init__(self, rel, target):
        super().__init__(f"tracked symlink not permitted in the anonymised mirror: "
                         f"{rel} -> {target}")
        self.rel, self.target = rel, target


class SecretAbort(Exception):
    def __init__(self, rel, highs):
        self.rel, self.highs = rel, highs
        super().__init__(f"HIGH secret in {rel}: {[h['name'] for h in highs]}")


def _run(cmd, cwd=None, check=True, text_input=None):
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, input=text_input)
    if check and r.returncode != 0:
        raise RuntimeError(f"{' '.join(cmd)} failed ({r.returncode}): {r.stderr.strip()}")
    return r


def _is_text(path):
    try:
        with open(path, "rb") as f:
            chunk = f.read(4096)
        if b"\x00" in chunk:
            return False
        chunk.decode("utf-8")
        return True
    except Exception:
        return False


def build_mirror(repo, amap, lits, mirror, allow_secrets=False):
    """Scrub each tracked text file into the mirror. Returns (scrubbed, skipped)."""
    files = _run(["git", "ls-files"], cwd=repo).stdout.splitlines()
    scrubbed, skipped = 0, []
    for rel in files:
        src = os.path.join(repo, rel)
        # os.path.isfile() FOLLOWS symlinks, so a tracked link could pull an external
        # file into the scrubbed mirror and defeat the repo boundary this workflow
        # exists to enforce. Fail CLOSED on an unexpected tracked symlink rather than
        # dereferencing it or silently skipping: omission changes what the agent
        # believes the source tree contains, which is its own failure mode.
        if os.path.islink(src):
            raise SymlinkAbort(rel, os.path.realpath(src))
        if not os.path.isfile(src):
            continue
        # Belt and braces: a tracked path must also resolve inside the repo.
        if not pathguard.contains(repo, src):
            raise SymlinkAbort(rel, os.path.realpath(src))
        if not _is_text(src):
            skipped.append(rel)
            continue
        text = open(src, encoding="utf-8", errors="replace").read()
        s = anon_map.forward(text, amap, lits)
        ok, red, findings = secret_gate.gate(s, allow_high=allow_secrets)
        if not ok:
            raise SecretAbort(rel, [f for f in findings if f["confidence"] == "high"])
        dst = os.path.join(mirror, rel)
        d = os.path.dirname(dst)
        if d:
            os.makedirs(d, exist_ok=True)
        open(dst, "w", encoding="utf-8").write(red)
        scrubbed += 1
    return scrubbed, skipped


def run_workspace(repo, prompt, coder_fn, allow_secrets=False):
    """Full Mode B cycle. `coder_fn(mirror_dir, prompt)` edits the scrubbed mirror
    (production: run `claude -p` there). Returns a result dict."""
    repo = os.path.abspath(repo)
    if _run(["git", "rev-parse", "--is-inside-work-tree"], cwd=repo, check=False).returncode != 0:
        raise RuntimeError(f"not a git repo: {repo}")
    # "Inside a work tree" is NOT "is the work tree". A run directory whose .git has been
    # damaged — the map fixture's cleanup.sh deletes .git/HEAD and .git/config because its
    # exclusion list omits .git — makes git DISCOVER AN ANCESTOR repository. Every operation
    # below then targets that ancestor: the mirror is built from its ls-files (empty in an
    # ignored subdirectory) and, worse, callers commit to it. Observed on routecon4/map/r4,
    # which produced a real commit in the setup repository. Fail closed before mutating.
    top = _run(["git", "rev-parse", "--show-toplevel"], cwd=repo, check=False).stdout.strip()
    if os.path.realpath(top) != os.path.realpath(repo):
        raise RuntimeError(
            f"git top-level is {top!r}, not the project root {repo!r} — refusing to mirror "
            f"or mutate an ancestor repository. The run directory's .git is missing or "
            f"damaged.")
    anon_dir = os.path.join(repo, ".anon")
    mp = os.path.join(anon_dir, "map.tsv")
    amap = anon_map.AnonMap().load(mp)
    lits = anon_map.load_names(os.path.join(anon_dir, "names.tsv"))
    mirror = tempfile.mkdtemp(prefix="anon-mirror-")
    try:
        scrubbed, skipped = build_mirror(repo, amap, lits, mirror, allow_secrets)
        amap.save(mp)   # persist newly-minted placeholders so reverse is complete
        env = {**os.environ, "GIT_AUTHOR_NAME": "anon", "GIT_AUTHOR_EMAIL": "anon@local",
               "GIT_COMMITTER_NAME": "anon", "GIT_COMMITTER_EMAIL": "anon@local"}
        subprocess.run(["git", "init", "-q"], cwd=mirror, check=True)
        subprocess.run(["git", "add", "-A"], cwd=mirror, check=True)
        subprocess.run(["git", "commit", "-q", "-m", "scrubbed baseline"],
                       cwd=mirror, check=True, env=env)

        coder_fn(mirror, prompt)   # the coder edits the mirror in scrubbed space

        subprocess.run(["git", "add", "-A"], cwd=mirror, check=True)
        patch = _run(["git", "diff", "--cached", "HEAD"], cwd=mirror).stdout
        if not patch.strip():
            return {"changed": False, "scrubbed": scrubbed, "skipped": skipped}

        real_patch = anon_map.reverse(patch, amap)   # placeholders → real tokens
        if anon_dir and not os.path.isdir(anon_dir):
            os.makedirs(anon_dir, exist_ok=True)
        patch_path = os.path.join(anon_dir, "last.patch")
        open(patch_path, "w", encoding="utf-8").write(real_patch)

        # Reversed context lines equal the real file content, so a plain context apply
        # lands cleanly. On conflict, emit .rej and stop — never half-apply silently.
        ap = _run(["git", "apply", "--whitespace=nowarn", patch_path], cwd=repo, check=False)
        if ap.returncode != 0:
            _run(["git", "apply", "--reject", "--whitespace=nowarn", patch_path],
                 cwd=repo, check=False)
        return {"changed": True, "applied": ap.returncode == 0, "patch": patch_path,
                "apply_err": ap.stderr.strip(), "scrubbed": scrubbed, "skipped": skipped}
    finally:
        shutil.rmtree(mirror, ignore_errors=True)
