# W3 — Notes & disclosure forensics: BSE Limited, FY2017–FY2026

Wave 3 artifact (doctrine §7). Scope: every note in FY2024, FY2025 and FY2026 in both blocks, plus the
policy, contingent-liability, lease, guarantee and restatement notes across all nine available years.
FY2023 is absent (GAP-001) and is reachable only as the comparative column inside FY2024.

**Page citations.** Every figure carries `PDF p<n>/pr<n>` using the W1_docmap §0.1 offsets
(FY2017 +2, FY2018 +7, FY2019 +9, FY2020 +7, FY2021 +5, FY2022 +9, FY2024 +6, FY2025 +11, FY2026 +11).
Pages found by grep were resolved against the §0.2 bleed rule before being cited.

**Headline for the reader who stops here.**

1. The unexplained FY2024 CFO restatement **is explained**, and the explanation was hiding in a
   one-line footnote: the FY2025 consolidated cash flow statement **changed its basis of preparation**
   to exclude Core SGF movements of subsidiaries. Four adjustment lines were deleted from the FY2024
   comparative. The change is disclosed; the amount is not, in either report.
2. The ₹10,60,024 lakh guarantee did not collapse — **the disclosure did.** It was ICCL's bank
   guarantee for Inter-CCP collateral under SEBI's interoperability framework. FY2026 **restated the
   FY2025 comparative down to ₹24 lakh**, which is only possible if the group now takes the view that
   it never was a Group contingent liability. The words "bank guarantee" do not occur anywhere in the
   FY2026 annual report.
3. The two largest accounting-standard transitions of the window — **Ind AS 115 and Ind AS 116** —
   were both booked at **zero**, and Ind AS 116 is still being asserted as inapplicable in FY2026
   while the same statements carry a lease liability, a lease-security footnote and an operating-lease
   expense.

---

## 1. ACCOUNTING POLICY CHANGE LOG, FY2017 → FY2026

Ordered chronologically. "Quantified" means the annual report itself states the ₹ effect of the change
on the P&L or balance sheet — not merely that the new number is visible.

| FY | Change | Quantified in the AR? | Source |
|---|---|---|---|
| FY2017 | **Ind AS first-time adoption.** Three-column balance sheet (2017 / 2016 / 1-Apr-2015); full transition reconciliations | **YES** — consolidated Note 4 *"Explanation of transition to Ind AS"*, standalone Note 4.2.1 | `[AR FY2017, Note 4, PDF p134-140/pr132-138]` |
| FY2019 | **Ind AS 115 Revenue from Contracts with Customers**, adopted 1-Apr-2018 on the cumulative-effect method | **YES, and the answer is zero**: *"There was no impact on the adoption of the standard on the financial statements of the Group."* | `[AR FY2019, Note 2(xii), PDF p163/pr154]` |
| FY2019 | **ICCL's Core SGF contribution moved from investment earmarking to a P&L charge.** ₹684 lakh charged in FY2019; ₹2,256 lakh of earlier-year contributions had been *"earmarked from investments and was not charged to Statement of Profit and Loss"* | **YES** — both amounts stated, and prior-year figures and EPS restated | `[AR FY2019, Note 30 fn 2, PDF p202/pr193]` |
| FY2020 | **Ind AS 116 Leases**, effective 1-Apr-2019. A full right-of-use / lease-liability policy was written into Note 2 — and the lease note simultaneously states the standard is not applied | **YES, and the answer is zero**: *"As per the assessment of management, there are no lease contracts for which IND AS 116 – Leases is required to be applied."* | policy `[AR FY2020, Note 2, PDF p172/pr165]`; note `[AR FY2020, Note 32, PDF p214/pr207]` |
| FY2020 | **SEBI plough-back to Investors' Services Fund and Investor Protection Fund.** SEBI concluded a 2005–2017 inspection and instructed a plough-back of ₹1,037 lakh with interest | **YES** — ₹1,385 lakh charged to P&L, further ₹476 lakh for the subsequent period, ₹1,861 lakh provision | `[AR FY2020, Note 36 fn 3, PDF p227/pr220]` |
| FY2022 | **Schedule III amendments** — trade receivable / payable ageing, CWIP and IAUD ageing, analytical ratios, struck-off companies, title deeds. Presentation only | n/a — no P&L or equity effect | first appear FY2022; §6 below records which are still missing |
| FY2024 | **Provision for differential SEBI regulatory fee.** SEBI's 26-Apr-2024 letter re-based the fee to notional option value from 2006-07 with 15% interest. Provided *"based on the prudence"* while contesting | **YES** — ₹16,977 lakh, *"including ₹7,347 lakhs in respect of periods up to March 31, 2023"* | `[AR FY24, Note 46, PDF p233/pr227]`; P&L face `[AR FY24, PDF p157/pr151]` |
| FY2025 | **Regulatory contribution carved out of Administration and other expenses into its own P&L line and note (Note 28)** | **Effectively yes** — the restated FY2024 comparative of ₹23,690 lakh ties exactly to the five FY2024 components (W1_ledger §L5) | `[AR FY25, Note 28, PDF p196/pr185]` |
| FY2025 | **New P&L subtotal *"Profit before contribution to core settlement guarantee fund"***, with the SGF contribution moved below the operating total | **NO** — the FY2024 comparative was re-presented but no note explains the subtotal or its purpose | `[AR FY25, Consolidated P&L, PDF p156/pr145]` |
| **FY2025** | **CONSOLIDATED CASH FLOW STATEMENT CHANGED ITS BASIS OF PREPARATION.** A fourth footnote was inserted: *"Movement in Core Settlement Guarantee Fund liabilities and related assets of subsidiary companies are not considered."* Absent from every earlier year; present FY2025 and FY2026 | **NO** — the footnote is unquantified, and no restatement note exists. This is the whole of RF-027's 19,679 (§2, F-1 below) | `[AR FY25, Consolidated Cash Flow, PDF p159/pr148]` vs `[AR FY24, PDF p159/pr153]` |
| FY2025 | **SEBI's notional-turnover methodology accepted.** After SEBI's 14-Aug-2024 reiteration, *"the Holding Company has appropriately accounted based on the SEBI's advice"* | **PARTIAL** — the resulting expense is visible (₹33,141 lakh) but no reconciliation of contest-to-acceptance, and no statement of the cumulative catch-up | `[AR FY25, Note 46, PDF p217/pr206]` |
| FY2025→FY2026 | **Ind AS 8 change in accounting estimate: building useful life revised to 25 years, effective 1-Apr-2024**, on external valuers' advice, applied prospectively | **YES** — impact ₹13 lakh | `[AR FY26, Note 3 fn 3, PDF p181/pr170]`; first stated `[AR FY25, Note 3, PDF p172/pr161]` |
| FY2026 | **Two revenue notes merged into a single Note 22** with a re-cut service-line taxonomy | **NO** — no bridge from the old lines to the new (RF-004) | `[AR FY26, Note 22, PDF p211/pr200]` |
| FY2026 | **SEBI Regulatory fees note deleted.** Substance absorbed into Note 27 Regulatory contribution alongside ISF, IPF and SEBI contribution | **NO** — see §4.1 | note absent; expense `[AR FY26, Note 27, PDF p212/pr201]` |
| FY2026 | **Contingent-liability "of which remote" grading deleted** after eight consecutive years | **NO** — see §3.2 and F-3 | `[AR FY26, Note 37, PDF p227/pr216]` |
| FY2026 | **Group guarantee disclosure basis changed and the FY2025 comparative restated by ₹10,60,000 lakh** | **NO** — see §3.3 and F-2 | `[AR FY26, Note 37, PDF p227/pr216]` |
| FY2026 | **Liquidity enhancement scheme expense moved off the P&L face into Note 28 Other expenses** | **Implicitly** — the ₹666 lakh FY2025 comparative reappears inside the note | `[AR FY26, Note 28, PDF p213/pr202]` vs `[AR FY25, P&L, PDF p156/pr145]` |

### 1.1 Ind AS 115 — adopted at zero, and never disclosed against

BSE adopted Ind AS 115 on the cumulative-effect method and recorded **no transition adjustment at
all**. The revenue policy text it carried forward is Ind AS 18 vocabulary, not Ind AS 115 vocabulary:
*"Revenue from Annual / monthly fee contracts is recognised ratably over the period of the contract
using the percentage of completion method"* `[AR FY2019, Note 2(xii), PDF p163/pr154]`. Ind AS 115
does not contain a percentage-of-completion method; it contains input and output measures of progress
toward satisfying a performance obligation. That wording survives verbatim into FY2022
`[AR FY2022, Note 2, PDF p166/pr157]`.

The consequence is not the transition entry — a zero transition entry for an exchange billing
transaction charges monthly is defensible. **The consequence is the disclosure package that never
arrived.** W1_docmap §6 #8 established independently that FY2024, FY2025 and FY2026 contain **zero**
occurrences of "disaggregat", "contract asset", "contract liabilit" or "remaining performance
obligation". Ind AS 115.114–115.122 requires all four. Nine years after notification, BSE publishes
none of them, and the FY2026 unbilled receivable of ₹50,637 lakh — 10.5% of revenue — is a contract
asset in everything but name `[AR FY26, Note 10.5, PDF p199/pr188]`.

**Does it break the trend lines?** No. Total income and revenue from operations are continuous across
FY2018/FY2019 on the restated basis; the restatement that does break FY2018/FY2019 is the Core SGF
one (§2), not Ind AS 115.

### 1.2 Ind AS 116 — asserted inapplicable for seven consecutive years, against the company's own numbers

The same sentence appears in the Lease note in **FY2020, FY2024, FY2025 and FY2026**, in both blocks:

> *"As per the assessment of management, there are no lease contracts for which IND AS 116 – Leases is
> required to be applied."*
> `[AR FY2020, Note 32, PDF p214/pr207]` · `[AR FY24, Note 32, PDF p211/pr205]` ·
> `[AR FY25, Note 33, PDF p198/pr187]` · `[AR FY26, Note 32, PDF p216/pr205]`

Set against three things inside the same financial statements:

| Contradicting item | FY2026 | FY2025 | Source |
|---|---|---|---|
| **Lease obligations** (non-current, other financial liabilities) | 2 | 2 | `[AR FY26, Note 16, PDF p206/pr195]` |
| Note 16.1: *"Secured by lease asset. Liability is at a fixed rate of interest with original repayment period of 5 years"* | present | present | `[AR FY26, Note 16.1, PDF p206/pr195]` |
| **Operating lease expenses** (in Other expenses) | 141 | 233 | `[AR FY26, Note 28, PDF p213/pr202]` |
| PPE note 1: *"The Group's obligations under leases are secured by the lessors' title to the leased assets"* | present | present | `[AR FY26, Note 3 fn 1, PDF p181/pr170]` |
| Full right-of-use asset / lease liability accounting policy in Note 2 | present | present | `[AR FY26, Note 2.3.11, PDF p177/pr166]` |

The amounts are small. **The disclosure failure is not.** Ind AS 116.53 requires a lessee to disclose
depreciation on right-of-use assets by class, interest on lease liabilities, short-term and low-value
lease expense, total cash outflow for leases and the carrying amount of ROU assets; Ind AS 116.58
requires a maturity analysis. None of the six exists in any year. And "operating lease expense" is a
caption Ind AS 116 abolished for lessees — it is Ind AS 17 language still running in FY2026.

FY2019 is the year the picture is cleanest: the FY2019 Lease note ran a full **finance-lease** maturity
table with minimum lease payments of ₹4 lakh and a present value of ₹3 lakh
`[AR FY2019, Note 31, PDF p203/pr194]`. The disclosure existed under the old standard, and stopped
under the new one.

**Does it break the trend lines?** No — the amounts are immaterial to any ratio. It is a control and
attention finding, not a measurement finding, which is why it ships at Medium and not High.

---

## 2. RESTATEMENT REGISTER — COMPLETED

The register in `records/restatements.md` (18 detector candidates, 2 verified, several ruled
artifacts) is merged here with W1_ledger §1.7's eight, plus four this wave found. **Nothing from
either source is deleted; where I disagree with an earlier ruling, both positions stand (doctrine
§10).**

Legend: **STATED** — a note gives the reason. **QUANTIFIED** — the note gives the amount of the
restatement. **NEITHER** — the movement is visible only by comparing two reports.

### 2.1 The register

