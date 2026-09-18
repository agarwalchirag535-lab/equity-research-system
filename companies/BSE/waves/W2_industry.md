# W2 — Industry & value chain: BSE Limited

Wave-2 artifact under `ANALYSIS_DOCTRINE.md` §7, executed against the MII overlay
(`waves/W1.7_mii_overlay.md` §1, §4, §6). **Scope: the structure the numbers sit inside.** BSE's own
financial statements are W3's; figures below appear only as evidence for a structural claim, and every
one carries a tag. Page cites use the verified offsets in `waves/W1_docmap.md` §0.1
(FY17 +2 · FY18 +7 · FY19 +9 · FY20 +7 · FY21 +5 · FY22 +9 · FY24 +6 · FY25 +11 · FY26 +11).

External figures are tagged `[SECONDARY: …]`. Per doctrine §1a-iii no SECONDARY-sourced step alone
carries a conclusion; every SECONDARY figure used below is paired with a primary corroborant, and where
it is not, the step is marked as unable to carry weight.

---

## 0. The answer, first

**The overlay's hypothesis is right about the rate and wrong about the share.**

Pricing power in this chain splits into two different powers, and they sit in two different places:

| Power | Who holds it | Evidence |
|---|---|---|
| **The rate** — what may be charged, on what base, and retrospectively | **SEBI, near-absolutely.** Charge structure (true-to-label), the fee base (notional vs premium), lot size, expiry-day allocation, position limits, product eligibility. Plus **RBI** and **the Finance Ministry (STT)**, neither of which the overlay named | §3 timeline; F1, F3 |
| **The share** — how much activity comes to which venue | **Contestable, and it moved.** Not SEBI's and not permanently NSE's | §2; F2 |

BSE does not set its own prices in any segment that matters. It does not choose its expiry day, its lot
size, the base its largest single cost is levied on, or whether a segment continues to exist. In the
last three years the regulator has (i) re-based BSE's largest levy retrospectively to FY2007 with 15%
interest, (ii) extinguished two of BSE's segments outright, and (iii) reallocated the expiry-day
calendar three times.

But the naive form of the hypothesis — *"the regulator holds the power, so exchange outcomes are
regulator-determined"* — is falsified by FY2026 itself. **BSE and NSE faced identical rules and moved in
opposite directions**: NSE's consolidated total income fell 2.4% and its PAT fell 15.5%
`[SECONDARY: NSE Q4FY26 press release as reported, 2026-05-05]`, while BSE's consolidated total income
rose 59.1% to ₹5,14,810 lakh and PAT attributable rose 88.3% to ₹2,49,698 lakh
`[AR FY26, consolidated P&L, PDF p164/pr153; records/trend_10y.csv]`. The regulator sets the price of a
unit of activity; it does not decide whose venue the unit occurs on.

**Where BSE actually holds pricing power: nowhere on transaction charges, and on exactly one asset —
the index.** BSE bought out S&P Dow Jones' 50% of Asia Index Private Limited for ₹3,001 lakh effective
1 June 2024 `[AR FY25, Board's Report, PDF p24/pr13 and PDF p200/pr189]`. That subsidiary earned a PBT
margin of 82.9% in FY2026 (₹32.13 cr on ₹38.76 cr) `[AR FY26, MD&A, PDF p63/pr52]` — the highest-margin
node in the entire chain, and 0.87% of standalone revenue from operations.

---

## 1. The value chain, node by node

The overlay's §1 established that BSE earns *"a toll on activity it does not own."* This section
establishes **who owns each step, who captures the economics, and who can change the split.**

### 1.1 The map

```
INVESTOR  →  BROKER / TRADING MEMBER  →  EXCHANGE  →  CLEARING CORP  →  DEPOSITORY  →  SETTLEMENT
  |               |                        |              |                 |             |
  |          brokerage +               transaction    clearing fee +    demat/txn      bank leg
  |          float on client           charge         float on            charges
  |          funds                                    margin
  |
  +--> pays, on every trade, in this order:
       brokerage  ·  exchange transaction charge  ·  clearing charge  ·  depository charge
       ·  SEBI turnover fee  ·  STT  ·  stamp duty  ·  GST
```

### 1.2 Who captures what, and who can change it

| Node | Who is it, for BSE | What BSE captures | Who can change the split |
|---|---|---|---|
| **Investor** | 24 crore+ registered investor accounts on BSE `[Q3FY26 Concall, MD&CEO]` | nothing directly | — |
| **Broker / trading member** | ~610 members regularly trading Sensex options; ~650 FPIs `[Q1FY27 Concall, MD&CEO]`; 1,190 cumulative deposit-based membership applications since Apr-2010 `[AR FY26, MD&A, PDF p63/pr52]` | nothing — the broker keeps brokerage | SEBI (broker regulation); the broker (order routing) |
| **Exchange** | BSE | transaction charges ₹3,66,948 lakh = 82% of standalone revenue from operations `[AR FY26, MD&A, PDF p75/pr64]` | **SEBI** sets the charge structure, the base, and the products |
| **Clearing corporation** | ICCL, **100% owned** `[AR FY26, AOC-1 Part A, PDF p312/pr301]` | ICCL FY26 PAT ₹16,979 lakh = 6.8% of consolidated PAT attributable (16,979 / 2,49,698 = 6.8%, `DERIVED`) | SEBI (interoperability, since 3 Jun 2019, lets a member clear a BSE trade elsewhere) |
| **Depository** | CDSL, **15% associate** `[AR FY26, AOC-1 Part B, PDF p313/pr302]` | ₹6,842 lakh equity-method profit = 2.74% of consolidated PAT attributable (6,842 / 2,49,698 = 2.74%, `DERIVED`) | **SEBI forced the divestment** — see F6 |
| **Index (the input to the derivative)** | BSE Index Services (BISPL), **100%** since 1 Jun 2024 | ₹3,876 lakh revenue, ₹2,387 lakh PAT `[AR FY26, AOC-1 Part A, PDF p312/pr301]`; passive AUM linked to BSE indices ₹2,42,114 cr `[AR FY26, MD&A, PDF p63/pr52]` | BSE — **the one node it controls** |
| **Colocation / connectivity** | BSE-owned racks | ₹16,899 lakh, +132.7% `[AR FY26, MD&A, PDF p75/pr64]`; run-rate "₹45 to ₹48 crores per quarter… around 500 racks" `[Q3FY26 Concall, MD&CEO]` | SEBI (fair-access rules); demand is set by member latency needs |
| **Market data** | BSE domestic; **Deutsche Börse is the exclusive international licensor since Apr-2014** | ₹67.63 cr, +34.1% `[AR FY26, MD&A, PDF p63/pr52]` | the licensing counterparty offshore; BSE domestically |
| **Listing (issuers)** | 5,663 listed companies — the world's largest by count `[AR FY26, MD&A, PDF p57/pr46]` | listing fees ₹38,861 lakh = 8.70% of standalone revenue from operations `[AR FY26, MD&A, PDF p75/pr64]` | SEBI (fee slabs); and BSE **regulates these same customers** (overlay §1 L4 rule) |
| **State** | SEBI turnover fee, STT, stamp duty | **negative** — SEBI regulatory fees ₹55,625 lakh standalone `[AR FY26, Note, PDF p287/pr276]`; ₹51,478 lakh of STT collected and remitted `[AR FY26, MD&A, PDF p77/pr66]` | SEBI and the Union Budget |

### 1.3 The structural asymmetry the map exposes

**The node with the most counterparties captures the least economics, and vice versa.**

- **5,663 issuers** produce **8.70%** of standalone revenue from operations (₹38,861 lakh / ₹4,46,951 lakh).
- **~610 actively trading members** produce **82%** of it (transaction charges, ₹3,66,948 lakh).
  `[AR FY26, MD&A, PDF p75/pr64; Q1FY27 Concall, MD&CEO]`

Neither proportion alone says anything. Together they say the business is not a listing utility with a
trading arm; it is a **member-facing execution venue with a large, low-yield listing register attached**.
That inverts the intuitive reading of "world's largest exchange by number of listed companies," which is
the first thing the MD&A says about itself `[AR FY26, MD&A, PDF p57/pr46]`.

### 1.4 The float — whose money moves through the chain

Overlay §2 requires this be stated before any cash claim. ICCL's balance sheet is the clearest single
illustration: total assets ₹5,67,395 lakh against total liabilities ₹4,84,532 lakh
`[AR FY26, AOC-1 Part A, PDF p312/pr301]`. **85.4% of the clearing corporation's balance sheet is other
people's money** (4,84,532 / 5,67,395 = 85.4%, `DERIVED`). At the parent, member deposits are ₹14,401 lakh
and STT collected-and-payable ₹51,478 lakh `[AR FY26, MD&A, PDF p77/pr66]`.

---

## 2. The duopoly, segment by segment

### 2.1 The scoreboard

| Segment | BSE position, FY2026 | NSE position | Direction over 5 years |
|---|---|---|---|
| **Equity cash** | ADT ₹7,950 cr, +2.36% `[AR FY26, MD&A, PDF p58/pr47]`; share "hovering around 7% to 8% compared to 5% to 6% when I joined" (Jan-2023) `[Q4FY26 Concall, MD&CEO]` | 92.99% `[SECONDARY: NSE FY26 disclosure as reported, 2026]` | **Improving, slowly.** ~+2pp in 40 months |
| **Equity index options** | Premium ADT ₹19,523 cr vs ₹8,978 cr, **+117.5%** `[AR FY26, MD&A, PDF p58/pr47]`; premium share ~32–34% mid-2026 `[SECONDARY: Business Today / Jefferies, 2026-07-03]` | ~66–68% of premium | **Transformed.** Near-zero in FY2023 to a third of the market |
| **Equity futures** | ADT ₹342 cr vs ₹207 cr `[AR FY26, MD&A, PDF p58/pr47]` | 99.79% `[SECONDARY: NSE FY26 disclosure as reported, 2026]` | **Not contested.** Management: "futures are not very heavily traded product in BSE" `[Q1FY27 Concall, MD&CEO]` |
| **Single-stock derivatives** | Relaunched 1 Jul 2024; since-relaunch turnover ₹564 cr futures / ₹498 cr options as at Q3FY25 `[Q3FY25 Concall, MD&CEO]`; "a very challenging situation" `[Q1FY27 Concall, MD&CEO]` | dominant | **Failed to date** |
| **Currency derivatives** | **NIL** in FY2026, vs ADT ₹1,525.34 cr FY25, ₹9,733.67 cr FY24, ₹25,599 cr FY23, ₹26,672 cr FY22 `[AR FY26, MD&A, PDF p58/pr47; AR FY25, MD&A, PDF p52/pr41; AR FY24, MD&A, PDF p54/pr48; AR FY22, MD&A, PDF p73/pr64]` | also collapsed | **Extinguished** |
| **Interest-rate derivatives** | **NIL** from FY2025 `[AR FY25, MD&A, PDF p52/pr41]`, vs ADT ₹122 cr FY24, ₹178 cr FY22 | — | **Extinguished** |
| **Commodity derivatives** | ADT ₹1.08 cr FY25 vs ₹32 cr FY23 `[AR FY25, MD&A, PDF p52/pr41; AR FY24, MD&A, PDF p54/pr48]` | MCX dominant | **Never launched successfully** |
| **SME platform** | 146 listings vs 78 (+87.18%); ₹6,312.50 cr raised vs ₹2,700.58 cr (+133.75%); 712 SMEs cumulative `[AR FY26, MD&A, PDF p57/pr46]`; share 52% in FY2024 `[AR FY24, MD&A, PDF p54/pr48]` | NSE Emerge | **Leading, and accelerating** |
| **Mutual-fund platform (StAR MF)** | 84.1 cr transactions, +26.8%; ">85% of market share by number of transactions amongst exchange-based platforms"; 83,000+ distributors, 50 AMCs `[AR FY26, MD&A, PDF p57/pr46]` | NSE MFSS | **Dominant and stable** |
| **Corporate bonds / G-sec reporting** | 27% corporate-bond reporting; 39% G-sec reporting; 79% retail corporate-bond trading (74% prior); 15% corporate-bond settlement `[AR FY26, MD&A, PDF p58/pr47]` | — | **Mixed** |

