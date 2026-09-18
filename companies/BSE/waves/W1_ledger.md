# W1 — Evidence ledger: BSE Limited

Wave 1 artifact (doctrine §7, "one read, many uses"). Three jobs: **audit** the mechanically extracted
series, **resolve** whether own-account operating cash can be separated from clearing-member float, and
**chain** the FY2026 lines that decide the case. No investment conclusions — that is W3/W4/W5's work.

Navigation throughout is `waves/W1_docmap.md`. Every cite carries both page numbers using that map's
per-document offsets (FY2017 +2 · FY2018 +7 · FY2019 +9 · FY2020 +7 · FY2021 +5 · FY2022 +9 ·
FY2024 +6 · FY2025 +11 · FY2026 +11), so `PDF p164/pr153` = PDF page 164, printed folio 153.

**Basis rule applied to both CSVs, and it is the fix for most of what was wrong:** each year's column is
taken from **that year's own annual report, as first reported**, never from a later report's comparative
column. FY2016 (from the FY2017 AR) and FY2023 (from the FY2024 AR, GAP-001) are the two unavoidable
exceptions and are flagged as comparatives.

---

## 1. Audit result in one line

**413 populated cells checked — every populated cell in both CSVs, not a sample. 39 were wrong or
mis-based (9.4%): 35 factually wrong, 4 carrying a sign convention that breaks the P&L identity.
101 further cells were filled that the extractor had missed, 66 of them in eight new rows.**

Every cell was checked against the statement page in the source document, read directly from
`data/text/*.txt` with the docmap's page-bleed rule applied and the printed folio confirmed in the page
body. Both CSVs were then run through four arithmetic identities (revenue components = revenue from
operations; total income − total expenses ± exceptional − SGF contribution + associate share = PBT;
PBT − tax + discontinued = PAT total; non-current + current assets = total assets = equity + Core SGF +
liabilities). **All eleven years now close exactly on all four**; before the corrections, five of eleven
years failed the PBT identity and two failed the balance-sheet identity.

### 1.1 The single most important data-integrity problem

**The FY2016 and FY2017 balance-sheet columns of `balance_cash_10y.csv` were shifted by one full year —
every one of the ten balance-sheet rows, twenty cells, silently one column to the left.**

Cause: FY2017 is the **Ind AS first-time-adoption year and its consolidated balance sheet carries three
columns**, not two — March 31 2017, March 31 2016 and **April 1 2015**
`[AR FY2017, Consolidated Balance Sheet, PDF p116/pr114]`. The extractor's "last two numeric tokens on a
statement line" heuristic therefore captured columns 2 and 3 (FY2016 and Apr-2015) and labelled them
FY2017 and FY2016. Nothing about the output looked wrong: the numbers were real, internally consistent
year-on-year, and the totals still tied to themselves.

| Row | CSV said FY2017 | Truth FY2017 | CSV said FY2016 | Truth FY2016 |
|---|---|---|---|---|
| total_equity | 2,76,020 | **2,95,328** | 2,74,299 | **2,76,020** |
| total_assets | 4,24,339 | **5,18,301** | 4,21,033 | **4,24,339** |
| total_current_liabilities | 1,29,575 | **2,01,643** | 1,34,646 | **1,29,575** |
| trade_receivables | 4,719 | **6,872** | 3,481 | **4,719** |

All three FY2017 columns read on the page: total assets `5,18,301 / 4,24,339 / 4,21,033`; total equity
`2,95,328 / 2,76,020 / 2,74,299` `[AR FY2017, Consolidated Balance Sheet, PDF p116/pr114]`. The FY2018
AR's comparative column independently confirms FY2017 total assets **5,18,301** and total equity
**2,95,328** `[AR FY2018, Consolidated Balance Sheet, PDF p133/pr126]`.

Why this is the worst of the 39: it understates FY2017 total assets by **93,962 lakh (18.1%)** and
FY2017 equity by **19,308 lakh (6.5%)**, and it is invisible to every internal check because the
column was consistent — the wrong year, not a wrong number. Any ten-year ROE, asset-turnover or
book-value series starting at FY2016 was computing off a base that is one year stale at both ends.

### 1.2 The second problem: the FY2024 column was on two different bases at once

FY2024 was populated partly from the FY2024 AR and partly from the FY2025 AR's restated comparative.
`trend_provenance.json` records a source for only 18 of the 27 populated FY2024 P&L cells; the nine
cells with **no provenance entry at all** are exactly the nine taken from the FY2025 comparative
(`total_income`, `technology_expense`, `regulatory_contribution`, `exceptional_items`,
`core_sgf_contribution`, `pbt`, `pat_continuing`, `pat_discontinued`, `pat_total`). The column therefore
combined revenue of 1,39,003 (as first reported) with total income of 1,59,588 (as restated) — figures
that cannot both be true, and whose difference (1,39,003 + 20,247 + 2,540 = 1,61,790 ≠ 1,59,588) is the
discontinued operation the FY2025 AR carved out.

`records/restatements.md` already documents the FY2024 restatement correctly. The CSV did not follow it.

### 1.3 Where the "last two numeric tokens" heuristic failed — the taxonomy