| # | Year restated | Line | As first reported | As restated | Δ | Reason stated? | Quantified? | Source pair |
|---|---|---|---|---|---|---|---|---|
| R-01 | FY2017 | Revenue from operations (consol) | 51,723 | 37,365 | −14,358 | **STATED** — CDSL deconsolidation to discontinued operations, Ind AS 105 | **NO** | `[AR FY2017, PDF p117/pr115]` → `[AR FY2018, PDF p134/pr127]` |
| R-02 | FY2017 | Total income | 80,075 | 61,828 | −18,247 | same | NO | same |
| R-03 | FY2017 | Total expenses | 47,530 | 40,939 | −6,591 | same | NO | same |
| R-04 | FY2017 | CFO (consol) | 81,711 | 77,450 | −4,261 | **NEITHER** | NO | `[AR FY2017, PDF p118/pr116]` → `[AR FY2018, PDF p135/pr128]` |
| **R-05** | **FY2018** | **PAT attributable to shareholders** | **71,128** | **68,872** | **−2,256 (−3.17%)** | **STATED AND QUANTIFIED** — ICCL Core SGF contributions of earlier years, previously earmarked from investments, charged to P&L | **YES, ₹2,256 lakh** | `[AR FY2018, PDF p134/pr127]` → `[AR FY2019, Note 30 fn 2, PDF p202/pr193]` |
| **R-06** | **FY2018** | **Total equity (consol BS)** | **3,13,435** | **3,08,055** | **−5,380 (−1.72%)** | **PARTIAL** — the same Note 30 fn 2 explains ₹2,256 of it; the residual ₹3,124 is unexplained | PARTIAL | `[AR FY2018, PDF p133/pr126]` → `[AR FY2019, PDF p147/pr138]` |
| **R-07** | **FY2018** | **Core settlement guarantee fund (BS caption)** | **29,096** | **35,848** | **+6,752 (+23.2%)** | same partial | PARTIAL | same pair |
| R-08 | FY2018 | Total assets / total equity+liabilities | 4,98,436 | 4,99,808 | +1,372 | **NEITHER** | NO | same pair |
| R-09 | FY2018 | Revenue from operations ↔ Other income | 47,698 / 5,324 | 50,720 / 2,302 | ±3,022 | **NEITHER** — total income unchanged | NO | `[AR FY2018, PDF p134/pr127]` → `[AR FY2019, PDF p148/pr139]` |
| R-10 | FY2019 | Total equity | 2,93,569 | 2,92,856 | −713 | **NEITHER** | NO | `[AR FY2019, PDF p147/pr138]` → `[AR FY2020, PDF p159/pr152]` |
| R-11 | FY2019 | Total expenses | 48,563 | 49,861 | +1,298 | **NEITHER** — the FY2019 exceptional item *Liquidity enhancement scheme 1,298* is the same figure, folded into expenses in the FY2020 presentation | NO | `[AR FY2019, PDF p148/pr139]` → `[AR FY2020, PDF p160/pr153]` |
| R-12 | FY2020 | Total assets | 4,47,591 | 4,47,577 | −14 | **NEITHER** | NO | `[AR FY2020, PDF p159/pr152]` → `[AR FY2021, PDF p145/pr140]` |
| R-13 | FY2021 | Trade receivables | 8,757 | 8,732 | −25 | **NEITHER** | NO | `[AR FY2021, PDF p145/pr140]` → `[AR FY2022, PDF p149/pr140]` |
| R-14 | FY2024 | Revenue from operations | 1,39,003 | 1,37,104 | −1,899 | **STATED** — BSE Institute Limited to discontinued operations (Ind AS 105) plus the Regulatory-contribution carve-out | **NO** | `[AR FY24, PDF p157/pr151]` → `[AR FY25, PDF p156/pr145]` |
| R-15 | FY2024 | Total income | 1,61,790 | 1,59,588 | −2,202 | same | NO | same |
| R-16 | FY2024 | Total expenses | 1,10,082 | 99,040 | −11,042 | same | NO | same |
| R-17 | FY2024 | PAT (continuing) | 77,166 (total ops) | 76,870 continuing + 296 discontinued | reclass, PAT attributable unchanged at 77,839 | STATED | NO | same |
| **R-18** | **FY2024** | **NET CASH FROM OPERATING ACTIVITIES** | **2,84,203** | **2,64,435 continuing + (89) discontinued = 2,64,346** | **−19,857** | **STATED — in a footnote, not a note** (§2.2) | **NO** | `[AR FY24, PDF p158/pr152]` → `[AR FY25, PDF p158-159/pr147-148]` |
| **R-19** | **FY2025** | **Guarantees given by the Group (contingent liability)** | **10,60,024** | **24** | **−10,60,000 (−99.998%)** | **NEITHER** | **NO** | `[AR FY25, Note 38, PDF p209-210/pr198-199]` → `[AR FY26, Note 37, PDF p227/pr216]` |
| R-20 | FY2025 | Provisions — current (consol) | 8,071 | 2,627 | −5,444 | **NEITHER** — the amount equals the *Provision for SEBI regulatory fee* exactly | NO | `[AR FY25, Note 17, PDF p191/pr180]` → `[AR FY26, Note 17, PDF p207/pr196]` |
| R-21 | FY2025 | Other liabilities — current (consol) | 42,503 | 47,947 | +5,444 | **NEITHER** — the mirror of R-20 | NO | `[AR FY25, Note 19, PDF p193/pr182]` → `[AR FY26, Note 19, PDF p208/pr197]` |
| R-22 | FY2025 | Trade receivables (consol BS) | 30,967 | 28,778 | −2,189 | **NEITHER** | NO | `[AR FY25, PDF p155/pr144]` → `[AR FY26, PDF p163/pr152]` |
| R-23 | FY2025 | Administration and other expenses → Other expenses | 20,154 | 20,820 | +666 | **NEITHER** — equals the FY2025 face line *Liquidity enhancement scheme expense 666*, folded into the note | NO | `[AR FY25, Note 29, PDF p196/pr185]` → `[AR FY26, Note 28, PDF p213/pr202]` |
| **R-24** | **FY2025** | **CFO working-capital lines, restated a second time** — provision (10,793) → 740 and other liabilities (25,155) → (36,688); trade receivables (12,641) → (12,196) and other assets (25,506) → (25,951) | see left | see left | **±11,533 and ±445, both exactly offsetting; cash generated from operations unchanged at 73,812** | **NEITHER** | NO | `[AR FY25, PDF p158/pr147]` → `[AR FY26, PDF p165/pr154]` |
| R-25 | FY2026 | EPS — prior year adjusted for the 2:1 bonus (27,46,52,718 shares allotted on the 23-May-2025 record date) | 96.55 | 32.18 | Ind AS 33 | **STATED AND QUANTIFIED** | YES | `[AR FY26, Note 30, PDF p216/pr205]` |
| R-26 | FY2021 | One-off caption *Share Application Money Pending Allotment* 1,417 | n/a | n/a | one year only | NEITHER | NO | `[AR FY2021, PDF p145/pr140]` |

### 2.2 R-18 — the 19,679 FY2024 CFO restatement, resolved

**RF-027 asked whether a note states the reason. A note does not. A footnote does, and it does not
quantify.** The FY2025 consolidated cash flow statement carries **four** footnotes where FY2024
carried three. The inserted one is:

> **3. Movement in Core Settlement Guarantee Fund liabilities and related assets of subsidiary
> companies are not considered.** `[AR FY25, PDF p159/pr148]`

I searched all nine text files for that sentence. It appears in **FY2025 and FY2026 only** — never in
FY2017 through FY2024. It is a change in the basis of preparation of the consolidated cash flow
statement, disclosed as a footnote, unquantified, with no Ind AS 1.41 reclassification note.

**Full reconciliation.** Four adjustment lines present in the FY2024 statement are **absent** from the
FY2025 report's FY2024 comparative:

| Line deleted from the FY2024 comparative | ₹ lakh |
|---|---|
| Contribution to core settlement guarantee fund | 9,170 |
| Contribution received from other clearing corporation | 3,427 |
| Investment income on core settlement guarantee fund | 5,351 |
| Penalties / contribution received towards settlement guarantee fund | 1,769 |
| **Total SGF de-recognition** | **19,717** |

`[AR FY24, PDF p158/pr152]` for all four; none appears at `[AR FY25, PDF p158/pr147]`.

`DERIVED`: `9,170 + 3,427 + 5,351 + 1,769 = 19,717`.
Remaining movement, from the Ind AS 105 continuing/discontinued carve-out and regrouping:
`profit (296) + tax (34) + FCTR (15) + D&A (51) − FVTPL gain 164 − interest income 372 = +140` net
credit before working capital; working capital `−231`; direct taxes paid `+40`; discontinued-ops CFO
`(89)`.
`DERIVED`: `−19,717 − 140 = −19,857 = 2,84,203 − 2,64,346`. **The SGF exclusion is 19,717 of 19,857 =
99.3% of the restatement.**

Tie-outs, each reproduced independently:
`61,110 − 19,577 = 41,533` (operating cash flow before working capital) ✓
`3,01,594 − 19,808 = 2,81,786` (cash generated from operations) ✓
`2,84,203 − 19,768 = 2,64,435` (continuing-operations CFO) ✓

**Correction to RF-027's arithmetic, offered against the ledger, not to replace it.** The ledger's
19,679 is `2,84,203 − 2,64,435 − 89`; the discontinued-operations CFO of ₹(89) lakh belongs in the
restated *base*, not in the *delta*. Like-for-like total operations is `2,84,203 → 2,64,435 + (89
outflow) = 2,64,346`, so the restatement is **19,857**, and the continuing-only comparison is
**19,768**. Both the ledger's figure and mine identify the same event; the ledger's direction of the
89 was inverted. Recorded per §10.

### 2.3 What the register now says about BSE

- **Twenty-six movements across nine years. Exactly two are earnings restatements**: R-05 (FY2018 PAT
  −2,256) and R-25 (FY2026 EPS, mechanical, bonus-driven). Everything else is reclassification,
  presentation or basis-of-preparation.
- **Exactly three are STATED AND QUANTIFIED**: R-05, R-25, and the FY2020 ISF/IPF plough-back in §1.
  **Fifteen are NEITHER** — visible only by holding two audited reports side by side.
- **`records/restatements.md` ruled the FY2018 PAT delta an ARTIFACT.** That ruling is correct for the
  71,128 → 21,475 comparison it was made against (continuing versus total operations). It is not
  correct as a conclusion that FY2018 PAT was never restated: 71,128 → **68,872** is a real −2,256,
  it is on the FY2019 P&L face `[AR FY2019, PDF p148/pr139]`, and FY2019 Note 30 fn 2 explains it. Both
  positions stand.
- **The boilerplate never became a disclosure.** *"Previous year's figures have been regrouped wherever
  necessary"* runs unquantified in all nine years. Fifteen of the twenty-six movements above sit under
  it.

---

## 3. CONTINGENT LIABILITIES AND COMMITMENTS

### 3.1 The nine-year table (consolidated)

| ₹ lakh | FY2017 | FY2018 | FY2019 | FY2020 | FY2021 | FY2022 | FY2024 | FY2025 | FY2026 |
|---|---|---|---|---|---|---|---|---|---|
| Income tax matters | 1,404 | — | — | 7,695 | 7,897 | 19,532 | 11,003 | 11,170 | **13,496** |
| Service / indirect tax matters | 3,993 | — | — | 405 | 2,155 | 2,171 | 2,138 | 2,210 | **5,930** |
| Claims not acknowledged as debts | 10,401 | 10,362 | 51,282 | 16,778 | 10,352 | 10,591 | 10,557 | 10,504 | **13,567** |
| **— of which Management grades remote** | **10,370** | **10,362** | **51,281** | **16,777** | **10,351** | **10,590** | **10,556** | **10,504** | **ROW DELETED** |
| Guarantees given by the Group | 46 | — | — | 50,192 | 1,00,219 | 2,00,220 | 7,70,006 | 10,60,024 | **23** |

Sources: `[AR FY2017, Note 38, PDF p189/pr187]` · `[AR FY2018, Note 36, PDF p195/pr188]` ·
`[AR FY2019, Note 36, PDF p214/pr205]` · `[AR FY2020, Note 36, PDF p227/pr220]` ·
`[AR FY2021, Note 36, PDF p208/pr203]` · `[AR FY2022, Note 36, PDF p214/pr205]` ·
`[AR FY24, Note 37, PDF p225/pr219]` · `[AR FY25, Note 38, PDF p209/pr198]` ·
`[AR FY26, Note 37, PDF p227/pr216]`.

