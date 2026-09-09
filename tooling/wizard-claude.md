# /wizard — generate a deterministic setup wizard (Claude is the author)

> **`$SETUP_DIR`** = the larry-setup repo on this machine. Resolve once, first that exists: `$SETUP_DIR` · `~/larry-setup` · `/mnt/rojaws/localDev/setup` (same chain `alw` uses).

Read and follow the canonical wizard instructions at
`$SETUP_DIR/tooling/wizard.md` (ignore its pi-specific `$@` placeholder — the
mission is below; you ARE the strong model it wants).

The thing to provision is:

$ARGUMENTS

Notes for this entry point:
- If the mission is empty, ask what to set up (one line) before the interview.
- Interactive → run the Step 1 interview as written. Non-interactive (`claude -p`) → skip it, infer
  the steps from the repo/docs you can read, and leave every unknown as a clearly-marked
  `# TODO(human): …` line in the script rather than guessing a URL, path, or secret name.
- Use `AskUserQuestion` for the interview rounds (2–3 per round).
- Deliver exactly as the canonical file's Step 3 specifies: write the script, `chmod +x`, tell the
  user to read-then-run, and STOP — do not run the wizard yourself, and never invent secret values.