### 2.2 The gradient — the finding inside the scoreboard

Ordering BSE's share by node produces a monotone gradient away from the one product it competes in:

> index options premium **~32–34%** › clearing (ICCL) **~25–27%** › colocation **~14–15%** ›
> equity cash **7–8%** › equity futures **~0.2%**

`[SECONDARY: Business Today / Jefferies, 2026-07-03]` for the first; the middle two are an analyst's
figures put to management on the Q3FY26 call and **not contradicted** but also not confirmed
`[Q3FY26 Concall, analyst question]` — they cannot carry a conclusion alone and are used here only to
establish the ordering, which the primary figures at both ends independently support.

The gradient says the derivatives franchise has **not** dragged the rest of the chain with it. Order flow
in index options is genuinely fungible day to day; order flow in cash equities is not, because best-price
execution requires Smart Order Routing, and management states SOR applications have been "pending for
more than six months at the other exchange" `[Q4FY26 Concall, MD&CEO]`. That is a claim about a
competitor made by an interested party and it is recorded as such — but it is the mechanism management
itself offers for why a 32% options share coexists with a 7% cash share.

### 2.3 Sizing the duopoly — the pie barely grew; the split moved

| ₹ crore | FY2025 | FY2026 | Change |
|---|---|---|---|
| BSE consolidated total income | 3,236.31 `[AR FY26 comparative; records/trend_10y.csv]` | 5,148.10 `[AR FY26, consolidated P&L, PDF p164/pr153]` | **+59.1%** |
| NSE consolidated total income | 19,177 `[SECONDARY: NSE Q4FY26 results as reported, 2026-05-05]` | 18,713 `[SECONDARY: same]` | **−2.4%** |
| Combined pool | 22,413.31 `DERIVED` | 23,861.10 `DERIVED` | **+6.46%** |
| BSE share of pool | 14.44% `DERIVED` | 21.58% `DERIVED` | **+714 bps** |

Arithmetic shown: `3,236.31 / 22,413.31 = 14.44%` · `5,148.10 / 23,861.10 = 21.58%` ·
`23,861.10 / 22,413.31 = 1.0646`.

NSE's PAT fell 15.5% to ₹10,302 cr from ₹12,188 cr over the same period
`[SECONDARY: NSE Q4FY26 results as reported, 2026-05-05]`, while BSE's rose 88.3%. **The pool grew 6.5%;
BSE grew 59%.** Roughly nine-tenths of BSE's incremental income came out of NSE, not out of market
growth. This is the single most important structural fact in the wave and it is what disconfirms the
strong form of the overlay hypothesis.

---

## 3. The regulator as price-setter — the timeline and what each action did

Every row states the action, then **what it did to volume and to realisation per unit**. Where the
disclosure does not permit that split, the row says so.

| Date | Action | Source | Effect on activity | Effect on realisation |
|---|---|---|---|---|
| 2023-05-15 / 2023-10-16 | BSE relaunches Sensex derivatives (Friday expiry) and Bankex (Monday expiry) | `[AR FY24, MD&A, PDF p53/pr47]` | EDX ADT ₹1,37,813 cr (FY23) → ₹34,60,747 cr (FY24) | premium ADT ₹4 cr (FY23) → ₹2,133 cr (FY24) `[AR FY24, MD&A, PDF p75/pr69]` |
| 2024-01-05, eff. 2024-05-03 | **RBI**: exchange-traded currency derivatives permitted only against contracted FX exposure | `[SECONDARY: RBI circular, 2024-01-05]`, corroborated by the BSE volume series | BSE CDX ADT ₹9,733.67 cr → ₹1,525.34 cr (−84%) → **NIL** `[AR FY25/FY26, MD&A]` | n/a — base extinguished |
| **2024-04-26** | **SEBI letter**: regulatory fee payable on **notional** value of option contracts, **retrospective to FY2006-07, with 15% p.a. interest** | `[AR FY24, Board's Report, PDF p19/pr13; AR FY25, Note 45, PDF p275/pr264]` | none | **₹16,977 lakh provided FY24 + ₹5,444 lakh FY25 = ₹22,421 lakh** `[AR FY25, consolidated P&L, PDF p191/pr180]` |
| 2024-07-01, eff. 2024-10-01 | **SEBI "True to Label"** — MII charges must be uniform per unit; slab-based volume discounts removed | `[AR FY25, MD&A policy list, PDF p50/pr39]`; "BSE has revised its transaction charges for Sensex and Bankex Options – in accordance with SEBI's True to Label circular" `[Q2FY25 Concall, 2024-11-12]` | none directly | **FY26 is the first full year.** Contributes to the equity-cash realisation fall in F5 |
| **2024-10-01** | **SEBI "Measures to Strengthen Equity Index Derivatives Framework"** — six measures: contract size to ₹15–20 lakh; **one weekly expiry per exchange on one benchmark index**; 2% ELM on expiry-day shorts; upfront premium collection; calendar-spread benefit withdrawn on expiry day; intraday position monitoring | `[AR FY25, MD&A policy list, PDF p50/pr39]`; measure detail `[SECONDARY: SEBI/HO/MRD/TPD-1/P/CIR/2024/132]` | Bankex moved to monthly from 2024-11-20 `[Q2FY25 Concall]`; BSE: "the number of contracts traded, and notional turnover has declined… while the premium turnover has remained stable" `[Q3FY25 Concall, MD&CEO]`; market-wide, index-option annual premium turnover fell in FY25 for the first time in eight years `[SECONDARY: Business Standard, 2025-04-28]` | contracts down, premium flat → **realisation per contract up, realisation per rupee of premium unchanged** |
| 2024-10-15 | SEBI: monitoring of position limits, equity derivatives | `[AR FY25, MD&A policy list, PDF p50/pr39]` | see 2025-09-01 | — |
| 2025-01-03 | BSE moves Sensex weekly expiry Friday→Tuesday; Bankex Monday→Tuesday | `[Q3FY25 Concall; Q2FY26 Concall slide]` | contracts and notional declined; premium stable | premium/notional ratio rose |
| 2025-06-27 | **SEBI Common Contract Note with single VWAP** | `[SECONDARY: SEBI press release, 2025-07]`, corroborated by `[Q3FY26 Concall, MD&CEO]` "common contract notes were brought in place" | intended to make execution venue-agnostic; cash share 5–6% → 7–8% over the period, but SOR "has not taken off" `[Q4FY26 Concall, MD&CEO]` | — |
| 2025-07-03 | **SEBI interim order, Jane Street** — restraint plus ₹4,843.57 cr impounded | `[SECONDARY: SEBI interim order, 2025-07-03]` | BSE index-options premium turnover on the first expiry after fell to ₹19,683 cr from ₹44,010 cr on 24-Jun-2025, **−55.3%** `[SECONDARY: Business Standard, 2025-07-10]` | **not durable** — FY26 premium ADT still +117.5%; management: "not seeing any specific impact arising out of Jane Street" `[Q1FY26 Concall, 2025-08-13]` |
| 2025-07-28 | Revised **ESM** framework (joint SEBI/exchange surveillance meeting 2025-07-25) | `[AR FY26, MD&A, PDF p64/pr53]` | restricts trading in small-cap scrips | reduces turnover in BSE's higher-charge groups |
| 2025-09-01 | BSE moves Sensex weekly expiry Tuesday→Thursday; Bankex monthly→Thursday | `[Q2FY26 Concall slide; Q3FY26 Concall, MD&CEO]` | "pronounced expansion in open interest, deeper market participation" `[Q3FY26 Concall, MD&CEO]` | **premium/notional ratio 0.0811% → 0.1043%, +28.6%** `DERIVED`, §3.1 |
| 2025-09-01, eff. 2025-10-01 | **SEBI Intraday Position Limits framework** — intraday net FutEq ₹5,000 cr, gross ₹10,000 cr, against EOD net ₹1,500 cr; ≥4 random intraday snapshots | `[AR FY26, MD&A policy list, PDF p55/pr44]`; limits `[SECONDARY: SEBI/HO/MRD/TPD/CIR/P/2025/122]` | caps the largest participants' expiry-day size | — |
| 2025-10-30 | SEBI: eligibility criteria for derivatives on existing **non-benchmark indices** | `[AR FY26, MD&A policy list, PDF p54/pr43]` | BSE "revamped the Bankex index to make it broad-based" `[Q3FY26 Concall, MD&CEO]` | — |
| 2025-11-10 | BSE **AMS** — 1% price band and once-a-week trading for certain **BSE-exclusive** securities | `[AR FY26, MD&A, PDF p64/pr53]` | removes turnover from BSE-exclusive small caps | these are BSE's highest-charge cash groups — see F5 |
| 2025-12-12 | SEBI: Strengthening Governance of MIIs | `[AR FY26, MD&A policy list, PDF p54/pr43]` | — | governance cost |
| 2026-01-16, impl. 2026-08-03 | **SEBI Closing Auction Session** in equity cash + pre-open modification | `[AR FY26, MD&A policy list, PDF p53/pr42; Q3FY26 Concall, MD&CEO]` | changes how the closing price used for derivative settlement, index computation and MF NAV is formed | too early to observe `[Q1FY27 Concall, MD&CEO]` |
| **2026-02-01, eff. 2026-04-01** | **STT raised**: futures 0.02%→0.05%; options premium 0.10%→0.15%; exercise 0.125%→0.15% | `[AR FY26, MD&A policy list, PDF p53/pr42]` | "impacted the market significantly in respect of futures and to some extent in terms of options"; BSE impact "minimal" because BSE's futures book is small `[Q1FY27 Concall, MD&CEO]` | raises the all-in cost to the trader without raising BSE's take |
| 2026-02-13, eff. 2026-07-01 | **RBI final Amendment Directions on Capital Market Exposure** (deferred from 2026-04-01) | `[AR FY26, MD&A policy list, PDF p53/pr42; Q1FY27 Concall, MD&CEO]` | live headwind; full effect masked because "there are remnant bank guarantees in the system which are of the past" `[Q1FY27 Concall, MD&CEO]` | **unresolved — the monitorable** |
| 2026-02-04 / 2026-02-05 | Order-to-Trade Ratio framework revised; calendar-spread margin benefit on single-stock expiry reviewed | `[AR FY26, MD&A policy list, PDF p53/pr42]` | affects HFT order behaviour | — |