Standalone, for the three deep years: income tax 5,332 / 5,486 / **7,006**; service or indirect tax
299 / 302 / **245**; other matters 10,556 / 10,303 / **13,521**; of which remote 10,556 / 10,303 /
**deleted**; guarantees 4 / 23 / 23. `[AR FY24, Note 36, PDF p302/pr296]` ·
`[AR FY25, Note 37, PDF p270/pr259]` · `[AR FY26, Note 36, PDF p302/pr291]`.

### 3.2 RF-009 — what the claims are, and what the dropped grading was worth

**What they are.** The note itself says only *"claims against the Group primarily by the customers/
vendors and proceedings pending with Tax and Other Regulatory authorities"*
`[AR FY26, Note 37 fn 1, PDF p227/pr216]`. No counterparty, no vintage, no individual case above a
threshold, in any of the nine years. `NOT-DISCLOSED -> the composition of the ₹13,567 lakh claims
population would be settled only by BSE's litigation schedule, which is not filed publicly; the
nearest public proxy is CARO 3(vii)(b), which covers statutory dues only.`

**What the tax half is, exactly.** The FY2026 standalone tax rows tie to the rupee to the CARO
disputed-dues table:

| CARO 3(vii)(b) row | ₹ lakh | Forum |
|---|---|---|
| Income tax AY2010-11 / 11-12 / 12-13 / 14-15 / 15-16 | 574.74 + 303.74 + 243.18 + 158.05 + 1,297.92 | High Court |
| Income tax AY2016-17 / 17-18 | 3,023.72 + 1,404.44 | CIT(Appeals) |
| Service tax FY2005-06 to 2008-09 and FY2014-15 to Jun-2017 | 127.43 + 117.31 | CESTAT |

`[AR FY26, Annexure 1 CARO (vii)(b), PDF p246/pr235]`.
`DERIVED`: income tax `574.74 + 303.74 + 243.18 + 158.05 + 1,297.92 + 3,023.72 + 1,404.44 = 7,005.79`
against the note's **7,006**. Service tax `127.43 + 117.31 = 244.74` against the note's **245**.
The two disclosures are the same population.

**The oldest live income-tax dispute is AY2010-11 — sixteen years at 31-Mar-2026, and it is at the
High Court.** Nothing in the note tells the reader that; only CARO does.

**What the grading was worth.** For eight consecutive available years management graded
**99.99%–100.00%** of the "claims not acknowledged as debts" population as remote — 10,370 of 10,401
in FY2017, 10,504 of 10,504 in FY2025. Under Ind AS 37.86 a remote contingency need not be disclosed
at all, so BSE was volunteering both the number and its own probability grading. In FY2026 the
population rose for the first time in the window and the grading vanished.

`DERIVED`: consolidated claims not acknowledged `13,567 ÷ 10,504 = 1.2916`, **+29.2%** — the exact
figure RF-009 carries. Standalone `13,521 ÷ 10,303 = 1.3123`, **+31.2%**.
Total consolidated claims `(13,496 + 5,930 + 13,567) = 32,993` against
`(11,170 + 2,210 + 10,504) = 23,884`, `9,109 ÷ 23,884 = +38.1%`.

The note did not get shorter. FY2026 **added** a third footnote — a qualitative paragraph on
*"Clearing and Settlement Activities"* asserting that clearing-member collateral is adequate
`[AR FY26, Note 37 fn 3, PDF p227/pr216]`. A quantified probability grading was removed and an
unquantified management assertion was added in the same note in the same year.

### 3.3 The SEBI ₹170cr differential regulatory fee provision — no longer carried

| ₹ lakh | FY2024 | FY2025 | FY2026 |
|---|---|---|---|
| Provision for SEBI regulatory fee (Note 17, current) | **16,977** | **5,444** | **nil** |
| FY2025 comparative as restated in the FY2026 AR | — | **nil** (moved to Other liabilities, R-20/R-21) | — |
| SEBI regulatory fees — P&L expense | 17,212 (restated) | 33,141 | **56,616** |
| SEBI Regulatory fees explanatory note | Note 46 | Note 46 | **NOTE DELETED** |

`[AR FY24, Note 17, PDF p203/pr197]` · `[AR FY25, Note 17, PDF p191/pr180]` ·
`[AR FY26, Note 17, PDF p207/pr196]` · `[AR FY26, Note 27, PDF p212/pr201]`.

**Answer to the question asked: the ₹170cr provision is not carried at FY2026, and it was never
released to income.** It converted into a permanent, growing operating expense. `DERIVED`:
`56,616 ÷ 33,141 = 1.708`, **+70.8%**, against revenue from operations `4,83,395 ÷ 2,95,734 = 1.635`,
**+63.5%** `[AR FY26, Consolidated P&L, PDF p164/pr153]`. Against the restated FY2024 base the fee is
`56,616 ÷ 17,212 = 3.29×` in two years. The FY2024 provision that was made *"based on the prudence"*
while the company intended to *"present its position to SEBI and request to reconsider"*
`[AR FY24, Note 46, PDF p233/pr227]` is now the third-largest expense line in the group, and the note
that traced it was deleted in the year it grew 70.8%.

Disconfirming evidence, sought and found: as a share of revenue from operations the fee is roughly
stable — `56,616 ÷ 4,83,395 = 11.71%` FY2026 against `33,141 ÷ 2,95,734 = 11.21%` FY2025. Total
regulatory contribution actually **fell** as a share of revenue, `64,969 ÷ 4,83,395 = 13.44%` against
`41,046 ÷ 2,95,734 = 13.88%`. This is not a margin story. It is a disclosure story.

### 3.4 The ₹7.25cr CGST demand — disclosed in the BRSR, absent from the financial statements

| Element | Detail | Source |
|---|---|---|
| Authority | Principal Commissioner of CGST & Central Excise, Mumbai South | `[AR FY26, BRSR Sec C P1 Q2, PDF p124/pr113]` |
| Order | Section 73, CGST Act 2017, dated **17.12.2025**, for **Apr 2021–Mar 2022** | same |
| Allegation | **excess Input Tax Credit availed by BSE Limited** | same |
| Amount | GST ₹6,59,26,901 + penalty ₹65,92,690 + interest *not quantified* = **₹7,25,19,591** (₹725 lakh) | same |
| Appeal | filed **06.03.2026** to Commissioner (Appeals-I), CGST & C.Ex., Mumbai | same |

Both the order and the appeal fall inside FY2026, and the matter was live at the balance-sheet date.
It appears in **neither** of the two places a disputed indirect-tax demand belongs:

- **Standalone contingent liabilities, indirect tax matters: ₹245 lakh, and it FELL from ₹302 lakh**
  `[AR FY26, Note 36, PDF p302/pr291]`. §3.2 shows that ₹245 lakh is the CESTAT service-tax matters,
  to the rupee. There is no room in it for ₹725 lakh.
- **CARO 3(vii)(b)** — "dues of goods and services tax … which have not been deposited on account of
  any dispute" — carries **no GST row at all** `[AR FY26, PDF p246/pr235]`.

Three readings, and the annual report does not distinguish between them: (a) the demand was paid in
full before year end, so it is neither a contingent liability nor an undeposited disputed due — but
then it is an expense or a recoverable of ₹725 lakh that appears as neither in Note 28 nor Note 13;
(b) management assessed outflow as remote and, having deleted the "remote" row (§3.2), had nowhere to
put it; (c) it was omitted.
`NOT-DISCLOSED -> settled only by BSE's FY2026 Form 3CD / GST annual return, or by the FY2027 annual
report's comparative.`

### 3.5 Capital commitments

| ₹ lakh | FY2023 | FY2024 | FY2025 | FY2026 |
|---|---|---|---|---|
| Consolidated | 4,660 | 8,793 | 17,006 | **10,029** |
| Standalone | — | 7,315 | 16,022 | **9,257** |

`[AR FY24, Note 38, PDF p225/pr219]` · `[AR FY25, Note 39, PDF p210/pr199]` ·
`[AR FY26, Note 38, PDF p227/pr216]`.

Commitments fell 41.0% (`10,029 ÷ 17,006 = 0.590`) in the year capex tripled
(`51,516 ÷ 15,323 = 3.36×`, W1_ledger). That is the expected shape — commitments converting into
spend, not an unexplained fall. Recorded as a **clean** line: it is one of the few places in this
wave where the movement and the story agree.

---

## 4. TABLES THAT STOPPED APPEARING — item ceased, or disclosure ceased?

The two are different findings. Adjudicated one by one, with the evidence that settles which.

| # | Disclosure | Last year | Verdict | Evidence |
|---|---|---|---|---|
| 1 | **SEBI Regulatory fees note** (consol 46 / standalone 45) | FY2025 | **DISCLOSURE CEASED.** The item grew 70.8% in the year the note was deleted | expense ₹56,616 lakh alive inside Note 27 `[AR FY26, Note 27, PDF p212/pr201]`; note absent from both blocks |
| 2 | **Buyback note** (consol 51 / standalone 50) | FY2025 | **ITEM CEASED.** No FY2026 buyback | *"Shares buyback during the year — nil"* in the SOCIE `[AR FY26, PDF p167/pr156]`. But the capital redemption reserve created by past buybacks was **fully utilised in FY2026 against the bonus issue** `[AR FY26, Note 15, PDF p205/pr194]` — a real equity event that now has no buyback note to sit beside |
| 3 | **Liquidity Enhancement Scheme note** (consol 45 / standalone 41) | FY2024 | **BOTH — and they are two different schemes.** BSE's own SEBI-circular LES genuinely ended (discontinued w.e.f. 1-Apr-2023, ₹2,174 lakh incurred in FY2023). India INX's LES did **not** end | cessation `[AR FY24, Note 45, PDF p233/pr227]`; continuation — *Liquidity enhancement scheme expense* **556** (FY2025: 666) inside Note 28 `[AR FY26, Note 28, PDF p213/pr202]`, and the LES reserve of 9 (FY2025: 8) still runs at Note 15.8 `[AR FY26, Note 15.8, PDF p205/pr194]`. The FY2025 P&L **face** line was moved into the note (R-23) |
| 4 | **Impairment loss on financial assets note** (consol 30) | FY2017 | **DISCLOSURE CEASED, and the item is now 4× larger.** FY2017 note total ₹1,043 lakh; FY2026 equivalent components ₹4,065 − 8 + 4 = ₹4,061 lakh, buried in a 25-line Other-expenses note | `[AR FY2017, Note 30, PDF p177/pr175]` → `[AR FY26, Note 28, PDF p213/pr202]`. This is the line RF-026 turns on (§7) |
| 5 | **Specified Bank Notes disclosure** (consol 50 / standalone 42) | FY2018 | **ITEM CEASED — regulatory sunset.** Not a company choice | `[AR FY2018, Note 50, PDF p203/pr196]`. Recorded only so the crosswalk is complete |
| 6 | **Two-segment consolidated disclosure** | FY2017 | **ITEM CEASED, DISCLOSURE NEVER RETURNED.** The Depository segment genuinely left on the CDSL deconsolidation. But BSE has since built ICCL clearing, India INX, BSE Technologies, index services and StAR MF, and still reports **one** operating segment with geography as the only disaggregation | `[AR FY2017, Note 40.1, PDF p189/pr187]`; `[AR FY2019, Note 38.1, PDF p215/pr206]`; `[AR FY26, Note 39, PDF p228/pr217]`. Nine years and no business-line segment P&L. Ind AS 108.5 turns on what is reported to the CODM, and the note asserts the CODM sees one segment |

**Two of the six are pure item-cessation (SBN, buyback). One is genuinely both (LES). Three are
disclosure-cessation over a live and in two cases growing item.**

---

## 5. THE COMPANIES (AUDIT) ADDITIONAL DISCLOSURES AND CARO — read in full

### 5.1 CARO 2020, FY2026 standalone — the two qualified clauses, and everything clean

`[AR FY26, Annexure 1, PDF p245-247/pr234-236]`, and the group table
`[AR FY26, consolidated Annexure 1, PDF p160/pr149]`.

