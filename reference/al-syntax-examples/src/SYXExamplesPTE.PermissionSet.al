// RULES DEMONSTRATED (permission set):
//  - object entries (table/page/codeunit/enum) take ONLY `= X`
//  - data access goes on `tabledata <name> = RIMD` (NOT `table <name> = RIMD`, which is AL0195)
//  - required whenever the extension adds a table (PerTenantExtensionCop -> PTE0004 otherwise)
//  - every object the extension creates is listed
namespace SinclairSoftScotland.SyntaxExamples;

permissionset 57905 "SYX Examples PTE"
{
    Assignable = true;
    Caption = 'AL Syntax Examples';
    Permissions =
        table "SYX Player Setup" = X,
        tabledata "SYX Player Setup" = RIMD,
        codeunit "SYX Greet Mgt" = X,
        page "SYX Greet Card" = X;
}