### 3.1 What the FY2026 decomposition actually shows (overlay §1 mandatory L3 rule)

Activity and realisation must be separated. Both computed inline and re-derived independently; both are
`ESTIMATE` because trading-day counts are assumed equal across the two years, which the AR does not state.

**Equity derivatives — realisation was flat; it was all activity.**
`19,523 / 8,978 = 2.1746` (premium ADT, +117.5%)
`3,13,437 / 1,41,554 = 2.2143` (derivatives transaction charges, +121.4%)
`2.2143 / 2.1746 = 1.0183` → **realisation per unit of premium +1.8%**
`[AR FY26, MD&A, PDF p58/pr47 and PDF p75/pr64]`

**The SEBI fee base is notional, not premium — and the arithmetic proves it.**
`1,87,15,375 / 1,10,66,674 = 1.6912` (options **notional** ADT, +69.1%)
`55,625 / 33,123 = 1.6794` (standalone SEBI regulatory fees, +67.9%)
`[AR FY26, MD&A, PDF p58/pr47; AR FY26, Note, PDF p287/pr276]`
The fee tracked notional to within 1.2 percentage points while revenue tracked premium and grew 117.5%.
**BSE's revenue and its largest single levy are indexed to two different quantities, and the ratio
between them is not BSE's to set.**

**The ratio itself moved 28.6% in one year.**
`1,87,15,375 / 19,523 = 958.6` (FY26 notional per ₹1 of premium)
`1,10,66,674 / 8,978 = 1,232.7` (FY25)
Premium/notional: `1/1,232.7 = 0.0811%` → `1/958.6 = 0.1043%`, **+28.6%**.
Consequence: SEBI regulatory fees absorbed `33,123 / 1,41,554 = 23.4%` of derivatives transaction
charges in FY25 and `55,625 / 3,13,437 = 17.7%` in FY26 — a 5.7pp swing, worth ₹17,866 lakh on FY26
revenue, driven entirely by where in the expiry cycle the trading sat. Management confirms the direction
and the cause: "the premium to notional ratio of Sensex vis-à-vis comparable indices in the market, the
ratio at Sensex is lower. This is mainly because still the monthly contracts are yet to develop"
`[Q4FY26 Concall, MD&CEO]`.

**A cross-check on the volume series that validates the reading.** FY25's AR reported EDX daily average
value of ₹1,10,66,881.25 cr `[AR FY25, MD&A, PDF p52/pr41]`; FY26's AR reports FY25 options notional ADT
of ₹1,10,66,674 cr and futures ADT ₹207 cr `[AR FY26, MD&A, PDF p58/pr47]`.
`1,10,66,674 + 207 = 1,10,66,881` — exact. The two disclosures tie and the split is safe to use.

---

## 4. Entry barriers and substitutes

### 4.1 Why no third equity exchange has succeeded

The count of exchanges is itself the primary evidence, and BSE prints it every year:

| Year | Equity-cash exchanges | Clearing corps | Depositories | Source |
|---|---|---|---|---|
| FY2019 | **5** | — | 2 | `[AR FY19, MD&A, PDF p68/pr59]` |
| FY2021 | **3** | 5 | 2 | `[AR FY21, MD&A, PDF p63/pr58]` |
| FY2022 | **3** | 5 | 2 | `[AR FY22, MD&A, PDF p66/pr57]` |
| FY2024 | **3** | 4 | 2 | `[AR FY24, MD&A, PDF p48/pr42]` |
| FY2026 | **3** | 4 | 2 | `[AR FY26, MD&A, PDF p53/pr42]` |

Five barriers, in descending order of how binding they are:

1. **Liquidity is a network good and the network is the product.** BSE's own history is the cleanest
   proof available: its equity-derivatives segment ran at **498 contracts per day in FY2017 and 182 in
   FY2018** after the Liquidity Enhancement Incentive Programme was discontinued, then **126 in FY2019**
   `[AR FY18, MD&A, PDF p24/pr17; AR FY19, MD&A, PDF p77/pr68]`. Four separate incentive-funded relaunches
   (LEIPS to FY2018 · LES from 1 Sep 2018 · LES relaunch 26 Aug 2019 · Sensex 50 with Friday expiry
   29 Jun 2020) produced ADTs of ₹1,062 cr (FY20) and ₹1,40,804 cr (FY21) that did not hold
   `[AR FY20, MD&A, PDF p82/pr75; AR FY21, MD&A, PDF p71/pr66]`. **It took roughly ten years and at least
   four attempts before the May-2023 Sensex relaunch worked.** An incumbent's book is not bought cheaply.
2. **The index is a licensed asset.** No venue can list a Nifty derivative without NSE's licence; BSE
   secured full ownership of the Sensex family only in June 2024. A new entrant has neither.
3. **Regulatory capital and the SGF.** Overlay §5: capital here is regulatory, not physical. A new
   exchange must fund a clearing corporation, a core SGF and an investor protection fund before it earns
   a rupee.
4. **Post-trade plumbing that the incumbent controls in practice.** Interoperability (3 Jun 2019) and the
   common contract note (27 Jun 2025) were both SEBI attempts to lower switching cost; management's
   position is that SOR approvals still sit unactioned at the competitor `[Q4FY26 Concall, MD&CEO]`.
5. **SEBI restricts even the movement of people.** Circular of 26 May 2025 imposes a **cooling-off period
   for KMPs of an MII joining a competing MII** `[AR FY26, MD&A policy list, PDF p56/pr45]`.

**The live test of these barriers.** MSEI resumed live equity cash and derivatives trading in January 2026
after raising roughly ₹1,240 cr from Groww, Zerodha, Share India, Peak XV and others
`[SECONDARY: business press, 2024–2026]`. Primary corroboration that it is a real presence: BSE's own AR
counts three equity-cash exchanges `[AR FY26, MD&A, PDF p53/pr42]`, and BSE's MD&CEO was asked directly
"How do you look at MSE as an emerging competitor?" on the Q4FY26 call and answered that "the number of
exchanges can be whatever it is and they can cater to the society by creating niche products"
`[Q4FY26 Concall, MD&CEO]`. **Next check: MSEI's disclosed turnover share at FY2027 year-end.**

### 4.2 The realistic substitute for on-exchange derivatives trading

There is essentially none, and the numbers are not close.

- **Offshore / GIFT IFSC.** India INX's derivatives ADTV was **USD 16.87 mn per day** in FY2026 across
  52,341 lots `[AR FY26, MD&A, PDF p60/pr49]`, against BSE's domestic options **premium** ADT of
  ₹19,523 cr `[AR FY26, MD&A, PDF p58/pr47]`. Orders of magnitude apart.
- **OTC and ODIs.** SEBI's 17 Dec 2024 circular on "regulatory arbitrage with respect to Offshore
  Derivative Instruments and FPIs with segregated portfolios" `[AR FY25, MD&A policy list, PDF p50/pr39]`
  narrows that route deliberately.
- **The real substitute is abstention.** The retail index-options trade is discretionary. The STT rise of
  1 Feb 2026 and the RBI collateral directions of 13 Feb 2026 both raise the cost of the trade without
  changing where it happens. Management's own framing: the headwinds "appear to have impacted the market
  significantly" while BSE's share held `[Q1FY27 Concall, MD&CEO]`.

**Consequence for the competitive read.** BSE does not compete against a substitute product; it competes
against one venue and against the participation rate. Both are things the regulator moves.

---

## 5. Concentration — customers and suppliers

### 5.1 Customers (trading members and issuers)

**Not disclosed, and the gap is real.** BSE reports one operating segment under Ind AS 108
`[AR FY26, Note 39, PDF p228/pr217]` with a geographic split (within India ₹5,08,140 lakh, outside India
₹6,670 lakh) and **no major-customer disclosure**. Ind AS 108 requires that disclosure once a single
external customer reaches 10% of revenue; its absence implies no member crosses 10%, but the **top-10
concentration is not disclosed at all.**
→ `NOT-DISCLOSED -> the Ind AS 108.34 major-customer disclosure, or a member-wise turnover concentration
table; neither exists in the FY2026 consolidated or standalone notes.`

**The available proxy is a realised event, and it is severe.** SEBI's interim order against Jane Street
on 3 July 2025 restrained one group. BSE's index-options premium turnover on the first expiry after the
order (8 Jul 2025) was ₹19,683 cr against ₹44,010 cr on the 24 Jun 2025 expiry — `19,683 / 44,010 =
0.4472`, a **55.3% fall** `[SECONDARY: Business Standard, 2025-07-10]`. That single-source figure cannot
carry a conclusion alone, but it is directionally corroborated by management being asked about it on the
Q1FY26 call `[Q1FY26 Concall, 2025-08-13]`. **One counterparty's removal halved a quarter's expiry-day
turnover.** See F8.

**Issuers.** 5,663 listed companies `[AR FY26, MD&A, PDF p57/pr46]`, and BSE delisted 1,484 of them
between 1 Apr 2016 and 31 Mar 2026 `[AR FY26, MD&A, PDF p66/pr55]`. Issuer concentration is structurally
nil — but so is issuer economics (§1.3). The overlay §1 L4 conflict stands: annual listing fees of ₹242 cr
`[AR FY26, MD&A, PDF p63/pr52]` are paid by entities BSE supervises as first-line regulator, against
which it ran 37,164 surveillance alerts and 434 member inspections in FY2026
`[AR FY26, MD&A, PDF p64/pr53]`.

### 5.2 Suppliers

