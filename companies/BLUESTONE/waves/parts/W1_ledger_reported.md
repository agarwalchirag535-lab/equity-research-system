# W1 — Evidence ledger: the REPORTED statements, FY2025 and FY2026 (standalone AND consolidated)

**Agent:** W1 ledger — reported statements slice · **Compiled:** 2026-09-09
**Sources read in full:** `data/text/BLUESTONE-AR-FY2026.txt` (314 PDF pages) · `data/text/BLUESTONE-AR-FY2025.txt` (230 PDF pages)
**Status:** TRANSCRIPTION WITH TAGS. No S1–S6, no chain records, no conclusions, no ratios computed that the
company did not print. Where an arithmetic check was run it is shown inline and labelled, per doctrine §4a
(triggers 1 and 3: column sums >7 operands, and exact tie-outs).

---

## 0. Scope, unit rule, basis rule, citation rule

### 0a. UNITS — verified on the page, not assumed

Every page of both annual reports' financial statements and notes carries a printed header:

> **AR FY2026:** *"(All amounts are in INR million unless otherwise stated)"* — appears on the standalone
> Balance Sheet `[AR FY26, SA BS, p164/pr185]`, SA P&L `[p165/pr186]`, SA Cash Flows `[p166/pr187]`,
> SA SOCIE `[p168–169/pr189–190]`, every page of SA Notes `[p181–231/pr202–252]`, the consolidated
> Balance Sheet `[p243/pr264]`, CFS P&L `[p244/pr265]`, CFS Cash Flows `[p245–246/pr266–267]`,
> CFS SOCIE `[p247–248/pr268–269]` and every page of CFS Notes `[p261–313/pr282–334]`.

> **AR FY2025:** *"(All amounts are in ` million unless otherwise stated)"* — the backtick is the PDF's
> rendering of the rupee glyph. Appears on SA BS `[AR FY25, SA BS, p97/pr92]`, SA P&L `[p98/pr93]`,
> SA SOCIE `[p99–100/pr94–95]`, SA Cash Flows `[p101–102/pr96–97]`, SA Notes `[p103–159/pr98–154]`,
> CFS BS `[p166/pr161]`, CFS P&L `[p167/pr162]`, CFS SOCIE `[p168–169/pr163–164]`,
> CFS Cash Flows `[p170–171/pr165–166]`, CFS Notes `[p172–230/pr167–225]`.

**Therefore: every number in §1–§5 and §8 of this ledger is in ₹ MILLION unless the row says otherwise.**

**Two exceptions inside the same documents, both live traps:**

| Where | Unit actually printed | Verbatim header |
|---|---|---|
| **AR FY26 Annexure-2 FORM AOC-1** `[AR FY26, p79–80/pr100–101]` | **₹ absolute rupees** | *"(Information in respect of each subsidiary to be presented amount in Rs)"* / *"(Amount in Rupees)"* |
| **AR FY25 Form AOC-1** `[AR FY25, p49–50/pr44–45]` | **₹ absolute rupees** | same form |

§8 of this ledger states the AOC-1 figure **as printed** and gives the ₹-million equivalent alongside,
each labelled.

### 0b. BASIS — reported, not restated

Everything below is **REPORTED** (audited statutory Ind AS accounts). It is a **different basis** from the
*Restated Consolidated Summary Statements* in the Prospectus/RHP for FY23/FY24/FY25 and must never be
joined to those without the basis stated on each point (`state/TEMPLATES.md`, new-listing additions).

```
BASIS: FY24 = AR FY25 comparative, REPORTED | FY25 = AR FY25 primary AND AR FY26 comparative, REPORTED
       (both bases named per row where they differ) | FY26 = AR FY26 primary, REPORTED
       Prospectus/RHP restated FY23–FY25 is a SEPARATE basis and is NOT in this file.
```

**FY25 appears on two reported presentations** — as the primary year in AR FY2025 and as the comparative
in AR FY2026. AR FY2026 Note 55 (SA) / Note 58 (CFS) states: *"Previous year's figures have been
regrouped/reclassified, wherever necessary, to conform to current year classification"*
`[AR FY26, SA Note 55, p231/pr252]` `[AR FY26, CFS Note 58, p313/pr334]`. Where the two presentations of
FY25 differ, **both are recorded and the row is marked DISAGREE**. See §9.

### 0c. Citation

`[AR FY26, SA Note 25, p206/pr227]` — PDF page from the `===== PDF PAGE n =====` marker, printed page after
`/pr`. AR FY26 mapping: `printed = PDF + 21` for p31–p313. AR FY25 mapping: `printed = PDF − 5` throughout.
`SA` = standalone, `CFS` = consolidated. **Note numbers differ between SA and CFS and between years** —
every citation names the statement set and the year.

### 0d. Auditor and signatories on the record

| Item | FY2026 | FY2025 |
|---|---|---|
| Auditor firm | **M S K A & Associates LLP** (formerly M S K A & Associates), FRN **105047W/W101187** `[AR FY26, SA BS, p164/pr185]` | **M S K A & Associates**, FRN **105047W** `[AR FY25, SA BS, p97/pr92]` |
| Engagement partner | Ankush Agrawal, M.No. 159694 | Ankush Agrawal, M.No. 159694 |
| UDIN — SA report | **26159694FBQAUO4774** `[AR FY26, p155/pr176]` | **25159694BMLWGT7265** `[AR FY25, p89/pr84]` |
| UDIN — CFS report | **26159694CAQCKF4199** `[AR FY26, p238/pr259]` | **25159694BMLWGU2463** `[AR FY25, p163/pr158]` |
| Date of audit report / FS authorisation | **23 April 2026** `[AR FY26, SA Note 52, p230/pr251]` | **24 April 2025** `[AR FY25, SA Note 56, p159/pr154]` |
| MD & CEO | Gaurav Singh Kushwaha, DIN 01674879 | same |
| Director | Sameer Dilip Nath, DIN 07551506 | same |
| CFO | Rumit Dugar | Rumit Dugar |
| Company Secretary | **Paras Shah, M.No. 30357** | **Jasmeet Saluja, M.No. 46206** |

---

## 1. STATEMENT OF PROFIT AND LOSS — every line as printed

### 1.1 STANDALONE — AR FY2026 (FY26 primary, FY25 comparative)

**Unit: ₹ million.** Source: `[AR FY26, SA Statement of Profit and Loss, p165/pr186, REPORTED]`

| Line, as printed | Note | FY2026 | FY2025 |
|---|---|---|---|
| **Income** | | | |
| Revenue from operations | 25 | 24,412.30 | 17,700.02 |
| Other income | 26 | 491.81 | 599.18 |
| **Total income** | | **24,904.11** | **18,299.20** |
| **Expenses** | | | |
| Cost of materials consumed | 27 | 22,042.90 | 17,215.35 |
| Change in inventories of finished goods, work-in-progress and stock-in-trade | 28 | (8,039.58) | (6,230.46) |
| Employee benefits expense | 29 | 2,786.94 | 2,022.43 |
| Finance costs | 30 | 2,095.18 | 2,075.42 |
| Depreciation and amortization expense | 31 | 2,081.18 | 1,474.75 |
| Other expenses | 32 | 3,677.49 | 3,933.85 |
| **Total expenses** | | **24,644.11** | **20,491.34** |
| **Profit/(Loss) before tax** | | **260.00** | **(2,192.14)** |
| Tax expenses: Current tax | 34 | – | – |
| Tax expenses: Deferred tax | 34 | – | – |
| **Total tax expenses** | | **–** | **–** |
| **Profit/(Loss) for the year** `A` | | **260.00** | **(2,192.14)** |
| **Other comprehensive income** — *Items that will not be reclassified subsequently to profit or loss:* | | | |
| i. Re-measurement of employee defined benefit plans | 33 | (0.23) | (8.10) |
| ii. Income tax on (i) above | 34 | – | – |
| **Other comprehensive loss for the year, net of tax** `B` | | **(0.23)** | **(8.10)** |
| **Total comprehensive income/(loss) for the year** `A+B` | | **259.77** | **(2,200.24)** |
| **Earnings per share (in ₹) (Nominal value of ₹ 1 each)** — Basic | 36 | **2.18** | **(78.86)** |
| **Earnings per share (in ₹) (Nominal value of ₹ 1 each)** — Diluted | 36 | **2.07** | **(78.86)** |

*Tie-out (DERIVED, code-run per §4a trigger 1): total expenses FY26 = 22,042.90 − 8,039.58 + 2,786.94 +
2,095.18 + 2,081.18 + 3,677.49 = 24,644.11 ✔ exact. FY25 = 20,491.34 ✔ exact.*
*Tie-out: 24,904.11 − 24,644.11 = 260.00 ✔.*

**NOTE ON A LINE THAT DOES NOT EXIST:** there is **no exceptional items line** on the standalone P&L in
either year, and **no separate "Purchases of stock-in-trade"** line standalone (that line exists only on the
consolidated face — see §1.3).

### 1.2 STANDALONE — AR FY2025 (FY25 primary, **FY24 comparative — a REPORTED FY24, a basis distinct from the Prospectus restated FY24**)

**Unit: ₹ million.** Source: `[AR FY25, SA Statement of Profit and Loss, p98/pr93, REPORTED]`

| Line, as printed | Note | FY2025 | **FY2024 (AR FY25 comparative, REPORTED)** |
|---|---|---|---|
| Revenue from operations | 27 | 17,700.02 | 12,658.39 |
| Other income | 28 | 599.18 | 376.52 |
| **Total income** | | **18,299.20** | **13,034.91** |
| **Cost of raw materials consumed** *(label differs from FY26 — see §9)* | 29 | 17,215.35 | 12,346.71 |
| Change in inventories of finished goods, work-in-progress and stock-in-trade | 30 | (6,230.46) | (4,803.30) |
| Employee benefits expense | 31 | 2,022.43 | 1,384.25 |
| Finance costs | 32 | 2,075.42 | 1,376.71 |
| Depreciation and amortization expense | 33 | 1,474.75 | 952.66 |
| Other expenses | 34 | 3,933.85 | 3,200.24 |
| **Total expenses** | | **20,491.34** | **14,457.27** |
| **Loss before tax** | | **(2,192.14)** | **(1,422.36)** |
| Current tax | 36 | – | – |
| Deferred tax | 36 | – | – |
| **Total tax expenses** | | **–** | **–** |
| **Loss for the year** `A` | | **(2,192.14)** | **(1,422.36)** |
| OCI — i. Re-measurement of employee defined benefit plans | 35 | (8.10) | 9.77 |
| OCI — ii. Income tax on (i) above | 36 | – | – |
| **Other comprehensive (loss)/income for the year, net of tax** `B` | | **(8.10)** | **9.77** |
| **Total comprehensive loss for the year** `A+B` | | **(2,200.24)** | **(1,412.59)** |
| **EPS (in ₹) (Nominal value of ₹ 1 each)** — Basic | 38 | **(78.86)** | **(78.36)** |
| **EPS (in ₹) (Nominal value of ₹ 1 each)** — Diluted | 38 | **(78.86)** | **(78.36)** |

*Every FY25 figure above is identical to the FY25 comparative column printed in AR FY2026 §1.1 — the two
reported presentations of the FY25 P&L face AGREE line for line, with one exception: the label of the
first expense head (see §9, row A-12).*

### 1.3 CONSOLIDATED — AR FY2026 (FY26 primary, FY25 comparative)

**Unit: ₹ million.** Source: `[AR FY26, CFS Statement of Profit and Loss, p244/pr265, REPORTED]`

| Line, as printed | Note | FY2026 | FY2025 |
|---|---|---|---|
| Revenue from operations | 26 | **24,364.24** | 17,700.02 |
| Other income | 27 | 495.76 | 600.34 |
| **Total income** | | **24,860.00** | **18,300.36** |
| Cost of materials consumed | 28 | 22,043.45 | 17,215.35 |
| **Purchases of stock-in-trade** *(new line, consolidated only)* | 29 | **127.52** | – |
| Change in inventories of finished goods, work-in-progress and stock-in-trade | 30 | (8,241.16) | (6,230.46) |
| Employee benefits expense | 31 | 2,824.43 | 2,026.02 |
| Finance costs | 32 | 2,104.11 | 2,075.45 |
| Depreciation and amortization expense | 33 | 2,099.27 | 1,474.89 |
| Other expenses | 34 | 3,715.07 | 3,938.04 |
| **Total expenses** | | **24,672.69** | **20,499.29** |
| **Profit/(Loss) before share of profit/(loss) of an investment accounted for using the equity method and tax** | | **187.31** | **(2,198.93)** |
| Share of loss of investment accounted for using the equity method | 50 | (55.52) | (19.44) |
| **Profit/(Loss) before tax** | | **131.79** | **(2,218.37)** |
| Current tax | 36 | – | – |
| Deferred tax | 36 | – | – |
| **Total tax expenses** | | **–** | **–** |
| **Profit/(Loss) for the year** `A` | | **131.79** | **(2,218.37)** |
| OCI — i. Re-measurement of employee defined benefit plans | 35 | (0.23) | (8.10) |
| OCI — ii. Income tax on (i) above | 36 | – | – |
| **Net other comprehensive loss for the year, net of tax** `B` | | **(0.23)** | **(8.10)** |
| **Total comprehensive income/(loss) for the year** `A+B` | | **131.56** | **(2,226.47)** |
| **Profit/(Loss) attributable to: Owners of the Parent** | | **148.37** | **(2,216.69)** |
| **Profit/(Loss) attributable to: Non-Controlling Interest** | | **(16.58)** | **(1.68)** |
| — total | | 131.79 | (2,218.37) |
| OCI attributable to: Owners of the Parent | | (0.23) | (8.10) |
| OCI attributable to: Non-Controlling Interest | | – | – |
| — total | | (0.23) | (8.10) |
| Total comprehensive income attributable to: Owners of the Parent | | 148.14 | (2,224.79) |
| Total comprehensive income attributable to: Non-Controlling Interest | | (16.58) | (1.68) |
| — total | | 131.56 | (2,226.47) |
| **EPS (in INR) (Nominal value of INR 1 each)** — Basic | 38 | **1.10** | **(79.74)** |
| **EPS (in INR) (Nominal value of INR 1 each)** — Diluted | 38 | **1.05** | **(79.74)** |

*Tie-out (code-run): total expenses FY26 = 22,043.45 + 127.52 − 8,241.16 + 2,824.43 + 2,104.11 + 2,099.27 +
3,715.07 = 24,672.69 ✔ exact.*
**→ The FY26 consolidated EPS does not recompute from its own stated numerator. See §9, row A-01 — the
single largest internal contradiction found in this slice.**

### 1.4 CONSOLIDATED — AR FY2025 (FY25 primary, FY24 comparative)

**Unit: ₹ million.** Source: `[AR FY25, CFS Statement of Profit and Loss, p167/pr162, REPORTED]`

| Line, as printed | Note | FY2025 | **FY2024 (AR FY25 comparative, REPORTED)** |
|---|---|---|---|
| Revenue from operations | 27 | 17,700.02 | 12,658.39 |
| Other income | 28 | 600.34 | 376.52 |
| **Total income** | | **18,300.36** | **13,034.91** |
| Cost of raw materials consumed | 29 | 17,215.35 | 12,346.71 |
| Change in inventories of FG and WIP and stock-in-trade | 30 | (6,230.46) | (4,803.30) |
| Employee benefits expense | 31 | 2,026.02 | 1,384.25 |
| Finance costs | 32 | 2,075.45 | 1,376.71 |
| Depreciation and amortization expense | 33 | 1,474.89 | 952.66 |
| Other expenses | 34 | 3,938.04 | 3,200.24 |
| **Total expenses** | | **20,499.29** | **14,457.27** |
| **Loss before share of profit/(loss) of an investments accounted for using the equity method and tax** | | **(2,198.93)** | **(1,422.36)** |
| Share of loss of investments accounted for using the equity method | 51 | (19.44) | – |
| **Loss before tax** | | **(2,218.37)** | **(1,422.36)** |
| Current tax / Deferred tax / Total tax expenses | 36 | – | – |
| **Loss for the year** `A` | | **(2,218.37)** | **(1,422.36)** |
| OCI — Re-measurement of employee defined benefit plans | 35 | (8.10) | 9.77 |
| **Net OCI for the year, net of tax** `B` | | **(8.10)** | **9.77** |
| **Total comprehensive loss for the year** `A+B` | | **(2,226.47)** | **(1,412.59)** |
| Loss attributable to: Owners of the Parent | | (2,216.69) | (1,422.36) |
| Loss attributable to: Non-Controlling Interest | | (1.68) | – |
| OCI attributable to: Owners / NCI | | (8.10) / – | 9.77 / – |
| Total comprehensive income attributable to: Owners / NCI | | (2,224.79) / (1.68) | (1,412.59) / – |
| **EPS (in ₹) (Nominal value of ₹ 1 each)** — Basic | 38 | **(79.74)** | **(78.36)** |
| **EPS (in ₹) (Nominal value of ₹ 1 each)** — Diluted | 38 | **(79.74)** | **(78.36)** |

*FY25 consolidated EPS recomputes exactly from owners' share: (2,216.69) / 27,799,051 = (79.74) ✔.
The FY26 consolidated EPS does not (§9, A-01).*

### 1.5 The SA → CFS bridge on the P&L face, both years (as printed, no interpretation)

**Unit: ₹ million.**

| Line | FY26 SA | FY26 CFS | Δ | FY25 SA | FY25 CFS | Δ |
|---|---|---|---|---|---|---|
| Revenue from operations | 24,412.30 | 24,364.24 | **(48.06)** | 17,700.02 | 17,700.02 | – |
| Other income | 491.81 | 495.76 | +3.95 | 599.18 | 600.34 | +1.16 |
| Total expenses | 24,644.11 | 24,672.69 | +28.58 | 20,491.34 | 20,499.29 | +7.95 |
| PBT (before associate share) | 260.00 | 187.31 | (72.69) | (2,192.14) | (2,198.93) | (6.79) |
| Share of associate loss | n/a | (55.52) | — | n/a | (19.44) | — |
| PAT | 260.00 | 131.79 | (128.21) | (2,192.14) | (2,218.37) | (26.23) |
| PAT — owners | n/a | 148.37 | — | n/a | (2,216.69) | — |
| Basic EPS (₹) | 2.18 | 1.10 | (1.08) | (78.86) | (79.74) | (0.88) |

Tags: SA FY26/FY25 `[AR FY26, SA P&L, p165/pr186]`; CFS FY26/FY25 `[AR FY26, CFS P&L, p244/pr265]`.

---

## 2. BALANCE SHEET — every line as printed, both sides

### 2.1 STANDALONE — AR FY2026

**Unit: ₹ million.** Source: `[AR FY26, SA Balance Sheet, p164/pr185, REPORTED]`

| Line, as printed | Note | As at 31-Mar-2026 | As at 31-Mar-2025 |
|---|---|---|---|
| **ASSETS — Non-current assets** | | | |
| Property, plant and equipment | 3 | 2,638.59 | 2,659.82 |
| Right-of-use assets | 4 | 8,430.31 | 7,430.33 |
| Capital work-in-progress | 5 | 26.02 | 43.57 |
| Other intangible assets | 6a | 25.62 | 36.74 |
| Intangible asset under development | 6b | – | 10.28 |
| Financial assets — i) Investments | 7 | 524.98 | 272.98 |
| Financial assets — ii) Other financial assets | 8 | 727.65 | 2,120.42 |
| Non-current tax assets (net) | 9 | 98.68 | 117.47 |
| Other non-current assets | 10 | 1,732.36 | 1,515.60 |
| **Total non-current assets** | | **14,204.21** | **14,207.21** |
| **Current assets** | | | |
| Inventories | 11 | 26,516.51 | 16,525.47 |
| Financial assets — i) Investments | 12 | 436.14 | 508.35 |
| Financial assets — ii) Trade receivables | 13 | 74.98 | 56.06 |
| Financial assets — iii) Cash and cash equivalents | 14 | 960.81 | 430.57 |
| Financial assets — iv) Bank balances other than (iii) above | 15 | 4,041.46 | 1,341.18 |
| Financial assets — v) Other financial assets | 8 | 3,015.07 | 1,932.73 |
| Other current assets | 10 | 237.91 | 344.60 |
| **Total current assets** | | **35,282.88** | **21,138.96** |
| **Total assets** | | **49,487.09** | **35,346.17** |
| **EQUITY AND LIABILITIES — Equity** | | | |
| Equity share capital *(FY25 figure INCLUDES preference capital — see §9, A-05)* | 16 | 152.23 | 296.56 |
| Share application money pending allotment | | 0.02 | – |
| Other equity | 17 | 18,031.85 | 8,836.88 |
| **Total equity** | | **18,184.10** | **9,133.44** |
| **Non-current liabilities** | | | |
| Financial liabilities — i) Borrowings | 18 | 2,010.58 | 1,972.83 |
| Financial liabilities — ii) Lease liabilities | 19 | 8,010.95 | 7,051.07 |
| Financial liabilities — iii) Other financial liabilities | 20 | 30.82 | 143.31 |
| Provisions | 21 | 50.68 | 35.44 |
| **Total non-current liabilities** | | **10,103.03** | **9,202.65** |
| **Current liabilities** | | | |
| Financial liabilities — i) Borrowings | 18 | 5,432.65 | 5,313.35 |
| Financial liabilities — ii) Gold on loan | 22 | 2,848.14 | 3,865.53 |
| Financial liabilities — iii) Lease liabilities | 19 | 1,307.34 | 943.06 |
| iv) Trade payables — (a) Total outstanding dues of micro enterprises and small enterprises | 23 | 399.25 | 282.97 |
| iv) Trade payables — (b) Total outstanding dues of creditors other than micro enterprises and small enterprises | 23 | 1,160.11 | 1,364.21 |
| Financial liabilities — v) Other financial liabilities | 20 | 2,420.88 | 2,348.79 |
| Provisions | 21 | 36.68 | 28.46 |
| Other current liabilities | 24 | 7,594.91 | 2,863.71 |
| **Total current liabilities** | | **21,199.96** | **17,010.08** |
| **Total liabilities** | | **31,302.99** | **26,212.73** |
| **Total equity and liabilities** | | **49,487.09** | **35,346.17** |

*Tie-outs (code-run, §4a trigger 3): non-current assets ✔; current assets ✔; current liabilities (8 operands) ✔;
total liabilities ✔; 18,184.10 + 31,302.99 = 49,487.09 ✔.*

### 2.2 STANDALONE — AR FY2025 (FY24 comparative is a REPORTED FY24)

**Unit: ₹ million.** Source: `[AR FY25, SA Balance Sheet, p97/pr92, REPORTED]`

