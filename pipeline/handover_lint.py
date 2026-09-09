#!/usr/bin/env python3
"""
handover_lint — validate a project's handover/spec BEFORE spending a build on it.

Written after nine separate fixture defects were found in one day, every one of which
presented as a *model* failure and cost hours of GPU time to chase:

  1. manifest demanded `.PageExtension.al`; AL-REFERENCE §2 specifies `.PageExt.al`
  2. same for `.TableExtension.al` vs `.TableExt.al`
  3. app.json written as prose bullets — write_canonical_app_json() needs a ```json block
  4. ...under a plain `## app.json` heading; a '### app.json' heading fails its regex silently
  5. no permission set, while PerTenantExtensionCop makes that a hard error (PTE0004)
  6. `"target": "OnPrem"` -> PTE0005; `"Extension"` -> AL0666 at runtime 16.0. Omit it.
  7. permission set described in prose -> AL0195 (`table X = RIMD`; RIMD is for tabledata)
  8. manifest, cleanup.sh EXPECTED and disk disagreeing with each other
  9. spec naming a BC object that does not exist (`Document Attachment Mgt` vs `Mgmt`),
     and telling the model to "confirm the event name" for an event that is not published

Every one of these is mechanically checkable in seconds. A build is not.

  handover_lint.py <project-dir> [more...]     lint one or more projects
  handover_lint.py --all                       lint every known fixture
  handover_lint.py --generic <project-dir>     manifest checks only (Go/C# projects —
                                               no app.json/permission-set/BC-name checks;
                                               a MISSING manifest is fine there, the
                                               runner falls back to ">=1 source file")

Exit code 1 if any ERROR is found (warnings do not fail).
"""
import os, re, sys, json, glob

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

# Contracts copied from run-build.py — if those change, these must too.
MANIFEST_ABS = re.compile(r"^(?:[A-Za-z]:[\\/]|[\\/])")
APPJSON_RE = re.compile(r'##\s*app\.json.*?```json\s*(\{.*?\})\s*```', re.DOTALL | re.IGNORECASE)

# AL-REFERENCE §2 file suffixes. The long forms are the classic defect.
BAD_SUFFIX = {
    ".pageextension.al": ".PageExt.al",
    ".tableextension.al": ".TableExt.al",
    ".enumextension.al": ".EnumExt.al",
    ".reportextension.al": ".ReportExt.al",
}


class Report:
    def __init__(self, name):
        self.name, self.errors, self.warns = name, [], []

    def err(self, code, msg):
        self.errors.append((code, msg))

    def warn(self, code, msg):
        self.warns.append((code, msg))


def _handover(project):
    hits = sorted(glob.glob(os.path.join(project, "*andover*.md")))
    return hits[0] if hits else None


def check_manifest(text, project, r, generic=False):
    """The manifest must parse the way run-build.py parses it, not merely look right."""
    idx = text.lower().rfind("machine-readable manifest")
    if idx == -1:
        r.err("MAN001", "no 'machine-readable manifest' heading — parse_manifest returns [] "
                        "and the AL runner aborts the build")
        return []
    block = re.search(r"```[^\n]*\n(.*?)```", text[idx:], re.DOTALL)
    if not block:
        r.err("MAN002", "no fenced block after the manifest heading")
        return []
    files = [os.path.normpath(l.strip()) for l in block.group(1).splitlines()
             if MANIFEST_ABS.match(l.strip())]
    if not files:
        r.err("MAN003", "manifest block contains no absolute paths (relative paths are ignored)")
    # a later mention of the phrase would hijack rfind()
    if text.lower().count("machine-readable manifest") > 1:
        r.warn("MAN004", "the phrase 'machine-readable manifest' appears more than once — "
                         "parse_manifest uses the LAST one; make sure that is the real block")
    if generic:                  # Go/C#: suffix and app.json rules are AL-only
        return files
    for f in files:
        low = f.lower()
        for bad, good in BAD_SUFFIX.items():
            if low.endswith(bad):
                r.err("NAM001", f"{os.path.basename(f)} uses {bad} — AL-REFERENCE §2 says {good}")
    if not any(os.path.basename(f) == "app.json" for f in files):
        r.warn("MAN005", "app.json is not in the manifest")
    return files