| Supplier | Dependence | Owned? |
|---|---|---|
| Clearing corporation | ICCL — clearing & settlement expense ₹37,191 lakh standalone, **−5% on far higher volume** `[AR FY26, MD&A, PDF p75/pr64]` | **100%** |
| Index licensor | BISPL — bought out from S&P Dow Jones for ₹3,001 lakh, eff. 1 Jun 2024 `[AR FY25, PDF p200/pr189]` | **100%** since FY2025 |
| Depository | CDSL | **15%** — SEBI-forced (F6) |
| International market-data distribution | **Deutsche Börse, exclusive licensor for all international clients since Apr-2014** `[AR FY26, MD&A, PDF p63/pr52]` | **not owned — the only single-supplier dependency in the chain** |
| Power exchange (adjacency) | Hindustan Power Exchange, 22.62% via BSE Technologies `[AR FY26, MD&A, PDF p68/pr57 and AOC-1 Part B, PDF p313/pr302]` | minority |

The Deutsche Börse arrangement is the one genuine single-supplier exposure and it sits on a line worth
₹67.63 cr `[AR FY26, MD&A, PDF p63/pr52]` — 1.5% of standalone revenue from operations. Immaterial in
size; noted because it is the only exclusivity in the chain BSE does not own.
→ `NOT-DISCLOSED -> the Deutsche Börse cooperation agreement's term, revenue-share and termination
provisions; not filed, and not summarised in any AR FY2017–FY2026.`

---

## 6. Cyclicality — what the record shows, not what theory predicts

### 6.1 The equity-cash cycle is real and it is deep

BSE's own average daily equity turnover, one series, ten years (₹ crore):

| FY16 | FY17 | FY18 | FY19 | FY20 | FY21 | FY22 | FY23 | FY24 | FY25 | FY26 |
|---|---|---|---|---|---|---|---|---|---|---|
| 2,996 | 4,025 | 4,402 | **3,127** | **2,676** | 4,197 | 5,396 | **4,132** | 6,622 | 7,766 | 7,950 |
| | +34% | +9.4% | **−29%** | **−14.4%** | +56.9% | +28.6% | **−23.4%** | +60% | +17% | +2.4% |

