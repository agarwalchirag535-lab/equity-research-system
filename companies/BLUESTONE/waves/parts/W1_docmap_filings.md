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
