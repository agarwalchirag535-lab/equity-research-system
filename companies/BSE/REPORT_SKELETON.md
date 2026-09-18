# BSE Limited — report skeleton

Assembly scaffold for W8_report. Section order follows `INSTRUCTIONS.md` §8. Each section names its
source artifact and what is still open. **W20/W8_report adds no new analysis** — it assembles.
Status at 2026-09-08: 10 of 26 units verified.

| # | Section | Source artifact | Status |
|---|---|---|---|
| 1 | What the company does — one page, no numbers | `waves/W2_business.md` | **READY** — 557 lines, zero financial figures, regex-verified |
| 2 | Industry structure, where pricing power sits | `waves/W2_industry.md` | **READY** — 8 findings; hypothesis partly falsified, overlay corrected |
| 3 | Business model, ₹100 engine, unit economics, operating leverage | `waves/W1.7_mii_overlay.md` + W4_unitecon | overlay ready; **W4_unitecon pending** |
| 4 | Revenue post-mortem — break-up and growth attribution | W3_revenue | **RUNNING** |
| 5 | Cost post-mortem and margin explanation | W3_cost | **RUNNING** |
| 6 | P&L line-by-line findings | W4_belowline + W3_revenue + W3_cost | pending |
| 7 | Balance sheet findings | W3_balancesheet | **RUNNING** |
| 8 | Cash flow and the ₹100 source-to-destination map | W4_cash + `records/cash_ledger_note.md` | pending; float split resolved by W1_ledger |
| 9 | Earnings quality verdict with reasons | W5 | pending — **GATE** |
| 10 | Capital allocation scorecard | W4_capalloc | pending |
| 11 | Promise vs delivery scorecard | `waves/W2_promise.md` | **READY** — 61.3% hit rate, 2.0× action-vs-reassurance gap |
| 12 | Corporate governance — 12 points, 5-bucket summary, 8-point screen | `waves/W2_gov_early.md` + `W1.5_triage.md` + W6 | two of three ready; **W6 pending** |
| 13 | Peer comparison | `waves/W2_peers.md` | **READY** — 5 MIIs, disclosure question settled 4/4 |
| 14 | Red flag register with severity | `records/red_flags.md` | **34 entries**, live; consolidated at W7 |
| 15 | Bear case and thesis-breakers | W7_bearcase | pending |
| 16 | What is not disclosed — the gap register | `records/gap_register.md` | live; GAP-001 open |
| 17 | Questions to ask management on the next concall | derived from open NOT-DISCLOSED links | pending |
| 18 | Valuation — base/bear/bull with visible assumptions | W8_valuation | pending — **precondition: W5 verdict ≠ "cannot be relied upon" and no unresolved Critical** |
| 19 | Monitorables — the 5–10 to track | derived at W7/W8 | pending |

## Inputs already assembled for the back half

| Artifact | What it gives |
|---|---|
| `records/trend_10y.csv` | 28 P&L lines × FY2016–FY2026, **audited cell-by-cell** (413 checked, 39 corrected) |
| `records/balance_cash_10y.csv` | 16 BS/CF lines, same basis |
| `records/quarterly_series.csv` + `.md` | 10 quarters Mar-2024 → Jun-2026 — the only place the **Jun-2026 sequential stall** is visible |
| `records/price_series.csv` + `.md` | 25 month-end closes, **bonus-adjusted**; ₹3,409.80 at 4-Sep-2026 |
| `records/capital_structure.md` | 40,78,84,077 shares; market cap ₹1.391 lakh cr; P/E 55.7× consolidated |
| `records/restatements.md` | FY2017 −27.8%, FY2024 −1.4% verified; 8 more found by W1_ledger |
| `records/revenue_disaggregation.md` | audited Note 22 split, with the MD&A basis warning |
| `records/gap_register.md` | GAP-001 (FY2023 AR) |

## Standing constraints on the final document

1. **No buy/sell/hold, no target price as certainty** — doctrine §1c. Permitted: durability, margin of
   safety, monitorables with triggers, thesis-breakers, what the price implies.
2. **Sections lead with the conclusion**; evidence subordinate (§1f). A table with no conclusion above it
   is a data print and does not ship.
3. **Every contradiction on the record stays on the record** (§10). QC fails the report if one present in
   an intermediate artifact is absent from the final.
4. **Findings ranked by materiality to the investment case**, never by statement order.
5. **Two bases must be stated explicitly wherever used**: standalone vs consolidated, and
   as-first-reported vs as-restated. Both have already produced errors in this run.
6. **The FY2026 accounts end one quarter before the first sequential stall.** Any trailing multiple or
   growth rate must say so.

## Corrections made to this run's own artifacts — must survive into the final report

The doctrine requires that a withdrawn position stay visible against what replaced it. Five so far:

| Artifact | Was | Now |
|---|---|---|
| RF-003 | "no audited revenue split exists" | audited Note 22 exists at p211; the finding is that it **stops above the only line that matters**, and 4/4 peers go further |
| RF-005 / `cash_ledger_note.md` | headline CFO/PAT 1.264, "unquotable" | float **is** separable; own-account **0.942** cumulative |
| RF-014 | treasury income "has no note" | it is named line C in Note 22 at ₹17,142 lakh |
| W1.7 overlay §4.1 | "six of eight screen points inapplicable" | **two** wholly inapplicable; six would have been a false gap |
| W2_promise | treasury income "retired from disclosure" | **withdrawn** — printed in all three 2026 decks |

Two of the five were errors of mine, one was the overlay's, two were agents correcting themselves.
