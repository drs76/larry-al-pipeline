#!/usr/bin/env python3
"""
run-ingest — sources (YouTube / blogs) → AL knowledge base, orchestrated.

  scan --channel <url> [--limit N]   triage a channel/feed/page; writes a plan you approve
  run  --plan <plan.md>              fetch + distil + merge everything marked KEEP

<url> may be a YouTube channel, an RSS/Atom feed, a blog root (its feed is
auto-discovered) or a single article.

Two phases on purpose. `scan` is cheap and ends at a checkpoint: a markdown table of
KEEP/SKIP verdicts. You edit it (flip a verdict, delete a row) and only then run the
expensive half, so a long fetch/distil pass is never spent on the wrong 60 items.

Deterministic work (channel listing, caption fetch, VTT cleaning, archiving) is
source_collect.py — no model. Judgement work (is this dev-relevant? what's the durable
knowledge?) is Claude. Distillation writes original technical notes, never a
reproduction of the transcript.

Merging: distilled blocks are auto-merged into a TOPIC FILE under
reference/al-reference/ (syntax/API) or reference/al-knowledge/ (platform/DevOps/
features) — the root AL-*.md files are indexes, not content. A topic file that grows
past ~8k tokens gets a warning telling you to re-split it, because the coder is served
at num_ctx=32768 and a topic is meant to be readable in one go. The curated files are
only touched when the setup repo is clean or --force is given, so a bad pass is one
`git checkout` away.

Env:
  CLAUDE_BIN     claude binary (default: PATH)
  CLAUDE_TIMEOUT seconds per Claude call (default 900)
  LARRY_REPO     setup repo (default: parent of this file)
"""
import os, sys, re, json, argparse, subprocess, shutil, datetime, glob

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import source_collect as vc

REPO = os.environ.get("LARRY_REPO", os.path.dirname(HERE))
REFERENCE = os.path.join(REPO, "reference")
CLAUDE_BIN = (os.environ.get("CLAUDE_BIN") or shutil.which("claude")
              or os.path.expanduser("~/.local/bin/claude"))
CLAUDE_TIMEOUT = int(os.environ.get("CLAUDE_TIMEOUT", "900"))
TARGETS = {"AL-REFERENCE.md": "AL syntax, language features, object/API code patterns",
           "AL-KNOWLEDGE.md": "platform, DevOps, admin, agents, features, product behaviour",
           # Third tier: distilled conference/community talks. Searchable via kb, never
           # auto-read into a build, so it can grow without threatening the 32k budget
           # the curated files must respect.
           "al-talks": "conference/community talk notes — searchable tier, not hand-verified"}
# Each target's content lives in topic files under these dirs (the AL-*.md roots are indexes).
TARGET_DIRS = {"AL-REFERENCE.md": "al-reference", "AL-KNOWLEDGE.md": "al-knowledge",
               "al-talks": "al-talks"}
# Targets whose topic files may be CREATED on demand (curated tiers are hand-structured;
# the talks tier starts empty and grows a topic per subject as material arrives).
OPEN_TARGETS = {"al-talks"}


def run_claude(prompt, label="Claude"):
    """Headless one-shot. Prompt goes over stdin, never argv — a multi-line argv is
    silently truncated at the first newline by the npm .CMD shim on Windows."""
    if not os.path.exists(CLAUDE_BIN) and not shutil.which(CLAUDE_BIN):
        raise RuntimeError(f"claude not found at {CLAUDE_BIN}")
    print(f"  [{label}] thinking...", flush=True)
    r = subprocess.run([CLAUDE_BIN, "-p"], input=prompt, capture_output=True,
                       text=True, timeout=CLAUDE_TIMEOUT, cwd=REPO)
    if r.returncode != 0:
        raise RuntimeError(f"{label} failed (rc={r.returncode}): {(r.stderr or '')[:300]}")
    return (r.stdout or "").strip()


