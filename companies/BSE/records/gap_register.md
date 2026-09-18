# Gap register — BSE Limited

> **GAP-001 CLOSED 2026-09-08.** The FY2023 annual report has been obtained — 317 pages, complete with
> auditor's report, all statements, notes, corporate governance report and MD&A. See the closure note
> below. The corpus is now **10 of 10 years, FY2017–FY2026, with no missing year.**

Per doctrine §9, this is a **section of the final report**, not an internal note. What a company or a
channel does not make available is part of the case.

## GAP-001 — FY2023 annual report not obtained

**What is missing.** The full FY2022-23 annual report: its notes to accounts, MD&A, board's report,
corporate governance report and related-party disclosures.

**Channel, not company.** Every channel tried, and what each returned:

| Channel | Result |
|---|---|
| NSE `/api/annual-reports?index=equities&symbol=BSE` | 200, 9 rows, **FY2023 absent from the index** (FY2017-22, FY2024-26 present) |
| BSE `api/AnnualReport_New/w?scripcode=543066` | 200 — but 543066 is **SBI Cards**, not BSE Ltd. BSE Ltd has no BSE scrip for its own equity |
| `bseindia.com/bseplus/AnnualReport/...` patterns | 404 |
| `bseindia.com/investor_relations/annualreport.html` | 301 → 200 returning the **14,287-byte Angular shell**; content is JS-loaded, no HTML links |
| Web search → two candidate corpfiling PDFs | **Both were other companies** (GPIL scrip 542857; Weizmann Ltd). Discarded on first-page verification |

**Impact, bounded.** FY2023 *statements* are recoverable as the comparative column of the FY2024 annual
report, so the 10-year trend lines can be completed. What is genuinely lost is FY2023's own notes, MD&A,
governance report and RPT schedule — i.e. one year of L2/L4/L5 depth, not the L1 series.

**What would close it.** BSE Ltd's investor-relations API behind the Angular page, or the FY2023 AR
filed as an NSE corporate announcement around July 2023.

**Status: CLOSED 2026-09-08.**

**How it was closed, and why it was missed.** The FY2023 annual report was filed on **07-Aug-2023 as an
attachment to the Notice of the Eighteenth Annual General Meeting**, under the announcement category
*"Shareholders meeting"* — not as an annual-report filing. It is therefore **absent from NSE's
`/api/annual-reports` index entirely**, which is why six separate channels returned nothing.

File: `BSE_07082023160115_NSEIntimationAnnualreport.pdf`, 11.1 MB, **317 pages**, saved as
`data/bronze/BSE-AR-FY2023.pdf`. Verified to contain the Independent Auditor's Report, Balance Sheet,
Notes, Corporate Governance Report and MD&A — not merely a covering letter.

**The lesson, and it generalises.** Every earlier probe asked *"is there an annual report in the annual
report index?"* The answer was correctly no. The right question was *"has the annual report been filed
at all, under any category?"* — and it had been, under a heading about a shareholders' meeting. This is
the standing rule in practice: **a zero from a channel is a fact about the channel, never about the
document.** Six channels returning nothing did not make the document absent; it made six channels the
wrong place to look.

**Consequences now reversed:**
- The 10-year trend lines no longer bridge a hole — FY2023 was previously recoverable only as FY2024's
  comparative column, i.e. on the restated basis only. The as-first-reported FY2023 figures are now
  available from the company's own FY2023 accounts.
- FY2023's own notes, MD&A, governance report and RPT schedule — one full year of L2/L4/L5 depth
  previously written off — are now readable.
- Every chain link marked `NOT-DISCLOSED -> FY2023 AR, not obtained (GAP-001)` should be revisited.
