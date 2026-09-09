#!/usr/bin/env python3
"""
al_lsp — AL Language Server (stdio JSON-RPC) client.

⚠ DIAGNOSTICS: the beta AL LSP (dev-tools 18.0.37) is **navigation-only** — hover,
go-to-definition, find-references, document/workspace symbols, rename. It advertises
`diagnosticProvider: None` and does NOT push `textDocument/publishDiagnostics` (verified:
a file with a confirmed AL0118 error, didOpen+didSave, 75s → zero diagnostics). So this
module is NOT a diagnostics source — run-build gets structured diagnostics from the AL
COMPILER's SARIF (`alc /errorlog`) instead. `diagnostics()` below returns None whenever
the server lacks a diagnostic provider, so callers fall back to SARIF automatically; if a
future AL build starts providing diagnostics, it will start returning them with no change.

Kept for the semantic-navigation use (agent / ALNvim): the handshake + framed JSON-RPC
read/write here are the reusable part for find-references, symbols, etc.

Requires AL dev-tools >= 18.0.37 (the `launchlspserver` command).
"""
import os, json, glob, time, select, subprocess

AL = os.environ.get("AL_CLI", os.path.expanduser("~/.dotnet/tools/al"))
SEV = {1: "Error", 2: "Warning", 3: "Information", 4: "Hint"}


def _has_lsp():
    if not (os.path.exists(AL) or _which(AL)):
        return False
    try:
        h = subprocess.run([AL, "-h"], capture_output=True, text=True, timeout=20)
        return "launchlspserver" in (h.stdout + h.stderr)
    except Exception:
        return False


def _which(name):
    from shutil import which
    return which(name)


def _send(proc, msg):
    data = json.dumps(msg).encode()
    proc.stdin.write(f"Content-Length: {len(data)}\r\n\r\n".encode() + data)
    proc.stdin.flush()


def _read(proc, timeout):
    """Read one framed LSP message; None on idle timeout / EOF."""
    if not select.select([proc.stdout], [], [], timeout)[0]:
        return None
    header = b""
    while b"\r\n\r\n" not in header:
        ch = proc.stdout.read(1)
        if not ch:
            return None
        header += ch
    length = 0
    for ln in header.decode("ascii", "replace").split("\r\n"):
        if ln.lower().startswith("content-length:"):
            length = int(ln.split(":", 1)[1].strip())
    body = b""
    while len(body) < length:
        chunk = proc.stdout.read(length - len(body))
        if not chunk:
            break
        body += chunk
    try:
        return json.loads(body.decode("utf-8", "replace"))
    except Exception:
        return None


def diagnostics(project_root, pkg_cache, timeout=120):
    """Structured first-pass diagnostics for a project. None if LSP unavailable."""
    if not _has_lsp():
        return None
    files = sorted(glob.glob(project_root + "/src/**/*.al", recursive=True))
    if not files:
        return []
    cmd = [AL, "launchlspserver", project_root]
    if pkg_cache:
        cmd += ["--packagecachepath", pkg_cache]
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                            stderr=subprocess.DEVNULL, bufsize=0)
    deadline = time.time() + timeout
    try:
        _send(proc, {"jsonrpc": "2.0", "id": 1, "method": "initialize",
                     "params": {"processId": os.getpid(), "rootUri": "file://" + project_root,
                                "capabilities": {"textDocument": {"publishDiagnostics": {}}},
                                "initializationOptions": {}}})
        caps = {}
        while time.time() < deadline:                    # await initialize result
            m = _read(proc, 10)
            if m and m.get("id") == 1:
                caps = (m.get("result") or {}).get("capabilities", {})
                break
        # Beta AL LSP provides no diagnostics — bail so the caller uses SARIF instead.
        if caps.get("diagnosticProvider") is None:
            return None
        _send(proc, {"jsonrpc": "2.0", "method": "initialized", "params": {}})
        for f in files:
            _send(proc, {"jsonrpc": "2.0", "method": "textDocument/didOpen",
                         "params": {"textDocument": {"uri": "file://" + f, "languageId": "al",
                                                     "version": 1, "text": open(f).read()}}})

        diags, seen, idle = {}, set(), 0
        while time.time() < deadline:
            m = _read(proc, 3)
            if m is None:                                # quiet tick
                idle += 1
                if (idle >= 2 and len(seen) >= len(files)) or idle >= 5:
                    break
                continue
            idle = 0
            if m.get("method") == "textDocument/publishDiagnostics":
                p = m.get("params", {})
                seen.add(p.get("uri"))
                diags[p.get("uri")] = p.get("diagnostics", [])

        out = []
        for uri, ds in diags.items():
            path = uri[7:] if uri and uri.startswith("file://") else (uri or "")
            for d in ds:
                code = d.get("code")
                if isinstance(code, dict):
                    code = code.get("value", "")
                out.append({"code": str(code or ""),
                            "severity": SEV.get(d.get("severity", 1), "Error"),
                            "uri": path,
                            "line": (d.get("range", {}).get("start", {}).get("line", 0) + 1),
                            "message": d.get("message", "")})
        return out
    finally:
        try:
            _send(proc, {"jsonrpc": "2.0", "id": 99, "method": "shutdown"})
            _send(proc, {"jsonrpc": "2.0", "method": "exit"})
        except Exception:
            pass
        try:
            proc.terminate()
            proc.wait(timeout=5)
        except Exception:
            proc.kill()


if __name__ == "__main__":
    import sys
    proj = sys.argv[1] if len(sys.argv) > 1 else "."
    cache = sys.argv[2] if len(sys.argv) > 2 else proj + "/.alpackages"
    ds = diagnostics(proj, cache)
    if ds is None:
        print("LSP unavailable (need AL dev-tools >= 18.0.37)")
    else:
        print(f"{len(ds)} diagnostic(s)")
        for d in ds:
            print(f"  {d['severity']:8} {d['code']:8} {os.path.basename(d['uri'])}:{d['line']}  {d['message'][:70]}")
