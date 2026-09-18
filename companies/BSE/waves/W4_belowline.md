# W4 — Below the line: everything from depreciation down

**Scope.** The P&L lines no other agent owns: depreciation and amortisation · finance cost ·
**investment income** · other income · **share of net profit of associates (the CDSL stake)** · tax
(current, deferred, prior-period) · exceptional items · discontinued operations · OCI · EPS.
W3_revenue owns revenue; W3_cost owns operating costs. Doctrine: `ANALYSIS_DOCTRINE.md` §1a (S1–S6),
§2 (L1–L8), §3 (materiality triggers), §4b (arithmetic shown inline), §5 (evidence tags).

**Source of record.** The audited consolidated statements and notes in the FY2026 annual report, not the
MD&A and not the Board's Report. Where the standalone is used it is named. Printed-page mapping is
`PDF − 11` for FY2026 and FY2025, `PDF − 6` for FY2024, `PDF − 7` for FY2023 and FY2020, `PDF − 5` for
FY2021, `PDF − 9` for FY2022 and FY2019, `PDF − 7` for FY2018, `PDF − 2` for FY2017
`[AR FY26, printed_page_offsets.json]`.

**Read, not redone:** `W3_revenue.md` (Note 22, the treasury-income line, the standalone/consolidated
bridge), `W3_cost.md` (the operating cost engine, the technology capitalisation shift, an earlier
depreciation chain), `W3_notes.md` (policy-change log, restatements, R-25 the EPS restatement),
`W1_ledger.md` (the own-account / earmarked / clearing-float separation, an earlier investment-income
chain), `records/trend_10y.csv`, `records/capital_structure.md`, `records/restatements.md`.

**W3_group_rpt does not exist as at this writing** — `waves/` contains no such file. Group-structure and
related-party questions raised below are handed to it rather than answered here.

---

## 0. The one-paragraph answer

Netted, every line in this file **took ₹2,810 lakh off FY2026's profit increase**:
`+3,560 (investment income) − 42 (other income) − 1,717 (associates) − 4,598 (depreciation) − 13
(finance cost) = −2,810`, against a PBT increase of `3,29,914 − 1,74,827 = 1,55,087`
`[AR FY26, Consolidated P&L, PDF p164/pr153]`. **`−2,810 / 1,55,087 = −1.81%`: none of the year's
earnings growth came from below the line, and a little was lost there.** That is the correct first
sentence, and it is not the interesting one. The interesting facts are three: a corpus that grew 43.9%
earned a yield 156 basis points lower, so that **BSE's total treasury earnings actually fell**; ₹17,142
lakh of that treasury income is earned on money the group owes to its members and is nonetheless
credited to shareholders, while income on every other restricted pool is credited away from them; and
the associate line that fell 20.8% is carried at **12.8% of its own market value**.

---

## 1. Investment income — ₹29,030 lakh, and it is the line that matters

### 1.1 What it is made of (L2 ties, zero residual)

| Note 23 component, ₹ lakh | FY2026 | FY2025 | Δ | share of FY26 line |
|---|---|---|---|---|
| Interest on bank deposits (amortised cost) | 14,448 | 10,473 | +3,975 | 49.77% |
| Interest on debt instruments (amortised cost) | 5,706 | 8,024 | −2,318 | 19.66% |
| Dividend from mutual funds (FVTPL) | 1 | 1 | 0 | 0.00% |
| Net gain on disposal of equity instrument at FVTPL | — | 108 | −108 | — |
| **Net gain on financial assets measured at FVTPL** | **8,875** | **6,864** | **+2,011** | **30.57%** |
| **Total** | **29,030** | **25,470** | **+3,560** | **100%** |

`[AR FY26, Note 23, PDF p211/pr200]`. `DERIVED` tie: `14,448 + 5,706 + 1 + 0 + 8,875 = 29,030` and
`10,473 + 8,024 + 1 + 108 + 6,864 = 25,470`; growth `29,030 / 25,470 − 1 = +13.98%`.

**The first asymmetry, inside one disclosure.** Contractual yield — the two interest lines — is
`14,448 + 5,706 = 20,154`, i.e. `20,154 / 29,030 = 69.43%` of the line. Mark-to-market on debt mutual
funds and ETFs is `8,875 / 29,030 = 30.57%`. But of the year's **increase**, mark-to-market supplied
`2,011 / 3,560 = 56.49%` and net contractual interest only `(3,975 − 2,318) / 3,560 = 46.55%`. A line
that is 69% contractual grew 56% on revaluation. Those are the two shares that have to be read together.

### 1.2 Whose money — the four pools, and which one reaches shareholders

This is the overlay's §2 rule applied to the income side rather than the balance side. BSE's group holds
four distinct pools, and the annual report treats income on each of them differently.

| Pool | Balance at FY2026, ₹ lakh | Where its income goes | Reaches shareholders? |
|---|---|---|---|
| **Own corpus** (Notes 9, 11, 12, all lines labelled *Owned*) | **6,10,190** `DERIVED` | P&L line **"Investment income" 29,030** | **Yes** |
| **Clearing and settlement float** — Note 16 bucket (C) | **3,55,423** | P&L line **"Treasury income from clearing and settlement funds" 17,142**, inside *revenue from operations* | **Yes** |
| **Earmarked deposits** — Note 16 bucket (B) | 26,004 | Credited to the liability itself: *"Others (refer note 16.4)"* **8,896** (8,929 prior), and note 16.4 reads *"Income earned on earmarked amount"* | **No** |
| **Core Settlement Guarantee Fund** | 1,24,683 | Credited directly to the fund under policy 2.3.12 | **No** |

`[AR FY26, Note 9, PDF p191-192/pr180-181]`, `[AR FY26, Notes 11 and 12, PDF p200-202/pr189-191]`,
`[AR FY26, Note 16, PDF p206/pr195]`, `[AR FY26, Note 2.3.2, PDF p173/pr162]`,
`[AR FY26, Note 2.3.12, PDF p178/pr167]`, `[AR FY26, Note 22, PDF p211/pr200]`.

Policy 2.3.2 is explicit for bucket (B): *"Investment income earned and gain/(loss) in fair value on
financial instruments, if any is credited to respective earmarked liabilities and not routed through the
Consolidated Statement of Profit and Loss"* `[AR FY26, Note 2.3.2, PDF p173/pr162]`. Policy 2.3.12 is
explicit for the Core SGF: *"Income earned on such investments is attributed directly and credited to
the fund balance. Fines and penalties recovered from members are also directly attributed and credited
to the fund balance"* `[AR FY26, Note 2.3.12, PDF p178/pr167]`.

**Size the Core SGF exclusion.** The fund grew `1,24,683 − 1,13,260 = 11,423` on a P&L charge of only
7,696, so `11,423 − 7,696 = 3,727` of fund income and member penalties never touched the P&L
`[AR FY26, Consolidated Balance Sheet, PDF p163/pr152]`. On the average fund balance
`(1,24,683 + 1,13,260) / 2 = 1,18,972` that is `3,727 / 1,18,972 = 3.13%` — an **upper bound** on the
fund's investment yield, because penalties are inside the numerator.

**No such paragraph exists for bucket (C).** The clearing and settlement float is 87.5% of Note 16's
current other financial liabilities and it is member and clearing-bank money — *Deposit and margins from
members 2,06,976*, *Others 87,714*, *Settlement obligation payable 42,357*, *Deposit from clearing banks
18,376* `[AR FY26, Note 16, PDF p206/pr195]`. Income earned on it, **17,142 lakh, is recognised as group
revenue and accrues to shareholders**. The annual report nowhere states why the boundary sits where it
does. It is presumably contractual — buckets (B) and the Core SGF carry an obligation to return the
income, bucket (C) does not — but that is an inference, not a disclosure.

### 1.3 What yield is being earned — and on what base

**The own corpus has to be built from the notes; the company does not print it.** Only the lines
labelled *Owned* are included; every *Earmarked* line is stripped.

| ₹ lakh | FY2024 | FY2025 | FY2026 |
|---|---|---|---|
| Owned liquid funds (Notes 11 + 12: cash, deposits, accrued interest) | 1,41,528 | 1,67,486 | 3,08,596 |
| Owned non-current investments (Note 9: bonds/NCD + SDL + G-Sec + MF) | 49,429 | 56,641 | 69,761 |
| Owned current investments (Note 9: debt MF + ETF + current portion of LT − provision + accrued interest) | 1,21,259 | 1,42,850 | 2,31,833 |
| **Own investible corpus** | **3,12,216** | **3,66,977** | **6,10,190** |

`DERIVED`, arithmetic shown, `[AR FY26, Note 9, PDF p191-192/pr180-181]`,
`[AR FY25, Note 9, PDF p179-180/pr168-169]`, `[AR FY26, Notes 11 and 12, PDF p200-202/pr189-191]`;
owned liquid funds from `W1_ledger.md` §3.1(b):

- FY2026 non-current owned: `23,897 + 40,465 + 5,399 = 69,761`
- FY2026 current owned: `2,13,088 + 8,006 + 7,325 + 2,203 − 1,398 + 2,609 = 2,31,833`
- FY2026 total: `3,08,596 + 69,761 + 2,31,833 = 6,10,190`
- FY2025 non-current owned: `24,202 + 27,052 + 5,377 + 10 = 56,641`
- FY2025 current owned: `1,09,772 + 8,338 + 13,831 + 9,571 − 1,415 + 2,753 = 1,42,850`
- FY2025 total: `1,67,486 + 56,641 + 1,42,850 = 3,66,977`
- FY2024 non-current owned: `21,926 + 22,136 + 5,357 + 10 = 49,429`
- FY2024 current owned: `51,355 + 4,122 + 33,184 + 30,569 − 1,611 + 3,640 = 1,21,259`
- FY2024 total: `1,41,528 + 49,429 + 1,21,259 = 3,12,216`

**The yield, on the average balance:**

- FY2026: `(3,66,977 + 6,10,190) / 2 = 4,88,584`; `29,030 / 4,88,584 = 5.942%`
- FY2025: `(3,12,216 + 3,66,977) / 2 = 3,39,597`; `25,470 / 3,39,597 = 7.500%`
- **The own-account yield fell 156 basis points, `5.942 − 7.500 = −1.558pp`, i.e. `−1.558 / 7.500 = −20.8%`.**

**Balance versus rate, and it is the whole story:**

- Balance effect: `(4,88,584 − 3,39,597) × 7.500% = 1,48,987 × 0.075 = +11,174`
- Rate effect, as the residual: `3,560 − 11,174 = −7,614`
- Independent recompute of the rate effect: `4,88,584 × (5.942% − 7.500%) = 4,88,584 × (−0.01558) = −7,612`, a rounding residual of 2

> **The line rose 13.98% while the rate it earns fell 20.8%. A 43.9% larger corpus
> (`4,88,584 / 3,39,597 = 1.439`) bought a `+11,174` balance gain and paid back `−7,614` of it in
> price.** The MD&A's explanation — *"reflecting a combination of a larger investable corpus (driven by
> higher operating cash generation)"* `[AR FY26, MD&A, PDF p75/pr64]` — is directionally true and
> materially incomplete: it names the half that helped and not the half that hurt, and it does not
> mention the yield at all.

### 1.4 Why economically similar income sits in two places — and what it costs the reader

The two lines are the same economic activity: cash invested in bank deposits, debt mutual funds and
government securities, earning interest and revaluation.

- **Investment income 29,030** is governed by policy 2.3.4: *"Investment income consists of interest
  income on funds invested, dividend income and gains on the disposal of financial assets measured at
  FVTPL and amortised cost"* `[AR FY26, Note 2.3.4, PDF p174/pr163]`.
- **Treasury income from clearing and settlement funds 17,142** sits inside revenue from operations as
  Note 22 component C `[AR FY26, Note 22, PDF p211/pr200]` — and **the Ind AS 115 revenue policy 2.3.10
  does not name it**, a point W3_revenue established and registered.

So the 17,142 satisfies BSE's own stated definition of *investment income* and is nonetheless presented
as *revenue*, while no revenue policy covers it. **The classification is not driven by any disclosed
policy; it is driven by which legal entity earns it.** W3_revenue established that the entire 17,142
arises outside the parent — the standalone Note 22 has no such caption and runs A+B+C only
`[AR FY26, Standalone Note 22, PDF p285/pr274]`. The same rupee of interest is *revenue* when the
clearing corporation earns it on member collateral and *investment income* when BSE Limited earns it on
its own corpus.

**What the placement costs.** Moving the 17,142 to where its economics sit would change three headline
numbers, none of them trivially:

- Revenue from operations FY2026 `4,83,395 − 17,142 = 4,66,253`; FY2025 `2,95,734 − 21,778 = 2,73,956`;
  growth `4,66,253 / 2,73,956 − 1 = +70.19%` against the reported **+63.46%**. Stripping the line makes
  growth *better*, because the line fell.
- Total expenses to revenue `1,83,742 / 4,66,253 = 39.41%` against the reported `1,83,742 / 4,83,395 = 38.01%`.
- Any revenue multiple struck on the printed top line is, to the extent of `17,142 / 4,83,395 = 3.55%`,
  a multiple on interest earned on deposits the group owes back to its members.

### 1.5 The combined treasury result — the number nobody prints

Because the two halves are separated, the group's actual treasury outcome is not visible on any page.

