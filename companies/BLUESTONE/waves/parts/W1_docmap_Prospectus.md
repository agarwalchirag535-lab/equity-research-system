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
