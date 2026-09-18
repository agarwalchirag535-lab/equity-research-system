# MODEL CRITIQUE — BSE_Financial_Model.xlsx v1, challenged against the evidence base

**Date:** 2026-09-15. **Method:** every v1 assumption re-tested against `waves/` and `records/`.
**Verdict:** v1 was *mechanically* sound (formulas recalculated, balanced, no errors) and
**economically wrong in ways that mattered.** 18 defects below, ranked. v2 (`BSE_Financial_Model_v2.xlsx`)
fixes them.

---

## A. CRITICAL — defects that change the valuation

### A1. Double-count of the treasury in the DCF
v1 put investment income inside total income → EBIT → NOPAT → FCFF → enterprise value, **and then added
net cash of ₹5,000 cr again** in the EV→equity bridge. The treasury was capitalised twice: once as a
perpetual income stream, once as principal.
**Fix (v2):** FCFF is built from **operating EBIT excluding investment income**. The treasury is then
added once, at its own book corpus, in the bridge. Investment income is disclosed separately and its
yield is a stated assumption, not a capitalised growth stream.

### A2. One driver where the business has three
Management states the mechanism: *"the SEBI turnover fee is based on the notional trading, the clearing
expense is based on the number of contracts, and we earn revenue based on premium"*
`[Q4FY26 Concall 13May2026, MD & CEO]`.

| Line | Real base | v1 modelled it as |
|---|---|---|
| Derivatives transaction charges | **premium** ADT | ADTO × take-rate ✔ (right shape, wrong level) |
| SEBI regulatory fee | **notional** ADT | % of transaction charges ✘ |
| Clearing & settlement | **contract count** | % of transaction charges ✘ |

FY2026 proves the three diverge: revenue +63.46%, notional +69.12%, **contracts −6.53%**. `W4_unitecon`
sizes the error at up to **1.78 elasticity points**. v1's cost forecast was anchored to the wrong series.
**Fix (v2):** three independent exogenous series, each with its own growth input and its own realisation.

### A3. The premium/notional wedge was absent
The ratio *is* the margin, and it is the most volatile variable in the case:

| | FY2025 | FY2026 | Q1FY27 | Q2FY26 low |
|---|---:|---:|---:|---:|
| Premium ÷ notional | 0.081126% | **0.104315%** | 0.124959% | **0.091491%** |

Range ±37% inside eight quarters. Reversion merely to the Q2FY26 level **already printed inside this
cycle** costs `3,13,437 × (1 − 0.091491/0.104315) = ₹38,535 lakh` of derivatives revenue at unchanged
premium turnover. Management: *"it is, of course, not predictable"*.
**Fix (v2):** the wedge is an explicit driver cell; the levy is computed from it; it is a sensitivity axis.

### A4. Wrong ADTO levels — take-rates were compensating garbage
v1 seeded derivatives premium ADTO at ₹12,000 cr and cash at ₹7,165 cr, then back-solved take-rates to
force FY26 to tie. Real: **premium ADT ₹19,523 cr**, **cash ADT ₹7,950 cr** `[AR FY26, MD&A, PDF p58/pr47]`.
Two wrong numbers multiplied to a right answer — the tie-out passed while both inputs were false, so any
change to either produced nonsense.
**Fix (v2):** real ADT series typed as actuals; realisation used as the research states it —
**₹16.055 lakh of charges per ₹1 cr of premium ADT** (FY26), ₹15.767 (FY25). No invented day-count needed.

### A5. Core SGF understated by ₹11,279 lakh a year
Announced policy is **5% of transaction revenue** monthly, capped at 150% of the minimum:
`3,79,499 × 5% = ₹18,975 lakh` a year against **₹7,696 lakh actually charged** — `2.47×`.
The Q1FY27 charge already annualises at `2,591 × 4 = ₹10,364` (+34.67%) on flat sequential revenue.
It is also **counter-cyclical**: the SEBI Minimum Required Contribution is computed from stress-test
values, so it rises with volatility — exactly when turnover-linked revenue falls.
v1 grew the ₹7,696 at a generic admin growth rate.
**Fix (v2):** SGF is modelled at the **policy rate as a switch** (charged vs policy), with the ₹11,279
lakh gap shown as a named line. It is permanent cash leaving shareholders into a restricted fund.

