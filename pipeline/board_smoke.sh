#!/usr/bin/env bash
# board_smoke.sh — live end-to-end smoke for board.py against the real Kanboard.
# Needs ~/.config/board/env + a reachable Kanboard. Creates a throwaway board, asserts,
# and cleans up. Does NOT touch github (local-only path only — no undeletable test repo).
#   ./board_smoke.sh   → exit 0 = pass
set -uo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
SB="$(mktemp -d)/proto-smoke"; mkdir -p "$SB/docs"
echo "# spec" > "$SB/docs/SPEC.md"
git -C "$SB" init -q -b main 2>/dev/null; git -C "$SB" config user.email s@s; git -C "$SB" config user.name s
. ~/.config/board/env
rpc(){ curl -s -u "jsonrpc:$KANBOARD_TOKEN" "$KANBOARD_URL" -d "$1"; }
fail(){ echo "  [FAIL] $1"; FAILED=1; }
ok(){ echo "  [OK ] $1"; }
FAILED=0

echo "=== board project ==="
python3 "$HERE/board.py" project "$SB" >/dev/null 2>&1
PID=$(python3 -c "import json;print(json.load(open('$SB/.board'))['project_id'])")
COLS=$(rpc "{\"jsonrpc\":\"2.0\",\"method\":\"getColumns\",\"id\":1,\"params\":{\"project_id\":$PID}}" | python3 -c "import sys,json;print(','.join(c['title'] for c in json.load(sys.stdin)['result']))")
[ "$COLS" = "Backlog,Planning,Building,Review,Promoted,Done" ] && ok "6 lifecycle columns" || fail "columns: $COLS"
NDOC=$(rpc "{\"jsonrpc\":\"2.0\",\"method\":\"getAllTasks\",\"id\":1,\"params\":{\"project_id\":$PID,\"status_id\":1}}" | python3 -c "import sys,json;print(sum(1 for t in json.load(sys.stdin)['result'] if t['title'].startswith('doc:')))")
[ "$NDOC" -ge 1 ] && ok "doc card(s) seeded ($NDOC)" || fail "no doc cards"

echo "=== rfc + hook + commit link ==="
RFC=$(python3 "$HERE/board.py" rfc "$SB" "smoke rfc"); TID=${RFC#T-}
[ -n "$TID" ] && ok "rfc → $RFC" || fail "rfc returned nothing"
python3 "$HERE/board.py" install-hook "$SB" >/dev/null 2>&1
echo c > "$SB/c.txt"; git -C "$SB" add -A; git -C "$SB" commit -q -m "c

Ticket: $RFC"
NL=$(rpc "{\"jsonrpc\":\"2.0\",\"method\":\"getAllExternalTaskLinks\",\"id\":1,\"params\":{\"task_id\":$TID}}" | python3 -c "import sys,json;print(len(json.load(sys.stdin)['result']))")
[ "$NL" -ge 1 ] && ok "post-commit hook linked the commit" || fail "commit not linked"

echo "=== local-only promote (must SKIP github) ==="
OUT=$(python3 "$HERE/board.py" promote "$SB" 2>&1)
echo "$OUT" | grep -q "github mirror SKIPPED" && ok "local-only promote skipped github" || fail "promote: $OUT"
[ "$(python3 -c "import json;print(json.load(open('$SB/.board')).get('github'))")" = "False" ] && ok "marker github=False" || fail "marker github not False"

echo "=== cleanup ==="
rpc "{\"jsonrpc\":\"2.0\",\"method\":\"removeProject\",\"id\":1,\"params\":{\"project_id\":$PID}}" >/dev/null
OV=$(rpc '{"jsonrpc":"2.0","method":"getProjectByName","id":1,"params":{"name":"Prototypes"}}' | python3 -c "import sys,json;print(json.load(sys.stdin)['result']['id'])")
for t in $(rpc "{\"jsonrpc\":\"2.0\",\"method\":\"getAllTasks\",\"id\":1,\"params\":{\"project_id\":$OV,\"status_id\":1}}" | python3 -c "import sys,json;print(' '.join(str(t['id']) for t in json.load(sys.stdin)['result'] if 'proto-smoke' in t['title']))"); do
  rpc "{\"jsonrpc\":\"2.0\",\"method\":\"removeTask\",\"id\":1,\"params\":{\"task_id\":$t}}" >/dev/null; done
rm -rf "$(dirname "$SB")"

[ "$FAILED" = 0 ] && { echo "SMOKE PASS"; exit 0; } || { echo "SMOKE FAIL"; exit 1; }
