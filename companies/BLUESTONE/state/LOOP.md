# Loop protocol — BlueStone Jewellery and Lifestyle Ltd full report

Survives compaction. On resume: read `state/progress.json`, continue at the first `pending` unit whose
`deps` are all `verified`. Nothing needs to be remembered across a context boundary.

## Definition of done
A unit is done when its artifact exists AND `python3 verify.py` exits 0 for the files it touched.
**Judgement does not decide done. Only the exit code does.**

## Per-unit cycle
1. CLAIM   — set `status: in_progress`, `attempts += 1`
2. EXECUTE — fresh-context subagent, given: doctrine + templates + its inputs. Never the producing
             agent's reasoning trace.
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
- Never write outside `companies/BLUESTONE/`. Never write to `~/Desktop/equity reserch`.
- No buy/sell/hold anywhere in any artifact.

## THE NEW-LISTING ADJUSTMENT (owner directive, 2026-09-09)

BlueStone listed **19-Aug-2025**. The standard doctrine assumes 5–10 years of audited history. It does
not exist here. The method is not relaxed — it is **re-pointed**, and every re-pointing is declared:

| Standard doctrine asks | Not available | What this run does instead |
|---|---|---|
| 5–10y trend, CAGR | 2 ARs only | RHP **restated** FY23–FY25 + AR **reported** FY25–FY26. Basis stated on every point. Max 4 years. No CAGR presented as a trend where n<4 |
| Cumulative 5–10y CFO vs PAT | company is loss-making, 2 years reported | Cumulative CFO vs cumulative EBITDA **and** vs cumulative capital raised, FY23–FY26. The conversion question becomes *how much cash did each rupee of reported growth consume* |
| Capital allocation over 5–10y | no such history | **IPO objects vs actual deployment**, from 4 Monitoring Agency Reports + 4 Statements of Deviation. This is the capital-allocation record that exists |
| Promise vs delivery over 8–12 concalls | 5 concalls | RHP stated objects and strategy + 5 concalls. Hit-rate reported **with n stated**; a 5-quarter base is named as a limit on the finding, not hidden |
| Governance track record | ~13 months | Events that did occur are read at full weight: auditor change, director resignations, CS change, ESOP grants, related-party investment. **Absence of history is a gap, not a clean record** |
| Base rate "has it ever cost money here" | no company history | Base rate is taken from the **system**: the recent Indian IPO cohort and the listed jewellery peer set. Company-level absence is recorded explicitly, never treated as a pass |
| Peer comparison | — | Titan (CaratLane is the closest single comparable), Kalyan, Senco, PN Gadgil (itself a recent listing). Same FY26 period basis |

**Two things a new listing has that an old one does not, and both are mandatory here:**

1. **The RHP is the deepest disclosure this company will ever make.** Risk factors, restated financials,
   pre-IPO capital history, litigation, promoter history, unit economics, customer data. It is read in
   full and is a first-class source, not background.
2. **The lock-in / exit ladder.** Anchor 30-day and 90-day, pre-IPO shareholder 6-month, promoter
   18-month. Who sold, when, at what price, and what remains — traced against bulk/block deals,
   shareholding patterns and insider filings. For a 13-month-old listing this is a live governance and
   supply fact, not a market-technical aside.

**What does NOT relax:** every number keeps its tag; every chain keeps 8 links; every finding keeps
S1–S6 and >=3 domains; NOT DISCLOSED still names the document that would answer it; no gap is filled by
inference. A short history means **more** `NOT DISCLOSED`, not more estimation.
