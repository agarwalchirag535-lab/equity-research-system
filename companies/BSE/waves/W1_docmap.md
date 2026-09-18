# W1 — Document map: BSE Limited annual reports FY2017–FY2026

Wave 1 artifact (doctrine §7). **Locations only — no financial analysis, no figures asserted as facts
about the business.** Every location below was opened and read in the extracted text; none is carried
over from the auto-generated draft index, which is materially wrong (§6).

Source files: `companies/BSE/data/text/BSE-AR-FY{2017..2022,2024,2025,2026}.txt`
(page markers `===== PDF PAGE n =====`), PDFs in `companies/BSE/data/bronze/`.

**GAP-001 — FY2023 annual report is absent.** Not chased, per instruction. Consequence for later
waves: FY2023 is reachable only as the comparative column inside the FY2024 report, and that column
was itself restated in FY2025 (see §5.6). Any FY2023 figure is a comparative, never a primary.

---

## 0. How to cite from these documents

### 0.1 PDF-page → printed-page offset (derived per document from actual page furniture)

The draft index records `printed_map: null` for all nine years. I derived each offset from the running
head / folio printed on the page itself and validated it page-by-page across the whole document.
**All nine documents carry printed folios and all nine offsets are constant end-to-end.**

| Year | Offset (printed = PDF − offset) | How verified | Pages confirming |
|---|---|---|---|
| FY2017 | **+2** | folio in running head, e.g. PDF 89 → "Corporate Governance Report 87"; PDF 268 → "266" (AOC-1) | 273 / 284 |
| FY2018 | **+7** | spread-style head "BSE Limited Consolidated Financial Statements 133132" — PDF 139 = printed 132, PDF 140 = printed 133 | verified on the run PDF 131–142 and via contents |
| FY2019 | **+9** | PDF 112 → "103 Corporate Governance Report"; PDF 147 = printed 138 (consol BS) | 295 / 313 |
| FY2020 | **+7** | PDF 120 → "113"; PDF 159 = printed 152 (consol BS) | 307 / 317 |
| FY2021 | **+5** | PDF 138 → "133"; PDF 225 → "220" (standalone BS) | 286 / 293 |
| FY2022 | **+9** | PDF 149 → "140 Consolidated Financial Statements"; PDF 233 → "224" | 143 / 305 (even pages carry no extractable folio; offset constant on every page that does) |
| FY2024 | **+6** | PDF 23 → "17"; PDF 153 → "147"; PDF 251 → "245" | 308 / 316 |
| FY2025 | **+11** | PDF 24 → "13"; PDF 155 → "144"; PDF 228 → "217" | 257 / 283 |
| FY2026 | **+11** | PDF 163 → "152"; PDF 300 → "289" | 304 / 317 |

Pages that do not confirm are front-cover / back-cover matter that carries no folio at all
(FY2026 PDF 1–11, FY2025 PDF 1–11 incl. the NSE covering letter at PDF 1, FY2024 PDF 1–6).

Cite form (TEMPLATES.md): `[AR FY26, Note 22, PDF p211/pr200]`.

### 0.2 Text-extraction defect you must know about — page bleed

The extracted `.txt` files duplicate adjacent-page content on some pages. A page block can begin with
the **previous** page's body (forward bleed) or end with the **next** page's body (backward bleed).
Measured incidence:

| Year | Forward-bleed pages | Backward-bleed pages | Where concentrated |
|---|---|---|---|
| FY2017 | 0 | 0 | — |
| FY2018 | 6 | 4 | PDF 133–166, 213–216, 238, 262 |
| FY2019 | 0 | 0 | — |
| FY2020 | 0 | 0 | — |
| FY2021 | 0 | 0 | — |
| FY2022 | 0 | 0 | — |
| FY2024 | 16 | **50** | consolidated notes PDF 156–184, standalone PDF 266–302 |
| FY2025 | **56** | 20 | consolidated notes PDF 173–198 & 209–213, standalone PDF 240–266 |
| FY2026 | 28 | 2 | consolidated notes PDF 171–180, 185–202, 214–231 |

**Rule I used and you should use.** Where a heading appears on two consecutive pages inside a
forward-bleed run, the earlier page is the true page; inside a backward-bleed run, the later one is.
Where a heading appears once, there is no ambiguity. I checked every deep-year note heading for
adjacent duplication: FY2024 had none, FY2026 had none in the financial statements, FY2025 had eight
(all inside forward-bleed runs, resolved to the earlier page). **Every page number in this map has
been resolved against that rule and cross-checked against the printed folio.** If a later agent greps
these text files directly, it must apply the same rule or it will cite off-by-one.

### 0.3 Statutory auditor and engagement partner (needed to read the audit reports correctly)

| Year | Firm | FRN | Engagement partner |
|---|---|---|---|
| FY2017 | **Deloitte Haskins & Sells LLP** | 117366W/W-100018 | G. K. Subramaniam |
| FY2018–FY2023 | **S.R. Batliboi & Co. LLP** | 301003E/E300005 | (per year) |
| FY2024 | S.R. Batliboi & Co. LLP | 301003E/E300005 | **Jayesh Gandhi**, M.No. 037924 |
| FY2025 | S.R. Batliboi & Co. LLP | 301003E/E300005 | **Pikashoo Mutha**, M.No. 131658 |
| FY2026 | S.R. Batliboi & Co. LLP | 301003E/E300005 | **Pikashoo Mutha**, M.No. 131658 |

Auditor change at FY2018 (Deloitte → S.R. Batliboi); partner rotation at FY2025 (Gandhi → Mutha).

---

## 1. FY2026 (Annual Report 2025-26) — DEEP MAP

PDF pages 317 · printed folios 1–302 · **offset +11** · contents page at PDF p4.

### 1.1 Document skeleton

| Section | PDF pages | Printed pages | Verified at |
|---|---|---|---|
| Board of directors / contents | 4 | — | p4 |
| AGM Notice | 12–22 | 1–11 | p12 ("Twenty-First Annual General Meeting") |
| — Annexure: director seeking re-appointment | 22 | 11 | p22 |
| **Board's Report** | **23–50** | **12–39** | p23 ("presents the 21st Annual Report") |
| — Annexure A: s.197(12) + Rule 5(1) & 5(2) managerial remuneration | 37–41 | 26–30 | p37 |
| — Annexure B: Form MR-3 Secretarial Audit (BSE Limited) | 42–44 | 31–33 | p42 |
| — Annexure C: **Annual Report on CSR activities** | 45–46 | 34–35 | p45 |
| — Annexure D: Form MR-3 Secretarial Audit (material subsidiary) | 47–49 | 36–38 | p47 |
| — Annexure E: Dividend Distribution Policy | 50 | 39 | p50 |
| — AOC-2 (RPT contracts): stated **not applicable** for FY2025-26 | 31 | 20 | p31; repeated in CG report p94 |
| **Management Discussion & Analysis** | **51–77** | **40–66** | p51 |
| **Corporate Governance Report** | **78–101** | **67–90** | p78 |
| — CG Annexures A / B / C / D | 98 / 99 / 100 / 101 | 87 / 88 / 89 / 90 | p98–101 |
| **BRSR** (Business Responsibility & Sustainability Report) | **102–154** | **91–143** | p102 |
| — Independent practitioner's reasonable-assurance report on BRSR Core | 103–105 | 92–94 | p103 |
| — Appendix 1: list of BRSR Core indicators | 106 | 95 | p106 |
| **CONSOLIDATED financial statements** | | | |
| Independent Auditor's Report (consolidated) | 155–162 | 144–151 | p155 |
| Consolidated Balance Sheet | 163 | 152 | p163 |
| Consolidated Statement of Profit and Loss | 164 | 153 | p164 |
| Consolidated Statement of Cash Flows | 165–166 | 154–155 | p165 |
| Consolidated Statement of Changes in Equity | 167–168 | 156–157 | p167 |
| Notes to consolidated financial statements | 169–240 | 158–229 | p169 |
| **STANDALONE financial statements** | | | |
| Independent Auditor's Report (standalone) | 241–248 | 230–237 | p241 |
| Standalone Balance Sheet | 249 | 238 | p249 |
| Standalone Statement of Profit and Loss | 250 | 239 | p250 |
| Standalone Statement of Cash Flows | 251–252 | 240–241 | p251 |
| Standalone Statement of Changes in Equity | 253 | 242 | p253 |
| Notes to standalone financial statements | 254–311 | 243–300 | p254 |
| **Form AOC-1** (subsidiaries / associates / JVs) | **312–313** | **301–302** | p312 |