| ₹ lakh | FY2025 | FY2026 | Δ |
|---|---|---|---|
| Investment income (own corpus) | 25,470 | 29,030 | +3,560 |
| Treasury income on clearing float (members' money) | 21,778 | 17,142 | −4,636 |
| **Total investment-type income in the P&L** | **47,248** | **46,172** | **−1,076** |
| Average own corpus | 3,39,597 | 4,88,584 | +1,48,987 |
| Average clearing float, Note 16 bucket (C) | 3,44,669 | 3,43,298 | −1,371 |
| **Total earning base** | **6,84,266** | **8,31,882** | **+1,47,616** |
| **Blended yield** | **6.905%** | **5.551%** | **−1.354pp** |

`DERIVED` throughout: `25,470 + 21,778 = 47,248`; `29,030 + 17,142 = 46,172`; `46,172 − 47,248 = −1,076`,
`−1,076 / 47,248 = −2.28%`; `3,39,597 + 3,44,669 = 6,84,266`; `4,88,584 + 3,43,298 = 8,31,882`;
`47,248 / 6,84,266 = 6.905%`; `46,172 / 8,31,882 = 5.551%`; `5.551 − 6.905 = −1.354pp`, i.e.
`−1.354 / 6.905 = −19.6%`. Float averages from `W3_revenue.md` §1.4 and `[AR FY26, Note 16, PDF p206/pr195]`.

> **BSE's total treasury earnings fell 2.28% in a year when its earning base grew 21.6%
> (`8,31,882 / 6,84,266 = 1.216`) and its own corpus grew 43.9%.** Both pools repriced by almost exactly
> the same proportion — own account `−20.8%`, clearing float `−21.0%` (W3_revenue §1.4) — which is what
> a single interest-rate cycle looks like when it is read across two P&L captions. Neither caption alone
> shows it.

**The counter-proportion on whose money.** Members' float is `3,43,298 / 8,31,882 = 41.27%` of the
earning base but produces only `17,142 / 46,172 = 37.13%` of the income, because it earns
`17,142 / 3,43,298 = 4.99%` against the own corpus's 5.942% — the restricted instrument set permitted
for clearing collateral yields less. Shareholders therefore take a **disproportionately large share of
the income from a disproportionately small share of their own money**: 58.73% of the base, 62.87% of the
income, and 100% of the claim on both.

### 1.6 The number management leads with is not the group's

The MD&A reports *"Total investment income grew 20% to ₹ 33,114 Lakh"* `[AR FY26, MD&A, PDF p75/pr64]`.
That is the **standalone** figure. The audited consolidated figure is 29,030 — **4,084 lakh, 14.07%,
lower** (`33,114 − 29,030 = 4,084`; `4,084 / 29,030 = 14.07%`).

The bridge closes exactly, and it is worth closing because it identifies the CDSL dividend:

| Step, ₹ lakh | Amount |
|---|---|
| Standalone investment income `[AR FY26, Standalone Note 23, PDF p286/pr275]` | 33,114 |
| less dividend income from subsidiaries (eliminated on consolidation) | (6,118) |
| less dividend income from others — **the CDSL dividend**, which under the equity method reduces the associate's carrying value instead of being income | (3,919) |
| add subsidiaries' bank-deposit interest `14,448 − 9,413` | +5,035 |
| add subsidiaries' debt-instrument interest `5,706 − 5,302` | +404 |
| add subsidiaries' FVTPL gain `8,875 − 8,361` | +514 |
| **Consolidated investment income** | **29,030** |

`DERIVED`: `33,114 − 6,118 − 3,919 + 5,035 + 404 + 514 = 29,030` — **exact, zero residual**
`[AR FY26, Note 23, PDF p211/pr200]` and `[AR FY26, Standalone Note 23, PDF p286/pr275]`.

**Decomposing the "20% growth" the MD&A claims.** Standalone investment income rose
`33,114 − 27,692 = 5,422`:

| Standalone component | Δ | share of the increase |
|---|---|---|
| Bank deposit interest `9,413 − 6,641` | +2,772 | 51.13% |
| Debt instrument interest `5,302 − 7,622` | −2,320 | −42.79% |
| **Dividend from subsidiaries** `6,118 − 3,900` | **+2,218** | **40.91%** |
| Dividend from others (CDSL) `3,919 − 3,449` | +470 | 8.67% |
| **FVTPL gain** `8,361 − 6,079` | **+2,282** | **42.09%** |
| **Total** | **+5,422** | **100%** |

`DERIVED`: `2,772 − 2,320 + 2,218 + 470 + 2,282 = 5,422` `[AR FY26, Standalone Note 23, PDF p286/pr275]`.

> **`(2,218 + 2,282) / 5,422 = 83.00%` of the growth management attributes to "a larger investable
> corpus" is an intra-group dividend that vanishes on consolidation plus a mark-to-market movement.**
> Net contractual interest — the thing a larger corpus actually produces — supplied
> `(2,772 − 2,320) / 5,422 = 8.34%`.

### 1.7 What is inside the corpus, and what the notes do not say

The own corpus at FY2026 is `2,21,094 / 6,10,190 = 36.23%` debt mutual funds and exchange-traded funds
carried at FVTPL, `2,88,807 / 6,10,190 = 47.33%` bank deposits (`1,37,461 + 1,51,346 = 2,88,807`), and
the balance amortised-cost bonds, state development loans and government securities
`[AR FY26, Note 9, PDF p191-192/pr180-181]`, `[AR FY26, Note 12, PDF p201-202/pr190-191]`.

Two things the notes do not give, and both bear on whether the 8,875 repeats:

1. **The ETF holding of 8,006 is not identified by asset class.** Note 9 lists it as *"Investment in
   exchange traded funds"* with no issuer, index or underlying `[AR FY26, Note 9, PDF p192/pr181]`. An
   equity ETF and a debt ETF have different distributions of the FVTPL line.
2. **The Board-approved investment policy is described but not disclosed.** The MD&A asserts it
   *"mandates diversification across high rated instruments reflecting a conservative,
   capital-preservation orientation"* `[AR FY26, MD&A, PDF p75/pr64]`; no rating floor, duration cap,
   single-issuer limit or asset-class band is published anywhere in the annual report.

---

## 2. The CDSL associate — why it fell while everything else rose

### 2.1 The line, decomposed to the last rupee

Share of net profit of associates `6,542` against `8,259`, **−1,717, −20.79%**
`[AR FY26, Consolidated P&L, PDF p164/pr153]`. Note 8 gives the roll-forward for every associate, so the
fall is fully attributable:

| Associate, ₹ lakh | FY2025 share | FY2026 share | Δ | share of the −1,717 |
|---|---|---|---|---|
| **Central Depository Services (India) Limited** | **7,900** | **6,842** | **−1,058** | **61.62%** |
| India International Bullion Holding IFSC | 240 | (432) | −672 | 39.14% |
| BSE Index Services (formerly Asia Index) | 145 | — | −145 | 8.44% |
| Hindustan Power Exchange | 241 | 104 | −137 | 7.98% |
| Countrywide Commodity Repository | (31) | (58) | −27 | 1.57% |
| EBIX Insurance Broking | 25 | 66 | +41 | −2.39% |
| EBIX Insuretech | (115) | (1) | +114 | −6.64% |
| BSE E-Agricultural Markets | (146) | 20 | +166 | −9.67% |
| **Total** | **8,259** | **6,541** | **−1,718** | **100%** |

`[AR FY26, Note 8, PDF p188-189/pr177-178]`. `DERIVED` tie-outs:
FY2025 `7,900 + 145 − 31 − 115 + 25 + 241 + 240 − 146 = 8,259` ✓ exact;
FY2026 `6,842 − 58 − 1 + 66 + 104 − 432 + 20 = 6,541` against the face figure of **6,542**.

> **A 1-lakh residual, and it is a disclosure inconsistency, not rounding.** Note 8 gives BSE
> E-Agricultural Markets a share of **20**; AOC-1 Part B gives the same entity **21**
> `[AR FY26, AOC-1 Part B, PDF p313/pr302]`. With 21 the components tie to 6,542 exactly. Two audited
> annexures of the same report carry different figures for the same associate.

### 2.2 Is it CDSL's own earnings, a stake change, or an equity-method adjustment? — **its own earnings**

All three candidates are testable and two are eliminated by the disclosure.

**Not a stake change.** BSE held **3,13,50,000 CDSL shares at both year-ends**, and the extent of holding
is **15%** in both years `[AR FY26, Note 8, PDF p188/pr177]`, `[AR FY26, AOC-1 Part B, PDF p313/pr302]`,
`[AR FY25, Note 8, PDF p177/pr166]`. The FY2025 movement from 1,56,75,000 to 3,13,50,000 shares was
CDSL's own 1:1 bonus, not a purchase — the carrying value moved `37,494 → 41,949` on share of profit and
dividend alone, with no "investment made during the year" line.

**Not an equity-method adjustment.** The FY2026 CDSL roll-forward has exactly four lines and no
adjustment line at all:

`41,949 (opening) + 6,842 (share of profit) + 68 (share of OCI) − 3,919 (dividend received) = 44,940`
— **exact** `[AR FY26, Note 8, PDF p189/pr178]`. Compare FY2024, where the same roll-forward *did* carry
an *"Adjustment on account of partial sale (10,935)"* `[AR FY24, Note 8, PDF p184/pr178]`, and FY2025,
where BSE Index Services carried *"Adjustments on account of change in ownership (3,037)"*
`[AR FY26, Note 8, PDF p188/pr177]`. When BSE makes such an adjustment it prints one. It printed none
for CDSL in FY2026.

**Therefore it is CDSL's own earnings.** At an unchanged 15.00% the implied CDSL-group PAT is
`6,842 / 0.15 = 45,613` lakh against `7,900 / 0.15 = 52,667` lakh, **−13.39%**. That derivation is
confirmed independently against CDSL's own audited accounts, which W2_peers read: CDSL FY2026
consolidated PAT attributable **₹456.13 crore = 45,613 lakh — an exact match**
`[AR CDSL FY26, Consolidated P&L, PDF p288, via W2_peers §3.1]`.

### 2.3 Why CDSL's own earnings fell — and why it matters to BSE specifically

CDSL's **revenue grew 5.79%** while its PAT fell 13.39% `[AR CDSL FY26, Note 19, PDF p321, via W2_peers
§3.2]`. The entire fall therefore sits below CDSL's revenue line: costs and mix, not demand collapse.
CDSL's PAT margin went `526.67 / 1,082.25 = 48.66%` to `456.13 / 1,144.92 = 39.84%`, **−8.82pp**
(`DERIVED`; FY2025 revenue `1,144.92 / 1.0579 = 1,082.25` ₹cr).

Inside that revenue, the mix moved decisively: **annual issuer charges +40.18%**, a fee SEBI resets,
against **transaction charges −9.93%** and **online data charges −27.88%** — the two activity-driven
lines `[AR CDSL FY26, Note 19, PDF p321, via W2_peers §3.2]`.

**And that is the connection to BSE's own report.** BSE's MD&A records *"Equity cash transaction charges
moderated by 18% to ₹ 25,021 Lakh, consistent with industry-wide reduction in average daily turnover
value"* `[AR FY26, MD&A, PDF p75/pr64]`. Depository transaction charges are levied per debit from a
demat account; they are a function of the same cash-market activity. **CDSL's transaction charges
(−9.93%) and BSE's equity-cash transaction charges (−18%) are two readings of one exogenous variable.**

> **The associate line is the only place in BSE's consolidated P&L where the FY2026 cash-market
> slowdown appears undiluted.** Everywhere else it is buried under a derivatives engine that grew
> 121.43% (W2_peers §3.2). The line fell 20.79% in a year attributable PAT rose 88.32% precisely
> because it is the one node whose earnings do not come from Sensex index options.

### 2.4 The cash, and the carrying value

Dividend received from CDSL: `3,919` against `3,449`, **+13.63%**
`[AR FY26, Note 8, PDF p189/pr178]`. On the 3,13,50,000 shares held at both year-ends that is
`3,919 lakh / 3,13,50,000 = ₹12.50` and `3,449 lakh / 3,13,50,000 = ₹11.00` per share (`DERIVED`).

**Cash conversion of the associate line: `3,919 / 6,842 = 57.28%`.** The remaining 42.72% accretes to
carrying value and reaches shareholders only on a sale. The standalone claims the whole 10,037 of
dividend received (subsidiaries 6,118 plus CDSL 3,919) as a section 80M deduction — see §3.4 — so the
cash half of this line is, at the parent, effectively untaxed.

**The carrying value against the market value is the fact.**

| ₹ lakh | FY2025 | FY2026 |
|---|---|---|
| Carrying value of the CDSL stake (equity method) | 41,949 | **44,940** |
| Aggregate **market value** of quoted associate investments | 3,82,486 | **3,50,932** |
| Unrecognised excess | 3,40,537 | **3,05,992** |

`[AR FY26, Note 8, PDF p188/pr177]`. CDSL is the only quoted associate, so the market-value line is the
stake. `DERIVED`: `3,50,932 − 44,940 = 3,05,992`; `3,50,932 / 44,940 = 7.81×`, i.e. the stake is carried
at `44,940 / 3,50,932 = 12.81%` of what the market pays for it. The unrecognised excess is
`3,05,992 / 6,67,301 = 45.86%` of attributable equity and `3,50,932 / 1,39,08,000 = 2.52%` of BSE's own
market capitalisation of ₹1,39,080 crore `[NSE Bhavcopy, 2026-09-04, via records/capital_structure.md]`.

And the market's own verdict on CDSL diverges from BSE's: implied CDSL market capitalisation
`3,50,932 / 0.15 = 23,39,547` lakh = ₹23,395 cr against `3,82,486 / 0.15 = 25,49,907` lakh = ₹25,499 cr,
**−8.25%** — a smaller fall than the 13.39% earnings decline, so CDSL's multiple *rose*
(`23,395 / 456.13 = 51.3×` against `25,499 / 526.67 = 48.4×`).

---

## 3. Tax — the effective rate on two bases, and why only one of them is honest

### 3.1 The charge

| Note 29(a), ₹ lakh | FY2026 | FY2025 |
|---|---|---|
| Current tax | 82,590 | 42,184 |
| Prior period tax adjustments | 256 | (2,987) |
| Deferred tax | (462) | 3,924 |
| **Total, continuing operations** | **82,384** | **43,121** |
| Tax in OCI (remeasurement of defined benefit plans) | 44 | (103) |
| Tax on discontinued operations | 251 | 181 |

`[AR FY26, Note 29, PDF p214/pr203]`, `[AR FY26, Consolidated P&L, PDF p164/pr153]`.

### 3.2 The effective rate — **the two bases differ by 0.505pp, and the difference decides the sign**

The company's own reconciliation, Note 29(b), starts from **"(A) Income before income tax 3,23,372"**
`[AR FY26, Note 29(b), PDF p215/pr204]`. That figure is P&L line 5 — *profit before tax and share of net
profits of investments accounted for using equity method* — **not** the P&L's own "Profit before tax" of
3,29,914 on line 7. The difference is the associate share of 6,542, which is **already net of CDSL's own
tax**.

| Basis | FY2026 | FY2025 |
|---|---|---|
| Statutory rate enacted in India (s.115BAA: 22% + surcharge + cess) | **25.168%** | **25.168%** |
| **ETR excluding the associate** — `82,384 / 3,23,372` | **25.477%** | `43,121 / 1,66,568` = **25.888%** |
| ETR on the face "Profit before tax" — `82,384 / 3,29,914` | **24.971%** | `43,121 / 1,74,827` = **24.665%** |

`DERIVED`, arithmetic shown; rate `[AR FY26, Note 29(b), PDF p215/pr204]`.

> **On the face of the P&L BSE's FY2026 tax rate looks 0.197pp *below* statutory
> (`25.168 − 24.971 = 0.197`). It is in fact 0.309pp *above* it (`25.477 − 25.168 = 0.309`). The whole
> apparent shortfall is an artefact of dividing a full tax charge by a denominator that contains
> post-tax income.** The gap between the two bases is `25.477 − 24.971 = 0.505pp`, worth
> `0.505% × 3,23,372 = 1,633` lakh of apparent tax. Any ETR taken off the face of BSE's P&L — as the
> FY2024 MD&A itself does, printing "Effective tax rate 22%" `[AR FY24, MD&A, PDF p76/pr70]` — is
> understated for exactly this reason, and the understatement grows with the associate.

### 3.3 The bridge from statutory to effective, in percentage points

FY2026 `[AR FY26, Note 29(b), PDF p215/pr204]`:

| Step | ₹ lakh | pp of the 3,23,372 base |
|---|---|---|
| (C) Expected tax at 25.168% | 81,386 | 25.168 |
| (D) Investment income taxed at different rates | 55 | +0.017 |
| (D) Tax on remeasurement of defined benefit plans | (44) | −0.014 |
| (D) Tax holiday benefit — the IFSC units | (83) | −0.026 |
| (D) Expenses disallowed | 165 | +0.051 |
| (E) Business losses on which no deferred tax asset is recognised | 649 | +0.201 |
| (G) Prior period tax adjustments | 256 | +0.079 |
| **(H) Tax expense in profit or loss** | **82,384** | **25.477** |

`DERIVED`: `25.168 + 0.017 − 0.014 − 0.026 + 0.051 + 0.201 + 0.079 = 25.476`, against
`82,384 / 3,23,372 = 25.477%` — residual 0.001pp from rounding. Component checks:
`93 / 3,23,372 = 0.029pp` for the whole of (D); `649 / 3,23,372 = 0.201pp`; `256 / 3,23,372 = 0.079pp`.

FY2025 on the same construction `[AR FY25, Note 29(b), PDF p197/pr186]`:
`25.168 + 3,876 / 1,66,568 (= 2.327) + 310 / 1,66,568 (= 0.186) − 2,987 / 1,66,568 (= 1.793) = 25.888%` ✓

> **FY2025's effective rate is the net of two large, opposite and entirely undisclosed items.** An
> "expenses disallowed" add-back of **3,041** (worth `3,041 / 0.25168 = 12,083` lakh of disallowed
> expenditure) and a prior-period credit of **(2,987)**. Neither is explained anywhere in the FY2025 or
> FY2026 annual report. Without the credit FY2025's ETR would have been
> `(43,121 + 2,987) / 1,66,568 = 27.68%`; without the disallowance, `(43,121 − 3,041) / 1,66,568 = 24.06%`.
> **A 3.62 percentage-point spread inside one year's tax note, resolved by two numbers the reader
> cannot see the composition of.**

**Base rate on prior-period tax adjustments.** FY2022 **9** · FY2023 **42** · FY2024 **51** ·
FY2025 **(2,987)** · FY2026 **256** `[AR FY23, Note 29, PDF p216/pr209]`,
`[AR FY24, Note 29, PDF p210/pr204]`, `[AR FY25, Note 29, PDF p197/pr186]`,
`[AR FY26, Note 29, PDF p214/pr203]`. The FY2025 item is **58.6× the largest of the three preceding
years** (`2,987 / 51 = 58.6`) and the only one to reverse the sign. FY2026's 256 is `256 / 51 = 5.0×` the
FY2024 figure but `256 / 82,384 = 0.31%` of the charge — small, and in the *opposite* direction to
FY2025, which is what a partial unwind of an over-claim looks like. The annual report does not say
whether the two are connected, and neither can be tested from the disclosure.

### 3.4 Are the sector-specific charges deductible? — **yes, both, and it is provable from the reconciliation**

The overlay's §3 flags two costs unique to an MII. Neither generates a permanent add-back, and the test
is arithmetic rather than assertion.

- **SEBI regulatory fee, 56,616** `[AR FY26, Note 27, PDF p212/pr201]`. If disallowed it would appear in
  the reconciliation at `56,616 × 25.168% = 14,249`. The entire "expenses disallowed" line is **165**,
  implying only `165 / 0.25168 = 656` lakh of disallowed expenditure across the whole group —
  `656 / 56,616 = 1.16%` of the SEBI fee alone. **Deductible.**
- **Contribution to core SGF, 7,696** `[AR FY26, Consolidated P&L, PDF p164/pr153]`. Disallowance would
  cost `7,696 × 25.168% = 1,937`, again far above the 165 actually present. **Deductible.**
- Cross-checked on the standalone, where both charges are borne in full by the parent (core SGF 7,696
  and 9,000 are identical to the consolidated figures): "Expenses disallowed **193**", i.e.
  `193 / 0.25168 = 767` lakh `[AR FY26, Standalone Note 29(b), PDF p289/pr278]`. Same conclusion on an
  independent statement.
- **FY2025 cannot be settled the same way.** Its 3,041 add-back implies 12,083 lakh of disallowed
  expenditure, which is larger than that year's core SGF contribution of 9,000, so a disallowance of the
  SGF charge in FY2025 cannot be excluded from the disclosure alone. `NOT-DISCLOSED` — the tax note
  gives no break-up of "expenses disallowed" in either year.

**Section 80M — the parent's dividend deduction, and it ties to the rupee.** The standalone
reconciliation carries *"Dividend income for which deduction claimed u/s 80M (2,526)"*
`[AR FY26, Standalone Note 29(b), PDF p289/pr278]`. `DERIVED`: `2,526 / 0.25168 = 10,036.55` lakh of
dividend against dividend actually received of `6,118 + 3,919 = 10,037` — **a residual under half a lakh,
so the deduction was claimed on 100% of it**. Section 80M requires the recipient to redistribute at least that
amount; dividend paid in the year was `31,585` `[AR FY26, Consolidated Cash Flow, PDF p165/pr154]`, i.e.
`31,585 / 10,037 = 3.15×` the dividend received, so the condition is met with wide margin. The
consolidated reconciliation has **no 80M line at all**, because both dividends are eliminated on
consolidation — which is itself the cleanest confirmation that the standalone investment-income figure
management quotes is not a group number.

### 3.5 Deferred tax — small, and one residual

Net deferred tax asset `2,371` against `1,939`, +432 `[AR FY26, Note 18, PDF p207-208/pr196-197]`. The
movement schedule is internally exact: `476 (recognised in P&L) − 44 (recognised in OCI) = 432` ✓.

But the schedule's P&L figure of **476** does not equal the P&L's deferred tax credit of **462**
`[AR FY26, Consolidated P&L, PDF p164/pr153]`. Residual **14** (`476 − 462 = 14`, i.e. 3.0% of the
credit). FY2025's schedule carried a separate column *"Recognised in profit and loss (discontinued
operation)"*; FY2026's does not, and the discontinued operation was sold during FY2026 — the most likely
home of the 14, but the note does not say so.

What moved: impairment of financial assets +933 (the expected-credit-loss build W3_cost sized at 4,057
of P&L charge), a new PPE deferred tax liability of 320 against a 59 asset reversal — the first year the
group carries a *net* deferred tax liability on fixed assets, and a direct consequence of the FY2026
capex — and expenses allowed on payment basis +11.

**Unrecognised deferred tax assets are growing.** Tax losses on which no asset is recognised
`21,960` against `21,449` `[AR FY26, Note 18 note 1, PDF p208/pr197]`, plus unabsorbed depreciation of
`3,164` against `3,028`, with an expiry ladder running to 2034-35 and a new 2,450 tranche added in
FY2026. The annual current-year cost is the (E) line: **649** against 310, `649 / 310 = 2.09×`. These are
the IFSC entities — the same entities whose translation gains fill OCI (§6.3) and whose losses are borne
`(973)` by non-controlling interests. The group pays 0.201pp of extra tax rate for them.

### 3.6 Cash tax against the charge

| ₹ lakh | FY2025 | FY2026 |
|---|---|---|
| Total tax charge, continuing | 43,121 | 82,384 |
| Direct taxes paid, net of refunds `[AR FY26, Consolidated Cash Flow, PDF p165/pr154]` | (32,797) | (65,541) |
| **Cash tax / book charge** | **76.06%** | **79.56%** |
| Cash tax rate on face PBT | `32,797 / 1,74,827` = **18.76%** | `65,541 / 3,29,914` = **19.87%** |

`DERIVED`: `32,797 / 43,121 = 76.06%`; `65,541 / 82,384 = 79.56%`.

The gap is a timing build and it reconciles to the balance sheet:

- Net current tax position FY2025: `12,056 (asset) − 8,447 (liability) = +3,609`
- Net current tax position FY2026: `6,279 − 20,109 = −13,830`
- Movement: `−13,830 − 3,609 = −17,439`
- Current-tax charges less cash paid: `82,590 + 256 + 251 − 65,541 = 17,556`
- **Residual `17,556 − 17,439 = 117`, i.e. 0.67%** `[AR FY26, Note 21, PDF p210/pr199]`

So the cash tax rate runs roughly 5pp below the book rate two years running
(`24.971 − 19.87 = 5.10pp` in FY2026; `24.665 − 18.76 = 5.91pp` in FY2025) and the deferral now sits as a
**current tax liability of 20,109, up 138.1% (`20,109 / 8,447 = 2.381`)**. This is a payable, not a
benefit: it is FY2026 tax that will be paid in FY2027.

**Disputed tax is growing faster than the group.** Contingent liabilities for income tax matters
`13,496` against `11,170`, **+20.8%** `[AR FY26, Note 37, PDF p227/pr216]`. On a group whose PBT rose
88.7%, that is a fall in relative terms (`13,496 / 3,29,914 = 4.09%` against `11,170 / 1,74,827 = 6.39%`)
but an absolute increase of 2,326 in a year with no disclosed new assessment.

---

## 4. Depreciation and amortisation — ₹15,896 lakh, +40.70%

W3_cost has already traced this line (`W3_cost.md`, CHAIN: Depreciation and amortisation expense | FY26)
and established the asset-class decomposition, the 16.21% effective rate, the 39/81 residual against the
notes, and the 1,212 of forward charge already committed. **That work is not repeated.** This section
adds four things it did not cover: the contradiction between the policy table and the note, the
arithmetic test of the useful-life change, the investment property, and the standalone-versus-
consolidated gap the MD&A quotes from.

### 4.1 Asset lives as published, and the contradiction inside the same report

The accounting-policy table `[AR FY26, Note 2.3.5(b), PDF p174/pr163]`:

| Category | Useful life as printed |
|---|---|
| **Buildings\*** | **60 years** |
| Leasehold buildings | 30 years |
| Plant and equipment | 15 years |
| Electrical installations | 10 years |
| Computer hardware and networking equipment | 3–6 years |
| Furniture, fixtures and office equipment | 5–10 years |
| Motor vehicles | 3–8 years |
| Investment property — buildings `[AR FY26, Note 2.3.6, PDF p175/pr164]` | 60 years |
| Computer software `[AR FY26, Note 2.3.7, PDF p175/pr164]` | 3–6 years |

Two pages later, Note 3 footnote 3 says something else: *"the Holding Company has revised the estimated
useful life of its building to **25 years**, effective April 01, 2024 impact of same was Rs. 13. The
change in useful life has been accounted for prospectively"* `[AR FY26, Note 3 fn 3, PDF p181/pr170]`.

> **The policy table prints 60 years for the asset class whose life the note says was cut to 25 —
> and it does so for the second consecutive year.** The FY2025 report carries the identical pair: "60
> years" in the policy table `[AR FY25, Note 2.2.5, PDF p166/pr155]` against "revised … to 25 years,
> effective April 01, 2024" in Note 3 `[AR FY25, Note 3 fn 3, PDF p172/pr161]`. The asterisk on
> "Buildings\*" points to the note, so the report is aware of the tension and resolves it by
> cross-reference rather than by correcting the table.

**Two methods run inside one group.** Property, plant and equipment is depreciated on the **written-down
value** method for the parent and most subsidiaries, but on the **straight-line** method for BSE Index
Services, India International Exchange (IFSC), India International Clearing Corporation (IFSC) and
India INX Global Access IFSC `[AR FY26, Note 2.3.5(b), PDF p174/pr163]`; the same split applies to
intangibles, with BSE Technologies added `[AR FY26, Note 2.3.7, PDF p175/pr164]`. The report does not
quantify the effect of running two methods, and the entities on SLM are the loss-making IFSC units whose
charge is borne partly by minorities.

### 4.2 Testing the useful-life change against the actual charge

The disclosure quantifies the impact at **13** — `13 / 15,896 = 0.08%` of the charge — but does not state
the life it was revised *from*, so the reader is asked to accept the 13 without an input. It can be
tested against the buildings row itself.

| Buildings, ₹ lakh | FY2025 | FY2026 |
|---|---|---|
| Opening net carrying value | 1,916 | 1,778 |
| Additions during the year | 15 | **18,022** |
| Depreciation for the year | **122** | **1,269** |

`[AR FY26, Note 3, PDF p181/pr170]`, `[AR FY25, Note 3, PDF p172/pr161]`.

`ESTIMATE`, assumptions stated: a mid-year convention on additions and a 5% residual value, which is the
Schedule II convention BSE does not disclose departing from.

- Implied FY2026 rate: `1,269 / (1,778 + 18,022 / 2) = 1,269 / 10,789 = 11.76%`
- Written-down-value rate for a **25-year** life at 5% residual: `1 − 0.05^(1/25) = 11.29%`
- Written-down-value rate for a **60-year** life at 5% residual: `1 − 0.05^(1/60) = 4.87%`
- Implied FY2025 rate: `122 / (1,916 + 15 / 2) = 122 / 1,923.5 = 6.34%`

> **FY2026's charge is consistent with the 25-year life the note describes (11.76% against 11.29%).
> FY2025's is not consistent with either life (6.34% against 11.29% and 4.87%) — yet FY2025 is the year
> the change is stated to have taken effect from.** On the 1,916 opening block, a full-year 25-year WDV
> charge would have been roughly `1,916 × 11.29% = 216` against the 122 actually taken, a gap of ~94 —
> seven times the "impact of same was Rs. 13" the note reports. The assumptions above could each move
> the result, which is why this is `ESTIMATE` and not `DERIVED`; what is not an estimate is that the
> disclosure gives no way to reproduce the 13.

### 4.3 The residual between the notes and the face, and where it goes

`13,720 (PPE) + 5 (investment property) + 2,210 (software) = 15,935` against the P&L's **15,896** —
residual **39**. FY2025: `8,996 + 4 + 2,379 = 11,379` against 11,298 — residual **81**
`[AR FY26, Notes 3, 4 and 6, PDF p181-185/pr170-174]`, `[AR FY26, Consolidated P&L, PDF p164/pr153]`.

The P&L line is *continuing operations*; Notes 3, 4 and 6 are the whole group including BSE Institute
Limited up to its sale on 2 May 2025. BIL's total expenses were 185 in FY2026 and 2,174 in FY2025
`[AR FY26, Note 49, PDF p239/pr228]`, and a depreciation charge of 39 and 81 inside those totals is
arithmetically comfortable. That is the explanation the numbers support; **the report does not state
it**, because Note 49 gives the discontinued operation only as Total Income / Total Expenses / PBT / Tax
with no expense analysis. W3_cost logged this as G-COST-06; it is unchanged and now has a named
mechanism.

### 4.4 Investment property — a rounding error on the balance sheet, ₹497 crore on the municipal roll

| Investment property, ₹ lakh | FY2025 | FY2026 |
|---|---|---|
| Gross carrying value | 143 | **42** |
| Net carrying value | 67 | **8** |
| Depreciation for the year | 4 | 5 |
| **Fair value (based on municipal value), Level 3** | **49,594** | **13,689** |
| Rental income derived | 661 | 885 |
| Profit after depreciation | 547 | 730 |

`[AR FY26, Note 4, PDF p182/pr171]`. During FY2026, gross 101 and accumulated depreciation 47 were
transferred out to property, plant and equipment, which is `101 / 143 = 70.6%` of the gross block; the
fair value fell in almost exactly that proportion (`13,689 / 49,594 = 27.6%` remaining against
`42 / 143 = 29.4%` of gross remaining), so the two disclosures are internally consistent.

> **The remaining investment property is carried at 8 and valued at 13,689 — a ratio of 1,711×.** The
> asset the group *reclassified into PPE* carried a municipal fair value of roughly
> `49,594 − 13,689 = 35,905` lakh, and it moved into a line where no fair value is disclosed at all,
> because Ind AS 16 requires none. The FY2026 depreciation charge on the entire investment-property
> portfolio is **5**. This is a below-the-line item only in the sense that its charge is; the asset
> question belongs to W3_balancesheet and is flagged there.

### 4.5 The number the MD&A quotes

MD&A: *"Depreciation increased 50% to ₹ 13,533 Lakh, attributable to the significant capital additions
of ₹ 45,753 Lakh during the year"* `[AR FY26, MD&A, PDF p76/pr65]`. Both figures are **standalone**.

| ₹ lakh | Standalone | Consolidated |
|---|---|---|
| Depreciation and amortisation FY2026 | 13,533 | **15,896** |
| Depreciation and amortisation FY2025 | 9,049 | **11,298** |
| Growth | `13,533 / 9,049 − 1 = +49.55%` | `15,896 / 11,298 − 1 = +40.70%` |
| Capital additions / cash capex | 45,753 | PPE additions 47,578 + software 2,470 = **50,048**; cash capex **51,516** |

`[AR FY26, MD&A, PDF p76/pr65]`, `[AR FY26, Consolidated P&L, PDF p164/pr153]`,
`[AR FY26, Note 3, PDF p181/pr170]`, `[AR FY26, Note 6, PDF p185/pr174]`,
`[AR FY26, Consolidated Cash Flow, PDF p165/pr154]`.

Subsidiaries carry `15,896 − 13,533 = 2,363` of the charge — 14.86% of it — and the MD&A's "+50%"
overstates the group's +40.70% by 8.85pp. Management's own condition, *"as these assets are fully
commissioned and contribute to revenue generation … the incremental depreciation charge is offset by
corresponding incremental revenue"* `[AR FY26, MD&A, PDF p76/pr65]`, is a forecast, not an L8 condition;
W3_cost has already recorded that and sized the 1,212 of committed forward charge.

---

## 5. Earnings per share — three published numbers, one denominator nobody expects

### 5.1 The denominator is **issued** capital, not paid-up

| Note 14, FY2026 | Amount ₹ lakh | Number of shares |
|---|---|---|
| Authorised | 30,000 | 1,50,00,00,000 |
| **Issued** | **8,240** | **41,19,79,077** |
| **Subscribed and paid-up** | **8,158** | **40,78,84,077** |

`[AR FY26, Note 14, PDF p203/pr192]`. Note 30 states the EPS denominator explicitly: *"Weighted average
number of equity shares **(issued share capital)** outstanding during the year"* = **41,19,79,077**, and
the same figure for FY2025 `[AR FY26, Note 30, PDF p215-216/pr204-205]`.

`DERIVED`, and every step ties:

- Pre-bonus issued capital `41,19,79,077 / 3 = 13,73,26,359` — exactly the FY2025 issued figure in Note 14 ✓
- Pre-bonus paid-up `13,53,76,359`; bonus allotted `27,07,52,718 = 13,53,76,359 × 2` ✓
- The gap between issued and paid-up at FY2026: `41,19,79,077 − 40,78,84,077 = 40,95,000` shares, i.e.
  `40,95,000 / 40,78,84,077 = 1.004%` of the paid-up count
- Why the denominator is **identical in both years despite 17,55,000 shares being allotted in FY2026**:
  Note 14's reconciliation labels those additions *"allotment of shares held in abeyance including bonus
  entitlements on such shares"* — they came **out of** issued capital, not into it
  `[AR FY26, Note 14, PDF p203/pr192]`
- The abeyance pool is the residue of the 2005 Demutualisation Scheme: of 4,77,75,000 shares issuable to
  card-based members, 4,73,20,000 have been allotted and **4,55,000 remain in abeyance** (6,50,000 at
  FY2025), with the Scheme providing that *"all corporate benefits as declared from time to time,
  including dividend and bonus are accrued to all the 4,77,75,000 equity shares"*
  `[AR FY26, Note 14(c), PDF p203/pr192]`

### 5.2 The published figures, and which base each uses

| Published EPS, ₹ | FY2026 | FY2025 as restated | Numerator, ₹ lakh | Denominator |
|---|---|---|---|---|
| **Consolidated, total operations** `[AR FY26, Note 30, PDF p216/pr205]` | **60.61** | 32.18 | 2,49,698 | 41,19,79,077 |
| Consolidated, continuing operations | 60.32 | 32.06 | 2,48,503 | 41,19,79,077 |
| Consolidated, discontinued operations | 0.29 | 0.12 | 1,195 | 41,19,79,077 |
| Standalone, after exceptional items `[AR FY26, Standalone Note 30, PDF p290/pr279]` | 56.66 | 27.00 | 2,33,416 | 41,19,79,077 |
| **Standalone, before exceptional items — the figure the Board's Report leads with** `[AR FY26, Board's Report, PDF p23/pr12]` | **56.27** | 27.00 | see below | 41,19,79,077 |

`DERIVED` checks: `2,49,698 lakh / 41,19,79,077 = ₹60.61` ✓ · `2,48,503 / 41,19,79,077 = ₹60.32` ✓ ·
`1,195 / 41,19,79,077 = ₹0.29` ✓ · `60.32 + 0.29 = 60.61` ✓ · `2,33,416 / 41,19,79,077 = ₹56.66` ✓ ·
FY2025 restatement `1,32,589 / 13,73,26,359 = ₹96.55` as first published, `96.55 / 3 = ₹32.18` as
restated under Ind AS 33 — matching R-25 in `W3_notes.md` `[AR FY26, Note 30, PDF p216/pr205]`.

### 5.3 Two things wrong with the number management leads with

**(a) It does not tie to the line printed immediately above it.** Standalone Note 30 prints *"Profit
before exceptional items (net of tax) – ₹ lakhs **2,32,075**"* and, on the next row, *"EPS – Basic and
Diluted (before exceptional items net of tax) ₹ **56.27**"* `[AR FY26, Standalone Note 30, PDF
p290/pr279]`.

- `2,32,075 lakh / 41,19,79,077 = ₹56.33`, **not ₹56.27**
- The printed 56.27 requires a numerator of `56.27 × 41,19,79,077 = 2,31,826` lakh
- `2,33,416 − 1,590 = 2,31,826` — **the EPS row deducts the *pre-tax* exceptional item of 1,590, while
  the profit row above it deducts the *net-of-tax* 1,341** (`2,33,416 − 2,32,075 = 1,341`, and
  `1,590 − 1,341 = 249` is exactly the tax on the gain shown in Note 49)
- Size: `₹56.33 − ₹56.27 = ₹0.06`, `0.06 / 56.33 = 0.11%`, worth `254` lakh of profit

Small in rupees; not small in what it is. **Two adjacent rows of one audited note use two different
numerators for the same concept, and the row that is wrong is the one reproduced in the Board's Report
and the MD&A.**

**(b) It is standalone, and before an item.** The group's audited earnings per share is **₹60.61**. The
headline figure is **₹56.27** — `60.61 − 56.27 = ₹4.34`, i.e. the group number is **7.71% higher**
(`60.61 / 56.27 = 1.0771`) than the one the reader meets first.

**(c) A correction for W8.** `records/capital_structure.md` derives consolidated FY2026 EPS as **₹61.22**
using the closing paid-up count of 40,78,84,077. The audited denominator is issued capital,
41,19,79,077, which is 1.004% larger; `2,49,698 / 40,78,84,077 = ₹61.22` against the audited
`₹60.61`, a 1.01% overstatement. **W8 should strike its P/E on ₹60.61**, which moves the trailing
multiple from `3,409.80 / 61.22 = 55.7×` to `3,409.80 / 60.61 = 56.3×`.

---

## 6. Exceptional items and discontinued operations — ten years, and one asset

### 6.1 FY2026: the sale of BSE Institute Limited, presented two different ways

BSE Institute Limited was approved for divestment on 8 May 2024, the share purchase agreement was signed
on **2 May 2025**, and Ind AS 105 disclosure follows `[AR FY26, Note 49, PDF p238-239/pr227-228]`.

| Consolidated, ₹ lakh | FY2026 | FY2025 |
|---|---|---|
| BIL total income to date of sale | 191 | 2,881 |
| BIL total expenses | 185 | 2,174 |
| Profit before tax from discontinued operation | 6 | 707 |
| **Gain on sale of subsidiary on loss of control** | **1,440** | — |
| Tax expense on discontinued operation | 251 | 181 |
| **Net profit from discontinued operation** | **1,195** | **526** |

`DERIVED` ties, all exact: `6 − 251 + 1,440 = 1,195` ✓ · gain `1,690 (cash consideration) − 250 (net
assets disposed) = 1,440` ✓ · net assets `300 + 1,380 − 3 − 1,427 = 250` ✓ · gain net of tax
`1,440 − 249 = 1,191`, and `1,191 + 4 = 1,195` ✓ `[AR FY26, Note 49, PDF p239/pr228]`.

**The same transaction is classified differently in the two statements.** Consolidated: *discontinued
operations*, gain **1,440**, below the tax line. Standalone: *"Exceptional item – sale of strategic
investment"*, **1,590**, above the tax line inside continuing operations
`[AR FY26, Standalone P&L, PDF p250/pr239]`. The 150 difference is the gap between the parent's carrying
cost of the investment and the group's share of BIL's net assets. Both presentations are defensible
under their respective standards; the consequence is that BSE's **consolidated** P&L reports zero
exceptional items in FY2026 while its **standalone** P&L reports 1,590, and the Board's Report prints
the standalone version `[AR FY26, Board's Report, PDF p23/pr12]`.

Materiality: `1,195 / 2,48,725 = 0.48%` of group PAT. Cash: the discontinued-operations cash flow shows
`+6,191` of investing inflow against a consideration of 1,690, the balance being BIL's own deposits
maturing on the way out `[AR FY26, Consolidated Cash Flow, PDF p166/pr155]`.

### 6.2 Ten years of "one-offs"

| Year | Consolidated exceptional, ₹ lakh | Standalone, ₹ lakh | What it was |
|---|---|---|---|
| FY2017 | (2,079) | (364) | Not described beyond the amount in the FY2017 MD&A `[AR FY17, Board's Report, PDF p17/pr15]` |
| FY2018 | (260) | **+31,556** | **CDSL partial divestment, 29 June 2017** — SEBI-directed cut from 50.05% to 24%; the consolidated gain sat in discontinued operations (48,722), not here `[AR FY18, MD&A, PDF p17/pr10]` |
| FY2019 | (1,352) | +457 | Liquidity Enhancement Scheme 1,298 plus voluntary retirement 54 `[AR FY19, Board's Report, PDF p25/pr16]`, `[AR FY20, MD&A, PDF p118/pr111]` |
| FY2020 | **+3,204** | **+9,158** | **CDSL: a further 4% divested by offer for sale**, 24% → 20% `[AR FY20, MD&A, PDF p118/pr111]` |
| FY2021 | (1,453) | (1,453) | **S&P Dow Jones arbitration award** — the Singapore tribunal held BSE's termination of the index licence invalid and awarded SPDJ its costs `[AR FY21, MD&A, PDF p102/pr97]` |
| FY2022 | — | — | none `[AR FY22, Board's Report, PDF p25/pr16]` |
| FY2023 | — | — | none `[AR FY23, MD&A, PDF p90/pr83]` |
| FY2024 | **+40,662** | **+50,417** | **CDSL: a further 5% sold**, 20% → 15%; approved 7 Feb 2023, held for sale at FY2023 at 10,935, completed in FY2024 `[AR FY24, Consolidated P&L, PDF p157/pr151]`, `[AR FY24, Note 8.1, PDF p185/pr179]` |
| FY2025 | — | — | none `[AR FY25, Consolidated P&L, PDF p156/pr145]` |
| FY2026 | — (1,440 in discontinued ops) | **+1,590** | Sale of BSE Institute Limited `[AR FY26, Note 49, PDF p239/pr228]` |

> **The base rate: a below-the-line non-operating item appears in 7 of the 10 years — FY2017, FY2018,
> FY2019, FY2020, FY2021, FY2024 and FY2026.** Only FY2022, FY2023 and FY2025 are clean. On the
> standalone the count is the same 7 of 10. A category that recurs in seven years out of ten is a
> feature of the P&L, not an exception to it.

**And the composition is one asset.** Gross positive standalone exceptional income across the ten years
is `31,556 + 457 + 9,158 + 50,417 + 1,590 = 93,178` lakh. The three CDSL tranches supply
`31,556 + 9,158 + 50,417 = 91,131`, i.e. **`91,131 / 93,178 = 97.80%`** (`DERIVED`).

> **97.8% of ten years of exceptional income is the same shareholding being sold down in three
> instalments: 50.05% → 24% → 20% → 15%.** The first was regulator-compelled (SEBI letter
> MRD/DSA/OW/9183/1/2017, per `W2_industry.md` finding F6); the second and third were not. The asset
> being progressively monetised is the same asset whose recurring contribution — the associate line —
> just fell 20.8%, and which is carried at 12.81% of its market value (§2.4). Those are not three
> separate facts.

---

## 7. The small lines — recorded, with the reason each was not chained (doctrine §3 brake)

### 7.1 Other income — 2,385 against 2,427, −1.73%

| Note 24, ₹ lakh | FY2026 | FY2025 |
|---|---|---|
| Rental income | 1,916 | 1,763 |
| Royalty income | 18 | — |
| Net gain/(loss) on disposal of PPE | (4) | 5 |
| Net foreign exchange gain/(loss) | 48 | (42) |
| **Interest on income tax refunds** | **214** | **508** |
| Miscellaneous income | 187 | 182 |
| Incentives from government authorities | 6 | 11 |
| **Total** | **2,385** | **2,427** |

`[AR FY26, Note 24, PDF p212/pr201]`. `DERIVED` tie: `1,916 + 18 − 4 + 48 + 214 + 187 + 6 = 2,385` ✓;
prior year `1,763 + 0 + 5 − 42 + 508 + 182 + 11 = 2,427` ✓.

**Not chained.** It is 0.46% of total income (`2,385 / 5,14,810`), moved 1.73%, carries no policy change,
no related party, no auditor comment and no management attention — it fails every §3 trigger. Two
observations recorded rather than traced: rental income of 1,916 exceeds the 885 the investment-property
note attributes to investment properties, so `1,916 − 885 = 1,031` is rent on assets sitting inside PPE
where no fair value is disclosed `[AR FY26, Note 4, PDF p182/pr171]`; and interest on income tax refunds
of 214 (508 prior) is a tax item presented as other income, `214 / 82,384 = 0.26%` of the tax charge.

### 7.2 Finance cost — 16 against 3

**Not chained.** It is `16 / 5,14,810 = 0.003%` of total income. It clears §3 trigger 2 on percentage
movement only because the base is three lakh rupees; the absolute movement is 13 lakh. BSE is a zero-debt
group — the MD&A's *"The Company remains a zero-debt business; all financial liabilities are operational
in nature"* `[AR FY26, MD&A, PDF p77/pr66]` is confirmed by the balance sheet, whose only borrowing-like
item is a lease obligation of **2** `[AR FY26, Note 16, PDF p206/pr195]`. Recorded and dismissed. Note
for context that finance cost was 2,748 in FY2023 and 1,505 in FY2024 `[AR FY24, Consolidated P&L, PDF
p157/pr151]` — it was a real line as recently as two years ago, and it went to nil.

### 7.3 Other comprehensive income — 3,744 against 501, and 36.9% of it is not shareholders'

| Consolidated OCI, ₹ lakh | FY2026 | FY2025 |
|---|---|---|
| i. Remeasurement gain/(loss) on defined benefit plans | 201 | (437) |
| ii. Income tax on the above | 44 | (103) |
| iii. **Foreign currency translation reserve** | **3,123** | 731 |
| iv. Share of OCI of associate (equity method) | 464 | 104 |
| **Total OCI (i − ii + iii + iv)** | **3,744** | **501** |

`[AR FY26, Consolidated P&L, PDF p164/pr153]`. `DERIVED`: `201 − 44 + 3,123 + 464 = 3,744` ✓.

Three things follow, none of them visible on the face:

1. **Translation is 83.4% of it** (`3,123 / 3,744`). It arises in the GIFT City IFSC entities — India
   International Exchange, India International Clearing Corporation, India INX Global Access — whose
   functional currency is the US dollar. The cash flow adjusts a slightly different figure, 2,994, a
   129 difference the statements do not reconcile `[AR FY26, Consolidated Cash Flow, PDF p165/pr154]`.
2. **The associate OCI line understates the associates' OCI.** Note 8 gives CDSL 68 and Hindustan Power
   Exchange 1 in addition to India International Bullion Holding's 464
   `[AR FY26, Note 8, PDF p188-189/pr177-178]`, so `68 + 464 + 1 = 533` against the 464 on the face. The
   face total nonetheless ties exactly, so the missing 69 must sit inside line (i) — `ESTIMATE`, because
   the note does not say so, and line (i) is not disaggregated.
3. **Minorities take 36.9% of the OCI while absorbing a loss on the PAT.** Net profit attributable to
   non-controlling interests is **(973)**; total comprehensive income attributable to them is **+408**.
   `DERIVED`: NCI share of OCI `408 − (−973) = 1,381`, i.e. `1,381 / 3,744 = 36.88%`; shareholders'
   share `3,744 − 1,381 = 2,363`, which ties exactly to
   `2,52,061 − 2,49,698 = 2,363` `[AR FY26, Consolidated P&L, PDF p164/pr153]`.

> **The minority-held IFSC subsidiaries flatter attributable PAT by 973 — attributable profit of
> 2,49,698 exceeds group profit of 2,48,725 because minorities absorb their losses — and then take
> 1,381 of the translation gain those same subsidiaries generate.** Non-controlling interest on the
> balance sheet nonetheless fell `15,197 → 12,249`, −2,948, despite +408 of comprehensive income and
> +1,215 of "issue of share by subsidiary" in financing. That movement is not explained by the P&L and
> is handed to **W3_group_rpt**, which does not yet exist.

### 7.4 Lines explicitly not traced, with the reason (§3 brake)

| Line | FY2026, ₹ lakh | Why not traced |
|---|---|---|
| Other income | 2,385 | 0.46% of total income; −1.73%; no §3 trigger fires |
| Finance cost | 16 | 0.003% of total income; absolute movement 13 lakh; group is debt-free |
| Other comprehensive income | 3,744 | 1.50% of PAT; analysed in §7.3 but not chained — it is a presentation aggregate, not a line with an economic driver, and its two real components (translation, remeasurement) belong to W3_group_rpt and W3_cost respectively |
| Exceptional items (consolidated) | nil in FY2026 | No consolidated exceptional item exists this year; the ten-year history is in §6.2 and the FY2026 equivalent is chained as discontinued operations |

---

## 8. Chain records (doctrine §2)

### CHAIN: Investment income | FY26
L1 REPORTED   TRACED | 29,030 against 25,470, +13.98% (29,030 − 25,470 = 3,560); unit "Rupees in Lakhs"; face line referencing Note 23; 5.64% of total income of 5,14,810 | [AR FY26, Consolidated P&L, PDF p164/pr153] and [AR FY26, Note 23, PDF p211/pr200]
L2 COMPONENTS TRACED | bank deposit interest 14,448 + debt instrument interest 5,706 + mutual fund dividend 1 + FVTPL net gain 8,875 = 29,030, zero residual; prior year 10,473 + 8,024 + 1 + 108 + 6,864 = 25,470. Contractual yield is 20,154 / 29,030 = 69.43% of the line but only (3,975 − 2,318) / 3,560 = 46.55% of the increase, while mark-to-market is 30.57% of the line and 2,011 / 3,560 = 56.49% of the increase | [AR FY26, Note 23, PDF p211/pr200]
L3 DRIVER     DERIVED | own corpus x yield, and the whole of the movement is decomposed. Own investible corpus, built by taking only the lines labelled Owned in Notes 9, 11 and 12: 6,10,190 against 3,66,977 against 3,12,216 (FY2026, FY2025, FY2024); average 4,88,584 against 3,39,597; yield 29,030 / 4,88,584 = 5.942% against 25,470 / 3,39,597 = 7.500%, so the rate fell 1.558pp or 20.8%. Balance effect (4,88,584 − 3,39,597) x 7.500% = +11,174; rate effect 3,560 − 11,174 = −7,614, cross-checked as 4,88,584 x (−0.01558) = −7,612. A 43.9% larger corpus paid back two-thirds of its gain in price | [AR FY26, Note 9, PDF p191-192/pr180-181], [AR FY26, Notes 11 and 12, PDF p200-202/pr189-191] and [AR FY25, Note 9, PDF p179-180/pr168-169]
L4 COUNTERPARTY TRACED | bank fixed deposits, growth-oriented debt mutual funds 2,13,088, exchange traded funds 8,006, state development loans 40,465, bonds and non-convertible debentures 23,897 and government securities 5,399, listed issuer by issuer in Note 9; no investment income from any related party appears in Note 36. The money is the group's own: every Earmarked line in Notes 9, 11 and 12 is excluded from the L3 base, and income on earmarked balances is credited to the liability under policy 2.3.2 and to the fund under policy 2.3.12 | [AR FY26, Note 9, PDF p191-192/pr180-181] and [AR FY26, Note 36, PDF p223-227/pr212-216]
L5 RECOGNITION TRACED | policy 2.3.4: effective-interest recognition on amortised-cost assets, fair-value movements on FVTPL assets through profit or loss, dividend when the right to receive is established. No policy change FY2025 to FY2026. The policy's own definition of investment income also describes the 17,142 of treasury income on clearing float, which is nonetheless presented inside revenue and is not covered by the Ind AS 115 policy 2.3.10 — the classification boundary is entity-driven, not policy-driven | [AR FY26, Note 2.3.4, PDF p174/pr163] and [AR FY26, Note 2.3.10, PDF p176-177/pr165-166]
L6 BALANCE-SHEET DERIVED | the corpus behind it is disclosed and separable. Owned securities 69,761 non-current + 2,31,833 current = 3,01,594 against 56,641 + 1,42,850 = 1,99,491; owned bank deposits and cash 3,08,596 against 1,67,486; total 6,10,190 against 3,66,977, +66.3%. Composition at FY2026: 36.23% debt mutual funds and ETFs at FVTPL (2,21,094 / 6,10,190), 47.33% bank deposits (1,37,461 + 1,51,346 = 2,88,807), balance amortised-cost debt. The ETF holding of 8,006 is not identified by asset class anywhere in Note 9 | [AR FY26, Note 9, PDF p191-192/pr180-181] and [AR FY26, Notes 11 and 12, PDF p200-202/pr189-191]
L7 CASH       DERIVED | removed from CFO in full and reappears in investing. Interest income (20,154), FVTPL gain (8,875) and dividend (1) are all deducted as non-cash adjustments; investing shows interest received 23,798 and dividend received 1. Cash exceeded accrued interest: 23,798 − 20,154 = 3,644. The FVTPL half converts only on redemption — of the 8,875, nothing is separately shown as realised, and gross mutual fund purchases of 91,484 against fixed deposit purchases of 3,29,857 indicate the corpus is being rebuilt rather than harvested | [AR FY26, Consolidated Cash Flow, PDF p165/pr154]
L8 SUSTAIN    DERIVED | three conditions, not a forecast. (i) 8,875 / 29,030 = 30.57% is mark-to-market on debt funds and repeats only while rates fall or stay put — the same rate move that produced it cut the contractual yield 156bp. (ii) The interest half repeats only while the corpus holds at 6,10,190, which is itself the FY2026 own-account cash build and is exposed to dividend, buyback or capex decisions. (iii) Read together with the 17,142 of treasury income inside revenue, total investment-type income FELL: 29,030 + 17,142 = 46,172 against 25,470 + 21,778 = 47,248, −2.28%, on an earning base that grew 21.6% | [AR FY26, Note 23, PDF p211/pr200] and [AR FY26, Note 22, PDF p211/pr200]
CHAIN-STATE: TRACED

> **Recorded contradiction, not resolved by overwriting (doctrine §10).** `W1_ledger.md` carries an
> earlier chain for this line whose L3 divides cash-flow interest income of 20,154 by *owned liquid
> funds* only, giving 8.47%. That denominator omits the Note 9 owned securities portfolio while the
> numerator includes 5,706 of interest earned on it, so numerator and denominator cover different
> assets. The chain above uses the full owned corpus for both. **Both positions stand on the record;
> the 5.94% is the one this file relies on, and the reason is stated rather than asserted.**

### CHAIN: Share of net profit of associates | FY26
L1 REPORTED   TRACED | 6,542 against 8,259, −20.79% (6,542 − 8,259 = −1,717); face line 6, struck after profit before tax and before the tax line, so it enters PBT of 3,29,914 net of the associates' own tax; 6,542 / 3,29,914 = 1.98% of PBT and 6,542 / 2,49,698 = 2.62% of attributable PAT | [AR FY26, Consolidated P&L, PDF p164/pr153]
L2 COMPONENTS TRACED | eight associates in Note 8: CDSL 6,842, EBIX Insurance Broking 66, BSE E-Agricultural Markets 20, Hindustan Power Exchange 104, EBIX Insuretech (1), Countrywide Commodity Repository (58), India International Bullion Holding (432), BSE Index Services nil. Sum 6,842 − 58 − 1 + 66 + 104 − 432 + 20 = 6,541 against the face 6,542; the 1-lakh residual is a disclosure inconsistency — Note 8 gives BSE E-Agricultural Markets 20 and AOC-1 Part B gives 21 for the same entity. Prior year 7,900 + 145 − 31 − 115 + 25 + 241 + 240 − 146 = 8,259, exact | [AR FY26, Note 8, PDF p188-189/pr177-178] and [AR FY26, AOC-1 Part B, PDF p313/pr302]
L3 DRIVER     DERIVED | stake x associate earnings, and the stake did not move. CDSL supplies 1,058 / 1,717 = 61.62% of the fall; holding unchanged at 3,13,50,000 shares and 15% at both year-ends; implied CDSL group PAT 6,842 / 0.15 = 45,613 lakh against 7,900 / 0.15 = 52,667, −13.39%, confirmed exactly against CDSL's own audited attributable PAT of 456.13 crore. CDSL's revenue GREW 5.79% while its PAT fell, so its margin went 526.67 / 1,082.25 = 48.66% to 456.13 / 1,144.92 = 39.84%, −8.82pp. Within CDSL's revenue the regulated annual issuer charge rose 40.18% while the activity lines fell — transaction charges −9.93%, online data charges −27.88% | [AR FY26, Note 8, PDF p189/pr178], [AR FY26, AOC-1 Part B, PDF p313/pr302] and [AR CDSL FY26, Note 19, PDF p321, via W2_peers 3.2]
L4 COUNTERPARTY TRACED | CDSL is a related party under Ind AS 24 and BSE is its promoter; BSE's payables to CDSL 38 and to CDSL Ventures 20 at FY2026, all stated to be at arm's length. The remaining seven associates are held indirectly — four through BSE Technologies, three through the IFSC entities — so the line aggregates two ownership layers with no separate disclosure of which layer earns what beyond AOC-1 | [AR FY26, Note 36, PDF p223-224/pr212-213] and [AR FY26, AOC-1 Part B, PDF p313/pr302]
L5 RECOGNITION TRACED | equity method under Ind AS 28; the FY2026 CDSL roll-forward carries no adjustment line of any kind — 41,949 + 6,842 + 68 − 3,919 = 44,940, exact. Compare FY2024, which carried "Adjustment on account of partial sale (10,935)", and FY2025, which carried "Adjustments on account of change in ownership (3,037)" for BSE Index Services. When an equity-method adjustment occurs the group prints one; none was printed for CDSL in FY2026 | [AR FY26, Note 8, PDF p189/pr178] and [AR FY24, Note 8, PDF p184/pr178]
L6 BALANCE-SHEET DERIVED | carrying value 44,940 against 41,949, +2,991 (6,842 + 68 − 3,919 = 2,991); total investments in associates 53,657 against 50,053 after a 100 impairment of the new BFSI Sector Skill Council holding. The market value of the same stake is 3,50,932 against 3,82,486, so it is carried at 44,940 / 3,50,932 = 12.81% of market and the unrecognised excess of 3,50,932 − 44,940 = 3,05,992 is 45.86% of attributable equity of 6,67,301 | [AR FY26, Note 8, PDF p188/pr177] and [AR FY26, Consolidated Balance Sheet, PDF p163/pr152]
L7 CASH       DERIVED | the line is non-cash and is deducted in full in the cash flow as "Share of net profit of associates (6,542)"; the cash leg is the dividend of 3,919, which does not appear as a separate cash-flow caption and instead reduces the associate's carrying value. Conversion 3,919 / 6,842 = 57.28% for CDSL and 3,919 / 6,542 = 59.90% for the whole line, since no other associate paid a dividend | [AR FY26, Consolidated Cash Flow, PDF p165/pr154] and [AR FY26, Note 8, PDF p189/pr178]
L8 SUSTAIN    DERIVED | the condition is CDSL's margin, not BSE's business. 6,842 / 6,542 = 104.6% of the line is CDSL, so everything else nets to −300; repetition requires CDSL's cost base to stop outrunning its revenue and requires depository transaction and online-data revenue to stop falling, which is the same cash-market activity that took BSE's own equity-cash transaction charges down 18% to 25,021. It is also the one node in the group that BSE may not own outright — SEBI capped it at 24% in 2017 and BSE has since taken it to 15% by choice | [AR FY26, MD&A, PDF p75/pr64] and [AR FY26, AOC-1 Part B, PDF p313/pr302]
CHAIN-STATE: TRACED

### CHAIN: Tax expense | FY26
L1 REPORTED   TRACED | 82,384 against 43,121, +91.05%; three face components current 82,590, prior period 256, deferred (462); plus 251 of tax on discontinued operations and 44 in OCI, so the full-year tax recognised anywhere is 82,384 + 251 + 44 = 82,679 | [AR FY26, Consolidated P&L, PDF p164/pr153] and [AR FY26, Note 29, PDF p214-215/pr203-204]
L2 COMPONENTS DERIVED | the reconciliation ties exactly on the company's own base: expected 81,386 + other-than-temporary differences 93 + unrecognised business losses 649 + prior period 256 = 82,384. Inside the 93: investment income taxed at different rates 55, tax on remeasurement of defined benefit plans (44), tax holiday benefit (83), expenses disallowed 165. Prior year: 41,922 + 3,876 + 310 − 2,987 = 43,121 | [AR FY26, Note 29(b), PDF p215/pr204]
L3 DRIVER     DERIVED | rate x base, and the base the company uses is not the base on the face. Note 29(b) starts from "Income before income tax 3,23,372", which is P&L line 5 and excludes the post-tax associate share of 6,542. ETR excluding the associate 82,384 / 3,23,372 = 25.477%, i.e. 0.309pp ABOVE the 25.168% statutory rate; ETR on the face PBT 82,384 / 3,29,914 = 24.971%, i.e. 0.197pp BELOW it. The two bases differ by 0.505pp, worth 0.505% x 3,23,372 = 1,633 lakh of apparent tax. Prior year 43,121 / 1,66,568 = 25.888% and 43,121 / 1,74,827 = 24.665% | [AR FY26, Note 29(b), PDF p215/pr204] and [AR FY26, Consolidated P&L, PDF p164/pr153]
L4 COUNTERPARTY TRACED | the Indian tax authorities under the section 115BAA concessional regime, rate 25.168%, plus the IFSC units' tax holiday worth (83). Sector-specific counterparties tested and found deductible: the SEBI regulatory fee of 56,616 would add 56,616 x 25.168% = 14,249 to the reconciliation if disallowed, and the core SGF contribution of 7,696 would add 1,937; the entire "expenses disallowed" line is 165, implying 165 / 0.25168 = 656 lakh of disallowance across the whole group. Confirmed independently on the standalone, where the same line is 193 | [AR FY26, Note 27, PDF p212/pr201] and [AR FY26, Standalone Note 29(b), PDF p289/pr278]
L5 RECOGNITION TRACED | policy 2.3.13: current tax at enacted rates, deferred tax on the balance-sheet approach, tax recognised in profit or loss except where the underlying item is in equity or OCI. No policy change. One presentational fact matters: the prior-period adjustment is a separate face line rather than being folded into current tax, which is what makes the FY2025 credit visible at all | [AR FY26, Note 2.3.13, PDF p178-179/pr167-168]
L6 BALANCE-SHEET DERIVED | it leaves a growing payable. Current tax liabilities 20,109 against 8,447, +138.1%; non-current tax assets 6,279 against 12,056; net position moved from 12,056 − 8,447 = +3,609 asset to 6,279 − 20,109 = −13,830 liability, a swing of 17,439. Deferred tax asset net 2,371 against 1,939, of which a new PPE deferred tax LIABILITY of 320 appears for the first time — the balance-sheet echo of the FY2026 capex. Disputed income tax in contingent liabilities 13,496 against 11,170, +20.8% | [AR FY26, Notes 18 and 21, PDF p207-210/pr196-199] and [AR FY26, Note 37, PDF p227/pr216]
L7 CASH       DERIVED | cash lags the charge and the reconciliation closes. Direct taxes paid net of refunds 65,541 against 32,797; cash-to-charge 65,541 / 82,384 = 79.56% against 76.06%; cash tax rate on face PBT 65,541 / 3,29,914 = 19.87% against 18.76%, i.e. roughly 5pp below the book rate two years running. Tie-out: 82,590 + 256 + 251 − 65,541 = 17,556 against the balance-sheet movement of 17,439, residual 117 or 0.67% | [AR FY26, Consolidated Cash Flow, PDF p165/pr154] and [AR FY26, Note 21, PDF p210/pr199]
L8 SUSTAIN    BROKEN | the rate repeats; the FY2025 comparative does not, and it cannot be tested. FY2025's 25.888% is the net of an undisclosed "expenses disallowed" add-back of 3,041 (implying 3,041 / 0.25168 = 12,083 lakh of disallowed expenditure) and an undisclosed prior-period credit of (2,987), which nearly cancel: without the credit FY2025 would be (43,121 + 2,987) / 1,66,568 = 27.68%, without the disallowance (43,121 − 3,041) / 1,66,568 = 24.06% — a 3.62pp spread inside one audited note. The prior-period base rate makes the FY2025 item exceptional: 9, 42, 51, (2,987), 256 across FY2022 to FY2026, so it is 2,987 / 51 = 58.6x the largest of the three preceding years and the only sign reversal | [AR FY25, Note 29(b), PDF p197/pr186] and [AR FY26, Note 29(b), PDF p215/pr204]
CHAIN-STATE: BROKEN at L8

> The break is doctrine §2c pattern 2 in the tax note rather than the revenue note: the reconciliation
> is arithmetically complete and economically opaque. Two items of roughly ₹30 crore each, moving in
> opposite directions in the same year, with no composition disclosed for either, are the reason the
> FY2025 comparative cannot support a statement about the durability of the rate. **Sized for the
> register: `3,041 + 2,987 = 6,028` lakh of tax-note movement with no narrative, against an FY2025 total
> charge of 43,121 — 13.98% of it.**

### CHAIN: Depreciation and amortisation | FY26
L1 REPORTED   TRACED | 15,896 against 11,298, +40.70% (15,896 − 11,298 = 4,598); face line referencing Notes 3, 4 and 6; 3.09% of total income against 3.49% | [AR FY26, Consolidated P&L, PDF p164/pr153]
L2 COMPONENTS DERIVED | property, plant and equipment 13,720 + investment property 5 + software amortisation 2,210 = 15,935 against the face 15,896, residual 39; prior year 8,996 + 4 + 2,379 = 11,379 against 11,298, residual 81. The residual is the discontinued operation's depreciation: the notes cover the whole group including BSE Institute Limited to its sale on 2 May 2025, the face line is continuing operations only, and BIL's total expenses were 185 and 2,174 respectively | [AR FY26, Notes 3, 4 and 6, PDF p181-185/pr170-174] and [AR FY26, Note 49, PDF p239/pr228]
L3 DRIVER     DERIVED | asset base, not rate. Effective rate on average gross block 13,720 / ((63,738 + 1,05,539) / 2) = 16.21% against 8,996 / ((50,796 + 63,738) / 2) = 15.71%, a 0.50pp move against a 40.70% charge increase; gross block 1,05,539 against 63,738, +65.58%, on additions of 47,578. Within the 4,724 rise in PPE depreciation, computers 1,880, buildings 1,147 and plant 1,053 — decomposed in full by W3_cost and not repeated | [AR FY26, Note 3, PDF p181/pr170]
L4 COUNTERPARTY TRACED | not a counterparty line, but the asset base is split by entity and by method: written-down value for the parent and most subsidiaries, straight-line for BSE Index Services and the three IFSC entities, and straight-line for intangibles at those four plus BSE Technologies. The group does not quantify the effect of running two methods; the entities on straight-line are the loss-making IFSC units whose result is shared with non-controlling interests | [AR FY26, Note 2.3.5(b), PDF p174/pr163] and [AR FY26, Note 2.3.7, PDF p175/pr164]
L5 RECOGNITION BROKEN | the policy table and the note disagree, for the second year running. The accounting-policy table prints "Buildings* 60 years" while Note 3 footnote 3 states the Holding Company "has revised the estimated useful life of its building to 25 years, effective April 01, 2024 impact of same was Rs. 13". The FY2025 report carries the identical pair. The stated impact of 13 is 13 / 15,896 = 0.08% of the charge and cannot be reproduced from any published input, because the note does not state the life it was revised from | [AR FY26, Note 2.3.5(b), PDF p174/pr163] and [AR FY26, Note 3 fn 3, PDF p181/pr170]
L6 BALANCE-SHEET ESTIMATE | the charge is consistent with the revised life in FY2026 and not in FY2025. Assuming a mid-year convention on additions and a 5% residual value, the implied FY2026 buildings rate is 1,269 / (1,778 + 18,022 / 2) = 11.76% against a 25-year written-down-value rate of 1 − 0.05^(1/25) = 11.29% and a 60-year rate of 4.87%; the implied FY2025 rate is 122 / (1,916 + 15 / 2) = 6.34%, which matches neither, in the very year the change is said to take effect from. Both assumptions are the group's undisclosed choices and either could move the result | [AR FY26, Note 3, PDF p181/pr170] and [AR FY25, Note 3, PDF p172/pr161]
L7 CASH       TRACED | wholly non-cash, added back in full in CFO at 15,896; the cash leg is combined capex of 51,516 against 15,323, given as a single line covering PPE, intangibles, capital work in progress, intangibles under development and capital advances, with no split by asset class | [AR FY26, Consolidated Cash Flow, PDF p165/pr154]
L8 SUSTAIN    DERIVED | it rises before it plateaus, and the run-rate is understated twice over. W3_cost sized the committed forward charge at 1,05,539 x 16.21% − 15,896 = 1,212 from assets already bought, and showed that the capitalised share of technology outlay moved 18,530 / 38,843 = 47.71% from 8,279 / 24,708 = 33.51%, a 14.20pp shift, so part of what would have been technology expense is now future depreciation. Capital commitments not provided for are 10,029 and capital work in progress plus intangibles under development is 7,675 consolidated (3,255 + 4,420) | [AR FY26, Note 38, PDF p227/pr216] and [AR FY26, Consolidated Balance Sheet, PDF p163/pr152]
CHAIN-STATE: BROKEN at L5

> The break is narrow and it is real: an accounting-policy table and a note in the same report state two
> different useful lives for the same asset class, and the note's quantification of the change is not
> reproducible from any published input. It does not make the 15,896 wrong — L3 shows the charge is an
> asset-base effect and the FY2026 buildings rate is consistent with 25 years — but it means **the
> policy a reader would apply and the policy the company applied are not the same policy.**

### CHAIN: Discontinued operations | FY26
L1 REPORTED   TRACED | net profit from discontinued operations 1,195 against 526, +127.2%; presented on the face as three lines — profit before tax 6, gain on sale of subsidiary on loss of control 1,440, tax 251 — referencing Note 49; 1,195 / 2,48,725 = 0.48% of group PAT | [AR FY26, Consolidated P&L, PDF p164/pr153] and [AR FY26, Note 49, PDF p238-239/pr227-228]
L2 COMPONENTS TRACED | BSE Institute Limited to the date of sale: total income 191, total expenses 185, profit before tax 6, tax 2, profit after tax 4; plus gain on sale net of tax 1,191; total 1,195. Prior year total income 2,881, expenses 2,174, PBT 707, tax 181, PAT 526. All ties exact: 6 − 251 + 1,440 = 1,195 and 1,191 + 4 = 1,195 | [AR FY26, Note 49, PDF p239/pr228]
L3 DRIVER     DERIVED | a single disposal, not an operating result. The gain is consideration less book value: cash consideration 1,690 − net assets disposed 250 = 1,440; net assets 300 non-current + 1,380 current − 3 non-current liabilities − 1,427 current liabilities = 250. The operating half is negligible — BIL contributed 191 of income against 2,881 a year earlier because the sale completed on 2 May 2025, roughly one month into the year | [AR FY26, Note 49, PDF p239/pr228]
L4 COUNTERPARTY NOT-DISCLOSED | the purchaser of BSE Institute Limited is not named anywhere in the annual report; Note 49 states only that a share purchase agreement was signed on 2 May 2025, and BIL does not appear in the related-party note as a counterparty to the sale -> the share purchase agreement itself, or the stock-exchange announcement of the transaction under Regulation 30, which would identify the buyer and whether it is a related party
L5 RECOGNITION TRACED | Ind AS 105, with prior-year P&L and cash-flow figures bifurcated into continuing and discontinued as the standard requires. The same disposal is classified differently in the two statements: discontinued operations at 1,440 below the tax line in the consolidated, and an exceptional item at 1,590 above the tax line in the standalone, the 150 difference being the parent's carrying cost against the group's share of net assets | [AR FY26, Note 49, PDF p239/pr228] and [AR FY26, Standalone P&L, PDF p250/pr239]
L6 BALANCE-SHEET TRACED | assets classified as held for sale fell from 6,798 to 127, and liabilities held for sale from 1,559 to nil, as BIL left the balance sheet; the 127 remaining is a different transaction — the in-principle approval of 11 November 2025 to divest EBIX Insurance Broking, still awaiting regulatory approval, which will be the FY2027 equivalent of this line | [AR FY26, Consolidated Balance Sheet, PDF p163/pr152] and [AR FY26, Note 8.1, PDF p190/pr179]
L7 CASH       TRACED | reported separately as required: discontinued operations produced 4 of operating cash, 6,191 of investing cash and nil financing, total 6,195 against 1,288. The investing inflow of 6,191 exceeds the 1,690 consideration because BIL's own deposits matured on the way out; the excess of 6,191 − 1,690 = 4,501 is not separately explained | [AR FY26, Consolidated Cash Flow, PDF p166/pr155]
L8 SUSTAIN    DERIVED | not recurring as this asset, recurring as a category. BIL is gone and cannot repeat; but a below-the-line non-operating item has appeared in 7 of the last 10 years, and the next one is already on the balance sheet at 127. Ten-year gross positive standalone exceptional income is 31,556 + 457 + 9,158 + 50,417 + 1,590 = 93,178, of which three CDSL sell-downs supply 31,556 + 9,158 + 50,417 = 91,131 = 97.80% | [AR FY26, Note 8.1, PDF p190/pr179] and [AR FY24, Consolidated P&L, PDF p157/pr151]
CHAIN-STATE: TRACED

---

## 9. Findings

### FINDING: A 44% larger corpus earned a 156bp lower yield, so BSE's total treasury income fell in a year its earning base grew 22%
S1 WHAT: Investment income rose 13.98% to 29,030 [AR FY26, Note 23, PDF p211/pr200]. Over the same year the own investible corpus rose from 3,66,977 to 6,10,190 and the yield on the average balance fell from 7.500% to 5.942%. Read together with the 17,142 of treasury income that sits inside revenue, total investment-type income in the P&L FELL from 47,248 to 46,172.
S2 WHY: One interest-rate cycle acting on two pools that are reported in two places. The mechanism is price, not volume: both pools repriced by almost the same proportion — own account −20.8% (7.500% to 5.942%) and clearing float −21.0% (6.32% to 4.99%, W3_revenue §1.4) — while the own corpus grew 66.3% on the FY2026 operating cash build. Growth in the balance masked the fall in the rate on one line and could not mask it on the other, because the clearing float did not grow.
S3 EVIDENCE: Balance effect `(4,88,584 − 3,39,597) × 7.500% = +11,174`; rate effect `3,560 − 11,174 = −7,614`, cross-checked `4,88,584 × (5.942% − 7.500%) = −7,612` [AR FY26, Note 9, PDF p191-192/pr180-181; AR FY26, Notes 11 and 12, PDF p200-202/pr189-191; AR FY25, Note 9, PDF p179-180/pr168-169]. Combined: `29,030 + 17,142 = 46,172` against `25,470 + 21,778 = 47,248`, `−1,076 / 47,248 = −2.28%`, on a combined average earning base of `4,88,584 + 3,43,298 = 8,31,882` against `3,39,597 + 3,44,669 = 6,84,266`, `+21.6%`; blended yield `46,172 / 8,31,882 = 5.551%` against `47,248 / 6,84,266 = 6.905%`, −1.354pp [AR FY26, Note 22, PDF p211/pr200; AR FY26, Note 16, PDF p206/pr195]. **The counter-proportion inside the line:** contractual interest is `20,154 / 29,030 = 69.43%` of the reported income but only `(3,975 − 2,318) / 3,560 = 46.55%` of the increase, while mark-to-market is 30.57% of the line and `2,011 / 3,560 = 56.49%` of the increase. A line that is two-thirds contractual grew on revaluation.
S4 CONNECTS: The corpus is the balance-sheet consequence of the year's operating cash — own-account CFO of 2,86,117 (W1_ledger §3.3) — so the P&L line is downstream of the derivatives boom, not independent of it. The rate half is exogenous and is the same variable moving the clearing-float line inside revenue, which W3_revenue chained separately. Management describes the growth as "reflecting a combination of a larger investable corpus (driven by higher operating cash generation)" and names no rate [AR FY26, MD&A, PDF p75/pr64]. The peer set gives the industry frame: every MII in W2_peers is a price-taker on its regulated revenue, and treasury is the one line where the price-taking is set by the RBI cycle rather than by SEBI.
DOMAINS: IncomeStatement, BalanceSheet, CashFlow, Notes, MgmtCommentary, Industry
DISCONFIRM: Sought and partly found. (i) The corpus effect is real and large — +11,174 — and it is the company's own cash, so the line is not manufactured. (ii) 8,875 of FVTPL gain on debt mutual funds is the economically correct way to report the return on those instruments; excluding it would understate the yield, not improve it. (iii) A falling-rate environment produces mark-to-market gains and lower reinvestment yields simultaneously, so the two halves of the finding are the same event and should not be double-counted as two problems. What survives disconfirmation: the total fell, on a base that grew, and no single page of the annual report shows that.
S5 MEANS: Treasury is the second-largest earnings block after transaction charges and it is now running on a shrinking rate against a growing balance, which means the corpus must keep growing simply to hold the income flat — at the FY2026 yield, replacing the 7,614 of lost rate requires `7,614 / 0.05942 = 1,28,139` lakh of additional corpus. The composition compounds it: 30.57% of the line is revaluation that reverses if rates rise, and the same rate rise would lift the contractual half, so the line's two halves are negatively correlated and its reported volatility understates the swing in either.
BASE-RATE: Investment income has fallen in absolute terms in four of the ten years in `trend_10y.csv` — FY2018 (23,802 to 16,870), FY2020 (20,218 to 15,866), FY2021 (to 12,908) and FY2022 (to 9,755, a ten-year low) — and the FY2019-to-FY2022 decline was 20,218 to 9,755, −51.8%, without any impairment or credit event. So a realised, sustained fall in this exact line has already happened at this company within the window, on a corpus that did not shrink by anything like that proportion. No credit loss on the portfolio is recorded in any of the ten years; the only impairment in Note 9 is a 1,398 provision for diminution, essentially flat against 1,415.
S6 IMPLICATION: Any forward earnings frame should split this line before extending it — the 30.57% revaluation half is not a yield and should not be capitalised at an operating multiple, and the contractual half should be modelled as corpus × a rate that has fallen 156bp in one year. The durability question is whether the corpus survives capital-allocation decisions, since it is the same cash that funds dividend, capex and any future distribution. Monitorable: the blended yield recomputed each year as `(Note 23 total + Note 22 line C) ÷ (average own corpus + average Note 16 bucket C)`, next checked at FY2027. Thesis-breaker: a year in which the corpus grows and total investment-type income still falls, which would mean the rate decline has outrun the group's ability to out-save it.
SEVERITY: Medium

### FINDING: 37% of the treasury income credited to BSE's shareholders is earned on money the group owes its members, and it is the only restricted pool whose income they get
S1 WHAT: "Treasury income from clearing and settlement funds" of 17,142 lakh is earned on Note 16 bucket (C), 3,55,423 lakh of member deposits, member margins, settlement obligations and clearing-bank deposits, and it is recognised as group revenue [AR FY26, Note 22, PDF p211/pr200; AR FY26, Note 16, PDF p206/pr195]. Income on every other restricted pool the group holds is credited away from shareholders — to the liability for earmarked deposits, and to the fund itself for the Core SGF.
S2 WHY: Two accounting policies exist and neither covers bucket (C). Policy 2.3.2 says income on earmarked funds "is credited to respective earmarked liabilities and not routed through the Consolidated Statement of Profit and Loss" [AR FY26, Note 2.3.2, PDF p173/pr162]; policy 2.3.12 says Core SGF investment income "is attributed directly and credited to the fund balance" [AR FY26, Note 2.3.12, PDF p178/pr167]. Bucket (C) has no policy paragraph in either direction — the Ind AS 115 revenue policy 2.3.10 names every revenue stream except this one (W3_revenue) — so the boundary is presumably contractual, but the report never states it. What is stated is that the classification follows the entity: 100% of the 17,142 arises outside the parent [AR FY26, Standalone Note 22, PDF p285/pr274].
S3 EVIDENCE: Sized: 17,142 is `17,142 / 46,172 = 37.13%` of all investment-type income reaching the P&L and `17,142 / 2,48,725 = 6.89%` of group PAT. **The counter-proportion:** members' float is `3,43,298 / 8,31,882 = 41.27%` of the group's total average earning base but produces only 37.13% of the income, because it yields `17,142 / 3,43,298 = 4.99%` against the own corpus's 5.942% — shareholders take a larger share of the income than of the base, on money that is not theirs. Against that, the pools whose income they do NOT get: the Core SGF grew `1,24,683 − 1,13,260 = 11,423` on a P&L charge of only 7,696, so `11,423 − 7,696 = 3,727` of fund income and penalties bypassed the P&L entirely — `3,727 / 1,18,972 = 3.13%` on the average fund balance [AR FY26, Consolidated Balance Sheet, PDF p163/pr152]; and the earmarked-income liability "Others (refer note 16.4)" was 8,896 against 8,929, i.e. income accrued to depositors, not to shareholders [AR FY26, Note 16, PDF p206/pr195].
S4 CONNECTS: The overlay's §2 rule — most of an MII's balance sheet is not the company's money — is normally applied to the balance sheet; this is its income-statement consequence, and it is the reason the overlay's §5 table says CFO/PAT and ROE must be struck on own-account bases. It connects to governance because the counterparties are the clearing members BSE's group regulates through ICCL, and to industry because SEBI sets the permitted instruments for clearing collateral: a direction narrowing them moves the whole 17,142 with no change in BSE's business. W2_peers records that neither NSE nor MCX presents an equivalent line inside revenue in the same way, and that CDSL and IEX have no such float at all.
DOMAINS: IncomeStatement, BalanceSheet, Notes, Governance, Industry
DISCONFIRM: Sought and found in three forms. (i) It is standard practice for a clearing corporation to retain the return on member collateral where it does not contract to pay interest — this is not an appropriation, it is the ordinary economics of a clearing house, and members receive the service rather than the yield. (ii) The disclosure is honest at the balance-sheet level: Notes 11, 12 and 16 label every rupee owned or earmarked, and Note 12.1 states plainly which balances are restricted, so nothing is concealed. (iii) The line is separately captioned in Note 22 rather than buried in transaction charges. What survives: the income is presented as *revenue from operations* rather than as investment income even though it meets the group's own definition of investment income, no policy explains the boundary, and the placement raises reported revenue by 3.55%.
S5 MEANS: A reader taking "revenue from operations" as a proxy for customer income is overstating it by 17,142, and a reader taking group PAT as a claim on shareholders' capital is including 6.89% earned on liabilities. More importantly, the pool is the one part of the group's earning base that BSE neither owns nor controls the size of — bucket (C) fell 2,24,870 to 2,06,976 on member margins alone — so it is an earnings stream with no retention mechanism: BSE cannot add to it, cannot price it, and would lose it entirely if members moved their clearing elsewhere under interoperability.
BASE-RATE: A realised loss in this exact channel has already occurred at this company: the treasury line fell 21.29% in FY2026 (21,778 to 17,142) purely on rate, with the float rising 7.32% — 6,231 lakh of income lost to price on other people's money, computed in W3_revenue §1.4. In the wider system, the base rate is regulatory rather than credit: RBI's 5 January 2024 ETCD directions extinguished an entire BSE segment (W1.7 §6), which is the demonstrated form the risk takes — a rule change, not a default.
S6 IMPLICATION: The float-derived income should be carried as a separate block from customer revenue in any earnings-quality view, because it is a rate on a restricted balance rather than a contract with a customer, and because the two treasury lines must be read together or the direction of the total is invisible. Monitorable: Note 16 bucket (C) against the Note 22 line C each year, with the implied yield recomputed, next at FY2027. Thesis-breaker: a SEBI or RBI direction requiring clearing collateral to be segregated, remunerated to members, or invested in a narrower instrument set — any of which moves 17,142 without touching a single trade.
SEVERITY: High

### FINDING: The associate line is the only place in BSE's P&L where the FY2026 cash-market slowdown shows up undiluted
S1 WHAT: Share of net profit of associates fell 20.79% to 6,542 in a year attributable PAT rose 88.32% [AR FY26, Consolidated P&L, PDF p164/pr153]. CDSL supplies 61.62% of the fall. The stake did not change — 3,13,50,000 shares and 15% at both year-ends — and no equity-method adjustment was made; CDSL's own PAT fell 13.39%.
S2 WHY: CDSL's costs outran its revenue, and the revenue that fell is the activity-linked half. CDSL's revenue GREW 5.79% while its PAT fell 13.39%, so its PAT margin went 48.66% to 39.84%, −8.82pp. Inside that revenue, the regulated annual issuer charge rose 40.18% while depository transaction charges fell 9.93% and online data charges fell 27.88% [AR CDSL FY26, Note 19, PDF p321, via W2_peers §3.2]. Depository transaction charges are levied per debit from a demat account, so they move with cash-market activity — the same variable that took BSE's own equity-cash transaction charges down 18% to 25,021 [AR FY26, MD&A, PDF p75/pr64].
S3 EVIDENCE: The stake is proved unchanged three ways: share count 3,13,50,000 in both years and holding 15% in both years [AR FY26, Note 8, PDF p188/pr177; AR FY26, AOC-1 Part B, PDF p313/pr302]; and the FY2026 roll-forward has no adjustment line — `41,949 + 6,842 + 68 − 3,919 = 44,940`, exact — where FY2024's carried "Adjustment on account of partial sale (10,935)" and FY2025's carried "Adjustments on account of change in ownership (3,037)" for a different associate [AR FY26, Note 8, PDF p189/pr178; AR FY24, Note 8, PDF p184/pr178]. Implied CDSL PAT `6,842 / 0.15 = 45,613` against `7,900 / 0.15 = 52,667`, confirmed exactly against CDSL's own audited attributable PAT of ₹456.13 cr. **The counter-proportion:** CDSL is 61.62% of the fall but the fall is only `1,717 / 1,17,109 = 1.47%` of the year's increase in attributable PAT — the line is immaterial to FY2026 earnings and material to what FY2026 earnings are made of, since `6,542 / 2,49,698 = 2.62%` of PAT comes from the one node whose earnings are cash-market-driven while `3,13,437 / 4,83,395 = 64.84%` of revenue comes from index options.
S4 CONNECTS: The business domain gives the structural reason the line exists at all — SEBI ordered BSE out of the depository in 2017 and permitted it to own the clearing corporation outright, so the same value chain produces a 100%-consolidated ICCL contributing ₹16,979 lakh of PAT and a 15% equity-accounted CDSL contributing 6,842 (W2_industry F6). The industry domain supplies the driver: W2_peers records that not one of the five MIIs moved a price it controls in FY2026, and CDSL's growth came from a SEBI fee reset while its activity lines fell. The income statement supplies the contrast: BSE's own cash segment fell 18% and its derivatives segment rose 121.43%, and only the derivatives half is visible in the headline.
DOMAINS: IncomeStatement, Notes, Business, Industry
DISCONFIRM: Sought and found. (i) The line is small — 1.98% of PBT — so the fall changes no conclusion about FY2026 profitability. (ii) 38.4% of the fall is not CDSL at all: India International Bullion Holding swung 240 to (432), a −672 move that is a GIFT City start-up loss, and BSE Index Services' 145 disappeared because it became a subsidiary, so its earnings moved INTO consolidated revenue rather than being lost. (iii) CDSL's own revenue grew, so this is not a demand collapse in the depository. What survives: the direction of the one cash-market-exposed node in the group is opposite to the direction of the group, and it is the only line that shows it.
S5 MEANS: BSE's FY2026 result is more concentrated than the consolidated P&L makes it look, because the only earnings stream inside it that is exposed to a different exogenous variable — cash-market activity rather than index-option premium turnover — is also the only stream that fell. The associate line is therefore a read-out on the half of the market BSE's headline no longer depends on, and it read down 13.4% at the source. That is a diversification argument working in reverse: the group has one non-correlated asset and it is 2.62% of PAT.
BASE-RATE: The equity-method line has fallen before, and by more in proportion: 6,418 to 4,923 in FY2023, −23.3%, per `trend_10y.csv`, in the year cash-market turnover last contracted. CDSL's own contribution has otherwise risen every year from 5,203 in FY2023 to 6,287 in FY2024 to 7,900 in FY2025, so FY2026 is the first fall in CDSL's contribution on an unchanged stake in the window. No realised loss — no impairment of the CDSL carrying value has ever been recorded, and none could plausibly be, since the stake is carried at 12.81% of market.
S6 IMPLICATION: The line should be read as an indicator rather than as earnings — 2.62% of PAT does not move a valuation, but a 13.4% fall in the earnings of the group's only cash-market-exposed asset is direct evidence about the durability of the 18% decline in BSE's own equity-cash segment, which is the segment a derivatives-normalisation case would depend on. Monitorable: CDSL's implied PAT recomputed each year as the Note 8 share divided by the AOC-1 holding percentage, cross-checked against CDSL's own accounts, next at FY2027. Thesis-breaker: CDSL's transaction and online-data revenue returning to growth while BSE's equity-cash transaction charges continue to fall, which would mean the cause is BSE-specific rather than market-wide.
SEVERITY: Medium

### FINDING: 97.8% of ten years of exceptional income is one shareholding being divested in three instalments, and what remains of it is carried at 12.8% of its market value
S1 WHAT: A below-the-line non-operating item appears in 7 of the last 10 years. Gross positive standalone exceptional income across the window is 93,178 lakh, of which 91,131 — 97.80% — is three tranches of the CDSL stake: FY2018 (50.05% to 24%), FY2020 (24% to 20%) and FY2024 (20% to 15%). The residual 15% is carried at 44,940 against a disclosed market value of 3,50,932.
S2 WHY: The first divestment was compelled — SEBI letter MRD/DSA/OW/9183/1/2017 required the holding down to 24% by 30 June 2017 (W2_industry F6). The second and third were not: the FY2020 4% was an offer for sale [AR FY20, MD&A, PDF p118/pr111] and the FY2024 5% was Board-approved on 7 February 2023, classified as held for sale at FY2023 at 10,935 and completed in FY2024 [AR FY24, Note 8.1, PDF p185/pr179]. The carrying-value gap exists because the equity method carries the stake at cost plus accumulated share of profit less dividends, which is unrelated to what the market pays for a depository monopoly duopolist.
S3 EVIDENCE: `31,556 + 457 + 9,158 + 50,417 + 1,590 = 93,178` gross positive standalone exceptional income; `31,556 + 9,158 + 50,417 = 91,131`; `91,131 / 93,178 = 97.80%` [AR FY18, Board's Report, PDF p16/pr9; AR FY20, MD&A, PDF p118/pr111; AR FY24, Consolidated P&L, PDF p157/pr151; AR FY26, Standalone P&L, PDF p250/pr239]. The carrying gap: `3,50,932 − 44,940 = 3,05,992`, i.e. the stake is carried at `44,940 / 3,50,932 = 12.81%` of market and the unrecognised excess is `3,05,992 / 6,67,301 = 45.86%` of attributable equity [AR FY26, Note 8, PDF p188/pr177]. **The counter-proportion that makes it a finding rather than a hidden-asset note:** the same 15% stake is `3,50,932 / 1,39,08,000 = 2.52%` of BSE's own market capitalisation but 45.86% of its book equity — so the market has already paid for it in BSE's price while the balance sheet has not recognised it, and the recurring contribution it makes to the P&L, 6,542, is `6,542 / 3,50,932 = 1.86%` of its own market value.
S4 CONNECTS: Governance supplies the frame — BSE is CDSL's promoter and nominates directors to its board (W2_peers §1.3), so this is a related-party holding progressively monetised through the P&L. Business supplies the structure: SEBI permits ownership of the clearing node and caps ownership of the depository node, so one adjacent business is consolidated and the other is being converted into exceptional income. Cash flow supplies the proof that the gains are real: FY2024's 40,662 was a cash disposal, and FY2026's 1,440 came with 1,690 of cash consideration. And the notes supply the pattern's own next instance — 127 of EBIX Insurance Broking already sits in assets held for sale on an in-principle approval of 11 November 2025 [AR FY26, Note 8.1, PDF p190/pr179].
DOMAINS: IncomeStatement, BalanceSheet, Notes, Governance, Business
DISCONFIRM: Sought and found, and it is substantial. (i) Each disposal is separately captioned, quantified and explained in the year it occurs — nothing is disguised as operating income, and the FY2024 consolidated P&L segregates 40,662 on its own face line. (ii) The FY2018 tranche was regulator-compelled and cannot be characterised as management-driven earnings management. (iii) BSE consistently presents EPS both before and after exceptional items, so the underlying number is always available to a reader. (iv) The carrying-versus-market gap is a required Ind AS disclosure that BSE makes plainly in Note 8, not something extracted against its will. What survives: seven years in ten is a frequency, not an exception; and three of the four largest items are the same asset, which means the category is better modelled as a divestment programme than as chance.
S5 MEANS: "Profit before exceptional items" has been the more meaningful line in seven of ten years, and the exceptional line has been, in substance, the progressive conversion of a strategic stake into reported profit. The remaining 15% is the last tranche of that programme, it is carried at an eighth of its value, and it is now producing a falling contribution — so the asset that has supplied nearly all of a decade's exceptional income is simultaneously the asset whose recurring income just fell 20.8%. A valuation that adds the CDSL stake at market and also capitalises the associate line is counting the same asset twice.
BASE-RATE: Realised, repeatedly, and always as a gain: FY2018 31,556, FY2020 9,158, FY2024 50,417 on the standalone — no loss has ever been realised on this holding, and no impairment has ever been taken against it. The counter-example within the same category is FY2021, where the exceptional item was a loss: 1,453 payable to S&P Dow Jones after a Singapore arbitration held BSE's termination of the index licence invalid [AR FY21, MD&A, PDF p102/pr97] — the one year the category ran the other way, and it arose from a contract dispute rather than from a disposal.
S6 IMPLICATION: The CDSL stake belongs in a valuation at its disclosed market value of 3,50,932 as a separate asset, with the associate line then excluded from the earnings stream to avoid double-counting, and the ten-year record suggests the residual 15% should be treated as a divestible asset rather than a permanent one. Monitorable: any Board approval or held-for-sale classification touching the CDSL holding, and the Note 8 market-value line each year; next at FY2027 or at any interim Regulation 30 announcement. Thesis-breaker: a further reduction below 15% would remove the last recurring depository income and convert the residual into a one-time gain, ending both the associate line and the hidden-asset argument in the same transaction.
SEVERITY: Medium

### FINDING: BSE's tax rate looks below statutory on the face of the P&L and is above it on the only base that is arithmetically valid
S1 WHAT: Total tax of 82,384 over the P&L's own "Profit before tax" of 3,29,914 gives 24.971%, which is 0.197pp below the 25.168% statutory rate. The company's own reconciliation uses a different denominator — 3,23,372, which excludes the associate share — and on that base the effective rate is 25.477%, 0.309pp ABOVE statutory [AR FY26, Note 29(b), PDF p215/pr204; AR FY26, Consolidated P&L, PDF p164/pr153].
S2 WHY: The 6,542 associate share enters PBT already net of CDSL's own corporate tax, so including it in the denominator of an effective tax rate divides a full tax charge by a partly post-tax profit. The gap is not an accounting choice by BSE — Note 29(b) uses the correct base — it is an artefact of how the face of an Ind AS P&L orders the associate line, above tax rather than below it. What raises the true rate above statutory is specific and disclosed: 649 of losses in the IFSC subsidiaries on which no deferred tax asset is recognised, and 256 of prior-period charge.
S3 EVIDENCE: `82,384 / 3,23,372 = 25.477%` against `82,384 / 3,29,914 = 24.971%`; the two bases differ by 0.505pp, worth `0.505% × 3,23,372 = 1,633` lakh of apparent tax. The bridge: `25.168 + 0.029 (other-than-temporary differences) + 0.201 (unrecognised business losses) + 0.079 (prior period) = 25.477` [AR FY26, Note 29(b), PDF p215/pr204]. **The counter-proportion:** the item that pushes the rate above statutory, 649, is `649 / 82,384 = 0.79%` of the tax charge but arises on entities that contributed `(973)` of loss to non-controlling interests and 3,123 of the group's translation gain — so the same subsidiaries that cost 0.201pp of tax rate supply 83.4% of OCI. Both sector-specific charges are proved deductible from the same note: the SEBI regulatory fee of 56,616 would add `56,616 × 25.168% = 14,249` if disallowed and the core SGF contribution of 7,696 would add 1,937, against a total "expenses disallowed" line of 165 implying only `165 / 0.25168 = 656` lakh of disallowance group-wide, confirmed on the standalone at 193 [AR FY26, Note 27, PDF p212/pr201; AR FY26, Standalone Note 29(b), PDF p289/pr278].
S4 CONNECTS: The balance sheet shows the cash consequence — current tax liabilities up 138.1% to 20,109, and a first-ever net deferred tax liability on fixed assets of 320 created by the FY2026 capex. The cash flow shows the lag — direct taxes paid 65,541 against a charge of 82,384, a cash rate of 19.87% on face PBT, roughly 5pp below the book rate for two years running, reconciling to the balance sheet within 117 lakh. Management's own precedent for the error is on the record: the FY2024 MD&A printed "Effective tax rate 22%" [AR FY24, MD&A, PDF p76/pr70], which is the face-PBT calculation on a year when the associate contributed 7,182 and an exceptional gain of 40,662 sat in the denominator. Industry: at a 25.168% statutory rate with no meaningful shelters, an MII's tax rate is the least discretionary line in its P&L, which is precisely why a 0.5pp presentation artefact matters more here than it would elsewhere.
DOMAINS: IncomeStatement, BalanceSheet, CashFlow, Notes, MgmtCommentary
DISCONFIRM: Sought and found. (i) BSE itself uses the correct base in Note 29(b) and always has; the misleading calculation is the one a reader performs off the face, not one the company publishes in its tax note. (ii) The magnitude is 0.5pp, which changes no investment conclusion on its own. (iii) The reconciliation is complete for FY2026 — every component is named and the arithmetic closes exactly. What survives: the FY2024 MD&A did publish the face-based rate, so the error has been made in this company's own reporting; and the gap grows with the associate, so it is not self-limiting.
S5 MEANS: BSE pays slightly more than the statutory rate, not less, and the reason is a structural drag rather than a timing item — unrecognised losses in GIFT City that have accumulated to 21,960 of tax losses plus 3,164 of unabsorbed depreciation with an expiry ladder running to 2034-35, and a new 2,450 tranche added in FY2026. That drag costs 0.201pp of rate a year and rose `649 / 310 = 2.09×` in one year. The tax line therefore contains no cushion: there is no shelter to unwind, no MAT credit left (the entitlement went to nil in FY2026), and the only direction the rate can move from a policy change is up.
BASE-RATE: The eleven-year effective-rate series on the face basis is 17.48%, 13.34%, 18.94%, 10.73%, 10.98%, 7.12%, 25.16%, 30.82%, 22.49%, 24.66%, 24.97% (`trend_10y.csv`, total tax over PBT), so FY2026 is the third-highest of eleven and the series has been above 22% in every year since FY2022. No tax dispute has produced a realised loss in the window: contingent income-tax matters stand at 13,496 against 11,170 and no provision has been made against them, and no year in the corpus records a settled adverse tax assessment charged to the P&L.
S6 IMPLICATION: Any forward tax assumption should be struck at or slightly above 25.168% on profit before the associate, with the associate added back after tax, rather than at the ~25% implied by the face — and the GIFT City drag should be modelled as a persistent 0.2pp rather than a one-off, since the loss pool is growing and the expiry ladder means tranches will lapse unused. Monitorable: the (E) line "business loss carried forward" in Note 29(b) each year against the unrecognised loss pool in Note 18, next at FY2027. Thesis-breaker: recognition of a deferred tax asset on the IFSC losses, which would signal management expects those entities to become profitable and would produce a one-time credit of up to `(21,960 + 3,164) × 25.168% = 6,324` lakh.
SEVERITY: Watch

### FINDING: The accounting-policy table says buildings run 60 years, the note two pages later says 25, and the report has printed both for two consecutive years
S1 WHAT: Note 2.3.5(b) prints "Buildings* 60 years" in the table of estimated useful lives. Note 3 footnote 3 states the Holding Company "has revised the estimated useful life of its building to 25 years, effective April 01, 2024 impact of same was Rs. 13" [AR FY26, Note 2.3.5(b), PDF p174/pr163; AR FY26, Note 3 fn 3, PDF p181/pr170]. The FY2025 report carries the identical pair [AR FY25, Note 2.2.5, PDF p166/pr155; AR FY25, Note 3 fn 3, PDF p172/pr161].
S2 WHY: The asterisk resolves the conflict by cross-reference rather than by correcting the table, and the note itself is incomplete in a way that makes the quantification uncheckable: it states the life the asset was revised TO and never the life it was revised FROM, so the 13 has no reproducible input. The change matters more in FY2026 than in FY2025 because buildings gross block rose from 3,849 to 21,970 on additions of 18,022 — the class whose life is disputed grew 470.8% in the year after the revision.
S3 EVIDENCE: The buildings charge went 122 to 1,269, ×10.4, on a class whose opening net block was 1,778 and which received 18,022 of additions [AR FY26, Note 3, PDF p181/pr170]. `ESTIMATE`, assumptions declared (mid-year convention on additions, 5% residual value, neither disclosed by the company): implied FY2026 rate `1,269 / (1,778 + 18,022 / 2) = 11.76%` against a 25-year written-down-value rate of `1 − 0.05^(1/25) = 11.29%` and a 60-year rate of `1 − 0.05^(1/60) = 4.87%`; implied FY2025 rate `122 / (1,916 + 15 / 2) = 6.34%`, which matches neither, in the very year the change is stated to take effect from. **The counter-proportion:** the disclosed impact of 13 is `13 / 15,896 = 0.08%` of the total charge, while the class it applies to now carries `21,970 / 1,05,539 = 20.82%` of the group's gross block against `3,849 / 63,738 = 6.04%` a year earlier — a policy footnote sized against last year's asset base and left standing against this year's.
S4 CONNECTS: W3_cost established that the real discretion in this line sits upstream, in what enters the asset base rather than in the rate — the capitalised share of technology outlay moved 14.20pp in one year, from 33.51% to 47.71%. The two findings compound: more cost is being capitalised, and the policy governing how fast the largest new asset class is written off is stated two ways in the same document. Governance is engaged because the sole Key Audit Matter for FY2026 is "Information Technology (IT) systems and controls" [AR FY26, Auditor's Report, PDF p155/pr144] — the auditor's attention is on the systems, not on the property estimates. Management commentary quotes a different depreciation number again: "+50% to ₹13,533 Lakh", the standalone, against the consolidated +40.70% [AR FY26, MD&A, PDF p76/pr65].
DOMAINS: IncomeStatement, BalanceSheet, Notes, MgmtCommentary, Governance
DISCONFIRM: Sought and found. (i) The asterisk on "Buildings*" explicitly directs the reader to Note 3, so the report does connect the two statements and the conflict is signposted rather than concealed. (ii) The note's own wording — "some of its properties" — is consistent with a partial revision, in which case 60 years may remain correct for buildings the review did not cover. (iii) A shorter life is the conservative direction: it accelerates the charge and reduces reported profit, which is the opposite of the incentive that would make this worth suspecting. (iv) The FY2026 implied rate IS consistent with 25 years, so the charge actually taken looks right. What survives: the reader cannot tell which buildings are on which life, cannot reproduce the stated 13, and would apply the wrong rate to the 18,022 of new buildings if working from the policy table alone.
S5 MEANS: The forward depreciation charge on the largest single capital addition of the year cannot be estimated from the published policy, because the published policy gives two answers that differ by a factor of 2.3 in rate terms (11.29% against 4.87%). On the 18,022 of building additions that is a first-full-year difference of roughly `18,022 × (11.29% − 4.87%) = 1,157` lakh — comparable in size to the entire 1,212 of committed incremental charge W3_cost derived for the whole asset base. The uncertainty is therefore not academic; it is about the same order of magnitude as the depreciation increase that is already known.
BASE-RATE: No realised loss from a useful-life estimate is recorded at BSE in the ten-year corpus — no impairment of property has ever been taken, and the only FY2026 impairments are 4 of goodwill and 100 against a newly acquired associate. The company's disclosed history of estimate changes is thin: `W3_notes.md` records one quantified accounting change in the window that actually moved earnings, the FY2019 ICCL Core SGF reclassification worth 2,256, and the building-life revision is the only change of estimate disclosed under Ind AS 8 in the last two years. So the base rate for this specific failure mode at this company is zero occurrences, and the finding is about checkability rather than about a demonstrated loss.
S6 IMPLICATION: Depreciation modelled off the published policy table will understate the charge on 20.82% of the gross block, so a forward earnings frame should use the 25-year life for the parent's buildings and treat the difference as a range rather than a point. The quality signal is the larger one: a policy table and a note stating different lives for the same class, uncorrected across two audited reports, is a control observation about disclosure review at a company whose only Key Audit Matter is systems and controls. Monitorable: whether the FY2027 policy table is corrected, and whether the buildings depreciation rate implied by Note 3 stays near 11.3%. Thesis-breaker: an FY2027 restatement or a materially different implied rate, either of which would mean the estimate was not applied as described.
SEVERITY: Watch

### FINDING: The earnings-per-share figure BSE leads with is standalone, before an item, and does not tie to the profit printed on the line above it
S1 WHAT: The Board's Report and MD&A lead with basic and diluted EPS of ₹56.27 [AR FY26, Board's Report, PDF p23/pr12]. The audited consolidated total-operations EPS is ₹60.61 [AR FY26, Note 30, PDF p216/pr205]. The ₹56.27 is standalone, is struck before an exceptional item, and is arithmetically inconsistent with the profit figure printed immediately above it in the same note.
S2 WHY: Three separate mechanisms stack. (i) The standalone excludes ICCL, BSE Index Services and the other subsidiaries whose profit consolidates. (ii) The "before exceptional items" presentation removes the 1,590 gain on the BSE Institute sale, which the consolidated statements classify as discontinued operations instead. (iii) The EPS row deducts the PRE-TAX exceptional item while the profit row above it deducts the NET-OF-TAX amount, so the two rows use different numerators for the same concept.
S3 EVIDENCE: Standalone Note 30 prints "Profit before exceptional items (net of tax) – ₹ lakhs 2,32,075" and, on the next row, EPS of ₹56.27 [AR FY26, Standalone Note 30, PDF p290/pr279]. But `2,32,075 lakh / 41,19,79,077 = ₹56.33`, not ₹56.27; the printed figure requires a numerator of `56.27 × 41,19,79,077 = 2,31,826` lakh, and `2,33,416 − 1,590 = 2,31,826` — the pre-tax deduction — where `2,33,416 − 2,32,075 = 1,341` is the net-of-tax amount and `1,590 − 1,341 = 249` is exactly the tax on the gain in Note 49. Size: ₹0.06 per share, `0.06 / 56.33 = 0.11%`, worth 254 lakh of profit. **The counter-proportion that matters more than the 0.11%:** the group figure is ₹60.61 and the headline is ₹56.27, so the number the reader meets first is `60.61 / 56.27 = 7.71%` below the audited group figure — the presentation gap is seventy times the arithmetic gap.
S4 CONNECTS: The denominator is itself unusual and correctly disclosed: EPS is struck on ISSUED share capital of 41,19,79,077, not on subscribed and paid-up capital of 40,78,84,077, the `41,19,79,077 − 40,78,84,077 = 40,95,000` difference being shares still in abeyance under the 2005 Demutualisation Scheme to which "all corporate benefits ... including dividend and bonus are accrued" [AR FY26, Note 14, PDF p203/pr192]. That is why the denominator is identical in both years despite 17,55,000 shares being allotted in FY2026 — they came out of the abeyance pool, not from a new issue. The MD&A's use of standalone figures is systematic rather than isolated: it quotes standalone investment income (33,114 against a consolidated 29,030), standalone depreciation (13,533 against 15,896) and standalone capital additions (45,753) in the same section, a pattern W3_revenue independently found on the revenue side.
DOMAINS: IncomeStatement, Notes, MgmtCommentary, Governance
DISCONFIRM: Sought and found, and it is strong. (i) Every figure is published: the consolidated EPS of ₹60.61 is on the face of the consolidated P&L, the standalone ₹56.66 after exceptional items is in Note 30, and both bases are shown side by side in the Board's Report's own five-column table. Nothing is hidden. (ii) The headline is the LOWER number, so the presentation is conservative, not flattering — the opposite of the incentive that would make this suspicious. (iii) The 0.11% arithmetic slip is immaterial in rupees and is confined to a supplementary "before exceptional" line, not to the statutory EPS. (iv) The FY2025 comparative in the same note ties exactly (`1,11,245 / 41,19,79,077 = ₹27.00`), so this is a one-year slip rather than a systematic method. What survives: an audited note contains two adjacent rows that cannot both be right, and the wrong one is the figure reproduced in the Board's Report.
S5 MEANS: There is no single number called "BSE's EPS" — there are five published figures for FY2026 (₹60.61, ₹60.32, ₹0.29, ₹56.66, ₹56.27) and a sixth in circulation inside this project (₹61.22, struck on paid-up rather than issued capital in `records/capital_structure.md`). Any per-share metric therefore has to name its basis or it is uninterpretable, and the spread between the highest and lowest reasonable candidates is `61.22 / 56.27 = 8.80%`. On the 4 September 2026 close of ₹3,409.80 that is a trailing P/E anywhere between 55.7× and 60.6× depending on which of the company's own numbers is used.
BASE-RATE: The company has published a mismatched pair before, in the opposite direction: the FY2024 consolidated EPS of ₹56.66 after exceptional items implies a denominator of `77,839 lakh / 56.66 = 13,73,79,xxx` against the 13,73,26,359 actually used, a 0.04% discrepancy [AR FY24, Note 30, PDF p211/pr205]. So small EPS rounding inconsistencies recur, and none has ever been restated. The one genuine EPS restatement in the window is mechanical and correctly done: FY2025's ₹96.55 became ₹32.18 under Ind AS 33 after the 2:1 bonus, `96.55 / 3 = 32.18`, logged as R-25 in `W3_notes.md`.
S6 IMPLICATION: Per-share work should be struck on the audited consolidated total-operations figure of ₹60.61 with the denominator stated as issued capital of 41,19,79,077, and the ₹61.22 currently carried in this project's capital-structure record should be corrected — it overstates by 1.01% because it uses the closing paid-up count. The wider signal is about which basis management reaches for: standalone, before items, in three separate places in the same MD&A section, which means every management-quoted growth rate in that section needs re-striking on the consolidated base before it enters a model. Monitorable: whether FY2027's Note 30 reconciles its two rows, and whether the MD&A moves to consolidated figures. Thesis-breaker: none applies — this is a measurement convention, and it is falsified simply by the FY2027 note tying.
SEVERITY: Watch

---

## 10. Gap register additions (doctrine §9)

Each is a `NOT-DISCLOSED` or unreproducible link from the chains above, with the document that would
settle it and the concall question it generates.

| ID | Line | What is missing | Do peers disclose it? | What would settle it |
|---|---|---|---|---|
| G-BL-01 | Tax — FY2025 reconciliation | No composition for either the 3,041 "expenses disallowed" add-back or the (2,987) prior-period credit; together 6,028 lakh, 13.98% of that year's charge | NSE and MCX disaggregate their disallowance lines; CDSL and IEX do not | AR FY27 Note 29(b) with a break-up, or the FY2025 tax assessment order |
| G-BL-02 | Tax — deferred | 14-lakh residual between the Note 18 movement schedule (476 recognised in P&L) and the P&L's deferred tax credit (462); FY2025 had a separate discontinued-operations column, FY2026 does not | n/a — a within-company reconciliation | AR FY27 Note 18 with the discontinued-operations column restored |
| G-BL-03 | Depreciation | The useful life buildings were revised FROM is not stated, so the disclosed impact of 13 cannot be reproduced; and the policy table still prints 60 years | Peers state a single life per class | AR FY27 Note 2.3.5(b) corrected, or a Note 3 footnote giving the prior life |
| G-BL-04 | Depreciation | 39 (FY2026) and 81 (FY2025) residual between Notes 3+4+6 and the face line, attributable to the discontinued operation but not stated | n/a | AR FY27 Note 49 expense analysis; carried jointly with W3_cost's G-COST-06 |
| G-BL-05 | Investment income | The exchange-traded fund holding of 8,006 is not identified by asset class, issuer or index anywhere in Note 9 | IEX and CDSL name their fund holdings | AR FY27 Note 9 with ETF detail, or the Board-approved investment policy |
| G-BL-06 | Investment income | The Board-approved investment policy is described in the MD&A but not published — no rating floor, duration cap, single-issuer limit or asset-class band | NSE publishes an investment-policy summary in its risk note | The investment policy itself, or an MD&A expansion |
| G-BL-07 | Investment income | No policy explains why income on Note 16 bucket (C) is revenue while income on bucket (B) and the Core SGF is credited away from the P&L | No peer holds all three pools, so ungraded | AR FY27 Note 2.3.10 or 2.3.4 extended to cover treasury income on clearing float |
| G-BL-08 | Discontinued operations | The purchaser of BSE Institute Limited is not named, and it is not stated whether the buyer is a related party | Ordinary practice is to name the counterparty | The Regulation 30 announcement of the transaction, or the share purchase agreement |
| G-BL-09 | Discontinued operations | The 6,191 of investing cash from discontinued operations against a consideration of 1,690 — the 4,501 excess is not explained | n/a | AR FY27 comparative, or BIL's own final accounts |
| G-BL-10 | Associates | Note 8 gives BSE E-Agricultural Markets a share of profit of 20; AOC-1 Part B gives 21 for the same entity in the same report | n/a — an internal inconsistency | AR FY27 Note 8 and AOC-1 agreeing |
| G-BL-11 | OCI | Note 8 shows 533 of associate OCI (`464 + 68 + 1`) against 464 on the face; the 69 must sit inside the undisaggregated remeasurement line but the report does not say so | Peers disaggregate OCI lines | AR FY27 OCI note, which BSE does not currently provide |

**Concall questions generated** (for `records/concall_questions.md`, W6 or the next investor call):

1. What were the two items behind FY2025's ₹30.41 crore of disallowed expenses and ₹29.87 crore
   prior-period tax credit, and are they the same matter?
2. Income earned on clearing and settlement balances is credited to revenue while income on earmarked
   deposits is credited to the depositors and Core SGF income to the fund. What is the contractual basis
   for the difference, and could a SEBI direction change it?
3. What is the duration, credit-rating floor and single-issuer limit in the Board-approved investment
   policy, and what is the ₹80.06 crore of exchange-traded funds invested in?
4. The accounting-policy table states a 60-year life for buildings and Note 3 states 25 years. Which
   applies to the ₹180.22 crore of buildings added in FY2026?
5. Is the 15% CDSL holding a permanent strategic asset or the residual of a divestment programme?

---

## 11. Handoffs

- **W4_cash and the ₹100 map** — investment income is removed from CFO in full and returns in investing
  as 23,798 of interest received; the map must not treat the 29,030 as operating cash. The 17,142 of
  treasury income *is* inside revenue and therefore inside CFO, so the two halves enter the map at
  different points. Own-account corpus 6,10,190 against 3,66,977 is the closing stock the map's capex
  and distribution steps draw down.
- **W4_capalloc** — the three CDSL tranches (§6.2) are capital-allocation decisions, two of them
  voluntary, and the residual 15% is carried at 12.81% of market. The Core SGF's 3,727 of retained fund
  income and the 1,24,683 balance are not deployable and must be excluded before any return measure.
- **W4_uniteconomics** — the tax rate to use is 25.477% on profit before the associate, not the 24.971%
  the face implies; depreciation carries 1,212 of already-committed forward charge (W3_cost) plus an
  unquantifiable range on the 18,022 of buildings (§4.2).
- **W3_group_rpt, when it exists** — three items are handed over rather than answered: the fall in
  non-controlling interest from 15,197 to 12,249 despite +408 of comprehensive income and +1,215 of
  share issue by a subsidiary; the identity and related-party status of the BSE Institute purchaser; and
  the two-layer associate structure, four associates held through BSE Technologies and three through the
  IFSC entities.
- **W5 earnings-quality gate** — the reliable numbers here are the tax charge (reconciliation closes
  exactly, cash ties to the balance sheet within 0.67%) and the associate line (roll-forward exact to the
  rupee). The two that carry a caveat are the FY2025 tax comparative (BROKEN at L8, §3.3) and the
  depreciation policy (BROKEN at L5, §4.1). The 8,875 of FVTPL gain is 30.57% of investment income and
  3.57% of PBT and is a revaluation, not a realised return.
- **W8 valuation** — strike per-share metrics on ₹60.61 and 41,19,79,077 issued shares, not on ₹61.22 and
  the paid-up count; carry the CDSL stake at its disclosed market value of 3,50,932 as a separate asset
  and exclude the associate line from the earnings stream if doing so; and do not extend an operating
  multiple to the 17,142 of float-derived treasury income.

---

## 12. Verification

`python3 companies/BSE/verify.py` run after writing this file; result recorded at the foot of
`state/progress.json` by the runner. Every `DERIVED` value above shows its arithmetic inline per §4b, and
each of the four exact tie-outs that gate a conclusion — Note 23 components to 29,030, the
standalone-to-consolidated investment-income bridge to 29,030, the CDSL roll-forward to 44,940, and the
tax reconciliation to 82,384 — was recomputed a second time independently rather than re-read.
