# Quarterly consolidated series — BSE Limited

Ten consecutive quarters, Mar-2024 → Jun-2026, read from the consolidated results filings
(`data/quarterly/BSE-Q-*.pdf`). Column 0 of each statement is the current quarter; the column count is
derived from the modal amounts-per-line in each filing (they carry 4, 5 or 6 columns depending on
whether year-to-date and prior-FY columns are present) — never assumed.

**Nobody in the wave graph owns this series.** It is built to support W4 (the ₹100 map), W5 (earnings
quality) and W8 (valuation), none of which had quarterly granularity.

| Quarter ended | Revenue from ops | Regulatory contribution | Clearing & settlement | PBT |
|---|---|---|---|---|
| Mar-2024 | 48,837 | — | 6,372 | 15,393 |
| Jun-2024 | 60,770 | — | 8,055 | 34,937 |
| Sep-2024 | 74,632 | 11,267 | 10,072 | 45,670 |
| Dec-2024 | 77,354 | 9,823 | 8,249 | 28,798 |
| Mar-2025 | 84,664 | — | — | 65,910 |
| Jun-2025 | 95,839 | 11,626 | 5,550 | 70,140 |
| Sep-2025 | 1,06,839 | 14,669 | 6,327 | 73,896 |
| Dec-2025 | 1,24,410 | 18,702 | 7,433 | 79,533 |
| Mar-2026 | 1,56,351 | 19,972 | 8,725 | 1,06,345 |
| **Jun-2026** | **1,56,602** | 19,278 | 9,028 | 1,16,366 |

₹ lakh. Blanks are lines this filing's text extraction damaged; they are flagged in the extractor
output and left empty rather than guessed. `records/quarterly_series.csv` carries the machine copy.

## The observation this series exists to surface

**Sequential revenue growth stopped in Jun-2026.**
`1,56,602 − 1,56,351 = 251`, i.e. **+0.16% quarter-on-quarter**, after nine quarters averaging well
into double digits. The annual accounts cannot show this: FY2026 closed 31-Mar-2026 at the top of the
run, so the FY2026 annual report — the source of record for every other wave — **ends one quarter before
the first stall in the series**.

Year-on-year the quarter is still strong (`1,56,602 / 95,839 = +63.4%`), which is how it will be
presented. The sequential flattening is only visible by putting the filings side by side.

**This is a monitorable, not a finding, and it is one quarter.** One flat quarter is not a trend, and
Q1 is seasonally distinct. What makes it worth carrying into W8 is the concentration: ~70% of revenue is
one product whose activity depends on a regulator-set expiry calendar (RF-020), and W2_industry measured
BSE's premium share falling to 32.4% in June 2026 — the same quarter — **solely because NSE had an extra
weekly expiry**. Two independent observations of the same month.

## Cost behaviour across the same window

Clearing and settlement: `5,550 (Jun-2025) → 9,028 (Jun-2026) = +62.7%` against revenue `+63.4%`.
The line now tracks revenue almost exactly. That is worth putting against RF-025: the FY2026 *annual*
consolidated clearing line **fell** 19.4%, and W1_ledger established 81.2% of that fall was an
intra-group elimination rather than lower external cost. On a quarterly basis the underlying cost is
rising in line with activity, which is consistent with the elimination explanation and inconsistent with
the MD&A's "structural efficiency".

Regulatory contribution: `11,626 (Jun-2025) → 19,278 (Jun-2026) = +65.8%`, marginally faster than
revenue — consistent with RF-030, the levy running on notional while revenue runs on premium.

## Method note
Two parsing traps were hit and fixed rather than worked around: statement labels carry formula groups
(`(1+2+3)`, `(8+9)`, `(5a to 5f)`, `(refer note 6)`) whose digits parse as amounts, and amounts below
₹1,000 carry no thousands separator so they are indistinguishable from line indices unless the label is
stripped first. Both are handled; 44 genuinely OCR-damaged lines remain flagged and empty.
