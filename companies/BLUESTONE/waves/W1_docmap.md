# W1 — Document map — BlueStone Jewellery and Lifestyle Ltd

**Assembled:** 2026-09-09 from four fresh-context mapping agents, one per source document.
Unit W1_docmap. Inputs: doctrine §7 wave 1, state/LOOP.md, data/source_register.md.

This file locates disclosure. It extracts no series and reaches no conclusion. Where a mapper
recorded something a later agent would be wrong to assume, it is kept verbatim in that mapper's
own section rather than summarised here.

| Part | Document | Pages | Section below |
|---|---|---|---|
| 1 | Annual Report FY2026 (reported, audited) | 314 | Part 1 |
| 2 | Annual Report FY2025 (reported, audited, pre-listing year) | 230 | Part 2 |
| 3 | Prospectus 14-Aug-2025 (restated FY23–FY25, offer facts) | 532 | Part 3 |
| 4 | 119 post-listing exchange filings | — | Part 4 |

---

# PART 1 — Annual Report FY2026

# W1 — Document map: BlueStone Annual Report FY2026 (audited, first full year as a listed company)

**Agent:** A2 Document Mapper (doctrine wave 1) · **Compiled:** 2026-09-09
**Source file:** `data/text/BLUESTONE-AR-FY2026.txt` (314 PDF pages, page-marked) · PDF `data/bronze/BLUESTONE-AR-FY2026.pdf`
**Status:** MAP ONLY. No financial series extracted (ledger agent's job). No interpretation. No chain records, no findings.

---

## 0. How to cite this document, and the unit rule

### 0a. Units — the exact wording that establishes scale

Every page of the financial statements carries a **printed header**, verbatim:

> **"(All amounts are in INR million unless otherwise stated)"**

It appears on the standalone Balance Sheet [AR FY26, p164/pr185], the standalone Statement of Profit and Loss
[AR FY26, p165/pr186], the standalone Cash Flow Statement [AR FY26, p166/pr187], the Statement of Changes in
Equity [AR FY26, p168-169/pr189-190], and on **every** page of the Notes to the Standalone Financial Statements
[AR FY26, p181-231/pr202-252] and Notes to the Consolidated Financial Statements [AR FY26, p261-313/pr282-334].
The policy note repeats it: *"The standalone financial statements are presented in Indian Rupee ("₹" or "INR"),
which is Company's functional and presentation currency and is **rounded-off to the nearest million** except when
otherwise indicated"* [AR FY26, Note 2.1(iii), p170/pr191]; identically for the Group [AR FY26, Note 2.1(iii)
consolidated, p249/pr270].

**Three scale traps in this one document — all live, all capable of a 10x–100x error:**

| Where | Unit actually used | Trap |
|---|---|---|
| Financial statements + all notes (PDF p164-231, p243-313) | **₹ million** | The default. |
| **Board's Report §1 financial summary** [AR FY26, p48/pr69] | ₹ millions — header reads *"₹ In millions (Except EPS)"* | Same basis as the statements. Safe. |
| **Board's Report §10 subsidiary/associate summaries** [AR FY26, p57-58/pr78-79] | ₹ million — *"(Amount in ₹ million)"* | Safe. |
| **Annexure-2 FORM AOC-1** [AR FY26, p79-80/pr100-101] | **₹ absolute rupees** — *"(Information in respect of each subsidiary to be presented amount in Rs)" / "(Amount in Rupees)"* | **TRAP.** Ethereal House "Turnover 6,31,40,000" is ₹63.14 mn, not ₹6,314 mn. Same figure appears as 63.14 in the Board's Report table. |
| **Corporate Governance Report — remuneration, sitting fees, audit fees** [AR FY26, p100-101/pr121-122; p114/pr135] | **₹ absolute rupees** — *"(Amount in Rupees)"* | **TRAP.** MD remuneration "₹ 3,38,54,004"; audit fee "₹ 50,00,000". |
| **Board's Report §8 share capital, §41 energy, §45 general disclosure** [AR FY26, p49-52/pr70-73; p71/pr92; p74/pr95] | ₹ absolute rupees, and **lakhs** in one place (*"approximately ₹41.30 lakhs"*, *"₹125.00 lakhs"*) [AR FY26, p71/pr92] | **TRAP.** Mixed within a single section. |
| **Chapters / KPI / Chairman pages** [AR FY26, p9, p24-26] | **₹ crore** and ₹ million, mixed on the same spread | *"₹ 2,441 CRORE"* [AR FY26, p9] vs *"24,412.30"* ₹ mn [AR FY26, p26]. Same number, two scales, nine pages apart. |

**Rule for every later agent: read the header of the page you are quoting from, not the section you think you are in.**

### 0b. PDF page ↔ printed page mapping (derived, not assumed)

| PDF page range | Printed page | Formula |
|---|---|---|
| p1–p2 | none (covering letter to BSE/NSE, 17-Aug-2026) | — |
| p3–p5 | none (cover, Corporate Information, Contents) | — |
| p6–p30 | printed **2–51**, **two printed pages per PDF page** (design spreads) | `printed = 2×PDF − 10` (e.g. p9 → printed 8-9; p26 → printed 42-43) |
| **p31–p313** | printed **52–334** | `printed = PDF + 21` |
| p314 | none (back cover) | — |

Cite as `[AR FY26, Note 25, p206/pr227]`. Where a note spans pages, the range is given in the tables below.

---

## 1. Structure table — every section with its PDF page range

| # | Section | PDF pages | Printed pages | Notes |
|---|---|---|---|---|
| 0 | Covering letter to BSE (544484) and NSE (BLUESTONE), dated 17-Aug-2026, submitting AR 2025-26 + AGM notice | p1–p2 | — | Confirms 15th AGM on Mon 14-Sep-2026, 4:30 pm IST, VC/OAVM |
| 1 | Cover — *"Designed to lead"* | p3 | — | |
| 2 | **Corporate Information** | p4 | — | Board, KMP, SMP, all 6 committees, statutory auditor, internal auditor (both, with change date), RTA, exchanges, 3 manufacturing units, 5 bankers |
| 3 | Contents / forward-looking statement / theme note | p5 | — | |
| 4 | **01 / Chapters of Our Craft and Growth** (unaudited management narrative) | **p6–p30** | 2–51 | See §5 below for the operating-metric locator |
| 4a | — About the Report (scope, boundary, board approval date) | p6 | 2–3 | Reporting scope is **standalone only** for this section; AR approved for issue by the Board **14-Aug-2026** |
| 4b | — Who We Are / transformational journey timeline | p7–p8 | 4–7 | |
| 4c | — **Highlights of the Year** | p9 | 8–9 | |
| 4d | — Board of Directors + Management Team biographies | p10–p11 | 10–13 | |
| 4e | — Presence (state-wise store map) | p12 | 14–15 | |
| 4f | — What Makes Us Different (7 numbered pillars) | p13–p23 | 16–37 | |
| 4g | — **Message from the Chairman** (incl. *"Where we got it wrong"*) | p24–p25 | 38–41 | |
| 4h | — **Key Performance Indicators** (4-year revenue / EBITDA / PAT / EBITDA-margin bars) | p26 | 42–43 | |
| 4i | — Growth Strategy ("BlueStone in FY30", six pillars) | p27–p28 | 44–47 | |
| 4j | — Corporate Governance overview + list of 19 board-adopted policies | p29–p30 | 48–51 | |
| 5 | **02 / Statutory Reports — Notice of the 15th AGM** | **p31–p47** | 52–68 | 3 ordinary items only; **no special resolution**; explanatory statement u/s 102 at p42/pr63; Annexure A (Amit Jain profile) p44–p45/pr65–66; Forms SH-13 / SH-14 p46–p47/pr67–68 |
| 6 | **Board's Report** (49 numbered paragraphs) | **p48–p75** | 69–96 | Signed Mumbai, 14-Aug-2026 by Gaurav Singh Kushwaha (MD) and Sameer Dilip Nath (Director) |
| 7 | **Annexure-1 — Dividend Distribution Policy** | p76–p78 | 97–99 | |
| 8 | **Annexure-2 — FORM AOC-1** (subsidiary Part A, associate Part B) | **p79–p80** | 100–101 | **In ₹ absolute rupees** |
| 9 | **Annexure-3 — FORM MR-3 Secretarial Audit Report** (+ its Annexure A limitation letter) | **p81–p84** | 102–105 | Mihen Halani & Associates, dated 23-Apr-2026, UDIN F009926H000184628 |
| 10 | **Annexure-4 — Annual Secretarial Compliance Report** (Reg 24A(2)) | **p85–p88** | 106–109 | 13-point compliance grid; UDIN F009926H000184584 |
| 11 | **Annexure-5 — CORPORATE GOVERNANCE REPORT** (sections I–XIX) | **p89–p118** | 110–139 | |
| 11a | — MD & CFO compliance certificate (Reg 17(8)) | p119 | 140 | Dated 23-Apr-2026 |
| 11b | — PCS certificate on Corporate Governance | p120 | 141 | UDIN F009926H000184551 |
| 11c | — Secretarial auditor certificate on ESOP scheme (Reg 13 SBEB) | p121 | 142 | UDIN F009926H000184463 |
| 12 | **Annexure-6 — Annual Report on CSR activities** | p122–p124 | 143–145 | Nil spend; average net profit negative |
| 13 | **Annexure-7 — Certificate of Non-Disqualification of Directors** | p125 | 146 | Lists all 6 directors + date of first appointment |
| 14 | **MANAGEMENT DISCUSSION AND ANALYSIS REPORT** | **p126–p149** | 147–170 | Divider p126; content p127–p149 |
| 14a | — Economic Outlook (global, India) | p127–p128 | 148–149 | IMF WEO Apr-2026 table |
| 14b | — Industry Outlook (Indian retail, e-commerce, jewellery market, omnichannel) | p129–p139 | 150–160 | **Sourced from a Redseer industry research report** [AR FY26, p139/pr160] |
| 14c | — Company Overview / Strengths | p140–p141 | 161–162 | |
| 14d | — **Performance Review (standalone AND consolidated tables) + Key Highlights** | **p142–p143** | 163–164 | |
| 14e | — Opportunities / Threats & Outlook | p144–p145 | 165–166 | |
| 14f | — **Significant changes in key financial ratios (≥25%)** | **p146** | 167 | Explicitly *"Basis standalone financials reporting"* |
| 14g | — Risks and Concerns (R1–R8) | p147 | 168 | |
| 14h | — Internal Control Systems and Adequacy | p148 | 169 | |
| 14i | — Human Resources | p148–p149 | 169–170 | |
| 15 | **03 / Financial Statements — Independent Auditor's Report, STANDALONE** | **p150–p163** | 171–184 | |
| 15a | — Opinion + Basis for Opinion | p150 | 171 | |
| 15b | — **Key Audit Matters (2)** | p150–p152 | 171–173 | |
| 15c | — Other information / Responsibilities | p152–p153 | 173–174 | |
| 15d | — **Report on Other Legal and Regulatory Requirements** (incl. the §143(3)(b) and Rule 11(g) modifications) | **p153–p155** | 174–176 | |
| 15e | — Annexure A: Auditor's responsibilities | p156–p157 | 177–178 | |
| 15f | — **Annexure B: CARO 2020** (clauses i–xxi) | **p158–p161** | 179–182 | |
| 15g | — Annexure C: Internal Financial Controls opinion | p162–p163 | 183–184 | |
| 16 | **STANDALONE Balance Sheet** | **p164** | 185 | |
| 17 | **STANDALONE Statement of Profit and Loss** | **p165** | 186 | |
| 18 | **STANDALONE Statement of Cash Flows** (+ financing-liability reconciliation) | **p166–p167** | 187–188 | |
| 19 | **STANDALONE Statement of Changes in Equity** (A share capital, B other equity) | **p168–p169** | 189–190 | |
| 20 | **Notes to the STANDALONE Financial Statements (Notes 1–55)** | **p170–p231** | 191–252 | Full locator at §2A |
| 21 | **Independent Auditor's Report, CONSOLIDATED** | **p232–p242** | 253–263 | |
| 21a | — Opinion + Basis + **Key Audit Matters (2)** | p232–p234 | 253–255 | |
| 21b | — Report on Other Legal and Regulatory Requirements (incl. **CARO summary table, para 3**) | **p235–p238** | 256–259 | |
| 21c | — Annexure A: Auditor's responsibilities | p239–p240 | 260–261 | |
| 21d | — Annexure B: Internal Financial Controls opinion (Group) | p241–p242 | 262–263 | |
| 22 | **CONSOLIDATED Balance Sheet** | **p243** | 264 | |
| 23 | **CONSOLIDATED Statement of Profit and Loss** | **p244** | 265 | |
| 24 | **CONSOLIDATED Statement of Cash Flows** (+ financing-liability reconciliation) | **p245–p246** | 266–267 | Page 245 is **mis-titled "Standalone Statement of Cash Flows"** — see §7 |
| 25 | **CONSOLIDATED Statement of Changes in Equity** (incl. NCI column) | **p247–p248** | 268–269 | |
| 26 | **Notes to the CONSOLIDATED Financial Statements (Notes 1–58)** | **p249–p313** | 270–334 | Full locator at §2B |
| 27 | Back cover | p314 | — | |

**Sections that DO NOT EXIST in this document:** BRSR (see §6), Business Responsibility Report, ESG/sustainability
report, a 5- or 10-year financial highlights table, a separate CARO annexure for the consolidated statements
(folded into para 3 of the consolidated auditor's report), and Form AOC-2 (Board's Report §29 states it is
"not applicable" [AR FY26, p67/pr88]).

---

## 2A. Note locator — NOTES TO THE **STANDALONE** FINANCIAL STATEMENTS (PDF p170–p231 / printed 191–252)

| Note | Title | PDF p / printed | What a later agent comes here for |
|---|---|---|---|
| 1 | General Information | p170/pr191 | Entity status, listing on NSE and BSE, business description |
| 2.1 | Basis of preparation; estimates, assumptions & judgements | p170–p171/pr191–192 | **Authorisation date of the FS: 23 April 2026.** Fair-value hierarchy definition. Operating cycle = 12 months. The list of nine estimation-uncertainty areas (incl. Note 50 call-option fair value) |
| 2.2.1 | PPE and depreciation | p171–p172/pr192–193 | **Useful-life table: management estimate vs Schedule II.** Leasehold improvements 5y (Sch II 5–10y); Vehicles 5y (Sch II 8y); Plant & machinery 15y (Sch II 10–15y). Capitalisation of borrowing cost |
| 2.2.2 | Other intangible assets and amortisation | p172–p173/pr193–194 | Application software 3y. Internally-generated / development-cost capitalisation criteria |
| 2.2.3 | Impairment of non-financial assets | p173/pr194 | CGU definition — relevant to store-level ROU and leasehold-improvement impairment testing |
| 2.2.4 | **Leases (Ind AS 116)** | p173–p174/pr194–195 | Judgement on lease term incl. anticipated renewals; incremental borrowing rate; short-term exemption; lease payments classified as **financing** cash flows |
| 2.2.5 | **Inventories** | p174/pr195 | Gold on FIFO; raw materials weighted average except solitaires (specific identification); **"Unfixed gold" valued at the provisional gold price on the closing date**; hedge-accounted gold excluded from lower-of-cost-or-NRV |
| 2.2.6 | Foreign currency transactions | p174/pr195 | |
| 2.2.7 | **Revenue recognition** | p174–p175/pr195–196 | **The KAM policy.** Three operating models (FOCO, COCO, online). Company is **principal**, franchisees are **agents**. Returns → refund liability + right-to-recover asset. Gift vouchers → liability, to other income on expiry |
| 2.2.8 | Employee benefits | p175/pr196 | Gratuity **unfunded**, Projected Unit Credit |
| 2.2.9 | **Share-based payments** | p176/pr197 | Black-Scholes; **graded vesting expensed on accelerated amortisation** — the mechanism behind the "front-loaded" ESOP charge management cites |
| 2.2.10 | **Financial instruments** (incl. derivatives / hedge accounting) | p176–p178/pr197–199 | CCPS/OCRPS classified FVTPL where they meet the Ind AS 32 liability definition. **Fair value hedge designation: derivative contracts against fixed gold inventory, AND borrowings under gold-on-loan ("unfixed gold") designated as a fair value hedge of the corresponding gold inventory** |
| 2.2.11 | Income tax | p178/pr199 | |
| 2.2.12 | Provisions | p178/pr199 | |
| 2.2.13 | **Contingent liabilities** | p178/pr199 | Policy only; the amount is in Note 46 |
| 2.2.14 | Cash and cash equivalents | p178/pr199 | |
| 2.2.15 | Cash flow statement | p178/pr199 | Indirect method |
| 2.2.16 | **Segment reporting** | p179/pr200 | **CODM = the Managing Director.** One segment (Jewellery), one geography (India) |
| 2.2.17 | Earnings per share | p179/pr200 | |
| 2.2.18 | **New and amended standards** | p179–p180/pr200–201 | (A) Ind AS 1 current/non-current + covenants adopted 1-Apr-2025, **stated to have no measurement effect, no retrospective adjustment**; (B) Ind AS 1 covenant-breach provisions effective 1-Apr-2026, **stated to have no expected impact** |
| **3** | **Property, plant and equipment** | **p181/pr202** | Full gross-block / depreciation / disposal roll-forward by 7 asset classes, both years. No impairment, no revaluation. Points to Note 46 for capital commitments |
| **4** | **Leases** | **p182–p183/pr203–204** | 4A ROU roll-forward (Building + Furniture & fixtures, new class in FY26); 4B lease-liability movement (opening, additions, termination, accretion, payments); current/non-current split; **undiscounted contractual maturities in 3 buckets**; 4C P&L expense (ROU depreciation, lease interest, short-term rent); total cash outflow for leases; **variable lease payments 1.00%–4.00% of net sales per store**; extension/termination option commentary |
| **5** | **Capital work-in-progress** | **p184/pr205** | CWIP movement (additions vs capitalised) and **ageing schedule**; explicit statement that no project is overdue or over cost |
| **6A** | Other intangible assets | p184–p185/pr205–206 | Application software only |
| **6B** | Intangible asset under development | p185–p186/pr206–207 | Movement + ageing; FY26 closing nil (written off — see cash-flow line) |
| **7** | **Investments (non-current)** | **p186–p187/pr207–208** | Investment in subsidiary Ethereal House (equity + CCPS) and associate Redefine Fashion (equity + CCPS), **at cost less impairment**. Quoted/unquoted aggregate values. Carried forward to p187 |
| **8** | **Other financial assets** (non-current and current) | **p187/pr208** | Rental deposits; margin money; **bank deposits and the footnotes showing exactly which deposits are lien-marked against gold-on-loan, bank overdraft, working-capital loan, term loan, RCF and vendor financing**; deposits with NBFCs; margin with brokers; **call option on subsidiary**; **receivables from franchisee** |
| **9** | Non-current tax assets (net) | p188/pr209 | |
| **10** | Other assets (non-current and current) | p188/pr209 | Balance with government authorities; capital advances; **right to recover returned goods**; prepaid expenses + the footnote confirming FY25 prepaid IPO expenses were adjusted to securities premium |
| **11** | **Inventories** | **p188/pr209** | Raw materials / WIP / finished goods / packing materials. Points to Note 18 for the charge over inventory |
| **12** | Investments — current | p189/pr210 | Two money-market mutual funds; **unit counts pledged against hedging activities** |
| **13** | **Trade receivables** | **p189–p190/pr210–211** | Balance + **ageing schedule for both years**, disputed/undisputed, ECL = nil. Points to Note 35 for director-related receivables |
| **14** | Cash and bank balances | p190/pr211 | Cash on hand, current accounts, ≤3-month deposits + gold-on-loan security footnote |
| **15** | Other bank balances | p191/pr212 | 3–12 month deposits + margin money, with gold-on-loan / overdraft security footnotes |
| **16** | **Share capital** | **p191–p200/pr212–221** | The single richest governance note. (a) reconciliation of equity shares and of **treasury shares**; (III) series-by-series CCPS roll-forward (A, B, B1, B2, B3, C, D, D1, D2, D3, E, E2, F, G, H); (b) rights; **(c) the CCPS→equity conversion ratios (10:1 for A–F, 5.01:1 for E2, 1:1 for G and H)**; (d) FY23 bonus issue; (g) FY25 rights issue at ₹34; **(h) the IPO: 1,58,60,735 shares at ₹517 (₹1 face + ₹516 premium)**; **(i) >5% shareholders for both years, equity and every CCPS series — the pre-IPO cap table**; (j) promoter shareholding |
| **17** | **Other equity** | **p200–p201/pr221–222** | Securities premium roll-forward (premium received, reclassification from liability, CCPS conversion, **share issue expenses**); retained earnings; **ESOP reserve roll-forward (granted / exercised)**; OCI. Nature-and-purpose paragraphs |
| **18** | **Borrowings** | **p201–p203/pr222–224** | **Non-current: redeemable NCDs, term loans from banks, term loans from financial institutions, vehicle loans, less current maturities.** Coupon ranges and tenors for each class. **Full security description (first-ranking pari passu charge over current AND non-current assets including intellectual property and brand/trademarks).** Current: working capital loan, bank overdraft, current maturities. **Stock-statement agreement confirmation. Explicit "no instances of default in payment of principal or interest"** |
| **19** | Lease liabilities | p203/pr224 | Current / non-current split only (movement is in Note 4B) |
| **20** | **Other financial liabilities** | **p203/pr224** | Interest accrued; **deposit received from franchisee (current + non-current)**; payable to employees; **derivative instruments in designated hedge accounting relationship** |
| **21** | Provisions | p204/pr225 | Gratuity + compensated absences, current and non-current |
| **22** | **Gold on loan** | **p204/pr225** | **The gold metal loan.** Interest 2.50%–6.50% p.a. (PY 2.50%–9.00%), monthly; **credit period up to 180 days from delivery**; secured against fixed deposits (cross-refs Notes 8, 14, 15) |
| **23** | **Trade payables** | **p204–p206/pr225–227** | MSME / non-MSME split; **full MSMED Act §16/§23 interest disclosure**; **ageing schedule both years including an "Unbilled" column** |
| **24** | **Other liabilities** | **p206/pr227** | **The most load-bearing single note in the document.** Advance from customers; **Gold Schemes**; capital creditors; **refund liability**; statutory dues; **gift vouchers**; **"Gold on lease" — a line that is nil in FY25 and material in FY26, procured from external parties at 4%–5% variable interest, 365-day tenure, sitting in Other current liabilities rather than in Borrowings or Gold on loan** |
| **25** | **Revenue from operations** | **p206–p207/pr227–228** | (A) Ind AS 115 disaggregation — **India vs Outside India, and at-a-point-in-time vs over-time only. There is no product, channel, store-format or category disaggregation.** (B) **reconciliation of contracted price to net revenue, i.e. the gross discount/incentive/returns deduction.** (C) contract assets and contract liabilities. (D) **no single customer ≥10% of revenue** |
| **26** | Other income | p208/pr229 | Interest on deposits; MF gain; **liabilities no longer required written back**; **fair value movement on the subsidiary call option**; unwinding of interest on amortised-cost assets; gain on lease termination; rent waiver; miscellaneous |
| **27** | **Cost of materials consumed** | **p208/pr229** | Opening RM + purchases − closing RM. **This is where the purchases figure lives** |
| **28** | Changes in inventories of finished goods and WIP | p208/pr229 | Opening/closing FG and WIP both years |
| **29** | **Employee benefits expense** | **p209/pr230** | Salaries and wages; PF and other funds; gratuity; **expense on ESOP scheme (cross-ref Note 38)**; staff welfare |
| **30** | **Finance costs** | **p209/pr230** | Interest on term loans; **debentures**; **franchisee deposit**; **lease liabilities**; other borrowing costs |
| **31** | Depreciation and amortisation expense | p209/pr230 | Split PPE / intangibles / ROU |
| **32** | **Other expenses** | **p209–p210/pr230–231** | 26 named lines including **advertisement & marketing, job work charges, contract labour, payment gateway charges, shipping, brokerage & commission, store maintenance, loss on sale of PPE**; sub-note (a) **auditors' remuneration split (statutory audit / certification / reimbursement)** and the footnote naming IPO-related fees paid to the auditors and to the erstwhile auditors |
| **33** | **Employee benefits (gratuity)** | **p211–p213/pr232–234** | Defined contribution expense; DBO reconciliation; **actuarial assumptions incl. discount rate, salary escalation and a three-band attrition table**; sensitivity analysis; expected future cash flows; compensated-absences policy |
| **34** | **Income taxes** | **p213–p214/pr234–235** | Current + deferred nil both years; **effective-tax-rate reconciliation with the enacted rate**; income tax assets; **deferred tax asset schedule — recognised NIL, with the explicit statement that reasonable certainty of future taxable income "is not yet established"**. This is the unrecognised-DTA disclosure |
| **35** | **Related party disclosures** | **p214–p217/pr235–238** | (i) full relationship list incl. **five relatives of KMP/directors by name**; (ii) transactions — **remuneration by individual**, sitting fees, rights-issue and private-placement subscriptions by the promoter, **"The Promoter Contribution Shortfall"**, ESOP exercised by individual, sale of products to related parties incl. **sales to the subsidiary**, sale of fixed assets to the subsidiary, investments in subsidiary and associate; (iii) **year-end payables to KMP and directors** and receivables from a director's relative; the CFO gold-leasing test-transaction note |
| **36** | Earnings per share | p217–p218/pr238–239 | Basic and diluted; weighted-average share counts; **the anti-dilution note for FY25**; adjustment for employee share options |
| **37** | Expenditure on CSR | p218/pr239 | Not required — no net profits in the three preceding years |
| **38** | **Employee stock option plan** | **p218–p219/pr239–240** | Scheme history and every amendment date; **vesting 1–7 years, exercise window 10 years from vesting**; options outstanding roll-forward; **reconciliation of vested options**; **weighted average remaining contractual life**; Black-Scholes-Merton inputs (grant dates, vesting period, volatility, risk-free rate, expected life, weighted-average fair value); **the statement that the stock price used was "the last round of funding closest to the grant date" and volatility from peer listed companies** |
| **39** | **Financial instruments — fair value measurement** | **p220–p221/pr241–242** | Carrying value by category (amortised cost vs FVTPL) for all financial assets and liabilities; **Level 1/2/3 hierarchy table** — note gold-on-loan and the hedge derivatives are shown at **Level 1**, the subsidiary call option at **Level 2**; no transfers between levels |
| **40** | **Financial instruments — risk management** | **p221–p225/pr242–246** | **(a) Hedge table: sell forward/future contracts — average rate per gram, quantity in kg, nominal amount, both years.** Fair-value-hedge mechanics and the hedged-item/hedging-instrument table with maturity buckets. (b) **credit risk + ECL table + the statement that the business is "cash and carry except for franchisee partners"**. (c) **liquidity risk — full undiscounted contractual maturity table in 5 buckets for both years**, plus **undrawn borrowing facilities**. (d) market risk: currency (nil exposure), **interest rate — variable-rate borrowings and the ±100bp sensitivity**, commodity price risk and the gold-on-loan balance |
| **41** | **Capital management** | **p226/pr247** | The company's own **"adjusted net debt to adjusted equity"** definition and calculation, both years. Note the deduction basis: cash, other bank balances and deposits **unless marked for GML collateral or bank guarantee** |
| **42** | **Analytical ratios** | **p226–p227/pr247–248** | Eleven Schedule III ratios with **the company's own methodology stated for each**, prior-year comparatives, % change and a variance explanation. Footnotes define EBIT, PBIT, PAT, **"Debt includes current and non-current lease liabilities"**, credit purchases, and capital employed |
| **43** | Relationship with struck-off companies | p228/pr249 | Nil |
| **44** | **Segment reporting** | **p228/pr249** | Single segment; **domestic vs export revenue split (export nil)**; all non-current assets in India |
| **45** | **Promoter contribution** | **p228/pr249** | Securities premium includes the promoter's **"Promoter contribution shortfall amount"** under Reg 15 of SEBI ICDR |
| **46** | **Commitments and contingencies** | **p228/pr249** | Capital commitments net of advances, both years; **"there are no contingent liabilities requiring disclosure"** for both years |
| **47** | **Other statutory information — the Companies (Audit and Auditors) additional disclosures** | **p228–p229/pr249–250** | (i) **benami**; (ii) unregistered charges/satisfaction; (iii) **crypto/virtual currency**; (iv) **funds routed through intermediaries**; (v) **funds received from funding parties**; (vi) **undisclosed income surrendered in tax assessments**; (vii) **wilful defaulter**; (viii) **the Section 186 table — inter-corporate deposits (Blacksoil Capital, Capsave Finance) with purpose, rate and term, and the investments roll-forward for subsidiary and associate** |
| **48** | **Audit trail compliance** | **p229/pr250** | The management-side counterpart to the auditor's Rule 11(g) modification. Four sub-paragraphs (a) main accounting software, (b) **inventory management and POS (revenue) software — audit trail NOT enabled at database level**, (c) lease-processing software, (d) payroll software up to 16-Jul-2025 |
| **49** | **Maintenance of books of account on server in India** | **p230/pr251** | The management-side counterpart to the §143(3)(b) modification: payroll software up to 15-Jul-2025 and lease-processing software, both unable to be assessed for daily India-located backup |
| **50** | **Fair value of contingent call options** | **p230/pr251** | The Ethereal House Shareholders' Agreement dated 06-Jan-2025; options linked to **revenue and EBITDA milestones**; **Monte Carlo simulation**; carrying value both years |
| **51** | Investment in subsidiary | p230/pr251 | The FY26 CCPS subscription in Ethereal House — number of shares, premium per share, total consideration |
| **52** | **Events after the reporting period** | **p230/pr251** | Evaluated through 23-Apr-2026; **"not aware of any events or transactions that would require recognition or disclosure"** |
| **53** | **IPO completion and utilisation of proceeds** | **p230–p231/pr251–252** | Fresh issue and offer-for-sale share counts and amounts; listing date 19-Aug-2025; net proceeds received after IPO expenses; IPO expenses adjusted to securities premium; **and, printed on p231/pr252, the object-wise utilisation table: proposed vs utilised vs unutilised for working capital, general corporate purpose and issue expenses, plus where the unutilised money is parked** |
| **54** | The Code on Social Security, 2020 | p231/pr252 | Four Labour Codes notified 21-Nov-2025; the incremental gratuity/compensated-absence impact |
| **55** | Regrouping/reclassification of prior-year figures | p231/pr252 | Boilerplate, but it is the only restatement statement in the document |

---

## 2B. Note locator — NOTES TO THE **CONSOLIDATED** FINANCIAL STATEMENTS (PDF p249–p313 / printed 270–334)

**Numbering differs from the standalone set from Note 7 onward** — the consolidated set has 58 notes vs 55.
A later agent quoting "Note 25" must state which basis.

| Note | Title | PDF p / printed | Why come here rather than to the standalone note |
|---|---|---|---|
| 1 | General Information | p249/pr270 | **Names the Group and describes the associate's business: Redefine Fashion Private Limited — footwear and accessories through D2C, B2B, B2C and e-commerce.** A jewellery company's associate is a footwear company |
| 2.1(i)–(vi) | Basis of preparation | p249–p250/pr270–271 | Authorised 23-Apr-2026. **(iv) Basis of measurement lists seven fair-valued items — a longer list than the standalone note** |
| **2.1(vii)** | **Principles of Consolidation** | **p250–p251/pr271–272** | Control definition; **line-by-line consolidation and elimination**; NCI measurement policy (**the Group has not elected the fair-value option in acquisitions to date**); equity method for the associate; **the subsidiary and associate holding tables — Ethereal House 75.51% (both years) and Redefine Fashion 49.12% FY26 vs 51.19% FY25, both "on dilutive basis"** |
| 2.1(viii) | Business combinations and goodwill | p251–p252/pr272–273 | Acquisition-method policy — read against Note 54, which explains why it was **not** applied |
| 2.2.1–2.2.18 | Material accounting policies | p252–p260/pr273–281 | Mirror the standalone policies |
| 3 | Property, plant and equipment | p261/pr282 | Group roll-forward |
| 4 | Leases | p262–p264/pr283–285 | Group ROU, lease liabilities, maturities, P&L expense |
| 5 | Capital work-in-progress (CWIP) | p264/pr285 | |
| 6A / 6B | Other intangible assets / under development | p264–p265/pr285–286 | **6A carries a Group-only sentence: "Product related intangibles (Trademark) are available to the Group in perpetuity"** |
| **7** | **Investments accounted for using the equity method** | **p266/pr287** | The associate carrying value **net of cumulative share of losses** — the standalone Note 7 carries it at cost |
| 8 | Other financial assets | p267/pr288 | Same structure as standalone Note 8 |
| 9 | Non-current tax assets (net) | p267/pr288 | |
| 10 | Other assets | p268/pr289 | |
| 11 | Inventories | p268/pr289 | **Group finished goods exceed the standalone figure — the difference is the subsidiary's lab-grown-diamond stock** |
| 12 | Investments — current | p269/pr290 | |
| **13** | **Loans** | **p269/pr290** | **Consolidated-only line: advances to employees. There is no standalone Note "Loans"** |
| 14 | Trade receivables (+ageing) | p269–p271/pr290–292 | |
| 15 | Cash and bank balances | p271/pr292 | |
| 16 | Other bank balances | p271/pr292 | |
| 17 | Share capital (incl. >5% holders, promoter holding, treasury reconciliation) | p271–p280/pr292–301 | Identical content to standalone Note 16 |
| **18** | **Other equity — including Non-Controlling Interest** | **p280–p282/pr301–303** | **(v) the NCI roll-forward: opening, "Adjustments for changes in ownership interests", "Founders' capital contribution at the time of incorporation", profit attributable, closing.** This is where the subsidiary's minority economics live |
| 19 | Borrowings | p282–p283/pr303–304 | Same instruments, coupons, tenors and security as standalone Note 18 |
| 20 | Lease liabilities | p283/pr304 | |
| 21 | Other financial liabilities | p284/pr305 | |
| 22 | Provisions | p284/pr305 | |
| 23 | Gold on loan | p284/pr305 | |
| 24 | Trade payables (+MSME + ageing) | p285–p286/pr306–307 | |
| 25 | Other liabilities | p286–p287/pr307–308 | Includes the same **Gold on lease** line |
| 26 | Revenue from operations (+Ind AS 115, contracted-price reconciliation, contract balances) | p287–p288/pr308–309 | **Group revenue is LOWER than standalone — intra-group sales to Ethereal House are eliminated** |
| 27 | Other income | p288/pr309 | |
| 28 | Cost of materials consumed | p288/pr309 | |
| **29** | **Purchases of stock-in-trade** | **p289/pr310** | **Consolidated-only expense line, nil in FY25 — the subsidiary's traded goods. There is no standalone equivalent** |
| 30 | Change in inventories of FG and WIP | p289/pr310 | |
| 31 | Employee benefits expense | p289/pr310 | |
| 32 | Finance costs | p289/pr310 | |
| 33 | Depreciation and amortisation expense | p290/pr311 | |
| 34 | Other expenses (+auditors' remuneration) | p290–p291/pr311–312 | **Group audit fee exceeds the standalone fee — the gap is the subsidiary's auditor** |
| 35 | Employee benefits (gratuity) | p291–p294/pr312–315 | |
| 36 | Income taxes | p294–p295/pr315–316 | Group unrecognised deferred tax asset schedule |
| 37 | Related party disclosures | p295–p297/pr316–318 | **Subsidiary transactions drop out (eliminated); the associate and the KMP/relatives remain** |
| 38 | Earnings per share | p298/pr319 | Attributable to owners of the parent |
| 39 | Expenditure on CSR | p298/pr319 | |
| 40 | Employee stock option plan | p299–p300/pr320–321 | |
| 41 | Financial instruments — fair value measurement | p300–p302/pr321–323 | |
| 42 | Financial instruments — risk management | p302–p306/pr323–327 | Hedge, credit, liquidity, market, commodity — Group basis |
| 43 | Capital management | p306–p307/pr327–328 | Group adjusted net debt / adjusted equity |
| 44 | Analytical ratios | p307–p308/pr328–329 | **Eleven ratios on the Group basis — different values from standalone Note 42. Any ratio quoted must name its basis** |
| 45 | Relationship with struck-off companies | p308/pr329 | |
| 46 | Operating segments | p309/pr330 | Single segment; domestic/export |
| 47 | Promoter contribution | p309/pr330 | |
| 48 | Commitments and contingencies | p309/pr330 | Same capital commitment; **no contingent liabilities** |
| **49** | **Other statutory information** | **p309–p310/pr330–331** | Same seven Companies (Audit and Auditors) items, plus **(viii) the Section 186 inter-corporate-deposit and investment table**, plus **(ix) the Schedule III entity-wise table: net assets, share in profit or loss, share in OCI and share in total comprehensive income, as a % of consolidated and in amount, for the Parent, the Subsidiary, "Adjustment on account of consolidation", the Non-controlling interest and the Associate.** This is the single best page for isolating what the parent earns from what the group reports |
| **50** | **Investment in associate company** | **p311/pr332** | Country, **proportion of ownership interest**, the associate's total comprehensive loss and **the Group's share of it**. States there is no *material* associate requiring Ind AS 112 disclosure |
| 51 | Audit trail compliance | p311/pr332 | Group counterpart to standalone Note 48 |
| 52 | Maintenance of books of account on server in India | p311–p312/pr332–333 | Group counterpart to standalone Note 49 |
| 53 | Fair value of contingent call options | p312/pr333 | |
| **54** | **Acquisition of Ethereal House Private Limited** | **p312/pr333** | **The key consolidation-judgement note. The controlling stake was acquired in the previous year in "a newly incorporated entity with no operations or assets other than initial cash contributed by its founders". Because there was no substantive process or organised workforce it is NOT a business combination under Ind AS 103, and because no tangible or intangible assets were acquired other than cash it is NOT an asset acquisition either. It is accounted for as "a corporate control transaction": no goodwill, no capital reserve, no revaluation, consolidated line-by-line from the date control was obtained** |
| 55 | Events after the reporting period | p312/pr333 | Nothing to report through 23-Apr-2026 |
| 56 | IPO completion + **utilisation table** (printed on p313/pr334) | p312–p313/pr333–334 | Same table as standalone Note 53 |
| 57 | The Code on Social Security, 2020 | p313/pr334 | |
| 58 | Regrouping/reclassification | p313/pr334 | |

### Note-number crosswalk (the trap)

| Disclosure | Standalone note | Consolidated note |
|---|---|---|
| Revenue from operations | **25** (p206/pr227) | **26** (p287/pr308) |
| Other income | 26 | 27 |
| Cost of materials consumed | 27 | 28 |
| Purchases of stock-in-trade | *(none)* | **29** |
| Employee benefits expense | 29 | 31 |
| Finance costs | 30 | 32 |
| Depreciation and amortisation | 31 | 33 |
| Other expenses | 32 | 34 |
| Income taxes | 34 | 36 |
| Related party disclosures | **35** | **37** |
| EPS | 36 | 38 |
| ESOP | 38 | 40 |
| Analytical ratios | **42** | **44** |
| Segment | 44 | 46 |
| Commitments and contingencies | 46 | 48 |
| Other statutory information | 47 | 49 |
| Audit trail | 48 | 51 |
| IPO utilisation | 53 | 56 |
| Share capital | 16 | 17 |
| Other equity | 17 | 18 |
| Borrowings | 18 | 19 |
| Gold on loan | 22 | 23 |
| Other liabilities (incl. Gold on lease) | 24 | 25 |

**The auditors' own KAM cross-references use the consolidated numbering in the consolidated report
(*"refer note 2.2.7 and 26"* [AR FY26, consolidated auditor's report, p232/pr253]) and the standalone
numbering in the standalone report (*"refer note 2.2.7 and 25"* [AR FY26, standalone auditor's report,
p150/pr171]). One KAM cross-reference is wrong: the consolidated inventory KAM says *"refer note 2.2.5 and
11 of the consolidated financial statements"* [AR FY26, p233/pr254] — consolidated Note 11 IS inventories,
so this one holds.**

---

## 3. Standalone vs consolidated map — which pages are which

| Set | Auditor's report | Balance Sheet | P&L | Cash Flows | SoCiE | Notes |
|---|---|---|---|---|---|---|
| **STANDALONE** | **p150–p163** / pr171–184 | **p164** / pr185 | **p165** / pr186 | **p166–p167** / pr187–188 | **p168–p169** / pr189–190 | **p170–p231** / pr191–252 |
| **CONSOLIDATED** | **p232–p242** / pr253–263 | **p243** / pr264 | **p244** / pr265 | **p245–p246** / pr266–267 | **p247–p248** / pr268–269 | **p249–p313** / pr270–334 |

The boundary is unambiguous: **PDF page 232 (printed 253) is where the consolidated set begins.** Every page from
p232 to p313 is consolidated. Every page from p150 to p231 is standalone. There is no interleaving.

### Does a subsidiary exist, and where is it disclosed?

**Yes — one subsidiary and one associate.** Neither is a material subsidiary under SEBI LODR.

| Entity | Relationship | CIN | Where disclosed |
|---|---|---|---|
| **Ethereal House Private Limited** | **Subsidiary**, 75.51% on a dilutive basis (both years) | U32111HR2024PTC124350 | Board's Report §10 [p57/pr78] with a full FY26 P&L summary in ₹ million · **FORM AOC-1 Part A** [p79/pr100] in ₹ absolute rupees, with authorised/paid-up capital, reserves, total assets, total liabilities, turnover, loss before and after tax, and the acquisition date (Shareholders' agreement 06-Jan-2025; shares allotted 13-Jan-2025) · Standalone Note 7 [p186/pr207] and Note 51 [p230/pr251] · Standalone Note 50 (contingent call options) [p230/pr251] · Standalone Note 35 (RPT: sale of products, sale of fixed assets, reimbursement, CCPS subscription) [p215–p216/pr236–237] · Standalone Note 47(viii) [p229/pr250] · **Consolidated Note 2.1(vii) holding table** [p251/pr272] · **Consolidated Note 18(v) NCI roll-forward** [p281/pr302] · **Consolidated Note 49(ix) entity-wise contribution table** [p310/pr331] · **Consolidated Note 54 acquisition accounting** [p312/pr333] · CARO summary table in the consolidated auditor's report [p238/pr259] |
| **Redefine Fashion Private Limited** | **Associate**, 49.12% FY26 (51.19% FY25), on a dilutive basis; footwear and accessories | U74101KA2024PTC191944 | Board's Report §10 [p57–p58/pr78–79] with a FY26 P&L summary in ₹ million · **FORM AOC-1 Part B** [p80/pr101] · Standalone Note 7 [p186/pr207] (at cost) · **Consolidated Note 7** [p266/pr287] (equity method, net of share of losses) · Consolidated Note 1 [p249/pr270] · Consolidated Note 2.1(vii) [p251/pr272] · **Consolidated Note 50** [p311/pr332] · Consolidated Note 37 RPT [p297/pr318] · Consolidated Note 49(viii)/(ix) [p310/pr331] |

**Corporate-governance statements about the subsidiary:** Board's Report §10 confirms no joint ventures and no
entity ceased to be a subsidiary/associate during the year [AR FY26, p58/pr79]. The Corporate Governance Report
§XVIII(d) and (g) state the Company has **no material subsidiary** and describes the oversight arrangements
(subsidiary board minutes placed before the Board quarterly, subsidiary financial statements reviewed by the
Audit Committee) [AR FY26, p115–p116/pr136–137]. §XV(13) states **the subsidiary operates no manufacturing
facility** [AR FY26, p113/pr134].

---

## 4. Auditor block

### 4a. Identity

| Item | Standalone | Consolidated |
|---|---|---|
| Firm | **M S K A & Associates LLP** (formerly M S K A & Associates), Chartered Accountants | same |
| ICAI FRN | **105047W/W101187** | same |
| Signing partner | **Ankush Agrawal**, Membership No. 159694 | same |
| Place / date | **Bangalore, 23 April 2026** | Bangalore, 23 April 2026 |
| UDIN | **26159694FBQAUO4774** | **26159694CAQCKF4199** |
| Where | p150–p163 / pr171–184 | p232–p242 / pr253–263 |

Tenure and fees: appointed at the AGM of 30-Sep-2023 for five years, to the conclusion of the AGM for FY2027-28;
the firm converted to an LLP during the year and continues for the remaining tenure [AR FY26, Board's Report §20,
p65/pr86]. **There has been no resignation of the statutory auditors during the year** [AR FY26, CARO clause xviii,
p161/pr182]. Total fees to the auditor and its network, on a consolidated basis, are disclosed in the Corporate
Governance Report §XVII [AR FY26, p114/pr135] in **₹ absolute rupees**, split into audit of statutory accounts,
taxation matters, other services and reimbursement — cross-check against Note 32(a) [AR FY26, p210/pr231] and
consolidated Note 34(a) [AR FY26, p291/pr312], which are in ₹ million and which additionally footnote the
IPO-related fees paid to the auditors **and to the erstwhile auditors**.

### 4b. Is the opinion modified?

**The audit OPINION on both the standalone and the consolidated financial statements is UNMODIFIED** — a clean
true-and-fair opinion under Ind AS [AR FY26, p150/pr171 and p232/pr253]. There is **no Emphasis of Matter
paragraph** and **no Material Uncertainty Related to Going Concern paragraph** in either report.

**BUT the report itself carries two express modifications outside the opinion**, and a later agent must not
report the audit as "clean" without them:

1. **Section 143(3)(b) — proper books of account.** *"In our opinion, proper books of account as required by law
   have been kept by the Company so far as it appears from our examination of those books, **except that** (i) in
   case of an accounting software that is part of books of accounts, in the absence of sufficient appropriate audit
   evidence we are unable to comment whether back-up of the books of account … have been kept in servers physically
   located in India on a daily basis, (ii) in case of another accounting software … in the absence of adequate
   coverage in SOC report, we are unable to comment whether back-up … is maintained on a daily basis"*
   [AR FY26, standalone auditor's report ¶2(b), p153/pr174]. Same wording, consolidated, at ¶1(b) [p235/pr256].
2. **Rule 11(g) — audit trail.** *"no audit trail feature was enabled at the database level in respect of an
   accounting software to log any direct data changes"* and *"we are unable to comment on audit trail at database
   level in respect of an accounting software due to absence adequate coverage in SOC report"*; separately, for the
   **payroll (to 16-Jul-2025) and lease-processing softwares** managed by a third party, *"in absence of sufficient
   and appropriate audit evidence including SOC report, we are unable to comment whether these accounting softwares
   has a feature of recording audit trail (edit log) facility … or whether there is any instance of audit trail
   feature being tampered with"* [AR FY26, standalone auditor's report ¶2(h)(vi)(a) and (b), p154–p155/pr175–176].
   Same, consolidated, at ¶1(h)(vi) [p237/pr258].
3. The auditors themselves label these as modifications: *"**The modification** relating to the maintenance of
   accounts and other matters connected therewith are as stated in paragraph 2(b) above … and paragraph 2(h)(vi)"*
   [AR FY26, standalone auditor's report ¶2(f), p153/pr174; consolidated ¶1(f), p236/pr257].

Management's own account of the same matters is at **standalone Notes 48 and 49** [AR FY26, p229–p230/pr250–251]
and **consolidated Notes 51 and 52** [AR FY26, p311–p312/pr332–333]. Note 48(b) is the sharpest sentence:
*"In respect of the **inventory management and POS (revenue) softwares**, the audit trail feature was **not enabled
at the database level** to log direct data changes."* Inventory and revenue are precisely the two Key Audit Matters.

### 4c. Key Audit Matters

| # | KAM | Standalone page | Consolidated page | Note cross-ref |
|---|---|---|---|---|
| 1 | **Revenue Recognition** — multiple operating models (owned retail outlets, online, franchisee); varying pricing, discounts, returns, incentives, loyalty programmes and timing of transfer of control; high daily transaction volume across multiple systems and locations; significant reliance on IT systems and controls; risk of material misstatement due to **error or fraud** | **p150–p151 / pr171–172** | **p232–p233 / pr253–254** | Std 2.2.7 + 25; Cons 2.2.7 + 26 |
| 2 | **Existence of inventory** — high-value, portable, large variety by purity/weight/quality/design, decentralised storage, frequent inter-location movement; susceptibility to **theft, loss, damage and human error**; reliance on physical counts and on segregation of duties and secure custody | **p151–p152 / pr172–173** | **p233–p234 / pr254–255** | Std 2.2.5 + 11; Cons 2.2.5 + 11 |

Both reports list the audit procedures performed. The inventory procedures include attending physical counts at
selected retail outlets and manufacturing facilities, independent test counts verifying gross weight, net weight,
purity and unique identification numbers, **independent confirmations for inventory held with job workers**, and
cut-off testing. The consolidated revenue KAM adds one procedure the standalone does not name: *"Tested manual
adjustments impacting revenue including credit notes etc., by inspecting supporting documents and understanding
business rationale"* [AR FY26, p233/pr254].

**No KAM was raised on:** leases and the ROU asset (₹8.4bn class), the gold-on-loan / gold-on-lease financing,
the ESOP charge, the unrecognised deferred tax asset, or the fair value of the subsidiary call option.

### 4d. Emphasis of matter

**None.** Neither report contains an Emphasis of Matter paragraph or an Other Matter paragraph.

### 4e. CARO observations that are NOT clean

The standalone CARO 2020 report is **Annexure B, p158–p161 / pr179–182**. There is **no separate CARO annexure for
the consolidated statements**; the consolidated position is summarised in paragraph 3 of "Report on Other Legal and
Regulatory Requirements" [AR FY26, p238/pr259].

**The one non-clean standalone CARO clause:**

- **Clause xvii — cash losses.** *"Based on the overall review of standalone financial statements, Company has not
  incurred cash losses during the current financial year **but has incurred cash losses amounting to ₹ 236.29
  million during the immediately preceding financial year**"* [AR FY26, CARO clause xvii, p161/pr182].

**The consolidated CARO summary table names three qualified/adverse clauses** [AR FY26, p238/pr259]:

| Company | CIN | Type | Clause qualified or adverse |
|---|---|---|---|
| BlueStone Jewellery Lifestyle Limited | L72900KA2011PLC059678 | Holding Company | **Clause xvii** |
| **Ethereal House Private Limited** | U32111HR2024PTC124350 | Subsidiary | **Clause vii(a)** *(undisputed statutory dues not regularly deposited)* **and Clause xvii** |

**Internal contradiction to carry forward:** the sentence immediately above that table reads *"…based on the CARO
reports issued by us, we report that **there are no qualifications or adverse remarks** in the CARO reports of the
companies included in the consolidated financial statements"* [AR FY26, p238/pr259] — and is followed by a table
listing three. The subsidiary's own CARO report is **not reproduced anywhere in this document**; only the clause
number is given. Clause vii(a) for Ethereal House therefore states that a statutory-dues problem exists in the
subsidiary **without a single number attached to it**.

**Clauses that are clean but load-bearing, and where to find them:**

| CARO clause | Subject | PDF p / printed |
|---|---|---|
| i(a)–(e) | PPE and ROU records, phased physical verification over three years, **no immovable properties**, no revaluation, **no benami proceeding** | p158/pr179 |
| ii(a) | Inventory physically verified; third-party stock confirmed; **"discrepancies noticed on physical verification … were not 10% or more in aggregate for each class of inventory"** — note this is a threshold statement, not a nil statement | p158/pr179 |
| ii(b) | **Working capital limits in excess of ₹5 crore against security of current assets; quarterly statements filed with banks are in agreement with the books** | p158/pr179 |
| iii(a) | No loans, guarantees or security given; **investment in a subsidiary of ₹252.00 million during the year** | p158/pr179 |
| iii(b) | Investment terms **"not prejudicial to the interest of the Company"** | p159/pr180 |
| iv | Sections 185/186 complied | p159/pr180 |
| vii(a)/(b) | Undisputed statutory dues **regularly deposited**; **no disputed dues at all** | p159/pr180 |
| viii | **No transactions surrendered or disclosed as income in tax assessments** | p159/pr180 |
| ix(a) | **No default in repayment of loans or borrowings or interest to any lender** | p159/pr180 |
| ix(b) | **Not declared a wilful defaulter** | p160/pr181 |
| ix(c) | **Term loans applied for the purpose raised** | p160/pr181 |
| ix(d) | **No short-term funds used for long-term purposes** | p160/pr181 |
| ix(e)/(f) | No funds taken to meet subsidiary/associate obligations; no loans against pledge of subsidiary securities | p160/pr181 |
| **x(a)** | **IPO monies applied for the purpose raised, "though idle funds which were not required for immediate utilization have been invested in bank deposits"; the maximum amount of idle funds invested during the year and the amount outstanding at year end are both quantified** | **p160/pr181** |
| x(b) | **No preferential allotment or private placement of shares or convertible debentures during the year** | p160/pr181 |
| **xi(a)/(b)/(c)** | **No fraud by or on the Company noticed or reported; no ADT-4 filed; "We have taken into consideration the whistle blower complaints received by the Company during the year while determining the nature, timing, and extent of audit procedures"** — the auditor confirms whistleblower complaints WERE received, without quantifying them | **p160/pr181** |
| xiii | **Related party transactions comply with Sections 177 and 188 and are disclosed as required** | p160/pr181 |
| xiv(a)/(b) | Internal audit system commensurate with size; internal audit reports considered | p160/pr181 |
| xv | **No non-cash transactions with directors or persons connected with directors** | p161/pr182 |
| **xix** | **Material-uncertainty / one-year liquidity statement, framed on the note 42 ratios** — with the explicit caveat that it "is not an assurance as to the future viability of the Company" | **p161/pr182** |
| xx | Section 135 not applicable | p161/pr182 |

**Internal Financial Controls opinion:** unqualified for both the Company [Annexure C, p162–p163/pr183–184] and the
Group [consolidated Annexure B, p241–p242/pr262–263]. The Group IFC report notes that IFC reporting is **not
applicable to the associate** under MCA notification GSR 583(E) dated 13-Jun-2017 [AR FY26, p241/pr262].

**Secretarial audit (MR-3, Mihen Halani & Associates, p81–p84/pr102–105):** no qualifications, reservations,
adverse remarks or disclaimers. Its "events having a major bearing" list [AR FY26, p82–p83/pr103–104] is a
standalone checklist of the year's corporate actions and is the **only place in the document where the FY26
issuance of 800 unlisted, secured, redeemable non-convertible debentures of ₹5,00,000 each aggregating
₹40,00,00,000 on a private-placement basis is stated**. **Annual Secretarial Compliance Report (p85–p88/pr106–109):**
13-point grid, all "YES" or "NA", **no deviations recorded**.

---

## 5. Where management makes claims — and every operating metric with its page

### 5a. The claim-bearing sections

| Section | PDF pages | Character |
|---|---|---|
| Highlights of the Year | **p9** | Headline claims and CAGRs |
| What Makes Us Different (7 pillars) | p13–p23 | Store economics, technology, marketing, people |
| **Message from the Chairman** | **p24–p25** | Named, signed claims by Gaurav Singh Kushwaha, incl. an explicit self-criticism section |
| **Key Performance Indicators** | **p26** | The 4-year bar series |
| Growth Strategy | p27–p28 | Forward targets |
| Corporate Governance overview | p29–p30 | Committee and policy claims |
| **Board's Report** (49 paragraphs) | **p48–p75** | The statutory claims |
| **MD&A — Performance Review + Key Highlights** | **p142–p143** | The management explanation of FY26 |
| MD&A — Opportunities / Threats / Risks / Internal Control / HR | p144–p149 | Qualitative |

### 5b. Operating-metric locator

| Metric | Value as printed | PDF p / printed | Basis stated? |
|---|---|---|---|
| **Store count, year end** | **340 stores** | p9, p12, p15, p20, p140/pr161, p143/pr164 | Yes — "as at 31st March 2026" |
| **New stores added in FY26** | **65** | p9, p24, p143/pr164 | Yes |
| **Cities / towns** | **134** | p9, p12, p140/pr161, p143/pr164 | Yes |
| **States and union territories** | **28** | p12, p20 | Yes |
| **State-wise store count** | 28-row map table, **sums exactly to 340** | **p12** | Yes |
| **Tier-wise store split** | FY23–FY26 stacked bars, Tier 1 / Tier 2 / Tier 3; FY26 = 68 / 94 / 178 (=340) | **p20** | Yes |
| **Total store area** | FY23–FY26 series in '000 sq ft; FY26 = 800 | **p20** | Yes |
| Share of stores in Tier II/III | "~50%" | p12 | No — a rounding of the p20 table |
| **PIN codes served** | **12,660+** | p9, p12, p20 | Yes |
| **Lifetime customers served** | **"over 9.4 lakh customers"** | **p143/pr164** | Yes — "expanding lifetime customer base" |
| Lifetime consumers (chapters timeline) | "9 lakh+ consumers since incorporation" (2026 milestone); "5 lakh+" (2024) | p8 | Timeline, not a period metric |
| **New consumers added in FY26** | **"over 1.7 lakh new consumers"** | **p24** | Chairman's letter |
| **Repeat-customer share of revenue** | **"54.5% of FY26 revenue came from repeat customers"**; separately "more than half our revenue now comes from consumers who came back" | **p25** and p24 | Yes, FY26 |
| **Online sessions** | "nearly 300 million online sessions this year" | p24 | Yes, FY26 |
| Product/consumer trend data | "over 300 million days of product data" | p18, p19 | Different unit from the sessions figure — do not conflate |
| **Same-store sales growth** | *"healthy SSSGs across cohorts"* — **qualitative only, never quantified anywhere in this document** | p143/pr164 | **NOT DISCLOSED as a number** |
| **Store cohort breakeven** | "75% of our store cohorts break even within three months of opening" | **p13** | No cohort definition, no basis |
| Store maturity | "More than half of our store network comprises stores that are less than three years old" | p28 | No table behind it |
| **City case studies** | Ranchi FY22–FY26 revenue in ₹ mn with store count; Lucknow FY22–FY26; Silchar, Brahmapur, Gorakhpur FY23–FY26 | **p16** | City-level revenue, ₹ mn — **the only geographic revenue disaggregation in the document** |
| Designs | "over 15,000 unique designs" | p7, p9, p15, p140/pr161 | |
| In-house manufacturing | "over 95% of jewellery manufactured in-house" | p9, p17, p19, p25 | |
| Designers | "25-30 designers" / "over 25 designers" | p17, p140/pr161 | Inconsistent between the two pages |
| Market share | "28-32% market share among omni-channel jewellery players in 2024" | **p9** | **Redseer, FY24 — a two-year-old third-party estimate** |
| Ranking | "#2 digital-first omni-channel jewellery brands in India"; "#1 by manufacturing-to-shelf turnaround"; "Top 6 by number of designs listed" | p9, p16, p140/pr161 | Redseer, peer set defined in the p9 footnote as omnichannel/multichannel players with FY2024 revenue > ₹5,000 mn and >50 stores |
| **Digital marketing spend** | **"~₹100 cr digital marketing investments (a scale-up of ~30% over the past year)"** | **p22** | ₹ crore. Compare against Note 32 "Advertisement & marketing costs" in ₹ mn [p210/pr231] |
| **Advertising & marketing as % of sales** | **"contained at 6.6% of sales in FY26, as against 9.0% in FY25"** | **p143/pr164** | Standalone |
| Instagram following | "crossed 1 million this year" | p22 | |
| Content performance | "~30% of content formats consistently emerge as high performers" | p21 | |
| Cost of an unsuccessful product | "below ₹2,000 per piece" | p9 | |
| **Headcount** | **2,576 total; 38.50% female / 61.50% male; 84% retail / 8% operations / 4% corporate / 4% manufacturing; 297 new female hires; female representation +2.8% YoY** | **p23**, and p148/pr169; the statutory version (Male 1,585 / Female 991 / Transgender NIL) is at Board's Report §31(iii) [p68/pr89] | Both figures reconcile |
| **Median employee remuneration** | ₹6,21,702 (₹ absolute rupees); +11% YoY; MD ratio 54:1 | **Board's Report §31, p67–p68/pr88–89** | Excludes post-retirement benefits and joiners/leavers |
| **Employees above the §197(12) threshold** | "9 (nine) employees" above ₹1,02,00,000 p.a. — **the schedule itself is omitted from the AR and available only on inspection** | p68/pr89 | **Disclosure withheld under the second proviso to §136(1)** |
| **Energy** | Total energy consumption across all three manufacturing units FY2025-26 = 28,63,546 units; **1.33 units/gm** of production | **p71/pr92** | Board's Report §41(A). The only production-volume-linked metric in the document, and it is stated per gram — an implied production quantity |
| Solar | 140 kW at Surat (~187 MWh, ~31% of that unit); 500 kW under implementation at Jaipur (~730 MWh, ~40%) | p70–p71/pr91–92 | |
| Digital certificates | applied to over 13,43,067 units in FY2025-26, saving ~6,715 kg of PVC | p72/pr93 | **A unit count that behaves like an order/piece volume proxy** |
| **Foreign exchange outgo** | ₹49.40 million; **foreign earnings nil** | **p73/pr94** | Board's Report §41(C) |
| **Gold commodity exposure and hedge** | Total commodity exposure ₹3,011.66 million (gold); **205 kg**; **100% hedged, domestic exchange** | **CG Report §XVIII(f), p116/pr137** | Cross-check to Note 40 hedge table [p222/pr243] |
| POSH complaints | 3 received, 3 disposed, nil pending, nil over 90 days | p69/pr90 and p117/pr138 | Stated twice |
| Investor complaints | **nil received during FY2025-26** | p102/pr123 | |
| Familiarisation | Independent Directors spent **"~4 hours"** cumulatively on familiarisation programmes | **p73/pr94** | |
| Dematerialisation | 97.98% in demat; 2.02% (30,80,655 shares) still in physical form | p113/pr134 | |
| Shareholders | 39,697 total; 97.76% hold 1–501 shares; **149 folios (0.38%) hold 97.94% of shares** | **p112/pr133** | |
| **Shareholding pattern** | Promoter and promoter group 16.27%; FDI/FPI Cat I 34.19%; AIF 22.38%; resident individuals 12.64%; bodies corporate/MF/insurance 14.47% | **p112/pr133** | As at 31-Mar-2026 |

### 5c. Forward-looking targets management put on the record

- **"Targeting a network of 700+ stores over the long term"** [AR FY26, p28].
- *"The company plans to significantly increase its retail footprint in F.Y. 2027"*; two dedicated Men's and Kids
  stores opened in the year [AR FY26, p145/pr166].
- **ESOP charge**: *"this charge has been front-loaded under the current grant cycle and is expected to decline
  materially from FY27 onwards, with the reduction flowing through to reported EBITDA and PAT in subsequent
  years"* [AR FY26, p143/pr164].
- *"We believe the fixed cost base remains only partially leveraged, leaving headroom for further operating margin
  expansion over the medium term"* [AR FY26, p143/pr164].
- The Chairman's own scoreboard: *"hold us to three things … how many new consumers we bring in; how many of our
  consumers come back; and how efficiently we turn our capital"* [AR FY26, p25].
- The Chairman's admission on entry-level merchandise: *"as gold climbed, our entry-level pieces … quietly thinned
  out, because at the new prices the system rebalanced away from them … we exited the fourth quarter growing above
  30%"* [AR FY26, p25]. **The Q4 growth rate is stated in the letter and is not reconcilable to any table in this
  document** — the AR carries no quarterly split.

### 5d. Management figures that do not reconcile inside this document — flagged for later waves, not resolved here

These are recorded because a document map that hides them forces every later agent to rediscover them.

1. **Return on Capital Employed.** MD&A Key Highlights says *"Return on Capital Employed turned positive at 8.6%,
   as against (4.7)% in FY25"* [AR FY26, p143/pr164]. The MD&A's own ratio table on the next spread says **11.20%
   vs (0.95)%** [AR FY26, p146/pr167], as does standalone Note 42(j) [AR FY26, p227/pr248]. Three pages, two
   different pairs of numbers, same label, same basis line ("Basis standalone financials reporting").
2. **The KPI bar chart mixes bases across years.** [AR FY26, p26] shows FY26 EBITDA 3,944.6 and margin 16.2
   (which are the **standalone** figures per MD&A p142/pr163) against FY25 EBITDA 731.64 and margin 4.1 (which are
   the **consolidated** figures — standalone FY25 EBITDA is 758.85 and 4.29%). The "1,187 bps" expansion claimed on
   p9 is the standalone-to-standalone delta. The chart and the headline are on different bases.
3. **The "83% CAGR (FY24-26)" revenue claim on p9** cannot be reproduced from the FY23–FY26 revenue series printed
   on p26 (7,707.26 / 12,658.39 / 17,700.02 / 24,412.30 ₹ mn). The 173% EBITDA CAGR on the same page does
   reproduce from that series; the 47% three-year revenue CAGR stated in the p26 body text also reproduces.
4. **Managing Director's remuneration.** Corporate Governance Report §IV shows *"Salary & Allowance including
   perquisites and variables pay and Bonus ₹ 3,38,54,004"* [AR FY26, p100/pr121, in ₹ absolute rupees]. Standalone
   Note 35(ii) shows *"Remuneration paid/accrued to KMP's and Directors — Mr. Gaurav Singh Kushwaha 94.21"*
   [AR FY26, p215/pr236, in ₹ million], against 30.83 in FY25. Note 35(iii) shows the year-end payable to him
   rising from 3.60 to 63.60 [AR FY26, p216/pr237]. Board's Report §31 states his **"% increase in Remuneration in
   the Financial Year 2025-26: NIL"** [AR FY26, p67/pr88]. Board's Report §26 records that a **one-time special
   bonus and a remuneration increase for the MD were approved by members through postal ballot on 30 May 2026**,
   after the year end [AR FY26, p66/pr87 and CG Report §XIV(B), p109/pr130], while standalone Note 52 states there
   were **no events after the reporting period requiring recognition or disclosure** [AR FY26, p230/pr251]. Four
   documents, four different pictures of the same payment.
5. **Auditor observations.** Board's Report §21 states *"The Statutory Auditors of the Company have made no
   observations, reservations, adverse remarks, disclaimers or qualifications"* [AR FY26, p65/pr86], and CG Report
   §XVIII(e)(a) states the auditors' reports *"are unqualified"* [AR FY26, p115/pr136] — against the auditor's own
   ¶2(f) naming its modifications [AR FY26, p153/pr174].
6. **Board-meeting attendance for 16.07.2025.** Board's Report §12 shows 6 entitled / **5** attended [AR FY26,
   p59/pr80]; the Corporate Governance Report shows 6 entitled / **6** attended for the same meeting [AR FY26,
   p90/pr111].
7. **The Sudeep Nagar ESOP grant percentage.** Board's Report §8(j)(iii) writes *"representing 1.04% (one point one
   zero percent)"* — the numeral and the words disagree [AR FY26, p52/pr73]; the same grant is stated as **1.10%**
   in the Secretarial Audit Report [AR FY26, p82/pr103] and as **1.04%** again on p54/pr75.
8. **Non-executive director remuneration.** The CG Report gives a sitting-fees table totalling one amount and a
   remuneration table totalling another, with three footnotes stating a *"Remuneration **payable**"* figure per
   director different from the amount in the table body [AR FY26, p101/pr122].
9. **Redefine Fashion ownership.** Consolidated Note 2.1(vii) shows the associate at **51.19% on a dilutive basis
   at 31-Mar-2025** [AR FY26, p251/pr272] while it was equity-accounted as an associate, not consolidated. FORM
   AOC-1 Part B leaves *"Description of how there is significant influence"* and *"Reason why the Associate/Joint
   Venture is not consolidated"* both answered **"Not applicable"**, and leaves *"Net worth attributable to
   shareholding as per latest Audited Balance Sheet"* **blank** [AR FY26, p80/pr101].
10. **Page 245 (printed 266), the Consolidated Statement of Cash Flows, is titled "Standalone Statement of Cash
    Flows."** The figures on it are consolidated (they agree with the consolidated P&L and balance sheet); the title
    block is wrong. A later agent citing "p245, Standalone Cash Flow" would be citing the consolidated statement.
11. **Advertisement and marketing.** Management states A&M was 6.6% of sales in FY26 vs 9.0% in FY25 [AR FY26,
    p143/pr164], while Note 32 shows advertisement & marketing costs essentially flat in absolute ₹ mn between the
    two years [AR FY26, p210/pr231], and the chapters section separately claims digital marketing investment of
    "~₹100 cr" **up ~30%** [AR FY26, p22]. Three statements, and they are not obviously all true together.
12. **"Pre-IndAS EBITDA reached 181 crores at a 7.4% margin"** [AR FY26, p24]. This non-GAAP measure appears once,
    in the Chairman's letter, and **is not defined, reconciled or repeated anywhere else in the document** — not in
    the MD&A performance review, not in the notes.

---

## 6. What is NOT in this document that the doctrine will look for

Each line names the document that would answer it, per doctrine §1a-iii.

### 6a. Absent because the company says the requirement does not apply

- **Business Responsibility and Sustainability Report (BRSR) — absent.** Board's Report §46 states BlueStone was
  outside the top 1,000 listed entities on the 1-Jul-2024 to 31-Dec-2024 market-cap list, and that **BRSR becomes
  applicable from FY2026-27** on the 1-Jul-2025 to 31-Dec-2025 list [AR FY26, p74/pr95]. **-> the FY2027 annual
  report will carry the first BRSR; for FY26, ESG/emissions/water/waste data beyond Board's Report §41(A)/(B)
  [p70–p73/pr91–94] does not exist in any BlueStone filing.**
- **Form AOC-2 (material related-party contracts) — absent.** Board's Report §29 states no material RPTs were
  entered into, so AOC-2 "is not applicable" [AR FY26, p67/pr88]. **-> RPT detail exists only in standalone Note 35
  [p214–p217/pr235–238] and consolidated Note 37 [p295–p297/pr316–318]; for related-party *approvals*, the audit
  committee's omnibus approvals -> the quarterly related-party-transaction disclosures filed under LODR Reg 23(9),
  held in `data/quarterly_text/`.**
- **CSR spend — nil, and no CSR programme detail.** Annexure-6 and standalone Note 37 both record that the
  three-year average net profit is negative [AR FY26, p122–p124/pr143–145; p218/pr239]. **-> nothing to find
  elsewhere; the absence is the disclosure.**
- **Cost records — not maintained.** Board's Report §34 and CARO clause vi [AR FY26, p68/pr89; p159/pr180].
  **-> per-unit cost of production is not obtainable from any statutory source.**
- **Contingent liabilities — stated as nil**, both bases [AR FY26, Note 46, p228/pr249; Note 48, p309/pr330], and
  the auditor confirms *"The Company does not have any pending litigations which would impact its financial
  position"* [AR FY26, p153/pr174]. **-> for litigation that existed at the offer stage, the "Outstanding
  Litigation and Material Developments" section of `data/ipo/BLUESTONE-PROSPECTUS-2025.pdf`.**
- **Credit rating — Board's Report §38 and CG Report §XV(12) state no credit rating was obtained during FY26**
  [AR FY26, p69/pr90; p113/pr134] — notwithstanding ₹1,667.91 mn of redeemable NCDs outstanding at year end
  [AR FY26, Note 18, p201/pr222] and the ₹40,00,00,000 private placement of NCDs recorded in the Secretarial Audit
  Report [AR FY26, p82/pr103]. **-> the rating agency's rationale behind the company's 07-Aug-2026 rating
  intimation (GAP-004 in `data/source_register.md`); the debenture trust deed terms -> the private-placement offer
  letter / PAS-4, not held.**

### 6b. Absent although the doctrine needs it, and a peer or another document supplies it

| Missing | Why it matters | -> the document that would answer it |
|---|---|---|
| **Revenue disaggregation by product category (gold / studded / diamond / platinum / silver)** — Note 25(A) disaggregates only India-vs-outside-India and point-in-time-vs-over-time [AR FY26, p207/pr228] | Studded mix is the single largest driver of gross margin in this industry, and management's whole positioning rests on it | **-> the Titan, Kalyan, Senco and PN Gadgil FY2026 annual reports in `data/peer_text/`, all of which disclose a category split; and BlueStone's own investor presentations in `data/quarterly/`, which are marketing documents and can never carry an L1** |
| **Revenue split online vs offline vs franchisee** | The entire "omnichannel" thesis is a channel-mix claim | **-> the RHP/Prospectus "Our Business" and "Management's Discussion and Analysis" sections, `data/ipo/BLUESTONE-PROSPECTUS-2025.pdf`; and the quarterly investor presentations** |
| **Store count split COCO vs FOCO** — the policy note names both formats [AR FY26, Note 2.2.7, p174/pr195] and the balance sheet carries franchisee deposits and franchisee receivables [AR FY26, Notes 8 and 20, p187 and p203/pr208 and pr224], but no store count by format appears | Franchisee deposits are a financing line and franchisee interest is in finance costs; the number of franchise stores is the denominator | **-> the Prospectus "Our Business — Our store network" section; and the quarterly investor presentations** |
| **Average order value / average selling price / average ticket size** — the words do not appear in the document | The volume × realisation decomposition that doctrine L3 requires cannot be built from this document | **-> the RHP/Prospectus KPI section (BlueStone disclosed a KPI set at the offer stage, approved by the Audit Committee per CG Report §III(24) [p97/pr118]); and the quarterly investor presentations** |
| **Order count / transaction count / bill count** | Same L3 problem | **-> as above. The only piece-count in this document is the 13,43,067 digital certificates issued [AR FY26, p72/pr93], which is a certificate count, not an order count** |
| **Quantified same-store sales growth** — only the words *"healthy SSSGs across cohorts"* [AR FY26, p143/pr164] | The cohort claim on p13 and p28 is unfalsifiable without it | **-> the quarterly earnings-call transcripts and investor presentations in `data/quarterly_text/`; n=5 quarters** |
| **Store-level or cohort unit economics — capex per store, payback period, revenue per square foot** | Doctrine wave 4 requires "₹x of capital per ₹1 of revenue" | **-> the Prospectus "Our Business" unit-economics disclosure; the concalls** |
| **Gold-price sensitivity of revenue, and the volume/price split of the 37.9% growth** | The Chairman attributes an entry-level demand miss to the gold-price move [AR FY26, p25], but the document quantifies neither the move nor the effect | **-> the concall transcripts; the World Gold Council / Redseer data cited in the MD&A, which is itself a secondary source** |
| **A quarterly split of FY26** | The Chairman's *"exited the fourth quarter growing above 30%"* [AR FY26, p25] cannot be checked here | **-> the five quarterly results filings and board outcomes in `data/quarterly/`** |
| **Reconciliation of "Pre-IndAS EBITDA ₹181 crore at 7.4% margin"** [AR FY26, p24] | A non-GAAP measure that reverses Ind AS 116, stated once and never reconciled | **-> the FY26 investor presentation (Apr-2026) and the Q4FY26 earnings call, both in `data/quarterly/` — and per doctrine §5 a presentation can establish what management claimed but can never be the source of an L1** |
| **Any financial year before FY2025** — this AR presents FY2026 and FY2025 only; the four-year bar series on p26 is an unaudited chart in the design section with no note reference | The doctrine's trend tests | **-> the FY2025 annual report `data/bronze/BLUESTONE-AR-FY2025.pdf` for reported FY24/FY25; and the Restated Consolidated Summary Statements for FY23/FY24/FY25 in `data/ipo/BLUESTONE-PROSPECTUS-2025.pdf` — a DIFFERENT BASIS, never to be joined to reported figures without the basis stated on each point (state/TEMPLATES.md)** |
| **The subsidiary's own CARO report** — only the qualified clause numbers appear [AR FY26, p238/pr259] | Clause vii(a) says a statutory-dues problem exists in Ethereal House and gives no amount | **-> Ethereal House Private Limited's own audited financial statements, which the AGM notice says are on the company's website [AR FY26, Notice note 16, p34/pr55]; not held in `data/`** |
| **The list of employees drawing above ₹1,02,00,000 p.a.** (9 employees) | Concentration of managerial pay | **-> available only on inspection at the registered office; the AR omits it under the second proviso to §136(1) [AR FY26, p68/pr89]** |
| **Promoter share pledge / encumbrance** | Nothing in this AR states whether the promoter's 2,44,65,127 shares are encumbered; Note 16(j) and CG Report §XV(7)/(8) give holdings only [AR FY26, p200/pr221; p112/pr133] | **-> the promoter's SAST Reg 31(4) filing of 24-Jun-2026, which is a scanned image (GAP-002 in `data/source_register.md`) and must be read as an image; and the quarterly shareholding-pattern XBRLs `data/filings/SHP_*.xml`, which carry the pledge fields** |
| **Lock-in expiry schedule and post-listing selldown by pre-IPO holders** | The new-listing overlay in `state/LOOP.md` makes this mandatory | **-> the Prospectus "Capital Structure" lock-in table; the five shareholding-pattern XBRLs; `data/filings/insider.json`; and the bulk/block-deal data, which is SECONDARY until reconciled (GAP-003)** |
| **Quarter-by-quarter IPO proceeds deployment against the stated schedule** — this AR gives only the cumulative position at 31-Mar-2026 [AR FY26, Note 53, p231/pr252] | The capital-allocation record for a company with no other | **-> the four Monitoring Agency Reports and four Statements of Deviation in `data/quarterly/`** |
| **The deployment schedule the Prospectus promised** (year-wise) against which Note 53 should be read | Note 53 gives "Amount as proposed in the Offer Document" as a single total per object, not a schedule | **-> `data/ipo/BLUESTONE-PROSPECTUS-2025.pdf`, "Objects of the Offer"** |
| **Segment or geographic profitability** | Note 44/46 declare a single segment and a single geography [AR FY26, p228/pr249; p309/pr330] | **-> nowhere. The single-segment declaration is itself the finding; the peer set (Titan discloses CaratLane separately) is the comparator** |
| **Deferred tax asset recognition trigger** — Note 34(e) discloses an unrecognised gross DTA and states reasonable certainty "is not yet established" [AR FY26, p214/pr235] but gives no expiry profile of the carried-forward losses | Section 79 / eight-year expiry matters after a change in shareholding | **-> the income-tax returns, not a public document; partially -> the Prospectus "Statement of Tax Benefits" and the restated financial statements' tax notes** |
| **Gross margin** — the P&L is presented by nature, not by function; there is no "gross profit" line | The whole studded-mix argument | **-> derivable from Notes 27 and 28 by the ledger agent, with the arithmetic shown inline; management's own gross-margin claim is on p26 ("while maintaining gross margins") and is unquantified** |
| **Related-party pricing basis** — Note 35 records sales to the subsidiary and a sale of fixed assets to the subsidiary, but no arm's-length evidence is shown in the note | Doctrine materiality trigger 4 fires at any size | **-> the Audit Committee's approvals, disclosed in the LODR Reg 23(9) half-yearly RPT filings in `data/quarterly/`** |
| **Whistleblower complaints received in FY26** — CARO xi(c) confirms complaints were received and used in audit planning [AR FY26, p160/pr181]; the Vigil Mechanism section of the CG Report gives the process and states only that *"No personnel have been denied access to the Audit Committee"* [AR FY26, p106/pr127] — **the count is nowhere** | | **-> nowhere in the statutory record; this is a genuine disclosure gap and a concall question** |
| **Board-evaluation outcome detail** — Board's Report §16 names Potentia as the external evaluator and the Fidem platform, and lists four focus areas including *"Monitor a strong succession pipeline for the CEO role"* [AR FY26, p63–p64/pr84–85], but gives no scores | | **-> nowhere; the naming of an external evaluator and of CEO succession as a focus area is itself the disclosure** |
| **Gold-on-lease counterparties, security and covenants** — Note 24 discloses only *"external parties… variable interest rates ranging from 4% to 5%… tenure of such lease arrangements is 365 days"* [AR FY26, p206/pr227] | This is a large FY26-new financing line sitting inside Other current liabilities rather than in Borrowings or Gold on loan, and it is not in the Note 40 liquidity maturity table | **-> the concall transcripts; the CG Report §XVIII(f) Bullion Risk Management Policy description [p116/pr137]; and the Bullion Risk Management Policy itself, which is not in the AR** |
| **Reconciliation of the ₹40 crore FY26 NCD private placement to the Note 18 NCD balance movement** | The Secretarial Audit Report records the issuance [AR FY26, p82/pr103]; Note 18 shows the NCD balance falling year on year [AR FY26, p201/pr222]; neither reconciles issuance to redemption | **-> the corporate announcements in `data/filings/announcements_2025.json` / `announcements_2026.json`, and the board-outcome filings** |
| **Any restatement, reclassification or prior-period adjustment detail** — Note 55 / Note 58 say figures were *"regrouped/reclassified, wherever necessary"* without saying which [AR FY26, p231/pr252; p313/pr334]; Board's Report §7 separately states there were **no revisions to the financial statements in any of the three preceding financial years** [AR FY26, p49/pr70] | | **-> comparison of the FY2025 AR's FY2025 columns against this AR's FY2025 columns, which is the ledger agent's tie-out** |

---

## 7. Four warnings for every agent that reads this document after me

1. **Page 245 (printed 266) is titled "Standalone Statement of Cash Flows" and is the CONSOLIDATED cash flow
   statement.** Cite it by page and by the figures, and say "consolidated".
2. **Note numbers diverge between the two bases from Note 7 onward.** Use the crosswalk in §2A/2B. "Note 25" is
   Revenue on the standalone basis and Other liabilities on the consolidated basis.
3. **Three different scales are live in this one PDF** (₹ million in the statements, ₹ absolute rupees in AOC-1 and
   the Corporate Governance Report, ₹ crore and ₹ lakh in the chapters and Board's Report). Read the header of the
   page you are quoting, not the section.
4. **The unaudited chapters section (p6–p30) and the audited statements (p150–p313) do not use the same basis for
   the same metric.** The KPI chart on p26 mixes standalone FY26 with consolidated FY25. Anything taken from p6–p30
   is a management claim and must be tagged as such, never as an L1.

---

# PART 2 — Annual Report FY2025

# W1 — Document map: Annual Report FY2025 (BlueStone Jewellery and Lifestyle Limited)

**Agent:** A2 (Document Mapper, doctrine wave 1) · **Produced:** 2026-09-09
**Source:** `data/bronze/BLUESTONE-AR-FY2025.pdf` (230 PDF pages) · text `data/text/BLUESTONE-AR-FY2025.txt` (page-marked)
**Scope:** MAP ONLY. No series extracted, no interpretation, no S1–S6 findings, no chain records.
Every number below is a locator, carried with its tag so a later wave can pull the page.

---

## 0. Reading conventions for this document

**Unit.** The financial statements state on every page footer: *"(All amounts are in ` million unless
otherwise stated)"* `[AR FY25, Standalone BS, p97/pr92]`. The Board's Report financial summary table is
headed *"(INR in millions)"* `[AR FY25, Board's Report §1, p25/pr20]`. **Exception — the share-capital
narrative in the Board's Report and the AGM Notice is written in absolute rupees and the Indian
lakh/crore system**, e.g. authorised capital *"` 45,05,00,000/-"* `[AR FY25, Board's Report §8(a),
p26/pr21]`, and the AOC-1 annexure is *"(Amount in `)"* i.e. absolute rupees `[AR FY25, Annexure-2 Form
AOC-1, p49/pr44]`. Mixing the AOC-1 rupee figures with the ₹-million statements is the single largest
scale trap in this document.

**Page mapping (derived per document, not assumed).** PDF page − 5 = printed page, uniformly from PDF
p7 to PDF p230. Checks: PDF p7 prints "2/" (Shareholder Letter); PDF p25 prints "20/"; PDF p103 prints
"98/"; PDF p160 prints "/155"; PDF p230 prints "/225". PDF p1–p2 are the covering letter to BSE/NSE
dated 05-Sep-2025 and carry **no printed page number**; PDF p3–p6 (cover, corporate information, index)
are likewise unnumbered. Cite as `[AR FY25, <locator>, p<PDF>/pr<printed>]`.

**Tag shorthand used inside this artifact.** Every source in this document is the FY2025 annual report,
so after the first full citation the tags are written short. **Each of the following is shorthand for the
fully qualified form `[AR FY25, <locator>, p<PDF>/pr<printed>]` and must be expanded to it when quoted
into any downstream artifact:** `[SA <locator>, …]` = standalone financial statements or their notes ·
`[CFS <locator>, …]` = consolidated financial statements or their notes · `[Board's Report §n, …]` ·
`[CG Report <section>, …]` = Annexure-5 Corporate Governance Report · `[MD&A, …]` · `[Annexure-n, …]` ·
`[Auditor's Report — Standalone/Consolidated, …]` · `[CARO clause 3(x), …]` · `[AGM Notice …]` ·
`[Corporate Information, …]` · `[Shareholder Letter, …]`. No number appears anywhere below without one
of these locators plus a PDF page.

**Two signing dates inside one document — load-bearing.**

| Block | Signed / dated | Place |
|---|---|---|
| Standalone + Consolidated financial statements and both auditor's reports | **24 April 2025** | Bengaluru / Bangalore / Mumbai `[AR FY25, p89/pr84; p97/pr92; p163/pr158; p166/pr161]` |
| Secretarial Audit Report (Form MR-3), Kalaivani S | **24 April 2025** | Bangalore `[AR FY25, Annexure-3, p53/pr48]` |
| Board's Report, Corporate Governance Report, CSR Annexure-4, AGM Notice, PCS certificates (Parth Joshi & Co) | **04 September 2025** | Mumbai / Bangalore / Chandigarh `[AR FY25, p46/pr41; p80/pr75; p81/pr76; p56/pr51; p22/pr17]` |
| Annual Report submitted to exchanges | 05 September 2025 | `[AR FY25, covering letter, p1]` |

The report states the reason expressly: *"This Annual Report is re adopted and re approved at the Board
meeting held on September 04, 2025 post listing with a view to present the Annual Report to the
shareholders of the Company to provide full disclosures and transparent information even though the
shares of the Company were not listed as on 31 st March 2025."* `[AR FY25, Board's Report §10, p35/pr30]`
and repeated verbatim `[AR FY25, Corporate Governance Report preamble, p57/pr52]`.

**Consequence a later wave must not miss:** the financial statements were **not re-opened**. Everything
that happened between 24-Apr-2025 and 04-Sep-2025 — the 04-Jul-2025 CCPS conversion, the RHP, the
Prospectus, the IPO, the 19-Aug-2025 listing — appears **only in the Board's Report and Corporate
Governance Report**, and is **explicitly absent** from the audited subsequent-events notes (§4, §6, §10
below).

---

## 1. Structure table

| # | Block | PDF pages | Printed pages | Signed | Notes |
|---|---|---|---|---|---|
| 1 | Covering letter to BSE / NSE, submission of AR + AGM Notice | 1–2 | unnumbered | 05-Sep-2025, Gaurav Singh Kushwaha MD | Confirms AGM 29-Sep-2025 by VC; e-voting via NSDL |
| 2 | Report cover | 3 | unnumbered | — | "ANNUAL REPORT 2024-25" |
| 3 | Corporate Information — board, KMP, SMP, committees, auditors, RTA, exchanges, manufacturing units, bankers | 4–5 | unnumbered | — | States CIN `U72900KA2011PLC059678` with "(CIN Change is under Process)"; listing "with effect from August 19, 2025" |
| 4 | Index | 6 | unnumbered | — | Lists 9 blocks by printed page |
| 5 | **Shareholder Letter** | 7 | 2 | Gaurav Singh Kushwaha, MD | Unaudited narrative; the only place "~40%" standalone revenue growth and "275 stores across more than 100 cities" are asserted in the front section |
| 6 | **Notice of 14th AGM** + explanatory statement u/s 102 | 8–24 | 3–19 | 04-Sep-2025, Paras Shah CS | 3 ordinary + 2 special items; includes SH-13 / SH-14 nomination forms (p23–24/pr18–19) |
| 7 | **Board's Report** (52 numbered paragraphs) | 25–46 | 20–41 | 04-Sep-2025, Kushwaha (MD) + Sameer Dilip Nath (Director) | The capital-structure, ESOP, NCD, post-year-end and governance narrative all sit here |
| 8 | Annexure-1 — Dividend Distribution Policy | 47–48 | 42–43 | — | Policy text only; no dividend declared |
| 9 | Annexure-2 — Form AOC-1 (subsidiary + associate) | 49–50 | 44–45 | 04-Sep-2025 | **Absolute rupees**, not millions |
| 10 | Annexure-3 — Form MR-3 Secretarial Audit Report + its own Annexure letter | 51–53 | 46–48 | 24-Apr-2025, Kalaivani S, ACS 57112, CP 22158, UDIN A057112G000192808 | |
| 11 | Annexure-4 — CSR annual report | 54–56 | 49–51 | 04-Sep-2025 | Nil obligation, nil spend |
| 12 | **Annexure-5 — Corporate Governance Report** (sections I–XXII) | 57–79 | 52–74 | 04-Sep-2025 | Includes PCS Certificate on Corporate Governance (p80/pr75) |
| 13 | Annexure-6 — PCS Certificate of Non-Disqualification of Directors | 81 | 76 | 04-Sep-2025, Parth Joshi & Co, UDIN A047604G001169703 | |
| 14 | **Management Discussion and Analysis Report** | 82–85 | 77–80 | unsigned | Economy → industry → company overview → standalone financials → opportunities/threats/outlook → risks → internal controls → HR → ratio commentary |
| 15 | **Independent Auditor's Report — Standalone** + Annexure A (auditor responsibilities), Annexure B (CARO 2020), Annexure C (IFC u/s 143(3)(i)) | 86–96 | 81–91 | 24-Apr-2025, M S K A & Associates, FRN 105047W, Ankush Agrawal (M.No. 159694), UDIN 25159694BMLWGT7265 | |
| 16 | **Standalone financial statements** — Balance Sheet (p97), P&L (p98), SOCIE (p99–100), Cash Flows (p101–102) | 97–102 | 92–97 | 24-Apr-2025 | |
| 17 | **Notes to the Standalone financial statements** — Note 1 General Information, Note 2 Material Accounting Policies (2.1–2.20), Notes 3–57 | 103–159 | 98–154 | 24-Apr-2025 | |
| 18 | **Independent Auditor's Report — Consolidated** + Annexure A (responsibilities), Annexure B (IFC) | 160–165 | 155–160 | 24-Apr-2025, same partner, UDIN 25159694BMLWGU2463 | **No separate consolidated CARO annexure** — CARO is addressed inside para 3 of the main report (p163/pr158) |
| 19 | **Consolidated financial statements** — Balance Sheet (p166), P&L (p167), SOCIE (p168–169), Cash Flows (p170–171) | 166–171 | 161–166 | 24-Apr-2025 | |
| 20 | **Notes to the Consolidated financial statements** — Note 1, Note 2 (2.1–2.20), Notes 3–59 | 172–230 | 167–225 | 24-Apr-2025 | |

**No Business Responsibility and Sustainability Report and no ESG/BRSR section exists in this document**
(reason given at §6 below).

---

## 2. Note locator table

Both statement sets use the **same note numbers 1–50**; they diverge from note 51 onward. Standalone
runs to note 57, consolidated to note 59. Printed page = PDF − 5 throughout.

| Coverage item | Standalone note | SA PDF page | Consolidated note | CFS PDF page |
|---|---|---|---|---|
| General information / entity status | 1 | p103/pr98 | 1 | p172/pr167 |
| Material accounting policies (2.1 basis of preparation incl. **going concern 2.1(iv)**, 2.2 PPE, 2.3 intangibles, 2.4 impairment, 2.5 leases, 2.6 inventories, 2.7 FX, 2.8 revenue, 2.9 employee benefits, **2.10 share-based payments**, 2.11 financial instruments, 2.12 income tax, 2.13 provisions, 2.14 contingent liabilities, 2.15 cash, 2.16 cash flow, 2.17 segments, 2.18 EPS, 2.20 recent pronouncements) | 2 | p103–112/pr98–107 | 2 | p172–182/pr167–177 |
| Property, plant and equipment | 3 | p113/pr108 | 3 | p183/pr178 |
| Leases (ROU assets, lease disclosures 4(c)) | 4 | p114/pr109 | 4 | p184/pr179 |
| Capital work-in-progress (+ ageing) | 5 | p115/pr110 | 5 | p185/pr180 |
| Other intangible assets | 6.A | p116/pr111 | 6.A | p186/pr181 |
| Intangible asset under development | 6.B | p116–117/pr111–112 | 6.B | p187/pr182 |
| Investments — non-current / equity-method | 7 (Financial assets — Investments, non-current) | p117/pr112 | 7 (**Investments accounted for using the equity method**) | p187/pr182 |
| Other financial assets (non-current + current) | 8 | p118/pr113 | 8 | p188/pr183 |
| Non-current tax assets (net) | 9 | p118/pr113 | 9 | p188/pr183 |
| Deferred tax assets (net) — nil both years | 10 | p118/pr113 | 10 | p188/pr183 |
| Other assets (incl. **IPO expenses in prepaid**) | 11 | p119/pr114 | 11 | p189/pr184 |
| Inventories | 12 | p119/pr114 | 12 | p189/pr184 |
| Investments — current (mutual funds) | 13 | p120/pr115 | 13 | p190/pr185 |
| Loans | 14 | p120/pr115 | 14 | p190/pr185 |
| Trade receivables (+ ageing) | 15 | p120/pr115 | 15 | p190/pr185 |
| Cash and bank balances | 16 | p121/pr116 | 16 | p191/pr186 |
| Other bank balances | 17 | p122/pr117 | 17 | p192/pr187 |
| **Share capital** (authorised, issued, reconciliation, CCPS/OCRPS terms, bonus/rights history, >5% holders, promoter holding) | **18** | **p122–129/pr117–124** | **18** | **p192–199/pr187–194** |
| Other equity (securities premium, retained earnings, ESOP reserve, OCI) | 19 | p129–130/pr124–125 | 19 | p199–200/pr194–195 |
| Borrowings (NCDs, term loans, vehicle loans, OCRPS liability component, security, quarterly-return reconciliation with banks) | 20 | p131–133/pr126–128 | 20 | p201–204/pr196–199 |
| Lease liabilities | 21 | p134/pr129 | 21 | p204/pr199 |
| Other financial liabilities (franchisee deposits, RTS liability, phantom liability, derivatives) | 22 | p134–135/pr129–130 | 22 | p205/pr200 |
| Provisions (gratuity, compensated absence) | 23 | p135/pr130 | 23 | p205/pr200 |
| **Gold on loan** (gold metal loan) | 24 | p135/pr130 | 24 | p205/pr200 |
| Trade payables (+ MSME, ageing) | 25 | p136/pr131 | 25 | p206/pr201 |
| Other liabilities (gift vouchers, gold-mine scheme, advances) | 26 | p137/pr132 | 26 | p207–208/pr202–203 |
| **Revenue from operations** (Ind AS 115 disaggregation, contracted price → variable consideration reconciliation, contract balances) | 27 | p138/pr133 | 27 | p208/pr203 |
| Other income (incl. **fair value gain on call option**) | 28 | p139/pr134 | 28 | p209/pr204 |
| Cost of raw materials consumed | 29 | p139/pr134 | 29 | p209/pr204 |
| Change in inventories of FG and WIP | 30 | p139/pr134 | 30 | p209/pr204 |
| Employee benefits expense (**incl. ESOP charge line**) | 31 | p139/pr134 | 31 | p210/pr205 |
| Finance costs | 32 | p140/pr135 | 32 | p210/pr205 |
| Depreciation and amortization | 33 | p140/pr135 | 33 | p210/pr205 |
| Other expenses (+ auditors' remuneration sub-note) | 34 | p140–141/pr135–136 | 34 | p210–211/pr205–206 |
| Employee benefits (gratuity actuarial, defined contribution) | 35 | p141–143/pr136–138 | 35 | p212–214/pr207–209 |
| Income taxes (incl. unrecognised DTA / loss carry-forward) | 36 | p143/pr138 | 36 | p214/pr209 |
| **Related party disclosures** | 37 | p144–146/pr139–141 | 37 | p215–217/pr210–212 |
| Earnings per share | 38 | p147/pr142 | 38 | p217/pr212 |
| CSR expenditure | 39 | p147/pr142 | 39 | p217/pr212 |
| **Employee stock option plan** | **40** | **p147–148/pr142–143** | **40** | **p217–219/pr212–214** |
| Financial instruments — fair value measurement (incl. fair-value hierarchy) | 41 | p149–150/pr144–145 | 41 | p219–220/pr214–215 |
| Financial instruments — risk management: (a) framework + **commodity price risk / hedging**, (b) credit risk + ECL, (c) liquidity risk + maturity ladder, (d) market risk — currency (p153/pr148), interest rate (p154/pr149) | 42 | p150–154/pr145–149 | 42 | p220–224/pr215–219 |
| Capital management (adjusted net debt / adjusted equity) | 43 | p154–155/pr149–150 | 43 | p224/pr219 |
| **Analytical ratios** (11 ratios + variance explanations) | 44 | p155/pr150 | 44 | p225/pr220 |
| Relationship with struck-off companies | 45 | p156/pr151 | 45 | p226/pr221 |
| Operating segments (single segment; domestic/export split) | 46 | p156/pr151 | 46 | p226/pr221 |
| Phantom Option Scheme 2016 | 47 | p156/pr151 | 47 | p226/pr221 |
| InnoVen "right to subscribe" (RTS) termination | 48 | p157/pr152 | 48 | p226/pr221 |
| Commitments and contingencies | 49 | p157/pr152 | 49 | p226/pr221 |
| Other statutory information (benami, crypto, wilful defaulter, s.186 ICDs) | 50 | p157/pr152 | 50 | p226–228/pr221–223 |
| **Schedule III "Additional information on the entities included in the CFS"** (net assets / share in P&L by entity) | — *(n/a)* | — | 50(ix) | p228/pr223 |
| Investment in associate company (Ind AS 112) | — | — | **51** | p228/pr223 |
| Non-controlling interest (balance-sheet reference) | — | — | 51 (referenced from CFS BS) | p166/pr161, p228/pr223 |
| Audit trail compliance | **51** | p158/pr153 | **52** | p228–229/pr223–224 |
| Maintenance of books of accounts on server in India | 52 | p158/pr153 | 53 | p229/pr224 |
| **Fair value of contingent call options (Ethereal House)** | 53 | p158/pr153 | 54 | p229/pr224 |
| ESOP trust and treasury shares | 54 | p158/pr153 | 55 | p229/pr224 |
| Acquisition of Ethereal House Private Limited (Ind AS 103 assessment) | — *(not in SA)* | — | **56** | p229/pr224 |
| Investment in subsidiary and associate | 55 | p158–159/pr153–154 | 57 | p230/pr225 |
| Events after the reporting period | **56** | p159/pr154 | **58** | p230/pr225 |
| **Regrouping / reclassification of previous-year figures** | **57** | p159/pr154 | **59** | p230/pr225 |

**Note-numbering trap for later waves.** From note 51 the two sets are **offset by one** (SA 51 audit trail
= CFS 52; SA 53 call option = CFS 54; SA 56 subsequent events = CFS 58), and the offset widens to two at
CFS note 56. A citation of "Note 53" is ambiguous unless the statement set is named.

---

## 3. Standalone vs consolidated map

**Group perimeter as at 31-Mar-2025** `[AR FY25, Board's Report §12, p35/pr30]` and `[AR FY25, CFS Note
50(ix), p228/pr223]`:

| Entity | CIN | Relationship | Basis of inclusion | Date acquired |
|---|---|---|---|---|
| BlueStone Jewellery and Lifestyle Limited | U72900KA2011PLC059678 | Parent | — | — |
| Ethereal House Private Limited (EHPL) | U32111HR2024PTC124350 | **Subsidiary**, 75.51% on a diluted basis (without ESOP pool) | Line-by-line consolidation from date of control | SSA/SHA 06-Jan-2025; shares allotted 13-Jan-2025 `[AR FY25, Form AOC-1, p49/pr44]` |
| Redefine Fashion Private Limited | U74101KA2024PTC191944 | **Associate**, 51.19% on a diluted basis (without ESOP pool) | **Equity method** | SHA 11-Nov-2024; shares allotted 15-Nov-2024 `[AR FY25, Form AOC-1 Part B, p50/pr45]` |

No joint ventures; no entity ceased to be a subsidiary/associate during the year `[AR FY25, Board's
Report §12, p36/pr31]`.

**Reconciling map, SA → CFS (Rs. million, FY2025):**

| Line | Standalone | Consolidated | Difference | Where the difference is explained |
|---|---|---|---|---|
| Revenue from operations | 17,700.02 `[SA P&L, p98/pr93]` | 17,700.02 `[CFS P&L, p167/pr162]` | nil — EHPL turnover is nil `[Form AOC-1, p49/pr44]` | — |
| Other income | 599.18 `[SA Note 28, p139/pr134]` | 600.34 `[CFS Note 28, p209/pr204]` | +1.16 | EHPL other income Rs 1.15 mn `[Board's Report §12, p35/pr30]` |
| Total expenses | 20,491.34 `[SA P&L, p98/pr93]` | 20,499.29 `[CFS P&L, p167/pr162]` | +7.95 | EHPL expenses Rs 8.00 mn `[Board's Report §12, p35/pr30]` |
| Loss before tax | (2,192.14) | (2,218.37) | (26.23) | (6.79) EHPL + (19.44) share of associate loss `[CFS P&L, p167/pr162; CFS Note 51, p228/pr223]` |
| Share of loss of equity-method investment | not applicable | (19.44) | — | CFS Note 51, p228/pr223 |
| Loss attributable to owners / NCI | n/a | (2,216.69) / (1.68) | — | CFS P&L, p167/pr162 |
| Basic and diluted EPS (Rs) | (78.86) `[SA Note 38, p147/pr142]` | (79.74) `[CFS Note 38, p217/pr212]` | (0.88) | — |
| Total assets | 35,346.17 `[SA BS, p97/pr92]` | 35,322.81 `[CFS BS, p166/pr161]` | (23.36) | Investment in sub/associate (272.98) eliminated / re-presented; equity-method investment 85.56 introduced |
| Investments — non-current | 272.98 (cost of EHPL 167.98 + RFPL 105.00) `[SA Note 7, p117/pr112; SA Note 55, p158/pr153]` | replaced by "Investments accounted for using the equity method" 85.56 `[CFS Note 7, p187/pr182]` | — | — |
| Total equity | 9,133.44 | 9,107.40 (owners 9,067.74 + NCI 39.66) `[CFS BS, p166/pr161]` | (26.04) | — |
| Retained earnings (closing) | (24,517.62) `[SA Note 19, p129/pr124]` | (24,583.31) `[CFS Note 19, p199/pr194]` | (65.69) | Includes "Adjustments for changes in ownership interests" (41.14) `[CFS SOCIE, p168/pr163]` |
| Net cash used in operating activities | (6,648.41) `[SA CFS, p101/pr96]` | (6,658.28) `[CFS CFS, p170/pr165]` | (9.87) | — |
| Net cash used in investing activities | (909.53) | (842.33) | +67.20 | SA carries "Payment for acquisition of subsidiary (167.98)" `[SA CFS, p101/pr96]` |
| Net cash from financing activities | 7,397.16 | 7,397.01 | (0.15) | — |
| Closing cash and cash equivalents | 430.57 | 487.75 | +57.18 | EHPL cash |

**Schedule III entity table** (the CFS-only disclosure a later wave will need for the group-vs-parent
split): parent 98.26% of consolidated net assets (Rs 9,133.44 mn) and 99.69% of the consolidated loss;
EHPL 1.74% (Rs 161.34 mn) and 0.31%; adjustment on consolidation (252.71) net assets and (1.62) loss;
NCI (39.66) and 1.68; associate 105.00 and (19.44) `[AR FY25, CFS Note 50(ix), p228/pr223]`.

**Which set the Board's Report uses.** §1 prints a three-column table — Standalone FY25, Standalone FY24,
**Consolidated FY25 only** (no consolidated FY24, because there was no group in FY24) `[AR FY25, Board's
Report §1, p25/pr20]`. §2 "State of the Company's Affairs" discusses **standalone only**
`[p25/pr20]`. **The MD&A is standalone only** and says so in its table heading *"Standalone Financial
Performance (₹ in Million)"* `[AR FY25, MD&A, p83/pr78]`. The Board's Report ESOP table, however, quotes
diluted EPS of ` (79.74) `[AR FY25, Board's Report §8(b), p32/pr27]`, which is the **consolidated** figure,
not the standalone (78.86) — a basis mismatch inside the statutory report.

**Consolidation policy** is in CFS Note 2.1 (p172–174/pr167–169), including the Ind AS 103 discussion for
EHPL at CFS Note 56 (p229/pr224).

---

## 4. Auditor block

### 4.1 Statutory auditor identity and tenure

| Item | Detail | Tag |
|---|---|---|
| Firm | **M S K A & Associates**, Chartered Accountants, Mumbai · ICAI FRN **105047W** | `[AR FY25, Board's Report §22, p40/pr35]` |
| Signing partner | **Ankush Agrawal**, Membership No. 159694 | `[AR FY25, p89/pr84]` |
| UDIN — standalone | 25159694BMLWGT7265 | `[AR FY25, p89/pr84]` |
| UDIN — consolidated | 25159694BMLWGU2463 | `[AR FY25, p163/pr158]` |
| Appointed | AGM of **30 September 2023**, for five years to the AGM for FY2027-28 | `[AR FY25, Board's Report §22, p40/pr35]` |
| Resignation during year | *"There has been no resignation of the statutory auditors during the year"* | `[AR FY25, CARO clause 3(xviii), p94/pr89]` |
| Internal auditor | **Nexdigm Private Limited** (s.138) | `[AR FY25, Board's Report §25, p40/pr35]` |
| Secretarial auditor FY25 | **Kalaivani S**, PCS, ACS 57112 / CP 22158 | `[AR FY25, Annexure-3, p53/pr48]` |
| Secretarial auditor proposed FY26–FY30 | **Mihen Halani & Associates**, remuneration ` 1,00,000 for FY2025-26 | `[AR FY25, Notice Item 4 explanatory statement, p20/pr15]` |
| Corporate-governance / non-disqualification certifier | **Parth Joshi & Co**, PCS | `[AR FY25, p80/pr75; p81/pr76]` |
| Audit fees (CG Report XIX, consolidated basis, absolute rupees) | Statutory audit incl. consolidated ` 34,50,000; taxation NIL; other services NIL; reimbursements ` 1,38,000; **total ` 35,88,000** | `[AR FY25, CG Report XIX, p77/pr72]` |
| Audit fees (Note 34(a), Rs mn) | Statutory audit 3.35 + reimbursement 0.13 = **3.48** (FY24: 2.35) | `[AR FY25, SA Note 34(a), p141/pr136]` |
| **IPO-related auditor fees excluded from the above** | *"Excludes fees paid to auditors amounting to ` 14.09 million (including reimbursement of expenses) and fees paid to **erstwhile auditors** ` 16.07 million (including reimbursement of expenses) for the year ended 31 March 2025 (31 March 2024 - Nil) in connection with the initial public offer ... which has currently recognized under prepaid expenses (other current assets)."* | `[AR FY25, SA Note 34(a) footnote, p141/pr136]` |

> The phrase **"erstwhile auditors"** is the only reference in this document to a predecessor audit firm,
> and the firm is **not named**. NOT DISCLOSED: identity of the erstwhile auditor and the date/reason of
> the change -> would be answered by the Prospectus/RHP "Our Statutory Auditors — changes in auditors in
> the last three years" section (`data/ipo/BLUESTONE-PROSPECTUS-2025.pdf`).

### 4.2 Opinion

| | Standalone | Consolidated |
|---|---|---|
| Opinion type | **Unmodified / unqualified** — "give a true and fair view ... of the state of affairs of the Company as at 31 March 2025, and its loss (including other comprehensive loss), changes in equity and its cash flows" `[p86/pr81]` | **Unmodified / unqualified** — "of the consolidated state of affairs of the Group and its associate as at 31 March 2025, and of its consolidated loss ..." `[p160/pr155]` |
| Reporting framework | Ind AS, s.133 | Ind AS, s.133 |
| Internal financial controls opinion (s.143(3)(i)) | **Adequate and operating effectively** as at 31-Mar-2025 `[Annexure C, p95/pr90]` | **Adequate and operating effectively** for Holding + subsidiary; **IFC reporting not applicable to the associate** per MCA notification GSR 583(E) dated 13-Jun-2017 `[Annexure B, p164/pr159]` |

### 4.3 Key Audit Matters

**ABSENT — there is no Key Audit Matters section in either auditor's report.** The standalone report runs
Opinion → Basis for Opinion → Information Other than the Financial Statements → Responsibilities of
Board → Auditor's Responsibilities → Report on Other Legal and Regulatory Requirements `[p86–89/pr81–84]`,
with no SA 701 section interposed; the consolidated report has the same sequence `[p160–163/pr155–158]`.
A text search of the whole 230-page document returns **no occurrence of "Key Audit Matter"**. This is
consistent with SA 701 applying to listed entities — the Company was unlisted for the whole of FY2025 —
but it means **the auditor has named no account balance as a focus of the audit**, and the doctrine §3
trigger 6 ("the auditor named it") therefore fires on nothing in this year.

### 4.4 Emphasis of Matter / Other Matter / Material Uncertainty

- **No Emphasis of Matter paragraph** in either report (no occurrence of the phrase in the document).
- **No Material Uncertainty Related to Going Concern paragraph**, notwithstanding management's own going-
  concern discussion at SA Note 2.1(iv) (p103/pr98) and CFS Note 2.1(iv) (p172–173/pr167–168), which
  discloses a loss of Rs 2,192.14 mn and **accumulated losses of Rs 24,517.62 mn** (consolidated: loss
  Rs 2,218.37 mn, accumulated losses Rs 24,583.31 mn) `[SA Note 2.1(iv), p103/pr98; CFS Note 2.1(iv),
  p172/pr167]`.
- **No Other Matter paragraph** identifying financial statements of components audited by other auditors
  — even though the consolidated report's para 3 refers to *"CARO reports issued by the statutory auditors
  of the subsidiary company"* `[p163/pr158]`, implying a component auditor exists. NOT DISCLOSED: the
  identity of EHPL's and RFPL's statutory auditors, and whether the parent auditor relied on their work
  -> would be answered by EHPL's / RFPL's own filed accounts (MCA) or by the Prospectus.

### 4.5 The reservation the Board's Report says does not exist

Both audit reports carry a **reservation on the maintenance of books of account**, worded as a carve-out
rather than as a qualification of opinion:

- Standalone para 2(b): *"proper books of account as required by law have been kept by the Company so far
  as it appears from our examination of those books **except for the matters stated in paragraph 2(h)(vi)
  below on reporting under Rule 11(g)**"* `[AR FY25, Auditor's Report — Standalone, para 2(b), p87/pr82]`.
- Standalone para 2(f): *"**The reservation relating to the maintenance of accounts** and other matters
  connected therewith are as stated in paragraph 2(b) above ... and paragraph 2(h)(vi) below on reporting
  under Rule 11(g)."* `[p87/pr82]`.
- Consolidated para 1(b): *"proper books of account ... have been kept so far as it appears from our
  examination of those books, **except for not complying with the requirement of audit trail** as stated
  in 1(h)(vi) below."* `[p161/pr156]`; and para 1(f) repeats the "reservation" wording `[p161/pr156]`.

The Rule 11(g) content itself (standalone p88–89/pr83–84; consolidated p162–163/pr157–158):

| Entity | Auditor's Rule 11(g) statement | Company's own note |
|---|---|---|
| Holding Company — pre-migration software | audit trail operated at application level, but *"we are unable to comment on audit trail at database level due to absence of SOC I Type II report"* | SA Note 51 / CFS Note 52 |
| Holding Company — **migrated to a new accounting software on 1 October 2024** | again unable to comment at database level, *"due to absence of adequate coverage in SOC 1 Type II report"* | SA Note 51 (p158/pr153); CFS Note 52 (p228/pr223) |
| Holding Company — a further third-party-maintained software | *"in absence of sufficient and appropriate audit evidence including SOC I Type II report we are unable to comment whether the accounting software has a feature of recording audit trail"* | SA Note 51 |
| **Subsidiary (EHPL)** | *"the Company has used an accounting software for maintaining its books of account **which do not have a feature of recording audit trail (edit log) facility**"* | CFS Note 52 (p229/pr224) |
| **Associate (RFPL)** | unable to comment whether audit trail existed or operated for the period 12-Aug-2024 to 31-Mar-2025 | CFS Note 52 (p229/pr224) |

**Against this, the Board's Report states:** *"The statutory auditors of the Company have made no
observations, reservations, adverse remarks, disclaimers or qualifications."* `[AR FY25, Board's Report
§23, p40/pr35]`, and the Corporate Governance Report states *"the auditor's report on standalone and
consolidated financial statements of the Company for the financial year ended March 31, 2025 are
unqualified"* `[AR FY25, CG Report XX(e)(a), p78/pr73]`. **Both positions are recorded here without
adjudication**, per doctrine §10 "Contradiction adjudication"; the contradiction is between a directors'
assertion and the auditor's own paragraph headed "reservation" in the same document.

### 4.6 CARO 2020 — clauses reported, and the exceptions

Standalone CARO is **Annexure B**, PDF p91–94 / pr86–89. There is **no separate consolidated CARO
annexure**; the consolidated report disposes of CARO in one sentence: *"we report that there are no
qualifications/adverse remarks"* `[p163/pr158]`.

**Clauses where the auditor reported something other than "not applicable" or a clean pass:**

| Clause | What the auditor said | Tag |
|---|---|---|
| **3(iii)(a)** | *"During the year, the Company has made investment in a subsidiary company amounting to ` 167.98 million and in an associate amounting to ` 105.00 million (refer note 7 ...)"* | p91–92/pr86–87 |
| **3(ii)(b)** | Working-capital limits **in excess of ` 5 crores** sanctioned against security of current assets; quarterly returns **are in agreement** with books | p91/pr86 |
| **3(ix)(c)** | Term-loan money **applied for the purpose raised**; refers to Note 20 | p93/pr88 |
| **3(x)(a)** | *"the Company did not raise any money by way of initial public offer or further public offer ... during the year"* — the IPO is outside FY2025 | p93/pr88 |
| **3(x)(b)** | **Preferential allotment of shares made during the year**; s.42 and s.62 complied with; amount used for the purposes raised | p93/pr88 |
| **3(xi)(c)** | *"We have taken into consideration the **whistle blower complaints received by the Company during the year** while determining the nature, timing, and extent of audit procedures."* — the number of complaints is **not stated by the auditor** | p93/pr88 |
| **3(xvii)** | **Cash losses in both years**: FY2025 Rs **236.29** mn; FY2024 Rs **469.72** mn (` million) | p94/pr89 |
| **3(xix)** | No material uncertainty about meeting liabilities falling due within one year — with the explicit caveat *"this is not an assurance as to the future viability of the Company"* | p94/pr89 |
| **3(xx)** | s.135(5) CSR spend not required — no average net profits in the three preceding years | p94/pr89 |

Clean or not-applicable: 3(i)(a)–(f) fixed assets and title deeds (no immovable property, no revaluation,
no benami proceedings); 3(ii)(a) inventory physically verified, **no class with 10%+ discrepancy**;
3(iii)(b)–(f), 3(iv), 3(v) deposits, 3(vi) cost records, 3(vii)(a)–(b) statutory dues (none in arrears >6
months, none unpaid on account of dispute), 3(viii) no unrecorded surrendered income, 3(ix)(a) **no
default in repayment of loans or interest**, 3(ix)(b) not a wilful defaulter, 3(ix)(d)–(f), 3(xi)(a) **no
material fraud noticed or reported**, 3(xi)(b) no ADT-4 required, 3(xii) not a Nidhi, 3(xiii) RPTs
compliant with s.177/188 and disclosed, 3(xiv)(a)–(b) internal audit system commensurate, 3(xv) no
non-cash transactions with directors, 3(xvi)(a)–(d) not an NBFC/CIC, 3(xviii) no auditor resignation,
3(xxi) not applicable to standalone.

*(Typographical note for later citation: the CARO annexure mislabels internal audit as clause "xi" where
it should be "xiv" `[p93/pr88]`.)*

---

## 5. Where management makes claims

Ordered by how far the claim sits from an audited number.

| # | Location | Claim class | Specific claims a later wave must test |
|---|---|---|---|
| 1 | **Shareholder Letter**, p7/pr2, signed Gaurav Singh Kushwaha MD | Unaudited narrative, no numbers tied to notes | "275 stores across more than 100 cities"; "Standalone revenues grew by ~40% year-on-year, led by **healthy same-store sales growth**"; "despite a **record upward movement in gold prices** during FY25, which impacted consumer decision-making"; "even with this front-loaded spend, we **continued to operate with positive EBITDA**"; long-term profitability "underpinned by ... operating leverage from scale benefits in A&P and corporate costs, manufacturing efficiencies ... and improving store-level economics as newer stores mature"; "added more than 80 new stores" |
| 2 | **Board's Report §2**, p25/pr20 | Restatement of audited standalone P&L | Revenue 17,700.02; other income 599.18; total expenses 20,491.35; loss 2,192.15 — all tie to the SA P&L p98/pr93 (rounding of 0.01 on loss and expenses) |
| 3 | **Board's Report §8(b) and the SBEB disclosure table**, p29–33/pr24–28 | ESOP scheme disclosure under SEBI SBEB Regs Reg. 14 / Sch. I Part F | Grants 20,56,016; vested 9,03,797; exercised/modified 15,08,947; shares issued on exercise 15,00,243; lapsed 50,403; in force 35,48,669; **"stock option compensation cost of INR 512.39 million"**; weighted-average fair value ` 540.29; volatility 41.57%; risk-free 6.44%; expected life 4–7 years; **"the Company was unlisted as at the date of preparation of the financial results ... expected volatility ... determined based on the historical volatility of comparable listed entities (peer group)"**; underlying share price at grant ` 315 to ` 578 |
| 4 | **Board's Report §10 "Material events after end of financial year"**, p34–35/pr29–30 | Post-balance-sheet, post-audit events | CCPS conversion 04-Jul-2025; UDRHP 18-Jul-2025; RHP 05-Aug-2025; Prospectus 14-Aug-2025; listing/trading approval 18-Aug-2025; listing 19-Aug-2025; post-IPO paid-up capital ` 15,13,20,372 |
| 5 | **Board's Report §27 and §51**, p41/pr36 and p46/pr41 | Directors' assertions on controls | "the Company has maintained internal controls that are **appropriate for its size and the nature of its operations**"; Directors' Responsibility Statement including "internal financial controls ... are adequate and are operating effectively" and going-concern basis |
| 6 | **Board's Report §23 and §24**, p40/pr35 | Assertion about the auditors | "no observations, reservations, adverse remarks, disclaimers or qualifications" (see §4.5 above); "the Statutory Auditors, the Internal Auditors and the Secretarial Auditors have **not reported any instances of frauds**" |
| 7 | **Board's Report §32**, p41/pr36 | Related-party assertion | All RPTs "in the ordinary course of business and on an **arm's length basis**. Therefore, reporting in **Form AOC-2 is not required**" |
| 8 | **Board's Report §42 / CG Report XX(k)**, p43/pr38 and p79/pr74 | POSH | 3 complaints filed FY25, 3 disposed, nil pending, nil pending >90 days |
| 9 | **Corporate Governance Report I**, p57/pr52 | Governance philosophy | "commitment to ethical conduct, transparency, and accountability"; "Corporate Governance is not just a destination, but a journey" |
| 10 | **CG Report XX(f) + table**, p78–79/pr73–74 | **Commodity hedging — the most testable single claim in the document** | Gold exposure as at 31-Mar-2025 **Rs 3,278.75 million / 370 Kgs**, and **"% of such exposure hedged through commodity derivatives ... Domestic OTC 100% ... Total 100%"**; mechanism described as (a) gold on lease from banks priced only at customer sale, (b) sell-future/forward against customer-exchange and spot gold, MTM daily; governed by a Board-approved "Bullion Risk Management Policy" reviewed quarterly by a Bullion Risk Management Committee of senior management |
| 11 | **CG Report XX(e)(a)**, p78/pr73 | Assertion about the audit reports | "unqualified" (see §4.5) |
| 12 | **MD&A — Industry**, p82/pr77 | Market sizing, unsourced | Indian domestic gems & jewellery market "valued at **over ₹ 5 trillion**"; six named structural shifts |
| 13 | **MD&A — Company overview**, p82/pr77 | Business model | "over 8,000 active designs"; "**275 stores across 117 cities as of March 31, 2025**" (note: the Shareholder Letter says "more than 100 cities"); "Just-in-time production for certain SKUs **minimises working capital requirements**" |
| 14 | **MD&A — Standalone Financial Performance table**, p83/pr78 | **Non-GAAP measure with no reconciliation** | **EBITDA 758.85 (FY25) vs 530.49 (FY24), +43.05%; EBITDA margin 4.29% vs 4.19%**. EBITDA does not appear on the face of the P&L and **no reconciliation to loss before tax is given anywhere in the document** |
| 15 | **MD&A — Key highlights**, p83/pr78 | Driver attribution (doctrine L3 input) | Growth "driven by a combination of **robust same-store sales growth**, a well-planned store expansion strategy, and **enhanced online conversions**"; "expansion was **balanced between company-owned and franchise formats**"; "**Inventory Efficiency** — ... reduced working capital requirements"; "reduced acquisition costs" |
| 16 | **MD&A — Outlook**, p84/pr79 | Forward commitments (promise-vs-delivery seed) | "plans to **significantly increase its retail footprint in FY 2026**"; product portfolio diversification into daily-wear and gifting; deeper omni-channel integration; operational efficiencies from supply-chain tech, vendor partnerships, design automation |
| 17 | **MD&A — Risks and Concerns**, p84/pr79 | Named risks | **dependency on a limited number of vendors** for gold/diamonds/gemstones and for certain manufacturing processes; regulatory change; metal price volatility; cybersecurity/data privacy; competition; seasonality; FX on imported raw materials |
| 18 | **MD&A — HR**, p85/pr80 | Workforce | **1,943 full-time employees** and **1,264 contract workers** at manufacturing facilities as at 31-Mar-2025 |
| 19 | **MD&A — ratio commentary**, p85/pr80 | Explanation of ratio movements, ending with a pointer out of the document | Current ratio 1.24 from 0.94; gross debt-equity 1.67 from 2.46 "driven by the **infusion of share capital (H Series)**"; RoE −34.05% from −94.09%; receivables turnover 443.48 from 735.86; net capital turnover 10.99 from (16.30) "on account of higher inventory levels as we opened significant new stores". Closes: ***"For more detail, please refer the Company's prospectus filed with SEBI."*** |
| 20 | **SA Note 2.1(iv) / CFS Note 2.1(iv) — Going concern**, p103/pr98 and p172–173/pr167–168 | Management's own going-concern basis | Net current assets exceed net current liabilities by **Rs 4,128.88 mn** (consolidated **Rs 4,286.32 mn**); CCPS raised in the year for **Rs 7,091.46 mn**; "**regulatory approval on its draft red herring prospectus for its IPO** and strategic expansion plans" cited as part of the basis |
| 21 | **Note 44 Analytical Ratios — "Explanation for the variance" column**, p155/pr150 and p225/pr220 | Management's own causal attributions, inside the audited notes | Debt-equity and RoE movements both attributed to "increase in share capital (H Series)"; net capital turnover to "increase in inventory"; receivables turnover to "increase in trade receivables" |
| 22 | **Note 42(a) risk framework**, p150–151/pr145–146 | Hedging narrative inside the audited notes | Designation of derivative contracts as hedging instruments; commodity price risk carrying values |
| 23 | **CFS Note 56 — Acquisition of Ethereal House**, p229/pr224 | Accounting judgement asserted by management | EHPL "**lacked any substantive process, organized workforce, or other economic resources**", so not a business combination under Ind AS 103 and **not an asset acquisition either**; treated as a "corporate control transaction"; **no goodwill, capital reserve or revaluation recognised** |
| 24 | **SA Note 53 / CFS Note 54 — contingent call options**, p158/pr153 and p229/pr224 | Level-3 fair value taken to P&L | Rs **52.16 mn** recognised as a financial asset at FVTPL, valued by **Monte Carlo simulation** on projected revenues, EBITDA margins and net asset values, with volatility from comparable listed companies and FIMMDA risk-free rates; recognised in **Other income** `[SA Note 28, p139/pr134]` |

---

## 6. What is absent

Each entry names the document that would answer it, per doctrine §1a-iii.

**A. Absent because the Company was unlisted for the whole of FY2025 (the report says so)**

1. **No Business Responsibility and Sustainability Report (BRSR).** *"The Company was not classified among
   the top 1,000 listed entities as of December 31, 2024 as it was not listed at the time."* `[AR FY25,
   Board's Report §49, p46/pr41]` -> AR FY2026 (`data/bronze/BLUESTONE-AR-FY2026.pdf`) is the first place a
   BRSR could appear.
2. **No Reg. 17–27 / Reg. 46(2)(b)–(i) corporate-governance compliance disclosure.** *"Not applicable since
   during the period under review, the Company was not a listed company."* `[AR FY25, CG Report XX(j),
   p79/pr74]` -> AR FY2026.
3. **No quarterly-results publication, no newspaper publication, no analyst/institutional presentations,
   no schedule of analyst meets.** All four are declared not required because the Company was unlisted
   `[AR FY25, CG Report XVI-C "Means of Communication", p74/pr69]` -> quarterly filings from Q1FY26
   (`data/quarterly_text/`).
4. **No share-price data, no monthly high/low, no performance-versus-index chart, no market
   capitalisation** anywhere in the General Shareholder Information section `[AR FY25, CG Report XVII
   items 1–17, p74–77/pr69–72]` -> BSE/NSE price history; AR FY2026.
5. **No Reg. 32(7A) disclosure of utilisation of preferential-allotment funds.** *"Not applicable since the
   Company was not a listed company during the review period."* `[AR FY25, CG Report XX(l), p79/pr74]` and
   `[Board's Report §6, p26/pr21]` — **even though a preferential allotment (Series H CCPS, Rs 5,978.39 mn
   of preference-share proceeds) did occur in the year** `[SA Cash Flow, p101/pr96]` -> Prospectus
   "Capital Structure" and "Objects of the Offer".
6. **No credit rating of any kind.** *"Your Company did not obtain any credit ratings for its securities
   during the year."* `[AR FY25, Board's Report §41, p43/pr38; CG Report XVII item 15, p76/pr71]` —
   notable given Rs 4,050 mn of unlisted NCDs issued in FY2025 (§9 below) -> the 07-Aug-2026 rating
   intimation and the agency's rationale (GAP-004 in `data/source_register.md`).
7. **No postal ballots and no resolutions passed by postal ballot during FY2024-25** `[AR FY25, CG Report
   XVI-B, p74/pr69]` -> the Jan-2026 and Jun-2026 postal ballots in `data/quarterly_text/`.
8. **No Reg. 33 audited/limited-review quarterly numbers.** The document contains **no quarterly
   split of any line item**; FY2025 exists only as a full year -> Q1FY26 onward filings; the Prospectus
   restated interim statements.

**B. Absent from the audited financial statements themselves**

9. **No Key Audit Matters, no Emphasis of Matter, no Other Matter, no Material Uncertainty paragraph** in
   either auditor's report (§4.3, §4.4) -> AR FY2026 auditor's report, where SA 701 becomes applicable.
10. **No subsequent-events disclosure of the IPO or the CCPS conversion in the notes.** SA Note 56:
    *"the Company is not aware of any events or transactions that would require recognition or disclosure"*
    `[p159/pr154]`; CFS Note 58 identical `[p230/pr225]`. Both were evaluated only "up through 24 April
    2025" -> Board's Report §10 (p34–35/pr29–30) inside this same document, and the Prospectus.
11. **No revenue disaggregation beyond Domestic/Export and point-in-time/over-time.** Note 46 declares a
    single operating segment `[p156/pr151]`; Note 27 gives only Sale of products in total `[p138/pr133]`.
    **No split by product (gold / studded / diamond / platinum), by channel (online vs store), by store
    format (COCO vs franchise), by city tier, or by geography within India** -> Prospectus "Our Business"
    and the FY26 investor presentations (`data/quarterly_text/`, `data/index/filing_index.json`).
12. **No store-level or unit-economics data in the audited section.** Store count (275) and city count
    (117) appear **only in the MD&A** `[p83/pr78]`, with no ASP, no average order value, no same-store
    sales growth number (the phrase is used, the number is not given), no store-maturity cohort table, no
    revenue per store, no capex per store -> Prospectus and the FY26 investor presentations.
13. **No customer-concentration or vendor-concentration quantification.** MD&A names "dependency on a
    **limited number of vendors**" as a risk `[p84/pr79]`; no number, no share, no named counterparty is
    given anywhere -> Prospectus "Risk Factors" and "Our Business — Suppliers".
14. **No contingent liabilities.** *"the Company has assessed its obligations and confirms that there are no
    contingent liabilities requiring disclosure."* `[SA Note 49, p157/pr152; CFS Note 49, p226/pr221]`, and
    the auditor states there are **no pending litigations which would impact its financial position**
    `[p87/pr82]` -> Prospectus "Outstanding Litigation and Material Developments", which uses a materiality
    threshold rather than a financial-impact test and is expected to list matters this note does not.
15. **No FY2023 comparative on the face of any statement.** The P&L, Balance Sheet and Cash Flow carry
    FY2025 and FY2024 only. FY2023 survives only as **opening balances in the SOCIE** (equity 18,151,940
    shares / Rs 18.16 mn; preference 7,413,747 shares / Rs 74.13 mn; other equity (810.55)) `[SA SOCIE,
    p99/pr94]` and as the 1-April-2023 opening rows of the PPE and intangibles schedules `[SA Note 3,
    p113/pr108; Note 6.A, p116/pr111]` -> RHP/Prospectus restated consolidated FY23/FY24/FY25.
16. **No quantity disclosure for gold.** Note 24 gives Gold on loan of Rs 3,865.53 mn with an interest
    range of 2.50%–9.00% p.a. and a credit period "upto 180 days", but **no tonnage** `[p135/pr130]`. The
    only physical quantity in the document is **370 Kgs** of gold exposure, and it sits in the CG Report,
    not the notes `[p79/pr74]` -> Prospectus; FY26 investor presentations.
17. **No deferred tax asset recognised and no explicit quantum of unabsorbed losses/depreciation on the
    face of Note 10** — DTA is nil in both years `[SA BS, p97/pr92]`. Note 36 (p143/pr138) is where the
    recognition rationale sits and must be read by the tax chain.
18. **No disclosure of a promoter pledge or encumbrance.** The word does not appear. Promoter holding is
    given as a share count only `[SA Note 18(i), p129/pr124]` -> promoter SAST Reg. 31(4) filing of
    24-Jun-2026 (scanned — GAP-002) and AR FY2026.
19. **No EBITDA reconciliation** for the MD&A's Rs 758.85 mn `[p83/pr78]` -> would have to be derived from
    the P&L; the document offers no bridge.
20. **No Form AOC-2** — asserted not required `[Board's Report §32, p41/pr36]`; consequently **no
    disclosure of individual RPT contract values against arm's-length benchmarks**. RPTs appear only as
    Note 37 aggregates by counterparty `[p144–146/pr139–141]`.
21. **No employee remuneration schedule under Rule 5(2)/5(3)** — the top-ten and Rs 1.02 crore+ employee
    list is **excluded from the circulated report** and available only for inspection at the registered
    office `[Board's Report §34, p42/pr37]`.
22. **No number of whistle-blower complaints.** CARO 3(xi)(c) confirms complaints **were** received during
    the year `[p93/pr88]`; neither the Board's Report nor the CG Report's vigil-mechanism section (XI,
    p71/pr66) states how many -> AR FY2026 vigil-mechanism disclosure; audit-committee minutes (not public).
23. **No CSR spend and no CSR committee meetings** — the CSR committee met **zero times** in FY25 (0 held,
    0 attended for all three members) `[Annexure-4 §2, p54/pr49]`; obligation nil because average net
    profit of the preceding three years is negative `[Annexure-4 §5, p54/pr49; SA Note 39, p147/pr142]`.
24. **No shareholding band below 501 shares** in the distribution table, and only **83 shareholders in
    total**, of whom 36 hold 99.41% `[CG Report XVII item 10, p75/pr70]` — the table is a pre-IPO private-
    company register, not a public float -> shareholding-pattern XBRLs from 18-Aug-2025 (`data/filings/SHP_*.xml`).
25. **No consolidated CARO annexure** (§4.6) -> EHPL's own audited accounts.
26. **No R&D expenditure and no technology-absorption disclosure** — "NIL" / "Not Applicable"
    `[Board's Report §44(B), p44/pr39]`; foreign exchange **outgo Rs 53.61 million, earnings nil**
    `[§44(C), p44/pr39]`.

**C. Internal tie-outs that a later wave must resolve (recorded, not adjudicated)**

27. **Four-share discrepancy in total share capital.** Note 18(a) prints *"Total Share Capital [I + III]
    70,709,930"* `[p125/pr120]`, while the SOCIE prints *"Total Share capital as at 31 March 2025
    70,709,934.00"* `[p99/pr94]`. DERIVED: the Note 18(a) series detail sums to 609,594 + 186,982 + 88,624
    + 1,339,659 + 128,207 + 1,417,252 + 1,940,933 + 416,865 + 359,257 + 110,754 + 169,122 + 395,836 +
    250,658 + 17,680,565 + 10,380,622 = **35,474,930** preference shares, whereas the SOCIE's two
    preference lines sum to 25,094,312 + 10,380,622 = **35,474,934**, a difference of **4 shares** (face
    value ` 40) that the SOCIE has carried since its 31-March-2023 opening line (7,413,747 vs a series
    detail of 7,413,743). The Board's Report uses the note figure: *"all series of the 3,54,74,930
    Compulsory Convertible Preference shares"* `[p34/pr29]`.
28. **Standalone Note 48 states the wrong year.** *"During the year ended 31 March 2024, Company has
    discharged its liability towards right to subscribe shares."* `[SA Note 48, p157/pr152]` — but Note 22
    shows *"Liabilities towards rights to subscribe shares (Refer note no. 48)"* of **166.99** at
    31-Mar-2024 and **nil** at 31-Mar-2025 `[SA Note 22, p135/pr130]`, and the consolidated version of the
    same note says *"During the year ended **31 March 2025**"* `[CFS Note 48, p226/pr221]`.
29. **FY2024 ESOP charge does not tie between the P&L and the reserve.** P&L FY24 ESOP expense **292.58**
    `[SA Note 31, p139/pr134]`; Note 19(iii) FY24 *"Options granted during the year"* **193.50**, less
    surrendered (43.85), giving the SOCIE's net **149.65** `[SA Note 19(iii), p130/pr125; SA SOCIE,
    p99/pr94]`. DERIVED gap = 292.58 − 193.50 = **99.08**, presumptively the cash-settled portion (Note 40
    footnote: employees requested cash settlement, incremental impact ` 218.51 per option `[p148/pr143]`;
    Note 22 carries a *"Liabilities towards share based payment"* of 24.87 at 31-Mar-2024 `[p135/pr130]`).
    **FY2025 does tie**: P&L 512.39 = Note 19(iii) "Options granted during the year" 512.39.
30. **Basis mismatch in the Board's Report ESOP table**: diluted EPS quoted as ` (79.74) `[p32/pr27]` is
    the **consolidated** figure `[CFS Note 38, p217/pr212]`, not the standalone ` (78.86) `[SA Note 38,
    p147/pr142]`; the table also cites "Accounting Standard (AS) 20" although the statements are Ind AS.
31. **Options-exercised count differs by 8,704 between two tables in the same note**: *"Options
    exercised/modified during the year (1,508,947)"* in the vested-options reconciliation versus
    *"Options exercised 1,500,243"* / *"total number of shares arising as a result of exercise of option
    1,500,243"* `[SA Note 40, p148/pr143; Board's Report §8(b) items (c) and (d), p29/pr24]`.

---

## 7. CCPS, preference shares and compulsorily convertible instruments — page-cited

### 7.1 Where the disclosure lives

| Disclosure | Location |
|---|---|
| Authorised preference capital, 16 series, series-by-series | SA Note 18 "Authorized share capital" `[p122–123/pr117–118]`; CFS Note 18 `[p192–193/pr187–188]`; and in absolute rupees at `[Board's Report §8(a), p26–27/pr21–22]` and `[AGM Notice Item 5, p21–22/pr16–17]` |
| Issued/subscribed/paid-up preference capital, series-by-series | SA Note 18 "Equity component of Compulsorily Convertible Preference Shares (CCPS)" `[p123/pr118]`; `[Board's Report §8(a), p27–28/pr22–23]` |
| Series-by-series movement reconciliation (opening / issued / converted / closing) | SA Note 18(a)III `[p124–125/pr119–120]`; CFS Note 18 `[p194–195/pr189–190]` |
| **Classification rationale — why CCPS is equity and OCRPS was a liability** | **SA Note 18(c)** `[p125–126/pr120–121]`; CFS Note 18(c) `[p195–196/pr190–191]` |
| Liability component of OCRPS inside borrowings | SA Note 20 "Unsecured: Liability component of Optionally Convertible Redeemable Preference Shares" `[p131/pr126]` |
| Fair value of the OCRPS liability component | SA Note 41(ii) *"The fair values of liability component of Optionally Convertible Preference Shares is included at the ..."* `[p150/pr145]` |
| Equity effect of conversion | SA Note 19(i) Securities premium: *"Add: Reclassification from Liability to Equity (Refer note 18 (c)) 6.92"* and *"Add: Conversion from CCPS to Equity 8.86"* `[p129/pr124]`; SA SOCIE `[p100/pr95]` |
| Financing-activity reconciliation showing the non-cash fair-value adjustment | SA Cash Flow note (b) `[p102/pr97]` |
| >5% holders of every CCPS series | SA Note 18(h) `[p126–129/pr121–124]` |
| **Post-year-end conversion of all CCPS on IPO** | **Board's Report §10** `[p34/pr29]` — **not in the notes** |
| Cancellation of the unissued preference classes after conversion | AGM Notice Item 5 + explanatory statement `[p8–9/pr3–4 and p21–22/pr16–17]` |

### 7.2 What the classification note actually says (SA Note 18(c), p125–126/pr120–121)

- *"During the year ended 31 March 2024, the Company had issued G series CCPS and the CCPS holders of
  Series G have agreed a **fixed conversion of 1 equity shares for every 1 CCPS** held and therefore the
  same is **classified as equity**."*
- *"During the year ended 31 March 2025, 9,84,790 series G CCPS is converted into equity shares in the
  ratio of 1:1."*
- *"During the year ended 31 March 2025, the Company had issued H series CCPS and the CCPS holders of
  Series H have agreed a **fixed conversion of 1 equity shares for every 1 CCPS** held and therefore the
  same is **classified as equity**."*
- *"As per the terms and conditions of issue of Series E1 OCRPS, the holders shall have a right to convert
  any or all of the series at their sole discretion and at any time within 19 (nineteen) years from the
  issue of the Series, **into variable number of Equity Shares** of the Company and hence were classified
  as **financial instrument in the nature of financial liability designated to be measured at fair value
  through profit or loss** as at 31 March 2024."*
- *"During the year ended 31 March 2025, Series E1 OCRPS is converted into equity shares in the ratio of
  10:1."*

### 7.3 Fair value gain or loss taken on these instruments

**Direct answer: no fair value gain or loss on CCPS was routed through the FY2025 statement of profit and
loss, and none is disclosed for FY2024 either.** The conversion terms are fixed 1:1 for every CCPS series
described, so all CCPS sit in equity `[SA Note 18(c), p125–126/pr120–121]`. The only preference instrument
ever carried at FVTPL was the **7,292 Series E1 OCRPS**, and its movement was:

| Item | Amount (Rs mn) | Tag |
|---|---|---|
| OCRPS liability component at 31-Mar-2024 | **6.99** | `[SA Note 20, p131/pr126]` |
| OCRPS liability component at 31-Mar-2025 | **nil** | `[SA Note 20, p131/pr126]` |
| Non-cash "Fair value changes/Adjustments" against "Issue of Equity shares" in the FY25 financing reconciliation | **6.99** | `[SA Cash Flow note (b), p102/pr97]` |
| Amount credited to securities premium on reclassification from liability to equity | **6.92** | `[SA Note 19(i), p129/pr124; SA SOCIE, p100/pr95]` |
| Amount credited to securities premium on conversion of CCPS (Series G, 984,790 shares) to equity | **8.86** | `[SA Note 19(i), p129/pr124; SA SOCIE, p100/pr95]` |

Neither 6.92 nor 8.86 passes through profit or loss — both are equity-to-equity reclassifications shown in
the SOCIE. **NOT DISCLOSED: any fair-value remeasurement of the E1 OCRPS through P&L in FY2025, and the
line of the P&L in which it would sit** -> would be answered by the Prospectus restated statements
(`data/ipo/BLUESTONE-PROSPECTUS-2025.pdf`, "Restated Consolidated Statement of Profit and Loss" and the
corresponding note on financial instruments), which restate FY23–FY25 on a different basis.

**Adjacent fair-value items that a reader may confuse with a CCPS fair value and must not:**

- **Rs 52.16 mn "Fair value gain on call option in subsidiary"**, credited to **Other income** and
  recognised as a Level-3 financial asset — this relates to contingent call options over **Ethereal
  House**, not to preference shares `[SA Note 28, p139/pr134; SA Note 53, p158/pr153]`.
- **Rs 154.62 mn "Change in fair value of Equity on termination of Right to subscribe shares"**, charged
  **directly to retained earnings in FY2024** (never to P&L), relating to InnoVen Capital's right to
  subscribe 64,967 shares `[SA SOCIE, p99/pr94; SA Note 19(ii), p130/pr125; SA Note 48, p157/pr152]`. The
  matching liability of **166.99** sat in Note 22 at 31-Mar-2024 and is nil at 31-Mar-2025
  `[SA Note 22, p135/pr130]`.

### 7.4 The conversion on IPO

*"The Company has converted all series of the **3,54,74,930** Compulsory Convertible Preference shares
("CCPS") into **100,224,637** Equity shares of the Company on **July 04, 2025**, in accordance with the
terms of issuance and applicable regulatory provisions of the Companies Act, 2013."* `[AR FY25, Board's
Report §10, p34/pr29]`.

This event is **absent from SA Note 56 and CFS Note 58** (subsequent events), both of which were closed at
24-Apr-2025 and state that no disclosable event exists `[p159/pr154; p230/pr225]`.

DERIVED conversion ratio, blended: 100,224,637 ÷ 35,474,930 = **2.825 equity shares per CCPS**. This is
**not** the 1:1 ratio the accounting-classification note describes for Series G and H `[SA Note 18(c),
p125–126/pr120–121]`, and the AR discloses **no series-wise conversion ratio**. **NOT DISCLOSED:
series-wise CCPS conversion ratios and the anti-dilution / bonus mechanics that produce a blended 2.825x
-> Prospectus "Capital Structure — History of the Equity Share Capital" and "Notes to the Capital
Structure", `data/ipo/BLUESTONE-PROSPECTUS-2025.pdf`.**

---

## 8. Share-based payment / ESOP — page-cited, with the charge

| Item | Value | Tag |
|---|---|---|
| **Accounting policy** | Note 2.10 "Share based payments" | `[SA, p108/pr103; CFS, p179/pr174]` |
| **Principal note** | Note 40 "Employee Stock Option Plan" | `[SA, p147–148/pr142–143; CFS, p217–219/pr212–214]` |
| Scheme | BlueStone Jewellery and Lifestyle Employees Stock Option Plan – 2014 ("ESOP 2014"); approved 2014, amended 2016, 2022 and **August 2024** | `[SA Note 40, p147/pr142]` |
| Board / shareholder approval chain | Board 08-May-2014 / shareholders 09-May-2014; amended by Board 23-Jun-2016, 04-Jul-2016, 29-Sep-2016, 11-Jul-2022, 16-Aug-2024, 09-Apr-2025; by shareholders 24-Jun-2016, 05-Jul-2016, 30-Sep-2016, 20-Jul-2022, 21-Aug-2024, 02-May-2025 | `[Board's Report §8(b), p29/pr24]` |
| Total options approved under the scheme | **7,484,330** | `[Board's Report SBEB table (c), p30/pr25]` |
| **Charge to the statement of profit and loss, FY2025** | **Rs 512.39 million** (FY2024: Rs 292.58 million) — line *"Expense on employee stock option scheme (Refer note 40)"* | `[SA Note 31, p139/pr134; CFS Note 31, p210/pr205]` |
| Same charge, add-back in the cash flow | **512.39** (FY24: 292.58) | `[SA Cash Flow, p101/pr96; CFS Cash Flow, p170/pr165]` |
| Same charge, credited to the ESOP reserve | Note 19(iii): opening 553.00 + **512.39** granted − 167.91 exercised = **897.48** closing | `[SA Note 19(iii), p130/pr125]` |
| Board's Report restatement of the charge | *"The Company has recognized stock option compensation cost of **INR 512.39 million** in the statement of profit and loss for the financial year 2024-25."* | `[Board's Report §8(b)(II), p31/pr26]` |
| Method | **Fair value method** (not intrinsic value), Black-Scholes-Merton | `[Board's Report §8(b)(II) and (III), p31/pr26; SA Note 40, p148/pr143]` |
| Option movement FY25 | opening 2,446,853; granted 2,056,016; vested 903,797; lapsed 50,403; **closing outstanding 3,548,669**; exercisable at year end 2,376,602 | `[SA Note 40, p147–148/pr142–143]` |
| Grant dates FY25 | 17-May-24, 04-Jun-24, 01-Aug-24, 27-Sep-24, 27-Nov-24 | `[SA Note 40, p148/pr143]` |
| Fair-value inputs FY25 | weighted-average fair value **540.29** per option (FY24: 313.89); exercise price **` 1**; volatility **41.57%** (FY24: 46.53%); risk-free **6.44%**; dividend yield 0%; expected life **4–7 years**; vesting 4–7 years | `[SA Note 40, p148/pr143]` |
| **Volatility source — the pre-listing tell** | *"During the year, the Company was **unlisted** as at the date of preparation of the financial results ... Accordingly, the expected volatility used for valuation purposes has been determined based on the **historical volatility of comparable listed entities (peer group)**, as the Company's own share price information was not available."* | `[Board's Report §8(b), p33/pr28]`; echoed in the note: *"The stock price is arrived using the **last round of funding** closest to the grant date."* `[SA Note 40, p148/pr143]` |
| Underlying share price used at grant | **` 315 to ` 578** | `[Board's Report §8(b), p33/pr28]` |
| Weighted-average remaining contractual life | **3.61 years** at 31-Mar-2025 (FY24: 2.98 years) | `[SA Note 40, p148/pr143]` |
| Shares actually allotted on exercise during FY25 | 27-Sep-2024: 1,04,512; 22-Jan-2025: 12,10,172; 06-Feb-2025: 1,85,559 — **total 15,00,243** at ` 1 | `[Board's Report §8(a) item 6, p29/pr24]` |
| Cash proceeds on exercise | ` 15,00,243 (absolute rupees) | `[Board's Report §8(b)(h), p29/pr24]` |
| Named grants to KMP/SMP in FY25 | Rumit Dugar (CFO) 547,232; Vipin Sharma (CMO) 407,786; Sudeep Nagar (COO) 311,419; Harshit Desai 158,785; Mikhil Raj 158,785; Tarun Rajput 103,807; Gaurav Sachdeva 118,519 | `[Board's Report §8(b)(j), p29/pr24 and p31/pr26]` |
| Employees ≥1% of issued capital (equity-only basis) | Rumit Dugar 547,232 and Vipin Sharma 407,786; note added: *"No employee granted ≥1% of issued capital on fully diluted basis (post-Compulsory Convertible Preference Shares - conversion)"* | `[Board's Report §8(b), p32/pr27]` |
| **Cash-settled ESOP (FY2024 only)** | Employees requested cash settlement; settled at the Series-G CCPS fair value; *"The **incremental impact due to cash settlement is ` 218.51 per option**"*; 455,035 options exercised/modified in FY24; liability of 24.87 at 31-Mar-2024, nil at 31-Mar-2025; cash outflow of 117.96 shown in FY24 financing as "Settlement of cash settled ESOP liability" | `[SA Note 40, p148/pr143; SA Note 22, p135/pr130; SA Cash Flow, p101/pr96]` |
| **ESOP trust / treasury shares — closed out in FY2025** | 3,223,260 equity shares held by BlueStone Trust were classified as treasury shares; *"As of 31 March 2025, the Trust has **transferred all of its holdings** to its employees and its beneficiaries and no longer possesses any shares in the Company."* Treasury deduction of (3.22) in FY24 equity share capital falls to nil | `[SA Note 54, p158/pr153; SA Note 18, p123/pr118; SA Note 18(a)II, p124/pr119; CFS Note 55, p229/pr224]` |
| **Phantom Option Scheme 2016 — separate from ESOP, now closed** | 109,715 options granted to **former employees and non-employee associates**; FY2023 Board approved liquidation at **` 2,453.55 per option**; Rs 261.55 mn paid in FY24 and the balance paid in FY25; liability 7.53 at 31-Mar-2024, nil at 31-Mar-2025 | `[SA Note 47, p156/pr151; SA Note 22, p135/pr130]` |
| Options surrendered back to the pool | *"None of the ESOPs shares are surrendered and returned back to the ESOP pool."* | `[Board's Report §8(c), p30/pr25]` |
| SBEB certificate | Certificate from Kalaivani S on ESOP 2014 implementation to be placed at the AGM; Reg. 14 / Sch. I Part F information on the website | `[Board's Report §8(b), p33/pr28]` |

**NOT DISCLOSED: the grant-date-wise breakdown of the 2,056,016 FY25 grants, and the split of the Rs
512.39 mn charge between grant tranches or between KMP and other employees** -> Prospectus "Employee
Stock Option Scheme" section and the SBEB Table F published on the Company's website
(`https://kinclimg1.bluestone.com/static/ir/rfd/Table-F_v1.pdf`, cited at `[Board's Report §8(b),
p33/pr28]` and not held in `data/`).

---

## 9. Capital structure history and the share count before and after the IPO

### 9.1 Where the history lives

- **Board's Report §8 "Share Capital"** `[p26–34/pr21–29]` — authorised capital before/after, corporate
  actions on authorised capital, issued/paid-up capital series-by-series, and the seven paid-up capital
  events of FY2025.
- **SA Note 18(a)** reconciliation of shares outstanding `[p124–125/pr119–120]`; **Note 18(d)–(g)**
  five-year history `[p126/pr121]`; **Note 18(h)** >5% holders `[p126–129/pr121–124]`; **Note 18(i)**
  promoter shareholding `[p129/pr124]`.
- **SOCIE part A** `[SA p99/pr94; CFS p168/pr163]`.
- **Board's Report §10** for the post-year-end conversion and IPO `[p34–35/pr29–30]`.
- **AGM Notice Item 5** for the cancellation of unissued preference classes `[p8–9/pr3–4; p21–22/pr16–17]`.

### 9.2 Authorised capital

| Date | Authorised capital | Composition | Tag |
|---|---|---|---|
| Before 21-Aug-2024 | ` 34,00,00,000 | — | `[Board's Report §8(a), p27/pr22]` |
| From 21-Aug-2024 (AGM) | **` 45,05,00,000** | Increase created **1,05,00,000 Series H CCPS of ` 1** and **10,00,00,000 equity shares of ` 1** | `[Board's Report §8(a), p27/pr22]` |
| At 31-Mar-2025 | ` 45,05,00,000 = Rs **450.50 mn** | 16,82,90,700 equity of ` 1 (Rs 168.29 mn) + 16 preference series (Rs 282.21 mn). DERIVED: 168.29 + 282.21 = 450.50 ✓ | `[SA Note 18, p122–123/pr117–118]` |
| Proposed at the 14th AGM (29-Sep-2025) | ` 45,05,00,000 **divided into 45,05,00,000 equity shares of ` 1 only**, *"by way of cancellation of unissued Preference Shares of the Company"* | | `[AGM Notice Item 5 explanatory statement, p22/pr17]` |

### 9.3 Corporate actions on issued capital during FY2025 (seven events, in the order the report lists them)

| # | Event | Detail | Tag |
|---|---|---|---|
| 1 | **OCRPS conversion** | 7,292 Series E1 OCRPS of ` 10 → **72,920** equity shares of ` 1 (ratio 10:1), Board resolution **17-May-2024** | `[Board's Report §8(a), p28/pr23; SA Note 18(c), p126/pr121]` |
| 2 | **CCPS conversion** | 9,84,790 Series G CCPS of ` 10 → **9,84,790** equity shares of ` 1 (ratio 1:1), Board resolution **19-Jul-2024** | `[Board's Report §8(a), p28/pr23]` |
| 3 | **Rights issue** | **99,41,456** equity shares at ` 34 (` 1 face + ` 33 premium), Board resolution **13-Aug-2024** | `[Board's Report §8(a), p28/pr23]` |
| 4 | **Rights issue** | **60,391** equity shares at ` 34, Board resolution **16-Aug-2024** | `[Board's Report §8(a), p28/pr23]` |
| 5 | **Series H CCPS private placement** | **1,03,80,622** Series H CCPS of ` 1 at a **premium of ` 577** (` 578 per share), approved at the AGM of 21-Aug-2024, allotted in three tranches: 10-Sep-2024 34,42,899; 14-Sep-2024 62,88,449; 20-Sep-2024 6,49,274 | `[Board's Report §8(a), p28/pr23]` |
| 6 | **ESOP allotments** | 27-Sep-2024 1,04,512; 22-Jan-2025 12,10,172; 06-Feb-2025 1,85,559 — total **15,00,243** at ` 1 | `[Board's Report §8(a), p29/pr24]` |
| 7 | **Private placement to the promoter** | **13,00,000** equity shares to **Mr. Gaurav Singh Kushwaha** at ` 578 (` 577 premium), **02-Dec-2024**, aggregating up to ` 75,14,00,000 | `[Board's Report §8(a), p29/pr24]` |

Note 18(g) states the rights issue in a single line: *"During the year ended 31 March 2025, the Company
has issued **10,001,847 rights equity shares at a price of ` 34 each**, which includes a premium of ` 33
per share."* `[SA Note 18(g), p126/pr121]`. DERIVED cross-check: 99,41,456 + 60,391 = **10,001,847** ✓
`[Board's Report §8(a), p28/pr23]`.

Note 18(a)I reconciliation `[p124/pr119]`: opening 18,151,940 + shares issued 12,802,090 + treasury shares
transferred 3,223,260 + OCRPS conversion 72,920 + Series G CCPS conversion 984,790 = **35,235,000**.
DERIVED cross-check of "shares issued 12,802,090": 10,001,847 rights + 1,500,243 ESOP + 1,300,000
promoter private placement = **12,802,090** ✓.

### 9.4 Longer capital history disclosed in the notes

| Item | Disclosure | Tag |
|---|---|---|
| **Bonus issue** | *"In the period of five years, during the year 2022-23, the Company had issued **bonus shares of 16,336,746 of equity shares**."* | `[SA Note 18(d), p126/pr121]` |
| **Buy-back** | *"No class of shares have been bought back by the Company during the period of five years immediately preceding the current year."* | `[SA Note 18(e), p126/pr121]`; also `[Board's Report §8(e), p30/pr25]` |
| **Shares for consideration other than cash** | *"No class of shares have been issued for consideration other than cash ... during the year of five years immediately preceding the current year."* | `[SA Note 18(f), p126/pr121]` |
| **Sweat equity** | none issued | `[Board's Report §8(d), p30/pr25]` |
| **Shares with differential rights** | none issued | `[Board's Report §8(f), p30/pr25]` |
| **Share split** | **NOT DISCLOSED in the AR.** Face value is ` 1 throughout FY23–FY25 in the SOCIE; no split event is recorded -> Prospectus "Capital Structure — History of Equity Share Capital" would show any split before FY2023 |
| **NCDs issued in FY2025** (unlisted, unrated, secured, redeemable, private placement) | 06-Apr-2024 10,000 NCDs × ` 1,00,000 = ` 100 cr; 29-May-2024 250 × ` 10,00,000 = ` 25 cr; 07-Jun-2024 2,500 × ` 1,00,000 = ` 25 cr; 07-Jun-2024 500 × ` 1,00,000 = ` 5 cr; 13-Jun-2024 5,000 × ` 1,00,000 = ` 50 cr; 21-Jun-2024 10,000 × ` 1,00,000 = ` 100 cr; 03-Aug-2024 10,000 × ` 1,00,000 = ` 100 cr. **Total ` 405,00,00,000 (Rs 4,050 mn)** | `[Board's Report §9, p34/pr29]` |

### 9.5 Share count before and after the IPO

| Point in time | Equity shares of ` 1 | Preference shares | Total instruments | Paid-up equity capital | Tag |
|---|---|---|---|---|---|
| 31-Mar-2023 | 18,151,940 | 7,413,747 of ` 10 | 25,565,687 | Rs 18.16 mn equity | `[SA SOCIE, p99/pr94]` |
| 31-Mar-2024 | 18,151,940 (after deducting 3,223,260 treasury shares from 21,375,200 issued) | 26,079,102 of ` 10 | — | Rs 18.16 mn net of treasury; Rs 21.38 mn gross | `[SA Note 18, p123/pr118; SA SOCIE, p99/pr94]` |
| **31-Mar-2025** | **35,235,000** (no treasury shares remaining) | **25,094,312** of ` 10 + **10,380,622** of ` 1 | **70,709,934** per SOCIE / 70,709,930 per Note 18(a) (see §6 item 27) | Rs **35.23 mn** equity; **total share capital Rs 296.56 mn** | `[SA BS, p97/pr92; SA Note 18, p123/pr118; SA SOCIE, p99/pr94]` |
| 31-Mar-2025, in absolute rupees | — | — | — | *"the issued, subscribed and paid-up share capital of the Company as on 31st March, 2025 is **` 29,65,58,702**"* | `[Board's Report §8(a), p27/pr22]` |
| **04-Jul-2025 — CCPS conversion** | +100,224,637 | −35,474,930 (all series) | — | — | `[Board's Report §10, p34/pr29]` |
| **IPO, priced at ` 517 per share** | fresh issue **15,860,735**; offer for sale **13,939,063**; total offer **29,799,798** shares; total issue size **` 15,40,64,95,566** | — | — | — | `[Board's Report §6, p26/pr21; §10, p34/pr29; CG Report preamble, p57/pr52]` |
| **Post-IPO (from 19-Aug-2025 listing)** | **151,320,372** | nil | 151,320,372 | *"the paid-up share capital of the Company increased to **` 15,13,20,372/-**"* | `[Board's Report §10, p35/pr30; CG Report preamble, p57/pr52]` |

**DERIVED tie-out (recomputed independently, doctrine §4b):**
35,235,000 (31-Mar-2025 equity) + 100,224,637 (CCPS conversion) + 15,860,735 (fresh issue) = **151,320,372**
= the stated post-IPO share count and, at ` 1 face value, the stated paid-up capital of ` 15,13,20,372.
The offer for sale of 13,939,063 shares changes ownership, not the count — consistent.

**DERIVED sanity check on the issue size:** 29,799,798 × ` 517 = ` 15,40,64,95,566 ✓ exactly as stated
`[Board's Report §6, p26/pr21]`.

*(Transcription note for later citation: the Board's Report and the CG Report both write "` 15,13,20,372
equity shares of ` 1/- each" `[p35/pr30; p57/pr52]` — the rupee figure and the share count are the same
number at ` 1 face value, but the sentence as printed conflates rupees with shares.)*

**Shareholding at 31-Mar-2025 (pre-IPO, private-company register):** 83 shareholders in total, 36 of whom
hold 99.41% of the 3,52,35,000 equity shares `[CG Report XVII item 10, p75/pr70]`. Category split:
Promoters and Promoter Group 2,47,61,977 (70.28%); Institutional/Corporate/QIB/AIF/Trust 35,14,414
(9.97%); RII 66,33,238 (18.82%); FPI and NRI 3,26,371 (0.93%) `[CG Report XVII item 11, p75/pr70]`.
Mr. Gaurav Singh Kushwaha held 24,465,127 equity shares = **69%** at 31-Mar-2025 (77% at 31-Mar-2024)
`[SA Note 18(h) and 18(i), p126/pr121 and p129/pr124]`, and **2,44,65,127 shares / 69.43%** in the KMP
table `[CG Report XVII, p76/pr71]`. Rumit Dugar (CFO) held 1,06,104 shares / 0.30% `[p76/pr71]`.
Dematerialisation at 31-Mar-2025: NSDL 3,04,07,094 (86.30%), CDSL 17,47,251 (4.96%) — i.e. **8.74% still
in physical form pre-listing**; post-listing NSDL 13,42,03,053 (88.69%) and CDSL 1,40,36,664 (9.28%)
`[CG Report XVII item 12, p76/pr71]`.

**Series-level pre-IPO investor register** (the base for the lock-in/exit ladder that `state/LOOP.md`
makes mandatory) is at **SA Note 18(h), p126–129/pr121–124**, naming Accel (India III / India VII / Growth
III Mauritius), Saama Capital II, Kalaari Capital Partners II and Opportunity Fund, Sunil Kant Munjal and
other partners of Hero, Steadview Capital Mauritius, Peak XV Partners Growth Investments IV, IvyCap
Ventures Trust Funds 1/2/3, 360 ONE (Special Opportunities Series 11/12, Large Value Series 5/13), Iron
Pillar Fund I / Fund I India / II WH, RB Investment Pte, Ashoka Pte, Japonica Holdings Pte, DF
International, Avanz EM Partnerships Fund II, NKSquared, Kamath Associate, IE Venture Investment Fund II,
NV Holdings, Pratithi Growth Fund 1, **MIH Investments One B.V. (59% of Series H)**, Think Investments
PCC, and Access India Capital (8% of equity at 31-Mar-2025).

---

## 10. Restatement, reclassification and regrouping language — verbatim

**(a) Standalone Note 57** `[AR FY25, SA Note 57, p159/pr154]`:
> "Previous year's figures have been regrouped/reclassified, wherever necessary, to conform to current
> year classification."

**(b) Consolidated Note 59** `[AR FY25, CFS Note 59, p230/pr225]`:
> "Previous year's figures have been regrouped/reclassified, wherever necessary, to confirm to current
> year classification."

*(The consolidated version prints "confirm" where the standalone prints "conform".)*

Neither note quantifies a single reclassification, names a single line item moved, or gives a
before/after table.

**(c) Board's Report §7 "Revision of financial statement"** `[AR FY25, Board's Report §7, p26/pr21]`:
> "According to Secretarial Standard-4, if a company revises its financial statements or reports for any
> of the three preceding financial years - whether voluntarily or as directed by a judicial authority -
> the detailed reasons for such revisions must be disclosed in both the report for the current year and
> the report for the relevant financial year in which the revision occurred.
> For your Company, there were no revisions to the financial statements in any of the three preceding
> financial years."

**(d) Accounting-policy consistency assertion, SA Note 2.1(i)** `[AR FY25, SA Note 2.1(i), p103/pr98]`:
> "The Company's standalone financial statement consistently apply uniform accounting policies across all
> periods."

**(e) The only two accounting standards adopted in the year, both stated to have nil impact, SA Note 2.20**
`[AR FY25, SA Note 2.20, p112/pr107; CFS Note 2.20, p182/pr177]`:
> "The application of Ind AS 117 had no impact on the Company's financial statements as the Company has
> not entered any contracts in the nature of insurance contracts covered under Ind AS 117."
> "The application of Ind AS 116 had no impact on the Company's financial statements as the Company has
> not entered into any transaction with respect to sale and leaseback."
> "There are no standards on accounting or any addendum thereto, prescribed by Ministry of Corporate
> Affairs (MCA) under Section 133 of the Companies Act, 2013 which are issued and not effective as at
> 31 March, 2025."

**(f) Reclassification between liability and equity — the one reclassification the document does
quantify**, SA Note 19(i) `[p129/pr124]`:
> "Add: Reclassification from Liability to Equity (Refer note 18 (c)) 6.92"
> "Add: Conversion from CCPS to Equity 8.86"

**Basis warning for later waves (per `state/TEMPLATES.md`).** The AR FY2025 is **REPORTED, standalone and
consolidated, Ind AS, audited 24-Apr-2025**. The Prospectus/RHP carry **RESTATED consolidated FY23/FY24/
FY2025**. Nothing in this annual report acknowledges the existence of a restated set, states a
reconciliation to it, or explains any difference. **NOT DISCLOSED: the reconciliation between reported
FY2025 and restated FY2025** -> `data/ipo/BLUESTONE-PROSPECTUS-2025.pdf`, "Restated Consolidated Financial
Information — Statement of Adjustments to Audited Financial Statements", which is the only document that
can carry that bridge.

---

## 11. A report for a company that was private for part of the year

**The transition dates, in order:**

| Date | Event | Tag |
|---|---|---|
| 22-Jul-2011 | Incorporation | `[Corporate Information, p4]` |
| 16-Aug-2024 | Three Independent Directors appointed (Rohit Bhasin, Rajesh Kumar Dahiya, Neha); regularised at the AGM of 21-Aug-2024 | `[Board's Report §13, p36/pr31]` |
| 21-Aug-2024 | AGM: authorised capital raised; **main objects clause changed** by special resolution | `[Board's Report §48, p45/pr40]` |
| **08-Nov-2024** | **Converted from private limited to unlisted public limited company** by RoC Central Processing Centre letter; CIN changed to `U72900KA2011PLC059678` | `[Board's Report §48, p45/pr40; SA Note 1, p103/pr98]` |
| 27-Nov-2024 | Nominee Director Vikram Gupta resigns — from this date *"at least half of the Board members comprises of Independent Directors"* | `[CG Report II, p57/pr52; Board's Report §13, p36/pr31]` |
| 11-Dec-2024 | DRHP filed with SEBI/BSE/NSE | `[Board's Report §48, p45/pr40]` |
| 24-Feb-2025 | In-principle listing approvals from BSE and NSE | `[Board's Report §48, p45/pr40]` |
| 31-Mar-2025 | **Balance sheet date — company is an unlisted public company** | |
| 24-Apr-2025 | Financial statements and both audit reports signed | `[p89/pr84; p163/pr158]` |
| 30-Apr-2025 | Company Secretary Jasmeet Kaur Saluja resigns | `[Board's Report §13, p37/pr32]` |
| 15-Jul-2025 | Paras Shah appointed Company Secretary and Compliance Officer | `[Board's Report §13, p37/pr32]` |
| 04-Jul-2025 | All CCPS converted to equity | `[Board's Report §10, p34/pr29]` |
| 18-Jul / 05-Aug / 14-Aug-2025 | UDRHP / RHP / Prospectus filed | `[Board's Report §10, p34/pr29]` |
| 18-Aug-2025 | Listing and trading approval from BSE and NSE | `[Board's Report §10, p34/pr29]` |
| **19-Aug-2025** | **Listing** | `[Corporate Information, p5; Board's Report §10, p34/pr29]` |
| 04-Sep-2025 | Annual Report re-adopted and re-approved by the Board post-listing | `[Board's Report §10, p35/pr30]` |

**The Company's own framing of what this does to the disclosures** `[Board's Report §10, p35/pr30;
CG Report preamble, p57/pr52]`:
> "This Annual Report is re adopted and re approved at the Board meeting held on September 04, 2025 post
> listing with a view to present the Annual Report to the shareholders of the Company to provide full
> disclosures and transparent information even though the shares of the Company were not listed as on 31
> st March 2025. **The information which was not applicable to the Company being unlisted during the
> financial year has been mentioned accordingly.** Directors have tried to maintain coherence in
> disclosures and flow of the information by **clubbing required information topic-wise** and thus certain
> information which is required in Directors' Report is clubbed elsewhere and has to be read as a part of
> Directors' Report."

**The secretarial auditor's own scoping** `[Annexure-3, p51–52/pr46–47]`:
> "During the period under review, the Company was a 'to be listed company' and was in the process of
> undertaking its initial public offer ('IPO'); therefore, **only those provisions of the Securities and
> Exchange Board of India Act, 1992 and the regulations framed thereunder that are specifically applicable
> to a company proposed to be listed were applicable** to the Company as on the date of this Report."
> "The Listing Agreements entered into by the Company with the Stock Exchange(s), if applicable - **The
> Company is an Unlisted Public Limited Company as on the date of this report and hence not applicable.**"
> "...**certain non-material findings** made during the course of the audit relating to the provisions of
> Companies Act, secretarial standards and Labour Laws were **addressed suitably by the Management**." —
> the findings themselves are not described.

**The corporate-governance certifier's own scoping** `[PCS Certificate on Corporate Governance,
p80/pr75]`:
> "we certify that the Company has complied with the conditions of Corporate Governance as stipulated in
> the aforesaid provisions of SEBI Listing Regulations, **to the extent applicable on it during the time
> period pre-listing of securities** as the securities of the company were listed on August 19, 2025."

**Governance disclosures that are consequently absent or abbreviated** (each already page-cited in §6):
BRSR (§6.1); Reg. 17–27 / Reg. 46 compliance statement (§6.2); results publication, newspaper
publication, analyst presentations and the analyst-meet schedule (§6.3); share price / market-cap /
index-comparison data (§6.4); Reg. 32(7A) preferential-allotment utilisation (§6.5); credit ratings
(§6.6); postal ballots (§6.7); quarterly financials (§6.8); the shareholder register is 83 names deep
with no public float (§6.24).

**Governance disclosures that are present and are full-weight evidence in their own right**, per the
LOOP.md new-listing adjustment ("Events that did occur are read at full weight"):

| Event | Detail | Tag |
|---|---|---|
| **17 board meetings** in FY2024-25 | 19-Apr, 17-May, 27-May, 04-Jun, 10-Jun, 17-Jun, 12-Jul, 17-Jul, 19-Jul, 01-Aug, 03-Aug, 13-Aug, 16-Aug, 27-Sep, 27-Nov, 10-Dec-2024, 06-Feb-2025; full attendance by every director for every meeting he/she was entitled to attend | `[Board's Report §14, p37–38/pr32–33]` |
| **Only 2 Audit Committee meetings** in the year (10-Dec-2024 and 11-Mar-2025), plus 3 Compensation Committee, 1 NRC, 1 IPO Committee, 2 Operation Committee and 1 Independent Directors' meeting | | `[Board's Report §14, p38/pr33]` |
| **CSR Committee met zero times** | 0 meetings held, 0 attended | `[Annexure-4 §2, p54/pr49]` |
| Director resignation | Vikram Gupta (Nominee Director, IvyCap) ceased 27-Nov-2024 | `[Board's Report §13, p36/pr31]` |
| Company Secretary turnover | Jasmeet Kaur Saluja appointed 19-Mar-2024, resigned 30-Apr-2025; Paras Shah appointed 15-Jul-2025 | `[Board's Report §34 footnote, p42/pr37]` |
| MD reappointment | Gaurav Singh Kushwaha reappointed for three years from 21-Jul-2025 to 20-Jul-2028, approved 21-Aug-2024 | `[Board's Report §13, p36/pr31]` |
| MD pay ratio | 41% increase in remuneration in FY25; ratio to median **88:1**; median employee remuneration ` 3,25,337; aggregate non-KMP remuneration +10.1%, KMP +8% excluding ESOP perquisites | `[Board's Report §34, p42/pr37]` |
| Related-party investments into two new entities in the year | EHPL Rs 167.98 mn (premium ` 2,714/share) and RFPL Rs 105.00 mn (premium ` 614.38/share) | `[SA Note 55, p158–159/pr153–154; SA Note 37, p146/pr141]` |
| Promoter subscribed to both the rights issue and a private placement | Rights issue Rs 313.31 mn; private placement Rs 751.40 mn — both to Gaurav Singh Kushwaha, disclosed as **related-party transactions** | `[SA Note 37(ii), p145/pr140]` |
| Receivable from a director's relative outstanding at year end | Mrs. Duhita Nath Rs 3.19 mn (sale of products Rs 3.19 mn in the year) | `[SA Note 37(ii) and (iii), p146/pr141]` |
| POSH | 3 complaints filed, 3 disposed, nil pending | `[Board's Report §42, p43/pr38]` |
| Sitting fees to independent directors | Dahiya 0.55; Bhasin 0.50; Neha 0.45 (Rs mn) | `[SA Note 37(ii), p145/pr140]` |
| Independent-director remuneration | Dahiya 1.70; Bhasin 1.75; Neha 1.80 (Rs mn) | `[SA Note 37(ii), p145/pr140]` |

**Absence of history is a gap, not a clean record** (LOOP.md). This report is the **first** governance
report the Company has ever published, its comparative period is a private company, and the corporate-
governance certificate covers only the pre-listing part of a year in which the Company had independent
directors for **seven and a half months** (16-Aug-2024 to 31-Mar-2025) and an audit committee that met
**twice**.

---

## 12. Handoff notes for waves 2–8

1. **Cite the statement set.** Note numbers diverge from 51 onward (§2). "Note 53" alone is ambiguous.
2. **Never join this document's FY2025 to the Prospectus FY2025** without the basis tag; the AR is
   REPORTED, the offer document is RESTATED, and this AR offers no bridge (§10).
3. **The auditor named nothing.** No KAM, no EoM (§4.3, §4.4). Doctrine §3 trigger 6 fires on no line in
   FY2025. Materiality must be established from triggers 1–5, 7 and 8 instead. For orientation, inventories
   of Rs 16,525.47 mn are DERIVED 16,525.47 ÷ 35,346.17 = **46.75% of standalone total assets**
   `[SA BS, p97/pr92]`.
4. **Four numbers in this document do not tie** and are recorded, not resolved: the 4-share capital
   difference, the Note 48 year, the FY24 ESOP charge bridge, and the 1,508,947 vs 1,500,243 option count
   (§6 items 27–31).
5. **The single most testable management claim is the 100% gold hedge** at `[CG Report XX(f), p78–79/
   pr73–74]`, against Note 42's commodity-risk carrying values `[p150–151/pr145–146]` and the Rs 3,865.53
   mn gold-on-loan balance `[SA Note 24, p135/pr130]`.
6. **Cash-loss and going-concern language exist without an auditor paragraph**: CARO 3(xvii) cash losses
   Rs 236.29 mn (FY25) and Rs 469.72 mn (FY24) `[p94/pr89]`, accumulated losses Rs 24,517.62 mn
   `[SA Note 2.1(iv), p103/pr98]`, standalone CFO of Rs (6,648.41) mn `[SA Cash Flow, p101/pr96]`.
7. **IPO costs of Rs 117.08 mn sit in prepaid expenses (other current assets) at 31-Mar-2025**, to be
   adjusted against securities premium on completion `[SA Note 11, p119/pr114]` — the FY2026 map should
   trace where they landed.

---

# PART 3 — Prospectus

# W1 — Document map: Prospectus (BlueStone Jewellery and Lifestyle Limited)

**Agent:** A2, Document Mapper, doctrine wave 1
**Source file:** `data/ipo/BLUESTONE-PROSPECTUS-2025.pdf` · text `data/text/BLUESTONE-PROSPECTUS-2025.txt`
**Compiled:** 2026-09-09
**Scope:** map only. No series extracted, no interpretation, no conclusions. Every locator carries a page.

---

## 0. Document identity, units, and the page-number convention

### 0.1 The date on the document is **13-Aug-2025**, not 14-Aug-2025

The cover page, the repeated cover on the second leaf, and the Declaration all read **"PROSPECTUS
Dated August 13, 2025"**. The Declaration signed by the Chairman and Managing Director is dated
**"Date: August 13, 2025 / Place: Bangalore, India"** `[Prospectus p1/pr—]` `[Prospectus p2/pr—]`
`[Prospectus p519/pr516]`.

`data/source_register.md` Tier 1 row 1 and the task brief both describe this document as the
"Prospectus, 14-Aug-2025". **The document itself says 13-Aug-2025.** Every certificate reproduced
inside it (Rawat & Associates on WACA, KPIs, offer expenses, working-capital projections; DVD &
Associates on share capital history) is also dated **August 13, 2025**. 14-Aug-2025 is plausibly the
RoC *filing* date, but the Prospectus nowhere states a filing date. **This is a source-register
correction, not a finding**: cite the document as `Prospectus dated 13-Aug-2025` and, if the
14-Aug date is used anywhere, state which act it refers to.

### 0.2 Units — the exact wording

Two different unit conventions run in this document and they must not be confused.

| Where | Exact printed wording | Unit |
|---|---|---|
| **Restated Financial Information (Annexures I–VII, PDF p321–397)** | **"(All amounts are in INR million unless otherwise stated)"** — printed as a standing sub-header on **every page** of Annexures I to VII | **₹ million** |
| Offer / Objects / Capital Structure / MD&A tables | "(in ₹ million)" or "(₹ in million)" per table | ₹ million |
| Capital Structure share-capital table | "(in ₹, except share data)" `[Prospectus p120/pr117]` | **absolute ₹** |
| Manufacturing capacity table | "Details of capacity as at and for the period (in Kilograms)" `[Prospectus p260/pr257]` | **kg of gold** |
| Promoter contribution escrow / PC shortfall amounts | quoted as absolute rupees, e.g. "₹115,760,127", "₹76,833,708", "₹38,926,419" `[Prospectus p142/pr139]` | **absolute ₹** |

**The scale trap in this document:** the capital-structure table on `p120/pr117` prints the authorised
and paid-up capital in *absolute rupees* (`135,459,637`) on the same page as the offer size in
*₹ million* (`15,406.50`). Reading `135,459,637` as ₹ million would be a 10⁶ error. Always re-read the
unit line above the table.

### 0.3 PDF page ↔ printed page

**Offset is uniform: PDF page n = printed page (n − 3), for every page from PDF 4 to PDF 532.**
Verified programmatically across all 532 pages: the printed folio appears in the header on prose pages
and in the **footer** on the financial-statement pages (PDF 321–397, PDF 108–110), and matches `n − 3`
on all of them. PDF pages 1–3 (cover, repeat cover, table of contents) carry no printed folio.

Citation form used below: `[Prospectus p<PDF>/pr<printed>]`. Restated-financials cites additionally
carry the basis word, per `state/TEMPLATES.md`: `[Prospectus p<PDF>/pr<printed>, RESTATED]`.

### 0.4 The single most important basis fact in this document

> **The "Restated Consolidated" financial information is consolidated for FY2025 only. FY2024 and
> FY2023 are restated STANDALONE.**

Every column header in Annexures I, II, III, IV and in Note tables reads:
`Consolidated | Standalone | Standalone` for FY2025 | FY2024 | FY2023 respectively
`[Prospectus p322/pr319, RESTATED]` `[Prospectus p324/pr321, RESTATED]` `[Prospectus p327/pr324, RESTATED]`.

The auditor's report title says so explicitly: *"Restated **Consolidated** Statement of Assets and
Liabilities as at March 31, 2025 … ; Restated **Standalone** Statement of Assets and Liabilities as at
March 31, 2024 and 31 March 2023 …"* `[Prospectus p316/pr313]`.

And MD&A says so in terms: *"In this section, we have compared our consolidated financial information
as of and for the year ended March 31, 2025 and our standalone financial information as of and for the
year ended March 31, 2024 **and these periods are not comparable to each other**."*
`[Prospectus p399/pr396]`.

**Consequence for the run:** the `BASIS:` line required by `state/TEMPLATES.md` needs a third state.
FY23 and FY24 are not merely "restated" — they are restated *standalone*. FY25 exists on three bases in
the evidence set: restated consolidated (Prospectus), restated standalone parent-share (Note 50), and
reported (AR FY2025). See §8.1.

---

## 1. Structure table

Sections in document order. All ranges inclusive. Printed page from the TOC at `[Prospectus p3]`,
PDF page = printed + 3, each start verified against the actual heading on the page.

| Section | Printed pages | PDF pages | Notes |
|---|---|---|---|
| Cover page / repeat cover | — | 1–2 | Both dated "August 13, 2025" |
| **TABLE OF CONTENTS** | — | 3 | Unfoliated |
| **SECTION I — GENERAL** | 1–33 | 4–36 | |
| Definitions and Abbreviations | 1–14 | 4–17 | |
| Certain Conventions, Presentation of Financial, Industry and Market Data and Currency of Presentation | 15–17 | 18–20 | Non-GAAP measures caveat at pr16 |
| Forward-Looking Statements | 18–19 | 21–22 | |
| **Summary of the Offer Document** | **20–33** | **23–36** | KPI table pr24–25; litigation summary pr25; contingent liabilities pr26; RPT summary pr26–27; WACA / average cost of acquisition pr28; secondary transactions pr29–32; pre-IPO placement pr33 |
| **SECTION II — RISK FACTORS** | **34–101** | **37–104** | 96 numbered risk factors. Index at §5 |
| **SECTION III — INTRODUCTION** | 102–180 | 105–183 | |
| **The Offer** | **102–103** | **105–106** | Full offer/allocation table |
| Summary Financial Information | 104–107 | 107–110 | Restated BS pr105, P&L pr106, CF pr107 (folio in footer on pr105–107) |
| General Information | 108–116 | 111–119 | BRLMs, auditors, monitoring agency, bid dates |
| **Capital Structure** | **117–151** | **120–154** | See §4 |
| **Objects of the Offer** | **152–161** | **155–164** | See §2 |
| **Basis for Offer Price** | **162–173** | **165–176** | EPS/P-E pr162–163; peer P/E pr163; RoNW pr163; NAV pr164; peer accounting ratios pr164–165; KPIs pr166–168; peer KPI comparison pr168–170; WACA pr171–173 |
| Statement of Special Tax Benefits | 174–180 | 177–183 | |
| **SECTION IV — ABOUT OUR COMPANY** | 181–311 | 184–314 | |
| **Industry Overview** | **181–228** | **184–231** | RedSeer Report, commissioned and paid for by the issuer; financial/operational benchmarking of listed peers at pr220–227 |
| **Our Business** | **229–266** | **232–269** | See §6 |
| Key Regulations and Policies in India | 267–275 | 270–278 | |
| History and Certain Corporate Matters | 276–287 | 279–290 | MoA amendments pr277; shareholders' agreements pr278–286; material acquisitions/divestments pr284; time/cost overruns and defaults pr284 |
| Our Subsidiary and Associate | 288–290 | 291–293 | Ethereal House Pvt Ltd (subsidiary); Redefine Fashion Pvt Ltd (associate) |
| **Our Management** | **291–307** | **294–310** | Board pr291–293; remuneration pr294–295; interests pr296; borrowing powers pr296; Audit Cttee pr296–298; NRC pr298–300; SRC pr301; RMC pr302–303; CSR Cttee pr303; org chart pr304; KMP/SMP pr305–307 |
| **Our Promoter and Promoter Group** | **308–310** | **311–313** | See §7 |
| Dividend Policy | 311 | 314 | |
| **SECTION V — FINANCIAL INFORMATION** | 312–428 | 315–431 | |
| **Restated Financial Information** | **312–394** | **315–397** | See §3 |
| **Other Financial Information** | **395** | **398** | Accounting ratios; pointer to off-document Audited Financial Information hosted on company website |
| **Management's Discussion and Analysis** | **396–425** | **399–428** | Significant factors pr397–399; non-GAAP reconciliations pr399–401; accounting policies pr402–413; results FY25 v FY24 pr413–415; FY24 v FY23 pr416–418; liquidity/cash flows pr418–420; contractual obligations pr421; contingent liabilities & risk pr422–423; competitive conditions pr424; recent developments/NCDs pr425 |
| Capitalisation Statement | 426 | 429 | As at 31-Mar-2025, pre- and post-Offer |
| **Financial Indebtedness** | **427–428** | **430–431** | Borrowings summary as at 31-May-2025 |
| **SECTION VI — LEGAL AND OTHER INFORMATION** | 429–455 | 432–458 | |
| **Outstanding Litigation and Material Developments** | **429–435** | **432–438** | See §7 |
| **Government and Other Approvals** | **436–438** | **439–441** | Incorporation, tax, labour, business approvals; approvals applied-for-not-received |
| **Our Group Company** | **439–440** | **442–443** | **Singular** — one group company only |
| Other Regulatory and Statutory Disclosures | 441–455 | 444–458 | Eligibility under Reg 6(2) at pr442; BRLM disclaimers; selling-shareholder consents |
| **SECTION VII — OFFER RELATED INFORMATION** | 456–485 | 459–488 | |
| **Terms of the Offer** | **456–461** | **459–464** | |
| **Offer Structure** | **462–465** | **465–468** | QIB / NIB / Retail split table at pr462 |
| Offer Procedure | 466–484 | 469–487 | |
| Restriction on Foreign Ownership of Indian Securities | 485 | 488 | |
| **SECTION VIII — Description of Equity Shares and Terms of the Articles of Association** | 486–511 | 489–514 | |
| **SECTION IX — OTHER INFORMATION** | 512–515 | 515–518 | |
| **Material Contracts and Documents for Inspection** | **512–515** | **515–518** | 41+ numbered items incl. SSAs, certificates, in-principle approvals dated 24-Feb-2025 |
| **Declaration** (company / directors) | 516–522 | 519–525 | Seven separate declarations, all dated 13-Aug-2025 |
| **Declarations by Selling Shareholders** | 523–529 | 526–532 | One per selling shareholder, seven in total |

---

## 2. Objects of the Offer — full locator

Section runs **printed 152–161 / PDF 155–164**.

### 2.1 Total issue size, split, price

| Item | Value | Locator |
|---|---|---|
| **Total Offer** | 29,799,798 Equity Shares of face value ₹1, **aggregating ₹15,406.50 million** | `[Prospectus p105/pr102]` · also cover `[Prospectus p1]`, `[Prospectus p120/pr117]`, `[Prospectus p155/pr152]`, `[Prospectus p465/pr462]` |
| **Fresh Issue** | 15,860,735 Equity Shares, **₹8,200.00 million** | `[Prospectus p105/pr102]` · `[Prospectus p120/pr117]` |
| **Offer for Sale** | 13,939,063 Equity Shares, **₹7,206.50 million** | `[Prospectus p105/pr102]` · `[Prospectus p155/pr152]` |
| **OFS as % of Fresh Issue** | **87.88%** (stated as a risk factor heading) | `[Prospectus p43/pr40]` RF7 |
| **Price Band** | **₹492 (Floor) to ₹517 (Cap)** per Equity Share | `[Prospectus p165/pr162]` |
| **Offer Price (final)** | **₹517** per Equity Share = 517× face value | `[Prospectus p2]` · `[Prospectus p165/pr162]` · `[Prospectus p176/pr173]` |
| **Face value** | ₹1 | `[Prospectus p1]` |
| **Offer as % of post-Offer paid-up capital** | **19.69%** | `[Prospectus p2]` |
| Pre-Offer shares outstanding | 135,459,637 | `[Prospectus p105/pr102]` |
| Post-Offer shares outstanding | 151,320,372 | `[Prospectus p105/pr102]` |
| Anchor Investor Bidding Date | Friday, 08-Aug-2025 | `[Prospectus p1]` |
| Bid/Offer opened | Monday, 11-Aug-2025 | `[Prospectus p1]` |
| Bid/Offer closed | Wednesday, 13-Aug-2025 | `[Prospectus p1]` |
| Allocation: QIB / NIB / Retail | not less than 75% / not more than 15% / not more than 10% — Reg 6(2) route | `[Prospectus p105/pr102]` · `[Prospectus p465/pr462]` |
| Anchor Investor Portion | 13,409,910 Equity Shares | `[Prospectus p105/pr102]` |

### 2.2 Net Proceeds bridge

| Particulars | ₹ million | Locator |
|---|---|---|
| Gross proceeds from the Fresh Issue | **8,200.00** | `[Prospectus p155/pr152]` |
| Less: Offer related expenses **to be borne by the Company** | **(492.51)** | `[Prospectus p155/pr152]` |
| **Net Proceeds** | **7,707.49** | `[Prospectus p156/pr153]` |
| *Memo:* **total** Offer expenses (Company + Selling Shareholders) | **925.52** = 6.01% of Offer size | `[Prospectus p161/pr158]` |

Offer-expense line detail (BRLM fees 401.94 / 43.43%; brokerage & selling commission 31.81; advertising
& marketing 109.65; other expenses itemised in five sub-lines) at `[Prospectus p161/pr158]`;
commission and processing-fee schedules run to `[Prospectus p163/pr160]`.

### 2.3 **The stated objects and the rupee amount against each** — the promise the MARs are measured against

| # | Stated object (verbatim) | Amount ₹ million | Locator |
|---|---|---|---|
| a | **"Funding our working capital requirements"** | **7,500.00** | `[Prospectus p156/pr153]` |
| b | **"General corporate purposes"** | **207.49** | `[Prospectus p156/pr153]` |
| | **Net Proceeds** | **7,707.49** | `[Prospectus p156/pr153]` |

There are **only two objects**. There is no repayment-of-debt object, no capex object, no
acquisition object, and no inorganic-growth object. Statement of objects at
`[Prospectus p155/pr152]`; detailed narrative for object (a) at `[Prospectus p157/pr154]`–
`[Prospectus p160/pr157]`; for object (b) at `[Prospectus p160/pr157]`.

GCP cap: *"shall not exceed 25% of the Gross Proceeds"* `[Prospectus p156/pr153]`.

### 2.4 **Deployment schedule by financial year**

| Particulars | Amount from Net Proceeds (₹ mn) | Deployment in **Fiscal 2026** (₹ mn) | Locator |
|---|---|---|---|
| Funding working capital requirements | 7,500 | **7,500** | `[Prospectus p156/pr153]` |
| General corporate purposes | 207.49 | **207.49** | `[Prospectus p156/pr153]` |
| **Net Proceeds** | **7,707.49** | **7,707.49** | `[Prospectus p156/pr153]` |

**The schedule has exactly one column: Fiscal 2026.** 100% of Net Proceeds was promised for
deployment inside FY2026 — i.e. by 31-Mar-2026. There is no FY2027 or later tranche. The escape
clause — *"In the event that the estimated utilization of the Net Proceeds in a scheduled fiscal year is
not completely met … the same shall be utilised in the next fiscal year"* — is at
`[Prospectus p156/pr153]`.

### 2.5 Working-capital object — basis of estimation (the numbers the object was sized from)

| Table | Content | Locator |
|---|---|---|
| Existing working capital, FY23/FY24/FY25 | Current assets, current liabilities, net current assets, and **funding pattern** (bank+GML / internal accruals & equity / Net Proceeds) | `[Prospectus p157/pr154]`–`[Prospectus p158/pr155]` |
| **Projected** working capital as at 31-Mar-2026 | Total current assets 32,064.82; total current liabilities 10,155.83; **net current assets 21,908.99**; funding pattern includes **"Use of net Proceeds from the Fresh Issue 7,500.00"** | `[Prospectus p158/pr155]` |
| Holding-level days, actual FY23–FY25 and assumed FY26 | e.g. inventory **341 / 341 / 286 / 187 days** (FY26E / FY25 / FY24 / FY23) | `[Prospectus p159/pr156]` |
| Key assumptions and justification, line by line | Prose per working-capital line | `[Prospectus p159/pr156]`–`[Prospectus p160/pr157]` |

Board resolution approving the FY2026 projected working capital: **dated 16-Jul-2025**
`[Prospectus p158/pr155]`. Certification of the projection and the holding levels: **Rawat & Associates,
Chartered Accountants, certificate dated 13-Aug-2025** `[Prospectus p158/pr155]`,
`[Prospectus p159/pr156]`, `[Prospectus p160/pr157]`.

Existing borrowings quoted inside the object narrative, **as on 31-May-2025**: working-capital
facilities (incl. payable financing) up to ₹1,761.93 mn; NCDs up to ₹4,239.86 mn; non-current facilities
incl. current maturities ₹1,543.36 mn; **gold metal loans ₹2,261.54 mn**. Plus: **franchise partners had
funded ₹2,261.68 mn of inventory working capital as at 31-Mar-2025** `[Prospectus p157/pr154]`.

### 2.6 Offer-for-Sale — selling shareholders and shares offered

| # | Selling Shareholder | Shares offered | % pre-Offer (fully diluted) | Post-Offer shares held | WACA per share (₹) |
|---|---|---|---|---|---|
| 1 | Accel India III (Mauritius) Ltd | 2,603,915 | 1.88 | 13,540,055 | 63.68 |
| 2 | Saama Capital II, Ltd. | 4,100,970 | 2.97 | **0** | 48.70 |
| 3 | Kalaari Capital Partners II, LLC | 3,536,990 | 2.56 | 3,536,990 | 59.28 |
| 4 | Kalaari Capital Partners Opportunity Fund, LLC | 452,145 | 0.33 | 452,145 | 82.41 |
| 5 | Iron Pillar Fund I Ltd | 821,085 | 0.59 | 2,609,925 | 92.81 |
| 6 | Iron Pillar India Fund I | 493,958 | 0.36 | 1,568,052 | 82.41 |
| 7 | Sunil Kant Munjal (and other partners of Hero Enterprise Partner Ventures) | 1,930,000 | 1.40 | 5,827,570 | 262.76 |
| | **Total** | **13,939,063** | **10.08** | **27,534,737** | — |

`[Prospectus p155/pr152]` (shares/percentages/post-Offer holding) · `[Prospectus p1]` and
`[Prospectus p31/pr28]` (average cost of acquisition, certified by Rawat & Associates 13-Aug-2025).

**Withdrawal on record:** *"IvyCap Ventures Trust – Fund 1 has withdrawn its participation as a Selling
Shareholder in the Offer for Sale of 3,126,950 Equity Shares."* `[Prospectus p153/pr150]`
The same table shows offered quantities **cut between DRHP and RHP** for Accel (3,027,303 → 2,603,915),
Kalaari II (7,073,980 → 3,536,990), Kalaari Opportunity (904,290 → 452,145), Iron Pillar Fund I
(1,094,780 → 821,085), Iron Pillar India (658,610 → 493,958) and Hero (4,000,000 → 1,930,000)
`[Prospectus p153/pr150]`.

### 2.7 Monitoring, variation, and appraisal — the compliance frame the four MARs sit inside

| Item | Content | Locator |
|---|---|---|
| **Monitoring Agency** | **CARE Ratings Limited**, appointed under Reg 41 SEBI ICDR (Fresh Issue > ₹1,000 mn). Quarterly report under Reg 41(2) until Gross Proceeds fully utilised. Audit Committee to receive it without delay | `[Prospectus p163/pr160]` |
| **Statement of deviation** | Quarterly statement to the Stock Exchanges under Reg 32(1) SEBI LODR: (i) deviations in actual utilisation vs objects; (ii) category-wise variations. To be published in newspapers alongside results; explanation in the directors' report | `[Prospectus p163/pr160]` |
| Annual statement of funds used for other purposes | To be certified by the statutory auditor | `[Prospectus p163/pr160]` |
| **Appraisal** | *"The objects of the Fresh Issue have not been appraised by any bank, financial institution or agency and we have not raised any bridge loans against the Net Proceeds."* | `[Prospectus p163/pr160]` |
| Means of finance | Reg 7(1)E / para 9C not applicable — objects funded **entirely** from Net Proceeds; no 75% firm-arrangement requirement | `[Prospectus p157/pr154]` |
| **Interim use** | Net Proceeds to be deposited **only** in scheduled commercial banks (RBI Act 2nd Schedule) as approved by the Board; **no** investment in shares of any listed company or the equity markets (s.27 Companies Act) | `[Prospectus p164/pr161]` |
| **Variation in objects** | Requires shareholder **special resolution**; notice published in English, Hindi and **Kannada**; promoter must provide an exit opportunity to dissenting shareholders under s.13(8) | `[Prospectus p164/pr161]` |
| Other confirmations | No part of Offer proceeds to Promoter / Promoter Group / Directors / KMP / SMP except OFS proceeds to Selling Shareholders. No arrangements with Directors/KMP/SMP in relation to Net Proceeds utilisation | `[Prospectus p164/pr161]` |
| Risk factor on variation | RF59 | `[Prospectus p79/pr76]` |
| Risk factor on non-appraisal | RF60 | `[Prospectus p79/pr76]` |

---

## 3. Restated financial information locator

Section runs **printed 312–394 / PDF 315–397**. Prepared by MSKA & Associates (FRN 105047W), partner
Ankush Agrawal, M.No. 159694, **UDIN 25159694BMLWHH3274**, report dated **16-Jul-2025**
`[Prospectus p320/pr317]`. Board approved the Restated Financial Information on **16-Jul-2025**
`[Prospectus p316/pr313]`.

### 3.1 Primary statements — Annexure map

| Annexure | Statement | PDF pages | Printed pages |
|---|---|---|---|
| — | Independent Auditor's **Examination Report** | **316–320** | 313–317 |
| — | Index of annexures | 321 | 318 |
| **I** | **Restated Statement of Assets and Liabilities** | **322–323** | 319–320 |
| **II** | **Restated Statement of Profit and Loss** (incl. OCI) | **324** | 321 |
| **III** | **Restated Statement of Changes in Equity** | **325–326** | 322–323 |
| **IV** | **Restated Statement of Cash Flows** (+ financing-liabilities reconciliation) | **327–328** | 324–325 |
| **V** | **Material Accounting Policies and Other Explanatory Notes** | **329–344** | 326–341 |
| **VI** | **Statements of Restatement Adjustments** | **345–350** | 342–347 |
| **VII** | **Notes to the Restated Financial Information** | **351–397** | 348–394 |

Signature block on each primary statement: Ankush Agrawal (Partner, MSKA), Gaurav Singh Kushwaha
(MD & CEO, DIN 01674879, Bangalore), Sameer Dilip Nath (Director, DIN 07551506, **New York**), Rumit
Dugar (CFO, Mumbai) — all dated **16-Jul-2025** `[Prospectus p323/pr320, RESTATED]`.

### 3.2 Note-number locator — Annexure VII

Basis of preparation is **Note 2.1 to Annexure V** (referenced by the auditor at
`[Prospectus p316/pr313]` and `[Prospectus p319/pr316]`).

| Note | Title | PDF page / printed page |
|---|---|---|
| 3 | Property, plant and equipment | p351 / pr348 |
| 4 | Leases | p352 / pr349 |
| 5 | Capital work in progress | p354 / pr351 |
| 6a | Other intangible assets | p354 / pr351 |
| 6b | Intangible asset under development | p355 / pr352 |
| 7 | Investments accounted for using the equity method (associate) | p356 / pr353 |
| 8 | Other financial assets (non-current and current) | p356 / pr353 |
| 9 | Non-current tax assets (net) | p357 / pr354 |
| 10 | Other assets | p357 / pr354 |
| **11** | **Inventories** | **p357 / pr354** |
| 12 | Investments — current | p358 / pr355 |
| 13 | Loans | p358 / pr355 |
| 14 | Trade receivables | p358 / pr355 |
| 15 | Cash and bank balances | p359 / pr356 |
| 16 | Other bank balances | p359 / pr356 |
| **17** | **Share capital** (incl. 17(c) CCPS/OCRPS conversion) | **p360–364 / pr357–361** |
| 18 | Other equity | p365–366 / pr362–363 |
| **19** | **Borrowings** | **p367–370 / pr364–367** |
| 20 | Lease liabilities | p371 / pr368 |
| 21 | Other financial liabilities | p371 / pr368 |
| 22 | Provisions | p371 / pr368 |
| **23** | **Gold on loan** | **p372 / pr369** |
| 24 | Trade payables (incl. MSME ageing) | p372 / pr369 |
| 25 | Other liabilities | p373 / pr370 |
| **26** | **Revenue from operations** | **p374 / pr371** |
| 27 | Other income | p374 / pr371 |
| 28 | Cost of raw materials consumed | p375 / pr372 |
| 29 | Change in inventories of FG/WIP/stock-in-trade | p375 / pr372 |
| 30 | Employee benefits expense | p375 / pr372 |
| 31 | Finance costs | p375 / pr372 |
| 32 | Depreciation and amortization expense | p376 / pr373 |
| 33 | Other expenses | p376–377 / pr373–374 |
| 34 | Employee benefits (gratuity/actuarial) | p378–379 / pr375–376 |
| 35 | Income taxes | p380 / pr377 |
| **36** | **Related party disclosures** | **p381–382 / pr378–379** |
| 37 | Earnings per share | p383 / pr380 |
| 38 | Expenditure on CSR | p383 / pr380 |
| 39 | Employee Stock Option Plan | p383–385 / pr380–382 |
| 40 | Financial instruments — fair value measurement (incl. Level 1/2/3) | p386–387 / pr383–384 |
| **41** | **Financial risk management** — (a) framework; (b) credit risk & ECL; liquidity maturity table; interest-rate risk; commodity price risk; hedge accounting | **p388–391 / pr385–388** |
| 42 | Capital management | p391 / pr388 |
| 43 | Analytical Ratios | p392 / pr389 |
| 44 | Relationship with struck-off companies | p393 / pr390 |
| **45** | **Operating segments** — single segment; domestic only, export nil | **p394 / pr391** |
| 46 | **Phantom Option Scheme 2016** — 109,715 options, settled for cash at ₹2,453.55 per option | p394 / pr391 |
| 47 | **InnoVen right-to-subscribe (RTS) 64,967 shares — terminated for ₹154.62 mn** | p394 / pr391 |
| 48 | Commitments and Contingencies | p394 / pr391 |
| 49 | Other statutory information (benami, crypto, wilful defaulter, layering, ultimate beneficiaries) | p394 / pr391 |
| **50** | **Additional information under Schedule III** — parent/subsidiary/associate split of net assets and loss; also the inter-corporate-deposit and strategic-investment tables | **p395 / pr392** |
| 51 | Investment in associate company (proportion of ownership) | p395 / pr392 |
| **52** | **Fair Value of Contingent Call Options** (Ethereal; ₹52.16 mn recognised) — *also the note the auditor's Rule 11(g) audit-trail comment points to* | **p396 / pr393** |
| 53 | ESOP Trust and Treasury Shares (3,223,260 shares) | p396 / pr393 |
| 54 | Acquisition of Ethereal House Private Limited | p396 / pr393 |
| 55 | Investment in Subsidiary and Associate (consideration and premium detail) | p396 / pr393 |
| **56** | **Events after the reporting period** (evaluated through **16-Jul-2025**) | **p396 / pr393** |
| 57 | Previous period figures regrouped/reclassified | p397 / pr394 |

### 3.3 Restatement adjustments and their reconciliation to audited numbers — Annexure VI

**The reconciliation is a null.** Verbatim, `[Prospectus p345/pr342, RESTATED]`:

> *"There are no restatement adjustments required to be made under the SEBI ICDR Regulations for the
> years ended 31 March 2025, 31 March 2024 and 31 March 2023. **Accordingly, there are no
> reconciliations between total equity and total comprehensive income as per the Restated Financial
> Information and as per the audited Financial Statements of the respective years.**"*

Annexure VI is therefore almost entirely **Part B — Non-adjusting events**. Its contents:

| Part | Content | Locator |
|---|---|---|
| Part A | *"Statement of adjustments to Restated Financial Information / Reconciliation between audited equity and restated equity"* — heading present, no reconciliation because there are no adjustments | `[Prospectus p345/pr342, RESTATED]` |
| Part B (a) | Audit qualifications not requiring adjustment — **"There are no audit qualification in auditor's report for the financial years ended 31 March 2025, 31 March 2024, and 31 March 2023 which require adjustments"** | `[Prospectus p345/pr342, RESTATED]` |
| Part B (b) | Emphasis of Matter not requiring adjustment — none | `[Prospectus p345/pr342, RESTATED]` |
| Part B (c) | Other Matter — FY2023 audited by another auditor (unmodified opinion) | `[Prospectus p345/pr342, RESTATED]` |
| **Part B (d)** | **Rule 11(g) audit-trail reporting, FY2025 and FY2024** — holding co., subsidiary and associate each separately | `[Prospectus p345/pr342]`–`[Prospectus p346/pr343, RESTATED]` |
| **Part B (e)** | **CARO matters not requiring adjustment**: FY2024 **clause ii(b)** bank quarterly-return discrepancies (HDFC/Kotak/ICICI, five quarters, line-by-line ₹ amounts); **clause vii(a)** statutory dues (PF, professional tax) in arrears >6 months; **clause ix(a)** defaults in repayment of loans/interest to named lenders | `[Prospectus p347/pr344]`–`[Prospectus p348/pr345, RESTATED]` |
| Part B (e), FY2023 | **clause ii(b)** HDFC/ICICI inventory discrepancies incl. **₹(1,983.56) mn and ₹(1,997.47) mn at 31-Mar-2023**; **clause ix(a)** defaults to InnoVen Capital, Klub Works, Oxyzo | `[Prospectus p349/pr346, RESTATED]` |
| Part B (e), FY2023 | **Corrections between audited and restated**: Series D3 and Series E >5% shareholder counts wrongly disclosed in the FY2023 audited statements, rectified in the restated | `[Prospectus p349/pr346, RESTATED]` |
| Part B (f) | **Change in equity share capital: 18,151,940 (Restated) vs 18,151,920 (Audited)** — 20 shares issued in FY2023 not disclosed in the FY2023 audited statements, rectified in the restated | `[Prospectus p350/pr347, RESTATED]` |
| Part B (g) | **Material regrouping**: FY2023 — bank charges **₹2.76 mn** reclassified from Finance costs to Other expenses | `[Prospectus p350/pr347, RESTATED]` |

### 3.4 Auditor's examination report — qualifications, modifications, and reliance

| Item | Content | Locator |
|---|---|---|
| **Qualifications on the Restated Financial Information** | Para 7(ii): *"there are no qualifications in the auditor's reports on the Financial Statements of the Company as at and for the years ended March 31, 2025, March 31, 2024 and March 31, 2023 which require any adjustments to the Restated Financial Information; **and there are other legal and regulatory matter referred to in clause 5(a) above which do not require any adjustment**"* | `[Prospectus p319/pr316]` |
| **The clause 5(a) matter — modified Rule 11(g) reporting, FY2025 holding company** | *"we are unable to comment on audit trail at database level (managed and maintained by a third-party service provider) due to absence of adequate coverage in SOC 1 Type II report"*; and separately, *"in the absence of sufficient and appropriate audit evidence, we are unable to comment on whether the statutory requirements for record retention prescribed under Rule 11(g) … "* | `[Prospectus p317/pr314]` |
| Software migration | Company **migrated to a new accounting software on 01-Oct-2024**; same database-level audit-trail limitation | `[Prospectus p317/pr314]` |
| **Subsidiary (EHPL)** | *"has used an accounting software … which do **not** have a feature of recording audit trail (edit log) facility … Accordingly, we are unable to comment whether the audit trail feature has been tampered with"* | `[Prospectus p317/pr314]`–`[Prospectus p318/pr315]` |
| **Associate (RFPL)** | Unable to comment whether the software has an audit-trail feature at all, whether it operated 12-Aug-2024 to 31-Mar-2025, or whether it was tampered with | `[Prospectus p318/pr315]` |
| FY2024 | Audit trail not enabled at **database level** in **MS Navision** throughout the year; payroll software operated by a third party, no independent service auditor's report, unable to comment | `[Prospectus p318/pr315]` |
| **Prior auditor** | **FY2023 audited by Deloitte Haskins & Sells**, report dated **30-Sep-2023**, unmodified opinion. MSKA's examination report *"in so far as it relates to the said financial year is based **solely** on the report submitted by the Previous Auditor"* | `[Prospectus p318/pr315]`–`[Prospectus p319/pr316]` |
| Board approval dates of the source financial statements | FY2025 consolidated: **24-Apr-2025**; FY2024: **17-May-2024**; FY2023: **30-Sep-2023** | `[Prospectus p317/pr314]` |
| Scope limitation on the report itself | *"Our report is intended solely for use of the Board of Directors and for inclusion in the RHP and Prospectus … should not be used, referred to or distributed for any other purpose"* | `[Prospectus p319/pr316]` |
| **Emphasis of matter (in the Special Purpose Interim Financial Statements report, reproduced as RF8)** | Draws attention to Note 2.1 — the special-purpose basis; *"may not be suitable for any another purpose"*; *"MSKA & Associates shall not be liable to the Company or to any other concerned"* | `[Prospectus p44/pr41]` |
| Prospectus's own summary of qualifications | *"There are no auditor qualifications in the examination report that have not been given effect to in the Restated Financial Information."* | `[Prospectus p27/pr24]` |

---

## 4. Capital structure locator

Section runs **printed 117–151 / PDF 120–154**.

### 4.1 Share capital table and premium

| Item | Locator |
|---|---|
| Authorised capital: 168,290,700 Equity Shares of ₹1 **plus sixteen classes of preference shares** (Series A, B, B1, B2, B3, C, D, D1, D2, D3, E, **E1 OCRPS**, E2, F, G of ₹10 each and **Series H of ₹1 each**); total ₹450,500,000 | `[Prospectus p120/pr117]` |
| Issued, subscribed and paid-up **before** the Offer: 135,459,637 Equity Shares of ₹1 | `[Prospectus p120/pr117]` |
| Issued, subscribed and paid-up **after** the Offer: 151,320,372 Equity Shares of ₹1 | `[Prospectus p120/pr117]` |
| **Securities premium: before Offer ₹32,451.30 mn → after Offer ₹40,712.27 mn** | `[Prospectus p120/pr117]` |
| Offer authorisations: Board 16-Aug-2024; Shareholders' special resolution 21-Aug-2024; Board took OFS on record 04-Aug-2025 | `[Prospectus p120/pr117]` |

### 4.2 Every round of capital raised — history tables

| Table | Content | PDF pages / printed |
|---|---|---|
| **1.A History of Equity Share capital** | Every allotment from incorporation (22-Jul-2011, 100,000 shares at ₹1 to K. Ganesh and B.M. Manjunath) through the pre-IPO rounds, with **date, number, face value, issue price, form of consideration, nature of allotment, number of allottees and named allottees**. Includes the ₹8.75 (Oct-2011), ₹321.42 (Feb-2012), ₹382.88 (2014), ₹575.64 (2015), ₹824.05 (2016), ₹959.91 (2018–2020), **₹102 rights issue (16-Feb-2022)**, and the conversions | **p121–128 / pr118–125** |
| **1.B History of Preference Share capital** | All CCPS/OCRPS series with date, number, price and allottees | **p129–136 / pr126–133** |
| Certification | *"As certified by DVD & Associates, independent practicing company secretary pursuant to their certificate dated August 13, 2025"* | `[Prospectus p139/pr136]` |

### 4.3 CCPS / OCRPS conversion

| Event | Content | Locator |
|---|---|---|
| **Bulk conversion of Preference Shares into Equity Shares, 04-Jul-2025** | Named allottee-by-allottee in the promoter-contribution lock-in table: Accel India III 16,832,970; IvyCap III 1,476,706; IvyCap II 2,539,390; Iron Pillar Fund I 3,430,210; Iron Pillar India I 2,061,160; IE Venture II 3,175,712; 360 One LVF-13 2,215,059; 360 One SOF-11 1,476,706; 360 One Seed-2 738,353 | `[Prospectus p143/pr140]`–`[Prospectus p144/pr141]` |
| **NAV effect of conversion** | *"Assuming the conversion of **35,474,930 Preference Shares to 100,224,687 Equity Shares**"* — NAV falls from ₹257.35 to **₹66.94** | `[Prospectus p166/pr163]` |
| Earlier conversions in the equity history | 11-Jul-2022 (4 Series E2 CCPS → 2 equity shares, to Ganesh Krishnan); 17-May-2024 (72,920 shares, **Series E1 OCRPS**, to Ashwin Kedia); 19-Jul-2024 (984,790 shares, Series G CCPS, 17 allottees incl. 360 One entities) | `[Prospectus p121/pr118]`–`[Prospectus p122/pr119]` |
| Accounting treatment | CCPS accounted as **financial liabilities** at 31-Mar-2022 and **reclassified to equity from 31-Mar-2023** (₹18,210.08 mn reclassification visible in Annexure III) | `[Prospectus p27/pr24]` · `[Prospectus p325/pr322, RESTATED]` |
| Note reference | Restated Note **17(c)** | `[Prospectus p360–364/pr357–361, RESTATED]` |
| Confirmation of no other convertibles | *"Except for the outstanding vested stock options granted under the ESOP 2014, our Company has no outstanding warrants, options to be issued or rights to convert debentures, loans or other convertible instruments into Equity Shares"* | `[Prospectus p154/pr151]` |

### 4.4 Consolidation, bonus and split history

| Corporate action | Detail | Locator |
|---|---|---|
| **Consolidation ₹1 → ₹10** | Board 11-Jul-2022, Shareholders 20-Jul-2022. 3,700,000 shares of ₹1 consolidated into 370,000 of ₹10. Fractional shares vested with the Promoter, who was entitled to realise and distribute the value | `[Prospectus p141/pr138]` |
| **Bonus issue** | **03-Aug-2022, 1,923,768 equity shares of ₹10, nine-for-one**, record date 20-Jul-2022, no cash consideration | `[Prospectus p140/pr137]` |
| **Split ₹10 → ₹1** | Board 03-Aug-2022, Shareholders 09-Aug-2022. Promoter's 1,395,030 shares of ₹10 split into 13,950,300 of ₹1; he then transferred 300 fractional shares to five named holders | `[Prospectus p141/pr138]` |
| Schemes of arrangement | **None** — no equity allotted under ss.391–394 / 230–234 | `[Prospectus p140/pr137]` |
| Split/consolidation in last one year | **None** | `[Prospectus p35/pr32]` |

### 4.5 Pre-IPO shareholding tables

| Table | Content | Locator |
|---|---|---|
| **Shareholding pattern as on the date of the Prospectus** | Promoter & Promoter Group **2 holders, 24,761,977 shares, 18.28%**; Public **221 holders, 110,697,660, 81.72%**; total **223 holders, 135,459,637**. Columns XII (locked-in) and XIII (**pledged/encumbered: 9,056,051 promoter shares = 36.57%; public 962,177 = 0.87%; total 10,018,228 = 37.44%**) | `[Prospectus p146/pr143]` |
| Directors / KMP / SMP shareholding | Gaurav Singh Kushwaha 24,465,127 (17.70% FD); Rumit Dugar 106,104; Sudeep Nagar 92,700; Tarun Rajput 80,000; Vipin Sharma 70,000 | `[Prospectus p147/pr144]` |
| Number of shareholders | **223** | `[Prospectus p147/pr144]` |
| **Holders ≥1% — as on date of Prospectus** | 26 named holders, 118,086,630 shares, 85.43% FD | `[Prospectus p147/pr144]`–`[Prospectus p148/pr145]` |
| Holders ≥1% — **ten days prior** | 26 named holders, 85.48% FD | `[Prospectus p148/pr145]` |
| Holders ≥1% — **one year prior** | 22 named holders; Promoter shown at **71.55% of pre-Offer equity capital / 18.48% FD** | `[Prospectus p148/pr145]`–`[Prospectus p149/pr146]` |
| Holders ≥1% — **two years prior** | 17 named holders; Promoter 65.26% / 14.46% FD | `[Prospectus p149/pr146]`–`[Prospectus p150/pr147]` |
| Promoter & Promoter Group holding | Gaurav Singh Kushwaha 24,465,127 (17.70% pre / 15.88% post, FD); **Arpita Tomar 296,850 (0.21% pre / 0.19% post)** — the only other promoter-group holder | `[Prospectus p141/pr138]` |
| Build-up of Promoter's shareholding | Every allotment/transfer since incorporation with date, number, price, nature — Oct-2011 further issue at ₹8.75, transfers from B M Manjunath / K. Ganesh / Vidya Nataraj, **rights issue 16-Feb-2022 at ₹102**, bonus, split, **rights issue 13-Aug-2024 at ₹34**, **private placement 02-Dec-2024 at ₹578** | `[Prospectus p140/pr137]`–`[Prospectus p141/pr138]` |
| Secondary transactions by Promoter / Promoter Group / Selling Shareholders, last 3 years | Acquirer-by-acquirer with dates and prices | `[Prospectus p32/pr29]`–`[Prospectus p36/pr33]` |
| WACA at which all specified securities were transacted in the last one year / 18 months / 3 years | Three separate tables | `[Prospectus p36/pr33]` |
| Sales/purchases by Promoter, Promoter Group, Directors and relatives in the six months preceding | **None** | `[Prospectus p145/pr142]` |
| Financing arrangements by Promoter/Directors for purchase of the Company's securities in the preceding six months | **None** | `[Prospectus p154/pr151]` · `[Prospectus p30/pr27]` |

### 4.6 ESOP pool and outstanding options

Single scheme: **BlueStone Jewellery and Lifestyle — Employee Stock Option Plan 2014 ("ESOP 2014")**,
adopted Board 08-May-2014 / Shareholders 09-May-2014; most recently amended Board 09-Apr-2025 /
Shareholders 02-May-2025. Certified by Rawat & Associates, certificate dated 13-Aug-2025.

| Metric, as on the date of the Prospectus | Value | Locator |
|---|---|---|
| Cumulative options **granted** | **10,066,798** (7.43% of capital) | `[Prospectus p150/pr147]` |
| Options **vested** | **2,770,029** — the number used for every "fully diluted" percentage in this document | `[Prospectus p150/pr147]` |
| Options **exercised** | **1,500,243** (all in FY2025) | `[Prospectus p150/pr147]`, `[Prospectus p151/pr148]` |
| Options **outstanding** | **4,797,243** | `[Prospectus p150/pr147]`, `[Prospectus p151/pr148]` |
| Exercise price | **₹1** in every year | `[Prospectus p151/pr148]` |
| Year-by-year grant/vest/exercise/lapse table, FY2023 → FY2025 → 01-Apr-2025 to date of RHP | Full table | `[Prospectus p150/pr147]`–`[Prospectus p153/pr150]` |
| Named grants to KMP/SMP | Rumit Dugar 64,000 / 253,752 / 547,232; **Sudeep Nagar 985,127 / 402,066 / 311,419 / 1,602,557**; Vipin Sharma, Harshit Kulin Desai, Mikhil Raj, Tarun Rajput, Gaurav Sachdeva | `[Prospectus p151/pr148]` |
| **Variation in terms, FY2024** | Vesting window extended from *"not less than one year and not more than **five** years"* to *"not more than **seven** years"* | `[Prospectus p151/pr148]` |
| Fair-value assumptions (Black-Scholes-Merton), by year | Volatility 43% / 47% / 42% / 42%; expected life 4 yrs → 4–7 yrs; risk-free 7% / 7.18% / 6.44% / 6.06%; dividend yield NIL throughout | `[Prospectus p152/pr149]` |
| Intention of option-holding KMP/SMP to sell within 3 months of listing | **"No intention to sell"** | `[Prospectus p152/pr149]`–`[Prospectus p153/pr150]` |
| Restated note on ESOP | Note 39 | `[Prospectus p383–385/pr380–382, RESTATED]` |
| ESOP Trust / treasury shares | **3,223,260 shares held by BlueStone Trust classified as treasury shares**; as at the reporting date the Trust *"no longer possesses any shares in the Company"* | `[Prospectus p396/pr393, RESTATED]` Note 53 |

### 4.7 **Lock-in table** — the exit ladder

| Lock-in class | Content | Locator |
|---|---|---|
| **Promoter's Contribution — 18 months** | Regs 14–16 SEBI ICDR. **20% of the fully diluted post-Offer capital.** Full share-by-share table with date of allotment, nature of transaction, number allotted, **number locked in**, issue/acquisition price, and % of pre- and post-Offer FD capital | `[Prospectus p142/pr139]`–`[Prospectus p144/pr141]` |
| — Promoter's own contribution (A) | **15,409,076 shares = 10.00% of post-Offer FD capital** | `[Prospectus p143/pr140]` |
| — **PC Shortfall Shares** (B) | **15,409,076 shares = 10.00%**, contributed by **nine non-promoter shareholders** by consent letters dated 02-Dec-2024 to 10-Dec-2024: Accel India III (6,361,916), IvyCap III (981,395), IvyCap II (1,502,448), Iron Pillar Fund I (1,382,001), Iron Pillar India I (830,184), IE Venture II (1,406,946), 360 One LVF-13 (1,472,093), 360 One SOF-11 (981,395), 360 One Seed-2 (490,698) | `[Prospectus p142/pr139]`, `[Prospectus p143/pr140]`–`[Prospectus p144/pr141]` |
| — **Grand total locked in for 18 months (A+B)** | **30,818,152 shares = 20.00% of post-Offer FD capital** | `[Prospectus p144/pr141]` |
| — **PC Shortfall Amount** | Promoter deposited **₹115,760,127** into the Promoter Contribution Escrow (agreement dated 04-Aug-2025) — the gap between the ₹517 Cap Price and the ₹34 acquisition price on 239,669 shares from the 13-Aug-2024 rights issue. At the final ₹517 Offer Price the actual obligation is **₹76,833,708** on 159,076 shares, and **₹38,926,419 will be refunded to the Promoter** | `[Prospectus p142/pr139]` |
| — Why a shortfall arose | Promoter's eligible shareholding falls **below 10% of post-Offer FD capital** after the Fresh Issue, so it cannot meet Reg 14 alone; Reg 15 route used | `[Prospectus p142/pr139]` |
| **Pre-IPO shareholders — 6 months** | Reg 17. Entire pre-Offer capital held by persons other than the Promoter, **except** (i) the Promoter's Contribution, (ii) shares allotted to employees under ESOP 2014 pre-Offer, and (iii) shares held by a **VCF / Cat-I or Cat-II AIF / FVCI** — those are locked in for six months **from the respective date of purchase** (with the holding period of the converted preference shares counted). Reg 8A carve-out removes that relaxation for any such fund holding, alone or in concert, **>20% of pre-Offer FD capital** | `[Prospectus p144/pr141]`–`[Prospectus p145/pr142]` |
| **Promoter's excess over the Contribution — 6 months** | Locked in six months from Allotment | `[Prospectus p142/pr139]` |
| **Anchor Investors — 90 days / 30 days** | *"**50% of the Equity Shares Allotted to Anchor Investors** in the Anchor Investor Portion shall be locked-in for a period of **90 days** from the date of Allotment and the **remaining 50%** shall be locked-in for a period of **30 days** from the date of Allotment."* | `[Prospectus p145/pr142]` |
| Pledge of locked-in shares | Reg 21 — permitted as collateral for a loan from a scheduled commercial bank / PFI / NBFC-ND-SI / HFC, subject to conditions; **for the 18-month Promoter's Contribution the loan must have been granted to the Company for the purpose of financing one or more of the objects of the Offer**. Lock-in survives invocation of the pledge | `[Prospectus p145/pr142]` |
| Transfer of locked-in shares | Reg 22 — permitted to Promoter / Promoter Group / new promoter with lock-in continuing in the transferee's hands | `[Prospectus p145/pr142]` |
| Depository recording | Reg 20 — details of locked-in shares to be recorded with the Depository | `[Prospectus p145/pr142]` |
| Selling shareholders' 1-year eligibility | All Selling Shareholders held for ≥1 year pre-DRHP; conversion holding period counted under Reg 8 | `[Prospectus p153/pr150]` |

### 4.8 Promoter pledge — the encumbrance disclosed here and nowhere else in the evidence set

> *"Our Promoter, Gaurav Singh Kushwaha, has pledged **9,215,127 Equity Shares, aggregating 6.80% of the
> pre-Offer paid-up Equity Share capital (or 37.67% of the shareholding held by Gaurav Singh
> Kushwaha), in favour of 360 One Prime Limited**, pursuant to sanction letters dated **August 2, 2024,
> and November 26, 2024**. These pledged shares are currently unpledged prior to the commencement of the
> lock-in period … Subsequently, **9,056,051 Equity Shares** of face value of ₹1 each **will be
> re-pledged** in favour of 360 One Prime Limited."*
> `[Prospectus p312/pr309]`; the same disclosure appears at `[Prospectus p141/pr138]`.

Cross-tie: the shareholding-pattern table's column XIII shows **9,056,051 promoter shares (36.57%)** as
"pledged or otherwise encumbered", footnoted *"currently unpledged for the purposes of lock in
requirements … and these will be re-pledged and will entitle the pledgee to enforce the pledge over
these Equity Shares"* `[Prospectus p146/pr143]`. Risk factor RF5 at `[Prospectus p42/pr39]`.

**This is the document that answers GAP-002** (`data/source_register.md`) at the pre-listing date. It
does not resolve the post-listing SAST Reg 31(4) filing of 24-Jun-2026, which remains a scanned image.

---

## 5. Risk factors index — specific and quantified only

Section runs **printed 34–101 / PDF 37–104**, **96 numbered risk factors**. Generic
boilerplate (macro, FEMA, FATCA, PFIC, ASM/GSM, sovereign rating, Ind AS vs IFRS, seasonality,
competition, IP, insurance, data privacy, key personnel, work stoppages, natural disasters — RF9, RF11,
RF16, RF19–20, RF25–28, RF32–34, RF39, RF41–45, RF49–57, RF61–68, RF73–74, RF77, RF80–96) is **not**
indexed here. Below are only the risk factors that carry a **number, a named counterparty, a named
legal matter, or a named dependency**.

| RF # | PDF p / pr | The specific or quantified content |
|---|---|---|
| **1** | p37 / pr34 | **Never profitable since inception.** Losses **₹2,218.37 mn (FY25), ₹1,422.36 mn (FY24), ₹1,672.44 mn (FY23)**; **negative total equity of ₹718.26 mn in FY2023** |
| **2** | p38–40 / pr35–37 | **Past non-compliances with secretarial/regulatory filings for corporate actions.** A dated, allotment-by-allotment table of missing/late Form 23, PAS-3 and MGT-14 challans running from Feb-2012 to Oct-2016, naming Accel, SVB Financial Group, Saama, Kalaari, IIFL, IvyCap, Iron Pillar |
| **3** | p40 / pr37 | **Repeat Revenue Ratio 44.61% / 39.83% / 34.67%** (FY25/24/23) — dependency on repeat customers |
| **4** | p41 / pr38 | **Inventory ₹16,525.47 mn / ₹9,912.21 mn / ₹3,953.17 mn** (FY25/24/23); purchase and manufacture **in anticipation of sales** |
| **5** | p42 / pr39 | **Promoter share pledge** — exercise by the lender could dilute his shareholding (counterparty named at p312/pr309: **360 One Prime Limited**) |
| **6** | p42 / pr39 | **Negative operating cash flow ₹6,658.28 mn (FY25) and ₹1,811.64 mn (FY24)** |
| **7** | p43 / pr40 | **The OFS is 87.88% of the Fresh Issue**; company receives none of it. Full selling-shareholder pre/post table |
| **8** | p44 / pr41 | **Emphasis of matter** in the examination report — special-purpose basis, Note 2.1; auditor's liability disclaimer quoted verbatim |
| **10** | p44–45 / pr41–42 | **Capacity utilisation by facility**: Mumbai **98.57% / 78.19% / 83.91%**; Jaipur **81.72% / 80.34% / 31.75%**; Surat **68.25% / – / –**. Certified by Rahul Rawat, Chartered Engineer, 04-Aug-2025 |
| **11** | p45 / pr42 | **Insurance claim of ₹8.83 mn for misappropriation of gold jewellery at a store, pending**; outstanding claims for products lost by transporters **nil** |
| **12** | p46 / pr43 | **Shipping charges ₹90.05 / 74.77 / 76.89 mn** (0.51% / 0.59% / 1.00% of revenue); **payment-gateway charges ₹138.32 / 98.27 / 69.13 mn** (0.67% / 0.68% / 0.72% of total expenses) |
| **13** | p46–47 / pr43–44 | **Online vs offline split: online ₹1,178.05 mn = 6.66% (FY25), ₹1,078.52 mn = 8.52% (FY24), ₹1,204.61 mn = 15.63% (FY23)**; stores and other channels the balance. States plainly: *"we are **unable to track the conversion rate** of users online sessions into actual sales from stores and other channels"* |
| **14** | p47 / pr44 | **SEBI SCORES complaints on the DRHP** alleging wrong categorisation of promoters, inadequate disclosure and omission of litigations; **appeal before the Securities Appellate Tribunal, Mumbai by C. Krishniah Chetty & Sons**, seeking a **stay of the Offer** |
| **15** | p47–48 / pr44–45 | **Four ED summons** (20-Jan-2016, 29-Jan-2021, 03-Mar-2021, 13-Mar-2023) under FEMA s.37(1)/(3) r/w IT Act s.131(1), on FDI received and on ownership of the bluestone.com domain and payment-gateway merchant identities; **M/s Jewels Online Distribution India Private Limited** named |
| **17** | p48–49 / pr45–46 | **Delays in payment of statutory dues in FY2024 and delays in repayment of loans in FY2024 and FY2023** |
| **18** | p49–50 / pr46–47 | Related party transactions — past and continuing; potential conflicts of interest |
| **19** | p50 / pr47 | **Fraud, theft and employee negligence** — past incidents of theft/damage to inventory in transit, before or during manufacturing, and at store level |
| **21** | p51 / pr48 | **Gold bullion, diamonds and other stones = 101.74% / 109.36% / 104.98% of cost of materials consumed** (FY25/24/23) — i.e. **above 100%** |
| **22** | p52 / pr49 | **184 / 207 / 170 raw-material suppliers** (FY25/24/23) — supplier count **fell** while revenue rose |
| **23** | p53 / pr50 | **Total borrowings ₹2,284.18 mn (FY23) → ₹4,304.26 mn (FY24) → ₹7,286.18 mn (FY25)** alongside the three loss years |
| **24** | p53–54 / pr50–51 | Revenue **₹7,707.26 → ₹12,658.39 → ₹17,700.02 mn** |
| **29** | p56–57 / pr53–54 | **Monthly Instalment Plan scheme** — money collected from customers; refund/suspension risk |
| **30** | p57 / pr54 | **"Blue Credits" under the Old Gold Exchange Scheme** — a claim on the Company for future purchases |
| **31** | p57–58 / pr54–55 | Substantial portion of sales from physical stores, not online — geographic concentration |
| **34** | p63–64 / pr60–61 | **Advertising and marketing = 7.76% / 8.59% / 8.81% of total expense** (FY25/24/23) |
| **35** | p64–65 / pr61–62 | Outstanding litigation against Company, Promoter and Directors (summary table cross-referenced) |
| **36** | p65 / pr62 | **Accumulated losses ₹24,583.31 mn as of 31-Mar-2025** |
| **37** | p65–66 / pr62–63 | **Delays in repayment of loans in FY2024 and FY2023** — facilities could be recalled |
| **38** | p66–68 / pr63–65 | **Working-capital loans = 19.61% / 16.26% / 45.49% of total borrowings** (FY25/24/23) |
| **40** | p68–69 / pr65–66 | **298.87 / 165.97 / 81.86 million unique online sessions** (FY25/24/23) |
| **46** | p71–72 / pr68–69 | **275 stores in 117 cities across 26 States and UTs as of 31-Mar-2025**, including Franchise Stores |
| **47** | p72 / pr69 | **Franchise model** — store owned by the franchisee but *"all operational control is exercised by our Company"* |
| **48** | p72–73 / pr69–70 | **Dependence on three manufacturing facilities — Mumbai (Maharashtra), Jaipur (Rajasthan), Surat (Gujarat)** |
| **49** | p73 / pr70 | **Gold obtained on loan basis, subject to RBI regulation** — regulatory change risk on the GML funding model |
| **53** | p75–76 / pr72–73 | **Registered and Corporate Office, all stores and all manufacturing facilities are leased / leave-and-license / rented** |
| **58** | p78–79 / pr75–76 | **"We have discontinued our 'Shop-In-Shop' (SIS) channel and corporate channel."** |
| **59** | p79 / pr76 | Variation in utilisation of Net Proceeds requires shareholder special resolution |
| **60** | p79–80 / pr76–77 | **Objects not appraised** by any bank/FI/agency; **no definitive agreements** entered in relation to the objects |
| **69** | p85 / pr82 | Promoter, Directors, KMP and SMP may have interests beyond reimbursement and normal remuneration |
| **70** | p85–86 / pr82–83 | **No dividend paid in FY2025, FY2024, FY2023 or from 01-Apr-2025 to the date of the Prospectus** |
| **71** | p86 / pr83 | **Average cost of acquisition for Promoter and Selling Shareholders may be less than the Offer Price** (₹47.92 to ₹262.76 vs ₹517) |
| **72** | p86–93 / pr83–90 | **Equity and Preference Shares issued in the preceding twelve months, some at a price lower than the Offer Price** — full dated table |
| **75** | p94 / pr91 | **RedSeer Report was exclusively commissioned and paid for by the Company** |
| **76** | p94–95 / pr91–92 | Non-GAAP measures (EBITDA, Adjusted EBITDA, Gross Profit, ROCE, Net Debt) may not be comparable across the industry |
| **78** | p95 / pr92 | **GST input/output mismatch** between services acquired and jewellery sold |
| **79** | p95 / pr92 | **Offer Price, market-cap-to-revenue multiple and EV/EBITDA may not be indicative** of the post-listing price |

### 5.1 Risk factors disclosing something absent from both annual reports

Verified by keyword search across `data/text/BLUESTONE-AR-FY2025.txt` and
`data/text/BLUESTONE-AR-FY2026.txt`. Hit counts: AR FY25 / AR FY26 / Prospectus.

| RF | The disclosure | AR presence |
|---|---|---|
| RF15 | **Directorate of Enforcement — four summons** | **0 / 0 / 3** — absent from both ARs |
| RF14 | **C. Krishniah Chetty & Sons; Securities Appellate Tribunal appeal; stay of the Offer sought** | "Krishniah" **0 / 0 / 5**; "Securities Appellate" **0 / 0 / 3** — absent from both ARs |
| RF5 | **Promoter pledge to 360 One Prime Limited** | "360 One Prime" **0 / 0 / 5** — absent from both ARs. The three "pledge" hits in each AR are (i) mutual-fund units pledged for hedging and (ii) a CARO line about pledge of securities held in a subsidiary/associate — **neither is the promoter's pledge** |
| RF2 | Secretarial/regulatory filing non-compliances table, 2012–2016 | Not present in either AR |
| RF10 | Capacity utilisation by facility | "capacity utilization"/"Capacity Utilisation" **0 / 0 / 16** |
| RF3, RF13, RF40, RF46 | Repeat Revenue Ratio, online/offline split, unique sessions, store/city counts | "Average Order Value" **0 / 0 / 24**; "Same Store" **0 / 0 / 19**; "unique online sessions" **0 / 0 / 5**; "Company Stores"/"Franchisee Stores" **0 / 0 / 48**. AR FY26 carries "Repeat Revenue" (2 hits) and "Studded" (9 hits) in its front section but not the AOV / SSSG / store-format series |
| RF22 | 184 / 207 / 170 supplier counts | "184, 207" **0 / 0 / 3** |
| RF29, RF30, RF58 | Monthly Instalment Plan; Blue Credits / Old Gold Exchange; discontinued Shop-In-Shop and corporate channels | **0 / 0 / 2**, **0 / 0 / 4**, **0 / 0 / 2** |
| RF71, RF72 | WACA and average cost of acquisition | "Weighted average cost of acquisition" **0 / 0 / 8** |

---

## 6. Business and operating metrics locator

Section **"Our Business"** runs **printed 229–266 / PDF 232–269**. Every metric below is located, not
extracted; the figures shown are those needed to identify the table.

| Metric | Value(s) as printed | Locator |
|---|---|---|
| **Store count** | **275 (FY25) / 192 (FY24) / 155 (FY23)** | `[Prospectus p240/pr237]` · `[Prospectus p251/pr248]` |
| **Store count by format** | **200 Company Stores + 75 Franchisee Stores** as of 31-Mar-2025 | `[Prospectus p247/pr244]` · `[Prospectus p255/pr252]` · `[Prospectus p176/pr173]` |
| **Towns and cities** | **117 / 80 / 71**; 26 States and UTs | `[Prospectus p240/pr237]` |
| **Store count by city tier and format** | Company Stores: Tier-I 105/55/24, Tier-II 55/28/19, Tier-III 40/13/6. Franchisee Stores: Tier-I 40/58/65, Tier-II 22/25/27, Tier-III 13/13/14 (FY25/24/23). **Franchisee count in Tier-I fell from 65 to 40 while Company Stores rose from 24 to 105** | `[Prospectus p249/pr246]` |
| **Stores opened / closed** | Opened 83 / 42 / 78, of which own 81 / 37 / 26 and franchisee 2 / 5 / 52. Closed – / 5 / – | `[Prospectus p255/pr252]` |
| **Store count and revenue by region** | South 77 stores ₹4,308.14 mn 24.34%; West 65 ₹3,915.13 mn 22.12%; East 50 ₹2,489.78 mn 14.07%; North 83 ₹6,986.97 mn 39.47% (FY25, with FY24 and FY23 columns) | `[Prospectus p256/pr253]` |
| **Total area square footage** | **608.53 / 364.48 / 287.71 thousand sq ft** | `[Prospectus p240/pr237]` |
| **Channel split (online vs stores/other)** | **Online ₹1,178.05 mn = 6.66% / ₹1,078.52 mn = 8.52% / ₹1,204.61 mn = 15.63%**; stores and other channels ₹16,521.97 / 11,579.87 / 6,502.65 mn | `[Prospectus p251/pr248]` · `[Prospectus p47/pr44]` |
| **Average Order Value** | **₹47,671.26 / 41,204.71 / 32,038.38** — defined as total retail invoice amount ÷ number of delivered orders to retail customers | `[Prospectus p241/pr238]` · `[Prospectus p251/pr248]` · `[Prospectus p27/pr24]` |
| **Customer count** | **771,845 / 562,729 / 390,959** — unique customers who have made and retained a purchase till date | `[Prospectus p241/pr238]` · `[Prospectus p27/pr24]` |
| **Repeat Revenue Ratio** | **44.61% / 39.83% / 34.67%** | `[Prospectus p242/pr239]` · `[Prospectus p40/pr37]` · `[Prospectus p176/pr173]` |
| **Studded ratio** | **Revenue from sale of studded jewellery as % of revenue from operations: 67.88% / 67.44% / 68.31%** | `[Prospectus p240/pr237]` · `[Prospectus p27/pr24]` |
| **Same Store Sales Growth** | **32.14% / 51.16% / 72.06%** | `[Prospectus p240/pr237]` · `[Prospectus p251/pr248]` |
| **Average Revenue Per Store** | **₹61.42 / 60.61 / 36.19 mn** | `[Prospectus p251/pr248]` |
| **Revenue per store per month (PSPM), by tier** | Tier-I ₹6.44 / 5.53 / 3.18 mn; Tier-II ₹5.18 / 4.46 / 2.61 mn; Tier-III ₹4.03 / 3.70 / 1.94 mn | `[Prospectus p252/pr249]` |
| **PSPM, stores operational >3 years** | **₹7.68 / 7.55 / 5.59 mn** | `[Prospectus p251/pr248]` |
| **Store cohort analysis** | Cohort chart, 18 stores opened in Fiscal 2020 highlighted | `[Prospectus p251/pr248]` |
| **Number of online sessions** | **298.87 / 165.97 / 81.86 million** | `[Prospectus p241/pr238]` |
| **Financial and operational parameters block** | Revenue, studded %, Gross Profit ₹6,715.13/5,114.98/2,456.04 mn, Gross Margin 37.94%/40.41%/31.87%, advertising %, EBITDA ₹731.64/530.49/(560.34) mn, EBITDA margin, **Adjusted EBITDA ₹1,278.06/1,054.23/(272.79) mn**, rental expense, inventory turnover 1.34/1.83/2.75, ROCE (3.67)%/(3.39)%/(31.16)%, **Net Debt with and without GML**, Net Debt/Equity — with all 13 definition footnotes | `[Prospectus p240/pr237]` |
| **Full KPI table with definitions** | Same series plus PAT margin, average inventory, number of customers, advertising cost ₹1,591.66/1,242.30/841.40 mn — 26 numbered definitions | `[Prospectus p27/pr24]`–`[Prospectus p28/pr25]` · repeated at `[Prospectus p169/pr166]`–`[Prospectus p171/pr168]` |
| **KPI comparison with listed peers** | Operational and financial parameters, FY25/24/23, BlueStone vs peer set | `[Prospectus p171/pr168]`–`[Prospectus p173/pr170]` |
| **Gold sourcing** | *"We procure our gold from banks in the form of **gold metal loans** and from metal traders."* **Bullion Price Risk Management Policy adopted by the Board on 27-Sep-2024.** Also *"we have also recently entered an arrangement with a vendor for **leasing gold**"* — monthly interest rate, gold returned or cash-settled at term end | `[Prospectus p263/pr260]` |
| **Gold metal loan mechanics in the working-capital object** | *"we place a **fixed deposit collateral** with lenders for procuring additional bullion, based on which such lenders then provide bullion to our Company on lease through gold metal loans"* | `[Prospectus p157/pr154]` |
| **GML outstanding and sanction** | Gold metal loans: sanctioned **₹7,917.50 mn**, outstanding **₹2,261.54 mn** as on 31-May-2025, at **2.50%–9.00% p.a.** | `[Prospectus p430/pr427]` |
| **"Gold on loan" balance-sheet line** | Restated Note 23 | `[Prospectus p372/pr369, RESTATED]` |
| **Gold hedging** | Fair-value hedge; notional and average rate per gram; derivative fair value ₹77.78 mn at 31-Mar-2025 | `[Prospectus p388/pr385, RESTATED]` Note 41 |
| **Other raw materials** | Silver and platinum from third-party traders; coloured stones and gemstones bought in bulk; **diamonds on 60–150 days' credit, solitaires cash-on-delivery**; all diamonds Kimberley Process certified | `[Prospectus p263/pr260]` |
| **Manufacturing — facilities** | Three operating facilities: **Mumbai (Maharashtra), Jaipur (Rajasthan), Surat (Gujarat)**, with area and address per facility; a fourth, under construction, in Jaipur | `[Prospectus p259/pr256]`–`[Prospectus p260/pr257]` · `[Prospectus p247/pr244]` |
| **Manufacturing — capacity table** | Installed capacity, average estimated annual available capacity, actual production and utilisation, **in kilograms**, by facility, FY23–FY25. Surat became operational **May-2024 with installed capacity to process 1,844.50 kg of gold**; Jaipur commenced commercial production **March-2025** and relocated within Jaipur Mar–May-2025. Certified by **Rahul Rawat, Chartered Engineer** | `[Prospectus p260–261/pr257–258]` |
| **In-house manufacturing share** | *"the **only** Leading Jewellery Retailer in India with an in-house manufacturing set-up having **more than 75% of the total jewellery produced in-house** as of Fiscal 2025"* | `[Prospectus p176/pr173]` |
| **Manufacturing process** | CAD → mould → wax → treeing → casting → setting → finishing, step by step | `[Prospectus p262/pr259]`–`[Prospectus p263/pr260]` |
| **Supply chain / logistics** | Third-party transportation by air, road and rail; inter-store stock movement; PIN-code-level demand analytics driving store siting | `[Prospectus p45/pr42]` · `[Prospectus p250/pr247]` · `[Prospectus p256/pr253]` |
| **Franchise arrangements** | *"Our franchisee agreements differ from the traditional franchisee models, in the way that they are **a form of capital arrangement** for our Company. Franchisee partners only provide capital … we typically pay them the **higher of a minimum guaranteed fixed return on the investment, or a fixed return on the revenue** generated by the store."* Stores operated entirely by the Company; leases in the Company's name; retail staff on the Company's payroll | `[Prospectus p256/pr253]` |
| **Franchise capital outstanding** | **₹2,261.68 mn funded by franchise partners as at 31-Mar-2025** | `[Prospectus p157/pr154]` |
| **Franchisee commission in Adjusted EBITDA** | Adjusted EBITDA adds back **ESOP charge and Franchisee Commission**, the latter being *"minimum guarantee on the franchisee deposits and the margin paid to the Franchisees over and above the minimum guarantee (forms part of brokerage and commission)"* | `[Prospectus p240/pr237]` |
| **Stated franchise strategy** | *"Our focus will be to **expand our network of Company Stores, to reduce dependencies on franchisees for capital**."* | `[Prospectus p251/pr248]` |
| **Lease terms** | Average lease period **5.66 years**; capital blocked in security deposits **₹535.90 mn** (Company Stores, 31-Mar-2025) | `[Prospectus p257/pr254]` |
| **Technology** | In-house full-stack proprietary IT architecture; **42-member in-house technology team** as of 31-Mar-2025; PMS software managing production flow; ERP | `[Prospectus p239/pr236]`–`[Prospectus p240/pr237]` · `[Prospectus p244/pr241]` · `[Prospectus p264–265/pr261–262]` · `[Prospectus p176/pr173]` |
| **Product portfolio** | **Over 7,400 designs, 91 collections, 16 jewellery categories** as of 31-Mar-2025 | `[Prospectus p176/pr173]` · `[Prospectus p258/pr255]` |
| **Lifetime exchange and buy-back policy** | Terms and mechanics | `[Prospectus p257/pr254]` |
| **Old Gold Exchange / higher caratage** | Customers may exchange old gold at a higher caratage value | `[Prospectus p266/pr263]` |
| **Employees** | **1,943 full-time employees** as of 31-Mar-2025; **1,264 / 1,080 / 298 contract labourers** (FY25/24/23) | `[Prospectus p233/pr230]` · `[Prospectus p268/pr265]` |
| **Market position claims (RedSeer)** | Second-largest digital-first omni-channel jewellery brand by FY2024 revenue; **28%–32% market share among omni-channel players in 2024**; 50%–60% of jewellery purchases "online influenced" | `[Prospectus p241/pr238]` |
| **Insurance, CSR, ESG, competition, IP, HR** | Sub-sections | `[Prospectus p267–269/pr264–266]` |

---

## 7. Litigation and promoter locator

### 7.1 Materiality policy — the threshold every "material" count depends on

| Threshold | Value | Locator |
|---|---|---|
| Material litigation | **>1% of turnover per the latest Restated Financial Information = >₹177.00 mn** (Board resolution 16-Jul-2025) | `[Prospectus p432/pr429]` |
| Material creditor | **>5.00% of trade payables at 31-Mar-2025 = >₹82.37 mn** | `[Prospectus p432/pr429]` · `[Prospectus p437/pr434]` |
| Group company | Promoter-Group entity with transactions **>10% of revenue from operations** in the most recent FY | `[Prospectus p442/pr439]` |
| Pre-litigation notices | **Excluded** from "material" unless the party is impleaded before a judicial/arbitral forum | `[Prospectus p432/pr429]` |

### 7.2 Outstanding litigation summary table

`[Prospectus p28/pr25]`. Counts as at the date of the Prospectus.

| Party | Criminal | Tax | Statutory/regulatory | SEBI/exchange disciplinary vs Promoter (5 yrs) | Material civil | Aggregate ₹ mn |
|---|---|---|---|---|---|---|
| By the Company | 3 | Nil | Nil | NA | Nil | — |
| **Against the Company** | **Nil** | **6** | **5** | NA | **7** | **82.83** |
| By / against the Subsidiary | Nil | Nil | Nil | Nil | Nil | Nil |
| By the Directors | Nil | Nil | Nil | Nil | Nil | — |
| Against the Directors | Nil | Nil | Nil | Nil | **1** | — |
| By the Promoter | Nil | Nil | Nil | Nil | Nil | Nil |
| **Against the Promoter** | Nil | Nil | Nil | **Nil** | **1** | Nil |
| By / against KMP and SMP | Nil | — | Nil | — | — | Nil |

Separate civil-case table: **15 civil cases against the Company (including legal notices), ₹4.23 mn to
the extent ascertainable** `[Prospectus p435/pr432]`.
Tax proceedings table: **Company Direct Tax 2 cases ₹50.94 mn (excluding interest and penalty);
Indirect Tax 4 cases ₹16.82 mn**; Subsidiary, Promoter and other Directors all Nil
`[Prospectus p437/pr434]`.

### 7.3 Matters by party — the named ones

**Actions by regulatory/statutory authorities against the Company** `[Prospectus p433/pr430]`–`[Prospectus p434/pr431]`:

| # | Authority | Matter | Status |
|---|---|---|---|
| 1 | **Reserve Bank of India** | SCN dated **31-Aug-2023** under reg 16(2) FEMA Export Regulations — failure to realise and repatriate **export value of approx. ₹15.07 mn across 532 export transactions between 2016 and 2019**; sought to show cause why the Company should not be placed on the **caution list of exporters**. 177 of 530 regularised; **original FIRCs misplaced** for the remainder; indemnities furnished to the AD Bank | **Pending** |
| 2 | **Directorate of Enforcement, Bangalore Zonal Office** | Four summons (20-Jan-2016, 29-Jan-2021, 03-Mar-2021, **13-Mar-2023**) under FEMA s.37(1)/(3) r/w IT Act s.131(1) and CPC s.30 — FDI received and its utilisation; domain and website ownership of bluestone.com; supply agreement with **M/s Jewels Online Distribution India Private Limited**; payment-gateway agreements and merchant identities | **Pending** |
| 3 | **Registrar of Companies, Karnataka** | Notice dated **12-Feb-2024** under s.206(1) Companies Act — SBO compliance under s.90 and the SBO Rules; show cause why **Bluestone Jewellery and Lifestyle Management Share Trust** was not identified as significant beneficial owner | Responded |
| 4 | **Senior Labour Inspector** | Cases under ss.21(3)/(3A) Payment of Wages Act 1936, Judicial Magistrate First Class, Bengaluru; referred to Lok Adalat | **Pending** |
| 5 | **EPFO, Sri Ganganagar** | Notice dated **21-Jan-2025** — alleged non-compliance with the EPF Act at a store employing >19 employees | Responded |

**Other material pending proceedings against the Company** `[Prospectus p434/pr431]`–`[Prospectus p435/pr432]`:

| # | Matter |
|---|---|
| 1 | **Two partition suits** by Ms. B. Sharmila and Ms. Sanmathi Cotha Pasupathy, City Civil & Sessions Court Bengaluru, claiming rights in the HUF of Mr. C. A. Venkatachalapathy Chetty, alleging **HUF/joint-family funds were used or invested in the Company**. Plaintiffs are relatives of **Mr. Ganesh Narayan and Ms. Vidya Nataraj**, erstwhile director and initial shareholders. Pending |
| 2 | **C. Krishniah Chetty & Sons** letter dated **04-Apr-2012** alleging nexus with the CKC group via Ms. Vidya Nataraj (wife of Mr. Ganesh Narayan, a CKC director); legal notice **11-Sep-2015** alleging violation of CKC's IP rights. This is also the **only** matter listed against the Promoter and against the Directors |
| 3 | Legal notice **30-Sep-2024** — copyright infringement, sound recordings played in a store without licence. Pending |
| 4 | Legal notice **28-Oct-2024** to the Company **and the Board** — alleged **blasphemy and religious insensitivity** in jewellery designs; demands cessation of manufacture and sale, delisting and a written apology. Pending |
| 5 | **SAT Appeal by C. Krishniah Chetty & Sons** challenging closure of the SEBI SCORES complaint filed **18-Feb-2025** (alleging misrepresentation of promoter classification, inadequate DRHP disclosure, misuse of CKC's reputation and omission of material litigations); complaint **auto-closed 22-Mar-2025**; appeal seeks **a stay of the Offer**. Plus a **writ petition before the High Court of Karnataka** on similar grounds, **yet to be admitted**. Both pending |
| 6 | Legal notice **13-Feb-2025** from **Titan Company Limited** alleging infringement of the trademark **"Celeste"**; Company denied and **confirmed discontinuation of use** of the word mark |

**Outstanding litigation by the Company — criminal** `[Prospectus p435/pr432]`: three FIRs/complaints
for misappropriation and theft of company assets — New BEL Road store (Sadashivanagar PS, Bengaluru);
Tambaram, Velachery Main Road store (Selaiyur PS, Chennai); and a s.200 CrPC complaint with a s.156(3)
application at Dwaraka Court, South Delhi. All pending.

**Outstanding dues to creditors, as of 31-Mar-2025** `[Prospectus p437/pr434]`: **454 creditors,
₹1,647.35 mn total** — MSMEs 148 creditors ₹362.97 mn; **material creditors 3, ₹344.86 mn**; other
creditors 303, ₹939.52 mn (including ₹431.39 mn of outstanding expenses). Names and amounts of the
three material creditors are **hosted on the company website and expressly not part of the Prospectus**
`[Prospectus p438/pr435]` — a locator that leads off the document.

**Material developments since the last balance sheet:** none other than as stated in MD&A
`[Prospectus p438/pr435]`.

### 7.4 CARO / statutory-dues matters carried in Annexure VI (not in the litigation section)

These sit in the restated financials, not in Section VI, and are easy to miss:

| Matter | Content | Locator |
|---|---|---|
| **FY2024 CARO ii(b)** | Quarterly stock/debtor/creditor statements filed with **HDFC Bank & Kotak Bank** and **ICICI Bank** **not in agreement with the books** for Q1–Q4 FY2024, with line-by-line discrepancies — largest **creditor discrepancies ₹(723.70) mn, ₹(701.27) mn, ₹(479.83) mn, ₹(814.70) mn**; purchase ₹(530.67) mn; cash ₹(352.07) mn | `[Prospectus p347/pr344, RESTATED]` |
| **FY2023 CARO ii(b)** | HDFC and ICICI inventory statements vs books: **31-Mar-2023 difference ₹(1,983.56) mn (HDFC) and ₹(1,997.47) mn (ICICI)**, explained as franchisee-location inventory consolidated under Ind AS but excluded from bank statements | `[Prospectus p349/pr346, RESTATED]` |
| **FY2024 CARO vii(a)** | Provident Fund (Karnataka, Maharashtra) and Professional Tax (Assam, Nagaland, Odisha, West Bengal, Gujarat) dues outstanding >6 months; Nagaland professional tax **"Remains unpaid till the date of audit report"** | `[Prospectus p348/pr345, RESTATED]` |
| **FY2024 CARO ix(a)** | Defaults in repayment of loans/interest to **Klub Works Private Limited (₹10.00 mn principal, ₹0.88 mn interest, 8 days), Stride Ventures (₹0.59 mn, 31 days), BMW Financial Services, Capsave Finance Private Limited (₹1.96 mn, ₹0.06 mn, ₹1.83 mn)** | `[Prospectus p348/pr345, RESTATED]` |
| **FY2023 CARO ix(a)** | Defaults to **InnoVen Capital India Private Limited, Klub Works Private Limited, Oxyzo Financial Services Private Limited** — principal and interest, days of delay | `[Prospectus p349/pr346, RESTATED]` |

### 7.5 Promoter, promoter group, group company

| Item | Content | Locator |
|---|---|---|
| **Promoter** | **Gaurav Singh Kushwaha**, aged 45, DOB 02-Oct-1979, PAN ALPPK1711L, address Bangalore. Chairman, Managing Director and CEO | `[Prospectus p311/pr308]` |
| Holding | 24,465,127 Equity Shares = **18.06% of paid-up capital / 17.70% fully diluted** | `[Prospectus p311/pr308]` |
| **Date of promoter identification** | *"Pursuant to a Board resolution dated **November 27, 2024**, our Company has identified Gaurav Singh Kushwaha as the Promoter"* — with the statement that there has been **no change in control in the last five years** | `[Prospectus p311/pr308]` |
| Promoter background / profile | Cross-referenced to "Our Management – Brief profiles of our Directors" | `[Prospectus p296/pr293]` |
| Interests of Promoter | Promotion, shareholding, dividends, and remuneration as MD & CEO | `[Prospectus p311/pr308]`–`[Prospectus p312/pr309]` |
| **Promoter pledge** | 9,215,127 shares to **360 One Prime Limited**, sanction letters 02-Aug-2024 and 26-Nov-2024; 9,056,051 to be re-pledged post lock-in | `[Prospectus p312/pr309]` |
| Disassociations in last 3 years | **None** | `[Prospectus p312/pr309]` |
| Other ventures in the same line of business | **None** | `[Prospectus p312/pr309]` |
| Confirmations | Not a Wilful Defaulter or Fraudulent Borrower; not debarred from capital markets | `[Prospectus p312/pr309]` |
| **Promoter Group — natural persons** | Shivraj Singh Kushwaha (father), Prabha Kushwaha (mother), **Arpita Tomar (spouse — the only other holder, 296,850 shares)**, Prashant Singh Kushwaha (brother), Nivaan Singh Kushwaha (son), Kayna Singh Kushwaha (daughter), Arvind Pratap Singh Tomar (spouse's father) | `[Prospectus p312/pr309]`–`[Prospectus p313/pr310]` |
| **Subsidiary** | **Ethereal House Private Limited (EHPL)**, CIN U32111HR2024PTC124350, incorporated **21-Aug-2024**, Gurgaon. Lab-grown diamonds and precious metals. BlueStone holds 100 equity + 61,567 series A1 preference = **75.52%**; Nitesh Jain 12.24%, Sharad Arora 12.24%. FY2025: net worth ₹161.34 mn, **revenue nil, PAT ₹(6.85) mn**, borrowings nil. **Common pursuits with the Company acknowledged** | `[Prospectus p291/pr288]`–`[Prospectus p292/pr289]` |
| **Associate** | **Redefine Fashion Private Limited (RFPL)** | `[Prospectus p292/pr289]`–`[Prospectus p293/pr290]` |
| **Group Company — one only** | **Redefine Fashion Private Limited.** Its reserves, sales, PAT, EPS and NAV for the preceding three years are **not printed in the Prospectus** — they are hosted on `www.bluestone.com/investor-relations.html`, and the Prospectus expressly disclaims that website content | `[Prospectus p442/pr439]` |
| RFPL shareholders' agreement | Share subscription agreement dated **11-Nov-2024** among RFPL, Sankar Bora, Deepan Babu, Bharat Mahajan, Deepak Patil and the Company; termination triggers at pr287 | `[Prospectus p516/pr513]` · `[Prospectus p290/pr287]` |
| **Related party transactions, restated period** | Restated **Note 36** — full RPT disclosure for FY2025 (consolidated), FY2024 and FY2023 (standalone) | `[Prospectus p381–382/pr378–379, RESTATED]` |
| RPT summary table (all parties, three years, each sized in ₹ mn and as % of revenue) | KMP remuneration (Gaurav Singh Kushwaha ₹30.83 / 24.25 / 31.26 mn; Rumit Dugar; Vipin Sharma; Sudeep Nagar; company secretaries), independent-director remuneration and sitting fees (all first appearing in FY2025), and **investment of ₹104.94 mn in the Associate's preference shares (0.59% of revenue)** | `[Prospectus p30/pr27]`–`[Prospectus p31/pr28]` |
| Inter-corporate deposits and strategic investments table | Stride One Capital ₹75.00 mn (9.00%), Blacksoil Capital ₹31.25 mn (7.00%), Capsave Finance ₹20.00 mn; EHPL ₹167.98 mn and RFPL ₹105.00 mn strategic investments | `[Prospectus p395/pr392, RESTATED]` Note 50 |
| Payment or benefits to Promoter / Promoter Group in the preceding two years | None beyond ordinary course and the RPT note | `[Prospectus p312/pr309]` |

**Internal inconsistency to carry forward, not to resolve here.** The litigation section opens with
*"as on the date of this Prospectus, our Company **does not have any subsidiary or group company**"*
`[Prospectus p432/pr429]`, while the same document devotes `[Prospectus p291/pr288]` to a subsidiary
(EHPL) and `[Prospectus p442/pr439]` to a group company (RFPL), and the litigation section itself then
prints "Litigation involving our Subsidiary" three paragraphs later. Recorded as read.
Similarly, the Promoter section cross-references the RPT note as **"Note 34"** `[Prospectus p312/pr309]`
while the RPT note is **Note 36** `[Prospectus p381/pr378, RESTATED]`; Note 34 is Employee benefits.

---

## 8. What the Prospectus discloses that the annual reports do NOT

Method: keyword presence tested across `data/text/BLUESTONE-AR-FY2025.txt` (230p),
`data/text/BLUESTONE-AR-FY2026.txt` (314p) and the Prospectus. Counts below are
**AR FY25 / AR FY26 / Prospectus** hits. Only differences that survived that check are listed.

### 8.1 The basis problem the ARs cannot show you

| # | Disclosure | Prospectus page | Why its absence from the ARs matters |
|---|---|---|---|
| 1 | **FY2023 and FY2024 are RESTATED STANDALONE, FY2025 is RESTATED CONSOLIDATED, and the document says the periods "are not comparable to each other"** | `[Prospectus p316/pr313]` · `[Prospectus p322/pr319, RESTATED]` · `[Prospectus p399/pr396]` | The ARs carry only FY2025 and FY2026 reported consolidated. AR FY2026 prints a four-year chart — revenue 7,707.26 / 12,658.39 / 17,700.02 / 24,412.30 and PAT (1,672.44) / (1,422.36) / (2,192.14) / 260.00 `[AR FY26, p26, REPORTED]` — **with no basis note at all**. Anyone building a FY23→FY26 series from the AR alone silently joins standalone to consolidated. This is the single largest basis trap in the run |
| 2 | **The FY2025 PAT printed in AR FY2026's chart is ₹(2,192.14) mn; the Prospectus restated consolidated FY2025 loss is ₹(2,218.37) mn and the loss attributable to owners is ₹(2,216.69) mn** | `[Prospectus p324/pr321, RESTATED]` vs `[AR FY26, p26, REPORTED]` | ₹(2,192.14) mn is identifiable in the Prospectus as the **parent's 99.69% share** in the Schedule III consolidation note `[Prospectus p395/pr392, RESTATED]` Note 50. Without the Prospectus, the ₹26.23 mn gap between the two published FY2025 losses has no explanation and looks like an unreconciled difference. **Flagged for W3/W5, not resolved here** |
| 3 | **The complete FY2023 balance sheet, P&L and cash flow** — including inventory ₹3,953.17 mn, negative total equity ₹(718.26) mn, accumulated losses ₹(20,748.50) mn at FY2023 | `[Prospectus p322–328/pr319–325, RESTATED]` | `"3,953.17"` **0 / 0 / 12**. FY2023 exists nowhere in the ARs except as three chart values. GAP-001 in the source register is confirmed: **the Prospectus is the only FY2023 statement-level source that exists** |
| 4 | **CCPS were financial liabilities at 31-Mar-2022 and reclassified to equity at 31-Mar-2023 — ₹18,210.08 mn moved through securities premium** | `[Prospectus p27/pr24]` · `[Prospectus p325/pr322, RESTATED]` | Equity in FY2023 is not comparable to equity in FY2024+ for the same reason. Neither AR states this, because neither covers FY2023 |

### 8.2 Governance, regulatory and legal facts absent from both ARs

| # | Disclosure | Prospectus page | AR hits | Why its absence matters |
|---|---|---|---|---|
| 5 | **Four Directorate of Enforcement summons under FEMA, 2016–2023**, the latest concerning ownership of the bluestone.com domain, the supply agreement with Jewels Online Distribution India Pvt Ltd, and payment-gateway merchant identities | `[Prospectus p433/pr430]` · RF15 `[Prospectus p47/pr44]` | **0 / 0 / 3** | An open FEMA enquiry into the company's foreign capital and its principal domain asset is a live regulatory exposure. A reader of the two ARs would not know it exists |
| 6 | **RBI show-cause notice of 31-Aug-2023: ₹15.07 mn of export proceeds across 532 transactions (2016–2019) unrealised; caution-list risk; original FIRCs misplaced; indemnities furnished to the AD Bank** | `[Prospectus p433/pr430]` | Absent | A record-keeping failure serious enough that the company cannot produce its own inward-remittance certificates. Speaks to internal control, and it is invisible in the ARs |
| 7 | **SAT appeal by C. Krishniah Chetty & Sons seeking a stay of the IPO; SEBI SCORES complaint alleging misrepresentation of promoter classification and omission of material litigations; writ petition before the Karnataka High Court on the same grounds** | `[Prospectus p434/pr431]`–`[Prospectus p435/pr432]` · RF14 `[Prospectus p47/pr44]` | "Krishniah" **0 / 0 / 5**; "Securities Appellate" **0 / 0 / 3** | A third party formally alleged, before a tribunal, that the offer document misstated who the promoters are. That allegation and its outcome are part of the governance record and appear in neither AR |
| 8 | **Promoter pledged 9,215,127 shares (37.67% of his holding) to 360 One Prime Limited; 9,056,051 to be re-pledged after lock-in** | `[Prospectus p141/pr138]` · `[Prospectus p312/pr309]` · `[Prospectus p146/pr143]` | "360 One Prime" **0 / 0 / 5**; the ARs' "pledge" hits are mutual-fund units pledged for hedging and a CARO line about securities of a subsidiary/associate | The promoter's entire disclosed encumbrance. The ARs do not carry it. Combined with GAP-002 (the 24-Jun-2026 SAST filing is a scanned image), **the Prospectus is currently the only readable source on promoter encumbrance in this evidence set** |
| 9 | **RoC Karnataka s.206(1) notice of 12-Feb-2024 on significant-beneficial-owner compliance, asking why the BlueStone Management Share Trust was not identified as SBO** | `[Prospectus p433/pr430]` | Absent | A regulator questioned the company's own beneficial-ownership disclosure |
| 10 | **Two HUF partition suits alleging that joint-family funds of the C. A. Venkatachalapathy Chetty HUF were invested in the Company**, naming the erstwhile director/initial shareholders Ganesh Narayan and Vidya Nataraj | `[Prospectus p434/pr431]` | "Vidya Nataraj" **0 / 0 / 6** | A title claim, however remote, over the origin of the Company's early capital |
| 11 | **Blasphemy/religious-insensitivity notice of 28-Oct-2024 served on the Company and the Board**, demanding withdrawal of products | `[Prospectus p434/pr431]` | Absent | Brand and product risk, served on the Board itself |
| 12 | **Titan Company Limited trademark notice of 13-Feb-2025 over "Celeste"; use discontinued** | `[Prospectus p435/pr432]` | Absent | The single closest listed comparable (Titan / CaratLane) took formal action against the issuer's branding |
| 13 | **Table of secretarial and regulatory filing non-compliances, 2012–2016** — missing Form 23 / PAS-3 / MGT-14 challans, allotment by allotment | `[Prospectus p38–40/pr35–37]` RF2 | Absent | A documented, itemised compliance history that the ARs' governance sections do not reproduce |
| 14 | **The promoter was identified as promoter only by Board resolution of 27-Nov-2024** — roughly nine months before listing | `[Prospectus p311/pr308]` | Absent | Directly relevant to the SCORES/SAT allegation at #7, and to how the pre-IPO cap table was characterised |
| 15 | **Prior auditor was Deloitte Haskins & Sells for FY2023; MSKA & Associates relied "solely" on Deloitte's report for that year** | `[Prospectus p318/pr315]`–`[Prospectus p319/pr316]` | "Deloitte" **0 / 0 / 3** | Establishes an auditor change *before* the 14-Jan-2026 auditor change already in the governance record. The pre-listing audit chain is only visible here |

### 8.3 Financial-statement facts absent from both ARs

| # | Disclosure | Prospectus page | AR hits | Why its absence matters |
|---|---|---|---|---|
| 16 | **FY2024 CARO clause ii(b): quarterly stock/debtor/creditor statements filed with HDFC, Kotak and ICICI did not agree with the books in all four quarters** — creditor gaps of ₹(723.70), ₹(701.27), ₹(479.83) and ₹(814.70) mn | `[Prospectus p347/pr344, RESTATED]` | Absent (FY2024 CARO is not in either AR) | Bank-facility statements diverging from the books by hundreds of millions is a working-capital-control observation of the first order, and the working-capital object is what the Fresh Issue funded |
| 17 | **FY2023 CARO clause ii(b): inventory per bank statements vs books differed by ₹(1,983.56) mn (HDFC) and ₹(1,997.47) mn (ICICI) at 31-Mar-2023**, explained by franchisee-location inventory | `[Prospectus p349/pr346, RESTATED]` | Absent | Roughly half of FY2023 closing inventory. It also quantifies the franchise-inventory consolidation question that the franchise model raises |
| 18 | **FY2024 and FY2023 CARO clause ix(a): defaults in repayment of loans/interest to InnoVen Capital, Klub Works, Oxyzo Financial Services, Stride Ventures, BMW Financial Services and Capsave Finance** | `[Prospectus p348/pr345]` · `[Prospectus p349/pr346, RESTATED]` | Klub Works **2 / 0 / 4**; Oxyzo **2 / 0 / 3**; InnoVen **8 / 0 / 22** — the names appear in AR FY2025 but the **default record does not**, and AR FY2026 has none of them | A pre-listing history of missed payments to lenders, sized and dated |
| 19 | **FY2024 CARO clause vii(a): PF and professional-tax dues outstanding beyond six months; Nagaland professional tax "remains unpaid till the date of audit report"** | `[Prospectus p348/pr345, RESTATED]` | Absent | Statutory dues in arrears is a solvency and control signal at the smallest scale |
| 20 | **Audited-vs-restated corrections for FY2023: equity share count 18,151,940 (restated) vs 18,151,920 (audited); Series D3 and Series E >5% shareholder counts wrongly disclosed in the audited statements** | `[Prospectus p349/pr346]`–`[Prospectus p350/pr347, RESTATED]` | Absent | Errors in the FY2023 audited statements, identified and corrected only in the offer document |
| 21 | **Rule 11(g) audit-trail limitations for FY2024 — MS Navision with no database-level audit trail, and payroll processed by a third party with no service-auditor report** | `[Prospectus p318/pr315]` · `[Prospectus p346/pr343, RESTATED]` | The ARs carry FY2025/FY2026 audit-trail language ("audit trail" **35 / 28 / 41**) but **not the FY2024 MS Navision or payroll findings** | Establishes that the audit-trail limitation is multi-year and pre-dates listing, not a one-off |
| 22 | **The migration to a new accounting software on 01-Oct-2024** | `[Prospectus p317/pr314]` | Absent | An ERP cut-over mid-way through the last pre-IPO year, in a year whose inventory grew 67% |
| 23 | **Phantom Option Scheme 2016: 109,715 options settled for cash at ₹2,453.55 per option; ₹261.55 mn paid in FY2024 and the balance in FY2025** | `[Prospectus p394/pr391, RESTATED]` Note 46 | "Phantom" **10 / 0 / 12** — present in AR FY2025, **absent from AR FY2026** | A cash-settled equity-linked liability that leaves the record entirely after FY2025 |
| 24 | **InnoVen right-to-subscribe over 64,967 shares, terminated for ₹154.62 mn, charged against retained earnings in FY2024** | `[Prospectus p394/pr391, RESTATED]` Note 47 · `[Prospectus p325/pr322, RESTATED]` | "154.62" **6 / 0 / 3** — in AR FY2025, absent from AR FY2026 | A pre-IPO dilution instrument bought out in cash |
| 25 | **Financial indebtedness as at 31-May-2025: sanctioned ₹18,271.54 mn vs outstanding ₹9,806.69 mn, by facility type, with tenor, interest-rate ranges (GML 2.50%–9.00%, WC 11%–13.50%, NCDs 11.25%–14.50%), security, repayment and prepayment terms** | `[Prospectus p430–431/pr427–428]` | Not disclosed in this form in either AR | The **headroom** figure — ₹8,464.85 mn unutilised — and the price of each facility. Neither AR gives sanctioned limits by facility |
| 26 | **Covenant list**, including lender consent required for changes to capital structure, ownership structure, shareholding pattern and dilution | `[Prospectus p431/pr428]` | Absent | Covenants constraining the equity story |

### 8.4 Operating and unit-economics disclosure absent from both ARs

| # | Disclosure | Prospectus page | AR hits |
|---|---|---|---|
| 27 | **Average Order Value ₹47,671.26 / 41,204.71 / 32,038.38**, with its definition | `[Prospectus p241/pr238]` | "Average Order Value" **0 / 0 / 24**; "AOV" **0 / 0 / 10** |
| 28 | **Same Store Sales Growth 32.14% / 51.16% / 72.06%** and the >12-month store definition | `[Prospectus p240/pr237]` | "Same Store" **0 / 0 / 19** |
| 29 | **Store count split by format (200 Company / 75 Franchisee) and by city tier, three years** — showing franchisee Tier-I stores falling 65 → 40 while Company Stores rose 24 → 105 | `[Prospectus p249/pr246]` · `[Prospectus p255/pr252]` | "Company Stores" **0 / 0 / 17**; "Franchisee Stores" **0 / 0 / 31** |
| 30 | **PSPM by tier, and PSPM for stores older than three years (₹7.68 / 7.55 / 5.59 mn)**, plus the store cohort chart | `[Prospectus p251/pr248]`–`[Prospectus p252/pr249]` | "PSPM" **0 / 0 / 6** |
| 31 | **Online vs offline revenue split — online fell from 15.63% of revenue in FY2023 to 6.66% in FY2025 while absolute online revenue fell from ₹1,204.61 mn to ₹1,178.05 mn** | `[Prospectus p251/pr248]` · `[Prospectus p47/pr44]` | Not disclosed in either AR |
| 32 | **The Company states it cannot track online-session-to-store conversion**: *"we are unable to track the conversion rate of users online sessions into actual sales from stores and other channels"* | `[Prospectus p47/pr44]` | Absent |
| 33 | **Capacity utilisation by facility, three years** (Mumbai 98.57% / 78.19% / 83.91%; Jaipur 81.72% / 80.34% / 31.75%; Surat 68.25% / – / –) and installed capacity in kg of gold, certified by a Chartered Engineer | `[Prospectus p45/pr42]` · `[Prospectus p260–261/pr257–258]` | "capacity utilization" / "Capacity Utilisation" **0 / 0 / 16** |
| 34 | **Raw-material supplier count 184 / 207 / 170** — falling while revenue rose 130% | `[Prospectus p52/pr49]` · `[Prospectus p263/pr260]` | **0 / 0 / 3** |
| 35 | **Gold sourced from banks as gold metal loans and from metal traders; a separate gold-leasing arrangement with a vendor; Bullion Price Risk Management Policy adopted 27-Sep-2024; diamonds on 60–150 days' credit, solitaires cash-on-delivery** | `[Prospectus p263/pr260]` | Not disclosed at this granularity; "bullion" **2 / 2 / 20** |
| 36 | **Franchise model described as a capital arrangement: franchisee funds capex and inventory, is paid the higher of a minimum guaranteed return or a fixed return on store revenue; the Company operates the store, holds the lease and employs the staff. ₹2,261.68 mn of franchise-partner capital outstanding at 31-Mar-2025. Stated strategy: expand Company Stores to reduce dependence on franchisees for capital** | `[Prospectus p256/pr253]` · `[Prospectus p157/pr154]` · `[Prospectus p251/pr248]` | The ARs mention "franchisee" (13 / 19) but not the funding mechanics, the minimum-guarantee structure, or the ₹2,261.68 mn |
| 37 | **Cost of gold bullion, diamonds and stones = 101.74% / 109.36% / 104.98% of cost of materials consumed** | `[Prospectus p51/pr48]` RF21 | Absent |
| 38 | **Discontinued "Shop-In-Shop" and corporate channels** | `[Prospectus p78/pr75]` RF58 | **0 / 0 / 2** |
| 39 | **Monthly Instalment Plan scheme and "Blue Credits" under the Old Gold Exchange Scheme** — both customer-money liabilities | `[Prospectus p56/pr53]` · `[Prospectus p57/pr54]` | **0 / 0 / 2** and **0 / 0 / 4** |
| 40 | **Average lease period 5.66 years and ₹535.90 mn of capital blocked in Company-Store security deposits** | `[Prospectus p257/pr254]` | Absent |
| 41 | **Insurance claim of ₹8.83 mn for misappropriation of gold jewellery at a store, pending** | `[Prospectus p45/pr42]` | Absent |

### 8.5 Capital-history and pricing disclosure absent from both ARs

| # | Disclosure | Prospectus page | AR hits |
|---|---|---|---|
| 42 | **Complete equity and preference share-capital history from 22-Jul-2011**, with issue price and named allottee for every round, certified by a practising company secretary | `[Prospectus p121–136/pr118–133]` | Absent |
| 43 | **The full lock-in ladder** — 18-month promoter contribution (30,818,152 shares = 20%), the nine PC Shortfall contributors, the 6-month pre-IPO lock-in and its VCF/AIF/FVCI carve-out, and the anchor 90-day/30-day split | `[Prospectus p142–145/pr139–142]` | "lock-in" **0 / 0 / 13**; "Anchor Investor" **0 / 0 / 138**. **The exit ladder that LOOP.md makes mandatory exists in no other document in the evidence set** |
| 44 | **WACA ₹311.05 per share on primary issuances; Offer Price 1.66× WACA; average cost of acquisition ₹47.92 (Promoter) to ₹262.76 (Hero)** | `[Prospectus p176/pr173]` · `[Prospectus p31/pr28]` | "Weighted average cost of acquisition" **0 / 0 / 8** |
| 45 | **Promoter's rights issue at ₹34 on 13-Aug-2024 and private placement at ₹578 on 02-Dec-2024** — a 17× price move within four months, both in the year before listing | `[Prospectus p141/pr138]` | Absent |
| 46 | **NAV per share collapses from ₹257.35 to ₹66.94 on conversion of 35,474,930 Preference Shares into 100,224,687 Equity Shares** | `[Prospectus p166/pr163]` | Absent |
| 47 | **IvyCap Ventures Trust – Fund 1 withdrew from the OFS (3,126,950 shares), and six of the seven remaining Selling Shareholders cut their offered quantity between DRHP and RHP** | `[Prospectus p153/pr150]` | Absent |
| 48 | **The ESOP 2014 vesting window was extended from five years to seven years in FY2024**, and the full grant/vest/exercise/lapse history FY2023 onward with named KMP grants | `[Prospectus p150–153/pr147–150]` | Absent |
| 49 | **Peer P/E set used to price the issue: highest Titan 88.14, lowest PC Jeweller 22.76, average 55.45, on 01-Aug-2025 closing prices**, plus the KPI-vs-peer comparison tables | `[Prospectus p166/pr163]` · `[Prospectus p171–173/pr168–170]` | "RedSeer" **0 / 4 / 122** — AR FY2026 cites RedSeer four times but carries no peer pricing set |

---

## 9. Locators that lead outside this document

Recorded because a later agent will otherwise assume the data is in the Prospectus.

| What | Where the Prospectus sends you | Locator |
|---|---|---|
| **Group Company (RFPL) financials** — reserves, sales, PAT, EPS, NAV, three years | `www.bluestone.com/investor-relations.html`, expressly **not part of the Prospectus** | `[Prospectus p442/pr439]` |
| **Names and amounts of the three material creditors** | Same website, expressly not part of the Prospectus | `[Prospectus p438/pr435]` |
| **Audited Financial Information FY2023/FY2024/FY2025** (as distinct from the restated) | Same website; the Prospectus disclaims it as not part of the offer document | `[Prospectus p398/pr395]` |
| **RedSeer Report** (source of every market-share and "second largest" claim) | Same website | `[Prospectus p399/pr396]` |

None of these four are in `data/` today. Each is a candidate gap for `records/gap_register.md`.

---

## 10. Mapping caveats

1. **This is a map.** No series has been extracted and no number has been interpreted. Figures appear
   only where they identify a table or establish a basis, and each carries a page.
2. **Page offset re-verify.** PDF = printed + 3 was confirmed on all 529 foliated pages
   programmatically. Any later agent quoting a printed page must add 3 before opening the PDF.
3. **The RHP (04-Aug-2025) has not been compared page-by-page** with the Prospectus. Both are 532 pages
   and the Prospectus text repeatedly says "the Red Herring Prospectus and this Prospectus", so the
   pagination is probably identical — **but that has not been tested, and RHP cites must not be assumed
   to share this offset.** A2's mandate was the Prospectus.
4. **AR comparisons in §8 are keyword-presence tests, not full readings** of the two annual reports.
   They establish absence of the *term*; a later agent reading the ARs in full may find a paraphrase.
   Where a term was present in one AR and not the other, that is stated explicitly.
5. **The two internal inconsistencies recorded in §7.5** (the "no subsidiary or group company"
   sentence, and the Note 34 / Note 36 cross-reference) are recorded as read. Adjudicating them is a
   later wave's job; per doctrine §10 they must not disappear from the record.

---

# PART 4 — Post-listing exchange filings

# W1_docmap_filings — the 119 post-listing exchange filings, mapped

**Agent A2 (Document Mapper), doctrine wave 1.** Company: BlueStone Jewellery and Lifestyle Limited
(NSE `BLUESTONE` / BSE `544484`), listed 19-Aug-2025. Corpus: `data/quarterly/*.pdf` (119),
`data/quarterly_text/*.txt` (119, page-marked), index `data/index/filing_index.json`, exchange
categories `data/filings/announcements_2025.json` + `announcements_2026.json` (142 announcement rows).

**This is a map, not an analysis.** No number below is offered as an input to a conclusion. Numbers
appear only where they are the *identity* of a document (share counts in an allotment intimation, the
quarter a report covers) or where the company's own wording is being quoted. Every locator is given as
`p<n>` = the PDF page number shown by the `===== PDF PAGE n =====` marker in the matching `.txt`;
where a deck prints its own slide number the form is `p<PDF>/s<slide>`.

**Cite these documents as** `[NSE ann <dd-Mmm-yyyy>, <file stem>, p<n>]`, e.g.
`[NSE ann 23-Apr-2026, 20260423_MonitoringAgencyReportFinal, p8]`.

---

## 0. What the corpus actually contains — counts, before anything else

| | Count |
|---|---|
| PDFs collected | **119** |
| Distinct PDFs by md5 | **103** (16 are exact duplicate copies — sect. 1a) |
| Of those, byte-identical to a Tier-1 document already held | **2** (both annual reports) |
| **Distinct post-listing documents not already held elsewhere** | **101** |
| Exchange announcement rows for the same window | 142 (23 announcements have no PDF in the set or share one) |

**Six corrections to `data/source_register.md` Tier 2, found by opening the files:**

1. **Management commentaries: 5, not 2.** One per quarter, Q1FY26 → Q1FY27. The register lists Nov-25
   and Jul-26 only. (`20250904_Final`, `20251104_Management_commentaryUploading`,
   `20260122_Coveringletter`, `20260423_DisclosureunderRegulation30`,
   `20260720_BlueStone_Management_Commentary_Q1FY27`.)
2. **Press releases: 5, not 3.** Same quarterly cadence.
3. **Investor presentations: 5 quarterly decks + 2 Investor-Day decks**, not "4 + 2 roadshow decks".
   There is a Q3FY26 deck (`20260122_Coveringletter_2`) the register omits, and the two June-2026
   144-page files are the *same* Investor Day deck — an original and a corrigendum — not two decks.
4. **The "auditor change (14-Jan-2026)" is an INTERNAL auditor change**, not a statutory one. A
   *separate* statutory-auditor event exists three days later (17-Jan-2026, constitution change to LLP)
   and is not in the register at all.
5. **The "director resignation (10-Mar-2026)" was not a director.** It was Gaurav Sachdeva, Chief Retail
   Officer, Senior Management Personnel. Likewise the "director resignation and cessation (30-Jun-2026)"
   was Paras Shah, Company Secretary & Compliance Officer. **No director resigned in the 13 months.**
   One director (Sameer Nath) declined re-appointment on 14-Aug-2026 — a different event.
6. **A sixth assurance-provider change is in the corpus and not in the register:** the secretarial
   auditor changed at the 14th AGM — Ms Kalaivani S for FY2024-25, Mihen Halani & Associates appointed
   for FY2025-26 to FY2029-30 (`20250929_Proceedings...`, p2).

**And one gap closes.** GAP-002 (the scanned promoter SAST filing) has been read — sect. 7. It does not
say "no encumbrance".

---

## 1. Master filing table — all 119, in date order

Column 4 says what the document *is*; column 5 says which later wave needs it. "-- do not read" means the
file is an exact duplicate and reading it buys nothing.

| Date | File stem (`data/quarterly_text/<stem>.txt`) | Pages | What it actually is | Wave |
|---|---|---|---|---|
| 2025-08-19 | `20250819_DisclosureunderCodeofConduct` | 5 | PIT Code of Practices & Procedures for Fair Disclosure of UPSI + Policy for Determination of Legitimate Purpose, adopted on listing [Reg 8(2) PIT] | W6_gov (policy baseline) |
| 2025-08-19 | `20250819_DisclosureunderRegulation30` | 1 | Reg 30(5) authorisation: names the KMP authorised to determine materiality of events (MD, CFO, CS) | W6_gov |
| 2025-08-19 | `20250819_DisclosureunderRegulation7` | 1 | Reg 7(1) intimation: KFin Technologies appointed RTA | none (housekeeping) |
| 2025-08-29 | `20250829_ConferenceCallresultsfinal` | 2 | Q1FY26 earnings-call invite (call 05-Sep-2025, 4:00pm). p2 names the panel: Kushwaha (Founder/MD/CEO) + Dugar (CFO) | W2_promise (panel composition) |
| 2025-09-04 | `20250904_Final` | 10 | **Management Commentary Q1FY26** (9 numbered pp on PDF p2-p10). Q&A format; KPI annexure p8; DataBook p9; glossary p10 | W2_promise, W3_revenue, W4_unitecon |
| 2025-09-04 | `20250904_Financial_result_June_2025` | 14 | **Q1FY26 results** (qtr ended 30-Jun-2025), unaudited. Consol limited-review report p3-p4, consol results p5, consol notes p6-p7; standalone review p8-p9, standalone results p10, standalone notes p11-p12; Annexure A p13-p14 (secretarial auditor appt) | W3 (all statement waves) |
| 2025-09-04 | `20250904_Financial_result_June_2025_2` | 14 | DUPLICATE (byte-identical) of `20250904_Financial_result_June_2025`. Same PDF filed under both 'Outcome of Board Meeting' announcements | -- do not read |
| 2025-09-04 | `20250904_Investor_presentation` | 34 | **Investor Presentation Q1FY26**, 33 slides (slide n = PDF p n+1). Stores by tier p17/s16; AOV+repeat-revenue-ratio+customers p26/s25; performance snapshot p27/s26; store unit economics (ARPS p.m., SSSG, payback) p31/s30 | W2_promise, W4_unitecon |
| 2025-09-04 | `20250904_OutcomeofPressrelease` | 3 | Press release Q1FY26 (3p) | W2_promise |
| 2025-09-05 | `20250905_StockExchangesRegulation34` | 230 | **Annual Report FY2024-25 + Notice of 14th AGM**, 230p. BYTE-IDENTICAL to `data/bronze/BLUESTONE-AR-FY2025.pdf` (md5 c1204e19...) | canonical copy is data/bronze -- do not re-read here |
| 2025-09-06 | `20250906_Conference_Call_Recording` | 1 | Q1FY26 audio-recording weblink intimation | none |
| 2025-09-06 | `20250906_StockExchangesdisclosure` | 2 | Reg 36(1)(b) letter to shareholders without registered e-mail (AR weblink/QR) | none |
| 2025-09-08 | `20250908_Cuttoffdate` | 1 | AGM cut-off date intimation (22-Sep-2025) | none |
| 2025-09-11 | `20250911_StockExchangeupload` | 22 | **Q1FY26 earnings-call transcript** (call 05-Sep-2025). Cover letter p1; transcript p2-p22 | W2_promise |
| 2025-09-16 | `20250916_Conferencecall` | 1 | Schedule-of-meet: J.P. Morgan India Consumption Forum, Mumbai, 24-Sep-2025 | W2_promise (coverage map) |
| 2025-09-17 | `20250917_DisclosureunderRegulation30` | 1 | CIN changed U72900KA2011PLC059678 -> L72900KA2011PLC059678 on listing | none |
| 2025-09-24 | `20250924_Conferencecall` | 1 | Schedule-of-meet: meeting with sell-side analysts, Mumbai, 30-Sep-2025 | W2_promise (coverage map) |
| 2025-09-29 | `20250929_ProceedingsAnnualGeneralMeeting29092025Final` | 4 | **14th AGM proceedings** (29-Sep-2025). p1-p2 attendance: all 6 directors, CFO, CS, statutory-auditor reps, scrutinizer, BOTH the outgoing FY25 secretarial auditor (Ms Kalaivani S) and the incoming FY26-FY30 one (Mihen Halani); 42 members present incl. 1 promoter. p3 the 5 resolutions incl. authorised-capital reclassification to Rs 45,05,00,000 | W6_gov |
| 2025-09-29 | `20250929_ProceedingsAnnualGeneralMeeting29092025Final_2` | 4 | DUPLICATE (byte-identical) of `20250929_Proceedings...Final`; same PDF filed under 'Shareholders meeting' and 'Amendment to AOA/MOA' | -- do not read |
| 2025-09-30 | `20250930_VotingResultuploading` | 18 | **14th AGM voting results** = Scrutinizer's Report (Parth Joshi & Co), 8 pp on PDF p2-p9. **IMAGE-ONLY** -- see sect.7. Resolution-wise tables on PDF p4-p8; p10-p18 are blank pages | W6_gov -- read the rasterised pages |
| 2025-10-11 | `20251011_NSE_Reply` | 1 | Reply to NSE surveillance query NSE/CM/Surveillance/15957 on price movement; company states there is no undisclosed UPSI | W6_gov, W7_bear |
| 2025-10-30 | `20251030_Bluestone_Q2Final` | 2 | Q2FY26 earnings-call invite (call 04-Nov-2025, 6:30pm). p2 is an image-only invite card | W2_promise |
| 2025-11-04 | `20251104_Coveringletter_merged` | 11 | **Monitoring Agency Report Q2FY26** (CARE Ratings, qtr ended 30-Sep-2025). See sect.4 | W4_capalloc |
| 2025-11-04 | `20251104_Disclosureunder` | 3 | **Statement of Deviation Q2FY26**. See sect.4 | W4_capalloc |
| 2025-11-04 | `20251104_Investor_presentationFinal` | 40 | **Investor Presentation Q2 & H1 FY26**, 39 slides. Stores by tier p17/s16; AOV etc p26/s25; balance-sheet metrics (inventory turns, ROCE, gross borrowings ex-GML) p29/s28; balance sheet p30/s29; store unit economics p33/s32 | W2_promise, W4_unitecon |
| 2025-11-04 | `20251104_Management_commentaryUploading` | 10 | **Management Commentary Q2FY26**. Standalone KPI annexure p7; **consolidated KPI page p8 (first appearance)**; DataBook p9 | W2_promise, W3, W4 |
| 2025-11-04 | `20251104_Press_releaseFinal` | 3 | Press release Q2FY26 | W2_promise |
| 2025-11-04 | `20251104_Results_september_25` | 15 | **Q2/H1FY26 results** (qtr+half ended 30-Sep-2025), unaudited. Consol: review p2-p3, results p4, **balance sheet p5, cash flow p6** (half-year mandatory), notes p7-p8. Standalone: review p9-p10, results p11, **balance sheet p12, cash flow p13**, notes p14-p15 | W3, W4_cash -- the only interim balance sheet + cash flow in the corpus |
| 2025-11-04 | `20251104_Results_september_25_2` | 15 | DUPLICATE (byte-identical) of `20251104_Results_september_25` | -- do not read |
| 2025-11-05 | `20251105_CoveringLettertostockexchanges` | 1 | Q2FY26 audio-recording weblink | none |
| 2025-11-10 | `20251110_Intimationsubmission` | 1 | Schedule-of-meet: Avendus Spark INDX Annual Investor Conference, Mumbai, 17-Nov-2025 | W2_promise (coverage map) |
| 2025-11-10 | `20251110_RevisedDisclosure` | 1 | **Revised** version of the same 10-Nov schedule-of-meet (superseded by this one; not byte-identical) | W2_promise -- canonical of the pair |
| 2025-11-12 | `20251112_Q2FY26EarningsCallTranscriptupload` | 19 | **Q2FY26 earnings-call transcript** (call 04-Nov-2025). Cover p1; transcript p2-p19 | W2_promise |
| 2025-11-27 | `20251127_AnalystsInvestorsRoadshow_27112025_Final_Uploading` | 1 | Schedule-of-meet: Non-deal roadshow, Mumbai, 02/03-Dec-2025 | W2_promise (coverage map) |
| 2025-12-03 | `20251203_DisclosureunderRegulation30` | 1 | Schedule-of-meet: Singapore non-deal roadshow, 08-10 Dec 2025 | W2_promise (coverage map) |
| 2025-12-26 | `20251226_NoticeofPostalBallotupload` | 15 | **Postal Ballot Notice dated 23-Dec-2025**, 15p. Single Special Resolution: ratification of the BlueStone ESOP 2014 under s.62(1)(b) | W6_gov, W5_dilution |
| 2026-01-03 | `20260103_ESOP_Allotment` | 2 | ESOP allotment 1,23,069 shares; capital 15,13,20,372 -> 15,14,43,441; exercise price Re.1, premium NIL | W5_dilution |
| 2026-01-14 | `20260114_StockExchnagedisclosure` | 5 | **INTERNAL auditor change** (not statutory). p1 item 1 resignation of Nexdigm Private Limited; item 2 appointment of Sudit K. Parekh & Co. LLP for the SAME year FY2025-26. Annexure A p3, Annexure B p4. p5 = image-only resignation letter | W6_gov |
| 2026-01-16 | `20260116_DisclosureunderRegulation` | 2 | Q3FY26 earnings-call invite (call 22-Jan-2026, 6:00pm) | W2_promise |
| 2026-01-17 | `20260117_DisclosureunderRegulation30` | 1 | **Statutory auditor constitution change**: M S K A & Associates (FRN 105047W) converted to M S K A & Associates LLP (FRN 105047W/W101187); same firm continues the 5-year term from 30-Sep-2023 | W6_gov |
| 2026-01-22 | `20260122_Coveringletter` | 11 | **Management Commentary Q3FY26** (11p). Standalone KPIs p8; consolidated KPIs p9; DataBook p10 | W2_promise, W3, W4 |
| 2026-01-22 | `20260122_Coveringletter_2` | 35 | **Investor Presentation Q3 & 9M FY26**, 34 slides. Stores by tier p17/s16; **'Performance Update and Growth Trends -- On Cohorts' p24/s23 (first cohort/PSPM slide)**; AOV etc p27/s26; store unit economics p32/s31 | W2_promise, W4_unitecon |
| 2026-01-22 | `20260122_Coveringletter_3` | 3 | Press release Q3FY26 | W2_promise |
| 2026-01-22 | `20260122_Coveringletter_4` | 11 | **Q3/9MFY26 results** (qtr+9M ended 31-Dec-2025), unaudited. Consol: review p2-p3, results p4, notes p5-p6. Standalone: review p7-p8, results p9, notes p10-p11. No balance sheet, no cash flow | W3 |
| 2026-01-22 | `20260122_Coveringletter_5` | 11 | DUPLICATE (byte-identical) of `20260122_Coveringletter_4` | -- do not read |
| 2026-01-22 | `20260122_DisclosureFinal` | 3 | **EtherealHouse investment -- board/audit-committee approval**, 22-Jan-2026. Annexure A p2-p3 is the Reg 30 related-party disclosure table | W6_gov, W3_RPT |
| 2026-01-22 | `20260122_DisclosureunderRegulation30` | 10 | **Monitoring Agency Report Q3FY26** (CARE Ratings, qtr ended 31-Dec-2025). See sect.4 | W4_capalloc |
| 2026-01-22 | `20260122_DisclosureunderRegulation30ESOP` | 2 | ESOP allotment 2,95,857 shares; capital 15,14,43,441 -> 15,17,39,298; exercise price Re.1, premium NIL | W5_dilution |
| 2026-01-22 | `20260122_StatementofDeviation` | 3 | **Statement of Deviation Q3FY26**. NOTE: the cover-letter subject line on p1 wrongly reads 'quarter ended September 30, 2025'; the body and the p2 table both say 31-Dec-2025. See sect.4 | W4_capalloc |
| 2026-01-23 | `20260123_ConferenceCallQ3` | 1 | Q3FY26 audio-recording weblink | none |
| 2026-01-23 | `20260123_Conferencecall` | 1 | Q3FY26 audio-recording weblink -- SAME TEXT as `20260123_ConferenceCallQ3` (different PDF bytes; the two 23-Jan 'Link of Recording' announcements). Canonical: either | -- read one only |
| 2026-01-27 | `20260127_Stockexchangeupload` | 10 | **Postal-ballot (Dec-2025) voting results**: p1 text cover; p2-p7 blank; **p8-p10 image-only Scrutinizer's Report (Mitesh J. Shah & Associates)**. See sect.7 | W6_gov -- read the rasterised pages |
| 2026-01-27 | `20260127_Stockexchangeupload_2` | 10 | DUPLICATE (byte-identical) of `20260127_Stockexchangeupload` | -- do not read |
| 2026-01-29 | `20260129_Q3FY26EarningsCallTranscriptupload` | 18 | **Q3FY26 earnings-call transcript** (call 22-Jan-2026). Cover p1; transcript p2-p18 | W2_promise |
| 2026-02-03 | `20260203_IntimationStockExchange` | 1 | Schedule-of-meet: Axis Capital Advantage India Conf 11-Feb-2026 + a 25-Feb-2026 conference | W2_promise (coverage map) |
| 2026-02-03 | `20260203_IntimationStockExchange_2` | 1 | DUPLICATE (byte-identical) of `20260203_IntimationStockExchange` | -- do not read |
| 2026-02-03 | `20260203_StockExchangeDisclosureFinal` | 2 | **EtherealHouse -- Share Subscription Agreement executed 03-Feb-2026** | W6_gov, W3_RPT |
| 2026-02-06 | `20260206_StockExchangedisclosure` | 1 | **EtherealHouse -- subscription completed**: 92,172 Series A2 CCPS at INR 2,734 each = INR 25,19,98,248 | W6_gov, W3_RPT |
| 2026-02-16 | `20260216_StockExchangedisclosureallotmentofshares` | 2 | ESOP allotment 65,494 shares; capital 15,17,39,298 -> 15,18,04,792; exercise price Re.1, premium NIL | W5_dilution |
| 2026-02-17 | `20260217_DisclosureunderRegulation30` | 1 | Schedule-of-meet: IIFL 17th Enterprising India Global Investors' Conference, 26-Feb-2026 | W2_promise (coverage map) |
| 2026-02-19 | `20260219_DisclosureunderRegulation30` | 1 | Schedule-of-meet: meeting with sell-side analysts, Mumbai, 24-Feb-2026 | W2_promise (coverage map) |
| 2026-03-02 | `20260302_StockExchnageintimation` | 1 | Schedule-of-meet: Investec India Promoter & Founder Conference 2026, 09-Mar-2026 | W2_promise (coverage map) |
| 2026-03-10 | `20260310_DisclosureunderRegulation30` | 3 | **Departure of Gaurav Sachdeva, Chief Retail Officer** (Senior Management Personnel -- NOT a director). p1 letter; **p2 is the image-only resignation letter**; p3 Annexure B. See sect.5 | W6_gov |
| 2026-03-10 | `20260310_DisclosureunderRegulation30_2` | 1 | Schedule-of-meet: UBS 'Connect the Dots -- India Consumer Tour', Bangalore, 19-Mar-2026 (same date, unrelated to the resignation above) | W2_promise (coverage map) |
| 2026-03-18 | `20260318_ESOPExercsieAllotment` | 2 | ESOP allotment 4,26,573 shares; capital 15,18,04,792 -> 15,22,31,365; exercise price Re.1, premium NIL | W5_dilution |
| 2026-04-16 | `20260416_IntimationofGrantFinal` | 5 | **ESOP GRANT** (not allotment): NRC approved 2,09,319 options on 16-Apr-2026; exercise price Rs.1 per option; vesting schedule set out p2-p5 | W5_dilution, W6_gov |
| 2026-04-17 | `20260417_CoveringLetter` | 2 | Q4/FY26 earnings-call invite (call 24-Apr-2026, 11:00am) | W2_promise |
| 2026-04-23 | `20260423_DisclosureunderRegulation30` | 12 | **Management Commentary Q4FY26** (12p). Standalone KPIs p9; consolidated KPIs p10; DataBook p11. p6 contains the explicit 'Any store closures in the quarter? No' answer | W2_promise, W3, W4 |
| 2026-04-23 | `20260423_DisclosureunderRegulation30_2` | 3 | Press release Q4/FY26 | W2_promise |
| 2026-04-23 | `20260423_DisclosureunderRegulation30_3` | 23 | **AUDITED FY2026 FULL-YEAR RESULTS** -- the 23-Apr-2026 board outcome, 23p. See sect.6 for the page map. Also carries the 1,29,573-share ESOP allotment (p2, p4) and the internal-auditor Annexure A (p3) | W3 (all), W4, W5 -- but see the OCR warning in sect.6 |
| 2026-04-23 | `20260423_DisclosureunderRegulation30_4` | 23 | DUPLICATE (byte-identical) of `..._3` | -- do not read |
| 2026-04-23 | `20260423_DisclosureunderRegulation30_5` | 23 | DUPLICATE (byte-identical) of `..._3` | -- do not read |
| 2026-04-23 | `20260423_DisclosureunderRegulation30_6` | 23 | DUPLICATE (byte-identical) of `..._3` | -- do not read |
| 2026-04-23 | `20260423_InvestorPresentation` | 42 | **Investor Presentation Q4 & FY26**, 41 slides. Stores by tier p14/s13; **ESOP-charge taper slide p23/s22**; AOV etc p28/s27; ROCE + gross borrowings p31/s30; **DataBook p33/s32**; annexure statements p35-p40 | W2_promise, W4_unitecon, W5_dilution |
| 2026-04-23 | `20260423_MonitoringAgencyReportFinal` | 9 | **Monitoring Agency Report Q4FY26** (CARE Ratings, qtr ended 31-Mar-2026). **This is the one that turns.** See sect.4 | W4_capalloc -- highest priority |
| 2026-04-23 | `20260423_StatementofDeviation` | 3 | **Statement of Deviation Q4FY26**. Declares 'No' deviation on the same day the MAR flags delay and comingling. See sect.4 | W4_capalloc |
| 2026-04-24 | `20260424_DisclosureunderRegulation30` | 1 | Q4FY26 audio-recording weblink | none |
| 2026-04-29 | `20260429_DisclosureunderRegulation30` | 21 | **Q4FY26 earnings-call transcript** (call 24-Apr-2026). Cover p1; transcript p2-p21. Longest transcript in the set | W2_promise |
| 2026-04-30 | `20260430_NoticeofPostalBallotupload` | 19 | **Postal Ballot Notice dated 23-Apr-2026**, 19p. Two Special Resolutions, both promoter-interested: (1) one-time special bonus to the MD & Chairman; (2) increase in his remuneration | W6_gov -- highest priority |
| 2026-05-19 | `20260519_DisclosureunderRegulation30` | 1 | Schedule-of-meet: Axis Capital Rising Star Conference 2026, Mumbai, 01-Jun-2026 | W2_promise (coverage map) |
| 2026-05-19 | `20260519_DisclosureunderRegulation30_2` | 1 | DUPLICATE (byte-identical) of `20260519_DisclosureunderRegulation30` | -- do not read |
| 2026-05-28 | `20260528_DisclosureunderRegulation30` | 1 | Schedule-of-meet: **Investor Day 2026**, Mumbai, 03-Jun-2026 -- the notice for the 144-page deck | W2_promise |
| 2026-06-01 | `20260601_VotingResults` | 12 | **Postal-ballot (Apr-2026) voting results**, 12p. p2-p9 machine-readable: p6 = Resolution 1 (special bonus to MD), p8 = Resolution 2 (MD remuneration increase). p10-p12 image-only Scrutinizer's Report | W6_gov -- highest priority |
| 2026-06-03 | `20260603_CoveringLetter` | 144 | **Investor Day 2026 deck, 03-Jun-2026 original issue**, 143 slides + cover letter (144 PDF pages). SUPERSEDED by the 04-Jun corrigendum version | -- use the 04-Jun file; keep this one only to diff (sect.3) |
| 2026-06-04 | `20260604_DisclosureunderRegulation30` | 144 | **Investor Day 2026 deck -- CORRIGENDUM/REVISED, canonical**, 144p. The FY30 aspiration document. See sect.3 | W2_promise -- highest priority; W4, W7 |
| 2026-06-08 | `20260608_DisclosureunderRegulation30` | 1 | Schedule-of-meet: Avendus Spark Small-Cap Investor Conference 2026, 15-Jun-2026 | W2_promise (coverage map) |
| 2026-06-09 | `20260609_DisclosureunderRegulation30` | 3 | ESOP allotment 40,843 shares; capital 15,23,60,938 -> 15,24,01,781; exercise price Re.1, premium NIL | W5_dilution |
| 2026-06-10 | `20260610_DisclosureunderRegulation30` | 1 | Schedule-of-meet: ICICI Securities Consumption Yatra, Ahmedabad, 19-Jun-2026 | W2_promise (coverage map) |
| 2026-06-18 | `20260618_DisclosureunderRegulation30` | 1 | Schedule-of-meet: Singapore non-deal roadshow, 24/25-Jun-2026 | W2_promise (coverage map) |
| 2026-06-18 | `20260618_DisclosureunderRegulation30_2` | 1 | DUPLICATE (byte-identical) of `20260618_DisclosureunderRegulation30` | -- do not read |
| 2026-06-23 | `20260623_DisclosureunderRegulation30` | 1 | Schedule-of-meet: Singapore non-deal roadshow, 30-Jun-2026 | W2_promise (coverage map) |
| 2026-06-24 | `24-Jun-2026_team_sandeshc_23062026122639_50` | 2 | **Promoter SAST Reg 31(4) annual encumbrance declaration**, filed by Gaurav Singh Kushwaha. 2p, both image-only. **NOW READ** -- see sect.7 | W6_gov, W4_capalloc -- highest priority |
| 2026-06-30 | `20260630_DisclosureunderRegulation30` | 3 | **Resignation of Paras Shah, Company Secretary & Compliance Officer (KMP)** -- NOT a director. p1 letter; p2 Annexure A; **p3 image-only resignation letter**. Filed under two exchange categories ('Resignation' and 'Cessation'). See sect.5 | W6_gov |
| 2026-06-30 | `20260630_DisclosureunderRegulation30_2` | 3 | DUPLICATE (byte-identical) of `20260630_DisclosureunderRegulation30` -- the second exchange category | -- do not read |
| 2026-07-14 | `20260714_EarningsCallInvite` | 2 | Q1FY27 earnings-call invite (call 21-Jul-2026, 11:00am) | W2_promise |
| 2026-07-20 | `20260720_Allotment_of_Equity_Shares` | 3 | ESOP allotment 4,853 shares; capital 15,24,01,781 -> 15,24,06,634; exercise price Re.1, premium NIL | W5_dilution |
| 2026-07-20 | `20260720_BlueStone_Earnings_Press_Release_Q1FY27` | 3 | Press release Q1FY27 | W2_promise |
| 2026-07-20 | `20260720_BlueStone_Investor_Presentation_Q1FY27` | 39 | **Investor Presentation Q1FY27**, 38 slides. Stores by tier p14/s13; AOV etc p29/s28; **cumulative inventory-gains + ESOP allocated-pool slide p31/s30**; DataBook p33-p35/s32-s34 | W2_promise, W4, W5_dilution |
| 2026-07-20 | `20260720_BlueStone_Management_Commentary_Q1FY27` | 9 | **Management Commentary Q1FY27** (9p). p2 Key Financial Highlights; p6 gross/net debt table; standalone KPIs p7; DataBook p8. **No consolidated KPI page** (dropped vs Q2-Q4 FY26) | W2_promise, W3, W4 |
| 2026-07-20 | `20260720_BlueStone_Monitoring_Agency_Report_Q1FY27` | 11 | **Monitoring Agency Report Q1FY27** (CARE Ratings, qtr ended 30-Jun-2026). See sect.4 | W4_capalloc |
| 2026-07-20 | `20260720_Outcome_of_BM_Financial` | 19 | **Q1FY27 results** (qtr ended 30-Jun-2026), unaudited -- merged omnibus: press release p2-p3, management commentary p4-p11, consol review p12-p13, consol results p14, consol notes p15-p16, standalone review p17, standalone results p18, standalone notes p19 | W3 |
| 2026-07-20 | `20260720_Outcome_of_BM_Other_Agenda` | 12 | Second 20-Jul-2026 board outcome (12p): trading-window note p2, ESOP allotment Annexure I p3-p4, then the SAME Q1FY27 review reports + results as `..._Financial` p5-p12 | W5_dilution; results pages are a re-file |
| 2026-07-21 | `20260721_BlueStone_Earnings_Call_Recording` | 1 | Q1FY27 audio-recording weblink | none |
| 2026-07-21 | `20260721_BlueStone_Statement_of_Deviation_Q1_FY27` | 3 | **Statement of Deviation Q1FY27**. See sect.4 | W4_capalloc |
| 2026-07-28 | `20260728_BlueStone_Earnings_Call_Transcript_Q1FY27` | 20 | **Q1FY27 earnings-call transcript** (call 21-Jul-2026). Cover p1; transcript p2-p20 ('Page 1 of 19' onwards) | W2_promise |
| 2026-08-05 | `20260805_Allotment_of_Equity_Shares` | 3 | ESOP allotment 3,42,766 shares by circular resolution; capital 15,24,06,634 -> 15,27,49,400; exercise price Re.1, premium NIL | W5_dilution |
| 2026-08-07 | `20260807_BlueStone_Intimation_of_Credit_Rating` | 1 | **New issuer credit rating**: India Ratings & Research (Fitch) assigns **IND A-/Stable**, report dated 07-Aug-2026. Issuer rating; size of issue 'Not Applicable'. The rationale itself is NOT in the corpus (GAP-004) | W4_cash, W6_gov, W8_valuation |
| 2026-08-14 | `20260814_BlueStone_Outcome_of_Board_Meeting_14August2026` | 5 | **Board changes**: (1) Sameer Nath, Non-Executive Director (DIN 07551506), retires by rotation at the 15th AGM and has 'expressed his desire not to seek re-appointment'; (2) **the FY2026 Directors' Report was REVISED after issue** to record that and to add the recommendation of Amit Jain (DIN 01613364, CEO/co-founder CarDekho) as Non-Executive Non-Independent Director; (3) AGM notice approved. Annexure I p3, Annexure II p4-p5 | W6_gov -- highest priority |
| 2026-08-17 | `20260817_Intimation_of_Book_Closure` | 1 | Book closure 08-14 Sep 2026 for the 15th AGM (14-Sep-2026) | none |
| 2026-08-17 | `20260817_Intimation_of_Notice` | 314 | **Annual Report FY2025-26 + Notice of 15th AGM**, 314p. BYTE-IDENTICAL to `data/bronze/BLUESTONE-AR-FY2026.pdf` (md5 ad949989...) | canonical copy is data/bronze -- do not re-read here |
| 2026-09-01 | `20260901_Intimation_to_stock_exchanges_Conferences_Septem` | 1 | Schedule-of-meet: Axis Capital Consumer & Tech Conf 11-Sep-2026 + a 23-Sep-2026 event | W2_promise (coverage map) |
| 2026-09-01 | `20260901_Intimation_to_stock_exchanges_Conferences_Septem_2` | 1 | DUPLICATE (byte-identical) | -- do not read |
| 2026-09-01 | `20260901_Intimation_to_stock_exchanges_Conferences_Septem_3` | 1 | DUPLICATE (byte-identical) | -- do not read |
| 2026-09-02 | `20260902_Allotment_of_Equity_Shares` | 3 | ESOP allotment 29,305 shares; capital 15,27,49,400 -> 15,27,78,705; exercise price Re.1, premium NIL | W5_dilution |
| 2026-09-02 | `20260902_Appointment_of_CS` | 2 | **Appointment of Mandar Godbole as CS & Compliance Officer** w.e.f. 02-Sep-2026. Annexure A p2 states the reason verbatim. See sect.5 | W6_gov |
| 2026-09-02 | `20260902_Outcome_of_BM` | 6 | Board outcome 02-Sep-2026 (6p): CS appointment (Annexure A p3-p4) + 29,305-share ESOP allotment (Annexure B p5-p6). Overlaps the two files above | W6_gov, W5_dilution |
| 2026-09-03 | `20260903_Stock_Exchange_Intimation_for_conferences_Sep26` | 1 | Schedule-of-meet: revised/expanded September-2026 conference schedule (supersedes the 01-Sep file) | W2_promise (coverage map) |
| 2026-09-03 | `20260903_Stock_Exchange_Intimation_for_conferences_Sep26_2` | 1 | DUPLICATE (byte-identical) | -- do not read |
| 2026-09-03 | `20260903_Stock_Exchange_Intimation_for_conferences_Sep26_3` | 1 | DUPLICATE (byte-identical) | -- do not read |

### 1a. Duplicates — 16 extra copies of 12 documents

Verified by md5 over the PDF bytes (`data/quarterly/*.pdf`), not by filename. In every case the `_2`,
`_3`… suffix is the collector's, applied because the **same PDF was filed under two or three different
exchange announcement categories** on the same day — not because two documents exist.

| Canonical file (read this) | Redundant copies | Why there are copies |
|---|---|---|
| `20250904_Financial_result_June_2025` | `_2` | filed twice under "Outcome of Board Meeting" |
| `20250929_ProceedingsAnnualGeneralMeeting29092025Final` | `_2` | "Shareholders meeting" + "Amendment to AOA/MOA" |
| `20251104_Results_september_25` | `_2` | filed twice under "Outcome of Board Meeting" |
| `20260122_Coveringletter_4` | `_5` | filed twice under "Outcome of Board Meeting" |
| `20260127_Stockexchangeupload` | `_2` | two "Shareholders meeting" postings |
| `20260203_IntimationStockExchange` | `_2` | two "Analysts/Institutional Investor Meet" postings |
| `20260423_DisclosureunderRegulation30_3` | `_4`, `_5`, `_6` | **four copies** — 2× "Outcome of Board Meeting" + 2× "General Updates" |
| `20260519_DisclosureunderRegulation30` | `_2` | two schedule-of-meet postings |
| `20260618_DisclosureunderRegulation30` | `_2` | two schedule-of-meet postings |
| `20260630_DisclosureunderRegulation30` | `_2` | filed under "Resignation" **and** "Cessation" |
| `20260901_Intimation_to_stock_exchanges_Conferences_Septem` | `_2`, `_3` | three identical postings |
| `20260903_Stock_Exchange_Intimation_for_conferences_Sep26` | `_2`, `_3` | three identical postings |

**Near-duplicates — same document, different version. Do NOT treat as identical:**

- `20260603_CoveringLetter` vs **`20260604_DisclosureunderRegulation30`** — Investor Day 2026 deck,
  original vs corrigendum. Canonical is the 04-Jun file. Eight text-layer slide differences; the
  corrigendum letter discloses four (sect. 3).
- `20251110_Intimationsubmission` vs **`20251110_RevisedDisclosure`** — the same 17-Nov conference
  intimation, revised the same day. Canonical is `RevisedDisclosure`.
- `20260123_ConferenceCallQ3` and `20260123_Conferencecall` — identical *text*, different PDF bytes.
  Either one; there is nothing in them but a weblink.
- `20260720_Outcome_of_BM_Financial` (19p) and `20260720_Outcome_of_BM_Other_Agenda` (12p) — two
  distinct board-outcome letters that **both carry the full Q1FY27 review reports and results**
  (`_Financial` p12–p19 = `_Other_Agenda` p5–p12). Read `_Financial` for the results; read
  `_Other_Agenda` only for its trading-window note and ESOP annexure.
- **`20250905_StockExchangesRegulation34` (230p) and `20260817_Intimation_of_Notice` (314p) are
  byte-identical to `data/bronze/BLUESTONE-AR-FY2025.pdf` and `BLUESTONE-AR-FY2026.pdf`.** Confirmed by
  md5. The annual reports are inside the filing corpus twice over. Cite the bronze copies; the AR PDF is
  the source of record and its page numbering is the one the rest of the run uses.

---

## 2. The five earnings-call transcripts — and the analyst list

All five are transcripts of the company's own quarterly call, hosted by the company, with **EY LLP as
investor-relations moderator (Ms Rhea Dharia; Diwakar Pingle and Avantika Mishra on the contact page)**.
No broking house sponsors any of the five. Page 1 of each PDF is the covering letter; the transcript
body begins on p2.

| Call | Held | Transcript filed | File stem | PDF pp | Transcript pp | Management on the panel |
|---|---|---|---|---|---|---|
| Q1FY26 | 05-Sep-2025 | 11-Sep-2025 | `20250911_StockExchangeupload` | 22 | p2–p22 | Kushwaha (Founder, MD & CEO); Dugar (CFO) |
| Q2FY26 | 04-Nov-2025 | 12-Nov-2025 | `20251112_Q2FY26EarningsCallTranscriptupload` | 19 | p2–p19 | Kushwaha; Dugar; **Vipin Sharma (Chief Merchandising Officer)** |
| Q3FY26 | 22-Jan-2026 | 29-Jan-2026 | `20260129_Q3FY26EarningsCallTranscriptupload` | 18 | p2–p18 | Kushwaha; Dugar (Sharma absent) |
| Q4FY26 | 24-Apr-2026 | 29-Apr-2026 | `20260429_DisclosureunderRegulation30` | 21 | p2–p21 | Kushwaha (billed **"Founder and CEO"**, not MD); Sharma; Dugar |
| Q1FY27 | 21-Jul-2026 | 28-Jul-2026 | `20260728_BlueStone_Earnings_Call_Transcript_Q1FY27` | 20 | p2–p20 | Kushwaha ("Founder and CEO"); Dugar |

> **Locator note on the panel line.** From the Q4FY26 transcript onward the cover page describes Gaurav
> Singh Kushwaha as "Founder and Chief Executive Officer" and drops "Managing Director", while he
> continues to sign every exchange letter as "Managing Director, DIN: 01674879" through 02-Sep-2026.
> A drafting change, not a filing; W6_gov should check it against the AR FY2026 board table rather than
> read anything into the transcript cover alone.

### 2a. Who asked questions, in order, per call

Names and firms exactly as the moderator announced them. A name appearing twice means the analyst was
brought back for a second turn.

| Call | Questioners in order (firm as announced) | Distinct firms |
|---|---|---|
| **Q1FY26** | Aravind Kodipaka (IME Portfolio Managers) · Tejas Shah (**"an individual investor"**) · Aditya Jain (Katrela Ventures) · Gopal (SBI Life Insurance) · Arpit Shah (Stallion Asset) · Percy (IIFL Capital) | 5 firms + 1 individual |
| **Q2FY26** | Percy Panthaki (IIFL Securities) · Tejas Shah (Avendus Spark Institutional Equities) · Harish Advani (Axis Capital) · Harsh Shah (Bandhan Asset Management) · Alok Shah (360 One Asset Management) · Kashyap Mehta (WhiteOak Alpha) · Shirish Pardeshi (Motilal Oswal) · Gopal Nawandhar (SBI Life) · Charchit Maloo (Genuity Capital) | 9 |
| **Q3FY26** | Percy Panthaki (IIFL) · Devanshu Bansal (Emkay Global) · Saurabh Jain (HDFC Life Insurance) · Tejash Shah (Avendus Spark) · Sanidhya (Unicorn Assets) · Karan Gupta (ACMIL) · Subhanu (3 Head Capital) · Abhay Sakariya (V C AN and Company) · Gopal Nawandhar (SBI Life) · **Devanshu Bansal (Emkay Global) again** | 9 |
| **Q4FY26** | Akhil Gulecha (Hornbill Capital) · Adityapal (MSA Capital Partners) · Vikram Devanathan (Prodigy Investment and Management) · Harish Advani (Axis Capital) · Kaustubh Pawaskar (ICICI Direct) · Percy Panthaki (IIFL Securities) · Abhishek Shankar (ICICI Direct) · Rajiv B (Nuvama) · Kumanika (Sameeksha Capital) · Deeya (Sapphire Capital) · **Adityapal (MSA) again** · Karan Gupta (Asit C Mehta Investments) | 10 |
| **Q1FY27** | Harish Advani (Axis Capital) · Jay Doshi (Kotak) · Devanshu Bansal (Emkay Global) · Kaivalya Baing (IIFL Capital) · Ankush Agarwal (Surge Capital) · Karan Gupta (Asit C Mehta Investment) · Pallavi (Sameeksha Capital) · Gopal Nawandhar (SBI Life) · Varun Singh (Alf Accurate Advisors) · Harsh Shah (Bandhan AMC) · Ashish Kumar (Infinity Alternatives) · Shrinarayan Mishra (Baroda BNP Paribas) | 12 |

**What the list itself says, as a mapping fact, for W2_promise to weigh:**

- **Sell-side coverage is thin and concentrated.** Across five calls the recurring sell-side names are
  IIFL (5 of 5 calls), Axis Capital (3), Avendus Spark (2), Emkay (3), ICICI Direct (1 call, 2 analysts),
  Motilal Oswal (1), Nuvama (1), Kotak (1, first appearance Q1FY27), Asit C Mehta / ACMIL (3). The rest
  of the questioner set is buy-side and boutique. IIFL and Axis Capital were both in the IPO syndicate
  (`data/source_register.md` Tier 1 names IIFL Capital and Axis Capital as BRLMs) — the two most
  persistent questioners are the banks that sold the issue.
- **The first call was the thinnest and the least institutional** — six questioners, one of whom the
  moderator announced as an individual investor, and only one sell-side house. Q1FY27 is the deepest at
  twelve. Coverage is building, not established.
- **Kotak's first appearance is Q1FY27** (28-Jul-2026), eleven months after listing.
- Nobody from a top-tier foreign house (Morgan Stanley, Goldman, JPMorgan, UBS, CLSA, Jefferies) asks a
  question on any of the five calls, although the company attended J.P. Morgan and UBS conferences
  (sect. 1 rows for 16-Sep-2025 and 10-Mar-2026).

---

## 3. Investor presentations and the Investor Day deck

Seven decks. Slide numbers are printed on the quarterly decks; **slide n = PDF page n+1** in every one of
them (PDF p1 is the covering letter). The Investor Day deck prints no slide numbers but the corrigendum
letter's own references confirm the same offset.

### 3a. The five quarterly decks — where each operating metric sits

| Metric | Q1FY26 `20250904_Investor_presentation` (34p) | Q2FY26 `20251104_Investor_presentationFinal` (40p) | Q3FY26 `20260122_Coveringletter_2` (35p) | Q4FY26 `20260423_InvestorPresentation` (42p) | Q1FY27 `20260720_..._Q1FY27` (39p) |
|---|---|---|---|---|---|
| **Store count, split Tier-I/II/III** | p17/s16 | p17/s16 | p17/s16 | **p14/s13** | **p14/s13** |
| **AOV + repeat-revenue ratio + cumulative customers** | p26/s25 | p26/s25 | p27/s26 | p28/s27 | p29/s28 |
| **Channel mix / omnichannel evidence** | p12/s11 (+p11/s10) | p12/s11 | p12/s11 | **p12–p13/s11–s12** (two slides: beyond Tier-I/II, and city penetration) | p12–p13/s11–s12 |
| **Orders / order-value mechanics** | p15/s14 | p15/s14 | p15/s14 | p19/s18 | p20/s19 |
| **Cohort data** | — (only a CAGR headline p6/s5) | — | **p24/s23 — "Performance Update and Growth Trends … On Cohorts", PSPM by cohort. First cohort slide.** | — (cohort slide dropped) | — (dropped) |
| **Store-level unit economics** (revenue/store p.m. for >3-yr stores, SSSG, breakeven) | p31/s30 (annexure) | p33/s32 (annexure) | p32/s31 (annexure) | — **annexure slide dropped** | — dropped |
| **Balance-sheet metrics** (inventory turns, ROCE, gross borrowings ex-GML) | — | p29/s28 | — | p31/s30 | — |
| **DataBook** (line-item quarterly detail) | — | — | — | **p33/s32** | **p33–p35/s32–s34** |
| **ESOP charge / dilution** | — | — | — | **p23/s22 — ESOP taper FY26→FY30** | **p31/s30 — cumulative inventory gains + "allocated pool ~9.1mn shares"** |
| **Guidance** | none | none | none | none | none |

Two disclosure-shape facts a later wave should not have to rediscover:

- **The store-level unit-economics annexure slide exists in Q1, Q2 and Q3 FY26 and disappears from
  Q4FY26 onward**, replaced by a DataBook. The cohort slide appears once (Q3FY26) and does not recur.
- **No quarterly deck contains guidance.** The management commentaries answer the question directly and
  in the negative — "What is management's take on giving guidance?" (`20250904_Final` p4;
  `20251104_Management_commentaryUploading` p4; `20260122_Coveringletter` — same question, same stance).
  Guidance exists in exactly one document in the entire corpus, and it is the Investor Day deck below.

### 3b. The 144-page June-2026 deck — what it is

**It is the "Investor Day 2026" presentation**, made at the company's own Investor Day in Mumbai on
03-Jun-2026 (notified 28-May-2026, `20260528_DisclosureunderRegulation30`). It is not a roadshow deck and
not a results deck. It runs 143 slides across a cover letter + six executive-authored sections, and it
ends with a five-year financial aspiration that appears nowhere else in the corpus.

**Two files, and only one is canonical.**

- `20260603_CoveringLetter` — the deck as presented on the day.
- **`20260604_DisclosureunderRegulation30` — the corrigendum-revised deck. This is the one to cite.**

Structure (PDF pages; slide = page − 1):

| PDF pp | Section | Presenter |
|---|---|---|
| p1 | covering letter / corrigendum letter | — |
| p2–p12 | Overview; "The India Setup"; "The Digital Shift" | Gaurav Singh Kushwaha, Founder & CEO |
| p13–p26 | "The BlueStone Thesis"; "The Opportunity & The Proof" | " |
| p27–p32 | "Technology, People & the Road Ahead" | " |
| p33–p45 | "Tech At The Core" | Mikhil Raj, Chief Product Officer |
| p46–p74 | "The Craft, The Catalogue & the Consumer" | Vipin Sharma, Chief Merchandising Officer |
| p75–p91 | "The Manufacturing Moat" | Harshit Desai, Chief Manufacturing Officer |
| p92–p99 | "The Marketing Engine" | Mikhil Raj |
| p100–p120 | "The Retail Story" | Sudeep Nagar, Chief Operating Officer |
| p121–p132 | "The Numbers Behind The Story" — ROIC drivers, cohort unit economics, network vintage, the hedging policy walk-through | Rumit Dugar, CFO |
| **p133–p143** | **"BlueStone in FY30"** — the aspiration | " |
| p144 | Thank you | — |

**Operating-metric locators inside it (this is where the cohort and guidance evidence lives):**

| What | PDF page / slide |
|---|---|
| Store count "340 across India in just 8 years" | p101/s100 |
| Consumer growth CAGR | p108/s107 |
| Revenue from repeat customers, FY22→FY26 | p109/s108 |
| AOV series (the slide the corrigendum corrected) | p110/s109 |
| Older-cohort SSSG ("older stores don't plateau") | p112–p113/s111–s112 |
| Omnichannel impact on revenue growth | p114/s113 |
| Store density / small-city analysis | p115–p116/s114–s115 |
| Unit economics at store 1 vs store 340 | p117/s116 |
| Retail expansion plan incl. FOFO | p119/s118 |
| **Cohort-wise unit economics and ROIC** (inventory turns, store-level EBITDA, ROIC by year-of-opening) | **p123/s122** |
| **Network vintage** — stores under vs over 3 years old | **p124/s123** |
| Hedging policy and the gold-price scenarios | p128–p132/s127–s131 |
| **FY30 revenue bridge** (store revenue only; excludes B2B and online) | **p134/s133** |
| **"50% CAGR: The roadmap"** — 30% SSSG + 20% new-store CAGR | **p135/s134** |
| 30% SSSG defended by older-cohort performance | p136/s135 |
| Cumulative A&P: last 4 years vs next 4 years | p137/s136 |
| FY30 distribution plan | p138/s137 |
| Margin roadmap — store maturity | p139/s138 |
| Margin roadmap — operating leverage on below-store costs | p140/s139 |
| Margin roadmap — summary | p141/s140 |
| Inventory turns by vintage | p142/s141 |
| **"BlueStone in FY30: Summary"** — the four headline FY30 targets | **p143/s142** |

> **This deck is W2_promise's single most important input.** It is the only document in 119 filings in
> which management commits to forward numbers, and it does so over a four-year horizon while declining
> quarterly guidance in every management commentary. The promise-vs-delivery test has a 5-quarter
> delivery base against a FY30 promise — state the asymmetry, do not smooth it.

### 3c. The corrigendum — four changes disclosed, at least eight made

`20260604_DisclosureunderRegulation30` p1, verbatim:

> "Please note the following changes: 1. On Slide 5 – share of affluent households in 2029 rectified from
> 50% to 40%+ 2. On Slide 109 – AOV for FY22 updated from Rs 32k in FY22 to Rs 27.9k along with CAGR
> 3. On Slide 130 – MTM call cash outflow rectified to cash inflow 4. On Slide 139 – Revenue of Rs.
> 22,342 Cr. on the bar graph rectified to Rs. 2,342 Cr."

A page-by-page diff of the two text layers shows **eight** substantive differences. The four disclosed
ones map to PDF p6, p110, p131 and p140. The four **undisclosed** ones are:

| PDF p / slide | 03-Jun text | 04-Jun text |
|---|---|---|
| p20 / s19 | "$75bn … **Today** … *Affluent households includes households having annual income > $9,400. Source: RedSeer" | "$75bn … **2024** …" — the affluent-household footnote is deleted |
| p25 / s24 | "3-4 month to operational breakeven" | "3-4 month to operational break-even" (wording only) |
| p109 / s108 | "Revenue from repeat customers improved from **growth - 32%** 54.5% in FY22 to in FY26" | the "growth -" fragment removed |
| p110 / s109 | headline "**More trust. Bigger occasions. Higher tickets.** The flywheel is working." | headline "**The relationship deepens. The economics follow.** The flywheel is working." |
| p126 / s125 | "Scale and vintage drive operating leverage Pre IndAS EBITDA **₹(20) Cr (5.7)% → ₹181 Cr 7.4%**" | "Scale and vintage drive operating leverage Pre IndAS EBITDA" — **the two figures are gone from the text layer** |

Two of these matter and neither was declared: **slide 125's Pre-IndAS EBITDA figures disappear**, and
**slide 109's headline claim is rewritten**. Caveat for whoever picks this up: these are *text-layer*
differences extracted from the PDFs; a figure can move from live text into a rasterised chart without the
slide changing visually. **W2_promise must diff the two PDFs page-for-page visually before asserting that
a number was removed.** What is safe to state now is that the corrigendum letter names four changes and
the files differ in more places than four.

The disclosed change on slide 139 is an order-of-magnitude error — a revenue base printed as
₹22,342 Cr instead of ₹2,342 Cr, on the slide that anchors the FY30 operating-leverage bridge. It was
caught by the company and corrected the next day.

---

## 4. The four Monitoring Agency Reports and the four Statements of Deviation

All eight relate to the same IPO: **Rs 820.00 crore raised, funds raised 14-Aug-2025, Monitoring Agency
CARE Ratings Limited.** Three stated objects: funding working capital requirements (Rs 750.00 cr),
general corporate purposes (Rs 20.75 cr), issue expenses (Rs 49.25 cr).

### 4a. Statements of Deviation — where the table is, and why it is empty

| Quarter covered | Filed | File stem | Pages | Object-wise table | Deviation declared? |
|---|---|---|---|---|---|
| Q2FY26 (30-Sep-2025) | 04-Nov-2025 | `20251104_Disclosureunder` | 3 | **p2, foot of page** | **No** |
| Q3FY26 (31-Dec-2025) | 22-Jan-2026 | `20260122_StatementofDeviation` | 3 | **p2, foot of page** | **No** |
| Q4FY26 (31-Mar-2026) | 23-Apr-2026 | `20260423_StatementofDeviation` | 3 | **p2, foot of page** | **No** |
| Q1FY27 (30-Jun-2026) | 21-Jul-2026 | `20260721_BlueStone_Statement_of_Deviation_Q1_FY27` | 3 | **p2, foot of page** | **No** |

Two things W4_capalloc must know before it opens these:

1. **The object-wise utilisation table in the SoDs carries no numbers.** In all four, the table headed
   "Objects for which funds have been raised and where there has been a deviation/variation, in the
   following table: Original object | Modified object | Original allocation | Modified allocation |
   Funds utilised | Amount of deviation/variation | Remarks" is completed with the single entry
   **"Not Applicable"**. The object-wise deployment numbers exist **only in the Monitoring Agency
   Reports**. Go to sect. 4b.
2. **All four answer "Is there a deviation/variation in use of funds raised?" with "No"**, and all four
   record "Comments of the Audit Committee after review: Nil" and "Comments of the auditors, if any:
   Nil". All four are signed by Rumit Dugar, CFO, on p3, over a cover letter signed by Gaurav Singh
   Kushwaha, MD, on p1.

**Locator defect to carry forward:** the Q3FY26 SoD (`20260122_StatementofDeviation`) has the wrong
quarter in its cover-letter **subject line** — "for the quarter ended September 30, 2025" — while the
body of the same page says "for quarter ended December 31, 2025" and the p2 table says "Report filed for
Quarter ended 31st December, 2025". It is the Q3 statement. Cite it as such and note the subject line.

### 4b. Monitoring Agency Reports — page-precise locators

Every MAR has the same shape: p1 company covering letter, p2 CARE transmittal letter, p3 the summary
declaration ("Deviation from the objects", "Range of Deviation"), then numbered sections 1–5.

| Quarter | Filed | File stem | Pages | §4(i) Cost of objects | **§4(ii) Progress in the objects — the object-wise utilisation table** | §4(iii) Deployment of unutilised proceeds | §4(iv) Delay in implementation | §5 GCP utilisation |
|---|---|---|---|---|---|---|---|---|
| Q2FY26 (30-Sep-2025) | 04-Nov-2025 | `20251104_Coveringletter_merged` | 11 | p5 | **p5 (rows) → p6 (Total row)** | p6–p9 | p9 | p9–p10 |
| Q3FY26 (31-Dec-2025) | 22-Jan-2026 | `20260122_DisclosureunderRegulation30` | 10 | p5 | **p5 (rows) → p6 (Total row)** | p7–p8 | p8 | p8–p9 |
| Q4FY26 (31-Mar-2026) | 23-Apr-2026 | `20260423_MonitoringAgencyReportFinal` | 9 | p5 | **p6 (rows) → p7 (Total row)** | p7 | **p8** | p8 |
| Q1FY27 (30-Jun-2026) | 20-Jul-2026 | `20260720_BlueStone_Monitoring_Agency_Report_Q1FY27` | 11 | p6 | **p6–p7 (rows) → p8 (Total row)** | p8 | **p9** | p9–p10 |

The §4(ii) table's columns are: `Sr. No | Item Head | Source of information | Amount as proposed in the
Offer Document (Rs Cr) | Amount utilised: as at beginning of quarter / during the quarter / at end of
quarter | Total unutilised amount (Rs cr) | Comments of the Monitoring Agency | Comments of the Board`.
The three rows are the three objects; the Total row is on the following page in every report.

**Certifier changed after two quarters.** The CA certificate underpinning the MAR is from
**M S K A & Associates** (the statutory auditor) for Q2FY26 — dated 02-Nov-2025, UDIN
25159694BMLWKV2425 — and from **M/s. Sudit K. Parekh & Co. LLP** for Q3FY26 onward (15-Jan-2026,
14-Apr-2026, 13-Jul-2026). Sudit K. Parekh & Co. LLP is the same firm appointed **internal auditor** on
14-Jan-2026. W6_gov should look at that: from Q3FY26 the certificate the Monitoring Agency relies on is
signed by the internal auditor rather than the statutory auditor.

### 4c. Does any of them declare a deviation? Yes — and the answer changes at Q4FY26

The headline field says no in all four. The body does not.

| | Q2FY26 p3 | Q3FY26 p3 | Q4FY26 p3 | Q1FY27 p3 |
|---|---|---|---|---|
| "Deviation from the objects" | **No** | **No** | **Nil** | **Nil** |
| "Range of Deviation" | Not applicable | Not applicable | Nil | Not Applicable |

But inside §3 "Details of the arrangement made to ensure the monitoring of issue proceeds":

- **Q2FY26, p4** — "Is there any major deviation observed over the earlier monitoring agency reports?
  **Not applicable** … This is the first monitoring agency report for the issue."
- **Q3FY26, p4** — "Is there any major deviation observed over the earlier monitoring agency reports?
  **No** … There are no deviations over the previous monitoring agency report."
- **Q4FY26, p4** — "Whether all utilization is as per the disclosures in the Offer Document? **No** …
  *The offer document stipulates the timeline for deployment of net proceeds as March 31, 2026. However,
  gross IPO proceeds of Rs. 56.63 crore remain unutilized as on March 31, 2026. The MA has not received
  any supporting approvals for extension of timeline for deployment of net proceeds. Refer to detailed
  note under point iv for more details. The company has transferred funds from MA account to current
  accounts for utilization of proceeds resulting in comingling of funds.*"
- **Q4FY26, p5** — "Is there any major deviation observed over the earlier monitoring agency reports?
  **Yes** … *The previous MA report dated January 22, 2026 did not specify any delay in implementation of
  the objects of issue. However, the current MA report specifies a delay in implementation of the objects
  of issue.*"
- **Q4FY26, p5** — "Are there any favorable/unfavorable events affecting the viability of these
  object(s)? **Yes** … *There is a delay in utilization of net proceeds beyond the timeline of March 31,
  2026 as stipulated in the offer document, which may affect the viability of the objects.*"
- **Q4FY26, p5** — "Is there any other relevant information that may materially affect the decision
  making of the investors? **Yes**" — followed by the loss history.
- **Q4FY26, p8, §4(iv)** — both monitored objects marked "**Delay (exact number of days
  unascertainable)**".
- **Q1FY27, p4** — "Whether all utilization is as per the disclosures in the Offer Document? **No**" —
  with the comingling sentence repeated, but now: "*The board has, vide resolution dated April 23, 2026,
  approved the extension of timeline for utilisation of balance net proceeds till March 31, 2027.*"
- **Q1FY27, p5** — "Is there any major deviation observed over the earlier monitoring agency reports?
  **Yes** … *The previous monitoring agency report dated April 23, 2026 stated that the MA has not
  received any Board approval for the extension of timeline … The MA has now received board resolution
  dated April 23, 2026.*"
- **Q1FY27, p9, §4(iv)** — general corporate purposes now shows "**Delay (79 days)**"; working capital
  still "Delay (exact number of days unascertainable)".
- **Q1FY27, p9, §5** — the first non-nil GCP utilisation appears, described as repayment of
  non-convertible debentures (ISIN INE304W07092), authorised by a board resolution of 04-Nov-2025 and
  confirmed by CFO e-mail of 10-Jun-2026.

> **The single most important pointer in this section.** On **23-Apr-2026 the company filed both
> `20260423_StatementofDeviation` — "Is there a deviation/variation in use of funds raised? No",
> audit-committee comments "Nil" — and `20260423_MonitoringAgencyReportFinal`, in which the Monitoring
> Agency records that utilisation is **not** as per the offer document, that it has received no approval
> for the timeline extension, and that funds were comingled.** Same day, same board meeting, two
> documents, opposite postures. W4_capalloc extracts the numbers; W6_gov and W7 own the contradiction.
> Do not resolve it by preferring either document — doctrine §2c and §10 both forbid that.

**One extraction caveat, flagged not solved.** In the Q2FY26 MAR, the p5 §4(ii) row for "Funding working
capital requirements" shows a total-unutilised figure that does not tie to that row's own
proposed-minus-utilised arithmetic, and the p6 Total row does not tie to the sum of the three row
residuals as they extract from the text layer. This may be a column-alignment artefact of the text
extraction rather than an error in the report. **W4_capalloc must read the §4(ii) table off the PDF, not
off the `.txt`, and must tie the Total row before using any of it.**

---

## 5. The governance event file — with the company's stated reasons, verbatim

Nine events plus nine ESOP actions in thirteen months. Reasons are quoted exactly; where the company
gave a reason twice (letter and annexure) both are given, because the wording differs.

### 5a. Assurance providers — three changes, none of them a statutory-auditor replacement

**(1) Internal auditor resigned mid-year — 14-Jan-2026.** `20260114_StockExchnagedisclosure`, p1 and p3.
Exchange category: "Change in Auditors".

> p1: *"please note that the M/s Nexdigm Private Limited, Internal Auditor of the Company for the
> financial year 2025-2026, has tendered its resignation vide letter dated January 14, 2026, **due to
> pre-occupied other commitments**. The internal Auditor has confirmed that there are no material reasons
> for resignation other than those mentioned in the resignation letter."*
>
> p3, Annexure A, "Reason for Change": *"M/s Nexdigm Private Limited has vide its Resignation Letter
> dated 14th January, 2026 resigned as the Internal Auditors of the Company **due to pre-occupied other
> commitments**"*

Same letter, p1 item 2: **M/s. Sudit K. Parekh & Co. LLP appointed internal auditor the same day**, for
the same financial year 2025-26, effective 14-Jan-2026. The resignation letter itself is on p5 and is
image-only (sect. 7).

**(2) Statutory auditor's constitution changed — 17-Jan-2026.** `20260117_DisclosureunderRegulation30`,
p1. Exchange category: "General Updates" — *not* "Change in Auditors".

> *"the Statutory Auditors of the Company, M S K A & Associates, Chartered Accountants (the "Firm") have
> intimated the Company that the Firm has converted itself into a Limited Liability Partnership ("LLP")
> under the provisions of the Limited Liability Partnership Act, 2008 and is now known as "M S K A &
> Associates LLP", with ICAI Firm Registration No.105047W/W101187. Further, they will continue to
> function and discharge their obligations as Statutory Auditors for the remaining period of their
> current tenure."*

This is a conversion, not a change of auditor. The five-year appointment dates from the members'
resolution of 30-Sep-2023.

**(3) Secretarial auditor changed at the 14th AGM — 29-Sep-2025.**
`20250929_ProceedingsAnnualGeneralMeeting29092025Final`, p2 attendance list and p3 resolution (iv). Both
the outgoing FY2024-25 secretarial auditor (Ms Kalaivani S) and the incoming one attended the same AGM:

> p3: *"Members by an ordinary resolution have approved the appointment of M/s. Mihen Halani and
> Associates, Company Secretaries as the Secretarial Auditors of the Company for a term of (5)
> consecutive years."*

### 5b. Personnel departures — neither of them a director

**(4) Chief Retail Officer — resigned 09-Mar-2026, disclosed 10-Mar-2026.**
`20260310_DisclosureunderRegulation30`. Exchange category: "Resignation" (NSE's own description reads
"Resignation of Mr Gaurav Sachdeva as **Other** of the company").

> p1: *"we wish to inform that Mr. Gaurav Sachdeva- Chief Retail Officer (designated as Senior Management
> Personnel), has tendered his resignation from the services of the Company effective from the close of
> business hours of March 09, 2026."*
>
> p2, his own letter, as OCR'd from the image: *"I hereby tender my resignation from the position of
> Chief Retail Officer **due to personal reasons and pursue other career opportunities outside the
> organization**. I would request you to relieve me of my duties with effect from the close of business
> hours on March 9[th], 2026. I hereby confirm that there are no other material reasons for my
> resignation other than those mentioned above."*
>
> p3, Annexure B: *"Resignation of Mr. Gaurav Sachdeva- Chief Retail Officer, a Senior Management
> Personnel of the Company **due to personal reasons and pursue other career opportunities outside the
> Organization**."*

The head of retail left seven months after listing, in a company whose entire equity story is store
rollout. No replacement is announced anywhere in the 119 filings. p2 is image-only (sect. 7).

**(5) Company Secretary & Compliance Officer — resigned 30-Jun-2026.**
`20260630_DisclosureunderRegulation30` (and its duplicate `_2`). Filed under **two** exchange
categories, "Resignation" and "Cessation" — one event, two postings.

> p1: *"we wish to inform that Mr. Paras Shah, has tendered his resignation from the position of Company
> Secretary and Compliance Officer (Key Managerial Personnel) of the Company **due to personal reasons**.
> He tendered his resignation and will be relieved from his responsibilities with effect from close of
> business hours on June 30, 2026. There are no material reasons for his resignation other than those
> mentioned above."*
>
> p2, Annexure A, "Reason for Change": *"**Resignation due to personal reasons.**"*

His resignation letter is on p3 and is image-only (sect. 7).

**(6) Company Secretary appointed — 02-Sep-2026.** `20260902_Appointment_of_CS` p1–p2, repeated as
Annexure A of `20260902_Outcome_of_BM` p3–p4.

> p2, Annexure A, "Reason for Appointment": *"Mr. Mandar Godbole is appointed as Company Secretary and
> Compliance Officer of the Company with effect from September 02, 2026 **due to the resignation tendered
> by Mr. Paras Shah as the Company Secretary and Compliance Officer of the Company w.e.f. June 30,
> 2026**."*
>
> p2: *"He is not related to any Directors, promoters or KMP of the Company"*; *"He is not holding any
> shares in the Company."*

**The company had no Company Secretary and Compliance Officer between 30-Jun-2026 and 02-Sep-2026** — a
64-day vacancy in a Section 203 KMP post. That is a fact of dates on the face of two filings, and W6_gov
should size it against Companies Act s.203(4) (vacancy to be filled within six months) and against what
was filed in the interval.

**(7) Director declines re-appointment — 14-Aug-2026.**
`20260814_BlueStone_Outcome_of_Board_Meeting_14August2026`, p1 and p3.

> p1: *"Retirement of Mr. Sameer Nath: Mr. Sameer Nath, Non-Executive Director (DIN: 07551506) of the
> Company retires by rotation at the ensuing 15th AGM of the Company. **He has expressed his desire not
> to seek re-appointment.** Respecting his decision, the Board noted and accepted his request and
> recommended that his reappointment be not sought at the ensuing AGM."*
>
> p3, Annexure I, "Reason for change": *"Mr. Sameer Nath, Non-Executive Director (DIN: 07551506) of the
> Company retires by rotation and **has expressed his desire not to seek reappointment** at the ensuing
> Annual General Meeting (AGM) of the Company."*

No reason beyond "desire" is given anywhere. Same letter, p1 item 2, discloses something else that
matters:

> *"Approval of the **Revised Director's Report** for the financial year ended March 31, 2026
> incorporating the necessary modifications consequent to: (i) recording the retirement by rotation of
> Mr. Sameer Nath … and (ii) the recommendation for appointment of Mr. Amit Jain (DIN: 01613364) as a
> Non-Executive, Non-Independent Director (Professional) of the Company, liable to retire by rotation,
> subject to the approval of the Members at the ensuing Annual General Meeting."*

**The FY2026 Directors' Report was revised after the annual report was already prepared.** The incoming
director's profile is on p4–p5 (Amit Jain, CEO and co-founder of CarDekho Group; shareholding in the
company Nil; board meetings attended last FY Nil).

**(8) Credit rating — 07-Aug-2026.** `20260807_BlueStone_Intimation_of_Credit_Rating`, p1.

> *"we wish to inform that India Ratings and Research Private Limited (a Fitch Group company) vide their
> report dated 07 August, 2026 has assigned the Company (issuer) credit rating as mentioned in the below
> table: | India Ratings and Research Private Limited | **Issuer Rating** | Size of Issue: **Not
> Applicable** | Assigned Rating: **IND A-/Stable** |"*

A first-time issuer rating, thirteen months after listing. No rationale document is in the corpus
(GAP-004 stands) and the intimation gives no rated instrument, no outlook commentary and no covenant
detail.

### 5c. The EtherealHouse investment — a related-party transaction in three filings

**(9a) Approval, 22-Jan-2026.** `20260122_DisclosureFinal`, p1–p3.

> p1: *"the audit committee … and the board of directors … have inter alia approved investment in the
> Series A2 compulsorily convertible preference shares … of Ethereal House Private Limited ("Ethereal"),
> **a subsidiary of the Company**, up to an amount of INR 25,19,98,248 … by way of subscription to 92,172
> … Series A2 CCPS of INR 10 … each, at the price per Series A2 CCPS of INR 2,734 … The Proposed
> Investment is pursuant to the capital infusion provisions under the **Shareholders' Agreement dated
> January 6, 2025**."*
>
> p2, Annexure A item 2 — the related-party answer, verbatim: *"**Yes, the Proposed Investment is a
> related party transaction under the provisions of Listing Regulations.** Ethereal is a subsidiary of
> the Company, where the Company currently holds 74% shareholding (on a fully diluted basis) in Ethereal.
> The Proposed Investment is being carried out on an arm's length basis. The promoter, promoter
> group/group companies do not have any interest in Ethereal **except that the promoter of the Company
> (i.e., Gaurav Singh Kushwaha) is a non-executive director (nominated by the Company) in Ethereal**."*
>
> p2, item 4 — the stated purpose: *"The Proposed Investment is pursuant to the capital infusion/ funding
> framework provided under the SHA. The Proposed Investment will be utilized by Ethereal for **working
> capital purposes and for expanding its business**."*
>
> p2, item 1: Ethereal was *"Being incorporated on August 21, 2024"*; *"Turnover: INR Nil; Net Worth: INR
> 16,13,36,076"* for FY ended 31-Mar-2025. p3 item 10 repeats: FY24-25 turnover **NIL**, FY23-24 and
> FY22-23 **N.A.** p3 item 9 records the 74% fully-diluted ceiling under the SHA.

**(9b) SSA executed, 03-Feb-2026.** `20260203_StockExchangeDisclosureFinal`, p1 — the company
*"has executed a share subscription agreement ("SSA") on February 03, 2026 with Ethereal and its
shareholders"*.

**(9c) Subscription completed, 06-Feb-2026.** `20260206_StockExchangedisclosure`, p1 — *"the Company has
subscribed to 92,172 … Series A2 CCPS of Ethereal at the price per Series A2 CCPS of INR 2,734 …
aggregating to INR 25,19,98,248."*

Note for W3_RPT: the company put ~Rs 25.2 crore into a **nil-revenue** subsidiary in the same quarter in
which the Monitoring Agency was tracking whether IPO proceeds had reached their stated objects, and the
promoter sits on that subsidiary's board.

### 5d. Every ESOP action, in order

All exercises are at an exercise price of **Re. 1 per share with NIL premium** — the allotment
intimations state this in field 13/14 of the Regulation 10(c) annexure in every case.

| Date | File stem | Action | Shares | Paid-up capital after |
|---|---|---|---|---|
| 03-Jan-2026 | `20260103_ESOP_Allotment` | allotment (board by circulation) | 1,23,069 | 15,14,43,441 |
| 22-Jan-2026 | `20260122_DisclosureunderRegulation30ESOP` | allotment (board meeting) | 2,95,857 | 15,17,39,298 |
| 16-Feb-2026 | `20260216_StockExchangedisclosureallotmentofshares` | allotment (circulation) | 65,494 | 15,18,04,792 |
| 18-Mar-2026 | `20260318_ESOPExercsieAllotment` | allotment (circulation) | 4,26,573 | 15,22,31,365 |
| **16-Apr-2026** | `20260416_IntimationofGrantFinal` | **GRANT, not allotment** — NRC approves **2,09,319 options**, exercise price Rs.1; vesting schedule pp2–5 | — | — |
| **23-Apr-2026** | `20260423_DisclosureunderRegulation30_3`, p2 and p4 | allotment **buried inside the audited-results board outcome, item 3** — no standalone intimation | 1,29,573 | 15,23,60,938 |
| 09-Jun-2026 | `20260609_DisclosureunderRegulation30` | allotment (circulation) | 40,843 | 15,24,01,781 |
| 20-Jul-2026 | `20260720_Allotment_of_Equity_Shares` | allotment (board meeting) | 4,853 | 15,24,06,634 |
| 05-Aug-2026 | `20260805_Allotment_of_Equity_Shares` | allotment (circular resolution) | 3,42,766 | 15,27,49,400 |
| 02-Sep-2026 | `20260902_Allotment_of_Equity_Shares` (= `20260902_Outcome_of_BM` Annexure B, p5–p6) | allotment (board meeting) | 29,305 | 15,27,78,705 |

Two mapping points: the register's "6 ESOP allotments" is **nine allotments plus one grant**, and the
23-Apr-2026 allotment has **no standalone filing** — it is item 3 of a 23-page results letter, which is
why a filename-based sweep misses it. The distinctive-number ranges are contiguous across all nine
(151320373 → 152778705), so nothing is missing from the sequence.

Related: the **ESOP 2014 scheme itself was put to shareholders for ratification** by the December-2025
postal ballot (sect. 6c), and **7.65% of votes cast were against it**.

### 5e. Shareholder votes — three, and the dissent is not zero

| Meeting | Notice | Result file | Resolutions | Dissent |
|---|---|---|---|---|
| 14th AGM, 29-Sep-2025 | `20250905_StockExchangesRegulation34` (= AR FY2025) | `20250930_VotingResultuploading` — **image-only**, tables on p4–p8 | 5 (accounts ×2, director re-appointment, secretarial auditor, authorised-capital reclassification) | Verified on the rasterised p5: Resolution 2 passed 100.0000% in favour, 4 votes against out of 10,23,80,203 polled |
| Postal ballot, notice 23-Dec-2025 | `20251226_NoticeofPostalBallotupload` | `20260127_Stockexchangeupload` — **image-only**, result on p9 | 1 Special Resolution: **ratification of the ESOP 2014** | **7.6528% against** — 32 shareholders, 78,88,838 votes, out of 10,30,83,687 polled by 244 shareholders |
| Postal ballot, notice 23-Apr-2026 | `20260430_NoticeofPostalBallotupload` | `20260601_VotingResults` — machine-readable p2–p9 | 2 Special Resolutions, **promoter interested in both**: (1) **one-time special bonus to Mr Gaurav Singh Kushwaha, MD and Chairman** — p6; (2) **increase in his remuneration** — p8 | Resolution 1: public institutions **3.4924% against** (promoter 100% in favour). Resolution 2: 0% against |

Scrutinizers differ by meeting: **Parth Joshi & Co** for the AGM (report signed 29-Sep-2025, UDIN
A047604G001386568); **Mitesh J. Shah & Associates** for both postal ballots.

W6_gov should note the shape rather than the level: the only two resolutions that drew meaningful
institutional opposition in thirteen months were **the ESOP scheme** and **a special bonus to the
promoter-CEO** — and both are pay.

---

## 6. Results filings — which file carries which quarter

| Period | Basis | Filed | File stem (canonical) | Consolidated | Standalone | Balance sheet | Cash flow |
|---|---|---|---|---|---|---|---|
| **Q1FY26** (qtr to 30-Jun-2025) | Unaudited, limited review | 04-Sep-2025 | `20250904_Financial_result_June_2025` | review p3–p4, results **p5**, notes p6–p7 | review p8–p9, results **p10**, notes p11–p12 | — | — |
| **Q2FY26 + H1FY26** (to 30-Sep-2025) | Unaudited, limited review | 04-Nov-2025 | `20251104_Results_september_25` | review p2–p3, results **p4**, notes p7–p8 | review p9–p10, results **p11**, notes p14–p15 | **consol p5 · standalone p12** | **consol p6 · standalone p13** |
| **Q3FY26 + 9MFY26** (to 31-Dec-2025) | Unaudited, limited review | 22-Jan-2026 | `20260122_Coveringletter_4` | review p2–p3, results **p4**, notes p5–p6 | review p7–p8, results **p9**, notes p10–p11 | — | — |
| **Q4FY26 + FY2026** (to 31-Mar-2026) | **AUDITED** | **23-Apr-2026** | **`20260423_DisclosureunderRegulation30_3`** | **Independent Auditor's Report p5–p8, results p9, balance sheet p10, cash flow p11, notes p12–p13** | **Independent Auditor's Report p14–p17, results p18, balance sheet p19, cash flow p20, notes p21–p22** | **consol p10 · standalone p19** | **consol p11 · standalone p20** |
| **Q1FY27** (qtr to 30-Jun-2026) | Unaudited, limited review | 20-Jul-2026 | `20260720_Outcome_of_BM_Financial` | review p12–p13, results **p14**, notes p15–p16 | review p17, results **p18**, notes **p19** | — | — |

**The audited FY2026 full-year results are in `20260423_DisclosureunderRegulation30_3`** (and its three
byte-identical twins `_4`, `_5`, `_6`). That 23-page letter also carries, in one envelope: the covering
letter (p1–p2), the internal-auditor Annexure A (p3), the 1,29,573-share ESOP Regulation 10(c) annexure
(p4), and both auditor's reports and both sets of audited statements (p5–p22), with a closing page p23.
The statements are stated **"All amounts are in INR million unless otherwise stated"** on p9 and p18.

> **Read this before extracting a single figure from that file.** Pages 5–22 are an **OCR of a scanned,
> signed printout**, not native text. The text layer shows characteristic OCR corruption —
> `8lueStone`, `Villaa:e`, `financia l liabilities`, `Redemption ol mutual funds`, `7.479.00` for
> `7,479.00`, `1486.41` and `(486.41'` for `(486.41)` — and, worse, **the column headers float away from
> their columns**: on p9 the header sequence extracts as "31-03-2026 / 31-03-2025 / 31-12-2025" while
> the value triples run in a different order, and on p18 the quarter block and the year block collide.
> **Nothing may be transcribed from `20260423_DisclosureunderRegulation30_3.txt`.** Read the PDF, or
> better, read the audited statements from `data/bronze/BLUESTONE-AR-FY2026.pdf`, which is the source of
> record under `CLAUDE.md`'s source rule and is native text. Use the 23-Apr filing only to establish
> what was published on 23-Apr-2026 and to date the auditor's report.

Interim quarters are also scans, but of much better quality (the Q1FY26/Q2FY26/Q3FY26/Q1FY27 statement
pages carry 450–970 extractable digits each and are internally consistent); they still want a PDF check
on any number that carries a conclusion.

**Auditor's signature block changes name mid-year, same firm:** "MSKA & Associates" on the Q1FY26 and
Q2FY26 review reports; "MSKA & Associates LLP (Formerly known as MSKA & Associates)" from the Q3FY26
review report (22-Jan-2026) onward — consistent with the 17-Jan-2026 constitution-change intimation.

Two supporting documents per quarter accompany each results filing and are mapped in sect. 1: a press
release and a management commentary. The **management commentary is the densest quarterly disclosure in
the corpus** — Standalone KPI annexure, Consolidated KPI annexure (Q2FY26–Q4FY26 only), a DataBook of
line-item detail, and a glossary. Locators:

| Quarter | File stem | Standalone KPIs | Consolidated KPIs | DataBook |
|---|---|---|---|---|
| Q1FY26 | `20250904_Final` | p8 | **absent** | p9 |
| Q2FY26 | `20251104_Management_commentaryUploading` | p7 | p8 | p9 |
| Q3FY26 | `20260122_Coveringletter` | p8 | p9 | p10 |
| Q4FY26 | `20260423_DisclosureunderRegulation30` | p9 | p10 | p11 |
| Q1FY27 | `20260720_BlueStone_Management_Commentary_Q1FY27` | p7 | **absent again** | p8 |

---

## 7. Filings that could not be read from the text layer

Twelve documents contain pages with no extractable text. Eight of them are consequential. Every page
listed below has been **rasterised to `data/scanned_pages/<stem>_p<n>.png`** using the embedded JPEG at
its native resolution, so no later wave needs to repeat the step. Extraction recipe, for anything else:
`pypdf.PdfReader(pdf).pages[n-1].images[0].image.save(out)` — there is no `tesseract`, `ocrmypdf` or
`pdftoppm` on this machine, so these must be read visually, not OCR'd.

| File | Pages with no text | What is on them | Status |
|---|---|---|---|
| **`24-Jun-2026_team_sandeshc_23062026122639_50`** | **p1, p2** (whole document) | Promoter SAST Reg 31(4) annual encumbrance declaration + promoter-group list | **READ — see below** |
| `20250930_VotingResultuploading` | p2–p9 (p10–p18 are genuinely blank pages, no content stream) | Scrutinizer's Report, 8 pp, incl. the five AGM resolution-wise voting tables on p4–p8 | **Rasterised; p5 and p9 read and verified** |
| `20260127_Stockexchangeupload` (+`_2`) | p8–p10 (p2–p7 blank) | Scrutinizer's Report on the Dec-2025 postal ballot | **Rasterised; p9 read — ESOP ratification, 7.6528% against** |
| `20260601_VotingResults` | p10–p12 | Scrutinizer's Report on the Apr-2026 postal ballot (the tabulated results are already machine-readable on p2–p9) | Rasterised; not yet read — low priority, results are in the text layer |
| `20260114_StockExchnagedisclosure` | p5 | Nexdigm's own internal-auditor resignation letter | Rasterised; unread. **Read it — the company's paraphrase ("pre-occupied other commitments") is on p1/p3; the letter is the primary source** |
| `20260630_DisclosureunderRegulation30` (+`_2`) | p3 | Paras Shah's own CS resignation letter | Rasterised; unread. Same reasoning |
| `20260310_DisclosureunderRegulation30` | p2 | Gaurav Sachdeva's own CRO resignation letter | Rasterised; a partial OCR already exists in the `.txt` (quoted in sect. 5b) — read the image to confirm |
| `20251030_Bluestone_Q2Final` | p2 | Q2FY26 call-invite card (decorative) | ignore |
| `20260604_DisclosureunderRegulation30` / `20260603_CoveringLetter` | ~50 of 144 pages carry little or no text | The Investor Day deck's charts are rendered as images | **Material.** Cohort economics (p123), network vintage (p124) and most of the FY30 bridge charts are pictures. W2_promise must read the deck as a PDF, not as `.txt` |
| the 5 quarterly IP decks | 5–6 section-divider pages each | dividers only | ignore |

### 7a. GAP-002 is closed, and the answer is not "no encumbrance"

`24-Jun-2026_team_sandeshc_23062026122639_50` p1, read from
`data/scanned_pages/24-Jun-2026_team_sandeshc_23062026122639_50_p1.png`. It is a personal letter on
Gaurav Singh Kushwaha's own letterhead, addressed to BSE, NSE **and the company's Audit Committee**,
**dated 08-April-2026** and filed to the exchange on **24-Jun-2026**. Verbatim:

> *"Pursuant to the provisions of the Regulation 31(4) of SEBI (Substantial Acquisition of Shares &
> Takeovers) Regulations, 2011, I hereby confirm and declare that, during the financial year 2025-26,
> the Promoter of Bluestone Jewellery and Lifestyle Limited, ("the Target Company"), **have pledged
> equity shares of the Target Company as on March 31, 2026 the total pledged quantity stands at
> 92,15,127 equity shares of the Target Company.** Please note that the Non-Disposal Undertaking (NDU),
> **where Multiple NDU have been executed with different lenders and varying levels of shareholding.**
> Further, the Promoter have made encumbrance, directly or indirectly during the financial year
> 2025-2026."*
>
> *"Further, the Promoter Group along with Person acting in concert, have not created encumbrance or
> pledged any equity shares of the Target Company as on March 31, 2026 and the total pledged quantity
> stands at Nil equity shares of the Target Company."*

p2 is Annexure I, the list of promoter and promoter group as at 31-Mar-2026: **Gaurav Singh Kushwaha
(Promoter)**; Arpita Tomar, Shivraj Singh Kushwaha, Prabha Kushwaha, Prashant Singh Kushwaha, Nivaan
Singh Kushwaha, Kayna Singh Kushwaha, Arvind Pratap Singh Tomar, Mina Tomar, Anurag Tomar, Archana Tomar
(Promoter Group) — eleven names, matching the promoter list CARE prints in every Monitoring Agency
Report (spelling of two given names differs between the two sources).

**Consequences for later waves, stated as pointers not conclusions:**

- The register's caution was right: this must **not** be treated as "no encumbrance". The promoter's
  own declaration is that 92,15,127 shares stood encumbered at 31-Mar-2026, under **multiple
  Non-Disposal Undertakings with different lenders**. W6_gov and W4_capalloc must size that against the
  promoter's holding in `data/filings/SHP_31MAR2026_new.xml` and against the promoter-group total of
  16.25% recorded in the source register, and must find out who the lenders are and what the borrowing
  is for — the filing names neither.
- The declaration is **dated 08-Apr-2026 and reached the exchange on 24-Jun-2026**. Reg 31(4) requires
  the annual declaration within seven working days of the financial year end. The gap between the two
  dates is on the face of the document; W6_gov should establish whether an earlier filing exists that
  this corpus did not capture before drawing anything from it.
- It arrived as an **image with a 50-byte text layer, under a filename that carries neither the company
  name nor the subject** (`team_sandeshc_23062026122639_50.pdf`). It is the single most
  governance-relevant document in the 119 and it is the least findable. Note the pattern.

---

## 8. Handover — what the next waves should take from this map

**W2_promise.** Your evidence base is five transcripts (sect. 2), five management commentaries and five
quarterly decks (sect. 3a and sect. 6), and **one FY30 aspiration document** (sect. 3b). The asymmetry
is structural and must be stated with n: five quarters of delivery against a four-year promise made once,
in a deck whose charts are images. Read `20260604_DisclosureunderRegulation30` as a PDF. The analyst
list in sect. 2a is itself a finding about who is watching.

**W3 (revenue, cost, balance sheet, notes).** Use `data/bronze/BLUESTONE-AR-FY2026.pdf` for FY2026 and
`BLUESTONE-AR-FY2025.pdf` for FY2025. Use the quarterly results filings only for intra-year shape, and
only from the PDFs. `20251104_Results_september_25` is the **only** interim filing with a balance sheet
and a cash flow (p5/p6 consolidated, p12/p13 standalone). Do not transcribe from
`20260423_DisclosureunderRegulation30_3.txt` at all.

**W4_capalloc.** Everything you need is in sect. 4. The object-wise numbers are in the four MARs, never
in the SoDs. The Q4FY26 MAR is where the record turns, and the SoD filed the same day says the opposite.

**W6_gov.** Sect. 5 and sect. 7a. Thirteen months produced: one internal-auditor resignation with a same-
day replacement by a firm that then certifies the Monitoring Agency's report; one secretarial-auditor
change; the head of retail gone at month seven with no announced successor; a 64-day KMP vacancy in the
Company Secretary post; a non-executive director declining re-appointment with no reason given; a
Directors' Report revised after issue; ~Rs 25 crore into a nil-revenue related-party subsidiary; nine
ESOP allotments at Re.1; a promoter-pay resolution that drew institutional dissent; and 92,15,127
promoter shares under multiple lender NDUs disclosed in a two-page image. **`state/LOOP.md` says the
absence of history is a gap, not a clean record. The history that does exist is not empty either.**

**W7 / QC.** Two contradictions are already on the record and must survive to the final report under
doctrine §10: (a) the 23-Apr-2026 Statement of Deviation versus the 23-Apr-2026 Monitoring Agency Report;
(b) the Investor Day corrigendum's four disclosed changes versus the eight text-layer differences between
the two PDFs. Neither is resolved here. Neither may be silently resolved later.