### 1.2 Independent Auditor's Report — FY2026

| Element | Consolidated (PDF 155–162) | Standalone (PDF 241–248) |
|---|---|---|
| Opinion | **Unmodified / clean**, p155 | **Unmodified / clean**, p241 |
| Basis for Opinion | p155 | p241 |
| **Key Audit Matters** | **One KAM:** *Information Technology (IT) systems and controls* — p155 | **Two KAMs:** (1) *Valuation of investments in subsidiary and associate and its impairment* (refers to standalone Note 32) — p241; (2) *Information Technology (IT) systems and controls* — p242 |
| Emphasis of Matter | **NONE** | **NONE** |
| Qualification / adverse / disclaimer | **NONE** | **NONE** |
| Material uncertainty re going concern | **NONE** | **NONE** |
| Other Matter | p157 — six subsidiaries not audited by the principal auditor; opinion relies on other auditors' reports | — |
| Annexure 1 (CARO / s.143(11)) | p160 — **table of CARO clauses qualified or adverse across group companies** (see §1.5) | p244–247 — full CARO 2020 report on the standalone |
| Annexure 2 (IFC u/s 143(3)(i)) | p161–162, opinion unmodified | p248, opinion unmodified |
| Signature block | S.R. Batliboi & Co. LLP, per Pikashoo Mutha, M.No. 131658, UDIN 26131658SEPYUU5112, Mumbai, **May 7, 2026** | same firm/partner, dated May 7, 2026 |

### 1.3 Material accounting policies — FY2026 (sub-note index)

Consolidated **Note 2**, PDF 169–180 (printed 158–169). Standalone **Note 2**, PDF 254–262 (printed 243–251).

| Policy | Consolidated | Standalone |
|---|---|---|
| Basis of preparation and presentation | 2.1, p169 | 2.1, p254 |
| Statement of compliance / basis of measurement / functional currency / estimates | 2.1.1–2.1.5, p169 | 2.1.1–2.1.4, p254 |
| Dividend distribution | 2.1.6, p170 | 2.1.5, p255 |
| Changes in ownership interests in existing subsidiaries | 2.1.7, p170 | — |
| Basis of consolidation | 2.1.3, p169 | n/a |
| Accounting for investments in subsidiaries (not consolidated) and associates | 2.2, p170 | — |
| **Summary of material accounting policies** | **2.3, p172** | **2.2, p255** |
| Financial instruments | 2.3.1, p172 | 2.2.1, p255 |
| **Earmarked funds** | 2.3.2, p173 | 2.2.2, p256 |
| Expected credit loss | 2.3.3, p173 | 2.2.3, p256 |
| Investment income and interest expense | 2.3.4, p174 | 2.2.4, p257 |
| Property, plant and equipment | 2.3.5, p174 | 2.2.5, p257 |
| Investment properties | 2.3.6, p175 | 2.2.6, p257 |
| Intangible assets | 2.3.7, p175 | 2.2.7, p258 |
| Employee benefits | 2.3.8, p176 | 2.2.8, p258 |
| Provisions, contingent liabilities and contingent assets | 2.3.9, p176 | 2.2.9, p259 |
| **Revenue** (Ind AS 115 policy; per-stream recognition at p177) | **2.3.10, p176–177** | **2.2.10, p259** |
| Leases | 2.3.11, p177 | 2.2.11, p260 |
| **Core Settlement Guarantee Fund (Core SGF)** | **2.3.12, p178** | **2.2.12, p260** |
| Taxes | 2.3.13, p178 | 2.2.13, p261 |
| Current / non-current classification | 2.3.14, p179 | 2.2.14, p261 |
| Cash and cash equivalents | 2.3.15, p179 | 2.2.15, p262 |
| Government grants | 2.3.16, p180 | — |
| Business combinations | 2.3.17, p180 | — |

### 1.4 Note-number index — FY2026