| Line, as printed | Note | 31-Mar-2025 | **31-Mar-2024 (REPORTED)** |
|---|---|---|---|
| Property, plant and equipment | 3 | 2,659.82 | 1,238.25 |
| Right-of-use assets | 4 | 7,430.33 | 4,610.36 |
| Capital work-in-progress | 5 | 43.57 | 166.64 |
| Other intangible assets | 6a | 36.74 | 1.91 |
| Intangible asset under development | 6b | 10.28 | – |
| Financial assets — i) Investments | 7 | 272.98 | – |
| Financial assets — ii) Other financial assets | 8 | 2,120.42 | 4,106.05 |
| Non-current tax assets (net) | 9 | 117.47 | 36.33 |
| **Deferred tax assets (net)** *(a line that disappears in AR FY26)* | 10 | – | – |
| Other non-current assets | 11 | 1,515.60 | 1,001.77 |
| **Total non-current assets** | | **14,207.21** | **11,161.31** |
| Inventories | 12 | 16,525.47 | 9,912.21 |
| Financial assets — i) Investments | 13 | 508.35 | – |
| Financial assets — ii) **Loans** | 14 | – | 0.39 |
| Financial assets — iii) Trade receivables | 15 | 56.06 | 23.77 |
| Financial assets — iv) Cash and cash equivalents | 16 | 430.57 | 591.35 |
| Financial assets — v) Bank balances other than (iv) above | 17 | 1,341.18 | 473.61 |
| Financial assets — vi) Other financial assets | 8 | 1,932.73 | 2,193.96 |
| Other current assets | 11 | 344.60 | 178.32 |
| **Total current assets** | | **21,138.96** | **13,373.61** |
| **Total assets** | | **35,346.17** | **24,534.92** |
| Equity share capital | 18 | 296.56 | **278.95** |
| Other equity | 19 | 8,836.88 | 3,462.77 |
| **Total equity** | | **9,133.44** | **3,741.72** |
| Borrowings (non-current) | 20 | 1,972.83 | 1,851.40 |
| Lease liabilities (non-current) | 21 | 7,051.07 | 4,301.18 |
| Other financial liabilities (non-current) | 22 | 143.31 | 325.10 |
| Provisions (non-current) | 23 | 35.44 | 33.93 |
| **Total non-current liabilities** | | **9,202.65** | **6,511.61** |
| Borrowings (current) | 20 | 5,313.35 | 2,452.86 |
| Gold on loan | 24 | 3,865.53 | 4,424.61 |
| Lease liabilities (current) | 21 | 943.06 | 588.06 |
| Trade payables — (a) micro and small enterprises | 25 | 282.97 | 418.55 |
| Trade payables — (b) creditors other than micro and small | 25 | 1,364.21 | 1,748.94 |
| Other financial liabilities (current) | 22 | 2,348.79 | 2,712.60 |
| Provisions (current) | 23 | 28.46 | 20.52 |
| Other current liabilities | 26 | 2,863.71 | 1,915.45 |
| **Total current liabilities** | | **17,010.08** | **14,281.59** |
| **Total liabilities** | | **26,212.73** | **20,793.20** |
| **Total equity and liabilities** | | **35,346.17** | **24,534.92** |

*Every 31-Mar-2025 figure above equals the 31-Mar-2025 comparative column in AR FY2026 (§2.1) line for
line — the two reported presentations of the FY25 balance sheet AGREE. Two presentation lines drop out of
AR FY26 (Deferred tax assets (net), and Loans), both nil at 31-Mar-2025.*

### 2.3 CONSOLIDATED — AR FY2026

**Unit: ₹ million.** Source: `[AR FY26, CFS Balance Sheet, p243/pr264, REPORTED]`

| Line, as printed | Note | 31-Mar-2026 | 31-Mar-2025 |
|---|---|---|---|
| Property, plant and equipment | 3 | 2,662.48 | 2,659.88 |
| Right-of-use assets | 4 | 8,655.21 | 7,432.77 |
| Capital work-in-progress | 5 | 27.49 | 43.57 |
| Other intangible assets | 6a | 25.60 | 36.81 |
| Intangible asset under development | 6b | – | 10.28 |
| **Investment accounted for using the equity method** | 7 | 30.04 | 85.56 |
| Financial assets — i) Other financial assets | 8 | 748.63 | 2,123.00 |
| Non-current tax assets (net) | 9 | 99.00 | 117.47 |
| Other non-current assets | 10 | 1,750.34 | 1,516.02 |
| **Total non-current assets** | | **13,998.79** | **14,025.36** |
| Inventories | 11 | 26,718.09 | 16,525.47 |
| Financial assets — i) Investments | 12 | 436.14 | 508.35 |
| Financial assets — ii) Loans | 13 | 0.02 | – |
| Financial assets — iii) Trade receivables | 14 | 75.43 | 56.06 |
| Financial assets — iv) Cash and cash equivalents | 15 | 1,075.24 | 487.75 |
| Financial assets — v) Bank balances other than (iv) above | 16 | 4,041.48 | 1,381.18 |
| Financial assets — vi) Other financial assets | 8 | 3,015.42 | 1,993.89 |
| Other current assets | 10 | 249.51 | 344.75 |
| **Total current assets** | | **35,611.33** | **21,297.45** |
| **Total assets** | | **49,610.12** | **35,322.81** |
| Equity share capital | 17 | 152.23 | 296.56 |
| Share application money pending allotment | | 0.02 | *(blank)* |
| Other equity | 18 | 17,854.70 | 8,771.18 |
| **Equity attributable to the owners of the parent** | | **18,006.95** | **9,067.74** |
| **Non-Controlling Interest** | 18 | **23.08** | **39.66** |
| **Total Equity** | | **18,030.03** | **9,107.40** |
| Borrowings (non-current) | 19 | 2,010.58 | 1,972.83 |
| Lease liabilities (non-current) | 20 | 8,218.58 | 7,052.70 |
| Other financial liabilities (non-current) | 21 | 30.82 | 143.31 |
| Provisions (non-current) | 22 | 51.75 | 35.44 |
| **Total non-current liabilities** | | **10,311.73** | **9,204.28** |
| Borrowings (current) | 19 | 5,432.65 | 5,313.35 |
| Gold on loan | 23 | 2,848.14 | 3,865.53 |
| Lease liabilities (current) | 20 | 1,329.00 | 943.79 |
| Trade payables — (a) micro and small enterprises | 24 | 399.56 | 282.97 |
| Trade payables — (b) other than micro and small | 24 | 1,204.26 | 1,364.38 |
| Other financial liabilities (current) | 21 | 2,420.88 | 2,348.79 |
| Provisions (current) | 22 | 36.87 | 28.46 |
| Other current liabilities | 25 | 7,597.00 | 2,863.86 |
| **Total current liabilities** | | **21,268.36** | **17,011.13** |
| **Total liabilities** | | **31,580.09** | **26,215.41** |
| **Total equity and liabilities** | | **49,610.12** | **35,322.81** |

### 2.4 CONSOLIDATED — AR FY2025 (FY24 comparative)

**Unit: ₹ million.** Source: `[AR FY25, CFS Balance Sheet, p166/pr161, REPORTED]`

| Line, as printed | Note | 31-Mar-2025 | **31-Mar-2024 (REPORTED)** |
|---|---|---|---|
| Property, plant and equipment | 3 | 2,659.88 | 1,238.25 |
| Right-of-use assets | 4 | 7,432.77 | 4,610.36 |
| Capital work-in-progress | 5 | 43.57 | 166.64 |
| Other intangible assets | 6a | 36.81 | 1.91 |
| Intangible asset under development | 6b | 10.28 | – |
| Investments accounted for using the equity method | 7 | 85.56 | – |
| Other financial assets (non-current) | 8 | 2,123.00 | 4,106.05 |
| Non-current tax assets (net) | 9 | 117.47 | 36.33 |
| Deferred tax assets (net) | 10 | – | – |
| Other non-current assets | 11 | 1,516.02 | 1,001.77 |
| **Total non-current assets** | | **14,025.36** | **11,161.31** |
| Inventories | 12 | 16,525.47 | 9,912.21 |
| Investments (current) | 13 | 508.35 | – |
| Loans | 14 | – | 0.39 |
| Trade receivables | 15 | 56.06 | 23.77 |
| Cash and cash equivalents | 16 | 487.75 | 591.35 |
| Bank balances other than (iv) above | 17 | 1,381.18 | 473.61 |
| Other financial assets (current) | 8 | 1,993.89 | 2,193.96 |
| Other current assets | 11 | 344.75 | 178.32 |
| **Total current assets** | | **21,297.45** | **13,373.61** |
| **Total assets** | | **35,322.81** | **24,534.92** |
| Equity share capital | 18 | 296.56 | 278.95 |
| Other equity | 19 | 8,771.18 | 3,462.77 |
| **Equity attributable to the owners of the parent** | | **9,067.74** | **3,741.72** |
| Non-Controlling Interest | 51 | 39.66 | – |
| **Total equity** | | **9,107.40** | **3,741.72** |
| Borrowings (non-current) | 20 | 1,972.83 | 1,851.40 |
| Lease liabilities (non-current) | 21 | 7,052.70 | 4,301.18 |
| Other financial liabilities (non-current) | 22 | 143.31 | 325.10 |
| Provisions (non-current) | 23 | 35.44 | 33.93 |
| **Total non-current liabilities / Current liabilities** *(the row label is misprinted — see §9, A-15)* | | **9,204.28** | **6,511.61** |
| Borrowings (current) | 20 | 5,313.35 | 2,452.86 |
| Gold on loan | 24 | 3,865.53 | 4,424.61 |
| Lease liabilities (current) | 21 | 943.79 | 588.06 |
| Trade payables — (a) micro and small | 25 | 282.97 | 418.55 |
| Trade payables — (b) other | 25 | 1,364.38 | 1,748.94 |
| Other financial liabilities (current) | 22 | 2,348.79 | 2,712.60 |
| Provisions (current) | 23 | 28.46 | 20.52 |
| Other current liabilities | 26 | 2,863.86 | 1,915.45 |
| **Total current liabilities** | | **17,011.13** | **14,281.59** |
| **Total liabilities** | | **26,215.41** | **20,793.20** |
| **Total equity and liabilities** | | **35,322.81** | **24,534.92** |

---

## 3. CASH FLOW STATEMENT — every line in all three activities, incl. each PAT-to-CFO adjustment separately

### 3.1 STANDALONE — AR FY2026

**Unit: ₹ million.** Indirect method, Ind AS 7. Source: `[AR FY26, SA Statement of Cash Flows, p166/pr187, REPORTED]`

| Line, as printed | FY2026 | FY2025 |
|---|---|---|
| **A. Cash flows from operating activities** | | |
| Profit/(Loss) before tax | 260.00 | (2,192.14) |
| *Adjustments for non cash items and other adjustments:* | | |
| Depreciation and amortisation | 2,081.18 | 1,474.75 |
| **Expense on employee stock option scheme** | **926.51** | **512.39** |
| Finance costs | 2,052.78 | 2,038.10 |
| Interest income | (352.59) | (350.63) |
| Loss on sale of property, plant and equipment (net) | 31.05 | 19.48 |
| Rent waiver on lease liabilities | – | (3.88) |
| Gain on mutual fund | (30.31) | (39.31) |
| Liabilities no longer required written back | (67.12) | (95.16) |
| **Gain on termination of lease** | **(15.75)** | **(10.84)** |
| Fair value loss/(gain) on call option in subsidiary | 33.94 | (52.16) |
| Intangible asset under development written off | 10.28 | – |
| Unwinding of interest on financial assets carried at amortised cost | (34.77) | (28.22) |
| **Operating profit before working capital changes** | **4,895.20** | **1,272.38** |
| *Working capital adjustments:* | | |
| (Increase)/Decrease in other financial assets | (287.62) | 218.19 |
| Increase in other assets | (113.04) | (722.78) |
| **Increase in inventories** | **(9,991.04)** | **(6,613.26)** |
| Decrease in loans | – | 0.39 |
| Increase in trade receivables | (18.92) | (32.29) |
| Decrease in other financial liabilities | (41.39) | (547.42) |
| Increase in provisions | 23.23 | 1.35 |
| Decrease in gold on loan | (1,017.39) | (559.08) |
| Decrease in trade payables | (20.70) | (425.15) |
| **Increase in other current liabilities** | **4,817.74** | **840.40** |
| **Cash used in operations** | **(1,753.93)** | **(6,567.27)** |
| Income tax paid (net) | 18.79 | (81.14) |
| **Net cash used in operating activities (A)** | **(1,735.14)** | **(6,648.41)** |
| **B. Cash flows from investing activities** | | |
| Acquisition of property, plant and equipment (including capital work-in-progress and capital advances) | (957.78) | (1,630.82) |
| Proceeds from sale of property, plant and equipment | 221.92 | 7.80 |
| Acquisition of intangible assets | (3.33) | (38.96) |
| Payment for acquisition of subsidiary | (252.00) | (167.98) |
| Payment for acquisition of associate | – | (105.00) |
| Investment in fixed deposits | (17,054.73) | (6,016.55) |
| Redemption of fixed deposits | 14,888.50 | 7,141.32 |
| Investment in mutual funds | (1,104.50) | (3,395.00) |
| Redemption of mutual funds | 1,207.02 | 2,925.96 |
| Interest received on fixed deposits | 334.37 | 369.70 |
| **Net cash used in investing activities (B)** | **(2,720.53)** | **(909.53)** |
| **C. Cash flows from financing activities** | | |
| Proceeds from issue of equity shares (net of IPO expenses) | 7,864.37 | 1,092.97 |
| Share application money pending allotment | 0.02 | – |
| Proceeds from issue of preference shares | – | 5,978.39 |
| Proceeds from borrowings (Refer note b (i) below) | 20,719.58 | 8,254.26 |
| Repayment of borrowings (Refer note b (i) below) | (20,562.53) | (5,272.34) |
| Interest paid (Refer note b(i) below) | (1,417.28) | (1,526.95) |
| **Repayment of lease liabilities including interest (Refer note b(ii) below)** | **(1,618.25)** | **(1,129.17)** |
| **Net cash generated from financing activities (C)** | **4,985.91** | **7,397.16** |
| **Net (decrease)/increase in cash and cash equivalents (A+B+C)** | **530.24** | **(160.78)** |
| Cash and cash equivalents at the beginning of the year | 430.57 | 591.35 |
| **Cash and cash equivalents at the end of the year (Note no. 14)** | **960.81** | **430.57** |

*Tie-outs (code-run, §4a triggers 1 and 3): operating profit before WC changes (13 operands) ✔;
cash used in operations (11 operands) ✔; investing (10 operands) ✔; financing (7 operands) ✔;
(1,735.14) + (2,720.53) + 4,985.91 = 530.24 ✔; 430.57 + 530.24 = 960.81 ✔ closing reconciliation.*

**Reconciliation of movements in liabilities arising from financing activities**
`[AR FY26, SA Cash Flows note (b), p167/pr188]`

| Particulars | 01-Apr-2024 | Non-cash: Fair value changes/Adjustments | Non-cash: Finance cost accrued during the year | Non-cash: Additions (Net) | Cash flows | 31-Mar-2025 |
|---|---|---|---|---|---|---|
| i) Borrowings (including interest) | 4,297.27 | **6.99** | 1,526.95 | – | 1,454.97 | **7,286.19** |
| ii) Lease liabilities | 4,889.24 | (3.88) | 509.33 | 3,728.61 | (1,129.17) | 7,994.13 |

| Particulars | 01-Apr-2025 | Fair value changes/Adjustments | Finance cost accrued | Additions (Net) | Cash flows | 31-Mar-2026 |
|---|---|---|---|---|---|---|
| i) Borrowings (including interest) | 7,286.19 | – | 1,417.28 | – | (1,260.23) | 7,443.23 |
| ii) Lease liabilities | 7,994.13 | – | 634.50 | 2,307.91 | (1,618.25) | 9,318.29 |

*The 31-Mar-2025 borrowings closing of 7,286.19 here DISAGREES with 7,286.18 in AR FY25 and in AR FY26
Note 18 — see §9, A-06.*

### 3.2 STANDALONE — AR FY2025 (FY24 comparative)

**Unit: ₹ million.** Source: `[AR FY25, SA Statement of Cash Flows, p101/pr96, REPORTED]`

| Line, as printed | FY2025 | **FY2024 (REPORTED)** |
|---|---|---|
| Loss before tax | (2,192.14) | (1,422.36) |
| Depreciation and amortisation | 1,474.75 | 952.66 |
| Expense on employee stock option scheme | 512.39 | **292.58** |
| Finance costs | 2,038.10 | 1,366.03 |
| Interest income | (350.63) | (250.58) |
| Loss/(Profit) on sale of property, plant and equipment (net) | 19.48 | (19.43) |
| **Bad debts written off** | – | 2.75 |
| **Provision for doubtful debt and other receivables** | – | 1.20 |
| Rent waiver on lease liabilities | (3.88) | – |
| Gain on mutual fund | (39.31) | – |
| Liabilities no longer required written back | (95.16) | (96.71) |
| Gain on termination of lease | (10.84) | (7.96) |
| Fair value gain on call option in subsidiary | (52.16) | *(blank)* |
| Unwinding of interest on financial assets carried at amortised cost | (28.22) | – |
| **Operating profit before working capital changes** | **1,272.38** | **818.18** |
| Decrease/(Increase) in other financial assets | 218.19 | (520.42) |
| Increase in other assets | (722.78) | (319.12) |
| Increase in inventories | (6,613.26) | (5,959.04) |
| Decrease in loans | 0.39 | 11.68 |
| Increase in trade receivables | (32.29) | (17.07) |
| Decrease in other financial liabilities | (547.42) | (320.50) |
| Increase in provisions | 1.35 | 15.21 |
| (Decrease)/Increase in gold on loan | (559.08) | 2,212.19 |
| (Decrease)/Increase in trade payables | (425.15) | 1,480.43 |
| Increase in other current liabilities | 840.40 | 810.43 |
| **Cash used in operations** | **(6,567.27)** | **(1,788.03)** |
| Income tax paid (net) | (81.14) | (23.61) |
| **Net cash used in operating activities (A)** | **(6,648.41)** | **(1,811.64)** |
| Acquisition of PPE (incl. CWIP and capital advances) | (1,630.82) | (988.00) |
| Proceeds from sale of PPE | 7.80 | 172.34 |
| Acquisition of intangible assets | (38.96) | (1.08) |
| Payment for acquisition of subsidiary | (167.98) | – |
| Payment for acquisition of associate | (105.00) | – |
| Investment in fixed deposits | (6,016.55) | – |
| **Redemption of fixed deposits** | 7,141.32 | **(3,276.26)** ← printed as a negative under a "Redemption" caption; see §9, A-11 |
| Investment in mutual funds | (3,395.00) | – |
| Redemption of mutual funds | 2,925.96 | – |
| Interest received on fixed deposits | 369.70 | 276.52 |
| **Net cash used in investing activities (B)** | **(909.53)** | **(3,816.48)** |
| Proceeds from issue of equity shares | 1,092.97 | – |
| Proceeds from issue of preference shares | 5,978.39 | 5,877.53 |
| Proceeds from borrowings | 8,254.26 | 4,393.28 |
| Repayment of borrowings | (5,272.34) | (2,373.20) |
| Interest paid | (1,526.95) | (1,056.65) |
| **Settlement of cash settled ESOP liability** | – | **(117.96)** |
| Repayment of lease liabilities (Refer note b(iii) below) | (1,129.17) | (774.53) |
| **Net cash generated from financing activities (C)** | **7,397.16** | **5,948.47** |
| **Net (decrease)/increase in cash and cash equivalents** | **(160.78)** | **320.35** |
| Cash and cash equivalents at the beginning of the year | 591.35 | 271.00 |
| **Cash and cash equivalents at the end of the year (Note no. 16)** | **430.57** | **591.35** |

**Financing-liability reconciliation, AR FY2025** `[AR FY25, SA Cash Flows note (b), p102/pr97]`

| Particulars | 01-Apr-2023 | FV changes/Adj | Finance cost accrued | Additions (Net) | Cash flows | 31-Mar-2024 |
|---|---|---|---|---|---|---|
| i) Borrowings (including interest) | 2,277.20 | – | 1,056.65 | – | 963.43 | 4,297.27 |
| ii) Lease liabilities | 3,729.31 | – | 305.30 | 1,629.16 | (774.53) | 4,889.24 |
| iii) Issue of Preference shares | – | – | – | – | 5,877.53 | – |
| iv) Issue of Equity shares | – | – | – | – | – | – |

| Particulars | 01-Apr-2024 | FV changes/Adj | Finance cost accrued | Additions (Net) | Cash flows | 31-Mar-2025 |
|---|---|---|---|---|---|---|
| i) Borrowings (including interest) | 4,297.27 | **6.99** | 1,526.95 | – | 1,454.97 | **7,286.18** |
| ii) Lease liabilities | 4,889.24 | (3.88) | 509.33 | 3,728.61 | (1,129.17) | 7,994.13 |
| iii) Issue of Preference shares | – | – | – | *(blank)* | 5,978.39 | – |
| iv) **Issue of Equity shares** | – | **6.99** | – | – | 1,092.97 | – |

*The 6.99 appears TWICE in the FY25 table — once against Borrowings and once against Issue of Equity
shares. It is the OCRPS Series-E1 liability component reclassified to equity `[AR FY25, SA Note 20,
p131/pr126]`. Recorded as printed; no netting applied here.*

### 3.3 CONSOLIDATED — AR FY2026

**Unit: ₹ million.** Source: `[AR FY26, CFS Statement of Cash Flows, p245/pr266, REPORTED]`
**The page is MIS-TITLED "Standalone Statement of Cash Flows" although it sits inside the consolidated
financial statements and carries consolidated figures — see §9, A-14.**

| Line, as printed | FY2026 | FY2025 |
|---|---|---|
| Profit/(Loss) before tax | 131.79 | (2,218.37) |
| Depreciation and amortisation | 2,099.27 | 1,474.89 |
| Expense on employee stock option scheme | 926.67 | 512.39 |
| Finance costs | 2,061.71 | 2,038.13 |
| **Share of loss of Associate** | 55.52 | 19.44 |
| Interest income | (356.23) | (351.78) |
| Loss on sale of property, plant and equipment (net) | 31.05 | 19.48 |
| Rent waiver on lease liabilities | – | (3.88) |
| Gain on mutual fund | (30.31) | (39.31) |
| Liabilities no longer required written back | (67.12) | (95.16) |
| Gain on termination of lease | (15.73) | (10.84) |
| Fair value loss/(gain) on call option – subsidiary | 33.94 | (52.16) |
| Intangible asset under development written off | 10.28 | *(blank)* |
| Unwinding of interest on financial assets carried at amortised cost | (35.10) | (28.23) |
| **Operating profit before working capital changes** | **4,845.74** | **1,264.60** |
| (Increase)/Decrease in other financial assets | (311.72) | 216.35 |
| Increase in other assets | (139.92) | (723.34) |
| Increase in inventories | (10,192.62) | (6,613.26) |
| (Increase)/Decrease in loans | (0.02) | 0.39 |
| Increase in trade receivables | (19.37) | (32.29) |
| Decrease in other financial liabilities | (41.39) | (547.42) |
| Increase in provisions | 24.49 | 1.35 |
| Decrease in gold on loan | (1,017.39) | (559.08) |
| Increase/(Decrease) in trade payables | 23.59 | (424.98) |
| Increase in other current liabilities | 4,819.22 | 840.55 |
| **Cash used in operations** | **(2,009.39)** | **(6,577.13)** |
| Income tax paid (net) | 18.47 | (81.14) |
| **Net cash used in operating activities (A)** | **(1,990.92)** | **(6,658.28)** |
| Acquisition of PPE (incl. CWIP and capital advances) | (986.62) | (1,630.88) |
| Proceeds from sale of PPE | 221.92 | 7.80 |
| Acquisition of intangible assets | (3.33) | (39.03) |
| Payment for acquisition of associate | – | (105.00) |
| Investment in fixed deposits | (17,054.73) | (6,117.20) |
| Redemption of fixed deposits | 14,988.48 | 7,141.32 |
| Investment in mutual funds | (1,104.50) | (3,395.00) |
| Redemption of mutual funds | 1,207.02 | 2,925.96 |
| Interest received on fixed deposits | 338.82 | 369.70 |
| **Net cash used in investing activities (B)** | **(2,392.94)** | **(842.33)** |
| Proceeds from issue of equity shares (net of IPO expenses) | 7,864.37 | 1,092.97 |
| Share application money pending allotment | 0.02 | – |
| Proceeds from issue of preference shares | – | 5,978.39 |
| Proceeds from borrowings | 20,719.58 | 8,254.26 |
| Repayment of borrowings | (20,562.53) | (5,272.34) |
| Interest paid | (1,417.28) | (1,526.95) |
| Repayment of lease liabilities | (1,632.81) | (1,129.32) |
| **Net cash generated from financing activities (C)** | **4,971.35** | **7,397.01** |
| **Net (decrease)/increase in cash and cash equivalents** | **587.49** | **(103.60)** |
| Cash and cash equivalents at the beginning of the year | 487.75 | 591.35 |
| **Cash and cash equivalents at the end of the year (Note no. 16)** | **1,075.24** | **487.75** |

