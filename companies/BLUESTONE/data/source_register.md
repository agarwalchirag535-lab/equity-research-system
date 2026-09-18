# 01 — Source register — BlueStone Jewellery and Lifestyle Limited

**Compiled:** 2026-09-09  ·  **As-of:** 2026-09-09

**Entity.** BlueStone Jewellery and Lifestyle Limited (formerly BlueStone Jewellery and Lifestyle Private
Limited). CIN `L72900KA2011PLC059678` · ISIN `INE304W01038` · NSE `BLUESTONE` · BSE scrip `544484`.
Registered office Bengaluru; corporate office Andheri East, Mumbai. Industry (BSE): Gems, Jewellery and
Watches / Consumer Durables. **Listing date 19-Aug-2025.**

**The governing constraint on this whole run.** The company has been listed for **thirteen months**.
Two annual reports exist, five quarters of results exist, five earnings calls have been held. There is
no ten-year series and there will not be one. `state/LOOP.md` §"THE NEW-LISTING ADJUSTMENT" records what
each standard test is re-pointed to. Nothing below is a substitute for history — it is the disclosure
that does exist, listed so that a later agent can tell the difference between *not disclosed* and
*not collected*.

---

## Tier 1 — the source of record

| # | Document | File | Pages | Basis | Channel |
|---|---|---|---|---|---|
| 1 | **Prospectus, 14-Aug-2025** (filed with RoC; supersedes the RHP) | `data/ipo/BLUESTONE-PROSPECTUS-2025.pdf` | 532 | Restated consolidated FY23/FY24/FY25 | Axis Capital (BRLM) |
| 2 | **Red Herring Prospectus, 04-Aug-2025** | `data/ipo/BLUESTONE-RHP-04Aug2025.pdf` | 532 | same | IIFL Capital (BRLM) |
| 3 | **Annual Report FY2026** (audited, first full year as a listed company) | `data/bronze/BLUESTONE-AR-FY2026.pdf` | 314 | Reported, Ind AS | NSE `annual-reports` |
| 4 | **Annual Report FY2025** (audited, covers the pre-listing year) | `data/bronze/BLUESTONE-AR-FY2025.pdf` | 230 | Reported, Ind AS | NSE `annual-reports` |
| 5 | Abridged Prospectus | `data/ipo/BLUESTONE-ABRIDGED-PROSPECTUS.pdf` | 8 | Restated | Axis Capital |

**Source-priority note (doctrine §5).** Where the Prospectus restated FY2025 and the FY2025 annual
report reported FY2025 disagree, **the annual report is the audited statutory account and outranks the
offer document**; the offer-document figure is used only to establish the basis on which the issue was
sold, and the difference between the two is itself a finding to be sized, never averaged away.

---

## Tier 2 — post-listing filings (119 PDFs collected, 2025-08-19 → 2026-09-03)

| Class | Count | Coverage | Why it is load-bearing here |
|---|---|---|---|
| **Earnings call transcripts** | **5** | Q1FY26 (11-Sep-25), Q2FY26 (12-Nov-25), Q3FY26 (29-Jan-26), Q4FY26 (29-Apr-26), Q1FY27 (28-Jul-26) | The entire promise-vs-delivery base. n=5, and the report says so |
| **Investor presentations** | 4 + 2 roadshow decks | Sep-25, Nov-25, Apr-26, Jun-26 (144p), Jul-26 | Management's claims. Marketing documents — never the source of an L1 |
| **Monitoring Agency Reports** | 4 | Q2FY26, Q3FY26, Q4FY26, Q1FY27 | **IPO proceeds vs stated objects.** This is the capital-allocation record for a company with no other |
| **Statements of Deviation** | 4 | same quarters | The company's own declaration of whether proceeds went where promised |
| **Quarterly results + board outcomes** | 17 | Jun-25 → Jun-26 (5 quarters + FY26 audited) | The only intra-year evidence |
| **Management commentary** | 2 | Nov-25, Jul-26 | Named claims, dated |
| **Press releases** | 3 | Sep-25, Nov-25, Jul-26 | |
| **Governance events** | — | Auditor change (14-Jan-26), director resignation (10-Mar-26), director resignation + cessation (30-Jun-26), CS appointment (02-Sep-26), credit rating (07-Aug-26) | A 13-month governance record in which five personnel/assurance events occurred |
| **ESOP allotments** | 6 | Jan-26, Feb-26, Mar-26, Jul-26, Aug-26, Sep-26 | Continuing dilution, post-listing |
| **Corporate action** | 2 | Investment into EtherealHouse (03-Feb-26, 06-Feb-26) | New venture / related-party test |
| **Promoter SAST 31(4)** | 1 | 24-Jun-26, Gaurav Singh Kushwaha | Encumbrance declaration. **Scanned — 50 bytes of text extracted; must be read as an image (GAP-002)** |
| Postal ballots + voting results + AGM proceedings | 6 | Sep-25 AGM, Jan-26 PB, Jun-26 PB | Dissent is a governance signal |

