#!/usr/bin/env python3
"""
split_knowledge — turn a monolithic knowledge file into an index + topic files.

Why: the coder is served at num_ctx=32768, and both curated knowledge files grew
past that (AL-REFERENCE ~47k tokens, AL-KNOWLEDGE ~57k), so the handover's "read
this before writing AL" instruction became impossible to satisfy. Splitting into
topic files small enough to read whole restores that, and keeps `kb` retrieval
pointing at a meaningful unit instead of a chunk of a monolith.

Re-runnable: it reads the ORIGINAL monolith from git if the working copy has
already been replaced by an index, so a later ingestion round can re-split.

  split_knowledge.py plan <file.md>        show sections + sizes, propose grouping
  split_knowledge.py apply <file.md>       write topic files + rewrite root as index

Grouping is declared in TOPICS below — deliberately explicit rather than automatic,
because where a split lands matters for whether a topic reads coherently.
"""
import os, re, sys, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.environ.get("LARRY_REPO", os.path.dirname(HERE))
REFERENCE = os.path.join(REPO, "reference")
TOK = 3700          # bytes per token, rough, for tech prose
BUDGET = 8000       # target max tokens per topic file

# Topic groupings. Keys are the output filename; values are the "## " section
# numbers (or, for a sub-split, a (section, start_subhead, end_subhead) triple).
# end_subhead is exclusive; None means "to the end of the section".
TOPICS = {
    "AL-KNOWLEDGE.md": {
        "dir": "al-knowledge",
        "groups": [
            ("platform-runtime.md", "Scale design, NuGet packaging, app packaging",
             [(1, None, "Handling large/high-concurrency BC SaaS customers")]),
            ("performance-concurrency.md", "Large customers, job queues, locking, BCPT",
             [(1, "Handling large/high-concurrency BC SaaS customers",
                  "Performance in BC — locking, finds, telemetry")]),
            ("performance-telemetry.md", "Performance sessions, telemetry & App Insights",
             [(1, "Performance in BC — locking, finds, telemetry",
                  "Table indexes & SIFT — planning for performance")]),
            ("indexes-sift.md", "Table indexes, SIFT, NCCI, full-text, key ordering",
             [(1, "Table indexes & SIFT — planning for performance", None)]),
            ("reporting-powerbi.md", "Reporting, Power BI, Excel layouts", [2]),
            ("testing-automation.md", "Test automation, mocking, datasets, code-review tooling",
             [(3, None, "Page scripting, data-driven testing & AL coded tests")]),
            ("testing-patterns.md", "Page scripting, test doubles, Kiota clients, WireMock",
             [(3, "Page scripting, data-driven testing & AL coded tests", None)]),
            ("cicd-algo.md", "CI/CD with AL-Go for GitHub", [4]),
            ("ai-platform.md", "AI resources, agent platform, billing & models", [5]),
            ("developer-apis.md", "API pages, integration patterns, event grid master-data sync",
             [(6, None, "Power Automate flows for BC")]),
            ("integration-powerplatform.md", "Power Automate, Power Platform ALM, web hooks",
             [(6, "Power Automate flows for BC", None)]),
            ("functional-features.md", "Functional feature awareness", [7]),
            ("docs-pointers.md", "Docs & learning pointers", [8]),
        ],
    },
    "AL-REFERENCE.md": {
        "dir": "al-reference",
        "groups": [
            ("00-gotchas.md", "LLM gotcha summary — READ FIRST", [0]),
            ("01-syntax-style.md", "Formatting, naming, structure, variables, flow, abbreviations",
             [1, 2, 3, 4, 9, 17]),
            ("02-objects.md", "Tables, codeunits, pages, reports, factboxes & control add-ins",
             [5, 6, 7, 8, 19]),
            # §10 had drifted: ingestion's fuzzy heading match filed "New AL language
            # features" and the HTTP client material under "Record Operations &
            # Performance". The split re-files them where they belong.
            ("03-records-performance.md", "Record operations, data access, SQL-level tuning, locking",
             [(10, None, "Validate() triggers — behaviour, patterns, gotchas")]),
            ("04-validate.md", "Validate() triggers — behaviour, patterns, gotchas",
             [(10, "Validate() triggers — behaviour, patterns, gotchas",
                   "New AL language features")]),
            ("05-language-features.md", "Newer AL language features (what's-new rollups)",
             [(10, "New AL language features", "HTTP client mocking in tests")]),
            ("06-http-client.md", "HttpClient, RestClient, mocking, JSON/YAML test utils",
             [(10, "HTTP client mocking in tests", None)]),
            ("07-events-errors.md", "Events & subscribers, error handling, archiving, upgrade codeunits",
             [11, 12, 20, 21]),
            ("08-data-storage.md", "Streams & blobs, isolated storage, Azure Blob Storage",
             [13, 14, 15]),
            ("09-api-web.md", "API pages / web services, interfaces, permission sets",
             [23, 24, 26]),
            ("10-quality-breaking.md", "PTE conventions, signature verification, obsoletion, extra rules",
             [16, 18, 22, 25, 27]),
            ("11-agents.md", "AI agents in BC — functional concepts & setup", [28]),
            ("12-agents-coding.md", "Coding agents in AL, agent testing, BC MCP server",
             [29, 30, 31]),
            ("13-testing.md", "AL test codeunits", [32]),
            ("14-namespaces.md", "Namespaces & `using`", [33]),
        ],
    },
}


