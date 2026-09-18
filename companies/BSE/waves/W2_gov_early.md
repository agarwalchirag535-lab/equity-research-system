# W2 — Governance (early, independent half) — BSE Limited (NSE: BSE)

**Scope:** framework points **1 (board), 2 (ownership), 5 (auditor), 9 (shareholder treatment),
10 (transparency), 11 (regulatory & legal)** only. Accounting quality, capital allocation, RPTs and
promise-vs-delivery are other agents' and are not adjudicated here.

**Sources read:** BSE annual reports FY2017–FY2022 and FY2024–FY2026 (`data/text/BSE-AR-FY*.txt`),
NSE shareholding-pattern index (`data/filings/shareholding.json`, 22 quarterly records
30-Sep-2021 → 30-Jun-2026), NSE corporate announcements 2024–2026 (`announcements_*.json`, 477
records). No external source was used; nothing was downloaded.

**GAP-001 (inherited, not chased):** the **FY2023 annual report is absent**. Every FY2023 column below
is therefore blank or reconstructed from the FY2024 comparative. The 163-day MD&CEO vacancy and the
S.S. Mundra chairmanship both fall inside that hole and are visible only through FY2024's
comparatives and its related-party note. → the document that would close it is **AR FY2023**.

**Page-cite convention (doctrine §5).** `pNN` = **PDF page of the file in `data/text/`**, derived from
the `===== PDF PAGE n =====` markers, not the printed folio. The offset is derived per document and
is not constant: AR FY26 PDF p79 carries printed folio 68; AR FY25 PDF p75 carries printed 64; AR
FY24 PDF p79 carries printed 73.

**Index caveat.** `data/index/*.index.json` is regex-built and was checked before use. It is
unreliable for this domain: FY2017's `notes` map labels note "3" as "BOARD OF DIRECTORS" and note "1"
as "INDIAN CLEARING CORPORATION LIMITED" — those are headings, not notes. Its `sections.corp_governance`
page lists were used only as a starting hint and every page cited below was read directly.

---

## 0. Bottom line, before the evidence

BSE is a **demutualised Market Infrastructure Institution with no promoter at all** — the annual
report says so in terms: *"There are no promoters identified for the Company"*
[AR FY26, Standalone Note 49, p310; Consolidated Note 52, p240]. That single fact removes the
instrument the standard 8-point screen leans on hardest. There is no controlling family to tunnel
value, no pledge to blow up, no promoter-entity RPT chain to trace back to a household. What replaces
it is a **regulator-administered governance structure**: SEBI-approved directors, statutory
shareholding caps, and a board two-thirds of which is Public Interest Directors.

The trust question therefore moves. It is not *"will the promoter take the minority's money"* — there
is no promoter. It is **"does the disclosure machinery of an institution that is itself a regulator
tell you the bad news, and is the function that makes it a regulator adequately accountable?"** On the
first, BSE's *exchange* disclosure is fast and unfailing (same-day, 477 announcements, no exception
found) while its *annual report* aggregation is selectively porous — the group's largest-ever SEBI
penalty, ₹5.05 crore, is disclosed only inside a subsidiary's secretarial-audit annexure while the
same annual report's BRSR penalty table reads "Nil". On the second, the SEBI-mandated Executive
Directors for the three MII verticals were **still not appointed** as at the FY2026 Corporate
Governance Report date, leaving the Chief Regulatory Officer reporting to the MD & CEO — and both of
the group's realised regulatory penalties came out of exactly that function.

The financial size of everything found here is small: ₹8.33 crore of SEBI penalties across FY22–FY26
against FY26 consolidated PAT of ₹2,48,725 lakh — 0.33%. **The money is trivial; the information is
not.** What is at stake is how much of the reported number a reader should assume they are seeing.

---

## 1. BOARD

### 1.1 Composition, year by year