def check_appjson(text, r):
    m = APPJSON_RE.search(text)
    if not m:
        r.err("APP001", "no `## app.json` section with a literal ```json block — "
                        "write_canonical_app_json() silently bails and the model authors "
                        "app.json itself, which mangles id/version/idRanges")
        return None
    try:
        d = json.loads(m.group(1))
    except json.JSONDecodeError as e:
        r.err("APP002", f"app.json block is not valid JSON: {e}")
        return None
    if "target" in d:
        r.err("APP003", f'"target": "{d["target"]}" is set — omit it. OnPrem trips PTE0005, '
                        f"Extension trips AL0666 at runtime 16.0; the fixtures that build "
                        f"clean set no target at all")
    for k in ("id", "name", "publisher", "version", "runtime", "idRanges"):
        if k not in d:
            r.warn("APP004", f"app.json block has no '{k}'")
    rng = d.get("idRanges")
    if isinstance(rng, list) and rng and not {"from", "to"} <= set(rng[0]):
        r.err("APP005", f"idRanges entry needs 'from'/'to', got {list(rng[0])}")
    return d


def check_permissionset(text, files, r):
    """PTE0004 makes a missing permission set a hard error once the extension adds a table."""
    adds_table = any(f.lower().endswith(".table.al") for f in files)
    has_ps = any(f.lower().endswith(".permissionset.al") for f in files)
    if adds_table and not has_ps:
        r.err("PRM001", "extension adds a table but no .PermissionSet.al is in the manifest — "
                        "PerTenantExtensionCop raises PTE0004")
    if not has_ps:
        return
    # the block must be literal: prose produced `table X = RIMD` (AL0195) on every model
    blocks = re.findall(r"```al\s*(.*?)```", text, re.DOTALL | re.IGNORECASE)
    ps = next((b for b in blocks if re.search(r"^\s*permissionset\s", b, re.M | re.I)), None)
    if ps is None:
        r.err("PRM002", "permission set is described but no literal ```al permissionset block — "
                        "models then guess and write `table X = RIMD`, which is AL0195")
        return
    for m in re.finditer(r"^\s*(table|tabledata|page|codeunit|report|query|xmlport)\s+"
                         r"(\"[^\"]+\"|\S+)\s*=\s*([A-Za-z]+)", ps, re.M | re.I):
        kind, name, perm = m.group(1).lower(), m.group(2), m.group(3).upper()
        if kind == "tabledata":
            if not set(perm) <= set("RIMDX"):
                r.err("PRM003", f"tabledata {name} = {perm} is not a valid permission")
        elif perm != "X":
            r.err("PRM004", f"{kind} {name} = {perm} is invalid — the OBJECT takes only X "
                            f"(RIMD belongs on tabledata). This is AL0195")


AL_KEYWORDS = {
    "begin", "end", "var", "if", "then", "else", "exit", "procedure", "trigger", "local",
    "repeat", "until", "while", "for", "do", "case", "of", "with", "true", "false",
    "codeunit", "table", "page", "record", "interface", "enum", "report", "query",
    "and", "or", "not", "in", "downto", "to", "temporary", "label", "text", "integer",
    "boolean", "decimal", "date", "time", "datetime", "guid", "blob", "media", "option",
}
# AL system objects that are globally available — never declared in a var block.
AL_BUILTINS = {
    "isolatedstorage", "session", "database", "system", "format", "message", "error",
    "dialog", "file", "system.utilities", "currpage", "currreport", "page", "report",
    "codeunit", "xmlport", "query", "webserviceaction", "usersettings",
}