def _json_block(text):
    """Pull the first JSON array/object out of a model reply (may be fenced).

    Order matters: try the reply AS-IS before hunting for code fences. Distilled
    content routinely contains ```al fences INSIDE the JSON string, and a fence-first
    regex extracts the AL between them instead of the JSON around them — which made
    every well-formed reply carrying a code sample "unusable" (the whole objects
    batch, 15/16)."""
    body = text.strip()
    start = min((i for i in (body.find("["), body.find("{")) if i != -1), default=-1)
    if start != -1:
        end = max(body.rfind("]"), body.rfind("}"))
        try:
            return json.loads(body[start:end + 1])
        except Exception:
            pass
    # Not bare JSON — now try a fenced block (a reply that wraps its JSON in ```json).
    m = re.search(r"```(?:json)?\s*(.+?)```", text, re.S)
    if m:
        inner = m.group(1).strip()
        s2 = min((i for i in (inner.find("["), inner.find("{")) if i != -1), default=-1)
        if s2 != -1:
            return json.loads(inner[s2:max(inner.rfind("]"), inner.rfind("}")) + 1])
    raise ValueError("no JSON found in reply")


def _distil_reply(reply, prompt, label):
    """Get {section, content} out of a distil reply, tolerating a model that ignores
    the JSON instruction. Without this a prose reply throws away a transcript we have
    already fetched and paid to process (1 in 10 on the first real batch)."""
    try:
        return _json_block(reply)
    except Exception:
        pass
    # It answered in prose. Ask once more, explicitly.
    try:
        strict = run_claude(prompt + "\n\nIMPORTANT: reply with ONLY the JSON object — "
                            "no preamble, no explanation, no code fence.", f"{label} retry")
        return _json_block(strict)
    except Exception:
        pass
    # Still not JSON: if it looks like the notes we asked for, keep them rather than
    # discard the whole video; merge_block falls back to end-of-file when section=None.
    if re.search(r"^\s*[#*-]", reply, re.M) and len(reply) > 200:
        print("  (reply was not JSON — salvaged the markdown body)")
        return {"section": None, "content": reply}
    # Include a sample. "distil reply unusable" with no evidence is undiagnosable —
    # it cost a 16-item batch to work out that the replies were bare NOTHING variants.
    sample = " ".join(reply.split())[:160] or "<empty>"
    raise ValueError(f"distil reply unusable (got: {sample!r})")


# ---------------------------------------------------------------------------
# scan / triage
# ---------------------------------------------------------------------------

