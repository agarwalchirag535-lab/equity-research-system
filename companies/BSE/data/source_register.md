# 01 — Source register — BSE Limited

**Compiled:** 2026-09-07  ·  **As-of:** 2026-09-07

**Entity.** BSE Limited. Listed on **NSE only** (symbol `BSE`) — an exchange cannot list on itself, so
BSE Ltd has no BSE scrip code for its own equity and files its corporate disclosures with NSE.
*(Scrip 543066, initially assumed, is SBI Cards and Payment Services — not this company.)*

## Annual reports held (audited, source of record)

| FY | File | Size | Pages | Audited |
|---|---|---|---|---|
| 2017.p | `BSE-AR-FY2017.pdf` | 15.0 MB | 284 | yes |
| 2018.p | `BSE-AR-FY2018.pdf` | 66.9 MB | 289 | yes |
| 2019.p | `BSE-AR-FY2019.pdf` | 8.6 MB | 313 | yes |
| 2020.p | `BSE-AR-FY2020.pdf` | 28.9 MB | 317 | yes |
| 2021.p | `BSE-AR-FY2021.pdf` | 2.5 MB | 293 | yes |
| 2022.p | `BSE-AR-FY2022.pdf` | 58.2 MB | 305 | yes |
| 2024.p | `BSE-AR-FY2024.pdf` | 25.0 MB | 316 | yes |
| 2025.p | `BSE-AR-FY2025.pdf` | 31.5 MB | 283 | yes |
| 2026.p | `BSE-AR-FY2026.pdf` | 14.6 MB | 317 | yes |

**9 annual reports, 2,717 pages.** Channel: NSE `/api/annual-reports?index=equities&symbol=BSE`,
files from `nsearchives.nseindia.com/annual_reports/`.

**Format-boundary note.** The implementation repo records "every AR through FY2023 is a ZIP, FY2024+ a bare
PDF". **That does not hold here:** FY2022 was served with a `.zip` extension but is a bare PDF
(magic `25504446`). A reader keying on file extension loses it. FY2017–FY2021 were genuine ZIPs.

## Not yet collected

Concall transcripts, investor presentations, quarterly results, shareholding patterns and RPT filings
are pending — they are wave-2 inputs, not wave-1 blockers.

---

## Supplementary filings collected (2026-09-07)

| Class | Count | Coverage | Channel |
|---|---|---|---|
| Concall transcripts | 11 | Feb-2024 → Aug-2026 | NSE corporate announcements |
| Investor presentations | 4 | Nov-2024 → Nov-2025 | same |
| Quarterly results + board outcomes + analyst decks | 32 | Feb-2024 → Aug-2026 | same |
| Shareholding pattern | 22 quarters | Sep-2021 → Jun-2026 | NSE `corporate-share-holdings-master` |
| Corporate announcements | 477 | 2024 → Sep-2026 | NSE `corporate-announcements` |

All extracted to text: `data/concall_text/`, `data/quarterly_text/`.

The Q3FY26 results filing (09-Feb-2026) and its analyst deck were collected specifically to close two
contradictions W2_promise could not settle from transcripts alone.

## Peer documents

| Peer | Reports | Held |
|---|---|---|
| CDSL — Central Depository Services (India) Ltd | 9 on NSE | FY2025, FY2026 |
| IEX — Indian Energy Exchange Ltd | 9 on NSE | FY2025, FY2026 |
| MCX — Multi Commodity Exchange | **0 rows** | — |

**MCX channel finding, recorded per the standing rule rather than as a fact about the company.**
`/api/annual-reports?index=equities&symbol=MCX` returned `{"data":[]}` with HTTP 200, and the zero was
**retried once** on a fresh session cookie with the same result. MCX is a listed company that must
publish an annual report under SEBI LODR Reg 46, so the correct statement is:

> *MCX annual reports are not available in NSE's `annual-reports` equities family; they are obtainable
> from another channel not yet tried (BSE's `AnnualReport_New` API, or MCX's own investor-relations
> site).*

Not *"MCX has no data"*. W2_peers should try those channels before treating MCX as unavailable.
