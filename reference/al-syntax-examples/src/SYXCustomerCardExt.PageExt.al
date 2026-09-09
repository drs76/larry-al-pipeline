// RULES DEMONSTRATED (page extension):
//  - a page extension that names its own `namespace` MUST add a `using` for the base app's
//    namespace so the base page ("Customer Card") resolves
//  - addlast/addfirst MUST nest inside `layout { }` or `actions { }` — never at page-ext top level
//  - use OnModify (page trigger), NEVER OnAfterModify, on a page/page extension
namespace SinclairSoftScotland.SyntaxExamples;

using Microsoft.Sales.Customer;

pageextension 57904 "SYX Customer Card Ext" extends "Customer Card"
{
    actions
    {
        addlast(Processing)
        {
            action(SYXPlayTetris)
            {
                ApplicationArea = All;
                Caption = 'Play Tetris';
                Image = Start;
                ToolTip = 'Open the game for this customer.';

                trigger OnAction()
                begin
                    Message('Launching...');
                end;
            }
        }
    }

    trigger OnModifyRecord(): Boolean
    begin
        exit(true);
    end;
}