def cmd_scan(args):
    print(f"Scanning {args.channel} ...")
    vids = vc.scan_any(args.channel)
    if not vids:
        print("Nothing found at that URL.")
        return 1
    fresh = [v for v in vids if not v["archived"]]
    print(f"  {len(vids)} item(s); {len(vids) - len(fresh)} already ingested, "
          f"{len(fresh)} new.")
    if args.limit:
        fresh = fresh[:args.limit]
        print(f"  limited to {len(fresh)}.")
    if not fresh:
        print("Nothing new to ingest.")
        return 0

    listing = "\n".join(
        f'{i+1}. id={v["id"]} | {v["title"]} | '
        f'{str(int(v["duration"])//60)+"m" if v.get("duration") else "article"} | '
        f'{v["upload_date"]}' + (f' | {v.get("description","")[:120]}' if v.get("description") else "")
        for i, v in enumerate(fresh))
    prompt = (
        "You are triaging Business Central / AL material (conference talks, videos, blog "
        "posts) for ingestion into a "
        "Business Central AL developer knowledge base.\n\n"
        "KEEP an item if it teaches something durable and useful to an AL developer or "
        "BC technical consultant: language/API/syntax, architecture, platform behaviour, "
        "DevOps, agents/Copilot implementation, testing, performance, admin.\n"
        "SKIP: marketing, partner/customer success stories, pure end-user UI walkthroughs, "
        "event promos, keynote fluff, obvious duplicates/re-uploads of another entry, and "
        "anything with no technical content.\n\n"
        "Items:\n" + listing + "\n\n"
        'Reply ONLY with a JSON array, one object per video: '
        '{"n": <number>, "id": "<id>", "verdict": "KEEP"|"SKIP", '
        '"target": "AL-REFERENCE.md"|"AL-KNOWLEDGE.md"|null, "reason": "<8 words max>"}\n'
        f'target = where its knowledge belongs: AL-REFERENCE.md ({TARGETS["AL-REFERENCE.md"]}); '
        f'AL-KNOWLEDGE.md ({TARGETS["AL-KNOWLEDGE.md"]}). null when SKIP.'
    )
    try:
        verdicts = _json_block(run_claude(prompt, "triage"))
    except Exception as e:
        print(f"ERROR: triage failed ({e})")
        return 1

    by_id = {v["id"]: v for v in fresh}
    rows, keep = [], 0
    for d in verdicts:
        v = by_id.get(d.get("id"))
        if not v:
            continue
        k = str(d.get("verdict", "")).upper() == "KEEP"
        keep += k
        safe = lambda t: str(t).replace("|", "/").strip()
        rows.append(f'| {"KEEP" if k else "SKIP"} | {safe(v["id"])} | {safe(v["title"])[:60]} | '
                    f'{str(int(v["duration"])//60)+"m" if v.get("duration") else "article"} | '
                    f'{d.get("target") or "-"} | {safe(d.get("reason",""))} |')

    plan = args.plan or os.path.join(REPO, "reference", "ingest-plan.md")
    with open(plan, "w", encoding="utf-8") as fh:
        fh.write(
            f"# Ingest plan — {args.channel}\n\n"
            f"Generated {datetime.date.today().isoformat()}. "
            f"{keep} KEEP / {len(rows) - keep} SKIP.\n\n"
            "Edit before running: flip a verdict, change a target, or delete a row.\n"
            "Then: `ingw run " + os.path.relpath(plan, os.getcwd()) + "`\n\n"
            "| Verdict | ID | Title | Len | Target | Reason |\n"
            "|---|---|---|---|---|---|\n" + "\n".join(rows) + "\n")
    print(f"\nPlan written: {plan}\n  {keep} KEEP / {len(rows)-keep} SKIP")
    print("Review/edit it, then: ingw run " + plan)
    return 0


# ---------------------------------------------------------------------------
# run: fetch -> distil -> merge
# ---------------------------------------------------------------------------

def parse_plan(path):
    keeps = []
    for ln in open(path, encoding="utf-8"):
        if not ln.strip().startswith("|"):
            continue
        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
        if len(cells) < 5 or cells[0].upper() != "KEEP":
            continue
        keeps.append({"id": cells[1], "title": cells[2],
                      "target": cells[4] if cells[4] in TARGETS else "AL-KNOWLEDGE.md"})
    return keeps


def git_dirty():
    """Only the CURATED auto-merge targets matter. Checking all of reference/ would trip
    on the ingest plan (it lives there); including the open talks tier would trip on this
    run's own output, since that tier is designed to accumulate every run. Guard what
    needs protecting: the hand-curated files the coder reads."""
    paths = [os.path.join("reference", t) for t in TARGETS if t not in OPEN_TARGETS]
    r = subprocess.run(["git", "-C", REPO, "status", "--porcelain", "--"] + paths,
                       capture_output=True, text=True)
    return bool(r.stdout.strip())


TOK = 3700          # bytes per token, rough, for technical prose
TOPIC_BUDGET = 8000  # warn above this; a topic must stay readable in one go


def topic_files(target):
    """Topic files for a target, newest content lands in one of these. The root
    AL-*.md files are indexes now (see pipeline/split_knowledge.py), so merging
    into them would put prose in a table of contents. README.md is a tier
    explainer, not a topic."""
    d = os.path.join(REFERENCE, TARGET_DIRS[target])
    if not os.path.isdir(d):
        return []
    return sorted(f for f in glob.glob(os.path.join(d, "*.md"))
                  if os.path.basename(f).lower() != "readme.md")


