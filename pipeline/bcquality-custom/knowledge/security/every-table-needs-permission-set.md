---
bc-version: [all]
domain: security
keywords: [permissionset, permissions, tabledata, PTE0004, pertenantextensioncop, assignable, rimd]
technologies: [al]
countries: [w1]
application-area: [all]
---

# Every extension table needs a matching permission set (PTE0004)

## Description

PerTenantExtensionCop raises **error PTE0004** for any table the extension adds that no
permission set in the same extension covers. The build referee compiles with PTECop, so a
new table without coverage fails the build. Ship a `.PermissionSet.al` from the start and
add every new object to it in the same change that creates the object. Note `table … = X`
(object execute) and `tabledata … = RIMD` (data access) are separate grants — PTE0004 is
about the tabledata coverage.

## Best Practice

```al
permissionset 50103 "PTE My Feature"
{
    Assignable = true;
    Caption = 'My Feature', MaxLength = 30;

    Permissions =
        table "PTE My Setup" = X,
        tabledata "PTE My Setup" = RIMD,
        codeunit "PTE My Mgt" = X,
        page "PTE My Setup Card" = X;
}
```

## Anti Pattern

```al
// extension ships table 50100 "PTE My Setup" with NO permissionset object at all
// → error PTE0004: Table 50100 'PTE My Setup' is missing a matching permission set
```
