import type { ExtensionAPI } from "@earendil-works/pi-coding-agent";
import { execFile } from "node:child_process";
import * as fs from "node:fs";
import * as os from "node:os";
import * as path from "node:path";

// Control the Ternary-Bonsai chat server on Larry from within pi — no ssh.
// Talks to the larry-dashboard maintenance API over TLS+basic-auth:
//   POST https://larry.home.arpa/dash/api/action/bonsai-{on,off}
// which runs `doas systemctl {start,stop} bonsai-llama` on Larry.
//
// Credentials (dashboard basic-auth) are read, in order, from:
//   1. env LARRY_DASH_AUTH   ("user:pass")
//   2. file ~/.pi/.larry-dash-auth  (one line "user:pass", chmod 600)
// Never hard-code them here — this file is committed to the setup repo.

const DASH = "https://larry.home.arpa/dash/api/action";
const MODEL_ENDPOINT = "https://larry.home.arpa:8444/v1/chat/completions";
let woken = false; // once per session; systemctl start is idempotent anyway

function creds(): string | null {
  if (process.env.LARRY_DASH_AUTH) return process.env.LARRY_DASH_AUTH;
  try {
    const f = path.join(os.homedir(), ".pi", ".larry-dash-auth");
    const s = fs.readFileSync(f, "utf8").trim();
    return s || null;
  } catch { return null; }
}

// curl uses the system CA store (already trusts the HomeLab CA on these boxes),
// dodging Node's separate bundle. Returns {code, out}.
function sh(args: string[], timeoutMs = 45000): Promise<{ code: number; out: string }> {
  return new Promise((resolve) => {
    execFile("curl", args, { timeout: timeoutMs }, (err, stdout, stderr) => {
      resolve({ code: err ? (err as any).code ?? 1 : 0, out: (stdout || "") + (stderr || "") });
    });
  });
}

async function dashAction(name: "bonsai-on" | "bonsai-off"): Promise<string> {
  const auth = creds();
  if (!auth) return "no dashboard creds — set LARRY_DASH_AUTH=user:pass or ~/.pi/.larry-dash-auth";
  const r = await sh(["-fsS", "-u", auth, "-X", "POST", `${DASH}/${name}`]);
  return r.code === 0 ? "ok" : `dashboard call failed: ${r.out.trim().slice(0, 200)}`;
}

// Poll a real 1-token completion until the model can answer (health greens
// ~3s before weights finish loading ~18s).
async function waitReady(maxS = 45): Promise<boolean> {
  for (let i = 0; i < maxS; i++) {
    const r = await sh([
      "-fsS", "--max-time", "3", MODEL_ENDPOINT,
      "-H", "Content-Type: application/json",
      "-d", '{"messages":[{"role":"user","content":"hi"}],"max_tokens":1}',
    ], 5000);
    if (r.code === 0 && r.out.includes('"choices"')) return true;
    await new Promise((res) => setTimeout(res, 1000));
  }
  return false;
}

async function bonsaiUp(notify?: (m: string) => void): Promise<boolean> {
  const a = await dashAction("bonsai-on");
  if (a !== "ok") { notify?.(`bonsai: ${a}`); return false; }
  notify?.("bonsai: starting on Larry (evicting coder)…");
  const ok = await waitReady();
  notify?.(ok ? "bonsai: ready" : "bonsai: start triggered but not ready yet — retry your message");
  if (ok) woken = true;
  return ok;
}

export default function (pi: ExtensionAPI) {
  // ── auto-wake on launch ──────────────────────────────────────────────────
  // The public ExtensionAPI has no per-request hook, so wake at session_start
  // when the active model is bonsai. Covers `pi --provider bonsai` (the common
  // path); for a mid-session model switch use `/bonsai on`.
  pi.on("session_start", async (_event: unknown, ctx: any) => {
    if (woken) return;
    let isBonsai = false;
    try { isBonsai = JSON.stringify(ctx?.model ?? "").toLowerCase().includes("bonsai"); } catch { /* ignore */ }
    if (!isBonsai) return;
    await bonsaiUp((m) => { try { ctx?.ui?.notify?.(m, "info"); } catch { /* ignore */ } });
  });

  // ── explicit control ─────────────────────────────────────────────────────
  pi.registerCommand("bonsai", {
    description: "Control the Bonsai chat server on Larry: /bonsai on|off|status",
    handler: async (args: string, ctx: any) => {
      const sub = (args ?? "").trim().toLowerCase() || "status";
      const say = (m: string) => { try { ctx.ui.notify(m, "info"); } catch { /* ignore */ } };
      if (sub === "on")  { await bonsaiUp(say); return; }
      if (sub === "off") { woken = false; say(`bonsai: ${await dashAction("bonsai-off")}`); return; }
      // status
      const r = await sh(["-fsS", "--max-time", "3", "https://larry.home.arpa:8444/health"], 5000);
      say(r.code === 0 ? "bonsai: UP (server answering :8444)" : "bonsai: down (run /bonsai on)");
    },
  });
}