def new_topic_file(target, section_hint):
    """Create a topic file for an open tier. Without this the talks tier — which
    starts empty — would have nowhere to put its first note."""
    # Strip a trailing .md first: the distiller often answers with a filename
    # ("copilot-agents.md"), and slugifying that yields "copilot-agents-md" —
    # a second topic file for a topic that already exists.
    hint = re.sub(r"\.md$", "", (section_hint or "misc").strip(), flags=re.I)
    slug = re.sub(r"[^a-z0-9]+", "-", hint.lower()).strip("-")[:48] or "misc"
    d = os.path.join(REFERENCE, TARGET_DIRS[target])
    os.makedirs(d, exist_ok=True)
    path = os.path.join(d, f"{slug}.md")
    if not os.path.exists(path):
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(f"# {section_hint or 'Misc'}\n\n"
                     f"Distilled talk notes. Not hand-verified — see "
                     f"[`README.md`](README.md) for caveats, and check anything marked "
                     f"`[sic?]` before relying on it.\n")
        print(f"  created topic {os.path.basename(path)}")
    return path


def register_topic(target, path, subject):
    """Add a newly created topic to its index table, and refresh every row's size.

    The index is what a reader (and the coder's context builder) sees; a topic missing
    from it is a topic nobody finds. Sizes are recomputed from disk on the way past
    because they drift silently — the budget warnings quote them, so a stale number
    understates how close a topic is to the 8k limit.

    Conservative by design: if the table is not shaped as expected the index is left
    untouched and the caller still gets its printed reminder. Mangling the index is a
    worse outcome than a missing row.
    """
    index = os.path.join(REFERENCE, target)
    tdir = TARGET_DIRS[target]
    try:
        text = open(index, encoding="utf-8").read()
    except OSError:
        return False
    lines = text.splitlines()
    # locate the table: header row, separator, then the topic rows
    hdr = next((i for i, l in enumerate(lines)
                if l.startswith("| Topic ") and "Covers" in l), None)
    if hdr is None or hdr + 1 >= len(lines) or not lines[hdr + 1].startswith("|---"):
        return False
    start = hdr + 2
    end = start
    while end < len(lines) and lines[end].startswith("|"):
        end += 1

    row_re = re.compile(r"^\|\s*\[`([^`]+)`\]\([^)]*\)\s*\|(.*?)\|[^|]*\|\s*$")
    rows = {}
    for l in lines[start:end]:
        m = row_re.match(l)
        if not m:
            return False                      # unfamiliar shape — do not touch it
        rows[m.group(1)] = m.group(2).strip()

    base = os.path.basename(path)
    if base not in rows:
        rows[base] = subject
    def ktok(fn):
        """TOK is bytes per THOUSAND tokens, so this already yields k-tokens."""
        try:
            return os.path.getsize(os.path.join(REFERENCE, tdir, fn)) / TOK
        except OSError:
            return 0.0
    ordered = sorted(rows)                    # NN- prefixes sort into reading order
    new_rows = [f"| [`{fn}`]({tdir}/{fn}) | {rows[fn]} | ~{ktok(fn):.1f}k tok |"
                for fn in ordered]
    total = sum(ktok(fn) for fn in ordered)

    out = lines[:start] + new_rows + lines[end:]
    for i, l in enumerate(out):
        if l.startswith("_Total across topics:"):
            out[i] = re.sub(r"~\d+(\.\d+)?k tokens", f"~{total:.0f}k tokens", l)
            break
    open(index, "w", encoding="utf-8").write("\n".join(out) + "\n")
    return True


