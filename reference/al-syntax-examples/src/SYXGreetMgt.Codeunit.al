// RULES DEMONSTRATED:
//  - `using` directives go ABOVE the object (order: namespace -> using -> blank -> object -> {)
//  - complete codeunit skeleton: declaration line, { }, codeunit-level var section, then procedures
//  - lowercase keywords; begin/end for multi-statement blocks; exit(value) with a return type
//  - the guard pattern: check setup exists AND is enabled before doing work
//  - every identifier a procedure uses is declared (var block or parameter) — no floating names
namespace SinclairSoftScotland.SyntaxExamples;

using System.Environment;

codeunit 57902 "SYX Greet Mgt"
{
    var
        Setup: Record "SYX Player Setup";

    procedure Greet(Name: Text): Text
    var
        Result: Text;
    begin
        if not Setup.Get('') then
            exit('');
        if not Setup.Enabled then
            exit('');
        if Name = '' then
            Name := 'Player';
        Result := 'Hello, ' + Name;
        exit(Result);
    end;

    procedure CurrentUser(): Code[50]
    var
        EnvInfo: Codeunit "Environment Information";
    begin
        if EnvInfo.IsSaaS() then
            exit(CopyStr(UserId(), 1, 50));
        exit(CopyStr(UserId(), 1, 50));
    end;
}