def check_snippet_vars(text, r):
    """Every identifier a code snippet USES must also be declared somewhere in the spec.

    Defect #11: the "Auth / init" snippet used `Authorize` and `SSAuthorization` but never
    showed their declarations, so the model copied it verbatim and never wrote a `var`
    block — AL0118 x36, on a run where the earlier AL0118 defect had already been fixed.
    """
    blocks = re.findall(r"```al\s*(.*?)```", text, re.DOTALL | re.IGNORECASE)
    if not blocks:
        return
    declared, used = set(), {}
    for b in blocks:
        # `Name: Type` in a var block, or a procedure parameter list
        for m in re.finditer(r"^\s*(\w+)\s*:\s*\w", b, re.M):
            declared.add(m.group(1).lower())
        for m in re.finditer(r"\(([^)]*)\)", b):
            for part in m.group(1).split(";"):
                mm = re.match(r"\s*(?:var\s+)?(\w+)\s*:", part)
                if mm:
                    declared.add(mm.group(1).lower())
        # an identifier that receives an assignment or has a method called on it
        for m in re.finditer(r"^\s*(\w+)\s*:=|(?<![\w.])(\w+)(?:\.\w+)+\s*\(", b, re.M):
            name = (m.group(1) or m.group(2))
            if (name and name.lower() not in AL_KEYWORDS
                    and name.lower() not in AL_BUILTINS and not name.isupper()):
                used.setdefault(name.lower(), name)
    missing = sorted(n for k, n in used.items() if k not in declared)
    # `Rec`, `Setup` etc. are conventionally supplied by context; flag the rest
    missing = [m for m in missing if m.lower() not in {"rec", "xrec", "setup", "currpage"}]
    if missing:
        r.err("VAR001", f"snippet uses {', '.join('`'+m+'`' for m in missing[:4])} but the spec "
                        f"never declares them — the model copies the snippet and omits the "
                        f"`var` block (AL0118)")


def check_cleanup(project, files, r):
    cs = os.path.join(project, "cleanup.sh")
    if not os.path.exists(cs):
        r.warn("CLN001", "no cleanup.sh")
        return
    txt = open(cs, encoding="utf-8", errors="replace").read()
    m = re.search(r"^ROOT=(.*)$", txt, re.M)
    if m and "dirname" not in m.group(1):
        r.err("CLN002", f"cleanup.sh hardcodes ROOT={m.group(1).strip()} — a copied project "
                        f"then cleans the ORIGINAL directory. Use $(cd \"$(dirname \"$0\")\" && pwd)")
    if re.search(r"^\s*EXPECTED=\(\s*\)", txt, re.M) or "HANDOVER=" in txt:
        # EXPECTED is built at runtime by parsing the handover — nothing to compare,
        # and it cannot drift out of sync by construction.
        return
    listed = set(re.findall(r'"\$ROOT/([^"]+)"', txt))
    manifest_rel = {os.path.relpath(f, project) for f in files} if files else set()
    if listed and manifest_rel:
        only_clean = listed - manifest_rel
        only_man = manifest_rel - listed
        if only_clean:
            r.err("CLN003", f"cleanup.sh EXPECTED has {len(only_clean)} entry(s) not in the "
                            f"manifest: {sorted(only_clean)[:3]}")
        if only_man:
            r.err("CLN004", f"manifest has {len(only_man)} file(s) missing from cleanup.sh "
                            f"EXPECTED: {sorted(only_man)[:3]}")


def _own_object_names(files):
    """Object names THIS project declares, derived from its manifest filenames:
    CustomerCardMapExt.PageExt.al -> {customercardmapext, customer card map ext}."""
    out = set()
    for f in files:
        stem = os.path.basename(f).split(".")[0]
        if not stem:
            continue
        out.add(stem.lower())
        spaced = re.sub(r"(?<!^)(?=[A-Z])", " ", stem).lower().strip()
        out.add(spaced)
        out.add(spaced.replace("ext", "extension"))
    return out