*Tie-outs (code-run): operating profit before WC changes (14 operands) ✔; investing ✔; financing ✔.*

**Financing-liability reconciliation, consolidated** `[AR FY26, CFS Cash Flows note (b), p246/pr267]`

| Particulars | 01-Apr-2024 | FV changes/Adj | Finance cost accrued | Additions (Net) | Cash flows | 31-Mar-2025 |
|---|---|---|---|---|---|---|
| i) Borrowings (including interest) | 4,297.27 | 6.99 | 1,526.95 | – | 1,454.97 | **7,286.18** |
| ii) Lease liabilities | 4,889.24 | (3.88) | 509.36 | 3,731.09 | (1,129.32) | 7,996.49 |

| Particulars | 01-Apr-2025 | FV changes/Adj | Finance cost accrued | Additions (Net) | Cash flows | 31-Mar-2026 |
|---|---|---|---|---|---|---|
| i) Borrowings (including interest) | 7,286.18 | – | 1,417.28 | – | (1,260.22) | 7,443.23 |
| ii) Lease liabilities | 7,996.49 | – | 643.43 | 2,540.47 | (1,632.81) | 9,547.58 |

### 3.4 CONSOLIDATED — AR FY2025 (FY24 comparative)

**Unit: ₹ million.** Source: `[AR FY25, CFS Statement of Cash Flows, p170/pr165, REPORTED]`

| Line, as printed | FY2025 | **FY2024 (REPORTED)** |
|---|---|---|
| Loss before tax | (2,218.37) | (1,422.36) |
| Depreciation and amortisation | 1,474.89 | 952.66 |
| Expense on employee stock option scheme | 512.39 | 292.58 |
| Finance costs | 2,038.13 | 1,366.03 |
| Share of loss of Associate | 19.44 | – |
| Interest income | (351.78) | (250.58) |
| (Profit)/Loss on sale of PPE (net) | 19.48 | (19.43) |
| Rent waiver on lease liabilities | (3.88) | – |
| (Gain) on mutual fund | (39.31) | – |
| Liabilities no longer required written back | (95.16) | (96.71) |
| Gain on termination of lease | (10.84) | (7.96) |
| Fair value gain on call option – subsidiary | (52.16) | – |
| Unwinding of interest on financial assets carried at amortised cost | (28.23) | – |
| **Operating profit before working capital changes** | **1,264.60** | **818.18** |
| Decrease/(Increase) in other financial assets | 216.35 | (520.42) |
| Increase in other assets | (723.34) | (319.12) |
| Increase in inventories | (6,613.26) | (5,959.04) |
| Decrease in loans | 0.39 | 11.68 |
| Increase in trade receivables | (32.29) | (17.07) |
| Decrease in other financial liabilities | (547.42) | (320.50) |
| Increase in provisions | 1.35 | 15.21 |
| (Decrease)/Increase in gold on loan | (559.08) | 2,212.19 |
| (Decrease)/Increase in trade payables | (424.98) | 1,480.43 |
| Increase in other current liabilities | 840.55 | 810.43 |
| **Cash used in operations** | **(6,577.13)** | **(1,788.03)** |
| Income tax paid (net) | (81.14) | (23.61) |
| **Net cash used in operating activities (A)** | **(6,658.28)** | **(1,811.64)** |
| Acquisition of PPE (incl. CWIP and capital advances) | (1,630.88) | **(989.08)** |
| Proceeds from sale of PPE | 7.80 | 172.34 |
| Acquisition of intangible assets | (39.03) | **–** |
| Payment for acquisition of associate | (105.00) | – |
| Investment in fixed deposits | (6,117.20) | – |
| Redemption of fixed deposits | 7,141.32 | **(3,276.26)** |
| Investment in mutual funds | (3,395.00) | – |
| Redemption of mutual funds | 2,925.96 | – |
| Interest received on fixed deposits | 369.70 | 276.52 |
| **Net cash used in investing activities (B)** | **(842.33)** | **(3,816.48)** |
| Proceeds from issue of equity shares | 1,092.97 | – |
| Proceeds from issue of preference shares | 5,978.39 | 5,877.53 |
| Proceeds from borrowings | 8,254.26 | 4,393.28 |
| Repayment of borrowings | (5,272.34) | (2,373.20) |
| Interest paid | (1,526.95) | (1,056.65) |
| Settlement of cash settled ESOP liability | – | (117.96) |
| Repayment of lease liabilities | (1,129.32) | (774.53) |
| **Net cash generated from financing activities (C)** | **7,397.01** | **5,948.47** |
| **Net (decrease)/increase in cash** | **(103.60)** | **320.35** |
| Opening cash and cash equivalents | 591.35 | 271.00 |
| **Closing cash and cash equivalents (Note no. 16)** | **487.75** | **591.35** |

**Financing-liability reconciliation, consolidated, AR FY2025** `[AR FY25, CFS Cash Flows note (b), p171/pr166]`
adds two rows absent from the standalone table: *"ii) Preference shares classified as financial liability"*
(nil in every column, both years) and *"v) Issue of Equity shares"* (cash flows 1,092.97 in FY25, nil in FY24
— note the FV-changes column here is **nil**, whereas the standalone FY25 table puts **6.99** in that cell:
see §9, A-16).

---

## 4. STATEMENT OF CHANGES IN EQUITY — share capital and each reserve column, with movement lines

### 4.1 STANDALONE — AR FY2026, Part A: EQUITY SHARE CAPITAL

**Unit: ₹ million; share counts in absolute numbers.** `[AR FY26, SA SOCIE, p168/pr189]`

**Equity shares of INR 1 each, fully paid up**

| Movement line | Note | Number | Amount |
|---|---|---|---|
| As at 01 April 2024 | | 1,81,51,940 | 18.16 |
| Changes in equity share capital during the year | 16 | 1,70,83,060 | 17.08 |
| **As at 31 March 2025** | | **3,52,35,000** | **35.24** |
| Changes in equity share capital during the year | 16 | 11,69,96,365 | 117.00 |
| **As at 31 March 2026** | | **15,22,31,365** | **152.23** |

**Preference shares of INR 10 each, fully paid up**

| Movement line | Note | Number | Amount |
|---|---|---|---|
| As at 01 April 2024 | | 2,60,79,102 | 260.78 |
| Changes during the year | 16 | (9,84,790) | (9.84) |
| **As at 31 March 2025** | | **2,50,94,312** | **250.94** |
| Changes during the year | 16 | (2,50,94,312) | (250.94) |
| **As at 31 March 2026** | | **–** | **–** |

**Preference shares of INR 1 each, fully paid up**

| Movement line | Note | Number | Amount |
|---|---|---|---|
| As at 01 April 2024 | | – | – |
| Changes during the year | 16 | 1,03,80,622 | 10.38 |
| **As at 31 March 2025** | | **1,03,80,622** | **10.38** |
| Changes during the year | 16 | (1,03,80,622) | (10.38) |
| **As at 31 March 2026** | | **–** | **–** |

| **Total Share capital as at 31 March 2025** | **7,07,09,934.00** | **296.56** |
|---|---|---|
| **Total Share capital as at 31 March 2026** | **15,22,31,365.00** | **152.23** |

*The 7,07,09,934 total here DISAGREES with 7,07,09,930 in Note 16 III — see §9, A-04.*

### 4.2 STANDALONE — AR FY2026, Part B: OTHER EQUITY

**Unit: ₹ million.** `[AR FY26, SA SOCIE Part B, p169/pr190]`
Column headings as printed: *Reserves and surplus → Securities Premium · Retained earnings · Share options
outstanding account*; *Other comprehensive income → Re-measurement of (gain)/loss*; *Total*.

| Movement line | Securities Premium | Retained earnings | Share options outstanding account | Re-measurement of (gain)/loss | Total |
|---|---|---|---|---|---|
| **As at 31 March 2024** | 25,221.43 | (22,325.48) | 553.00 | 13.82 | **3,462.77** |
| Loss for the year | – | (2,192.14) | – | – | (2,192.14) |
| Other comprehensive income (net of tax) | – | – | – | (8.10) | (8.10) |
| Premium received on issue of shares (net of expenses) | 7,214.09 | – | – | – | 7,214.09 |
| Options granted during the year (net of exercised) | – | – | 344.48 | – | 344.48 |
| Conversion of compulsorily convertible preference shares to Equity (Refer note 16c) | 8.86 | – | – | – | 8.86 |
| Conversion of optionally convertible redeemable preference shares to equity (Refer note 16c) | 6.92 | – | – | – | 6.92 |
| *(sub-total of the year's movements)* | 7,229.87 | (2,192.14) | 344.48 | (8.10) | 5,374.11 |
| **As at 31 March 2025** | **32,451.30** | **(24,517.62)** | **897.48** | **5.72** | **8,836.88** |
| Profit for the year | – | 260.00 | – | – | 260.00 |
| Other comprehensive income (net of tax) | – | – | – | (0.23) | (0.23) |
| Premium received on issue of shares (net of expenses) | 8,027.22 | – | – | – | 8,027.22 |
| Options granted during the year (net of exercised) | – | – | 746.88 | – | 746.88 |
| Conversion of compulsorily convertible preference shares to Equity (Refer note 16c) | 161.10 | – | – | – | 161.10 |
| *(sub-total of the year's movements)* | 8,188.32 | 260.00 | 746.88 | (0.23) | 9,194.97 |
| **As at 31 March 2026** | **40,639.62** | **(24,257.62)** | **1,644.36** | **5.49** | **18,031.85** |

### 4.3 STANDALONE — AR FY2025 SOCIE (adds the 1-Apr-2023 opening and the FY24 year)

**Unit: ₹ million.** `[AR FY25, SA SOCIE, p99–100/pr94–95]`

**Part A — share counts, adding the 31-Mar-2023 opening not shown in AR FY26:**

| Class | 31-Mar-2023 | change FY24 | 31-Mar-2024 | change FY25 | 31-Mar-2025 |
|---|---|---|---|---|---|
| Equity shares of ₹1 each — Number | 18,151,940 | – | 18,151,940 | 17,083,060 | 35,235,000 |
| Equity shares of ₹1 each — Amount | 18.16 | – | 18.16 | 17.08 | 35.24 |
| Preference shares of ₹10 each — Number | 7,413,747 | 18,665,355 | 26,079,102 | (984,790) | 25,094,312 |
| Preference shares of ₹10 each — Amount | 74.13 | 186.65 | 260.78 | (9.84) | 250.94 |
| Preference shares of ₹1 each — Number | – | – | – | 10,380,622 | 10,380,622 |
| Preference shares of ₹1 each — Amount | – | – | – | 10.38 | 10.38 |
| **Total Share capital as at 31 March 2025** | | | | | **70,709,934.00 / 296.56** |

**Part B — other equity, FY24 year (the only place the 1-Apr-2023 opening appears in a reported statement):**

| Movement line | Securities premium | Retained earnings | Share options outstanding account | Re-measurement of (gain)/loss | Total other equity |
|---|---|---|---|---|---|
| **As at 1 April 2023** | **19,530.55** | **(20,748.50)** | **403.35** | **4.05** | **(810.55)** |
| Loss for the year | – | (1,422.36) | – | – | (1,422.36) |
| Other comprehensive income (net of tax) | – | – | – | 9.77 | 9.77 |
| Premium received on issue of shares | 5,690.88 | – | – | – | 5,690.88 |
| Options granted during the year (net) | – | – | 149.65 | – | 149.65 |
| **Change in fair value of Equity on termination of Right to subscribe shares (Refer note 48)** | – | **(154.62)** | – | – | **(154.62)** |
| *(sub-total)* | 5,690.88 | (1,576.98) | 149.65 | 9.77 | 4,273.32 |
| **As at 31 March 2024** | **25,221.43** | **(22,325.48)** | **553.00** | **13.82** | **3,462.77** |
| *(FY25 movements identical to §4.2 above)* | 7,229.87 | (2,192.14) | 344.48 | (8.10) | 5,374.11 |
| **As at 31 March 2025** | **32,451.30** | **(24,517.62)** | **897.48** | **5.72** | **8,836.88** |

### 4.4 CONSOLIDATED — AR FY2026 SOCIE

**Unit: ₹ million.** `[AR FY26, CFS SOCIE, p247–248/pr268–269]`
Part A share-capital tables are **identical to the standalone** (§4.1), note reference 17 instead of 16;
"Total Share capital as at 31 March 2026" is printed as `15,22,31,365 / 152.23`.

**Part B — OTHER EQUITY (adds NCI column):**

| Movement line | Securities Premium | Retained earnings | Share options outstanding account | Re-measurement of (gain)/loss | Total other equity | Non-controlling interest | Total |
|---|---|---|---|---|---|---|---|
| **As at 01 April 2024** | 25,221.43 | (22,325.48) | 553.00 | 13.82 | 3,462.77 | – | 3,462.77 |
| Loss for the year | – | (2,216.69) | – | – | (2,216.69) | (1.68) | (2,218.37) |
| Other comprehensive income (net of tax) | – | – | – | (8.10) | (8.10) | – | (8.10) |
| **Adjustments for changes in ownership interests** | – | **(41.14)** | – | – | (41.14) | **41.34** | **0.20** |
| Premium received on issue of shares (net of expenses) | 7,214.08 | – | – | – | 7,214.08 | – | 7,214.08 |
| Options granted during the year (net of exercised) | – | – | 344.48 | – | 344.48 | – | 344.48 |
| Conversion of CCPS to Equity (Refer note 17c) | 8.86 | – | – | – | 8.86 | – | 8.86 |
| Conversion of OCRPS to equity (Refer note 17c) | 6.92 | – | – | – | 6.92 | – | 6.92 |
| *(sub-total)* | 7,229.86 | (2,257.83) | 344.48 | (8.10) | 5,308.41 | 39.66 | 5,348.07 |
| **As at 31 March 2025** | **32,451.29** | **(24,583.31)** | **897.48** | **5.72** | **8,771.18** | **39.66** | **8,810.84** |
| Profit for the year | – | 148.37 | – | – | 148.37 | (16.58) | 131.79 |
| Other comprehensive income (net of tax) | – | – | – | (0.23) | (0.23) | – | (0.23) |
| Premium received on issue of shares (net of expenses) | 8,027.23 | – | – | – | 8,027.23 | – | 8,027.23 |
| Options granted during the year (net of exercised) | – | – | 747.05 | – | 747.05 | – | 747.05 |
| Conversion of CCPS to Equity (Refer note 17c) | 161.10 | – | – | – | 161.10 | – | 161.10 |
| *(sub-total)* | 8,188.33 | 148.37 | 747.05 | (0.23) | 9,083.52 | (16.58) | 9,066.94 |
| **As at 31 March 2026** | **40,639.62** | **(24,434.94)** | **1,644.53** | **5.49** | **17,854.70** | **23.08** | **17,877.78** |

*Consolidated securities premium (32,451.29 / 8,027.23) and share-options reserve (1,644.53 / 747.05)
differ from standalone by ₹0.01–0.17 mn — see §9, A-07.*

### 4.5 CONSOLIDATED — AR FY2025 SOCIE

`[AR FY25, CFS SOCIE, p168–169/pr163–164]`. Part A identical to standalone §4.3. Part B adds the
**1 April 2023** opening with an NCI column of nil throughout FY24:

| Movement line | Securities premium | Retained earnings | Share options outstanding account | Re-measurement | Total other equity | NCI | Total |
|---|---|---|---|---|---|---|---|
| **As at 1 April 2023** | 19,530.55 | (20,748.50) | **403.34** | 4.05 | (810.55) | – | (810.55) |
| Loss for the year | – | (1,422.36) | – | – | (1,422.36) | – | (1,422.36) |
| OCI (net of tax) | – | – | – | 9.77 | 9.77 | – | 9.77 |
| Premium received on issue of shares | 5,690.88 | – | – | – | 5,690.88 | – | 5,690.88 |
| Options granted during the year (net) | – | – | 149.65 | – | 149.65 | – | 149.65 |
| Change in FV of Equity on termination of Right to subscribe shares (note 48) | – | (154.62) | – | – | (154.62) | – | (154.62) |
| *(sub-total)* | 5,690.88 | (1,576.98) | 149.65 | 9.77 | 4,273.32 | – | 4,273.32 |
| **As at 31 March 2024** | 25,221.43 | (22,325.48) | 553.00 | 13.82 | 3,462.77 | – | 3,462.77 |
| *(FY25 movements as §4.4)* | 7,229.86 | (2,257.83) | 344.48 | (8.10) | 5,308.41 | 39.66 | 5,348.07 |
| **As at 31 March 2025** | 32,451.29 | (24,583.31) | 897.48 | 5.72 | 8,771.18 | 39.66 | 8,810.84 |

*The 1-Apr-2023 share-options reserve is **403.34** consolidated vs **403.35** standalone — §9, A-07.*

---

## 5. THE NOTES THAT CARRY A BREAK-UP — one table each

**Unit for the whole of §5: ₹ million**, unless a row says otherwise. Share counts and option counts are in
absolute numbers.

### 5.1 Revenue disaggregation

**SA `[AR FY26, SA Note 25, p206–207/pr227–228]` · CFS `[AR FY26, CFS Note 26, p287–288/pr308–309]` ·
SA FY25 `[AR FY25, SA Note 27, p138/pr133]` · CFS FY25 `[AR FY25, CFS Note 27, p208/pr203]`**

| Line, as printed | SA FY26 | SA FY25 | CFS FY26 | CFS FY25 | SA FY24 (AR FY25) |
|---|---|---|---|---|---|
| Sale of products | 24,412.30 | 17,700.02 | 24,364.24 | 17,700.02 | 12,658.39 |
| **Total revenue from operations** | **24,412.30** | **17,700.02** | **24,364.24** | **17,700.02** | **12,658.39** |
| *(A) Ind AS 115 — Revenue from contract with customers: Sale of products* | 24,412.30 | 17,700.02 | 24,364.24 | 17,700.02 | 12,658.39 |
| **India** | 24,412.30 | 17,700.02 | 24,364.24 | 17,700.02 | 12,658.39 |
| **Outside India** | – | – | – | – | – |
| **At a point in time** | 24,412.30 | 17,700.02 | 24,364.24 | 17,700.02 | 12,658.39 |
| **Over a period of time** | – | – | – | – | – |

**(B) Reconciliation of revenue recognised with the contracted price** — the gross deduction:

| Line | SA FY26 | SA FY25 | CFS FY26 | CFS FY25 | SA FY24 |
|---|---|---|---|---|---|
| **Contracted price** | **32,339.63** | **25,122.22** | **32,228.41** | **25,122.22** | **17,411.81** |
| Less: Reductions towards variable consideration components | (7,927.33) | (7,422.20) | (7,864.17) | (7,422.20) | (4,753.42) |
| **Net consideration recognised as revenue** | **24,412.30** | **17,700.02** | **24,364.24** | **17,700.02** | **12,658.39** |

Verbatim: *"The reduction towards variable consideration comprises of scheme discounts, incentives, returns
etc."* `[AR FY26, SA Note 25(B), p207/pr228]`

**(C) Contract balances**

| Line | SA 31-Mar-26 | SA 31-Mar-25 | CFS 31-Mar-26 | 31-Mar-24 (AR FY25) |
|---|---|---|---|---|
| Contract assets — Right to recover returned goods | 66.56 | 67.67 | 66.56 | 38.76 |
| Contract liabilities — Refund liability *(FY25 label: "Liability for sales return")* | 108.86 | 105.73 | 108.86 | 66.20 |
| Contract liabilities — Gift voucher | 603.91 | 517.49 | 603.91 | 384.83 |
| Contract liabilities — Gold schemes *(FY25 label: "Gold mine scheme")* | 1,900.97 | 1,727.97 | 1,900.97 | 1,087.74 |
| Contract liabilities — Advance from customers | 616.94 | 272.85 | **617.31** | 99.72 |

**(D)** Verbatim: *"No single customer contributed 10% or more to the Company's revenue for the year ended
31 March 2026 and 31 March 2025."* `[AR FY26, SA Note 25(D), p207/pr228]` (CFS: *"…to the Group's revenue…"*).

> **NOT DISCLOSED — revenue by product, channel, store format, category, own-store vs franchise vs online,
> or by state.** The only disaggregation published is geography (India / Outside India) and timing (point in
> time / over time). → would be answered by the **RHP/Prospectus "Our Business — operational KPIs"** section
> and by the **investor presentations**; neither is a statutory account and neither can carry an L1.
> **CFS Note 26(C) advance from customers 617.31 vs CFS Note 25 balance-sheet line 616.94 — see §9, A-08.**

### 5.2 Other income

**SA `[AR FY26, SA Note 26, p208/pr229]` · CFS `[AR FY26, CFS Note 27, p288/pr309]` ·
SA FY25 `[AR FY25, SA Note 28, p139/pr134]` · CFS FY25 `[AR FY25, CFS Note 28, p209/pr204]`**

| Line, as printed | SA FY26 | SA FY25 | CFS FY26 | CFS FY25 | SA FY24 (AR FY25) |
|---|---|---|---|---|---|
| Interest on fixed deposits and others | 352.59 | 350.63 | 356.23 | 351.78 | 250.58 |
| Profit on sale of property plant and equipment (net) | — | — | — | — | 19.43 |
| Gain on mutual fund | 30.31 | 39.31 | 30.31 | 39.31 | – |
| Liabilities no longer required written back | **67.11** | 95.16 | 67.11 | 95.16 | 96.71 |
| Fair value (loss)/gain on call option in subsidiary | **(33.94)** | 52.16 | (33.94) | 52.16 | – |
| Unwinding of interest on financial assets carried at amortized cost | 34.77 | 28.22 | 35.10 | 28.23 | – |
| Gain on termination of lease | **17.74** | 10.84 | **17.62** | 10.84 | 7.96 |
| Rent waiver on lease liabilities | – | 3.88 | – | 3.88 | – |
| Miscellaneous income | 23.33 | 18.98 | 23.33 | 18.98 | 1.84 |
| **Total** | **491.81** | **599.18** | **495.76** | **600.34** | **376.52** |

> **CONFIRMED ARITHMETIC BREAK (code-run, §4a trigger 3).** SA FY26 components sum to **491.91**;
> printed total **491.81**; **residual (0.10) unnamed**. FY25 SA (599.18), CFS FY26 (495.76) and CFS FY25
> (600.34) all tie exactly. See §9, A-02.

### 5.3 Cost of materials consumed / purchases of stock in trade / changes in inventories

**Cost of materials consumed** — SA `[AR FY26, SA Note 27, p208/pr229]`, label in AR FY25 is
**"Cost of raw materials consumed"** `[AR FY25, SA Note 29, p139/pr134]`.

| Line, as printed | SA FY26 | SA FY25 | CFS FY26 | CFS FY25 | SA FY24 |
|---|---|---|---|---|---|
| Inventory at the beginning of the year | 2,291.68 | 1,992.69 | 2,291.68 | 1,992.69 | 837.54 |
| **Add: Purchases** | **23,981.75** | **17,514.34** | **23,982.30** | **17,514.34** | **13,501.86** |
| Less: Inventory at the end of the year | 4,230.53 | 2,291.68 | 4,230.53 | 2,291.68 | 1,992.69 |
| **Total cost of material consumed** | **22,042.90** | **17,215.35** | **22,043.45** | **17,215.35** | **12,346.71** |

**Purchases of stock-in-trade** — a **consolidated-only** note, new in FY26. `[AR FY26, CFS Note 29, p289/pr310]`

| Line | CFS FY26 | CFS FY25 |
|---|---|---|
| Purchases | 127.52 | – |
| **Total** | **127.52** | **–** |

**Change in inventories of finished goods and work-in-progress** — SA `[AR FY26, SA Note 28, p208/pr229]`;
CFS `[AR FY26, CFS Note 30, p289/pr310]`; FY24 `[AR FY25, SA Note 30, p139/pr134]`

| Line, as printed | SA FY26 | SA FY25 | CFS FY26 | SA FY24 |
|---|---|---|---|---|
| Inventories at the end of the year — Finished goods | 22,166.65 | 13,787.66 | **22,368.23** | 7,894.09 |
| Inventories at the end of the year — Work-in-progress | 8.45 | 347.86 | 8.45 | 10.97 |
| Inventories at the beginning of the year — Finished goods | 13,787.66 | 7,894.09 | 13,787.66 | 3,013.82 |
| Inventories at the beginning of the year — Work-in-progress | 347.86 | 10.97 | 347.86 | 87.94 |
| **Net change** | **(8,039.58)** | **(6,230.46)** | **(8,241.16)** | **(4,803.30)** |

### 5.4 Employee benefit expense, with the share-based payment charge shown separately

SA `[AR FY26, SA Note 29, p209/pr230]` · CFS `[AR FY26, CFS Note 31, p289/pr310]` ·
FY24 `[AR FY25, SA Note 31, p139/pr134]` · CFS FY25 `[AR FY25, CFS Note 31, p210/pr205]`

| Line, as printed | SA FY26 | SA FY25 | CFS FY26 | CFS FY25 | SA FY24 |
|---|---|---|---|---|---|
| Salaries and wages | 1,710.92 | 1,358.27 | 1,745.46 | 1,361.79 | 980.58 |
| Contribution to provident and other funds | 52.79 | 42.17 | 53.96 | 42.17 | 33.69 |
| Gratuity expenses | 20.79 | 8.01 | 21.22 | 8.01 | 16.78 |
| **Expense on employee stock option scheme** | **926.50** | **512.39** | **926.67** | **512.39** | **292.58** |
| Staff welfare expenses | 75.94 | 101.59 | 77.12 | 101.66 | 60.62 |
| **Total** | **2,786.94** | **2,022.43** | **2,824.43** | **2,026.02** | **1,384.25** |

*Tie-outs (code-run) ✔ on SA FY26 and CFS FY26.*
**The share-based payment charge appears at three different values in FY26: 926.50 (Note 29), 926.51
(SA cash flow) and 926.50/(179.62 exercised) in the ESOP-reserve roll-forward. See §9, A-03.**

**Defined contribution plan detail** — SA `[AR FY26, SA Note 33 I, p211/pr232]`:

| Line | SA FY26 | SA FY25 | **CFS FY26** | CFS FY25 | SA FY24 |
|---|---|---|---|---|---|
| Employer's Contribution to Provident Fund | 52.39 | 41.68 | **–** | 41.68 | 33.01 |
| Employer's Contribution to Employee State Insurance Corporation | 0.40 | 0.49 | **–** | 0.49 | 0.68 |
| **Expense recognized during the year** | **52.79** | **42.17** | **–** | **42.17** | **33.69** |

> **The consolidated FY26 defined-contribution table is printed as NIL in all three rows**
> `[AR FY26, CFS Note 35 I, p291/pr312]`, while CFS Note 31 charges **53.96** for the same item. §9, A-09.

### 5.5 Other expenses, line by line (this is where a fast-growing 'others' hides)

**SA `[AR FY26, SA Note 32, p209–210/pr230–231]` and `[AR FY25, SA Note 34, p140–141/pr135–136]`**

| Line, as printed | SA FY26 | SA FY25 **as shown in AR FY26** | SA FY25 **as shown in AR FY25** | SA FY24 (AR FY25) |
|---|---|---|---|---|
| Power and fuel | 188.50 | 176.07 | 176.07 | 110.10 |
| Certification & hallmarking charges | 53.42 | 70.63 | 70.63 | 76.14 |
| Job work charges | 130.99 | 251.12 | 251.12 | 374.91 |
| Contract labour charges | 428.79 | 620.67 | 620.67 | 249.02 |
| Consumables | 82.63 | 100.30 | 100.30 | 50.39 |
| Security charges | 69.86 | 76.03 | 76.03 | 44.47 |
| Bank charges | 5.01 | 5.76 | 5.76 | 3.39 |
| Insurance | 55.82 | 42.92 | 42.92 | 18.09 |
| Repairs and maintenance — Buildings | 49.58 | 93.33 | 93.33 | 60.68 |
| Rates and taxes | 33.58 | 41.26 | 41.26 | 45.48 |
| **Advertisement & marketing costs** | **1,595.01** | **1,591.66** | **1,591.66** | **1,242.30** |
| Payment gateway charges | 167.50 | 138.32 | 138.32 | 102.13 |
| Shipping charges | 82.12 | 89.95 | 89.95 | 74.77 |
| Brokerage & commission | 78.10 | 58.34 | 58.34 | 271.09 |
| Printing & stationery expenses | 46.91 | **52.98** | **49.49** | 37.09 |
| **Postage and courier charges** | *(line absent)* | *(line absent)* | **3.49** | 1.79 |
| Software and web development charges | 29.09 | 25.77 | 25.77 | 11.41 |
| **Recruitment charges** | *(line absent)* | *(line absent)* | **1.32** | 4.61 |
| Bad debts written off | – | 1.60 | 1.60 | 2.75 |
| Less: Provision created in earlier years | – | (1.60) | (1.60) | – |
| **Advances written off** | *(line absent)* | *(line absent)* | – | **25.02** |
| Rent (Refer note 4c) | 33.07 | 20.22 | 20.22 | 36.13 |
| Legal and professional charges | 92.89 | 133.74 | 133.74 | 100.88 |
| Travelling and conveyance expenses | 94.52 | 80.48 | 80.48 | 46.06 |
| Technology & communication expenses | 96.17 | 61.03 | 61.03 | 46.98 |
| Auditors remuneration (refer note (a) below)* | 4.98 | 3.48 | 3.48 | 2.35 |
| **Provision for doubtful debt and other receivables** | *(line absent)* | *(line absent)* | – | 1.20 |
| **Office maintenance** | 19.54 | **28.23** | **176.13** | 141.80 |
| **Store maintenance** | **201.72** | **147.90** | *(line absent)* | *(line absent)* |
| Loss on sale of Property, plant and equipment | 31.05 | 19.48 | 19.48 | – |
| Miscellaneous expenses | 6.64 | **4.18** | **2.86** | 19.22 |
| **Total** | **3,677.49** | **3,933.85** | **3,933.85** | **3,200.24** |

*Tie-outs (code-run, §4a trigger 1 — 27–30 operand columns): SA FY26 ✔ 3,677.49; SA FY25 on both
presentations ✔ 3,933.85; **SA FY24 components sum to 3,200.25 vs printed 3,200.24, residual (0.01)** — §9, A-10.*

*Reclassification of the FY25 comparative between the two annual reports, arithmetic shown
(DERIVED): Office maintenance 176.13 = Office maintenance 28.23 + Store maintenance 147.90 ✔;
Printing & stationery 52.98 = 49.49 + Postage and courier 3.49 ✔; Miscellaneous 4.18 = 2.86 + Recruitment
charges 1.32 ✔. Three FY25 line items were merged/split without the note saying which. §9, A-12.*

**CONSOLIDATED other expenses** `[AR FY26, CFS Note 34, p290/pr311]` and `[AR FY25, CFS Note 34, p210–211/pr205–206]`

| Line, as printed | CFS FY26 | CFS FY25 **as shown in AR FY26** | CFS FY25 **as shown in AR FY25** |
|---|---|---|---|
| Power and fuel | 189.33 | 176.07 | 176.07 |
| Certification & hallmarking charges | 53.87 | 70.63 | 70.63 |
| Job work charges | 131.08 | 251.12 | 251.12 |
| Contract labour charges | 428.79 | 620.67 | 620.67 |
| Consumables | 82.63 | 100.30 | 100.30 |
| Security charges | 70.34 | 76.03 | 76.03 |
| Bank charges | 5.03 | 5.76 | 5.76 |
| Insurance | 56.44 | 43.02 | 43.02 |
| Repairs and maintenance — Buildings | 50.18 | 93.33 | 93.33 |
| Rates and taxes | 34.77 | 41.38 | 41.38 |
| Advertisement & marketing costs | 1,609.67 | 1,591.66 | 1,591.66 |
| Payment gateway charges | 167.57 | 138.32 | 138.32 |
| Shipping charges | 82.12 | 90.05 | 90.05 |
| Brokerage & commission | 80.39 | 58.34 | 58.34 |
| Printing & stationery expenses | 48.74 | 52.99 | 49.49 |
| Postage and courier charges | *(absent)* | *(absent)* | 3.50 |
| Software and web development charges | 32.03 | 26.16 | 26.16 |
| Recruitment charges | *(absent)* | *(absent)* | 1.32 |
| Bad debts written off / Less: Provision created in earlier years | – / – | 1.60 / (1.60) | 1.60 / (1.60) |
| Rent (Refer note 4c) | 34.76 | 20.37 | 20.37 |
| Legal and professional charges | 100.06 | 136.77 | 136.77 |
| Travelling and conveyance expenses | 95.71 | 80.62 | 80.62 |
| Technology & communication expenses | 96.30 | 61.03 | 61.03 |
| Auditors remuneration | 5.48 | 3.59 | 3.59 |
| **Office maintenance** | 19.58 | **176.21** | **176.21** |
| **Store maintenance** | **202.86** | **–** | *(absent)* |
| Loss on sale of Property, plant and equipment | 31.05 | 19.48 | 19.48 |
| Miscellaneous expenses | 6.29 | 4.14 | 2.82 |
| **Total** | **3,715.07** | **3,938.04** | **3,938.04** |

*Tie-outs (code-run) ✔ on all three columns.*
**The consolidated FY25 comparative in AR FY26 keeps 176.21 in Office maintenance and shows Store
maintenance as nil, while the standalone FY25 comparative in the same annual report splits the same
population 28.23 / 147.90 — see §9, A-13.**

**Payment to Auditors sub-note**

| Line, as printed | SA FY26 | SA FY25 | CFS FY26 | CFS FY25 | SA FY24 |
|---|---|---|---|---|---|
| As auditor: Statutory audit | 4.50 | 3.35 | 5.00 | 3.45 | 2.25 |
| Certification services | 0.19 | – | 0.19 | – | – |
| Reimbursement of expenses | 0.29 | 0.13 | 0.29 | 0.14 | 0.10 |
| **Total** | **4.98** | **3.48** | **5.48** | **3.59** | **2.35** |

Verbatim footnote, AR FY26: *"Excludes fees paid to auditors amounting to ₹ 9.85 million (including
reimbursement of expenses) (31 March 2025 - ₹ 14.09 million) and fees paid to erstwhile auditors ₹ 4.13
million (including reimbursement of expenses) (31 March 2025 - ₹ 16.07 million) in connection with the
initial public offer of equity shares of the Company."* `[AR FY26, SA Note 32(a), p210/pr231]`

AR FY25 footnote adds: *"…for the year ended 31 March 2025 (31 March 2024 - Nil) in connection with the
initial public offer … **which has currently recognized under prepaid expenses (other current assets)**"*
`[AR FY25, SA Note 34(a), p141/pr136]`

### 5.6 Finance costs by instrument

SA `[AR FY26, SA Note 30, p209/pr230]` · CFS `[AR FY26, CFS Note 32, p289/pr310]` ·
FY24 `[AR FY25, SA Note 32, p140/pr135]`

| Line, as printed | SA FY26 | SA FY25 | CFS FY26 | CFS FY25 | SA FY24 |
|---|---|---|---|---|---|
| Interest on: Term loans from banks and financial institutions | 796.49 | 604.42 | 796.49 | 604.42 | 280.09 |
| Interest on: **Debentures** | 234.78 | 460.26 | 234.78 | 460.26 | 289.70 |
| Interest on: **Delayed payment of taxes** | *(absent)* | *(absent)* | *(absent)* | – | **2.07** |
| Interest on: **Franchisee deposit** *(CFS FY25 label: "Franchisee")* | 387.01 | 464.09 | 387.01 | 464.09 | 488.87 |
| Interest on: Lease liabilities (Refer note 4c) | 634.50 | 509.33 | **643.43** | 509.36 | 305.30 |
| Other borrowing costs | 42.40 | 37.32 | 42.40 | 37.32 | 10.68 |
| **Total** | **2,095.18** | **2,075.42** | **2,104.11** | **2,075.45** | **1,376.71** |

*Tie-outs (code-run) ✔ all columns.*
*Note the gap between P&L finance costs (2,095.18 SA FY26) and the cash-flow add-back (2,052.78):
₹42.40 mn = "Other borrowing costs", i.e. the add-back excludes it. Transcribed, not interpreted.*

### 5.7 Depreciation split — PPE vs ROU vs intangibles

SA `[AR FY26, SA Note 31, p209/pr230]` · CFS `[AR FY26, CFS Note 33, p290/pr311]` ·
FY24 `[AR FY25, SA Note 33, p140/pr135]`

| Line, as printed | SA FY26 | SA FY25 | CFS FY26 | CFS FY25 | SA FY24 |
|---|---|---|---|---|---|
| Depreciation of property, plant and equipment (Refer note 3) | 670.30 | 445.29 | 672.14 | 445.29 | 279.97 |
| Amortization of other intangible assets (Refer note 6a) | 14.45 | 4.13 | 14.53 | 4.13 | 2.08 |
| **Depreciation of right to use assets (Refer note 4c)** | **1,396.43** | **1,025.33** | **1,412.60** | **1,025.47** | **670.61** |
| **Total** | **2,081.18** | **1,474.75** | **2,099.27** | **1,474.89** | **952.66** |

*Tie-outs ✔.*

### 5.8 Tax reconciliation, statutory rate to effective rate

SA `[AR FY26, SA Note 34, p213–214/pr234–235]` · CFS `[AR FY26, CFS Note 36, p294–295/pr315–316]` ·
FY24/FY25 `[AR FY25, SA Note 36, p143–144/pr138–139]`

| Line, as printed | SA FY26 | SA FY25 | CFS FY26 | CFS FY25 | SA FY24 |
|---|---|---|---|---|---|
| **a) Amount recognized in Statement of Profit or Loss** | | | | | |
| Current tax | – | – | – | – | – |
| Deferred tax | – | – | – | – | – |
| **Income tax expense reported in the Statement of Profit and Loss** | **–** | **–** | **–** | **–** | **–** |
| **b) Income tax recognized in OCI** — Remeasurement of the net defined benefit liability/asset | – | – | – | – | – |
| **b)** Tax (expense)/benefit | – | – | – | – | – |
| **c) Reconciliation of effective tax rate** — Profit/(loss) before tax | 260.00 | (2,192.14) | 131.79 | (2,218.37) | (1,422.36) |
| **c)** Tax amount at the enacted income tax rate | **25.17%** | 25.17% | 25.17% | 25.17% | 25.17% |
| **c)** *"Expected income tax expense at statutory tax rate"* *(row exists only in AR FY25)* | — | — | — | — | – |
| **c)** Income tax expense recognised in Statement of Profit and Loss | – | – | – | – | – |