FY2016 and FY2017 `[AR FY17, MD&A financial review, PDF p83/pr81]` ("equity cash segment by 34% to
₹4,025 Crore in FY 2016-17 (FY 2015-16: ₹2,996 Crore)"); thereafter
`[AR FY18, MD&A, PDF p24/pr17; AR FY19, MD&A, PDF p77/pr68; AR FY20, MD&A, PDF p82/pr75;
AR FY21, MD&A, PDF p71/pr66; AR FY22, MD&A, PDF p73/pr64; AR FY24, MD&A, PDF p53/pr47;
AR FY25, MD&A, PDF p52/pr41; AR FY26, MD&A, PDF p58/pr47]`. FY2023 is a comparative inside the FY2024
report; per `waves/W1_docmap.md` GAP-001 no FY2023 annual report exists.

**Peak to trough, FY2018 → FY2020: `2,676 / 4,402 = 0.6079`, a 39.2% fall over two consecutive years.**
Three separate down-years in ten. This is not a theoretical cycle.

### 6.2 What a down-cycle did to earnings — the FY2019–FY2021 episode

| ₹ lakh, consolidated | FY2019 | FY2020 | FY2021 | Source |
|---|---|---|---|---|
| Revenue from operations | 45,030 | 45,051 | 50,137 | `records/trend_10y.csv`, from `[AR FY20/FY21 consolidated P&L]` |
| Investment income | 20,218 | 15,866 | 12,908 | same |
| **PAT attributable** | **19,417** | **12,227** | **14,490** | same |

`12,227 / 19,417 = 0.6297` → **PAT fell 37.0% while revenue from operations was flat.**
`12,908 / 20,218 = 0.6384` → **investment income fell 36.2% over the same two years.**

**The mechanism, and it is the important part.** Revenue did not fall — earnings did, because the cost
base is fixed (overlay §5) *and* because investment income falls at the same time and for the same
reason: rates come down when activity comes down. The two shock absorbers fail together. Market
capitalisation of all listed companies confirms the environment: ₹151 trillion at FY2019 → **₹113.5
trillion at FY2020**, `113.5 / 151 = 0.7517`, a 24.8% fall `[AR FY19, MD&A, PDF p68/pr59; AR FY20, MD&A,
PDF p77/pr70]`.

### 6.3 The new engine has a different cycle, and it is not the equity cycle

FY2026 is the test case. **The Sensex fell 7.06% over the year** (71,947.55 from 77,414.92) and equity
cash ADT rose only 2.4% `[AR FY26, MD&A, PDF p58/pr47]` — yet options premium ADT more than doubled.
Index-derivative revenue is a claim on **volatility, participation and the rule-set**, not on the index
level. Market capitalisation of all listed companies was flat at ₹412 trillion in both FY2025 and FY2026
`[AR FY25, MD&A, PDF p49/pr38; AR FY26, MD&A, PDF p53/pr42]`.

**The corollary is the risk.** A bear market no longer switches the revenue off; a **volatility collapse
plus a regulatory tightening** does. FY2025 is the proof that the second combination bites: India's index
option annual premium turnover fell for the first time in eight years
`[SECONDARY: Business Standard, 2025-04-28]`, and BSE's currency and interest-rate segments went to nil
in the same window `[AR FY25, MD&A, PDF p52/pr41]`.

---

## 7. Adjacent economics

| Node | FY2026 | FY2025 | Read |
|---|---|---|---|
| **Depository (CDSL, 15%)** | equity-method profit ₹6,842 lakh = **2.74%** of consolidated PAT attributable `[AR FY26, AOC-1 Part B, PDF p313/pr302]` | — | BSE participates in the depository leg as a minority financial investor only. Implied CDSL-group PAT `6,842 / 0.15 = 45,613 lakh` (`ESTIMATE` — equity-method share may embed adjustments) |
| **Clearing (ICCL, 100%)** | revenue ₹42,464 lakh, PAT ₹16,979 lakh, **85.4% of its balance sheet is other people's money** `[AR FY26, AOC-1 Part A, PDF p312/pr301]` | — | The one large adjacent node BSE owns outright. Clearing & settlement expense **fell 5%** on far higher volume `[AR FY26, MD&A, PDF p75/pr64]` — an intra-group transfer price, not an arm's-length cost |
| **Colocation / connectivity** | ₹16,899 lakh, **+132.7%** `[AR FY26, MD&A, PDF p75/pr64]` | ₹7,262 lakh | "we never started as a profit center… it is incidental that we put in place colocation as a requirement and it has become a profit center… could get stabilized at that level" `[Q3FY26 Concall, MD&CEO]`. **Management is guiding this line to plateau.** Capex-funded: additions ₹45,753 lakh in FY26 `[AR FY26, MD&A, PDF p76/pr65]` |
| **Market data** | ₹67.63 cr, +34.1% `[AR FY26, MD&A, PDF p63/pr52]` | ₹50.42 cr | growth attributed to "new domestic and international customers, along with **a revision in international pricing**" — the only line in the AR where BSE describes raising a price |
| **Index licensing (BISPL, 100%)** | revenue ₹38.76 cr (+44.25%), PBT ₹32.13 cr (+26%), **PBT margin 82.9%**; passive AUM linked ₹2,42,114 cr `[AR FY26, MD&A, PDF p63/pr52]` | ₹26.87 cr / ₹25.56 cr | **The highest-margin node in the chain and the only one BSE prices.** Bought for ₹3,001 lakh; FY26 PAT ₹2,387 lakh = `2,387 / 3,001 = 79.5%` of the purchase price in one year |
| **Power exchange (HPX, 22.62%)** | — | — | Optionality on "market coupling… centralizing price discovery across competing exchanges" `[AR FY26, MD&A, PDF p68/pr57]` — a reform that would do to power exchanges what interoperability did to clearing |

**The conclusion the table supports.** Adjacent economics are not where the case is: depository 2.74% and
index 0.87% of revenue. What they establish is a **pattern of regulatory determination over which nodes an
exchange may own** — forced out of the depository, permitted to own the clearing corporation, free to own
the index. The one node BSE controls end-to-end is also the one with the highest margin, and it is
sub-1% of revenue.

---

## 8. Findings

### FINDING: SEBI can re-price BSE retrospectively, and has — the notional-turnover fee reinterpretation cost 21.8% of a year's profit
S1 WHAT: On 26 April 2024 SEBI wrote to BSE advising that the regulatory fee on "annual turnover" be computed on the **notional** value of option contracts **from FY2006-07 onwards, with interest at 15% per annum**; SEBI reiterated the instruction by letter of 14 August 2024 and BSE accounted for it `[AR FY24, Board's Report, PDF p19/pr13; AR FY25, Note 45, PDF p275/pr264]`.
S2 WHY: The 2007 regulation fixed a levy on "annual turnover" without defining turnover for an option. BSE bills members on **premium**; SEBI elected to read the fee base as **notional**. Nothing in BSE's conduct changed — only the regulator's reading of its own rule, applied backwards over seventeen years. This is the mechanism, not "higher regulatory cost": a unilateral redefinition of the base by the party that also writes the rule.
S3 EVIDENCE: ₹16,977 lakh provided in FY2024 and ₹5,444 lakh in FY2025, ₹22,421 lakh in total `[AR FY25, consolidated P&L, PDF p191/pr180]`. Against FY2024 consolidated PAT attributable of ₹77,839 lakh that is `16,977 / 77,839 = 21.8%`; across the two years, `22,421 / (77,839 + 1,32,589) = 10.7%` (`DERIVED`). **The asymmetry inside the disclosure:** in FY2026 BSE earned on options **premium** ADT of ₹19,523 cr while paying the SEBI fee on options **notional** ADT of ₹1,87,15,375 cr — `1,87,15,375 / 19,523 = 958.6`, so the levy base is 959x the revenue base `[AR FY26, MD&A, PDF p58/pr47]`. Recomputed independently: standalone SEBI regulatory fees grew `55,625 / 33,123 = 67.9%` against notional turnover growth of `1,87,15,375 / 1,10,66,674 = 69.1%` and premium growth of 117.5% — the fee tracks notional, not revenue `[AR FY26, Note, PDF p287/pr276]`.
S4 CONNECTS: Industry — the same base applies to every exchange, so it is a structural feature of Indian index derivatives, not a BSE-specific dispute. MgmtCommentary — the MD&A calls regulatory contribution "a volume-correlated cost" whose scaling means "the Company's margin profile is unaffected" `[AR FY26, MD&A, PDF p76/pr65]`, which is true only while the premium/notional ratio holds; it moved 28.6% in FY2026 alone. IncomeStatement — the levy absorbed `33,123 / 1,41,554 = 23.4%` of derivatives transaction charges in FY25 and `55,625 / 3,13,437 = 17.7%` in FY26, a 5.7pp swing worth ₹17,866 lakh on FY26 revenue. Notes — the provision sits in a standalone note with no quantification of remaining exposure. The compensating control management offers is scale: revenue grew faster than the fee in FY26. **The class of error that control cannot catch is a reversion in the premium/notional ratio, because the ratio is set by where in the expiry cycle participants trade — which is neither BSE's decision nor a function of its scale.**
DOMAINS: Industry, MgmtCommentary, IncomeStatement, Notes
DISCONFIRM: Searched for evidence that the fee base is contested or reversible. BSE did not litigate; it provided and paid, and the FY2025 note records only that SEBI "reiterated the advise." Contrary evidence found and material: in FY2026 the arrangement worked **in BSE's favour** — notional grew 69.1% while premium grew 117.5%, so the fee fell from 23.4% to 17.7% of derivatives revenue. The exposure is two-sided, not one-sided. No disclosure of any residual or disputed amount was found in the FY2026 notes.
S5 MEANS: BSE's largest single levy is assessed on a quantity it neither bills nor controls, by a body that has demonstrated it will re-read its own rule retrospectively with penal interest — so the cost line is not forecastable from revenue.
BASE-RATE: **Realised, at this company, twice-booked.** ₹22,421 lakh charged across FY2024–FY2025 for conduct in FY2007–FY2023 `[AR FY25, PDF p191/pr180]`. In the wider system: RBI's ETCD directions of 5 January 2024 took BSE's currency-derivatives ADT from ₹9,733.67 cr to nil within two years `[AR FY24/FY25/FY26, MD&A]`, and SEBI's October 2024 index-derivatives measures coincided with the first fall in India's annual index-option premium turnover in eight years `[SECONDARY: Business Standard, 2025-04-28]`. This pattern has cost exchanges money repeatedly and recently.
S6 IMPLICATION: Earnings durability is bounded by a cost the company cannot forecast from its own revenue, so any multiple applied to derivatives profit carries an unpriced regulatory tail and requires a wider margin of safety than the operating-leverage narrative implies. Monitorable: the premium-to-notional ratio disclosed each quarter — a reversion to the FY2025 level of 0.0811% would restore roughly 5.7pp of derivatives revenue to the levy. Thesis-breaker: a further retrospective re-basing, or a change in the fee base that is not offset by ratio improvement. Next check: Q2FY27 results and the FY2027 AR regulatory-fee note.
SEVERITY: High

### FINDING: The overlay's hypothesis is half wrong — SEBI sets the rate, but the share moved decisively against the incumbent under identical rules
S1 WHAT: In FY2026, under the same SEBI framework, the same STT increase and the same RBI collateral directions, BSE's consolidated total income rose 59.1% to ₹5,14,810 lakh and PAT attributable rose 88.3% to ₹2,49,698 lakh, while NSE's consolidated total income fell 2.4% to ₹18,713 cr and its PAT fell 15.5% to ₹10,302 cr.
S2 WHY: The mechanism is not pricing — it is the expiry-day calendar and the product. SEBI's 1 October 2024 measures limited each exchange to one weekly expiry on one benchmark index, converting an incumbency advantage in *number of weekly products* into a symmetric one-each allocation. BSE then moved its Sensex weekly expiry twice (Friday→Tuesday, January 2025; Tuesday→Thursday, September 2025) and reports that expiry-day concentration "has significantly fallen down and it has gotten distributed" `[Q4FY26 Concall, MD&CEO]`. A rule intended to restrain speculation redistributed order flow.
S3 EVIDENCE: BSE ₹5,148.10 cr vs NSE ₹18,713 cr total income in FY26 `[AR FY26, consolidated P&L, PDF p164/pr153; SECONDARY: NSE Q4FY26 results as reported, 2026-05-05]`. **The counter-proportion is the finding:** the combined pool grew only `23,861.10 / 22,413.31 = 6.46%`, while BSE grew 59.1% — so BSE's share went `3,236.31 / 22,413.31 = 14.44%` to `5,148.10 / 23,861.10 = 21.58%`, +714 bps (`DERIVED`, recomputed independently). Roughly nine-tenths of BSE's incremental income came out of the incumbent, not out of market growth. **The share gain is not uniform across the chain**, which is the second half of the asymmetry: index-options premium share ~32–34% `[SECONDARY: Business Today/Jefferies, 2026-07-03]` against equity cash 7–8% `[Q4FY26 Concall, MD&CEO]` and equity futures ~0.2% (BSE futures ADT ₹342 cr `[AR FY26, MD&A, PDF p58/pr47]`; NSE 99.79% `[SECONDARY: NSE FY26 disclosure as reported]`).
S4 CONNECTS: Industry — three equity-cash exchanges exist, down from five in FY2019 `[AR FY19, MD&A, PDF p68/pr59; AR FY26, MD&A, PDF p53/pr42]`, so the share moved *within* a duopoly, not through new entry. Business — BSE's revenue concentration is the flip side: equity derivatives are `3,13,437 / 4,46,951 = 70.1%` of standalone revenue from operations `[AR FY26, MD&A, PDF p75/pr64]`. MgmtCommentary — management explicitly declines to manage to share: "we do not measure our success in terms of market share… our primary goal is deepening and broadening of markets" `[Q1FY27 Concall, MD&CEO]`, and targets member and FPI counts instead (610 members, 650 FPIs, target 800). Governance — SEBI's 26 May 2025 KMP cooling-off circular restricts movement between competing MIIs `[AR FY26, MD&A policy list, PDF p56/pr45]`, which is the regulator treating inter-exchange competition as something to be shaped rather than left alone. The compensating control on the share gain is product breadth; **the class of error it cannot catch is that the gain is concentrated in one contract on one expiry day, so a rule touching that day is not diversified against.**
DOMAINS: Industry, Business, MgmtCommentary, Governance
DISCONFIRM: Sought evidence the share gain is regulator-granted rather than won. Found partially supporting: SEBI's own actions (one-weekly-expiry-per-exchange, common contract note, interoperability) each mechanically improved a challenger's position. Found against a purely regulatory reading: BSE's cash share moved only 5–6% to 7–8% over 40 months despite the common contract note, because SOR remains unimplemented `[Q4FY26 Concall, MD&CEO]` — i.e. where the regulator enabled but the incumbent could delay, the share barely moved. NSE's FY26 figures are SECONDARY-sourced from a private company's results release and are corroborated only by consistent reporting across multiple outlets; they cannot alone carry this conclusion, and the direction is independently supported by BSE's own primary disclosures.
S5 MEANS: Order flow in index options is genuinely contestable at the margin of an expiry-day calendar, but nothing else in the chain is — so the competitive achievement is real, narrow, and rests on a variable the regulator allocates annually.
BASE-RATE: **Realised, and it has cut both ways.** Against BSE: currency derivatives, where BSE reached 46.3% share in FY2018 `[AR FY18, MD&A, PDF p24/pr17]` and fell to 29.59% by FY2021 `[AR FY21, MD&A, PDF p71/pr66]` before the segment was extinguished. For BSE: NSE's PAT fell 15.5% in FY2026 `[SECONDARY: NSE Q4FY26 results as reported]`, the clearest evidence in the record that an incumbent exchange can lose money to a challenger in this market. In the wider system, no third equity venue has converted funding into share — MSEI's ~₹1,240 cr raise and January 2026 relaunch is the live test `[SECONDARY: business press, 2024–2026]`.
S6 IMPLICATION: The durability question is not whether BSE can compete — FY2026 answers that — but whether a share won on one weekly expiry day survives the next reallocation of expiry days, which makes the base/bear/bull spread on this name a function of a regulatory calendar rather than of execution. Monitorable: monthly index-options premium share, and specifically the share of BSE premium arising outside the current and next week, which management puts at "around 5%" `[Q3FY26 Concall, MD&CEO]`. Thesis-breaker: a SEBI reallocation of expiry days that places both exchanges on the same day, or removes weekly expiries entirely.
SEVERITY: Medium

### FINDING: 70% of revenue rests on one contract, on one index, on one weekly expiry day that SEBI allocates
S1 WHAT: Equity-derivatives transaction charges were ₹3,13,437 lakh in FY2026, `3,13,437 / 4,46,951 = 70.1%` of standalone revenue from operations, having grown 121%; the product is essentially one contract — Sensex index options — and SEBI permits each exchange exactly one weekly expiry on one benchmark index.
S2 WHY: SEBI's circular of 1 October 2024 rationalised weekly expiries to one per exchange `[AR FY25, MD&A policy list, PDF p50/pr39; SECONDARY: SEBI/HO/MRD/TPD-1/P/CIR/2024/132]`. BSE elected Sensex and moved Bankex to monthly from 20 November 2024. Because a weekly expiry is where premium concentrates, the choice of *which* day is the single largest determinant of the revenue line — and it has been changed three times in 21 months, each requiring regulatory approval (IFSCA approval for the mirror change was itself a disclosed event, 17 July 2025 `[AR FY26, MD&A, PDF p62/pr51]`).
S3 EVIDENCE: Equity derivatives ₹3,13,437 lakh (+121%) against equity cash ₹25,021 lakh (**−18%**) and StAR MF ₹28,490 lakh (+23%) inside the same transaction-charge line `[AR FY26, MD&A, PDF p75/pr64]`. **The counter-proportion:** the two largest sub-components moved in opposite directions in the same year, so the 88% growth of the aggregate is not a statement about trading activity — it is one product. Concentration by node reinforces it: options premium share ~32–34% against equity futures ~0.2% and single-stock derivatives that management calls "a very challenging situation" with no meaningful volume `[Q1FY27 Concall, MD&CEO]`. Expiry-day dependence, sized by management: premium from weeks other than the current and next week is "around 5%" of total volumes `[Q3FY26 Concall, MD&CEO]` — i.e. roughly 95% sits in the two nearest weeks.
S4 CONNECTS: Industry — the expiry calendar is a regulatory allocation, and BSE's share fell to 32.4% in June 2026 specifically because "NSE had an additional weekly expiry" `[SECONDARY: Business Today/Jefferies, 2026-07-03]`, which is the dependency demonstrated in a single month. Business — BSE has attempted product diversification repeatedly and the record is poor: currency, interest-rate and commodity derivatives all at or near nil (§2.1). MgmtCommentary — management's stated remedy is longer-dated contracts and institutional participation ("650 FPIs… target 800"), explicitly a multi-year project: "Sensex is just a three-year-old product, whereas the other comparable products are 26-year-old" `[Q4FY26 Concall, MD&CEO]`. Notes — no Ind AS 115 disaggregation exists, so this 70.1% concentration is disclosed **only in unaudited MD&A** (`records/revenue_disaggregation.md`). The compensating control is the new-product pipeline — Sensex Next 30, Focused Midcap, Focused IT, corporate bonds, StAR NPS, electronic gold receipts `[AR FY26, MD&A, PDF p58/pr47; Q1FY27 Concall, MD&CEO]`. **The class of error it cannot catch is timing: every one of those is pre-revenue, and the four prior diversification attempts each took years and three of them ended at zero.**
DOMAINS: Industry, Business, MgmtCommentary, Notes
DISCONFIRM: Looked for evidence the franchise is broadening. Found, and it is genuine: expiry-day concentration "has significantly fallen down and it has gotten distributed"; contracts traded outside the current and next week are "5 times more" than January 2025 and premium from those weeks "almost 10 times" `[Q1FY27 Concall, MD&CEO]`; the premium/notional ratio improved 28.6% in FY2026 (§3.1); open interest expanded after the Thursday move `[Q3FY26 Concall, MD&CEO]`. Also found against the risk: the Jane Street shock of July 2025 cut a single expiry's premium turnover by 55.3% and FY2026 still closed +117.5%, so the franchise absorbed a severe single-participant shock within one year.
S5 MEANS: This is a single-product business whose product definition — index, expiry day, lot size, position limit — is set entirely by a third party, so concentration risk here is regulatory rather than commercial.
BASE-RATE: **Realised, at this company, three times.** Currency derivatives ₹26,672 cr ADT (FY22) to nil; interest-rate derivatives to nil from FY2025; commodity derivatives ₹32 cr (FY23) to ₹1.08 cr (FY25) `[AR FY22, MD&A, PDF p73/pr64; AR FY25, MD&A, PDF p52/pr41]`. And in equity derivatives itself: 498 contracts per day in FY2017 falling to 126 in FY2019 when incentive schemes lapsed `[AR FY18, MD&A, PDF p24/pr17; AR FY19, MD&A, PDF p77/pr68]`. BSE has never before sustained a derivatives franchise.
S6 IMPLICATION: Seventy per cent of the earnings stream has a three-year operating history and a product specification renewable at regulatory discretion, so the durability assumption embedded in any long-horizon compounding case is the weakest link in the structure, and the margin of safety must be sized against the possibility that this line is materially smaller rather than merely slower. Monitorable: the disclosed share of premium arising outside the current and next expiry week — currently ~5%; a durable move above 20% would materially change the read. Thesis-breaker: SEBI placing both exchanges' weekly expiries on the same day, or withdrawing weekly index expiries.
SEVERITY: High

### FINDING: Two of BSE's five derivative segments were legislated to zero in four years — the segment-extinction base rate is 40%
S1 WHAT: Currency-derivatives turnover on BSE was **nil** in FY2026 against a daily average of ₹1,525.34 cr in FY2025, ₹9,733.67 cr in FY2024, ₹25,599 cr in FY2023 and ₹26,672 cr in FY2022; interest-rate derivatives turnover was **nil** from FY2025 against ₹122 cr ADT in FY2024; commodity derivatives ran at ₹1.08 cr ADT in FY2025 against ₹32 cr in FY2023.
S2 WHY: For currency derivatives the mechanism is external and dated: RBI's circular of 5 January 2024, effective 3 May 2024, requires exchange-traded rupee derivative users to have a valid contracted underlying exposure `[SECONDARY: RBI circular, 2024-01-05]`. Proprietary and retail participation — which is what made the segment liquid — became non-compliant, and the order flow did not migrate to a competing venue; it ceased to exist. This is not competitive loss and not cyclical decline. It is a regulator removing the participant class that constituted the market.
S3 EVIDENCE: The four-year currency series above `[AR FY22, MD&A, PDF p73/pr64; AR FY24, MD&A, PDF p54/pr48; AR FY25, MD&A, PDF p52/pr41; AR FY26, MD&A, PDF p58/pr47]`. **The counter-proportion that gives the number meaning:** in FY2018 BSE held **46.3% share** of the currency-derivatives segment, up from 38.09% in FY2017, with 361 participating members including 21 banks `[AR FY18, MD&A, PDF p24/pr17]` — this was BSE's *most successful* competitive segment before Sensex options, and it is the one that reached zero. Share of a market is worth nothing when the market is abolished. Two of five derivative segments (currency, interest-rate) at nil and a third (commodity) at 3% of its FY2023 level is a 40–60% extinction rate over four years.
S4 CONNECTS: Industry — the count of clearing corporations fell from 5 (FY2021/FY2022) to 4 (FY2024–FY2026) and equity-cash exchanges from 5 (FY2019) to 3 `[AR FY19/FY21/FY22/FY24/FY26, MD&A]`, so segment and venue mortality is a feature of this industry, not an accident. Business — BSE's own strategy section still lists commodity derivatives as an opportunity: "a generational business opportunity in India" `[AR FY26, MD&A, PDF p67/pr56]`, written about a segment running at ₹1.08 cr a day. MgmtCommentary — the FY2026 threats section names "industry activity levels decline" and "regulatory changes impacts our ability to compete" as the first two threats `[AR FY26, MD&A, PDF p68/pr57]`, so management does identify the exposure, without sizing it. IncomeStatement — the extinctions are invisible in the FY2026 revenue table because equity derivatives grew faster than they shrank. **The compensating control is diversification into new segments; the class of error it cannot catch is that the same regulator that opens a segment can close it, so segment count is not risk reduction unless the segments have independent regulatory sponsors.**
DOMAINS: Industry, Business, MgmtCommentary, IncomeStatement
DISCONFIRM: Sought evidence the segments could return. The AR gives none: currency derivatives are reported as a single line of nil with no commentary, and interest-rate derivatives disappear from the FY2026 MD&A entirely. Contrary evidence on materiality: none of the three extinguished segments was individually large in revenue terms in its final years, so the realised P&L cost was small — the finding is about the mechanism and its precedent value, not about the rupees lost.
S5 MEANS: A demonstrated 40% four-year extinction rate across BSE's own derivative segments establishes that segment existence, not merely segment share, is a live regulatory variable in this business.
BASE-RATE: **Realised, at this company, twice to zero.** Currency derivatives and interest-rate derivatives, both extinguished within the disclosure window, both with the volume series printed in BSE's own MD&A. In the wider system the same RBI action removed the segment from every Indian exchange simultaneously, and SEBI's October 2024 measures coincided with the first fall in India's annual index-option premium turnover in eight years `[SECONDARY: Business Standard, 2025-04-28]`.
S6 IMPLICATION: Segment diversification cannot be treated as risk reduction in this business, because the segments share one regulator and the record shows that regulator willing to remove a participant class entirely — so the quality of the asset base rests on the durability of a single permitted product rather than on the breadth of the product list. Monitorable: whether the FY2027 MD&A restores a currency or interest-rate turnover line, and whether the commodity segment shows any turnover after the 16 March 2026 SGF-coverage review. Thesis-breaker: a comparable directive touching equity index options — the RBI capital-market-exposure directions effective 1 July 2026 are the nearest live candidate.
SEVERITY: High

### FINDING: Equity-cash realisation fell about 19.5% while BSE's own turnover rose — and management's stated explanation is contradicted by its own disclosure
S1 WHAT: Equity-cash transaction charges fell 18% to ₹25,021 lakh in FY2026 while BSE's own average daily equity turnover **rose** 2.36% to ₹7,950 crore. The MD&A explains the fall as "consistent with industry-wide reduction in average daily turnover value" — a sentence about the industry offered as the explanation for a line whose own volume driver moved the other way.
S2 WHY: With activity up and revenue down, the residual is realisation. Two disclosed FY2026 changes bear on it and the AR attributes the fall to neither: (i) FY2026 is the **first full year** of SEBI's true-to-label uniform per-unit charging, effective 1 October 2024, which removed slab-based volume pricing `[AR FY25, MD&A policy list, PDF p50/pr39]`; (ii) two new surveillance frameworks — the revised ESM from 28 July 2025 and the **AMS from 10 November 2025, which imposes a 1% price band and once-a-week trading on certain BSE-exclusive securities** `[AR FY26, MD&A, PDF p64/pr53]`. BSE-exclusive small caps sit in the groups that historically carried its highest cash transaction charges; the FY2017 MD&A attributes a cash-revenue increase specifically to "increase in transaction charges… in companies listed in XC, XD, XT, Z and ZP group" `[AR FY17, MD&A financial review, PDF p81/pr79 and PDF p83/pr81]`. The AR does not decompose the line, so the split between (i) and (ii) cannot be established.
S3 EVIDENCE: `25,021 / 30,356 = 0.8243` (charges, −17.57%) against `7,950 / 7,766 = 1.0237` (ADT, +2.37%). Realisation per rupee of turnover: `0.8243 / 1.0237 = 0.8052`, **−19.5%** (`DERIVED`, recomputed independently). Sized: had realisation held flat, charges would have been `30,356 × 1.0237 = 31,076 lakh`; the shortfall is `31,076 − 25,021 = 6,055 lakh`, ₹60.55 crore `[AR FY26, MD&A, PDF p58/pr47 and PDF p75/pr64]`. **The counter-proportion that makes this a finding rather than an observation:** in the same year and the same disclosure, **derivatives** realisation per unit of premium **rose 1.8%** while cash realisation fell 19.5% (§3.1). One rate collapsed and one held, inside one company, in one year — so this is not a general repricing of BSE's services.
S4 CONNECTS: MgmtCommentary — the explanatory sentence and the volume sentence sit in the same MD&A, seventeen pages apart, and contradict each other on the direction of BSE's own turnover `[AR FY26, MD&A, PDF p58/pr47 vs PDF p75/pr64]`. Industry — BSE's cash **share** rose from 5–6% to 7–8% over the period `[Q4FY26 Concall, MD&CEO]`, so an industry ADT fall is consistent with BSE's own ADT rising; management's sentence is defensible about the industry and non-responsive about the line it explains. Governance — BSE is the entity that designed and implemented the AMS restriction that plausibly removed its own highest-yield cash turnover, which is the first-line-regulator conflict of overlay §4.3 operating on the revenue line rather than on listing fees. Notes — no Ind AS 115 disaggregation exists, so realisation cannot be tied to an audited figure at all (`records/revenue_disaggregation.md`). **The compensating control is that cash is only 5.6% of standalone revenue (`25,021 / 4,46,951`); the class of error it cannot catch is that the same true-to-label constraint governs derivatives pricing, where the base is 70.1%.**
DOMAINS: MgmtCommentary, Industry, Governance, Notes
DISCONFIRM: Sought a reading under which realisation did not fall. The only one available is a mix shift within cash — a move from high-charge illiquid groups to low-charge liquid ones — which is not a contradiction of the finding but its mechanism. Sought management commentary explaining the fall on any FY2026 concall: none found; the quarterly calls discuss cash **volumes** ("long-term normalized levels of ₹7,645 crores in Q3 FY2026" `[Q3FY26 Concall, MD&CEO]`) and cash **share**, never cash realisation. Two consecutive attempts to source a decomposition failed, so this routes to the gap register.
S5 MEANS: A one-fifth fall in the rate BSE realises on cash turnover, unexplained in the report and unexplainable from the disclosure, shows the transaction-charge rate is not a managed variable even where volumes are growing.
BASE-RATE: **Realised, here, in the year under review** — ₹60.55 crore of foregone charges against flat-realisation. In the StAR MF line the same pattern is present and smaller: revenue per order fell from `23,077 lakh / 66.3 cr = ₹3.48` to `28,490 lakh / 84.1 cr = ₹3.39`, −2.7% (`DERIVED`), while SEBI issued a circular on "Transaction charges paid to Mutual Fund Distributors" on 8 August 2025 `[AR FY26, MD&A policy list, PDF p55/pr44]`. Rate erosion under regulatory uniformity is observable on two of BSE's three transaction-charge lines.
S6 IMPLICATION: Volume growth cannot be read as revenue growth for this issuer, and any model that projects a transaction-charge line from turnover alone will be wrong in the direction of optimism — the rate is a separate, regulator-controlled variable that has moved 19.5% in one year on one line. Monitorable: the FY2027 MD&A equity-cash charge against the FY2027 equity-cash ADT, computed as a ratio; a second consecutive fall would indicate a permanent re-basing rather than a transition effect. Thesis-breaker: the same realisation compression appearing in the derivatives line.
SEVERITY: Medium

### FINDING: The regulator decides which nodes of the chain an exchange may own — BSE was ordered out of the depository and now captures 2.7% of consolidated profit from it
S1 WHAT: SEBI, by letter MRD/DSA/OW/9183/1/2017 dated 24 April 2017, required BSE to reduce its shareholding in Central Depository Services (India) Limited to **24% by 30 June 2017**; BSE divested 26.05% by offer for sale on 29 June 2017, CDSL ceased to be a subsidiary, and the stake has since fallen further to 20% (FY2020) and **15%** (FY2024 onwards).
S2 WHY: SEBI's ownership rules for market infrastructure institutions cap cross-holdings between an exchange and a depository. The mechanism is not a commercial decision by BSE and was not presented as one — the FY2017 note records the obligation and its deadline verbatim. The exchange was removed from the depository node of its own value chain by directive, on a nine-week timetable.
S3 EVIDENCE: The SEBI letter and 24% deadline `[AR FY17, Note on investments, PDF p229/pr227]`; the divestment of 27,217,850 shares, 26.05%, reducing the holding to 24% `[AR FY17, Board's Report, PDF p33/pr31]`; the resulting one-off gain of ₹45,118 lakh consolidated / ₹31,603 lakh standalone `[AR FY18, Board's Report, PDF p17/pr10]`; the step-down to 15% `[AR FY24, AOC-1 Part B, PDF p313/pr307; AR FY26, AOC-1 Part B, PDF p313/pr302]`. **The counter-proportion:** BSE was ordered *out* of the depository but is *permitted* to own the clearing corporation outright — ICCL, 100%, FY2026 PAT ₹16,979 lakh `[AR FY26, AOC-1 Part A, PDF p312/pr301]` against CDSL's equity-method contribution of ₹6,842 lakh `[AR FY26, AOC-1 Part B, PDF p313/pr302]`. Same value chain, adjacent nodes, opposite ownership outcomes — `16,979 / 2,49,698 = 6.8%` of consolidated PAT from the node it may own versus `6,842 / 2,49,698 = 2.74%` from the node it may not (`DERIVED`).
S4 CONNECTS: Governance — the divestment converted a recurring claim on depository economics into a one-time ₹45,118 lakh accounting gain, and the FY2018 PAT attributable of ₹71,128 lakh against ₹19,417 lakh the following year is the distortion that gain created `[AR FY18, PDF p17/pr10; records/trend_10y.csv]`. Industry — the number of depositories has been fixed at two throughout FY2017–FY2026 `[AR FY19/FY21/FY24/FY26, MD&A]`, so this is a stake in a regulated duopoly whose economics BSE no longer directs. Business — the depository leg captures a per-transaction and per-demat-account toll on the same order flow BSE originates, so the economics forgone are correlated with BSE's own volume growth, not independent of it. **The compensating control is that BSE retained the clearing node; the class of error it cannot catch is a future SEBI ownership rule applied to clearing corporations, for which the 2017 depository directive is the precedent.**
DOMAINS: Governance, Industry, Business, Notes
DISCONFIRM: Sought evidence the divestment was value-accretive rather than value-destroying. It is genuinely ambiguous and the ambiguity is recorded: BSE realised ₹45,118 lakh consolidated gain in FY2018 and has retained a 15% stake now contributing ₹6,842 lakh a year, so the transaction was not a loss in cash terms. Also found against the finding: BSE has since reduced the stake voluntarily below the 24% SEBI required (to 20%, then 15%), which indicates its own preference, not only compulsion — the further step-downs are not attributable to the 2017 directive.
S5 MEANS: An exchange's ability to integrate along its own value chain is a regulatory permission rather than a strategic choice, and BSE holds that permission for clearing and does not hold it for depository.
BASE-RATE: **Realised, at this company, with the instrument on file** — the SEBI letter of 24 April 2017 and its nine-week deadline `[AR FY17, PDF p229/pr227]`. Precedent for the same instrument being reused: the December 2025 circular on "Provisions relating to Strengthening Governance of Market Infrastructure Institutions" and the 26 May 2025 circular governing appointment and cooling-off of MII key managerial personnel `[AR FY26, MD&A policy list, PDF p54/pr43 and PDF p56/pr45]` show SEBI continuing to legislate MII ownership, governance and staffing directly.
S6 IMPLICATION: Vertical integration cannot be assumed as an available lever for this business, so any long-horizon compounding case that relies on capturing more of the chain has to be tested against a demonstrated precedent of forced divestment on a nine-week notice. Monitorable: any SEBI consultation paper on MII cross-holdings, particularly one touching exchange ownership of clearing corporations, where BSE's exposure is ₹16,979 lakh of annual PAT. Thesis-breaker: a directive requiring dilution of ICCL.
SEVERITY: Medium

### FINDING: The one node BSE prices freely is the index — bought back from S&P Dow Jones for ₹30 crore, now earning an 82.9% PBT margin on 0.87% of revenue
S1 WHAT: BSE acquired the remaining 50% of Asia Index Private Limited from SPDJ Singapore for ₹3,001 lakh, making it a wholly owned subsidiary effective 1 June 2024; renamed BSE Index Services Private Limited, it earned income from index-related services of ₹38.76 crore in FY2026 (from ₹26.87 crore in FY2025 and ₹14.87 crore in FY2024) with PBT of ₹32.13 crore.
S2 WHY: An index derivative cannot exist without a licence to the index. Until June 2024 BSE shared the economics of its own flagship benchmark with a joint-venture partner while simultaneously building the derivative that monetises it. Buying out the partner removed the only external claim on the input to the product that now produces 70% of revenue. The timing — thirteen months after the 15 May 2023 Sensex derivatives relaunch and four months before SEBI's October 2024 measures — placed the acquisition before the franchise scaled.
S3 EVIDENCE: Consideration ₹3,001 lakh `[AR FY25, Board's Report investments table, PDF p200/pr189]`; effective date 1 June 2024 and prior JV status with SPDJ Singapore `[AR FY25, Board's Report, PDF p24/pr13]`; FY2026 revenue ₹3,876 lakh and PAT ₹2,387 lakh `[AR FY26, AOC-1 Part A, PDF p312/pr301]`; income and PBT series and passive AUM of ₹2,42,114 crore linked to BSE indices `[AR FY26, MD&A, PDF p63/pr52]`. **The asymmetry:** PBT margin `32.13 / 38.76 = 82.9%` — the highest of any disclosed node — against a revenue share of `3,876 / 4,46,951 = 0.87%` of standalone revenue from operations (`DERIVED`). The highest-margin activity in the chain is also the smallest. Payback on the purchase: `2,387 / 3,001 = 79.5%` of the price of half the company recovered in a single year's full PAT.
S4 CONNECTS: Business — index licensing is the only line where the AR describes BSE setting a price on its own initiative, alongside market data, whose growth is attributed partly to "a revision in international pricing" `[AR FY26, MD&A, PDF p63/pr52]`. Industry — the same asset is the barrier to entry in §4.1: BSE's ownership of the Sensex is what makes the derivative unassailable by a third venue, and NSE's ownership of the Nifty is what makes it unassailable by BSE. MgmtCommentary — management names indices as a strategic focus, "We have created 60 new indices… there is a good amount of demand" `[Q1FY27 Concall, MD&CEO]`, and BISPL launched over 30 new indices serving 350+ clients in FY2026 `[AR FY26, MD&A, PDF p67/pr56]`. Notes — BISPL paid an interim dividend of ₹15 crore, ₹75 per share, to the parent in FY2026 `[AR FY26, MD&A, PDF p63/pr52]`, so the cash is fungible upward. **The compensating control on the concentration risk of F3 is that BSE now owns the index outright; the class of error that cannot catch is regulatory — SEBI's 30 October 2025 eligibility criteria for derivatives on non-benchmark indices constrain which owned indices may carry a derivative at all.**
DOMAINS: Business, Industry, MgmtCommentary, Notes
DISCONFIRM: Sought evidence the price paid signals a low valuation of the asset by the seller. It does: ₹3,001 lakh for 50% of a business that generated ₹20.47 crore of PBT in FY2024 `[AR FY25, MD&A index section, PDF p55/pr44]` is roughly three times that half-share of profit, which is either an exceptionally favourable purchase or evidence that a pre-agreed exit mechanism governed the price. Neither the FY2025 nor FY2026 AR discloses the valuation basis. Also found against over-weighting this node: at 0.87% of revenue it cannot move the case on its own, and its growth is a derived function of the derivatives franchise it supports rather than an independent driver.
S5 MEANS: BSE has exactly one node where it sets its own price, and it acquired full control of that node for a sum equal to about one year of its subsequent profit — which is the strongest single piece of evidence that pricing power in this chain is a property of owned intellectual assets, not of market position.
BASE-RATE: **No realised loss found** at this node — the index business has been profitable in each disclosed year (PBT ₹20.47 crore FY2024, ₹25.56 crore FY2025, ₹32.13 crore FY2026). The relevant systemic precedent runs the other way: index licensing is the highest-margin revenue line at every major global exchange group, and the risk historically realised is regulatory constraint on *which* indices may carry derivatives, which SEBI imposed on 30 October 2025 `[AR FY26, MD&A policy list, PDF p54/pr43]`.
S6 IMPLICATION: The quality of the asset base is better than a transaction-charge business implies, because the group owns the intangible that makes its principal product possible — but the node is too small to change the earnings profile, so it belongs in the durability assessment rather than in the growth case. Monitorable: BISPL revenue and passive AUM linked to BSE indices, disclosed annually in the MD&A; and whether the valuation basis of the ₹3,001 lakh acquisition is ever disclosed. Thesis-breaker: a SEBI eligibility rule that disqualifies Sensex-family indices from carrying derivatives.
SEVERITY: Watch

### FINDING: Customer concentration is not disclosed and cannot be — but one participant's removal halved a single expiry's premium turnover
S1 WHAT: BSE reports a single operating segment under Ind AS 108 with a geographic revenue split and **no major-customer disclosure** in either the consolidated or standalone FY2026 notes. Separately, SEBI's interim order of 3 July 2025 restrained the Jane Street group and impounded ₹4,843.57 crore; on the first BSE index-options expiry after the order, 8 July 2025, premium turnover was ₹19,683 crore against ₹44,010 crore on the 24 June 2025 expiry.
S2 WHY: Concentration in an index-options book is not a customer-relationship fact but a liquidity fact: a small number of market-making and high-frequency participants supply the quotes against which retail premium is transacted. Removing one changes the width of the book, and the premium that trades across it, immediately. Because no member reaches 10% of *revenue*, Ind AS 108.34 never triggers, so the disclosure that would size the exposure is not merely absent — it is not required.
S3 EVIDENCE: Segment note with geography only, within India ₹5,08,140 lakh and outside India ₹6,670 lakh, and no major-customer paragraph `[AR FY26, Note 39, PDF p228/pr217]`. The expiry-day fall `19,683 / 44,010 = 0.4472`, **−55.3%** `[SECONDARY: Business Standard, 2025-07-10]`, with the order and quantum `[SECONDARY: SEBI interim order, 2025-07-03]`. **The counter-proportion:** against ~610 members and ~650 FPIs participating `[Q1FY27 Concall, MD&CEO]` and 1,190 cumulative membership applications since April 2010 `[AR FY26, MD&A, PDF p63/pr52]`, the member *count* implies diffusion while the volume response to one removal implies the opposite. Count and effect point in opposite directions, and the effect is the truer measure. Management's own participation targets confirm the gap: FPI contribution to BSE volumes is "around 5% to 6%" against market-wide "around 9%", with a target of 9% `[Q4FY26 Concall, MD&CEO]`.
S4 CONNECTS: Notes — the absence of the Ind AS 108.34 disclosure means no audited statement of concentration exists at any threshold. MgmtCommentary — management repeatedly frames its strategy as concentration reduction: "deepening and broadening of markets", "we cannot have monopoly structures. We cannot have concentration" `[Q3FY25 Concall, MD&CEO]`, and measures itself on member and FPI counts rather than volume. Industry — the same event hit NSE harder in absolute terms, with weekly-expiry index-option premium turnover falling from ₹80,731 crore on 26 June 2025 to ₹45,884 crore on 10 July 2025 `[SECONDARY: Business Standard, 2025-07-10]`, so the concentration is a market structure feature rather than a BSE-specific weakness. Governance — SEBI's intraday position-limit framework of 1 September 2025, capping intraday net FutEq exposure at ₹5,000 crore per entity, exists precisely because "several incidents in which entities created outsized intra-day FutEq positions" occurred `[AR FY26, MD&A policy list, PDF p55/pr44; SECONDARY: SEBI/HO/MRD/TPD/CIR/P/2025/122]` — the regulator has independently confirmed that single-entity size was material. **The compensating control is the growing member and FPI count; the class of error it cannot catch is that added members are small — management's own words, "these are all small members… I don't think so" they add runway `[Q4FY26 Concall, MD&CEO]`.**
DOMAINS: Notes, MgmtCommentary, Industry, Governance
DISCONFIRM: Strong contrary evidence found and it matters. The shock did not persist: FY2026 closed with options premium ADT up 117.5% `[AR FY26, MD&A, PDF p58/pr47]`, and management stated five weeks after the order that "we are not seeing any specific impact arising out of Jane Street" `[Q1FY26 Concall, 2025-08-13]`. The premium/notional ratio *improved* 28.6% across the same year (§3.1), which is the opposite of what a permanently thinner book would produce. The single-day figures are SECONDARY-sourced and cannot alone carry the conclusion; they are used here only to establish that a single-participant sensitivity exists and is large, which SEBI's own position-limit framework independently corroborates.
S5 MEANS: The concentration that matters in this business is in liquidity provision rather than in revenue, so it is structurally invisible in the financial statements and observable only in the market's response to a regulatory event.
BASE-RATE: **Realised, market-wide, within the last fifteen months.** The July 2025 episode is the instance, and it produced a measurable one-expiry effect at both exchanges `[SECONDARY: Business Standard, 2025-07-10]`. The system-level precedent is broader: SEBI's October 2024 measures on contract size, upfront premium and expiry-day margins were addressed at the same participant class and coincided with the first annual fall in India's index-option premium turnover in eight years `[SECONDARY: Business Standard, 2025-04-28]`.
S6 IMPLICATION: The earnings stream depends on a small set of liquidity providers whose size the financial statements will never reveal, so a reader cannot size this exposure from the filings and must treat the disclosure gap itself as part of the required margin of safety. Monitorable: the FPI share of BSE volumes, which management discloses on calls (currently 5–6%, target 9%), and any further SEBI enforcement action against a large algorithmic participant. Thesis-breaker: a second single-entity restraint whose volume effect persists beyond one quarter.
SEVERITY: High

---

## 9. Gap register additions

Per doctrine §9, each entry names the document that would answer it.

| # | Gap | What is missing | Peers disclose? | Question for the next call |
|---|---|---|---|---|
| W2-G1 | Trading-member concentration | Top-10 member share of transaction charges → `NOT-DISCLOSED -> Ind AS 108.34 major-customer disclosure, or a voluntary member-concentration table; neither exists in the AR FY2026 consolidated or standalone notes` | No — no Indian exchange discloses it | "What share of FY2026 equity-derivatives premium turnover came from your ten largest members?" |
| W2-G2 | Equity-cash realisation decomposition | The split of the 19.5% realisation fall between true-to-label uniformity, surveillance-driven mix shift and rate changes → `NOT-DISCLOSED -> an MD&A rate/volume bridge for the equity-cash transaction-charge line, absent from AR FY2026 PDF p75/pr64` | No | "Of the 18% fall in equity-cash transaction charges, how much is rate and how much is mix?" |
| W2-G3 | Deutsche Börse market-data agreement | Term, revenue share, exclusivity scope, termination → `NOT-DISCLOSED -> the October 2013 cooperation agreement, never filed and never summarised in any AR FY2017–FY2026` | n/a | "What are the term and renewal terms of the Deutsche Börse international distribution arrangement?" |
| W2-G4 | BISPL acquisition valuation basis | How ₹3,001 lakh for 50% was determined → `NOT-DISCLOSED -> a business-combination valuation note or a related-party/JV exit-mechanism disclosure; neither appears in AR FY2025 or FY2026` | n/a | "On what basis was the consideration for the remaining 50% of Asia Index determined?" |
| W2-G5 | Listing-fee internal inconsistency | MD&A p63/pr52 reports annual listing fees of ₹242 cr; MD&A p75/pr64 reports a listing-fee line of ₹38,861 lakh (₹388.61 cr). The ₹146.61 cr difference is unlabelled → `NOT-DISCLOSED -> an audited Ind AS 115 disaggregation of the listing-fee line, which does not exist (records/revenue_disaggregation.md)` | Yes — exchanges elsewhere disaggregate initial vs annual listing revenue | "What comprises the ₹388.61 crore listing-fee line beyond the ₹242 crore of annual listing fees?" |

---

## 10. Handoffs

- **W3_revenue** — §3.1 supplies the activity/realisation decomposition the overlay mandates for
  derivatives (+117.5% activity, +1.8% realisation) and cash (+2.37% activity, −19.5% realisation).
  W2-G2 is the unresolved half. Do not compute a realisation series from the audited notes: no Ind AS 115
  disaggregation exists (`records/revenue_disaggregation.md`).
- **W3_balancesheet** — ICCL's 85.4% other-people's-money ratio (§1.4) is the segregation test.
- **W3_costs** — the SEBI regulatory fee tracks **notional** turnover, not revenue (§3.1). Model it off
  notional, not off the top line.
- **W4_capalloc** — the CDSL step-downs (24% → 20% → 15%) are capital-allocation decisions after the 2017
  directive, and the BISPL buyout is the one integration BSE was permitted to make. Both belong there.
- **W5_earnings_quality** — F5's story-versus-numbers contradiction is a fact about management's
  presentation, not about the business, and should be weighed with `waves/W2_promise.md`.
- **W7_bear_case** — F3 and F4 are the structural spine: one product, one expiry day, a 40% four-year
  segment-extinction rate, and a levy base the company does not control.

---

## 11. Sources

**Primary.** BSE Limited annual reports FY2017–FY2022, FY2024–FY2026 (`data/text/`), MD&A and AOC-1
sections as cited, with printed-page offsets from `waves/W1_docmap.md` §0.1. BSE quarterly earnings-call
transcripts, 13 Aug 2024 to 10 Aug 2026 (`data/concall_text/`).

**Secondary** (each tagged inline; none carries a conclusion alone, per doctrine §1a-iii):
NSE Q4FY26 results as reported, 5 May 2026 · SEBI circular SEBI/HO/MRD/TPD-1/P/CIR/2024/132 of
1 Oct 2024 · SEBI circular SEBI/HO/MRD/TPD/CIR/P/2025/122 of 1 Sep 2025 · SEBI interim order in the
matter of index manipulation by Jane Street Group, 3 Jul 2025 · SEBI press release on the Common
Contract Note with single VWAP, Jul 2025 · RBI circular on exchange-traded currency derivatives,
5 Jan 2024 · Business Standard, 28 Apr 2025 and 10 Jul 2025 · Business Today citing Jefferies,
3 Jul 2026 · business-press reporting on MSEI's 2024–2026 fundraising and January 2026 relaunch.