| Item | Consolidated note (PDF page) | Standalone note (PDF page) |
|---|---|---|
| Company / group overview | 1 (p169) | 1 (p254) |
| Material accounting policies | 2 (p169–180) | 2 (p254–262) |
| Property, plant and equipment | 3 (p181) | 3 (p263) |
| — CWIP ageing schedule | **absent — see §6** | 3.1 (p264) |
| Investment properties | 4 (p182) | 4 (p264) |
| Goodwill | 5 (p183) | — |
| Other intangible assets | 6 (p184) | 5 (p266) |
| Intangible assets under development — ageing & completion schedule | **absent — see §6** | 6 (p266–267) |
| Investments in subsidiaries | 7 (p185–187) | 7 (p267) |
| — Assets/liabilities held for sale | 7.1 (p186), 8.1 (p190) | — |
| Investments in associates | 8 (p187) | 8 (p268) |
| **Other investments** (MFs, bonds, ETFs, debentures) | **9 (p190–198)** | **9 (p269–275)** |
| **Trade receivables** | **10 (p199)** | **10 (p276)** |
| — impairment-allowance movement / ageing schedule | 10.4, 10.5 (p199) | 10.1 (p276) |
| Other financial assets | 11 (p200) | 11 (p277) |
| **Cash and cash equivalents & other bank balances** | **12 (p201)** | **12 (p278)** |
| Other assets | 13 (p202) | 13 (p278) |
| Equity share capital | 14 (p203) | 14 (p279) |
| Other equity (reserve-by-reserve, 15.1–15.8) | 15 (p204–205) | 15 (p280) |
| **Other financial liabilities — incl. all member/clearing deposits** | **16 (p206)** | **16 (p281)** |
| Provisions | 17 (p207) | 17 (p282) |
| Deferred tax assets and liabilities | 18 (p207) | 18 (p282) |
| Other liabilities (incl. Investors' Services Fund, IPF contribution payable) | 19 (p208) | 19 (p283) |
| **Trade payables** (+ ageing schedule 20.1) | **20 (p209–210)** | **20 (p284)** |
| Income tax assets and liabilities | 21 (p210) | 21 (p285) |
| **Revenue from operations — single note, with service-line disaggregation** | **22 (p211)** | **22 (p285)** |
| Investment income | 23 (p211) | 23 (p286) |
| Other income | 24 (p212) | 24 (p286) |
| **Employee benefits expense** | **25 (p212)** | **25 (p286)** |
| Technology expenses | 26 (p212) | 26 (p287) |
| **Regulatory contribution** | **27 (p212)** | **27 (p287)** |
| **Other expenses** (incl. *Payment to auditors*) | **28 (p213)** | **28 (p287)** |
| — CSR expenditure | 28.1 (p214) | 28.1 (p288) |
| Tax expense | 29 (p214) | 29 (p289) |
| **Earnings per share** | **30 (p215)** | **30 (p290)** |
| Expenditure in foreign currency | 31 (p216) | 39 (p303) |
| Lease | 32 (p216) | 31 (p290) |
| **Financial instruments / fair-value hierarchy** | **33 (p216)** | **32 (p290)** |
| Financial risk management | 34 (p218) | 33 (p292) |
| Capital management | 35 (p222) | 34 (p295) |
| **Related party transactions (Ind AS 24)** | **36 (p223–227)** | **35 (p295–301)** |
| **Contingent liabilities** | **37 (p227)** | **36 (p302)** |
| **Capital commitments** | **38 (p227)** | **37 (p303)** |
| **Segment reporting** (39.2 geography) | **39 (p228)** | **38 (p303)** |
| Schedule III para 2 — entity-wise net assets / P&L share | 40 (p228–231) | — |
| **Core SGF — ICCL, by segment** | **41 (p231)** | — (policy 2.2.12 only) |
| **Core SGF — India ICC / IFSCA** | **42 (p232)** | — |
| Employee benefits — actuarial (43.3 compensated absences) | 43 (p232–236) | 40 (p303–306) |
| Non-controlling interest reconciliation | 44 (p236) | — |
| Relationship with struck-off companies | 45 (p237) | 43 (p307) |
| Long-term contracts incl. derivatives | 46 (p238) | 42 (p307) |
| Events after reporting date | 47 (p238) | 46 (p309) |
| Non-current assets held for sale | 48 (p238) | — |
| **Discontinued operation** | **49 (p238–239)** | — |
| Divestment of wholly-owned subsidiary (in-principle approval May 8, 2024) | — | 41 (p307) |
| Maintenance of books of account and servers | 50 (p239) | 47 (p310) |
| Audit trail | 51 (p239) | 48 (p310) |
| Title deeds not held in the Company's name | — | 44 (p308) |
| **Analytical ratios** | — | **45 (p309)** |
| Other statutory information | 52 (p240) | 49 (p310) |

**Statement-face lines with no note reference (FY2026 consolidated P&L, p164):** *Clearing and
settlement expense*, *Finance cost*, and *Contribution to core settlement guarantee fund* carry no
note number; *Depreciation and amortisation expense* points to "3 & 4 & 6" rather than a dedicated
expense note. There is no borrowings note in either block — the standalone Analytical Ratios note
(45, p309) states the Company has no borrowings, and CARO clause (ix)(a) (p246) says the same. Lease
liabilities sit inside Note 16.

**Where member deposits actually are (FY2026 consolidated Note 16, p206):** the note splits into
*Owned* (deposits received from trading members; other deposits received from members; other
deposits), *Earmarked* (1%-of-public-issue deposits from companies; defaulters' liabilities; withheld
liabilities; recovery expense fund), and *Clearing and settlement* (deposit from clearing banks;
deposit and margins from members; settlement obligation payable). Standalone equivalent Note 16, p281.

### 1.5 FY2026 CARO 3(xxi) group-level table (consolidated auditor's report, PDF p160)

Entities whose own CARO reports carry a qualification or adverse remark, and the clause:
BSE Limited (holding) 3(i)(c); BSE Limited (holding) 3(vii)(b); BSE Technologies Private Limited
(subsidiary) 3(vii)(b); India Clearing Corporation Limited (subsidiary) 3(vii)(b); India
International Exchange IFSC Limited (subsidiary) 3(xvii). Wave-2 governance should start here.

---

## 2. FY2025 (Annual Report 2024-25) — DEEP MAP

PDF pages 283 · printed folios 1–268 · **offset +11** · contents page at PDF p4.
PDF p1 is the NSE covering letter dated July 24, 2025 (not part of the report body).

### 2.1 Document skeleton

| Section | PDF pages | Printed pages | Verified at |
|---|---|---|---|
| Contents | 4 | — | p4 |
| AGM Notice | 12–23 | 1–12 | p12 ("Twentieth Annual General Meeting") |
| — Annexure: director re-appointment | 21 | 10 | p21 |
| **Board's Report** | **24–47** | **13–36** | p24 |
| — Annexure A: s.197(12) Rule 5(1) **and** Rule 5(2) | 36–38 | 25–27 | p36 |
| — Annexure B: Form MR-3 Secretarial Audit | 39–41 | 28–30 | p39 |
| — Annexure C: **Annual Report on CSR activities** | 42–43 | 31–32 | p42 |
| — Annexure D: Form MR-3 (material subsidiary) | 44–46 | 33–35 | p44 |
| — Annexure E: Dividend Distribution Policy | 47 | 36 | p47 |
| **Management Discussion & Analysis** | **48–73** | **37–62** | p48 |
| **Corporate Governance Report** | **74–93** | **63–82** | p74 |
| — CG Annexures A / B / C / D | 90 / 91 / 92 / 93 | 79 / 80 / 81 / 82 | p90–93 |
| **BRSR** | **94–148** | **83–137** | p94 |
| **CONSOLIDATED** | | | |
| Independent Auditor's Report (consolidated) | 149–154 | 138–143 | p149 |
| Consolidated Balance Sheet | 155 | 144 | p155 |
| Consolidated Statement of Profit and Loss | 156–157 | 145–146 | p156 (P&L face), p157 (OCI + EPS) |
| Consolidated Statement of Cash Flows | 158–159 | 147–148 | p158–159 |
| Consolidated Statement of Changes in Equity | 160–161 | 149–150 | p160–161 |
| Notes to consolidated financial statements | 162–219 | 151–208 | p162 |
| **STANDALONE** | | | |
| Independent Auditor's Report (standalone) | 220–227 | 209–216 | p220 |
| Standalone Balance Sheet | 228 | 217 | p228 |
| Standalone Statement of Profit and Loss | 229 | 218 | p229 |
| Standalone Statement of Cash Flows | 230 | 219 | p230 (Ind AS 7 indirect-method footnotes) |
| Standalone Statement of Changes in Equity | 231 | 220 | p231 |
| Notes to standalone financial statements | 232–277 | 221–266 | p232 |
| **Form AOC-1** | **278–279** | **267–268** | p278 |

*Caution:* the FY2025 contents page and the actual pagination agree, but the text extract's
forward-bleed (§0.2) makes PDF p156 look like a balance-sheet page. It is the **P&L**; the
balance-sheet text at its head is bled in from p155.

### 2.2 Independent Auditor's Report — FY2025

| Element | Consolidated (PDF 149–154) | Standalone (PDF 220–227) |
|---|---|---|
| Opinion | Unmodified / clean, p149 | Unmodified / clean, p220 |
| **Key Audit Matters** | **One KAM:** *Valuation of investments and its impairment* (refers to consolidated Note 34) — p149 | **One KAM:** *Valuation of investments and its impairment* (refers to standalone Note 33) — p220 |
| Emphasis of Matter | **NONE** | **NONE** |
| Qualification / adverse / disclaimer | **NONE** | **NONE** |
| Other Matter | p151 (reliance on other auditors) and p154 (IFC annexure) | p225–226 |
| Annexure 1 (CARO) | p153 — 3(xxi) table, six entity-rows (BSE Limited ×2, BSE Technologies Private Limited, India International Clearing Corporation (IFSC) Limited, Indian Clearing Corporation Limited ×2) | p224–226 |
| Annexure 2 (IFC) | p154 | p227 |
| Signature | S.R. Batliboi & Co. LLP, per Pikashoo Mutha, UDIN 25131658BMJARM3824, **May 06, 2025** | same |

**The IT-systems-and-controls KAM is absent from FY2025 in both blocks.** It was present in FY2024
and returns in FY2026. Flagged in §5.2 — this is the single most notable audit-report movement in the
deep window.

### 2.3 Note-number index — FY2025

Material accounting policies: consolidated **Note 2**, PDF 162–171 (2.1 basis p162; 2.3 summary p165;
2.3.2 earmarked funds p165; 2.3.3 ECL p166; 2.3.5 PPE p166; **2.3.10 Revenue p168**; 2.3.11 Leases
p169; **2.3.12 Core SGF p169**). Standalone **Note 2**, PDF 232–238 (2.1 p232; 2.2 summary p233;
2.2.2 earmarked p233; 2.2.3 ECL p233; 2.2.5 PPE p234; **2.2.10 Revenue p236**; 2.2.11 Leases p236;
**2.2.12 Core SGF p237**).

| Item | Consolidated note (PDF page) | Standalone note (PDF page) |
|---|---|---|
| Overview | 1 (p162) | 1 (p232) |
| Material accounting policies | 2 (p162–171) | 2 (p232–238) |
| Property, plant and equipment | 3 (p172) | 3 (p239) |
| — CWIP ageing schedule | absent | 3.1 (p239) |
| Investment properties | 4 (p173) | 4 (p240) |
| Goodwill | 5 (p174) | — |
| Other intangible assets | 6 (p174) | 5 (p241) |
| Intangible assets under development — ageing & completion | absent | 6 (p241–242) |
| Investments in subsidiaries | 7 (p175); held-for-sale 7.1 | 7 (p242) |
| Investments in associates | 8 (p177) | 8 (p243) |
| Other investments | 9 (p179–185) | 9 (p244–247) |
| **Trade receivables** (+ ageing) | **10 (p186)** | **10 (p248)** |
| Other financial assets | 11 (p187) | 11 (p249) |
| Cash and cash equivalents & other bank balances | 12 (p188) | 12 (p250) |
| Other assets | 13 (p189) | 13 (p250) |
| Equity share capital | 14 (p189) | 14 (p250) |
| Other equity | 15 (p190) | 15 (p251) |
| **Other financial liabilities — member/clearing deposits** | **16 (p191)** | **16 (p252)** |
| Provisions | 17 (p191) | 17 (p252) |
| Deferred tax | 18 (p192) | 18 (p253) |
| Other liabilities (Investors' Services Fund; IPF payable) | 19 (p193–194) | 19 (p253) |
| Trade payables (+ ageing 20.1) | 20 (p193–194) | 20 (p254) |
| Income tax assets and liabilities | 21 (p194) | 21 (p254) |
| **Income from securities services** | **22 (p194)** | **22 (p254)** |
| **Income from services to corporates** | **23 (p195)** | **23 (p255)** |
| Investment income | 24 (p195) | 24 (p255) |
| Other income | 25 (p195) | 25 (p255) |
| Employee benefits expense | 26 (p195) | 26 (p255) |
| **Technology expenses** | **27 (p196)** | **27 (p255)** |
| **Regulatory contribution** | **28 (p196)** | **28 (p256)** |
| Administration and other expenses | 29 (p196) | 29 (p256) |
| Tax expense | 30 (p197) | 30 (p257) |
| Earnings per share | 31 (p198) | 31 (p258) |
| Expenditure in foreign currency | 32 (p198) | 40 (p271) |
| Lease | 33 (p198) | 32 (p258) |
| **Financial instruments** | **34 (p199)** | **33 (p258)** |
| Financial risk management | 35 (p200) | 34 (p259) |
| Capital management | 36 (p204) | 35 (p262) |
| **Related party transactions** | **37 (p204–209)** | **36 (p262–270)** |
| Contingent liabilities | 38 (p209) | 37 (p270) |
| Capital commitments | 39 (p210) | 38 (p270) |
| **Segment reporting** | **40 (p210)** | **39 (p270)** |
| Schedule III para 2 entity-wise info | 41 (p210) | — |
| **Core SGF — ICCL** | **42 (p213)** | — |
| **Core SGF — India ICC / IFSCA** | **43 (p213–214)** | — |
| Employee benefits — actuarial | 44 (p214) | 41 (p271) |
| Non-controlling interest reconciliation | 45 (p217) | — |
| **SEBI regulatory fees** | **46 (p217)** | **45 (p275)** |
| Relationship with struck-off companies | 47 (p217) | 43 (p274) |
| Long-term contracts incl. derivatives | 48 (p218) | 42 (p274) |
| Events after reporting date | 49 (p218) | 47 (p276) |
| Audit trail | 50 (p218) | 49 (p276) |
| **Buyback** | **51 (p218)** | **50 (p276)** |
| CDSL 5% stake divestment (prior year) | 52 (p218) | 51 (p276) |
| **Discontinued operation** | **53 (p218)** | — |
| Maintenance of books / servers | 54 (p219) | 48 (p276) |
| Title deeds not in Company's name | — | 44 (p275) |
| **Analytical ratios** | — | **46 (p275)** |
| Other statutory information | 55 (p219) | 52 (p276) |

---

## 3. FY2024 (Annual Report 2023-24) — DEEP MAP

PDF pages 316 · printed folios 1–307 · **offset +6** · contents page at PDF p3.

### 3.1 Document skeleton

| Section | PDF pages | Printed pages | Verified at |
|---|---|---|---|
| Contents | 3 | — | p3 |
| AGM Notice | 7–17 | 1–11 | p12 (folio "06") |
| **Board's Report** | **18–45** | **12–39** | p18 ("present the 19th Annual Report") |
| — Annexure A: s.197(12) Rule 5(1) (p32) and Rule 5(2) (p35) | 32–35 | 26–29 | p32, p35 |
| — Annexure B: Form MR-3 Secretarial Audit | 36–38 | 30–32 | p36 |
| — Annexure C: **Annual Report on CSR activities** | 39–41 | 33–35 | p39 |
| — Annexure D: Form MR-3 (material subsidiary) | 42–44 | 36–38 | p42 |
| — Annexure E: Dividend Distribution Policy | 45 | 39 | p45 |
| — Buyback of shares (Board's Report section) | 20 | 14 | p20 |
| **Management Discussion & Analysis** | **46–78** | **40–72** | p46 |
| **Corporate Governance Report** | **79–101** | **73–95** | p79 |
| — CG Annexures A / B / C / D | 98 / 99 / 100 / 101 | 92 / 93 / 94 / 95 | p98–101 |
| **BRSR** | **102–147** | **96–141** | p102 |
| **CONSOLIDATED** | | | |
| Independent Auditor's Report (consolidated) | 148–155 | 142–149 | p148 |
| Consolidated Balance Sheet | 156 | 150 | p156 |
| Consolidated Statement of Profit and Loss | 157 | 151 | p157 |
| Consolidated Statement of Cash Flows | 158–159 | 152–153 | p158 |
| Consolidated Statement of Changes in Equity | 160–161 | 154–155 | p160 |
| Notes to consolidated financial statements | 162–236 | 156–230 | p162 |
| **STANDALONE** | | | |
| Independent Auditor's Report (standalone) | 237–245 | 231–239 | p237 |
| Standalone Balance Sheet | 246 | 240 | p246 |
| Standalone Statement of Profit and Loss | 247 | 241 | p247 |
| Standalone Statement of Cash Flows | 248–249 | 242–243 | p248 |
| Standalone Statement of Changes in Equity | 250 | 244 | p250 |
| Notes to standalone financial statements | 251–311 | 245–305 | p251 |
| **Form AOC-1** | **312–313** | **306–307** | p312 |

### 3.2 Independent Auditor's Report — FY2024

| Element | Consolidated (PDF 148–155) | Standalone (PDF 237–245) |
|---|---|---|
| Opinion | Unmodified / clean, p148 | Unmodified / clean, p237 |
| **Key Audit Matters** | **Two:** (1) *Valuation of investments and its impairment* (consolidated Note 33) — p148; (2) *Information Technology (IT) systems and controls* — p149 | **Two:** (1) *Valuation of investments and its impairment* (standalone Note 32) — p237; (2) *Information Technology (IT) systems and controls* — p238 |
| Emphasis of Matter | **NONE** | **NONE** |
| Qualification / adverse / disclaimer | **NONE** | **NONE** |
| Other Matter | p151, p155 | p242 |
| Annexure 1 (CARO) | **p153 — 3(xxi) table with six rows:** BSE Limited 3(i)(c); BSE Limited 3(vii)(b); BSE Institute Limited 3(vii)(b); India International Clearing Corporation IFSC Limited 3(vii)(b); India International Exchange IFSC Limited 3(xvii); India International Clearing Corporation (IFSC) Limited 3(xvii) | p242–244 |
| Annexure 2 (IFC) | p154 | p245 |
| Signature | S.R. Batliboi & Co. LLP, per **Jayesh Gandhi**, M.No. 037924 | same |

### 3.3 Note-number index — FY2024

Material accounting policies: consolidated **Note 2**, PDF 162–175; the summary sits at **2.1.6**
(p166) with **roman-numeral** sub-clauses — *(xi) Revenue* at p172, *(xix) Core SGF* at p175,
*Earmarked Funds* at p168. Standalone **Note 2**, PDF 251–260; summary at **2.1.5** (p252),
*Earmarked Funds* p253, ECL p255, *(x) Revenue* p257. **This roman-numeral scheme was replaced by the
decimal 2.3.x / 2.2.x scheme in FY2025** — see §5.7.

| Item | Consolidated note (PDF page) | Standalone note (PDF page) |
|---|---|---|
| Company overview | 1 (p162) | 1 (p251) |
| Material accounting policies | 2 (p162–175) | 2 (p251–260) |
| Property, plant and equipment | 3 (p176) | 3 (p260) |
| — CWIP ageing schedule | absent | 3.1 (p261) |
| Investment properties | 4 (p177) | 4 (p261) |
| Goodwill | 5 (p178) | — |
| Other intangible assets | 6 (p179) | 5 (p263) |
| Intangible assets under development — ageing schedule | absent | 6 (p263) |
| Investments in subsidiaries | 7 (p180) | 7 (p264) |
| Investments in associates | 8 (p182) | 8 (p265) |
| Other investments | 9 (p185–194) | 9 (p266–273) |
| **Trade receivables** (+ ageing) | **10 (p195)** | **10 (p274)** |
| Other financial assets | 11 (p196) | 11 (p276) |
| Cash and cash equivalents & other bank balances | 12 (p198) | 12 (p276) |
| Other assets | 13 (p199) | 13 (p277) |
| Equity share capital | 14 (p199) | 14 (p278) |
| Other equity | 15 (p200) | 15 (p279) |
| **Other financial liabilities — member/clearing deposits** | **16 (p202)** | **16 (p280)** |
| Provisions | 17 (p203) | 17 (p281) |
| Deferred tax | 18 (p203) | 18 (p281) |
| Other liabilities | 19 (p204) | 19 (p282) |
| Trade payables | 20 (p205) | 20 (p283) |
| Income tax assets and liabilities | 21 (p206) | 21 (p284) |
| **Income from securities services** | **22 (p207)** | **22 (p284)** |
| **Income from services to corporates** | **23 (p207)** | **23 (p285)** |
| Investment income | 24 (p207) | 24 (p285) |
| Other income | 25 (p208) | 25 (p285) |
| Employee benefits expense | 26 (p208) | 26 (p286) |
| **Computer technology related expenses** | **27 (p208)** | **27 (p286)** |
| **Administration and other expenses** | **28 (p208)** | **28 (p286)** |
| Tax expense | 29 (p210) | 29 (p288) |
| Earnings per share | 30 (p211) | 30 (p289) |
| Expenditure in foreign currency | 31 (p211) | 39 (p303) |
| Lease | 32 (p211) | 31 (p289) |
| **Financial instruments** | **33 (p211)** | **32 (p289)** |
| Financial risk management | 34 (p213) | 33 (p291) |
| Capital management | 35 (p218) | 34 (p294) |
| **Related party transactions** | **36 (p219–225)** | **35 (p295–302)** |
| Contingent liabilities | 37 (p225) | 36 (p302) |
| Capital commitments | 38 (p225) | 37 (p302) |
| **Segment reporting** | **39 (p225)** | **38 (p302)** |
| Schedule III para 2 entity-wise info | 40 (p226) | — |
| **Core SGF — ICCL / NSE contribution** | **41 (p229)** | — |
| **Core SGF — IFSCA / India ICC** | **42 (p230)** | — |
| Employee benefits — actuarial | 43 (p230) | 40 (p303) |
| Non-controlling interest reconciliation | 44 (p233) | — |
| **Liquidity Enhancement Scheme (SEBI circular Apr 23, 2014)** | **45 (p233)** | **41 (p306)** |
| **SEBI regulatory fees** | **46 (p233)** | **45 (p308)** |
| Relationship with struck-off companies | 47 (p234) | 43 (p307) |
| Long-term contracts incl. derivatives | 48 (p235) | 42 (p306) |
| Events after reporting date | 49 (p235) | 47 (p309) |
| Audit trail | 50 (p235) | 49 (p310) |
| **Buyback** | **51 (p235)** | **50 (p310)** |
| Maintenance of books / servers | 52 (p235) | 48 (p310) |
| Other statutory information | 53 (p235) | 51 (p310) |
| ICCL — SEBI-mandated discontinuation of pooling mechanism / third-party | 54 (p236) | — |
| Title deeds not in Company's name | — | 44 (p308) |
| **Analytical ratios** | — | **46 (p309)** |

---

## 4. FY2017–FY2022 — TREND-YEAR LIGHT MAP

All page numbers below are **PDF pages**, verified in the text; printed folio = PDF − offset.

### 4.1 Statements and reports

| | FY2017 (+2) | FY2018 (+7) | FY2019 (+9) | FY2020 (+7) | FY2021 (+5) | FY2022 (+9) |
|---|---|---|---|---|---|---|
| Contents page | 3 | 8 | 10 | 4 | 4 | 4 |
| Directors'/Board's Report | 17–68 | 16–76 | 25–67 | 22–68 | 23–55 | 25–59 |
| Management Discussion & Analysis | 69–88 | 77–101 | 68–111 | 69–119 | 56–105 | 60–108 |
| **Corporate Governance Report** | **89–110** | **102–119** | **112–128** | **120–139** | **106–126** | **109–129** |
| Business Responsibility Report | **NONE — see §6** | 120–128 | 129–139 | 140–151 | 127–137 | 130–140 |
| **Consolidated auditor's report** | 111–115 | 129–132 | 140–146 | 152–158 | 138–144 | 141–148 |
| Consolidated Balance Sheet | 116 | 133 | 147 | 159 | 145 | 149 |
| Consolidated P&L | 117 | 134 | 148 | 160 | 146 | 150 |
| Consolidated Cash Flow | 118–119 | 135–136 | 149–150 | 161–162 | 147–148 | 151–152 |
| Consolidated SOCIE | 120 | 137 | 151 | 163 | 149 | 153 |
| **Consolidated notes block** | **121–198** | **138–206** | **152–226** | **164–237** | **150–217** | **154–224** |
| **Standalone auditor's report** | 199–203 | 207–212 | 227–234 | 238–244 | 218–224 | 225–232 |
| Standalone Balance Sheet | 204 | 213 | 235 | 245 | 225 | 233 |
| Standalone P&L | 205 | 214 | 236 | 246 | 226 | 234 |
| Standalone Cash Flow | 206–207 | 215–216 | 237–238 | 247–248 | 227–228 | 235–236 |
| Standalone SOCIE | 208 | 217 | 239 | 249 | 229 | 237 |
| **Standalone notes block** | **209–267** | **218–269** | **240–296** | **250–309** | **230–285** | **238–296** |
| **Form AOC-1** | **268** | **270–271** | **297–298** | **310–311** | **286–287** | **297–298** |

### 4.2 The four notes the trend pass must be able to find

| Note | FY2017 | FY2018 | FY2019 | FY2020 | FY2021 | FY2022 |
|---|---|---|---|---|---|---|
| Significant/material accounting policies — consol | Note 2, p121 | Note 2, p138 | Note 2, p152 | Note 2, p164 | Note 2, p150 | Note 2, p154 |
| Significant/material accounting policies — standalone | Note 2, p209 | Note 2, p218 | Note 2, p240 | Note 2, p250 | Note 2, p230 | Note 2, p238 |
| **Related party transactions — consol** | **37, p186** | **35, p192** | **35, p211** | **35, p222** | **35, p205** | **35, p210** |
| **Related party transactions — standalone** | **37, p257** | **35, p259** | **35, p285** | **35, p297** | **35, p273** | **35, p281** |
| **Segment reporting — consol** | **40, p189** | **38, p195** | **38, p215** | **38, p228** | **38, p208** | **38, p214** |
| **Segment reporting — standalone** | **40, p262** | **38, p264** | **38, p291** | **38, p304** | **38, p280** | **38, p288** |
| Contingent liabilities — consol | 38, p189 | 36, p195 | 36, p214 | 36, p227 | 36, p208 | 36, p214 |
| Contingent liabilities — standalone | 38, p262 | 36, p264 | 36, p291 | 36, p303 | 36, p280 | 36, p288 |
| **Revenue notes — consol** | **24 & 25, p174** | **22 & 23, p179–180** | **22 & 23, p197–198** | **22 & 23, p209–210** | **22 & 23, p193** | **22 & 23, p198–199** |
| **Revenue notes — standalone** | **24 & 25, p247** | **22 & 23, p249** | **22 & 23, p274–275** | **22 & 23, p286** | **22 & 23, p263–264** | **22 & 23, p272** |
| Ind AS 115 policy text — consol | n/a (Ind AS 18) | "not yet determined", p205 | p163 | p176 | p161 | p166 |
| Ind AS 116 / right-of-use policy — consol | n/a | n/a | "notified, not yet effective", p226 | **p172 (adopted)** | p158 | p161 |

**Extraction note — heading corruption in FY2019, FY2020 and FY2021.** The text layer of these three
files mangles capitalised headings and a naive grep returns **zero hits on headings that are plainly
there**:

- FY2019 / FY2020 insert stray spaces: `RELA TED PARTY TRANSACTIONS`, `COMP ANY OVERVIEW`,
  `O THER INTANGIBLE ASSETS`, `INVESTMENT PROPER TY`, `INCOME FROM SERVICES TO CORPORA TES`.
- FY2021 mangles the case as well: `35. reLATed PAr TY TrANSACTioNS`, `32. FiNANCiAL iNSTrUMeNTS`,
  `28. AdMiNiSTrATioN ANd oTher eXPeNSeS`.

Use case-insensitive, space-tolerant patterns (`RELA *TED *PAR *TY`) on these three files.
Every FY2019–FY2021 page number in the table above was found that way and then confirmed against the
printed folio.

---

## 5. STRUCTURE CHANGE LOG (FY2017 → FY2026)

Ordered by consequence for the analysis, not chronologically.

### 5.1 The revenue notes were merged in FY2026 — the line taxonomy is NOT comparable across FY2025/FY2026

For nine years BSE ran **two** revenue notes: *Income from securities services* and *Income from
services to corporates*. FY2026 collapses them into a single **Note 22, "Revenue from operations"**
(consolidated PDF p211, standalone p285), grouped as Trading services / Listing services / Treasury
income from clearing and settlement funds / Other operating income.

| Line item | FY2025 (Notes 22 & 23) | FY2026 (Note 22) |
|---|---|---|
| Transaction charges | Note 22 | Note 22, "Trading services" |
| Other charges | Note 22 | **replaced by "Colocation and connectivity charges"** |
| Annual subscription and admission fees | Note 22, separate line | **merged** into "Annual subscription and processing fees" |
| Processing fees | Note 22, separate line | **merged** as above |
| Treasury income from clearing and settlement funds | Note 22 | Note 22 |
| Auction charges | Note 22 | Note 22 |
| Listing fees / Book building software charges / Other fees | Note 23 | Note 22, "Listing services" |
| **Company reinstatement fees** | Note 23, **separate line** | **no longer a separate line** |
| Data dissemination fees / Index related services / Sale of software licences | **P&L face**, no note | Note 22, "Other operating income" as *Data services / Index services / Software solutions and services* |

Net effect: FY2026 is *finer* in some places (colocation, data, index and software each get a line)
and *coarser* in others (reinstatement fees, subscription vs processing). **A revenue-line trend
series built by matching labels across FY2025 and FY2026 will be wrong.** This is a mandatory-chain
trigger under doctrine §3 #3.

### 5.2 The IT-systems Key Audit Matter vanished in FY2025 and came back in FY2026

| Year | Consolidated KAMs | Standalone KAMs |
|---|---|---|
| FY2020 | Valuation of investments (Note 32) | Valuation of investments |
| FY2024 | Valuation of investments (Note 33) **+ IT systems and controls** | Valuation of investments (Note 32) **+ IT systems and controls** |
| FY2025 | Valuation of investments (Note 34) **only** | Valuation of investments (Note 33) **only** |
| FY2026 | **IT systems and controls only** — the investments KAM is gone from the consolidated | Valuation of investments **in subsidiary and associate** (Note 32) **+ IT systems and controls** |

Two movements in two years, in the year the trading business scaled, with a partner rotation in
between (Gandhi → Mutha at FY2025). Doctrine §3 #6 makes anything the auditor named material.

### 5.3 The only Emphasis of Matter in nine years is FY2020

FY2020, **both** blocks: consolidated PDF p152, standalone PDF p238 — Core SGF contribution owed by
BSE to clearing corporations **other than ICCL**, referred to consolidated Note 47, with no impact
taken into the accounts pending SEBI clarification. Opinion not modified. **No emphasis of matter,
qualification, adverse opinion, disclaimer or going-concern material uncertainty exists in FY2017,
FY2018, FY2019, FY2021, FY2022, FY2024, FY2025 or FY2026** — searched for all of those phrases in
every file.

### 5.4 Segment disclosure collapsed from two segments to one at FY2018

- **FY2017**: consolidated **Note 40.1** (PDF p189) — the Group operates in **two** operating
  segments, "Facilitating Trading in Securities and other related ancillary Services" **and
  Depository** services. Standalone Note 40 already reported one segment.
- **FY2018 onward**: one reportable segment in both blocks. FY2019 **Note 38.1** (PDF p215) states
  it explicitly: *"The group operated in two reportable business segments viz: Stock Exchange
  Operations and Depository Services. However, pursuant to the partial …"* — i.e. the CDSL
  deconsolidation removed a whole reportable segment.
- **FY2019 → FY2026**: one operating segment, "Facilitating Trading in Securities and other related
  ancillary services"; the only disaggregation offered is **geography** (within India / outside
  India) plus the revenue note. There has been **no** business-line segment P&L since FY2017.

Note-number path: **40 (FY2017) → 38 (FY2018–FY2022) → 39 (FY2024) → 40 (FY2025) → 39 (FY2026)**.

### 5.5 Note renumbering — the full crosswalk for the lines that matter

| Line | FY2017 | FY2018–FY2022 | FY2024 | FY2025 | FY2026 |
|---|---|---|---|---|---|
| Revenue (securities services) | **24** | 22 | 22 | 22 | **22 (merged)** |
| Revenue (services to corporates) | **25** | 23 | 23 | 23 | **22 (merged)** |
| Investment income | 26 | 24 | 24 | 24 | **23** |
| Other income | 27 | 25 | 25 | 25 | **24** |
| Employee benefits expense | 28 | 26 | 26 | 26 | **25** |
| Computer technology / Technology expense | **none (FY2017 consol)** | 27 | 27 | 27 (**renamed** "Technology expenses") | **26** |
| Regulatory contribution | — | — | — | **28 (new)** | **27** |
| Administration and other expenses / Other expenses | 29 | 28 | 28 | 29 | **28 (renamed "Other expenses")** |
| Impairment loss on financial assets | **30 (consol only)** | **dropped** | — | — | — |
| Tax expense | 31 | 29 | 29 | 30 | **29** |
| Earnings per share | 32 | 30 | 30 | 31 | **30** |
| Financial instruments | 34 | 32 | 33 | 34 | **33** |
| Financial risk management | 35 | 33 | 34 | 35 | **34** |
| Related party transactions (consol) | **37** | 35 | 36 | **37** | **36** |
| Contingent liabilities (consol) | 38 | 36 | 37 | 38 | **37** |
| Segment reporting (consol) | **40** | 38 | 39 | **40** | **39** |
| Core SGF — ICCL (consol) | — | — | **41** | **42** | **41** |
| Core SGF — IFSCA / India ICC (consol) | — | — | **42** | **43** | **42** |
| Trade receivables | 12 | 10 | 10 | 10 | 10 |
| Other financial liabilities (member deposits) | 18 | 16 | 16 | 16 | 16 |

FY2017's higher numbering is caused by two transition-only notes occupying slots 3 and 4
(§5.7). The FY2024→FY2025 shift of +1 in the back half is caused by inserting **Note 28 Regulatory
contribution**; FY2025→FY2026 shifts back by −1 because the two revenue notes merged.

Two FY2017-only wrinkles inside that row, both verified:

- **The FY2017 standalone Note 24 is titled "INCOME FROM TRADING MEMBER"** (PDF p247), not "Income
  from securities services" — that title appears only in the FY2017 *consolidated* Note 24 (PDF
  p174). From FY2018 both blocks use "Income from securities services". A label-matched trend series
  starting at FY2017 standalone will miss the line.
- **FY2017 has no technology-expense note in either block.** Standalone runs 28 Employee benefits →
  29 Administration and other expenses directly (PDF p248–249); consolidated the same (p175–176).
  "Computer technology related expenses" first appears as Note 27 in FY2018, is renamed "Technology
  expenses" in FY2025, and becomes Note 26 in FY2026.

### 5.6 Restatements and reclassifications the company flags

1. **FY2025 restated the FY2024 comparative P&L.** The FY2025 consolidated P&L (PDF p156) shows a
   FY2024 comparative *Revenue from operations* and *Administration and other expenses* that do not
   agree with the FY2024 report as originally issued (PDF p157 of FY2024). The causes named in the
   documents: (a) a **discontinued operation** (FY2025 consolidated Note 53, PDF p218), and (b) the
   carve-out of **Regulatory contribution** into its own line and note. **Any FY2024 P&L figure must
   be taken from one report or the other, never mixed.**
2. **FY2026 restated the FY2025 comparative balance sheet.** Several FY2025 comparative lines in the
   FY2026 consolidated balance sheet (PDF p163) differ from FY2025 as originally reported (PDF
   p155–156) — held-for-sale reclassification (Notes 7.1 & 8.1) and the FY2026 discontinued operation
   (Note 49) are the mechanisms named.
3. **EPS restated in FY2026.** Board's Report PDF p23: *"as per IND AS 33 - Earnings per share, the
   basic and diluted earnings per share for the previous year have been adjusted and restated."*
   (Equity share capital moved between the two years; the Statement of Changes in Equity, PDF p167,
   is the place to read what happened.)
4. **Boilerplate regrouping note.** *"Previous year's figures have been regrouped wherever
   necessary"* appears as a cash-flow footnote in every year (FY2020 p162, FY2021 p148, FY2022 p152,
   FY2024 p159, FY2025 p159, FY2026 p166). It is unquantified in all nine years — a standing
   disclosure gap, not a one-off.
