// Minimal placeholder so the ControlAddin resources resolve. Real add-ins build DOM inside
// document.getElementById('controlAddIn') (NOT document.body) and bridge to AL via
// Microsoft.Dynamics.NAV.InvokeExtensibilityMethod('ScoreChanged', [score]).
(function () {
    var root = document.getElementById('controlAddIn');
    if (root) {
        root.textContent = 'SYX Board';
    }
})();

// AL ControlAddin `procedure Reset()` maps to this global function.
function Reset() {
}