def new_curated_topic(target, subject):
    """Create a NUMBERED topic file in a curated tier (al-reference / al-knowledge).

    Curated tiers used to be closed: the distiller had to name the "closest" existing
    topic, so material with no natural home was filed under whatever scored a single
    word in common. That is how the app.json manifest reference and four analyzer-rule
    pages both landed at the end of 10-quality-breaking.md, taking it to ~10k tokens
    against an 8k budget. A subject with no home needs a home, not the nearest stranger.
    """
    d = os.path.join(REFERENCE, TARGET_DIRS[target])
    os.makedirs(d, exist_ok=True)
    subject = re.sub(r"\.md$", "", (subject or "misc").strip(), flags=re.I)
    slug = re.sub(r"[^a-z0-9]+", "-", subject.lower()).strip("-")[:48] or "misc"
    # continue the tier's NN- numbering so the index stays ordered
    nums = [int(m.group(1)) for f in topic_files(target)
            if (m := re.match(r"(\d+)-", os.path.basename(f)))]
    nxt = max(nums) + 1 if nums else 0
    path = os.path.join(d, f"{nxt:02d}-{slug}.md")
    if not os.path.exists(path):
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(f"<!-- topic file split from {target}; edit here, not in the index -->\n"
                     f"# {subject}\n\n"
                     f"Part of [`{target}`](../{target}) — see that index for the other topics.\n\n"
                     f"---\n")
        if register_topic(target, path, subject):
            print(f"  created topic {os.path.basename(path)} (added to {target} index)")
        else:
            print(f"  created topic {os.path.basename(path)} "
                  f"— could not parse the {target} index table, ADD THE ROW BY HAND")
    return path


def pick_topic(target, section_hint):
    """Map the distiller's section hint onto a topic file. Falls back to the target's
    catch-all so a merge never silently lands in the index."""
    files = topic_files(target)
    # Open tiers name their own topics: the hint IS the subject, so slugify it and
    # reuse-or-create. Scoring it against existing filenames (as the curated tiers do)
    # sent everything to one catch-all, because a fresh tier has nothing to match.
    if target in OPEN_TARGETS:
        return new_topic_file(target, section_hint)
    if not files:
        return None
    hint = (section_hint or "").strip()

    # The distiller may answer "NEW: <subject>" when nothing existing fits. Honour it
    # rather than forcing the block into the nearest stranger.
    m = re.match(r"^NEW\s*:\s*(.+)$", hint, re.I)
    if m:
        return new_curated_topic(target, m.group(1))

    # 1. Exact filename match — the prompt asks for a topic FILENAME, so trust it when
    #    it names one. Word scoring on an exact answer risks scoring it away.
    if hint:
        want = re.sub(r"\.md$", "", hint.lower()).strip()
        for f in files:
            if os.path.basename(f)[:-3].lower() == want:
                return f

    if hint:
        norm = re.sub(r"[^a-z0-9]+", " ", hint.lower()).strip()
        # Words too generic to constitute a match on their own: every AL topic file is
        # "al ... code ... rules". Matching on these is what filed analyzer rules under
        # "quality-breaking" — one shared word, score 1, good enough to win.
        STOP = {"al", "and", "the", "for", "with", "in", "of", "to", "a",
                "code", "rules", "guide", "notes", "reference", "topic", "bc",
                "business", "central", "dev", "developer", "development"}
        want = set(norm.split()) - STOP
        best, score = None, 0
        for f in files:
            words = set(re.sub(r"[^a-z0-9]+", " ",
                              os.path.basename(f)[:-3].lower()).split()) - STOP
            hit = len(words & want)
            # also consider the topic file's own H1, which carries the description
            try:
                with open(f, encoding="utf-8") as fh:
                    h1 = next((l for l in fh if l.startswith("# ")), "")
                hit += len((set(re.sub(r"[^a-z0-9]+", " ", h1.lower()).split()) - STOP) & want)
            except OSError:
                pass
            if hit > score:
                best, score = f, hit
        # Require TWO independent signals. A single shared word is noise, and acting on
        # it silently appends to an unrelated topic — the failure this guard exists for.
        if best and score >= 2:
            return best
    if target in OPEN_TARGETS:
        return new_topic_file(target, section_hint)
    # No confident home. Make one: a weak guess costs a manual re-split every time.
    return new_curated_topic(target, hint or "misc")


