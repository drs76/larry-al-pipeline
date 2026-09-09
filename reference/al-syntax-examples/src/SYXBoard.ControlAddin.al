// RULES DEMONSTRATED (ControlAddin):
//  - resource paths (Scripts/StartupScript/StyleSheets) are STRING LITERALS -> single-quoted,
//    relative to the project root
//  - NO `HtmlFiles` property (it does not exist -> AL0124); build DOM in the startup script instead
//  - `event` = JS -> AL (raised from JS via Microsoft.Dynamics.NAV.InvokeExtensibilityMethod)
//  - `procedure` = AL -> JS (maps to a global JS function of the same name)
//  - controladdins have NO numeric id
namespace SinclairSoftScotland.SyntaxExamples;

controladdin "SYX Board"
{
    Scripts = 'src/addin/board.js';
    StartupScript = 'src/addin/board.js';
    StyleSheets = 'src/addin/board.css';
    RequestedHeight = 300;
    RequestedWidth = 300;
    VerticalStretch = true;
    HorizontalStretch = true;

    event ControlAddInReady();
    event ScoreChanged(NewScore: Integer);
    procedure Reset();
}