5. **FY2022 and FY2026 SOCIE** both carry a *"Restated balance at the beginning of the current
   reporting period"* row (FY2022 p153, FY2026 p167).

### 5.7 Accounting-standard transitions

| Standard | Year adopted | Where the transition is documented |
|---|---|---|
| **Ind AS (first-time adoption)** | **FY2017** | Consolidated **Note 4 "Explanation of transition to Ind AS"**, PDF p134–140; **Note 3 "New standards and interpretations not yet adopted"**, p133. Standalone equivalent Note 4, incl. *"4.2.1 Effect of Ind AS adoption on the Standalone Balance Sheet as at March 31, 2016 and April 1, 2015"* at PDF p220–221. The FY2017 balance sheets carry **three** columns (2017, 2016, 1-Apr-2015). |
| **Ind AS 115 Revenue from Contracts with Customers** | **FY2019** (effective 1-Apr-2018), **cumulative-effect method** | FY2018 flags it as notified but *"effect … yet to be determined"* (consol PDF p205, standalone p269). FY2019 policy note states adoption: consol PDF p163, standalone p248. Wording persists FY2020 p176 / p259, FY2021 p161 / p239, FY2022 p166 / p247, FY2026 p175 / p257. |
| **Ind AS 116 Leases** | **FY2020** (effective 1-Apr-2019) | FY2019 consolidated PDF p226 records it as notified and not yet effective. FY2020 introduces the right-of-use asset / lease liability policy: consol PDF p172, standalone p255. The FY2020 report does **not** name "Ind AS 116" in the policy text — search for "right-of-use", not the standard number. |
| **Schedule III amendments (ageing schedules, ratios, struck-off companies, title deeds)** | **FY2022 onward** | Trade receivable / trade payable ageing, CWIP and IAUD ageing, analytical ratios, struck-off companies and title-deeds notes all appear from FY2022. See §6 for which of them are still missing from the consolidated statements. |
| **Accounting-policy note restructured** | **FY2025** | FY2024 used roman-numeral sub-clauses under 2.1.6 / 2.1.5; FY2025 and FY2026 use decimal 2.3.x (consolidated) / 2.2.x (standalone). The policy content maps across, but a cite of the form "Note 2(xi)" only exists for FY2024 and earlier. |