| Clause | Reading |
|---|---|
| **(i)(c) QUALIFIED** | Title deeds of two properties still in the name of the pre-demutualisation bodies: **Machinery House ₹307 lakh** held by *The Trustees of the Bombay Stock Exchange* for **30 years**, and **CAMA ₹69 lakh** held by *Trustees of the Native Share & Stock Brokers Association* for **52 years**. An application to the Superintendent of Land Records was filed during FY2026 |
| **(vii)(b) QUALIFIED** | Disputed statutory dues ₹7,250.53 lakh — the table reproduced at §3.2 |
| **(ix)(a) — VERIFIED, as W1_docmap says** | *"The Company did not have any outstanding loans or borrowings or interest thereon due to any lender during the year."* Corroborated three ways: no borrowings line on either balance sheet; standalone Note 45 Analytical Ratios states no borrowings; (ix)(c) no term loans; (ix)(d) no funds raised; (ii)(b) **no working-capital limits sanctioned on the security of current assets at any point in the year** |
| (ix)(b) | **Not declared a wilful defaulter** by any bank, financial institution, government or government authority |
| (ix)(e) | **No funds taken from any entity or person to meet the obligations of subsidiaries or associates** — a direct read on the ICCL guarantee question of §3.3 and F-2 |
| (iii)(a) | Loans **only to employees**: ₹3.10 lakh granted in FY2026, ₹24 lakh outstanding. *"the Company has not provided advances in the nature of loans, stood guarantee or provided security to companies, firms, Limited Liability Partnerships or any other parties"* |
| (iii)(b)–(f) | Terms not prejudicial; repayment regular; **nothing overdue beyond ninety days**; no evergreening; no repayable-on-demand loans |
| (iv) | No section 185 loans/guarantees; section 186 complied with |
| (v) | No public deposits or deemed deposits |
| (viii) | **No previously unrecorded transaction surrendered or disclosed as income** in any income-tax assessment |
| (x)(a)(b) | No IPO/FPO; **no preferential allotment or private placement** |
| (xi)(a) | **No fraud by or on the Company noticed or reported** |
| (xi)(b) | **No ADT-4 filed** by the secretarial auditor or the statutory auditor |
| (xi)(c) | Whistle-blower complaints **were received** and were taken into account in scoping the audit. The number is not given and CARO does not require it. `NOT-DISCLOSED -> the whistle-blower complaint count is in the Audit Committee section of the Corporate Governance Report, W2_gov_early's territory` |
| (xiii) | Related-party transactions comply with sections 177 and 188 |
| (xv) | No non-cash transactions with directors |
| (xvii) | No cash losses in FY2026 or FY2025 |
| (xviii) | **No resignation of the statutory auditors** |
| (xix) | No material uncertainty on meeting liabilities falling due within twelve months |
| (xx)(a)(b) | No unspent CSR to transfer, ongoing or otherwise |

**Group-level CARO 3(xxi), FY2026:** five rows — BSE Limited 3(i)(c) and 3(vii)(b); BSE Technologies
Private Limited 3(vii)(b); India Clearing Corporation Limited 3(vii)(b); India International Exchange
IFSC Limited 3(xvii) (cash losses). Compared with FY2024's six rows, **BSE Institute Limited and India
International Clearing Corporation (IFSC) Limited have dropped off and Indian Clearing Corporation has
appeared** — the first because BIL was sold (discontinued operation, Note 49), the second is a genuine
clean-up. Every one of the four 3(vii)(b) rows is disputed statutory dues.

### 5.2 The Schedule III additional regulatory information — and the two clauses the consolidated version drops

`[AR FY26, standalone Note 49, PDF p310-311/pr299-300]` (twelve clauses) versus
`[AR FY26, consolidated Note 52, PDF p240/pr229]` (ten clauses).

| Test | Standalone Note 49 | Consolidated Note 52 |
|---|---|---|
| **Promoters** | *"There are no promoters identified for the Company"* | same. **This is the answer to the loans-to-promoters question: BSE has no identified promoter**, so the test is structurally inapplicable, and (xii) confirms no loans to directors, KMP or related parties on demand or without terms |
| Benami property | none, current and prior year | none |
| **Crypto / virtual currency** | none traded or invested, current and prior year | none |
| Undisclosed income surrendered in tax assessment | none | none |
| **Intermediary leg** — funds advanced with an understanding the intermediary onward-lends | none | none |
| **Funding-party leg** — funds *received* with an understanding the Company onward-lends | **PRESENT, clause (vii)** | **ABSENT** |
| Charges or satisfaction to be registered with ROC | **PRESENT, clause (iii)** | **ABSENT** |
| Wilful defaulter | not declared | not declared |
| Layers of subsidiaries (s.2(87)) | complied | complied |
| Scheme of arrangement (ss.230–237) | none | none |
| Revaluation of PPE or intangibles | none | none |
| Loans to directors/KMP/related parties repayable on demand | none | none |

**The consolidated Note 52 omits the funding-party leg entirely.** The auditor's Rule 11(e) statement
covers both legs at the standalone level `[AR FY26, PDF p244/pr233]` — sub-clause (b) is the
funding-party representation — so the assurance exists; the group-level disclosure does not. For a
group holding ₹4,06,419 lakh of member and clearing-and-settlement deposits, the "funds received with
an understanding" clause is the one a reader would most want at consolidated level.

---

## 6. AGEING SCHEDULES — CONFIRMED MISSING FROM THE CONSOLIDATED

W1_docmap §6 #6 and #7 are **confirmed by direct search of each consolidated notes block.**

| Report | Consolidated notes block searched | Ageing schedules found |
|---|---|---|
| FY2022 | PDF 154–224 | trade receivables 10.6, trade payables 20.2 — **only two** |
| FY2024 | PDF 162–236 | trade receivables 10.6, trade payables 20.2 — **only two** |
| FY2025 | PDF 162–219 | trade receivables 10.5, trade payables 20.1 — **only two** |
| FY2026 | PDF 169–240 | trade receivables 10.5, trade payables 20.1 — **only two** |

Meanwhile both assets sit on the face of the consolidated balance sheet **with no note reference at
all**: *Capital work-in-progress* ₹3,255 lakh (FY2025: ₹4,073 lakh) and *Intangible assets under
development* ₹4,420 lakh (FY2025: ₹1,339 lakh) `[AR FY26, Consolidated Balance Sheet, PDF p163/pr152]`
— note-number columns b. and f. are blank where every other line carries one.

The **standalone** carries both schedules in all four years: CWIP Note 3.1
`[AR FY26, Note 3.1, PDF p264/pr253]` and intangibles-under-development ageing and completion Note 6
`[AR FY26, Note 6, PDF p266-267/pr255-256]`.

Schedule III Division II applies to consolidated financial statements. **This is a five-year
Schedule III omission that no auditor has remarked on, in the one asset class where ageing is the
whole point of the disclosure.** IAUD grew `4,420 ÷ 1,339 = 3.30×` in FY2026 — precisely the movement
the missing completion schedule would explain.

---

## 7. RF-026 SUPPORT — trade receivables, unbilled, and the ECL movement

### 7.1 The numbers

| ₹ lakh, consolidated | FY2025 | FY2026 | Change |
|---|---|---|---|
| Revenue from operations | 2,95,734 | 4,83,395 | **+63.5%** |
| Gross trade receivables | 34,802 | 65,109 | **+87.1%** |
| — of which **unbilled** | 22,184 | 50,637 | **+128.3%** |
| — of which **billed** | 12,618 | 14,472 | **+14.7%** |
| Impairment allowance (closing) | 6,024 | 9,793 | +62.6% |
| Impairment charge to P&L | 3,635 | 4,025 | +10.7% |
| Bad debts written off | 452 | 256 | −43.4% |
| Net trade receivables | 28,778 | 55,316 | +92.2% |

`[AR FY26, Note 10 and 10.4-10.5, PDF p199-200/pr188-189]`; revenue
`[AR FY26, Consolidated P&L, PDF p164/pr153]`.
Allowance roll-forward ties: `6,024 − 256 + 4,025 = 9,793` ✓.

### 7.2 The shape — three asymmetries, each with its counter-proportion

**(a) The growth is entirely unbilled.** Unbilled is **77.8%** of gross receivables at FY2026
(`50,637 ÷ 65,109`) against **63.7%** at FY2025 (`22,184 ÷ 34,802`). The counter-proportion: **billed**
receivables grew only **+14.7%** while revenue grew +63.5%. Billed collection did not deteriorate; the
whole movement is revenue recognised and not yet invoiced.

Sized in days, which is what makes it comparable:
`DERIVED`: FY2026 `50,637 ÷ 4,83,395 × 365 = 38.2 days`; FY2025 `22,184 ÷ 2,95,734 × 365 = 27.4 days`.
`DERIVED`: the extension is `10.8 days × (4,83,395 ÷ 365 = 1,324) = 14,300 lakh`, **5.7% of FY2026 PAT
attributable of 2,49,698**. The standalone moves identically — `47,735 ÷ 4,46,951 × 365 = 39.0` against
`20,108 ÷ 2,60,643 × 365 = 28.2` — so this is a parent-level billing-cycle change, not a subsidiary
artefact `[AR FY26, Note 10.1, PDF p276-277/pr265-266]`.

**(b) The expected-loss rate on the newest bucket was cut by two-thirds.**

| Bucket | FY2025 loss rate | FY2026 loss rate |
|---|---|---|
| Unbilled | 0% | 0% |
| Not due | 0% | 0% |
| **Less than 6 months** | **39%** | **13%** |
| 6 months – 1 year | 50% | 72% |
| 1–2 years | 46% | 100% |
| 2–3 years | 99% | 100% |
| More than 3 years | 100% | 100% |
| **Total** | **17%** | **15%** |

`[AR FY26, Note 10.5, PDF p199-200/pr188-189]`. The standalone cut the same bucket from **47% to 13%**
`[AR FY26, Note 10.1, PDF p276-277/pr265-266]`. No reason is given in either block. The standalone
note offers only *"a practical expedient by computing the expected credit loss allowance for trade
receivables based on a detailed analysis of trade receivable by individual departments"* — which is
not the provision matrix Ind AS 109.B5.5.35 describes, and which explains the method, not the change.

**(c) The parent released provisions while the group more than doubled them.**

| ₹ lakh | FY2025 | FY2026 |
|---|---|---|
| Group impairment allowance | 6,024 | 9,793 |
| Standalone impairment allowance | 2,834 | **2,294 (a fall)** |
| **Subsidiaries, by difference** | **3,190** | **7,499** |
| Standalone P&L charge | 554 | **(284) — a write-back** |
| Subsidiaries' P&L charge, by difference | 3,081 | 4,309 |

`DERIVED`: standalone roll-forward `2,834 − 256 + (284) = 2,294` ✓; subsidiary allowance
`9,793 − 2,294 = 7,499` against `6,024 − 2,834 = 3,190`, **+135.1%**.

The counter-proportion that makes this a finding: **subsidiaries hold 19.0% of the group's gross
receivables (`12,373 ÷ 65,109`) but 76.6% of its impairment allowance (`7,499 ÷ 9,793`)**. A year
earlier they held 30.8% of gross and 53.0% of the allowance. The subsidiary ECL rate went from
`3,190 ÷ 10,733 = 29.7%` to `7,499 ÷ 12,373 = 60.6%` while the parent's went the other way. No note
identifies which subsidiary. `NOT-DISCLOSED -> only the subsidiaries' own financial statements filed
with the MCA would identify the entity; the AOC-1 at PDF p312-313 gives turnover and PAT but no
receivable or provision detail.`

---

## 8. CHAIN RECORDS

