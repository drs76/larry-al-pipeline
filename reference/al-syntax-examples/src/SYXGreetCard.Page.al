// RULES DEMONSTRATED (Card page hosting a ControlAddin):
//  - PageType + SourceTable; searchable via UsageCategory + ApplicationArea
//  - usercontrol(...) sits inside area(Content) within layout { }
//  - the usercontrol BODY contains ONLY trigger definitions — NO procedures inside it
//  - the page's own procedures live at PAGE level (below), not inside the usercontrol
//  - every visible field has ApplicationArea + ToolTip (UICop); calls to the add-in use CurrPage.<name>
namespace SinclairSoftScotland.SyntaxExamples;

page 57903 "SYX Greet Card"
{
    PageType = Card;
    ApplicationArea = All;
    UsageCategory = Tasks;
    Caption = 'Greet Card';
    SourceTable = "SYX Player Setup";
    SourceTableTemporary = true;

    layout
    {
        area(Content)
        {
            group(Details)
            {
                Caption = 'Details';

                field("Player Name"; Rec."Player Name")
                {
                    ApplicationArea = All;
                    ToolTip = 'Specifies the player name.';
                }
            }
            usercontrol(Board; "SYX Board")
            {
                ApplicationArea = All;

                trigger ControlAddInReady()
                begin
                    CurrPage.Board.Reset();
                end;

                trigger ScoreChanged(NewScore: Integer)
                begin
                    Rec."High Score" := NewScore;
                end;
            }
        }
    }

    actions
    {
        area(Processing)
        {
            action(SayHello)
            {
                ApplicationArea = All;
                Caption = 'Say Hello';
                Image = Info;
                ToolTip = 'Show a greeting for the current player.';

                trigger OnAction()
                begin
                    Message(GreetMgt.Greet(Rec."Player Name"));
                end;
            }
        }
    }

    var
        GreetMgt: Codeunit "SYX Greet Mgt";
}
