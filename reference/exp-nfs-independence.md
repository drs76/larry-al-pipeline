# Larry executor phase 6 — is a build independent of the NFS mount?

**Question.** The dashboard triggers builds by `ssh deb`, so a build fails whenever the
dev box sleeps. Moving execution to Larry only helps if a build does not secretly depend
on `/mnt/rojaws` — which is NFS from nemesis (`192.168.0.175:/mnt/storage5/data`) and
mounted on *both* boxes. If it does, the move trades one dependency for another.

**Method, and why not the obvious one.** Grepping the source for `/mnt/rojaws` says only
that a path is written down, not that it is read at runtime — and the memory of this work
says so explicitly: *do not infer independence from grepping source*. So this runs a real
build with the pipeline and the project both OFF the mount, and reports what it observed.

## Result — a full build completed off-NFS (2026-09-10)

    clone:   git clone /mnt/rojaws/localDev/setup -> ~/phase6-offnfs/setup  (ext4)
    fixture: bench-p1-crud inputs copied to      -> ~/phase6-offnfs/p1      (ext4)
    run:     run-build.py --project <local p1>,  env-contract cleared, escalation off

    Wrote 6/6 expected files
    error score: 0   ->  RESULT: PASS at round 0
    /mnt/rojaws occurrences in the run log: 0

What the clone supplied, rather than the mount:

| need | source in the off-NFS run |
|---|---|
| AL-REFERENCE topics | 26 files in the clone (`REPO_REFERENCE` derives from `__file__`) |
| AL ruleset | `reference/AL_RULES.md` in the clone |
| BC symbols | downloaded fresh from MS NuGet into the LOCAL `.alpackages` |
| RAG corpus | 8578 objects built from those downloaded symbols |
| coder | ollama on Larry over HTTPS — network, not filesystem |
| compiler | `dotnet altool`, local |

So the runtime dependency set is: the clone, the project directory, the network to Larry,
and a local toolchain. None of them is the mount.

## What this does NOT establish

A passing run proves the build SUCCEEDS off-NFS. It does not prove nothing *touched* the
mount: an incidental read that happens to succeed is invisible to a green result. `strace`
is not installed on this box, so syscall-level proof was not available.

**The remaining test is therefore the real one, and it needs a maintenance window and a
human at the machine** — the memory is explicit that `umount` under live services is not
something to do casually, and everything in this session runs from the mount.

## Procedure for the maintenance-window test

Run ON LARRY, not from a session whose own files live on the mount.

1. Prepare off-mount copies while NFS is still up:
   `git clone /mnt/rojaws/localDev/setup ~/nfs-test/setup`
   and copy a fixture's inputs (app.json, cleanup.sh, docs/, .alpackages/, and the
   handover with its absolute paths rewritten) to `~/nfs-test/p1`.
2. Stop anything that writes to the mount. Confirm with `lsof +D /mnt/rojaws`.
3. `doas umount /mnt/rojaws` — expect EBUSY if step 2 was incomplete; do not force it.
4. Run the build from the clone against the local fixture, exactly as in the result above.
5. Remount, and diff the log against the mounted-run log.

**Pass** = the build completes with the mount absent. **Fail** = any FileNotFoundError or
hang mentioning `/mnt/rojaws`, which names the residual dependency precisely — the thing
grep could not have told you.

## Status

Functional independence: **demonstrated** by a real off-NFS build.
Absence of incidental access: **not yet tested** — requires the unmount above.
