# Cash-flow ledger — BSE Limited

> **SUPERSEDED IN PART, 2026-09-07.** The float **is** separable — see `waves/W1_ledger.md` §2 and
> RF-005. Own-account CFO/PAT is **0.942 cumulative over FY2024–FY2026**, against 1.393 on the headline.
> **Do not quote the 1.264 below.** It is arithmetically 1.269 after the cell corrections, and it is the
> wrong measure regardless. The warning attached to it was right in substance but wrong in its reason:
> the disclosure to separate the float existed in Notes 11, 12 and 16 all along.

## The series (consolidated, ₹ lakh)

| FY | PAT attributable | CFO | CFO/PAT | CFI | CFF | Total equity |
|---|---|---|---|---|---|---|
| FY2016 | 13,293 | — | — | 16,385 | −11,968 | 2,74,299 |
| FY2017 | 22,057 | 77,450 | 3.51 | 9,467 | −8,436 | 2,76,020 |
| FY2018 | 71,128 | −27,147 | −0.38 | −23,604 | −22,272 | 3,13,435 |
| FY2019 | 19,417 | −31,805 | −1.64 | 34,712 | −35,201 | 2,93,569 |
| FY2020 | 12,227 | 39,671 | 3.24 | 47,029 | −61,777 | 2,44,366 |
| FY2021 | 14,490 | −6,787 | −0.47 | −18,939 | −5,525 | 2,51,593 |
| FY2022 | 25,433 | 1,44,175 | 5.67 | −97,990 | 894 | 2,78,971 |
| FY2023 | 22,067 | −13,711 | −0.62 | −11,133 | −18,551 | 2,82,899 |
| FY2024 | 77,839 | 2,84,203 | 3.65 | −1,07,145 | −14,905 | 3,45,466 |
| FY2025 | 1,32,589 | 41,015 | 0.31 | −76,723 | −20,599 | 4,57,570 |
| FY2026 | 2,49,698 | 3,10,368 | 1.24 | −2,73,967 | −30,370 | 6,79,550 |

Provenance per cell in `trend_provenance.json`; each year read from that year's own AR consolidated
cash flow statement at the PDF page recorded there.

**Cumulative, 10 years with both figures (DERIVED, arithmetic shown):**
`cumulative CFO 8,17,432 / cumulative PAT attributable 6,46,945 = 1.264`

## WARNING — do not quote 1.264 as a cash-conversion ratio without this

**Headline CFO is not a clean measure of own-account cash generation for an exchange-and-clearing
group.** BSE consolidates Indian Clearing Corporation Limited. Settlement obligations, margin money and
member deposits move through the group's cash and working capital, and those balances are **not the
company's money** — they are held on behalf of members. Movements in them flow through CFO.

The evidence that this is happening, not merely possible:

- Year-to-year CFO/PAT ranges from **−1.64 to +5.67** across the ten years. No operating business with
  this P&L stability produces that. The swing is a balance-sheet float, not trading performance.
- CFO is **negative in four of ten years** (FY2018, FY2019, FY2021, FY2023) in years when PAT
  attributable was positive in all four.
- Current "Other financial liabilities" stands at **4,06,419 lakh** at FY2026 against total equity of
  6,79,550 `[AR FY2026, Consolidated Balance Sheet, PDF p163]` — a liability pool 60% the size of
  equity sitting in current liabilities.

**Required before W4 uses any conversion ratio:** separate own-account CFO from settlement/member float
by reading the cash flow statement's working-capital lines and the note behind "Other financial
liabilities". If the split is not disclosed, the L7 state is
`NOT-DISCLOSED -> AR FY2026 note to Other financial liabilities`, and the honest output is that
cash conversion **cannot be measured** from the face of the statement — which is itself a finding, not a
gap to paper over with the 1.264.

## Also for W4

- **FY2026 CFI −2,73,967 against CFO +3,10,368.** Nearly all operating cash went into investing. What
  was bought — investment book, or capacity? Chain it.
- **`capex_ppe` captured nothing in any year** — the label in these cash flow statements differs from
  the patterns tried. W4 must read the investing section directly rather than trusting this row's
  absence. An absent row here is a fact about the extractor, not about capex.
- **CFF is negative in ten of eleven years**, deepening to −30,370 in FY2026 — consistent with dividends
  and buyback rather than external funding. Confirm against the financing section.
