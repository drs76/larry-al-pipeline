// RULES DEMONSTRATED:
//  - namespace at top, no `using` needed (only same-namespace + primitive/enum types used here)
//  - object = declaration line THEN a { } body; table id required
//  - EVERY field has DataClassification (PerTenantExtensionCop / CodeCop hard requirement on SaaS)
//  - Caption on the table and on each field (UICop)
//  - keys block with a clustered primary key
namespace SinclairSoftScotland.SyntaxExamples;

table 57901 "SYX Player Setup"
{
    Caption = 'Player Setup';
    DataClassification = CustomerContent;

    fields
    {
        field(1; "Primary Key"; Code[10])
        {
            Caption = 'Primary Key';
            DataClassification = SystemMetadata;
        }
        field(2; Enabled; Boolean)
        {
            Caption = 'Enabled';
            DataClassification = SystemMetadata;
        }
        field(3; "Player Name"; Text[100])
        {
            Caption = 'Player Name';
            DataClassification = EndUserIdentifiableInformation;
        }
        field(4; "Favourite Colour"; Enum "SYX Piece Colour")
        {
            Caption = 'Favourite Colour';
            DataClassification = CustomerContent;
        }
        field(5; "High Score"; Integer)
        {
            Caption = 'High Score';
            DataClassification = CustomerContent;
        }
    }

    keys
    {
        key(PK; "Primary Key")
        {
            Clustered = true;
        }
    }
}