### CHAIN: Net cash from operating activities (consolidated) | FY24 restated
L1 REPORTED   TRACED | 2,84,203 as first reported; 2,64,435 continuing + (89) discontinued = 2,64,346 as restated | [AR FY24, PDF p158/pr152] and [AR FY25, PDF p158-159/pr147-148]
L2 COMPONENTS DERIVED | four Core SGF adjustment lines deleted: 9,170 + 3,427 + 5,351 + 1,769 = 19,717, against a total restatement of 2,84,203 - 2,64,346 = 19,857, i.e. 99.3% | [AR FY24, PDF p158/pr152]
L3 DRIVER     TRACED | not an economic driver at all: the cash flows did not change, the boundary of the statement did. Footnote 3 inserted in FY2025 excludes Core SGF liabilities and related assets of subsidiary companies | [AR FY25, PDF p159/pr148]
L4 COUNTERPARTY TRACED | ICCL and India International Clearing Corporation (IFSC) Limited hold the Core SGF; the fund stood at 1,24,683 at FY2026 and 1,13,260 at FY2025 on the face of the consolidated balance sheet | [AR FY26, Notes 41 and 42, PDF p231-232/pr220-221]
L5 RECOGNITION NOT-DISCLOSED | no Ind AS 1.41 reclassification note and no Ind AS 8 disclosure; the change is carried by an unquantified one-line footnote -> settled only by BSE's FY2025 board-approved accounting-policy paper, which is not published; the next-best public source is the FY2025 limited-review quarterly filings, which would show when the presentation first changed | [AR FY25, PDF p159/pr148]
L6 BALANCE-SHEET TRACED | the SGF caption sits between equity and liabilities on the face of the balance sheet and is unaffected by the cash flow change; the FY2018 restatement (R-06/R-07) shows the same caption absorbing 5,380 out of Other equity | [AR FY26, PDF p163/pr152] and [AR FY2019, PDF p147/pr138]
L7 CASH       DERIVED | own-account CFO was already separable (RF-005 resolved): FY2024 own-account 75,840 against a headline 2,84,203, so 2,08,363 / 2,84,203 = 73.3% was clearing-member float. The 19,857 restatement removes SGF flows but leaves the member float in | [AR FY26, Note 16, PDF p206/pr195]
L8 SUSTAIN    TRACED | the new basis persists into FY2026, where footnote 3 is repeated verbatim; from FY2025 the reported CFO series is on a different basis from FY2017-FY2024 and any multi-year CFO/PAT test must break at that boundary | [AR FY26, PDF p166/pr155]
CHAIN-STATE: BROKEN at L5 — a change in the basis of preparation with no recognition disclosure and no quantification

### CHAIN: Guarantees given by the Group | FY26
L1 REPORTED   TRACED | 23 at FY2026 against a restated FY2025 comparative of 24; the FY2025 report itself showed 10,60,024 | [AR FY26, Note 37, PDF p227/pr216] and [AR FY25, Note 38, PDF p209/pr198]
L2 COMPONENTS TRACED | FY2025 footnote 3: the Subsidiary Company gave a bank guarantee of 10,60,000 lakhs at 31-Mar-2025 (7,70,000 at 31-Mar-2024) towards Inter CCP collateral under the Interoperability framework prescribed by SEBI; the residual 24 is the legacy employee housing-loan guarantee | [AR FY25, Note 38 fn 3, PDF p209-210/pr198-199] and [AR FY24, Note 37 fn 2, PDF p225/pr219]
L3 DRIVER     DERIVED | the guarantee scaled with BSE derivative volume: 31 (FY2019) then 50,192, 1,00,219, 2,00,220, 3,00,217, 7,70,006, 10,60,024, so 10,60,024 / 31 = 34,194x over six years, then 23 in FY2026, i.e. 23 / 10,60,024 = 0.002% of the prior year | [AR FY2020, Note 36, PDF p227/pr220] through [AR FY25, Note 38, PDF p209/pr198]
L4 COUNTERPARTY TRACED | given by Indian Clearing Corporation Limited to the other interoperable clearing corporations; ICCL remains fully consolidated at 12% of consolidated net assets, 81,645 lakh | [AR FY26, Note 40, PDF p228/pr217]
L5 RECOGNITION NOT-DISCLOSED | no note states why the caption changed basis, and Ind AS 8.49 would require the nature and amount of a prior-period error if that is what it was -> settled only by ICCL's own FY2026 financial statements filed with the MCA, or by the SEBI-mandated ICCL risk disclosures on the BSE website | [AR FY26, Note 37, PDF p227/pr216]
L6 BALANCE-SHEET TRACED | nothing on the balance sheet moved: Core SGF 1,24,683 and clearing-and-settlement liabilities 3,55,423 both grew. The 10,60,000 was always off balance sheet and its removal changes no recognised amount | [AR FY26, PDF p163/pr152] and [AR FY26, Note 16, PDF p206/pr195]
L7 CASH       TRACED | no cash consequence in any year: it never appears in the cash flow statement in FY2024, FY2025 or FY2026 | [AR FY26, PDF p165-166/pr154-155]
L8 SUSTAIN    NOT-DISCLOSED | the interoperability framework did not end — SEBI disposed of its interoperability show-cause notice against ICCL on 15-May-2025 without penalty, and the FY2026 report still describes interoperable CCPs in the ICCL liquidity-risk section -> whether the guarantee itself was released is settled only by ICCL's collateral disclosures, which the annual report does not carry | [AR FY26, Secretarial Audit ICCL, PDF p48/pr37]
CHAIN-STATE: BROKEN at L5/L8 — the largest single disclosure movement in the corpus, with no stated recognition basis and no evidence the underlying obligation ended

### CHAIN: Trade receivables — impairment allowance | FY26
L1 REPORTED   TRACED | gross 65,109, allowance 9,793, net 55,316 (FY2025: 34,802 / 6,024 / 28,778) | [AR FY26, Note 10, PDF p199/pr188]
L2 COMPONENTS TRACED | unbilled 50,637, not due 1,836, under 6 months 3,092, 6-12 months 520, 1-2 years 2,922, 2-3 years 4,228, over 3 years 1,874 | [AR FY26, Note 10.5, PDF p199/pr188]
L3 DRIVER     DERIVED | billed receivables grew 14,472 / 12,618 = +14.7% against revenue +63.5%, so the driver is invoicing lag not collection: unbilled days 50,637 / 4,83,395 x 365 = 38.2 against 22,184 / 2,95,734 x 365 = 27.4 | [AR FY26, Note 10.5, PDF p199/pr188]
L4 COUNTERPARTY NOT-DISCLOSED | no customer, member or listed-company breakup in any year, and no Ind AS 108.34 concentration trigger arises -> settled only by BSE's internal receivable ledger; the nearest public proxy is the count of suspended and non-compliant listed companies published on the BSE website | [AR FY26, Note 10, PDF p199/pr188]
L5 RECOGNITION BROKEN | the under-6-month expected loss rate was cut from 39% to 13% consolidated and 47% to 13% standalone with no stated reason; the only method disclosure is a practical expedient by individual department, which is not the Ind AS 109 provision matrix | [AR FY26, Note 10.1, PDF p276/pr265]
L6 BALANCE-SHEET DERIVED | the ECL rate on billed receivables rose 6,024 / 12,618 = 47.7% to 9,793 / 14,472 = 67.7% at group level while the parent's allowance fell 2,834 to 2,294; subsidiaries hold 12,373 / 65,109 = 19.0% of gross but 7,499 / 9,793 = 76.6% of the allowance | [AR FY26, Note 10.4, PDF p199/pr188] and [AR FY26, Note 10, PDF p276/pr265]
L7 CASH       DERIVED | the cash flow charges the movement back: decrease in trade receivables (30,595) and impairment loss on financial assets 4,057, against 4,025 charged in Note 10.4, so 4,057 - 4,025 = 32 lakh arises on non-receivable financial assets; the receivable absorption 30,595 / 3,10,368 = 9.9% of reported CFO | [AR FY26, PDF p165/pr154]
L8 SUSTAIN    ESTIMATE | sustainable only if the unbilled balance is genuinely last-period transaction charges; at 38.2 days against a stated credit period of 0 to 60 days it is inside terms, but the 10.8-day extension is worth about 14,300 lakh = 5.7% of PAT attributable of 2,49,698 and it recurs only if billing cadence stays where it moved to | [AR FY26, Note 10.2, PDF p199/pr188]
CHAIN-STATE: BROKEN at L5 — a material ECL assumption change with no disclosed reason, inside a note whose headline growth is explained by billing lag

---

## 9. FINDINGS

### FINDING: The unexplained FY2024 cash-flow restatement is a change in the basis of preparation, disclosed as an unquantified footnote
S1 WHAT: The FY2025 annual report restated FY2024 consolidated CFO from ₹2,84,203 lakh to ₹2,64,346 lakh on a total-operations basis — a fall of ₹19,857 lakh — by deleting four Core Settlement Guarantee Fund adjustment lines from the comparative and inserting a new footnote saying SGF movements of subsidiaries are no longer considered.
S2 WHY: Not an economic event. The mechanism is a redrawing of the boundary of the cash flow statement: BSE already excluded the parent's earmarked balances (footnote 2, present since FY2018) and from FY2025 extended the same treatment to the Core SGF held by ICCL and India ICC. The four deleted lines are the contribution to the fund, the contribution received from the other clearing corporation, investment income on the fund and penalties received into it — each of which is a movement in a fund the group holds but does not own.
S3 EVIDENCE: `9,170 + 3,427 + 5,351 + 1,769 = 19,717` of a `2,84,203 − 2,64,346 = 19,857` restatement, i.e. **99.3%** `[AR FY24, PDF p158/pr152]` against `[AR FY25, PDF p158-159/pr147-148]`. The counter-proportion that shapes it: the SGF exclusion is 99.3% of the restatement but the Ind AS 105 discontinued-operations carve-out — the reason a reader would assume, because it is the reason given for the P&L restatement on the facing page — is only `140 ÷ 19,857 = 0.7%`. Every subtotal ties: `61,110 − 19,577 = 41,533`; `3,01,594 − 19,808 = 2,81,786`; `2,84,203 − 19,768 = 2,64,435`. The sentence *"Movement in Core Settlement Guarantee Fund liabilities and related assets of subsidiary companies are not considered"* occurs in FY2025 and FY2026 and in no earlier year — searched all nine files.
S4 CONNECTS: The Core SGF is the subject of the only Emphasis of Matter in nine years (FY2020, W1_docmap §5.3); of the new P&L subtotal inserted in the same FY2025 report (§1); of the FY2018 equity restatement R-06/R-07; and of RF-017, where management defines the SGF contribution policy on a standalone basis and then quotes it on a consolidated one. Four separate presentation changes to one item in one nine-year window, all in the direction of moving it away from the operating line. Against this, the FY2025 auditor's report carries an unmodified opinion with a single KAM on investment valuation and no reference to the cash flow statement `[AR FY25, PDF p149/pr138]`.
DOMAINS: CashFlow, Notes, BalanceSheet, Governance, MgmtCommentary
DISCONFIRM: Sought and found, and it cuts in BSE's favour on substance. Excluding third-party settlement funds from operating cash flow is the more informative presentation, not the less — it is what RF-005 was asking for. The new basis moves reported CFO toward own-account CFO. The finding is therefore about disclosure quality, not about a flattering restatement: the FY2024 number was restated **downwards** by ₹19,857 lakh, which is the opposite of what an earnings-management reading would predict. Also recorded: footnote 2 (parent earmarked balances) has run since FY2018, so the principle was not invented in FY2025 — only extended.
S5 MEANS: BSE changed how it measures its own headline operating cash flow and told the reader in eleven words at the foot of a statement, without a number, in the year that number fell 85.6% (`41,015 ÷ 2,84,203`). A reader building a ten-year CFO series from the annual reports gets a break at FY2025 that no note warns of and that no amount in any filing quantifies. That is the specific failure Ind AS 1.41 exists to prevent, and it means the pre-FY2025 and post-FY2025 CFO series measure different things.
BASE-RATE: Has this ever cost money here? No realised loss is attached to it and none is expected — the cash was never the group's. But the pattern has cost readers before at this company: W1_ledger found nine ledger cells mixed reporting bases and RF-029 established that in every one of the nine cases an untagged number was a wrong number, driven by exactly this class of silent re-presentation. In the wider system, unannounced changes in the boundary of the cash flow statement are the standard mechanism by which clearing-house and NBFC operating cash flow becomes non-comparable; the SEBI-mandated separation of own funds from settlement funds exists precisely because the two have been conflated before.
S6 IMPLICATION: Every multi-year CFO-to-PAT conversion test must break at FY2025 and be run on two segments, or on own-account CFO throughout, which W1_ledger has already made possible. The durability question is unaffected — no cash was gained or lost — but the **measurability** of the earnings stream is: a company that can move ₹19,857 lakh out of its headline operating cash flow on a footnote can do so again, and the monitorable is whether the FY2027 report adds a fifth footnote. Thesis-breaker for anyone relying on reported CFO: if own-account CFO and reported CFO diverge again in FY2027 without a quantified note, reported CFO is not a usable series at this company. Next check: FY2027 annual report, consolidated cash flow footnotes.
SEVERITY: High