def merge_block(target, section_hint, block, video_title):
    """Append a distilled block into the right TOPIC file (not the index), under the
    section the distiller named when it matches an existing heading, else at the end.

    Warns when a topic file grows past TOPIC_BUDGET. The absence of exactly this
    check is what let AL-KNOWLEDGE reach ~57k tokens — well past the coder's 32k
    num_ctx — before anyone noticed."""
    path = pick_topic(target, section_hint) or os.path.join(REFERENCE, target)
    text = open(path, encoding="utf-8").read()
    stamp = f"<!-- ingested: {video_title} | {datetime.date.today().isoformat()} -->"
    payload = f"\n\n{stamp}\n{block.strip()}\n"

    heads = [(m.start(), m.end(), m.group(0)) for m in re.finditer(r"^#{2,3} .*$", text, re.M)]
    idx = None
    if section_hint:
        norm = re.sub(r"[^a-z0-9]+", " ", section_hint.lower()).strip()
        for i, (_, _, h) in enumerate(heads):
            hn = re.sub(r"[^a-z0-9]+", " ", h.lower()).strip()
            if norm and (norm in hn or hn in norm):
                idx = i
                break
    if idx is None:
        new = text.rstrip() + payload
    else:
        end = heads[idx + 1][0] if idx + 1 < len(heads) else len(text)
        new = text[:end].rstrip() + payload + "\n" + text[end:]
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(new)
    tk = len(new) / TOK
    if tk > TOPIC_BUDGET / 1000:
        print(f"  ⚠ {os.path.basename(path)} is now ~{tk:.1f}k tokens (budget "
              f"{TOPIC_BUDGET/1000:.0f}k) — split it: "
              f"pipeline/split_knowledge.py plan {target}")
    where = heads[idx][2] if idx is not None else "(end of file)"
    return f"{os.path.relpath(path, REFERENCE)} → {where}"