### 5.8 Tables that stopped appearing — flagged prominently

1. **"SEBI Regulatory fees" note is gone in FY2026.** Present as consolidated Note 46 / standalone
   Note 45 in **FY2024** (PDF p233 / p308) and **FY2025** (PDF p217 / p275). **Absent from both
   blocks of FY2026** — searched the whole file, the phrase does not occur as a note in FY2026. The
   substance now sits inside **Note 27 Regulatory contribution**, which nets SEBI fees together with
   the Investor Protection Fund and the Core SGF contribution (described in MD&A, PDF p76). The
   separately-visible SEBI regulatory-fee provision is therefore no longer separately visible.
2. **"Buyback" note is gone in FY2026.** Consolidated Note 51 / standalone Note 50 in FY2024 (PDF
   p235 / p310) and FY2025 (p218 / p276); no such note in FY2026. There was no FY2026 buyback, so
   this is expected — but the disclosure of the FY2024 scheme's mechanics is no longer carried
   forward.
3. **"Liquidity Enhancement Scheme" note is gone in FY2026.** Consolidated Note 45 / standalone Note
   41 in FY2024 (PDF p233 / p306); the LES expense also sat on the FY2024 and FY2025 P&L face (FY2025
   referencing note 15.6). Neither the note nor the P&L line appears in FY2026.
