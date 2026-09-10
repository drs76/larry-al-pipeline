#!/usr/bin/env bash
# publish-public.sh — sync the private working repo to the public snapshot repo.
#
# Not a mirror and not a periodic job. The public repo shares NO ancestry with this
# one (its history was squashed to keep a personal email and pre-scrub paths out of
# the public log), so syncing means: export this tree, gate it, commit the delta.
#
# Design decisions worth keeping:
#
#   APPEND, never force-push. Each sync is an ordinary commit in the public repo.
#   Re-squashing and force-pushing every time would break every clone and fork and
#   make the public repo useless to anyone following it.
#
#   FAIL CLOSED. The gate aborts the publish on any hit. A warning-only check is
#   worthless — the entire value is that a leak stops the sync.
#
#   DELETIONS PROPAGATE. `git archive | tar -x` only adds and overwrites, so a file
#   deleted here would live on in public forever. The public tracked tree is cleared
#   before extraction. This is the trap this script exists to prevent.
#
# Usage:  tooling/publish-public.sh [--dry-run]
set -uo pipefail

PRIVATE="${PRIVATE:-/mnt/rojaws/localDev/setup}"
PUBLIC="${PUBLIC:-/mnt/rojaws/localDev/larry-al-pipeline}"
DENYLIST="$PRIVATE/tooling/publish-denylist.txt"
DRY=0; [ "${1:-}" = "--dry-run" ] && DRY=1

die() { echo "FATAL: $*" >&2; exit 1; }

# ---- preflight -------------------------------------------------------------
[ -d "$PRIVATE/.git" ] || die "private repo not found: $PRIVATE"
[ -d "$PUBLIC/.git" ]  || die "public repo not found: $PUBLIC"
[ -f "$DENYLIST" ]     || die "denylist missing: $DENYLIST — refusing to publish ungated"

[ -z "$(git -C "$PRIVATE" status --porcelain)" ] || die "private tree dirty — commit first"
[ -z "$(git -C "$PUBLIC" status --porcelain)" ]  || die "public tree dirty — resolve first"

SRC_SHA=$(git -C "$PRIVATE" rev-parse HEAD)
SRC_SHORT=$(git -C "$PRIVATE" rev-parse --short HEAD)
echo "source: $PRIVATE @ $SRC_SHORT"
echo "target: $PUBLIC"

# ---- export into a staging tree, never straight onto the target ------------
STAGE=$(mktemp -d) || die "mktemp failed"
trap 'rm -rf "$STAGE"' EXIT
git -C "$PRIVATE" archive HEAD | tar -x -C "$STAGE" || die "export failed"
echo "exported $(find "$STAGE" -type f | wc -l) tracked files"

# ---- gate: denylist + secret_gate, one Python pass, fails closed ----------
# Deliberately NOT shell grep. Two bugs came from that: `grep -PE` specifies two
# conflicting matchers, so GNU grep exited 2 with no output and the gate silently
# PASSED (it looked fine only because this box aliases grep to ugrep); and a
# path-based exemption cannot be expressed as a content lookahead, because grep
# matches line text and never sees the filename. Python sees both, and a malformed
# regex raises instead of quietly matching nothing.
python3 - "$STAGE" "$PRIVATE" "$DENYLIST" <<'PY'
import os, re, sys
stage, private, denylist = sys.argv[1], sys.argv[2], sys.argv[3]
sys.path.insert(0, os.path.join(private, "pipeline"))
import secret_gate

# Path prefixes exempt from a given pattern, with the reason. An exemption is a
# decision: it names the pattern it weakens, so it cannot silently widen.
# Keyed by the `# @id` declared above a pattern in the denylist, NOT by the pattern
# text: keying by the literal would put the guarded string into this file, and the
# gate would then block on its own source. (It did — that is how this was found.)
SKIP = {
    "home-paths": [
        # sway(5) expands shell syntax for `include` only, not for `output ... bg`,
        # so genericising the wallpaper path breaks a working desktop config.
        "tower/sway-setup/",
        # Raw captured output. Editing it would falsify a preserved artefact.
        "reference/bench-results/",
    ],
}

pats, pending_id = [], None
for raw in open(denylist, encoding="utf-8"):
    line = raw.strip()
    if line.startswith("# @id "):
        pending_id = line[len("# @id "):].strip()
        continue
    if not line or line.startswith("#"):
        continue
    try:
        pats.append((pending_id, line, re.compile(line)))
        pending_id = None
    except re.error as e:
        print(f"GATE ERROR  unusable pattern /{line}/: {e}", file=sys.stderr)
        sys.exit(1)