def cmd_run(args):
    keeps = parse_plan(args.plan)
    if not keeps:
        print("No KEEP rows in plan.")
        return 1
    if git_dirty() and not args.force:
        print("ERROR: reference/ has uncommitted changes. Commit first so an auto-merge "
              "is trivially revertable, or pass --force.")
        return 1
    print(f"{len(keeps)} video(s) to ingest.\n")

    merged = skipped = 0
    for i, k in enumerate(keeps, 1):
        print(f"[{i}/{len(keeps)}] {k['title']}")
        import time
        # by ID, not title slug — the plan truncates titles, and a truncated title
        # slugifies to a different filename than the archived transcript.
        path = vc.find_archived(k["id"], k["title"]) or vc.archive_path(k["id"], k["title"])
        if vc.detect_source(k["id"]) != "youtube":
            # web article: full text is not archived by default, so distil from the
            # text we just fetched rather than re-reading the (stub) archive record.
            if os.path.exists(path):
                print("  already ingested.")
                skipped += 1
                continue
            got = vc.fetch_web({"url": k["id"], "id": k["id"], "title": k["title"]})
            if not got:
                skipped += 1
                continue
            transcript = got["text"]
            time.sleep(vc.FETCH_SLEEP)
        elif not os.path.exists(path):
            meta = {"id": k["id"], "title": k["title"],
                    "url": f"https://www.youtube.com/watch?v={k['id']}"}
            info = subprocess.run(vc.BASE + ["-J", "--skip-download", meta["url"]],
                                  capture_output=True, text=True, timeout=300)
            try:
                m = json.loads(info.stdout)
                meta.update({"title": m.get("title", k["title"]),
                             "duration": m.get("duration", 0),
                             "upload_date": m.get("upload_date", ""),
                             "channel": m.get("channel", "")})
            except json.JSONDecodeError:
                pass
            path = vc.fetch(meta)
            if not path:
                skipped += 1
                continue
            time.sleep(vc.FETCH_SLEEP)
            transcript = open(path, encoding="utf-8").read()
        else:
            transcript = open(path, encoding="utf-8").read()
        target = k["target"]
        # Offer the TOPIC FILES as filing choices — the root file is only an index.
        tops = topic_files(target)
        headings = "\n".join(
            f"- {os.path.basename(f)}: " +
            (next((l[2:].strip() for l in open(f, encoding='utf-8') if l.startswith('# ')), ''))
            for f in tops) or "(no topic files yet)"
        prompt = (
            f"Below is cleaned text from a Business Central source (video transcript or "
            f"blog article). Distil the "
            f"durable, developer-relevant knowledge into notes for {target} "
            f"({TARGETS[target]}).\n\n"
            "Rules:\n"
            "- Write ORIGINAL technical notes in your own words. Do NOT reproduce the "
            "source text or quote more than a short phrase from it.\n"
            "- Facts, APIs, behaviours, gotchas, procedures only. Drop all marketing, "
            "filler, anecdotes and presenter chatter.\n"
            "- Video text comes from auto-generated captions, which garble identifiers. Any API "
            "or object name you are not confident of, mark `[sic?]` and add a note to "
            "verify against Microsoft Learn or the compiler.\n"
            "- Terse markdown bullets under a `### <topic>` heading. No preamble.\n"
            "- If there is nothing worth keeping, reply exactly: NOTHING\n\n"
            + (f"Name the TOPIC this belongs to: reuse one of the existing topic names "
               f"below if it fits, else propose a short kebab-case subject (e.g. "
               f"copilot-agents, security-permissions, cloud-migration). Existing topics:\n"
               if target in OPEN_TARGETS else
               f"Topic files in {target} — the \"section\" field of your JSON reply "
               f"names which one this belongs in:\n")
            + f"{headings}\n\n"
            + ("" if target in OPEN_TARGETS else
               'If none of them is a genuine fit, set "section" to "NEW: <short subject>". '
               'A new topic is far better than appending to a loosely related one, which '
               'bloats it past the ~8k budget and buries the material where nobody looks.\n\n')
            + 'Reply ONLY as JSON, nothing before or after it: '
              '{"section": "<topic filename, or NEW: subject>", '
              '"content": "<markdown notes>"}\n\n'
            f"--- TRANSCRIPT ---\n{transcript[:120000]}"
        )
        try:
            reply = run_claude(prompt, f"distil {i}")
            if re.sub(r'[\s"\'`*.]+', "", reply).upper().startswith("NOTHING"):
                print("  nothing worth keeping.")
                skipped += 1
                continue
            got = _distil_reply(reply, prompt, f"distil {i}")
            content = (got.get("content") or "").strip()
            if not content or content.upper() == "NOTHING":
                print("  nothing worth keeping.")
                skipped += 1
                continue
            where = merge_block(target, got.get("section"), content, k["title"])
            # Re-register AFTER the merge. register_topic() runs when a topic file is
            # first created, at which point the file is a header stub — so a brand-new
            # topic was indexed at its stub size and never corrected. The mcp-tooling
            # topic landed as "~0.1k tok" for 8151 chars, a 20x understatement, while
            # every pre-existing row was accurate. The index sizes are what the budget
            # warnings quote, and understating one is how a topic slips past the 8k
            # limit unnoticed. Idempotent: an existing row keeps its subject and every
            # size is recomputed from disk.
            try:
                # merge_block returns "<relpath-from-REFERENCE> → <location>"
                register_topic(target,
                               os.path.join(REFERENCE, where.split(" → ")[0].strip()),
                               got.get("section") or "")
            except Exception:
                pass
            print(f"  merged into {target} under {where}")
            merged += 1
        except Exception as e:
            print(f"  distil failed ({e}) — transcript archived, not merged.")
            skipped += 1

    print(f"\nDone. {merged} merged, {skipped} skipped.")
    print("Review with: git -C %s diff reference/" % REPO)
    return 0


def main():
    ap = argparse.ArgumentParser(prog="run-ingest", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("scan"); s.add_argument("--channel", required=True)
    s.add_argument("--limit", type=int); s.add_argument("--plan")
    r = sub.add_parser("run"); r.add_argument("--plan", required=True)
    r.add_argument("--force", action="store_true")
    a = ap.parse_args()
    return cmd_scan(a) if a.cmd == "scan" else cmd_run(a)


if __name__ == "__main__":
    sys.exit(main())