### FINDING: The ₹10.6 lakh-crore guarantee did not collapse — the FY2025 comparative was restated to strip it out
S1 WHAT: The FY2025 annual report disclosed *Guarantees given by the Group* of ₹10,60,024 lakh, of which ₹10,60,000 lakh was ICCL's bank guarantee towards Inter-CCP collateral under SEBI's interoperability framework. The FY2026 annual report shows ₹23 lakh — **and shows the FY2025 comparative as ₹24 lakh**, not ₹10,60,024 lakh. The phrase "bank guarantee" does not occur anywhere in the FY2026 annual report.
S2 WHY: A guarantee that was released during FY2026 would leave the FY2025 comparative untouched at ₹10,60,024 lakh; only the FY2026 column would fall. Restating the comparative to ₹24 lakh is the signature of a change in view about what the item ever was — either a reclassification under Ind AS 1.41 or an error correction under Ind AS 8.49. Neither is disclosed. What replaced it in the same note is a new qualitative footnote asserting that clearing-member collateral is adequate on a net basis, with no number.
S3 EVIDENCE: ₹10,60,024 → ₹24 for the same balance-sheet date is a **−99.998%** restatement, the largest in the corpus by absolute magnitude at ₹10,60,000 lakh. The counter-proportion that sizes it: at FY2025 that guarantee was **2.32× total equity** (`10,60,024 ÷ 4,57,570`) and **102.5% of total assets** (`10,60,024 ÷ 10,34,165`) — it exceeded the group's entire balance sheet — while the ₹24 lakh that replaced it is **0.005%** of equity. The six-year build was disclosed year by year: 31 → 50,192 → 1,00,219 → 2,00,220 → 3,00,217 → 7,70,006 → 10,60,024, with FY2024 and FY2025 naming the mechanism explicitly `[AR FY24, Note 37 fn 2, PDF p225/pr219]` and `[AR FY25, Note 38 fn 3, PDF p209-210/pr198-199]`. The residual ₹23 lakh equals the standalone figure exactly `[AR FY26, Note 36, PDF p302/pr291]` — i.e. the consolidated caption has reverted to containing only the parent's legacy employee housing-loan guarantee, which is what it contained in FY2017 at ₹46 lakh.
S4 CONNECTS: Interoperability did not end. SEBI's show-cause notice to ICCL on interoperability was disposed of on 15-May-2025 without monetary penalty `[AR FY26, Secretarial Audit ICCL, PDF p48/pr37]`, and the FY2026 ICCL liquidity-risk disclosure still names interoperable CCPs. ICCL remains fully consolidated at 12% of group net assets `[AR FY26, Note 40, PDF p228/pr217]`. CARO (ix)(e) confirms the parent took no funds to meet subsidiary obligations `[AR FY26, PDF p246/pr235]`. RF-024 records RBI's 13-Feb-2026 directions on bank capital-market exposure effective 1-Jul-2026, with management stating legacy bank guarantees still mask the effect — which would explain a *forward* reduction, not a restated *past* comparative.
DOMAINS: Notes, BalanceSheet, Governance, Industry
DISCONFIRM: Actively sought, three ways. (1) If ICCL genuinely replaced bank guarantees with cash or securities collateral in FY2026, the fall is real — but the FY2025 comparative would not have been restated, and it was. (2) If the FY2025 disclosure was simply wrong — for instance a guarantee ICCL *received* rather than *gave* — restating is the correct remedy, and this is the reading most favourable to the company; but Ind AS 8.49 then requires the nature and amount of the error, and neither is given. (3) The auditor is the same firm and the same engagement partner across both years, Pikashoo Mutha, with an unmodified opinion on both, so no audit-driven change in view is signalled. On every reading the note fails a disclosure requirement, which is why the finding does not depend on choosing between them.
S5 MEANS: A reader comparing the FY2025 and FY2026 reports side by side would conclude the group's largest off-balance-sheet exposure fell 99.998%; a reader with only FY2026 would never know it existed. Neither reader is being told what happened, and the item is not small — it was larger than the entire consolidated balance sheet. Whatever the true answer, the consequence is identical: BSE's disclosure of the group's off-balance-sheet obligations arising from clearing is now qualitative where it used to be quantified, in the one part of the business where the tail risk lives.
BASE-RATE: Has an interoperability or inter-CCP collateral exposure ever cost money? Not at BSE and not in India — no clearing corporation default has been realised since interoperability went live in June 2019, and BSE's own Core SGF has never been drawn on in the window. But the base rate that matters is the disclosure one: this is the second time in two years that a quantified BSE contingent-liability disclosure has been replaced by a management assertion (the other is the "remote" grading, next finding), and W2_industry has already established two cases (RF-021, RF-025) where a favourable BSE presentation was refuted by the company's own numbers.
S6 IMPLICATION: The group's off-balance-sheet clearing exposure is now unmeasurable from the annual report, which bounds any assessment of the quality of the asset base: the balance sheet is complete only if the ₹10,60,000 lakh really was never a Group obligation. That is an assumption the reader must now make rather than verify, and it argues for a wider margin of safety on the clearing subsidiary's contribution to value than on the exchange's. Monitorable with a trigger: whether the FY2027 note either restores a quantified guarantee line or states the accounting basis for its removal; and separately whether ICCL's inter-CCP collateral is disclosed in the SEBI-mandated risk disclosures on the BSE website. Thesis-breaker: evidence that ICCL still gives inter-CCP bank guarantees of this order while the note shows ₹23 lakh.
SEVERITY: High

### FINDING: A probability grading disclosed for eight straight years was deleted in the first year the underlying claims rose
S1 WHAT: From FY2017 to FY2025, in both blocks, BSE disclosed "Claims not acknowledged as debts" **and** a second row, *"Out of the above, in the opinion of the Management are remote"*. The second row is absent from FY2026 — the year the first row rose 29.2% consolidated and 31.2% standalone, its first material increase in the window.
S2 WHY: Ind AS 37.86 requires disclosure of possible obligations but explicitly does not require disclosure where the possibility of outflow is remote. BSE was therefore volunteering both the number and its own grading. Removing the grading is permitted; what it does is convert a disclosure that told the reader the exposure was priced at zero into one that says nothing about probability at all. The note gives no reason.
S3 EVIDENCE: The grading ran at essentially 100% for eight years — 10,370 of 10,401 (FY2017), 10,362 of 10,362 (FY2018), 51,281 of 51,282 (FY2019), 16,777 of 16,778 (FY2020), 10,351 of 10,352 (FY2021), 10,590 of 10,591 (FY2022), 10,556 of 10,557 (FY2024), 10,504 of 10,504 (FY2025). The counter-proportion: across those eight years the population itself was flat — it moved from 10,401 to 10,504, a total of +1.0% over eight years — and then rose `13,567 ÷ 10,504 = +29.2%` in one year. Total consolidated claims rose `(13,496 + 5,930 + 13,567) ÷ (11,170 + 2,210 + 10,504) = 32,993 ÷ 23,884 = +38.1%`, or 13.2% of FY2026 PAT attributable. The note did not shrink: FY2026 **added** a third footnote on Clearing and Settlement Activities `[AR FY26, Note 37 fn 3, PDF p227/pr216]`, so space was not the constraint.
S4 CONNECTS: The tax half of the claims population is independently visible through CARO 3(vii)(b), and ties to the rupee — `574.74 + 303.74 + 243.18 + 158.05 + 1,297.92 + 3,023.72 + 1,404.44 = 7,005.79` against the standalone note's 7,006, and `127.43 + 117.31 = 244.74` against 245 `[AR FY26, PDF p246/pr235]`. CARO also reveals what the note conceals: the oldest live income-tax dispute is AY2010-11, sixteen years old, at the High Court. This is the same year in which the SEBI regulatory-fee note was deleted (§3.3) and the guarantee line was restated to near-zero (previous finding) — three quantified disclosures removed from one report.
DOMAINS: Notes, Governance, IncomeStatement, Industry
DISCONFIRM: Sought and partly found. Many Indian filers never disclose a remote grading at all, so BSE removing it brings it in line with common practice rather than below it, and Ind AS 37 does not require it — this is a genuine mitigant and it is why the finding is Medium and not High. Against that: the compensating control a reader would reach for is CARO 3(vii)(b), and the class of error CARO cannot catch is precisely the non-tax half — the ₹13,567 lakh of customer and vendor claims, which CARO does not cover at all and which is the row whose grading was removed. Also recorded: the individual amounts are small relative to PAT, and management's grading was empirically right for eight consecutive years.
S5 MEANS: The information content of the deleted row was the entire difference between "₹135.7 crore of claims, all of which we consider remote" and "₹135.7 crore of claims". BSE removed its own probability opinion in the first year the number moved, and offered no substitute. A disclosure that stops in the year its subject deteriorates is a fact about the disclosure decision, not only about the claims.
BASE-RATE: Has it ever cost money? Twice, in the window, and both times through the regulatory channel rather than the customer one. FY2020: SEBI's 2005–2017 inspection produced a ₹1,037 lakh plough-back to ISF/IPF that became ₹1,861 lakh charged and provided `[AR FY2020, Note 36 fn 3, PDF p227/pr220]`. FY2024–FY2025: the SEBI differential regulatory fee produced ₹16,977 lakh of provision and then ₹22,421 lakh of charge across two years (RF-019), 21.8% of FY2024 PAT — an obligation that was not even a contingent liability before the 26-Apr-2024 letter. So at this company the realised losses have come from items the contingent-liability note did not carry, which weakens rather than strengthens the reliance a reader can place on the note either way.
S6 IMPLICATION: The claims population is now a number without a probability, and the reader must supply the grading BSE withdrew. Sized at 13.2% of PAT attributable it does not move the value of the business, but the disappearance is a governance signal about what this management removes from disclosure when it moves against them, and that signal is worth more than the ₹330 crore. Monitorable with a trigger: whether FY2027 restores the grading, and whether the claims line continues to rise. Thesis-breaker for the disclosure-quality reading: a FY2027 note that reinstates the row would show FY2026 was an editing choice rather than a judgement change.
SEVERITY: Medium

