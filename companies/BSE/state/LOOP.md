# Loop protocol — BSE Ltd full report

Survives compaction. On resume: read `state/progress.json`, continue at the first `pending` unit whose
`deps` are all `verified`. Nothing needs to be remembered across a context boundary.

## Definition of done
A unit is done when its artifact exists AND `python3 verify.py` exits 0 for the files it touched.
**Judgement does not decide done. Only the exit code does.**

## Per-unit cycle
1. CLAIM   — set `status: in_progress`, `attempts += 1`
2. EXECUTE — fresh-context subagent (Opus), given: doctrine + templates + its inputs. Never the
             producing agent's reasoning trace.
3. VERIFY  — `python3 verify.py`
4. REVIEW  — at every GATE unit, a second fresh-context subagent re-derives the conclusion
             adversarially. The producer never reviews itself.
5. RECORD  — exit 0 -> `verified`; else write `last_error` and leave `pending`

## Escalation
3 failed attempts on one unit -> append to `state/BLOCKED.md`, set `blocked`, move to the next unit
whose deps are met. A fourth attempt has never once been the fix.

## Model policy (owner directive)
Opus 5 for every unit. Never below Sonnet 5 anywhere, including transcription.

## Hard stops
- A gate returning `UNINVESTABLE ON TRUST GROUNDS` still ships a report — that verdict IS the output.
- Documents unobtainable -> stop and report. Never write a report on data that was not read.
- Never write outside `companies/BSE/`. Never write to `~/Desktop/equity reserch`.
- No buy/sell/hold anywhere in any artifact.
