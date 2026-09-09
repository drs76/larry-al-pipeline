# house addendum — house rules that exist nowhere else

Hand-written. This is the **only** hand-maintained input to `AL_RULES.md`; everything else in
that file is generated from `al-reference/`. Keep it to rules that are genuinely ours.

If a rule here restates alguidelines or Microsoft guidance, **delete it** — the duplication is
what let the old `AL_RULES.md` drift 4.3 months out of step with the reference while claiming
to be authoritative.

> Grounded 2026-08-28 from `~/.claude/AL_RULES.md` on the Windows workstation, the last
> surviving copy. Sections 1–3 are that file's text verbatim. See §4 for the one gap the
> source could not fill.

---

## 1. Labels and `Locked`

No raw string literals. Every string is a Label variable.
- Technical/protocol strings: `Locked = true`
- User-facing strings: `Locked = false` (or omit)
```al
var
    RoleLbl: Label 'role', Locked = true;
    KeyNotSetErr: Label 'API key not configured.';
```

## 2. TextBuilder

Never concatenate strings for multi-line text. Use TextBuilder.
```al
var
    TB: TextBuilder;
begin
    TB.AppendLine(Line1Lbl);
    TB.AppendLine(Line2Lbl);
    TB.Append(LastLineLbl);
    exit(TB.ToText());
end;
```

The source states no threshold — the rule is written as absolute for multi-line text, and it
is recorded here as it stands rather than given a boundary it never had.

## 3. Custom telemetry conventions

- Treat telemetry as a public API — versioned, documented, non-breaking
- PascalCase field names, no spaces or special chars
- Message format: "Object ActionInPastTense" (e.g. "Web service call failed")
- Emit from the object where the condition occurs, not a central handler
- Only emit data the customer can act on
- DataClassification::SystemMetadata for all telemetry dimensions
```al
CustomDimensions.Add('HttpStatusCode', Format(Response.HttpStatusCode));
Session.LogMessage('MyExt0001', 'Web service call failed',
    Verbosity::Error, DataClassification::SystemMetadata, TelemetryScope::ExtensionPublisher, CustomDimensions);
```

The event ID scheme is shown only by example (`MyExt0001`); the source defines no prefix
allocation, and none is invented here.

## 4. Project overrides

Add per-project overrides in that project's `CLAUDE.md`, referencing this file.

**Every rule here is overridable, and no override is valid without a written reason.**
(Decided 2026-08-28. The source defined no boundary at all — it said only the one line above —
so this is a new rule, not a recovered one.)

An override must name the rule it displaces and say **why** this project differs, inline in the
project's `CLAUDE.md`:

```markdown
## AL rule overrides
- **§2 TextBuilder** — overridden. This extension targets runtime 11.0, where TextBuilder is
  unavailable; concatenation is the only option until the platform bump.
```

A bare "we do it differently here" is not an override; treat the house rule as still in force.
The reason is the point: it makes an override reviewable, and it dates itself, so a constraint
that has since lifted is visible rather than permanent.

This applies uniformly rather than marking some rules non-negotiable. Singling out §1 and §2
was considered and rejected — a rule that cannot be overridden gets worked around silently,
which is harder to find than a stated exception.

---

## What must NOT go in this file

Recorded because the old ruleset accumulated all of it, and every item below is where it
contradicted the reference:

- Variable declaration order — `al-reference/01-syntax-style.md` owns it.
- Abbreviation tables — the alguidelines list is in `01-syntax-style.md`.
- Record-access patterns such as `Find('-')` versus `FindSet()` — `00-gotchas.md` owns those,
  and it is runtime-verified.
- `NoImplicitWith` and record qualification — `00-gotchas.md`.
- Anything about language features, analyzer codes, JSON, namespaces or `DataClassification`.