> **The "reconciliation of effective tax rate" prints only the rate and two nils. There is no
> line-by-line reconciliation of the ₹65.44 mn (25.17% × 260.00) that the enacted rate would imply on
> the FY26 standalone profit to the nil actually recognised.** The gap is explained only in a footnote:
> *"No current tax expense has been recognized during the year as the Company has sufficient brought-forward
> tax losses available for set-off against current year taxable profits. The tax impact of such losses has
> been considered in determining the current year's tax position."* `[AR FY26, SA Note 34(c), p213/pr234]`
> → a quantified statutory-to-effective bridge would be answered by the **tax computation / Form 3CD**,
> which is not a public document.

**d) Income tax assets and liabilities**

| Line | SA 31-Mar-26 | SA 31-Mar-25 | CFS 31-Mar-26 | 31-Mar-24 |
|---|---|---|---|---|
| Advance income tax and tax deducted at source | 98.68 | 117.47 | 99.00 | 36.33 |
| Provision for taxes | – | – | – | – |
| **Net income tax asset/(liability) at the end of the year** | **98.68** | **117.47** | **99.00** | **36.33** |

### 5.9 Deferred tax asset composition and the recognition judgement

SA `[AR FY26, SA Note 34(e), p214/pr235]` · CFS `[AR FY26, CFS Note 36(e), p294–295/pr315–316]` ·
FY24 `[AR FY25, SA Note 36E, p144/pr139]`

| Deferred tax assets on: | SA 31-Mar-26 | SA 31-Mar-25 | CFS 31-Mar-26 | CFS 31-Mar-25 | 31-Mar-24 |
|---|---|---|---|---|---|
| Provision for compensated absences, gratuity and other employee benefits | 21.99 | 16.08 | 22.31 | 16.08 | 13.70 |
| Excess of depreciation provided for in the books over the depreciation allowed under the Income tax laws | 97.18 | 57.61 | 97.71 | 57.61 | 81.87 |
| Lease liabilities (net of Right-to-use asset) under Ind AS 116 | 223.49 | 141.90 | 224.59 | **141.88** | 70.18 |
| **Brought forward losses of earlier years** | **896.73** | **1,514.38** | **912.76** | **1,516.10** | **1,250.82** |
| **Gross deferred tax assets** | **1,239.39** | **1,729.97** | **1,257.37** | **1,731.67** | **1,416.57** |
| **Net deferred tax liabilities/(assets)** | **(1,239.39)** | **(1,729.97)** | **(1,257.37)** | **(1,731.67)** | **(1,416.57)** |
| **Recognised in the balance sheet** | **NIL** | **NIL** | **NIL** | **NIL** | **NIL** |

*Tie-outs (code-run) ✔ every column.*

**The recognition judgement, verbatim (FY26):** *"Although the Company reported profits during the year
ended 31 March 2026, management believes that sufficient reasonable certainty regarding availability of
future taxable income is not yet established. Accordingly, deferred tax assets have not been recognized
for the year ended 31 March 2026 and 31 March 2025."* `[AR FY26, SA Note 34(e), p214/pr235]`
The consolidated wording is identical but says *"the Company"* inside a Group note `[AR FY26, CFS Note 36(e), p295/pr316]`.

**The FY25 wording, verbatim:** *"In absence of reasonable certainty of taxable income in future years,
during the year ended 31 March 2025 and 31 March 2024, the Company has not created deferred tax asset."*
`[AR FY25, SA Note 36E, p144/pr139]`

### 5.10 Inventories by class

SA `[AR FY26, SA Note 11, p188/pr209]` · CFS `[AR FY26, CFS Note 11, p268/pr289]` ·
FY24 `[AR FY25, SA Note 12, p119/pr114]`. Header on every version: *"(valued at lower of cost and net
realisable value)"*.

| Class, as printed | SA 31-Mar-26 | SA 31-Mar-25 | CFS 31-Mar-26 | 31-Mar-24 |
|---|---|---|---|---|
| Raw materials | 4,230.53 | 2,291.68 | 4,230.53 | 1,992.69 |
| Work-in-progress | 8.45 | 347.86 | 8.45 | 10.97 |
| **Finished goods** | **22,166.65** | **13,787.66** | **22,368.23** | **7,894.09** |
| Packing materials | 110.88 | 98.27 | 110.88 | 14.46 |
| **Total** | **26,516.51** | **16,525.47** | **26,718.09** | **9,912.21** |

*Tie-outs ✔.* Footnote: *"Refer note 18 for charge created against inventories"* (SA FY26); *"Refer note 19"*
(CFS FY26); *"Refer note 20"* (AR FY25).
> **NOT DISCLOSED — inventory by metal/stone content, by ageing bucket, by store vs warehouse vs job-worker,
> and the quantum of gold held under the fair-value hedge designation.** → would be answered by the
> **RHP "Our Business — inventory management"** section (restated basis) or a company disclosure that does
> not exist. No write-down/provision against inventory is disclosed in either year.

### 5.11 Trade receivables with ageing

SA `[AR FY26, SA Note 13, p189–190/pr210–211]` · CFS `[AR FY26, CFS Note 14, p269–271/pr290–292]` ·
FY24 `[AR FY25, SA Note 15, p120–121/pr115–116]`

| Line, as printed | SA 31-Mar-26 | SA 31-Mar-25 | CFS 31-Mar-26 | 31-Mar-24 |
|---|---|---|---|---|
| Trade receivables - considered good | 74.98 | 56.06 | 75.43 | 23.77 |
| Trade receivables - credit impaired | – | – | – | **1.60** |
| *(sub-total)* | 74.98 | 56.06 | 75.43 | 25.37 |
| **Less: Provision for expected credit loss** | **–** | **–** | **–** | **(1.60)** |
| **Total** | **74.98** | **56.06** | **75.43** | **23.77** |

**Ageing schedule — standalone, both years** (columns as printed: *Less than 6 months · 6 months–1 year ·
1-2 years · 2-3 years · More than 3 years · Total*)

| Row, as printed | <6m | 6m–1y | 1–2y | 2–3y | >3y | Total |
|---|---|---|---|---|---|---|
| **31-Mar-2026** Undisputed Trade receivables – considered good | 74.98 | – | – | – | – | 74.98 |
| Undisputed Trade Receivables – which have significant increase in credit risk | – | – | – | – | – | – |
| Undisputed Trade Receivables – credit impaired | – | – | – | – | – | – |
| Disputed Trade Receivables – considered good | – | – | – | – | – | – |
| Disputed Trade Receivables – which have significant increase in credit risk | – | – | – | – | – | – |
| Disputed Trade Receivables – credit impaired | – | – | – | – | – | – |
| **Total** | **74.98** | – | – | – | – | **74.98** |
| **31-Mar-2025** Undisputed – considered good | 56.06 | – | – | – | – | 56.06 |
| *(all other rows nil)* | – | – | – | – | – | – |
| **Total** | **56.06** | – | – | – | – | **56.06** |
| **31-Mar-2024** Undisputed – considered good | 23.77 | – | – | – | – | 23.77 |
| **31-Mar-2024** Undisputed – **credit impaired** | – | **1.60** | – | – | – | **1.60** |
| **Total** | **23.77** | **1.60** | – | – | – | **25.37** |

Footnote both years: *"There are no trade receivable which are not due."* ECL provision **nil** at both
31-Mar-2026 and 31-Mar-2025. Cross-reference to related-party receivables: SA Note 35 (FY26) / Note 37 (FY25).

### 5.12 Trade payables with ageing, and the MSMED disclosure

SA `[AR FY26, SA Note 23, p204–206/pr225–227]` · CFS `[AR FY26, CFS Note 24, p285–286/pr306–307]` ·
FY24 `[AR FY25, SA Note 25, p136–137/pr131–132]`

| Line, as printed | SA 31-Mar-26 | SA 31-Mar-25 | CFS 31-Mar-26 | CFS 31-Mar-25 | 31-Mar-24 |
|---|---|---|---|---|---|
| Total outstanding dues of micro enterprises and small enterprises | 399.25 | 282.97 | 399.56 | 282.97 | 418.55 |
| Total outstanding dues of creditors other than micro enterprises and small enterprises | 1,160.11 | 1,364.21 | 1,204.26 | 1,364.38 | 1,748.94 |
| **Total trade payables** | **1,559.36** | **1,647.18** | **1,603.82** | **1,647.35** | **2,167.49** |

**MSMED Act disclosure (SA, both years, and CFS)** — every one of the five statutory items is **NIL** except
principal outstanding:

| Item, as printed | SA 31-Mar-26 | SA 31-Mar-25 | CFS 31-Mar-26 |
|---|---|---|---|
| (i) Principal remaining unpaid to any supplier at year end | 399.25 | 282.97 | 399.56 |
| (i) Interest remaining unpaid | – | – | – |
| (ii) Interest paid by the buyer under s.16 MSMED / payment made beyond appointed day | – | – | – |
| (iii) Interest due and payable for the period of delay (paid beyond appointed day, without s.23 interest) | – | – | – |
| (iv) Interest accrued and remaining unpaid at the end of each accounting period | – | – | – |
| (v) Further interest remaining due and payable in succeeding years for s.23 disallowance | – | – | – |

**Ageing schedule — standalone** (columns as printed: *Unbilled · Not due · < 1 year · 1-2 years · 2-3 years · > 3 years · Total*)