def check_bc_names(text, r, files=None, symdir=None):
    """Names the spec tells the model to use must exist. Defect #9 was a spec instructing
    a subscription to an event on a codeunit that does not exist, then telling the model to
    'confirm the exact event name' — a confirmation it could never obtain."""
    if not symdir:
        cands = glob.glob("/mnt/rojaws/localDev/projects/bench/runs/*/.alpackages")
        symdir = cands[0] if cands else None
    if not symdir:
        r.warn("SYM001", "no .alpackages found — BC object names not verified")
        return
    try:
        import al_symbols
        idx = al_symbols.build_index(symdir)
    except Exception as e:
        r.warn("SYM002", f"symbol index unavailable ({e})")
        return
    if not idx:
        r.warn("SYM003", "symbol index empty")
        return
    # The app.json block names DEPENDENCIES ("Base Application", publisher "Microsoft"),
    # not objects — scanning it produced pure noise.
    body = APPJSON_RE.sub("", text)
    own = _own_object_names(files or [])
    obj_ctx = re.compile(
        r'(?:Record|Codeunit|Page|Report|Enum|Query|XmlPort|Interface|table|tableextension|'
        r'pageextension|codeunit|page)\s+(?:\d+\s+)?"([A-Z][A-Za-z0-9 .\-]{3,40})"'
        r'|on\s+(?:table|codeunit|page)\s+\d*\s*"([A-Z][A-Za-z0-9 .\-]{3,40})"',
        re.IGNORECASE)
    names = {g for m in obj_ctx.finditer(body) for g in m.groups() if g}
    for name in sorted(names):
        low = name.lower()
        if low in idx:
            continue
        # names this project declares itself are not BC objects
        if low in own or low.replace(" ", "") in {o.replace(" ", "") for o in own}:
            continue
        if re.match(r"(tsg|bench)", low):
            continue
        near = [k for k in idx if k.startswith(low[:12])][:2]
        if near:
            r.err("SYM004", f'spec references "{name}" which is not in the symbols — '
                            f'did you mean {" / ".join(idx[n]["name"] for n in near)}?')
        else:
            r.warn("SYM005", f'spec references "{name}", not found in symbols (may be '
                             f'project-defined or a caption)')


def lint(project, generic=False):
    r = Report(os.path.basename(project.rstrip("/")))
    h = _handover(project)
    if not h:
        r.err("GEN001", "no handover file (*andover*.md)")
        return r
    text = open(h, encoding="utf-8", errors="replace").read()
    if generic:
        # Go/C# runners treat the manifest as optional (fallback: >=1 source file
        # written) — only lint it when the author chose to include one.
        if "machine-readable manifest" in text.lower():
            check_manifest(text, project, r, generic=True)
        return r
    files = check_manifest(text, project, r)
    check_appjson(text, r)
    check_permissionset(text, files, r)
    check_snippet_vars(text, r)
    check_cleanup(project, files, r)
    check_bc_names(text, r, files)
    return r


def main():
    args = sys.argv[1:]
    generic = "--generic" in args
    args = [a for a in args if a != "--generic"]
    if not args or args[0] == "--all":
        args = sorted(glob.glob("/mnt/rojaws/localDev/projects/*/"))
        args = [a for a in args if _handover(a)]
    bad = 0
    for p in args:
        r = lint(p, generic=generic)
        if not r.errors and not r.warns:
            print(f"  ✓ {r.name}")
            continue
        print(f"\n  {'✗' if r.errors else '!'} {r.name}")
        for c, m in r.errors:
            print(f"      ERROR {c}  {m}")
        for c, m in r.warns:
            print(f"      warn  {c}  {m}")
        bad += bool(r.errors)
    print(f"\n  {bad} project(s) with errors")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