def original_text(path):
    """The monolith. If the working copy is already an index (no '## 1.'), recover
    the pre-split version from git so this stays re-runnable."""
    t = open(path, encoding="utf-8").read()
    if re.search(r"^## (?:1\.|LLM Gotcha)", t, re.M):
        return t
    rel = os.path.relpath(path, REPO)
    for rev in ("HEAD", "HEAD~1", "HEAD~2", "HEAD~3"):
        try:
            out = subprocess.run(["git", "-C", REPO, "show", f"{rev}:{rel}"],
                                 capture_output=True, text=True, check=True).stdout
            if re.search(r"^## (?:1\.|LLM Gotcha)", out, re.M):
                print(f"  (recovered monolith from {rev})")
                return out
        except subprocess.CalledProcessError:
            pass
    raise SystemExit(f"ERROR: {path} looks split already and no monolith found in git")


def parse_sections(text):
    """{section_number: (heading, body)} plus ('_pre', preamble). Section 0 is the
    unnumbered 'LLM Gotcha Summary' page that leads AL-REFERENCE."""
    heads = [(m.start(), m.end(), m.group(0)) for m in re.finditer(r"^## .*$", text, re.M)]
    out = {"_pre": text[:heads[0][0]] if heads else text}
    for i, (s, e, h) in enumerate(heads):
        end = heads[i + 1][0] if i + 1 < len(heads) else len(text)
        m = re.match(r"^## (\d+)\.", h)
        num = int(m.group(1)) if m else 0
        out[num] = (h.strip(), text[s:end])
    return out


def slice_subheads(body, start_sub, end_sub):
    """Cut a section between two '### ' subheadings. Boundaries always land on a
    subheading so a topic file never starts mid-explanation."""
    subs = [(m.start(), m.group(1).strip()) for m in re.finditer(r"^### (.*)$", body, re.M)]
    a = 0
    if start_sub:
        for pos, name in subs:
            if name.startswith(start_sub[:40]):
                a = pos
                break
    b = len(body)
    if end_sub:
        for pos, name in subs:
            if pos > a and name.startswith(end_sub[:40]):
                b = pos
                break
    head = body[:body.index("\n")] + "\n\n" if a > 0 else ""
    return head + body[a:b]


def build(path, spec, apply=False):
    text = original_text(path)
    secs = parse_sections(text)
    name = os.path.basename(path)
    outdir = os.path.join(REFERENCE, spec["dir"])
    rows, total = [], 0

    for fname, desc, members in spec["groups"]:
        parts = []
        for m in members:
            if isinstance(m, tuple):
                num, s_sub, e_sub = m
                if num not in secs:
                    continue
                parts.append(slice_subheads(secs[num][1], s_sub, e_sub))
            else:
                if m in secs:
                    parts.append(secs[m][1])
        if not parts:
            print(f"  WARN: {fname} matched no sections — skipped")
            continue
        body = "\n\n".join(p.rstrip() for p in parts) + "\n"
        tk = len(body) / TOK          # thousands of tokens
        total += len(body)
        flag = "  ⚠ OVER BUDGET" if tk > BUDGET / 1000 else ""
        rows.append((fname, desc, tk))
        print(f"  {tk:5.1f}k  {fname:32} {desc[:44]}{flag}")
        if apply:
            os.makedirs(outdir, exist_ok=True)
            header = (f"<!-- topic file split from {name}; edit here, not in the index -->\n"
                      f"# {desc}\n\n"
                      f"Part of [`{name}`]({os.path.relpath(path, outdir)}) — see that index for the "
                      f"other topics.\n\n---\n\n")
            with open(os.path.join(outdir, fname), "w", encoding="utf-8") as fh:
                fh.write(header + body)

    if apply:
        pre = secs["_pre"].rstrip()
        if pre.rstrip().endswith("---"):
            pre = pre.rstrip()[:-3].rstrip()
        idx = [pre, "", "---", "",
               "## How to use this file",
               "",
               f"This is an **index**, not the content. The knowledge lives in "
               f"[`{spec['dir']}/`]({spec['dir']}/) as topic files, each small enough to read whole.",
               "",
               "**Read this index, then read only the topic file(s) you need.** Do not read every "
               "topic — together they far exceed a 32k context window. To search across all topics "
               f"instead: `kb search \"<query>\" --corpus {spec['dir']}`.",
               "", "## Topics", "",
               "| Topic | Covers | Size |", "|---|---|---|"]
        for fname, desc, tk in rows:
            idx.append(f"| [`{fname}`]({spec['dir']}/{fname}) | {desc} | ~{tk:.1f}k tok |")
        idx += ["", f"_Total across topics: ~{total/TOK:.0f}k tokens. "
                    f"Split from the former single file by `pipeline/split_knowledge.py`._", ""]
        with open(path, "w", encoding="utf-8") as fh:
            fh.write("\n".join(idx))
        print(f"  → wrote {len(rows)} topic files + rewrote {name} as index "
              f"(~{len(chr(10).join(idx))/TOK:.1f}k tok)")
    print(f"  TOTAL content ~{total/TOK:.0f}k tokens (was one file)")


def main():
    if len(sys.argv) < 3 or sys.argv[1] not in ("plan", "apply"):
        print(__doc__)
        return 2
    mode, target = sys.argv[1], os.path.basename(sys.argv[2])
    if target not in TOPICS:
        print(f"no grouping declared for {target}; known: {', '.join(TOPICS)}", file=sys.stderr)
        return 2
    print(f"=== {target} ({mode}) ===")
    build(os.path.join(REFERENCE, target), TOPICS[target], apply=(mode == "apply"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