### FINDING: Both of the window's major accounting-standard transitions were booked at zero, and Ind AS 116 is still being asserted away
S1 WHAT: BSE adopted Ind AS 115 in FY2019 stating *"There was no impact on the adoption of the standard on the financial statements of the Group"*, and has stated in every Lease note from FY2020 to FY2026 that *"there are no lease contracts for which IND AS 116 – Leases is required to be applied"* — while the same statements carry a lease liability, a lease-security footnote on PPE, an operating-lease expense and a complete right-of-use accounting policy.
S2 WHY: For Ind AS 115 the zero is defensible on measurement — an exchange billing transaction charges monthly in arrears has little to re-time — but the standard's disclosure package is not conditional on the transition amount, and BSE carried forward Ind AS 18 policy wording including *"the percentage of completion method"*, a method Ind AS 115 does not contain. For Ind AS 116 the assertion is not defensible against the company's own numbers: a lessee with a recognised lease obligation and a lease secured by the lessor's title to the asset is inside the standard's scope by definition.
S3 EVIDENCE: Ind AS 115 disclosures required by paragraphs 114–122 and delivered: **zero of four** — "disaggregat", "contract asset", "contract liabilit" and "remaining performance obligation" return no hits in FY2024, FY2025 or FY2026 (W1_docmap §6 #8, re-verified). The counter-proportion: the de facto contract balances are all present and all unlabelled — unbilled receivables ₹50,637 lakh, income received in advance ₹2,901 + ₹1,753 lakh and advance from customers ₹4,475 lakh `[AR FY26, Note 19, PDF p208/pr197]`, together ₹59,766 lakh, **12.4% of revenue from operations**, none of it presented under the standard that governs it. Ind AS 116 disclosures required by paragraphs 53 and 58 and delivered: **zero of seven**, against a lease liability of ₹2 lakh, an operating-lease expense of ₹141 lakh and a lease-security footnote, all in the FY2026 statements `[AR FY26, Note 16 and Note 28 and Note 3, PDF p206 and p213 and p181/pr195 and pr202 and pr170]`. The contrast that dates it: FY2019, under the superseded Ind AS 17, published a full finance-lease maturity table `[AR FY2019, Note 31, PDF p203/pr194]`.
S4 CONNECTS: The missing Ind AS 115 disaggregation is what forces RF-003 — the equity-derivatives concentration that carries the investment case is disclosed only in the MD&A, on which no auditor has opined. The missing contract-liability label is what makes the unbilled receivable of §7 unreadable as a contract asset. And the FY2026 consolidated auditor's report carries **Information Technology systems and controls** as its only Key Audit Matter `[AR FY26, PDF p155/pr144]` — the audit's stated area of focus is systems, not disclosure completeness, in the year both gaps persist.
DOMAINS: Notes, IncomeStatement, Governance, MgmtCommentary
DISCONFIRM: Sought and substantially found on materiality, which is why this ships at Medium. The lease amounts are trivially small — ₹2 lakh of liability against ₹13,44,614 lakh of assets — so no ratio, covenant or margin in the model is misstated, and no user is misled about the economics. The Ind AS 115 zero-impact conclusion is plausible on the facts of an exchange. Nine consecutive unmodified audit opinions and an unmodified internal-financial-controls opinion in every year stand against the finding. What survives the disconfirmation is not a measurement error but a pattern: on the two occasions in nine years when a new standard required BSE to rebuild a disclosure, it asserted the standard away and kept the old note.
S5 MEANS: The Ind AS 116 sentence is falsified by three other places in the same document, which makes it the cheapest available test of how carefully BSE's boilerplate notes are maintained — and it fails. That matters more than the ₹2 lakh, because the same note-drafting process produces the SEBI regulatory-fee note that was deleted, the guarantee comparative that was restated without explanation, and the cash-flow footnote that carries a ₹19,857 lakh change. Read together, these are one finding about disclosure control, not four separate ones.
BASE-RATE: Has an unapplied disclosure standard ever cost money here? No — there is no restatement, no qualification and no regulatory action on any Ind AS disclosure matter in nine years. In the wider Indian system, ICAI's Financial Reporting Review Board and NFRA have issued observations against listed filers for exactly these two omissions (Ind AS 115 contract-balance disclosure and Ind AS 116 lessee disclosure), but no penalty of consequence has followed for a company of this profile. The realised cost so far is zero, and stating that is the point: this is a demonstrated control weakness with an undemonstrated loss.
S6 IMPLICATION: No number in the model changes. What changes is the weight a reader can put on any BSE note that has not been independently corroborated — and this wave found four that could not be. For the earnings-quality gate the relevant input is that the two disclosures which would let an outsider verify revenue timing (Ind AS 115 contract balances) and off-balance-sheet obligation (Ind AS 116 maturity analysis) are both absent by assertion rather than by exemption. Monitorable: whether the FY2027 Lease note is rewritten now that FY2026 capex tripled and buildings entered the asset base at ₹18,585 lakh net. Thesis-breaker: an Ind AS 115 disaggregation note appearing would remove the largest single gap in the revenue chain.
SEVERITY: Medium

### FINDING: The receivable blow-out is entirely unbilled, and the loss rate on the newest bucket was cut by two-thirds in the same note
S1 WHAT: Group gross trade receivables rose 87.1% against revenue of +63.5%, but billed receivables rose only 14.7% — the whole movement is unbilled, which grew 128.3% to ₹50,637 lakh and now carries a 0% expected loss rate. In the same note the expected loss rate on the under-six-month bucket was cut from 39% to 13% consolidated and 47% to 13% standalone, with no reason given, and the parent released ₹284 lakh of provision.
S2 WHY: The mechanism for the unbilled growth is a billing-cycle extension, not a collection failure: unbilled days went from 27.4 to 38.2 while the stated credit period is 0 to 60 days, and both the parent and the group move the same 10.8 days, so it is a parent-level invoicing cadence change. The mechanism for the ECL cut is not disclosed at all; the only method disclosure is *"a practical expedient by computing the expected credit loss allowance for trade receivables based on a detailed analysis of trade receivable by individual departments"*, which describes a method, not a change of assumption.
S3 EVIDENCE: `50,637 ÷ 65,109 = 77.8%` of gross receivables are unbilled against `22,184 ÷ 34,802 = 63.7%` a year earlier; the counter-proportion is that billed receivables are only `14,472 ÷ 12,618 = +14.7%`. Sized: `50,637 ÷ 4,83,395 × 365 = 38.2` days against `22,184 ÷ 2,95,734 × 365 = 27.4` days, and `10.8 × 1,324 = 14,300 lakh` of revenue accrued beyond the prior year's pace, **5.7% of PAT attributable of 2,49,698**. On the ECL: the group allowance rose 62.6% but the group **charge** rose only 10.7% (`4,025 ÷ 3,635`), and the second counter-proportion is the split — subsidiaries hold `12,373 ÷ 65,109 = 19.0%` of gross receivables but `7,499 ÷ 9,793 = 76.6%` of the allowance, against 30.8% and 53.0% a year earlier; the parent's own allowance **fell** from 2,834 to 2,294 while its gross receivables rose 119.1%. Group ECL rate on billed receivables: `6,024 ÷ 12,618 = 47.7%` to `9,793 ÷ 14,472 = 67.7%`.
S4 CONNECTS: The dedicated *Impairment loss on financial assets* note that would have carried this movement was dropped after FY2017 (§4 #4), so the ₹4,065 lakh charge now sits as one line among twenty-five in Other expenses. No Ind AS 115 contract-asset disclosure exists to label the ₹50,637 lakh unbilled balance (previous finding). And the group's revenue is dominated by equity-derivative transaction charges billed to a small member population (RF-020, RF-023) — a population whose concentration is structurally undisclosed, so no counterparty view of the receivable is available from any filing.
DOMAINS: BalanceSheet, IncomeStatement, Notes, Business, Industry
DISCONFIRM: Sought and it materially weakens the alarming reading. Transaction charges are billed monthly in arrears, so an exchange whose Q4 revenue is far above the prior Q4 will mechanically carry more unbilled — and 38.2 days is inside the stated 0-to-60-day credit period, so nothing is past due. The ageing supports this: the 1–2 year bucket is `2,922 ÷ 65,109 = 4.5%` of gross and is 100% provided, and every bucket beyond one year is 100% provided in FY2026 against 46% and 99% in FY2025 — the older book got **more** conservative, not less. Write-offs fell and no bad debt of size was taken. What survives is narrower and sharper: the 10.8-day extension is real and unexplained, and the under-6-month rate cut is a genuine assumption change with no stated basis.
S5 MEANS: Two-thirds of BSE's gross receivable is now an unbilled accrual carried at zero expected loss, up from under two-thirds, in a book where the ECL rate on everything that *has* been billed is 67.7%. The exchange is not failing to collect — it is invoicing later, and the provision it holds against the part it has invoiced has become almost entirely a subsidiary phenomenon while the parent released. Neither of those two movements is explained anywhere in the report, and the note that used to explain impairment was deleted eight years ago.
BASE-RATE: Has BSE's receivable book ever produced a realised loss? Yes, routinely and at scale, which is what makes the 67.7% ECL rate on billed receivables credible rather than alarming: listing fees billed to suspended and non-compliant listed companies are structurally uncollectible, and the company has written off ₹256 lakh (FY2026), ₹452 lakh (FY2025) and ₹277 lakh (standalone FY2025) in the window, with credit-impaired balances of ₹1,958 lakh carried on the face of the note. So the base rate is established and it is high — which is exactly why cutting the under-6-month rate from 39% to 13% without explanation is the part that needs an answer.
S6 IMPLICATION: The reported PAT contains roughly ₹14,300 lakh — 5.7% of attributable profit — of revenue that has been recognised but not yet invoiced beyond the prior year's billing pace, and a provision release at the parent that was not explained. Neither is large enough to change the earnings picture, but both point the same way, and together they mean FY2026 earnings quality is slightly worse than the headline conversion suggests. Monitorable with a trigger: whether unbilled days stay near 38 or revert toward 27 in FY2027, and whether the under-6-month loss rate stays at 13%. Thesis-breaker: unbilled days extending past the 60-day stated credit period, at which point the balance stops being a timing item.
SEVERITY: Medium

### FINDING: A ₹7.25 crore CGST demand appears in the sustainability report and in neither of the two places in the financial statements where it belongs
S1 WHAT: The Principal Commissioner of CGST, Mumbai South passed an order under section 73 on 17-Dec-2025 demanding ₹6,59,26,901 of GST plus ₹65,92,690 of penalty and unquantified interest — ₹7,25,19,591 in total — alleging excess input tax credit availed by BSE Limited for Apr-2021 to Mar-2022. BSE appealed on 06-Mar-2026. Both dates are inside FY2026. It is disclosed only in the BRSR, and appears in neither the standalone contingent-liability note nor CARO 3(vii)(b).
S2 WHY: The two financial-statement disclosures are drawn from the same population — §3.2 shows they tie to the rupee — so a single exclusion decision removed the item from both. The BRSR table it does appear in is headed *"fines / penalties / punishment / award / compounding fees / settlement amount **paid** in proceedings"*, which is the wrong table for a demand under appeal, so the item has been placed in the one disclosure whose caption does not fit it and omitted from the two whose captions do.
S3 EVIDENCE: Standalone *Indirect tax matters* is ₹245 lakh at FY2026 and it **fell** from ₹302 lakh `[AR FY26, Note 36, PDF p302/pr291]` — and `127.43 + 117.31 = 244.74` shows that ₹245 lakh is entirely the two CESTAT service-tax matters, leaving no room for ₹725 lakh. CARO 3(vii)(b), which covers *"dues of goods and services tax … which have not been deposited on account of any dispute"*, carries **no GST row at all** `[AR FY26, PDF p246/pr235]`. The counter-proportion that makes the omission visible rather than arguable: the **consolidated** indirect-tax contingent liability rose `5,930 ÷ 2,210 = +168.3%`, an increase of ₹3,720 lakh, while the **standalone** fell ₹57 lakh — so the entire group increase sits in subsidiaries in the very year the parent received a ₹725 lakh demand.
S4 CONNECTS: The "of which remote" row that would have been the natural home for a demand management assesses as unlikely to crystallise was deleted from the same note in the same year (finding three). The FY2026 CARO group table shows 3(vii)(b) qualifications at BSE Limited, BSE Technologies and Indian Clearing Corporation `[AR FY26, PDF p160/pr149]` — three of five rows are disputed statutory dues, so this is the group's most common audit exception. And BSE's Audit Committee and the Chief Financial Officer signed both the BRSR and the financial statements on 7-May-2026, so the two disclosures were prepared in the same cycle.
DOMAINS: Notes, Governance, IncomeStatement, Business
DISCONFIRM: Sought, and one benign reading survives: if BSE deposited the demand in full before 31-Mar-2026, it is correctly outside CARO 3(vii)(b) — which captures only undeposited dues — and correctly outside the contingent-liability note, because a paid amount under appeal is a recoverable, not a contingency. That reading is available and cannot be excluded from the annual report. But it does not close the gap, because the ₹725 lakh would then have to appear as an expense in Note 28 or as a recoverable in Note 13 or Note 21, and no such amount is identifiable in either. Also recorded in BSE's favour: the amount is 0.29% of PAT attributable, the appeal was filed within the statutory window, and section 107 requires only a 10% pre-deposit, so full payment would have been voluntary.
S5 MEANS: A live tax demand against the parent, ordered and appealed inside the reporting year, is legible only to a reader who opens the BRSR — a section of the annual report that carries no auditor opinion on its monetary tables and that most financial readers never open. The financial statements and CARO, which are audited and which are where the item belongs, both show a smaller indirect-tax exposure than the year before. That is a completeness failure in the disclosure whose entire purpose is completeness.
BASE-RATE: Has an indirect-tax dispute ever cost BSE money? Yes — service-tax demands for FY2005-06 to 2008-09 and FY2014-15 to Jun-2017 have been live at CESTAT for between nine and twenty-one years and remain unresolved at ₹245 lakh, so the realised loss to date is zero but the realised *duration* is a decade-plus. Across the window BSE's actual regulatory cash losses came from SEBI, not from tax: ₹1,861 lakh (FY2020 ISF/IPF) and ₹22,421 lakh (FY2024–FY2025 differential regulatory fee, 21.8% of FY2024 PAT). Input-tax-credit denials of this type routinely settle at a fraction of the demand at first appeal, so the expected loss is well below ₹725 lakh.
S6 IMPLICATION: The exposure itself is immaterial — under 0.3% of PAT — and does not move the earnings stream or the asset base. What it does is establish that BSE's contingent-liability note is not complete as at FY2026, which is the same note whose probability grading was deleted and whose guarantee line was restated to near-zero. Three independent defects in one note in one year is the finding; the ₹725 lakh is only how it was detected. Monitorable with a trigger: whether the FY2027 note restates the FY2026 indirect-tax comparative upward, which would confirm the omission. Thesis-breaker: locating the ₹725 lakh as a FY2026 expense or recoverable would resolve it entirely.
SEVERITY: Medium

### FINDING: CWIP and intangibles-under-development ageing has been absent from the consolidated statements for five years while the standalone carries both
S1 WHAT: Schedule III Division II requires an ageing schedule for capital work-in-progress and for intangible assets under development, plus a completion schedule for overdue projects. The consolidated notes of FY2022, FY2024, FY2025 and FY2026 contain exactly two ageing schedules each — trade receivables and trade payables — and neither of the two development schedules. Both assets sit on the face of the consolidated balance sheet with no note reference at all. The standalone carries both schedules in every one of those years.
S2 WHY: Not a scope question — the standalone preparer produced both schedules from the same underlying ledger, so the data exists and the consolidation pack simply does not carry them forward. The balance-sheet face makes the omission structural rather than incidental: lines b. (CWIP) and f. (intangible assets under development) are the only two asset lines on the consolidated balance sheet with a blank note-reference column.
S3 EVIDENCE: Searched each consolidated notes block in full for "ageing": FY2022 (PDF 154–224) returns 10.6 and 20.2 only; FY2024 (PDF 162–236) returns 10.6 and 20.2 only; FY2025 (PDF 162–219) returns 10.5 and 20.1 only; FY2026 (PDF 169–240) returns 10.5 and 20.1 only. The amounts omitted are CWIP ₹3,255 lakh and IAUD ₹4,420 lakh at FY2026 `[AR FY26, PDF p163/pr152]`. The counter-proportion that makes it matter: CWIP **fell** 20.1% (`3,255 ÷ 4,073`) while IAUD **rose 230%** (`4,420 ÷ 1,339`) — the two lines moved in opposite directions by large percentages in the same year, which is precisely the situation an ageing and completion schedule exists to explain, and precisely the year it is missing. The standalone equivalents are at `[AR FY26, Note 3.1, PDF p264/pr253]` and `[AR FY26, Note 6, PDF p266-267/pr255-256]`.
S4 CONNECTS: FY2026 is the year capex tripled to ₹51,516 lakh and net buildings went from ₹1,778 lakh to ₹18,585 lakh `[AR FY26, Note 3, PDF p181/pr170]`, so the development pipeline is the largest it has been in the window. W2_promise established that management's ~₹500 crore capex framing was met and exceeded, and withdrew an earlier concern that capex was hiding in uncapitalised CWIP — a withdrawal made on the standalone schedule, because the consolidated one does not exist. The auditor's only consolidated Key Audit Matter in FY2026 is IT systems and controls, and CARO carries no observation on Schedule III completeness.
DOMAINS: BalanceSheet, Notes, Governance, MgmtCommentary
DISCONFIRM: Sought and found on materiality, which caps this at Medium. The combined ₹7,675 lakh is 0.57% of consolidated total assets, below any quantitative materiality threshold an auditor would set, and the standalone schedules cover the parent, which is where the overwhelming majority of the group's development spend sits — so a determined reader can substantially reconstruct the consolidated position. Nine unmodified audit opinions and unmodified internal-financial-controls opinions stand against the finding, and no peer comparison was available within this wave to establish whether omitting these two schedules from consolidated statements is common practice in Indian listed groups.
S5 MEANS: The one disclosure that would show whether capitalised development cost is stalling is missing from the consolidated statements, in the year intangibles under development more than tripled. The class of error the standalone schedule cannot catch is exactly the subsidiary one — BSE Technologies and ICCL both build software, and any stalled project there is invisible in both blocks.
BASE-RATE: Has capitalised development ever gone wrong at BSE? Not in the window: there is no impairment of intangible assets under development in any year, no write-off of CWIP, and the only goodwill impairment in FY2026 is ₹4 lakh `[AR FY26, Note 28, PDF p213/pr202]`. So this is a theoretical risk at this company, and it is recorded as such. In the wider system, indefinitely-carried intangibles under development are among the most common Indian audit-observation and NFRA-review findings, which is why Schedule III added the completion schedule in the first place.
S6 IMPLICATION: A five-year, unremarked Schedule III omission in the consolidated statements is a control observation rather than a valuation one — the sums are too small to move the asset base. Its value is as corroboration: this wave found the same drafting process producing an Ind AS 116 assertion contradicted by three other notes, a deleted regulatory-fee note, a restated guarantee comparative and an unquantified cash-flow basis change. Monitorable: whether the FY2027 consolidated notes add the two schedules now that the development pipeline has tripled. Next check: FY2027 annual report, consolidated notes 3 and 6.
SEVERITY: Medium

### FINDING: Three quantified disclosures were removed from one annual report, and the items behind two of them grew
S1 WHAT: FY2026 deleted the SEBI Regulatory fees note, the contingent-liability "of which remote" grading, and the ₹10,60,000 lakh guarantee disclosure. It also deleted the Buyback note and the Liquidity Enhancement Scheme note. Of the five, two items genuinely ceased and three did not: the SEBI fee grew 70.8%, the claims population grew 29.2%, and there is no evidence the ICCL guarantee obligation ended.
S2 WHY: The stated mechanisms are presentational in each case — the SEBI fee was absorbed into a new Regulatory contribution aggregate, the LES expense moved from the P&L face into the Other-expenses note, the buyback ended. But no note in FY2026 explains any of the three that matter, and in two of the three the deletion coincides with the largest movement the item has ever recorded. The common cause is not stated anywhere; what can be observed is that FY2026 is the first year with an independent reasonable-assurance report on BRSR Core, a merged revenue note, a deleted exceptional-item line and a merged expense taxonomy — a general consolidation of the report's granularity.
S3 EVIDENCE: SEBI regulatory fees `56,616 ÷ 33,141 = +70.8%` with the note gone `[AR FY26, Note 27, PDF p212/pr201]` against `[AR FY25, Note 46, PDF p217/pr206]`. Claims not acknowledged `13,567 ÷ 10,504 = +29.2%` with the grading gone. Guarantees ₹10,60,024 → ₹23 with the FY2025 comparative restated to ₹24. The counter-proportion that separates disclosure-cessation from item-cessation: of the six disclosures W1_docmap flagged as having stopped, only **two** (Specified Bank Notes, buyback) correspond to an item that actually ceased, and one (LES) is genuinely both — the India INX scheme continues at ₹556 lakh inside Note 28 while BSE's own SEBI-circular scheme ended in FY2023. **Three of six are live and in two cases growing items whose disclosure stopped.**
S4 CONNECTS: The same report merged two revenue notes into one and dropped *Company reinstatement fees* as a line (RF-004); dropped the exceptional-item line; and moved three revenue streams off the P&L face into Note 22. Against that, FY2026 also **added** disclosure: a reasonable-assurance report on BRSR Core KPIs `[AR FY26, PDF p103-105/pr92-94]`, a discontinued-operation note with a full assets-and-liabilities disposal table `[AR FY26, Note 49, PDF p238-239/pr227-228]`, and the Clearing and Settlement Activities footnote. The direction is not uniformly toward less.
DOMAINS: Notes, Governance, MgmtCommentary, IncomeStatement
DISCONFIRM: Sought and found in three places, and it constrains the finding. (1) FY2026 added disclosures as well as removing them, listed above, so "reducing transparency" is too strong as a general characterisation. (2) The buyback and SBN deletions are correct and expected — the items ceased. (3) None of the removed disclosures was required: the "remote" grading is optional under Ind AS 37.86, a dedicated SEBI-fee note is not mandated once the amount sits in a disclosed expense line, and the LES note related to a scheme that ended. What survives is the pattern in the *subset*: where a disclosure was removed over a live item, the item was growing in two of three cases, and in the third the comparative was restated to make the item disappear retrospectively.
S5 MEANS: A reader tracking any of the three growing items across FY2025 and FY2026 loses the thread in the year the number moves most. Individually each deletion is defensible; taken together they mean the FY2026 annual report is materially less traceable than FY2025 on exactly the three items — regulatory cost, litigation exposure and clearing-guarantee exposure — that carry the company's largest non-operational risks. This is the disclosure-quality input the earnings-quality gate should carry forward, and it is what distinguishes a company whose numbers are hard to follow from one whose business is hard to follow.
BASE-RATE: Have BSE's own removed disclosures ever preceded a loss? Once, and it is the closest analogue available. The SEBI regulatory-fee matter was disclosed as a discrete note in FY2024 with a ₹16,977 lakh provision made *"based on the prudence"* while the company intended to contest; by FY2025 the contest was abandoned and by FY2026 the note was gone and the cost was ₹56,616 lakh — a `56,616 ÷ 17,212 = 3.29×` rise over the restated base in two years. So the one item in this set with a realised outcome went from note, to acceptance, to no note, while tripling. That is the base rate, and it is one for one.
S6 IMPLICATION: Three of the company's largest risk exposures — the regulatory levy, the litigation book and the clearing guarantee — are now less traceable than they were a year ago, which widens the margin of safety a reader should require on each of them without changing any reported number. For the red-flag gate the relevant input is that none of these deletions was accompanied by an explanation, so none can be distinguished from a deliberate reduction in traceability on the evidence available. Monitorable with a trigger and a date: the FY2027 annual report, May 2027 — whether the SEBI fee regains a note now that it is the third-largest expense, whether the remote grading returns, and whether the guarantee line is either restored or explained. Thesis-breaker: any one of the three reappearing with a stated basis would reduce this from a pattern to three coincidences.
SEVERITY: Medium

---

## 10. HANDOVER

**Closed by this wave.**
- **RF-027 CLOSED as to cause.** The FY2024 CFO restatement has a stated reason — an unquantified
  footnote recording a change in the basis of preparation — and 99.3% of it reconciles to four deleted
  Core SGF lines (§2.2, F-1). The ledger's 19,679 should read **19,857** on a total-operations basis.
- **RF-008 CLOSED as to mechanism, OPEN as to substance.** The ₹10,60,000 lakh was ICCL's Inter-CCP
  bank guarantee under SEBI's interoperability framework. The FY2026 report restated the FY2025
  comparative to ₹24 lakh, so it is a **disclosure-basis change applied retrospectively**, not a
  structural change in the year (§3.3, F-2). Whether the underlying obligation still exists is not
  answerable from the annual report.
- **RF-009 CLOSED as to fact.** Eight years of ~100% "remote" grading, deleted in the year the
  population rose 29.2% (§3.2, F-3).
- **RF-026 SUPPORTED and refined.** The receivable growth is entirely unbilled and inside terms; the
  sharper findings are the 10.8-day unbilled extension (~₹14,300 lakh, 5.7% of PAT) and the
  unexplained cut in the under-6-month expected loss rate (§7, F-5).
- **W1_docmap §5.8 adjudicated.** Three of six stopped disclosures cover live items; one (LES) is both
  (§4).

**New for the gap register.**
| Gap | Severity | Settling document |
|---|---|---|
| Quantification of the FY2025 cash-flow basis change | High | FY2025 quarterly limited-review filings, to date when the presentation first changed |
| Accounting basis for removing the ₹10,60,000 lakh guarantee, and whether ICCL still gives it | High | ICCL's own MCA-filed FY2026 financial statements; SEBI-mandated ICCL risk disclosures |
| Whereabouts of the ₹7.25cr CGST demand in the FY2026 financial statements | Medium | BSE FY2026 Form 3CD / GST annual return; FY2027 comparative |
| Which subsidiary holds the ₹7,499 lakh of trade-receivable ECL | Medium | subsidiaries' MCA-filed financial statements |
| Consolidated CWIP and IAUD ageing, FY2022–FY2026 | Medium | none exists — Schedule III requires it and it was not filed |
| Funding-party clause in the consolidated Schedule III additional information | Medium | standalone Note 49(vii) covers the parent only |
| Ind AS 115 contract balances and Ind AS 116 lessee disclosures | Medium | none exists in any year |
| The residual ₹3,124 lakh of the FY2018 equity restatement (R-06) | Low | no note in any year quantifies it |

**Contradictions preserved for QC (doctrine §10).**
1. `records/restatements.md` rules the FY2018 PAT movement an ARTIFACT; this wave records a real
   FY2018 PAT restatement of −2,256, stated and quantified in FY2019 Note 30 fn 2. Both stand — the
   artifact ruling is correct for the comparison it was made against.
2. `W1_ledger` §1.7 #6 gives the FY2024 CFO restatement as 19,679 and unexplained; this wave gives
   19,857, explained by footnote. Both stand.
3. `W1_docmap` §5.8 #3 states neither the LES note nor the LES P&L line appears in FY2026; the LES
   *note* is indeed gone and BSE's own scheme did end, but an India INX LES expense of ₹556 lakh and
   an LES reserve of ₹9 lakh are both live in FY2026. Both stand.
