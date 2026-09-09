# Larry Handover — [PROJECT NAME]

<!--
TEMPLATE INSTRUCTIONS (delete this block before use):

`alw new` substitutes these placeholders for you, in the right form for THIS host
(Windows gets `C:/Users/...`, Linux gets `/home/...` or `/mnt/...`):
  [PROJECT NAME]  extension / project name
  [PROJECT ROOT]  absolute path to this project dir — used by the filesystem rules,
                  the Strategy A file paths, and the machine-readable manifest
  [SETUP DIR]     the larry-setup repo (AL-REFERENCE.md lives under it)
  [CODE AL]       the promoted-AL tree that holds pastes/
If you are writing a handover BY HAND, replace all four yourself. Do NOT leave a
`/mnt/rojaws/...` path in on a non-Linux box, and do NOT use Git-Bash `/c/...` form
on Windows — the manifest parser and write-gate both need the native form.

Then:
1. Fill in "What you are building"
2. Fill in "Read first" paths for this project's docs
3. Fill in "AL examples" — list only relevant paste files and what pattern to extract
4. Fill in project-specific sections (tasks, patterns, conventions)
5. Set the object ID range
6. Delete any sections not relevant to this project
-->

## What you are building

<!-- One paragraph. State: what the extension does, what it extends, the core mechanism. -->
[Describe the extension purpose, what BC table/functionality it extends, and the main technical approach.]

## Filesystem tool rules

Use your built-in **write** and **edit** tools to create and change files. Do not invoke any
`*_mcp_filesystem` tool — those do not exist here.

ALWAYS use absolute paths starting with `[PROJECT ROOT]` for ALL tool calls. NEVER use relative paths.
Use that exact form — on Windows it is a drive-letter path (`C:/Users/...`); a Git-Bash `/c/...` path
is NOT interchangeable and makes the pipeline's write-gate report "0 files written".

File names must use EXACT extensions — NEVER append `.txt`. AL files end in `.al`.
Example: `PTEMyObject.Codeunit.al` NOT `PTEMyObject.Codeunit.al.txt`

Write each file directly to its full path. If a write fails because the directory is missing,
create it first with the bash tool (`mkdir -p`), then retry the write.
Do NOT run the compiler, `al`, or any build command yourself — the pipeline does that after you write.

## Read first

The AL syntax rules you must follow are **already injected at the top of this prompt** (the
"# AL rules you MUST follow" section, added by the pipeline). Do NOT go and read
`AL-REFERENCE.md` or its topic files yourself — they will not fit in your context and the
relevant ones are already above. If a rules section is NOT present above, read ONLY
`[SETUP DIR]/reference/al-reference/00-gotchas.md` plus the 1–2 topic files this project
needs — never all of them.

Project docs to read:
1. `docs/SPEC.md` — full spec, architecture, objects to create
2. `docs/TASKS.md` — task breakdown with acceptance criteria
3. `docs/AL-PROJECT-STRUCTURE.md` — folder layout and file naming rules. Follow exactly.

## AL examples — READ PATTERN ONLY, DO NOT COPY

<!--
List only paste files relevant to this project.
For each file, list ONLY the specific patterns to extract.
-->

Examples are in `[CODE AL]/pastes/`. Read them to understand patterns. **Do NOT copy any object, codeunit, table, or page from these files into this project.** Do NOT include any object not listed in `docs/SPEC.md`. Every object you write must appear in the SPEC.

| File | Extract only |
|---|---|
| `[PasteFile.al]` | [specific pattern, method signature, or code block] |

Extract only what is listed. Do not carry over unrelated objects, demo pages, test pages, or utility codeunits not required by the SPEC.

## Blocker — resolve before writing code

<!--
List any unknowns that must be confirmed before implementation starts.
Common examples: exact table/field names, event names, object IDs.
-->

Before writing any code, identify:
1. [Unknown 1 — e.g. exact table name and number]
2. [Unknown 2 — e.g. event or procedure that handles the current flow]

Search the AL workspace or ask the team. All subsequent tasks depend on this.

## File specification approach

Choose ONE of the following strategies. The verbatim checklist is strongly preferred when file count is known and small.

### Strategy A — Verbatim file checklist (preferred for ≤~15 files)

Number each file 1–N. For each entry, give the complete file content exactly as it should be written. Larry's task becomes transcription — no authoring latitude.

Structure per entry:

```
### [N]. Write `<relative-path>`
Path: `[PROJECT ROOT]/<relative-path>`
Copy character-for-character:
<fence>
<complete verbatim file content>
</fence>
```

End the checklist with an explicit STOP:
```
## STOP
You have written all N files. Do not create any additional files. Do not run compiler tools.
```

### Strategy B — Pattern-based (only when file count is large or variable)

Paste the minimal AL code snippets for the core patterns this project needs.
Only include patterns specific to this project — common patterns are in the `AL-REFERENCE.md` topic files (see "Read first").

**Every identifier a snippet USES must be DECLARED in the same snippet** (a `var` block or a
parameter list). Models copy snippets verbatim: an undeclared `Authorize` or `SSAuthorization`
in a snippet becomes AL0118 x36 in the build, because the model never writes the missing `var`
block. `handover_lint.py` flags this as VAR001 — write snippets self-contained from the start.

### [Pattern name]
```al
// pattern code here
```

## Suffix convention

Use `PTE` (PerTenantExtension) suffix on all new objects. Example: `PTEMyMgt`, `PTEMySetup`.

Do NOT carry over other suffixes from example/paste files (e.g. `TNP`, `NHC`).

## Object ID range

<!-- Confirm with team before writing any object. -->
`[start]..[end]` — confirm exact range before writing any object.

## Guard pattern

<!--
Every guarded operation must check setup exists AND is enabled before proceeding.
Adjust setup table name and fields for this project.
-->

```al
if not PTEMySetup.Get('DEFAULT') then
    exit;
if not PTEMySetup.IsEnabled then
    exit;
```

Extension must not break existing functionality if the feature is not configured.

## app.json

<!--
REQUIRED. `write_canonical_app_json()` overwrites app.json from the FIRST ```json block
under a heading matching `## app.json` — the model must never author it itself, because it
mangles id/version/idRanges. Fill this in completely.

Do NOT set "target": OnPrem trips PTE0005 and Extension trips AL0666 at runtime 16.0. The
fixtures that build clean set no target at all. Put any extra dependencies in the
"dependencies" array BELOW, not in a separate json block — a second block under a heading
starting "## app.json" would be captured instead of this one.
-->

```json
{
  "id": "[fresh-guid]",
  "name": "[PROJECT NAME]",
  "publisher": "[publisher]",
  "version": "1.0.0.0",
  "brief": "[one line]",
  "description": "[one sentence]",
  "platform": "1.0.0.0",
  "application": "27.0.0.0",
  "runtime": "16.0",
  "idRanges": [
    {
      "from": 50100,
      "to": 50199
    }
  ],
  "dependencies": []
}
```

## Permission set