### A6. Net debt of −₹5,000 cr conflated owner cash with clearing float
BSE's balance sheet is dominated by **earmarked** settlement/clearing balances that are not shareholders'
money. Real own investible corpus closing FY26 = **₹6,10,190 lakh (₹6,102 cr)**; earmarked liquid funds
₹5,00,657 lakh sit against member obligations.
**Fix (v2):** balance sheet and bridge separate **own-account** from **earmarked**; only the own corpus
enters equity value.

### A7. Cost base modelled as proportional — the bear case was therefore far too kind
`W7_bearcase`: the ex-levy cost floor is **₹1,18,773 lakh** and *"that floor has never contracted in a
down year"* (one single-quarter exception, Jun-2026). Any downside case must run revenue reversion
against an **unchanged** cost base. v1 grew every cost with revenue, so a bear case automatically
protected the margin — it could not produce the twelve-to-one hole the research identifies.
**Fix (v2):** an explicit **cost-floor switch**: opex cannot fall below the FY26 ex-levy run rate
(inflated), independent of revenue.

---

## B. HIGH — defects that distort the picture

### B8. No cash-flow statement, so the report's central finding could not be expressed
The report's headline cash fact: conversion is **1.272 headline and 0.712 own-account** — the printed
number is `1.272/0.712 = 1.787`, **78.7% too high**, because reported CFO absorbs movements in clearing
float that are not owner cash. A model with no CF statement cannot show this.
**Fix (v2):** new **Cash Flow** tab computing headline CFO *and* own-account CFO, with the wedge between
them as a named line, plus own-account FCF.

### B9. EPS wrong
v1 EPS FY26 = ₹62.7. Real consolidated EPS = **₹61.22** (P/E `3,409.80/61.22 = 55.7×`); standalone
₹56.27 (60.6×). v1 used PAT *total* rather than PAT *attributable*, and its reconstructed P&L drifted.
**Fix (v2):** PAT attributable is a modelled line; EPS uses it; a **Checks** tab reconciles model FY26
EPS to ₹61.22 and P/E to 55.7×.

### B10. Terminal growth of 5% left unchallenged on a peak-cycle base
FY2026 is the top of a cycle: Q1FY27 revenue grew **+0.16% sequentially** with **110.1% of the profit
increase non-operating**. And ~nine-tenths of FY26's increase was a **share transfer out of NSE**
(pool +6.46%; BSE share 14.44% → 21.58%), not market growth. Share gains cannot compound in perpetuity —
there is a ceiling at 100%.
**Fix (v2):** market share is an explicit driver with a **stated ceiling**, terminal growth defaults to a
lower figure, and the Checks tab prints the implied share in the terminal year so an impossible share is
visible.

### B11. Clearing expense rose with revenue in v1; in reality it fell 19.45% while notional rose 69.11%
Because the driver is contracts, and contracts fell. v1 could not reproduce this.
**Fix (v2):** clearing = contract count × cost per contract, both explicit.

### B12. Comps were invented
MCX and CDSL price / EBITDA / PAT / book in v1 were placeholder guesses presented in a finished-looking
table. That is the same sin the doctrine forbids: a number without a source.
**Fix (v2):** peer cells are **explicitly labelled `INPUT — UNVERIFIED, user to refresh`**, and the one
peer fact the research does establish is used as a real anchor: NSE FY26 revenue **₹16,60,131 lakh** and
SEBI fee **4.80% of revenue** against BSE's **11.71%** (ratio 2.44×).

