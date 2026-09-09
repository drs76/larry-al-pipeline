#!/usr/bin/env python3
"""test_objref.py — object-reference detection for add_missing_using_directives().

Guards the fix for the `extends`/`implements` gap AND the declaration forms that already
worked, so closing the gap cannot silently narrow what was already detected.

    python3 test_objref.py
"""

import importlib.util
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location("runbuild", os.path.join(HERE, "run-build.py"))
_rb = importlib.util.module_from_spec(_spec)
sys.modules["runbuild"] = _rb
try:
    _spec.loader.exec_module(_rb)
except SystemExit:
    pass   # run-build.py runs its CLI on import; the regex helpers are what we want

def names(src):
    """Exactly what the caller does: sanitise, then detect."""
    return set(_rb._referenced_object_names(_rb._strip_noncode(src.splitlines())))

CASES = [
    # ---- the gap this fix closes -------------------------------------------------
    ('tableextension 50110 "PTE Doc Attachment Ext" extends "Document Attachment"',
     {"Document Attachment"}, "extends, quoted"),
    ('pageextension 50111 "PTE Doc Att List" extends "Document Attachment List"',
     {"Document Attachment List"}, "pageextension extends"),
    ('enumextension 50112 "PTE Src Type" extends "Attachment Entity Buffer Document Type"',
     {"Attachment Entity Buffer Document Type"}, "enumextension extends"),
    ("tableextension 50113 PTECust extends Customer",
     {"Customer"}, "extends, unquoted"),
    ('codeunit 50100 "PTE Blob Store" implements "IBlobStore"',
     {"IBlobStore"}, "implements, single"),
    ('codeunit 50101 "PTE Multi" implements "IBlobStore", ITelemetry, "IAudit Log"',
     {"IBlobStore", "ITelemetry", "IAudit Log"}, "implements, comma list"),
    ('tableextension 50114 "X" extends "Document Attachment"\n{\n    fields\n    {',
     {"Document Attachment"}, "header followed by body brace"),

    # ---- regression: declaration forms that already worked ------------------------
    ('        TempBlob: Codeunit "Temp Blob";', {"Temp Blob"}, "Codeunit var"),
    ('        TenantMedia: Record "Tenant Media";', {"Tenant Media"}, "Record var"),
    ('        DocAtt: Record "Document Attachment";', {"Document Attachment"}, "Record var quoted"),
    ("        Cust: Record Customer;", {"Customer"}, "Record var unquoted"),
    ('    if Page.RunModal(Page::"Customer List", Cust) = Action::OK then',
     {"Customer List"}, "Page:: reference"),
    ('        Setup: Record "PTE Doc Link AZ Setup";', {"PTE Doc Link AZ Setup"}, "local object"),

    # ---- both shapes in one file --------------------------------------------------
    ('tableextension 50110 "PTE Ext" extends "Document Attachment"\n'
     '{\n    var\n        TempBlob: Codeunit "Temp Blob";\n}',
     {"Document Attachment", "Temp Blob"}, "header + declaration together"),
]

fails = 0
for src, expected, label in CASES:
    got = names(src)
    missing, extra = expected - got, got - expected
    # Extra bare identifiers are tolerated: the caller gates every name through the symbol
    # index, so an unresolvable word adds nothing. A MISSING name is a real defect.
    ok = not missing
    print(f"{'PASS' if ok else 'FAIL'}  {label}")
    if not ok:
        print(f"        expected ⊇ {sorted(expected)}")
        print(f"        got        {sorted(got)}")
        fails += 1
    elif extra:
        print(f"        (also matched, harmless: {sorted(extra)})")

# Commented-out and quoted code must not be read as a reference.
noise = names('tableextension 50110 "X" extends "Document Attachment"\n'
              '{\n'
              '    // extends "Commented Out Name"\n'
              "    Caption = 'extends Quoted Name';\n"
              '}')
leaked = {n for n in ("Commented Out Name", "Quoted Name") if n in noise}
if leaked:
    print(f"FAIL  read a reference out of a comment/string: {sorted(leaked)}"); fails += 1
else:
    print("PASS  comments and string literals are not references")

print(f"\n{len(CASES) + 1 - fails}/{len(CASES) + 1} passed")
sys.exit(1 if fails else 0)
