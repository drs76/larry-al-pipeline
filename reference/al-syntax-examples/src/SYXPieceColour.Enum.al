// RULE: enum — declaration line then brace body; each value has an id and a Caption.
namespace SinclairSoftScotland.SyntaxExamples;

enum 57900 "SYX Piece Colour"
{
    Extensible = true;
    Caption = 'Piece Colour';

    value(0; None) { Caption = 'None'; }
    value(1; Cyan) { Caption = 'Cyan'; }
    value(2; Yellow) { Caption = 'Yellow'; }
    value(3; Purple) { Caption = 'Purple'; }
}