| FY | Board size | PIDs | NID / Shareholder Dirs | MD&CEO | Board meetings | Tag |
|---|---|---|---|---|---|---|
| FY2017 | 10 | 5 (incl. Chairman) | 4 (Shareholder Directors) | 1 | n/d | [AR FY17, Board of Directors, p5] |
| FY2018 | 9 | 5 (incl. Chairman) | 3 | 1 | n/d | [AR FY18, Board of Directors, p3] |
| FY2019 | 9 | 6 (incl. Chairman) | 2 | 1 | n/d | [AR FY19, Board of Directors, p4] |
| FY2020 | 8 | 6 | 1 (LIC nominee) | 1 | n/d | [AR FY20, Board's Report, p25] |
| FY2021 | 8 | 6 | 1 (LIC nominee) | 1 | n/d | [AR FY21, Board's Report, p26] |
| FY2022 | 8 | 6 | 1 (LIC nominee) | 1 | n/d | [AR FY22, Board's Report, p28] |
| FY2023 | — | — | — | — | — | GAP-001 |
| FY2024 | 9 | 7 | 1 NID | 1 | 10 | [AR FY24, Board's Report, p21]; [AR FY24, CG Report, p80] |
| FY2025 | 8 | 6 | 1 NID | 1 | 8 | [AR FY25, Board's Report, p25]; [AR FY25, CG Report, p74] |
| FY2026 | 8 | 6 | 1 NID | 1 | 8 | [AR FY26, CG Report, p78]; [AR FY26, CG Report, p79] |

**Conclusion:** independence is not a judgement call at BSE — it is a structural quota. Six of eight
directors are Public Interest Directors at 31-Mar-2026, and the Chairperson must be one
[AR FY26, CG Report, p78]. Chair/CEO separation has been continuous across every year read
(FY2017–FY2026), and it is mandated, not chosen [AR FY26, CG Report, p95]. The board also states that
**no director holds any equity share of the Company** and that no convertible instruments exist
[AR FY26, CG Report, p80] — so no director has a price-linked incentive, in either direction.

### 1.2 Who actually appoints the Public Interest Directors — and the annual report's own contradiction

This is the load-bearing question for a company with no promoter, and **the FY2026 annual report gives
two different answers in the same document.**

- **Version A (CG Report):** *"While SEBI has the authority to appoint upto three nominee directors,
  there are currently no such appointments in place. All appointments of Directors have been duly
  approved by SEBI."* [AR FY26, CG Report, p78] — SEBI **approves**; the company proposes.
- **Version B (Board evaluation section, 8 pages later):** *"As per SECC Regulations, Public Interest
  Directors **can be appointed by SEBI** on the Board of a Recognized Stock Exchange for an initial
  term of three years, extendable by another term of three years subject to performance review
  prescribed by SEBI."* [AR FY26, CG Report, p85] — SEBI **appoints**.

The historical record supports a **migration from B to A**:

| Year | Language used | Tag |
|---|---|---|
| FY2019 | *"SEBI has nominated Shri Umakant Jayaram as PID … **based on the recommendation of** Nomination and Remuneration Committee and Board of Directors of the Company"* | [AR FY19, Board's Report, p28] |
| FY2020–FY2022 | *"the Board comprises of six Public Interest Directors **nominated by SEBI**, one Shareholder Director nominated by LIC…"* | [AR FY20, p25]; [AR FY21, p26]; [AR FY22, p28] |
| FY2024 | *"**Based on the recommendation of** Nomination and Remuneration Committee ("NRC"), Board of Directors **and approval of SEBI**, Shri Pramod Agrawal and Shri Nandkumar Saravade were appointed as PIDs"* | [AR FY24, Board's Report, p21] |
| FY2025–FY2026 | *"All appointments of Directors have been duly approved by SEBI"* | [AR FY25, CG Report, p74]; [AR FY26, CG Report, p78] |

**Conclusion — and it matters.** The source of PID independence has moved from *the regulator picks
them* to *the board's own NRC picks them and the regulator vetoes or clears*. That is a materially
weaker form of independence: a nominating committee composed of incumbent PIDs choosing the next PIDs
is a self-perpetuating body, with SEBI holding only a negative. The board still has a real external
brake — every appointment, re-appointment and extension needs SEBI's letter, and SEBI retains an
unexercised right to place up to three nominee directors — but the initiative sits inside the company.
This is not disclosed as a change; it is visible only by reading nine years of the same paragraph.

**NOT DISCLOSED:** the annual reports do not reproduce the SECC Regulation that governs PID
appointment, so a reader cannot check which version is right. → **SEBI (SECC) Regulations, 2018,
Regulation 24 and Schedule II Part B**, and **SEBI's approval letters** referenced but not reproduced
at [AR FY26, CG Report, p78].

### 1.3 Chairperson turnover — seven in nine years

| # | Chairperson | Chairman from | Chairman to | Days | Cause of exit | Tag |
|---|---|---|---|---|---|---|
| 1 | Sudhakar Rao (PID) | pre-FY2017 | 28-Jun-2017 | n/d | tenure completed | [AR FY17, Board's Report, p34] |
| 2 | Dhirendra Swarup (PID) | 31-Jul-2017 | 02-Nov-2017 | **94** | PID tenure completed | [AR FY18, Board's Report, p34, p53] |
| 3 | S. Ravi (PID) | 13-Nov-2017 | 04-Feb-2019 | **448** | PID tenure completed | [AR FY18, p53]; [AR FY19, Board's Report, p28] |
| 4 | Justice Vikramajit Sen (PID) | 2019 | FY2022/23 (exact date n/d) | n/d | tenure | signed FY22 Board's Report as Chairman [AR FY22, Annexure A, p49] |
| 5 | S. S. Mundra (PID) | FY2023 (date n/d, GAP-001) | 16-Jan-2024 | n/d | second term completed | [AR FY24, Board's Report, p21]; [AR FY24, CG Report, p81] |
| 6 | Pramod Agrawal (PID) | 17-Jan-2024 | 08-Nov-2024 | **296** | **resigned — "potential conflict with new assignment"** | [AR FY24, CG Report, p81]; [AR FY25, CG Report, p76] |
| 7 | Prof. Subhasis Chaudhuri (PID) | 21-Nov-2024 | in office | — | — | [AR FY25, CG Report, p75] |

Arithmetic (DERIVED, shown): 31-Jul-2017 → 02-Nov-2017 = 31+30+31+2 = **94 days**.
13-Nov-2017 → 04-Feb-2019 = 365 + (17+31+31+4) = **448 days**.
17-Jan-2024 → 08-Nov-2024 = 14+29+31+30+31+30+31+31+30+31+8 = **296 days**.

Two chair-less interregnums fall out of the same table: **02–13 Nov 2017 (11 days)** and
**08–21 Nov 2024 (13 days)**. And in the GAP-001 year the **MD & CEO seat itself was empty for 163
days** — Ashishkumar Chauhan up to 25-Jul-2022, Sundararaman Ramamurthy w.e.f. 04-Jan-2023
[AR FY24, Consolidated Note, p296]. Arithmetic: 6+31+30+31+30+31+4 = **163 days**.

### 1.4 Tenure, attendance, expertise, other directorships

Tenure at 31-Mar-2026, from the practising-company-secretary certificate [AR FY26, CG Report, p99]:

| Director | Category | Appointed | Elapsed at 31-Mar-2026 (DERIVED) |
|---|---|---|---|
| Prof. Subhasis Chaudhuri | PID, Chairperson | 19-May-2022 | 3.87 yr |
| Justice (Retd.) Shiavax Jal Vazifdar | PID | 19-May-2022 | 3.87 yr |
| Dr. Padmini Srinivasan | PID | 14-Feb-2023 | 3.12 yr |
| Shri Jagannath Mukkavilli | NID (LIC nominee) | 13-Feb-2024 | 2.13 yr |
| Shri Shamanna Balasubramanya | PID | 23-Jan-2025 | 1.19 yr |
| Shri Rajiv Bansal | PID | 01-Apr-2025 | 1.00 yr |
| Dr. Santanu Paul | PID | 14-Jan-2026 | 0.21 yr |
| Shri Sundararaman Ramamurthy | MD & CEO | 04-Jan-2023 | 3.24 yr |

Mean PID tenure = (3.87+3.87+3.12+1.19+1.00+0.21)/6 = 13.26/6 = **2.21 years**, against the SECC
maximum of 3+3 = 6 years [AR FY26, CG Report, p85] — i.e. **36.8% of the permitted maximum**. Two PIDs
(Chaudhuri, the Chairperson, and Vazifdar) were appointed on the *same day* and therefore hit the
6-year wall on the *same day* in May 2028.

**Attendance** [AR FY26, CG Report, p79–80]: FY2026, eight meetings. Chaudhuri 8/8, Vazifdar 8/8,
Srinivasan 8/8, Balasubramanya 8/8, Bansal 8/8; Paul 2/2 and Saravade 3/3 (part-year); MD 8/8; the
NID Mukkavilli **7/8**. All directors present attended the last AGM except Saravade.
FY2025, eight meetings [AR FY25, CG Report, p75]: five directors at 8/8, part-year directors at full
attendance, the NID at 7/8, and **one PID at 6/8**. The two-column PDF extraction does not let the
6/8 be pinned to a name with certainty; the sitting-fee schedule is consistent with it being Justice
(Retd.) Vazifdar (₹18,20,000 against ₹21,60,000–₹23,00,000 for the other full-year PIDs)
[AR FY25, CG Report, p84]. → the document that would settle it is **AR FY2025 printed folio 64**, read
as a rendered page rather than as extracted text.
FY2024, ten meetings [AR FY24, CG Report, p80]: Jayaram 10/10, Vazifdar 10/10, Chaudhuri 10/10,
Srinivasan 10/10, Mundra 9/9, Vyas 9/10, Wright 9/10.

**Expertise fit.** The SECC skills matrix at [AR FY26, CG Report, p81] shows only two of eight
directors ticking all six prescribed competences (the MD, and PID Balasubramanya). Legal & regulatory
practice is covered by four; technology by four; risk management by three. Capital markets — the
business the company is actually in — is claimed by only **three of eight** (Chaudhuri, Vazifdar,
Balasubramanya, plus the MD = four including the executive). The board is heavy on administration and
accountancy and thin on markets. Against that, the company runs a mandatory seven-day annual training
programme for every director under SECC [AR FY26, CG Report, p80], and the BRSR records 12 board-level
training programmes in FY2025 [AR FY25, BRSR, p120].

**Other directorships** are low and unproblematic: at 31-Mar-2026 the maximum held by any PID is five
(Bansal), the Chairperson holds one, three PIDs hold none [AR FY26, CG Report, p79–80]. No director is
inter-se related [AR FY26, CG Report, p80].

**Gender.** At 31-Mar-2025 the eight-member board had two women (Jayshree Vyas, Padmini Srinivasan)
[AR FY25, CG Report, p75]. Vyas's second term ended 24-Apr-2025, leaving **1 of 8 = 12.50%** at
31-Mar-2026 [AR FY26, BRSR, p109]. Statutorily compliant, directionally worse.

### 1.5 Resignations and their stated reasons — the same sentence, two years running

| Director | Role | Effective | Stated reason | Time served of a 3-year term | Tag |
|---|---|---|---|---|---|
| Pramod Agrawal | Chairperson & PID | 08-Nov-2024 | *"due to potential conflict with new assignment"* | appointed PID 29-Nov-2023 → **345 days** | [AR FY25, CG Report, p76] |
| Nandkumar Saravade | PID | 21-Aug-2025 | *"due to potential conflict with new assignment"* | appointed PID 07-Feb-2024 → **~18.5 months** | [AR FY26, CG Report, p80] |

Both carry the identical statutory boilerplate — *"there were no material reasons for his resignation
other than those mentioned in his resignation letter"* — and both point the reader to the stock
exchange intimation rather than reproducing the letter [AR FY25, CG Report, p76]; [AR FY26, CG Report, p80].
Both resignations were disclosed to NSE **the same day** [BSE Ann 08-Nov-2024, "Resignation of
Independent director"]; [BSE Ann 21-Aug-2025, "Resignation of Independent director"].

Two mid-term PID exits in consecutive years for the same stated cause is the shape worth naming: BSE
recruits PIDs from a pool of retired senior officials and jurists who are also the pool from which
government and regulatory appointments are made, so the exchange systematically loses independent
oversight to better offers. It is nobody's misconduct; it is a supply problem, and it is why the board
memory is short.

### 1.6 Committees — and the one place the structure does not follow the independence logic

FY2026 composition [AR FY26, CG Report, p83–87]:

| Committee | Chair | Composition | Meetings / attendance |
|---|---|---|---|
| Audit | Dr. Padmini Srinivasan (PID) | 3 PIDs + 1 NID = **75% independent** | 6 held; 6/6, 6/6, 6/6, NID 5/6 |
| Nomination & Remuneration | Dr. Padmini Srinivasan (PID) | 4 PIDs + 1 NID | 8 held; 8/8, 8/8, 8/8, NID 7/8, Paul 2/2 |
| Stakeholders' Relationship / Share Allotment | **Shri Jagannath Mukkavilli (NID)** | 1 NID (chair) + 2 PIDs + MD | 2 held; full attendance |
| PIDs' separate meetings | Prof. Subhasis Chaudhuri | PIDs only | **4 held** (6-May-25, 7-Aug-25, 11-Nov-25, 9-Feb-26), all full attendance |
| Regulatory Oversight | Shri Shamanna Balasubramanya (PID) | PIDs + external professional | n/d in extracted text |

Two observations. First, the Audit Committee is chaired by the one PID whose skills matrix ticks
*Finance and Accountancy* and *Risk Management* [AR FY26, CG Report, p81] — a correct fit, and the
Chairperson of the Audit Committee attended the last AGM [AR FY26, CG Report, p83]. Second, the
**Stakeholders' Relationship Committee — the body that handles minority-shareholder grievances — is
chaired by the Non-Independent Director**, who is the nominee of Life Insurance Corporation, the
largest single shareholder at 5.57% [AR FY26, CG Report, p94]. That is permitted (LODR requires only a
non-executive chair) but it is the one committee where the largest holder's representative presides
over the smallest holders' complaints. One investor complaint was outstanding at 31-Mar-2026, since
resolved [AR FY26, CG Report, p86].

### 1.7 The Executive Directors that are not there

The FY2026 Corporate Governance Report, dated **7 May 2026**, states: *"As on the date of this Report
of Corporate Governance the Company **has initiated the process** for the appointment of Executive
Directors ("EDs") for Vertical 1 (Critical Operations), Vertical 2 (Regulatory, Compliance, Risk
Management and Investor Grievances), and Vertical 3 (Business)."* [AR FY26, CG Report, p79]. As at
31-Mar-2026 the board therefore had **no** vertical ED and the regulatory function ran under a Chief
Regulatory Officer who *"reports to the Managing Director & CEO and the Regulatory Oversight
Committee"* [AR FY26, Board's Report, p32].

The same annual report's cover page — composed at print time, 23-Jul-2026 — lists
**"Shri Gopalan S Raghavan, Executive Director – Vertical 2 (Regulatory, Compliance, Risk Management
& Investor Grievances)"** among the directors [AR FY26, Board of Directors, p4]. The document gives no
appointment date for him, and he appears nowhere else in it. In between, on 2 June 2026, BSE told NSE
of *"resignation of Ms. Kamala Kantharaj from the position of Chief Regulatory Officer"*, redesignated
*"Chief – Special Duty"* [BSE Ann 02-Jun-2026, "Change in Management"].

**NOT DISCLOSED:** the appointment date and terms of the Vertical-2 ED, and whether Verticals 1 and 3
have been filled. → **BSE's stock-exchange intimation of the appointment (Reg. 30 disclosure,
May–July 2026)** and **AR FY2027, Board's Report**.

---

## 2. OWNERSHIP — there is no promoter, and that changes the question

### 2.1 The fact, stated plainly by the company

> *"There are no promoters identified for the Company."*
> [AR FY26, Standalone Note 49 "Other Statutory Information", p310] and identically at
> [AR FY26, Consolidated Note 52, p240].

Corroborated independently by every one of the 22 NSE quarterly shareholding-pattern records from
30-Sep-2021 to 30-Jun-2026: `promoter and promoter group = 0` in all 22, `employee trusts = 0` in all
22 [NSE SHP, shareholding.json]. Corroborated a third time by the FY2019 statutory annual-return
extract, whose promoter tables read *"NOT APPLICABLE"* [AR FY19, MGT-9, p60].

BSE is not a company that happens to have a diffuse register. It is a **demutualised exchange**: the
immovable property notes still record land held by *"The Trustees of the Bombay Stock Exchange"* and
*"Trustees of Native Share & Stock Brokers Associates"*, transferred *"pursuant to the Order of Scheme
of Corporatisation and Demutualisation dated May 20, 2005"*, and explicitly *"Not as promoter,
director, relative or employee of the Company"* [AR FY26, Consolidated Note, p308; Standalone, p245].
Twenty-one years on, the title deeds are still not in BSE's name and it *"has filed an application
with superintendent of land records during the year to update the name of BSE Limited in the property
card"* [AR FY26, Standalone Note, p245].

**Consequence for the screen.** Six of the standard eight promoter tests — pledge, promoter-entity
RPTs, promoter salary vs profit, promoter shareholding trend, promoter-group cross-holdings,
inter-corporate lending to promoter entities — **have no subject**. They are not "clean"; they are
*inapplicable*. The protections they proxy for are supplied instead by (a) SEBI's shareholding caps on
an MII, (b) the PID quota and SEBI's approval over every board seat, and (c) the SECC bar on
share-based pay. Governance risk at BSE is therefore **regulatory risk, not controlling-shareholder
risk** — which is a different animal with a different tail.

### 2.2 Concentration — nobody is near a cap

| As at | Largest holder | % | 2nd | % | Tag |
|---|---|---|---|---|---|
| 31-Mar-2019 | Deutsche Boerse AG | 4.92 | Life Insurance Corporation | 4.88 | [AR FY19, MGT-9, p60] |
| 31-Mar-2022 | Life Insurance Corporation | 5.60 | Zerodha Broking | 3.71 | [AR FY22, CG Report, p123] |
| 31-Mar-2024 | Life Insurance Corporation | 5.60 | Siddharth Balachandran | 3.52 | [AR FY24, CG Report, p94] |
| 31-Mar-2025 | Life Insurance Corporation | 5.60 | Siddharth Balachandran | 3.01 | [AR FY25, CG Report, p87] |
| 31-Mar-2026 | Life Insurance Corporation | 5.57 | Kotak Midcap Fund | 2.43 | [AR FY26, CG Report, p94] |

LIC is the only holder above 5% in any year read, and it is an insurance company and public financial
institution — a category the SECC framework treats differently from an ordinary shareholder. The
tenth-largest holder was 1.17% at 31-Mar-2026 [AR FY26, CG Report, p94]. **No holder approached a cap
in any year examined.**

Register composition has shifted decisively from retail to institutional:
resident individuals **50.93% (FY22) → 45.20% (FY24) → 39.68% (FY26)**; mutual funds
**0.46% (FY22) → 8.57% (FY24) → 12.52% (FY26)**; insurance **6.14% → 8.89% → 11.88%**; FPIs
**12.77% → 13.01% → 19.42%** [AR FY22, CG Report, p123]; [AR FY24, CG Report, p94];
[AR FY26, CG Report, p93]. Arithmetic: institutional (MF + insurance + FPI) **19.37% → 30.47% → 43.82%**.
For a company with no promoter, that is the substitute discipline arriving.

### 2.3 The one ownership fact the annual report does not explain

NSE's index shows `public` shareholding at **79.43%** on 30-Jun-2025 with promoter at zero — leaving
**20.57%** in a non-promoter, non-public bucket — and then **100.00%** from 30-Sep-2025 onward, with
the 30-Jun-2026 record carrying the remark: *"Details of shareholding of Trading Members and Associate
of Trading Members are included in Public category."* [NSE SHP 30-Jun-2026, shareholding.json].
The same series reads 72.89% (30-Sep-2021) → 73.52% (FY22) → 74.14% (FY23) → 77.64% (FY24) → 77.88%
(FY25) [NSE SHP, shareholding.json].

Whether that ~20.6% residual *was* the trading-member block is **not established by these records** —
they carry only the aggregate. The annual reports do not disclose the SECC numeric caps at all; the
FY2026 AGM notice only tells shareholders to *"adhere to the prescribed shareholding limits"* without
naming them [AR FY26, AGM Notice, p14].
**NOT DISCLOSED** → **SEBI (SECC) Regulations, 2018, Regulations 19–21**, and **BSE's quarterly
shareholding-pattern XBRL filings** (URLs are carried in `shareholding.json`, e.g. the 30-Jun-2026
record).

---

## 5. AUDITOR

### 5.1 Identity, tenure, rotation

| Period | Statutory auditor | Appointment | Tag |
|---|---|---|---|
| to FY2017 | Deloitte Haskins & Sells LLP (FRN 117366W/W-100018) | 9th AGM, 01-Aug-2014, 3 years to 12th AGM | [AR FY17, Board's Report, p34]; signed [AR FY17, p113, p115] |
| FY2018–FY2022 | S.R. Batliboi & Co. LLP (FRN 301003E/E300005) | 12th AGM, 04-Sep-2017, 5 years to 17th AGM | [AR FY17, AGM Notice, p11]; [AR FY18, Board's Report, p35] |
| FY2023–FY2027 | S.R. Batliboi & Co. LLP | re-appointed at 17th AGM for a further 5 years to the **22nd AGM (2027)** | [AR FY22, AGM Notice, p10]; [AR FY26, Board's Report, p28] |

**Conclusion.** S.R. Batliboi's first audited year is FY2018 and its last under the current term is
FY2027 — **ten consecutive years, the statutory maximum for an audit firm** under Companies Act
s.139(2). Mandatory rotation therefore falls due at the 22nd AGM in 2027, i.e. the audit of FY2027 is
the last one this firm can sign. The FY2026 annual report says only that the auditors *"have confirmed
that they are not disqualified from continuing"* [AR FY26, Board's Report, p28] and says nothing about
a successor process. **NOT DISCLOSED** → the **Audit Committee's recommendation and the 22nd AGM
notice (2027)**, and any Reg. 30 intimation of a new auditor.

The material subsidiary's auditor has already rotated once in the window: ICCL moved from
**Dalal Doctor and Associates** (appointed 22-Jul-2019) to **KKC & Associates LLP** (appointed
28-Jun-2024) [AR FY24, CG Report, p96]; [AR FY25, CG Report, p89]; [AR FY26, CG Report, p96]. A
five-year term ending in 2024 is the routine explanation and no resignation is reported.

**No auditor resignation** is recorded anywhere: CARO reporting confirms *"There has been no
resignation of the statutory auditors during the year"* [AR FY25, CARO, p226], and the Board's Report
confirms *"the Auditors have not reported any fraud to the Audit Committee or the Board"*
[AR FY26, Board's Report, p28]; [AR FY25, Board's Report, p27].

### 5.2 Opinion, Key Audit Matters, emphasis of matter

| FY | Opinion | KAM 1 | KAM 2 | Emphasis of matter | Tag |
|---|---|---|---|---|---|
| FY2017 | unmodified; ICFR *"opinion is not modified"* | KAM regime not yet in force | — | none found | [AR FY17, p113, p115] |
| FY2019 | unmodified | IT systems and controls | investments / litigation | none found | [AR FY19, Auditor's Report, p227–228] |
| FY2020 | unmodified | Valuation of investments & impairment — **₹2,16,030 lakh = 77% of total assets** | IT systems and controls | **YES** — Core SGF contribution of **₹1,264 lakh** to clearing corporations other than ICCL | [AR FY20, p238–239] |
| FY2021 | unmodified | Valuation of investments — **₹1,97,763 lakh ≈ 66% of total assets** | IT systems and controls | none | [AR FY21, p218] |
| FY2022 | unmodified | Valuation of investments — **₹1,95,987 lakh ≈ 62% of total assets** | IT systems and controls | none | [AR FY22, p225] |
| FY2023 | — | — | — | — | GAP-001 |
| FY2024 | unmodified | Valuation of investments | IT systems and controls | none | [AR FY24, Board's Report, p96]; [AR FY24, p237–238] |
| FY2025 | unmodified | Valuation of investments — **₹2,66,476 lakh = 53.69% of total assets** | IT systems and controls | none | [AR FY25, p220] |
| FY2026 | unmodified | Valuation of investments **in subsidiary and associate only — ₹85,469 lakh** | IT systems and controls | none | [AR FY26, p241] |

Nine consecutive unmodified opinions with a single emphasis of matter (FY2020, quantified at ₹1,264
lakh and resolved thereafter) is a clean record. The interesting movement is in **KAM scope**, not
opinion — see FINDING 5.

### 5.3 Fees — audit vs non-audit

| FY | Statutory audit (standalone, ₹ lakh) | Tax audit | **Other services** | Out of pocket | Non-audit as % of total paid | Tag |
|---|---|---|---|---|---|---|
| FY2017 (Deloitte) | 82 | 8 | 12 | — | 19.6% | [AR FY17, Standalone Note, p249] |
| FY2018 | 57 | 5 | 1 | — | 9.5% | [AR FY18, Standalone Note, p251] |
| FY2019 | 45 | 5 | 1 | 3 | 11.1% | [AR FY19, Standalone Note, p276] |
| FY2020 | 53 | 5 | 2 | 3 | 11.3% | [AR FY20, Standalone Note, p288] |
| FY2021 | 53 | 5 | 4 | — | 14.5% | [AR FY21, Standalone Note, p265] |
| FY2022 | 58 | 6 | 1 | — | 10.8% | [AR FY22, Standalone Note, p274] |
| FY2024 | 67 | 6 | 4 | 3 | 12.5% | [AR FY24, CG Report, p96] |
| FY2025 | 75 | 6 | 4 | 3 | 11.8% | [AR FY25, Standalone Note, p256] |
| FY2026 | 78 | 6 | 2 | 2 | **9.1%** | [AR FY26, Standalone Note, p287] |

Non-audit "other services" have never exceeded ₹4 lakh in any year since FY2018 and are **2.3% of the
₹88 lakh total paid to the auditor in FY2026** (2 ÷ (78+6+2+2) = 2.3%). Including tax audit, non-audit
work is 9.1%. **There is no fee-dependence problem.** The FY2021 Corporate Governance Report's
apparent outlier — *"other services 21"*, total 79 — reconciles once network entities are added:
53+5+4+0 = 62 (P&L note) + Ernst & Young LLP ₹8.00 lakh + PDS Legal ₹9.53 lakh = **₹79.53 lakh ≈ 79**
[AR FY21, CG Report, p121]; [AR FY21, Standalone Note, p265]. **TIE-OUT PASSES.**

Group-wide, the LODR-format disclosure appears only from FY2025: total fees to the statutory auditor
and its network across the Company and subsidiaries were **₹116 lakh (FY25)** and **₹112 lakh (FY26)**
[AR FY25, CG Report, p89]; [AR FY26, CG Report, p96]. In FY2024 and earlier the company published only
the parent's own table, which is a narrower disclosure than the one the format calls for
[AR FY24, CG Report, p96].

---

## 9. SHAREHOLDER TREATMENT

### 9.1 The distribution record

| FY | DPS ₹ (FV ₹2) | Total dividend ₹ lakh | Standalone PAT ₹ lakh | **Payout %** | Buyback | Bonus | ESOP | Tag |
|---|---|---|---|---|---|---|---|---|
| FY2018 | 31 final | n/d | 56,395 | n/d | open-market; 5,48,640 shares to 31-Mar-18; ₹4,487 lakh from securities premium | — | **none** | [AR FY18, Board's Report, p17] |
| FY2020 | — | — | 17,367 | — | **tender: 67,64,705 sh @ ₹680 = ₹460 crore** (13.06% of capital approved) | — | none | [AR FY20, Board's Report, p24] |
| FY2021 | 21 | 9,619 | 9,726 | **98.9%** | — | — | none | [AR FY21, Board's Report, p24] |
| FY2022 | 13.50 | 18,551 | 19,512 | **95.1%** | — | **2:1 — 9,01,78,594 shares allotted 24-Mar-2022** | none | [AR FY22, Board's Report, p26, p27] |
| FY2024 | 15 | 20,599 | 75,339 | **27.3%** | **tender: 34,70,370 sh @ ₹1,080** (revised down from 45,93,137 @ ₹816) | — | none | [AR FY24, Board's Report, p19, p20] |
| FY2025 | 23 (incl. ₹5 special, 150th year) | 31,137 (DERIVED: 23 × 13,53,76,359 = ₹31,136.56 lakh) | 1,11,245 | **28.0%** | — | — | none | [AR FY25, Board's Report, p25]; [AR FY25, Note, p189] |
| FY2026 | 10 (post-bonus) | **41,198** | 2,33,416 | **17.65%** | — | **2:1 — 27,07,52,718 shares allotted** | none | [AR FY26, Board's Report, p24] |

Arithmetic (recomputed independently, doctrine §4b): FY21 9,619 ÷ 9,726 = 98.9%; FY22 18,551 ÷ 19,512
= 95.1%; FY24 20,599 ÷ 75,339 = 27.3% (PAT = PBT 91,864 − tax 16,525 = 75,339); FY25 31,137 ÷ 111,245
= 28.0%; FY26 41,198 ÷ 233,416 = **17.65%**.

**No dilution of any kind.** *"The Company does not have any Employees Stock Option Plan (ESOP) Scheme
for its employees"* in every year read [AR FY22, Annexure, p49]; [AR FY24, p35]; [AR FY26, p40]. The
SEBI (Share Based Employee Benefits and Sweat Equity) Regulations are recorded as **not applicable**
in every secretarial audit [AR FY26, Secretarial Audit, p42]. And under SECC, *"the Managing Director,
being a Key Management Personnel of the Exchange, is not entitled to any stock options"*
[AR FY26, CG Report, p90]. **No preferential allotment or QIP** in any year: Reg. 32(7A) reads "Not
applicable" from FY2020 onward [AR FY20, CG Report, p134]; [AR FY26, CG Report, p93]. The only share
issues in nine years are the two bonus issues and the residual demutualisation-scheme allotments.

### 9.2 The one transaction that tested the board on minority capital

At the FY2022 AGM, shareholders were asked to approve a **one-time retrospective "re-compensation" of
₹99,18,750** to the outgoing MD & CEO Ashishkumar Chauhan, being the difference between his 15%
performance-rated increment eligibility for FY2020-21 and the 2.5% pandemic cap actually applied
[AR FY22, AGM Notice, p10, p23]. The full arithmetic was published — eligibility ₹1,19,02,500 less
increment allowed ₹19,83,750 = ₹99,18,750 — the payment was made **subject to SEBI's approval and to a
shareholder resolution**, it was applied *"as a policy applicable to all employees"*, and ₹12,39,844
of it (50% of the variable component) was deferred three years per SECC [AR FY22, AGM Notice, p23].
Sized: ₹99.19 lakh against FY22 standalone PAT of ₹19,512 lakh = **0.51%**.

**This is disconfirming evidence and should be read as such.** A retrospective top-up to a departing
CEO is exactly the transaction that goes through on a nod at a promoter-controlled company. Here it
was quantified line by line, tied to a firm-wide policy, made conditional on the regulator, and put to
a vote. That is the machinery working.

### 9.3 Executive pay

| FY | MD & CEO compensation | Ratio to median employee | Permanent employees | Tag |
|---|---|---|---|---|
| FY2024 | ₹5,40,78,629 | 48.39× | 518 | [AR FY24, Annexure A, p33] |
| FY2025 | +35.93% YoY | 84.46× | 771 | [AR FY25, Annexure A, p36] |
| FY2026 | ₹8,64,94,321 (+17%) | 79.16× | 850 | [AR FY26, Annexure A, p37, p40] |

MD pay rose 8,64,94,321 ÷ 5,40,78,629 = **+60.0% over two years**; the median employee's pay rose 47%
(FY24), 22% (FY25) and 26% (FY26) [AR FY24, p33]; [AR FY25, p36]; [AR FY26, p37]. PIDs receive
**sitting fees only** — ratios of 0.66× to 3.41× median in FY2026 — and *"None of the Directors were
in receipt of any Commission from the Company or any remuneration from its subsidiaries"*
[AR FY26, Annexure A, p37]; [AR FY25, CG Report, p84]. Half of the MD's variable pay is deferred three
years under SECC [AR FY26, CG Report, p90].

**Conclusion.** No equity, no options, no commission, half the variable deferred: the board and the
CEO are paid in cash and are structurally indifferent to the share price. For a minority holder that
cuts both ways — it removes every dilution and every earnings-management-for-options incentive, and it
removes the alignment too.

---

## 10. TRANSPARENCY

### 10.1 Disclosure speed for bad news — this is the strong part

Every adverse event traceable in the 477 NSE announcements of 2024–2026 was disclosed **on the day it
occurred**:

| Event | Event date | Announced to NSE | Lag | Tag |
|---|---|---|---|---|
| SEBI order against subsidiary ICCL | 25-Feb-2025 | 25-Feb-2025 22:43 | same day | [BSE Ann 25-Feb-2025, "SEBI Order against Indian Clearing Corporation Limited"] |
| ACB Court, Mumbai order — company press release | 02-Mar-2025 | 02-Mar-2025 20:34 | same day | [BSE Ann 02-Mar-2025, "Press Release … order of ACB Court, Mumbai"] |
| SEBI order, ₹25 lakh penalty on BSE | 25-Jun-2025 | 25-Jun-2025 18:06 | same day | [BSE Ann 25-Jun-2025, "Order passed by the Securities & Exchange Board of India"] |
| CGST order, ₹7.25 crore demand | 17-Dec-2025 | 17-Dec-2025 17:35 | same day | [BSE Ann 17-Dec-2025, "Action(s) taken or orders passed"] |
| Chairperson resignation (Agrawal) | 08-Nov-2024 | 08-Nov-2024 14:14 | same day | [BSE Ann 08-Nov-2024, "Resignation of Independent director"] |
| PID resignation (Saravade) | 21-Aug-2025 | 21-Aug-2025 19:23 | same day | [BSE Ann 21-Aug-2025, "Resignation of Independent director"] |
| Chief Regulatory Officer stepping down | 02-Jun-2026 | 02-Jun-2026 17:43 | same day | [BSE Ann 02-Jun-2026, "Change in Management"] |

**No delayed bad-news disclosure was found in the 2024–2026 announcement set.** No technical-glitch,
outage, trading-halt, cyber-incident or data-breach announcement appears at all in that set, and the
FY2026 BRSR reports *"Number of instances of data breaches - 0"* [AR FY26, BRSR, p153].

The company also publishes facts against itself in the annual report: it discloses that BSE
*"is ranked #8 by market capitalization among global stock exchanges … As of March 31, 2025, BSE was
ranked #7 globally"* [AR FY26, MD&A, p57], and that exclusive OFS issues on its platform declined
[AR FY26, MD&A, p59].

### 10.2 Where transparency thins out — the annual report, not the tape

Three of the seven adverse events above **never reach the annual report's governance tables**:

| Event | In CG "penalties/strictures (3 years)" table? | In BRSR Principle-1 penalty table? | Where it actually appears |
|---|---|---|---|
| ICCL ₹5.05 crore SEBI penalty, 25-Feb-2025 | **No** [AR FY25, CG Report, p88] | **No — table reads "Nil"** [AR FY25, BRSR, p120–121] | ICCL secretarial audit annexure only [AR FY25, p45] |
| ACB Court, Mumbai order, Mar-2025 | **No** | **No** [AR FY25, BRSR, p120–121] | nowhere in AR FY25 or AR FY26 |
| SEBI show-cause notice on interoperability against BSE (pending at the FY25 signing date) | **No** [AR FY25, CG Report, p88] | **No** | ICCL secretarial audit only [AR FY25, p45]; outcome first stated in AR FY26 [Secretarial Audit, p48] |

And the parent's own secretarial auditor certified for FY2025: ***"during the audit period, no
specific events took place"*** [AR FY25, Secretarial Audit (DM & Associates), p40], signed 6 May 2025 —
the same season in which the subsidiary's secretarial auditor was reporting a ₹5.05 crore penalty and
a live show-cause notice [AR FY25, ICCL Secretarial Audit (Dhrumil M. Shah & Co. LLP), p45, signed
23 April 2025]. **Both statements are in the same annual report, 5 pages apart. Both are recorded here;
neither is smoothed away** (doctrine §10).

### 10.3 Risk-factor quality, and one grading that disappeared

The FY2026 BRSR materiality table identifies risks and states the *direction* of financial
implications (positive/negative) but **quantifies none of them** — including *"regulatory scrutiny,
penalties, or legal consequences due to non-compliance with mandated recovery standards"*
[AR FY26, BRSR, p113] and *"non-compliance with applicable laws and regulations"* [AR FY26, BRSR, p115].

Contingent liabilities, consolidated (₹ lakh):

| Line | FY2024 | FY2025 | FY2026 | Tag |
|---|---|---|---|---|
| Income tax matters | 11,003 | 11,170 | 13,496 | [AR FY24, Note 37, p225]; [AR FY25, Note, p209]; [AR FY26, Note, p227] |
| Service / indirect tax matters | 2,138 | 2,210 | **5,930** | same |
| Claims not acknowledged as debts | 10,557 | 10,504 | **13,567** | same |
| *of which management considers **remote*** | **10,556 (99.99%)** | **10,504 (100%)** | **line dropped** | same |
| Guarantees given by the Group | 7,70,006 | 10,60,024 | 23 | same |

**The grading vanished in the year the number rose.** In FY2024 and FY2025 the reader was told that
essentially all of the "claims not acknowledged as debts" were considered remote; in FY2026, with that
line up 13,567 − 10,504 = **₹3,063 lakh (+29.2%)**, the sub-line is simply gone
[AR FY26, Consolidated Note, p227]. (The collapse of the guarantees line from ₹10,60,024 lakh to ₹23
lakh is a balance-sheet matter, flagged here for the balance-sheet agent, not adjudicated.)

### 10.4 Guidance

**No numeric forward guidance is given in any annual report read (FY2017–FY2026).** The question
*"was guidance ever withdrawn"* is therefore **not applicable on this evidence base**. → the document
that would settle whether guidance was ever given elsewhere is the **quarterly earnings-call
transcripts**, listed but not read by this half at `data/filings/transcript_candidates.json`.

---

## 11. REGULATORY AND LEGAL HISTORY

### 11.1 The complete ledger, FY2020–FY2026

| Order date | Authority | Entity | Matter | Amount | Status | Tag |
|---|---|---|---|---|---|---|
| 12-Apr-2022 | SEBI | **BSE** | Violation of SEBI circulars of 17-Mar-2010, 18-Nov-1993, 26-Sep-2016, 17-Dec-2018 **"in the matter of inspection and supervision of Karvy Stock Broking Ltd"** | **₹3.00 crore** | appealed; **stayed by SAT; still pending** as at the FY26 report | [AR FY26, CG Report, p94] |
| 29-Jul-2022 | SEBI | BSE | Reg. 38(2) SECC 2018 r/w Reg. 41(3) SECC 2012 — *"engaging in unrelated/non-incidental activities by BSE or its subsidiaries"* | ₹3 lakh | **SAT allowed the appeal and set the order aside, 02-May-2025** | [AR FY25, CG Report, p88]; [AR FY26, CG Report, p94] |
| 25-Feb-2025 | SEBI | **ICCL** (material subsidiary) | *"non-compliances relating to IT asset inventory, submission of audit reports and one-to-one correspondence between Primary Data Centre (PDC) and Disaster Recovery Site (DRS)"*; s.15HB SEBI Act ₹5 lakh + s.23GA SCRA ₹5 crore | **₹5.05 crore** | **paid 09-Apr-2025** | [AR FY25, ICCL Secretarial Audit, p45] |
| 15-May-2025 | SEBI | BSE and ICCL | show-cause notice on the interoperability-among-clearing-corporations circular; **settlement applications not accepted** | nil | disposed **without monetary penalty** | [AR FY26, Secretarial Audit, p48]; [AR FY26, ICCL Secretarial Audit, p48–49] |
| 25-Jun-2025 | SEBI | BSE | Reg. 39(3) SECC + circulars — *"delay in dissemination of information to investors, Institutional Client Code modification and error account monitoring"*, arising from SEBI's inspection of **1-Feb-2021 to 30-Sep-2022** | **₹25 lakh** | paid within the stipulated period | [AR FY26, CG Report, p95]; [AR FY26, BRSR, p124] |
| 17-Dec-2025 | CGST & Central Excise, Mumbai South | BSE | s.73 CGST — excess input tax credit availed, Apr-2021 to Mar-2022 | GST ₹6,59,26,901 + penalty ₹65,92,690 + unquantified interest = **₹7,25,19,591** | appeal filed 06-Mar-2026 | [AR FY26, BRSR, p124] |

Prior to this, the CG penalty table read *"Not Applicable"* for FY2020 [AR FY20, CG Report, p134] and
FY2021 [AR FY21, CG Report, p121]; the FY2022 table carried the Karvy order as a post-balance-sheet
event [AR FY22, CG Report, p124]. One pre-order figure is on the record and worth keeping: SEBI
*"indicated an amount of Rs. 8,62,50,000/- as a probable settlement amount"* for ICCL's
interoperability matter [AR FY24, ICCL Secretarial Audit, p43] — a matter that ultimately closed with
no penalty at all.

**Totals.** SEBI penalties imposed on the group FY22–FY26 = 3.00 + 0.03 + 5.05 + 0.25 = **₹8.33 crore**,
of which **₹5.30 crore paid**, ₹3.00 crore contested for over four years, ₹0.03 crore set aside.
Against FY2026 consolidated PAT of ₹2,48,725 lakh, that is **0.33%**.

### 11.2 Is it a pattern? Yes — and the pattern has a single address

Strip out the two items that are not about running an exchange (the ₹3 lakh unrelated-activities order,
set aside; the CGST input-credit demand, a tax dispute), and **every remaining SEBI action against the
group is a failure of the regulatory/supervisory/IT-resilience function**:

- Karvy — failure of **inspection and supervision** of a member.
- ICCL ₹5.05 crore — failure of **IT asset inventory, audit-report submission, PDC–DRS correspondence**.
- ₹25 lakh — failure of **dissemination to investors, institutional client-code modification, error
  account monitoring**.

Three orders, three different years, one function. That is a pattern, not an accident, and the
inspection windows land on the years when the activity-based spend on that function was at its lowest
(see §11.4).

### 11.3 BSE as regulator of its own fee-payers — the structural conflict, sized

BSE simultaneously (a) charges the companies it regulates, and (b) polices them.

| FY | Annual listing fees (₹ cr) | Corporate-services / book-building fees (₹ cr) | Combined | Standalone total revenue (₹ cr) | **Combined as % of revenue** | Tag |
|---|---|---|---|---|---|---|
| FY2021 | 159 | 34 | 193 | 565.05 | 34.2% | [AR FY22, MD&A, p81]; [AR FY22, Board's Report, p25] |
| FY2022 | 164 | 53 | 217 | 724.02 | **30.0%** | [AR FY22, MD&A, p81, Board's Report, p25] |
| FY2024 | 192 | 48 | 240 | 1,291.80 | 18.6% | [AR FY25, MD&A, p55]; [AR FY24, Board's Report, p18] |
| FY2025 | 224 | 95 | 319 | 2,912.75 | 11.0% | [AR FY25, MD&A, p55]; [AR FY26, Board's Report, p23] |
| FY2026 | 242 | 104 | 346 | 4,836.34 | **7.15%** | [AR FY26, MD&A, p63]; [AR FY26, Board's Report, p23] |

Counter-proportion, and it runs the *right* way: **the share of revenue that comes from the population
BSE regulates has fallen from 30.0% to 7.15% in four years** as derivatives transaction income
overwhelmed the listing franchise. The financial temptation to go soft on an issuer is a fifth of what
it was.

Two further mitigants, both checkable. **Enforcement fines do not reach BSE's P&L** — the consolidated
note records that Other Contribution to the settlement funds comprises, among other things,
*"penalties collected and transferred by BSE as per SEBI directions"* and *"fines & penalties collected
from members by ICCL"* [AR FY26, Consolidated Note 40, p231]. And BSE does in fact delist its own
fee-payers: **1,484 companies delisted between 1-Apr-2016 and 31-Mar-2026** for non-compliance
[AR FY26, MD&A, p66], up from 1,450 to 31-Mar-2025 [AR FY25, MD&A, p58] and 1,383 to 31-Mar-2024
[AR FY24, MD&A, p61].

The one uncomfortable number: enforcement delistings were **67 in FY2025 (1.23% of 5,452 listed
companies) and 34 in FY2026 (0.60% of 5,663)** — halved as a share of the base — in a year listing-fee
income rose 8% [AR FY26, MD&A, p57, p63, p66]. The honest counter is that the stock of chronically
suspended companies is finite and largely worked through; a declining run-rate is what exhaustion looks
like, not necessarily what forbearance looks like. Recorded, not concluded.

### 11.4 The regulatory function: what it costs, and what it is worth

BSE publishes, under a SECC disclosure requirement, an **activity-based-accounting** figure for
resources committed to its own regulatory and compliance function:

| FY | Regulatory-function spend (₹ lakh) | Standalone total revenue (₹ lakh) | **% of revenue (DERIVED)** | Regulatory headcount | Permanent employees | Reg. share of headcount | Tag |
|---|---|---|---|---|---|---|---|
| FY2019 | **2,555** | 61,239 | 2,555 ÷ 61,239 = **4.17%** | n/d | n/d | — | [AR FY19, Board's Report, p41]; [AR FY20, Board's Report, p22] |
| FY2020 | 2,116 | 54,213 | 2,116 ÷ 54,213 = **3.90%** | n/d | n/d | — | [AR FY20, Board's Report, p39, p22] |
| FY2021 | **1,699.66** | 56,505 | 1,699.66 ÷ 56,505 = **3.01%** | n/d | n/d | — | [AR FY21, Board's Report, p40, p21] |
| FY2022 | 1,965 | 72,402 | 1,965 ÷ 72,402 = **2.71%** | n/d | n/d | — | [AR FY22, Board's Report, p41, p25] |
| FY2023 | — | 74,239 | — | — | — | — | GAP-001; revenue from [AR FY24, Board's Report, p18] |
| FY2024 | 3,057.81 | 1,29,180 | 3,057.81 ÷ 1,29,180 = **2.37%** | 193 | 518 | 37.3% | [AR FY24, Board's Report, p28, p18, p33] |
| FY2025 | 4,692 | 2,91,275 | 4,692 ÷ 2,91,275 = **1.61%** | 295 | 771 | 38.3% | [AR FY25, Board's Report, p31, p36]; [AR FY26, p23] |
| FY2026 | **6,567** | 4,83,634 | 6,567 ÷ 4,83,634 = **1.36%** | 333 | 850 | 39.2% | [AR FY26, Board's Report, p32, p23, p37] |

**Do not confuse this with the P&L line called "Regulatory Fees."** That is a different measure — SEBI's
turnover-based fee plus Investor Services / Investor Protection Fund contributions — and it moved the
other way in FY2020, rising ₹2,031 lakh standalone from ₹4,830 lakh to ₹6,861 lakh, of which ₹1,861
lakh was an additional ISF/IPF provision [AR FY20, MD&A, p116]. The two series are not comparable and
are kept apart here deliberately.

---

## Gap register — this half's contributions

| # | Gap | What is missing | Peers disclose? | Document that would answer it |
|---|---|---|---|---|
| G-GOV-01 | PID appointment mechanism | Which of the AR's two contradictory accounts is correct | n/a (MII-specific) | SEBI (SECC) Regulations 2018 Reg. 24 & Sch. II Pt. B; SEBI approval letters cited at [AR FY26, CG Report, p78] |
| G-GOV-02 | SECC numeric shareholding caps | The 5% / 15% / trading-member limits are never stated | n/a | SECC Regulations 2018 Regs. 19–21; quarterly shareholding-pattern XBRL (URLs in `shareholding.json`) |
| G-GOV-03 | The ~20.6% non-promoter non-public block to Jun-2025 | Who held it and under what category | — | Quarterly shareholding-pattern XBRL, `shareholding.json` 30-Jun-2025 record |
| G-GOV-04 | Vertical ED appointments | Date, terms and identity for Verticals 1 and 3; date for Vertical 2 | NSE discloses its vertical EDs | BSE Reg. 30 intimation May–Jul 2026; AR FY2027 Board's Report |
| G-GOV-05 | Statutory auditor rotation due FY2027 | Whether a successor process has begun | yes, commonly | Audit Committee recommendation; 22nd AGM notice (2027) |
| G-GOV-06 | ACB Court, Mumbai order | Content and BSE's exposure; absent from AR FY25 and AR FY26 | — | The press release PDF at the URL in `announcements_2025.json`, 02-Mar-2025 record |
| G-GOV-07 | Contingent-liability "remote" grading | Dropped in FY2026 as the claim rose 29.2% | yes | AR FY2027 Note on contingent liabilities; or a direct question at the next call |
| G-GOV-08 | FY2023 annual report | Whole year: chairmanship dates, MD vacancy, regulatory spend | — | **AR FY2023** (GAP-001, not chased per instruction) |
| G-GOV-09 | FY2025 board attendance attribution | Which PID recorded 6/8 | — | AR FY2025 printed folio 64, rendered rather than text-extracted |

## Contradictions recorded (doctrine §10 — nothing resolved by deletion)

1. **Who appoints PIDs.** [AR FY26, CG Report, p78] (SEBI approves) vs [AR FY26, CG Report, p85]
   (SEBI appoints). Both stand.
2. **Whether anything happened in FY2025.** *"during the audit period, no specific events took place"*
   [AR FY25, Secretarial Audit, p40] vs a ₹5.05 crore penalty and a live show-cause notice
   [AR FY25, ICCL Secretarial Audit, p45]. Both stand.
3. **Whether BSE has a Vertical-2 Executive Director.** *"has initiated the process"*
   [AR FY26, CG Report, p79, dated 7-May-2026] vs Shri Gopalan S Raghavan listed as
   "Executive Director – Vertical 2" [AR FY26, Board of Directors, p4, printed 23-Jul-2026]. Both stand.
4. **FY2025 consolidated audit fee.** ₹124 lakh as originally reported [AR FY25, Consolidated Note,
   p196] vs ₹121 lakh as the FY2026 comparative [AR FY26, Consolidated Note, p213]. Difference ₹3 lakh;
   immaterial, but not explained. Routed to the notes-forensics agent.

---

## FINDINGS

### FINDING: BSE's regulatory function — the thing that makes it an exchange — has no board-level owner, and every SEBI penalty the group has ever paid came out of it
S1 WHAT: Across FY2022–FY2026 SEBI passed three enforcement orders against the BSE group that bite on the same function: ₹3.00 crore for failure of "inspection and supervision of Karvy Stock Broking Ltd" [AR FY26, CG Report, p94], ₹5.05 crore on subsidiary ICCL for "IT asset inventory, submission of audit reports and one-to-one correspondence between Primary Data Centre (PDC) and Disaster Recovery Site (DRS)" [AR FY25, ICCL Secretarial Audit, p45], and ₹25 lakh for "delay in dissemination of information to investors, Institutional Client Code modification and error account monitoring" [AR FY26, CG Report, p95] — while the SEBI-mandated Executive Directors for Vertical 1 (Critical Operations), Vertical 2 (Regulatory, Compliance, Risk Management and Investor Grievances) and Vertical 3 (Business) were still unappointed at the FY2026 Corporate Governance Report date of 7 May 2026 [AR FY26, CG Report, p79].
S2 WHY: The mechanism is the reporting line, not effort. The Chief Regulatory Officer "reports to the Managing Director & CEO and the Regulatory Oversight Committee" [AR FY26, Board's Report, p32] — that is, the head of supervision reports to the person whose scorecard is business growth, and the separation SEBI's three-vertical rule exists to create had not yet been built. A Regulatory Oversight Committee that meets periodically is not a substitute for a line manager; it reviews, it does not run. The absolute spend cut of FY2019–FY2021 then supplied the opportunity: the activity-based regulatory-function figure fell from ₹2,555 lakh to ₹1,699.66 lakh [AR FY19, Board's Report, p41]; [AR FY21, Board's Report, p40] over precisely the period spanning the Karvy default and the SEBI inspection window of 1-Feb-2021 to 30-Sep-2022 that produced the ₹25 lakh order [AR FY26, CG Report, p95].
S3 EVIDENCE: Regulatory-function spend and its counter-proportion: ₹2,555 lakh on standalone revenue of ₹61,239 lakh in FY2019 = 4.17%, against ₹6,567 lakh on ₹4,83,634 lakh in FY2026 = 1.36% [AR FY19, Board's Report, p41, p26]; [AR FY26, Board's Report, p32, p23] — spend up 6,567 ÷ 2,555 = 2.57× (+157%) while the revenue it must supervise rose 4,83,634 ÷ 61,239 = 7.90× (+690%), so supervisory intensity fell by two-thirds. Inside the window that matters, FY2019 to FY2021, spend fell 1,699.66 ÷ 2,555 = −33.5% while revenue fell only 56,505 ÷ 61,239 = −7.7% — a cut four times deeper than the revenue decline that ostensibly justified it. Realised cost: ₹5.30 crore paid (₹5.05 crore on 09-Apr-2025 plus ₹25 lakh), ₹3.00 crore contested in SAT since April 2022. Against FY2026 consolidated PAT of ₹2,48,725 lakh, total penalties of ₹8.33 crore are 0.33%.
S4 CONNECTS: The Governance record (unappointed vertical EDs, CRO reporting to the MD) meets the Business record (BSE is a Market Infrastructure Institution whose product is trust, [AR FY26, CG Report, p78]) meets Management commentary (the same Board's Report that discloses the ₹6,567 lakh spend also discloses the reporting line, [AR FY26, Board's Report, p32]) meets the Income Statement (the spend series against standalone revenue). The named compensating control is the auditor's IT-systems-and-controls Key Audit Matter, present in every year FY2019–FY2026 and concluded on each time [AR FY19, p227]; [AR FY26, p241]. The class of error it cannot catch is precisely the one SEBI found: an ITGC audit is scoped to controls relevant to the *financial statements*, so it tests user access, program change and related general controls over reporting systems — it does not test whether the disaster-recovery site mirrors the primary data centre one-to-one, because a DR failure destroys market continuity, not the trial balance. Nine clean IT KAMs and a ₹5.05 crore DR-site penalty are not in conflict; they are measuring different things.
DOMAINS: Governance, Business, MgmtCommentary, IncomeStatement, Notes
DISCONFIRM: Searched for, and found, three pieces of evidence cutting the other way. (i) The regulatory function is not shrinking in people: headcount rose 193 → 295 → 333 and its share of permanent employees rose 193/518 = 37.3% (FY24) to 333/850 = 39.2% (FY26) [AR FY24, Board's Report, p28, p33]; [AR FY26, Board's Report, p32, p37] — so "under-resourcing" is not established by the revenue ratio alone. (ii) Spend grew 6,567 ÷ 4,692 = +40.0% in FY2026 alone, the largest increase in the series. (iii) BSE does not profit from enforcement: fines collected from members and issuers are transferred to the settlement and protection funds, not to the P&L [AR FY26, Consolidated Note 40, p231]. The finding rests on the accountability structure and the penalty pattern, not on the ratio in isolation.
S5 MEANS: For an exchange, the regulatory function is not a cost centre attached to the business — it is the licence, and BSE ran it for the whole of FY2026 without the board-level owner its own regulator had mandated, having already been fined three times on that function's failures.
BASE-RATE: Yes — this pattern has cost money at this company, three times, which is what distinguishes it from a theoretical governance concern. ₹5.30 crore paid and ₹3.00 crore contested for over four years. The wider base rate is worse than the cash: the Karvy episode itself, in which a broker misused client securities, is the systemic precedent for what happens when exchange-level member supervision fails, and BSE's own penalty is the regulator's finding that BSE's supervision was part of that failure [AR FY26, CG Report, p94]. Separately, SEBI once indicated ₹8,62,50,000 as a probable settlement amount for the ICCL interoperability matter [AR FY24, ICCL Secretarial Audit, p43] — larger than any penalty actually levied, and a marker of the size SEBI thinks in.
S6 IMPLICATION: The durability of BSE's earnings rests on a licence that the regulator has already fined three times on the same function, so the monitorable is structural rather than financial — whether all three vertical Executive Directors are in place and reporting to the Governing Board rather than to the MD & CEO, checked at the FY2027 annual report and at any Reg. 30 intimation before it; the thesis-breaker is a SEBI order that restricts a segment or a product rather than levying cash, because the ₹8.33 crore of penalties to date is 0.33% of one year's consolidated PAT and is not the exposure — the exposure is an operational direction that suspends a revenue line.
SEVERITY: High

### FINDING: The group's largest-ever SEBI penalty, ₹5.05 crore, appears only inside a subsidiary's secretarial-audit annexure while the same annual report's own penalty tables read "Nil" and "no specific events took place"
S1 WHAT: SEBI's order of 25 February 2025 fined Indian Clearing Corporation Limited — BSE's wholly-owned material subsidiary — ₹5.05 crore (₹5 lakh under s.15HB of the SEBI Act and ₹5 crore under s.23GA of the SCRA), paid on 9 April 2025 [AR FY25, ICCL Secretarial Audit, p45]. In the FY2025 annual report that fact appears in exactly one place: page 45, inside Annexure C, the secretarial audit report *of the subsidiary*. It does not appear in the Corporate Governance Report's three-year "non-compliance, penalties, strictures" table, which lists only two BSE-level actions [AR FY25, CG Report, p88]. It does not appear in the BRSR Principle-1 penalty table, which records "Nil" for monetary penalty, "Nil" for settlement and "Nil" for compounding fee [AR FY25, BRSR, p120–121]. And BSE's own secretarial auditor certified for the same year that "during the audit period, no specific events took place" [AR FY25, Secretarial Audit, p40].
S2 WHY: The mechanism is a scoping rule applied literally rather than a concealment. The CG penalty table is framed as actions "on the Company", the BRSR table is expressly "on the basis of materiality as specified in Regulation 30", and the two secretarial audits are separate engagements by different firms — DM & Associates for BSE, signed 6 May 2025, and Dhrumil M. Shah & Co. LLP for ICCL, signed 23 April 2025 [AR FY25, p40, p45]. Nobody had to consolidate the subsidiary's enforcement record into the parent's governance narrative, so nobody did. That is exactly why the outcome is a governance fact and not a clerical one: the boundary was drawn at the legal entity, when the reader's boundary is the consolidated group whose PAT they are buying.
S3 EVIDENCE: The asymmetry is inside the disclosure choices, not between years. A ₹25 lakh penalty on BSE was disclosed in FY2026 in three separate places — CG Report [AR FY26, p95], BRSR monetary-penalty table [AR FY26, p124], and BSE's own secretarial audit [AR FY26, p43]. A ₹5.05 crore penalty on ICCL was disclosed in FY2025 in one place, a subsidiary annexure. The penalty that got triple billing is 0.25 ÷ 5.05 = **4.95% the size** of the penalty that got single billing — a 20-fold difference in amount running in the opposite direction to prominence. Sized against earnings: ₹5.05 crore is 0.38% of FY2025 consolidated PAT of ₹1,32,232 lakh [AR FY26, Board's Report, p23], and ₹25 lakh is 0.01% of FY2026 consolidated PAT of ₹2,48,725 lakh. Two further FY2025 adverse items received the same single-annexure treatment: the SEBI show-cause notice on interoperability, disclosed only via ICCL's annexure [AR FY25, p45], and the ACB Court, Mumbai order, disclosed to NSE on 2 March 2025 [BSE Ann 02-Mar-2025] and appearing in neither the FY2025 nor the FY2026 annual report.
S4 CONNECTS: Governance (which tables the company populates and which it leaves blank), Notes (ICCL is the material subsidiary carrying ₹81,645 lakh of consolidated net assets, 12% of group net assets, [AR FY26, Consolidated Note 40, p228]), Management commentary (the Board's Report designates ICCL the material subsidiary and annexes its secretarial audit under Reg. 24A, [AR FY26, Board's Report, p32]), and Business (the penalised failures — IT asset inventory, DR-site correspondence — sit in the clearing and settlement engine, not in a peripheral entity). The compensating control is Reg. 24A itself, which forced the subsidiary's secretarial audit into the annual report and is the only reason a reader can find this at all. The class of error it cannot catch: Reg. 24A guarantees the *document* is attached, not that its contents are carried up into the parent's own governance tables — so a diligent reader of the Corporate Governance Report and the BRSR, which is where a reader looks for penalties, learns nothing.
DOMAINS: Governance, Notes, MgmtCommentary, Business
DISCONFIRM: Looked for, and found, substantial evidence against a concealment reading. The order was disclosed to NSE on the day it was passed, at 22:43 on 25 February 2025 [BSE Ann 25-Feb-2025, "SEBI Order against Indian Clearing Corporation Limited"] — so the market was told in real time and the annual report is a lagging aggregation problem, not a suppression. The FY2025 annual report also discloses ICCL's live show-cause notice and, in FY2024, SEBI's indicated settlement amount of ₹8,62,50,000 [AR FY24, ICCL Secretarial Audit, p43] — a company hiding subsidiary enforcement would not publish a number that large. And the amount is genuinely immaterial to group earnings at 0.38% of PAT, so a materiality-based exclusion from the BRSR table is defensible on its face. What is not defensible is the same test producing "disclose" for ₹25 lakh and "Nil" for ₹5.05 crore.
S5 MEANS: BSE's disclosure is fast at the entity level and porous at the group level, so an investor who reads only the annual report's governance tables gets a materially incomplete enforcement record — and the incompleteness is not random, it removes the largest item.
BASE-RATE: The direct financial loss is established and small: ₹5.05 crore paid on 9 April 2025 [AR FY25, ICCL Secretarial Audit, p45], 0.38% of that year's consolidated PAT. No instance was found, at this company or in the announcement set, of a subsidiary-level disclosure gap escalating into a restatement, a qualification or a regulatory action against the parent for non-disclosure — recorded explicitly as none found. The pattern's cost here is informational rather than realised, which is why it is graded High on trust and not on cash.
S6 IMPLICATION: Where a company's governance tables and its exchange filings disagree in completeness, the filings are the primary record and the annual report is a summary that has been shown to omit its own largest item — so any assessment of this group's regulatory standing must be built from the announcement stream and the subsidiary annexures rather than from the Corporate Governance Report, and the practical monitorable is whether the FY2027 report consolidates subsidiary enforcement into the parent's penalty table now that a ₹5.05 crore precedent exists.
SEVERITY: High

### FINDING: BSE has no promoter under SEBI rules, which deletes six of the eight standard screen questions and replaces controlling-shareholder risk with regulator-administered risk
S1 WHAT: The company states in both sets of financial statements that "There are no promoters identified for the Company" [AR FY26, Standalone Note 49, p310; Consolidated Note 52, p240]. All 22 NSE quarterly shareholding-pattern records from 30-Sep-2021 to 30-Jun-2026 show promoter and promoter-group holding of zero and employee-trust holding of zero [NSE SHP, shareholding.json], and the FY2019 statutory annual-return promoter tables read "NOT APPLICABLE" [AR FY19, MGT-9, p60]. The largest holder in every year examined is Life Insurance Corporation of India at 5.60% (FY22, FY24, FY25) and 5.57% at 31-Mar-2026 [AR FY22, CG Report, p123]; [AR FY26, CG Report, p94].
S2 WHY: This is a legal consequence of demutualisation, not a drift in the register. BSE was corporatised and demutualised under a scheme dated 20 May 2005; the immovable-property notes still record land held by "The Trustees of the Bombay Stock Exchange" and "Trustees of Native Share & Stock Brokers Associates", expressly "Not as promoter, director, relative or employee of the Company" [AR FY26, Consolidated Note, p308]. The broker-members who owned the mutual exchange were converted into ordinary shareholders and no successor control block was permitted to form, because SECC Regulations cap what any single holder in an MII may own.
S3 EVIDENCE: Concentration and its counter-proportion. The single largest holder is 5.57% while the tenth-largest is 1.17%, so the entire top-ten block is a minority of the register [AR FY26, CG Report, p94]; the balance is 39.68% resident individuals, 19.42% foreign portfolio investors, 12.52% mutual funds, 11.88% insurance companies and 10.49% bodies corporate [AR FY26, CG Report, p93]. Over four years the register moved decisively: resident individuals 50.93% (FY22) to 45.20% (FY24) to 39.68% (FY26), while institutions (mutual funds plus insurance plus FPIs) went 0.46+6.14+12.77 = 19.37% to 8.57+8.89+13.01 = 30.47% to 12.52+11.88+19.42 = 43.82% [AR FY22, CG Report, p123]; [AR FY24, CG Report, p94]; [AR FY26, CG Report, p93]. No holder in any year read approached a cap. And no director holds a single share [AR FY26, CG Report, p80].
S4 CONNECTS: Governance (six of eight directors are Public Interest Directors and every appointment needs SEBI's clearance, [AR FY26, CG Report, p78]), Business (a Market Infrastructure Institution is licensed, not merely incorporated), Industry (the same SECC framework governs NSE, MCX, CDSL and NSDL, so this is a sector structure rather than a company choice), and the Balance Sheet (the demutualisation legacy is still live in the property notes and in 6,50,000 shares held in abeyance under the scheme, [AR FY26, Consolidated Note, p308]; [AR FY25, Note, p189]). The compensating controls for an absent promoter are the SECC ownership caps and the PID quota. The class of error they cannot catch: caps and quotas constrain *who* sits on the register and the board, but they say nothing about whether a diffuse register can actually discipline management — with no holder above 5.6% and directors paid entirely in cash with no equity [AR FY26, CG Report, p90], there is no shareholder with either the stake or the standing to force a change, and the only real external check is the regulator itself.
DOMAINS: Governance, Business, Industry, BalanceSheet
DISCONFIRM: Actively searched for a de facto controller and found none. No director holds equity and none are inter-se related [AR FY26, CG Report, p80]; there is no ESOP, no sweat equity and no convertible instrument in any year read [AR FY26, Annexure A, p40]; no preferential allotment or QIP has ever been made, Reg. 32(7A) reading "Not applicable" throughout [AR FY20, CG Report, p134]; [AR FY26, CG Report, p93]. The only nominee-type seat is the single Non-Independent Director nominated by LIC, whose appointment required both a shareholder postal ballot and SEBI's approval, received 13 February 2024 [AR FY24, Board's Report, p21]. Evidence against the *completeness* of this picture does exist: NSE's index shows a non-promoter, non-public residual of 100 − 79.43 = 20.57% at 30-Jun-2025, reported as folded into "Public" from 30-Sep-2025 with the remark that trading-member and associate shareholding is now included there [NSE SHP 30-Jun-2026, shareholding.json] — whose composition is not established by these records and is recorded as G-GOV-03.
S5 MEANS: The standard eight-point screen cannot be run here, because its central instrument is promoter conduct and there is no promoter — so the trust question shifts entirely onto disclosure integrity and regulatory standing, which is where the rest of this half's findings sit.
BASE-RATE: No realised loss from ownership concentration has ever occurred at BSE, and none could: no holder has exceeded 5.60% in any of the nine years read, and no pledge, encumbrance or promoter-entity transaction exists to have failed. The relevant systemic base rate runs the other way and is not favourable — the material governance losses at Indian exchanges have come from the management-and-regulator axis rather than from a controlling shareholder, and BSE's own realised penalties are all of that type. Absence of a promoter has removed one failure mode and left the other untouched.
S6 IMPLICATION: An investor cannot underwrite this company by reading promoter behaviour, because the variable does not exist — the durability of the earnings stream turns instead on the regulator's continued licence and on the quality of the disclosure machinery, so the base and bear cases should be driven by regulatory events rather than by any assumption about controlling-shareholder alignment, and the monitorable is the quarterly shareholding pattern for any holder approaching a SECC cap.
SEVERITY: Medium

### FINDING: Seven chairpersons in nine years, two of them lasting under 300 days, at an institution whose only durable asset is institutional memory
S1 WHAT: Between FY2017 and FY2026 the chair of BSE's Governing Board changed seven times: Sudhakar Rao to 28-Jun-2017 [AR FY17, Board's Report, p34]; Dhirendra Swarup 31-Jul-2017 to 02-Nov-2017; S. Ravi 13-Nov-2017 to 04-Feb-2019 [AR FY18, Board's Report, p53]; [AR FY19, Board's Report, p28]; Justice Vikramajit Sen through FY2022 [AR FY22, Annexure A, p49]; S. S. Mundra to 16-Jan-2024; Pramod Agrawal 17-Jan-2024 to 08-Nov-2024 [AR FY24, CG Report, p81]; and Prof. Subhasis Chaudhuri from 21-Nov-2024 [AR FY25, CG Report, p75]. Over the same period the MD & CEO chair was empty from 25-Jul-2022 to 04-Jan-2023 [AR FY24, Consolidated Note, p296].
S2 WHY: Two mechanisms compound, and only one is BSE's doing. The structural one is the SECC tenure cap — Public Interest Directors serve an initial three years extendable once by three, and the Chairperson must be a PID [AR FY26, CG Report, p85, p78] — so the chair's clock is capped at six years and usually starts partway through a PID term, guaranteeing a short chairmanship. The behavioural one is mid-term departure to other public appointments: Pramod Agrawal resigned "due to potential conflict with new assignment" [AR FY25, CG Report, p76] and Nandkumar Saravade resigned with the identical stated reason a year later [AR FY26, CG Report, p80]. BSE recruits PIDs from the same pool of retired senior officials and jurists that government and regulators recruit from, so it loses them to better offers.
S3 EVIDENCE: Computed chairmanship lengths and their counter-proportion. Dhirendra Swarup: 31-Jul-2017 to 02-Nov-2017 = 31+30+31+2 = 94 days. Pramod Agrawal: 17-Jan-2024 to 08-Nov-2024 = 14+29+31+30+31+30+31+31+30+31+8 = 296 days. S. Ravi: 13-Nov-2017 to 04-Feb-2019 = 365+(17+31+31+4) = 448 days. So two of the seven chairs served under 300 days each while the SECC framework permits up to 2,190 days — 296 days is 13.5% of the permitted maximum. Two interregnums fall out of the same dates: 02–13 November 2017 (11 days) and 08–21 November 2024 (13 days), plus 163 days with no MD & CEO from 25-Jul-2022 to 04-Jan-2023 (6+31+30+31+30+31+4). Board tenure at 31-Mar-2026 averages (3.87+3.87+3.12+1.19+1.00+0.21) ÷ 6 = 2.21 years across the six PIDs, 36.8% of the six-year maximum [AR FY26, CG Report, p99], and the two longest-serving PIDs — the Chairperson and Justice Vazifdar — were appointed on the same day, 19 May 2022, and therefore exhaust their terms on the same day in May 2028.
S4 CONNECTS: Governance (the tenure and chair record), Business (BSE's product is counterparty and listing trust built over 150 years, [AR FY26, MD&A, p33]), Management commentary (the Board's Report's own recitation of appointments, cessations and resignations, [AR FY24, p21]; [AR FY25, p25]), and Industry (the SECC 3+3 cap applies identically to every Indian MII, so peers face the same churn). The compensating control is the mandatory seven-day annual director training programme plus a structured induction under SECC [AR FY26, CG Report, p80], and the fact that the executive spine — MD since 4 January 2023, CFO Deepak Goel, Company Secretary Vishal Bhat — has been stable [AR FY26, CG Report, p89]. The class of error training cannot catch: induction transfers *procedure*, not *judgement about precedent*. A chair who has been in the seat 296 days has not lived through a member default, a settlement failure or an enforcement cycle at this exchange, and that is the exact knowledge a chair is there to supply when one recurs.
DOMAINS: Governance, Business, MgmtCommentary, Industry
DISCONFIRM: Weighed against the churn: the board attends. In FY2026, five of eight directors recorded 8/8 board attendance, part-year directors were at 100% of eligible meetings, the lowest figure was the Non-Independent Director at 7/8, and every serving director attended the last AGM except one part-year PID [AR FY26, CG Report, p79–80]; PIDs met separately four times against a SECC minimum of two, with full attendance [AR FY26, CG Report, p86–87]. In FY2024, six of nine directors recorded 10/10 [AR FY24, CG Report, p80]. Both resignations were disclosed to NSE the same day with a stated reason and a pointer to the letter [BSE Ann 08-Nov-2024]; [BSE Ann 21-Aug-2025], and both departures were replacements-in-waiting rather than gaps — Chaudhuri was elevated 13 days after Agrawal left, and Rajiv Bansal and Santanu Paul joined within the following 14 months [AR FY26, CG Report, p99]. Neither resignation was in dispute and neither was accompanied by any disagreement over accounts.
S5 MEANS: The board that supervises India's oldest exchange is a body of engaged part-timers with a mean elapsed tenure of 2.21 years and a chair who statistically will not be there in two years, so its capacity to challenge a long-serving executive team on anything requiring institutional memory is structurally weak — and that weakness is a feature of the regulatory design, not a failure of the individuals.
BASE-RATE: No realised loss at BSE has been traced to chair turnover, and none is claimed — recorded explicitly as none found in the nine years of reports read. The nearest thing to a cost is timing: the SEBI inspection window of 1-Feb-2021 to 30-Sep-2022 that produced the ₹25 lakh order [AR FY26, CG Report, p95] and the Karvy supervision failure both sit in periods of board and executive transition, but the reports do not establish causation and this half does not assert it. The general base rate is that short board tenure raises the cost of challenging management rather than producing a discrete loss event, which is why this is graded Medium.
S6 IMPLICATION: This is a permanent structural discount on the quality of board challenge rather than an event risk, so the margin of safety demanded of any assumption that depends on the board restraining executive ambition — a large acquisition, a new product line, an aggressive capital deployment — should be wider here than at a company with a long-tenured board, and the monitorable with a date is May 2028, when the Chairperson and the second-longest-serving PID exhaust their SECC terms simultaneously.
SEVERITY: Medium

### FINDING: The auditor's investment-valuation Key Audit Matter shrank from 53.69% to 11.36% of standalone total assets in the year the balance sheet grew 51.5%
S1 WHAT: For FY2025 the statutory auditor's Key Audit Matter on investments covered "investments in various unlisted subsidiaries along with investments in associate, mutual funds, bonds and debentures of corporates" aggregating ₹2,66,476 lakh, expressly "approx. 53.69% of total assets of the Company as at March 31, 2025" [AR FY25, Auditor's Report, p220]. For FY2026 the same auditor's KAM is retitled "Valuation of investments in subsidiary and associate and its impairment" and covers only "investments in subsidiaries and associates carried at cost amounting to INR 85,469 lacs" [AR FY26, Auditor's Report, p241]. Mutual funds, bonds and debentures dropped out of the named scope.
S2 WHY: The stated reason is a re-framing around Ind AS 36 impairment of cost-carried investments rather than around fair-value estimation across the whole portfolio [AR FY26, Auditor's Report, p241]. That is defensible in itself — cost-carried subsidiary investments involve the most judgement — but it is a narrowing, not a re-labelling, and the annual report offers no explanation for why the fair-valued and amortised-cost instruments that carried a KAM for six consecutive years from FY2020 ceased to warrant one.
S3 EVIDENCE: The shape is in the two shares of the same population. FY2025: KAM-covered ₹2,66,476 lakh of standalone total assets ₹4,96,359 lakh = 53.69%, leaving 4,96,359 − 2,66,476 = ₹2,29,883 lakh, or 46.31%, outside the named KAM [AR FY25, Auditor's Report, p220]; [AR FY26, Standalone Balance Sheet, p249]. FY2026: KAM-covered ₹85,469 lakh of standalone total assets ₹7,52,207 lakh = 11.36%, leaving 7,52,207 − 85,469 = ₹6,66,738 lakh, or 88.64%, outside it [AR FY26, Auditor's Report, p241]; [AR FY26, Standalone Balance Sheet, p249]. So the named-scope share fell 42.3 percentage points while the balance sheet it sits on grew 7,52,207 ÷ 4,96,359 = 1.5154, or +51.5%. The audit fee moved the same way in relative terms: standalone statutory audit fee rose 78 ÷ 45 = +73.3% from FY2019 to FY2026 [AR FY19, Standalone Note, p276]; [AR FY26, Standalone Note, p287], while standalone revenue rose +690% — the fee fell from 45 ÷ 61,239 = 0.0735% of revenue to 78 ÷ 4,83,634 = 0.0161%, a decline of 78%.
S4 CONNECTS: Notes (the KAM text and its own asset-share arithmetic), the Balance Sheet (total assets of ₹7,52,207 lakh standalone), Governance (the Audit Committee's terms of reference expressly require it to "review and monitor the auditor's independence and performance, and effectiveness of audit process" and to approve the auditor's remuneration, [AR FY26, CG Report, p81]), and Management commentary (the Board's Report records only that the auditors "are not disqualified", [AR FY26, p28]). The compensating control is the Audit Committee, which met six times in FY2026 with three PIDs and one NID and near-perfect attendance [AR FY26, CG Report, p83]. The class of error it cannot catch: an audit committee reviews the audit that was performed, and a KAM is by construction a report on what the auditor chose to emphasise — neither mechanism surfaces the areas the auditor decided *not* to name, so a narrowing of scope produces no observable artefact anywhere in the annual report other than the KAM text itself.
DOMAINS: Governance, Notes, BalanceSheet, MgmtCommentary
DISCONFIRM: Substantial evidence cuts against reading this as a weakening audit. The opinion has been unmodified in every one of the nine years read, with a single emphasis of matter in FY2020 that was quantified at ₹1,264 lakh and did not recur [AR FY20, Auditor's Report, p238]. The IT-systems-and-controls KAM was retained in FY2026, so the number of KAMs did not fall. Non-audit fees are trivial and falling — "other services" of ₹2 lakh in FY2026, 2 ÷ 88 = 2.3% of the ₹88 lakh total paid to the auditor [AR FY26, Standalone Note, p287] — so there is no fee-dependence motive; group-wide fees to the auditor and its network actually declined from ₹116 lakh to ₹112 lakh [AR FY25, CG Report, p89]; [AR FY26, CG Report, p96]. CARO confirms no auditor resignation and the Board confirms no fraud was reported [AR FY25, CARO, p226]; [AR FY26, Board's Report, p28]. And the FY2025 KAM's own "53.69%" ties exactly to the balance sheet — 2,66,476 ÷ 4,96,359 = 53.69% — which is evidence of a careful audit, not a careless one.
S5 MEANS: The auditor's declared area of greatest judgement now covers barely a ninth of a balance sheet that has grown by half, so the annual report's own signal about where the numbers are softest has become materially less informative in exactly the year the numbers got bigger.
BASE-RATE: No realised loss has ever been traced to BSE's investment valuation: the opinion has been unmodified for nine consecutive years, no impairment has been the subject of a modification, emphasis of matter or CARO observation in any year read, and no restatement appears in any report examined — recorded explicitly as none found. The FY2020 emphasis of matter concerned a Core Settlement Guarantee Fund contribution of ₹1,264 lakh, not a valuation error [AR FY20, Auditor's Report, p238]. The finding is therefore about the informativeness of the disclosure, not about a demonstrated misstatement, and is graded accordingly.
S6 IMPLICATION: The annual report's built-in signal for where management judgement is concentrated now covers 11.36% of assets rather than 53.69%, so any assessment of asset quality must be reconstructed from the investment notes directly rather than inherited from the auditor's emphasis — and the two things worth watching on a named date are the FY2027 audit report, which is the final year of S.R. Batliboi's maximum ten-year term ending at the 22nd AGM in 2027, and whether the incoming firm restores a wider valuation KAM on the same assets.
SEVERITY: Medium

### FINDING: Dividend payout fell from 95.1% to 17.65% of standalone profit in four years while the "progressive" dividend policy was left unamended and no retention rationale was given
S1 WHAT: BSE's standalone payout ratio was 98.9% in FY2021 and 95.1% in FY2022; it is 17.65% in FY2026 [AR FY21, Board's Report, p24]; [AR FY22, Board's Report, p26]; [AR FY26, Board's Report, p24]. Across the same period the Dividend Distribution Policy has not been changed — the FY2026 annexure still carries the text adopted "with effect from Financial Year 2017-18", describing itself as a "progressive Policy" reflecting "the intent of the Company to maintain or grow the dividend each year" [AR FY26, Annexure E, p50], identical to the FY2019 text [AR FY19, Annexure A, p46]. Neither the FY2025 nor the FY2026 Board's Report gives any reason for retaining a materially larger share of profit.
S2 WHY: The mechanism is that the policy's test is stated in *dividend per share*, not in payout, so an explosion in earnings satisfies the policy's letter while gutting its economic substance. On a constant share base — adjusting for the March 2022 2:1 bonus and the May 2025 2:1 bonus — the declared dividend rose from ₹13.50 (FY22) to ₹15.00 (FY24) to ₹23.00 (FY25) to ₹30.00 equivalent (FY26, being ₹10 post-bonus on triple the shares) [AR FY22, p26]; [AR FY24, p19]; [AR FY25, p25]; [AR FY26, p24]. The policy said "maintain or grow", and the dividend grew. Nothing in the policy binds the payout ratio, so nothing was breached and nothing had to be explained.
S3 EVIDENCE: The two proportions of the same population move in opposite directions. Dividend per share on a constant base: 13.50 → 30.00 = +122.2% over four years. Standalone profit after tax over the identical window: ₹19,512 lakh (FY22) → ₹2,33,416 lakh (FY26) = +1,096.3% [AR FY22, Board's Report, p26]; [AR FY26, Board's Report, p23]. Payout consequently: 18,551 ÷ 19,512 = 95.1% (FY22); 20,599 ÷ 75,339 = 27.3% (FY24); 31,137 ÷ 1,11,245 = 28.0% (FY25); 41,198 ÷ 2,33,416 = 17.65% (FY26). The retained amount is where the asymmetry becomes visible: FY2022 retained 19,512 − 18,551 = ₹961 lakh; FY2026 retained 2,33,416 − 41,198 = ₹1,92,218 lakh, a 200-fold increase, and standalone total equity accordingly rose from ₹3,74,764 lakh to ₹5,76,653 lakh in a single year [AR FY26, Standalone Balance Sheet, p249]. Nothing was transferred to reserves by resolution — "The Company has not transferred any amount to the reserves during the year under review" [AR FY26, Board's Report, p24] — so the retention is simply accumulation.
S4 CONNECTS: Governance (the policy is a board document and a Reg. 43A disclosure obligation, [AR FY26, CG Report, p32]), the Income Statement (the payout arithmetic), the Balance Sheet (equity accumulation of ₹2,01,889 lakh in one year), and Management commentary (the Board's Report announces the dividend and gives no retention rationale, [AR FY26, p24]). The compensating control is the policy itself plus the Reg. 43A requirement to publish it. The class of error that cannot catch: Reg. 43A compels *publication* of a policy, not that the policy contain a payout band or that deviations from its spirit be explained — so a policy written in per-share terms in FY2017-18, when profits were flat, silently ceases to constrain anything once profits multiply elevenfold, and no disclosure rule is triggered.
DOMAINS: Governance, IncomeStatement, BalanceSheet, MgmtCommentary
DISCONFIRM: The wider record of treatment of minority capital is good and must be set against this. There has never been an ESOP — "The Company does not have any Employees Stock Option Plan (ESOP) Scheme for its employees" in every year read [AR FY22, Annexure, p49]; [AR FY26, Annexure A, p40] — and under SECC the MD is barred from stock options entirely [AR FY26, CG Report, p90], so no shareholder has ever been diluted by management compensation. There has been no preferential allotment or QIP in any year, Reg. 32(7A) reading "Not applicable" throughout [AR FY26, CG Report, p93]. Capital has been returned repeatedly and at scale: a tender buyback of 67,64,705 shares at ₹680 for ₹460 crore in FY2020 [AR FY20, Board's Report, p24], a tender buyback of 34,70,370 shares at ₹1,080 in FY2024 [AR FY24, Board's Report, p20], and an open-market buyback in FY2018 [AR FY18, Board's Report, p17]. Two 2:1 bonus issues were made, in March 2022 and May 2025 [AR FY22, p27]; [AR FY26, p24]. FY2025 included a ₹5 special dividend to mark the 150th year [AR FY25, Board's Report, p25]. This is not a company that mistreats minority holders; it is a company that stopped explaining one decision.
S5 MEANS: A company with no promoter, no controlling shareholder and no equity-linked management pay is now retaining more than four-fifths of its profit under a policy written for a different scale of earnings and without stating what the money is for, which converts a distribution question into an unmonitored capital-allocation question.
BASE-RATE: No loss has been realised from this at BSE and none is asserted: distributions have risen in absolute terms every year since FY2022, two buybacks and two bonus issues have been completed, and no dividend has been passed or cut in per-share terms in any year read — recorded explicitly as none found. The general base rate is that unexplained retention at a cash-generative company with no controlling owner is where value leaks slowly through acquisitions and non-core investment rather than through a discrete event, which is precisely why it belongs to the capital-allocation agent to test and to this half only to flag.
S6 IMPLICATION: The gap between a policy that promises progression and a payout that fell by more than three-quarters means the distribution assumption in any base case cannot be taken from the stated policy and must be derived from what is actually being retained — and the monitorable, with a date, is the FY2027 Board's Report: either the Dividend Distribution Policy is amended to state a payout band, or the retention is explained against a named use of funds, or the ₹1,92,218 lakh a year now being accumulated becomes the single largest unexamined capital-allocation decision at this company.
SEVERITY: Medium

### FINDING: Same-day disclosure on the exchange, selective aggregation in the annual report — and the contingent-liability grading disappeared in the year the claim rose
S1 WHAT: Every adverse event traceable in 477 NSE announcements across 2024–2026 was disclosed the same day it occurred, without a single exception found — the SEBI order of 25-Jun-2025 announced at 18:06 that evening [BSE Ann 25-Jun-2025], the CGST order of 17-Dec-2025 announced at 17:35 the same day [BSE Ann 17-Dec-2025], the ICCL order of 25-Feb-2025 announced at 22:43 the same night [BSE Ann 25-Feb-2025], the Chairperson's resignation of 08-Nov-2024 announced at 14:14 [BSE Ann 08-Nov-2024], and the Chief Regulatory Officer's departure announced the same day [BSE Ann 02-Jun-2026]. Yet three of those items never appear in any annual report: the ₹5.05 crore ICCL penalty reaches only a subsidiary annexure [AR FY25, ICCL Secretarial Audit, p45], the ACB Court, Mumbai order of March 2025 [BSE Ann 02-Mar-2025] appears in neither the FY2025 nor the FY2026 report, and BSE's own pending interoperability show-cause notice is absent from the FY2025 Corporate Governance Report [AR FY25, CG Report, p88]. Alongside this, the consolidated contingent-liability note dropped its "remote" grading in FY2026 [AR FY26, Consolidated Note, p227].
S2 WHY: Two different disclosure regimes with two different triggers. Reg. 30 intimation is event-driven, automatic and time-stamped, so it fires reliably. The annual report's governance tables are format-driven and entity-scoped — the CG table asks for actions "on the Company", the BRSR table applies a materiality filter, and the contingent-liability note follows Ind AS 37 disclosure with no requirement to grade probability. Where a format does not compel inclusion, the item does not survive the year-end aggregation, regardless of size.
S3 EVIDENCE: The disproportion is between prominence and amount, inside the same company's own filings. A ₹25 lakh SEBI penalty on BSE was disclosed in three places in FY2026 — CG Report [p95], BRSR monetary-penalty table [p124] and BSE's own secretarial audit [p43] — while a ₹5.05 crore penalty on the material subsidiary was disclosed in one place in FY2025 [p45]: the smaller item is 0.25 ÷ 5.05 = 4.95% of the larger and received three times the coverage. On contingent liabilities, FY2024 and FY2025 both told the reader what share of the claims management considered remote — ₹10,556 lakh of ₹10,557 lakh, and ₹10,504 lakh of ₹10,504 lakh, i.e. 99.99% and 100.00% [AR FY24, Note 37, p225]; [AR FY25, Note, p209] — while FY2026 grades 0% of a figure that rose to ₹13,567 lakh, an increase of 13,567 − 10,504 = ₹3,063 lakh or +29.2%, and indirect-tax matters simultaneously rose from ₹2,210 lakh to ₹5,930 lakh, +168.3% [AR FY26, Consolidated Note, p227]. Total ungraded contingent claims of 13,496 + 5,930 + 13,567 = ₹32,993 lakh are 13.3% of FY2026 consolidated PAT of ₹2,48,725 lakh.
S4 CONNECTS: Governance (which tables are populated), Notes (the contingent-liability grading and the subsidiary secretarial audits), Management commentary (the Board's Report and MD&A, which carry neither the ACB matter nor the ICCL penalty), and Business (BSE is itself the venue at which other issuers' Reg. 30 disclosures are policed, so its own aggregation standard is not a neutral matter). The compensating control is Reg. 24A, which forces the material subsidiary's secretarial audit into the annual report and is the sole reason the ₹5.05 crore penalty is findable at all [AR FY26, Board's Report, p32]. The class of error it cannot catch: Reg. 24A guarantees attachment, not integration — a reader who goes to the Corporate Governance Report and the BRSR, which is where penalties are meant to live, will not be redirected to page 45 of an annexure, and the BRSR will affirmatively tell them "Nil".
DOMAINS: Governance, Notes, MgmtCommentary, Business
DISCONFIRM: The evidence against a bad-faith reading is strong and was looked for. Disclosure to the exchange is genuinely immediate and covers items that reflect poorly on the company, including two director resignations, a Chief Regulatory Officer's departure and four adverse orders. The annual report also volunteers facts against interest: it discloses that BSE slipped from #7 to #8 by market capitalisation among global exchanges [AR FY26, MD&A, p57] and that exclusive OFS executions on its platform declined [AR FY26, MD&A, p59]. The FY2026 report discloses the CGST demand in full, quantified to the rupee at GST ₹6,59,26,901, penalty ₹65,92,690, total ₹7,25,19,591, together with the appeal date [AR FY26, BRSR, p124]. It reports zero data breaches and zero POSH complaints with the underlying counts [AR FY26, BRSR, p153]; [AR FY26, Board's Report, p32]. And no evidence was found anywhere in the 477 announcements of a late or suppressed disclosure. The failure is one of consolidation at year-end, not of candour in the moment.
S5 MEANS: BSE tells the market the truth immediately and tells the annual-report reader a tidier version, so the annual report cannot be treated as a complete record of this group's regulatory standing and the disclosure gap widens precisely where the item is largest or sits in a subsidiary.
BASE-RATE: No realised loss has followed from these disclosure gaps — no restatement, no qualification, no regulatory action against BSE for non-disclosure appears in any report or announcement read, and this is recorded explicitly as none found. What has been realised is the underlying penalties themselves: ₹5.30 crore paid across FY2025 and FY2026 [AR FY25, ICCL Secretarial Audit, p45]; [AR FY26, CG Report, p95]. The relevant base rate for the dropped contingent-liability grading is that BSE's own history contains no instance of a contingent claim crystallising into a material charge in the nine years read, which is why this is graded Medium rather than higher.
S6 IMPLICATION: Any assessment of this group's litigation and regulatory exposure must be built from the announcement stream and the subsidiary annexures rather than from the annual report's governance tables, which have now been demonstrated to omit the largest item and to have stopped grading the fastest-growing one — the concrete monitorable is the FY2027 contingent-liability note, specifically whether the "of which remote" line returns against claims that rose 29.2% in FY2026, and the FY2027 Corporate Governance Report, specifically whether subsidiary enforcement is consolidated into the parent's penalty table.
SEVERITY: Medium