| Failure mode | Cells | Example |
|---|---|---|
| **Extra column on the page** (Ind AS transition, 3 columns) | 20 | FY2017 balance sheet, §1.1 |
| **Grabbed the subtotal above the target line** | 3 | `core_sgf_contribution` FY2026 = 3,31,068 — that is *"Profit before contribution to core settlement guarantee fund"*; the contribution itself is **7,696** `[AR FY26, Consolidated P&L, PDF p164/pr153]`. Same for FY2025 (1,75,568 vs **9,000**) and FY2024 (60,548, which is the FY2025 AR's restated FY2024 subtotal, vs **9,170**) |
| **Pulled a later AR's restated comparative** | 9 | `total_income` FY2024, `technology_expense` FY2024, `pat_continuing` FY2017/FY2024, `rev_training_institute`/`rev_software` FY2018 |
| **Matched a duplicated label on the same page** | 1 | `pat_attributable` FY2019 = 19,417 is the *continuing-operations* line; the total-operations line four rows below reads **19,928** `[AR FY2019, Consolidated P&L, PDF p148/pr139]` |
| **Sign convention lost** | 4 | `exceptional_items` FY2016–FY2019 stored as positive magnitudes although the AR *deducts* them ("Profit before tax (6−7)"); FY2020 onward the AR *adds* them ("Income/(expense)"). Summed unsigned, the PBT identity misses by twice the item |
| **Line silently dropped** | 2 | `cfo` FY2017 = 77,450 is the FY2018 AR's restated continuing-operations figure; FY2017's own statement reads **81,711** `[AR FY2017, Consolidated Cash Flow, PDF p118/pr116]`. `cfo` FY2016 (−4,422) was left blank although it is on the same page |

### 1.4 Full change log — `records/trend_10y.csv`

**Value corrected (7 factual + 4 sign):**

| Row | Year | Was | Now | Source |
|---|---|---|---|---|
| core_sgf_contribution | FY2026 | 3,31,068 | **7,696** | `[AR FY26, Consolidated P&L, PDF p164/pr153]` |
| core_sgf_contribution | FY2025 | 1,75,568 | **9,000** | `[AR FY26, Consolidated P&L, PDF p164/pr153]` |
| core_sgf_contribution | FY2024 | 60,548 | **9,170** | `[AR FY24, Note 28, PDF p208/pr202]` |
| total_income | FY2024 | 1,59,588 | **1,61,790** | `[AR FY24, Consolidated P&L, PDF p157/pr151]` ("Total revenue (1+2+3)") |
| technology_expense | FY2024 | 13,731 | **13,744** | `[AR FY24, Note 27, PDF p208/pr202]` |
| pbt | FY2024 | 99,222 | **99,552** | `[AR FY24, Consolidated P&L, PDF p157/pr151]` |
| pat_attributable | FY2019 | 19,417 | **19,928** | `[AR FY2019, Consolidated P&L, PDF p148/pr139]` |
| exceptional_items | FY2016 | 4,660 | **−4,660** | `[AR FY2017, Consolidated P&L, PDF p117/pr115]` |
| exceptional_items | FY2017 | 2,079 | **−2,079** | `[AR FY2017, Consolidated P&L, PDF p117/pr115]` |
| exceptional_items | FY2018 | 260 | **−260** | `[AR FY2018, Consolidated P&L, PDF p134/pr127]` |
| exceptional_items | FY2019 | 1,352 | **−1,352** | `[AR FY2019, Consolidated P&L, PDF p148/pr139]` |

**Blanked (value was real but came from the wrong report; the correct value is recorded here, not lost):**

| Row | Year | Was | Why blanked | The own-AR position |
|---|---|---|---|---|
| regulatory_contribution | FY2024 | 23,690 | The line **did not exist** in the FY2024 AR | FY2024 printed *Provision for SEBI regulatory fee* **16,977** on the P&L face `[AR FY24, Consolidated P&L, PDF p157/pr151]` plus four contribution lines inside Note 28 (§4, chain 3) |
| pat_continuing | FY2017 | 17,851 | FY2017 AR has no continuing/discontinued split | 17,851 is the FY2018 AR's restated FY2017 `[AR FY2018, PDF p134/pr127]` |
| pat_discontinued | FY2017 | 8,658 | same | 8,658, same source |
| pat_continuing | FY2024 | 76,870 | FY2024 AR has no split | 76,870 is the FY2025 AR's restated FY2024 `[AR FY25, PDF p156/pr145]` |
| pat_discontinued | FY2024 | 296 | same | 296, same source |
| rev_training_institute | FY2018 | 2,024 | Not on the FY2018 P&L face | 2,024 is the FY2019 AR's restated FY2018 `[AR FY2019, PDF p148/pr139]` |
| rev_software | FY2018 | 998 | same | 998, same source. **2,024 + 998 = 3,022** — exactly the amount `records/restatements.md` records as moved from other income into revenue in the FY2019 presentation. Keeping them made the FY2018 revenue rows sum to 50,720 against a reported 47,698 |

**Newly filled, pre-existing rows (28):** `core_sgf_contribution` FY2016–FY2023 (1,741 / 952 / 6,291 /
684 / 74 / 619 / 2,905 / 5,496 — from each year's cash-flow adjustment line, e.g.
`[AR FY2022, Consolidated Cash Flow, PDF p151/pr142]`, and FY2023/FY2024 from
`[AR FY24, Note 28, PDF p208/pr202]`); `exceptional_items` FY2022 0, FY2023 0, FY2024 **40,662**
(the CDSL partial-disposal gain, `[AR FY24, Consolidated P&L, PDF p157/pr151]`), FY2025 0;
`rev_software` FY2022 1,828 / FY2023 3,189 / FY2024 2,954 / FY2025 2,115; `technology_expense` FY2022
9,687 / FY2023 12,390; `total_income` FY2023 95,394; `pbt` FY2023 29,726; `pat_total` FY2016 17,713 /
FY2021 14,170 / FY2022 24,493 / FY2023 20,565; `pat_discontinued` FY2020 0; `total_comprehensive`
FY2018 72,466 / FY2019 20,627; `associate_profit` FY2016 224 (JV profit 251 less associate loss 27).

**New rows (3):**
- `rev_index_services` — FY2025 **2,403**, a P&L face line the extractor had no row for
  `[AR FY25, Consolidated P&L, PDF p156/pr145]`. With it the FY2025 revenue components now sum exactly:
  `2,37,179 + 48,995 + 5,042 + 2,403 + 2,115 = 2,95,734`.
- `les_expense` — Liquidity Enhancement Scheme, FY2016–FY2026. **Warning for code: this row is additive
  in FY2018–FY2025 (separate face line or exceptional item) but in FY2026 the 556 is a *component of*
  `other_admin_expenses` inside Note 28 `[AR FY26, Note 28, PDF p213/pr202]` — do not add it to the
  FY2026 expense stack.**
- `sebi_regulatory_fee` — FY2024 16,977 (P&L face, Note 46), FY2025 33,141, FY2026 56,616 (Notes 28/27).

### 1.5 Full change log — `records/balance_cash_10y.csv`

- **20 cells re-aligned** for the FY2016/FY2017 column shift (§1.1), across `total_equity`,
  `total_assets`, `total_noncurrent_assets`, `total_current_assets`, `total_current_liabilities`,
  `total_noncurrent_liab`, `trade_receivables`, `ppe`, `cwip`, `equity_and_liab_total`.
- **`cfo` FY2017 77,450 → 81,711** `[AR FY2017, Consolidated Cash Flow, PDF p118/pr116]`.
- **7 cells newly filled in pre-existing rows:** `cfo` FY2016 −4,422; `cash_close` FY2016 33,625;
  `dividend_paid` FY2016 −11,169, FY2017 −8,541, FY2018 −18,391, FY2019 −22,814, FY2020 −15,843.
  (FY2016 and FY2017 also carry a separate NCI dividend line, −1,267 and −1,441, not included in this
  row `[AR FY2017, Consolidated Cash Flow, PDF p119/pr117]`.)
- **8 new rows, 51 cells** — see §3.4 and §4.

### 1.6 Consequence for `records/cash_ledger_note.md` — it needs one number changed

Its cumulative figure `cumulative CFO 8,17,432 / cumulative PAT attributable 6,46,945 = 1.264` used the
wrong FY2017 CFO and the wrong FY2019 PAT. Recomputed on the corrected series:

`cumulative CFO FY2017–FY2026 = 81,711 − 27,147 − 31,805 + 39,671 − 6,787 + 1,44,175 − 13,711 +
2,84,203 + 41,015 + 3,10,368 = 8,21,693`
`cumulative PAT attributable = 22,057 + 71,128 + 19,928 + 12,227 + 14,490 + 25,433 + 22,067 + 77,839 +
1,32,589 + 2,49,698 = 6,47,456`
`8,21,693 / 6,47,456 = 1.269` (was 1.264)

The change is trivial. **The reason that ratio is unquotable is not arithmetic — it is §3 below.**

### 1.7 Restatements the audit surfaced that `records/restatements.md` does not yet carry

Recorded, not resolved; for W3_notes. Nothing is deleted — both sides stand.

1. **FY2018 total equity restated 3,13,435 → 3,08,055** (−5,380, −1.7%) between
   `[AR FY2018, PDF p133/pr126]` and `[AR FY2019, PDF p147/pr138]`. Total assets 4,98,436 → 4,99,808.
   A balance-sheet restatement, absent from the register, which covers P&L lines only.
2. **FY2018 Core SGF balance restated 29,096 → 35,848** (+6,752, +23.2%), same two pages.
3. **FY2025 "Administration and other expenses" 20,154 → "Other expenses" 20,820** (+666) in the FY2026
   AR: the FY2025 face line *Liquidity enhancement scheme expense 666* was folded into the expense note
   `[AR FY25, Note 29, PDF p196/pr185]` → `[AR FY26, Note 28, PDF p213/pr202]`. Exact, and it explains
   the whole difference.
4. **FY2025 trade receivables restated 30,967 → 28,778** (−2,189, −7.1%)
   `[AR FY25, PDF p155/pr144]` → `[AR FY26, PDF p163/pr152]`. Any FY2025→FY2026 receivable-days series
   must pick one side.
5. **FY2025 other current liabilities restated 42,503 → 47,947** (+5,444) across the same two pages —
   the amount equals the FY2025 *Provision for SEBI regulatory fee* of 5,444
   `[AR FY25, Note 17, PDF p191/pr180]`, i.e. a provision reclassified into other liabilities.
6. **FY2024 CFO restated 2,84,203 → 2,64,435 continuing + (89) discontinued**
   `[AR FY24, PDF p158/pr152]` → `[AR FY25, PDF p158/pr147]`. The 19,679 difference is not a
   discontinued-operations amount and is unexplained on either page — the FY2025 AR also restates the
   FY2024 working-capital line from 2,25,713 to 2,25,714 while restating direct taxes paid 17,391 →
   17,351. **Open item for W3_notes.**
7. **FY2019 total equity restated 2,93,569 → 2,92,856; FY2020 total assets 4,47,591 → 4,47,577;
   FY2021 trade receivables 8,757 → 8,732.** All small, all real, all unexplained by any note.
8. **FY2021 carried a one-off balance-sheet caption, "Share Application Money Pending Allotment"
   1,417** `[AR FY2021, Consolidated Balance Sheet, PDF p145/pr140]`. It is why FY2021 was the only year
   whose balance sheet failed the equity-plus-liabilities identity before this row was accounted for; it
   is not carried as a CSV row because it exists in one year only.

---

## 2. What the FY2026 revenue note actually contains — correcting one line of the record layer

`records/revenue_disaggregation.md` states that its figures are standalone-from-MD&A because no audited
disaggregation exists, and cites `[AR FY2026, Consolidated P&L, Note 22, PDF p164]`. Two corrections:

1. **Note 22 is at PDF p211 / printed 200, not p164** — p164 is the P&L face. The docmap has it right.
2. **The audited consolidated Note 22 does carry a four-way service-line split that sums exactly**,
   and it was not used. It is not an Ind AS 115 disaggregation-of-revenue disclosure — the docmap's §6
   #8 finding stands, there is no contract-asset, contract-liability or remaining-performance-obligation
   note anywhere — but it is an audited product split and it outranks the MD&A under §5:

   `3,79,499 + 51,903 + 17,142 + 34,851 = 4,83,395` `[AR FY26, Note 22, PDF p211/pr200]`

   with twelve named sub-lines beneath — including *Annual subscription and processing fees 4,594*,
   *Auction charges 60*, *Data services 6,763*, *Index services 3,661* and *Other fees 2,620*, none of
   which the MD&A names. The MD&A's unnamed residual of 2,620 (0.59% of standalone revenue) that
   `revenue_disaggregation.md` marks `NOT-DISCLOSED` **equals the consolidated note's *Other fees* line
   of 2,620 exactly**; the match is arithmetic, not asserted by the company, and W3_revenue should test
   it against the standalone Note 22 `[AR FY26, Standalone Note 22, PDF p285/pr274]` before relying on
   it. **W3_revenue should build from consolidated Note 22, and use the MD&A only for the
   equity-derivatives-versus-cash split, which the audited note genuinely does not give.**

---

## 3. The cash-flow float question — RESOLVED, and the answer is yes

**Question:** BSE consolidates Indian Clearing Corporation Limited. Member deposits, margin money and
settlement obligations move through group cash. Can own-account operating cash be separated?

**Answer: yes, to within 0.04% on FY2026, and the company gives every input needed. It is separable on
the balance sheet as a TRACED fact, and separable in the cash flow statement as an ESTIMATE with one
declared assumption. The 1.264 (now 1.269) headline conversion ratio is float-inflated, and on an
own-account basis the last three years convert at 0.94 — below one.**

### 3.1 Why it is separable — three disclosures the company actually makes

**(a) The liability side is split three ways, by name, in Note 16.**

| Note 16, current (₹ lakh) | FY2023 | FY2024 | FY2025 | FY2026 |
|---|---|---|---|---|
| **(A) Owned** | 20,539 | 21,060 | 23,291 | 24,992 |
| **(B) Earmarked** | 32,461 | 41,386 | 35,024 | 26,004 |
| **(C) Clearing and settlement** | **1,49,802** | **3,58,165** | **3,31,172** | **3,55,423** |
| Total | 2,02,802 | 4,20,611 | 3,89,487 | 4,06,419 |

`[AR FY26, Note 16, PDF p206/pr195]` and `[AR FY24, Note 16, PDF p202/pr196]`. Bucket (C) is member and
clearing-bank money: *Deposit and margins from members 2,06,976*, *Others 87,714*, *Settlement
obligation payable 42,357*, *Deposit from clearing banks 18,376* at FY2026.

**(b) The asset side is split the same way in Notes 11 and 12** — every bank line is labelled *Owned*,
*Earmarked – others*, *Earmarked – SGF* or *Earmarked – IPF*, and Note 12.1 states plainly that the
earmarked balances are restricted and *"all other cash and bank balances are available for the operating
activities of the Group"* `[AR FY26, Note 12.1, PDF p202/pr191]`.

| Consolidated liquid funds (₹ lakh) | FY2024 | FY2025 | FY2026 |
|---|---|---|---|
| **Owned** (cash + deposits + accrued interest) | **1,41,528** | **1,67,486** | **3,08,596** |
| Earmarked (others + SGF + IPF) | 4,89,249 | 4,68,109 | 5,00,657 |
| Total (ties to Notes 11 + 12) | 6,30,777 | 6,35,595 | 8,09,253 |

`[AR FY26, Notes 11 & 12, PDF p200-202/pr189-191]`, `[AR FY25, Notes 11 & 12, PDF p187-188/pr176-177]`.
The tie-out is exact in all three years — for FY2026,
`11,304 + 1,57,007 + 1,40,285 = 3,08,596` owned and `1,55,712 + 1,93,114 + 1,51,688 = 5,00,657`
earmarked, together `8,09,253` = `1,67,159 + 3,50,121 + 2,91,973` read off the balance sheet and Note 11.

**(c) The two sides cross-check.** Earmarked-*others* bank assets (i.e. excluding the Core SGF and IPF
pools) against Note 16 buckets (B) + (C):

| ₹ lakh | FY2024 | FY2025 | FY2026 |
|---|---|---|---|
| Earmarked-others assets | 4,09,809 | 3,68,635 | 3,82,349 |
| Note 16 (B) + (C) liabilities | 3,99,551 | 3,66,196 | 3,81,427 |
| Excess assets | 10,258 | 2,439 | **922** (0.24%) |

That is a genuine two-sided tie, and it is what makes the separation trustworthy rather than assumed.

### 3.2 Why the headline CFO is still contaminated — the two footnotes that say exactly what is excluded

The FY2026 consolidated cash flow carries `[AR FY26, Consolidated Cash Flow, PDF p166/pr155]`:

> 2. Movement in earmarked liabilities and corresponding assets of **parent company** are not considered.
> 3. Movement in **Core Settlement Guarantee Fund** liabilities and related assets of **subsidiary
>    companies** are not considered.

Read them for what they omit. The parent's earmarked pool and the subsidiaries' Core SGF are stripped.
**ICCL's clearing-and-settlement float — bucket (C), 3,55,423 lakh, 87.5% of the whole liability — is
not mentioned and is not stripped.** It runs through the operating section, inside a single aggregated
working-capital line, while the fixed deposits that hold the same money run through *investing*.

Reconciliation of that line, FY2026 (§4a trigger 3 — an exact tie-out gating a conclusion):

`Δ(A) 1,701 + Δ(C) 24,251 + Δ Note 19 other liabilities 46,865 + Δ non-current OFL (21) = 72,796`
against the reported *"Increase / (decrease) in other liabilities and other financial liabilities"* of
**72,767** — **residual 29 lakh, 0.04%** `[AR FY26, Consolidated Cash Flow, PDF p165/pr154]`.
Bucket (B) is absent from the sum, exactly as footnote 2 says it should be.

Same test on FY2025 as first reported: `2,231 − 26,993 + 440 − 11 = −24,333` against a reported
−25,155, residual 822 (3.3%) `[AR FY25, Consolidated Cash Flow, PDF p158/pr147]`.

### 3.3 The separated series — FY2024 to FY2026

| ₹ lakh | FY2024 | FY2025 | FY2026 |
|---|---|---|---|
| Reported CFO (continuing) | 2,84,203 | 41,015 | 3,10,368 |
| **less** Δ Note 16 bucket (C) | **(2,08,363)** | **26,993** | **(24,251)** |
| **Own-account CFO** | **75,840** | **68,008** | **2,86,117** |
| PAT (continuing operations) | 77,166 | 1,31,706 | 2,47,530 |
| **Own-account CFO / PAT** | **0.98** | **0.52** | **1.16** |
| Headline CFO / PAT | 3.68 | 0.31 | 1.25 |

`2,84,203 − 2,08,363 = 75,840` · `41,015 − (−26,993) = 68,008` · `3,10,368 − 24,251 = 2,86,117`

Three-year cumulative: own-account `75,840 + 68,008 + 2,86,117 = 4,29,965` against PAT
`77,166 + 1,31,706 + 2,47,530 = 4,56,402` → **0.942**. Headline: `6,35,586 / 4,56,402 = 1.393`.

**FY2024 is the year the distinction decides something.** Its reported CFO of 2,84,203 lakh included
**2,08,363 lakh — 73.3% of it — of clearing-member float that arrived because bucket (C) went from
1,49,802 to 3,58,165 in twelve months.** Strip it and FY2024 converted at 0.98, not 3.68.

Note on basis: FY2024's own cash flow has no continuing/discontinued split, so its 2,84,203 and 77,166
are both total-operations; the FY2025 AR restates them to 2,64,435 and 76,870 (see §1.7 #6). The
discontinued amounts are 89 and 296 lakh, immaterial to the ratio.

### 3.4 Where this leaves the record layer

Four TRACED rows were added to `balance_cash_10y.csv` so any later wave can re-derive this without
re-reading the notes: `ofl_owned_current`, `ofl_earmarked_current`, `ofl_clearing_settlement_current`
(FY2023–FY2026) and `liquid_funds_owned` / `liquid_funds_earmarked` (FY2024–FY2026). The **derived**
own-account CFO series is deliberately **not** in the CSV — it is an `ESTIMATE`, and an estimate in a
machine-read record file reads as a fact. It lives in the chain record at §4, chain 8.

### 3.5 What is still NOT disclosed

- **The working-capital line is never disaggregated by the company.** The 72,767 is one number covering
  Notes 16 and 19 together. My reconciliation closes to 29 lakh, but the company does not publish it.
  `-> AR FY26 gives no supporting schedule to the consolidated cash-flow working-capital lines; a
  disaggregated statement of changes in member obligations would answer it.`
- **The pre-FY2023 bucket split.** Note 16's Owned / Earmarked / Clearing-and-settlement presentation was
  read for FY2023–FY2026. Extending the separation to a ten-year series requires the same note in
  FY2017–FY2022 (Note 16 in FY2018–FY2022, Note 18 in FY2017 — page references in `W1_docmap.md` §4).
  **Until that is done, no ten-year own-account conversion ratio may be quoted.**
- **Average or peak margin balances.** Only the March 31 point is given, so whether FY2026's 3,55,423 is
  a normal level or a settlement-date artefact cannot be established from the annual report.

---

## 4. Chain records — FY2026

Format per `state/TEMPLATES.md`. Eight links, each in a declared state. `->` after a `NOT-DISCLOSED`
names the document that would answer it. `DERIVED` shows its arithmetic inline.

### CHAIN: Revenue from operations (consolidated) | FY26
L1 REPORTED   TRACED | 4,83,395 lakh against 2,95,734 prior year, +63.5% (4,83,395 − 2,95,734 = 1,87,661); unit "` in Lakhs"; single face line referencing Note 22 | [AR FY26, Consolidated P&L, PDF p164/pr153]
L2 COMPONENTS TRACED | Trading services 3,79,499 + Listing services 51,903 (listing fees 38,871, book building 10,412, other fees 2,620) + Treasury income from clearing and settlement funds 17,142 + Other operating income 34,851 (colocation and connectivity 17,109, annual subscription and processing 4,594, data services 6,763, index services 3,661, software solutions 2,664, auction 60) = 4,83,395, zero residual | [AR FY26, Note 22, PDF p211/pr200]
L3 DRIVER     TRACED | index-options premium turnover: options premium ADT `19,523 crore against `8,978 crore, +117.4%; equity cash ADT `7,950 crore against `7,766 crore, +2.4%; standalone derivative transaction charges 3,13,437 against 1,41,554 (+121.4%) while equity cash charges fell 18% to 25,021 | [AR FY26, MD&A, PDF p58/pr47] and [AR FY26, MD&A, PDF p75/pr64]
L4 COUNTERPARTY NOT-DISCLOSED | only geography is published — within India 5,08,140, outside India 6,670 of total income; no member, client-category, top-customer or related-party concentration for revenue -> AR FY26 Note 39.2 (PDF p228/pr217) gives geography only, and the docmap confirms zero Ind AS 115 disaggregation, contract-asset or contract-liability disclosure in FY2024, FY2025 or FY2026; SEBI member-wise turnover data would answer it
L5 RECOGNITION TRACED | Ind AS 115. Transaction charges at a point in time as the transaction occurs; listing, membership and index services straight-line over the period; book building at a point in time on completion; colocation over the contract period; technology services over the service period, third-party software recognised gross. No policy change disclosed between FY2025 and FY2026 | [AR FY26, Note 2.3.10, PDF p176-177/pr165-166]
L6 BALANCE-SHEET BROKEN | gross trade receivables 65,109 against 34,802, +87.1%, versus revenue +63.5%; unbilled receivables 50,637 against 22,184, +128.3%, now 77.8% of the gross book against 63.7% a year earlier; impairment allowance 9,793 against 6,024 with 4,025 charged in the year; every bucket beyond one year carries a 100% expected loss rate | [AR FY26, Note 10 and 10.5, PDF p199/pr188]
L7 CASH       DERIVED | revenue converts through CFO net of the receivable build: the cash flow carries "Decrease / (increase) in trade receivables (30,595)"; 4,83,395 − 30,595 = 4,52,800, i.e. 4,52,800 / 4,83,395 = 93.7% of the year's revenue reached cash or was already collected | [AR FY26, Consolidated Cash Flow, PDF p165/pr154]
L8 SUSTAIN    DERIVED | one product carries it: standalone equity-derivative transaction charges 3,13,437 / consolidated revenue 4,83,395 = 64.8%, and all transaction charges 3,79,499 / 4,83,395 = 78.5%. The condition for repetition is that index-options premium turnover holds and that SEBI's derivative position, expiry-day and lot-size framework is unchanged — not a forecast, a condition | [AR FY26, Note 22, PDF p211/pr200]
CHAIN-STATE: BROKEN at L1/L6

> The break is the doctrine's §2c pattern 3, L6 outrunning L1: revenue +63.5%, gross receivables +87.1%,
> unbilled +128.3%. Sizing for W3: the unbilled increase alone is `50,637 − 22,184 = 28,453` lakh, 15.2%
> of the year's revenue increase of 1,87,661. Recorded, not interpreted.

### CHAIN: Investment income | FY26
L1 REPORTED   TRACED | 29,030 against 25,470, +14.0% (29,030 − 25,470 = 3,560); Note 23 | [AR FY26, Consolidated P&L, PDF p164/pr153]
L2 COMPONENTS TRACED | interest on bank deposits at amortised cost 14,448 + interest on debt instruments at amortised cost 5,706 + dividend from mutual funds 1 + net gain on financial assets at FVTPL 8,875 = 29,030, zero residual; prior year 10,473 + 8,024 + 1 + 108 + 6,864 = 25,470 | [AR FY26, Note 23, PDF p211/pr200]
L3 DRIVER     ESTIMATE | own-account corpus times yield. Average owned liquid funds (3,08,596 + 1,67,486) / 2 = 2,38,041; cash-flow interest income 20,154; 20,154 / 2,38,041 = 8.47%. Assumption: all P&L interest arises on owned funds, none on earmarked funds — supported by policy 2.3.12, which credits Core SGF investment income directly to the fund, and by Note 16.4, which books income earned on earmarked amounts as a liability (8,896) rather than as income. Range: if a tenth of the interest arose on earmarked balances the implied own yield falls to 7.6% | [AR FY26, Consolidated Cash Flow, PDF p165/pr154] and [AR FY26, Note 16, PDF p206/pr195]
L4 COUNTERPARTY TRACED | bank fixed deposits plus mutual funds, government securities, state development loans, bonds, non-convertible debentures and ETFs listed issuer by issuer in Note 9; no investment income from any related party appears in Note 36 | [AR FY26, Note 9, PDF p190-198/pr179-187]
L5 RECOGNITION TRACED | policy 2.3.4 Investment income and interest expense: effective-interest-rate recognition on amortised-cost assets, fair-value movements on FVTPL assets through profit or loss. 8,875 of the 29,030 is fair-value movement and disposal gain on FVTPL assets, not contractual yield | [AR FY26, Note 2.3.4, PDF p174/pr163]
L6 BALANCE-SHEET TRACED | the corpus behind it: other investments 95,542 non-current + 2,34,501 current = 3,30,043 against 82,404 + 1,52,084 = 2,34,488; owned bank deposits 1,37,461 non-current + 1,51,346 current against 16,439 + 1,40,194 | [AR FY26, Consolidated Balance Sheet, PDF p163/pr152] and [AR FY26, Notes 11 and 12, PDF p200-202/pr189-191]
L7 CASH       DERIVED | investment income is removed from CFO entirely — interest income (20,154), FVTPL gain (8,875) and dividend (1) are all deducted as adjustments — and reappears in investing as interest received 23,798 and dividend received 1. Cash exceeded accrual: 23,798 − 20,154 = 3,644, because accrued interest on owned deposits fell from 7,886 + 325 = 8,211 to 5,661 + 2,824 = 8,485 while large FY2025 deposits matured | [AR FY26, Consolidated Cash Flow, PDF p165/pr154]
L8 SUSTAIN    DERIVED | split the line before repeating it: 8,875 / 29,030 = 30.6% is mark-to-market and disposal gain and is not a repeatable yield; the interest half, 20,154 / 29,030 = 69.4%, repeats only while the owned corpus stays at 3,08,596 and deposit rates hold. The corpus itself is the FY2026 own-account cash build, so this line is downstream of §3 | [AR FY26, Note 23, PDF p211/pr200]
CHAIN-STATE: TRACED

### CHAIN: Regulatory contribution | FY26
L1 REPORTED   TRACED | 64,969 against 41,046, +58.3% (64,969 − 41,046 = 23,923); Note 27 | [AR FY26, Consolidated P&L, PDF p164/pr153]
L2 COMPONENTS TRACED | SEBI regulatory fees 56,616 + contribution to investors' service fund 5,386 + contribution to SEBI 2,688 + contribution to investors' protection fund 279 = 64,969, zero residual; SEBI regulatory fees alone are 56,616 / 64,969 = 87.1% of the line and 56,616 − 33,141 = 23,475 of the 23,923 increase, i.e. 98.1% of it | [AR FY26, Note 27, PDF p212/pr201]
L3 DRIVER     TRACED | turnover-assessed levies. SEBI regulatory fees +70.8% (56,616 against 33,141) against options premium ADT +117.4% and consolidated revenue +63.5%; the other three components moved 6.3%, 4.6% and 4.1% and are activity-independent | [AR FY26, Note 27, PDF p212/pr201] and [AR FY26, MD&A, PDF p58/pr47]
L4 COUNTERPARTY TRACED | SEBI (regulatory fees and annual contribution), the Investors' Service Fund and the Investor Protection Fund. All statutory counterparties; none is a related party under Ind AS 24 and none appears in Note 36 | [AR FY26, Note 27, PDF p212/pr201] and [AR FY26, Note 36, PDF p223-227/pr212-216]
L5 RECOGNITION TRACED | the line was INSERTED in FY2025 as consolidated Note 28 and did not exist in FY2024. What it replaced, exactly: FY2024's separate P&L face line "Provision for SEBI regulatory fee" 16,977 (Note 46) plus four lines that sat inside FY2024's Note 28 Administration and other expenses — investors service fund 4,177, contribution to SEBI 2,083, investors' protection fund 218, SEBI regulatory fees 235. The tie is exact: 16,977 + 235 = 17,212 = the FY2025 AR's restated FY2024 "SEBI regulatory fees", and 17,212 + 4,177 + 2,083 + 218 = 23,690 = the restated FY2024 total | [AR FY24, Note 28, PDF p208-209/pr202-203] and [AR FY25, Note 28, PDF p196/pr185]
L6 BALANCE-SHEET TRACED | the line used to leave a provision and no longer does: "Provision for SEBI regulatory fee" 16,977 at FY2024 and 5,444 at FY2025 inside Note 17; FY2026's Note 17 current provisions are employee benefits only — compensated absences 2,463 + gratuity 1,279 = 3,742, with no SEBI-fee provision at all. The FY2025 5,444 was reclassified into other current liabilities in the FY2026 comparative (42,503 restated to 47,947) | [AR FY25, Note 17, PDF p191/pr180] and [AR FY26, Note 17, PDF p207/pr196]
L7 CASH       NOT-DISCLOSED | there is no separate cash-flow line; the charge enters CFO inside "Increase / (decrease) in other liabilities and other financial liabilities" +72,767 by way of statutory remittances, which rose from 29,843 to 74,780 in Note 19 — but that 74,780 also holds `51,478 lakh of Securities Transaction Tax collected for the tax authorities on the standalone, so the SEBI-fee cash cannot be isolated -> AR FY26 Note 19 gives "Statutory remittances" as a single figure with no sub-schedule; a break-up of statutory remittances, or a SEBI-fee payment schedule, would answer it
L8 SUSTAIN    DERIVED | recurring and near-proportional to revenue: 64,969 / 4,83,395 = 13.4% against 41,046 / 2,95,734 = 13.9%. It repeats at 13-14% of revenue for as long as SEBI's fee scale is unchanged, and it is not a margin story — it scales with the same turnover that drives L3 of the revenue chain | [AR FY26, Note 27, PDF p212/pr201]
CHAIN-STATE: TRACED

> One residual is not disclosed. Carving the five lines out of FY2024's admin expenses gives
> `33,884 − 4,177 − 2,083 − 218 − 235 − 9,170 = 18,001`, against a restated 16,758 — a **1,243 lakh
> residual** the FY2025 AR does not explain, attributable to the discontinued operation and to
> regrouping (FY2024's note had no *printing and stationery*, *property taxes* or *repairs to other
> assets* lines and the FY2025 restatement creates all three). For W3_notes.

### CHAIN: Clearing and settlement expense | FY26
L1 REPORTED   TRACED | 28,035 against 34,805, −19.4% (28,035 − 34,805 = −6,770), in a year consolidated revenue rose 63.5%. Face line with NO note reference in FY2024, FY2025 or FY2026, and no note of that title exists in any of the nine years | [AR FY26, Consolidated P&L, PDF p164/pr153]
L2 COMPONENTS BROKEN | no consolidated note exists, so the only break-up obtainable is the standalone-to-consolidated bridge. BSE Limited standalone charge 37,191 against 38,967 (−4.6%), of which paid to its own subsidiary ICCL 12,607 against 7,111 (+77.3%) and eliminated on consolidation; BSE Limited external 37,191 − 12,607 = 24,584 against 38,967 − 7,111 = 31,856 (−22.8%); other group entities' external cost 28,035 − 24,584 = 3,451 against 34,805 − 31,856 = 2,949 | [AR FY26, Standalone P&L, PDF p250/pr239] and [AR FY26, Standalone Note 35, PDF p298/pr287]
L3 DRIVER     BROKEN | management's stated driver is "structural efficiency" on a 5% decline; the consolidated line fell 19.4%. Of the 6,770 consolidated fall, 5,496 — 81.2% — is the increase in the intra-group ICCL charge that eliminates on consolidation, not a reduction in what the group pays outside itself. The MD&A quotes only the standalone figure and does not mention the elimination | [AR FY26, MD&A, PDF p76/pr65]
L4 COUNTERPARTY TRACED | Indian Clearing Corporation Limited, a 100%-held subsidiary and a related party, took 12,607 of the standalone 37,191 = 33.9%, against 7,111 of 38,967 = 18.2% a year earlier. The balance goes to clearing corporations and clearing banks outside the group and is not named anywhere in either block | [AR FY26, Standalone Note 35, PDF p298/pr287]
L5 RECOGNITION NOT-DISCLOSED | no accounting policy addresses clearing and settlement expense; consolidated Note 2.3 runs 2.3.1 to 2.3.17 with no such paragraph, and the revenue policy 2.3.10 covers the income side of clearing and settlement services but not the cost side -> AR FY26 consolidated Note 2 (PDF p169-180/pr158-169) contains no clearing-and-settlement expense policy; a dedicated expense note, which the docmap records as absent in all nine years, would answer it
L6 BALANCE-SHEET TRACED | leaves trade payables 12,271 + 816 = 13,087 against 11,188 + 208 = 11,396, +14.8%, and the MD&A attributes the standalone rise to "higher clearing-related payables consistent with elevated transaction volumes" — a payable growing 14.8% behind an expense line falling 19.4% | [AR FY26, Consolidated Balance Sheet, PDF p163/pr152] and [AR FY26, MD&A, PDF p77/pr66]
L7 CASH       TRACED | no dedicated cash-flow line; the item converts through "Increase / (decrease) in trade payables" +1,691 in the working-capital block, against −7,890 in FY2025 | [AR FY26, Consolidated Cash Flow, PDF p165/pr154]
L8 SUSTAIN    DERIVED | the cost ratio halved in one year: 28,035 / 4,83,395 = 5.8% of consolidated revenue against 34,805 / 2,95,734 = 11.8%. On the standalone the same ratio is 37,191 / 4,46,951 = 8.3% against 38,967 / 2,60,643 = 15.0%. Repetition depends on the clearing mix staying in-house — a group-structure choice under SEBI's interoperability framework, not an external price | [AR FY26, Consolidated P&L, PDF p164/pr153] and [AR FY26, MD&A, PDF p76/pr65]
CHAIN-STATE: BROKEN at L2/L3

> This is the §1a-i asymmetry the brief flagged, and it has a counter-proportion. Consolidated
> clearing cost **−19.4%** against consolidated revenue **+63.5%** is one share; the standalone
> **−4.6%** against standalone revenue **+71%** is the other, and the difference between them is the
> **+77.3%** intra-group charge that never reaches the consolidated P&L. Neither share alone says it.
> The absolute size of the divergence is `5,496` lakh, 1.7% of FY2026 PBT (`5,496 / 3,29,914 = 1.7%`).

### CHAIN: Contribution to core settlement guarantee fund | FY26
L1 REPORTED   TRACED | 7,696 against 9,000, −14.5% (7,696 − 9,000 = −1,304). Presented BELOW the subtotal "Profit before contribution to core settlement guarantee fund" 3,31,068 and therefore OUTSIDE total expenses 1,83,742; no note number on the face. This subtotal first appeared in FY2025; FY2024 had no such line and the contribution sat inside administration and other expenses | [AR FY26, Consolidated P&L, PDF p164/pr153]
L2 COMPONENTS NOT-DISCLOSED | the 7,696 is not split by clearing corporation or by segment. What is split is the accumulated FUND: ICCL Core SGF 1,23,264 by segment (equity derivative 96,432, equity 22,032, commodity derivative 1,762, currency derivative 1,538, EGR 1,265, debt 233, SLB 2) and by contributor (ICCL 60,896, BSE 17,952, NSE 26,529, MSE 934, other 16,953), plus India ICC 1,419, giving the balance-sheet caption 1,23,264 + 1,419 = 1,24,683 -> AR FY26 Notes 41 and 42 (PDF p231-232/pr220-221) give the fund balance, not the year's contribution by segment; a segment-wise contribution table, or ICCL's own SEBI monthly stress-test filing, would answer it
L3 DRIVER     TRACED | SEBI's Minimum Required Contribution, computed from monthly stress-test values, not from turnover. Under IFSCA (MII) Regulations 2021 the India ICC fund must equal the greater of the stress-tested minimum corpus or USD 1 million. Contribution once made is non-refundable even if the corpus later exceeds the MRC | [AR FY26, Note 2.3.12, PDF p178/pr167] and [AR FY26, Note 42, PDF p232/pr221]
L4 COUNTERPARTY TRACED | the group's own clearing corporations — Indian Clearing Corporation Limited and India International Clearing Corporation (IFSC) Limited, both subsidiaries. The ICCL fund also holds contributions from competing exchanges that clear through it: NSE 26,529 and MSE 934, together 27,463 of the 1,23,264 corpus = 22.3% | [AR FY26, Note 41, PDF p231-232/pr220-221]
L5 RECOGNITION TRACED | policy 2.3.12: expensed in the period contributed, never reversed. Income earned on the fund's investments and fines recovered from members are credited directly to the fund balance and never pass through the profit and loss account. The fund is presented as its own caption between equity and liabilities, so it is neither equity nor a liability on the face | [AR FY26, Note 2.3.12, PDF p178/pr167]
L6 BALANCE-SHEET DERIVED | the fund grew 1,24,683 − 1,13,260 = 11,423 (+10.1%) on a P&L charge of only 7,696; the 11,423 − 7,696 = 3,727 difference is fund investment income and member penalties credited straight to the fund under policy 2.3.12 and never seen in the P&L. Matching earmarked-SGF assets: non-current deposits 27,078 + current deposits 85,037 + accrued interest 544 + 5,454 + current account 143 = 1,18,256, leaving 1,24,683 − 1,18,256 = 6,427 held in prescribed securities inside Note 9 and not separately labelled | [AR FY26, Consolidated Balance Sheet, PDF p163/pr152] and [AR FY26, Notes 11 and 12, PDF p200-202/pr189-191]
L7 CASH       TRACED | the FY2026 cash flow does NOT add the contribution back — footnote 3 excludes Core SGF movements — so CFO 3,10,368 is net of the 7,696. In FY2024 and in every year back to FY2017 the same item WAS added back as a non-cash adjustment (FY2024 +9,170, FY2022 +2,905, FY2017 +952), so CFO in those years was gross of it. The two presentations are not comparable and no note bridges them | [AR FY26, Consolidated Cash Flow, PDF p166/pr155] and [AR FY24, Consolidated Cash Flow, PDF p158/pr152]
L8 SUSTAIN    DERIVED | recurring but explicitly not turnover-proportional: 7,696 / 4,83,395 = 1.6% of revenue against 9,000 / 2,95,734 = 3.0%, and it fell 14.5% in a year revenue rose 63.5% precisely because the MRC is a stress-test output. The condition for it staying small is that ICCL's stress-tested exposure does not step up with derivative open interest; the ten-year series in trend_10y.csv ranges from 74 (FY2020) to 9,170 (FY2024), so it is volatile by nature | [AR FY26, Note 2.3.12, PDF p178/pr167]
CHAIN-STATE: TRACED

### CHAIN: Share of net profit of associates | FY26
L1 REPORTED   TRACED | 6,542 against 8,259, −20.8% (6,542 − 8,259 = −1,717), sitting between "Profit before tax and share of net profits" 3,23,372 and "Profit before tax" 3,29,914 | [AR FY26, Consolidated P&L, PDF p164/pr153]
L2 COMPONENTS DERIVED | CDSL 6,842 + EBIX Insurance Broking 66 + Hindustan Power Exchange 104 + BSE E-Agricultural Markets 20 + Countrywide Commodity Repository (58) + EBIX Insuretech (1) + India International Bullion Holding (432) = 6,541 against a reported 6,542; residual 1 is rounding. Prior year the same roll-forwards sum exactly: 7,900 + 145 − 31 − 115 + 25 + 241 + 240 − 146 = 8,259 | [AR FY26, Note 8, PDF p188-189/pr177-178]
L3 DRIVER     DERIVED | one associate is the line: CDSL 6,842 / 6,542 = 104.6% of it, with the other six netting to −300. The move is CDSL's own earnings, not a stake change — 6,842 against 7,900 is −13.4% on an unchanged holding of 3,13,50,000 shares in both years. The second-largest mover is India International Bullion Holding, from +240 to −432, a 672 swing | [AR FY26, Note 8, PDF p188-189/pr177-178]
L4 COUNTERPARTY TRACED | Central Depository Services (India) Limited, a listed associate, 3,13,50,000 shares, 15% held, a related party under Ind AS 24. Trading balances with it are trivial — payable 38 at year end against 2, and the group's CDSL-related receivable is 5 | [AR FY26, Note 36, PDF p223-227/pr212-216] and [AR FY26, BRSR Section A.23(a), PDF p110/pr99]
L5 RECOGNITION TRACED | equity method at cost plus share of post-acquisition results. Carrying value of quoted associate investments 44,940 against an aggregate market value of 3,50,932 — an unrecognised 3,50,932 − 44,940 = 3,05,992 that never enters the balance sheet under the equity method. One impairment of 100 was taken in FY2026, on BFSI Sector Skill Council of India, fully provided | [AR FY26, Note 8, PDF p188/pr177]
L6 BALANCE-SHEET DERIVED | investments in associates 53,657 against 50,053. The CDSL roll-forward closes exactly: opening 41,949 + share of profit 6,842 + share of OCI 68 − dividend received 3,919 = 44,940 | [AR FY26, Note 8, PDF p189/pr178]
L7 CASH       NOT-DISCLOSED | the P&L amount is a non-cash add-back — the cash flow deducts "Share of net profit of associates (6,542)" from CFO in full — and the only cash is the 3,919 dividend recorded in the Note 8 roll-forward. That 3,919 cannot be located in the consolidated cash flow statement, whose investing section shows only "Dividend received 1" and "Investments in associates -" -> AR FY26 consolidated cash flow (PDF p165/pr154) has no dividend-from-associate line; a reconciliation of investing cash flows to Note 8, or the standalone Note 23 investment-income break-up, would answer it
L8 SUSTAIN    DERIVED | the line is shrinking as a share of earnings: 6,542 / 3,29,914 = 2.0% of PBT against 8,259 / 1,74,827 = 4.7%, because the parent's own profit tripled while the associate's fell. It repeats only if CDSL's earnings recover; the six non-CDSL associates net to −300 and have never contributed positively in aggregate in either of the two years read | [AR FY26, Note 8, PDF p188-189/pr177-178] and [AR FY26, Consolidated P&L, PDF p164/pr153]
CHAIN-STATE: TRACED

### CHAIN: Other financial liabilities (current) | FY26
L1 REPORTED   TRACED | 4,06,419 against 3,89,487, +4.3% (4,06,419 − 3,89,487 = 16,932). It is 4,06,419 / 5,37,049 = 75.7% of total current liabilities and 4,06,419 / 6,79,550 = 59.8% of total equity; Note 16 | [AR FY26, Consolidated Balance Sheet, PDF p163/pr152]
L2 COMPONENTS TRACED | Owned (A) 24,992 + Earmarked (B) 26,004 + Clearing and settlement (C) 3,55,423 = 4,06,419, zero residual. Within (C): deposit and margins from members 2,06,976, others 87,714, settlement obligation payable 42,357, deposit from clearing banks 18,376. Within (B): 1%-of-public-issue deposits from companies 6,213, recovery expense fund 5,625, withheld liabilities 2,969, defaulters' liabilities 1,555, other deposits from companies 746, income earned on earmarked amounts 8,896 | [AR FY26, Note 16, PDF p206/pr195]
L3 DRIVER     TRACED | member margin set by ICCL's risk model on open positions, plus the settlement cycle open at the reporting date. The two move in opposite directions: settlement obligation payable 1,594 to 42,357, +40,763, purely a March-31 cycle position, while deposit and margins from members FELL 2,24,870 to 2,06,976, −7.96%, in a year when options premium turnover rose 117.4% | [AR FY26, Note 16, PDF p206/pr195] and [AR FY26, MD&A, PDF p58/pr47]
L4 COUNTERPARTY TRACED | clearing members and clearing banks of Indian Clearing Corporation Limited — third-party money the group holds but does not own. Bucket (B) is issuer and defaulter money held under SEBI direction. Only bucket (A), 24,992 of 4,06,419 = 6.1%, is described by the company as owned, and even that includes 10,298 + 5,612 + 1,083 = 16,993 of trading-member and other deposits | [AR FY26, Note 16, PDF p206/pr195]
L5 RECOGNITION TRACED | policies 2.3.1 Financial instruments and 2.3.2 Earmarked funds. Notes 16.2 and 16.3 state that bank balances and deposits are earmarked against the (B) liabilities; Note 12.1 states the earmarked cash and bank balances are restricted to specified purposes and that all other cash and bank balances are available for the Group's operating activities | [AR FY26, Note 2.3.2, PDF p173/pr162] and [AR FY26, Note 12.1, PDF p202/pr191]
L6 BALANCE-SHEET DERIVED | the matching assets are disclosed and they tie. Earmarked-others bank assets: cash and equivalents 1,55,712 + other bank balances 1,02,571 + non-current deposits and interest 1,24,066 = 3,82,349, against (B) + (C) = 26,004 + 3,55,423 = 3,81,427; excess assets 3,82,349 − 3,81,427 = 922, i.e. 0.24%. FY2025 3,68,635 against 3,66,196, excess 2,439. FY2024 4,09,809 against 3,99,551, excess 10,258 | [AR FY26, Notes 11, 12 and 16, PDF p200-206/pr189-195]
L7 CASH       BROKEN | the liability's movement runs through OPERATING while the asset that holds the same money runs through INVESTING. The increase enters CFO inside "Increase / (decrease) in other liabilities and other financial liabilities" +72,767, which reconciles as delta(A) 1,701 + delta(C) 24,251 + delta Note 19 46,865 + delta non-current OFL (21) = 72,796, residual 29; the deposits sit in investing as "Investment in fixed deposits (3,29,857)" and "Proceeds from fixed deposits 1,74,471". Neither section is labelled as float | [AR FY26, Consolidated Cash Flow, PDF p165/pr154] and [AR FY26, Notes 16 and 19, PDF p206-208/pr195-197]
L8 SUSTAIN    NOT-DISCLOSED | whether 3,55,423 is a normal level or a reporting-date artefact cannot be established: the settlement obligation component alone swung from 13,724 (FY2024) to 1,594 (FY2025) to 42,357 (FY2026) on three single dates -> AR FY26 discloses only the March-31 balance; ICCL's monthly SEBI stress-test filings, or an average / peak margin disclosure, would answer it
CHAIN-STATE: BROKEN at L6/L7

### CHAIN: Own-account operating cash flow | FY26
L1 REPORTED   TRACED | reported CFO from continuing operations 3,10,368 against 41,015, and 2,84,203 in FY2024 on a total-operations basis. Cumulative FY2017 to FY2026, 8,21,693 against cumulative PAT attributable 6,47,456, a headline conversion of 1.269 | [AR FY26, Consolidated Cash Flow, PDF p165/pr154] and [AR FY24, Consolidated Cash Flow, PDF p158/pr152]
L2 COMPONENTS TRACED | the float travels in one aggregated working-capital line, "Increase / (decrease) in other liabilities and other financial liabilities": +72,767 in FY2026, −25,155 in FY2025 as first reported, +2,25,713 in FY2024. That single line covers Note 16 in all three of its buckets and Note 19 together, and the company never disaggregates it | [AR FY26, Consolidated Cash Flow, PDF p165/pr154] and [AR FY24, Consolidated Cash Flow, PDF p158/pr152]
L3 DRIVER     TRACED | Note 16 bucket (C), clearing and settlement: 1,49,802 at FY2023, 3,58,165 at FY2024, 3,31,172 at FY2025, 3,55,423 at FY2026. The FY2024 step of +2,08,363 is the single largest working-capital event in the ten-year series | [AR FY26, Note 16, PDF p206/pr195] and [AR FY24, Note 16, PDF p202/pr196]
L4 COUNTERPARTY TRACED | clearing members and clearing banks of Indian Clearing Corporation Limited; the money belongs to them, not to the group, and Note 12.1 says so of the corresponding assets | [AR FY26, Note 16, PDF p206/pr195] and [AR FY26, Note 12.1, PDF p202/pr191]
L5 RECOGNITION TRACED | cash-flow footnotes 2 and 3 state exactly what is excluded — "Movement in earmarked liabilities and corresponding assets of parent company are not considered" and "Movement in Core Settlement Guarantee Fund liabilities and related assets of subsidiary companies are not considered". Bucket (C), the subsidiary's clearing and settlement float, is named in neither exclusion, and the reconciliation in L7 confirms it does flow through | [AR FY26, Consolidated Cash Flow footnotes 2 and 3, PDF p166/pr155]
L6 BALANCE-SHEET TRACED | the balance-sheet separation is fully disclosed and needs no assumption. Own-account liquid funds 1,41,528 at FY2024, 1,67,486 at FY2025, 3,08,596 at FY2026; earmarked liquid funds 4,89,249, 4,68,109, 5,00,657. Both sides tie to Notes 11 and 12 exactly in all three years | [AR FY26, Notes 11 and 12, PDF p200-202/pr189-191] and [AR FY25, Notes 11 and 12, PDF p187-188/pr176-177]
L7 CASH       ESTIMATE | own-account CFO = reported CFO minus the movement in Note 16 bucket (C): FY2024 2,84,203 − 2,08,363 = 75,840; FY2025 41,015 − (−26,993) = 68,008; FY2026 3,10,368 − 24,251 = 2,86,117. Assumption: the whole of the (C) movement passed through the CFO working-capital line — evidenced by the FY2026 reconciliation residual of 29 on 72,767 (0.04%) and the FY2025 residual of 822 on 25,155 (3.3%). Range: also stripping the member deposits inside bucket (A) moves FY2026 to 3,10,368 − 24,251 − 1,701 = 2,84,416, a 0.6% band | [AR FY26, Consolidated Cash Flow, PDF p165/pr154] and [AR FY26, Note 16, PDF p206/pr195]
L8 SUSTAIN    DERIVED | three-year own-account conversion 75,840 + 68,008 + 2,86,117 = 4,29,965 against PAT 77,166 + 1,31,706 + 2,47,530 = 4,56,402, a ratio of 0.942, against a headline 6,35,586 / 4,56,402 = 1.393. The condition for the headline to keep exceeding one is that member margin keeps growing — a balance-sheet inflow, not an earnings one, and one that reverses when open interest falls, as it did in FY2025 | [AR FY26, Consolidated Cash Flow, PDF p165/pr154] and [AR FY26, Consolidated P&L, PDF p164/pr153]
CHAIN-STATE: BROKEN at L1/L7

> The break is §2c pattern 4 read in reverse. The multi-year cumulative CFO does not diverge downward
> from PAT — it diverges **upward**, and the reason is not earnings quality but a third-party liability
> pool routed through the operating section. FY2024 is the demonstration: `2,08,363 / 2,84,203 = 73.3%`
> of that year's reported operating cash was clearing-member float. Against that counter-proportion,
> the own-account share was 26.7%. Neither number alone says it.

---

## 5. Handover

1. **Use the corrected CSVs, not the earlier ones.** Both now close on all four arithmetic identities in
   all eleven years. `trend_provenance.json` was **not** rewritten and is now partly stale: it records
   sources for 18 of 27 FY2024 P&L cells and none for FY2016 or FY2023, and its FY2017 `cfo` entry
   points at the P&L page. Treat this file's §1.4 and §1.5 as the current change record.
2. **`records/cash_ledger_note.md` still carries 1.264.** The arithmetic is now 1.269 (§1.6) and the
   substantive answer is §3.3 — it is not the number to quote at all.
3. **Three lines in the CSVs are not comparable across a presentation change** and every one is
   quantified above: `regulatory_contribution` (inserted FY2025, §4 chain 3 L5),
   `core_sgf_contribution` (moved below the expense subtotal FY2025, and stopped being a cash-flow
   add-back, §4 chain 5 L7), and the revenue rows (two notes merged into one FY2026, §2).
4. **The extension of §3 backwards to FY2017 is the highest-value open task.** It needs only Note 16 /
   Note 18 read for FY2017–FY2022, at the pages in `W1_docmap.md` §4. Until it is done, ten-year cash
   conversion cannot be stated on an own-account basis.
5. **Open for W3_notes:** the FY2024 CFO restatement of 19,679 with no stated cause (§1.7 #6); the
   1,243 unexplained residual in the FY2024 administration-expense carve-out (§4 chain 3); and the
   3,919 CDSL dividend that Note 8 records as received but the cash flow statement does not show
   (§4 chain 6 L7).