| Row, as printed | Unbilled | Not due | <1y | 1–2y | 2–3y | >3y | Total |
|---|---|---|---|---|---|---|---|
| **31-Mar-2026** Micro enterprises and small enterprises | – | 259.87 | 122.22 | 5.53 | 10.65 | 0.98 | 399.25 |
| **31-Mar-2026** Creditors other than micro and small | **468.06** | 507.23 | 155.12 | 18.36 | 4.80 | 6.54 | 1,160.11 |
| Disputed dues — micro and small / other | – | – | – | – | – | – | – |
| **Total** | **468.06** | **767.10** | **277.34** | **23.89** | **15.45** | **7.52** | **1,559.36** |
| **31-Mar-2025** Micro enterprises and small enterprises | – | 62.99 | 153.55 | 65.87 | 0.43 | 0.13 | 282.97 |
| **31-Mar-2025** Creditors other than micro and small | **431.23** | 341.95 | 567.66 | 13.56 | 6.75 | 3.06 | 1,364.21 |
| **Total** | **431.23** | **404.94** | **721.21** | **79.43** | **7.18** | **3.19** | **1,647.18** |
| **31-Mar-2024** Micro enterprises and small enterprises | – | 271.98 | 146.57 | – | – | – | 418.55 |
| **31-Mar-2024** Creditors other than micro and small | **370.93** | 976.92 | 370.83 | 28.25 | 1.21 | 0.80 | 1,748.94 |
| **Total** | **370.93** | **1,248.90** | **517.40** | **28.25** | **1.21** | **0.80** | **2,167.49** |

*Tie-outs (code-run, §4a triggers 1 and 3) ✔ every row and every year.*
*Footnote in AR FY25 under the payables ageing reads "**There are no trade receivable which are not due**"
— a copy-paste from the receivables note `[AR FY25, SA Note 25, p137/pr132]`.*

### 5.13 Borrowings by instrument, with rate and security

**AR FY2026 — standalone (identical wording and figures in CFS Note 19)**
`[AR FY26, SA Note 18, p201–203/pr222–224]` · `[AR FY26, CFS Note 19, p282–283/pr303–304]`

| Non-current borrowings — At Amortised cost, as printed | 31-Mar-2026 | 31-Mar-2025 |
|---|---|---|
| Secured: Redeemable Non-convertible debentures | 1,667.91 | 4,190.11 |
| Secured: Term loan from banks | 232.35 | 33.14 |
| Secured: Term loan from financial institutions | 2,848.61 | 1,627.30 |
| Secured: Vehicle loan | 13.99 | 6.87 |
| Less: Current maturities of long-term borrowings | (2,752.28) | (3,884.59) |
| **Total (A)** | **2,010.58** | **1,972.83** |

| Current borrowings, as printed | 31-Mar-2026 | 31-Mar-2025 |
|---|---|---|
| Secured: Working capital loan | 1,759.99 | 1,320.00 |
| Secured: Bank overdraft | 920.38 | 108.76 |
| Secured: Current maturities of long-term borrowings | 2,752.28 | 3,884.59 |
| **Total (B)** | **5,432.65** | **5,313.35** |
| **Total (A+B)** | **7,443.23** | **7,286.18** |

**Rates and tenors, verbatim** `[AR FY26, SA Note 18, p202/pr223]`:
- *"The coupon rate for Redeemable Non-convertible debentures ranges from **12.75% p.a. to 14.50% p.a.**
  (31 March 2025 - 12.50% p.a. to 14.50% p.a.) with a tenor of **18 to 36 months**."*
- *"The rate of interest for term loan from banks and financial institutions is **7.90% p.a. to 13.10%**
  (31 March 2025 - 7.90% p.a. to 13.50% p.a.) with a tenor of **24 to 60 months**."*
- *"The rate of interest for vehicle loan is **7.99% p.a. to 9.55% p.a.** (31 March 2025 - same) with a tenor
  of 36 to 60 months."*
- *"The rate of interest for working capital loans ranges from **9.25% to 12.35% p.a.** (31 March 2025 -
  10.00% to 13.50% p.a.) with a tenor of **30 to 180 days**."*
- *"The rate of interest for cash credit/overdraft ranges from **7.35% - 10.25% p.a.** (31 March 2025 -
  10% - 10.70% p.a.)."*

**Security, verbatim** `[AR FY26, SA Note 18, p202–203/pr223–224]`:
> *"The Redeemable Non-convertible debentures are secured by way of **first ranking pari passu charge over
> all current assets of the Company, both present and future including intellectual properties and
> non-current assets (including tangible and intangible fixed assets)**."*
> *"The loan mentioned above is secured by way of first ranking pari passu charge by way of hypothecation on
> all existing and future current assets (including book debts, trade receivables, stock in trade, inventory,
> unencumbered cash equivalents **except for the fixed deposits exclusively lien marked with the lender or
> other financial institutions/lenders for gold on loan or otherwise**, customer advances, supplier advance,
> GST refunds etc.), immovable and movable assets, fixed assets, **intangible assets (including intellectual
> property, brand/trademarks)** of the Company."*
> *"The vehicle loan mentioned above is secured against hypothecation of vehicles."*

**Stock statement, verbatim:** *"The quarterly statements filed with the banks against the borrowings
obtained by the Company are in agreement with the books of accounts for the year ended 31 March 2026 and
31 March 2025."*
**Default, verbatim:** *"There are no instances of default in payment of principal or interest for the year
ended 31 March 2026 and 31 March 2025."* `[AR FY26, SA Note 18, p203/pr224]`

**AR FY2025 — standalone, LENDER-BY-LENDER (a granularity that disappears in AR FY26)**
`[AR FY25, SA Note 20, p131–134/pr126–129]`

| Non-current borrowings, as printed | 31-Mar-2025 | 31-Mar-2024 |
|---|---|---|
| Secured: Redeemable Non-convertible debentures | 4,190.11 | 2,332.57 |
| Less: Current maturities | (2,755.51) | (1,288.58) |
| *(sub-total NCD)* | 1,434.60 | 1,043.99 |
| Term loans from banks: a) **HDFC Bank Limited** | 33.14 | 62.38 |
| Less: Current maturities | (15.91) | (29.25) |
| *(sub-total banks)* | 17.23 | 33.13 |
| Term loans from others: b) **Blacksoil Capital Private Limited** | – | 200.00 |
| Term loans from others: c) **Oxyzo Financial Services Private Limited** | 589.17 | 425.00 |
| Term loans from others: d) **Incred Financial Services Limited** | 38.13 | 71.23 |
| Term loans from others: e) **Northern Arc Capital Limited** | 500.00 | 500.00 |
| Term loans from others: f) **Poonawalla Fincorp Limited** | 500.00 | – |
| Less: Current maturities | (1,111.19) | (433.93) |
| *(sub-total others)* | 516.11 | 762.30 |
| Vehicle loan: g) **BMW India Financial Services Private Limited** | 4.99 | 6.09 |
| Vehicle loan: h) **Axis Bank Limited** | 1.88 | – |
| Less: Current maturities | (1.98) | (1.10) |
| *(sub-total vehicle)* | 4.89 | 4.99 |
| Unsecured: **Liability component of Optionally Convertible Redeemable Preference Shares** — Nil OCRPS series E1 (31-Mar-2024: 7,292 shares of ₹10 each) | **–** | **6.99** |
| **Total (A)** | **1,972.83** | **1,851.40** |

| Current borrowings, as printed | 31-Mar-2025 | 31-Mar-2024 |
|---|---|---|
| Redeemable NCDs: a) Current maturities of long-term borrowings | 2,755.51 | 1,288.58 |
| From banks: b) Working capital loan | 620.00 | 200.00 |
| From banks: c) Bank overdraft | 108.76 | – |
| From banks: d) Current maturities of long-term borrowings | 15.91 | 29.25 |
| From others: e) Working capital loan | 450.00 | 200.00 |
| From others: f) **Payable Financing** | 250.00 | 300.00 |
| From others: g) Current maturities of long-term borrowings | 1,111.19 | 433.93 |
| Vehicle loan: h) Current maturities of long-term borrowings | 1.98 | 1.10 |
| **Total (B)** | **5,313.35** | **2,452.86** |
| **Total (A+B)** | **7,286.18** | **4,304.26** |

**AR FY2025 rate note, verbatim** `[AR FY25, SA Note 20, p131/pr126]` — *note the comparative-year label
is misprinted as "31 March 2025" inside the FY2025 report* (§9, A-17):
> *"The coupon rate for Redeemable Non-convertible debentures ranges from 12.50% p.a. to 14.50% p.a.
> (**31 March 2025** - 11.25% p.a. to 14.95% p.a.) with a tenor of 18 to 36 months."*
> *"The rate of interest for term loans from banks is 7.90% p.a. (31 March 2024 - 7.25% p.a. to 7.50%) and
> loan from others is 11.25% p.a. to 13.50% p.a. (31 March 2024 - 13% p.a. to 14.35% p.a.) with a maturity
> period ranging from 12 to 36 months."*
> *"The rate of interest for payable financing is 11.50% - 12.00% p.a. with a maturity period ranging from
> 90 to 120 days (31 March 2024 - 11.50% p.a. with a maturity period of 120 days)."*

**AR FY2025 — quarterly-return reconciliation with banks: FY25 clean, FY24 NOT clean.**
Verbatim `[AR FY25, SA Note 20, p133/pr128]`:
> *"**For 31 March 2025** — The quarterly statements of book debts and inventories filed with the banks
> against the borrowings obtained by the Company are in agreement with the books of accounts."*
> *"**For 31 March 2024** — The quarterly statements … are in agreement with the books of accounts
> **other than as below**:"*

FY2024 discrepancies as printed (₹ million) — **HDFC Bank Limited and Kotak Mahindra Bank Limited**
(sanctioned HDFC 300 / Kotak 250):

| Quarter ended | Item | As per Quarterly returns | As per unaudited books | Difference |
|---|---|---|---|---|
| 30-Jun-23 | Inventory | 3,622.57 | 3,581.69 | 40.88 |
| 30-Jun-23 | Debtors | 680.66 | 690.69 | (10.03) |
| 30-Jun-23 | **Creditors** | 221.42 | 945.11 | **(723.70)** |
| 30-Sep-23 | Inventory | 3,377.62 | 3,284.10 | 93.52 |
| 30-Sep-23 | Debtors | 1,855.91 | 1,789.16 | 66.74 |
| 30-Sep-23 | **Creditors** | 755.76 | 1,457.03 | **(701.27)** |
| 31-Dec-23 | Inventory | 5,097.24 | 5,165.55 | (68.31) |
| 31-Dec-23 | Debtors | 3,918.05 | 3,934.84 | (16.79) |
| 31-Dec-23 | **Creditors** | 1,318.76 | 1,798.59 | **(479.83)** |
| 31-Mar-24 | **Inventory** | 5,491.22 | 5,977.88 | **(486.66)** |
| 31-Mar-24 | Debtors | 4,516.78 | 4,547.15 | (30.37) |
| 31-Mar-24 | **Creditors** | 1,475.83 | 2,290.53 | **(814.70)** |

**ICICI Bank Limited** (sanctioned 300.00):

| Quarter ended | Item | Quarterly returns | Unaudited books | Difference |
|---|---|---|---|---|
| 30-Jun-23 | Inventory | 3,606.30 | 3,581.69 | 24.61 |
| 30-Jun-23 | Debtors | 771.20 | 690.69 | 80.51 |
| 30-Jun-23 | **Purchases** | 2,720.50 | 3,251.17 | **(530.67)** |
| 30-Jun-23 | **Cash and Cash Equivalent** | 2,834.30 | 3,186.37 | **(352.07)** |
| 30-Jun-23 | **Creditors** | 221.40 | 945.11 | **(723.71)** |
| 30-Sep-23 | Inventory | 3,362.60 | 3,284.10 | 78.50 |
| 30-Sep-23 | Debtors | 1,887.40 | 1,789.16 | 98.24 |
| 30-Sep-23 | **Purchases** | 4,155.90 | 3,610.40 | **545.50** |
| 30-Sep-23 | Cash and Cash Equivalent | 6,183.10 | 6,276.04 | (92.94) |
| 30-Sep-23 | **Creditors** | 755.80 | 1,457.03 | **(701.23)** |

Company's own remarks, verbatim: *"Creditors: Only payables with respect to raw materials purchased are
submitted to bank whereas, amount as per unaudited books of accounts consist of all trade payables
including expenses. Inventory, purchases and debtors: On account of book closure entries. Cash and cash
equivalents: Cash and cash equivalents includes cash balance, bank balances and fixed deposits with banks
and NBFC's. (excluding lien marked FD's other than GML)."* `[AR FY25, SA Note 20, p133/pr128]`

**AR FY2025 — instances of default, FY2024** `[AR FY25, SA Note 20, p134/pr129]`. Verbatim heading:
*"During the year 31 March 2024, the Company had instances of default in payment of principal/interest as below"*

| Lender | Principal not paid on due date | Interest not paid on due date | Days delay | Remark (verbatim, condensed) |
|---|---|---|---|---|
| Stride Fintree Private Limited | – | 0.59 | 31 | *"Caused due to processing delays. Amount repaid with default interest."* |
| Klub works private limited | 10.00 | 0.88 | 8 | *"The NACH facility was active however the lender presented the NACH after the due date. There was adequate balance available as on due date."* |
| Capsave finance private limited | – | 1.96 | 1 | same NACH remark |
| Capsave finance private limited | – | 0.06 | 3 | same NACH remark |
| Capsave finance private limited | – | 1.83 | 1 | same NACH remark |
| BMW India Financial services private limited | 0.09 | 0.02 | 1 | same NACH remark |
| BMW India Financial services private limited | 0.09 | 0.04 | 1 | same NACH remark |

All rows show **nil** amount remaining unpaid as at 31-Mar-2024 and nil paid till the date of report.
**No default table appears in AR FY2026 or for FY2025.**

### 5.14 Gold on loan (a separate balance-sheet line, not inside Borrowings)

SA `[AR FY26, SA Note 22, p204/pr225]` · CFS `[AR FY26, CFS Note 23, p284/pr305]` ·
FY24 `[AR FY25, SA Note 24, p135/pr130]`

| Line, as printed | SA 31-Mar-26 | SA 31-Mar-25 | 31-Mar-24 |
|---|---|---|---|
| Gold on loan *(AR FY25 label: "Gold Metal Loan")* | 2,848.14 | 3,865.53 | 4,424.61 |
| **Total** | **2,848.14** | **3,865.53** | **4,424.61** |

Verbatim FY26: *"Represents amounts payable against gold purchased from various banks under gold on loan
scheme with an interest rate of **2.50%-6.50% p.a.** (31 March 2025 - 2.50%-9.00% p.a.) and is payable at
monthly intervals. The credit period under the aforesaid arrangement is **upto 180 days** from the date of
delivery of gold. The amounts are secured against fixed deposits placed by the Company (refer note 8, 14
and 15)."* `[AR FY26, SA Note 22, p204/pr225]`
FY24 rate, verbatim: *"…with a interest rate of 2.50%-9.00% p.a. (**31 March 2024 - 2.50%**)…"*
`[AR FY25, SA Note 24, p135/pr130]`

### 5.15 Other liabilities — where the new FY26 funding line sits

SA `[AR FY26, SA Note 24, p206/pr227]` · CFS `[AR FY26, CFS Note 25, p286–287/pr307–308]` ·
FY24 `[AR FY25, SA Note 26, p137/pr132]`

| Line, as printed | SA 31-Mar-26 | SA 31-Mar-25 | CFS 31-Mar-26 | CFS 31-Mar-25 | 31-Mar-24 |
|---|---|---|---|---|---|
| Advance from customers *(FY25 label: "Advance received from customers")* | 616.94 | 272.85 | 616.94 | 272.85 | 99.72 |
| **Gold Schemes** *(FY25 label: "Gold Mine Scheme")* | 1,900.97 | 1,727.97 | 1,900.97 | 1,727.97 | 1,087.74 |
| Capital creditors | 86.52 | 173.06 | 86.52 | 173.06 | 65.20 |
| **Refund liability** *(FY25 label: "Liability for sales return")* | 108.86 | 105.73 | 108.86 | 105.73 | 66.20 |
| Statutory dues payable | 121.85 | 39.47 | 121.85 | 39.47 | 202.58 |
| Gift vouchers | 603.91 | 517.49 | 603.91 | 517.49 | 384.83 |
| **Gold on lease** *(new line, nil in FY25)* | **4,152.88** | **–** | **4,152.88** | **–** | *(line absent)* |
| Other payables | 2.98 | 27.14 | 2.98 | 27.14 | 9.18 |
| **Total** | **7,594.91** | **2,863.71** | **7,597.00** | **2,863.86** | **1,915.45** |

*Tie-outs (code-run, 8 operands) ✔ SA FY26, SA FY25 and FY24.*
**Gold on lease, verbatim:** *"The Company procures gold from external parties on lease basis with variable
interest rates ranging from **4% to 5%** payable at monthly intervals. The tenure of such lease arrangements
is **365 days** in case of fixed tenure leases."* `[AR FY26, SA Note 24 footnote **, p206/pr227]`
> **NOT DISCLOSED — the counterparties to the gold-on-lease arrangement, the security given, and whether it
> was reflected in the quarterly stock statements filed with lenders.** → would be answered by the
> **credit rating agency's rationale** (GAP-004 in `data/source_register.md`, not collected) or a
> lender-wise schedule the company does not publish.

### 5.16 Lease liability maturity, ROU movement, and lease expense

**A. ROU asset movement — standalone** `[AR FY26, SA Note 4A, p182/pr203]`; FY24 `[AR FY25, SA Note 4A, p114/pr109]`

| Line, as printed | Furniture and fixtures | Building | Total |
|---|---|---|---|
| **Cost** — Balance as at 1 April 2023 *(AR FY25; column then named "Right of Use buildings")* | — | 4,335.65 | 4,335.65 |
| Additions* (FY24) | — | 1,750.05 | 1,750.05 |
| Disposal/adjustments (FY24) | — | (59.08) | (59.08) |
| **Balance as at 31 March 2024** | — | **6,026.62** | **6,026.62** |
| Additions* (FY25) | – | 4,059.87 | 4,059.87 |
| Disposal/adjustments (FY25) | – | (356.79) | (356.79) |
| **Balance as at 31 March 2025** | – | **9,729.70** | **9,729.70** |
| Additions* (FY26) | **270.47** | 2,299.12 | 2,569.59 |
| Disposal/adjustments (FY26) | – | (460.25) | (460.25) |
| **Balance as at 31 March 2026** | **270.47** | **11,568.57** | **11,839.04** |
| **Accumulated depreciation** — as at 1 April 2023 | — | 745.65 | 745.65 |
| Charge for the year (FY24) | — | 670.61 | 670.61 |
| Deletions (FY24) | — | – | – |
| **Balance as at 31 March 2024** | — | **1,416.26** | **1,416.26** |
| Charge for the year (FY25) | – | 1,025.33 | 1,025.33 |
| Deletions (FY25) | – | (142.22) | (142.22) |
| **Balance as at 31 March 2025** | – | **2,299.37** | **2,299.37** |
| Charge for the year (FY26) | 1.21 | 1,395.22 | 1,396.43 |
| Deletions (FY26) | – | (287.07) | (287.07) |
| **Balance as at 31 March 2026** | **1.21** | **3,407.52** | **3,408.73** |
| **Net carrying amount as at 31 March 2024** | — | **4,610.36** | **4,610.36** |
| **Net carrying amount as at 31 March 2025** | – | **7,430.33** | **7,430.33** |
| **Net carrying amount as at 31 March 2026** | **269.26** | **8,161.05** | **8,430.31** |

*Footnote both years: "**Includes security deposit**". Tie-outs (code-run): gross 9,729.70 + 2,569.59 −
460.25 = 11,839.04 ✔; acc dep 2,299.37 + 1,396.43 − 287.07 = 3,408.73 ✔; net 8,430.31 ✔.*

**Consolidated ROU** `[AR FY26, CFS Note 4A, p262/pr283]`: cost 31-Mar-2026 **12,175.36** (FF 270.47 +
Building 11,904.89), acc. dep. **3,520.15**, net **8,655.21**; FY26 additions 2,810.44; disposals (367.36);
charge 1,412.60; deletions (191.96); 31-Mar-2025 net 7,432.77.

**B. Lease liability movement — standalone** `[AR FY26, SA Note 4B, p182/pr203]`; FY24 `[AR FY25, SA Note 4B, p114/pr109]`

| Line, as printed | FY2026 | FY2025 | **FY2024** |
|---|---|---|---|
| Opening balance | 7,994.13 | 4,889.24 | 3,729.31 |
| Additions | 2,503.77 | 3,950.53 | 1,693.54 |
| Termination | (195.86) | (221.93) | (64.38) |
| Accretion of interest | 634.50 | 509.33 | 305.30 |
| Payments (including rent concession) | (1,618.25) | (1,133.04) | (774.53) |
| **Closing balance** | **9,318.29** | **7,994.13** | **4,889.24** |
| Current | 1,307.34 | 943.06 | 588.06 |
| Non-Current | 8,010.95 | 7,051.07 | 4,301.18 |
| **Total** | **9,318.29** | **7,994.13** | **4,889.24** |

*Tie-out ✔. Consolidated `[AR FY26, CFS Note 4B, p262/pr283]`: opening 7,996.49, additions 2,738.44,
termination (197.97), accretion 643.43, payments (1,632.81), closing **9,547.58**; current 1,329.00,
non-current 8,218.58. FY25 CFS closing 7,996.49.*

**C. Contractual maturities of lease liabilities, undiscounted — standalone**
`[AR FY26, SA Note 4B, p183/pr204]`; FY24 `[AR FY25, SA Note 4, p115/pr110]`

| Bucket, as printed | 31-Mar-2026 | 31-Mar-2025 | **31-Mar-2024** |
|---|---|---|---|
| Not later than one year | 1,950.74 | 1,507.69 | 922.48 |
| Later than one year but within five years | 6,986.76 | 5,693.58 | 3,503.24 |
| Later than five years | 2,835.29 | 3,011.94 | 1,870.81 |
| **Total** | **11,772.79** | **10,213.21** | **6,296.53** |

*Only three buckets are given. Tie-outs ✔ all three years.*

**D. Lease expense recognised in P&L — standalone** `[AR FY26, SA Note 4C, p183/pr204]`

| Line, as printed | FY2026 | FY2025 | **FY2024** |
|---|---|---|---|
| Depreciation expense on Right of Use asset | 1,396.43 | 1,025.33 | 670.61 |
| Interest expense on lease liabilities | 634.50 | 509.33 | 305.30 |
| Rent expenses related to short term leases | 33.07 | 20.22 | 36.13 |
| **Total expense recognised in Statement of Profit and Loss** | **2,064.00** | **1,554.88** | **1,012.04** |

**Total cash outflow for leases, as stated in each report — the two reports DISAGREE on FY25:**
- AR FY26: *"The total cash outlow for leases is **₹ 1,618.25 million** for the year ended 31 March 2026
  (**₹ 1,133.04 million** for the year ended 31 March 2025)."* `[AR FY26, SA Note 4C, p183/pr204]`
