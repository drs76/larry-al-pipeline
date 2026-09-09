namespace SinclairSoftScotland.RuntimeProbes;

// Target for the trigger / event / record-loop probes. Triggers stamp a field so a
// test can prove they actually ran.
table 50110 "Probe Tbl"
{
    Caption = 'Probe Tbl';
    DataClassification = CustomerContent;

    fields
    {
        field(1; "Entry No."; Integer) { Caption = 'Entry No.'; }
        field(2; "Trigger Mark"; Code[20]) { Caption = 'Trigger Mark'; }
    }

    keys { key(PK; "Entry No.") { Clustered = true; } }

    trigger OnInsert()
    begin
        "Trigger Mark" := 'ONINSERT';
    end;

    trigger OnModify()
    begin
        "Trigger Mark" := 'ONMODIFY';
    end;
}