### B13. Investment yield held flat when the disclosed series is falling hard
Own-corpus yield went **7.500% → 5.942%** (−156bp, −20.8%); treasury on clearing float **6.32% → 4.99%**
(−21.0%). v1 held 5.6% flat forever.
**Fix (v2):** separate own-corpus and float yields, each an explicit input, defaulted to the FY26
realised level with the decline visible in the driver history.

---

## C. MEDIUM — modelling hygiene

- **B14. Associate (CDSL) grown positively** — v1 grew it at admin growth; the FY26 contribution actually
  **fell 13.4%**, and the stake is SEBI-capped at 15% so it cannot be increased. v2 makes it an explicit
  input defaulted flat, with the cap noted.
- **B15. `trading_days = 250` was a fabricated annualiser.** v2 removes it from the derivatives chain by
  using realisation per unit of ADT, the basis the disclosures actually publish.
- **B16. Revenue-linked current liabilities.** v1 set current liabilities at ~1.0× revenue, so the
  clearing float — a pass-through that moves with member margin and the settlement-cycle date, not with
  revenue — became a revenue function. v2 models own payables off costs and holds earmarked float as its
  own driver.
- **B17. No quarterly reality check.** Q1FY27 actuals exist (revenue ₹1,56,602 lakh; total income
  ₹1,70,672 lakh; PBT ₹1,16,366 lakh). v2's Checks tab compares FY27E against the Q1FY27 annualised
  run-rate, so an unreachable forecast is visible immediately.
- **B18. No scenario manager.** v2 adds base / bear / bull as a single switch driving the driver block,
  matching the research's own scenario architecture.

---

## D. What v1 got right (kept in v2)

- Full formula architecture with no typed numbers in projected columns; every projected cell traceable to
  an assumption. That discipline is retained and re-verified.
- Formatting doctrine (blue inputs on yellow, green cross-sheet, black same-sheet, ₹ crore, parens).
- Balance-sheet identity enforced by a computed plug, with a visible check row.
- Historical actuals taken from the audited consolidated series rather than invented.

---

## E. Residual limitations declared in v2 (not silently fixed)

1. **The product split is unaudited.** Every segment line below transaction charges comes from the MD&A;
   the audited Note 22 stops at one aggregate. `NOT-DISCLOSED -> Ind AS 115.114 disaggregation note.`
   v2 labels the segment tab accordingly.
2. **Contract count for FY26 is an index, not an absolute.** The disclosures give the *change* (−6.53%)
   and quarterly average daily lots (153mn → 100mn), not a clean audited annual count. v2 uses an
   indexed contract series with FY26 = 1.000 and says so.
3. **Peer multiples remain user inputs.** No verified peer market data exists in this corpus.
4. **Terminal value on a regulator-allocated variable is a stated fragility, not a solved problem.**
   v2 prints the terminal-year implied market share so the assumption is falsifiable on sight.

---

## F. ROUND 2 — defects found by independent adversarial audit of v2, and fixed

Two fresh-context auditors were run against v2. The **valuation-logic auditor found no errors**: the
double-count removal, unit consistency, H-model algebra, reverse-DCF closed form and every sign were
verified correct, including a numerical round-trip proving the implied-growth formula reproduces the
implied terminal value exactly. The **assumptions auditor found five real defects**, all now fixed.

### F1. EPS used the wrong share count — the most serious defect
v2 divided PAT attributable by **paid-up** shares (40.7884 cr) and printed **₹61.22**, then labelled it
"audited consolidated EPS". The audited basis uses **issued** shares (41.1979 cr):
`2,496.98 / 41.1979 = ₹60.61` [`records/capital_structure.md`, which explicitly corrects an earlier
₹61.22 in the research itself]. Worse, v2's own note said "EPS uses issued, market cap uses paid-up"
while the formula did the opposite — the model contradicted its own documentation.
Consequently the P/E was also wrong: the true price-to-audited-earnings multiple is
`3,409.80 / 60.61 = 56.26×`, which is the figure the report actually publishes. v2's 55.7× was
market-cap ÷ PAT, a different statistic.
**Fixed:** separate `shares_issued` (EPS) and `shares` (market cap, value per share) inputs; Checks
targets corrected to ₹60.61 and 56.26× and both now tie exactly.

