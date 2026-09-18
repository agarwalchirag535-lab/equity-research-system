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
