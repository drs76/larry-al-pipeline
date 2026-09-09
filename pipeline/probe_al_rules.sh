#!/usr/bin/env bash
# probe_al_rules.sh — check AL-SYNTAX.md's ✗ claims against the real compiler.
#
# validate_al_syntax.py proves the ✓ patterns COMPILE. Nothing proved the ✗ patterns
# actually FAIL, or that the diagnostic codes the ruleset cites are the ones emitted.
# They weren't: rule 7 claimed per-field DataClassification was a "SaaS hard
# requirement (PTE/CodeCop)" when no cop enforces it at all, and rule 10 cited UICop
# AA0218 for a missing ApplicationArea when the real diagnostic is PTE0008.
#
# TRAP: probe pages must bind to an OWN tooltip-less table. Bound to a base-app table
# (Customer, Item...) a bare page field inherits that table's tooltip -- MS moved them
# onto table fields in 2024w1 -- and AA0218 never fires, "proving" a rule that is real.
#
# Each probe compiles one deliberately-violating object and prints the diagnostic codes
# the toolchain emits. Compare against the ruleset; where they disagree, the compiler
# wins. Expected results are in the table at the bottom.
#
# For WHICH code to expect in the first place, see
# reference/al-reference/16-analyzer-rules.md — Microsoft's authoritative AS/AA/PTE/UI
# lists. Check a cop claim there before writing it into a rule; probe it here to prove
# it actually fires.
#
# Usage: ./probe_al_rules.sh [/path/to/.alpackages]
# Needs: dotnet altool (~/.dotnet/tools/al) + BC27 symbols.
set -u

AL="$HOME/.dotnet/tools/al"
PKG="${1:-/mnt/rojaws/localDev/projects/bench-p4-unseen/.alpackages}"
WORK="$(mktemp -d)"
trap 'rm -rf "$WORK"' EXIT

ANALYZER_DIR="$(find "$HOME/.dotnet/tools/.store/microsoft.dynamics.businesscentral.development.tools" \
  -name "Microsoft.Dynamics.Nav.CodeCop.dll" 2>/dev/null | head -1 | xargs -r dirname)"
[ -z "$ANALYZER_DIR" ] && { echo "ERROR: code cop analyzers not found"; exit 1; }
[ -d "$PKG" ] || { echo "ERROR: no symbols at $PKG"; exit 1; }

ANALYZERS=()
for c in CodeCop UICop PerTenantExtensionCop; do
  ANALYZERS+=(/analyzer:"$ANALYZER_DIR/Microsoft.Dynamics.Nav.$c.dll")
done

probe() {                    # name, filename, source
  local name="$1" fname="$2" src="$3"
  local d="$WORK/$name"
  mkdir -p "$d/src"
  ln -s "$PKG" "$d/.alpackages"
  cat > "$d/app.json" <<EOF
{"id":"$(uuidgen 2>/dev/null || echo 11111111-2222-3333-4444-555555555555)","name":"P","publisher":"Probe",
"version":"1.0.0.0","platform":"27.0.0.0","application":"27.0.0.0","runtime":"16.0",
"idRanges":[{"from":50000,"to":50099}]}
EOF
  printf '%s\n' "$src" > "$d/src/$fname"
  local out
  out=$("$AL" compile /project:"$d" /packagecachepath:"$d/.alpackages" "${ANALYZERS[@]}" 2>&1 \
        | grep -oE "(error|warning) [A-Z]{2,3}[0-9]{4}" | sort -u | tr '\n' ' ')
  # PTE0004 (missing permission set) fires on every probe that declares a table — noise here.
  printf "  %-24s %s\n" "$name" "${out:-<clean>}"
}

Q="'"
echo "AL-SYNTAX ✗-claim probes (BC27 / runtime 16.0)"
echo "symbols: $PKG"
echo

