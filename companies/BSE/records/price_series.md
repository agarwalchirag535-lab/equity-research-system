# Price series — BSE Limited

**Source: NSE's own daily bhavcopy archive**, `nsearchives.nseindia.com/content/cm/BhavCopy_NSE_CM_0_0_0_<YYYYMMDD>_F_0000.csv.zip`.
A primary source — the exchange's own file — so no `[SECONDARY: …]` limitation applies (doctrine §1a-iii).
25 month-end observations, Sep-2024 → 4-Sep-2026. Machine copy: `price_series.csv`.

**Channel note.** NSE's `api/quote-equity` returns **HTTP 403** with a primed cookie and browser headers.
The static archive does not. Separately, **`urllib` is blocked on this host where `curl` is not** — the
same URL returns the file via curl and nothing via urllib. Both are facts about channels, not about data.

## THE TRAP IN THIS SERIES — read before using any pre-May-2025 price

**A 2:1 bonus took effect between the 30-Apr-2025 and 30-May-2025 observations.** The raw series shows
`6,359.00 → 2,674.00`, a 58% one-month fall that is **not a price move**. The share count went
13,53,76,359 → 40,61,29,077, i.e. **×3** `[AR FY26, PDF p24]`.

Every observation before 2025-05-01 is therefore divided by 3 in the `close_bonus_adj` column. **Any
comparison, return or chart crossing that date on raw closes is wrong**, and wrong by a factor of three.

## Month-end closes (₹)

| Date | Raw | Bonus-adjusted | | Date | Raw | Bonus-adjusted |
|---|---|---|---|---|---|---|
| 2024-09-30 | 3,684.65 | **1,228.22** | | 2025-09-30 | 2,040.20 | 2,040.20 |
| 2024-10-31 | 4,465.60 | 1,488.53 | | 2025-10-31 | 2,479.00 | 2,479.00 |
| 2024-11-29 | 4,670.75 | 1,556.92 | | 2025-11-28 | 2,902.40 | 2,902.40 |
| 2024-12-31 | 5,325.40 | 1,775.13 | | 2025-12-31 | 2,632.20 | 2,632.20 |
| 2025-01-31 | 5,305.95 | 1,768.65 | | 2026-01-30 | 2,797.00 | 2,797.00 |
| 2025-02-28 | 4,633.70 | 1,544.57 | | 2026-02-27 | 2,707.10 | 2,707.10 |
| 2025-03-28 | 5,479.80 | 1,826.60 | | 2026-03-30 | 2,683.50 | 2,683.50 |
| 2025-04-30 | 6,359.00 | 2,119.67 | | 2026-04-30 | 3,640.50 | 3,640.50 |
| **bonus ×3** | | | | 2026-05-29 | 4,146.10 | **4,146.10** ← peak |
| 2025-05-30 | 2,674.00 | 2,674.00 | | 2026-06-30 | 3,865.60 | 3,865.60 |
| 2025-06-30 | 2,770.10 | 2,770.10 | | 2026-07-31 | 3,646.20 | 3,646.20 |
| 2025-07-31 | 2,427.40 | 2,427.40 | | 2026-08-31 | 3,282.00 | 3,282.00 |
| 2025-08-29 | 2,096.20 | 2,096.20 | | **2026-09-04** | **3,409.80** | **3,409.80** |

## What the series says (DERIVED, arithmetic shown)

- Two-year bonus-adjusted move: `3,409.80 ÷ 1,228.22 − 1 = +177.6%`
- From the May-2026 peak: `3,409.80 ÷ 4,146.10 − 1 = −17.8%`
- Market capitalisation at 4-Sep-2026: `3,409.80 × 40,78,84,077 = ₹1.391 lakh crore`
- Trailing P/E on consolidated FY2026 EPS ₹61.22: `3,409.80 ÷ 61.22 = 55.7×`
- Trailing P/E on the standalone EPS management reports (₹56.27): `3,409.80 ÷ 56.27 = 60.6×`

## Three things W8 must not do with this

1. **Do not present a trailing multiple without the stall.** Both P/Es are struck on FY2026 earnings that
   closed 31-Mar-2026 — the top of the run. `quarterly_series.md` shows Jun-2026 revenue **+0.16% QoQ**
   after nine strong quarters. The multiple is on a base whose sequential growth has already stopped.
2. **Do not read the drawdown as the market pricing the findings in.** The −17.8% from peak coincides
   with the June-2026 quarter in which W2_industry measured BSE's premium share falling to 32.4%
   **solely because NSE had an extra weekly expiry** (RF-020). That is a plausible alternative
   explanation, and no causal claim is supported either way.
3. **Do not compute a beta, correlation or index-relative return from this file.** It is month-end
   closes only, and the index-comparison chart BSE itself used to publish was withdrawn after FY2024
   (RF-032) — so the company's own basis for that comparison no longer exists.