- AR FY25: *"The total cash outlow for leases is **` 1,149.38 million** for the 31 March 2025
  (**` 810.66 million** for 31 March 2024) **including cash outlow for short term leases and leases of
  low-value assets**."* `[AR FY25, SA Note 4C, p115/pr110]` → §9, A-18.

**Variable lease payments — a disclosure that flips between the two reports:**
- AR FY26, verbatim: *"During the year ended 31 March 2026, the Company has incurred an amount of ₹ 33.07
  million (Previous year: 20.22 million) on account of **variable lease payments. Variable payment terms
  ranges from 1.00% to 4.00% of net sales from a particular store.** … Excess of variable lease payments
  that depend on sales, over the fixed rental, are recognised in the statement of profit or loss in the
  period in which the condition that triggers those payments occur."* `[AR FY26, SA Note 4C, p183/pr204]`
- AR FY25, verbatim: *"The Company **does not have any lease restrictons and commitment towards variable
  rent as per the contract**."* `[AR FY25, SA Note 4C, p115/pr110]` → §9, A-19.

**Extension/termination options, verbatim (FY26):** *"Extension and termination options are included in a
number of property lease arrangements of the Company. These are used to maximise operational flexibility
in terms of managing the assets used in the Company's operations. The majority of extension and
termination options held are exercisable based on mutual consent of the Company and respective lessors."*
`[AR FY26, SA Note 4C, p183/pr204]`. AR FY25 says only: *"The Company has lease term extension options that
are not reflected in the measurement of lease liabilites."*
> **NOT DISCLOSED — the ₹ amount of undiscounted potential lease payments under un-exercised extension
> options.** → would be answered by an Ind AS 116 para 59(b)(ii) disclosure the company does not make.

### 5.17 Provisions

SA `[AR FY26, SA Note 21, p204/pr225]` · CFS `[AR FY26, CFS Note 22, p284/pr305]` ·
FY24 `[AR FY25, SA Note 23, p135/pr130]`

| Line, as printed | SA 31-Mar-26 | SA 31-Mar-25 | CFS 31-Mar-26 | 31-Mar-24 |
|---|---|---|---|---|
| **Non-current** — Provision for gratuity (Refer note 33) | 50.68 | 35.44 | 51.11 | 22.83 |
| **Non-current** — Provision for compensated absence | *(nil, line printed blank)* | *(line absent)* | **0.64** | **11.10** |
| **Total non-current** | **50.68** | **35.44** | **51.75** | **33.93** |
| **Current** — Provision for gratuity (Refer note 33) | 13.29 | 12.53 | 13.28 | 11.68 |
| **Current** — Provision for compensated absence | 23.39 | 15.93 | 23.59 | 8.84 |
| **Total current** | **36.68** | **28.46** | **36.87** | **20.52** |

*No non-employee provision of any kind (warranty, litigation, restructuring, onerous contract) is disclosed
in either year, on either basis.*

**Gratuity — reconciliation of the projected benefit obligation (unfunded)** `[AR FY26, SA Note 33, p211/pr232]`

| Line, as printed | SA FY26 | SA FY25 | CFS FY26 |
|---|---|---|---|
| Obligations at beginning of the year | 47.97 | 34.51 | 47.97 |
| Service cost | 14.51 | 5.56 | 14.94 |
| **Past service cost** | **3.26** | – | 3.26 |
| Interest on defined benefit obligation | 3.02 | 2.45 | 3.02 |
| Benefits settled | (5.03) | (2.65) | (5.03) |
| Actuarial (gain)/loss | 0.24 | 8.10 | 0.23 |
| **Obligations at the end of year** | **63.97** | **47.97** | **64.39** |
| Closing fair value of plan assets | **–** | **–** | – |
| **Liability recognized in the balance sheet** | **63.97** | **47.97** | **64.39** |

**Expense recognised in P&L:** Service cost 14.51 + Past service cost 3.26 + Interest cost 3.02 =
**Net gratuity cost 20.79** (FY25: 5.56 + 0 + 2.45 = 8.01) `[AR FY26, SA Note 33 b(i), p212/pr233]`

**Remeasurements in OCI** `[AR FY26, SA Note 33 b(ii), p212/pr233]`

| Line, as printed | FY26 | FY25 |
|---|---|---|
| Changes in demographic assumption | (5.90) | 8.64 |
| Changes in financial assumptions | (6.11) | 0.39 |
| Experience variance (i.e. Actual experience vs assumptions) | 12.25 | (0.93) |
| **Actuarial loss/(gain) on defined benefit obligation** | **0.24** | **8.10** |

**Actuarial assumptions** `[AR FY26, SA Note 33 c(i), p212/pr233]`; FY24 `[AR FY25, SA Note 35, p143/pr138]`

| Assumption | FY2026 | FY2025 | **FY2024** |
|---|---|---|---|
| Discount rate | 6.50% | 6.50% | *(not on the extracted page)* |
| **Salary escalation rate** | **6.00%** | **10.00%** | *(not on the extracted page)* |
| Attrition — Annual CTC below ₹1 million | **50.54%** | 49.00% | *(not on the extracted page)* |
| Attrition — Annual CTC ₹1m–₹3m | 23.10% | 33.00% | *(not on the extracted page)* |
| Attrition — Annual CTC ₹3m and above | 28.57% | 18.00% | **17.00%** |
| Mortality rate | 100% of IALM 2012-14 | 100% of IALM 2012-14 | 100% of IALM 2012-14 |
| **Retirement Age (years)** | **60** | **60** | **58** |

**Sensitivity analysis (DBO, ₹ mn)** `[AR FY26, SA Note 33 c(ii), p212/pr233]`; FY24 `[AR FY25, p143/pr138]`

| Assumption | FY26 Increase | FY26 Decrease | FY25 Increase | FY25 Decrease | FY24 Increase | FY24 Decrease |
|---|---|---|---|---|---|---|
| Discount Rate (-/+ 1%) | 61.63 | 66.46 | 46.28 | 49.77 | 33.38 | 35.74 |
| Salary Growth Rate (-/+ 1%) | 66.24 | 61.79 | 49.40 | 46.56 | 35.47 | 33.58 |
| Attrition Rate (-/+ 50% of attrition rates) | 56.93 | 71.88 | 40.91 | 61.61 | 31.09 | 42.19 |
| Mortality Rate (**-/+ 50%** FY26; **-/+ 10%** in AR FY25) | 63.99 | 63.93 | 47.97 | 47.96 | 34.52 | 34.51 |

**Expected future cash flows** `[AR FY26, SA Note 33 c(iii), p213/pr234]`

| Projected benefits payable in future years | FY2026 | FY2025 | FY2024 |
|---|---|---|---|
| 1st following year | 13.29 | 12.53 | 11.68 |
| 2nd to 5th year | 44.79 | 31.84 | 20.48 |
| 6th to 10 years | 19.86 | 12.38 | 8.80 |
| More than 10 years | 5.98 | 6.08 | 4.76 |

### 5.18 Contingent liabilities and commitments — each item separately

| Item, verbatim | FY2026 | FY2025 | FY2024 |
|---|---|---|---|
| **Commitments** — *"Estimated amount of Contracts remaining to be executed on capital account (net of advances)"* | **₹ 114.55 mn** `[AR FY26, SA Note 46, p228/pr249]` | **₹ 248.30 mn** `[AR FY25, SA Note 49, p157/pr152]` | **₹ 212.83 mn** `[AR FY25, SA Note 49, p157/pr152]` |
| **Contingent liabilities** | *"As of the 31 March 2026 and 31 March 2025, the Company has assessed its obligations and confirms that there are **no contingent liabilities requiring disclosure**."* `[AR FY26, SA Note 46, p228/pr249]` | *"As of the 31 March 2025 and 31 March 2024, the Company has assessed its obligations and confirms that there are no contingent liabilities requiring disclosure."* `[AR FY25, SA Note 49, p157/pr152]` | same sentence |
| **Consolidated** | Identical wording and identical ₹114.55 mn / ₹248.30 mn `[AR FY26, CFS Note 48, p309/pr330]` | Identical `[AR FY25, CFS Note 49, p226/pr221]` | — |
| **Pending litigation** (auditor's Rule 11(a)) | *"The Company does not have any pending litigations which would impact its financial position."* `[AR FY26, SA Auditor's Report, para 2(h)(i), p153/pr174]` | Same sentence `[AR FY25, SA Auditor's Report, para 2(h)(i), p87/pr82]` | — |

> **The commitments line is the ONLY off-balance-sheet number disclosed. There is no contingent-liability
> table of any kind — no tax dispute, no guarantee, no letter of credit, no claim not acknowledged as debt —
> in either year, on either basis. This is a nil disclosure, not a missing one, and it is recorded as the
> company's own affirmative statement.**

### 5.19 Capital work in progress and intangible asset under development, with ageing

**CWIP — standalone** `[AR FY26, SA Note 5, p184/pr205]`; FY24 `[AR FY25, SA Note 5, p115–116/pr110–111]`

| Line, as printed | 31-Mar-2026 | 31-Mar-2025 | 31-Mar-2024 |
|---|---|---|---|
| Tangible asset | 26.02 | 43.57 | 166.64 |
| **Total** | **26.02** | **43.57** | **166.64** |
| *Movement:* opening | 43.57 | 166.64 | *(not given)* |
| Add: Additions during the year | 887.80 | 1,783.53 | *(not given)* |
| Less: Capitalised during the year | 905.35 | 1,906.60 | *(not given)* |
| **Closing** | **26.02** | **43.57** | — |

*Tie-out ✔ 43.57 + 887.80 − 905.35 = 26.02. Consolidated `[AR FY26, CFS Note 5, p264/pr285]`: opening
43.57, additions 914.93, capitalised 931.01, closing **27.49**.*
**AR FY2025 gives NO CWIP movement table — only the ageing table and a sentence:** *"During the current
year, Company has capitalised assets amounting to ` 1,906.60 million (31 March 2024 - ` 817.75 million)."*
`[AR FY25, SA Note 5, p116/pr111]`

**CWIP ageing schedule (tangible)** — buckets as printed:

| Bucket | 31-Mar-2026 | 31-Mar-2025 | 31-Mar-2024 | CFS 31-Mar-2026 |
|---|---|---|---|---|
| Projects in progress — Less than 1 year | 26.02 | 43.57 | 166.64 | 27.49 |
| Projects in progress — 1-2 years | – | – | – | – |
| Projects in progress — 2-3 years | – | – | – | – |
| Projects in progress — More than 3 years | – | – | – | – |
| Projects temporarily suspended — all four buckets | – | – | – | – |
| **Total** | **26.02** | **43.57** | **166.64** | **27.49** |

Verbatim: *"There is no CWIP under development whose completion is overdue or has exceeded its cost
compared to the original plan as of 31 March 2026 and 31 March 2025."* `[AR FY26, SA Note 5, p184/pr205]`

**Intangible asset under development** `[AR FY26, SA Note 6B, p185–186/pr206–207]`

| Line, as printed | 31-Mar-2026 | 31-Mar-2025 |
|---|---|---|
| Intangible asset under development | – | 10.28 |
| *Movement:* As at 1 April | 10.28 | – |
| Add: Additions during the year | – | 36.79 |
| **Less: Capitalised/write off during the year** | **10.28** | 26.51 |
| **Closing** | **–** | **10.28** |
| Ageing — Projects in progress, Less than 1 year | – | 10.28 |

*The FY26 movement runs the whole 10.28 through "Capitalised/write off"; the cash-flow add-back line reads
**"Intangible asset under development written off 10.28"** `[AR FY26, SA Cash Flows, p166/pr187]`, and the
P&L carries no separate write-off line — it is inside Other expenses or D&A without being named.
**NOT DISCLOSED — which P&L head absorbed the ₹10.28 mn write-off.** → would be answered by a
sub-analysis of Note 32 the company does not give.*

### 5.20 PPE gross block movement and accumulated depreciation movement

**STANDALONE** `[AR FY26, SA Note 3, p181/pr202]` (FY26 and FY25) and `[AR FY25, SA Note 3, p113/pr108]`
(FY25 and FY24). Classes as printed: *Leasehold improvements · Display Items · Plant and machinery ·
Furniture and fixtures · Office equipment · Computers · Vehicles.*

**Cost**

| Line | Leasehold improvements | Display Items | Plant and machinery | Furniture and fixtures | Office equipment | Computers | Vehicles | **Total** |
|---|---|---|---|---|---|---|---|---|
| Balance as at 1 April 2023 | 368.09 | 26.72 | 58.44 | 165.00 | 354.44 | 76.49 | 0.70 | **1,049.88** |
| Additions (FY24) | 164.87 | – | 24.18 | 141.18 | 437.95 | 35.74 | 13.83 | **817.75** |
| Disposals (FY24) | 98.11 | – | – | 21.81 | 65.36 | 5.70 | – | **190.98** |
| **Balance as at 31 March 2024** | 434.85 | 26.72 | 82.62 | 284.37 | 727.03 | 106.53 | 14.53 | **1,676.65** |
| Additions (FY25) | 874.91 | – | 220.39 | 349.50 | 396.58 | 50.24 | 2.52 | **1,894.14** |
| Disposals (FY25) | 31.17 | 26.72 | – | 4.41 | 6.72 | 0.08 | – | **69.10** |
| **Balance as at 31 March 2025** | 1,278.59 | – | 303.01 | 629.46 | 1,116.89 | 156.69 | 17.05 | **3,501.69** |
| Additions (FY26) | 448.14 | – | 47.07 | 132.89 | 234.73 | 29.14 | 10.05 | **902.02** |
| Disposals (FY26) | 28.57 | – | 6.09 | 142.31 | 165.68 | 0.11 | – | **342.76** |
| **Balance as at 31 March 2026** | 1,698.16 | – | 343.99 | 620.04 | 1,185.94 | 185.72 | 27.10 | **4,060.95** |

**Accumulated depreciation**

| Line | Leasehold improvements | Display Items | Plant and machinery | Furniture and fixtures | Office equipment | Computers | Vehicles | **Total** |
|---|---|---|---|---|---|---|---|---|
| Balance as at 1 April 2023 | 70.18 | 22.43 | 8.32 | 17.39 | 62.81 | 14.86 | 0.51 | **196.50** |
| Depreciation expense for the year (FY24) | 87.96 | 2.15 | 2.81 | 21.94 | 125.12 | 37.98 | 2.01 | **279.97** |
| Disposals (FY24) | 22.74 | – | – | 2.34 | 11.66 | 1.33 | – | **38.07** |
| **Balance as at 31 March 2024** | 135.40 | 24.58 | 11.13 | 36.99 | 176.27 | 51.51 | 2.52 | **438.40** |
| Depreciation expense for the year (FY25) | 156.15 | – | 14.13 | 46.74 | 183.70 | 41.33 | 3.24 | **445.29** |
| Disposals* (FY25) | 14.83 | 24.58 | – | 0.44 | 1.98 | 0.00* | – | **41.82** |
| **Balance as at 31 March 2025** | 276.72 | – | 25.26 | 83.29 | 358.00 | 92.84 | 5.76 | **841.87** |
| Depreciation expense for the year (FY26) | 293.00 | – | 23.32 | 70.23 | 239.06 | 40.66 | 4.03 | **670.30** |
| Disposals (FY26) | 12.63 | – | 1.26 | 21.89 | 53.94 | 0.09 | – | **89.81** |
| **Balance as at 31 March 2026** | 557.09 | – | 47.32 | 131.63 | 543.12 | 133.41 | 9.79 | **1,422.36** |

**Carrying amount (net)**

| As at | Leasehold improvements | Display Items | Plant and machinery | Furniture and fixtures | Office equipment | Computers | Vehicles | **Total** |
|---|---|---|---|---|---|---|---|---|
| 31 March 2024 | 299.45 | 2.14 | 71.49 | 247.38 | 550.76 | 55.02 | 12.01 | **1,238.25** |
| 31 March 2025 | 1,001.87 | – | 277.75 | 546.17 | 758.89 | 63.85 | 11.29 | **2,659.82** |
| 31 March 2026 | 1,141.07 | – | 296.67 | 488.41 | 642.82 | 52.31 | 17.31 | **2,638.59** |

*`*Amount less than ₹ 10,000` (footnote on the Computers FY25 disposal cell).*
*Tie-outs (code-run, §4a triggers 1 and 3): every class opening + additions − disposals = closing ✔;
all six column sums ✔; 4,060.95 − 1,422.36 = 2,638.59 ✔ ties to the balance sheet.*

**Standing statements, verbatim (both years):** *"1. No impairment loss has been recognised during the
current year or previous year. 2. No revaluation of property, plant and equipment were carried out during
the current or previous year."* `[AR FY26, SA Note 3, p181/pr202]`

**CONSOLIDATED PPE** `[AR FY26, CFS Note 3, p261/pr282]` — same seven classes; differences from standalone:
FY26 additions **927.69** (Leasehold improvements 459.83, Furniture and fixtures 140.00, Office equipment
239.79, Computers 30.95); FY26 depreciation **672.14**; cost 31-Mar-2026 **4,086.68**; accumulated
depreciation **1,424.20**; net **2,662.48**. FY25 comparatives differ from standalone only in Computers
(cost 156.75 vs 156.69; net 63.91 vs 63.85) and Total (3,501.75 vs 3,501.69; net 2,659.88 vs 2,659.82).
*Tie-outs ✔.*

### 5.21 Other intangible assets — gross block and amortisation movement

**Standalone** `[AR FY26, SA Note 6A, p184–185/pr205–206]`; FY24 `[AR FY25, SA Note 6A, p116/pr111]`.
Class as printed: **"Application software"** in AR FY26; **"Computer software"** in AR FY25.

| Line | FY24 | FY25 | FY26 |
|---|---|---|---|
| Cost — opening | 9.24 (1-Apr-2023) | 10.32 | 49.28 |
| Additions | 1.08 | 38.96 | 3.33 |
| Disposals | – | – | – |
| **Cost — closing** | **10.32** | **49.28** | **52.61** |
| Accumulated amortization — opening | 6.33 | 8.41 | 12.54 |
| Amortization expense for the year | 2.08 | 4.13 | 14.45 |
| **Accumulated amortization — closing** | **8.41** | **12.54** | **26.99** |
| **Carrying amount (net)** | **1.91** | **36.74** | **25.62** |

*"No revaluation of intangible assets were carried out during the year."*
**Consolidated adds a second class — "Trade Mark"** `[AR FY26, CFS Note 6A, p264–265/pr285–286]`:
cost 0.07 (added FY25), never amortised, net 0.07 at both year-ends; Application software cost 52.60,
amortisation 27.07, net 25.53; **total net 25.60**. Group-only sentence, verbatim:
> *"**Product related intangibles (Trademark) are available to the Group in perpetuity.** The amortisable
> amount of intangible assets is arrived at, based on the management's best estimates of useful lives of
> such assets after due consideration as regards their expected usage, the product life cycles and their
> expected future benefits to the Group."* `[AR FY26, CFS Note 6A, p265/pr286]`

### 5.22 Share capital reconciliation and share count

**Authorised share capital** `[AR FY26, SA Note 16, p191–192/pr212–213]`

| Class, as printed | 31-Mar-2026 | 31-Mar-2025 |
|---|---|---|
| Equity shares: **45,05,00,000** (31-Mar-2025: 16,82,90,700) Equity shares of ₹1 each | **450.50** | 168.29 |
| CCPS Series A / B / B1 / B2 / B3 / C / D / D1 / D2 / D3 / E of ₹10 each; OCRPS Series E1 of ₹10; CCPS E2 / F of ₹10; CCPS G of ₹10; CCPS H of ₹1 | **all Nil** | 6.10 / 1.87 / 0.89 / 13.40 / 1.28 / 14.17 / 19.80 / 6.25 / 6.00 / 3.00 / 1.69 / 0.07 / 3.96 / 3.23 / 190.00 / 10.50 |
| **Total authorised** | **450.50** | **450.50** |

*(AR FY25 authorised equity was **168,290,700 shares / 168.29** vs 31-Mar-2024 **68,290,700 / 68.29**
`[AR FY25, SA Note 18, p122/pr117]`.)*

**Issued, subscribed and paid-up** `[AR FY26, SA Note 16, p192–193/pr213–214]`

| Line, as printed | 31-Mar-2026 | 31-Mar-2025 |
|---|---|---|
| Equity share capital — 15,22,31,365 (PY 3,52,35,000) Equity shares of ₹1 each, fully paid up | **152.23** | **35.23** |
| **Equity component of Compulsory Convertible Preference Shares (CCPS)** — 16 series, all Nil at 31-Mar-2026 | **–** | **261.33** |
| **Total share capital** | **152.23** | **296.56** |

*The FY25 equity share capital is printed as **35.23** here and **35.24** in the SOCIE — §9, A-05b.*

**(a) I. Reconciliation of EQUITY shares outstanding** `[AR FY26, SA Note 16(a) I, p193/pr214]`

| Movement line, as printed | FY26 Number | FY26 Amount | FY25 Number | FY25 Amount |
|---|---|---|---|---|
| Balance at the beginning of the year | 3,52,35,000 | 35.23 | 1,81,51,940 | 18.16 |
| **Shares issued during the year (Refer note 16h)** | **1,67,71,728** | **16.77** | 1,28,02,090 | 12.80 |
| Shares transferred during the year | – | – | 32,23,260 | 3.22 |
| Conversion of OCRPS into equity shares | – | – | 72,920 | 0.07 |
| **Conversion of CCPS into equity shares** | **10,02,24,637** | **100.22** | 9,84,790 | 0.98 |
| **Total Equity shares at the end of the year** | **15,22,31,365** | **152.23** | **3,52,35,000** | **35.23** |

**(a) II. Treasury shares** `[AR FY26, SA Note 16(a) II, p193/pr214]`

| Movement line | FY26 Number | FY26 Amount | FY25 Number | FY25 Amount |
|---|---|---|---|---|
| Balance at the beginning of the year | – | – | 32,23,260 | 3.22 |
| Shares transferred during the year | – | – | (32,23,260) | (3.22) |
| **Total at the end of the year** | **–** | **–** | **–** | **–** |

Verbatim `[AR FY25, SA Note 54, p158/pr153]`: *"The Company has categorized **3,223,260 equity shares** held
by BlueStone Trust (formerly known as BlueStone Jewellery and Lifestyle Limited Management Stock Transfer
trust) as 'treasury shares' … As of 31 March 2025, the Trust has transferred all of its holdings to its
employees and its beneficiaries and no longer possesses any shares in the Company."*

**(a) III. CCPS series-by-series roll-forward, FY26 (all converted at IPO)** `[AR FY26, SA Note 16 III, p194–196/pr215–217]`

| Series | Opening 01-Apr-2025 Number | Opening Amount | Converted into equity shares | Closing 31-Mar-2026 |
|---|---|---|---|---|
| A | 6,09,594 | 6.09 | (6,09,594) / (6.09) | Nil |
| B | 1,86,982 | 1.87 | (1,86,982) / (1.87) | Nil |
| B1 | 88,624 | 0.89 | (88,624) / (0.89) | Nil |
| B2 | 13,39,659 | 13.40 | (13,39,659) / (13.40) | Nil |
| B3 | 1,28,207 | 1.28 | (1,28,207) / (1.28) | Nil |
| C | 14,17,252 | 14.17 | (14,17,252) / (14.17) | Nil |
| D | 19,40,933 | 19.41 | (19,40,933) / (19.41) | Nil |
| D1 | 4,16,865 | 4.17 | (4,16,865) / (4.17) | Nil |
| D2 | 3,59,257 | 3.59 | (3,59,257) / (3.59) | Nil |
| D3 | 1,10,754 | 1.11 | (1,10,754) / (1.11) | Nil |
| E | 1,69,122 | 1.69 | (1,69,122) / (1.69) | Nil |
| E2 | 3,95,836 | 3.96 | (3,95,836) / (3.96) | Nil |
| F | 2,50,658 | 2.51 | (2,50,658) / (2.51) | Nil |
| **G** | **1,76,80,565** | **176.81** | (1,76,80,565) / (176.81) | Nil |
| **H** | **1,03,80,622** | **10.38** | (1,03,80,622) / (10.38) | Nil |
| **Total Share Capital [I + III]** | **7,07,09,930 / 296.56** *(FY25)* | | | **15,22,31,365 / 152.23** |

*(FY25 movements in the same table: Series G opening 1,86,65,355 / 186.65, converted (9,84,790) / (9.84),
closing 1,76,80,565 / 176.81; Series H issued during FY25 1,03,80,622 / 10.38.)*

**(c) Conversion ratios, verbatim** `[AR FY26, SA Note 16(c), p196/pr217]`:
> *"During the year ended 31 March 2026, series A, B, B1, B2, B3, C, D, D1, D2, D3, E and F CCPS is
> converted into equity shares in the ratio of **10:1**, series E2 is converted into equity shares in the
> ratio of **5.01:1** and series G and H is converted into equity shares in the ratio of **1:1** pursuant to
> IPO."*
> *"During the year ended 31 March 2025, 9,84,790 series G CCPS is converted into equity shares in the ratio
> of 1:1."* · *"During the year ended 31 March 2025, 7,292 series E1 OCRPS is converted into equity shares
> in the ratio of 10:1."* · *"During the year ended 31 March 2025, the Company had issued H series CCPS and
> the CCPS holders of Series H have agreed a fixed conversion of 1 equity shares for every 1 CCPS held and
> therefore the same was classified as equity."*

**(d)–(h) Five-year capital history, verbatim** `[AR FY26, SA Note 16, p196/pr217]`:
- *"(d) In the period of five years immediately preceding the current year, during the year 2022-23, the
  Company had issued **bonus shares of 1,63,36,746 of equity shares**."*
- *"(e) **No class of shares have been bought back** by the Company during the period of five years…"*
- *"(f) **No class of shares have been issued for consideration other than cash** … during the period of
  five years…"*
- *"(g) During the year ended 31 March 2025, the Company has issued **1,00,01,847 rights equity shares at a
  price of ₹ 34 each**, which includes a premium of ₹ 33 per share."*
- *"(h) During the year ended 31 March 2026, the Company issued **1,58,60,735 equity shares** pursuant to
  its Initial Public Offering (IPO) at an issue price of **₹ 517 per share**, comprising a face value of ₹ 1
  per share and a securities premium of **₹ 516 per share**."*

**(i) Shareholders holding more than 5% — EQUITY** `[AR FY26, SA Note 16(i), p197/pr218]`

| Name | 31-Mar-2026 Number | % | 31-Mar-2025 Number | % |
|---|---|---|---|---|
| **Gaurav Singh Kushwaha** | 2,44,65,127 | **16%** | 2,44,65,127 | **69%** |
| Accel India III (Mauritius) Ltd | 1,32,90,055 | 9% | – | – |
| SBI Life Insurance Co. Ltd | 76,11,320 | 5% | – | – |
| M/s. Access India Capital* | – | – | 29,26,410 | 8% |
| **Total** | **4,53,66,502** | **30%** | **2,73,91,537** | **77%** |

*`*Holding below 5% during current year`. The FY26 report also prints the full pre-IPO >5% holder list for
every CCPS series at 31-Mar-2025 (Series A through H) at `[AR FY26, SA Note 16(i), p197–200/pr218–221]` —
the pre-IPO cap table; the FY26 column is Nil throughout because every series converted.*

**(j) Shareholding of promoters** `[AR FY26, SA Note 16(j), p200/pr221]`

| Particulars | 31-Mar-2026 Number | % | 31-Mar-2025 Number | % |
|---|---|---|---|---|
| Mr. Gaurav Singh Kushwaha, equity shares of ₹1 each | 2,44,65,127 | **16%** | 2,44,65,127 | **69%** |

*AR FY25 gives the FY24 comparative: **13,950,000 / 77%** `[AR FY25, SA Note 18(i), p129/pr124]`.*
> **NOT DISCLOSED in either annual report — promoter shares pledged or encumbered.** The Schedule III
> "% change during the year" column of the promoter table is not printed either. → would be answered by
> the **promoter SAST Reg 31(4) filing of 24-Jun-2026**, which is a scanned image with 50 bytes of extracted
> text (GAP-002 in `data/source_register.md`).

### 5.23 Other equity note — the reserve-by-reserve roll-forward behind the SOCIE

SA `[AR FY26, SA Note 17, p200–201/pr221–222]`; FY24 `[AR FY25, SA Note 19, p129–130/pr124–125]`

| (i) Securities premium | FY26 | FY25 | FY24 |
|---|---|---|---|
| Opening balance | 32,451.30 | 25,221.43 | 19,530.55 |
| **Premium received on issue of shares (Refer note 45)** | **8,440.59** | **7,235.70** | **5,690.88** |
| Add: Reclassification from Liability to Equity (Refer note 16c) | – | 6.92 | – |
| Add: Conversion from CCPS to Equity | 161.10 | 8.86 | – |
| **Less: Share issue expenses** | **(413.37)** | **(21.61)** | **–** |
| **Closing balance** | **40,639.62** | **32,451.30** | **25,221.43** |

| (ii) Retained earnings | FY26 | FY25 | FY24 |
|---|---|---|---|
| Opening balance | (24,517.62) | (22,325.48) | (20,748.50) |
| Add: Profit/(Loss) during the year | 260.00 | (2,192.14) | (1,422.36) |
| **Less: Change in fair value of Equity on termination of Right to subscribe shares (note 48)** | — | – | **(154.62)** |
| **Closing balance** | **(24,257.62)** | **(24,517.62)** | **(22,325.48)** |

| (iii) Employee Stock Options Reserves | FY26 | FY25 | FY24 |
|---|---|---|---|
| Opening balance | 897.48 | 553.00 | 403.35 |
| **Add: Options granted during the year (Refer note no. 38)** | **926.50** | **512.39** | **193.50** |
| **Less: Options exercised during the year** | **(179.62)** | **(167.91)** | – |
| **Less: Options surrendered during the year** | — | – | **(43.85)** |
| **Closing balance** | **1,644.36** | **897.48** | **553.00** |

| (iv) Items of Other Comprehensive Income | FY26 | FY25 | FY24 |
|---|---|---|---|
| Opening balance | 5.72 | 13.82 | 4.05 |
| Actuarial loss on remeasurement of employee defined benefit plan (net of tax) | (0.23) | (8.10) | 9.77 |
| **Closing balance** | **5.49** | **5.72** | **13.82** |
| **Total other equity** | **18,031.85** | **8,836.88** | **3,462.76** ← *printed 3,462.76 at the foot of AR FY25 Note 19 vs 3,462.77 at its head; §9, A-20* |

*Bridge to the SOCIE (DERIVED, arithmetic inline): "Premium received on issue of shares (net of expenses)"
in the SOCIE = 8,440.59 − 413.37 = **8,027.22** ✔ (FY25: 7,235.70 − 21.61 = 7,214.09 ✔).
"Options granted during the year (net of exercised)" = 926.50 − 179.62 = **746.88** ✔ (FY25: 512.39 −
167.91 = 344.48 ✔).*

*Bridge to the cash-flow financing line (DERIVED): premium received 8,440.59 + face value of shares issued
16.77 − share issue expenses 413.37 − non-cash ESOP-reserve transfer 179.62 = **7,864.37** = the cash-flow
line *"Proceeds from issue of equity shares (net of IPO expenses)"* ✔ exact. The same bridge does not close
on FY25: 7,235.70 + 12.80 − 21.61 − 167.91 = 7,058.98 vs cash-flow equity + preference proceeds of
1,092.97 + 5,978.39 = 7,071.36, **residual 12.38 unexplained** from the disclosed lines.*

**Nature and purpose paragraphs, verbatim (both years, both bases, unchanged):** Securities Premium —
*"…available for utilisation in accordance with the provisions of the Companies Act, 2013"*; Employee Stock
Options Reserves — *"The amounts recorded in this account are **transferred to share premium upon exercise**
of share options by employees. **In case of lapse, corresponding balance is transferred to retained
earnings**."* `[AR FY26, SA Note 17, p201/pr222]`

### 5.24 ESOP note — granted / exercised / lapsed / outstanding and the fair-value assumptions

SA `[AR FY26, SA Note 38, p218–219/pr239–240]`; FY24 `[AR FY25, SA Note 40, p147–148/pr142–143]`

**Scheme history, verbatim (FY26):** *"The ESOP scheme, named BlueStone Jewellery and Lifestyle Employees
Stock Option Plan – 2014 ("ESOP 2014"), was initially approved by shareholders in 2014. It was subsequently
amended and approved again in **2016**, further revised and approved during an extraordinary general
meeting in **2022**, further amended and approved by shareholders in **August 2024**, and most recently
amended and approved in **May 2025**."* `[AR FY26, SA Note 38, p218/pr239]`
*"The vesting period for these options spans from **1 to 7 years**. They can be exercised by the grantee
within a period of **10 years from the date of vesting**."*

**Options outstanding roll-forward** — note the company deducts VESTED options from "outstanding", so
"Outstanding at the end of the year" means **unvested** options:

| Line, as printed | FY2026 | FY2025 | **FY2024** |
|---|---|---|---|
| Outstanding at the beginning of the year | 35,48,669 | 24,46,853 | 18,94,796 |
| **Options granted during the year** | **16,47,192** | **20,56,016** | **13,43,506** |
| Options vested during the year | (11,18,933) | (9,03,797) | (7,74,012) |
| **Options lapsed during the year** | **(1,55,327)** | **(50,403)** | **(17,437)** |
| **Outstanding at the end of the year** | **39,21,601** | **35,48,669** | **24,46,853** |
| Weighted average exercise price per option (₹) | **1.00** | 1.00 | 1.00 |

*Tie-out ✔ 35,48,669 + 16,47,192 − 11,18,933 − 1,55,327 = 39,21,601.*

**Reconciliation of vested options**

| Line, as printed | FY2026 | FY2025 | **FY2024** |
|---|---|---|---|
| Outstanding at the beginning of the year | 23,76,602 | 29,81,752 | 26,62,775 |
| Options vested during the year | 11,18,933 | 9,03,797 | 7,74,012 |
| **Options exercised/modified during the year** | **(9,71,100)** | **(15,08,947)** | **(4,55,035)** |
| **Options expired during the year** | **(12,171)** | – | *(line absent)* |
| **Outstanding at the end of the year** | **25,12,264** | **23,76,602** | **29,81,752** |
| Options exercisable at the end of the year | 25,12,264 | 23,76,602 | 29,81,752 |

**FY2024 cash-settlement footnote, verbatim** `[AR FY25, SA Note 40, p148/pr143]`:
> *"During the previous year ended 31 March 2024, few employees requested to settle their rights to exercise
> the options in cash and the Company has accepted their request and settle their dues in cash instead of
> shares. The company had settled dues based on the fair value derived during the issue of series G CCPS.
> **The incremental impact due to cash settlement is ` 218.51 per option.**"*
The matching cash outflow is *"Settlement of cash settled ESOP liability (117.96)"* in FY24 financing
`[AR FY25, SA Cash Flows, p101/pr96]` and the liability *"Liabilities towards share based payment"* 24.87
at 31-Mar-2024, nil at 31-Mar-2025 `[AR FY25, SA Note 22, p135/pr130]`.

**Black-Scholes-Merton inputs**

| Input, as printed | FY2026 | FY2025 | **FY2024** |
|---|---|---|---|
| No. of options granted | 16,47,192 | 20,56,016 | 13,43,506 |
| **Date of grant** | 09-Apr-25, 05-May-25 | 17-May-24, 04-Jun-24, 01-Aug-24, 27-Sep-24, 27-Nov-24 | 01-Apr-2023, 03-Apr-2023, 26-Sep-2023, 01-Jan-2024, 02-Mar-2024 |
| Vesting Period | 4 years | 4 to 7 years | 4 years |
| Dividend yield | 0% | 0% | 0% |
| **Volatility rate** | **41.67%** | 41.57% | 46.53% |
| Risk free rate | 6.77% | 6.44% | 7.18% |
| Expected life of options | 4 years | 4 to 7 years | 4 |
| **Weighted average fair value of option per share (₹)** | **557.43** | **540.29** | **313.89** |
| Weighted average remaining contractual life of options outstanding | **3.14 years** | 3.61 years | 2.98 years |

**The stock-price input, verbatim — unchanged in the FY2026 report even though the shares listed on
19-Aug-2025:** *"**The stock price is arrived using the last round of funding closest to the grant date.**
Implied volatility is the unit at which the price of shares of **peer listed companies** has fluctuated
during the past period. The expected time to maturity/expected life of options is the period for which the
company expects the options to be alive, which has been taken as 4 to 7 years subject to adjustment of time
lapse from the date of grant. The risk free rate considered for calculation is based on yield on government
securities for 4 years as on date of valuation."* `[AR FY26, SA Note 38, p219/pr240]`
*(Both FY26 grant dates — 09-Apr-2025 and 05-May-2025 — precede the 19-Aug-2025 listing.)*
> **NOT DISCLOSED — the exercise price per option beyond the ₹1.00 weighted average, the grant-date share
> price used, the SBEB Reg 14 scheme-wise table (options in force, money realised, employee-wise grants to
> senior management / >1% grantees).** → would be answered by the **Board's Report ESOP annexure and the
> secretarial auditor's SBEB Reg 13 certificate** `[AR FY26, p121/pr142]`, which are outside this slice.

**ESOP charge, three values in FY26 (recorded, not reconciled):**

| Where | FY26 | FY25 | Tag |
|---|---|---|---|
| Employee benefits expense note | **926.50** | 512.39 | `[AR FY26, SA Note 29, p209/pr230]` |
| Cash-flow add-back | **926.51** | 512.39 | `[AR FY26, SA Cash Flows, p166/pr187]` |
| Other-equity ESOP reserve — options granted | **926.50** | 512.39 | `[AR FY26, SA Note 17(iii), p201/pr222]` |
| Consolidated employee benefits expense | **926.67** | 512.39 | `[AR FY26, CFS Note 31, p289/pr310]` |
| Consolidated cash-flow add-back | **926.67** | 512.39 | `[AR FY26, CFS Cash Flows, p245/pr266]` |

### 5.25 Earnings per share note

SA `[AR FY26, SA Note 36, p217–218/pr238–239]` · CFS `[AR FY26, CFS Note 38, p298/pr319]` ·
FY24 `[AR FY25, SA Note 38, p147/pr142]`

| Line, as printed | SA FY26 | SA FY25 | CFS FY26 | CFS FY25 | SA FY24 |
|---|---|---|---|---|---|
| **Profit/(Loss) after tax for calculating basic and diluted EPS** | **260.00** | (2,192.14) | **148.37** | (2,216.69) | (1,422.36) |
| Weighted average number of shares (for basic) | 11,95,35,383 | 2,77,99,051 | 11,95,35,383 | 2,77,99,051 | 1,81,51,940 |
| Weighted average number of shares (for diluted) | 12,57,93,939 | 2,77,99,051 | 12,57,93,939 | 2,77,99,051 | 1,81,51,940 |
| **Adjustments for employee share options** | **62,58,556** | – | 62,58,556 | – | — |
| **EPS — Basic (Rupees/share)** | **2.18** | (78.86) | **1.10** | (79.74) | (78.36) |
| **EPS — Diluted (Rupees/share)** | **2.07** | (78.86) | **1.05** | (79.74) | (78.36) |

Verbatim note (both bases, FY26): *"The impact of potential conversion of preference shares and ESOP into
equity is anti-dilutive in nature for the previous year ended 31 March 2025 and accordingly, the basic and
diluted loss per share are same."*

> **CHECK (code-run, §4a trigger 5): standalone recomputes exactly — 260.00 ÷ 11,95,35,383 = ₹2.175 → 2.18 ✔;
> 260.00 ÷ 12,57,93,939 = ₹2.067 → 2.07 ✔. CONSOLIDATED DOES NOT — 148.37 ÷ 11,95,35,383 = ₹1.241, printed
> 1.10; 148.37 ÷ 12,57,93,939 = ₹1.180, printed 1.05. The printed values recompute from PROFIT FOR THE YEAR
> INCLUDING NCI: 131.79 ÷ 11,95,35,383 = ₹1.1025 → 1.10 ✔ and 131.79 ÷ 12,57,93,939 = ₹1.0477 → 1.05 ✔.
> The FY25 consolidated EPS used the owners' share correctly ((2,216.69) ÷ 2,77,99,051 = (79.74) ✔).
> See §9, A-01.**

### 5.26 Analytical ratios (the Companies Act / Schedule III ratios) — as printed, with the company's own methodology

**STANDALONE** `[AR FY26, SA Note 42, p226–227/pr247–248]` and `[AR FY25, SA Note 44, p155/pr150]`

| Ratio | Company's stated methodology | FY26 | FY25 | % change FY25→FY26 | FY24 | % change FY24→FY25 |
|---|---|---|---|---|---|---|
| a) Current Ratio | Current assets over current liabilities | 1.66 | 1.24 | 34% | 0.94 | 33% |
| b) Debt - Equity Ratio | Debt⁽⁴⁾ over total shareholders' equity | 0.92 | 1.67 | -45% | 2.46 | -32% |
| c) Debt Service Coverage Ratio | EBIT⁽¹⁾ over debt | 0.14 | (0.01) | NA | (0.00) | 54% |
| d) Return on Equity Ratio | PAT⁽³⁾ over total average equity | 1.90% | -34.05% | NA | -94.09% | 64% |
| e) Inventory Turnover Ratio | Cost of goods sold over average inventory | 0.65 | 0.83 | -22% | 1.09 | -24% |
| f) Trade receivables turnover ratio | Revenue from operations over average trade receivables | 372.59 | 443.48 | -16% | 735.86 | -40% |
| g) Trade payables turnover ratio | Net credit purchases⁽⁵⁾ over average trade payables | 11.03 | 7.82 | 41% | 7.28 | 7% |
| h) Net Capital Turnover Ratio | Revenue from operations over average working capital | 2.68 | 10.99 | -76% | (16.30) | 167% |
| i) Net Profit Ratio | Net profit over revenue | 1.07% | -12.38% | NA | -11.24% | -10% |
| j) Return on Capital Employed | PBIT⁽²⁾ over average capital employed⁽⁶⁾ | 11.20% | -0.95% | NA | -0.95% | 0% |
| k) Return on Investment | Profit before tax over total assets | 0.53% | -6.20% | NA | -5.80% | -7% |

