# Capital structure — BSE Limited (valuation inputs for W8)

| Item | Value | Source |
|---|---|---|
| Paid-up equity share capital at 31-Mar-2026 | ₹81,57,68,154 | [AR FY26, PDF p24] |
| Shares outstanding at 31-Mar-2026 | **40,78,84,077** of ₹2 face value | same |
| Prior capital | ₹27,07,52,718 = 13,53,76,359 shares | same |
| Bonus issue | **2:1** — two bonus shares for every one held | same |
| Post-bonus count | 13,53,76,359 → 40,61,29,077 | same |
| Further issue | +17,55,000 to 10 trading members of erstwhile BSE | same |
| Shares at 30-Jun-2025 | 40,61,29,077 (capital ₹8,123 lakh) | [AR FY26, PDF p216] |
| Demat holding | 99.98% | [AR FY26, CG Report, PDF p92/pr81] |
| Listed on | **NSE only**, symbol `BSE`, ISIN INE118H01025 | same |

**DERIVED, arithmetic shown:**
- Bonus check: `13,53,76,359 × 3 = 40,61,29,077` ✓ — a 2:1 bonus trebles the count.
- Consolidated EPS FY2026: **₹60.61**, not ₹61.22.

> **CORRECTED 2026-09-08 by W4_belowline.** EPS is struck on **issued** capital of **41,19,79,077**
> shares, not the paid-up **40,78,84,077**. The **40,95,000-share gap is 2005 demutualisation shares
> held in abeyance** — issued but not paid up. My ₹61.22 used the paid-up count.
> `2,49,698 lakh ÷ 41,19,79,077 = ₹60.61`.
  Management reports standalone basic & diluted EPS of **₹56.27** (bonus-adjusted)
  `[AR FY26, MD&A, PDF p75/pr64]`; the difference is standalone-vs-consolidated **and** weighted-average
  versus closing share count. **W8 must state which basis it uses.**

## Market price — OBTAINED, from the exchange's own archive

**Resolved 2026-09-08.** NSE's `api/quote-equity` returns **HTTP 403** on every attempt, primed cookie
and browser headers included. But the **static bhavcopy archive is not blocked**:
`nsearchives.nseindia.com/content/cm/BhavCopy_NSE_CM_0_0_0_<YYYYMMDD>_F_0000.csv.zip`.

That is a **primary source — the exchange's own daily file**, not a data vendor, so it carries no
`[SECONDARY: …]` limitation under doctrine §1a-iii.

| Field | Value |
|---|---|
| Trade date | **2026-09-04** (most recent file available) |
| Close | **₹3,409.80** |
| High / Low | 3,474.00 / 3,391.70 |
| Previous close | 3,306.10 |
| Volume | 79,75,058 shares |
| Turnover | ₹2,739.58 cr |
| ISIN | INE118H01025 — **matches the annual report** |

`[NSE Bhavcopy, 2026-09-04, BhavCopy_NSE_CM_0_0_0_20260904_F_0000.csv]`

**DERIVED, arithmetic shown:**
- Market capitalisation: `₹3,409.80 × 40,78,84,077 = ₹13,90,80 crore` — i.e. **₹1.39 lakh crore**
  (`3,409.80 × 407,884,077 = 1,390,796,...` ≈ ₹1.391 × 10^12).
- P/E on consolidated FY2026 EPS of ₹61.22: `3,409.80 ÷ 61.22 = 55.7×`
- P/E on the standalone EPS management reports (₹56.27): `3,409.80 ÷ 56.27 = 60.6×`

> **And that ₹56.27 is itself internally inconsistent** (W4_belowline). Standalone Note 30's "before
> exceptional items (net of tax)" EPS — **the figure the Board's Report leads with** — deducts the
> **pre-tax** 1,590 while the profit row directly above it deducts the **net-of-tax** 1,341.
> Recomputed: `2,32,075 ÷ 41,19,79,077 = ₹56.33`, not ₹56.27.

**Both multiples are struck on FY2026 earnings that ended 31-Mar-2026** — before the sequential revenue
stall recorded in `quarterly_series.md` (Jun-2026 revenue +0.16% QoQ). W8 must not present a trailing
multiple without that.

A month-end series back to Sep-2024 is being built into `records/price_series.csv` from the same archive.

## The annual report cannot substitute for this

The market price table was removed from the annual report after FY2024 — see **RF-032**. The last month-wise high/low/volume series BSE published for its own shares covers
**April 2023 to March 2024** `[AR FY2024, CG Report, PDF p92/pr86]`, ending 29 months before today.

**Consequence for W8 — now removed.** With a primary-source price in hand, the valuation section can
state both what the fundamentals imply **and** what the price implies, which doctrine §1c permits as an
S6 statement. The constraint recorded here earlier no longer binds.