# Files whose HIGH secret_gate findings are known-fake, path-exact and justified.
# Deliberately not a "*test*" glob: a real credential in a new test file must block.
KNOWN_FAKE = {
    "pipeline/secret_gate.py":          "its own detection patterns",
    "pipeline/test_secret_gate.py":     "fixtures that prove the detector fires",
    "pipeline/test_board.py":           "fake AWS key in a redaction fixture",
    "pipeline/test_al_intelligence.py": "fake OpenAI key in a redaction fixture",
    # Plants AWS's own published documentation example access key as the fixture that
    # proves build_mirror aborts on a HIGH secret. The gate cannot know it is an example
    # and correctly blocked a publish on it; the exception is deliberate and path-exact
    # rather than a loosened pattern. The literal is deliberately NOT written here — a
    # justification that quotes the string re-triggers the gate on THIS file, which is
    # exactly what happened on the first attempt.
    "pipeline/probe_anon_mirror.sh":    "AWS documentation example key, secret-abort fixture",
}

bad = 0
for root, dirs, files in os.walk(stage):
    dirs[:] = [d for d in dirs if d != ".git"]
    for fn in files:
        p = os.path.join(root, fn)
        rel = os.path.relpath(p, stage)
        try:
            text = open(p, encoding="utf-8", errors="strict").read()
        except (UnicodeDecodeError, OSError):
            continue                      # binary or unreadable: nothing to scan
        # The denylist necessarily contains the strings it matches; scanning it
        # guarantees a self-hit on every pattern. Consequence accepted knowingly:
        # a secret pasted INTO the denylist is not caught by the denylist, which is
        # why its patterns match shapes rather than literal secret values.
        if rel != "tooling/publish-denylist.txt":
            for pid, src, rx in pats:
                if pid and any(rel.startswith(s) for s in SKIP.get(pid, ())):
                    continue
                if rx.search(text):
                    print(f"DENYLIST HIT  /{src}/  {rel}", file=sys.stderr)
                    bad = 1
        if rel in KNOWN_FAKE:
            continue
        for f in secret_gate.scan(text):
            if f["confidence"] == "high":
                print(f"SECRET_GATE HIT  {f['name']}  {rel}  preview={f['preview']}",
                      file=sys.stderr)
                bad = 1
sys.exit(bad)
PY
FAIL=$?

[ "$FAIL" = 0 ] || die "gate blocked the publish — nothing was written to $PUBLIC"
echo "gate: clean"

[ "$DRY" = 1 ] && { echo "--dry-run: stopping before any write"; exit 0; }

# ---- replace the public tracked tree (this is what propagates deletions) ---
# In Python, and with the base path passed explicitly, because the shell form was
# DANGEROUS:
#
#     git -C "$PUBLIC" ls-files -z | xargs -0 -r rm -f --
#
# `git -C` scopes GIT, not `rm`. ls-files prints repo-relative paths and rm resolved
# them against the CURRENT DIRECTORY. Run from the private repo — the normal way to
# invoke this script — it deleted 795 tracked files out of the PRIVATE working tree.
# Recovered from HEAD, nothing lost, but only because that tree happened to be clean.
#
# A guard also refuses to touch anything whose git remote is not the public repo, so
# pointing this at the wrong directory aborts instead of deleting it.
python3 - "$STAGE" "$PUBLIC" <<'PY' || die "tree replacement failed"
import os, subprocess, sys, shutil
stage, public = sys.argv[1], sys.argv[2]

def git(*a):
    r = subprocess.run(["git", "-C", public, *a], capture_output=True, text=True)
    return r.stdout.strip() if r.returncode == 0 else None

# Refuse unless this really is the public snapshot repo. Identity, not a path string.
remote = git("remote", "get-url", "origin") or ""
if "larry-al-pipeline" not in remote:
    sys.exit(f"REFUSING: {public} origin is {remote!r}, not the public repo")
top = git("rev-parse", "--show-toplevel")
if not top or os.path.realpath(top) != os.path.realpath(public):
    sys.exit(f"REFUSING: {public} is not a git top-level")

listing = subprocess.run(["git", "-C", public, "ls-files", "-z"],
                         capture_output=True, text=True)
tracked = [p for p in listing.stdout.split("\0") if p]
removed = 0
for rel in tracked:
    # Join against `public` EXPLICITLY. This is the line the shell version got wrong.
    p = os.path.join(public, rel)
    if os.path.realpath(p).startswith(os.path.realpath(public) + os.sep) and os.path.isfile(p):
        os.remove(p); removed += 1
for root, dirs, files in os.walk(public, topdown=False):
    if ".git" in root.split(os.sep):
        continue
    if not os.listdir(root) and os.path.realpath(root) != os.path.realpath(public):
        os.rmdir(root)
print(f"  cleared {removed} tracked file(s) from the public tree")
shutil.copytree(stage, public, dirs_exist_ok=True)
PY

git -C "$PUBLIC" add -A
if git -C "$PUBLIC" diff --cached --quiet; then
  echo "no change since last sync — nothing to publish"; exit 0
fi
echo "changed: $(git -C "$PUBLIC" diff --cached --name-only | wc -l) file(s)"

git -C "$PUBLIC" commit -q -m "sync: private @ $SRC_SHORT

Snapshot of the working repo at $SRC_SHA.
Exported and gated by tooling/publish-public.sh." || die "commit failed"
git -C "$PUBLIC" push -q origin HEAD || die "push failed"
echo "published: $(git -C "$PUBLIC" rev-parse --short HEAD)  <- private @ $SRC_SHORT"