4. **"Impairment loss on financial assets" note is gone after FY2017.** FY2017 consolidated Note 30
   (PDF p177). No equivalent note in FY2018 onward; the amount now sits inside other expenses / the
   cash-flow adjustment line.
5. **"Disclosure on Specified Bank Notes (SBNs)" is gone after FY2018.** FY2018 consolidated Note 50
   (PDF p203) / standalone Note 42 (p268). Regulatory sunset, not a company choice — recorded so the
   note-number crosswalk is complete.
6. **Business Responsibility Report did not exist in FY2017.** First appears FY2018 (BRR, printed
   113–121); becomes BRSR from FY2023/FY2024 onward. FY2026 is the first year with an independent
   **reasonable-assurance report on BRSR Core KPIs** (PDF p103–105).
7. **The two-segment consolidated disclosure stopped after FY2017** (§5.4). This is the largest
   single loss of granularity in the nine-year window.
8. **The P&L face lost its separate revenue lines in FY2026.** FY2024 and FY2025 printed *Data
   dissemination fees*, *Index related services* and *Sale of software licences, development,
   customisation & maintenance of software* directly on the consolidated P&L face with no note
   reference. FY2026 shows a single *Revenue from operations* line; those streams survive only inside
   Note 22.
9. **The "Exceptional item" line disappeared after FY2025.** Present on the FY2024 and FY2025
   consolidated P&L faces (FY2025 referencing Note 52, the CDSL stake divestment); no exceptional-item
   line in the FY2026 P&L.