**CONSOLIDATED** `[AR FY26, CFS Note 44, p307–308/pr328–329]` — different values, same eleven ratios:

| Ratio | CFS FY26 | CFS FY25 | % change |
|---|---|---|---|
| a) Current Ratio | 1.67 | 1.25 | 34% |
| b) Debt - Equity Ratio | 0.94 | 1.68 | -44% |
| c) Debt Service Coverage Ratio | 0.13 | (0.01) | NA |
| d) Return on Equity Ratio | 0.97% | -34.53% | NA |
| e) Inventory Turnover Ratio | 0.64 | 0.83 | -23% |
| f) Trade receivables turnover ratio | 370.60 | 443.48 | -16% |
| g) Trade payables turnover ratio | 10.77 | 7.82 | 38% |
| h) Net Capital Turnover Ratio | 2.62 | 10.48 | -75% |
| i) Net Profit Ratio | 0.54% | -12.53% | NA |
| j) Return on Capital Employed | 10.95% | -1.01% | NA |
| k) Return on Investment | 0.38% | -6.23% | NA |

**Footnote definitions, verbatim (identical on both bases and in both years):**
> *"1. EBIT - Earnings before interest and taxes. 2. PBIT - Profit before interest and taxes including other
> income. 3. PAT - Profit after taxes. 4. **Debt includes current and non-current lease liabilities.**
> 5. **Credit purchases means gross credit purchases after deducting purchase returns. Gross credit
> purchases includes other expenses.** 6. Capital employed refers to total shareholders' equity and debt."*

**Company's own variance explanations, verbatim (FY26 standalone):** Current ratio — *"Movement due to
increase in current assets during the year."* Debt-Equity — *"Movement due to increase in share capital
(fresh issue) during the year."* DSCR / RoE / Net profit ratio / RoCE / RoI — *"Movement due to
profitability during the current year"* / *"…increase in equity and profitability…"* / *"…increase in
revenue and profitability in current year"* / *"…profitability and increase in capital employed"* /
*"Movement on account of profitability."* Trade payables turnover — *"Movement on account of **decrease in
trade payables**."* Net capital turnover — *"Movement on account of increase in revenue and inventory."*
Inventory turnover and trade receivables turnover — *"NA - as the variance is less than 25%"*
(**stated for a −22% and a −16% move**). `[AR FY26, SA Note 42, p226–227/pr247–248]`

### 5.27 Capital management — the company's own adjusted net debt calculation

SA `[AR FY26, SA Note 41, p226/pr247]`; FY24 `[AR FY25, SA Note 43, p155/pr150]`;
CFS `[AR FY26, CFS Note 43, p307/pr328]`

| Line, as printed | SA 31-Mar-26 | SA 31-Mar-25 | CFS 31-Mar-26 | CFS 31-Mar-25 | 31-Mar-24 |
|---|---|---|---|---|---|
| Total borrowings | 7,443.23 | 7,286.18 | 7,443.23 | 7,286.18 | 4,304.26 |
| Less: Cash and cash equivalents | (960.81) | **(326.40)** | (1,075.24) | **(383.58)** | 591.35 |
| Less: Other bank balance and deposits with bank | (3,013.22) | **(788.76)** | (3,013.22) | (889.46) | 453.68 |
| **Adjusted net debt** | **3,469.20** | **6,171.02** | **3,354.77** | **6,013.14** | **3,259.23** |
| Total equity | 18,184.10 | 9,133.44 | 18,030.03 | 9,107.40 | 3,741.72 |
| **Adjusted net debt to adjusted equity ratio** | **0.19** | **0.68** | **0.19** | **0.66** | **0.87** |

**Definition, verbatim (FY26):** *"…adjusted net debt is defined as **total borrowings (current and
non-current) less cash and cash equivalents, other bank balances and deposits with bank unless marked for
GML collateral and bank guarantee**. Adjusted equity comprises all components of equity."*
`[AR FY26, SA Note 41, p226/pr247]`
**The AR FY2025 definition is materially different, verbatim:** *"…adjusted net debt is defined as **total
liabilities, including interest-bearing loans and borrowings** less cash and cash equivalents, other bank
balances and deposits with bank unless marked for GML collateral and bank guarantee."*
`[AR FY25, SA Note 43, p155/pr150]` — but the FY25 table is computed on **total borrowings 7,286.18**, not
total liabilities 26,212.73. §9, A-21.
*Note the FY25 cash deduction of 326.40 is smaller than the balance-sheet cash of 430.57 — the GML-marked
portion (₹104.17 mn per Note 14/16) is excluded. 430.57 − 104.17 = 326.40 ✔ (DERIVED).*

### 5.28 Segment reporting

| Item | FY2026 | FY2025 |
|---|---|---|
| Segment statement, verbatim | *"The Company is engaged in design, manufacture and sale of jewellery, which constitutes a **single segment**. Accordingly, there are no separate reportable primary segments."* `[AR FY26, SA Note 44, p228/pr249]` | Same `[AR FY25, SA Note 46, p156/pr151]` |
| CODM | *"the Chief Operating Decision Maker"* is defined in policy Note 2.2.16 as the **Managing Director** `[AR FY26, SA Note 2.2.16, p179/pr200]` | Note 2.17 `[AR FY25]` |
| Revenue — **Domestic** | 24,412.30 (SA) · 24,364.24 (CFS) | 17,700.02 |
| Revenue — **Export** | **–** | **–** (FY24: –) |
| Non-current assets by geography | *"The entire non-current assets of the Company are located in India."* | same |

### 5.29 Other financial assets — the lien-marked deposit map (the security given for the gold-on-loan book)

SA `[AR FY26, SA Note 8, p187/pr208]`; FY24 `[AR FY25, SA Note 8, p118/pr113]`

| Line, as printed | SA 31-Mar-26 | SA 31-Mar-25 | CFS 31-Mar-26 | 31-Mar-24 |
|---|---|---|---|---|
| **Non-current** — Rental and other deposits | 617.54 | 503.35 | 637.82 | 366.37 |
| **Non-current** — Margin money deposits* | 0.11 | 0.05 | 0.11 | – |
| **Non-current** — Bank deposits with more than 12 months maturity# | 110.00 | 1,617.02 | 110.70 | 3,739.68 |
| **Total non-current** | **727.65** | **2,120.42** | **748.63** | **4,106.05** |
| **Current** — Rental and other deposits | 33.21 | 30.67 | 33.21 | 6.89 |
| **Current** — Interest accrued but not due on FDs with banks | 28.53 | 10.31 | 28.88 | 29.39 |
| **Current** — Bank deposits with maturity of less than 12 months* | 2,418.21 | 1,459.35 | 2,418.21 | 1,273.93 |
| **Current** — Margin money deposits** | 1.25 | 1.25 | 1.25 | 12.65 |
| **Current** — **Deposits with NBFC***** | 65.30 | 51.25 | 65.30 | 95.00 |
| **Current** — Margin money with brokers# | 99.60 | 31.64 | 99.60 | – |
| **Current** — **Call Option – Subsidiary (Refer note 50)** | **18.22** | **52.16** | 18.22 | – |
| **Current** — **Receivables from franchisee** | **238.96** | **290.52** | 238.96 | **768.90** |
| **Current** — Other receivables | 111.79 | 5.58 | 111.79 | 7.20 |
| **Total current** | **3,015.07** | **1,932.73** | **3,015.42** | **2,193.96** |

