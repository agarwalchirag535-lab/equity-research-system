# W4_unitecon — BSE Limited: the ₹100 engine, unit economics, capital intensity, and the stall

**Wave 4. Evidence, not conclusions about the investment case** (doctrine §7). Sector overlay
`W1.7_mii_overlay.md` **§5 is binding**: no variable/fixed cost split, no physical capital intensity, no
price-per-unit / variable-cost-per-unit frame. Leverage is measured **to turnover**; capital intensity is
measured as **regulatory capital per ₹1 of revenue**. All figures ₹ lakh, consolidated, unless marked
standalone. Printed folio = PDF − offset; offsets FY2021 +5, FY2024 +6, FY2025 +11, FY2026 +11 per
`records/printed_page_offsets.json` and `W1_docmap.md` §0.1.

**Scope boundary, declared to avoid a duplicate artifact.** `state/progress.json` assigns "the ₹100 map"
to `W4_cash`. This file builds the **P&L half** — ₹100 of revenue through every cost layer to PAT. The
**cash half** — PAT → working capital → CFO → capex → FCF → distribution — is `W4_cash`'s and is not
reproduced here. The two halves join at PAT.

**No chain records are written in this file, by decision.** Every line in the ₹100 engine that loses more
than ₹5 already carries a chain in `W3_cost` (regulatory contribution, employee benefits, clearing and
settlement, other expenses) or `W3_revenue`. The one exception is **tax at ₹17.04 per ₹100**, which has no
chain anywhere; it is `W4_belowline`'s and is recorded here as an explicit not-traced decision rather than
silently skipped (doctrine §3's brake). Writing a second, competing chain on `Clearing and settlement
expense` — the line this file's new evidence actually moves — would create a duplicate record rather than a
recorded contradiction; §4.4 states the amendment in prose instead, with both positions standing.

---

## What this file settles, up front

1. **The leverage contradiction between `W3_cost` and `W3_revenue` is reconciled, not split.** They measure
   two different objects. Elasticity is measurable; attribution is not. §4.1.
2. **The third base is not undisclosed — it is disclosed at the bottom of the source hierarchy.** BSE
   publishes **Average Daily Lots** quarterly in its investor presentation. Contracts **fell 6.53%** in
   FY2026. §0.2.
3. **Consequently "operating leverage at BSE" has no single value.** The same cost base against the three
   simultaneously-true turnover measures gives **+0.094, +0.159 and −1.682**. §4.2.
4. **On the contract base, the "structural efficiency gain" reverses sign**: group clearing cost per
   contract **rose 3.74%**. §2.3.
5. **Capital intensity has inverted on flow.** Regulatory capital is 3.0% of equity; at the margin,
   physical capex per incremental rupee of revenue is **4.5× incremental regulatory capital**. §3.
6. **The stall quarter: operating revenue +0.16% and 73.3% of the sequential profit increase is investment
   income.** The operating top line supplied **2.5%**. §5.
7. **`RF-044`'s "the cost base has never contracted in ten years" is wrong, and the correction is recorded
   not resolved** (doctrine §10). It contracted in FY2021 by 4.07%, like-for-like, at source. §4.3.

---

## 0. Method, and the one new input

### 0.1 The three activity bases, restated

Management's own statement of the mechanism, unchanged since FY2026: *"the SEBI turnover fee is based on
the notional trading, the clearing expense is based on the number of contracts, and we earn revenue based
on premium"* `[Q4FY26 Concall 13May2026, MD & CEO]`.

| Base | Drives | FY2025 | FY2026 | Δ |
|---|---|---|---|---|
| **Premium** ADT (₹ cr) | revenue | 8,978 | 19,523 | **+117.45%** |
| **Notional** ADT (₹ cr) | the SEBI levy | 1,10,66,674 | 1,87,15,375 | **+69.11%** |
| **Contracts** — avg daily lots (Mn) | clearing cost | 122.5 | 114.5 | **−6.53%** |

Premium and notional `[AR FY26, MD&A, PDF p58/pr47]`. Contracts `[Q1FY27 IP 04Aug2026, PDF p14/slide 13]` —
see §0.2. `DERIVED`: `19,523 / 8,978 = 2.174538` · `1,87,15,375 / 1,10,66,674 = 1.691202` ·
`114.5 / 122.5 = 0.934694`.

**Three bases, three directions, one year.** Two grew at rates 48 percentage points apart and the third
fell. Every per-unit statement about BSE is therefore a statement about *which* unit, and the choice
changes the sign.

### 0.2 The contract base — where it actually is, and why it is usable

`W3_revenue` §2.3 recorded contract counts as `NOT-DISCLOSED`, and that is **exactly right for the corpus
it searched**: they appear in no annual report FY2024–FY2026 and in no concall as an annual figure. They
appear in the **quarterly investor presentation**, on the Equity Derivatives segment slide, as *"Average
Daily Lots (Mn)"* alongside *"Avg Daily Notional T/o (in Rs. Tn)"*:

| Quarter | Q1FY25 | Q2FY25 | Q3FY25 | Q4FY25 | Q1FY26 | Q2FY26 | Q3FY26 | Q4FY26 | **Q1FY27** |
|---|---|---|---|---|---|---|---|---|---|
| Avg daily lots (Mn) | 126 | 153 | 128 | 83 | 82 | 100 | 125 | 151 | **156** |
| Avg daily notional (₹ Tn) | 98 | 128 | 105 | 112 | 131 | 164 | 210 | 245 | **237** |
| AD premium T/o (₹ mn) | 71,617 | 82,034 | 87,584 | 1,17,827 | 1,50,838 | 1,50,045 | 1,94,591 | 2,89,207 | **2,96,154** |
| EQD revenue (₹ mn) | 2,422 | 3,456 | 3,530 | 4,748 | 5,980 | 6,242 | 7,842 | 11,279 | **11,550** |

`[Q1FY27 IP 04Aug2026, PDF p14/slide 13]`, cross-read against `[Q4FY26 IP 07May2026, PDF p14/slide 13]` and
`[Q1FY26 IP 07Aug2025, PDF p13/slide 12]`.

**Source tier, declared.** Doctrine §5 ranks an investor presentation **below** every audited and unaudited
filing and states it "is never the source of an L1". It is not used as an L1 here. It is used as an **L3
activity metric**, which is the same tier the entire premium/notional series already sits on — those come
from the MD&A, which is unaudited (`RF-003`). This series sits one rung lower than that, and every number
built on it below is marked `ESTIMATE`, never `DERIVED`.

**Five checks were run before using it, and it passes all five.**

1. **Stable across three independently filed decks.** The overlapping quarters are identical to the unit in
   all three.
2. **The same construction reproduces an independently sourced series.** Taking the simple average of the
   four quarterly *notional* values reproduces the MD&A's annual notional ADT to **0.19%** in FY2026
   (`(131 + 164 + 210 + 245) / 4 = 187.5` against 187.15) and **0.07%** in FY2025
   (`(98 + 128 + 105 + 112) / 4 = 110.75` against 110.67) `[AR FY26, MD&A, PDF p58/pr47]`. The same
   averaging is therefore applied to lots: FY2026 `(82 + 100 + 125 + 151) / 4 = 114.5`; FY2025
   `(126 + 153 + 128 + 83) / 4 = 122.5`.
3. **Internal economic coherence.** Notional per contract is `1,87,15,375 / 114.5 = ₹16.34` lakh in FY2026
   against `1,10,66,674 / 122.5 = ₹9.03` lakh in FY2025, **+80.9%**, and quarter by quarter the step lands
   between Q2FY25 (`128 / 153 = ₹8.37` lakh) and Q4FY25 (`112 / 83 = ₹13.49` lakh) — precisely when SEBI's
   lot-size increase took effect from 20-Nov-2024 `[AR FY25, MD&A policy list, PDF p50/pr39]`. A mis-read
   chart does not reproduce a regulatory event's date.
4. **Level plausibility.** Q1FY27 notional per contract is `237 / 156 = ₹15.19` lakh, consistent with a
   Sensex option lot at prevailing index levels.
5. **Definition.** "Lot" is BSE's own word and one lot is one contract. Futures are immaterial to the
   count: futures ADT was ₹342 crore against options notional ADT of ₹1,87,15,375 crore
   `[AR FY26, MD&A, PDF p58/pr47]`.

A quarterly total also exists and ties: **"EQD – Total Contracts Traded 9.34 Bn"** for Apr–Jun 2026
`[Q1FY27 IP 04Aug2026, PDF p8/slide 7]`, against `156 × 60 = 9,360` Mn on a 60-trading-day quarter — a
0.2% gap.

> **What this does and does not do to `RF-012`.** `RF-012` was closed as *"operating leverage is not
> measurable in the conventional sense"* because the third base was undisclosed. **The base exists and is
> quantified here, so the stated reason for the closure is narrower than it appeared** — but the closure's
> *conclusion* survives, for a different and stronger reason set out in §4.1. Both positions are on the
> record; neither is deleted.

---

## 1. THE ₹100 ENGINE — FY2026, consolidated

Base: **₹100 = revenue from operations of 4,83,395** `[AR FY26, Note 22, PDF p211/pr200]`. Every layer is
that layer's rupee amount ÷ 4,83,395 × 100, from the face of the audited consolidated statement of profit
and loss `[AR FY26, Consolidated P&L, PDF p164/pr153]`.

```
                                                     ₹ per ₹100      driven by
  Revenue from operations                             100.00         ACTIVITY  (92.28% of the increase)
+ Investment income                                   + 6.01         RATE      (yield on own corpus)
+ Other income                                        + 0.49         RATE
= Total income                                        106.50
  ------------------------------------------------------------------------------------------------
− Employee benefits                                   − 6.16         MANAGEMENT (headcount × cost/head)
− Clearing and settlement                             − 5.80         GROUP STRUCTURE (contracts × transfer price)
− Other expenses                                      − 5.12         MIXED (largest driver is receivables ECL)
− Technology                                          − 4.20         MANAGEMENT (and the capitalise/expense line)
− Depreciation and amortisation                       − 3.29         COMMITTED (past capex × rate)
− Finance cost                                        − 0.00         none — zero-debt group
  = controllable / non-levy cost layers               −24.57
− Regulatory contribution (the levy)                  −13.44         REGULATOR (notional × SEBI rate)
  = total expenses                                    −38.01
  ------------------------------------------------------------------------------------------------
= Profit before contribution to core SGF               68.49
− Contribution to core settlement guarantee fund      − 1.59         REGULATOR (stress-test MRC, not turnover)
+ Share of profit of associates                       + 1.35         EXOGENOUS (CDSL)
= Profit before tax                                    68.25
− Tax                                                 −17.04         STATUTORY
= PAT, continuing operations                           51.21
+ Discontinued operations                             + 0.25         one-off (BSE Institute disposal)
= PAT, total operations                                51.45
+ Loss attributable to non-controlling interest       + 0.20         IFSC subsidiaries
= PAT attributable to shareholders                     51.66
```

`DERIVED` throughout: `29,030 / 4,83,395 = 6.01` · `5,14,810 / 4,83,395 = 106.50` ·
`29,781 / 4,83,395 = 6.16` · `28,035 / 4,83,395 = 5.80` · `24,732 / 4,83,395 = 5.12` ·
`20,313 / 4,83,395 = 4.20` · `15,896 / 4,83,395 = 3.29` · `16 / 4,83,395 = 0.003` ·
`1,18,773 / 4,83,395 = 24.57` · `64,969 / 4,83,395 = 13.44` · `1,83,742 / 4,83,395 = 38.01` ·
`3,31,068 / 4,83,395 = 68.49` · `7,696 / 4,83,395 = 1.59` · `6,542 / 4,83,395 = 1.35` ·
`3,29,914 / 4,83,395 = 68.25` · `82,384 / 4,83,395 = 17.04` · `2,47,530 / 4,83,395 = 51.21` ·
`2,48,725 / 4,83,395 = 51.45` · `2,49,698 / 4,83,395 = 51.66`. Tie:
`100 + 6.01 + 0.49 − 24.57 − 13.44 − 1.59 + 1.35 − 17.04 + 0.25 + 0.20 = 51.66` ✓
`[AR FY26, Consolidated P&L, PDF p164/pr153]`.

### 1.1 Who takes the ₹54.84 that never reaches the shareholder

Of ₹106.50 of total income per ₹100 of revenue, ₹51.66 reaches PAT attributable. **₹54.84 leaves.**

| Taker | ₹ per ₹100 | Share of the ₹54.84 leakage |
|---|---|---|
| **Government and regulator** — levy 13.44 + core SGF 1.59 + tax 17.04 | **32.07** | **58.48%** |
| Group structure — clearing and settlement | 5.80 | 10.58% |
| Management's discretionary annual spend — employee + technology + other | 15.48 | 28.22% |
| Committed — depreciation, finance cost | 3.29 | 6.00% |
| less: associate profit, discontinued, NCI (add back) | −1.80 | −3.28% |

`DERIVED`: `106.4988 − 51.6551 = 54.8437`; `(64,969 + 7,696 + 82,384) / 4,83,395 = 32.075` and
`32.075 / 54.844 = 58.48%`; discretionary `(29,781 + 20,313 + 24,732) / 4,83,395 = 15.479` and
`15.479 / 54.844 = 28.22%`. Excluding tax, the regulator still takes
`(13.4401 + 1.5921) / (54.8437 − 17.0428) = 15.032 / 37.801 = 39.77%` of what is left
`[AR FY26, Consolidated P&L, PDF p164/pr153]`.

> **The engine's shape, in one sentence.** Nearly three-fifths of everything that leaves ₹100 of BSE's
> revenue before it reaches a shareholder is priced by SEBI or the Income-tax Act, and **₹15.48 — 28.2% of
> the leakage — is the only part any manager decides in a given year.**

### 1.2 The engine one year earlier, and what moved

| ₹ per ₹100 of revenue from operations | FY2025 | FY2026 | Contribution to PAT/₹100 |
|---|---|---|---|
| Investment income | 8.61 | 6.01 | −2.61 |
| Other income | 0.82 | 0.49 | −0.33 |
| Employee benefits | 8.00 | 6.16 | +1.84 |
| Technology | 5.56 | 4.20 | +1.35 |
| **Clearing and settlement** | **11.77** | **5.80** | **+5.97** |
| Regulatory levy | 13.88 | 13.44 | +0.44 |
| Depreciation | 3.82 | 3.29 | +0.53 |
| Other expenses | 7.04 | 5.12 | +1.92 |
| Finance cost | 0.00 | 0.00 | −0.00 |
| Core SGF | 3.04 | 1.59 | +1.45 |
| Associate profit | 2.79 | 1.35 | −1.44 |
| Tax | 14.58 | 17.04 | −2.46 |
| Discontinued + NCI | 0.30 | 0.45 | +0.15 |
| **PAT attributable** | **44.83** | **51.66** | **+6.82** |

`DERIVED`, all lines ÷ their own year's revenue from operations (FY2025 2,95,734; FY2026 4,83,395); the
contributions sum to `+6.8212` against `51.6551 − 44.8339 = +6.8212`, zero residual
`[AR FY26, Consolidated P&L, PDF p164/pr153]`.

**The single arithmetic fact this table produces: `5.9694 / 6.8212 = 87.5%` of the entire improvement in
PAT per ₹100 of revenue is one line — clearing and settlement.** `W3_cost` §3 established that 75.1% of
that line's margin contribution is the revenue denominator and a further 1.07pp of the 10.06pp margin gain
is a 5,496 intra-group elimination. So the largest single driver of BSE's FY2026 profit per rupee of
revenue is a line whose movement is three-quarters denominator and one-fifth consolidation arithmetic.

Second fact: **the regulator's share of the leakage rose while the leakage fell.** Total leakage per ₹100
fell from `109.4331 − 44.8339 = 64.60` to 54.84, but the regulator-and-tax share of it rose from
`(13.8794 + 3.0433 + 14.5810) / 64.5992 = 48.77%` to 58.48%. Growth made BSE more profitable and more
regulator-dependent at the same time.

### 1.3 The one layer with no chain — recorded, not skipped

**Tax, ₹17.04 per ₹100, is the second-largest single layer in the engine and no chain record exists for it
in any wave file.** It is `W4_belowline`'s line under `state/progress.json`. Recorded here as a decision on
the record per doctrine §3. Two facts a reader needs meanwhile: the effective rate rose from
`43,121 / 1,74,827 = 24.66%` to `82,384 / 3,29,914 = 24.97%`, and the FY2025 figure is net of a
**prior-period credit of 2,987** against a **charge of 256** in FY2026 — a 3,243 swing, `3,243 / 4,83,395 =
₹0.67 per ₹100`, which is 9.8% of the 6.82 improvement and is not an operating item
`[AR FY26, Consolidated P&L, PDF p164/pr153]`.

---

## 2. UNIT ECONOMICS — on the bases the overlay permits

Overlay §5 rules out price-per-unit / variable-cost-per-unit. What replaces it is **revenue per unit of
each disclosed activity measure** and **cost per unit of the base that actually drives that cost**. Method
throughout, as in `W3_revenue` §1: the **index** form (revenue index ÷ activity index) is day-count-neutral
and is `DERIVED`; any **absolute** per-unit rate requires a trading-day assumption and is `ESTIMATE`.
Trading days implied by BSE's own disclosure: `19,60,000 / 7,950 = 246.5` in FY2026 and
`19,30,000 / 7,766 = 248.5` in FY2025 `[AR FY26, MD&A, PDF p58/pr47]`.

### 2.1 Revenue per ₹1 crore of premium ADT — the overlay's headline unit

| ₹ lakh of revenue per ₹1 crore of premium ADT | FY2025 | FY2026 | Δ |
|---|---|---|---|
| **Consolidated revenue from operations** | 32.940 | **24.760** | **−24.83%** |
| Equity-derivatives transaction charges only (standalone) | 15.767 | **16.055** | **+1.83%** |

`DERIVED`: `2,95,734 / 8,978 = 32.940` · `4,83,395 / 19,523 = 24.760` · `1,41,554 / 8,978 = 15.767` ·
`3,13,437 / 19,523 = 16.055` `[AR FY26, Note 22, PDF p211/pr200]`, `[AR FY26, MD&A, PDF p75/pr64]` and
`[AR FY26, MD&A, PDF p58/pr47]`.

**The two rows point opposite ways and the gap is the finding.** The product line's realisation rose 1.83%;
the *group's* revenue per unit of the quantity that drives 78.51% of it fell 24.83%, because everything
that is not a transaction charge grew `1,03,896 / 92,741 = +12.03%` while premium ADT grew 117.45%
(`51,903 + 17,142 + 34,851 = 1,03,896` against `48,995 + 21,778 + 21,968 = 92,741`)
`[AR FY26, Note 22, PDF p211/pr200]`. BSE is becoming a **thinner** claim on premium turnover at the group
level while being a marginally **fatter** one at the product level. Neither number alone says that.

### 2.2 The take-rate on every disclosed activity measure

| Line | Activity measure | Unit rate FY2025 | Unit rate FY2026 | Δ (index method) | State |
|---|---|---|---|---|---|
| Equity derivatives | premium ADT, ₹ cr | ₹15.767 lakh | ₹16.055 lakh | **+1.83%** | DERIVED |
| Equity derivatives | notional ADT, ₹ cr | ₹1,279.1 | ₹1,674.8 | **+30.93%** | DERIVED |
| Equity derivatives | contracts traded | ₹0.4650 | ₹1.1105 | **+136.9%** | ESTIMATE |
| Equity cash | turnover, ₹ cr | ₹1,572.8 | ₹1,276.6 | **−19.48%** | ESTIMATE |
| StAR MF | orders | ₹3.481 | ₹3.387 | **−2.67%** | DERIVED |
| Listing (annual fee) | listed companies | ₹4.109 lakh | ₹4.273 lakh | **+4.01%** | ESTIMATE |
| Treasury on C&S float | average float | 6.32% | 4.99% | **−21.0%** | ESTIMATE |
| Colocation | racks | n/a | ~₹34.2 lakh/rack | n/a — no prior count | ESTIMATE |

Derivatives, equity cash, StAR MF, listing and treasury rows reproduce `W3_revenue` §1 and are not
re-derived; the two new rows are per-notional and per-contract.
`DERIVED`: `1,41,554 / 1,10,66,674 = 0.012791` lakh `= ₹1,279.1` and
`3,13,437 / 1,87,15,375 = 0.016748` lakh `= ₹1,674.8` per ₹1 crore of notional ADT
`[AR FY26, MD&A, PDF p58/pr47 and PDF p75/pr64]`.
`ESTIMATE` per contract, on the day-count and lot-count assumptions of §0.2:
contracts FY2026 `114.5 × 246.5 = 28,224` Mn and FY2025 `122.5 × 248.5 = 30,441` Mn;
`3,13,437 lakh ÷ 28,224 Mn = ₹1.1105` and `1,41,554 ÷ 30,441 = ₹0.4650` per contract
`[Q1FY27 IP 04Aug2026, PDF p14/slide 13]`. Day-count-neutral index check:
`2.214253 / 0.934694 = 2.368965`, +136.9% against the absolute +138.8% — the 1.9pp gap is the day count and
nothing else. Colocation `17,109 / ~500 racks = ₹34.2` lakh, prior-year rack count `NOT-DISCLOSED ->
Q1FY26 or FY2025 investor presentation, neither of which prints a rack count; the FY2027 MD&A would answer
it` `[Q3FY26 Concall, MD & CEO]`.

> **One trade, three take-rates: +1.83%, +30.93%, +136.9%.** Nothing about the price BSE charges changed.
> The three numbers differ only because premium, notional and contracts moved 117.45%, 69.11% and −6.53%.

### 2.3 Cost per contract — derivable, and it reverses the reported story

`W3_cost` established that one clearing cost carries **three published magnitudes**: consolidated −19.45%,
standalone −4.56%, grossed-up for the intra-group charge −3.04%, and that the MD&A quotes the middle one
and calls it *"a sustainable structural efficiency gain"* `[AR FY26, MD&A, PDF p76/pr65]`. Divided by the
base management itself names as the driver:

| Clearing cost, per contract | FY2025 | FY2026 | Δ, absolute (ESTIMATE) | Δ, index (day-count-neutral) |
|---|---|---|---|---|
| Consolidated (external only) | ₹0.11433 | ₹0.09933 | −13.12% | **−13.82%** |
| Standalone BSE Limited | ₹0.12801 | ₹0.13177 | +2.94% | **+2.11%** |
| **Grossed up for the intra-group charge** | **₹0.13769** | **₹0.14400** | **+4.58%** | **+3.74%** |
| Intra-group charge to the clearing subsidiary | ₹0.02336 | ₹0.04467 | +91.21% | **+89.68%** |
| memo: SEBI regulatory fee, standalone | ₹0.10881 | ₹0.19708 | +81.13% | **+79.67%** |

`ESTIMATE`, contracts as above: `28,035 lakh ÷ 28,224 Mn = ₹0.09933` · `34,805 ÷ 30,441 = ₹0.11433` ·
`37,191 ÷ 28,224 = ₹0.13177` · `38,967 ÷ 30,441 = ₹0.12801` · `40,642 ÷ 28,224 = ₹0.14400` ·
`41,916 ÷ 30,441 = ₹0.13769` · `12,607 ÷ 28,224 = ₹0.04467` · `7,111 ÷ 30,441 = ₹0.02336` ·
`55,625 ÷ 28,224 = ₹0.19708` · `33,123 ÷ 30,441 = ₹0.10881`. Index form:
`(40,642 / 41,916) ÷ 0.934694 = 0.969606 / 0.934694 = 1.037351` `[AR FY26, Consolidated P&L, PDF
p164/pr153]`, `[AR FY26, Standalone P&L, PDF p250/pr239]`, `[AR FY26, Standalone Note 35, PDF p298/pr287]`,
`[AR FY26, Standalone Note 27, PDF p287/pr276]` and `[Q1FY27 IP 04Aug2026, PDF p14/slide 13]`.

> **On the base management names, the group's clearing cost per contract rose 3.74%.** The −3.04% grossed-up
> rupee fall is entirely a 6.53% fall in the quantity being cleared; hold the quantity constant and the unit
> cost went up. The word "efficiency" describes a unit cost, and the unit cost did not improve.

### 2.4 Contribution per contract — the whole wedge in one number

Every derivatives trade generates revenue on premium, a levy on notional, and a clearing cost per
contract. Netting the three against the base they share:

| Per contract (ESTIMATE) | FY2025 | FY2026 | Δ |
|---|---|---|---|
| Equity-derivatives revenue | ₹0.46501 | ₹1.11052 | +138.8% |
| less SEBI regulatory fee (standalone) | (₹0.10881) | (₹0.19708) | +81.1% |
| less clearing cost, grossed up | (₹0.13769) | (₹0.14400) | +4.6% |
| **= contribution per contract** | **₹0.21850** | **₹0.76944** | **+252.1%** |

`ESTIMATE`: `1.11052 − 0.19708 − 0.14400 = 0.76944` and `0.46501 − 0.10881 − 0.13769 = 0.21850`;
`0.76944 / 0.21850 = 3.521`, +252.1% `[AR FY26, MD&A, PDF p75/pr64]`, `[AR FY26, Standalone Note 27, PDF
p287/pr276]` and `[Q1FY27 IP 04Aug2026, PDF p14/slide 13]`.

**None of the 252% is price.** Realisation per unit of premium moved +1.83%; the entire remainder is that
SEBI's November-2024 lot-size increase raised notional per contract from ₹9.03 lakh to ₹16.34 lakh (+80.9%)
while implied volatility and moneyness raised premium per rupee of notional 28.58%. BSE's best unit
economics on record were produced by two regulatory and market-microstructure quantities, in a year when
the number of contracts it cleared **fell**.

### 2.5 The equity-cash repricing, resolved into rate and book

`W3_revenue` F2 sized the equity-cash realisation loss at 6,054 lakh and recorded an open question: *"the
mix within BSE's own turnover between exclusive and dual-listed scrips is not disclosed, so part of the
19.48% could be mix rather than rate, and that split cannot be established."* The revenue side of the split
**is** disclosed, in the same presentation:

| Equity-cash transaction charges (₹ mn) | FY2025 | FY2026 | Δ | Q1FY26 | Q1FY27 | Δ |
|---|---|---|---|---|---|---|
| Normal rate (dual-listed) | 1,394 | 1,451 | **+4.09%** | 324 | 446 | **+37.65%** |
| **Special rate (BSE-exclusive)** | **1,624** | **1,044** | **−35.71%** | 224 | 208 | **−7.14%** |
| Total | 3,018 | 2,495 | −17.33% | 548 | 654 | +19.34% |
| memo: equity-cash ADT (₹ mn) | 77,666 | 79,500 | +2.36% | 71,801 | 99,553 | +38.65% |

`[Q1FY27 IP 04Aug2026, PDF p13/slide 12]`. The FY totals reconcile to the audited/MD&A line to within 0.6%
(`2,495 mn = 24,950 lakh` against 25,021 `[AR FY26, MD&A, PDF p75/pr64]`), which is rounding to ₹ million.

`ESTIMATE`: the special-rate line supplies **111% of the decline** — `1,044 − 1,624 = −580` against a total
change of `2,495 − 3,018 = −523`, i.e. `−580 / −523 = 110.9%`, with the normal-rate line adding +57.
Realisation index by rate book, Q1FY27 against Q1FY26: normal `(446 / 324) ÷ (99,553 / 71,801) = 1.376543 /
1.386513 = 0.992810`, **−0.72%**; total `(654 / 548) ÷ 1.386513 = 0.860738`, **−13.93%**.

> **The equity-cash "repricing" is not a repricing of BSE's ordinary book.** The normal-rate realisation is
> flat to within a percentage point. What is falling is a legacy exclusive-scrip rate whose remaining
> revenue is **10,440 lakh** (`1,044 mn`), 41.8% of the FY2026 equity-cash line and `10,440 / 4,83,395 =
> 2.16%` of consolidated revenue. That is the bounded size of the residual exposure — a number `W3_revenue`
> could not compute.

---

## 3. CAPITAL INTENSITY — regulatory, per overlay §5

BSE is a **zero-debt group by its own declaration**: *"The Group is zero debt company and predominantly
financed its operations through equity"* `[AR FY26, Note 35, PDF p222/pr211]`, corroborated by a finance
cost of 16 lakh, `16 / 4,83,395 = ₹0.003 per ₹100` `[AR FY26, Consolidated P&L, PDF p164/pr153]`. So there
is no leverage layer and the whole of capital intensity is equity and regulatory funds.

### 3.1 What the regulator actually requires

| Requirement | Entity | Amount | Source |
|---|---|---|---|
| SECC Regulation 14 minimum net worth | BSE Limited | ₹100 crore | `[AR FY26, Note 35, PDF p222/pr211]` |
| SECC 2018 minimum net worth, **"or capital under 14(3)(a)/(b), whichever is higher"** | ICCL | ₹100 crore floor | same |
| IFSCA (MII) Regulations 2021 Reg. 14 | India International Clearing Corporation | USD 3 mn | same |
| IFSCA (MII) Regulations 2021 Reg. 14 | India International Exchange | USD 3 mn | same |
| IFSCA global-access circular cl. 3 | India INX Global Access | USD 0.5 mn | same |
| RBI (Financial Benchmark Administrators) Directions 2023 cl. 4(ii) | BSE Index Services | ₹1 crore | same |
| Core settlement guarantee fund (SEBI Minimum Required Contribution) | ICCL + India ICC | **1,24,683** | `[AR FY26, Note 41, PDF p232/pr221]` |

**Rupee-denominated floors total 20,100 lakh** (`100 + 100 + 1 = ₹201 crore`). The USD floors are stated in
dollars and **not converted by the company**: `NOT-DISCLOSED -> AR FY26 Note 35 (PDF p222/pr211) states
USD 6.5 million in aggregate and gives no rupee equivalent; the FY2027 Note 35, or a Note 39 geographic
capital disclosure, would answer it.` At any exchange rate below ₹92/USD the aggregate rupee-equivalent
floor stays under 26,100 lakh, which does not change any conclusion below.

**One reconciliation, so it is not read as a contradiction.** `W3_balancesheet` §3 used floors of 20,000
(BSE Limited and ICCL only). Adding the BSE Index Services ₹1 crore gives 20,100 and moves regulatory
capital per ₹1 of revenue from `(1,24,683 + 20,000) / 4,83,395 = ₹0.2993` to `(1,24,683 + 20,100) / 4,83,395
= ₹0.2995`. Immaterial; both are correct on their stated basis.

### 3.2 The stock measures

| Per ₹1 of revenue from operations | FY2024 | FY2025 | FY2026 | Q1FY27 ann. |
|---|---|---|---|---|
| Core SGF | ₹0.687 | ₹0.383 | **₹0.258** | n/d |
| Core SGF + net-worth floors | ₹0.832 | ₹0.451 | **₹0.300** | n/d |
| Net worth (equity attributable) | ₹2.376 | ₹1.496 | **₹1.380** | **₹1.205** |
| Distributable equity | ₹1.799 | ₹1.222 | ₹1.212 | n/d |
| Physical (PPE + CWIP + intangibles + IAUD) | ₹0.188 | ₹0.107 | ₹0.141 | n/d |
| Regulatory ÷ physical | 3.65× | 3.59× | **1.83×** | n/d |

Core SGF, physical and the regulatory÷physical ratio are `W3_balancesheet` §3's series and are cited, not
recomputed `[AR FY26, Consolidated Balance Sheet, PDF p163/pr152]`. Net worth `DERIVED` from consolidated
net worth as BSE itself publishes it — FY2024 33,023 mn, FY2025 44,237 mn, FY2026 66,730 mn, Q1FY27 75,468
mn `[Q1FY27 IP 04Aug2026, PDF p31/slide 30]`, which ties to the audited equity attributable to shareholders
of 6,67,301 at FY2026 `[AR FY26, Statement of Changes in Equity, PDF p167-168/pr156-157]`:
`3,30,230 / 1,39,003 = 2.376` · `4,42,370 / 2,95,734 = 1.496` · `6,67,300 / 4,83,395 = 1.380` ·
`7,54,680 / (1,56,602 × 4) = 7,54,680 / 6,26,408 = 1.205`. Distributable equity from
`W3_balancesheet` §2. Q1FY27 core SGF balance `NOT-DISCLOSED -> the quarterly filing carries no balance
sheet; the FY2027 half-yearly balance sheet under SEBI LODR Reg. 33(3)(f), or FY2027 Note 41, would answer
it` `[Q1FY27 Results 04Aug2026, consolidated quarterly filing, PDF p5]`.

### 3.3 The two numbers that matter, and they are new

**(a) Regulatory capital is 3.0% of the equity BSE actually carries.**
`DERIVED`: total equity 6,79,550 against rupee-denominated net-worth floors of 20,100 leaves a surplus of
`6,79,550 − 20,100 = 6,59,450`, i.e. `6,59,450 / 6,79,550 = 97.04%` of equity is surplus to the disclosed
minimum. On capital employed including the restricted fund,
`(6,79,550 + 1,24,683) = 8,04,233` against required `(20,100 + 1,24,683) = 1,44,783`, surplus
`6,59,450 / 8,04,233 = 82.0%`. Return on the capital the regulator actually demands is
`2,48,725 / 1,44,783 = 171.8%`; on the capital carried, `2,48,725 / 8,04,233 = 30.9%`
`[AR FY26, Consolidated Balance Sheet, PDF p163/pr152]` and `[AR FY26, Note 35, PDF p222/pr211]`.

**(b) On flow, the overlay's premise has already inverted.**
Per ₹1 of **incremental** revenue in FY2026 (`4,83,395 − 2,95,734 = 1,87,661`):

| Incremental capital per ₹1 of incremental revenue | ₹ |
|---|---|
| Core SGF fund growth (`1,24,683 − 1,13,260 = 11,423`) | **₹0.061** |
| Net-worth floors (unchanged) | ₹0.000 |
| **Total incremental regulatory capital** | **₹0.061** |
| **Cash capex** (`51,516`) | **₹0.275** |
| ratio, physical ÷ regulatory | **4.51×** |

`DERIVED`: `11,423 / 1,87,661 = 0.0609` · `51,516 / 1,87,661 = 0.2745` · `51,516 / 11,423 = 4.51`
`[AR FY26, Note 41, PDF p232/pr221]` and `[AR FY26, Consolidated Cash Flow, PDF p165/pr154]`.

> **Overlay §5 says capital at an MII is regulatory rather than physical. On the FY2026 stock that is still
> true (1.83×). On the FY2026 flow it is false by 4.5×.** `W3_balancesheet` recorded the stock gap closing;
> the flow ratio shows it has already crossed. The reason is on the record on both sides: the core SGF is a
> stress-test output and not a turnover function `[AR FY26, Note 42, PDF p232/pr221]`, while capex tripled
> to build colocation and premises capacity `[AR FY26, MD&A, PDF p76/pr65]`.

**(c) The asymmetry the ratio conceals.** Regulatory capital per ₹1 of revenue fell 62% in two years
because the denominator grew, not because the numerator shrank — the core SGF fund grew every year in the
series (`95,496 → 1,13,260 → 1,24,683`) `[AR FY26, Note 41, PDF p232/pr221]` and the net-worth floors are
fixed rupee amounts that cannot fall at all. **The SEBI Minimum Required Contribution is computed from
monthly stress-test values, so it rises with open interest and volatility — the same conditions under which
turnover-linked revenue falls.** The Q1FY27 charge is already running at `2,591 × 4 = 10,364` annualised
against 7,696 for the whole of FY2026, **+34.67%**, on operating revenue that was flat sequentially
`[Q1FY27 Results 04Aug2026, consolidated quarterly filing, PDF p5]`. This is the only cost layer in the
engine that is structurally **counter-cyclical to revenue**, and the ten-year range of the annual
contribution is 74 (FY2020) to 9,170 (FY2024), a 124× spread `[records/trend_10y.csv]`.

---

## 4. OPERATING LEVERAGE — the contradiction, reconciled

### 4.1 The two files are not measuring the same object

Two statements are on the record and they look incompatible:

- `W3_cost` §4: *"Operating leverage to turnover is 0.159 upward and −0.61 to −0.78 downward."*
- `W3_revenue` §2.3 / `RF-012`: *"Operating leverage for BSE is not measurable from published information."*

**Both are correct, because "operating leverage" is doing two jobs in one phrase.**

| | What was measured | What it needs | Verdict |
|---|---|---|---|
| `W3_cost` | **cost elasticity to a named turnover series** — Δcost% ÷ Δturnover% | two published series | **Measurable, and measured** |
| `W3_revenue` | **attribution of the margin** between operating performance and market structure | all three bases, because revenue, levy and clearing each run on a different one | **Not measurable** |

An elasticity is a ratio of two published growth rates. It requires nothing about *why* either moved.
Attribution requires decomposing a residual, and the residual is the margin. `W3_cost` computed a ratio;
`W3_revenue` said the ratio cannot be read as operating capability. **Neither contradicts the other, and
the correct joint statement is: BSE's cost elasticity to turnover is measurable and its operating leverage
is not interpretable.**

### 4.2 What the third base does to the answer: leverage is a range, not a number

With contracts in hand (§0.2), the *same* cost base can be divided by all three turnover measures for
FY2025→FY2026:

| Cost base | vs premium (+117.45%) | vs notional (+69.11%) | vs contracts (−6.53%) |
|---|---|---|---|
| Total expenses (+24.10%) | **0.205** | **0.349** | **−3.690** |
| **Ex-levy expenses (+10.99%)** | **0.094** | **0.159** | **−1.682** |

`DERIVED`: `10.99 / 117.45 = 0.094` · `10.99 / 69.11 = 0.159` · `10.99 / (−6.53) = −1.682` ·
`24.10 / 117.45 = 0.205` · `24.10 / 69.11 = 0.349` · `24.10 / (−6.53) = −3.690`
`[AR FY26, Consolidated P&L, PDF p164/pr153]`, `[AR FY26, MD&A, PDF p58/pr47]` and
`[Q1FY27 IP 04Aug2026, PDF p14/slide 13]`.

> **`W3_cost`'s +0.159 is correct and it is the middle of three.** The full spread on the identical cost
> base and the identical year is **1.776 elasticity points**, from +0.094 to −1.682, and the sign flips.
> "Operating leverage at BSE" has no single value because *turnover* has no single definition here — and
> the choice of denominator is not an analyst's preference, it is a choice among three quantities the
> company itself says drive three different lines of its own income statement.

**This is the sharper form of `RF-012`'s closure.** `RF-012` said leverage is unmeasurable because a base
is missing. The base is not missing. Leverage is un-*single-valued* because there are three bases and they
diverged by 124 percentage points in one year (`117.45 − (−6.53)`). That is a stronger statement, because
it survives the disclosure improving.

### 4.3 Downward — and a correction to `RF-044`, recorded not resolved

`W3_cost` §4.2 and `RF-044` state: **"The cost base has never contracted in ten years."** Checked against
`records/trend_10y.csv` and re-verified at source, **that is not correct.** Total expenses contracted
twice:

| Window | Total expenses | Δ | Like-for-like? |
|---|---|---|---|
| FY2017 → FY2018 | 47,530 → 42,346 | **−10.91%** | **No** — crosses the verified FY2017 restatement (total expenses restated 47,530 → 40,939) |
| **FY2020 → FY2021** | **55,320 → 53,070** | **−4.07%** | **Yes** — both columns printed on one page of one audited statement |

FY2021 verified at source, both columns on the same page: employee 14,868 against 15,120, technology 9,479
against 11,760, administration 18,541 against 21,318, total **53,070 against 55,320**, `53,070 − 55,320 =
−2,250` `[AR FY2021, Consolidated P&L, PDF p146/pr141]`. FY2017 restatement from `records/restatements.md`
`[AR FY2018, Consolidated P&L, PDF p134]`.

**And the FY2021 contraction happened while turnover rose.** Equity-cash ADT went ₹2,676 crore to ₹4,197
crore, **+56.84%**, stated in the same annual report `[AR FY2021, MD&A, PDF p101/pr96]`. Elasticity
`−4.07 / 56.84 = −0.072` — the best operating-leverage year in the whole record, and it is an *up*-turnover
year that `W3_cost`'s down-window test never examined. The composition points at the cause: technology
−19.4% and administration −13.0% in the first pandemic year, when travel, events and premises spend
stopped.

> **The correct claim is narrower and it survives.** *The cost base has never contracted in a year when
> turnover fell.* In all three down-turnover windows on record it rose — FY2019 −0.507, FY2020 −0.781
> (−0.613 restated), FY2023 −0.750 (`W3_cost` §4.2). The one year it did contract, turnover was rising and
> the cause was an external shutdown of discretionary spend, not a response to falling activity. Both
> `RF-044`'s statement and this correction stand on the record per doctrine §10; QC fails the report if the
> contradiction is silently resolved.

### 4.4 Amendment to `W3_cost`'s Clearing and settlement chain, L3 — stated, not overwritten

`W3_cost` marks that chain **`BROKEN at L2/L3`**, with L3 reading *"there is no published quantity to
divide by"* for the driver. §0.2 supplies a published quantity, at investor-presentation tier. **The break
does not close, and the reason changes:**

- **What is now measurable:** cost per contract, on all three published magnitudes (§2.3). The grossed-up
  group figure rose 3.74%, which *contradicts the MD&A's "structural efficiency gain"* more directly than
  the rupee comparison did.
- **What is still broken:** the two proxies still disagree. Per contract, the intra-group charge rose
  89.68% while the consolidated external line fell 13.82% — a spread of **103.50 percentage points**,
  *wider* than the 96.74pp `W3_revenue` measured on rupees. Dividing by the correct base does not reconcile
  a transfer price with an external price; it only shows that the disagreement was never about the base.
- **What this settles:** `W3_revenue` §2.3's internal test — *"if +77.29% were contract growth, average
  notional per contract fell 4.61%, which the lot-size increase contradicts"* — is now answered directly.
  Notional per contract **rose 80.9%**, so the intra-group charge's +77.29% was **not** contract growth. The
  ICCL charge rose 89.68% *per contract*. It is a transfer-price change, and no policy, benchmark or
  arm's-length assertion exists for it (`G-COST-02`; AOC-2 declared "not applicable"
  `[AR FY26, Board's Report, PDF p31/pr20]`).

### 4.5 What a downturn does, given all of the above

The robust statement about a downturn is **a numerator fact, not an elasticity**, and that is why it
survives having three denominators:

1. **Absolute total expenses rose in nine of the ten years read**, and the single exception was a pandemic
   year with rising turnover (§4.3) `[records/trend_10y.csv]`.
2. **The floor is 1,18,773 of ex-levy expenses**, plus roughly 1,212 of depreciation already committed from
   FY2026 additions, less 1,301 of non-recurring past service cost (`W3_cost` §9).
3. **Two of the four layers that would have to fall cannot.** The core SGF rises with stress-tested
   exposure (§3.3c), and depreciation is committed. Together they are `1.5921 + 3.2884 = ₹4.88` per ₹100
   and neither is a management variable.
4. **Only ₹15.48 of the ₹100 is discretionary** (§1.1). Even a 20% cut in every discretionary layer —
   which has never happened at this company — recovers ₹3.10 per ₹100 against a revenue reversion to FY2025
   levels that would remove roughly ₹39 of revenue per ₹100.

`DERIVED`: `(29,781 + 20,313 + 24,732) × 0.20 = 14,965` and `14,965 / 4,83,395 = ₹3.10 per ₹100`;
reversion `(4,83,395 − 2,95,734) / 4,83,395 = 38.82%` `[AR FY26, Consolidated P&L, PDF p164/pr153]`.

---

## 5. THE SEQUENTIAL STALL — FY2026's economics, recomputed on Jun-2026

FY2026 closed 31-Mar-2026, at the top of the run. The **first quarter after the annual accounts**, Jun-2026,
is the last observation in the record and the annual report cannot show it.

**Source of record: the Q1FY27 consolidated filing.** It supersedes the extraction in
`records/quarterly_series.csv` in three places and those corrections are made here:
(i) the Jun-2026 **core SGF contribution is 2,591**, not the "2" the extractor produced;
(ii) Jun-2026 **other expenses of 6,316** sit against an FY2026 comparative of **24,748** in the quarterly
presentation, which is the audited 24,732 plus the 16 of finance cost — the quarterly format has no
separate finance-cost line;
(iii) the **Jun-2025 comparative has been restated** from 95,839 to **95,795** of revenue from operations,
with other income moving 700 to 744, a pure reclassification of 44 (`95,839 + 700 = 95,795 + 744 = 96,539`)
`[Q1FY27 Results 04Aug2026, consolidated quarterly filing, PDF p5]` and
`[Q1FY26 Results 07Aug2025, consolidated quarterly filing, PDF p5]`.

### 5.1 The quarter, and what actually moved

| ₹ lakh, consolidated | Jun-2025 | Mar-2026 | **Jun-2026** | QoQ | YoY |
|---|---|---|---|---|---|
| Revenue from operations | 95,795 | 1,56,351 | **1,56,602** | **+0.16%** | +63.48% |
| Investment income | 7,906 | 6,169 | **13,518** | **+119.13%** | +70.98% |
| Total income | 1,04,445 | 1,63,017 | 1,70,672 | +4.70% | +63.41% |
| Total expenses | 35,934 | 55,694 | 53,669 | −3.64% | +49.35% |
| Ex-levy expenses | 24,308 | 35,722 | 34,391 | −3.73% | +41.48% |
| Contribution to core SGF | — | 2,072 | 2,591 | +25.05% | n/a |
| PBT | 70,140 | 1,06,345 | 1,16,366 | +9.42% | +65.91% |
| PAT attributable | 53,941 | 79,733 | 87,402 | +9.62% | +62.03% |

`[Q1FY27 Results 04Aug2026, consolidated quarterly filing, PDF p5]`. `DERIVED`:
`1,56,602 − 1,56,351 = 251` and `251 / 1,56,351 = +0.16%`; ex-levy `53,669 − 19,278 = 34,391`,
`55,694 − 19,972 = 35,722`, `35,934 − 11,626 = 24,308`.

**The sequential PBT bridge — every rupee of the +10,021.**

| Driver | ₹ lakh | % of the +10,021 |
|---|---|---|
| **Investment income** | **+7,349** | **73.34%** |
| Other expenses (non-repeat of a one-off) | +3,687 | 36.79% |
| Depreciation | +1,219 | 12.16% |
| Share of associate profit | +860 | 8.58% |
| Regulatory levy | +694 | 6.93% |
| **Revenue from operations** | **+251** | **2.50%** |
| Other income | +55 | 0.55% |
| Clearing and settlement | −303 | −3.02% |
| Core SGF | −519 | −5.18% |
| Technology | −919 | −9.17% |
| Employee benefits | −2,353 | −23.48% |
| **Total** | **+10,021** | **100.00%** |

`DERIVED`, each line is Jun-2026 less Mar-2026 with the sign that helps PBT; sum
`7,349 + 3,687 + 1,219 + 860 + 694 + 251 + 55 − 303 − 519 − 919 − 2,353 = 10,021` against
`1,16,366 − 1,06,345 = 10,021`, zero residual `[Q1FY27 Results 04Aug2026, consolidated quarterly filing,
PDF p5]`.

**The 3,687 is not a cost improvement.** The CFO explains it: *"there was a provision of about Rs. 40 crores
made in our subsidiary clearing company from one of the debtors. Because of that, in previous quarter,
other expenses were slightly higher"* `[Q1FY27 Concall 10Aug2026, CFO]`. So `4,000` of the Mar-2026 base
does not repeat, and `3,687 / 4,000 = 92%` of the favourable other-expenses movement is that non-repeat.

> **Two items — investment income and the non-repeat of a receivables provision — supply
> `(7,349 + 3,687) / 10,021 = 110.1%` of the sequential profit increase. The operating top line supplied
> 2.5%.**

### 5.2 The ₹100 engine on the Jun-2026 quarter

| ₹ per ₹100 of revenue from operations | FY2026 | **Jun-2026 quarter** | Δ |
|---|---|---|---|
| Investment income | 6.01 | **8.63** | +2.62 |
| Other income | 0.49 | 0.35 | −0.14 |
| Employee benefits | 6.16 | 5.56 | +0.60 |
| Technology | 4.20 | 3.88 | +0.32 |
| Clearing and settlement | 5.80 | 5.76 | +0.04 |
| Regulatory levy | 13.44 | 12.31 | +1.13 |
| Other expenses | 5.12 | 4.03 | +1.09 |
| Depreciation | 3.29 | 2.72 | +0.57 |
| **Total expenses** | **38.01** | **34.27** | +3.74 |
| Core SGF | 1.59 | 1.65 | −0.06 |
| Share of associate profit | 1.35 | 1.25 | −0.10 |
| Tax | 17.04 | 18.58 | −1.54 |
| **PAT attributable** | **51.66** | **55.81** | **+4.15** |

`DERIVED`, each Jun-2026 line ÷ 1,56,602 × 100: `13,518 / 1,56,602 = 8.63` · `53,669 / 1,56,602 = 34.27` ·
`19,278 / 1,56,602 = 12.31` · `2,591 / 1,56,602 = 1.65` · `29,100 / 1,56,602 = 18.58` ·
`87,402 / 1,56,602 = 55.81`. Tie: `100 + 8.63 + 0.35 − 34.27 − 1.65 + 1.25 − 18.58 + 0.09 = 55.81` ✓
`[Q1FY27 Results 04Aug2026, consolidated quarterly filing, PDF p5]`.

**The engine looks better and is more dependent on things that are not the toll.** Of the +4.15 of PAT per
₹100, **+2.62 is investment income** — a return on the company's own securities portfolio, which
`W3_balancesheet` measured at 90.4% of total equity — and a further +1.09 is the Mar-2026 provision not
repeating. `2.62 / 4.15 = 63.1%` of the improvement in the engine is non-operating.

### 5.3 Unit economics, recomputed on Jun-2026

| Unit | FY2026 | Q1FY27 | Basis of change |
|---|---|---|---|
| Premium ADT (₹ cr) | 19,523 | 29,615 | +51.69% vs FY2026; **+2.40% QoQ** |
| Notional ADT (₹ cr) | 1,87,15,375 | 2,37,00,000 | +26.63% vs FY2026; **−3.27% QoQ** |
| Contracts, avg daily lots (Mn) | 114.5 | 156 | +36.24% vs FY2026; **+3.31% QoQ** |
| **Premium ÷ notional** | 0.104315% | **0.124959%** | **+19.79% vs FY2026; +5.86% QoQ** |
| Notional per contract (₹ lakh) | 16.34 | 15.19 | **−7.04%** |
| **EQD realisation index, QoQ** | — | **1.000006** | **+0.001%** — dead flat |
| **EQD realisation index, YoY** | +1.83% (FY26) | **0.983726** | **−1.63%** |
| EQD realisation, Q1FY27 annualised vs FY2026 | — | 0.971674 | **−2.83%** |
| Equity-cash realisation index, YoY | −19.48% (FY26) | 0.860738 | **−13.93%** |
| StAR MF, ₹ per order | ₹3.391 | ₹3.132 | **−6.33% YoY**, against −2.56% in FY2026 |

`DERIVED` / `ESTIMATE` as marked in §2. Q1FY27 activity `[Q1FY27 IP 04Aug2026, PDF p14/slide 13]` and
`[Q1FY27 Concall 10Aug2026, MD & CEO]` (*"average daily premium turnover reaching an all-time high of Rs.
29,615 crores"*). Realisation QoQ: `(11,550 / 11,279) ÷ (2,96,154 / 2,89,207) = 1.024027 / 1.024021 =
1.000006`. YoY: `(11,550 / 5,980) ÷ (2,96,154 / 1,50,838) = 1.931438 / 1.963391 = 0.983726`.
Premium/notional: `29,615.4 / 2,37,00,000 = 0.124959%` against `19,523 / 1,87,15,375 = 0.104315%`.
StAR MF `[Q1FY27 IP 04Aug2026, PDF p16/slide 15]`: `733 mn / 234 Mn orders = ₹3.132` against
`612 / 183 = ₹3.344`, and FY2026 `2,852 / 841 = ₹3.391` against FY2025 `2,307 / 663 = ₹3.480`.

**Three things this changes.**

**(a) The one line where realisation was rising has stopped.** Derivatives realisation was +1.83% in
FY2026; it is **exactly flat sequentially and −1.63% year-on-year** in Q1FY27. Every disclosed realisation
series at BSE is now flat or negative.

**(b) The wedge moved further in BSE's favour — and it is more volatile than the annual series shows.**
Premium/notional by quarter: `Q1FY26 0.115144% · Q2FY26 0.091491% · Q3FY26 0.092662% · Q4FY26 0.118044% ·
Q1FY27 0.124959%` `DERIVED` from `[Q1FY27 IP 04Aug2026, PDF p14/slide 13]`. The quarterly range is
`0.124959 / 0.091491 = 1.366`, **±37% within eight quarters**, against the +28.58% annual move `W3_revenue`
sized. `W3_revenue` costed a reversion to FY2025's 0.081126% at 17,709 lakh of derivatives revenue; a
reversion merely to the **Q2FY26 level already observed in this cycle** — 0.091491% — costs
`3,13,437 × (1 − 0.091491 / 0.104315) = 38,535` lakh at unchanged premium turnover, `DERIVED` and larger
than the annual-series estimate because the quarterly low is lower than the annual low.

**(c) Notional fell while premium rose — for the first time in the series.** Q1FY27 is the only quarter in
the thirteen disclosed where notional ADT falls (`245 → 237`) while premium ADT rises (`2,89,207 →
2,96,154`). The levy base contracted while the revenue base grew. That is the wedge working *for* BSE and
it is precisely the movement management says is unforecastable: *"whether we can predict this trend, it is,
of course, not predictable"* `[Q4FY26 Concall 13May2026, MD & CEO]`.

### 5.4 Operating leverage in the stall quarter

| Window | Ex-levy expenses | Notional ADT | Elasticity |
|---|---|---|---|
| Q1FY26 → Q1FY27 (YoY) | 24,308 → 34,391 = **+41.48%** | +80.92% | **+0.513** |
| Q4FY26 → Q1FY27 (QoQ), **as reported** | 35,722 → 34,391 = **−3.73%** | −3.27% | **+1.141** |
| Q4FY26 → Q1FY27 (QoQ), **ex the ₹40 cr provision** | 31,722 → 34,391 = **+8.41%** | −3.27% | **−2.577** |

`DERIVED`: `34,391 / 24,308 = 1.4148` · `34,391 / 35,722 = 0.9627` · `34,391 / (35,722 − 4,000) = 1.0841`;
notional `237 / 131 = 1.8092` and `237 / 245 = 0.9673` `[Q1FY27 Results 04Aug2026, consolidated quarterly
filing, PDF p5]`, `[Q1FY27 IP 04Aug2026, PDF p14/slide 13]` and `[Q1FY27 Concall 10Aug2026, CFO]`.

> **`W3_cost`'s thesis-breaker fired, and it fails on inspection.** `W3_cost` F4 named as its thesis-breaker
> *"a single quarter in which absolute expenses fall alongside turnover, which has not occurred in the ten
> years read."* In Jun-2026 total expenses fell 3.64% while notional turnover fell 3.27%. **It occurred.**
> Strip the ₹40 crore provision that management says inflated the Mar-2026 base and the same comparison
> reads +3.82% of expenses against −3.27% of turnover, an elasticity of **−1.168** — the negative-downward
> signature, intact. **The first apparent contradiction of the ratchet in ten years is a one-off provision
> not repeating.**

Year-on-year the deterioration is the more durable reading: **ex-levy cost elasticity to notional has gone
from 0.159 for FY2026 to 0.513 for Q1FY27.** Controllable costs now capture half of turnover growth,
against one-sixth in the annual accounts — employee benefits +24.30%, technology +21.91% and clearing
+62.67% year-on-year against revenue +63.48% `[Q1FY27 Results 04Aug2026, consolidated quarterly filing, PDF
p5]`.

### 5.5 Capital intensity in the stall quarter

Net worth per ₹1 of revenue fell again, `7,54,680 / 6,26,408 = ₹1.205` against ₹1.380, because retained
profit compounded on flat operating revenue `[Q1FY27 IP 04Aug2026, PDF p31/slide 30]`. Against that, the
core SGF **charge** annualises 34.67% higher on a flat top line (§3.3c). Both movements are the same
mechanism seen from opposite ends: **the capital this business carries is discretionary and the capital the
regulator demands is counter-cyclical.**

### 5.6 How this quarter is being presented

*"Q1 FY2027 being the company's best quarterly results on record and the 14th consecutive quarter of record
revenues. Consolidated revenues stood at Rs. 1,707 crores, surpassing the previous quarter's record of Rs.
1,630 crores"* `[Q1FY27 Concall 10Aug2026, MD & CEO]`. The figure quoted is **total income** — `1,70,672`
against `1,63,017`, +4.70% — of which `7,349 / 7,655 = 96.0%` of the increase is investment income. On
**revenue from operations** the same comparison is +0.16%. Both statements are true; they are not the same
statement, and only one of them is the toll.

The same remarks add: *"54% of the total operating expenses are attributable to regulatory fees and clearing
and settlement expenses, all of which is directly correlated to increasing transaction volumes"*
`[Q1FY27 Concall 10Aug2026, MD & CEO]`. `DERIVED`: `(19,278 + 9,028) / 53,669 = 52.74%` on the consolidated
face. The share is right; **"transaction volumes" is three different volumes** — the levy tracks notional
(−3.27% this quarter), clearing tracks contracts (+3.31%), and revenue tracks premium (+2.40%).

---

## 6. FINDINGS

### FINDING: Of every ₹100 of BSE's revenue, ₹32.07 is taken by a regulator or the tax code and only ₹15.48 is decided by management
S1 WHAT: On the FY2026 consolidated basis, ₹100 of revenue from operations plus ₹6.50 of income leaves ₹51.66 of PAT attributable; ₹54.84 leaves the engine, of which the regulatory levy 13.44, the core SGF 1.59 and tax 17.04 together are ₹32.07 `[AR FY26, Consolidated P&L, PDF p164/pr153]`.
S2 WHY: An exchange is a toll booth whose toll, whose levy base and whose settlement-fund capital are all set by third parties. The levy is assessed on notional option value at a rate SEBI fixed and BSE stopped contesting after SEBI's letter of 14-Aug-2024 `[AR FY25, Note 46, PDF p217/pr206]`; the core SGF is a stress-test Minimum Required Contribution `[AR FY26, Note 42, PDF p232/pr221]`; the tax rate is statutory. None of the three is a management variable, and the fourth-largest layer, clearing and settlement at ₹5.80, is a group-structure and transfer-price output rather than a negotiated price (`W3_cost` §2).
S3 EVIDENCE: `DERIVED` per ₹100 of revenue from operations of 4,83,395: employee 6.16, clearing 5.80, other expenses 5.12, technology 4.20, depreciation 3.29, finance cost 0.003, levy 13.44, core SGF 1.59, tax 17.04; total leakage `106.4988 − 51.6551 = 54.84`; regulator-and-tax share `32.075 / 54.844 = 58.48%`; discretionary annual spend `(29,781 + 20,313 + 24,732) / 4,83,395 = ₹15.48`, `15.479 / 54.844 = 28.22%`. **The counter-proportion that decides it:** the regulator-and-tax block is 58.48% of the leakage but was 48.77% a year earlier (`(13.8794 + 3.0433 + 14.5810) / 64.5992`) — so the leakage fell 9.76 points per ₹100 while the regulator's share of what remains rose 9.71 points. Growth made BSE more profitable and more regulator-dependent in the same year `[AR FY26, Consolidated P&L, PDF p164/pr153]`.
S4 CONNECTS: The Industry record locates the pricing authority outside the company in three places at once — SEBI for the levy and expiry framework, RBI for the ETCD directions that took currency-derivatives ADT from ₹9,733.67 crore to nil, and the Finance Ministry for STT (`W2_industry` §4 correction). Management commentary claims the levy "does not impact the operating efficiency of the business" `[AR FY26, MD&A, PDF p76/pr65]`, which is true to six basis points for FY2026 and false as a general statement, since the company's own table on the same page shows the levy moving −140bps of standalone operating revenue. The Notes supply the mechanism: SEBI regulatory fees are 87.1% of the levy line and 98.1% of its increase `[AR FY26, Note 27, PDF p212/pr201]`.
DOMAINS: IncomeStatement, Notes, MgmtCommentary, Industry
DISCONFIRM: Searched for and found, and it cuts hard. (i) Tax is not BSE-specific — every Indian company pays it, and stripping tax leaves the regulator at `15.032 / 37.801 = 39.77%` of the remaining leakage, a materially smaller claim. (ii) The levy fell as a share of revenue in FY2026, 13.88% to 13.44%, so the regulator's *rate* claim eased. (iii) The three discretionary layers all fell as a share of revenue — employee 8.00 to 6.16, technology 5.56 to 4.20, other 7.04 to 5.12 — which is genuine scale over a fixed base and is what the overlay predicts for an exchange. What survives all three: the direction of the regulator-set layers is not a company decision in either direction, and the discretionary block is too small to offset them.
S5 MEANS: BSE's profit per rupee of revenue is mostly a statement about what SEBI and the Income-tax Act took this year, not about how the company ran, and the ₹15.48 that management actually decides is smaller than the ₹15.03 of levy and settlement-fund contribution it cannot touch — so a margin forecast for this company is in substance a regulatory forecast wearing an operating label.
BASE-RATE: Realised, three times in three years, all regulator-authored: SEBI's 26-Apr-2024 re-basing of the fee to notional value with 15% interest, whose independently derived retrospective element is 7,347 lakh, 9.52% of FY2024 PAT (`W3_cost` §6); RBI's 5-Jan-2024 ETCD directions, which extinguished the currency-derivatives segment entirely; and SEBI's true-to-label charging from 1-Oct-2024, which cost 6,054 lakh of equity-cash revenue on rising volume (`W3_revenue` F2). No year in the last three has passed without a regulator moving a layer of this engine.
S6 IMPLICATION: The base-case margin assumption must be built as three separate assumptions — a levy rate on notional, an MRC on stress-tested exposure, and a statutory tax rate — rather than as one cost ratio, because the three move on different clocks and only one of them responds to activity; the monitorable is the regulator-and-tax share of leakage recomputed each year from the face of the P&L, and the thesis-breaker is that share passing 65%, which on FY2026 revenue would remove roughly ₹3.6 per ₹100 of PAT with no change in anything BSE does.
SEVERITY: High

### FINDING: The leverage contradiction between W3_cost and W3_revenue is not a contradiction — an elasticity was measured and an attribution was not, and both files are right
S1 WHAT: `W3_cost` §4 states operating leverage to turnover is +0.159 upward and −0.61 to −0.78 downward. `W3_revenue` §2.3 and `RF-012` state operating leverage "is not measurable from published information". Both statements are on the record and they appear to be incompatible.
S2 WHY: The phrase carries two different objects. An elasticity is the quotient of two published growth rates and needs nothing but two series, which exist. An attribution decomposes the margin between operating performance and market structure, and that needs all three of the bases management names, because revenue runs on premium, the levy on notional and clearing on contracts `[Q4FY26 Concall 13May2026, MD & CEO]`. `W3_cost` computed a ratio. `W3_revenue` said the ratio cannot be read as operating capability. Neither claim entails the other.
S3 EVIDENCE: With the contract base recovered (§0.2), the same cost base divided by the three simultaneously-true turnover measures for FY2025→FY2026 gives ex-levy elasticities of `10.99 / 117.45 = 0.094` to premium, `10.99 / 69.11 = 0.159` to notional, and `10.99 / (−6.53) = −1.682` to contracts; on total expenses, 0.205, 0.349 and −3.690 `[AR FY26, Consolidated P&L, PDF p164/pr153]`, `[AR FY26, MD&A, PDF p58/pr47]` and `[Q1FY27 IP 04Aug2026, PDF p14/slide 13]`. **The asymmetry that makes this a finding rather than a caveat:** the three denominators moved +117.45%, +69.11% and −6.53% in a single year — a spread of 123.98 percentage points on one quarter's worth of the same trades — while the numerator has exactly one value, 10.99%. A single-valued leverage number requires a single-valued turnover, and BSE does not have one.
S4 CONNECTS: The Industry record explains why the three diverged with nothing at BSE changing: SEBI's November-2024 lot-size increase raised notional per contract from ₹9.03 lakh to ₹16.34 lakh, and implied volatility and moneyness raised premium per rupee of notional 28.58% (`W2_industry` §2; `W3_revenue` §2.2). Management commentary claims the opposite reading of the same year — "the inherent operating leverage of BSE's exchange model" `[AR FY26, MD&A, PDF p74/pr63]` — without naming a turnover measure. The Notes confirm the levy tracked notional to within 1.02% and revenue tracked premium to within 1.83%, so the divergence is measured, not inferred `[AR FY26, Note 27, PDF p212/pr201]`.
DOMAINS: IncomeStatement, Notes, MgmtCommentary, Industry
DISCONFIRM: Searched for and found. (i) Notional is defensibly the *right* denominator for a levy-inclusive elasticity, because the levy is 67.05% of the FY2026 cost increase and is assessed on notional — on that reading 0.349 is the correct single number and there is no ambiguity. (ii) The contract-based elasticity of −1.682 is arithmetically unstable near a small denominator: contracts fell only 6.53%, so a 1-point measurement error in the lot series moves the elasticity by roughly 0.3. (iii) The contract series is investor-presentation tier, the lowest above media, and BSE could withdraw it without breaching anything. What survives: even discarding the contract row entirely, premium and notional alone give 0.094 and 0.159 — a 69% difference on the same cost base — so the range does not depend on the new input.
S5 MEANS: The honest single statement about operating leverage at BSE is that cost elasticity to turnover is measurable and takes three values between +0.094 and −1.682 depending on which of three co-existing turnover measures is chosen, while the attribution of the margin between operating capability and market structure is not measurable at all — so any report that quotes one leverage number for this company has silently chosen a denominator and should say which.
BASE-RATE: Realised, at this company, and the denominator choice has already cost money once. The 26-Apr-2024 SEBI letter re-based the levy from premium-adjacent to notional value retrospective to FY2007 with 15% interest; the independently derived retrospective charge is 7,347 lakh, 9.52% of FY2024 consolidated PAT of 77,166 (`W3_cost` §6). That is a completed cash loss arising purely from which base a ratio is computed on, which is the same class of error this finding is about.
S6 IMPLICATION: Any driver model for BSE must carry premium turnover, notional turnover and contract count as three separate exogenous inputs with their own ranges rather than a single "turnover growth" assumption, because a cost forecast anchored to the wrong one is wrong by up to 1.78 elasticity points; the monitorable is the quarterly investor presentation's three-series slide, which publishes all three together and is the only place they appear side by side, and the thesis-breaker is BSE withdrawing the lots series from that slide, which would return the third base to genuinely unpublished.
SEVERITY: High

### FINDING: The clearing cost management calls a structural efficiency gain rose 3.74% per contract — the base it fell on is the base that shrank
S1 WHAT: The MD&A explains a 5% decline in clearing and settlement expense as "a sustainable structural efficiency gain" `[AR FY26, MD&A, PDF p76/pr65]`. Divided by contracts — the base management itself names as the driver of that cost — the group's clearing cost per contract **rose 3.74%** on the grossed-up basis and 2.11% on the standalone.
S2 WHY: The number of contracts cleared fell 6.53% in FY2026, from 122.5 to 114.5 million average daily lots, because SEBI's November-2024 lot-size increase doubled the size of each contract. A rupee cost that falls 3.04% while the quantity being processed falls 6.53% is a unit cost that rose. The word "efficiency" describes a unit cost, and the rupee comparison the MD&A quotes holds no unit constant.
S3 EVIDENCE: `ESTIMATE` per contract on annual contracts of `114.5 × 246.5 = 28,224` Mn (FY2026) and `122.5 × 248.5 = 30,441` Mn (FY2025): grossed-up clearing cost `40,642 ÷ 28,224 = ₹0.14400` against `41,916 ÷ 30,441 = ₹0.13769`, +4.58% absolute and +3.74% on the day-count-neutral index `(40,642 / 41,916) ÷ 0.934694 = 1.037351`; standalone `₹0.13177` against `₹0.12801`, +2.11% on the index; consolidated external `₹0.09933` against `₹0.11433`, −13.82% `[AR FY26, Consolidated P&L, PDF p164/pr153]`, `[AR FY26, Standalone P&L, PDF p250/pr239]` and `[Q1FY27 IP 04Aug2026, PDF p14/slide 13]`. **The counter-proportion that identifies the mechanism:** the intra-group charge to the clearing subsidiary rose 89.68% per contract while the external consolidated line fell 13.82% per contract — a spread of 103.50 percentage points, **wider** than the 96.74pp `W3_revenue` measured on rupees. Dividing by the right base does not narrow the disagreement, which proves the disagreement was never about the base but about a transfer price.
S4 CONNECTS: The Governance dimension is that the transfer price has no disclosed basis: no accounting policy addresses clearing and settlement expense, no benchmark or arm's-length assertion exists for the 12,607 charged by the wholly owned clearing corporation, and the Board's Report declares AOC-2 "not applicable" for FY2025-26 `[AR FY26, Board's Report, PDF p31/pr20]` and `[AR FY26, Standalone Note 35, PDF p298/pr287]`. The Notes show the consequence in the group accounts: the clearing corporation's contribution to consolidated profit fell 37.22% to 6,805 while its own standalone PAT rose 6.27% to 16,979 `[AR FY26, Note 40, PDF p229/pr218]`. Business context closes it — the quarterly series shows the underlying cost tracking activity almost exactly, `5,550 (Jun-2025) → 9,028 (Jun-2026) = +62.67%` against revenue +63.48% `[Q1FY27 Results 04Aug2026, consolidated quarterly filing, PDF p5]`, which is inconsistent with a durable structural saving.
DOMAINS: IncomeStatement, Notes, MgmtCommentary, Governance
DISCONFIRM: Searched for and found, and it is real. (i) The consolidated −19.45% is a genuine reduction in cash leaving the group, and on the consolidated per-contract basis the fall survives at −13.82%, so the group is better off on the reported line whichever base is used. (ii) The per-contract figures rest on an investor-presentation lot count and a trading-day assumption, both weaker evidence than the audited rupees. (iii) The clearing system was genuinely rebuilt during the year — "the clearing system has gotten revamped… trades/second per member per client improved 9x" `[Q1FY27 IP 04Aug2026, PDF p18/slide 17]` — so a capability improvement did occur even if the cost line does not evidence it. What survives: the grossed-up group cost per contract still rose, and management quoted neither the consolidated figure nor any unit measure.
S5 MEANS: The only unit in which BSE's clearing cost improved in FY2026 is the rupee, and the rupee fell because SEBI made each contract twice as large — so the "structural efficiency gain" is a lot-size effect and an intra-group elimination wearing an operating description, and the cost per unit of the thing actually being cleared went up.
BASE-RATE: This is the third verified instance at this company of the MD&A attributing a favourable movement to a cause its own numbers refute — the equity-cash "industry-wide reduction in average daily turnover" against BSE's own turnover rising 2.36% seventeen pages earlier (`W3_revenue` F2), the clearing "structural efficiency" of which 81.18% of the fall is an intra-group elimination (`W3_cost` F2), and now the same claim failing on the unit basis. No realised loss has been established from any of the three; the base rate here is a pattern of narration and it is now three for three.
S6 IMPLICATION: A forward clearing-cost assumption should be built per contract and then multiplied by an expected contract count, not extrapolated from the reported rupee line, because the reported line embeds a one-off doubling of contract size that cannot repeat; the monitorable is the average-daily-lots series on the quarterly presentation's derivatives slide against the clearing line in the same filing, available every quarter, and the thesis-breaker is a quarter in which contracts and clearing cost move together at similar rates, which would show the unit cost stabilising.
SEVERITY: High

### FINDING: BSE's best unit economics on record were produced in a year its contract count fell 6.53%, and none of the gain is price
S1 WHAT: Contribution per derivatives contract — revenue less the SEBI levy less the grossed-up clearing cost — rose from ₹0.2185 to ₹0.7694, **+252.1%**, in a year when the number of contracts traded fell 6.53% and realisation per rupee of premium rose only 1.83% `[Q1FY27 IP 04Aug2026, PDF p14/slide 13]` and `[AR FY26, MD&A, PDF p75/pr64]`.
S2 WHY: Two exogenous quantities moved. SEBI's lot-size increase from 20-Nov-2024 raised notional per contract from ₹9.03 lakh to ₹16.34 lakh, so each contract carried 80.9% more notional; and implied volatility and moneyness raised premium per rupee of notional 28.58%, so each rupee of notional carried more premium. Revenue is charged on premium and the costs are charged on notional and contracts, so both movements landed on the same side of the unit economics.
S3 EVIDENCE: `ESTIMATE` per contract: revenue `₹1.11052` against `₹0.46501` (+138.8%); SEBI fee `₹0.19708` against `₹0.10881` (+81.1%); grossed-up clearing `₹0.14400` against `₹0.13769` (+4.6%); contribution `1.11052 − 0.19708 − 0.14400 = ₹0.76944` against `0.46501 − 0.10881 − 0.13769 = ₹0.21850`, `0.76944 / 0.21850 = 3.521` `[AR FY26, Standalone Note 27, PDF p287/pr276]`. **The counter-proportion:** revenue per contract rose 138.8% while revenue per rupee of premium rose 1.83% — a 137-point gap on the same revenue line, which is the entire measure of how much of the gain is unit redefinition rather than pricing. Sized in rupees, holding contracts constant at the FY2025 count of 30,441 Mn would put FY2026 derivatives revenue at `0.46501 × 1.0183 × 30,441 Mn = ₹1,44,146` lakh against the actual 3,13,437 — i.e. `3,13,437 − 1,44,146 = 1,69,291` lakh of the derivatives line, 54.0% of it, exists because each contract became bigger and richer, not because more of them traded or because BSE charged more.
S4 CONNECTS: The Industry record supplies the authorship — lot size, expiry day and position limits are SEBI's, and the same 2024 framework that raised lot sizes also took Bankex to monthly expiry `[AR FY25, MD&A policy list, PDF p50/pr39]`. Business context supplies the concentration: equity derivatives are 64.84% of consolidated revenue and one index on one weekly expiry day (`W2_industry` F4). Management commentary confirms it does not manage to the quantity that moved — "we do not measure our success in terms of market share… our primary goal is deepening and broadening of markets" `[Q1FY27 Concall 10Aug2026, MD & CEO]` — and describes the notional-to-premium relationship as not predictable `[Q4FY26 Concall 13May2026, MD & CEO]`.
DOMAINS: IncomeStatement, Industry, Business, MgmtCommentary
DISCONFIRM: Searched for and found. (i) A lot-size increase is not costless to BSE — it raises the minimum ticket for a retail participant and was explicitly intended by SEBI to reduce retail derivatives participation, so the same rule that improved unit economics shrank the participant base, and contracts falling 6.53% is the visible half of that. (ii) The contribution measure omits every fixed cost, so it is a gross unit margin and not a profit per contract; on total expenses per contract the increase is a much smaller 32.77%. (iii) BSE did add participants over the same period — 610 members and 650 FPIs against a target of 800 `[Q1FY27 Concall 10Aug2026, MD & CEO]` — which is a genuine broadening independent of contract size. What survives: none of the 252% is attributable to a price BSE set.
S5 MEANS: The unit economics that make FY2026 look like a step-change in business quality are a redefinition of the unit by the regulator, so the correct forward question is not whether BSE can sustain a ₹0.77 contribution per contract but whether SEBI leaves the contract the size it is — and a reversal of the lot-size decision would compress the unit while raising the count, with the net effect running through the premium-to-notional ratio rather than through anything BSE prices.
BASE-RATE: Realised, and in the unfavourable direction, twice. SEBI's own 2024 framework already reduced BSE's contract count — average daily lots fell from 153 Mn in Q2FY25 to 83 Mn in Q4FY25, −45.8%, immediately after the lot-size and single-weekly-expiry measures took effect `[Q1FY27 IP 04Aug2026, PDF p14/slide 13]`. And RBI's 5-Jan-2024 ETCD directions took an entire BSE segment from ₹9,733.67 crore of ADT to nil within two years (`W2_industry`). Regulator-authored redefinitions of a traded unit have moved this company's volumes by tens of percent twice in three years.
S6 IMPLICATION: The durability of FY2026's unit economics rests on a regulatory parameter — index-option lot size — that is not a company variable and has already been changed once in the observation window, so a driver model should carry notional-per-contract as an explicit assumption alongside premium turnover rather than treating unit revenue as a franchise property; the monitorable is notional per contract, computable each quarter as the presentation's notional ADT divided by its average daily lots, and the thesis-breaker is that ratio falling while premium turnover is flat, which would mean the unit is shrinking without the count recovering.
SEVERITY: High

### FINDING: Regulatory capital is 3.0% of the equity BSE carries, and at the margin physical capex is now 4.5 times incremental regulatory capital
S1 WHAT: The disclosed rupee-denominated regulatory minimum net worth for the group is 20,100 lakh, against consolidated equity of 6,79,550 — so `6,59,450 / 6,79,550 = 97.04%` of the equity is surplus to what the regulator requires `[AR FY26, Note 35, PDF p222/pr211]` and `[AR FY26, Consolidated Balance Sheet, PDF p163/pr152]`. In the same year, incremental cash capex per rupee of incremental revenue was ₹0.275 against incremental regulatory capital of ₹0.061.
S2 WHY: Overlay §5 replaces physical capital intensity with regulatory capital intensity because an exchange has almost no plant. That premise still holds on the stock — regulatory capital is 1.83× physical at FY2026 — but the flow has already crossed over, because the core settlement guarantee fund is sized by SEBI's Minimum Required Contribution off monthly stress-test values rather than by turnover, so it grew only 10.09% in a year revenue grew 63.46%, while FY2026 was the first year BSE spent seriously on colocation racks, buildings and plant, taking cash capex to 3.36× the prior year.
S3 EVIDENCE: `DERIVED`: floors `100 + 100 + 1 = ₹201 crore = 20,100 lakh`; surplus `6,79,550 − 20,100 = 6,59,450`, `= 97.04%` of equity and `6,59,450 / (6,79,550 + 1,24,683) = 82.0%` of capital employed; return on required regulatory capital `2,48,725 / (20,100 + 1,24,683) = 171.8%` against `2,48,725 / 8,04,233 = 30.9%` on capital carried. Flow: core SGF fund `1,24,683 − 1,13,260 = 11,423` and `11,423 / 1,87,661 = ₹0.061`; cash capex `51,516 / 1,87,661 = ₹0.275`; ratio `51,516 / 11,423 = 4.51×` `[AR FY26, Note 41, PDF p232/pr221]` and `[AR FY26, Consolidated Cash Flow, PDF p165/pr154]`. **The counter-proportion that reverses the reading:** on the *stock* the ratio of regulatory to physical capital is 1.83× and falling from 3.65× two years ago (`W3_balancesheet` §3), but on the *flow* it is already 0.22× — the two measures of the same question now point in opposite directions, and only the flow describes what the next rupee of revenue costs to serve.
S4 CONNECTS: Management's stated reason for carrying the surplus is regulatory display, not operating need: "a stronger balance sheet of an exchange is very essential to showcase to the world that the clearing corporation is strong enough" `[Q4FY26 Concall 13May2026, MD & CEO]`, and Note 35 sets the aim as "not only meet regulatory minimum capital, but also maintenance of financial cushion" `[AR FY26, Note 35, PDF p222/pr211]`. The Balance Sheet shows what the cushion actually is — own-account financial assets are 90.4% of total equity while the operating asset base is 10.0% (`W3_balancesheet` §1), so the surplus is a securities portfolio. The Business consequence is visible in the engine: investment income on that portfolio is ₹6.01 per ₹100 of revenue in FY2026 and ₹8.63 in the Jun-2026 quarter (§5.2).
DOMAINS: BalanceSheet, Notes, MgmtCommentary, Business
DISCONFIRM: Searched for and found, and part of it is decisive. (i) The ICCL floor is stated as "₹100 crore **or** capital as determined under regulation 14(3)(a) and 14(3)(b), **whichever is higher**" `[AR FY26, Note 35, PDF p222/pr211]` — the risk-based alternative is undisclosed, so the true floor may exceed ₹100 crore by an unknown amount and the 97.04% surplus is an upper bound, not a measurement. (ii) A clearing corporation's credit standing is itself an operating asset — the group holds AAA ratings from two agencies `[Q1FY27 IP 04Aug2026, PDF p18/slide 17]` — so "surplus to the regulatory minimum" is not the same as "surplus to commercial need". (iii) The USD-denominated IFSC floors are not converted by the company, adding up to roughly 6,000 lakh of unmeasured requirement. What survives: even the widest plausible reading of the floors leaves over 96% of equity unrequired.
S5 MEANS: The binding constraint on this business is neither capital nor plant — an incremental rupee of revenue costs about six paise of regulatory capital — so the equity base is a policy choice about optics and settlement confidence rather than a requirement of the earnings engine, and the overlay's own premise that capital here is regulatory rather than physical is now true of the balance sheet BSE has and false of the balance sheet it is building.
BASE-RATE: No realised loss found from under-capitalisation at this company or in the Indian MII set; searched the nine-year note history and the regulatory record and no capital shortfall, no SEBI capital direction and no clearing-fund shortfall appears in any year. Recorded as an absence, not as reassurance. The relevant realised event runs the other way: the core SGF contribution has ranged from 74 (FY2020) to 9,170 (FY2024) lakh, a 124× spread, so the requirement has moved violently even though it has never been missed `[records/trend_10y.csv]`.
S6 IMPLICATION: Capital-return capacity at this company is bounded by the parent's distributable retained earnings of 4,55,828 rather than by any regulatory need, since the regulatory need is 4.4% of that figure — which means the retention decision is discretionary and belongs in the capital-allocation assessment rather than being treated as a constraint; the monitorable is the core SGF contribution as a share of revenue each quarter, which is already running 34.67% higher annualised on flat operating revenue, and the thesis-breaker is a SEBI direction re-basing the Minimum Required Contribution or invoking ICCL's 14(3) risk-based floor, either of which would convert a 3% requirement into an unknown one.
SEVERITY: Medium

### FINDING: In the first quarter after the annual accounts, operating revenue grew 0.16% and 73.3% of the profit increase was investment income
S1 WHAT: Consolidated revenue from operations was 1,56,602 in Jun-2026 against 1,56,351 in Mar-2026, `1,56,602 − 1,56,351 = 251`, **+0.16% sequentially**, after nine quarters of double-digit sequential growth. PBT rose 10,021, of which investment income supplied 7,349 `[Q1FY27 Results 04Aug2026, consolidated quarterly filing, PDF p5]`.
S2 WHY: The activity that drives the top line stopped growing at the rate it had. Notional ADT fell 3.27% sequentially, premium ADT rose 2.40% and equity-derivatives realisation was exactly flat — `(11,550 / 11,279) ÷ (2,96,154 / 2,89,207) = 1.000006`. What replaced it was a non-operating item: investment income on BSE's own securities portfolio rose 119.13% sequentially, and a ₹40 crore receivables provision taken in the clearing subsidiary in Mar-2026 did not repeat `[Q1FY27 Concall 10Aug2026, CFO]`.
S3 EVIDENCE: The sequential PBT bridge ties to the rupee with zero residual: investment income +7,349, other expenses +3,687, depreciation +1,219, associates +860, levy +694, revenue from operations +251, other income +55, against clearing −303, core SGF −519, technology −919 and employee benefits −2,353; sum `= 10,021` against `1,16,366 − 1,06,345 = 10,021` `[Q1FY27 Results 04Aug2026, consolidated quarterly filing, PDF p5]`. **The counter-proportion:** investment income is 8.63% of the quarter's total income but 96.0% of its sequential increase (`7,349 / 7,655`), while revenue from operations is 91.75% of total income and 3.3% of the increase — a line that is 28 times the other in level supplied one-twenty-ninth as much of the movement. The two non-operating items together are `(7,349 + 3,687) / 10,021 = 110.1%` of the profit increase.
S4 CONNECTS: The Industry record puts a cause on the same month: BSE's index-options premium share fell to 32.4% in June 2026 specifically because NSE had an additional weekly expiry `[SECONDARY: Business Today/Jefferies, 2026-07-03]` (`W2_industry` F4), which is the expiry-calendar dependency showing up in the first month it was tested. Management commentary presents the quarter as "the 14th consecutive quarter of record revenues… Rs. 1,707 crores, surpassing the previous quarter's record of Rs. 1,630 crores" `[Q1FY27 Concall 10Aug2026, MD & CEO]` — a figure that is total income, not revenue from operations, and whose increase is 96.0% investment income. The Balance Sheet explains why investment income can do this: own-account financial assets are 90.4% of total equity (`W3_balancesheet` §1), so the portfolio is large enough to swamp a flat quarter of tolls.
DOMAINS: IncomeStatement, MgmtCommentary, Industry, BalanceSheet
DISCONFIRM: Searched for and found, and it is substantial. (i) Year-on-year the quarter is genuinely strong — revenue from operations +63.48%, PAT attributable +62.03% — and one flat sequential quarter after nine strong ones is not a trend. (ii) Q1 is seasonally distinct: the listing block fell 15.2% sequentially on an IPO pause management describes as temporary, with 13 mainboard IPOs raising ₹18,348 crore in July 2026 alone `[Q1FY27 Concall 10Aug2026, MD & CEO]`, so part of the flatness is a timing item outside the derivatives franchise. (iii) Equity-cash ADT set a record at ₹9,955 crore, +38.65% year-on-year, so the non-derivatives franchise was not flat. What survives: the derivatives line, which is 64.84% of consolidated revenue, grew 2.40% sequentially against 20.9% in the prior quarter, and the profit increase did not come from operations.
S5 MEANS: The FY2026 accounts measure this company at the top of a run, and the first observation after them shows the toll flat and the profit increase coming from a securities portfolio and a provision that did not repeat — so the FY2026 unit economics are a peak-cycle measurement, and the quality of the earnings step changed in the quarter immediately after the audit period without the reported growth rate showing it.
BASE-RATE: Realised at this company, and recently. BSE's own contract count fell 45.8% between Q2FY25 and Q4FY25 on a regulatory change, and its currency-derivatives ADT went from ₹9,733.67 crore to nil across FY2024–FY2026 (`W2_industry`). Activity at this company has stopped and reversed on regulatory action twice inside the observation window, so a flat quarter following a regulator-driven expiry reallocation is a demonstrated pattern rather than a hypothetical one. Against that, no quarter in the ten-quarter series has yet shown revenue from operations actually falling.
S6 IMPLICATION: The FY2026 ₹100 engine should be carried into any forward work with the Jun-2026 quarter attached as its first out-of-sample observation, because the two differ most in the layer that is least related to the franchise — investment income at ₹6.01 per ₹100 annually against ₹8.63 in the quarter; the monitorable is revenue from operations sequentially rather than year-on-year, next at the Q2FY27 filing due around early November 2026, and the thesis-breaker is a second consecutive sub-2% sequential quarter in revenue from operations, which would move the stall from a seasonal reading to a franchise reading.
SEVERITY: High

### FINDING: The down-leverage thesis-breaker fired in Jun-2026 and fails on inspection — and the ten-year "cost base has never contracted" claim is wrong in one like-for-like year
S1 WHAT: `W3_cost` F4 named its thesis-breaker as "a single quarter in which absolute expenses fall alongside turnover, which has not occurred in the ten years read". In Jun-2026 total expenses fell 3.64% (`53,669` against `55,694`) while notional turnover fell 3.27% (`237` against `245` ₹ Tn) `[Q1FY27 Results 04Aug2026, consolidated quarterly filing, PDF p5]` and `[Q1FY27 IP 04Aug2026, PDF p14/slide 13]`. Separately, `RF-044`'s claim that the cost base has never contracted in ten years is incorrect: total expenses fell 4.07% in FY2021.
S2 WHY: Neither exception is cost flexibility responding to activity. The Jun-2026 fall is a ₹40 crore receivables provision in the clearing subsidiary not repeating, which the CFO states directly `[Q1FY27 Concall 10Aug2026, CFO]`. The FY2021 fall is the first pandemic year, when technology spend fell 19.4% and administration 13.0% — and it happened while turnover was rising 56.84%, so it is not a downward-flexibility observation either.
S3 EVIDENCE: Jun-2026 stripped of the one-off: ex-levy expenses `35,722 − 4,000 = 31,722` in Mar-2026 against 34,391 in Jun-2026, `+8.41%` against notional `−3.27%`, elasticity `8.41 / (−3.27) = −2.577`; on total expenses, `53,669 / (55,694 − 4,000) = +3.82%` against −3.27%, elasticity −1.168. FY2021 verified at source with both columns on one audited page: employee `14,868` against `15,120`, technology `9,479` against `11,760`, administration `18,541` against `21,318`, total `53,070 − 55,320 = −2,250`, −4.07% `[AR FY2021, Consolidated P&L, PDF p146/pr141]`, against equity-cash ADT `4,197` against `2,676` crore, +56.84% `[AR FY2021, MD&A, PDF p101/pr96]`. **The counter-proportion that decides it:** in the two windows where absolute costs fell, turnover was *rising* in one (FY2021, +56.84%) and the fall was a provision reversal in the other; in the three windows where turnover actually fell, costs rose every time, by 14.68%, 30.64% and 17.56% (`W3_cost` §4.2). Costs have fallen twice and never once in response to falling activity.
S4 CONNECTS: The Industry record explains why the FY2021 exception does not generalise — it is a pandemic suspension of travel, events and premises spend, not a capacity decision, and the same categories rebounded, with other expenses reaching 24,732 by FY2026. Management commentary in the stall quarter attributes 54% of operating expenses to "regulatory fees and clearing and settlement expenses, all of which is directly correlated to increasing transaction volumes" `[Q1FY27 Concall 10Aug2026, MD & CEO]`, which is the company's own case that half the cost base is activity-linked; the Notes refute the symmetry, since the levy is assessed on notional and the clearing charge partly on an undisclosed intra-group transfer price. The Business consequence is that two of the four remaining layers cannot fall at all: the core SGF rises with stress-tested exposure and depreciation is committed, together ₹4.88 per ₹100.
DOMAINS: IncomeStatement, Industry, MgmtCommentary, Notes
DISCONFIRM: Searched for and found, and one item is material. (i) The FY2021 contraction is real, audited, like-for-like and 4.07% — the cost base **can** fall in absolute terms, which is the strongest available argument against reading the ratchet as a law rather than a pattern. (ii) The Jun-2026 figures are one quarter, and the Mar-2026 comparator is itself a residual derived as the audited year less the reviewed nine months `[Q1FY27 Results 04Aug2026, consolidated quarterly filing, PDF p6]`, so it carries whatever true-up the fourth quarter absorbed. (iii) The ₹40 crore is management's own approximation ("about Rs. 40 crores"), not a disclosed line. What survives: the direction of the correction to `RF-044` is to narrow it, not to reverse it, and the narrowed claim — costs have never fallen in a year turnover fell — holds in every window on record.
S5 MEANS: `RF-044`'s wording overstates a finding that is true in its substance, and the precise version is stronger because it is falsifiable: BSE's cost base is not incapable of contracting, it is unresponsive to activity — it fell once, for an exogenous reason, in a year turnover rose 57%, and it rose in every year turnover fell.
BASE-RATE: Realised at this company, twice, and sized. Cost-to-income went from 61.6% in FY2019 to 87.8% in FY2020 on a 14.44% turnover fall, and to 74.0% in FY2023 on a 23.42% fall (`W3_cost` F4). The ratchet has already destroyed two full cycles of margin at this company, which is what makes it a demonstrated risk rather than an inference from elasticity arithmetic.
S6 IMPLICATION: The bear-case cost assumption should remain an absolute rupee floor near the 1,18,773 ex-levy run-rate plus roughly 1,212 of committed incremental depreciation, but it should be stated as unresponsive rather than as incapable of falling, since a discretionary-spend shock of the FY2021 kind recovers roughly ₹3.10 per ₹100 at a 20% cut across the three discretionary layers; the monitorable is absolute quarterly total expenses ex the levy and ex any named provision, next at the Q2FY27 filing, and the thesis-breaker is a quarter in which that adjusted figure falls while turnover falls, which has still not occurred.
SEVERITY: High

### FINDING: The equity-cash repricing is not a repricing of BSE's ordinary book — 111% of it is a legacy exclusive-scrip rate whose residual is bounded at ₹104 crore
S1 WHAT: `W3_revenue` sized the FY2026 equity-cash realisation loss at 6,054 lakh and recorded that the split between exclusive and dual-listed scrips "cannot be established". The revenue side of the split is published: normal-rate charges rose 4.09% to ₹1,451 million while special-rate charges fell 35.71% to ₹1,044 million `[Q1FY27 IP 04Aug2026, PDF p13/slide 12]`.
S2 WHY: BSE charges two rates in the cash segment — a "normal rate" on securities also listed on NSE and a higher "special rate" on BSE-exclusive securities. SEBI's true-to-label uniform per-unit charging from 1-Oct-2024 removed the slab structure that supported the special rate, and the ESM and Additional Surveillance Measure regimes of 28-Jul-2025 and 10-Nov-2025 put price bands and once-a-week trading on exactly the BSE-exclusive scrips that carry it (`W3_revenue` F2). So the decline is the shrinkage of one book, not a rate cut across the segment.
S3 EVIDENCE: `ESTIMATE` from the presentation's rate split, which reconciles to the audited line within 0.6% (`2,495 mn = 24,950` lakh against 25,021 `[AR FY26, MD&A, PDF p75/pr64]`): special-rate change `1,044 − 1,624 = −580` against a total change of `2,495 − 3,018 = −523`, so the special-rate line is `−580 / −523 = 110.9%` of the decline and the normal-rate line offsets +57. Carried into Q1FY27: normal-rate realisation index `(446 / 324) ÷ (99,553 / 71,801) = 1.376543 / 1.386513 = 0.992810`, **−0.72%**, against a total equity-cash realisation index of 0.860738, **−13.93%**. **The counter-proportion:** the special-rate book is 41.8% of equity-cash revenue (`1,044 / 2,495`) and 111% of its decline, while the normal-rate book is 58.2% of revenue and −11% of the decline — the smaller half is doing all of the damage and the larger half is priced flat.
S4 CONNECTS: The Industry record establishes the rate authority sits with SEBI and dates the true-to-label reform, so the mechanism was available to management and was not named (`W2_industry` §2). The Notes exclude an accounting cause: transaction charges are recognised at a point in time at the specified rate, policy unchanged `[AR FY26, Note 2.3.10, PDF p176-177/pr165-166]`. Management commentary explained the same movement as "consistent with industry-wide reduction in average daily turnover value" `[AR FY26, MD&A, PDF p75/pr64]` while its own document reported BSE's cash turnover rising 2.36% seventeen pages earlier — and in Q1FY27 that turnover set a record at ₹9,955 crore ADT, +38.65% year-on-year `[Q1FY27 Concall 10Aug2026, MD & CEO]`, which removes the volume explanation entirely.
DOMAINS: IncomeStatement, Industry, MgmtCommentary, Notes
DISCONFIRM: Searched for and found. (i) The split is revenue by rate type, **not** turnover by scrip type, so it still does not separate rate from mix *within* the special-rate book — a fall could be fewer exclusive scrips trading rather than a lower rate on them, and that distinction remains unresolved. (ii) The figures are investor-presentation tier and rounded to ₹ million, giving a 0.6% reconciliation gap against the audited line. (iii) The normal-rate realisation of −0.72% is not exactly flat and is measured against *total* cash ADT rather than dual-listed turnover, which the company does not publish. What survives: whatever the internal composition, 111% of the aggregate decline sits in a line that is now 41.8% of the segment and shrinking, which bounds the exposure.
S5 MEANS: The 19.48% equity-cash realisation collapse is not evidence that BSE's cash-market pricing is being competed or regulated away generally — the ordinary book's realisation is flat to within a percentage point — it is the run-off of a legacy exclusive-listing premium, which is a wasting asset with a measurable balance rather than an open-ended repricing.
BASE-RATE: Realised and completed, at this company. The 6,054 lakh is a finished FY2026 loss of revenue against an unchanged-rate counterfactual on volume that grew, and the peer comparison sizes what is BSE-specific: NSE's cash-market transaction charges fell 7.93% in FY2026 `[NSE AR FY26, Note 27, PDF p159-160/pr314-317]` against BSE's 17.33% on the presentation basis, so roughly 2.2 times the peer decline is the exclusive-scrip premium unwinding.
S6 IMPLICATION: The residual exposure on this line is bounded at the remaining special-rate revenue of 10,440 lakh, `10,440 / 4,83,395 = 2.16%` of consolidated revenue, so the equity-cash line should be modelled as a flat normal-rate book plus a decaying special-rate book rather than as a single line with a declining realisation; the monitorable is the normal-versus-special split on the quarterly presentation's equity-cash slide, published every quarter, and the thesis-breaker is the normal-rate realisation index turning materially negative, which would mean the true-to-label logic has reached the book that is 58% of the segment.
SEVERITY: Medium

### Gap register — this wave's contributions

| # | Gap | What is missing | Peers disclose? | Document that would answer it |
|---|---|---|---|---|
| G-UE-01 | Contract counts are presentation-only | The lots and settled-contract series exist only in the quarterly investor deck — the lowest source tier — and appear in no annual report or audited note | Partially: NSE isolates Clearing Services revenue in its segment note | An Ind AS 115 disaggregation or an MD&A volume table carrying contracts alongside premium and notional |
| G-UE-02 | Tax layer has no chain | ₹17.04 of every ₹100 leaves as tax and no wave file traces it; the FY2025 prior-period credit of 2,987 against a FY2026 charge of 256 is unexplained | n/a | `W4_belowline`; AR FY26 Note 29 (PDF p214/pr203) tax reconciliation |
| G-UE-03 | ICCL's risk-based net-worth floor | Note 35 says "₹100 crore **or** capital under 14(3)(a)/(b), whichever is higher" and never states which bound applies | n/a | ICCL's standalone financial statements under s.136; a SECC 14(3) capital computation |
| G-UE-04 | IFSC net-worth floors unconverted | USD 3m + USD 3m + USD 0.5m stated in dollars with no rupee equivalent anywhere | n/a | FY2027 Note 35, or a Note 39 geographic capital disclosure |
| G-UE-05 | Q1FY27 core SGF balance | The quarterly filing carries no balance sheet, so regulatory capital per ₹1 of revenue cannot be recomputed on the stall quarter | n/a | FY2027 half-yearly balance sheet under SEBI LODR Reg. 33(3)(f) |
| G-UE-06 | Rack count series | Colocation is 49.09% of other operating income and ₹51 crore in Q1FY27, with a rack count for one date only | Not tested | FY2027 MD&A; a quarterly rack-occupancy disclosure |
| G-UE-07 | Exclusive-scrip turnover | The rate split of cash charges is published; the turnover behind each rate is not, so rate and mix inside the special-rate book stay unseparated | Not tested | A turnover-by-rate-category table in the MD&A |

### Handover, and the contradictions left standing

1. **For `W4_cash`.** This file ends at PAT of ₹51.66 per ₹100 of revenue from operations. The cash half of
   the ₹100 map starts there. Note that own-account separation is mandatory before any conversion statement
   (overlay §2) and that FY2026 cash capex of 51,516 is 3.36× the prior year, which is the single largest
   new claim on the ₹100.
2. **For `W4_belowline`.** The tax layer is ₹17.04 per ₹100 and is the largest single step in the engine
   after the levy. `G-UE-02` is yours. So is the finance-cost composition: 16 against a zero-debt
   declaration, and 3, 1,505, 2,748 and 2,215 in the four preceding years `[records/trend_10y.csv]`.
3. **For `W4_capalloc`.** Regulatory capital is 3.0% of equity (§3.3a) and the incremental requirement is
   six paise per incremental rupee of revenue. The retention decision is therefore discretionary, and the
   dividend payout ratio fell to 28% in FY2024-25 from 71% `[Q1FY27 IP 04Aug2026, PDF p31/slide 30]`.
4. **For `W5_earnings_quality`.** §5 is the material input: 110.1% of the sequential profit increase in the
   quarter after the audit period is a securities-portfolio gain plus a provision that did not repeat.
5. **For `W7_bear_case` and `W8_valuation`.** Do not carry a single operating-leverage number. Carry the
   three-base range of §4.2 and the cost floor of §4.5. The FY2026 unit economics are a lot-size artefact
   (§2.4) and the premium/notional ratio's quarterly range is ±37%, wider than the annual series shows
   (§5.3b), which makes the 17,709 lakh reversion cost in `W3_revenue` a lower bound; the Q2FY26 level
   already observed costs 38,535 lakh.
6. **Contradictions on the record, none resolved by deletion (doctrine §10).**
   (a) `RF-044` / `W3_cost` §4.2 "the cost base has never contracted in ten years" against the verified
   FY2021 contraction of 4.07% at `[AR FY2021, Consolidated P&L, PDF p146/pr141]` — §4.3.
   (b) `RF-012`'s closure reason ("the third base is undisclosed") against the presentation series of §0.2 —
   the conclusion survives, the stated reason does not.
   (c) `W3_cost` §2's Clearing chain L3 ("no published quantity to divide by") against §2.3 — the chain stays
   `BROKEN at L2/L3` and the break widens from 96.74pp to 103.50pp on the correct base.
   (d) `W3_cost` F4's thesis-breaker records that no quarter has shown expenses falling with turnover;
   Jun-2026 did, on a one-off — §5.4.
7. **Proposed register entries**, for whoever next writes `records/red_flags.md` (this wave writes one file
   only): RF-052 the three-base leverage range; RF-053 clearing cost per contract rose 3.74%; RF-054 the
   Jun-2026 stall and its 110.1% non-operating profit bridge; RF-055 the `RF-044` correction.

### Printed-page mapping used

Offsets from `records/printed_page_offsets.json`: FY2021 +5 · FY2024 +6 · FY2025 +11 · FY2026 +11.
Confirmed in the page text for every cite above: FY2026 consolidated P&L at PDF p164 carries folio 153;
Note 22 at PDF p211 carries folio 200; Note 27 at PDF p212 carries folio 201; Note 35 at PDF p222 carries
folio 211; Note 41 at PDF p232 carries folio 221; consolidated balance sheet at PDF p163 carries folio 152;
consolidated cash flow at PDF p165 carries folio 154; MD&A turnover at PDF p58 carries folio 47; MD&A
revenue table at PDF p75 carries folio 64; standalone Note 27 at PDF p287 carries folio 276; standalone
Note 35 at PDF p298 carries folio 287. FY2021 consolidated P&L at PDF p146 carries folio 141 and the
consolidated MD&A revenue discussion at PDF p101 carries folio 96.

Quarterly filings and presentations carry no printed folio and are cited by PDF page and, for the deck, by
the slide number printed on the page: `[Q1FY27 Results 04Aug2026, consolidated quarterly filing, PDF p5]`
is the consolidated statement of results for the quarter ended 30-Jun-2026; `[Q1FY27 IP 04Aug2026, PDF
p14/slide 13]` is the Equity Derivatives segment slide.