10. **A new subtotal appeared in FY2025 and persists**: *"Profit before contribution to core
    settlement guarantee fund"*, followed by *Contribution to core settlement guarantee fund* as a
    line below the operating total rather than inside expenses (FY2025 PDF p156, FY2026 PDF p164).
    FY2024 has no such subtotal. Operating-margin series that span FY2024/FY2025 are computing two
    different things unless this is normalised.

---

## 6. CANNOT LOCATE / NOT DISCLOSED

Each entry names what I searched for and where I looked. Per doctrine §2b these are gap-register
candidates, not blanks.

| # | Item | Status | Where I looked |
|---|---|---|---|
| 1 | **FY2023 annual report** | **ABSENT (GAP-001)** | `data/text/`, `data/bronze/`, `data/index/` — no FY2023 artifact of any kind. Not chased, per instruction. |
| 2 | **Borrowings note** | **NOT APPLICABLE — no borrowings** | Searched "Borrowings" across FY2026 both blocks. Consolidated and standalone balance sheets carry no borrowings line. Standalone Note 45 *Analytical Ratios* (PDF p309) states "Company does not have any borrowings" against both the debt-equity and DSCR rows; CARO clause (ix)(a) (PDF p246) says the same. Lease liabilities sit inside **Note 16**, not a borrowings note. |
| 3 | **Dedicated finance-cost note** | **NOT DISCLOSED (all nine years)** | FY2026 consolidated P&L p164 and standalone p250 show *Finance cost* with **no note number**; same in FY2025 p156 and FY2024 p157. No note titled "Finance cost" exists in any year. |
| 4 | **Dedicated depreciation & amortisation note** | **NOT DISCLOSED as a note** | The P&L face points to "3 & 4 & 6" (PPE, investment properties, intangibles) in FY2024, FY2025 and FY2026. There is no D&A expense note; the roll-forwards inside Notes 3/4/6 are the only source. |
| 5 | **"Clearing and settlement expense" note** | **NOT DISCLOSED** | Face line on the FY2024, FY2025 and FY2026 consolidated P&L with no note reference. No note of that title exists in any year. |
| 6 | **CWIP ageing schedule — CONSOLIDATED** | **NOT DISCLOSED, FY2024, FY2025 and FY2026** | Searched "capital work-in-progress ageing", "CWIP", "ageing" across each consolidated notes block. FY2026 consolidated (PDF 169–240) contains only two ageing schedules: trade receivables 10.5 (p199) and trade payables 20.1 (p210). CWIP is on the face of the consolidated balance sheet (p163) **with no note reference at all**. The **standalone** has it (Note 3.1: FY2024 p261, FY2025 p239, FY2026 p264). Schedule III requires it in both. |
| 7 | **Intangible-assets-under-development ageing / completion schedule — CONSOLIDATED** | **NOT DISCLOSED, FY2024–FY2026** | Same search. IAUD is on the face of the consolidated balance sheet with no note reference; the schedule exists only in the standalone (Note 6: FY2024 p263, FY2025 p241–242, FY2026 p266–267). |
| 8 | **Ind AS 115 disaggregation-of-revenue table (as such), contract assets, contract liabilities, remaining performance obligations** | **NOT DISCLOSED, FY2024, FY2025 and FY2026** | Searched "disaggregat", "contract liabilit", "contract asset", "remaining performance obligation" across all three files: **zero hits in any of them.** Revenue is broken up by service line inside the revenue note, and the recognition policy (FY2026 consol 2.3.10, p176–177) describes point-in-time vs over-time recognition in prose, but no Ind AS 115 contract-balance disclosure exists. "Income received in advance" and "Advance from customers" inside Note 19 (*Other liabilities*) are the de-facto contract liabilities but are not labelled as such. |
| 9 | **Standalone Core SGF note** | **NOT DISCLOSED as a note (by design)** | FY2026 standalone notes 1–49 contain no Core SGF fund note. The fund is held by ICCL, so it appears only in the consolidated (Notes 41 & 42). In the standalone the Core SGF appears as (a) accounting policy 2.2.12, PDF p260, and (b) part of the *Regulatory contribution* expense, Note 27, PDF p287. Anyone tracing BSE's own SGF exposure at the standalone level has only those two places. |
| 10 | **Analytical ratios — CONSOLIDATED** | **NOT DISCLOSED (all years that have the note)** | The Analytical Ratios note exists only in the standalone: FY2024 Note 46 (p309), FY2025 Note 46 (p275), FY2026 Note 45 (p309). Consistent across years, so not a change — but there is no consolidated ratio table. |
| 11 | **Managerial-remuneration s.197 disclosure inside the financial statements** | **NOT DISCLOSED in the notes** | It lives only in the Board's Report annexure (FY2026 Annexure A, PDF p37–41; FY2025 p36–38; FY2024 p32–35). Director/KMP compensation in the notes is inside the RPT note (FY2026 consolidated Note 36, p223–227). The two are on different bases and must not be treated as the same disclosure. |
| 12 | **AOC-2 (particulars of contracts with related parties)** | **STATED NOT APPLICABLE, FY2026** | Board's Report PDF p31 and CG Report PDF p94 both state AOC-2 under s.134(3)(h) is not applicable for FY2025-26. Recorded because "not applicable" is an assertion the RPT wave should test against Note 36. |
| 13 | **Business Responsibility Report — FY2017** | **DOES NOT EXIST** | Searched "Business Responsibility" across the whole FY2017 file: zero hits. The FY2017 contents page (PDF p3) lists only Directors' Report, MD&A and Corporate Governance Report under Statutory Reports. |
| 14 | **Cash-flow statement entries in the draft index for FY2017–FY2024** | **DRAFT-INDEX DEFECT** | The `cash_flow` key exists only in the FY2025 and FY2026 index files; it is missing entirely from the other seven. The statements themselves are present in all nine documents — see §4.1 and §1.1/§2.1/§3.1. |