<!--
REQUIRED whenever the extension adds a table — PerTenantExtensionCop makes a missing
permission set a hard error (PTE0004). Give the permission set as a LITERAL ```al block
(prose descriptions made every model guess `table X = RIMD`, which is AL0195: objects
take only X; RIMD belongs on tabledata). Add a `<Name>.PermissionSet.al` entry to the
manifest. Delete this section only if the project adds no table.
-->

```al
permissionset 50199 "[PROJECT NAME] PTE"
{
    Assignable = true;
    Caption = '[PROJECT NAME]';
    Permissions =
        table "PTE My Table" = X,
        tabledata "PTE My Table" = RIMD,
        codeunit "PTE My Mgt" = X,
        page "PTE My Page" = X;
}
```

Rules: object entries (`table`/`page`/`codeunit`/...) take only `= X`; data access goes on
`tabledata ... = RIMD`. Every object this project creates must be listed.

## Target environment

Always target **Business Central SaaS** unless this handover explicitly states on-premises.

SaaS rules:
- No CDN URLs in ControlAddin HTML files — BC SaaS CSP blocks external scripts and stylesheets. Bundle all third-party libraries locally.
- No `SecretText` as a table field type — use `IsolatedStorage`.
- No SFTP, SMB, or filesystem APIs.
- `DataClassification` required on every table field.

## AL Syntax Essentials — compiler requirements

These are hard compiler rules, not style. Violating any one is a compile error. Larry writing from a spec (not verbatim) consistently gets these wrong unless shown ✓/✗ examples — always include the relevant ones in the handover. (Baking AL rules into a tuned model's SYSTEM does NOT reach the LibreChat agent path — the request system message replaces the Modelfile SYSTEM — so these MUST live in the handover. Baked PARAMETERs like temperature DO apply.)

**`using` directives go at the TOP — never inside the object body (THE most common break):**
Order: `namespace` → `using` lines → blank → object → `{`. A `using` after the opening `{` causes a cascade of `AL0104 '}' expected` + `AL0114` + `AL0107`. Every LLM tried so far (qwen3-coder, north-mini, qwen3.6) makes this exact mistake unless the handover shows `using` above the object explicitly.

**Object structure — declaration line THEN a brace body (most common LLM failure):**
Every object is a declaration line followed by `{ ... }` with matching braces; object id required. Include one complete correct codeunit skeleton (with `using` ABOVE the object) so the model copies the shape:
```al
namespace MyExt;
using Microsoft.Foundation.Attachment;

codeunit 50100 "My Mgt"
{
    var
        Setup: Record "My Setup";

    procedure DoWork(Input: Text): Boolean
    begin
        if Input = '' then
            exit(false);
        exit(true);
    end;
}
```
Layout inside `{ }`: triggers, then codeunit-level `var` section (valid — don't move into procedures), then procedures (`begin ... end`). Lowercase keywords.

**String literals — quote all paths/captions:**
- ✓ `Scripts = 'src/controladdin/map.js';`
- ✗ `Scripts = src/controladdin/map.js;` (AL0219: string literal expected)

**Page extension `addlast`/`addfirst` must nest in `layout { }` or `actions { }`:**
- ✓ `layout { addlast(FactBoxes) { part(...) { } } }`
- ✗ `addlast(FactBoxes) { part(...) { } }` at page-extension level (AL0104 syntax error)

**Usercontrol block — only `trigger` definitions inside:**
- ✓ `usercontrol(Name; AddinType) { trigger ControlAddInReady() begin ... end; }`
- ✗ procedures declared inside the usercontrol block — put procedures at page level

**Namespace + base-app objects need `using`:**
- A page extension declaring `namespace X;` and extending a base-app page must add the base app's namespace, e.g. `using Microsoft.Sales.Customer;` to resolve `"Customer Card"`. Without it the base object won't resolve.

## ControlAddin notes (when project has a ControlAddin)

- `HtmlFiles` is NOT a valid ControlAddin property — do not use it (AL0124). Create any DOM elements in the startup script instead.
- `Scripts`, `StartupScript`, `StyleSheets` paths are relative to the **project root** (e.g. `src/controladdin/map.js`), and must be single-quoted (see above).
- Set `runtime` in app.json to match the symbol packages on disk (mismatched runtime = symbol resolution failures).
  Get the value from `al GetLatestSupportedRuntimeVersion <platform>` — it wants the **2-part** form
  (`27.0`, not `27.0.0.0`, which errors with *"Unknown platform version"*).
- **`target` depends on the AL compiler version on THIS box** — get it wrong and no amount of fix
  rounds will help, because the pipeline rewrites `app.json` canonically from this handover every
  round, so the model cannot correct it. Observed: al **17.0** rejects `"Extension"` at runtime 16.1
  (`AL0666`) and wants `"OnPrem"`; al **18.0** rejects `"OnPrem"` (`PTE0005`) and wants
  `"Extension"`/`"Cloud"`. Check `al --version` before writing this field.

## Expected files — machine-readable manifest

End the handover with a fenced block listing every expected file as an absolute path, one per line. The build pipeline (`cleanup.sh` + reviewer manifest check) parses THIS block to delete unspecced files and flag missing ones — keep it exact and complete.

```
[PROJECT ROOT]/app.json
[PROJECT ROOT]/src/<Object>.al
...
```

## When done

State explicitly: all N files written, STOP, do not run compiler tools, do not create additional files. The pipeline runs compile + review — Larry only writes and fixes.

## Compile check

Before reporting any task complete:

1. Every object written must be in `docs/SPEC.md`.
2. No object from the paste examples exists in the project unless explicitly in the SPEC.
3. All object IDs are unique within this project.
4. No `SecretText` used as a table field type.
5. No `OnAfterInsert`/`OnAfterModify`/`OnAfterDelete` triggers on PageExtensions — use `OnInsert`/`OnModify`/`OnDelete`.
6. All procedures referenced are implemented in objects written in this project.
7. All codeunit/table names referenced match names in `app.json` dependencies or objects written in this project.
8. No ControlAddin HTML file loads scripts or styles from external URLs.
9. All ControlAddin resource paths are single-quoted and relative to project root; no `HtmlFiles` property used.
10. Page-extension `addlast`/`addfirst` blocks are nested inside `layout` or `actions`.
