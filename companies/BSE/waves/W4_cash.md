# W4 — Cash flow and the ₹100 map: BSE Limited (consolidated), FY2026

**Agent:** W4_cash. **Date:** 2026-09-08. **Basis:** consolidated, total operations, unless stated.
Unit `₹ lakh`, matching the annual report's own `(₹ in Lakhs)`. Printed-page offsets from
`W1_docmap.md` §0.1 and confirmed in each page body: FY2017 +2 · FY2018 +7 · FY2019 +9 · FY2020 +7 ·
FY2021 +5 · FY2022 +9 · **FY2023 +7 (established here, from the page body "202" at PDF p209)** ·
FY2024 +6 · FY2025 +11 · FY2026 +11.

**What this file is for.** Doctrine §6: the ₹100 map is L1→L7 run across the whole P&L and summed into
one frame. Overlay `W1.7_mii_overlay.md` §2 makes that impossible to do honestly on the reported
numbers, because most of this balance sheet — and, it turns out, most of this year's operating
cash inflow — is not the company's money. So the map is built **twice**, and the difference between
the two is the deliverable.

**Prior work used, not rebuilt.** `W1_ledger.md` §3 (the float separation), `W3_balancesheet.md` §4 F2
and F4 (the ₹15,584 capital advance, the CDSL dividend), `W3_notes.md` §2.2 (RF-027, the FY2025
cash-flow basis change), `W3_cost.md` chain 7 (the Core SGF L7 break), `W3_group_rpt.md` §4.5–5.2 (the
ICCL transfer price and the associate dividend), `records/trend_10y.csv` and
`records/balance_cash_10y.csv` as corrected by W1_ledger. **Nothing here overwrites an earlier
position.** Where I disagree, both sides are stated with their evidence (doctrine §10); three such
disagreements are recorded in §1 and §8.

---

## 0. What this file settles, in five lines

1. **The CDSL dividend contradiction settles in W3_group_rpt's favour on the principle and against it
   on the consequence.** The omission is real, it breaches Ind AS 7, and it has run for **eight years,
   not two — ₹18,100 lakh**. But consolidated CFO is **not** overstated by it: the operating section
   reconciles line by line to the notes within ₹600 lakh in aggregate, and the money is absorbed
   inside the investing section. §1.
2. **The ten-year own-account conversion test CAN be run.** `W1.5_triage`'s finding that it cannot is
   **overturned**: Note 16's Owned / Earmarked / Clearing-and-settlement split exists in **all ten**
   annual reports (Note 18 in FY2017). §3.
3. **Ten-year cumulative own-account CFO / PAT = 0.712, against a headline 1.272.** Not 1.393, not
   0.942. The company has converted roughly **seven-tenths** of a decade of reported profit into
   operating cash it owns. §3.
4. **₹69,188 lakh of the ₹72,767 lakh working-capital inflow that carries FY2026's cash flow — 95.1%
   of it — is other people's money**: ₹24,251 lakh of clearing-member float and ₹44,937 lakh of tax
   collected for the government. §2, F2.
5. **The two maps differ by ₹20.20 of CFO per ₹100 of revenue.** Headline ₹64.21, own-account ₹44.01.
   §2.

---

## 1. THE OPEN CONTRADICTION — the ₹3,919 lakh CDSL dividend, settled

### 1.1 The two positions, as they actually read

Doctrine §10 forbids resolving a contradiction by preferring the later agent. Both positions are
reproduced before either is tested.

| Position | Source, verbatim | Consequence claimed |
|---|---|---|
| **A** | `records/red_flags.md`, RF-028 entry, attributed to W3_balancesheet: *"the consolidated cash flow shows 'Dividend received 1' and its investing section sums to its stated total with no room for the 3,919 — **because at consolidated level the associate dividend is eliminated against the equity-method carrying value. Not a missing cash flow; a consolidation mechanic.**"* | No defect of substance. CFO correct. |
| **A′** | `W3_balancesheet.md` §5 F4, the file the register is summarising, which says something **different**: *"a dividend from an equity-accounted associate **is not eliminated and should survive as an investing inflow. It has not been carried through**"*, and locates the money *"into another investing line — most plausibly netted against 'Investment in fixed deposits (3,29,857)' or 'Interest received 23,798'"*. Severity Watch. | A presentation defect **inside investing**. CFO correct. |
| **B** | `W3_group_rpt.md` §5.2: *"It is the consolidated cash flow that loses it… the 3,919 must be buried inside a working capital line — most plausibly 'Decrease / (increase) in other assets and other financial assets 13,638'. Consequence: **consolidated CFO of 3,10,368 is overstated and investing understated by 3,919**… and the same happened in FY2025 with 3,449 — **7,368 over two years**."* Severity Medium. | **CFO overstated** by ₹3,919 lakh in FY2026 and ₹7,368 lakh over two years. |

**First correction, recorded not resolved:** the register's entry (A) and the file it cites (A′) do not
say the same thing. The register attributes to W3_balancesheet a "consolidation mechanic" defence that
W3_balancesheet's own text explicitly rejects. Both stay on the record. The gloss is what needs
settling, because it is the version a later wave reading only the register would carry forward.

### 1.2 Test 1 — the standard. An associate dividend is not eliminated

Ind AS 7.37: *"When accounting for an investment in an associate, a joint venture or a subsidiary
accounted for by use of the equity or cost method, an investor restricts its reporting in the
statement of cash flows to the cash flows between itself and the investee, for example, to dividends
and advances."* Ind AS 7.31: *"Cash flows from interest and dividends received and paid shall each be
disclosed separately."* Ind AS 7.21 requires major classes of gross investing receipts and payments to
be reported separately rather than netted.