probe "r5-badfilename" "WrongName.Table.al" \
"table 50000 \"Probe Tbl\" { Caption = ${Q}Probe Tbl${Q}; DataClassification = CustomerContent;
  fields { field(1; \"No.\"; Integer) { Caption = ${Q}No.${Q}; } }
  keys { key(PK; \"No.\") { Clustered = true; } } }"

probe "r7-table-level-only" "ProbeTbl.Table.al" \
"table 50000 \"Probe Tbl\" { Caption = ${Q}Probe Tbl${Q}; DataClassification = CustomerContent;
  fields { field(1; \"No.\"; Integer) { Caption = ${Q}No.${Q}; } }
  keys { key(PK; \"No.\") { Clustered = true; } } }"

probe "r7-bad-value" "ProbeTbl.Table.al" \
"table 50000 \"Probe Tbl\" { Caption = ${Q}Probe Tbl${Q}; DataClassification = CustomerContent;
  fields { field(1; \"No.\"; Integer) { Caption = ${Q}No.${Q}; DataClassification = EndUser; } }
  keys { key(PK; \"No.\") { Clustered = true; } } }"

probe "r8-no-captions-no-keys" "ProbeTbl.Table.al" \
"table 50000 \"Probe Tbl\" { DataClassification = CustomerContent;
  fields { field(1; \"No.\"; Integer) { } } }"

probe "r9-secrettext-field" "ProbeTbl.Table.al" \
"table 50000 \"Probe Tbl\" { Caption = ${Q}Probe Tbl${Q}; DataClassification = CustomerContent;
  fields { field(1; \"No.\"; Integer) { Caption = ${Q}No.${Q}; }
           field(2; Sec; SecretText) { Caption = ${Q}Sec${Q}; } }
  keys { key(PK; \"No.\") { Clustered = true; } } }"

probe "r10-field-no-apparea" "ProbeCard.Page.al" \
"page 50000 \"Probe Card\" { PageType = Card; SourceTable = Customer;
  layout { area(Content) { group(G) { field(Nm; Rec.Name) { ToolTip = ${Q}n${Q}; } } } } }"

# own table, no table-level tooltips -- otherwise inheritance masks AA0218 (see TRAP)
probe "r10-field-no-tooltip" "TTTbl.Table.al" \
"table 50001 \"TT Tbl\" { Caption = ${Q}TT Tbl${Q}; DataClassification = CustomerContent;
  fields { field(1; \"No.\"; Code[20]) { Caption = ${Q}No.${Q}; } }
  keys { key(PK; \"No.\") { Clustered = true; } } }
page 50001 \"TT Card\" { PageType = Card; SourceTable = \"TT Tbl\";
  layout { area(Content) { group(G) { field(NoF; Rec.\"No.\") { ApplicationArea = All; } } } } }"

probe "r10-action-no-tooltip" "ProbeCard.Page.al" \
"page 50000 \"Probe Card\" { PageType = Card; SourceTable = Customer;
  layout { area(Content) { group(G) { field(Nm; Rec.Name) { ApplicationArea = All; ToolTip = ${Q}n${Q}; } } } }
  actions { area(Processing) { action(Go) { ApplicationArea = All; trigger OnAction() begin end; } } } }"

probe "r11-proc-in-usercontrol" "ProbeCard.Page.al" \
"page 50000 \"Probe Card\" { PageType = Card; SourceTable = Customer;
  layout { area(Content) { usercontrol(B; \"Probe Addin\") { procedure Foo() begin end; } } } }"

probe "r13-onaftermodify" "ProbeCard.Page.al" \
"page 50000 \"Probe Card\" { PageType = Card; SourceTable = Customer;
  layout { area(Content) { group(G) { field(Nm; Rec.Name) { ApplicationArea = All; ToolTip = ${Q}n${Q}; } } } }
  trigger OnAfterModify(): Boolean begin exit(true); end; }"

probe "r14-addlast-toplevel" "ProbeExt.PageExt.al" \
"pageextension 50000 \"Probe Ext\" extends \"Customer Card\" {
  addlast(Processing) { action(A) { ApplicationArea = All; ToolTip = ${Q}n${Q}; } } }"

probe "r17-htmlfiles" "ProbeAddin.ControlAddin.al" \
"controladdin \"Probe Addin\" { HtmlFiles = ${Q}src/addin/x.html${Q}; }"

probe "r19-table-rimd" "ProbePS.PermissionSet.al" \
"permissionset 50000 \"Probe PS\" { Assignable = true; Caption = ${Q}Probe PS${Q};
  Permissions = table \"G/L Entry\" = RIMD; }"

probe "r20-enum-noid" "ProbeEnum.Enum.al" \
"enum 50000 \"Probe Enum\" { value(Alpha) { Caption = ${Q}Alpha${Q}; } }"

cat <<'EXPECTED'

Expected (verified 2026-08-16, BC27 / runtime 16.0 / al 18.0.37):
  r5-badfilename           AA0215 (warning)
  r7-table-level-only      <clean>  — fields inherit; per-field NOT required
  r7-bad-value             AL0169   — only 7 enum members are valid
  r8-no-captions-no-keys   <clean>  — captions/keys/Clustered are NOT enforced
  r9-secrettext-field      AL0156   — hard error, not a SaaS preference
  r10-field-no-apparea     PTE0008 (error)
  r10-field-no-tooltip     AA0218 (warning) — fires for FIELDS too, not just actions
  r10-action-no-tooltip    AA0218 (warning) + AA0194
  (table-level tooltips inherit: table ToolTip + bare page field = clean.
   Mixing inline and inherited tooltips on one page also compiles clean —
   the compiler cannot catch that, so keep a page to one style.)
  r11-proc-in-usercontrol  AL0104 + AL0198
  r13-onaftermodify        AL0162
  r14-addlast-toplevel     AL0104 + AL0198
  r17-htmlfiles            AL0124
  r19-table-rimd           AL0195
  r20-enum-noid            AL0104 + AL0114
PTE0004 accompanies any probe that declares a table (no permission set) — ignore it.
EXPECTED