### F2. The CDSL stake value was wrongly called unverified
v2 set the stake to zero claiming "no market value is evidenced in this corpus". That was **false** —
**₹3,509.32 cr** is disclosed at `[AR FY26, Note 8]` and used throughout the research. Zeroing it
understated equity value by roughly ₹86/share on a false premise.
**Fixed:** the market value is now an input, governed by a **`cdsl_mode` switch** enforcing W5
constraint 4 (*market value **or** equity earnings, never both*): mode 1 keeps the associate profit in
PBT and values the stake at nil; mode 2 strips the profit and adds the market value. A **double-count
guard** on the Checks tab multiplies the two and must equal zero — verified zero in both modes.

### F3. Investment income treated wholly as recurring yield
~**30.57%** of investment income is **mark-to-market revaluation** — "not a yield and should not carry
an operating multiple" [W5]. v2 compounded the whole amount forward at the corpus growth rate.
**Fixed:** an `inv_recurring_pct` input (69.43%), a memo line sizing the MTM component (₹88.74 cr in
FY26) and a **quality-adjusted EPS** of ₹58.99 against the reported ₹60.61.

### F4. Float income on members' money sat inside the FCFF base
₹171 cr of FY26 revenue is interest earned on **members' clearing float** at 4.99%, credited to
shareholders as revenue. v2 correctly excluded the *own* treasury income from operating EBIT but left
this in, so the "operations only" FCFF still carried non-customer income.
**Fixed:** a memo line computes it (this also puts the previously dangling `float_yield` input to work)
and a `strip_float` switch removes it from the FCFF base by default. It is **added back in PBT**,
because it genuinely is inside reported revenue and reported PBT — only the valuation base changes.

### F5. The base case silently assumed perpetual share gains; the bear case was mislabelled
FY28E +10% and FY29E +8% both exceeded the two-exchange pool growth of 6.46%, so implied market share
rose every year — contradicting v2's own note that "share gains exhaust".
**Fixed:** FY29E base growth set **equal to pool growth (6.46%)** so share stops rising by construction.
Separately, the bear case's "0%" growth was labelled as flat when it actually holds FY27E at the FY26
*average*, a **−34% fall from the already-printed Q1FY27 run-rate**. The label now says so explicitly.

**A note on what the base case actually assumes, now visible.** FY29E premium ADT of ~₹30,300 cr is only
~2% above the **Q1FY27 actual of ₹29,615 cr**. So the base case is essentially *"the current run-rate
persists, with no further growth"* — and the implied FY29E share of ~28% is a property of the
run-rate already achieved, not of future share gains. The question the model puts to the reader is
therefore whether the Q1FY27 level is sustainable, which is exactly the question the research says is
unforecastable.

---

## G. What the finished model says (outputs, not recommendations)

| | Base | Bear | Bull |
|---|---:|---:|---:|
| WACC | 12.70% | 15.55% | 11.18% |
| Terminal growth | 4.0% | 3.0% | 5.0% |
| Value per share | **₹1,024** | ₹424 | ₹3,601 |
| as % of ₹3,409.80 | 30% | 12% | 106% |
| Cost floor binding? | no | **yes, +₹36 cr** | no |

**Reverse DCF — the question the doctrine actually asks.** At ₹3,409.80 the price requires
**~11.1% growth in perpetuity against a 12.70% WACC** — a perpetual rate only 1.6pp below the cost of
capital, on a business where 64.84% of revenue is one product on one regulator-allocated weekly expiry
slot, where every disclosed realisation series is now flat or negative, and where the two-exchange
premium pool grew only 6.46% while nine-tenths of BSE's FY26 increase came out of NSE's share.
Only the bull trajectory justifies the price. **That is a statement of what the price implies, not a
recommendation, and none is offered.**