An equity-accounted associate is **outside** the consolidated reporting entity. Elimination applies to
intra-group flows because both sides are inside it; CDSL's ₹3,919 lakh is cash arriving from a
third party. The reduction of the equity-method carrying amount is a **balance-sheet** mechanic with
no cash-flow counterpart — the cash-flow statement is not derived from a carrying amount. **Position A
(the register's gloss) is wrong as a matter of the standard.** Positions A′ and B are both right that
the item should appear and does not.

### 1.3 Test 2 — the empirical proof it is not a mechanic, and that it has run for eight years

The consolidated statements themselves settle it, and they do so more strongly than either agent
found. In **every one of the ten years read**, the consolidated statement of cash flows carries a
"Dividend received" line in investing that is **numerically identical to the "Dividend income"
adjustment deducted in the operating section** — i.e. it is a mechanical mirror of the consolidated
P&L's dividend income, not a record of dividend cash received.

| FY | Operating adjustment *Dividend income* | Investing *Dividend received* | Associate dividend actually received, per the Note 8 roll-forward | Tag (consolidated cash flow · Note 8) |
|---|---|---|---|---|
| 2017 | (1,720) | 1,720 | n/a — CDSL was a **subsidiary** (50.05%) | `[AR FY2017, PDF p118/pr116]` |
| 2018 | (1,633) | 1,633 | nil (first year as associate) | `[AR FY2018, PDF p135/pr128]` |
| 2019 | (1,994) | 1,994 | **1,058** | `[AR FY2019, PDF p149/pr140]` · `[AR FY2019, Note 16A, PDF p174/pr165]` |
| 2020 | (1,302) | 1,302 | **1,209** | `[AR FY2020, PDF p161/pr154]` · `[AR FY2020, PDF p185/pr178]` |
| 2021 | (31) | 31 | **941** | `[AR FY2021, PDF p147/pr142]` · `[AR FY2021, PDF p171/pr166]` |
| 2022 | (11) | 11 | **1,881** | `[AR FY2022, PDF p151/pr142]` · `[AR FY2022, PDF p177/pr168]` |
| 2023 | – | – | **3,135** | `[AR FY2023, PDF p163/pr156]` · `[AR FY2023, PDF p191/pr184]` |
| 2024 | (26) | 26 | **2,508** | `[AR FY2024, PDF p158/pr152]` · `[AR FY2024, PDF p184/pr178]` |
| 2025 | (1) | 1 | **3,449** | `[AR FY25, PDF p158/pr147]` · `[AR FY25, Note 8, PDF p178/pr167]` |
| 2026 | (1) | 1 | **3,919** | `[AR FY26, PDF p165/pr154]` · `[AR FY26, Note 8, PDF p189/pr178]` |

**`DERIVED`: cumulative associate dividend omitted from the consolidated statement of cash flows,
FY2019–FY2026 = 1,058 + 1,209 + 941 + 1,881 + 3,135 + 2,508 + 3,449 + 3,919 = 18,100 lakh**, against
the ₹7,368 lakh W3_group_rpt sized over two years — **2.46× larger** (`18,100 / 7,368 = 2.46`).

The mirror is the mechanism. Under the equity method an associate's dividend **never enters
consolidated P&L income**, so a "Dividend received" line built from the P&L's dividend-income
adjustment **cannot ever carry it**, in any year, by construction. The years FY2019 and FY2020 look
innocent only because mutual-fund dividend income happened to exceed the associate dividend
(`1,994 > 1,058`; `1,302 > 1,209`); the mirror shows they were omitted then too. FY2023 is the clean
demonstration: the group received **₹3,135 lakh** of associate dividend and printed a **dash**.

This is not a consolidation mechanic. It is a preparation artefact, and it is systematic.

### 1.4 Test 3 — where the money went, and whether CFO is overstated

The FY2026 statement foots exactly. `DERIVED`, checked independently: operating adjustments
`2,47,530 + 82,384 − 6,542 + 2,994 + 15,896 + 4 + 4,057 − 8,875 − 20,154 − 1 = 3,17,293`; working
capital `3,17,293 − 30,595 + 1,691 + 1,115 + 13,638 + 72,767 = 3,75,909`; `3,75,909 − 65,541 =
3,10,368`; investing `−51,516 + 59 − 91,484 − 21,520 + 22,081 − 3,29,857 + 1,74,471 + 23,798 + 1 =
(2,73,967)`; `3,10,368 − 2,73,967 − 30,370 = 6,031` `[AR FY26, Consolidated Cash Flow, PDF
p165-166/pr154-155]`. Every subtotal ties, so the ₹3,919 lakh of real cash is inside an aggregate.

**The operating section cannot be that aggregate.** Each of its five working-capital lines reconciles
to its note:

| Working-capital line, FY2026 | Reported | Rebuilt from the notes | Residual | Note tag |
|---|---|---|---|---|
| Trade receivables | (30,595) | `65,109 − 34,802 + 256 = 30,563` | **32** | `[AR FY26, Note 10.4-10.5, PDF p199/pr188]` |
| Trade payables | 1,691 | `13,087 − 11,396 = 1,691` | **0** | `[AR FY26, Note 20, PDF p209/pr198]` |
| Provisions | 1,115 | `(540 + 3,742) − (179 + 2,627) − 201 OCI = 1,275` | **160** | `[AR FY26, Note 17, PDF p207/pr196]` |
| Other assets and other financial assets | 13,638 | `(15,584) + 1,099 + 333 + 192 − 26 − 117 − 256 − 152 = 13,461` | **177** | `[AR FY26, Notes 11 & 13, PDF p200-202/pr189-191]` |
| Other liabilities and other financial liabilities | 72,767 | `Δ(A) 1,701 + Δ(C) 24,251 + Δ Note 19 46,865 + Δ non-current OFL (21) = 72,796` | **29** | `[AR FY26, Notes 16 & 19, PDF p206-208/pr195-197]` |

**`DERIVED`: aggregate absolute residual = 32 + 0 + 160 + 177 + 29 = 398 lakh, 0.13% of CFO
(398 / 3,10,368 = 0.13%).** No operating line has room for ₹3,919 lakh — the largest residual is
**4.1%** of it (`160 / 3,919`). W3_group_rpt's proposed hiding place, *"Decrease / (increase) in other
assets and other financial assets 13,638"*, reconciles to **177**.

**Where it is instead.** `ESTIMATE`, with the assumption stated. Cash interest receivable on owned
funds is the P&L interest income less the increase in accrued interest on owned deposits:
`20,154 − ((2,824 + 5,661) − (325 + 7,886)) = 20,154 − 274 = 19,880`
`[AR FY26, Note 23, PDF p211/pr200]` and `[AR FY26, Notes 11 & 12, PDF p200-202/pr189-191]`. The
statement reports **Interest received 23,798**. `DERIVED: 23,798 − 19,880 = 3,918`, against a CDSL
dividend of **3,919** — a residual of **1 lakh, 0.03%**. Assumption: accrued interest on the
amortised-cost investment book (Note 9, `2,609` against `2,753`, a fall of 144) is settled inside the
bond purchase and proceeds lines rather than inside "Interest received"; if instead it runs through
"Interest received", the unexplained excess is `23,798 − (20,154 − 274 + 144) = 3,774`, still within
**3.7%** of the dividend. Either way the money is in the **investing** section. The alternative
candidate — netting inside *Investment in fixed deposits (3,29,857)* — cannot be excluded, because the
footnote-2 and footnote-3 exclusions make the gross deposit lines unreconcilable to the balance sheet
by design.

### 1.5 The settlement

| Question | Answer | Which position it supports |
|---|---|---|
| Is the omission a normal consolidation mechanic? | **No.** Ind AS 7.37 requires it to be reported; Ind AS 7.31 requires it to be shown separately. | Against **A** (the register's gloss) |
| Is the omission real and recurring? | **Yes — eight years, ₹18,100 lakh, not two years and ₹7,368 lakh.** | For **B**, and larger than B stated |
| Is consolidated CFO of ₹3,10,368 lakh overstated by it? | **No.** All five operating working-capital lines reconcile to their notes; the aggregate residual is ₹398 lakh. | For **A′**, against **B** |
| Where is the money? | Inside **investing**, most consistently inside *Interest received 23,798* (`ESTIMATE`, residual 1 lakh). | For **A′** |
| Net severity | **Medium** — a recurring Ind AS 7.31/7.37 breach that misstates the composition of investing cash flow but not operating cash flow or closing cash. | — |

**RF-028 disposition:** the CDSL-specific point is settled. The **register entry should be corrected**
(it attributes to W3_balancesheet a defence W3_balancesheet does not make), the **window extended from
two years to eight**, and **W3_group_rpt's CFO-overstatement of ₹3,919 / ₹7,368 lakh withdrawn** — with
W3_group_rpt's own position retained on the record alongside, per doctrine §10.

**Why it still matters for the trust test:** the numerator of the conversion test is consolidated CFO,
and this exercise establishes that the *reported* CFO is arithmetically sound and reconciles to the
notes. What is wrong with it is not arithmetic. It is §2.

---

## 2. THE ₹100 MAP, TWICE

**Common scale for both maps: ₹1 = 4,833.95 lakh** (`DERIVED: 4,83,395 / 100 = 4,833.95`). Both maps
use the **same divisor**, so every line is directly comparable; the own-account map therefore starts
below ₹100 rather than being rebased. All FY2026 consolidated, continuing operations for the cash-flow
bridge with discontinued shown separately.

### 2.1 Definitions — what "own-account" removes, and why each item

| Removed | ₹ lakh | Why it is not the shareholders' | Source |
|---|---|---|---|
| *Treasury income from clearing and settlement funds*, inside revenue | **17,142** | Income earned on members' money, booked in the top line. Overlay §2; W3_balancesheet §2 sizes it after tax at 12,861 | `[AR FY26, Note 22, PDF p211/pr200]` |
| Tax on the above, at the reported effective rate | **(4,281)** | `DERIVED: 82,384 / 3,29,914 = 24.97%; 17,142 × 0.2497 = 4,281` | `[AR FY26, Consolidated P&L, PDF p164/pr153]` |
| Movement in Note 16 bucket **(C)** *Clearing and settlement* | **24,251** | Clearing-member and clearing-bank money. Note 12.1 restricts the matching assets | `[AR FY26, Note 16, PDF p206/pr195]` |
| Movement in **statutory remittances** inside Note 19 | **44,937** | Tax collected for the government — ₹51,478 lakh of the closing balance is Securities Transaction Tax | `[AR FY26, Note 19, PDF p208/pr197]` and `[AR FY26, MD&A, PDF p77/pr66]` |
| Release of the FY2025 **capital advance** | **15,584** | Cash that left the company in FY2025, credited to FY2026 operating (RF-046) | `[AR FY26, Note 13, PDF p202/pr191]` |

Two items **not** removed, and the reason recorded: (i) the ₹16,993 lakh of member deposits inside
bucket (A) — W3_balancesheet F6 shows these are member money, but the **movement** is only
`24,992 − 23,291 = 1,701` and stripping it moves own-account CFO by 0.6%, so it is carried as a
sensitivity rather than in the map; (ii) the Core SGF, which footnote 3 already excludes from the
FY2026 statement entirely `[AR FY26, Consolidated Cash Flow footnote 3, PDF p166/pr155]`.

### 2.2 Map A — headline basis, as reported

| Step | ₹ lakh | per ₹100 | running |
|---|---:|---:|---:|
| **Revenue from operations** `[AR FY26, Note 22, PDF p211/pr200]` | 4,83,395 | **100.00** | 100.00 |
| − Employee benefits `[AR FY26, Note 25, PDF p212/pr201]` | (29,781) | (6.16) | 93.84 |
| − Technology `[AR FY26, Note 26, PDF p212/pr201]` | (20,313) | (4.20) | 89.64 |
| − Clearing and settlement `[AR FY26, Consolidated P&L, PDF p164/pr153]` | (28,035) | (5.80) | 83.84 |
| − Other expenses `[AR FY26, Note 28, PDF p213/pr202]` | (24,732) | (5.12) | 78.72 |
| − Depreciation and amortisation `[AR FY26, Notes 3, 4 & 6, PDF p181-184/pr170-173]` | (15,896) | (3.29) | 75.43 |
| − Finance cost | (16) | (0.00) | 75.43 |
| **= Operating profit before levy** | **3,64,622** | | **75.43** |
| − **LEVY** — regulatory contribution `[AR FY26, Note 27, PDF p212/pr201]` | (64,969) | **(13.44)** | 61.99 |
| **= Operating profit after levy** | **2,99,653** | | **61.99** |
| + Investment income `[AR FY26, Note 23, PDF p211/pr200]` | 29,030 | 6.01 | 68.00 |
| + Other income `[AR FY26, Note 24, PDF p212/pr201]` | 2,385 | 0.49 | 68.49 |
| **= Profit before contribution to core SGF** | **3,31,068** | | **68.49** |
| − **CORE SGF** contribution `[AR FY26, Consolidated P&L, PDF p164/pr153]` | (7,696) | (1.59) | 66.90 |
| + Share of associates `[AR FY26, Note 8, PDF p188-189/pr177-178]` | 6,542 | 1.35 | 68.25 |
| **= Profit before tax** | **3,29,914** | | **68.25** |
| − Tax `[AR FY26, Note 29, PDF p213/pr202]` | (82,384) | **(17.04)** | 51.21 |
| **= PAT, continuing** | **2,47,530** | | **51.21** |
| + Discontinued operations | 1,195 | 0.25 | 51.46 |
| **= PAT, total operations** | **2,48,725** | | **51.46** |
| *(cash-flow bridge restarts from continuing PAT 2,47,530)* | | | *51.21* |
| + Non-cash adjustments | 69,763 | 14.43 | 65.64 |
| **= Operating cash flow before working capital** | **3,17,293** | | **65.64** |
| ± **Working-capital absorption** | 58,616 | **+12.13** | 77.76 |
| **= Cash generated from operations** | **3,75,909** | | **77.76** |
| − Direct taxes paid | (65,541) | (13.56) | 64.21 |
| **= CFO, continuing (+4 discontinued)** | **3,10,372** | | **64.21** |
| + Interest and dividend received (investing) | 23,799 | 4.92 | 69.13 |
| + Proceeds from sale of PPE | 59 | 0.01 | 69.14 |
| − **Capex** | (51,516) | **(10.66)** | 58.48 |
| **= Free cash flow (after interest received)** | **2,82,714** | | **58.48** |
| − **Dividend paid** `[AR FY26, Note 15, PDF p205/pr194]` | (31,585) | **(6.53)** | 51.95 |
| − Buyback | 0 | 0.00 | 51.95 |
| + Issue of shares by subsidiary | 1,215 | 0.25 | 52.20 |
| **= Cash available to deploy** | **2,52,344** | | **52.20** |
| − Net deployment into deposits and securities | (2,46,309) | (50.95) | 1.25 |
| **= Increase in cash and cash equivalents** | **6,035** | | **1.25** |

`DERIVED`, deployment: `91,484 + 21,520 − 22,081 + 3,29,857 − 1,74,471 = 2,46,309`. Statement check:
`3,10,368 + 23,798 + 1 + 59 − 51,516 − 2,46,309 − 31,585 + 1,215 = 6,031` continuing, plus 4
discontinued `[AR FY26, Consolidated Cash Flow, PDF p165-166/pr154-155]`.

**Headline conversion: `3,10,372 / 2,48,725 = 1.248`.**

### 2.3 Map B — own-account basis

| Step | ₹ lakh | per ₹100 | running |
|---|---:|---:|---:|
| **Revenue from operations, own-account** `DERIVED: 4,83,395 − 17,142 = 4,66,253` | 4,66,253 | **96.45** | 96.45 |
| − Employee benefits | (29,781) | (6.16) | 90.29 |
| − Technology | (20,313) | (4.20) | 86.09 |
| − Clearing and settlement | (28,035) | (5.80) | 80.29 |
| − Other expenses | (24,732) | (5.12) | 75.17 |
| − Depreciation and amortisation | (15,896) | (3.29) | 71.88 |
| − Finance cost | (16) | (0.00) | 71.88 |
| **= Operating profit before levy** | **3,47,480** | | **71.88** |
| − **LEVY** — regulatory contribution | (64,969) | **(13.44)** | 58.44 |
| **= Operating profit after levy** | **2,82,511** | | **58.44** |
| + Investment income (own corpus) | 29,030 | 6.01 | 64.45 |
| + Other income | 2,385 | 0.49 | 64.94 |
| **= Profit before core SGF, own-account** | **3,13,926** | | **64.94** |
| − **CORE SGF** contribution | (7,696) | (1.59) | 63.35 |
| + Share of associates | 6,542 | 1.35 | 64.70 |
| **= PBT, own-account** | **3,12,772** | | **64.70** |
| − Tax `DERIVED: 82,384 − 4,281 = 78,103` | (78,103) | (16.16) | 48.55 |
| **= PAT, continuing, own-account** | **2,34,669** | | **48.55** |
| + Discontinued operations | 1,195 | 0.25 | 48.80 |
| **= PAT, total operations, own-account** | **2,35,864** | | **48.80** |
| + Non-cash adjustments (unchanged) | 69,763 | 14.43 | 62.98 |
| **= Operating cash flow before working capital** | **3,04,432** | | **62.98** |
| ± **Working-capital absorption, own-account** `DERIVED: 58,616 − 24,251 − 44,937 − 15,584 = (26,156)` | (26,156) | **(5.41)** | 57.57 |
| **= Cash generated from operations** | **2,78,276** | | **57.57** |
| − Direct taxes paid | (65,541) | (13.56) | 44.01 |
| **= CFO, own-account (+4 discontinued)** | **2,12,739** | | **44.01** |
| + Interest and dividend received | 23,799 | 4.92 | 48.93 |
| + Proceeds from sale of PPE | 59 | 0.01 | 48.94 |
| − **Capex, cash, own-account** `DERIVED: 51,516 − 15,584 = 35,932` | (35,932) | **(7.43)** | 41.51 |
| **= Free cash flow, own-account (after interest received)** | **2,00,665** | | **41.51** |
| − **Dividend paid** | (31,585) | **(6.53)** | 34.98 |
| − Buyback | 0 | 0.00 | 34.98 |
| + Issue of shares by subsidiary | 1,215 | 0.25 | 35.23 |
| **= Own-account cash to deploy** | **1,70,295** | | **35.23** |

**Own-account conversion: `2,12,739 / 2,35,864 = 0.902`** (continuing only: `2,12,735 / 2,34,669 =
0.907`).

**The own-account map closes on the balance sheet.** §4a trigger 3, an exact tie-out gating a
conclusion: `DERIVED` — own-account CFO 2,12,735 + interest received 23,798 + dividend received 1 +
PPE proceeds 59 + subsidiary share issue 1,215 + discontinued net 6,195 − cash capex 35,932 −
dividend paid 31,585 + non-cash FVTPL gain 8,875 + after-tax float income retained 12,861 + government
float held 44,937 = **2,43,159**, against the actual increase in own-account financial assets of
`6,14,282 − 3,71,074 = 2,43,208` `[AR FY26, Notes 9, 11 & 12, PDF p190-202/pr179-191]` — **residual 49
lakh, 0.02%.** The construction is not an assertion; it reconciles.

### 2.4 The difference — the deliverable

| Step | Map A, headline | Map B, own-account | Gap, per ₹100 |
|---|---:|---:|---:|
| Revenue | 100.00 | 96.45 | **3.55** |
| Operating profit after levy | 61.99 | 58.44 | 3.55 |
| PAT, total operations | 51.46 | 48.80 | **2.66** |
| Working-capital absorption | **+12.13** | **(5.41)** | **17.54** |
| **CFO** | **64.21** | **44.01** | **20.20** |
| Capex | (10.66) | (7.43) | 3.23 |
| **FCF (CFO − capex)** | **53.55** | **36.58** | **16.97** |
| Dividend paid | (6.53) | (6.53) | 0.00 |
| **CFO / PAT** | **1.248** | **0.902** | **0.346** |

**Read the fourth row first.** The entire gap between the two maps is one step. Profit differs by
₹2.66; cash differs by ₹20.20; and ₹17.54 of that ₹20.20 — **86.8%** (`17.54 / 20.20`) — is the
working-capital line. On the reported presentation working capital **adds** ₹12.13 to every ₹100 of
revenue; on an own-account basis it **absorbs** ₹5.41. The reported map says this business releases
cash as it grows. The own-account map says it consumes it.

**What is inside the ₹72,767 lakh that does the work:**

| Component of the working-capital inflow | ₹ lakh | share | per ₹100 | Whose money |
|---|---:|---:|---:|---|
| Δ Note 16 bucket (C), clearing and settlement | 24,251 | 33.3% | 5.02 | **members'** |
| Δ statutory remittances, Note 19 | 44,937 | 61.8% | 9.30 | **government's** |
| Everything else (Δ bucket A, income in advance, customer advances, other) | 3,579 | 4.9% | 0.74 | the company's |
| **Total** | **72,767** | **100.0%** | **15.05** | |

`DERIVED: 24,251 + 44,937 = 69,188; 69,188 / 72,767 = 95.08%; 69,188 / 3,10,368 = 22.29% of reported CFO.`

### 2.5 Steps losing more than ₹5 of the ₹100 — and the chain behind each (doctrine §6)

A ₹100 map whose steps have no chains behind them does not ship. Every step below ₹5 is listed with
the reason it is not traced here (doctrine §3's brake).

| Step | per ₹100 | Chain record | Owner |
|---|---:|---|---|
| Levy — regulatory contribution | 13.44 | `CHAIN: Regulatory contribution \| FY26` | W3_cost §; W1_ledger §4 |
| Tax | 17.04 | `CHAIN: Income tax — expense and cash \| FY26` | **§4 below (new — no chain existed)** |
| Employee benefits | 6.16 | `CHAIN: Employee benefits expense \| FY26` | W3_cost |
| Clearing and settlement | 5.80 | `CHAIN: Clearing and settlement expense \| FY26` | W3_cost; W1_ledger; W3_group_rpt |
| Other expenses | 5.12 | `CHAIN: Other expenses \| FY26` | W3_cost |
| Working-capital absorption (own-account) | 5.41 | `CHAIN: Cash flow from operations — own-account \| FY26` and `CHAIN: Statutory remittances \| FY26` | **§4 below** |
| Capex | 10.66 | `CHAIN: Capital expenditure \| FY26` | **§4 below** |
| Dividend paid | 6.53 | `CHAIN: Dividend paid \| FY26` | **§4 below** |
| Net deployment into deposits and securities | 50.95 | `CHAIN: Investments \| FY26`; `CHAIN: Cash and bank balances \| FY26` | W3_balancesheet; **§4 below** |
| *Below ₹5, not traced here:* technology 4.20 (W3_cost owns it); D&A 3.29 (W3_cost); core SGF 1.59 (traced anyway — §4, it is the basis-change item); associates 1.35 (W1_ledger, W3_group_rpt); other income 0.49; finance cost 0.00 | | | |

---

## 3. THE CUMULATIVE CONVERSION TEST — W1.5_triage OVERTURNED

### 3.1 The blocker, and why it is not one

`W1.5_triage` established, and `W1_ledger` §3.5 repeated, that the ten-year own-account test **cannot
be run**: Note 16's three-way split had been read for FY2023–FY2026 only, three of ten years, below
doctrine's five-year floor, and *"until that is done, no ten-year own-account conversion ratio may be
quoted."*

**That is overturned. The split exists in all ten annual reports, and in the same form.** It was never
missing; it had not been opened. It is Note 16 in FY2018–FY2026 and **Note 18** in FY2017 — which is
why a search on "Note 16" found nine years and not ten.

| FY | Owned (A) | Earmarked (B) | **Clearing and settlement (C)** | Total (A+B+C) | Source, from that year's own AR |
|---|---:|---:|---:|---:|---|
| 2016 | 18,081 | 28,041 | **62,465** | 1,08,587 | `[AR FY2017, Note 18, PDF p170/pr168]` (comparative) |
| 2017 | 21,020 | 28,085 | **1,17,997** | 1,67,102 | `[AR FY2017, Note 18, PDF p170/pr168]` |
| 2018 | 17,337 | 25,260 | **91,529** | 1,34,126 | `[AR FY2018, Note 16, PDF p175/pr168]` |
| 2019 | 17,602 | 23,297 | **56,666** | 97,565 | `[AR FY2019, Note 16, PDF p193/pr184]` |
| 2020 | 21,741 | 19,822 | **89,240** | 1,30,803 | `[AR FY2020, Note 16, PDF p205/pr198]` |
| 2021 | 20,302 | 25,569 | **69,918** | 1,15,789 | `[AR FY2021, Note 16, PDF p189/pr184]` |
| 2022 | 21,048 | 32,260 | **1,81,730** | 2,35,038 | `[AR FY2022, Note 16, PDF p194/pr185]` |
| 2023 | 20,539 | 32,461 | **1,49,802** | 2,02,802 | `[AR FY2023, Note 16, PDF p209/pr202]` |
| 2024 | 21,060 | 41,386 | **3,58,165** | 4,20,611 | `[AR FY24, Note 16, PDF p202/pr196]` |
| 2025 | 23,291 | 35,024 | **3,31,172** | 3,89,487 | `[AR FY25, Note 16, PDF p192/pr181]` |
| 2026 | 24,992 | 26,004 | **3,55,423** | 4,06,419 | `[AR FY26, Note 16, PDF p206/pr195]` |

Every year's (A)+(B)+(C) ties to that year's balance-sheet caption exactly, and every year's total ties
to `records/balance_cash_10y.csv` row `other_fin_liab_current`.

### 3.2 The second blocker, which is real, and how it is handled

`RF-027`, resolved by `W3_notes` §2.2: the FY2025 annual report changed the **basis of preparation** of
the cash-flow statement, by an eleven-word unquantified footnote — *"Movement in Core Settlement
Guarantee Fund liabilities and related assets of subsidiary companies are not considered"*
`[AR FY25, PDF p159/pr148]`. Four adjustment lines vanished from the FY2024 comparative:
`9,170 + 3,427 + 5,351 + 1,769 = 19,717`, 99.3% of a `2,84,203 − 2,64,346 = 19,857` restatement.

**A ten-year series that ignores this compares gross years with net years.** So all ten years are put
on the **FY2026 basis** — Core SGF flows excluded throughout — by removing the same four add-back
lines from every year that carried them. That is the more economically honest basis in any case: the
Core SGF is restricted regulatory capital and is not the shareholders'.

| FY | Contribution to core SGF | Contribution from other CCs | Investment income on SGF | Penalties to SGF | **Total removed** | Cash-flow tag |
|---|---:|---:|---:|---:|---:|---|
| 2017 | 952 | – | 1,842 | 53 | **2,847** | `[AR FY2017, PDF p118/pr116]` |
| 2018 | 6,291 | – | 2,305 | 48 | **8,644** | `[AR FY2018, PDF p135/pr128]` |
| 2019 | 684 | – | 2,736 | 182 | **3,602** | `[AR FY2019, PDF p149/pr140]` |
| 2020 | 74 | – | 3,042 | 146 | **3,262** | `[AR FY2020, PDF p161/pr154]` |
| 2021 | 619 | 5,630 | 2,789 | 1,360 | **10,398** | `[AR FY2021, PDF p147/pr142]` |
| 2022 | 2,905 | 1,066 | 3,015 | 3,124 | **10,110** | `[AR FY2022, PDF p151/pr142]` |
| 2023 | 5,496 | 668 | 3,483 | 1,948 | **11,595** | `[AR FY2023, PDF p163/pr156]` |
| 2024 | 9,170 | 3,427 | 5,351 | 1,769 | **19,717** | `[AR FY24, PDF p158/pr152]` |
| 2025 | – | – | – | – | **0** (footnote 3 already applies) | `[AR FY25, PDF p158/pr147]` |
| 2026 | – | – | – | – | **0** | `[AR FY26, PDF p165/pr154]` |
| | | | | | **70,175** | |

### 3.3 The ten-year test (§4a trigger 2 — computed in code, not by hand)

| FY | Reported CFO, total ops | less SGF add-backs | = comparable-basis CFO | less Δ bucket (C) | RF-046 capital advance | **= own-account CFO** | PAT, total ops | ratio |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 2017 | 81,711 | (2,847) | 78,864 | 55,532 | – | **23,332** | 26,509 | 0.88 |
| 2018 | (24,600) | (8,644) | (33,244) | (26,468) | – | **(6,776)** | 72,453 | (0.09) |
| 2019 | (31,805) | (3,602) | (35,407) | (34,863) | – | **(544)** | 19,928 | (0.03) |
| 2020 | 39,671 | (3,262) | 36,409 | 32,574 | – | **3,835** | 12,061 | 0.32 |
| 2021 | (6,787) | (10,398) | (17,185) | (19,322) | – | **2,137** | 14,170 | 0.15 |
| 2022 | 1,44,175 | (10,110) | 1,34,065 | 1,11,812 | – | **22,253** | 24,493 | 0.91 |
| 2023 | (13,711) | (11,595) | (25,306) | (31,928) | – | **6,622** | 20,565 | 0.32 |
| 2024 | 2,84,203 | (19,717) | 2,64,486 | 2,08,363 | – | **56,123** | 77,166 | 0.73 |
| 2025 | 41,417 | – | 41,417 | (26,993) | +15,584 | **83,994** | 1,32,232 | 0.64 |
| 2026 | 3,10,372 | – | 3,10,372 | 24,251 | (15,584) | **2,70,537** | 2,48,725 | 1.09 |
| **Cumulative** | **8,24,646** | **(70,175)** | **7,54,471** | **2,92,958** | **0** | **4,61,513** | **6,48,302** | **0.712** |

CFO figures are each year's own AR, total operations (continuing + discontinued where split):
`DERIVED` FY2018 `−27,147 + 2,547 = −24,600`; FY2025 `41,015 + 402 = 41,417`; FY2026
`3,10,368 + 4 = 3,10,372`. PAT from `records/trend_10y.csv` as corrected by W1_ledger.
Cumulative float telescopes and is checkable in one line: `DERIVED: 3,55,423 − 62,465 = 2,92,958`.

**The result, six ways:**

| Basis | Cumulative CFO | Cumulative PAT | Ratio |
|---|---:|---:|---:|
| **Headline, as reported** | 8,24,646 | 6,48,302 | **1.272** |
| Headline / PAT attributable | 8,24,646 | 6,47,456 | 1.274 |
| Comparable basis (SGF excluded throughout), before the float | 7,54,471 | 6,48,302 | 1.164 |
| **Own-account (float removed)** | **4,61,513** | **6,48,302** | **0.712** |
| Own-account / PAT attributable | 4,61,513 | 6,47,456 | 0.713 |
| Own-account, PAT ex the three one-off disposal gains `DERIVED: 6,48,302 − 48,722 − (40,662 − 3,910) − 3,204 = 5,59,624` | 4,61,513 | 5,59,624 | **0.825** |

**Sensitivities, all stated rather than buried:**

- **Also stripping the member deposits inside bucket (A)** (W3_balancesheet F6): own-account CFO
  `4,59,532`, ratio **0.709** — a 0.4% move. Immaterial, because the balance has been flat for eleven
  years (`15,012` at FY2016 against `16,993` at FY2026).
- **Also stripping the government float** (Δ statutory remittances, §2.4): cumulative
  `DERIVED: 74,780 − 2,343 − 5,444 reclassification = 66,993`; own-account CFO `3,94,520`, ratio
  **0.609**. Statutory remittances by year, each from its own AR:
  `2,343 · 13,115 · 5,457 · 3,952 · 7,349 · 12,598 · 16,912 · 11,829 · 27,935 · 24,399 · 74,780`
  `[AR FY2017 PDF p173/pr171 · FY2018 p178/pr171 · FY2019 p196/pr187 · FY2020 p208/pr201 · FY2021
  p191/pr186 · FY2022 p196/pr187 · FY2023 p211/pr204 · FY24 p204/pr198 · FY25 p193/pr182 · FY26
  p208/pr197]`. **New restatement found, not in `records/restatements.md`:** FY2025 statutory
  remittances were reported at **24,399** in the FY2025 AR and appear as **29,843** in the FY2026
  comparative — `DERIVED: 29,843 − 24,399 = 5,444`, exactly the FY2025 *Provision for SEBI regulatory
  fee* reclassified out of provisions (W1_ledger §1.7 #5 found the aggregate; this locates it).
- **If only 90% of the bucket-(C) movement passed through the operating section**, own-account CFO is
  `4,61,513 + 0.10 × 2,92,958 = 4,90,809`, ratio **0.757**; at 110%, `4,32,217`, ratio **0.667**. The
  band is **0.67 to 0.76**, and it does not reach 1 anywhere inside it.
- **Reverse basis** — putting FY2025 and FY2026 back on the *old* (SGF-inclusive) basis instead:
  `DERIVED: 4,61,513 + 7,696 + 3,598 + 9,000 + 8,764 = 4,90,571`, ratio **0.757**.

### 3.4 The evidence that the assumption holds, year by year

The one assumption in the whole test is that the bucket-(C) movement passes through the operating
section's aggregated *"Increase / (decrease) in other liabilities and other financial liabilities"*
line. W1_ledger verified it for FY2026 (residual 29 on 72,767, 0.04%) and FY2025 (822 on 25,155,
3.3%). Extended to all ten years, the line has the **same sign as Δ(C) in ten years out of ten** and
is of the same order:

| FY | Reported working-capital line | Δ(C) | Δ(A) | Δ(B) | Δ total Note 16 current |
|---|---:|---:|---:|---:|---:|
| 2017 | 71,130 | 55,532 | 2,939 | 44 | 58,515 |
| 2018 | (40,959) | (26,468) | (3,683) | (2,825) | (32,976) |
| 2019 | (35,364) | (34,863) | 265 | (1,963) | (36,561) |
| 2020 | 40,685 | 32,574 | 4,111 | (3,475) | 33,210 |
| 2021 | (12,262) | (19,322) | (1,439) | 5,747 | (15,014) |
| 2022 | 1,14,383 | 1,11,812 | 746 | 6,691 | 1,19,249 |
| 2023 | (37,550) | (31,928) | (290) | 201 | (32,017) |
| 2024 | 2,25,713 | 2,08,363 | 521 | 8,925 | 2,17,809 |
| 2025 | (25,155) | (26,993) | 2,231 | (6,362) | (31,124) |
| 2026 | 72,767 | 24,251 | 1,701 | (9,020) | 16,932 |

Cash-flow tags as §3.2; Note 16 tags as §3.1. One presentation change is visible and is quantified:
in **FY2017–FY2019 the movement in trading-member deposits ran through FINANCING**, not operating —
*"(Decrease) / increase in trading members and other deposits (1,776) / 724"*
`[AR FY2017, PDF p119/pr117]` and `[AR FY2018, PDF p136/pr129]` — and that line disappears from
FY2020 onwards. It affects bucket (A) only, worth `DERIVED: 4,61,513 − 4,59,532 = 1,981` lakh across
the decade, **0.4%** of the numerator.

### 3.5 The answer to the question asked

> **The longest defensible window is the full ten years, FY2017–FY2026, and the value is 0.712.**

It is defensible because (i) the bucket split is a `TRACED` disclosure in every one of the ten annual
reports, read from each year's own report rather than from a later comparative; (ii) the FY2025
basis change is neutralised by restating all ten years to one basis, and the restatement is sized
(₹70,175 lakh) rather than assumed; (iii) the only estimate in the chain — that the float travels in
the aggregated working-capital line — is tested in all ten years and its sensitivity band (0.67–0.76)
does not cross 1.

**What this replaces.** W1_ledger's three-year cumulative of **0.942** and its headline of **1.393**
are both superseded as the number to quote, and both were computed on the reported basis without the
FY2024 SGF add-back removal. Recomputed on this file's basis, the same three years give
`DERIVED: (56,123 + 83,994 + 2,70,537) / (77,166 + 1,32,232 + 2,48,725) = 4,10,654 / 4,58,123 = 0.896`.
**Both W1_ledger's 0.942 and this file's 0.896 stand on the record; the difference is basis, not
arithmetic, and it is 19,717 of FY2024 Core SGF add-backs plus the total-operations alignment.**

**Shorter windows, for anyone who needs one:** FY2022–FY2026 (five years) **0.874**;
FY2021–FY2026 (six years) **0.854**; FY2020–FY2026 (seven years) **0.842**. Every window says the same
thing, and the ten-year window says it hardest because it contains the two years — FY2018 and
FY2019 — in which the float ran out.

---

## 4. CHAIN RECORDS

Format per `state/TEMPLATES.md`. Eight links, each in a declared state. `DERIVED` shows its arithmetic
inline; `NOT-DISCLOSED` names the settling document after `->`.

### CHAIN: Cash flow from operations — own-account | FY26
L1 REPORTED   TRACED | 3,10,368 continuing and 4 discontinued against 41,015 and 402; prepared under the indirect method as set out in Ind AS 7; four footnotes, of which 2 and 3 are exclusions of whole classes of movement | [AR FY26, Consolidated Cash Flow, PDF p165-166/pr154-155]
L2 COMPONENTS DERIVED | 2,47,530 PAT + 69,763 non-cash adjustments = 3,17,293; + 58,616 working capital = 3,75,909; − 65,541 taxes paid = 3,10,368. Adjustments: 82,384 tax + 15,896 D&A + 4,057 impairment + 2,994 FCTR + 4 PPE loss − 6,542 associates − 8,875 FVTPL − 20,154 interest − 1 dividend = 69,763. Working capital: (30,595) + 1,691 + 1,115 + 13,638 + 72,767 = 58,616 | [AR FY26, Consolidated Cash Flow, PDF p165/pr154]
L3 DRIVER     DERIVED | the year's operating cash is carried by one working-capital line and that line is carried by two third-party pools: Δ bucket (C) 24,251 + Δ statutory remittances 44,937 = 69,188 of the 72,767 line = 95.08%, and 69,188 / 3,10,368 = 22.29% of reported CFO. The genuinely corporate remainder of the line is 72,767 − 69,188 = 3,579 | [AR FY26, Note 16, PDF p206/pr195] and [AR FY26, Note 19, PDF p208/pr197]
L4 COUNTERPARTY TRACED | clearing members and clearing banks of Indian Clearing Corporation Limited hold the (C) money; the tax authorities hold the statutory remittances, of which 51,478 is Securities Transaction Tax collected on the standalone. Note 12.1 states the matching earmarked balances are restricted and that all other balances are available for the Group's operating activities | [AR FY26, Note 16, PDF p206/pr195] and [AR FY26, MD&A, PDF p77/pr66] and [AR FY26, Note 12.1, PDF p202/pr191]
L5 RECOGNITION TRACED | footnote 2 excludes movement in earmarked liabilities and corresponding assets of the parent; footnote 3, inserted in FY2025, excludes Core SGF liabilities and related assets of subsidiaries; footnote 4 regroups previous-year figures. Neither exclusion names bucket (C) or statutory remittances, so both run through the operating section. The FY2025 insertion is a basis change carried by eleven words with no Ind AS 1.41 note and no amount | [AR FY26, Consolidated Cash Flow footnotes 2-4, PDF p166/pr155] and [AR FY25, PDF p159/pr148]
L6 BALANCE-SHEET DERIVED | the own-account construction closes on the balance sheet: 2,12,735 + 23,798 + 1 + 59 + 1,215 + 6,195 − 35,932 − 31,585 + 8,875 + 12,861 + 44,937 = 2,43,159 against an actual own-account financial-asset build of 6,14,282 − 3,71,074 = 2,43,208, residual 49 = 0.02% | [AR FY26, Notes 9, 11 & 12, PDF p190-202/pr179-191] and [AR FY26, Consolidated Cash Flow, PDF p165/pr154]
L7 CASH       ESTIMATE | own-account CFO = 3,10,368 − 12,861 after-tax float income − 24,251 members' float − 44,937 government float − 15,584 released capital advance = 2,12,735, a conversion of 2,12,735 / 2,34,669 = 0.907 against a headline 3,10,368 / 2,47,530 = 1.254. Assumption: the whole of each third-party movement passed through the operating working-capital line, evidenced by the reconciliation residual of 29 on 72,767 (0.04%). Range: stripping the bucket-(A) member movement of 1,701 as well gives 2,11,034, a 0.8% band | [AR FY26, Note 16, PDF p206/pr195] and [AR FY26, Note 19, PDF p208/pr197]
L8 SUSTAIN    DERIVED | ten-year cumulative own-account CFO 4,61,513 against PAT 6,48,302 = 0.712, against a headline 8,24,646 / 6,48,302 = 1.272. The condition for the headline to keep exceeding one is that member margin and collected tax keep growing — balance-sheet inflows, not earnings — and both reverse when turnover falls, as bucket (C) did in FY2018, FY2019, FY2021, FY2023 and FY2025 | [AR FY26, Note 16, PDF p206/pr195] and [AR FY2017, Note 18, PDF p170/pr168]
CHAIN-STATE: BROKEN at L1/L7

### CHAIN: Statutory remittances | FY26
L1 REPORTED   TRACED | 74,780 against 29,843 restated, +150.6% (74,780 − 29,843 = 44,937), inside Note 19 Other liabilities (current) under the heading "Owned:", which totals 93,692 against 47,947 | [AR FY26, Note 19, PDF p208/pr197]
L2 COMPONENTS NOT-DISCLOSED | the 74,780 is a single figure with no sub-schedule. Only one component is identified anywhere in the report, and not in the note: the MD&A states 51,478 is Securities Transaction Tax collected, leaving 74,780 − 51,478 = 23,302 unattributed -> AR FY26 Note 19 gives no break-up of statutory remittances; a schedule of amounts collected and payable by statute (STT, GST, TDS, stamp duty) would answer it, as would the standalone GST and TDS returns
L3 DRIVER     DERIVED | collection volume, not company activity: STT is levied on turnover and collected by the exchange for the tax authorities. The balance rose 150.6% against consolidated revenue +63.5% and options premium ADT +117.4%; over ten years it tracks turnover, 2,343 at FY2016 to 74,780 at FY2026 = 31.9x while revenue rose 4,83,395 / 42,479 = 11.4x | [AR FY26, MD&A, PDF p58/pr47] and [AR FY2017, Note 19, PDF p173/pr171]
L4 COUNTERPARTY TRACED | the Government of India and state authorities. Not a related party; not a customer; the group is a collecting agent. The corresponding cash sits in the "Owned" pool of Notes 11 and 12 and is NOT earmarked — Notes 16.2, 16.3 and 12.1 earmark assets against bucket (B) and unpaid dividends only | [AR FY26, Note 19, PDF p208/pr197] and [AR FY26, Notes 12.1 and 16.2-16.3, PDF p202, p206/pr191, pr195]
L5 RECOGNITION TRACED | presented as an "Owned" current other liability under Schedule III, with no accounting policy addressing it anywhere in Note 2.3.1 to 2.3.17. Its movement is a working-capital item under Ind AS 7 and therefore lands in operating cash flow by default | [AR FY26, Note 2, PDF p169-180/pr158-169] and [AR FY26, Consolidated Cash Flow, PDF p165/pr154]
L6 BALANCE-SHEET DERIVED | it is now the third-largest liability in the group and the fastest-growing: 74,780 is 74,780 / 5,37,049 = 13.9% of total current liabilities against 29,843 / 4,61,463 = 6.5% a year earlier, and 74,780 / 6,79,550 = 11.0% of total equity. It also carries an unexplained comparative restatement: the FY2025 AR reported 24,399, the FY2026 AR shows 29,843, a difference of 29,843 − 24,399 = 5,444 equal to the FY2025 SEBI regulatory-fee provision | [AR FY25, Note 19, PDF p193/pr182] and [AR FY26, Note 19, PDF p208/pr197]
L7 CASH       BROKEN | the movement is presented as operating cash generated by the business. It is not: it is tax collected from members and owed to the government, and it is 44,937 of a reported CFO of 3,10,368 = 14.5%. The company holds it in unrestricted "Owned" bank balances until remittance, so it also finances the own-account asset build — 44,937 of the 2,43,208 own financial-asset increase = 18.5% | [AR FY26, Consolidated Cash Flow, PDF p165/pr154] and [AR FY26, Notes 11 & 12, PDF p200-202/pr189-191]
L8 SUSTAIN    DERIVED | a growth-dependent float, not a permanent one. The ten-year series falls in four of ten years (FY2018 −7,658, FY2019 −1,505, FY2023 −5,083, FY2025 −3,536), so it reverses whenever turnover does. Cumulative ten-year contribution to CFO is 74,780 − 2,343 − 5,444 reclassification = 66,993, i.e. 10.3% of cumulative PAT of 6,48,302 | [AR FY2017, Note 19, PDF p173/pr171] and [AR FY26, Note 19, PDF p208/pr197]
CHAIN-STATE: BROKEN at L2/L7

### CHAIN: Capital expenditure | FY26
L1 REPORTED   TRACED | 51,516 against 15,323, 3.36x (51,516 / 15,323 = 3.36), as ONE combined cash-flow line titled "Purchase of property, plant and equipment, intangible assets, capital work-in-progress, intangible assets under development and capital advances". No note reference; no capex disclosure in either 2026 investor deck | [AR FY26, Consolidated Cash Flow, PDF p165/pr154]
L2 COMPONENTS DERIVED | the cash line is not disaggregated, but the accrual additions are, and they reconcile. PPE additions 47,578 = buildings 18,022 + computers, hardware and networking 18,530 + plant and equipment 7,503 + electrical installations 2,117 + office equipment 709 + furniture 553 + motor vehicles 143 + leasehold buildings 1; plus intangible additions 2,470, plus CWIP movement 3,255 − 4,073 = (818), plus IAUD movement 4,420 − 1,339 = 3,081, giving 47,578 + 2,470 − 818 + 3,081 = 52,311 | [AR FY26, Notes 3, 4 & 6, PDF p181-184/pr170-173]
L3 DRIVER     TRACED | two assets are 76.8% of the year's PPE additions: buildings 18,022 and computers, hardware and networking 18,530, together 36,552 / 47,578 = 76.8%. Buildings additions were 15 in FY2025, so the item is a step change, not a run-rate. Management states the purpose and the amount: "In the last two years, we have built around Rs. 500 crores as gross block, which has gone for capacity increase", against an actual two-year gross-block build of 1,05,539 − 50,796 = 54,743 | [AR FY26, Note 3, PDF p181/pr170] and [Q4FY26 Concall 13May2026, MD & CEO]
L4 COUNTERPARTY NOT-DISCLOSED | no vendor, contractor or seller is named for the 18,022 building or the 18,530 of hardware; capital commitments are a single figure of 10,029 (17,006 at FY2025) and Note 36 shows no related-party capital transaction. The question was asked directly and refused: "Rs. 313 crores is not a small number... It is a mix of multiple things, including the physical and technology infrastructure. What we can do is right now in front of me, I don't have the breakup" -> AR FY26 Note 38 (PDF p227/pr216) gives capital commitments as one number with no counterparty; a fixed-asset addition schedule by counterparty, or the offline break-up management promised on 17-Nov-2025 and has not published, would answer it
L5 RECOGNITION TRACED | Ind AS 16 at cost less accumulated depreciation. One estimate change disclosed and quantified: building useful life revised to 25 years effective 1 April 2024 on external valuation advice, "impact of same was Rs. 13", applied prospectively under Ind AS 8. Capital advances are classified as an "other current asset" in Note 13, not as a capital work in progress, which is what creates the L7 break | [AR FY26, Note 3 notes 2-3, PDF p181/pr170] and [AR FY26, Note 13, PDF p202/pr191]
L6 BALANCE-SHEET DERIVED | the roll-forward closes exactly: gross 63,738 + 47,578 − 6,405 + 101 investment-property transfer + 527 FX = 1,05,539; accumulated depreciation 41,521 + 13,720 − 6,373 + 47 + 365 = 49,280; net 1,05,539 − 49,280 = 56,259, tying to the face. Depreciation ties to the P&L: 13,720 + 5 + 2,171 = 15,896 | [AR FY26, Notes 3, 4 & 6, PDF p181-184/pr170-173]
L7 CASH       BROKEN | 15,584 of the 51,516 reported as FY2026 investing capex left the company in FY2025 through the OPERATING section, as a capital advance in Note 13 that was nil at FY2024, 15,584 at FY2025 and nil at FY2026 — larger than FY2025's entire reported capex line of 15,323. True FY2026 cash capex is 51,516 − 15,584 = 35,932; true FY2025 cash capex is 15,323 + 15,584 = 30,907. On those figures the step-up is 35,932 / 30,907 = 1.16x, not the 3.36x the reported lines show | [AR FY26, Note 13, PDF p202/pr191] and [AR FY25, Note 13, PDF p188/pr177]
L8 SUSTAIN    ESTIMATE | maintenance and growth are not disclosed and cannot be separated from the filing, but two independent proxies converge. On the depreciation proxy, maintenance = D&A 15,896, so growth = 51,516 − 15,896 = 35,620, i.e. 69.1%. On the prior-run-rate proxy, maintenance = FY2025 reported capex 15,323, so growth = 51,516 − 15,323 = 36,193, i.e. 70.3%. Assumption: the pre-cycle spend level approximates replacement need; range 35,620 to 36,193, a 1.6% band. The cycle is not finished — management flags technology spend of "around Rs. 300 crores" that is "almost going to be doubling", plus colocation capacity and a possible Mumbai land purchase, against contracted commitments of only 10,029 | [Q4FY26 Concall 13May2026, MD & CEO] and [AR FY26, Note 38, PDF p227/pr216]
CHAIN-STATE: BROKEN at L4/L7

### CHAIN: Core settlement guarantee fund — movement and cash treatment | FY17-FY26
L1 REPORTED   TRACED | fund balance 1,24,683 against 1,13,260, +10.1% (1,24,683 − 1,13,260 = 11,423), presented as its own caption between total equity and liabilities; P&L charge 7,696 against 9,000, −14.5%, presented below the subtotal "Profit before contribution to core settlement guarantee fund" and outside total expenses | [AR FY26, Consolidated Balance Sheet, PDF p163/pr152] and [AR FY26, Consolidated P&L, PDF p164/pr153]
L2 COMPONENTS DERIVED | the balance splits and both splits tie: ICCL 1,23,264 + India International Clearing Corporation 1,419 = 1,24,683; within ICCL by contributor, ICCL 60,896 + BSE 17,952 + NSE 26,529 + MSE 934 + other 16,953 = 1,23,264. The YEAR'S MOVEMENT splits differently and only by residual: 11,423 − 7,696 P&L charge − 129 equity transfer = 3,598 of fund investment income and member penalties credited straight to the fund | [AR FY26, Notes 41 & 42, PDF p231-232/pr220-221] and [AR FY26, Statement of Changes in Equity, PDF p168/pr157]
L3 DRIVER     BROKEN | the annual report gives one driver and management gives a different one. Policy 2.3.12 and Note 42 say the charge is SEBI's Minimum Required Contribution computed from monthly stress-test values, "not a simple direct relationship with any single factor". Management announced on 17-Nov-2025 that BSE "introduced policy to contribute 5% of transaction-related revenue to the core SGF on a monthly basis", voluntarily, "as long as overall SGF is not exceeding 150% of the minimum requirement", started September 2025, with 1,060 contributed in that quarter under the new policy. The policy does not appear anywhere in the FY2026 annual report | [AR FY26, Note 2.3.12, PDF p178/pr167] and [Q2FY26 Concall 17Nov2025, MD & CEO]
L4 COUNTERPARTY TRACED | the group's own clearing corporations hold the fund, but 22.3% of ICCL's corpus was contributed by competitors clearing through it — NSE 26,529 and MSE 934, together 27,463 of 1,23,264. Contribution once made is non-refundable even if the corpus later exceeds the MRC | [AR FY26, Notes 41 & 42, PDF p231-232/pr220-221]
L5 RECOGNITION TRACED | policy 2.3.12: expensed in the period contributed, never reversed; fund investment income and member fines credited directly to the fund and never through profit or loss; presented as a caption that is neither equity nor a liability. The policy says the Group "at least contributes amounts pertaining to Minimum Required Contribution" — the words that permit the voluntary 5% policy — but neither the percentage, the 150% cap nor the September 2025 start date is disclosed | [AR FY26, Note 2.3.12, PDF p178/pr167]
L6 BALANCE-SHEET DERIVED | matching earmarked assets tie to the caption: earmarked-SGF bank balances 27,078 + 85,037 + 544 + 5,454 + 143 = 1,18,256, plus Note 13 "Others - SGF" 296, leaves 1,24,683 − 1,18,256 − 296 = 6,131 held in prescribed securities inside Note 9 and not separately labelled. Ten-year growth: 17,605 at FY2016 to 1,24,683 at FY2026 = 7.08x, against cumulative P&L charges of 1,741 + 952 + 6,291 + 684 + 74 + 619 + 2,905 + 5,496 + 9,170 + 9,000 + 7,696 = 44,628 — so 1,24,683 − 17,605 − 44,628 = 62,450 of the fund was built from income, penalties and other exchanges' contributions rather than from BSE's P&L | [AR FY26, Notes 11, 12, 13 & 41, PDF p200-202, p231/pr189-191, pr220] and [records/trend_10y.csv, row core_sgf_contribution]
L7 CASH       BROKEN | the item was added back to CFO as a non-cash adjustment in every year FY2017 to FY2024, together with SGF investment income and member penalties, and is added back in NEITHER FY2025 nor FY2026 because footnote 3 excludes the whole class. The four deleted FY2024 lines total 9,170 + 3,427 + 5,351 + 1,769 = 19,717, i.e. 99.3% of the 2,84,203 − 2,64,346 = 19,857 restatement of FY2024 CFO. Across ten years the same four lines total 70,175, so any uncorrected ten-year CFO series overstates the comparable-basis figure by that amount | [AR FY24, Consolidated Cash Flow, PDF p158/pr152] and [AR FY26, Consolidated Cash Flow footnote 3, PDF p166/pr155]
L8 SUSTAIN    ESTIMATE | the charge is about to stop being small and stop being volatile at the same time. On the announced policy, 5% of FY2026 transaction charges of 3,79,499 = 18,975 a year, against an actual FY2026 charge of 7,696 — 2.47x, and 18,975 / 4,83,395 = 3.93% of revenue against 1.59%. Assumption: "transaction-related revenue" means the Note 22 transaction-charges line and the 150% cap is not reached; range, on standalone transaction charges of 3,66,948 the figure is 18,347. The FY2026 charge does not reconcile to the policy on any base — seven months at 5% would be 11,069 — and no note explains the difference | [AR FY26, Note 22, PDF p211/pr200] and [Q2FY26 Concall 17Nov2025, MD & CEO]
CHAIN-STATE: BROKEN at L3/L7

### CHAIN: Dividend paid | FY26
L1 REPORTED   TRACED | 31,585 against 20,599, +53.3% (31,585 − 20,599 = 10,986), the only material financing outflow; financing activities in total were (30,370) against (20,599) | [AR FY26, Consolidated Cash Flow, PDF p165/pr154]
L2 COMPONENTS TRACED | one item: the final dividend for FY2025 of ₹23 per share, paid in FY2026. Note 15 gives both halves — "Dividend on equity shares declared and paid: Proposed dividend for the year ended on March 31, 2025: ₹23 per share (March 31, 2024: ₹15 per share) 31,585" and "Proposed dividends on equity shares (subject to shareholder's approval)... ₹10 per share 41,198". No NCI dividend line exists in FY2026 | [AR FY26, Note 15, PDF p205/pr194]
L3 DRIVER     DERIVED | share count times rate, and the bonus makes the rates non-comparable until adjusted. 31,585 lakh / ₹23 = 13,73,26,087 shares; x 3 for the 2:1 bonus = 41,19,78,261, against the 41,19,79,077 weighted-average shares on which the FY2026 ₹10 proposed dividend of 41,198 is computed. Bonus-adjusted DPS therefore went ₹23 / 3 = ₹7.67 to ₹10.00, i.e. 10.00 / 7.67 = +30.4%; excluding the ₹5 special dividend for the 150th year, ₹18 / 3 = ₹6.00 to ₹10.00 = +66.7% | [AR FY26, Consolidated P&L, PDF p164/pr153] and [Q4FY26 Concall 13May2026, MD & CEO]
L4 COUNTERPARTY TRACED | no promoter exists — a demutualised exchange. Only one shareholder above 5%, LIC at 2,27,29,500 shares, 5.57%. Non-controlling interests in India International Exchange and India International Clearing Corporation received nothing; the last NCI dividend line in the consolidated cash flow was FY2017 (1,441) | [AR FY26, Note 14(e), PDF p204/pr193] and [AR FY2017, Consolidated Cash Flow, PDF p119/pr117]
L5 RECOGNITION TRACED | Note 15.4 makes distributable dividends a function of the PARENT's retained earnings, not the group's: standalone retained earnings are 4,55,828, 67.1% of consolidated total equity of 6,79,550. Dividends are recognised when declared and approved, so the FY2026 proposed 41,198 is not a liability at 31 March 2026 and is not in this year's cash flow | [AR FY26, Note 15.4, PDF p204/pr193] and [AR FY26, Standalone Note 15, PDF p280/pr269]
L6 BALANCE-SHEET DERIVED | equity absorbed the retention: total equity rose 4,57,570 to 6,79,550 = +2,21,980 on profit attributable of 2,49,698 less dividends of 31,585, a payout of 31,585 / 2,49,698 = 12.6% on the year's own profit and 41,198 / 2,49,698 = 16.5% on the proposed. Cumulative ten-year dividends paid 1,71,662 against cumulative PAT 6,48,302 = 26.5%, and against ten-year own-account CFO of 4,61,513 = 37.2% | [AR FY26, Statement of Changes in Equity, PDF p167-168/pr156-157] and [records/balance_cash_10y.csv, row dividend_paid]
L7 CASH       TRACED | fully cash, in financing, with no scrip alternative; the 2:1 bonus of 27,07,52,718 shares moved 5,414 from general reserve to share capital and appears nowhere in the cash flow. Against own-account free cash flow of 2,12,735 − 35,932 = 1,76,803, the dividend paid is 31,585 / 1,76,803 = 17.9% and the FY2026 proposed dividend is 41,198 / 1,76,803 = 23.3% | [AR FY26, Consolidated Cash Flow, PDF p165/pr154] and [AR FY26, Note 15, PDF p205/pr194]
L8 SUSTAIN    DERIVED | the constraint is not cash and management does not claim it is. Own-account FCF of 1,76,803 covers the proposed dividend 1,76,803 / 41,198 = 4.29x and covers a full 100% payout of PAT attributable 1,76,803 / 2,49,698 = 0.71x. Payout fell 99% to 17.8% over three years while absolute rupees rose 412 / 154 = 2.67x. The condition for the current level to persist is that the capex cycle management describes — technology spend doubling from ~300 crore, colocation capacity, a possible Mumbai land purchase — actually consumes the retention; on FY2026's evidence it did not, since cash capex was 35,932 against own-account FCF of 1,76,803 | [Q4FY26 Concall 13May2026, MD & CEO] and [AR FY26, Consolidated Cash Flow, PDF p165/pr154]
CHAIN-STATE: TRACED

### CHAIN: Cash and bank balances — the cash-flow definition | FY26
L1 REPORTED   TRACED | closing "Cash and cash equivalents at the end of the year" 1,64,642 against 1,52,416, on the face of the cash-flow statement; the balance sheet's cash and cash equivalents is 1,67,159 and total liquid funds including all deposits are 8,09,253 | [AR FY26, Consolidated Cash Flow, PDF p166/pr155] and [AR FY26, Notes 11 & 12, PDF p200-202/pr189-191]
L2 COMPONENTS TRACED | the statement publishes its own reconciliation and it ties exactly: balance-sheet cash 1,67,159 less unpaid-dividend current accounts 1,826 less other earmarked current accounts 480 less SGF current accounts 143 less earmarked deposits under three months 68 = 1,64,642. Split by use: balances with banks excluding earmarked balances, current accounts 77,375 + deposits with original maturity of three months 87,267 = 1,64,642 | [AR FY26, Consolidated Cash Flow, PDF p166/pr155]
L3 DRIVER     DERIVED | the statement's "cash" is a small and shrinking window on the group's liquidity, because tenor lengthened. Owned deposits over twelve months went 16,439 to 1,37,461, +736%, and owned deposits under twelve months 1,40,194 to 1,51,346, +8.0%, so cash equivalents grew only 1,52,416 to 1,64,642 = +8.0% while own-account liquid funds grew 1,67,486 to 3,08,596 = +84.3% | [AR FY26, Notes 11 & 12, PDF p200-202/pr189-191]
L4 COUNTERPARTY NOT-DISCLOSED | the group holds 8,09,253 in bank deposits and current accounts and names not one bank; Note 34's credit-risk paragraph gives no bank-wise or rating-wise concentration -> AR FY26 Note 34 (PDF p218-222/pr207-211) gives no deposit counterparty disclosure; a bank-wise concentration schedule, or ICCL's clearing-bank list filed with SEBI, would answer it. The only bank ever named is Punjab & Sindh Bank, as a fully provided 316 receivable in Note 11
L5 RECOGNITION TRACED | Note 12.1 is the operative sentence and it is what makes the own/earmarked separation a TRACED fact: "the above mentioned cash and bank balances are restricted cash and bank balances which are to be used for specified purposes. All other cash and bank balances are available for the operating activities of the Group." Deposits above three months are excluded from cash equivalents under Ind AS 7 and run through investing | [AR FY26, Note 12.1, PDF p202/pr191]
L6 BALANCE-SHEET DERIVED | owned 3,08,596 = current accounts 6,637 + short deposits 4,667 + deposits under twelve months 1,51,346 + accrued interest 5,661 + deposits over twelve months 1,37,461 + accrued interest 2,824; earmarked 5,00,657; total 3,08,596 + 5,00,657 = 8,09,253, zero residual. The "owned" pool is not unencumbered: it funds 74,780 of government money awaiting remittance and 16,993 of refundable member deposits that carry no earmarked asset, so own liquid funds net of both are 3,08,596 − 74,780 − 16,993 = 2,16,823, i.e. 70.3% of the pool the company calls owned | [AR FY26, Notes 11, 12, 16 & 19, PDF p200-208/pr189-197]
L7 CASH       BROKEN | the statement's definition of cash is 1,64,642 / 8,09,253 = 20.3% of the group's actual liquid funds. The remainder is 8,09,253 − 1,64,642 = 6,44,611, of which 2,91,973 + 3,50,121 = 6,42,094 is deposits moving through INVESTING as gross flows of (3,29,857) and 1,74,471 that cannot be reconciled to the balance sheet because footnotes 2 and 3 remove an undisclosed subset, and 1,826 + 480 + 143 + 68 = 2,517 is earmarked balances the statement's own reconciliation removes. That unreconcilable deposit pair is also where the missing associate dividend of 3,919 is absorbed (section 1.4) | [AR FY26, Consolidated Cash Flow, PDF p165-166/pr154-155] and [AR FY26, Notes 11 & 12, PDF p200-202/pr189-191]
L8 SUSTAIN    DERIVED | own-account liquidity is compounding faster than the business absorbs it: 3,08,596 own-account liquid funds are 3,08,596 / 6,79,550 = 45.4% of total equity and 3,08,596 / 4,83,395 = 63.8% of a year's revenue, against cash capex of 35,932 = 11.6% of that pool. The condition for it to stop compounding is a payout above roughly 70% of profit or a capex programme several times the current one; management has flagged the second and rejected the first | [AR FY26, Notes 11 & 12, PDF p200-202/pr189-191] and [Q4FY26 Concall 13May2026, MD & CEO]
CHAIN-STATE: BROKEN at L1/L7

### CHAIN: Income tax — expense and cash | FY26
L1 REPORTED   TRACED | total tax expense 82,384 against 43,121, +91.1% (82,384 − 43,121 = 39,263); direct taxes paid net of refunds 65,541 against 32,797. Tax is the single largest step in the ₹100 map at 82,384 / 4,833.95 = ₹17.04 per ₹100 of revenue | [AR FY26, Consolidated P&L, PDF p164/pr153] and [AR FY26, Consolidated Cash Flow, PDF p165/pr154]
L2 COMPONENTS TRACED | current tax 82,590 + prior period adjustments 256 + deferred tax (462) = 82,384, zero residual; prior year 42,184 − 2,987 + 3,924 = 43,121. Discontinued operations carry a further 251. Deferred tax net asset 2,371 against 1,939, reconciling 1,939 + 476 − 44 = 2,371 | [AR FY26, Notes 18 & 29, PDF p207, p213/pr196, pr202]
L3 DRIVER     DERIVED | rate times base, with the rate almost unchanged and the base nearly doubled: effective rate 82,384 / 3,29,914 = 24.97% against 43,121 / 1,74,827 = 24.66%, +0.31pp, while PBT rose 3,29,914 / 1,74,827 = 1.887x. So 39,263 of the 39,263 increase, essentially all of it, is base rather than rate — a 0.31pp rate move on the prior base is 1,74,827 x 0.0031 = 542, i.e. 1.4% of the increase | [AR FY26, Consolidated P&L, PDF p164/pr153]
L4 COUNTERPARTY TRACED | the Indian tax authorities, plus the IFSC entities. Unrecognised deferred tax assets on revenue tax losses of 21,960 (21,449 at FY2025) expire between 2027-28 and 2034-35 and sit with the loss-making IFSC subsidiaries; contingent liabilities include income-tax matters of 13,496 against 11,170, +20.8%, and indirect-tax matters 5,930 against 2,210, +168.3% | [AR FY26, Note 18 note 1, PDF p208/pr197] and [AR FY26, Note 37, PDF p227/pr216]
L5 RECOGNITION TRACED | policy 2.3.13: current tax at enacted rates; deferred tax on the balance-sheet approach; recognised in profit or loss except where the item is in equity or OCI. No policy change disclosed. The 256 of prior-period adjustments in FY2026 follows (2,987) in FY2025 — a swing of 3,243 across two years on a line that should be near zero in a stable filing history | [AR FY26, Note 2.3.13, PDF p178-179/pr167-168] and [AR FY26, Note 29, PDF p213/pr202]
L6 BALANCE-SHEET DERIVED | the accrual-to-cash gap sits in the balance sheet and is identifiable: tax expense 82,384 less taxes paid 65,541 = 16,843, against a rise in current tax liabilities of 20,109 − 8,447 = 11,662 plus the deferred-tax credit of 462 plus prior-period 256, together 12,380, leaving 16,843 − 12,380 = 4,463 in advance-tax and current-tax-asset movements not separately disclosed | [AR FY26, Consolidated Balance Sheet, PDF p163/pr152] and [AR FY26, Note 18, PDF p207/pr196]
L7 CASH       DERIVED | cash tax ran below book tax and flattered CFO: 65,541 / 82,384 = 79.6% of the charge was paid, so 16,843 of the year's tax charge is still in the balance sheet — 16,843 / 3,10,368 = 5.4% of reported CFO. The prior year ran the same way, 32,797 / 43,121 = 76.1%. Over two years the group has accrued 1,25,505 of tax and paid 98,338, a shortfall of 27,167 | [AR FY26, Consolidated Cash Flow, PDF p165/pr154]
L8 SUSTAIN    DERIVED | the rate is stable and the deferral is not permanent. At 24.97% the charge repeats with the base; the 16,843 accrual-to-cash gap unwinds as advance tax and self-assessment are paid, so the 5.4% flattering of CFO is timing, not policy. The condition to watch is the disputed tax book: income-tax and indirect-tax contingent liabilities 13,496 + 5,930 = 19,426 against 11,170 + 2,210 = 13,380 a year earlier, +45.2% — slower than the tax charge at +91.1% and slower than revenue at +63.5%, but the indirect-tax half alone grew 5,930 / 2,210 = 2.68x, and that is the half a turnover-linked levy dispute would appear in | [AR FY26, Note 37, PDF p227/pr216] and [AR FY26, Consolidated P&L, PDF p164/pr153]
CHAIN-STATE: TRACED

---

## 5. CAPEX — reconciled, and what cannot be split

### 5.1 The reconciliation

`DERIVED`, accrual to cash, FY2026:

`accrual additions 47,578 PPE + 2,470 intangibles + CWIP movement (3,255 − 4,073) = (818) + IAUD
movement (4,420 − 1,339) = 3,081` → **52,311**
`less non-cash foreign-currency translation on PPE 527 and on intangibles 39, less the
investment-property transfer of 101, less the increase in payables for fixed assets of
(3,341 − 2,423) = 918` → **50,726**
against the reported cash line of **51,516** — **residual 790, 1.5%**
`[AR FY26, Notes 3, 4 & 6, PDF p181-184/pr170-173]` and `[AR FY26, Note 16, PDF p206/pr195]`.

**The bridge closes only if the ₹15,584 lakh capital advance is treated as paid in FY2026, and it was
not.** Note 13 *Capital advances* is nil at FY2024, **15,584** at FY2025 and nil at FY2026
`[AR FY26, Note 13, PDF p202/pr191]` and `[AR FY25, Note 13, PDF p188/pr177]` — and FY2025's entire
reported capex line was 15,323, **smaller than the advance**, so it cannot have been paid through
FY2025 investing. It was paid through FY2025 operating working capital and released through FY2026
operating working capital, while FY2026 investing reported it as that year's capex. RF-046, found by
W3_balancesheet, confirmed here from the other direction.

| | Reported | Corrected | Tag |
|---|---:|---:|---|
| FY2025 cash capex | 15,323 | **30,907** | `[AR FY25, PDF p158/pr147]` + `[AR FY26, Note 13, PDF p202/pr191]` |
| FY2026 cash capex | 51,516 | **35,932** | `[AR FY26, PDF p165/pr154]` + Note 13 |
| Step-up | **3.36x** | **1.16x** | `DERIVED: 51,516 / 15,323 = 3.36; 35,932 / 30,907 = 1.16` |

**The headline "3.4x capex step-up" is a presentation artefact.** On corrected cash, FY2026 capex was
**16% above** FY2025, not 236% above it. The two-year total is right either way:
`DERIVED: 15,323 + 51,516 = 66,839 = 30,907 + 35,932`.

### 5.2 Composition — what is disclosed and what is not

| Line | ₹ lakh | share of PPE additions | FY2025 | Tag |
|---|---:|---:|---:|---|
| Computers, hardware and networking | 18,530 | 38.9% | 8,279 | `[AR FY26, Note 3, PDF p181/pr170]` |
| Buildings | 18,022 | 37.9% | **15** | same |
| Plant and equipment | 7,503 | 15.8% | 682 | same |
| Electrical installations | 2,117 | 4.4% | 1,468 | same |
| Office equipment, furniture, vehicles, leasehold | 1,406 | 3.0% | 972 | same |
| **PPE additions** | **47,578** | **100.0%** | **11,416** | same |
| Intangible additions | 2,470 | | 2,318 | `[AR FY26, Note 6, PDF p184/pr173]` |
| IAUD movement | 3,081 | | 1,001 | `[AR FY26, Consolidated Balance Sheet, PDF p163/pr152]` |

**The counter-proportion that makes the asymmetry legible:** the accrual note splits 47,578 into
**nine** asset classes; the cash-flow line splits 51,516 into **none**, and the two are not the same
number. The composition of the *cash* figure — which is the one every model uses — is
**`NOT-DISCLOSED`**, in both 2026 investor decks and in the annual report.

**Maintenance versus growth: not separable from disclosure, and the honest answer is to say so.** No
line, note or deck distinguishes replacement from expansion. Two independent proxies are offered as an
`ESTIMATE` with the assumption stated:

| Proxy | Maintenance | Growth | Growth share |
|---|---:|---:|---:|
| Depreciation and amortisation as the replacement rate | 15,896 | `51,516 − 15,896 = 35,620` | 69.1% |
| FY2025 reported capex as the pre-cycle run-rate | 15,323 | `51,516 − 15,323 = 36,193` | 70.3% |
| On corrected cash capex, depreciation proxy | 15,896 | `35,932 − 15,896 = 20,036` | 55.8% |

The first two converge to within 1.6% (`36,193 / 35,620 = 1.016`), which is the strongest support
available for a split the company does not publish. The third is the honest one, because it uses the
capex that actually left the company in the year.

**The disclosure gap is graded, per doctrine §2b.** It is not that nobody discloses this — it is that
BSE was asked and declined. On 17 November 2025 an investor asked for the break-up of a ₹313 crore
half-year investing outflow. The MD & CEO: *"Rs. 313 crores is not a small number. It is a big number.
It is a mix of multiple things, including the physical and technology infrastructure. What we can do
is right now in front of me, I don't have the breakup. Offline, certainly we can take your call…
we will be able to provide you a breakup of whatever we are doing"*
`[Q2FY26 Concall 17Nov2025, MD & CEO]`. No break-up has appeared in the FY2026 annual report, in the
Q4FY26 deck or in the Q1FY27 deck.

---

## 6. FREE CASH FLOW, AND WHAT IT ACTUALLY FUNDED

### 6.1 The two FCF numbers

| | Headline | Own-account | Tag |
|---|---:|---:|---|
| CFO | 3,10,372 | 2,12,739 | §2 |
| Capex | (51,516) | (35,932) | §5.1 |
| **FCF** | **2,58,856** | **1,76,807** | `DERIVED` |
| Dividend paid | (31,585) | (31,585) | `[AR FY26, PDF p165/pr154]` |
| **FCF after dividend** | **2,27,271** | **1,45,222** | `DERIVED` |
| Dividend cover on FY2026 FCF | 8.20x | **5.60x** | `DERIVED: 2,58,856 / 31,585; 1,76,807 / 31,585` |
| Cover of the FY2026 *proposed* dividend of 41,198 | 6.28x | **4.29x** | `DERIVED: 2,58,856 / 41,198; 1,76,807 / 41,198` |

**W2_promise's framing needs one correction.** It records *"₹515cr of capex against ₹412cr of
dividend, so investment exceeded distribution in the year the payout ratio fell to 17.8%"* as
disconfirming evidence in management's favour. On corrected cash the comparison reverses:
**cash capex was ₹359 crore (35,932 lakh) against a proposed dividend of ₹412 crore (41,198 lakh)** —
`DERIVED: 41,198 / 35,932 = 1.15x`. Distribution exceeded investment. The disconfirming evidence is
weaker than it looked, and it looked stronger because ₹156 crore of FY2025's cash was reported in
FY2026's capex line. Both positions stand on the record.

### 6.2 Where the retained cash went — the sources and uses that close to ₹49 lakh

| Own-account sources and uses, FY2026 | ₹ lakh |
|---|---:|
| Own-account CFO | 2,12,735 |
| Interest received | 23,798 |
| Dividend received (as presented) | 1 |
| Proceeds from sale of PPE | 59 |
| Issue of shares by subsidiary | 1,215 |
| Discontinued operations, net | 6,195 |
| **Total sources** | **2,44,003** |
| Cash capex | (35,932) |
| Dividend paid | (31,585) |
| **Total uses** | **(67,517)** |
| **Net** | **1,76,486** |
| add non-cash fair-value gain on FVTPL assets | 8,875 |
| add after-tax income earned on members' float, retained | 12,861 |
| add government money held pending remittance | 44,937 |
| **= modelled increase in own-account financial assets** | **2,43,159** |
| actual increase `DERIVED: 6,14,282 − 3,71,074 = 2,43,208` | 2,43,208 |
| **residual** | **49 (0.02%)** |

`[AR FY26, Consolidated Cash Flow, PDF p165-166/pr154-155]` and
`[AR FY26, Notes 9, 11 & 12, PDF p190-202/pr179-191]`.

**The answer to "where did the retained cash go" is: into the securities and deposit book.** Cash
capex consumed **14.8%** of own-account sources (`35,932 / 2,44,003`); the dividend **12.9%**
(`31,585 / 2,44,003`); the residual **72.3%** went into mutual funds, bonds, state development loans,
government securities and bank deposits. Own-account investments rose `3,05,686 − 2,03,588 = 1,02,098`
and own-account liquid funds `3,08,596 − 1,67,486 = 1,41,110` `[AR FY26, Notes 9, 11 & 12, PDF
p190-202/pr179-191]`. Mutual funds alone rose `2,21,094 / 1,18,110 = 1.87x`.

**The ICCL channel W3_group_rpt found is real and it is the smaller half.** ₹12,607 lakh of pre-tax
profit moved from BSE Limited — the only entity that can declare a dividend — into ICCL through the
intra-group clearing charge, and ICCL returned 3,540, so `DERIVED: 12,607 − 3,540 = 9,067` was
retained inside a SEBI-regulated clearing corporation with its own net-worth floor
`[AR FY26, Standalone Note 35, PDF p298/pr287]` and `[AR FY26, Standalone Note 23, PDF p286/pr275]`.
Set that against the ₹1,76,486 lakh of net own-account cash the group retained in the same year:
`DERIVED: 9,067 / 1,76,486 = 5.1%`. **The trapped-in-ICCL mechanism explains one twentieth of the
retention. Nineteen twentieths sits in the parent's own treasury book and is not trapped by anything.**

**And the parent can pay it.** Note 15.4 caps distribution at the parent's retained earnings, which
are **4,55,828** `[AR FY26, Standalone Note 15, PDF p280/pr269]` — `DERIVED: 4,55,828 / 41,198 = 11.1x`
the proposed dividend. Legal capacity is not the constraint either.

---

## 7. FINDINGS

### FINDING: The consolidated statement of cash flows has omitted the associate dividend for eight consecutive years — ₹18,100 lakh — because the "Dividend received" line is a mirror of the P&L, not a record of cash
S1 WHAT: The consolidated cash flow reports "Dividend received 1" in FY2026 while the same report's Note 8 records ₹3,919 lakh of dividend received from CDSL `[AR FY26, Note 8, PDF p189/pr178]` and `[AR FY26, Consolidated Cash Flow, PDF p165/pr154]`. In every one of the ten years read, the investing "Dividend received" line equals the operating "Dividend income" adjustment to the rupee — 1,720 / 1,633 / 1,994 / 1,302 / 31 / 11 / – / 26 / 1 / 1 — so it is a mechanical mirror of consolidated P&L dividend income. Under the equity method an associate's dividend never enters that income, so the line cannot carry it in any year, by construction.
S2 WHY: Not an elimination. Ind AS 7.37 requires an investor using the equity method to report the cash flows between itself and the investee, dividends specifically; Ind AS 7.31 requires dividends received to be disclosed separately; Ind AS 7.21 requires gross reporting of major investing receipts. Elimination applies to intra-group flows because both sides sit inside the reporting entity; CDSL is outside it. The reduction of the equity-method carrying amount is a balance-sheet mechanic with no cash-flow counterpart. What has happened is that the preparer routes the P&L dividend-income line out of operating and into investing and never asks what dividend cash actually arrived.
S3 EVIDENCE: `DERIVED: 1,058 + 1,209 + 941 + 1,881 + 3,135 + 2,508 + 3,449 + 3,919 = 18,100` lakh omitted across FY2019–FY2026, against the ₹7,368 lakh W3_group_rpt sized over two years — 2.46x larger. FY2023 is the clean case: ₹3,135 lakh received `[AR FY2023, Note 16A, PDF p191/pr184]`, a dash printed `[AR FY2023, Consolidated Cash Flow, PDF p163/pr156]`. The counter-proportion that decides whether CFO is affected: the omitted amount is 3,919, i.e. 1.26% of reported CFO, while the aggregate reconciliation residual across all five operating working-capital lines is `DERIVED: 32 + 0 + 160 + 177 + 29 = 398`, 0.13% of CFO — so the largest operating line residual is 4.1% of the missing dividend (`160 / 3,919`) and none can hold it. Against that, the investing section contains an unreconcilable pair of gross deposit lines and an interest-received line that exceeds computed cash interest by `DERIVED: 23,798 − (20,154 − 274) = 3,918`, one lakh from the dividend.
S4 CONNECTS: The standalone settles that it is cash — standalone investing shows "Dividend received from subsidiaries, associate and others 10,038" and standalone Note 23 splits it `DERIVED: 6,118 + 3,919 + 1 = 10,038` `[AR FY26, Standalone Cash Flow, PDF p251/pr240]` and `[AR FY26, Standalone Note 23, PDF p286/pr275]`. Governance: this is the same preparation process that inserted an eleven-word unquantified cash-flow basis change (RF-027), restated a ₹10,60,000 lakh guarantee comparative with no note (RF-008), and split a ₹15,584 lakh capital advance across two sections in opposite directions (RF-046) — four defects in one statement in three years, under an auditor in year nine of a ten-year rotation cliff (RF-007). Business: CDSL is the group's only materially profitable associate and supplies 104.6% of the associate line, so this is not an immaterial counterparty. The compensating control is that closing cash ties to the balance sheet through a published reconciliation; the class of error it cannot catch is exactly this one — a misallocation between two lines that both sit inside a section that foots.
DOMAINS: CashFlow, Notes, Governance, Business
DISCONFIRM: Sought, and two things cut the company's way. (i) Total cash, closing cash and CFO are all correct — this misstates the composition of investing, not the amount of anything, and the sources-and-uses reconstruction closes to ₹49 lakh either way. (ii) The amount is small: 3,919 is 1.57% of PAT attributable and 1.26% of CFO. Against the company: the pattern is eight years old, it is structural rather than an oversight, and the "consolidation mechanic" defence recorded in the red-flag register is not available under Ind AS 7. Also recorded: I cannot prove which investing line absorbed it — the interest arithmetic points at "Interest received" with a one-lakh residual, but netting inside the fixed-deposit lines cannot be excluded because footnotes 2 and 3 make those lines unreconcilable by design.
S5 MEANS: The consolidated statement of cash flows at this group is not built from cash — at least one of its lines is built from the profit and loss account and mislabelled, and the error has survived two audit partners, one auditor-rotation cycle and eight annual reports without anyone noticing that a line called "Dividend received" reports something other than dividends received.
BASE-RATE: No realised loss: the ₹18,100 lakh is in the bank, evidenced on the standalone every year, and the group's closing cash ties to its balance sheet in all ten years. The base rate that matters is preparation quality rather than economics, and on that measure the record is now four independent tie-out failures in the same statement inside three years — the capital advance, the FY2024 restatement, this, and the unreconcilable gross deposit lines. In the system, cash-flow misclassification is the second most common Ind AS enforcement finding raised by the Financial Reporting Review Board on Indian listed companies after related-party disclosure, which is where the base rate for "one misclassification predicts another" comes from.
S6 IMPLICATION: Any figure taken from this consolidated statement of cash flows below the level of "net cash from operating activities" has to be re-derived from the notes or from the standalone before it is used, because two of its ten investing lines are demonstrably not what they are named; the durability of the earnings stream is unaffected but the cost of measuring it rises. Monitorable: whether the FY2027 consolidated investing section carries a separate "dividend received from associate" line, and whether "interest received" then falls by roughly the associate dividend. Next check: FY2027 annual report, consolidated investing section and Note 8 roll-forward.
SEVERITY: Medium

### FINDING: 95.1% of the working-capital inflow that carries FY2026's cash flow is other people's money — ₹24,251 lakh of members' float and ₹44,937 lakh of tax collected for the government
S1 WHAT: Reported CFO of ₹3,10,368 lakh depends on a single working-capital line, "Increase / (decrease) in other liabilities and other financial liabilities", of ₹72,767 lakh `[AR FY26, Consolidated Cash Flow, PDF p165/pr154]`. That line reconciles to `DERIVED: Δ bucket (A) 1,701 + Δ bucket (C) 24,251 + Δ Note 19 46,865 + Δ non-current OFL (21) = 72,796`, residual 29. Two components are third-party money: the clearing-and-settlement float of ₹24,251 lakh `[AR FY26, Note 16, PDF p206/pr195]` and statutory remittances of ₹44,937 lakh, of which the MD&A identifies ₹51,478 lakh of the closing balance as Securities Transaction Tax collected `[AR FY26, Note 19, PDF p208/pr197]` and `[AR FY26, MD&A, PDF p77/pr66]`.
S2 WHY: Both pools are liabilities that arise from collecting money from members, and under Ind AS 7 the movement in a current liability lands in operating working capital by default unless the preparer excludes it. BSE excludes two classes by footnote — the parent's earmarked balances (since FY2018) and the subsidiaries' Core SGF (since FY2025) — and excludes neither of these. The clearing float is named in neither footnote despite being 87.5% of Note 16's current balance; statutory remittances sit under Note 19's heading "Owned:", which is where the classification error starts.
S3 EVIDENCE: `DERIVED: 24,251 + 44,937 = 69,188; 69,188 / 72,767 = 95.08%` of the line, and `69,188 / 3,10,368 = 22.29%` of reported CFO. The counter-proportion inside the same line is what makes it a finding rather than a share: the genuinely corporate remainder — income received in advance, customer advances, employee accruals and the rest — is `DERIVED: 72,767 − 69,188 = 3,579`, i.e. **4.9%**. So the company's own working capital contributed ₹3,579 lakh to a line the reader is invited to read as ₹72,767 lakh of operating cash generation, a ratio of 20.3 to 1. Per ₹100 of revenue: the line is worth ₹15.05, of which ₹14.31 is other people's and ₹0.74 is the company's. On the government half specifically, the balance rose 150.6% against revenue +63.5% and is now 13.9% of total current liabilities against 6.5% a year earlier.
S4 CONNECTS: Balance sheet — W3_balancesheet classifies statutory remittances as "STATUTORY (held for the government)" and shows that 45.1% of the FY2026 funding side is not the company's money; this finding shows the same is true of 95.1% of the year's operating cash inflow, so the income statement is the only statement where the float does not dominate. Industry — the collection obligation is a consequence of being a Market Infrastructure Institution: SEBI's framework makes the exchange the collecting agent for STT, so the float scales with turnover the regulator prices and the company does not control (RF-012's three-base wedge). Management commentary — the MD&A discusses the STT balance only as a balance, never as a driver of cash flow, and the concall record contains no question or answer on working capital in any of the last eight calls. Notes — Note 19 gives no sub-schedule at all, so 23,302 of the 74,780 is unattributed even after the MD&A's STT identification. The compensating control is that the earmarked asset pool is disclosed and tested two-sided; the class of error it cannot catch is exactly this one, because statutory remittances are not earmarked against anything.
DOMAINS: CashFlow, BalanceSheet, Notes, Industry, MgmtCommentary
DISCONFIRM: Sought and partly found. (i) The presentation is standard: Ind AS 7 does not require collected taxes to be excluded from operating cash flow, and most listed companies present them the same way, so this is not a departure from practice. (ii) The float is real cash the company holds and earns on, and it is not owed on demand — STT is remitted on a statutory cycle. (iii) Over ten years the statutory-remittance float has been a net source of only 66,993, i.e. 10.3% of cumulative PAT, so it is not a decade-long distortion, only an FY2026 one. Against the company: the float fell in four of the last ten years, so it is not a permanent funding source; and the FY2026 amount is large enough that a reader who assumes it is operating cash mis-sizes the business by 22.3% of a year's CFO.
S5 MEANS: FY2026's headline cash flow is not a measure of the business converting profit into cash — it is a measure of how much of other people's money happened to be sitting in the group's bank accounts on 31 March 2026, and the company's own working capital contributed one twentieth of the line that produced it.
BASE-RATE: No loss has ever arisen from either pool at this company: no clearing-member default has been charged against ICCL's Core SGF in ten years, and no statutory remittance default appears in any CARO report or contingent-liability note in the nine years read. The demonstrated cost is not credit, it is measurement — the same two pools produced the reported CFO swinging from ₹2,84,203 lakh to ₹41,015 lakh to ₹3,10,368 lakh in three consecutive years on a profit series that only rose, and every one of those swings has been read by somebody as an operating event.
S6 IMPLICATION: Reported CFO is not a usable input for this company on any single year, and the only defensible cash figure is own-account CFO, which for FY2026 is ₹2,12,735 lakh rather than ₹3,10,368 lakh — 31.5% lower; any valuation anchored on a cash-flow multiple must be told which of those two numbers it is using. Monitorable: the statutory-remittance balance at each reporting date, which will fall the moment turnover does, and the bucket-(C) balance alongside it. Next check: Q2FY27 balance sheet if published, otherwise the FY2027 annual report Notes 16 and 19.
SEVERITY: High

### FINDING: The ten-year own-account conversion test can be run, and it is 0.712 — the disclosure was there in all ten annual reports and had not been opened
S1 WHAT: W1.5_triage concluded, and W1_ledger §3.5 repeated, that the ten-year own-account cash-conversion test cannot be run because Note 16's Owned / Earmarked / Clearing-and-settlement split exists for only three of ten years, below doctrine's five-year floor. The split exists in **all ten** annual reports, in identical form, with the same bucket labels and the same footnotes. It is Note 16 in FY2018–FY2026 and **Note 18** in FY2017.
S2 WHY: The blocker was a search artefact, not a disclosure gap. FY2017 was the Ind AS first-time-adoption year and carries a different note numbering — the other financial liabilities note is 18, not 16 — and FY2017's balance sheet has three columns rather than two, which is the same feature that caused W1_ledger §1.1's twenty-cell column shift. A search anchored on "Note 16" therefore finds nine years and reports three, because only FY2023–FY2026 had been read.
S3 EVIDENCE: Bucket (C) by year, each from that year's own annual report: `62,465 · 1,17,997 · 91,529 · 56,666 · 89,240 · 69,918 · 1,81,730 · 1,49,802 · 3,58,165 · 3,31,172 · 3,55,423` `[AR FY2017, Note 18, PDF p170/pr168 · AR FY2018 p175/pr168 · AR FY2019 p193/pr184 · AR FY2020 p205/pr198 · AR FY2021 p189/pr184 · AR FY2022 p194/pr185 · AR FY2023 p209/pr202 · AR FY24 p202/pr196 · AR FY25 p192/pr181 · AR FY26 p206/pr195]`. Every year's (A)+(B)+(C) ties to the balance-sheet caption exactly. `DERIVED: cumulative float FY2017–FY2026 = 3,55,423 − 62,465 = 2,92,958`; cumulative comparable-basis CFO `8,24,646 − 70,175 = 7,54,471`; own-account CFO `7,54,471 − 2,92,958 = 4,61,513`; against cumulative PAT of 6,48,302, a conversion of **0.712** against a headline **1.272**. The counter-proportion that makes 0.712 the honest number rather than a chosen one: the float contributed `2,92,958 / 8,24,646 = 35.5%` of a decade of reported operating cash, and the Core SGF add-backs a further `70,175 / 8,24,646 = 8.5%`, so 44.0% of ten years of headline CFO is neither own-account nor on a consistent basis. Sensitivity band, if only 90% to 110% of the float ran through the operating line: **0.667 to 0.757** — it does not reach 1 anywhere inside it.
S4 CONNECTS: Notes — the test only becomes runnable once RF-027's FY2025 basis change is neutralised, which required removing the four Core SGF adjustment lines from every year FY2017–FY2024, a total of ₹70,175 lakh that W3_notes had sized for FY2024 alone at ₹19,717 lakh. Business — the float is not a working-capital cycle but a consequence of consolidating a clearing corporation, so the correction is structural to the MII model and applies to NSE and MCX equally; W2_peers' conversion comparisons are computed on headline CFO for all four peers and are therefore comparing float behaviour, not earnings quality. Management commentary — in eight consecutive calls no analyst has asked about cash conversion and management has never volunteered an own-account cash figure, while publishing a standalone ROE of 49.07% in the MD&A `[AR FY26, MD&A, PDF p77/pr66]`. Governance — SEBI requires the segregation on the balance sheet through the SECC Regulations, which is why the disclosure exists at all; the company complies fully with the balance-sheet requirement and there is no equivalent cash-flow requirement.
DOMAINS: CashFlow, Notes, Business, Industry, MgmtCommentary
DISCONFIRM: Sought hard, because a result this different from the headline invites confirmation bias. (i) The single assumption — that the bucket-(C) movement travels in the aggregated working-capital line — is tested in all ten years and holds in sign in ten of ten, with the FY2026 reconciliation residual at 0.04% and FY2025's at 3.3%; but it is an ESTIMATE, and the company never disaggregates the line. (ii) A genuine presentation change works against the method: in FY2017–FY2019 trading-member deposits ran through FINANCING, not operating `[AR FY2017, PDF p119/pr117]`, which is bucket (A) rather than (C) and is worth 1,981 across the decade, 0.4% of the numerator. (iii) The cumulative PAT contains three one-off disposal gains that are investing cash by construction and can never appear in CFO — FY2018's 48,722 discontinued gain, FY2024's 40,662 exceptional net of 3,910 tax, and FY2020's 3,204; stripping all three raises the conversion to **0.825**, which is the number most favourable to the company that the evidence supports. (iv) Putting FY2025 and FY2026 back on the old SGF-inclusive basis instead of restating the earlier years gives 0.757. Every variant is below 1; none is above 0.83.
S5 MEANS: Over a full decade BSE has converted roughly seven-tenths of its reported profit into operating cash that belongs to its shareholders, while its published cash-flow statement says it converted more than one-for-one — and the entire difference is third-party money that the balance sheet has always separated and the cash-flow statement has never separated.
BASE-RATE: The pattern has cost money once, and the loss was measurement rather than cash. `records/cash_ledger_note.md` published a ten-year conversion of 1.264 which W1_ledger corrected to 1.269 and then declared unquotable; RF-005 was opened on the strength of the headline series; and W1.5_triage's 8-point screen was run on a number that has now moved from 1.27 to 0.71. Three internal artifacts in this run reached three different conclusions from the same ten filings, and each time the error ran in the company's favour. In the system, the base rate is well established for exchanges and clearing houses: LCH, DTCC and NSE all present member and settlement balances inside operating cash flow, and analyst coverage of NSE's unlisted paper has repeatedly quoted its CFO without the adjustment.
S6 IMPLICATION: The durable cash-generation figure for this company is roughly 0.71 to 0.83 of reported profit rather than 1.27, so any model that capitalises reported operating cash flow is capitalising a number that is between 54% and 79% too high (`DERIVED: 1.272 / 0.825 − 1 = 54.2%; 1.272 / 0.712 − 1 = 78.7%`), and the margin of safety required rises by that amount; the earnings-quality gate should carry 0.712 as the primary and 0.825 as the bound. Monitorable: bucket (C) at each reporting date — its ten-year mean of ₹1,50,000 lakh against ₹3,55,423 lakh at FY2026 means the reversal potential is roughly two-thirds of one year's PAT. Next check: FY2027 annual report, consolidated Note 16, and whether the FY2027 cash flow adds a fifth footnote excluding the clearing float as footnote 3 excluded the Core SGF.
SEVERITY: High

### FINDING: The two ₹100 maps diverge by ₹20.20 of cash per ₹100 of revenue, and 86.8% of the divergence is one working-capital line
S1 WHAT: Built on the same divisor of ₹4,833.95 lakh per ₹1, the FY2026 map on the reported basis converts ₹100 of revenue into ₹51.46 of profit and ₹64.21 of operating cash; on an own-account basis it converts the same ₹100 into ₹48.80 of profit and ₹44.01 of operating cash. Profit differs by ₹2.66; cash differs by ₹20.20.
S2 WHY: The two maps share every cost line — no expense is attributable to the float — and diverge at exactly two places. Revenue loses ₹3.55 because *Treasury income from clearing and settlement funds* of ₹17,142 lakh is income on members' money `[AR FY26, Note 22, PDF p211/pr200]`, and working capital swings by ₹17.54 because the reported presentation counts ₹69,188 lakh of members' and government money as operating cash while the own-account presentation does not. Everything else is arithmetic.
S3 EVIDENCE: `DERIVED: 64.21 − 44.01 = 20.20` of CFO per ₹100, of which the working-capital swing is `12.13 − (5.41) = 17.54`, i.e. `17.54 / 20.20 = 86.8%`; the revenue and tax effects together are `20.20 − 17.54 = 2.66`, 13.2%. The counter-proportion that gives the divergence its shape: on the reported basis working capital is a **source** of ₹12.13 per ₹100, on the own-account basis it is an **absorption** of ₹5.41 — the sign flips, which no amount of scaling can produce. In rupees, headline CFO 3,10,372 against own-account CFO 2,12,739, a difference of 97,633 = 31.5%; headline FCF 2,58,856 against own-account FCF 1,76,807, a difference of 82,049 = 31.7%. The own-account map is not an assertion: it reconciles to the balance sheet, `DERIVED: modelled own-account financial-asset build 2,43,159 against actual 6,14,282 − 3,71,074 = 2,43,208, residual 49 = 0.02%`.
S4 CONNECTS: Balance sheet — W3_balancesheet established that 45.1% of the funding side is not the company's money and that the operating asset base is only 10.0% of equity; this map shows the same structure running through the cash flow, and it shows that the own-account asset build of ₹2,43,208 lakh is what the retention actually bought. Business — the divergence exists because an exchange-and-clearing group holds float it does not own, which W1.7 §2 predicted and which the standard template would have missed entirely. Management commentary — management's own framing of the cash position is a standalone ROE of 49.07% and a market-capitalisation comparison `[Q4FY26 Concall 13May2026, MD & CEO]`, neither of which is a cash measure, and no own-account or float-adjusted figure has ever been published. Income statement — the profit maps differ by only ₹2.66, which is why the divergence is invisible to anyone reading the P&L, and why it took the balance-sheet note to find it. The compensating control is the two-sided earmarked asset test, which ties to 1.9%; the class of error it cannot catch is the statutory-remittance float, because Note 19's statutory remittances are not earmarked against any asset at all.
DOMAINS: CashFlow, IncomeStatement, BalanceSheet, Business, MgmtCommentary
DISCONFIRM: Sought. (i) The own-account map strips the treasury income on members' funds from both PAT and CFO; that income is genuinely earned by the group's risk management of the float and SEBI permits its recognition, so removing it entirely is the conservative bound rather than the certain answer — on the float-only definition W3_balancesheet used, FY2026 conversion is 1.093 rather than 0.907. (ii) The ₹15,584 lakh capital-advance correction reverses across FY2025 and FY2026, so the two-year total is unaffected and only the single-year maps move. (iii) Nothing in Ind AS requires the own-account presentation, and no peer publishes one, so this is an analyst construction and not a compliance finding. What cuts the other way and is decisive: the construction closes on the balance sheet to ₹49 lakh, which the reported presentation does not do at all — its two gross deposit lines cannot be reconciled to any note because footnotes 2 and 3 remove an undisclosed subset.
S5 MEANS: The difference between the two maps is not a rounding convention or a presentational preference — it is the difference between a business that funds itself from operations and one that funds itself from balances it must eventually give back, and on the reported map that distinction is invisible because both look identical down to the profit line.
BASE-RATE: The float has reversed at this company five times in ten years — bucket (C) fell in FY2018, FY2019, FY2021, FY2023 and FY2025, by 26,468, 34,863, 19,322, 31,928 and 26,993 respectively — and in each of those years reported CFO was negative or near zero while profit was positive. So the realised cost of relying on the reported map is on the record five times, and each time it appeared as an apparent cash-flow collapse that was not one. In the system, no exchange has ever reported a loss from returning member float, but every exchange's reported CFO series carries the same reversal shape.
S6 IMPLICATION: The ₹100 map that should feed the earnings-quality gate and the valuation is the own-account one, on which this business converts ₹44.01 of every ₹100 of revenue into cash it owns, spends ₹7.43 on assets and distributes ₹6.53, leaving ₹30.05 to compound in a securities portfolio; the reported map's ₹64.21 is not a claim on anything. Monitorable: the sign of the own-account working-capital line, which was negative in FY2026 for the first time in the three years it can be computed. Next check: FY2027 annual report, consolidated Notes 16 and 19 against the cash-flow working-capital block.
SEVERITY: High

### FINDING: The Core SGF stopped being a stress-test output in September 2025 and became a 5%-of-revenue levy, and the policy exists only in a concall transcript
S1 WHAT: The FY2026 accounting policy states that the Group "at least contributes amounts pertaining to Minimum Required Contribution to the Core Settlement Guarantee Fund maintained by clearing corporations, which is determined as per SEBI guidelines" `[AR FY26, Note 2.3.12, PDF p178/pr167]`. On 17 November 2025 management disclosed a different regime: "a BSE introduced policy to contribute 5% of transaction-related revenue to the core SGF on a monthly basis with a cap… as long as overall SGF is not exceeding 150% of the minimum requirement", live from September 2025, with ₹1,060 lakh contributed in that quarter under it `[Q2FY26 Concall 17Nov2025, MD & CEO]`. Neither the 5%, the 150% cap, nor the September start date appears anywhere in the FY2026 annual report.
S2 WHY: Management's stated reason is earnings smoothing, and it is explicit: "it is very difficult to predict the behaviour of core SGF requirement… This, in the past as we have seen, has been leading to a lot of sudden spurts in the requirement of core SGF and therefore having sudden impact on the quarterly earnings. In order to smoothen it and as a matter of financial prudence, what we thought was some minimum amount on a quarterly basis out of our revenue should be contributed" `[Q2FY26 Concall 17Nov2025, MD & CEO]`. The words in the policy that permit it are "at least" — the policy sets a floor, not a method, so a voluntary excess needs no policy amendment and triggers no Ind AS 8 disclosure.
S3 EVIDENCE: On FY2026 transaction charges of ₹3,79,499 lakh `[AR FY26, Note 22, PDF p211/pr200]`, `DERIVED: 3,79,499 x 5% = 18,975` a year against an actual FY2026 charge of ₹7,696 lakh — **2.47x** — and `18,975 / 4,83,395 = 3.93%` of revenue against `7,696 / 4,83,395 = 1.59%`, i.e. ₹3.93 of the ₹100 map instead of ₹1.59. The counter-proportion that shows the character of the item has changed: the ten-year charge ranged from ₹74 lakh (FY2020) to ₹9,170 lakh (FY2024), a 124x spread, and moved with no relationship to revenue — FY2026's charge **fell 14.5%** in a year revenue rose 63.5%; under the new policy the same charge becomes a fixed 5% of the fastest-growing line in the group. And the FY2026 number does not reconcile to the policy on any base: seven months at 5% of transaction charges would be `DERIVED: 3,79,499 x 5% x 7 / 12 = 11,069`, half as much again as the full year's actual charge of 7,696, and no note explains the difference.
S4 CONNECTS: Cash flow — the same item is the subject of RF-027, the FY2025 basis change that removed ₹19,717 lakh of Core SGF flows from the FY2024 comparative by footnote; so in two consecutive years the Core SGF changed how it is measured in the cash flow and how it is sized in the P&L, and neither change is in a note. Governance — a voluntary contribution to a non-refundable, non-distributable fund is a transfer of shareholders' money into restricted regulatory capital that cannot be reversed even if the corpus later exceeds the minimum, which policy 2.3.12 states plainly; it is a capital-allocation decision taken without a disclosed policy, in the same year the dividend payout fell to 17.8% (RF-010). Industry — 22.3% of ICCL's corpus was contributed by competitors clearing through it, NSE ₹26,529 lakh and MSE ₹934 lakh `[AR FY26, Note 41, PDF p231-232/pr220-221]`, so over-contributing strengthens a fund that also protects rivals' positions. Management commentary — the same call frames the retention as clearing-confidence spend: "a stronger balance sheet of an exchange is very essential to showcase to the world that the clearing corporation is strong enough" `[Q4FY26 Concall 13May2026, MD & CEO]`.
DOMAINS: Notes, IncomeStatement, CashFlow, Governance, Industry, MgmtCommentary
DISCONFIRM: Sought and substantially found. (i) The economics are conservative, not aggressive: contributing more to a settlement guarantee fund reduces reported profit and increases loss-absorbing capacity, which is the opposite of what earnings management would predict. (ii) The 150% cap is a genuine brake and management explained its purpose without being pressed. (iii) The policy wording "at least" does technically cover it, and there is no Ind AS requirement to disclose a voluntary contribution policy. (iv) The amounts so far are small — ₹1,060 lakh in the quarter of introduction, against quarterly PBT of ₹73,896 lakh, 1.4%. Against the company: a policy that will roughly two-and-a-half times a P&L line, permanently and irreversibly, is material by doctrine §3 trigger 3 and trigger 7 regardless of its current size, and the annual report is the source of record, not the transcript.
S5 MEANS: A charge that the annual report describes as a regulator-determined stress-test output is now, on management's own account, a self-imposed 5% levy on the group's fastest-growing revenue line — and a reader relying on the annual report alone would model it from a ten-year history that the company has already stopped following.
BASE-RATE: The fund has never paid a claim: no clearing-member default has been charged against ICCL's Core SGF in any of the ten years read, and the balance has risen in every one of them, from ₹17,605 lakh to ₹1,24,683 lakh. So the realised cost of the contribution is 100% of it — `DERIVED: cumulative eleven-year P&L charges 1,741 + 952 + 6,291 + 684 + 74 + 619 + 2,905 + 5,496 + 9,170 + 9,000 + 7,696 = 44,628` of shareholders' money placed permanently beyond reach with no loss ever absorbed. In the system the base rate is not zero — settlement guarantee funds exist because clearing defaults happen, and SEBI sizes them from monthly stress tests precisely because the loss is tail-shaped — but at this company the ratio of contributions made to losses absorbed is 44,628 to nil.
S6 IMPLICATION: The Core SGF step in the ₹100 map should be modelled forward at ₹3.93 rather than ₹1.59, which removes roughly ₹11,279 lakh a year of pre-tax profit from the base case, and the item should be treated as a permanent revenue-linked levy rather than a volatile one-off; the durability of the earnings stream is slightly reduced and its predictability slightly improved. Thesis-breaker for the disclosure question rather than the economics: if the FY2027 annual report still describes this as a Minimum Required Contribution regime, the annual report is no longer the source of record for this group's accounting policies. Monitorable: the quarterly Core SGF charge against 5% of that quarter's transaction charges, and whether the 150% cap is reached. Next check: Q2FY27 results and the FY2027 annual report, Note 2.3.12.
SEVERITY: High

### FINDING: The 3.4x capex step-up is a presentation artefact — on corrected cash it is 1.16x, and the composition of the cash figure is disclosed nowhere after being asked for on the record
S1 WHAT: FY2026 capex is reported as one combined cash-flow line of ₹51,516 lakh against ₹15,323 lakh, a 3.36x step-up, with no note reference and no capex slide in either 2026 investor deck `[AR FY26, Consolidated Cash Flow, PDF p165/pr154]`. ₹15,584 lakh of that ₹51,516 lakh was paid in FY2025 as a capital advance that ran through FY2025's operating section and was released through FY2026's operating section (RF-046) `[AR FY26, Note 13, PDF p202/pr191]` and `[AR FY25, Note 13, PDF p188/pr177]`.
S2 WHY: Capital advances are classified as an "other current asset" in Note 13 rather than as capital work in progress, so their payment and release both land in operating working capital, while the investing line's own title — "…intangible assets under development **and capital advances**" — reports the same rupee as an investing use in the year it is released. The accrual side is fully disclosed in nine asset classes; only the cash side is aggregated, and it is the cash side that every model uses.
S3 EVIDENCE: `DERIVED: corrected FY2026 cash capex 51,516 − 15,584 = 35,932; corrected FY2025 30,907 = 15,323 + 15,584; step-up 35,932 / 30,907 = 1.16x, not 51,516 / 15,323 = 3.36x`. The two-year total is unaffected: `DERIVED: 15,323 + 51,516 = 66,839 = 30,907 + 35,932`. The accrual bridge closes only on the reported basis: `DERIVED: 47,578 + 2,470 − 818 + 3,081 = 52,311; less non-cash FX 566, investment-property transfer 101 and the 918 rise in payables for fixed assets = 50,726 against a reported 51,516, residual 790 = 1.5%`. The counter-proportion that identifies the item: ₹15,584 lakh is 30.3% of the FY2026 capex line but **101.7%** of the FY2025 line — the same amount is a third of one year and more than all of the other. On composition: the accrual note splits ₹47,578 lakh into nine classes, of which buildings ₹18,022 lakh and computers and networking ₹18,530 lakh are 76.8%; the cash line of ₹51,516 lakh splits into none.
S4 CONNECTS: Management commentary — the break-up was requested on the record and refused, with a promise: "Rs. 313 crores is not a small number… It is a mix of multiple things, including the physical and technology infrastructure. What we can do is right now in front of me, I don't have the breakup. Offline, certainly we can take your call… we will be able to provide you a breakup" `[Q2FY26 Concall 17Nov2025, MD & CEO]`; nothing has been published in the FY2026 annual report, the Q4FY26 deck or the Q1FY27 deck since. Governance — W3_balancesheet F8 records that the consolidated CWIP and intangible-development ageing schedules required by Schedule III have been omitted for three consecutive years while the standalone carries both, so the one consolidated disclosure that would age the capital programme is also absent. Balance sheet — the corrected figures change what the retention bought: cash capex of ₹35,932 lakh against a proposed dividend of ₹41,198 lakh means distribution exceeded investment, reversing the direction W2_promise recorded as disconfirming evidence in management's favour. Business — management names colocation as the return, "the returns from this capex cycle are already visible in the 133% growth in colocation revenues", on colocation and connectivity revenue of ₹17,109 lakh `[AR FY26, Note 22, PDF p211/pr200]`.
DOMAINS: CashFlow, BalanceSheet, Notes, MgmtCommentary, Governance
DISCONFIRM: Sought. (i) Total cash is not misstated in either year and the errors reverse across the pair, so this is a classification finding and not a cash finding — W3_balancesheet said so first and it is right. (ii) The accrual disclosure is genuinely good: nine asset classes, an exact roll-forward, a quantified useful-life estimate change, and standalone ageing schedules showing no overdue or over-budget project. (iii) The auditor is not required to disaggregate a combined caption and issued an unmodified opinion. (iv) The capex is demonstrably real and capitalised rather than parked: PPE rose from ₹22,217 lakh to ₹56,259 lakh while CWIP **fell** from ₹4,073 lakh to ₹3,255 lakh. Against the company: the composition question was asked, an answer was promised, and ten months later nothing has been published — that is a choice, not an omission.
S5 MEANS: The most quoted operating statistic of BSE's FY2026 — that capital expenditure tripled — is an artefact of where a ₹15,584 lakh advance was recorded, and the underlying spend rose 16%; and the one figure that would let a reader test the story management tells about the cycle, the composition of the cash line, has been requested once and withheld twice since.
BASE-RATE: No loss and no restatement has arisen from either the misclassification or the non-disclosure: the roll-forward reconciles, the standalone ageing schedules show no project overdue or over cost in either year, and the two-year cash total is right. The base rate that matters is the pattern of withheld composition at this company, and it is now four instances in one reporting year — the capex break-up refused on 17-Nov-2025, the transaction-charges line left as one number at 78.5% of revenue (RF-003), statutory remittances at ₹74,780 lakh with no sub-schedule, and the consolidated CWIP and IAUD ageing schedules absent three years running.
S6 IMPLICATION: Any model of this company's reinvestment rate should use ₹35,932 lakh for FY2026 and ₹30,907 lakh for FY2025, which makes the reinvestment story a steady 1.16x rather than a step change, and should carry the maintenance-growth split as an ESTIMATE of roughly 56% growth on corrected cash rather than the 69% the reported line implies; the asset base is real and the disclosure around it is the weakest part of the group's reporting. Monitorable: whether the FY2027 consolidated cash flow presents capital advances inside investing, and whether the promised capex break-up appears in any FY2027 filing. Next check: FY2027 annual report, consolidated Note 13 and the investing section.
SEVERITY: Medium

### FINDING: The retained cash funded a securities portfolio, not the capex cycle — 72.3% of own-account sources went into deposits and funds, and the ICCL trap explains one twentieth of it
S1 WHAT: FY2026 own-account sources of cash were ₹2,44,003 lakh. Cash capex consumed ₹35,932 lakh and dividends ₹31,585 lakh, together 27.7%; the remaining ₹1,76,486 lakh, plus ₹66,673 lakh of fair-value gain, retained float income and government money held, went into mutual funds, bonds, state development loans, government securities and bank deposits — an own-account financial-asset build of ₹2,43,208 lakh `[AR FY26, Notes 9, 11 & 12, PDF p190-202/pr179-191]`.
S2 WHY: There was no competing use of the money. Own-account free cash flow of ₹1,76,807 lakh covers the proposed dividend of ₹41,198 lakh 4.29x and would cover a 100% payout of profit attributable 0.71x; contracted capital commitments are ₹10,029 lakh `[AR FY26, Note 38, PDF p227/pr216]`; and the parent's own retained earnings of ₹4,55,828 lakh, which Note 15.4 makes the legal distribution cap, are 11.1x the proposed dividend `[AR FY26, Standalone Note 15, PDF p280/pr269]`. Neither cash nor law nor a committed project constrains the payout. What management gives instead is a set of intentions — technology spend "almost going to be doubling" from around ₹300 crore, colocation capacity, a possible Mumbai land purchase, and a clearing-confidence balance sheet `[Q4FY26 Concall 13May2026, MD & CEO]`.
S3 EVIDENCE: `DERIVED: 35,932 / 2,44,003 = 14.7% to capex; 31,585 / 2,44,003 = 12.9% to dividend; the balance 72.3% to financial assets`. The counter-proportion that sizes the ICCL channel against the whole: W3_group_rpt established that ₹12,607 lakh of pre-tax profit moved into ICCL through the intra-group clearing charge and ICCL returned ₹3,540 lakh, so `DERIVED: 12,607 − 3,540 = 9,067` is trapped inside a regulated clearing corporation — but `DERIVED: 9,067 / 1,76,486 = 5.1%` of the year's net own-account retention. Nineteen twentieths of the retention is in the parent's treasury book and is not trapped by anything. Within the portfolio the mix shifted decisively toward mark-to-market instruments: mutual funds and ETFs `DERIVED: 2,21,094 / 1,18,110 = 1.87x`, while bonds and state development loans were roughly flat at 69,761 against 56,631 `[AR FY26, Note 9, PDF p191-192/pr180-181]`. The whole construction closes: modelled build 2,43,159 against actual 2,43,208, residual 49 = 0.02%.
S4 CONNECTS: Governance — RF-010 records the payout falling 99% to 17.8% in three years with no dividend policy, no target ratio and no capital-allocation disclosure, and management answering the question twice with a different metric, most recently market capitalisation; this finding supplies what the mechanism was missing, which is that the cash did not go where the answers implied. Balance sheet — own-account financial assets are now 90.4% of total equity while the operating asset base is 10.0%, so the group's shareholders own a securities portfolio with an exchange attached to it, and FY2026 increased that ratio rather than reducing it. Income statement — the consequence is already visible in earnings quality: 30.6% of FY2026 investment income of ₹29,030 lakh is fair-value movement rather than contractual yield `[AR FY26, Note 23, PDF p211/pr200]`, so retention is converting an exchange's operating earnings into a treasury book's mark-to-market. Business — the MII overlay's capital-intensity replacement, regulatory capital per rupee of revenue, fell 62% in two years, so the regulatory reason to hold capital is weakening as the pile grows.
DOMAINS: CashFlow, BalanceSheet, IncomeStatement, Governance, MgmtCommentary, Business
DISCONFIRM: Sought and partly found, and it is stronger than the payout critique usually allows. (i) Management's reasoning is coherent and stated: a 99% payout at FY2023 profit levels signalled no reinvestment opportunity, and "a 100% dividend payout… may indicate a situation where the company is not having any growth idea at all" `[Q4FY26 Concall 13May2026, MD & CEO]`. (ii) The capex is real and rising, PPE more than doubled, and the technology budget is flagged to double again. (iii) The clearing-corporation over-capitalisation worked — ICCL's clearing share reached 25-27% and the MD ties it directly to balance-sheet strength. (iv) There has been no dilution, ever, and the buyback take-up claim checks out at 2.0% of the earlier programme. (v) The treasury book is not idle: it earned ₹29,030 lakh, and the MD explicitly rejected the 4-4.5% return premise put to him. What survives all of that: the money went into securities, the amount that went into assets is smaller than reported, and there is still no policy.
S5 MEANS: BSE is not retaining cash to fund a capital programme — the capital programme consumed one seventh of the cash available and less than the dividend — it is accumulating a securities portfolio at roughly ₹2,000 crore a year, and the one structural reason offered for the retention, capital trapped inside the regulated clearing subsidiary, accounts for five per cent of it.
BASE-RATE: Retention at this company has never destroyed value and has twice created it: the CDSL stake produced realised gains of ₹9,158 lakh in FY2020 and ₹50,417 lakh standalone in FY2024, and the colocation capex is producing 133% revenue growth on the segment management names. The realised loss on the other side of the ledger is India International Exchange — ₹20,919 lakh injected across ten years, ten consecutive loss years, ₹24,023 lakh of cumulative loss and no dividend ever `[AR FY26, Form AOC-1, PDF p312/pr301]` — which is the demonstrated cost of undisclosed capital allocation at this group; the amount injected over a decade is `DERIVED: 20,919 / 1,76,486 = 11.9%` of what the group retained in FY2026 alone, so the pool being allocated without a policy is now an order of magnitude larger than the one loss on record.
S6 IMPLICATION: The reinvestment rate that drives any compounding case for this company is not the capex line — it is the rate of return on a growing securities book, which earned ₹29,030 lakh on an average own-account financial-asset base of `DERIVED: (6,14,282 + 3,71,074) / 2 = 4,92,678`, i.e. 5.89%, against a business earning 43.75% on equity; every rupee retained and not deployed dilutes the group's return on capital toward the treasury rate. The driver assumptions should therefore carry retention as a drag rather than as growth capital until the capex programme actually absorbs it. Monitorable: cash capex against own-account free cash flow each year, and whether the technology budget management says will double actually appears in the FY2027 investing line. Next check: FY2027 annual report, consolidated cash flow investing section and Note 13.
SEVERITY: Medium

---

## 8. HANDOVER — positions recorded, register changes, and gaps

### 8.1 Contradictions and corrections recorded rather than resolved (doctrine §10)

1. **RF-028, the CDSL dividend.** Three positions are now on the record and all three stay: the
   register's "consolidation mechanic" gloss (**wrong on Ind AS 7**, §1.2); W3_balancesheet's own text,
   which locates the money in investing (**correct**, §1.4); and W3_group_rpt's ₹7,368 lakh
   two-year CFO overstatement (**not supported** — the operating section reconciles to ₹398 lakh in
   aggregate, §1.4). **The register entry should be corrected and the window extended from two years
   to eight, ₹18,100 lakh.**
2. **W1.5_triage's "ten-year own-account test cannot be run" is overturned**, with the evidence in
   §3.1. W1.5's position is retained; it was a search artefact caused by FY2017's Note 18 numbering.
3. **W1_ledger's own-account series is superseded but not deleted.** Its 0.942 three-year cumulative
   and 1.393 headline stand on the record; on this file's comparable basis the same three years give
   0.896 and the ten-year figure is **0.712**. The difference is basis, and it is quantified
   (₹70,175 lakh of Core SGF add-backs, plus total-operations alignment).
4. **W2_promise's disconfirming evidence on the payout weakens.** It records ₹515 crore of capex
   against ₹412 crore of dividend as investment exceeding distribution; on corrected cash it is
   ₹359 crore against ₹412 crore, and distribution exceeded investment. Both stand.
5. **W3_notes' RF-027 arithmetic is confirmed independently and extended.** The four deleted FY2024
   lines of ₹19,717 lakh are 99.3% of a ₹19,857 lakh restatement — reproduced here from the FY2024 and
   FY2025 statements — and the same four lines exist in **every year FY2017 to FY2024**, totalling
   **₹70,175 lakh**, which is what a ten-year series must remove.

### 8.2 Red-flag register — proposed changes (not applied; this file does not own the register)

| Flag | Proposed | Reason |
|---|---|---|
| **RF-005** | **Re-closed with a new number.** Own-account conversion is measurable over **ten** years, not three, and it is **0.712** | §3 |
| **RF-028** | **Correct the entry, upgrade Watch → Medium, extend to eight years / ₹18,100 lakh, withdraw the CFO-overstatement claim** | §1 |
| **RF-046** | **Confirmed from the other direction and extended:** the corrected capex step-up is 1.16x, not 3.4x | §5.1 |
| **NEW — the government float** | **Proposed High.** ₹44,937 lakh of FY2026 CFO is tax collected for the authorities; 95.1% of the year's largest working-capital line is third-party money | §2.4, F2 |
| **NEW — the Core SGF policy** | **Proposed High.** A 5%-of-transaction-revenue voluntary contribution policy capped at 150% of the minimum requirement, live from September 2025, disclosed on a concall and absent from the annual report | §4 chain 4, F5 |
| **NEW — statutory-remittance restatement** | **Proposed Watch.** FY2025 statutory remittances reported at 24,399 and shown as 29,843 in the FY2026 comparative, a ₹5,444 lakh reclassification with no note; not in `records/restatements.md` | §3.3 |
| **RF-010** | **Mechanism completed.** The ICCL trap explains 5.1% of FY2026 retention; 72.3% of own-account sources went into the securities book | §6.2, F7 |

### 8.3 Gap register additions (doctrine §9)

| ID | Gap | Peers disclose? | Settling document |
|---|---|---|---|
| G-CASH-01 | No sub-schedule to statutory remittances of ₹74,780 lakh; ₹23,302 lakh unattributed after the MD&A's STT identification | Not tested | A statutory-dues break-up in Note 19, or BSE's GST and STT returns |
| G-CASH-02 | The consolidated cash-flow working-capital lines are never disaggregated; the company publishes no reconciliation of the ₹72,767 lakh line to Notes 16 and 19 | Not tested | A supporting schedule to the consolidated cash-flow working-capital block |
| G-CASH-03 | Composition of the ₹51,516 lakh capex cash line — asked on 17-Nov-2025, promised offline, never published | NSE and MCX publish capex by category in their decks | The break-up management undertook to provide; or a capex slide in any FY2027 deck |
| G-CASH-04 | Maintenance versus growth capex is not separable from any disclosure | Not tested | A replacement-versus-expansion split in the PPE note or the MD&A |
| G-CASH-05 | The voluntary Core SGF contribution policy — 5% of transaction revenue, 150% cap, September 2025 start — is not in the annual report | n/a — company-specific policy | Note 2.3.12 of the FY2027 annual report, or a stock-exchange intimation of the board resolution |
| G-CASH-06 | Gross fixed-deposit flows of ₹3,29,857 lakh and ₹1,74,471 lakh cannot be reconciled to the balance sheet because footnotes 2 and 3 exclude an undisclosed subset | Not tested | A statement of which balances footnotes 2 and 3 remove, with amounts |

### 8.4 For the waves downstream

- **W5 earnings quality:** the numbers to carry are **own-account ten-year conversion 0.712**
  (bound 0.825 ex one-off disposal gains; band 0.667–0.757 on the float assumption), **FY2026
  own-account CFO ₹2,12,735 lakh** against a reported ₹3,10,368 lakh, and **own-account FCF
  ₹1,76,807 lakh**. Reported CFO should not be used on any single year.
- **W4_capalloc:** §6.2's sources and uses closes to ₹49 lakh and is the frame for the payout
  question; the ICCL trap is 5.1% of retention, not the explanation.
- **W8 valuation:** the ₹100 map to use is Map B. Cash capex is ₹35,932 lakh, not ₹51,516 lakh, and
  the reinvestment rate is 1.16x the prior year, not 3.4x. The Core SGF should be modelled at
  ₹3.93 per ₹100 of revenue, not ₹1.59.
- **`records/balance_cash_10y.csv`:** four TRACED rows can now be extended to ten years —
  `ofl_owned_current`, `ofl_earmarked_current`, `ofl_clearing_settlement_current` (FY2016–FY2026,
  §3.1) and a new `statutory_remittances` row (FY2016–FY2026, §3.3). The **derived** own-account CFO
  series is deliberately **not** proposed for the CSV: it is an `ESTIMATE`, and an estimate in a
  machine-read record file reads as a fact. It lives in §3.3 and in the chain record at §4.