---

## 7. DRAFT-INDEX CORRECTION LOG

The auto-generated `data/index/*.index.json` was built by regex and is **unverified and materially
wrong**. Recording this explicitly because a later agent that trusts it will cite the wrong pages.

**Wrong in all nine files:**

- **`printed_map: null` everywhere.** All nine documents *do* carry printed folios; the offsets are
  in §0.1 and are constant. The claim that no mapping could be established is false.
- **The `notes` dictionary is unusable noise.** FY2026 example: note `"3"` → *"For updating E-mail ID
  & Bank details before the Cut-off date"* at PDF p21 (an AGM-notice bullet); note `"6"` → *"Shri
  Gaurav"* at p40; note `"9"` → *"Shri Mayuresh"* at p40; note `"11"` → *"Hindustan Power Exchange
  Limited"* at p110; note `"0"` → *"Number of Issuances"* at p61. **Not one of the primary financial
  notes (1–52 consolidated, 1–49 standalone) is correctly identified.** Only decimal sub-notes
  (2.1, 2.3, 10.4, 10.5, 15.1–15.8, 20.1, 28.1, 39.2, 43.3) were caught, and even those carry no
  consolidated-vs-standalone label, so `10.1` (p276, standalone) and `10.5` (p199, consolidated) are
  presented as if they were the same series.
- **`subsidiaries_aoc1` never points at the AOC-1 statement.** It points at contents pages and
  Board's-Report cross-references (FY2026 `[4, 28]`; FY2024 `[3, 23]`; FY2025 `[3, 4, 27]`). The
  actual Form AOC-1 is at FY2026 PDF 312–313, FY2025 278–279, FY2024 312–313, FY2022 297–298,
  FY2021 286–287, FY2020 310–311, FY2019 297–298, FY2018 270–271, FY2017 268.
- **`related_party` never points at the RPT note's first page.** FY2026 gives
  `[31, 54, 55, 65, 81, 94, 123, 214, 224, 288, 297]` — mostly Board's-Report and CG-Report prose,
  plus two note *continuation* pages (224, 297) and two cross-reference lines (214, 288). It **misses
  p223** (consolidated Note 36) and **p295** (standalone Note 35), the two pages that matter.
- **`corp_governance` misses the report's start page.** FY2026 gives `[35, 96, 98, 99, 100, 101]`;
  the Corporate Governance Report starts at **PDF p78**. FY2019 gives `[128]` alone; the report
  starts at **PDF p112**. FY2021 has **no `corp_governance` key at all**; the report is at PDF
  106–126.
- **`bsr` misses the BRSR start.** FY2026 gives `[35, 103]`; BRSR starts at **p102** (p103 is the
  assurance report inside it). FY2024 gives `[29]` only; BRSR is at PDF 102–147.
- **`accounting_policies` includes the balance sheet and P&L.** FY2026 lists 163 and 164 — those are
  the statements, which merely carry the footer "Material accounting policy 2".
- **`profit_loss` carries spurious pages.** FY2026 lists 265, which is inside the standalone *Other
  intangible assets* note, not a P&L.
- **`cash_flow` key absent** for FY2017–FY2024 (seven of nine files).

**What the draft index got right:** the `balance_sheet`, `profit_loss` (first two entries),
`cash_flow` (where present) and `segment` page hits for FY2025 and FY2026 match what I verified. Use
nothing else from it.

---

## 8. Handover notes for waves 1.5 and 2

1. **Use §0.1 offsets for every cite.** Do not infer an offset from a neighbouring year — they range
   from +2 to +11 and one document (FY2018) is laid out as spreads.
2. **Apply the §0.2 bleed rule** before citing any page you found by grepping the FY2024, FY2025 or
   FY2026 text files, and use tolerant patterns on FY2019/FY2020.
3. **The three lines with the highest structural risk in the deep window** are revenue (§5.1),
   regulatory contribution / SEBI fees (§5.8 #1), and the core-SGF subtotal (§5.8 #10). All three
   changed presentation between FY2024 and FY2026 and all three trip doctrine §3 trigger #3.
4. **Start governance at FY2026 PDF p160 and FY2024 PDF p153** — the consolidated auditor's
   CARO 3(xxi) tables naming which group companies carry qualified or adverse CARO clauses, and
   under which clause.
5. **The only audit-report modification in nine years is FY2020's Emphasis of Matter** (§5.3); it
   concerns the Core SGF, which is also the subject of the FY2025/FY2026 P&L presentation change.