**Lien footnotes, verbatim (FY26 standalone):**
- non-current #: *"Includes deposits given as security against **gold on loan ₹ 50 million** (31 March 2025 -
  ₹ 1,429.00 million) and deposits given as security against **bank overdraft ₹ 60 million** (31 March 2025 -
  ₹ 128.02 million)."*
- current *: *"Includes deposits given as security against **gold on loan ₹ 30.32 million** (31 March 2025 -
  ₹ 939.86 million), marked as lien against **working capital loan ₹ Nil** (31 March 2025 - ₹ 126.00 million)
  and deposits given as security against **bank overdraft ₹ 1,866.64 million** (31 March 2025 - ₹ 256.25
  million)."*
- ***: *"Represent deposits given as security against **working capital loan ₹ 0.55 million** (31 March 2025 -
  ₹ 20.00 million), marked as lien against **term loan ₹ 20 million** (31 March 2025 - ₹ Nil), marked as lien
  against **Revolving Credit Facility (RCF) ₹ 44.75 million** (31 March 2025 - ₹ Nil) and **vendor financing
  ₹ Nil** (31 March 2025 - ₹ 31.25 million)."*
- #: *"Represent deposits maintained by the Company with brokers for hedging contracts."*

**Other bank balances** `[AR FY26, SA Note 15, p191/pr212]`

| Line, as printed | 31-Mar-26 | 31-Mar-25 | 31-Mar-24 |
|---|---|---|---|
| In bank deposits (original maturity >3 months but <12 months)* | 3,958.45 | 995.00 | 120.34 |
| Balances with banks held as margin money** | 83.01 | 346.18 | 353.27 |
| **Total** | **4,041.46** | **1,341.18** | **473.61** |

*: *"Includes deposits given as security against **gold on loan ₹ 3,458.42 million** (31 March 2025 -
₹ 965.00 million) and deposits given as security against bank overdraft ₹ 0.03 million (31 March 2025 -
₹ 30.00 million)."* **: *"Represents balance held as margin money against **gold on loan ₹ 83.01 million**
(31 March 2025 - ₹ 346.18 million)."*

**Cash and cash equivalents** `[AR FY26, SA Note 14, p190/pr211]`

| Line, as printed | 31-Mar-26 | 31-Mar-25 | 31-Mar-24 |
|---|---|---|---|
| Cash on hand | 1.82 | 0.02 | 0.83 |
| **Demand drafts on hand** | *(line absent)* | *(line absent)* | **3.89** |
| Balances with banks - in current accounts | 608.99 | 76.38 | 585.98 |
| Balances with banks - in bank deposits (original maturity 3 months or less)# | 350.00 | 354.17 | 0.65 |
| **Total cash and cash equivalents** | **960.81** | **430.57** | **591.35** |

#: *"Includes deposits given as security against gold on loan **₹ Nil** (31 March 2025 - ₹ 104.17 million)."*

### 5.30 Other financial liabilities (liability side) — the franchisee deposit book

SA `[AR FY26, SA Note 20, p203/pr224]`; FY24 `[AR FY25, SA Note 22, p134–135/pr129–130]`

| Line, as printed | SA 31-Mar-26 | SA 31-Mar-25 | 31-Mar-24 |
|---|---|---|---|
| **Non-current** — Deposit received from franchisee *(FY25 label: "Deposit made by franchisee")* | 30.82 | 143.31 | 325.10 |
| **Current** — Interest accrued but not due on borrowings | 15.43 | 14.43 | 12.61 |
| **Current** — **Deposit received from franchisee** | **2,030.52** | **2,118.37** | **2,466.15** |
| **Current** — Payable to employees | 143.56 | 92.05 | 24.45 |
| **Current** — **Liabilities towards share based payment (Refer note no. 40)** | *(absent)* | – | **24.87** |
| **Current** — **Liabilities towards rights to subscribe shares (Refer note no. 48)** | *(absent)* | – | **166.99** |
| **Current** — **Liability towards Phantom options (Refer note no. 47)** | *(absent)* | – | **7.53** |
| **Current** — Derivative instruments in designated hedge accounting relationship | 78.94 | 77.78 | – |
| **Current** — Other liabilities | 152.43 | 46.16 | 10.00 |
| **Total current** | **2,420.88** | **2,348.79** | **2,712.60** |

*The franchisee deposit is the counterpart of "Interest on Franchisee deposit" of ₹387.01 mn in FY26 finance
costs (§5.6) and of "Receivables from franchisee" of ₹238.96 mn in other financial assets (§5.29).*

### 5.31 Non-current investments (standalone) and equity-method investment (consolidated)

**Standalone** `[AR FY26, SA Note 7, p186–187/pr207–208]`; FY24/FY25 `[AR FY25, SA Note 7, p117/pr112]`

| Line, as printed | 31-Mar-26 | 31-Mar-25 | 31-Mar-24 |
|---|---|---|---|
| **Equity instruments (Unquoted, at cost)** — In Subsidiary: 100 fully paid equity shares of ₹10 each in **Ethereal House Private Limited** | 0.27 | 0.27 | – |
| **Equity instruments** — In Associate: 100 fully paid equity shares of ₹1 each in **Redefine Fashion Private Limited** | 0.06 | 0.06 | – |
| **CCPS (Unquoted, at cost)** — In Subsidiary: **1,53,739** fully paid CCPS of ₹10 each in Ethereal House (PY 61,567) | **419.71** | 167.71 | – |
| **CCPS** — In Associate: 1,70,526 fully paid CCPS of ₹1 each in Redefine Fashion | 104.94 | 104.94 | – |
| **Total** | **524.98** | **272.98** | **–** |
| Aggregate book value / market value of quoted investments | – / – | – / – | – / – |
| Aggregate value of unquoted investments | 524.98 | 272.98 | – |
| **Aggregate amount of impairment in value of investments** | **–** | **–** | **–** |

*AR FY2025 labels this class **"INVESTMENT IN CUMULATIVE CONVERTIBLE PREFERENCE SHARES (CCPS)"**
`[AR FY25, SA Note 7, p117/pr112]`, AR FY2026 labels the same instruments **"COMPULSORY CONVERTIBLE
PREFERENCE SHARES (CCPS)"** `[AR FY26, SA Note 7, p186/pr207]` — §9, A-22.*

**Consolidated — Investments accounted for using the equity method** `[AR FY26, CFS Note 7, p266/pr287]`

| Line, as printed | 31-Mar-26 | 31-Mar-25 |
|---|---|---|
| 100 fully paid equity shares of ₹1 each in Redefine Fashion Private Limited | 0.06 | 0.06 |
| **1,70,526 fully paid CCPS of ₹1 each in Redefine Fashion Private Limited** | **85.50** | **104.94** |
| **Total** | **85.56** | **105.00** |
| **Less: Share of loss of Associate (Refer note 50)** | **(55.52)** | **(19.44)** |
| **Total** | **30.04** | **85.56** |

*The CCPS "cost" line is restated from 104.94 to 85.50 between the two columns with no movement line —
recorded as printed. §9, A-23.*

**Current investments (mutual funds)** `[AR FY26, SA Note 12, p189/pr210]`

| Line, as printed | 31-Mar-26 | 31-Mar-25 |
|---|---|---|
| Axis Money Market Fund (2,74,946.69 units)* (PY 3,59,017.399 units) | 415.77 | 508.35 |
| TATA Money Market fund (4,042.45 units)* (PY Nil) | 20.37 | – |
| **Total** | **436.14** | **508.35** |

*: *"A total of **278,989.14 units have been pledged against hedging activities** (31 March 2025: 344,174.00
units)."* Aggregate amount and market value of quoted investments both 436.14 / 508.35.

### 5.32 Other assets (non-financial)

`[AR FY26, SA Note 10, p188/pr209]`; FY24 `[AR FY25, SA Note 11, p119/pr114]`

| Line, as printed | SA 31-Mar-26 | SA 31-Mar-25 | CFS 31-Mar-26 | 31-Mar-24 |
|---|---|---|---|---|
| **Non-current** — Balance with Government authorities | 1,701.17 | 1,234.92 | 1,717.02 | 747.34 |
| **Non-current** — Capital advances | 31.19 | 34.16 | 33.32 | 76.82 |
| **Non-current** — Goods and service tax refund receivables | – | 246.52 | – | 177.61 |
| **Non-current** — *Advance paid to BlueStone Trust* / *Less: Adjustment for Treasury Shares* | *(absent)* | *(absent)* | *(absent)* | **1.24 / (1.24)** |
| **Total non-current** | **1,732.36** | **1,515.60** | **1,750.34** | **1,001.77** |
| **Current** — Advance to suppliers | 65.52 | 58.12 | 76.38 | 62.36 |
| **Current** — Right to recover returned goods | 66.56 | 67.67 | 66.56 | 38.76 |
| **Current** — Prepaid expenses* | 86.92 | 203.53 | 87.07 | 50.66 |
| **Current** — Other receivables | 18.91 | 15.28 | 19.50 | 26.54 |
| **Total current** | **237.91** | **344.60** | **249.51** | **178.32** |

**FY26 prepaid footnote, verbatim:** *"The Company has successfully completed its initial public offer ('IPO')
of equity shares during the year. **IPO related expenses incurred in the previous year aggregating to
₹ 117.08 million were adjusted against the securities premium account** in accordance with Section 52 of the
Companies Act, 2013 upon completion of the issue. Accordingly, there are no unamortized or prepaid IPO
expenses outstanding as at the reporting date."* `[AR FY26, SA Note 10, p188/pr209]`
**FY25 footnote, verbatim:** *"The Company is in the process of launching its initial public offer ('IPO') …
filed its draft offer documents with the Securities and Exchange Board of India ('SEBI') on **11 December
2024**, and has incurred ` 117.08 million (31 March 2024: ` Nil) in connection with the said public offer."*
`[AR FY25, SA Note 11, p119/pr114]`

### 5.33 IPO completion and utilisation of proceeds (a note, transcribed here as it is a break-up)

SA `[AR FY26, SA Note 53, p230–231/pr251–252]` · CFS `[AR FY26, CFS Note 56, p312–313/pr333–334]`
(identical text and table on both bases).

**Verbatim:** *"During the current financial year, the Company has completed its Initial Public Offe ("IPO")
of **29,799,798 equity shares of face value of ₹ 1 each** comprising of fresh issue of **15,860,735 equity
shares at an issue price of ₹ 517 per equity share aggregating to ₹ 8,200 million** and an offer for sale of
**13,939,063 equity shares at an issue price of ₹ 517 per equity share aggregating to ₹ 7406.50 million**.
Pursuant to IPO, equity shares of the Company were listed on BSE Limited and National Stock Exchange
**w.e.f. 19 August 2025**. The Company has received an amount of **₹ 7,707.49 million (net of IPO expenses of
₹ 492.51 million)** from proceeds out of fresh issue of equity shares. **The IPO expenses incurred of
₹ 413.38 million has been adjusted against securities premium.**"*

> **The offer-for-sale figure does not compute: 13,939,063 × ₹517 = ₹7,206.50 mn, not ₹7,406.50 mn
> (code-run). Fresh issue does: 15,860,735 × ₹517 = ₹8,200.00 mn ✔. See §9, A-24.**

**Utilisation table (₹ million)**

| Objects of issue as per prospectus | Amount as proposed in the Offer Document | Amount utilized up to 31 March 2026 | Total unutilised amount as on 31 March 2026 |
|---|---|---|---|
| Working capital requirement | 7,500.00 | 7,256.50 | 243.50 |
| General corporate purpose | 207.50 | 150.00 | 57.50 |
| Issue expenses | 492.50 | 227.20 | 265.30 |
| **Total** | **8,200.00** | **7,633.70** | **566.30** |

*Tie-outs ✔ (7,256.50 + 150.00 + 227.20 = 7,633.70; 243.50 + 57.50 + 265.30 = 566.30; 7,633.70 + 566.30 =
8,200.00). Verbatim: "Out of the net proceeds which were unutilised as at 31 March 2026, **₹ 500 million
are temporarily invested in fixed deposits and ₹ 66.30 million is held in the Company's public account**."*
*The note states IPO expenses of ₹492.51 mn deducted from proceeds, ₹492.50 mn proposed, ₹413.38 mn
adjusted against securities premium and ₹227.20 mn utilised — four different numbers for the same object.
Recorded, not reconciled.*

### 5.34 Promoter contribution, and other notes with a number

| Note | Verbatim | Tag |
|---|---|---|
| **Promoter contribution** | *"Securities premium includes **₹ 76.83 million** contributed by the Promoter of the Company towards the **'Promoter contribution shortfall amount'** in compliance with Regulation 15 of the SEBI (Issue of Capital and Disclosure Requirements) Regulations."* | `[AR FY26, SA Note 45, p228/pr249]`; identical `[AR FY26, CFS Note 47, p309/pr330]` |
| **Fair value of contingent call options** | Shareholders' Agreement dated **06 January 2025** with Ethereal House; *"linked to the achievement or non-achievement of specific **revenue and EBITDA milestones**"*; *"determined using a **Monte Carlo Simulation** technique, based on projected revenues, EBITDA margins, and net asset values … **volatility based on comparable listed companies**, and risk-free interest rates as published by **FIMMDA**"*; *"contingent rights triggered **only upon non-achievement conditions**"*; fair value **₹ 18.22 million (31 March 2025: ₹ 52.16 million)** | `[AR FY26, SA Note 50, p230/pr251]` |
| **Investment in subsidiary (FY26)** | *"…the Company had acquired **92,172 fully paid compulsory convertible preference shares of ₹ 10 each** of Ethereal House Private Limited (EHPL) on a **premium of ₹ 2,724 per share** aggregating to total consideration of **₹ 252.00 million** on a preferential basis pursuant to the Shares Subscription Agreement dated 06 January 2025"* | `[AR FY26, SA Note 51, p230/pr251]` |
| **Investment in subsidiary and associate (FY25)** | EHPL: 100 equity shares of ₹10 + **61,567 CCPS of ₹10 at a premium of ₹ 2,714 per share**, total **₹ 167.98 million**, SSA 06-Jan-2025. Redefine Fashion: 100 equity shares of ₹1 + **1,70,526 CCPS of ₹1 at a premium of ₹ 614.38 per share**, total **₹ 105.00 million**, SSA 11-Nov-2024 | `[AR FY25, SA Note 55, p158–159/pr153–154]` |
| **The Code on Social Security, 2020** | Four Labour Codes notified **21 November 2025**; *"The incremental impact, amounting to **₹ 4.15 million** relating to gratuity and long-term compensated absences, primarily arises from the revised definition of wages."* | `[AR FY26, SA Note 54, p231/pr252]`; identical `[AR FY26, CFS Note 57, p313/pr334]`. **No such note exists in AR FY2025.** |
| **Phantom Option Scheme 2016** *(FY25 only)* | POS 2016 approved FY2016-17; **109,715 options** granted to former employees and non-employee associates; settled for cash at a **liquidation price of ₹ 2,453.55 per option**; *"during the year ended 31 March 2024, the Company had paid **₹ 261.55 million** and the balance amount is paid by the company during the year ended 31 March 2025"* | `[AR FY25, SA Note 47, p156/pr151]`. **Absent from AR FY2026.** |
| **InnoVen right to subscribe (RTS)** *(FY25 only)* | InnoVen Capital India Private Limited had **right to subscribe 64,967 shares**; *"The Company and InnoVen has mutually decided to terminate the RTS agreement against the settlement amount of **₹ 154.62 million**"*; discharged during FY2024 | `[AR FY25, SA Note 48, p157/pr152]`. **Absent from AR FY2026.** |
| **Events after the reporting period** | FY26: *"…evaluated all events or transactions that occurred after 31 March 2026 up through **23 April 2026** … **not aware of any events or transactions that would require recognition or disclosure**."* FY25: same wording through **24 April 2025** | `[AR FY26, SA Note 52, p230/pr251]`; `[AR FY25, SA Note 56, p159/pr154]` |
| **Relationship with struck-off companies — FY26 and FY25** | *"There are no transactions with the struck off companies during the year…"* | `[AR FY26, SA Note 43, p228/pr249]`; `[AR FY25, SA Note 45, p156/pr151]` |
| **Relationship with struck-off companies — FY24** | **Sausha R&D Private Limited**, Payable, balance **0.60**, relationship Nil; **Nova Technosys Private Limited**, Payable, balance **0.03**, relationship Nil. Notes: *"During the financial year 2023-2024, the Company made purchases of ` 0.05 million, which was settled during the year and the opening balance remains outstanding as at year end."* / *"There were no transactions made during the financial year 2023-2024, the opening balance remains outstanding as at year end."* | `[AR FY25, SA Note 45, p156/pr151]` |
| **CSR** | *"Since the Company has not made net profits during the three immediately preceding financial years, the Company is not required to spend any amount as prescribed under section 135(5) of the Act."* — **nil spend, both years, both bases** | `[AR FY26, SA Note 37, p218/pr239]`; `[AR FY25, SA Note 39, p147/pr142]` |

### 5.35 Related party disclosures (transcribed because it carries the Section 188 / KMP break-up)

`[AR FY26, SA Note 35, p214–217/pr235–238]`; `[AR FY25, SA Note 37, p144–146/pr139–141]`

**A. Relationship list, FY2026 as printed**

| Category | Names |
|---|---|
| Key Management Personnel (KMP) | Mr. Gaurav Singh Kushwaha, Managing Director · Mr. Rumit Dugar, CFO · **Ms. Jasmeet Saluja, Company Secretary (upto 30 April 2025)** · Mr. Vipin Sharma, Chief Merchandising Officer · Mr. Sudeep Nagar, Chief Operating Officer · **Mr. Paras Dilip Shah, Company Secretary (w.e.f. 4 July 2025)** |
| Non executive - Nominee Directors | Mr. Prashanth Prakash · Mr. Sameer Dilip Nath · **Mr. Vikram Gupta (upto 27 November 2024)** |
| Non executive - Independent Directors | Mr. Rajesh Kumar Dahiya (w.e.f. 16 August 2024) · Mr. Rohit Bhasin (w.e.f. 16 August 2024) · Ms. Neha (w.e.f. 16 August 2024) |
| Subsidiary | Ethereal House Private Limited |
| Associate | Redefine Fashion Private Limited |
| **B. Other related parties with whom transactions have taken place** | Mrs. Arpita Tomar (Relative of KMP) · Mrs. Poonam Dugar (Relative of KMP) · Mrs. Duhita Nath (Relative of Director) · Mrs. Shikha Parikh (Relative of KMP) · Ms. Mallika Dahiya (Relative of Director) |

*(AR FY25 list adds **Ms. Roopa Hegde, Company Secretary (upto 14 April 2023)** and shows Ms. Jasmeet Saluja
**w.e.f. 19 March 2024** `[AR FY25, SA Note 37, p144/pr139]`.)*

**(ii) Related party transactions, ₹ million**

| Transaction, as printed | FY2026 | FY2025 |
|---|---|---|
| **Remuneration paid/accrued — Mr. Gaurav Singh Kushwaha** | **94.21** | **30.83** |
| Remuneration — Mr. Rumit Dugar | 16.87 | 14.79 |
| Remuneration — Mr. Vipin Sharma | 16.01 | 13.24 |
| Remuneration — Mr. Sudeep Nagar | 16.59 | 13.87 |
| Remuneration — Ms. Jasmeet Saluja | 0.13 | 1.75 |
| Remuneration — Mr. Rajesh Kumar Dahiya | 1.60 | 1.70 |
| Remuneration — Mr. Rohit Bhasin | 1.80 | 1.75 |
| Remuneration — Ms. Neha | 2.15 | 1.80 |
| Remuneration — Mr. Paras Dilip Shah | 2.23 | – |
| Sitting fees — Mr. Rajesh Kumar Dahiya | 2.00 | 0.55 |
| Sitting fees — Mr. Rohit Bhasin | 1.80 | 0.50 |
| Sitting fees — Ms. Neha | 1.45 | 0.45 |
| **Equity shares issued under Rights issue — Gaurav Singh Kushwaha** | – | **313.31** |
| **Equity shares issued under private placement — Gaurav Singh Kushwaha** | – | **751.40** |
| **The Promoter Contribution Shortfall — Gaurav Singh Kushwaha** | **76.83** | – |
| ESOP exercised* — Mr. Rumit Dugar | – | 61.22 |
| **ESOP exercised* — Mr. Vipin Sharma** | **127.98** | 40.39 |
| ESOP exercised* — Mr. Sudeep Nagar | 22.41 | 53.49 |
| Sale of products — Mr. Vikram Gupta | – | 0.01 |
| Sale of products — Mr. Vipin Sharma | 0.07 | 0.13 |
| Sale of products — Mr. Sudeep Nagar | 0.01 | 0.17 |
| Sale of products — Mrs. Arpita Tomar | 0.92 | 3.83 |
| Sale of products — Mrs. Poonam Dugar | 0.08 | 0.05 |
| Sale of products — Ms. Neha | 0.37 | 0.09 |
| Sale of products — Ms. Mallika Dahiya | – | 0.27 |
| Sale of products — Mrs. Duhita Nath | – | 3.19 |
| Sale of products — Mrs. Shikha Parikh | 2.69 | 1.78 |
| **Sale of products — Ethereal House Private Limited** | **111.22** | **–** |
| **Sale of fixed assets — Ethereal House Private Limited** | **0.71** | – |
| Reimbursement of expenses — Ethereal House Private Limited | 0.04 | – |
| **Investment in Subsidiary — Ethereal House: Equity shares / CCPS** | – / **252.00** | 0.27 / 167.71 |
| **Investment in Associate — Redefine Fashion: Equity shares / CCPS** | – / – | 0.06 / 104.94 |

**(iii) Amounts outstanding at the balance sheet date, ₹ million**

| Line, as printed | 31-Mar-2026 | 31-Mar-2025 |
|---|---|---|
| **Payables to KMP — Mr. Gaurav Singh Kushwaha** | **63.60** | 3.60 |
| Payables — Mr. Rumit Dugar | 1.36 | 0.96 |
| Payables — Mr. Vipin Sharma | 1.36 | 0.96 |
| Payables — Mr. Sudeep Nagar | 1.36 | 0.96 |
| Payables — Ms. Jasmeet Saluja | – | 0.09 |
| Payables — Mr. Rajesh Kumar Dahiya | 0.40 | – |
| Payables — Mr. Rohit Bhasin | 0.45 | – |
| Payables — Ms. Neha | 0.60 | – |
| **Receivables from Directors — Mrs. Duhita Nath** | **–** | **3.19** |

Footnotes, verbatim `[AR FY26, SA Note 35, p217/pr238]`:
> *"`*`ESOP exercised represents taxable amount."*
> *"(i) **Mr. Rumit Dugar, Chief Financial Officer, undertook a one-time test transaction by leasing gold
> through a platform. The value of the resulting related party transaction was only a few rupees and was
> immaterial in nature.**"*
> *"(ii) The Company has not written off or written back any related party balances."*
> *"(iii) Provisions for post-retirement benefits, namely gratuity and leave encashment, are made for the
> Company as a whole. The amount pertaining to Key management personnel has not been separately determined,
> accordingly, not included in the above note."*

*The consolidated related-party note `[AR FY26, CFS Note 37, p295–297/pr316–318]` drops the subsidiary
(eliminated) and keeps the associate and the KMP/relatives; the KMP remuneration figures are identical.*