Index of all 119 with subject lines and page counts: `data/index/filing_index.json`.
Text: `data/quarterly_text/` (one `.txt` per filing, page-marked).

## Tier 3 — ownership and market

| Item | Held | Note |
|---|---|---|
| Shareholding pattern XBRL | **5 quarters** — 18-Aug-25 (listing), 30-Sep-25, 31-Dec-25, 31-Mar-26, 30-Jun-26 | `data/filings/SHP_*.xml`. Promoter & group **16.36% → 16.25%**; public 83.64% → 83.75% |
| Insider trading (PIT) filings | Aug-25 → Sep-26 | `data/filings/insider.json` |
| Board meetings | full | `data/filings/board_meetings.json` |
| Corporate announcements | 142 rows | `data/filings/announcements_2025.json`, `_2026.json` |
| IPO bid detail | full | `data/ipo/nse_ipo_detail.json` — QIB 0.93x, NII 0.34x at NSE |
| Live quote | LTP ₹856.35 (09-Sep-2026) | BSE `getScripHeaderData` |

## Tier 4 — peers (FY2026 basis, all March year-end)

| Peer | Why in the set | Held |
|---|---|---|
| **Titan Company** | Owns **CaratLane** — the single closest comparable to BlueStone (online-first, studded-led, same customer) and separately disclosed inside Titan's filings | FY2026 (473p), FY2025 |
| **Kalyan Jewellers India** | Largest listed pure-play growth retailer; franchise-led expansion | FY2026 (145p), FY2025 (146p) |
| **Senco Gold** | Closest by revenue scale; east-India retail | FY2026 (377p), FY2025 (357p) |
| **PN Gadgil Jewellers** | Listed Sep-2024 — a **recent-listing base rate** as well as a peer | FY2026 (118p), FY2025 (114p) |
| Thangamayil Jewellery | South-India comparator | FY2025 |

---

## Gaps at collection (carried to `records/gap_register.md`)

- **GAP-001 — no pre-FY2023 history of any kind.** The Prospectus restates FY23/FY24/FY25 only. FY22 and
  earlier are not obtainable from any statutory channel. *Any statement about BlueStone before FY2023 is
  outside the evidence base of this report.*
- **GAP-002 — promoter SAST Reg 31(4) filing of 24-Jun-2026 is a scanned image**; 50 bytes of text
  extracted from 2 pages. Encumbrance status must be read from the image or from the AR FY2026
  disclosure. Not treated as "no encumbrance" until read.
- **GAP-003 — bulk/block deal feed not captured programmatically.** NSE `historical/bulk-deals` returned
  HTTP 503 and the BSE API redirected. Deal-level data seen in the BSE section inventory
  (09-Jun-2026: IVYCAP sell 26,04,023 @ ₹524.97; Nippon India MF buy 25,00,000 @ ₹522.05; 360 ONE sell
  10,55,074 @ ₹522.20; Accel India III Mauritius sell 9,76,964 @ ₹522.08) is `SECONDARY` until
  reconciled against the shareholding pattern XBRLs, which **are** held. W2_exits reconciles them.
- **GAP-004 — no credit rating rationale collected**, only the company's intimation of a new rating
  (07-Aug-2026). The rating agency's rationale (which would disclose debt structure and covenants) is a
  separate channel not yet tried.

**Nothing in this run may be written from a document not listed above.**
