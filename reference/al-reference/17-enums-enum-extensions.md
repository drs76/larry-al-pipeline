<!-- topic file split from AL-REFERENCE.md; edit here, not in the index -->
# enums & enum extensions

Part of [`AL-REFERENCE.md`](../AL-REFERENCE.md) — see that index for the other topics.

---

<!-- ingested: · Enums | 2026-08-16 -->
### Enums & Enum Extensions

- Enum = named-constant type. Usable as table field type, local/global var, procedure parameter.
- Object declaration needs ID + name. Each value needs ordinal ID + name. Ordinal must be unique in enum.
- UI sort order = declaration order, not ordinal order. Values from extended (base) app show before values added by extending app.

```al
enum 50121 Loyalty
{
    Extensible = true;

    value(0; None) { }
    value(1; Bronze) { }
    value(2; Silver) { }
    value(3; Gold)
    {
        Caption = 'Gold Customer';
    }
}
```

- `Extensible = true` required or enumextension against it fails to compile.

**Object IDs**

- enum/enumextension IDs not license-checked any more (old behaviour: shared table range, checked at deploy).
- Uniqueness checked at install time — install fails if enum object ID collides with already-installed enum. Still stay in assigned range.
- Range enforced for Marketplace/AppSource apps only; not PTE, not on-prem.
- Enum ID need not match ID of table it is used on.
- BC 2023 wave 1+: IntelliSense proposes next free ordinal when authoring enum or enumextension.

**Caption gotcha**

- No comma in enum captions. Comma-containing caption (e.g. `'Diamond Level, with bonus'`) can wrap over multiple UI lines AND cause the value the user picks in the UI to differ from the value stored in DB.
- AppSourceCop AS0087 warns when .xlf translation files contain commas in enum captions.

**enumextension**

```al
enumextension 50130 LoyaltyWithDiamonds extends Loyalty
{
    value(50130; Diamond)
    {
        Caption = 'Diamond Level';
    }
}
```

**Usage syntax**

- Type reference: `enum Loyalty`
- Table field: `field(50100; Loyal; enum Loyalty) { }`
- Variable: `LoyaltyLevel: enum Loyalty;`
- Parameter: `procedure Foo(p: enum Loyalty)`
- Value access via `::` on the variable/parameter, not the type name: `if p = p::Gold then ...`

**Enum in TableRelation / SourceTableView**

- Extension-added enum values usable in conditional TableRelation on a modified field, and in page `SourceTableView` filters:

```al
tableextension 50135 TableWithRelationExt extends TableWithRelation
{
    fields
    {
        modify(Relation)
        {
            TableRelation = if (Type = const(Resource)) Resource;
        }
    }
}
```

```al
page 50133 PageOnRelationTable
{
    SourceTable = TableWithRelation;
    SourceTableView = where(Type = const(Resource));
    PageType = List;
}
```

**Conversions**

- Stricter than C/SIDE Options.
- Enum assign/compare allowed only against same enum type.
- Conversion to/from any Option still allowed for backwards compatibility (legacy affordance, don't rely on it).
- See `AssignmentCompatibility` property for cross-type assignment rules.
