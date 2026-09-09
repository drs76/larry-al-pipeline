namespace SinclairSoftScotland.RuntimeProbes;

codeunit 50100 "Probe Impl A" implements "Probe IFace"
{
    procedure Ping(): Text
    begin
        exit('A');
    end;
}
