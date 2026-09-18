# W7 — The bear case: BSE Limited (NSE: BSE)

**Agent:** W7_bearcase. **Date:** 2026-09-08. **Price basis:** ₹3,409.80, 4-Sep-2026
`[NSE Bhavcopy, 2026-09-04]`. **Doctrine:** `ANALYSIS_DOCTRINE.md` §1a (six steps), §1a-i (asymmetry),
§1a-ii (base rate — mandatory), §1b (three domains, one non-statement), **§1c (this file may not contain
a recommendation or a target price presented as certainty; it may state durability, margin of safety,
monitorables with triggers, thesis-breakers, and what the price implies)**, §1f (lead with the
conclusion), §10 (nothing deleted).

**Inputs consumed.** `waves/W7_redflags.md` as the authoritative register (36 rows, gate verdict
**PROCEED**), all 22 files in `waves/`, all 20 files in `records/`. **This file inherits W7_redflags'
verdict and does not reopen it.** No flag is upgraded here, no Critical is smuggled in, and the eleven
W8 constraints in `W7_redflags.md` §7 bind every number below.

**Page-cite convention.** `PDF pN / prN` — PDF page of the file in `data/text/`, then printed folio,
offsets per `records/printed_page_offsets.json`: FY2017 +2 · FY2018 +7 · FY2019 +9 · FY2020 +7 ·
FY2021 +5 · FY2022 +9 · FY2023 +7 · FY2024 +6 · FY2025 +11 · FY2026 +11.

**Basis discipline (W5 constraint 5).** Every ratio below names *standalone* or *consolidated* and
*as-first-reported* or *as-restated*. The two headline multiples are on different share counts and both
are stated: `DERIVED: 3,409.80 / 60.61 = 56.26x` on **audited consolidated** EPS struck on **issued**
capital of 41,19,79,077 shares, and `DERIVED: 3,409.80 x 40,78,84,077 / 100000 = 1,39,08,031 lakh;
1,39,08,031 / 2,49,698 = 55.70x` market capitalisation to **PAT attributable**, on **paid-up** capital
`[records/capital_structure.md]`, `[AR FY26, Consolidated P&L, PDF p164/pr153]`.

---

# 0. THE BEAR CASE IN FIVE LINES

1. **FY2026 was a redistribution, not a market.** The two-venue income pool grew `DERIVED: 23,861.10 /
   22,413.31 = +6.46%`; BSE grew 59.1% and `DERIVED: (1,911.79 − 1,447.79 x 0.1444) / 1,911.79 = 89.07%`
   of its increment is share taken, not market created — and the share was handed over by a SEBI circular
   that converted NSE's advantage in *number* of weekly expiries into a one-each allocation. What a
   circular allocates, a circular re-allocates; BSE's own share fell to 32.4% in June 2026 on nothing
   more than a competitor's extra expiry week.
2. **The margin is the quotient of two exogenous ratios and the cost base only ratchets one way.**
   Premium/notional moved `0.081126% → 0.104315% = +28.58%` on the year and swings **±37% inside eight
   quarters**; reversion merely to the Q2FY26 level already printed in this cycle removes **₹38,535
   lakh** of revenue, while a 20% cut in *every* discretionary cost layer — never once achieved — recovers
   **₹3.10 per ₹100** against a reversion that removes **₹38.82 per ₹100**.
3. **Growth came on a shrinking contract base, which is the base the cost runs on.** Contracts fell
   `DERIVED: 114.5 / 122.5 = −6.53%` while revenue rose 63.46%; ex-levy cost elasticity is `+0.094` on
   premium, `+0.159` on notional and **`−1.682` on contracts**, and in all three windows where turnover
   actually fell costs rose **14.68%, 30.64% and 17.56%**.
4. **What the winnings became is a 4.42% bond portfolio.** `DERIVED: 5,22,509 / 6,67,301 = 78.30%` of
   shareholders' capital earns 4.42% after tax inside a business whose exchange engine earns
   `DERIVED: 2,15,055 / 1,10,285 = 195.02%`; the payout regime inverted from **24.21×** own-account free
   cash flow to **21.20%** of it in the exact three years the cash arrived, and ten annual reports carry
   no dividend policy.
5. **At 56.3× on a peak-cycle base, the price requires BSE to become larger than the entire Indian
   exchange income pool is today.** On a 12% required return, a 10-year horizon and a 25× exit,
   `ESTIMATE: 60.61 x (1 + g)^10 = 3,409.80 x 1.12^10 / 25` solves to **g = 21.5%**, which puts FY2036
   revenue at ₹33,786 cr against a pool growing at the observed 6.46% to ₹44,622 cr — **75.7% of it**,
   from 21.58% today.

> **The one-sentence version.** BSE is not being priced as a toll-booth on Indian equities; it is being
> priced as a compounding franchise — and the three things that produced FY2026 (an expiry slot, a
> volatility ratio and a competitor's stumble) are none of them owned, none of them priced by BSE, and
> two of them measurably reversible inside a single month.

**What this bear case is NOT.** It is not an accounting case. `W7_redflags.md` §6 establishes that in
ten years **zero rupees of realised loss at BSE is attributable to an accounting-quality channel**, and
that finding is accepted here in full. Anyone arguing against this company on the numbers being false is
arguing the wrong case. The numbers are true. The question is whether they repeat.

---

# 1. WHERE I DEPART FROM THE BRIEF'S RANKING

The brief supplied a ranking and asked that it be tested rather than inherited. Four changes, each with
its reason.

| Brief's rank | My rank | Change | Why |
|---|---|---|---|
| **1** concentration is a regulatory allocation | **1** | **merged with the brief's #2** | The revenue *share* and the revenue *rate* are not two exposures. Revenue runs on premium; the levy runs on notional; the clearing cost runs on contracts. All three are set outside the company, and the first two move **together**: when premium/notional falls, revenue falls and the levy does not. Ranking them separately understates the case, because the risk is **multiplicative and same-signed**, not additive. |
| **2** the margin is a market-structure ratio | — | folded into 1 | See above. Kept as the *sizing* limb of limb 1 rather than a limb of its own. |
| **3** negative operating leverage on contracts | **2** | unchanged in position | Correct and, I would argue, the sharpest single mechanism in the corpus. It is what converts limb 1 from a revenue event into a P&L collapse. |
| **6** capital allocation, ₹1 → ₹1.04 | **3** | **promoted from 6th to 3rd** | It is the **only limb that bites even if the bull case is entirely right about volumes.** Limbs 1 and 2 need something to go wrong. This one is already happening, is fully disclosed, and is management's own decision. At a 1.78% earnings yield the market is paying for compounding; the marginal rupee compounds at 4.42%. |
| **5** cash conversion 0.712 | **4** | merged with 3 as its input | 0.712 is a *measurement* correction, not an economic loss — `W7_redflags.md` §4.4 is right that the money is in the bank. Its bear function is that it halves the free cash flow against which limb 3's payout ratio is judged, and re-prices the multiple from ₹64.21 to ₹44.01 of cash per ₹100. It is not a separate mechanism. |
| **4** the stall | **5** | **demoted one place** | It is one quarter, Q1 is seasonally distinct, and year-on-year it is still `DERIVED: 1,56,602 / 95,839 = +63.4%`. As *evidence* it is thin. As a **dated trigger** it is the best thing in the file, and it is carried as the primary monitorable rather than as a finding. |
| **7** 58.5% to a regulator or the tax code | **6** | reframed as an amplifier | It is not an independent limb — it is the multiplier that turns a revenue reversion into a profit collapse, because 58.48% of what leaves the ₹100 cannot be cut by anyone at BSE. Its one independent edge is **direction**: the regulator's share of the leak rose from 48.77% to 58.48% **in the year of peak profitability**. |
| **8** the disclosure perimeter | **7** | **reframed, not demoted** | As a governance indictment it is weak and `W7_redflags.md` §6 is right to bound it — realised cost approximately nil, five accounting defects run *against* the company, an unbroken same-day disclosure record. Its real bear function is **epistemic**: every series a bear would need to track limbs 1–3 in real time is either withdrawn (Bankex, market share, the index chart, the market-price table, the inter-CCP guarantee) or was never disclosed (contract counts, the audited product split, the ICCL clearing rate, the >10% customer). **A thesis whose monitorables have been deleted cannot be falsified quickly, and that is a margin-of-safety fact, not a morality one.** |

**One limb the brief does not contain, and it is my third finding.** The treasury book is not a
valuation cushion. Marking it at book and marking CDSL at market makes the multiple on the operating
exchange **worse**, not better: `DERIVED: (1,39,08,031 − 5,22,509 − 3,50,932) / 2,15,055 = 60.61x` against
a headline 55.70×. A pool earning 4.42% after tax inside a share priced at `DERIVED: 1,39,08,031 / 6,79,550
= 20.47x` book dilutes; it does not protect. And the one down-cycle on the record proves it operationally
as well as arithmetically — see §2.5.

---

# 2. THE MECHANISM, LIMB BY LIMB

Each limb states four things and nothing else: **what breaks · through what channel · over what horizon ·
what observable event tells the reader it has started.**

## 2.1 LIMB 1 — The franchise is a redistribution authored by a circular, and it is priced by three bases BSE does not set

**What breaks.** ~65–70% of revenue, on one product, on one index, on a weekly expiry day the regulator
assigns — and a margin that is the quotient of two of the three bases.

**The channel, stated as arithmetic rather than as a worry.** Management describes it himself:
*"the SEBI turnover fee is based on the notional trading, the clearing expense is based on the number of
contracts, and we earn revenue based on premium"* `[Q4FY26 Concall 13May2026, MD & CEO]`. Those three
quantities moved as follows in FY2026 `[AR FY26, MD&A, PDF p58/pr47]`, `[Q1FY27 IP 04Aug2026, PDF
p14/slide 13]`:

| Base | What it drives | FY2025 | FY2026 | Change |
|---|---|---:|---:|---:|
| **Premium** ADT (₹ cr) | **revenue** | 8,978 | 19,523 | **+117.45%** |
| **Notional** ADT (₹ cr) | **the SEBI levy** | 1,10,66,674 | 1,87,15,375 | **+69.11%** |
| **Contracts** — avg daily lots (Mn) | **clearing cost** | 122.5 | 114.5 | **−6.53%** |

`DERIVED: 19,523 / 8,978 = 2.174538` · `1,87,15,375 / 1,10,66,674 = 1.691202` · `114.5 / 122.5 =
0.934694`. The premium base grew **48.33 percentage points faster** than the levy base
(`117.45 − 69.12`), and that gap is the whole of the margin gain. It is implied volatility and moneyness.
It is not a decision.

**Size it three ways, ascending.**

- The verified, already-observed reversion: to the **Q2FY26** ratio of 0.091491% — a level printed
  *inside this cycle, two quarters before the peak* — costs
  `DERIVED: 3,13,437 x (1 − 0.091491 / 0.104315) = 38,535` lakh of revenue at unchanged notional turnover
  `[Q1FY27 IP 04Aug2026, PDF p14/slide 13]`. That is `DERIVED: 38,535 / 3,29,914 = 11.68%` of FY2026 PBT.
- The levy-side mirror: the levy was worth `DERIVED: 33,123 / 1,41,554 = 23.40%` of derivatives revenue
  in FY2025 and `DERIVED: 55,625 / 3,13,437 = 17.75%` in FY2026 — a **5.65pp** swing worth
  `DERIVED: 3,13,437 x 0.0565 = 17,709` lakh `[AR FY26, Standalone Note 27, PDF p287/pr276]`.
- Full reversion to the FY2025 ratio: `ESTIMATE: 3,13,437 x (1 − 0.081126 / 0.104315) = 69,676` lakh of
  revenue, on the assumptions that notional turnover, the charge rate, the contract count and every cost
  line are unchanged. On those assumptions PBT falls `ESTIMATE: 69,676 / 3,29,914 = 21.12%` and PAT
  attributable falls to `ESTIMATE: 2,49,698 − 69,676 x 0.7503 = 1,97,420` lakh, EPS to
  `ESTIMATE: 1,97,420 x 100000 / 41,19,79,077 = ₹47.92`, and the trailing multiple at an unchanged price
  **rises to 71.2×**.

**The volatility is measured, not assumed.** Premium/notional by quarter:
`Q1FY26 0.115144% · Q2FY26 0.091491% · Q3FY26 0.092662% · Q4FY26 0.118044% · Q1FY27 0.124959%`
`DERIVED` from `[Q1FY27 IP 04Aug2026, PDF p14/slide 13]`. Range
`DERIVED: 0.124959 / 0.091491 = 1.366` — **±37% inside eight quarters**, against a +28.58% annual move.
The annual series understates the exposure; the quarterly series is the honest one.

**The share is a calendar, and the calendar has moved three times in 21 months.**
SEBI's framework of **1-Oct-2024** limited each exchange to **one weekly expiry on one benchmark index**
`[AR FY25, MD&A policy list, PDF p50/pr39]`, converting an incumbency advantage in *number* of weekly
products into a symmetric one-each allocation. BSE then moved Sensex weekly expiry **Friday→Tuesday on
3-Jan-2025** and **Tuesday→Thursday on 1-Sep-2025** `[Q3FY25 Concall]`, `[Q2FY26 Concall slide]`,
`[Q3FY26 Concall, MD & CEO]`; each move required regulatory approval, and the IFSCA approval for the
mirror change was itself a disclosed event on **17-Jul-2025** `[AR FY26, MD&A, PDF p62/pr51]`.
Management publicly misidentified the expiry slot as an exclusive moat and then grew fastest after moving
onto the competitor's day — two agents reached that independently (RF-020).

**And ~95% of it sits in two weeks.** Premium arising outside the current and next expiry week is
*"around 5%"* of volumes `[Q3FY26 Concall, MD & CEO]`. Carried against it, and it matters: contracts
outside those weeks are *"5 times more"* than January 2025 and premium *"almost 10 times"*
`[Q1FY27 Concall, MD & CEO]` — the two statements are one year apart and the corpus does not reconcile
them.

**The base rate — and this is the limb's strongest fact, not its weakest.** §1a-ii asks whether the
pattern has ever cost money. **It has, twice, at this company, inside the window.**
(i) **Extinction:** RBI's **5-Jan-2024** ETCD directions took BSE's currency-derivative ADT from
**₹9,733.67 cr → ₹1,525.34 cr → nil** in two years; interest-rate derivatives are at nil from FY2025;
commodity derivatives sit at 3% of their FY2023 level — *two of five derivative segments legislated to
zero in four years, a 40% four-year segment-extinction rate*, and none of it competitive
`[AR FY26, MD&A, PDF p58/pr47]`, `[AR FY25, MD&A, PDF p52/pr41]`, `[AR FY22, MD&A, PDF p73/pr64]`.
(ii) **Failure to hold:** BSE has attempted an equity-derivatives franchise **four times before and
failed every time.** Equity derivatives ran at **498 contracts per day in FY2017, 182 in FY2018 and 126
in FY2019** after LEIPS was discontinued `[AR FY2018, MD&A, PDF p24/pr17]`,
`[AR FY2019, MD&A, PDF p77/pr68]`; LEIPS, LES from 1-Sep-2018, the LES relaunch of 26-Aug-2019 and the
Sensex-50 Friday expiry of 29-Jun-2020 produced ADTs of ₹1,062 cr (FY2020) and ₹1,40,804 cr (FY2021)
that **did not hold** `[AR FY2020, MD&A, PDF p82/pr75]`, `[AR FY2021, MD&A, PDF p71/pr66]`.
**It took roughly ten years and at least four attempts before May-2023 worked.** The base rate for "BSE
sustains a derivatives franchise" is 1 in 5, and the one success is three years old.

**Horizon.** Immediate and continuous. The ratio re-prices every quarter; the calendar re-prices on a
circular with weeks of notice; the segment risk re-prices on a directive, and the precedent for that had
roughly two months' notice.

**Observable triggers.**
- BSE's index-option premium share falling below 30% for two consecutive months. *Note the source
  limitation: the 32.4% June-2026 reading is `[SECONDARY: Business Today/Jefferies, 2026-07-03]` and
  under §1a-iii cannot alone carry a conclusion. The primary-source corroborant for the same month is
  BSE's own filing: revenue from operations `DERIVED: 1,56,602 − 1,56,351 = 251`, **+0.16% QoQ**
  `[Q1FY27 Results 04Aug2026, consolidated quarterly filing, PDF p5]`.*
- Any SEBI circular reallocating expiry days, placing both venues on the same day, or removing weekly
  expiries. No such circular is scheduled or disclosed.
- Premium/notional printing below 0.09% for two consecutive quarters in the Average Daily Lots slide
  `[Q1FY27 IP 04Aug2026, PDF p14/slide 13]`. **Next check: the Q2FY27 investor presentation.**

## 2.2 LIMB 2 — The cost base is a ratchet, and the growth came on the base the cost runs on

**What breaks.** The margin, faster than revenue, because costs do not follow turnover down and 58.48%
of what leaves the ₹100 cannot be cut by anybody at BSE.

**The channel.** Operating leverage at BSE **has no single value**, and which value you get is chosen by
which base you divide by — on the *same* cost base and the *same* year
`[AR FY26, Consolidated P&L, PDF p164/pr153]`, `[Q1FY27 IP 04Aug2026, PDF p14/slide 13]`:

| Cost base | vs premium (+117.45%) | vs notional (+69.11%) | **vs contracts (−6.53%)** |
|---|---:|---:|---:|
| Total expenses (+24.10%) | 0.205 | 0.349 | −3.690 |
| **Ex-levy expenses (+10.99%)** | **+0.094** | **+0.159** | **−1.682** |

`DERIVED: 10.99 / 117.45 = 0.094` · `10.99 / 69.11 = 0.159` · `10.99 / (−6.53) = −1.682`. **A 1.776-point
spread, sign included, on one year's trades.** Any single operating-leverage figure quoted for this
company is a choice presented as a measurement.

**The asymmetry, which is the finding.** `W7_redflags.md` §5 #9 corrects the absolute claim and I carry
the correction: costs **have** contracted once, by 4.07% in FY2021 — verified like-for-like on one
audited page, `53,070 against 55,320` `[AR FY2021, Consolidated P&L, PDF p146/pr141]` — **in a year
equity-cash turnover ROSE 56.84%** `[AR FY2021, MD&A, PDF p101/pr96]`. The surviving claim is the
narrow one and it is the one that matters: **costs have never fallen in a year turnover fell.** In all
three windows on record they rose:

| Window | Turnover (equity-cash ADT) | Total expenses | Elasticity |
|---|---|---|---:|
| FY2018 → FY2019 | 4,402 → 3,127 = **−28.96%** | 42,346 → 48,563 = **+14.68%** | **−0.507** |
| FY2018 → FY2020 | 4,402 → 2,676 = **−39.21%** | 42,346 → 55,320 = **+30.64%** | **−0.781** (−0.613 restated) |
| FY2022 → FY2023 | 5,396 → 4,132 = **−23.42%** | 60,045 → 70,591 = **+17.56%** | **−0.750** |

`[AR FY2019, MD&A, PDF p77/pr68]`, `[AR FY2020, MD&A, PDF p82/pr75]`, `[AR FY2022, MD&A, PDF p73/pr64]`,
`[AR FY24, MD&A, PDF p53/pr47]`, `[records/trend_10y.csv]`. **Absolute total expenses rose in nine of the
ten years read.**

**The asymmetry sized — this is the arithmetic the bear case turns on.** Only **₹15.48 of every ₹100** of
revenue is discretionary annual spend (`DERIVED: (29,781 + 20,313 + 24,732) / 4,83,395 = 15.479`). A 20%
cut across every one of those layers — deeper than anything in the record — recovers
`DERIVED: (29,781 + 20,313 + 24,732) x 0.20 = 14,965` lakh, i.e. **₹3.10 per ₹100**. A reversion of
revenue merely to the FY2025 level removes `DERIVED: (4,83,395 − 2,95,734) / 4,83,395 = 38.82%`, i.e.
**₹38.82 per ₹100**. **The entire discretionary lever, pulled harder than it has ever been pulled,
covers one-twelfth of the hole** (`DERIVED: 38.82 / 3.10 = 12.5x`)
`[AR FY26, Consolidated P&L, PDF p164/pr153]`.

**And two layers cannot be cut at all** — the Core SGF contribution and depreciation already committed —
`DERIVED: 1.5921 + 3.2884 = ₹4.88` per ₹100. The forward cost floor is the ex-levy run-rate of
**₹1,18,773 lakh**, plus roughly **₹1,212 lakh** of depreciation already committed from FY2026 additions
(`DERIVED: 1,05,539 x 16.21% = 17,108; 17,108 − 15,896 = 1,212`), less **₹1,301 lakh** of non-recurring
gratuity past-service cost `[AR FY26, Note 43, PDF p233/pr222]`.

**The realised precedent, because §1a-ii demands one.** Cost-to-income went from **61.6% in FY2019 to
87.8% in FY2020** on a 14.44% turnover fall, and to **74.0% in FY2023** on a 23.42% fall
(`DERIVED: 55,320 / 63,000 = 87.8%`) `[records/trend_10y.csv]`. This has happened, at this company,
twice, in the last seven years.

**The efficiency claim that would rebut it does not survive the base change.** The MD&A calls the FY2026
clearing-cost fall *"a sustainable structural efficiency gain"* `[AR FY26, MD&A, PDF p76/pr65]`. One cost,
three published magnitudes: consolidated **−19.45%**, standalone **−4.56%** (the one the MD&A quotes),
grossed-up for the intra-group charge **−3.04%** — and `DERIVED: 5,496 / 6,770 = 81.18%` of the
consolidated fall is the ICCL intra-group charge rising `DERIVED: 12,607 / 7,111 = +77.29%` and
eliminating `[AR FY26, Standalone Note 35, PDF p298/pr287]`. **On the contract base management itself
names as the cost driver, clearing cost per contract ROSE 3.74%**
(`ESTIMATE: (40,642 / 41,916) / 0.934694 = 1.037351`).

**Horizon.** One to two quarters behind any turnover fall. The evidence that it is already tightening is
dated: ex-levy cost elasticity to notional went **0.159 (FY2026) → 0.513 (Q1FY27)**
(`DERIVED: 34,391 / 24,308 = +41.48%` of cost against `237 / 131 = +80.92%` of notional) — controllable
costs now capture **half** of turnover growth against **one-sixth** in the annual accounts
`[Q1FY27 Results 04Aug2026, consolidated quarterly filing, PDF p5]`.

**Observable triggers.**
- A quarter in which ex-levy expenses fall while notional turnover falls. **This test fired once and
  failed on inspection**, and it is recorded because a thesis-breaker that fires and survives scrutiny is
  worth more than one that never fires: Jun-2026 expenses read −3.64% on notional −3.27%, but stripping
  the ₹40 cr clearing-subsidiary provision it reads **+3.82% against −3.27%, elasticity −1.168.** The
  ratchet is intact.
- Ex-levy cost elasticity to notional printing above 0.60 for two consecutive quarters.
- Clearing cost per contract, grossed up, rising for a second consecutive year. **Next check: the FY2027
  annual report against the Q4FY27 Average Daily Lots slide.**

## 2.3 LIMB 3 — The compounding a 56× multiple pays for does not exist at the margin

**What breaks.** Nothing in the P&L. This limb is the one that bites **even if limbs 1 and 2 never
happen**, and that is precisely why it is ranked third rather than sixth.

**The channel.** The company is two businesses with a 44-to-1 spread in return across a 5-to-1 spread in
weight `[AR FY26, Consolidated Balance Sheet, PDF p163/pr152]`, `[AR FY26, Note 23, PDF p211/pr200]`,
`[AR FY26, Note 8, PDF p188-189/pr177-178]`:

| Pool | ₹ lakh | share of equity attributable | after-tax return |
|---|---:|---:|---:|
| **Securities and bank deposits, net of float repayable** | **5,22,509** | **78.30%** | **4.42%** |
| Operating assets of the exchange | 1,10,285 | 16.53% | **195.02%** |
| CDSL associate, at equity-method carrying value | 44,940 | 6.73% | 15.22% |
| Other associates and residual net operating liabilities | (10,433) | (1.56%) | n/m |
| **Equity attributable** | **6,67,301** | **100.00%** | **37.42%** |

`DERIVED: (6,14,282 + 3,71,074) / 2 = 4,92,678; 29,030 / 4,92,678 = 5.89%; 5.89% x (1 − 0.2497) = 4.42%`
and `DERIVED: 2,49,698 − 29,030 x 0.7503 − 17,142 x 0.7503 = 2,15,055; 2,15,055 / 1,10,285 = 195.02%`.

**On the capital management actually controls, ₹1 is becoming ₹1.04 a year** — 4.42% on the treasury book
and `DERIVED: 3,517 / 83,442 = 4.21%` on the subsidiary portfolio at cost
`[AR FY26, Standalone Note 7, PDF p267/pr256]` — inside a business earning 195%.

**Sized as return foregone.** One year's retention of ₹1,76,486 lakh costs **1,129 basis points of ROE**:
`DERIVED: 2,48,725 / 6,79,550 = 36.60%` as retained against
`DERIVED: (2,48,725 − 1,76,486 x 4.42%) / (6,79,550 − 1,76,486) = 2,40,923 / 5,03,064 = 47.89%` if
distributed. The accumulated pile costs **10,707 basis points**:
`DERIVED: (2,48,725 − 5,22,509 x 4.42%) / (6,79,550 − 5,22,509) = 2,25,630 / 1,57,041 = 143.67%`.
**The reported ROE of 43.75% is a decaying number by construction**, falling roughly 1,100bp for each
further year of retention at current rates, independently of anything that happens to volumes.

**The direction of travel is accelerating, not stabilising.** Own-account financial assets went from
`DERIVED: 3,71,074 / 4,42,373 = 83.88%` of equity attributable at FY2025 to
`DERIVED: 6,14,282 / 6,67,301 = 92.06%` at FY2026 — **+8.18pp in one year** — and
`DERIVED: 2,43,208 / 2,24,928 = 108.13%` of the entire FY2026 increase in shareholders' equity went into
the securities book. **₹6.68 of financial asset for every ₹1 of operating asset**
(`DERIVED: 2,43,208 / 36,412 = 6.68`).

**The payout regime inverted exactly when the money arrived** `[W4_capalloc §1.3]`,
`[AR FY26, Statement of Changes in Equity, PDF p167-168/pr156-157]`:

| | FY2017–FY2023 (7y) | FY2024–FY2026 (3y) |
|---|---:|---:|
| Own-account free cash flow | ₹6,854 lakh | **₹3,30,683 lakh** |
| Returned to shareholders | ₹1,65,964 lakh | ₹70,094 lakh |
| **Returned ÷ own-account FCF** | **24.21×** | **21.20%** |
| Returned ÷ profit attributable | 88.60% | **15.23%** |

`DERIVED: 1,65,964 / 6,854 = 24.21` · `70,094 / 3,30,683 = 21.20%`. **88.98% of the decade's operating
cash was earned in the last three years and 29.69% of its distributions were made in them.** Payout ratio
went `98.9% (FY2021) · 95.1% (FY2022) · 99% (FY2023) · 27.3% (FY2024) · 28.0% (FY2025) · 17.65% (FY2026)`
— **an 81.2 percentage-point fall in three years**, with **no dividend policy in any of ten annual
reports.** Every listed peer in `W2_peers.md` publishes one.

**And the explanations do not survive.** Regulatory floors are `DERIVED: 20,100 / 6,79,550 = 2.96%` of
equity — 97.04% surplus `[AR FY26, Note 35, PDF p222/pr211]`. Capital trapped at ICCL is
`DERIVED: 9,067 / 1,76,486 = 5.1%` of the year's retention. The capital-expenditure cycle is smaller than
the dividend: `DERIVED: 41,198 / 35,932 = 1.15x`. Legal capacity is `DERIVED: 4,55,828 / 41,198 = 11.07x`
`[AR FY26, Standalone Note 15, PDF p280/pr269]`. **Management's 13-May-2026 denial of an analyst's
"4–4.5% post-tax" premise is falsified by the two statements he invited the questioner to read** — the
answer is 4.42%, 0.08pp from the midpoint of the premise he rejected `[Q4FY26 Concall 13May2026, MD & CEO]`.

**The base rate on discretionary deployment.** `DERIVED: 20,919 / 3,001 = 6.97x` more capital into India
International Exchange — **ten consecutive loss years, ₹24,023 lakh cumulative loss, nil ever
returned**, the tenth tranche of ₹4,128 lakh paid in the tenth loss year — than into BSE Index Services,
which returned `DERIVED: (1,200 + 1,500) / 3,001 = 89.97%` of its purchase price in dividends within 24
months `[AR FY26, Form AOC-1, PDF p312/pr301]`, `[AR FY26, Standalone Note 7, PDF p267/pr256]`.

**Horizon.** Continuous and cumulative; roughly 1,100bp of ROE per year of retention.

**Observable triggers.**
- FY2027 payout below 20% of own-account free cash flow with capex under ₹600 cr, for a fourth
  consecutive year. **Next check: FY2027 annual report, Note 15 and the Board's Report.**
- The ratio of the annual increase in own-account financial assets to the annual increase in equity
  attributable staying above 100%. It was 108.13% in FY2026; **a reading below 60% would be the first
  evidence a capital programme is absorbing the retention.**
- Any further tranche into India INX.

## 2.4 LIMB 4 — The ₹100 the shareholder owns is ₹44.01 of cash, not ₹64.21

**What breaks.** Nothing in the accounts — this limb re-prices the multiple rather than reducing the
earnings. It is carried because it is the input to limb 3, not because it is a separate mechanism.

**The channel.** BSE consolidates its clearing corporation, so members' margins and settlement
obligations move through group cash and appear inside operating activities. Both ₹100 maps are struck on
the **same divisor** of ₹4,833.95 lakh per ₹1 `[W4_cash §2]`:

| Step | Map A, headline | Map B, own-account | Gap per ₹100 |
|---|---:|---:|---:|
| Revenue | 100.00 | 96.45 | 3.55 |
| **Working-capital absorption** | **+12.13** | **(5.41)** | **17.54** |
| **CFO** | **64.21** | **44.01** | **20.20** |
| Capex | (10.66) | (7.43) | 3.23 |
| **FCF** | **53.55** | **36.58** | **16.97** |
| **CFO / PAT** | **1.248** | **0.902** | **0.346** |

`DERIVED: 64.21 − 44.01 = 20.20`; the working-capital swing is `12.13 − (5.41) = 17.54`, i.e.
`17.54 / 20.20 = 86.8%` of the gap. **The sign flips**, and no amount of scaling produces a sign flip.
Inside the ₹72,767 lakh working-capital inflow: `DERIVED: 24,251 + 44,937 = 69,188; 69,188 / 72,767 =
95.08%` is members' and the government's money against `72,767 − 69,188 = 3,579` — **4.9%** — of the
company's own, **a ratio of 20.3 to 1** `[AR FY26, Note 16, PDF p206/pr195]`,
`[AR FY26, Note 19, PDF p208/pr197]`.

**Over ten years it is 0.712, and every bound was tested.** Cumulative own-account CFO ₹4,61,513 lakh
against cumulative PAT ₹6,48,302 lakh = **0.712**, against a printed **1.272**. Bounds: **0.825** ex three
one-off disposal gains · **0.609** also stripping government float · **0.667–0.757** across a ±10%
float-passthrough assumption · **0.874** on a five-year window · **0.896** on the last three years.
**Nothing in the range reaches parity.** Capitalising the reported series overstates by
`DERIVED: 1.272 / 0.712 − 1 = 78.7%` at worst and `1.272 / 0.825 − 1 = 54.2%` at best.

**Why this is a re-pricing and not a fraud, stated plainly.** The construction closes on the balance
sheet — modelled own-account financial-asset build ₹2,43,159 lakh against actual
`DERIVED: 6,14,282 − 3,71,074 = 2,43,208`, residual **49 lakh, 0.02%**. The money is in the bank. The
defect is a caption, and `W7_redflags.md` §4.4 is right that it does not stop the process.

**The forward hook.** The float is not a permanent asset: bucket (C) **fell** in FY2018, FY2019, FY2021,
FY2023 and FY2025 by **26,468 · 34,863 · 19,322 · 31,928 · 26,993** lakh respectively, and in each of
those years reported CFO was negative or near zero while profit was positive
`[AR FY26, Note 16, PDF p206/pr195]` and each prior year's own Note 16. Its ten-year mean of roughly
₹1,50,000 lakh against **₹3,55,423 lakh at FY2026** means the reversal potential is about two-thirds of
one year's PAT — of *printed* cash flow, not of profit.

**Horizon.** Immediate for valuation; the float reversal is unpredictable and has occurred in five of ten
years.

**Observable triggers.**
- The own-account construction failing to close on the balance sheet within 1% in any year — which would
  falsify the correction itself and is recorded as a falsifier of the bear case, not of the company.
- The FY2027 consolidated cash flow either restoring the pre-FY2025 presentation or quantifying the
  eleven-word basis change. **Next check: FY2027 annual report, consolidated cash flow footnotes.**

## 2.5 LIMB 5 — The stall, and the two shock absorbers that fail together

**What breaks.** The assumption that the treasury book cushions a trading downturn.

**The channel — and this is the fact the bull case has no answer to.** In the one clean down-cycle on the
ten-year record, **both engines failed in the same year.** FY2019 → FY2020: revenue from operations was
flat (`45,030 → 45,051`), investment income fell `DERIVED: 15,866 / 20,218 − 1 = −21.5%` and by FY2021 to
`DERIVED: 12,908 / 20,218 − 1 = −36.2%`, and **PAT attributable fell
`DERIVED: 12,227 / 19,417 − 1 = −37.0%` on flat operating revenue** `[records/trend_10y.csv]`. Market
capitalisation of all listed companies fell `DERIVED: 113.5 / 151 = −24.8%` over the same window
`[AR FY2019, MD&A, PDF p68/pr59]`, `[AR FY2020, MD&A, PDF p77/pr70]`. **A downturn that hits turnover
hits the yield on the corpus at the same time and through the same cause.** The 78.30% of capital in
limb 3 is not a hedge against limb 1; it is correlated with it.

**The dated evidence that the operating engine has already flattened.** Jun-2026 revenue from operations
`DERIVED: 1,56,602 − 1,56,351 = 251`, **+0.16% QoQ**, after nine quarters averaging well into double
digits. The PBT bridge ties to the rupee with zero residual: of `+10,021`, investment income
`DERIVED: 7,349 / 10,021 = 73.34%`, non-repeat of the ₹40 cr clearing-subsidiary provision
`DERIVED: 3,687 / 10,021 = 36.79%`, **operating top line `DERIVED: 251 / 10,021 = 2.50%`** — the two
non-operating items are **110.1%** of the increase `[records/quarterly_series.md]`.

**And the second-largest contributor is worth naming, because of who the counterparty is.** The ₹40 cr
whose non-repeat supplies 36.79% of the profit increase is an expected-credit-loss provision at the
clearing subsidiary against *"an outstanding of Rs. 80 crore, which is an old outstanding from NSE"*
`[Q4FY26 Concall 13May2026, MD & CEO]` — a **50.0% provisioning rate** on a balance that is
`DERIVED: 80 / 32 = 2.5x` an entire quarter's ICCL clearing revenue, and that had not been mentioned in
any of the **nine preceding earnings calls**, over a period in which management publicly complained about
NSE Clearing's charges in **five** of them. The largest single credit event in the ten-year record is a
receivable from the competitor whose share this company took.

**And the metric was substituted.** Management presented it as *"the 14th consecutive quarter of record
revenues, ₹1,707 crores"* `[Q1FY27 Concall 10Aug2026, MD & CEO]`. That figure is **total income**
(₹1,70,672 lakh against ₹1,63,017 lakh), and `DERIVED: 7,349 / 7,655 = 96.0%` of its increase is
investment income. The claim is true on the metric chosen and would be false on revenue from operations —
the metric the same company uses everywhere else.

**Underneath it, every disclosed realisation series is now flat or negative.** Equity-derivatives
realisation `DERIVED: (11,550 / 11,279) / (2,96,154 / 2,89,207) = 1.000006`, **+0.001% QoQ**, and
`0.983726`, **−1.63% YoY**, after +1.83% in FY2026; equity-cash realisation **−13.93% YoY**; StAR MF per
order `DERIVED: 733 / 234 = ₹3.132` against `612 / 183 = ₹3.344`, **−6.33%**
`[Q1FY27 IP 04Aug2026, PDF p14-16/slides 13-15]`.

**Horizon.** One to two quarters. **The bear must say plainly what this is and is not:** it is **one
quarter**, Q1 is seasonally distinct, year-on-year the quarter is still
`DERIVED: 1,56,602 / 95,839 = +63.4%`, and no realised loss attaches to it. It is the **trigger**, not
the finding.

**Observable triggers.**
- A second consecutive quarter of sequential revenue-from-operations growth below 2%. **Next check: the
  September-2026 quarterly filing, expected early November 2026.**
- The FY2027 accounts arriving with revenue from operations below FY2026's ₹4,83,395 lakh.

## 2.6 LIMB 6 — The regulator takes 58.48% of the leak and its share is rising

**What breaks.** The convertibility of any revenue gain into a profit gain, in both directions.

**The channel.** Of the ₹54.84 that leaves every ₹100 of revenue
(`DERIVED: 106.4988 − 51.6551 = 54.844`), **₹32.07 is levy, Core SGF or tax**
(`DERIVED: (64,969 + 7,696 + 82,384) / 4,83,395 = 32.075`), i.e. **58.48%**
(`DERIVED: 32.075 / 54.844 = 58.48%`). Only **₹15.48** is discretionary annual spend — **barely more than
the ₹15.03 of levy plus Core SGF that cannot be touched at all**
`[AR FY26, Consolidated P&L, PDF p164/pr153]`.

**The direction is the finding.** The regulator-and-tax share of the leak was
`DERIVED: (13.8794 + 3.0433 + 14.5810) / 64.5992 = 48.77%` a year earlier. **Total leakage fell 9.76
points per ₹100 while the regulator's share of what remains rose 9.71 points.** Growth made BSE more
profitable and more regulator-dependent in the same year.

**The levy is a turnover tax on a base 959× the base BSE bills on**
(`DERIVED: 1,87,15,375 / 19,523 = 958.6`), and it is permanent: `DERIVED: 64,969 / 4,83,395 = 13.44%` of
revenue, `DERIVED: 64,969 / 1,83,742 = 35.4%` of total expenses — **the largest single expense in the
group** `[AR FY26, Note 27, PDF p212/pr201]`. Against the peer control, BSE pays **11.71%** of revenue in
turnover-linked regulatory fees against NSE's **4.80%** — `DERIVED: 11.71 / 4.80 = 2.44x` — earning
`₹8.54` of revenue per ₹1 of levy against NSE's `₹20.85` `[AR FY26, Note 27, PDF p212/pr201]`,
`[NSE AR FY26, Consolidated P&L, PDF p140/pr318]`.

**And the block is about to get bigger by management's own voluntary policy.** The Core SGF contribution
was disclosed on a call — **5% of transaction revenue monthly, capped at 150% of the minimum** — and
appears nowhere in the FY2026 annual report. At policy that is `DERIVED: 3,79,499 x 5% = 18,975` lakh a
year against ₹7,696 lakh charged, **2.47×**, i.e. `DERIVED: 18,975 / 4,83,395 = ₹3.93` of the ₹100
instead of ₹1.59 `[Q2FY26 Concall 17Nov2025, MD]`, `[AR FY26, Note 22, PDF p211/pr200]`. **That moves the
regulator-and-tax block from ₹32.07 to roughly ₹34.41 per ₹100 and removes about ₹11,279 lakh a year of
pre-tax profit from any forward base** — and W5 already binds W8 to model it that way.

**The realised base rate, and it is three events in three years.** SEBI's re-basing of the levy to
notional retrospective to FY2007 with 15% penal interest (**₹7,347 lakh** as adjudicated, 9.52% of FY2024
consolidated PAT); RBI's ETCD directions that extinguished the currency segment; and the equity-cash
repricing that cost **₹6,054 lakh** of revenue on **rising** volume
(`DERIVED: 30,356 x 1.023693 = 31,075; 31,075 − 25,021 = 6,054`) `[AR FY26, MD&A, PDF p58/pr47 and PDF
p75/pr64]`. **The regulator has moved money at this company three times in three years, always in the
same direction.**

**Horizon.** Continuous, with a circular's notice.

**Observable triggers.**
- The FY2027 note either restoring a SEBI regulatory-fee reconciliation or not. FY2026 carries **no
  SEBI-fee note at all**, in the year the item rose 70.8%.
- The quarterly Core SGF charge against 5% of that quarter's transaction charges, and whether the 150%
  cap is reached. Q1FY27 annualises at `DERIVED: 2,591 x 4 = 10,364` against ₹7,696 lakh for FY2026,
  **+34.67%, on flat sequential operating revenue.** **Next check: Q2FY27 results.**
- Any SEBI circular fixing the levy base to premium rather than notional — which would **kill this limb
  and half of limb 1**.

## 2.7 LIMB 7 — Every series this bear case needs has either been withdrawn or never existed

**What breaks.** Not value — **falsifiability**. This limb does not claim management is dishonest, and
`W7_redflags.md` §6 forbids that reading: realised cost of the pattern to date is approximately nil, five
accounting defects run against the company's own interest, and the same-day disclosure record is unbroken
across 477 announcements including an adverse ICCL order told to the tape at **22:43 the same night**.

**The channel is narrower and sharper than "reducing transparency".** Match the seven withdrawn or absent
disclosures against the seven limbs above:

| To monitor | The reader needs | Status |
|---|---|---|
| Limb 1 — concentration | An audited product split of revenue | **Never disclosed.** Zero of four Ind AS 115 disclosures against **4 of 4 peers publishing the timing split**; on the dominant line specifically, **NSE and IEX split it and MCX does not** — NSE gives Cash/Futures/Options/MF/Others *inside the audited note* `[NSE AR FY26, Note 27, PDF p159-160/pr314-317]`. The ~70% concentration is **MD&A-only and unaudited** |
| Limb 1 — market share | Bankex and market-share metrics | **Withdrawn** from six concalls and three decks (RF-018) |
| Limb 1 — the price of BSE's own equity | The Schedule V Part C 9(d)/(e) market-price table and index charts | **Withdrawn after FY2024.** The last month-wise series BSE published for its own shares covers Apr-2023 to Mar-2024 `[AR FY2024, CG Report, PDF p92/pr86]` — 29 months stale |
| Limb 2 — cost per unit | Contract counts | **Never in any annual report.** Reconstructible only from an investor-presentation slide, which is an L3 metric and not an L1 |
| Limb 2 — the clearing charge | The ICCL clearing rate per contract or any pricing basis | **Never disclosed**; AOC-2 declared "not applicable" `[AR FY26, Board's Report, PDF p31/pr20]` |
| Limb 1 — single-participant risk | The >10% customer | **Acknowledged, never quantified** `[AR FY26, Note 39.2, PDF p228/pr217]`; no Ind AS 108.34 trigger arises, so it is not merely absent — it is **not required** |
| Clearing-subsidiary exposure | The inter-CCP guarantee | **₹10,60,000 lakh removed and the FY2025 comparative actively restated to ₹24 lakh**, with no Ind AS 1.41 or 8.49 disclosure. The phrase "bank guarantee" occurs nowhere in FY2026 |

**The asymmetry that makes it a pattern rather than a staffing problem** (W6's verdict, endorsed here):
BSE's **accounting** defects run *against* its interest — five of them, including a basis change that
cut the prior-year cash-flow comparative by ₹19,857 lakh — while its **disclosure deletions** run *with*
it in every establishable case. Inside one note: Auction charges of ₹60 lakh
(`DERIVED: 60 / 4,83,395 = 0.012%` of revenue) carry their own audited caption while **78.51% of revenue
is one line** `[AR FY26, Note 22, PDF p211/pr200]`. **Granularity was added exactly where it was
immaterial and withheld exactly where it decides the case.**

**And the trend is adverse without any accounting change.** Transaction charges as a share of revenue
went `DERIVED: 58,271 / 1,39,003 = 41.92%` (FY2024) → `2,02,993 / 2,95,734 = 68.64%` (FY2025) →
`3,79,499 / 4,83,395 = 78.51%` (FY2026) — **+36.59 percentage points in two years.** The disclosure did
not deteriorate; **the business concentrated into the part of the disclosure that was already blank.**

**And the spoken channel does not fill the gap, because it is systematically strongest exactly where it
matters least.** Across 53 scoreable claims made between 5-Feb-2024 and 4-Aug-2026, management's hit
rate is `DERIVED: 32.5 / 53 = 61.3%`. Split by type, the rate is not one number:

| Claim type | Hit rate | What it covers |
|---|---:|---|
| **Action** — something BSE controls and will build | `DERIVED: 21.5 / 33 = 65.2%` | racks, members, product launches, platform builds |
| **Reassurance** — a number BSE does not control, offered to close an analyst's question | `DERIVED: 4 / 12 = 33.3%` | Core SGF, the SEBI levy, cost run-rates, clearing charges |

**A 2.0× gap** (`DERIVED: 65.2 / 33.3 = 1.96`), and seven of the eight reassurance misses were
optimistic. The consequence is measurable rather than rhetorical: **the company's three largest P&L
swings in the window — the ₹199 cr Q3FY25 Core SGF charge, the ₹109 cr Q4FY25 reversal and the ₹170 cr
Q4FY24 SEBI provision, together ₹478 cr = `DERIVED: 478 / 1,326 = 36.0%` of FY2025 profit — all landed in
categories management had expressly declined to size.** `DERIVED: 33 / 53 = 62.3%` of the claims were
input promises and they explain **0%** of the earnings variance `[W2_promise §b]`.

**Nor is there guidance to fall back on.** Across eleven transcripts, seven decks and the quarterly
filings, **no numeric forward guidance on revenue, margin, volumes, Core SGF or cost was issued once** —
*"any projection whatsoever in respect of any segment you ask, any number of times, any number of
investors, the answer has to be same"* `[Q3FY24 Concall 07Feb2024, MD]`. Core SGF projectability was
refused **eight times across six calls**, ending *"I have already clarified it three times. I'll clarify
it for the fourth time"* — and then management published a precise formula, 5% of transaction revenue
monthly capped at 150% of the minimum, the moment it chose to `[Q2FY26 Concall 17Nov2025, MD]`. **What was
declared unknowable for seven quarters turned out to be manageable by policy, so the refusal was a choice
rather than a constraint** — which is the same fact about the perimeter, in the second channel.

**Horizon.** Permanent, and it compounds: each further year of concentration puts more of the case inside
the unsplit line.

**Observable triggers.**
- The FY2027 report carrying an Ind AS 115 disaggregation note, or reconciling the MD&A product split to
  an audited total.
- The FY2027 corporate-governance report restoring the market-price table; the FY2027 related-party note
  restoring the two employee-benefit trusts.
- **The disconfirming trigger, which must be watched as hard:** a year in which a growing or adverse item
  **retains** its disclosure would put the direction test on the other side. Colocation revenue was
  refused in Aug-2025 and then disclosed quarterly from Nov-2025 **and retrospectively for FY25** — the
  set is not monotonically narrowing.

---

# 3. WHERE THE BULL CASE IS RIGHT

Nine disconfirming items are on the record. All nine are serious. Each is stated at full strength, then
answered — and where it cannot be answered, that is said.

> **The instruction this section exists to satisfy, written by W6 and addressed to this file directly:**
> *"§4's two-part verdict is the governance input: the pattern is real **and** its realised cost is
> approximately nil. **A bear case that uses the first without the second is overstated; one that uses
> the second without the first is a false clean.**"* `[W6_gov_synth §7.4]`

## 3.1 Zero rupees of realised loss from an accounting channel in ten years — **CONCEDED IN FULL**

Every realised loss in the window has a non-accounting channel: the FY2020 SEBI ISF/IPF plough-back
(₹1,861 lakh, regulator), the FY2021 S&P Dow Jones award (₹1,453 lakh, counterparty), the FY2024
retrospective levy (₹7,347 lakh, regulator), SEBI penalties FY22–FY26 (₹833 lakh =
`DERIVED: 833 / 2,48,725 = 0.33%` of one year's PAT), receivable write-offs (₹1,535 lakh over three
years), India INX (₹20,919 lakh, capital allocation), and the currency segment (regulator). **Not one is
an accounting event.** No qualification in nine years; CARO FY2026 records no fraud, no ADT-4, no auditor
resignation, no borrowings, no preferential allotment ever.

**The concession is total, and it defines this file.** The bear case here is a **durability** case, not a
trust case. It runs entirely on numbers the company published and the auditor signed. If the reader's
objection to BSE is that the accounts are wrong, the reader is arguing against the evidence.

## 3.2 Five accounting defects run against the company's own interest — **CONCEDED, and it moves my own multiple down**

The FY2024 CFO restatement **cut** reported cash flow by ₹19,857 lakh; the ECL re-estimate is net
conservative by ₹879 lakh against the ₹809 lakh the under-6-month rate cut gives back; buildings moved to
the **shorter** 25-year life; the voluntary Core SGF policy **permanently reduces** profit by about
₹11,279 lakh a year; and **the headline EPS management leads with is the lower number** — ₹56.27
standalone against an audited consolidated ₹60.61.

**The consequence runs in the company's favour and is applied.** Because the audited number is the higher
one, this file strikes its multiple at `DERIVED: 3,409.80 / 60.61 = 56.26x` and not at the ₹56.27 basis
that would give `DERIVED: 3,409.80 / 56.27 = 60.60x`. **A register of five conservative errors is not the
register of a company managing earnings, and no part of this bear case rests on one.**

## 3.3 The buybacks are worth +18.9% of today's share price — **CONCEDED, and it is the strongest single bull fact in the corpus**

Three programmes retired 88,70,407 shares for ₹65,837 lakh
(`DERIVED: 20,19,170 + 67,64,705 + 86,532 = 88,70,407`); on today's basis that is
`DERIVED: (20,19,170 + 67,64,705) x 9 + 86,532 x 3 = 7,93,14,471` shares.

> **QC note, §4b, and it is minor.** `W4_capalloc.md` prints this as **7,93,13,471** and carries the
> counterfactual count as 48,71,97,548. Recomputed independently here the string gives
> `DERIVED: 87,83,875 x 9 = 7,90,54,875; 86,532 x 3 = 2,59,596; 7,90,54,875 + 2,59,596 = 7,93,14,471`
> — **1,000 shares higher, 0.0013%.** It changes nothing that carries a conclusion: the counterfactual
> price is ₹2,868.4 on either count and the uplift is +18.87% on either. Both figures stay on the record
> per §10; the load-bearing outputs are unaffected and the source's version is the one downstream
> artifacts already carry.

The honest counterfactual — not the flattering one — is that the count today would be
`DERIVED: 40,78,84,077 + 7,93,13,471 = 48,71,97,548` and equity value ₹1,39,080 cr + ₹658 cr, i.e.
`DERIVED: 1,39,738 / 48,71,97,548 = ₹2,868.4` per share against the actual ₹3,409.80 — **+18.87%**, worth
`DERIVED: 541.40 x 40,78,84,077 = ₹22,083 crore` for continuing holders against ₹658 crore paid. And
`DERIVED: 3,50,932 lakh` of CDSL value against a ₹12,795 lakh cost basis is **36.9×** on total value
created. Over the decade **₹1 unambiguously became more than ₹1**, and incremental ROCE FY2016→FY2026 is
**56.96%**.

**Three answers, and the first two are the ones that matter.**

**(a) It is a historic result, and my limb is specifically about the current regime.** All three buybacks
predate the money. `DERIVED: 4,497 + 12,300 + 47,620 = 64,417` lakh of the ₹65,837 lakh was spent
FY2018–FY2020, when own-account free cash flow for the whole seven-year era was ₹6,854 lakh. The FY2024
programme achieved **2.49% take-up** and the route is now arithmetically closed — a repeat must clear at
`DERIVED: 3,409.80 / 360.00 = 9.47x` the last offer price. **BSE was an outstanding allocator when it had
no money and has been a poor one since it has had plenty.** That claim survives the buyback fact intact,
and it is narrower and better-evidenced than "bad allocator".

**(b) The ₹22,083 crore is a mark-to-market on the multiple this file disputes, not a cash return.** It is
`541.40 × 40,78,84,077` at ₹3,409.80. If the multiple halves, so does the number. Counting it as
realised value while arguing the price is demanding would be double-counting.

**(c) The CDSL result was not a decision.** **Not one CDSL step was discretionary** — the FY2018 sell-down
was compelled by SEBI's letter MRD/DSA/OW/9183/1/2017, the FY2024 sell-down was *"to meet the requirement
of SEBI directive"*, and SEBI's 15% cap means the stake **cannot be increased**
`[AR FY26, Note 8, PDF p188/pr177]`, `[AR FY25, Note 52, PDF p218/pr207]`. `DERIVED: 91,131 / 93,178 =
97.8%` of ten years of exceptional income is this one stake. **BSE has been a forced seller throughout and
is now a forced holder.** That is a fine outcome and a thin basis for underwriting the next decade's
allocation.

## 3.4 The levy mismatch moved in BSE's favour by ₹16,402 lakh — **CONCEDED, and conceding it strengthens the bear case**

Had the fee been assessed on premium at the same effective yield, the FY2026 standalone levy would have
been `DERIVED: 33,123 x 2.17450 = 72,027` against an actual ₹55,625 lakh — **₹16,402 lakh more**. The
FY2026 delta decomposes **101.7% volume, −1.7% rate**, and the levy **fell** as a share of revenue,
13.88% → 13.44%. `W7_redflags.md` §4.2 is right: the wedge is a **level** exposure, not a growth driver.

**The answer is that a symmetric exposure is not a benign one when it sits at 13.44% of revenue.** The
same ratio move that handed BSE ₹16,402 lakh of levy relief in FY2026 hands it back on reversion, and it
does so **at the same time as** the revenue it flattered disappears. That is the whole of the mechanism in
limb 1: the two effects are **same-signed on the way down**. A level exposure of 13.44% of revenue, at
2.44× the peer's burden per rupee of revenue, is exactly what converts a 22% revenue reversion into a 21%
PBT fall. **I take the concession and use it.**

## 3.5 FY2020–FY2023 and FY2025 carry no restatement; the credit loss is one named debtor; ECL is net conservative by ₹879 lakh — **CONCEDED, and the receivables limb is dropped**

Twenty-six restatement movements across the corpus contain exactly **two** earnings restatements, one of
them mechanical. Every bucket beyond one year is 100% provided in FY2026; over-six-month provisioning went
`53.72% → 98.43%`; write-offs fell `827 → 452 → 256`. On the measure that normalises for the exit
run-rate, gross receivable days are **38.0 against 37.5** — half a day. The ₹40 crore charge is one named
counterparty at the clearing subsidiary.

**No part of this bear case rests on receivables.** `W7_redflags.md` §3.4 applied the downgrade on
adequacy and I apply it here. The residue — Note 34's liquidity table carrying `30,967 / 475` while Notes
10 and 11 carry `28,778 / 2,664` — is a preparation-quality defect that stays High in the register and is
**not a bear limb**.

## 3.6 BSE took share off NSE under identical rules — **CONCEDED as a genuine competitive result, and answered in three parts**

**The result, at full strength.** Under identical rules, identical STT and identical RBI directions, NSE's
consolidated total income fell 2.4% and PAT 15.5% while BSE's rose 59.1% and 88.3%. The combined pool grew
`DERIVED: 23,861.10 / 22,413.31 = 6.46%` and BSE's share went
`DERIVED: 3,236.31 / 22,413.31 = 14.44%` to `5,148.10 / 23,861.10 = 21.58%`, **+714bp**. Decomposed:
share-neutral growth would have given BSE `DERIVED: 1,447.79 x 0.1444 = 209.05` cr of the
`5,148.10 − 3,236.31 = 1,911.79` cr increment, so **`DERIVED: (1,911.79 − 209.05) / 1,911.79 = 89.07%` —
nine-tenths — is share taken.** This is not luck and this file does not pretend it is. On equity-derivative
transaction-charge revenue specifically, BSE went `DERIVED: 1,415.54 / 13,336.83 = 10.61%` to
`3,134.37 / 14,612.04 = 21.45%`, **+10.84pp** `[SECONDARY: NSE Q4FY26 results as reported, 2026-05-05]`,
`[NSE AR FY26, Note 27, PDF p159-160/pr314-317]` — and the NSE half is SECONDARY-sourced from a private
company's results release, so under §1a-iii it cannot alone carry a conclusion in either direction.

**(a) Naming the mechanism is what settles durability, and the mechanism is a circular.** W2_industry's own
verdict: SEBI's 1-Oct-2024 measures *"converted an incumbency advantage in number of weekly products into
a symmetric one-each allocation… A rule intended to restrain speculation redistributed order flow."* The
share gain rode the expiry calendar; management publicly misidentified the slot as an exclusive moat and
then grew fastest after moving onto the competitor's day; and the share fell to 32.4% in a single month on
an extra competitor expiry week. **A share won on a calendar is held on a calendar.** W2_industry's own
handoff says the base/bear/bull spread on this name is *"a function of a regulatory calendar rather than of
execution."*

**(b) A redistribution is a different asset from market growth, and the price is being struck as if it
were market growth.** The pool grew 6.46%. Redistribution is zero-sum and bounded above by the pool;
market growth is not. §4 below shows what happens to the arithmetic when you extrapolate a redistribution.

**(c) The share gain has no pricing follow-through, and that is the test that separates a moat from an
allocation.** In the year BSE took 714bp of share: realisation was a **drag** on the aggregate at
`DERIVED: 5,622 − 783 − 6,054 = −1,215` lakh, **−0.65%** of the increase; contracts **fell 6.53%**;
equity-cash realisation fell **19.48%** on rising volume; StAR MF realisation fell **2.67%**; and
`DERIVED: 1,73,176 / 1,87,661 = 92.28%` of the increase was activity. **The only line where realisation
rose is listing fees, at +4.01%, and it is 8.04% of revenue.** A franchise that wins share prices better.
This one won share and priced worse in four of its five disclosed lines.

**Where I cannot answer it.** The share gain is real, it was large, and there is no evidence in the corpus
that it has reversed on any measure other than one SECONDARY-sourced month. **A reader who believes the
expiry calendar will not move again is entitled to weight this heavily against everything above**, and
this file records that a reasonable analyst does so.

## 3.7 FY2026 added disclosure; the same-day record is unbroken — **CONCEDED, and limb 7 is bounded by it**

FY2026 added a reasonable-assurance report on BRSR Core, a full discontinued-operation disposal table and
a new Clearing and Settlement footnote. Every adverse event across **477 NSE announcements** in 2024–2026
was disclosed the day it occurred, including the ICCL order at **22:43 the same night**. Colocation revenue
was refused in Aug-2025 and then disclosed quarterly from Nov-2025 **and retrospectively**. One of the five
original disclosure-narrowing limbs was withdrawn as false by the producing agent itself.

**Accepted without qualification.** *"Reducing transparency"* is too strong and is not adopted here.
`W7_redflags.md` establishes **direction, not intent**, on five of seven instances, and limb 7 is written
on that footing: it is a **monitorability** cost that widens the required margin of safety on specific
voluntary disclosures, not a governance verdict.

## 3.8 Two further items the bear case must carry, because they cut hard and are not on the brief's list

**(i) BSE is the least regulatory-capital-intensive exchange-plus-clearing group in the peer set.**
Core SGF per ₹1 of revenue: **BSE ₹0.258 · NSE ₹0.788 · MCX ₹0.594** — BSE is lighter than NSE **by a
factor of three** `[AR FY26, Note 41, PDF p232/pr221]`, `[NSE AR FY26, Note 41, PDF p169]`. On the flow it
is starker: incremental regulatory capital per ₹1 of incremental revenue is
`DERIVED: 11,423 / 1,87,661 = ₹0.061` against cash capex of `51,516 / 1,87,661 = ₹0.275`. **Any bear
reading that BSE's growth is capital-hungry is refuted**, and this file does not make one. It makes the
opposite point — the capital is not needed, which is precisely why holding it at 4.42% is a choice.

**(ii) On money, BSE's supervision record is the best in the peer set.** Penalties as a share of own PAT:
**BSE 0.010% · NSE 13.50% · CDSL 0.66% · MCX 0.09% · IEX nil**. NSE paid ₹643.05 cr in FY2025 and ₹40.35
cr in FY2026 with ₹1,391.21 cr provided; BSE's three-year realised cost including the ICCL order is
**₹8.33 cr = 0.33% of FY2026 PAT.** BSE also runs **6 of 8 = 75% Public Interest Directors** with a
mandatory PID chairperson, against CDSL's 54.54% and IEX's zero. **This is strong disconfirming evidence
against reading BSE's supervision record as an outlier, and it ships.**

*The counter-proportion, which is what keeps it from being a clean bill.* The record is best on
**penalties**, which are the smallest regulator-authored number in the entire case, and it is the largest
that has ever moved money — the levy at 11.71% of revenue, a segment abolished, an equity-cash repricing.
And the penalties that did land have **one address**: strip the two items that are not about running an
exchange, and every remaining SEBI action against the group is a failure of the regulatory, supervisory or
IT-resilience function — Karvy (member inspection), the ICCL ₹5.05 cr (IT asset inventory and
disaster-recovery correspondence), the ₹25 lakh (dissemination, client-code modification, error-account
monitoring). **Three orders, three different years, one function** — and it is the one function that had
**no board-level owner** at the 7-May-2026 corporate-governance report date, with all three SEBI-mandated
vertical Executive Directors unappointed and the Chief Regulatory Officer reporting to the MD & CEO
`[AR FY26, CG Report, PDF p79/pr68]`. Between FY2019 and FY2021 — precisely the window spanning the Karvy
default and the SEBI inspection period that produced the ₹25 lakh order — that function's spend fell
`DERIVED: 1,699.66 / 2,555 − 1 = −33.5%` while the revenue said to justify the cut fell only
`DERIVED: 56,505 / 61,239 − 1 = −7.7%`: **a cut four times deeper than the revenue decline.** Against
that, and carried: `W7_redflags.md` §5 #16 **withdraws the funding-decline limb as a denominator effect**
— per listed company the spend **rose 138.8%** and per rupee of cash-market turnover it is flat — and
FY2026's spend increase of 40.0% is the largest in the series. The governance limb, that the function has
no board-level owner, is untouched by that withdrawal.

---

# 4. WHAT THE PRICE IMPLIES

Doctrine §1c permits this explicitly and forbids presenting any of it as a target. Everything below is an
**`ESTIMATE`** with its assumptions named; none of it is a forecast and none of it is a valuation.

## 4.1 The two multiples, and the base they are struck on

`DERIVED: 3,409.80 / 60.61 = 56.26x` trailing, on **audited consolidated** EPS of ₹60.61 struck on
**issued** capital of 41,19,79,077 shares (the 40,95,000-share gap to paid-up is 2005 demutualisation
shares held in abeyance) `[records/capital_structure.md]`. On market capitalisation to PAT attributable:
`DERIVED: 1,39,08,031 / 2,49,698 = 55.70x`. Price to book: `DERIVED: 1,39,08,031 / 6,79,550 = 20.47x`.

**Both are struck on accounts that close 31-Mar-2026 — one quarter before the first sequential stall in
the ten-quarter series** (W5 constraint 7, restated). Earnings yield
`DERIVED: 1 / 56.26 = 1.78%`; dividend yield on the ₹10 proposed
`DERIVED: 10 / 3,409.80 = 0.29%`.

## 4.2 The strip test — the treasury book is a dilutant, not a cushion

The intuition that a company with 78.30% of its capital in securities is "cheaper than it looks" is
**arithmetically backwards.** Mark the treasury at book and CDSL at its disclosed market value, and the
residual multiple on the operating exchange **rises**.

*(Unit discipline, stated because it is where this calculation goes wrong: market capitalisation of
₹1,39,080 **crore** is ₹1,39,08,031 **lakh**. Every line below is in ₹ lakh, on the same scale as the
audited statements.)*

| | ₹ lakh |
|---|---:|
| Market capitalisation `DERIVED: 3,409.80 x 40,78,84,077 = ₹1,39,080 crore = 1,39,08,031 lakh` | 1,39,08,031 |
| less treasury book **at book value** | (5,22,509) |
| less CDSL 15% **at disclosed market value** `[AR FY26, Note 8, PDF p188/pr177]` | (3,50,932) |
| **= implied value of the operating exchange** | **1,30,34,590** |
| Operating-exchange PAT, stripping every rupee of investment and float income | **2,15,055** |
| **Implied multiple on the operating exchange** | **`DERIVED: 1,30,34,590 / 2,15,055 = 60.61x`** |

**Against a headline 55.70×.** Marking the balance sheet at fair value makes the multiple on the part
that actually grows **worse by 4.91 turns**, because the pool being stripped earns 4.42% after tax and is
worth at most book. On a stricter and clearly-flagged assumption — capitalising a 4.42% perpetuity at a
12% required return, `ESTIMATE: 5,22,509 x 0.0442 / 0.12 = 1,92,457` — the implied multiple on the
operating exchange is `ESTIMATE: (1,39,08,031 − 1,92,457 − 3,50,932) / 2,15,055 = 62.15x`.

> **The conclusion, which is the point of the exercise:** there is no balance-sheet discount inside this
> price. The 78.30% of capital that a bull would read as downside protection is, at 4.42% after tax
> inside a 20.47× book multiple, a drag on the return the price requires.

## 4.3 The growth the price requires, and what it means in market share

**Assumptions, stated so a reader can change any of them:** (i) a ten-year horizon; (ii) a 12% annual
required return — chosen as a plain equity hurdle, not asserted as correct; (iii) constant share count and
constant net margin; (iv) FY2026 audited consolidated EPS of ₹60.61 as the base; (v) the two-venue income
pool compounding at the **observed** FY2026 rate of 6.46%. Dividend yield of 0.29% is ignored as
immaterial and its omission is conservative against the bear.

`ESTIMATE: 3,409.80 x 1.12^10 = ₹10,590` of required FY2036 value per share.

| Exit multiple in FY2036 | Required FY2036 EPS | Multiple of FY2026 EPS | **Required EPS CAGR** | Implied FY2036 revenue | **Required share of the FY2036 pool** |
|---:|---:|---:|---:|---:|---:|
| **25×** (a mature-exchange rating) | ₹423.6 | 6.99× | **21.5%** | ₹33,786 cr | **75.7%** |
| **35×** | ₹302.6 | 4.99× | **17.4%** | ₹24,133 cr | **54.1%** |
| **55.7×** (no de-rating at all, for ten years) | ₹190.1 | 3.14× | **12.1%** | ₹15,164 cr | **34.0%** |

`ESTIMATE: 10,590 / 25 = 423.6; (423.6 / 60.61)^(1/10) − 1 = 21.46%`; revenue at constant margin
`4,834 x 6.989 = ₹33,786 cr`; pool `23,861 x 1.0646^10 = ₹44,622 cr`; `33,786 / 44,622 = 75.7%`
`[W2_industry §2.3]`, `[AR FY26, Consolidated P&L, PDF p164/pr153]`.

**Read the bottom row first, because it is the least demanding one and it is already extraordinary.** On
the assumption that a 55.7× multiple survives ten years untouched — which is itself a heroic assumption
for a business whose margin is a volatility ratio — BSE must still take its share of the Indian exchange
income pool **from 21.58% to 34.0%**. On the row that assumes a normal terminal rating, BSE must become
**larger than the entire two-venue pool is today** (₹33,786 cr against ₹23,861 cr) and hold **75.7%** of a
market in which it currently holds **7–8% of equity cash and 0.2% of equity futures.**

**Sensitivity on the weakest assumption, which is the pool growth rate.** At a 10% pool CAGR
(`ESTIMATE: 23,861 x 1.10^10 = ₹61,889 cr`) the three required shares become **54.6% · 39.0% · 24.5%**; at
15% (`ESTIMATE: 23,861 x 1.15^10 = ₹96,531 cr`) they become **35.0% · 25.0% · 15.7%**. **Even at a decade
of 15% pool growth — more than double what FY2026 delivered — the 25× row still requires BSE to hold 35.0%
of the Indian exchange income pool for ten years.** The conclusion is not sensitive to the assumption in
any direction that rescues it.

## 4.4 What the price is therefore implying, stated as a proposition the reader can test

The price implies **all** of the following simultaneously, and each is contested by a limb above:

1. The premium/notional ratio holds at or above 0.104% — a level whose quarterly range inside the last
   eight quarters is ±37% and whose low in that window costs ₹38,535 lakh (limb 1).
2. The FY2026 margin of `DERIVED: 3,31,068 / 5,14,810 = 64.31%` — up **10.06pp** in one year — is a new
   base rather than a high-water mark, on a cost base with `−1.682` elasticity to contracts (limb 2).
3. The regulator does not re-price the levy base, reallocate the expiry calendar or extinguish a segment
   for a decade — against a base rate of **three regulator-authored money events in three years** and a
   **40% four-year segment-extinction rate** (limbs 1 and 6).
4. The retained capital eventually earns something other than 4.42% — with no dividend policy in ten
   annual reports, 108.13% of FY2026's equity increase going into securities, and 6.97× more capital into
   the ten-year loss-maker than into the 90%-payback winner (limb 3).
5. Free cash flow is the printed ₹53.55 per ₹100 rather than the own-account ₹36.58 (limb 4).

**Doctrine bound, restated:** none of this is a target price, a valuation or a recommendation. It is the
arithmetic of what must remain true, laid beside the evidence on whether it has been true.

---

# 5. THE DATED THESIS-BREAKERS

Ranked by severity of consequence. Each names the mechanism, the date and the document that settles it.

| # | Thesis-breaker | Date | Mechanism | Settling document / next check |
|---|---|---|---|---|
| **T1** | **ICCL's own accounts confirm the ₹10,60,000 lakh inter-CCP guarantee remains outstanding while the parent's note reads ₹23 lakh.** This is the dated breaker `W7_redflags.md` §4.1 named: **it flips RF-008 to Critical and the red-flag gate must be re-run**, with the terminal state `UNINVESTABLE ON TRUST GROUNDS` back in play | **Open now**; the FY2026 s.136 statements are filed | An exposure sized at **2.32× total equity and 102.5% of total assets at 31-Mar-2025** (`DERIVED: 10,60,024 / 4,57,570 = 2.3167`; `10,60,024 / 10,34,165 = 1.0250`) stopped being disclosed with no Ind AS 1.41 or 8.49 note. If it is live, the group's largest off-balance-sheet number is unbounded from the parent's filings | **ICCL's MCA-filed FY2026 financial statements**; the **SEBI-mandated ICCL risk disclosures on the BSE website**; **FY2027 consolidated Note 37** |
| **T2** | **RBI's capital-market-exposure directions bite as legacy bank guarantees roll off.** Management states the effect is currently masked: *"there are remnant bank guarantees in the system which are of the past"* `[Q1FY27 Concall, MD & CEO]` | Issued **13-Feb-2026**, deferred from 1-Apr-2026, **effective 1-Jul-2026** | Bank guarantees are how members fund collateral. Capping banks' capital-market exposure raises its cost and availability, which constrains member capacity and therefore turnover — the activity base 92.28% of FY2026 growth came from. It touches **the same instrument class as T1** | **The first quarter in which the legacy guarantees have rolled off — Q3FY27 results, expected Feb-2027.** `[SECONDARY: RBI directions 13-Feb-2026]`; primary confirmation in `[AR FY26, MD&A policy list, PDF p53/pr42]` |
| **T3** | **The auditor rotation cliff arrives with no successor process disclosed.** S.R. Batliboi has served **FY2018 → FY2027, exactly the ten consecutive years s.139(2) permits** | **The 22nd AGM, 2027** | A new firm arrives into a group carrying an undisclosed ₹56,751 lakh Core SGF reclassification at ICCL, an internally inconsistent Note 34, an eleven-word unquantified cash-flow basis change, an unexplained ₹5,250 lakh consolidation plug and four independent tie-out failures in one statement in three years. **A change of auditor is the commonest trigger for a restatement.** The peer facing the identical cliff has already published its landing — **NSE board-approved Walker Chandiok & Co LLP** — and BSE has not | **FY2027 Board's Report**; any interim board disclosure of a successor process |
| **T4** | **A second consecutive quarter of sequential revenue-from-operations growth below 2%** | **Q2FY27, filed ~Nov-2026** | Converts the Jun-2026 stall from one quarter into a trend, on a base 92.28% of whose growth is activity that fell 6.53% in contract terms | **The September-2026 quarterly consolidated filing** |
| **T5** | **A SEBI circular reallocating expiry days, placing both venues on the same day, or removing weekly expiries** | **Undated — none scheduled or disclosed** | The precedent exists three times in 21 months and each move required regulatory approval. ~95% of premium sits in two nearest expiries | **SEBI circulars; the MD&A policy list in the next annual report.** The June-2026 32.4% share reading is `[SECONDARY: Business Today/Jefferies, 2026-07-03]` and needs a primary corroborant before it carries a conclusion |
| **T6** | **STT on options premium rose 0.10% → 0.15% effective 1-Apr-2026**, and futures 0.02% → 0.05% | **Live throughout FY2027** | Raises the all-in cost to the trader **without raising BSE's take** — a participation-rate hit, not a venue-share hit. Management calls the BSE impact *"minimal"* because its futures book is small `[Q1FY27 Concall, MD & CEO]`; the options leg is not addressed | `[AR FY26, MD&A policy list, PDF p53/pr42]`; **Q2FY27 and Q3FY27 premium ADT** |
| **T7** | **SEBI's Closing Auction Session, implemented 3-Aug-2026**, changes how the closing price used for derivative settlement, index computation and MF NAV is formed | **Live since 3-Aug-2026** | Alters expiry-day settlement mechanics on the product that is ~65% of revenue. Management: *"too early to observe"* | **Q2FY27 concall and results** |
| **T8** | **FY2027 payout below 20% of own-account free cash flow with capex under ₹600 cr, for a fourth consecutive year** | **FY2027 annual report** | Confirms limb 3 as a regime rather than a phase | **FY2027 Note 15 and Board's Report** |
| **T9** | **Any further capital tranche into India International Exchange** | **FY2027 annual report** | Eleventh consecutive loss year, against a carrying value already at **2.59×** its net-asset share and an unprovided gap of `DERIVED: 19,408 − 7,481 = 11,927` lakh | **FY2027 Form AOC-1 and Standalone Note 7** |

**Two live competitive facts with no date attached, recorded because they will not announce themselves.**
MSEI resumed live equity cash and derivatives trading in **January 2026** after raising roughly ₹1,240 cr
from Groww, Zerodha, Share India and Peak XV `[SECONDARY: business press, 2024–2026]`; and SEBI's
intraday position-limit framework effective **1-Oct-2025** caps the largest participants' expiry-day size
at intraday net FutEq ₹5,000 cr and gross ₹10,000 cr `[AR FY26, MD&A policy list, PDF p55/pr44]` — the
class of participant whose removal cut a single BSE expiry's premium turnover **55.3%** in July 2025.

---

# 6. THE BEAR CASE'S OWN FALSIFIERS

A bear case that cannot be killed is not analysis. Each falsifier below would retire the limb named.

| Falsifier | Retires | Why it is decisive |
|---|---|---|
| **Premium/notional printing at or above 0.104% for four consecutive quarters while contracts grow** | Limbs 1 and 2 | It would establish the FY2026 ratio as a level rather than a peak, and remove the −1.682 contract elasticity from play because the base would be growing |
| **A quarter in which ex-levy expenses fall alongside falling turnover, with no one-off stripped out** | Limb 2 | The ratchet is the whole of the downside asymmetry. This test **fired once** — Jun-2026 expenses −3.64% on notional −3.27% — and **failed on inspection**: ex the ₹40 cr provision it reads +3.82% against −3.27%, elasticity −1.168. A clean pass kills the limb |
| **A board-approved dividend distribution policy with a target range, or FY2027 payout above 50% of own-account free cash flow** | Limb 3 | The limb is specifically about the absence of a policy and the inversion of the regime, not about the level of any one year's dividend |
| **A disclosed capital programme absorbing the retention, taking the financial-asset-build to equity-increase ratio below 60%** | Limb 3 | 108.13% is the number the limb rests on |
| **The own-account cash construction failing to close on the balance sheet within 1% in any year** | Limb 4 | It would falsify my correction, not the company's presentation. Recorded because a bear case must name what would make its own arithmetic wrong |
| **Two consecutive quarters of sequential revenue growth above 8% with no expiry-calendar change behind it** | Limb 5 and the peak-cycle framing | It would show the engine restarting on its own rather than on an allocation |
| **A SEBI circular fixing the regulatory-fee base to premium rather than notional** | Limb 6 and half of limb 1 | It would collapse the 959× base mismatch and remove the wedge that both flatters and threatens the margin |
| **The FY2027 report carrying an Ind AS 115 disaggregation note, and the FY2027 CG report restoring the market-price table** | Limb 7 | The limb is about monitorability. Restored monitorability retires it |
| **BSE holding above 40% index-option premium share for four consecutive quarters through an expiry calendar that favours the competitor** | **The whole case** | This is the single cleanest test. It would demonstrate that the share is a franchise rather than an allocation, and every limb above would need rewriting |

**And the honest limit of the whole file.** Three of the seven limbs — 4, 6 and 7 — are **re-pricings and
monitorability costs, not mechanisms of loss.** Only limbs 1, 2, 3 and 5 can actually take money off a
shareholder, and of those, limb 3 is the only one currently in progress. **This bear case does not
establish that BSE will lose money. It establishes that at 56.3× the price requires a sequence of
exogenous conditions to hold that the company neither sets nor discloses.**

---

# 7. FINDINGS

### FINDING: FY2026 was a redistribution authored by a SEBI circular, not a franchise — and BSE has failed to hold an equity-derivatives franchise four times before
S1 WHAT: BSE's consolidated total income rose 59.1% and profit after tax 88.3% in FY2026 while the two-exchange income pool grew `DERIVED: 23,861.10 / 22,413.31 = 6.46%`, so the great majority of the result is share taken from the incumbent rather than a market that grew, and the share was created by SEBI's framework of 1 October 2024 limiting each exchange to one weekly expiry on one benchmark index `[AR FY25, MD&A policy list, PDF p50/pr39]`.
S2 WHY: The mechanism is a rule, not an execution advantage. The 1 October 2024 measures converted the incumbent's advantage in the number of weekly expiry products into a symmetric one-each allocation, and BSE's expiry day has since been reassigned twice more with regulatory approval each time — Friday to Tuesday on 3 January 2025 and Tuesday to Thursday on 1 September 2025 `[Q3FY25 Concall]` and `[Q2FY26 Concall slide]`. Management publicly misidentified the slot as an exclusive moat and then grew fastest after moving onto the competitor's day, which is the clearest available evidence that the advantage was never the specific day.
S3 EVIDENCE: Decomposed against a share-neutral counterfactual: BSE's income increment is `DERIVED: 5,148.10 − 3,236.31 = 1,911.79` crore, of which growth at an unchanged 14.44% share of a pool that grew 1,447.79 crore would have supplied `DERIVED: 1,447.79 x 0.1444 = 209.05` crore, so `DERIVED: (1,911.79 − 209.05) / 1,911.79 = 89.07%` of the increment is share taken `[AR FY26, Consolidated P&L, PDF p164/pr153]` and `[SECONDARY: NSE Q4FY26 results as reported, 2026-05-05]`. The counter-proportion that identifies this as an allocation rather than a franchise sits inside the same year's own numbers: in the year BSE took 714 basis points of share, realisation across the revenue base was a **drag** of `DERIVED: 5,622 − 783 − 6,054 = −1,215` lakh, minus 0.65% of the increase, contracts traded **fell** `DERIVED: 114.5 / 122.5 = −6.53%`, equity-cash realisation fell 19.48% on rising volume, and StAR MF realisation fell 2.67% — so the company that won the share priced worse in four of its five disclosed lines while activity supplied `DERIVED: 1,73,176 / 1,87,661 = 92.28%` of the gain `[AR FY26, MD&A, PDF p58/pr47 and PDF p75/pr64]`.
S4 CONNECTS: Concentration into that single allocated slot is measured and extreme — equity derivatives are `DERIVED: 3,13,437 / 4,83,395 = 64.84%` of audited consolidated revenue and 70.1% of standalone, roughly 95% of premium sits in the two nearest weekly expiries per management `[Q3FY26 Concall, MD & CEO]`, and one participant's removal in July 2025 cut a single expiry's premium turnover from ₹44,010 crore to ₹19,683 crore, `DERIVED: 19,683 / 44,010 = −55.3%`. The industry frame supplies the regulator's willingness to extinguish rather than merely reprice: RBI's directions of 5 January 2024 took BSE's currency-derivative average daily turnover from ₹9,733.67 crore to ₹1,525.34 crore to nil, and interest-rate derivatives are at nil from FY2025 — two of five derivative segments legislated to zero in four years `[AR FY26, MD&A, PDF p58/pr47]` and `[AR FY25, MD&A, PDF p52/pr41]`.
DOMAINS: Industry, Business, MgmtCommentary, IncomeStatement, Notes
DISCONFIRM: Sought hard, and the strongest item cuts squarely against this finding and is conceded. BSE took the share under identical rules, identical securities transaction tax and identical RBI directions, while the incumbent's total income fell 2.4% and its profit after tax fell 15.5% — that is a genuine competitive result and no part of it is luck. Further against: the ~5% out-of-week premium figure is a Q3FY26 statement, while a Q1FY27 statement puts contracts outside the two nearest weeks at five times and premium at almost ten times their January 2025 level, and the corpus does not reconcile the two. And the 32.4% June 2026 share reading is `[SECONDARY: Business Today/Jefferies, 2026-07-03]`, which under section 1a-iii cannot alone carry a conclusion; its primary corroborant is BSE's own filing showing revenue from operations up 0.16% sequentially in the same month.
S5 MEANS: The distinction that decides this name is between a redistribution and a market, because a redistribution is bounded above by the pool and reversible by the instrument that created it, and everything in the FY2026 result — the share, the expiry day, the volatility ratio that set the margin — was authored outside the company by parties whose objectives are not shareholder returns.
BASE-RATE: Realised at this company, twice, inside the window. First, extinction: an entire segment went from ₹9,733.67 crore of average daily turnover to nil on a single RBI direction, and the segment-extinction rate is two of five in four years. Second, and stronger for this finding, failure to hold: BSE has attempted an equity-derivatives franchise at least four times before and failed every time — equity derivatives ran at 498 contracts per day in FY2017, 182 in FY2018 and 126 in FY2019 after the incentive scheme was discontinued, and four subsequent relaunches produced turnover peaks that did not survive `[AR FY2018, MD&A, PDF p24/pr17]` and `[AR FY2019, MD&A, PDF p77/pr68]`. It took roughly ten years and four attempts before May 2023 worked, so the base rate for sustaining this franchise is one in five and the single success is three years old.
S6 IMPLICATION: The durability of roughly two-thirds of the earnings stream rests on a regulatory calendar rather than on execution, which means the margin of safety required on this name is not the ordinary one for a monopoly-adjacent toll business but the one appropriate to a contract with an annual renewal clause held by a third party — and any base case that extrapolates the FY2026 share gain must state whether it is extrapolating a competitive advantage or an allocation, because the evidence supports only the second. Monitorable with a trigger: index-option premium share below 30% for two consecutive months, corroborated from a primary source. Thesis-breaker: any SEBI circular reallocating expiry days or removing weekly expiries. Next check: the Q2FY27 investor presentation and the FY2027 MD&A policy list.
SEVERITY: High

### FINDING: The growth came on the one activity base that fell, and that base is what the cost runs on — so operating leverage has no single value and its downside sign is negative
S1 WHAT: In FY2026 revenue rose 63.46% and contracts traded fell 6.53%, so the same ex-levy cost increase of 10.99% divides into an elasticity of positive 0.094 against premium turnover, positive 0.159 against notional turnover and **negative 1.682 against contracts** — a spread of 1.776 elasticity points, sign included, on one year of the same trades `[AR FY26, Consolidated P&L, PDF p164/pr153]` and `[Q1FY27 IP 04Aug2026, PDF p14/slide 13]`.
S2 WHY: Management states the three-base structure himself — the regulatory fee is assessed on notional, the clearing expense on the number of contracts, and revenue is earned on premium `[Q4FY26 Concall 13May2026, MD & CEO]`. Contracts fell because SEBI doubled lot sizes with effect from 20 November 2024, so notional per contract rose `DERIVED: 16.34 / 9.03 = +80.9%` and the same rupee of turnover now arrives in fewer, larger units. The revenue gain therefore came from each unit becoming bigger and richer rather than from more units being traded, which is precisely the composition that gives no protection when volatility normalises.
S3 EVIDENCE: `DERIVED: 10.99 / 117.45 = 0.094`, `10.99 / 69.11 = 0.159` and `10.99 / (−6.53) = −1.682`. The counter-proportion that turns the elasticity into a P&L statement is the split of the ₹100 of revenue: only `DERIVED: (29,781 + 20,313 + 24,732) / 4,83,395 = ₹15.48` per ₹100 is discretionary annual spend, against `DERIVED: (64,969 + 7,696 + 82,384) / 4,83,395 = ₹32.07` per ₹100 taken by the levy, the Core Settlement Guarantee Fund and tax — so a 20% cut in every discretionary layer, deeper than anything in the ten-year record, recovers `DERIVED: (29,781 + 20,313 + 24,732) x 0.20 = 14,965` lakh or ₹3.10 per ₹100 against a reversion of revenue merely to the FY2025 level that removes `DERIVED: (4,83,395 − 2,95,734) / 4,83,395 = 38.82%` or ₹38.82 per ₹100, a ratio of `DERIVED: 38.82 / 3.10 = 12.5` to one. On the contract base management itself names as the cost driver, grossed-up clearing cost per contract **rose** `ESTIMATE: (40,642 / 41,916) / 0.934694 = +3.74%`.
S4 CONNECTS: The efficiency claim that would rebut this does not survive a change of base. The MD&A calls the FY2026 clearing-cost fall a sustainable structural efficiency gain `[AR FY26, MD&A, PDF p76/pr65]`, but the same cost has three published magnitudes — consolidated minus 19.45%, standalone minus 4.56%, grossed up minus 3.04% — and `DERIVED: 5,496 / 6,770 = 81.18%` of the consolidated fall is an intra-group charge to the clearing subsidiary rising `DERIVED: 12,607 / 7,111 = +77.29%` and eliminating on consolidation `[AR FY26, Standalone Note 35, PDF p298/pr287]`. The quarterly filings show the underlying cost behaving normally: clearing and settlement rose `DERIVED: 9,028 / 5,550 = +62.67%` year on year against revenue plus 63.48%, which is consistent with the elimination explanation and inconsistent with structural efficiency `[Q1FY27 Results 04Aug2026, consolidated quarterly filing, PDF p5]`.
DOMAINS: IncomeStatement, Industry, MgmtCommentary, Notes, CashFlow
DISCONFIRM: Sought and materially limiting. The absolute claim that costs have never contracted is **wrong** and the correction is carried: total expenses fell 4.07% in FY2021, `53,070 against 55,320` verified like-for-like on one audited page `[AR FY2021, Consolidated P&L, PDF p146/pr141]`, in a year equity-cash turnover **rose** 56.84% — the best operating-leverage year in the record, and an up-turnover year. The negative 1.682 is also arithmetically unstable near a small denominator, since contracts fell only 6.53% and a one-point error in the lot series moves it by roughly 0.3; discarding the contract row entirely still leaves 0.094 against 0.159, a 69% difference on the same cost base. And the levy that dominates the cost increase moved in the company's favour this year, contributing minus 0.06 percentage points to the margin. Against all of that: the narrowed claim survives every test — costs have never fallen in a year turnover fell, and absolute total expenses rose in nine of the ten years read.
S5 MEANS: The FY2026 margin was earned on a unit base that was contracting, so the operating leverage the market is capitalising is measured against a quantity that has already stopped growing, and the company's own cost history says the leverage runs the other way with a coefficient between minus 0.5 and minus 0.8 the moment turnover turns.
BASE-RATE: Realised at this company twice in seven years and precisely sized. In all three windows where turnover actually fell, costs rose — FY2018 to FY2019 turnover minus 28.96% against expenses plus 14.68%, FY2018 to FY2020 minus 39.21% against plus 30.64%, FY2022 to FY2023 minus 23.42% against plus 17.56% — and the consequence landed on the margin: cost to income went from 61.6% in FY2019 to 87.8% in FY2020 on a 14.44% turnover fall, and to 74.0% in FY2023 on a 23.42% fall `[records/trend_10y.csv]`. This is not a modelled risk; it is the company's own last two downturns.
S6 IMPLICATION: The forward cost floor is the ex-levy run rate of ₹1,18,773 lakh plus roughly ₹1,212 lakh of depreciation already committed from FY2026 additions less ₹1,301 lakh of non-recurring gratuity past service cost, and that floor has never contracted in a down year — which means any bear scenario must model revenue reversion against an unchanged cost base rather than against a proportional one, and the margin of safety required is set by the twelve-to-one ratio between the hole and the lever rather than by the revenue fall itself. Monitorable with a trigger: ex-levy cost elasticity to notional turnover printing above 0.60 for two consecutive quarters, against 0.159 for FY2026 and 0.513 already for Q1FY27. Next check: the September 2026 quarterly filing.
SEVERITY: High

### FINDING: At 56.3 times a peak-cycle base the price requires BSE to become larger than the entire two-venue income pool is today
S1 WHAT: The shares trade at `DERIVED: 3,409.80 / 60.61 = 56.26` times audited consolidated FY2026 earnings per share struck on issued capital of 41,19,79,077 shares, and at `DERIVED: 1,39,08,031 / 100 = ₹1,39,080 crore` of market capitalisation against profit attributable of ₹2,49,698 lakh, i.e. `DERIVED: 1,39,08,031 / 2,49,698 = 55.70` times — both struck on accounts that close 31 March 2026, one quarter before the first sequential stall in the ten-quarter series `[records/capital_structure.md]` and `[records/quarterly_series.md]`.
S2 WHY: The arithmetic of a 1.78% earnings yield is that almost all of the value sits beyond the current earnings stream, so the price is a statement about a decade of growth rather than about FY2026. Translating that statement into the only quantity that constrains it — share of a two-venue market whose pool grew 6.46% in the year BSE grew 59.1% — is what tests whether the implied growth is available at all.
S3 EVIDENCE: On a ten-year horizon, a 12% required return, constant share count and constant net margin, `ESTIMATE: 3,409.80 x 1.12^10 = ₹10,590` per share of required FY2036 value. At a 25 times exit the required FY2036 earnings per share is `ESTIMATE: 10,590 / 25 = ₹423.6`, i.e. `ESTIMATE: (423.6 / 60.61)^(1/10) − 1 = 21.46%` a year, implying FY2036 revenue of `ESTIMATE: 4,834 x 6.989 = ₹33,786` crore against a pool compounding at the observed 6.46% to `ESTIMATE: 23,861 x 1.0646^10 = ₹44,622` crore — **75.7% of it**, from 21.58% today. The counter-proportion that decides whether the requirement is merely demanding or arithmetically extraordinary is the least demanding row of the same table: even assuming the 55.7 times multiple survives ten full years with no de-rating whatsoever, required earnings growth is still 12.1% a year and required FY2036 share is still **34.0%**, so there is no exit assumption inside the plausible range under which the price does not require BSE to take a further twelve to fifty-four percentage points of a duopoly it entered three years ago `[W2_industry §2.3]` and `[AR FY26, Consolidated P&L, PDF p164/pr153]`.
S4 CONNECTS: The requirement is sharpened by where BSE actually stands outside index options: equity cash share is 7 to 8% against the incumbent's 92.99%, equity futures roughly 0.2% against 99.79%, and management states smart-order-routing applications have been pending at the other exchange for more than six months `[Q4FY26 Concall, MD & CEO]` and `[SECONDARY: NSE FY26 disclosure as reported, 2026]`. On the cost side the same growth must be delivered by a company that is **not** the low-cost operator in the set — total expenses to revenue of 38.01% against the incumbent's 27.52% excluding its settlement provision — and that pays `DERIVED: 11.71 / 4.80 = 2.44` times the incumbent's turnover-linked regulatory levy per rupee of revenue `[NSE AR FY26, Consolidated P&L, PDF p140/pr318]` and `[AR FY26, Note 27, PDF p212/pr201]`.
DOMAINS: IncomeStatement, Industry, Business, BalanceSheet
DISCONFIRM: Sought, and the two strongest objections are recorded. First, the pool growth rate is the weakest assumption in the calculation, so it is stressed: at a 10% pool CAGR the three required shares fall to 54.6%, 39.0% and 24.5%, and at 15% to 35.0%, 25.0% and 15.7% — but even a decade of 15% pool growth, more than double what FY2026 delivered, still requires 35.0% of the pool on a normal terminal rating, so no assumption inside the range rescues the conclusion. Second, BSE has already delivered a 714 basis point share gain in a single year, which is direct evidence that large share moves are possible in this market and is the single best argument that the implied path is not absurd. Third, and cutting for the company on capital rather than growth: BSE is the least regulatory-capital-intensive exchange-and-clearing group in the peer set at ₹0.258 of Core Settlement Guarantee Fund per rupee of revenue against ₹0.788, so the growth it must deliver is not capital-constrained.
S5 MEANS: The price is not paying for a toll business at a demanding multiple; it is paying for a decade in which a three-year-old derivatives franchise takes between a third and three-quarters of the income of a market it currently supplies at 21.58%, and that is a proposition about a regulator's future circulars rather than about a management team's execution.
BASE-RATE: Not established at this company in either direction, and that is the honest answer. BSE has held above 20% of the two-venue income pool for exactly one financial year, so no base rate exists for durability at this share; the only comparable episode is the four failed derivatives franchises of FY2017 to FY2022, which is a base rate for the product rather than for the share. In the wider system the closest analogue is the segment BSE did once lead — currency derivatives, where its share reached 46.3% in FY2018 and the segment itself was abolished in FY2026 — which is the sense in which a share of a market is worth nothing when the market is abolished `[AR FY2018, MD&A, PDF p24/pr17]`.
S6 IMPLICATION: What the current price implies is testable and is stated here as a proposition rather than as a valuation: the premium-to-notional ratio holds above 0.104%, the 64.31% margin is a base rather than a high-water mark, the regulator neither re-prices the levy base nor reallocates the expiry calendar for a decade, the retained capital eventually earns more than 4.42%, and free cash flow is the printed ₹53.55 per ₹100 rather than the own-account ₹36.58 — five conditions, each contested by evidence already on this record, and the margin of safety a reader requires should be set against the joint probability of all five rather than against any one. Monitorable with a trigger: BSE's share of the two-venue income pool at FY2027, against 21.58%. Next check: the FY2027 annual reports of both venues.
SEVERITY: High

### FINDING: The treasury book is a dilutant rather than a cushion, and in the one down-cycle on record both engines failed in the same year
S1 WHAT: `DERIVED: 5,22,509 / 6,67,301 = 78.30%` of equity attributable sits in securities and bank deposits earning 4.42% after tax, while the 16.53% that is the exchange earns `DERIVED: 2,15,055 / 1,10,285 = 195.02%`, and stripping that pool at book value together with the CDSL stake at its disclosed market value **raises** the implied multiple on the operating exchange rather than lowering it `[AR FY26, Consolidated Balance Sheet, PDF p163/pr152]` and `[AR FY26, Note 23, PDF p211/pr200]`.
S2 WHY: A pool returning 4.42% after tax cannot be worth more than its carrying value to a shareholder whose required return is any figure above 4.42%, and the shares trade at `DERIVED: 1,39,08,031 / 6,79,550 = 20.47` times book — so anything inside the balance sheet carried at or near book is arithmetically small against the price and cannot supply the downside protection a large securities portfolio intuitively suggests.
S3 EVIDENCE: `DERIVED: 1,39,08,031 − 5,22,509 − 3,50,932 = 1,30,34,590` lakh of implied value for the operating exchange against operating-exchange profit after tax of ₹2,15,055 lakh — stripped of every rupee of investment and float income — gives `DERIVED: 1,30,34,590 / 2,15,055 = 60.61` times, against a headline `DERIVED: 1,39,08,031 / 2,49,698 = 55.70` times. The counter-proportion that makes this a finding rather than an arithmetic curiosity is the direction of travel inside the same balance sheet: own-account financial assets went from `DERIVED: 3,71,074 / 4,42,373 = 83.88%` of equity attributable to `DERIVED: 6,14,282 / 6,67,301 = 92.06%` in one year, plus 8.18 percentage points, and `DERIVED: 2,43,208 / 2,24,928 = 108.13%` of the entire increase in shareholders' equity went into that book — so the share of capital earning 4.42% is rising, not falling, and the dilution compounds `[AR FY26, Notes 9, 11 & 12, PDF p190-202/pr179-191]`.
S4 CONNECTS: The cushion argument fails operationally as well as arithmetically, and the company's own history proves it. Between FY2019 and FY2020, revenue from operations was flat at `45,030` against `45,051` while investment income fell `DERIVED: 15,866 / 20,218 − 1 = −21.5%` and profit attributable fell `DERIVED: 12,227 / 19,417 − 1 = −37.0%`; by FY2021 investment income was `DERIVED: 12,908 / 20,218 − 1 = −36.2%` below its FY2019 level `[records/trend_10y.csv]`. The industry cause is the same on both sides: market capitalisation of all listed companies fell `DERIVED: 113.5 / 151 = −24.8%` across that window `[AR FY2019, MD&A, PDF p68/pr59]` and `[AR FY2020, MD&A, PDF p77/pr70]`. A downturn that reduces turnover reduces the yield on the corpus through the same rate and risk-appetite channel, so the two shock absorbers fail together rather than in sequence.
DOMAINS: BalanceSheet, IncomeStatement, Industry, MgmtCommentary
DISCONFIRM: Found and substantial. `DERIVED: 30.6%` of the ₹29,030 lakh of investment income is fair-value movement rather than contractual yield, so the 4.42% is partly a mark and a rising rate environment would raise the contractual half. The Core Settlement Guarantee Fund sits in its own caption between equity and liabilities rather than inside equity, so reported return on equity of 43.75% **understates** the return on distributable shareholders' capital by 6.24 percentage points rather than overstating it — the overlay's original prediction was wrong in direction and the correction is carried. And the balance sheet genuinely does contain unrecognised value: the CDSL stake carried at ₹44,940 lakh against a disclosed quoted market value of ₹3,50,932 lakh is `DERIVED: 3,05,992 / 6,79,550 = 45.03%` of total equity — though at `DERIVED: 3,060 / 1,39,080 = 2.20%` of market capitalisation it is a large balance-sheet fact and a small valuation one, which is exactly the correction `W7_redflags.md` section 5 imposes.
S5 MEANS: There is no balance-sheet discount inside this price, and the intuition that a company holding four-fifths of its capital in government securities and deposits is protected on the downside is exactly inverted — the pool earns less than any plausible cost of equity, it is growing as a share of the total, and its income has historically fallen in the same year as the trading revenue it is supposed to offset.
BASE-RATE: Realised at this company once, cleanly, and it is the FY2020 episode: profit attributable fell 37.0% on flat operating revenue because the treasury half fell at the same time. No realised loss of principal has ever occurred in the portfolio, no impairment has been taken against it, and the yield risk rather than the credit risk is what the record demonstrates — which is why this is a return-composition finding rather than a solvency one.
S6 IMPLICATION: Any sum-of-parts treatment must carry the treasury pool at book or below rather than at a multiple, and doing so raises rather than lowers the multiple being paid for the part of the enterprise that grows — so the margin of safety required on the operating exchange is set by 60.61 times its own earnings rather than by 55.70 times the blended figure, and the historic pairing of falling turnover with falling yield means a downside case must move both engines together rather than treating investment income as a stabiliser. Monitorable with a trigger: the ratio of the annual increase in own-account financial assets to the annual increase in equity attributable, at 108.13% in FY2026, with a reading below 60% the first evidence a capital programme is absorbing the retention. Next check: FY2027 consolidated balance sheet against the statement of changes in equity.
SEVERITY: High

### FINDING: The compounding a fifty-six times multiple pays for does not exist at the margin, and the payout regime inverted in the exact three years the cash arrived
S1 WHAT: On the capital management actually controls, one rupee is becoming approximately one rupee and four paise a year — 4.42% after tax on the securities book and `DERIVED: 3,517 / 83,442 = 4.21%` on the subsidiary portfolio at cost — inside a group whose exchange engine earns 195.02% and whose shares carry a 1.78% earnings yield `[AR FY26, Note 23, PDF p211/pr200]` and `[AR FY26, Standalone Note 7, PDF p267/pr256]`.
S2 WHY: There is no dividend policy in any of ten annual reports, and none of the four available explanations for the retention survives sizing: regulatory net-worth floors are `DERIVED: 20,100 / 6,79,550 = 2.96%` of equity, capital trapped at the clearing subsidiary is `DERIVED: 9,067 / 1,76,486 = 5.1%` of the year's retention, the capital-expenditure cycle is smaller than the dividend at `DERIVED: 41,198 / 35,932 = 1.15` times, and legal capacity is `DERIVED: 4,55,828 / 41,198 = 11.07` times the proposed dividend `[AR FY26, Note 35, PDF p222/pr211]` and `[AR FY26, Standalone Note 15, PDF p280/pr269]`.
S3 EVIDENCE: One year's retention of ₹1,76,486 lakh costs 1,129 basis points of return on equity — `DERIVED: 2,48,725 / 6,79,550 = 36.60%` as retained against `DERIVED: (2,48,725 − 1,76,486 x 4.42%) / (6,79,550 − 1,76,486) = 47.89%` if distributed — and the accumulated pile costs 10,707 basis points, `DERIVED: (2,48,725 − 5,22,509 x 4.42%) / (6,79,550 − 5,22,509) = 143.67%`. The counter-proportion that turns a level into a regime is the two-era split of the same cash: across FY2017 to FY2023 the company returned `DERIVED: 1,65,964 / 6,854 = 24.21` times its own-account free cash flow, and across FY2024 to FY2026 it returned `DERIVED: 70,094 / 3,30,683 = 21.20%` of it — a 114-fold change in the measure — while `DERIVED: 4,10,654 / 4,61,513 = 88.98%` of the decade's operating cash was earned in those last three years and only `DERIVED: 70,094 / 2,36,058 = 29.69%` of the decade's distributions were made in them. The payout ratio fell from 98.9% in FY2021 to 17.65% in FY2026, 81.2 percentage points in three years `[AR FY26, Note 15, PDF p205/pr194]` and `[AR FY26, Statement of Changes in Equity, PDF p167-168/pr156-157]`.
S4 CONNECTS: The governance channel explains why nothing corrects it: there is no promoter in any of twenty-two shareholding records, no director holds equity, there has never been an employee stock option plan and the managing director is barred from stock options under the securities-contracts regulations, so the board and the executive are paid in cash and are structurally indifferent to the share price `[AR FY26, CG Report, PDF p80/pr69]`. Management's own account of the position is contradicted by the accounts: asked on 13 May 2026 whether the excess cash earns 4 to 4.5% post tax, the managing director answered that it is earning much more than that and invited the questioner to read the balance sheet and profit and loss account — where the answer is 4.42%, 0.08 percentage points from the midpoint of the premise he rejected `[Q4FY26 Concall 13May2026, MD & CEO]`.
DOMAINS: BalanceSheet, CashFlow, Governance, MgmtCommentary
DISCONFIRM: Found, and it is the strongest single bull fact in the corpus, conceded in full. Three share repurchase programmes retired 88,70,407 shares for ₹658 crore and are worth `DERIVED: 3,409.80 / 2,868.4 − 1 = +18.87%` of today's share price against the honest counterfactual share count of 48,71,97,548, i.e. `DERIVED: 541.40 x 40,78,84,077 = ₹22,083 crore` of value for continuing holders; the CDSL stake returned 36.9 times its cost basis; and incremental return on capital employed from FY2016 to FY2026 is 56.96%. Over the decade one rupee unambiguously became more than one rupee. Three answers are recorded rather than asserted: `DERIVED: 4,497 + 12,300 + 47,620 = 64,417` lakh of the ₹65,837 lakh was spent in FY2018 to FY2020, before the cash arrived, and the route is now closed at 2.49% take-up in FY2024 and a price `DERIVED: 3,409.80 / 360.00 = 9.47` times the last offer; the ₹22,083 crore is a mark to market on the very multiple this file disputes rather than a cash return; and not one CDSL step was discretionary, both sell-downs having been directed by the regulator and the residual 15% being a regulatory cap.
S5 MEANS: The company was an outstanding allocator of capital when it had almost none and has been a poor one in every one of the three years it has had a great deal, and since a fifty-six times multiple is a claim on reinvestment rather than on distribution, the gap between what the price assumes about the marginal rupee and what the accounts show the marginal rupee earning is the single largest unhedged assumption in the case.
BASE-RATE: Realised, at this company, and measurable in both directions. Against the company: `DERIVED: 20,919 / 3,001 = 6.97` times more discretionary capital went into India International Exchange — ten consecutive loss years, ₹24,023 lakh of cumulative loss, nil ever returned, the tenth tranche of ₹4,128 lakh paid in the tenth loss year — than into BSE Index Services, which returned `DERIVED: (1,200 + 1,500) / 3,001 = 89.97%` of its purchase price in dividends within twenty-four months. For the company: the two share repurchases of FY2018 to FY2020 are the clearest evidence in ten years that the board can convert a rupee into more than a rupee, and no dilution has ever occurred.
S6 IMPLICATION: Return on equity of 43.75% falls mechanically by roughly 1,100 basis points for each further year of retention at current marginal rates, independently of anything that happens to volumes, so the quality of the compounding engine deteriorates even in the bull case and any model that holds return on equity constant across a forecast period is assuming a change in capital policy that ten annual reports give no basis for. Monitorable with a trigger: FY2027 distributions below 20% of own-account free cash flow with cash capital expenditure under ₹600 crore, for a fourth consecutive year. Thesis-breaker for this limb: a board-approved distribution policy with a stated target range, or a disclosed capital programme taking the financial-asset build below 60% of the equity increase. Next check: FY2027 annual report, Note 15 and the Board's Report.
SEVERITY: High

### FINDING: The shareholder's hundred rupees yields forty-four of cash rather than sixty-four, and the regulator's share of what leaks out rose 9.71 points in the year the margin peaked
S1 WHAT: On the reported presentation ₹100 of FY2026 revenue converts into ₹64.21 of operating cash flow; on an own-account basis, with clearing-member float and statutory remittances removed, the same ₹100 converts into ₹44.01 — and over ten years the cumulative conversion is 0.712 against a printed 1.272 `[AR FY26, Consolidated Cash Flow, PDF p165/pr154]` and `[AR FY2017, Note 18, PDF p170/pr168]`.
S2 WHY: BSE consolidates its clearing corporation, so member margins, settlement obligations and clearing-bank deposits flow through group working capital inside the operating section, and a further ₹44,937 lakh of the FY2026 line is tax collected for the government and held pending remittance rather than any operating result. The FY2025 annual report changed the basis of preparation with eleven words in a footnote carrying no amount and no reclassification note `[AR FY25, PDF p159/pr148]`.
S3 EVIDENCE: The two maps use the same divisor of ₹4,833.95 lakh per rupee, and `DERIVED: 64.21 − 44.01 = 20.20` of the difference is `DERIVED: 12.13 − (−5.41) = 17.54`, i.e. `17.54 / 20.20 = 86.8%`, one working-capital line whose **sign flips** between the two presentations. The counter-proportion inside that line identifies whose money it is: of the ₹72,767 lakh inflow, `DERIVED: 24,251 + 44,937 = 69,188` or 95.08% is members' and the government's while `DERIVED: 72,767 − 69,188 = 3,579` or 4.9% is the company's own, a ratio of 20.3 to one `[AR FY26, Note 16, PDF p206/pr195]` and `[AR FY26, Note 19, PDF p208/pr197]`. On the cost side the same asymmetry recurs: of the ₹54.84 that leaves every ₹100, `DERIVED: 32.075 / 54.844 = 58.48%` is levy, Core Settlement Guarantee Fund or tax, against `DERIVED: (13.8794 + 3.0433 + 14.5810) / 64.5992 = 48.77%` a year earlier — so total leakage fell 9.76 points per ₹100 while the regulator's share of what remains rose 9.71 points, in the year of peak profitability.
S4 CONNECTS: The regulator's block is about to grow again by the company's own voluntary policy, disclosed on a call and nowhere in the annual report: a Core Settlement Guarantee Fund contribution of 5% of transaction revenue monthly, capped at 150% of the minimum, is `DERIVED: 3,79,499 x 5% = 18,975` lakh a year against ₹7,696 lakh charged, i.e. `DERIVED: 18,975 / 4,83,395 = ₹3.93` of the ₹100 instead of ₹1.59 `[Q2FY26 Concall 17Nov2025, MD]` and `[AR FY26, Note 22, PDF p211/pr200]`, which moves the regulator-and-tax block from ₹32.07 to roughly ₹34.41. The peer control establishes that the burden is company-specific rather than sectoral: BSE pays 11.71% of revenue in turnover-linked regulatory fees against the incumbent's 4.80%, `DERIVED: 11.71 / 4.80 = 2.44` times, earning ₹8.54 of revenue per rupee of levy against ₹20.85 `[NSE AR FY26, Consolidated P&L, PDF p140/pr318]`.
DOMAINS: CashFlow, IncomeStatement, Notes, Industry, Governance
DISCONFIRM: Found, and it bounds this finding to a re-pricing rather than a loss. The money is genuinely in the bank: the own-account construction closes on the balance sheet at `DERIVED: 2,43,208 − 2,43,159 = 49` lakh, 0.02%, every input is traced in all ten annual reports and each year ties to its balance-sheet caption exactly, so this is a caption defect and not a fabrication — `W7_redflags.md` section 4.4 is right that it does not stop the process. The FY2025 restatement also **cut** reported cash flow by ₹19,857 lakh, the opposite direction from what earnings management produces. And on the levy specifically, the direction was favourable in FY2026: the mismatch moved in BSE's favour by `DERIVED: 33,123 x 2.17450 = 72,027` against an actual ₹55,625 lakh, i.e. ₹16,402 lakh, and the levy fell as a share of revenue from 13.88% to 13.44%.
S5 MEANS: Two-fifths of the cash a reader would compute from the printed statement is not a claim on anything a shareholder owns, and the share of the residue that a regulator or the tax code takes rose almost ten points in a single year — so both halves of the free-cash-flow calculation moved against the shareholder in the year the reported margin looked best.
BASE-RATE: No realised loss arises from the conversion measure itself, and none is asserted: closing cash ties to the balance sheet in all ten years. The realised base rate that does attach is on the regulator's side and it is three events in three years — the levy re-basing to notional retrospective to FY2007 with 15% penal interest at ₹7,347 lakh or 9.52% of FY2024 consolidated profit after tax, RBI's directions extinguishing the currency segment, and the equity-cash repricing that cost `DERIVED: 30,356 x 1.023693 = 31,075; 31,075 − 25,021 = 6,054` lakh of revenue on **rising** volume. In the wider system, cash-flow misclassification is the second most common Ind AS enforcement finding on Indian listed companies, which is why the presentation half is carried at all.
S6 IMPLICATION: Every cash-based measure in the valuation must run on the own-account series of ₹36.58 of free cash flow per ₹100 rather than the printed ₹53.55, which roughly halves the coverage against which the payout question in the preceding finding is judged, and the forward regulatory block should be modelled at ₹34.41 per ₹100 rather than ₹32.07 because the Core Settlement Guarantee Fund policy is already in force and unpublished. Monitorable with a trigger: the quarterly Core Settlement Guarantee Fund charge against 5% of that quarter's transaction charges, which already annualises at `DERIVED: 2,591 x 4 = 10,364` lakh against ₹7,696 lakh for FY2026 on flat sequential operating revenue. Thesis-breaker: a SEBI circular fixing the levy base to premium rather than notional, which would remove the wedge in both directions. Next check: Q2FY27 results and the FY2027 annual report.
SEVERITY: High

### FINDING: Every series this bear case needs to monitor has either been withdrawn from disclosure or was never required, so the thesis cannot be falsified at the speed at which it would break
S1 WHAT: Six of the seven monitorables the mechanisms above depend on are unavailable from BSE's own filings — the audited product split of revenue, contract counts, the intra-group clearing rate, the customer above 10%, market-share and Bankex metrics, and the company's own share-price table — and the seventh, the ₹10,60,000 lakh inter-CCP guarantee, was removed with the prior-year comparative actively restated to ₹24 lakh and no reclassification or error-correction note `[AR FY26, Note 22, PDF p211/pr200]` and `[AR FY26, Consolidated Note 37, PDF p227/pr216]`.
S2 WHY: The regulatory design that removes the incentive to misstate also removes the incentive to inform. There is no promoter, no director holds equity, there has never been an employee stock option plan, and the managing director is barred from stock options — so the board and the executive are paid in cash and are structurally indifferent to the share price `[AR FY26, CG Report, PDF p80/pr69]`. What moves at BSE is therefore not the number but the boundary of what gets published, and no accounting standard forces the boundary outward: no Ind AS 108.34 trigger arises because no member reaches 10% of revenue, so the disclosure that would size the single largest participant exposure is not merely absent — it is not required `[AR FY26, Note 39, PDF p228/pr217]`.
S3 EVIDENCE: The asymmetry inside one audited note is the whole finding: Auction charges of ₹60 lakh, `DERIVED: 60 / 4,83,395 = 0.012%` of revenue, carry their own audited caption while transaction charges of `DERIVED: 3,79,499 / 4,83,395 = 78.51%` of revenue are printed as a single line with no split, and a category one-tenth the size is broken six ways `[AR FY26, Note 22, PDF p211/pr200]`. The counter-proportion that rules out a drafting accident is the peer control at an almost identical concentration: the incumbent's largest line is 78.65% of its revenue — 0.14 percentage points from BSE's — and it is split five ways inside the audited note as Cash ₹1,554.64 crore, Futures ₹1,480.10 crore, Options ₹9,997.57 crore, Mutual Fund ₹18.04 crore and Others ₹6.66 crore `[NSE AR FY26, Note 27, PDF p159-160/pr314-317]`. And the exposure is widening without any accounting change: transaction charges went from `DERIVED: 58,271 / 1,39,003 = 41.92%` of revenue in FY2024 to 68.64% in FY2025 to 78.51% in FY2026, plus 36.59 percentage points in two years — the business concentrated into the part of the disclosure that was already blank.
S4 CONNECTS: The pattern crosses two independent production channels, which is what rules out a single staffing constraint: the statutory annual report is annual, assured and produced by the secretarial function, while the investor-relations channel is quarterly, unassured and produced by a different team, and a shortage in the first does not propagate into the managing director's prepared remarks. The spoken channel does not fill the gap either, and its failure is structured rather than random: across fifty-three scoreable claims made between February 2024 and August 2026 the hit rate is `DERIVED: 32.5 / 53 = 61.3%`, but it splits into `DERIVED: 21.5 / 33 = 65.2%` on actions the company controls and `DERIVED: 4 / 12 = 33.3%` on reassurances about numbers it does not — a two-times gap, with seven of the eight reassurance misses optimistic — and the three largest profit-and-loss swings of the window, ₹199 crore, ₹109 crore and ₹170 crore, together `DERIVED: 478 / 1,326 = 36.0%` of FY2025 profit, all landed in categories management had expressly declined to size `[W2_promise §b]`. No numeric forward guidance on revenue, margin, volumes, the Core Settlement Guarantee Fund or cost was issued once across eleven transcripts and seven decks. The industry frame sharpens one instance specifically — BSE earns ₹6,763 lakh selling market data and supervises listing-obligation compliance for 5,663 listed companies, and it is the entity that polices this disclosure requirement for others that stopped making it about itself, the last month-wise series for its own shares covering April 2023 to March 2024 `[AR FY2024, CG Report, PDF p92/pr86]`.
DOMAINS: Governance, Notes, MgmtCommentary, Business, Industry
DISCONFIRM: Sought hard, because a multi-instance pattern invites confirmation bias, and six items cut materially the company's way and all six ship. The same-day disclosure record is unbroken across 477 announcements in 2024 to 2026, including an adverse clearing-subsidiary order told to the tape at 22:43 the same night — a company managing its narrative does not do that. FY2026 **added** disclosure as well as removing it, including a reasonable-assurance report on sustainability core indicators and a new clearing-and-settlement footnote, so "reducing transparency" is too strong as a general characterisation and is not adopted here. The set is not monotonically narrowing: colocation revenue was refused in August 2025 and then disclosed quarterly from November 2025 and retrospectively for FY2025 — the one offline routing of seven that went the other way. One of the five original narrowing limbs was withdrawn as false by the producing agent itself. None of the removed statutory disclosures was legally required, and a mechanical explanation survives on three of five — two secretarial audits by different firms signed thirteen days apart, six of eight deleted parties being legacy charitable trusts, and a reused section letter. And the peer control is not unanimous: **MCX also leaves its transaction-fee line undecomposed**, so the unsplit dominant line is not unique to BSE even though the absence of every Ind AS 115 disclosure is.
S5 MEANS: This is a monitorability defect rather than a governance verdict, and the distinction matters because the two carry different remedies — the register establishes direction rather than intent on five of seven instances, and what follows is not that anyone is concealing anything but that a reader who wants to track the four mechanisms that could actually take money off a shareholder must do it from investor-presentation slides, secondary press reports and a competitor's audited note.
BASE-RATE: The gap has cost a rupee once cleanly — the SEBI differential fee, where the sequence ran note, then contest abandoned, then no note, and the item is now ₹56,616 lakh a year — and twice arguably, and in both of those the loss was disclosed first and the silence followed. **Nowhere has the gap itself cost a rupee**: no restatement, no qualification, no non-disclosure action, no Indian clearing-corporation default since 2019 and no contingent claim crystallised in nine years. Realised cost of the pattern to date is therefore approximately nil, which is why it ranks last of the seven limbs and is framed as an epistemic cost rather than an economic one.
S6 IMPLICATION: Every quantified disclosure this company still publishes voluntarily should be treated as available only for as long as it remains favourable, which raises the required margin of safety specifically on the Core Settlement Guarantee Fund policy, the colocation split, the Average Daily Lots series and the inter-CCP guarantee — and because the four loss-bearing mechanisms in this file are monitored from those sources, the practical consequence is that a deterioration would be visible to a reader one to two quarters later than it becomes true. Monitorable with a trigger: whether the FY2027 report carries an Ind AS 115 disaggregation note and whether the FY2027 corporate governance report restores the market-price table. Thesis-breaker for this limb: a year in which a growing or adverse item retains its disclosure, which would put the direction test on the other side. Next check: FY2027 annual report, Note 22 and the Corporate Governance Report.
SEVERITY: High

### FINDING: The bull case is right on the accounts, on the repurchases and on the share gain — and what survives those concessions is a durability case rather than a trust case
S1 WHAT: Nine disconfirming items on the record cut against this bear case, and all nine are accepted here: zero rupees of realised loss from an accounting channel in ten years, five accounting defects running against the company's own interest, share repurchases worth `DERIVED: 3,409.80 / 2,868.4 − 1 = +18.87%` of today's share price, a levy mismatch that moved ₹16,402 lakh in BSE's favour in FY2026, five clean years of restatement history with the credit loss traced to one named debtor and an expected-credit-loss re-estimate net conservative by ₹879 lakh, a genuine 714 basis point share gain taken from the incumbent under identical rules, added disclosure in FY2026, an unbroken same-day disclosure record, and the lowest realised regulatory cost in the peer set.
S2 WHY: The concessions and the bear case are not in conflict because they answer different questions. The accounting evidence answers whether the FY2026 numbers are true; every limb in this file assumes they are. What the accounting evidence cannot answer is whether they repeat, and that question is settled by the expiry calendar, the premium-to-notional ratio and the cost ratchet — none of which appears in the accounts at all.
S3 EVIDENCE: On money rather than on process, BSE's supervision record is the best in its peer set: penalties as a share of own profit after tax are 0.010% at BSE against 13.50% at the incumbent, 0.66% at CDSL, 0.09% at MCX and nil at IEX, with the incumbent paying ₹643.05 crore in FY2025 and ₹40.35 crore in FY2026 against ₹1,391.21 crore provided, while BSE's three-year realised cost including the clearing-subsidiary order is ₹8.33 crore or 0.33% of FY2026 profit `[W2_peers §5]`. The counter-proportion that stops this becoming a clean bill is drawn from the same peer table: the record is best on **penalties**, which are the smallest regulator-authored number in the case, and worst on **rule changes**, which are the largest — the levy alone runs at `DERIVED: 56,616 / 4,83,395 = 11.71%` of revenue against the incumbent's 4.80%, `DERIVED: 11.71 / 4.80 = 2.44` times, and an entire segment worth ₹9,734 crore of average daily turnover was abolished by directive. Reading the ₹8.33 crore penalty ledger as the measure of regulatory exposure understates it by orders of magnitude.
S4 CONNECTS: Two further items cut for the company on capital rather than on conduct and are carried rather than buried. BSE is the **least** regulatory-capital-intensive exchange-and-clearing group in the set at ₹0.258 of Core Settlement Guarantee Fund per rupee of revenue against ₹0.788 for the incumbent and ₹0.594 for MCX, and on the flow, incremental regulatory capital per rupee of incremental revenue is `DERIVED: 11,423 / 1,87,661 = ₹0.061` against cash capital expenditure of `DERIVED: 51,516 / 1,87,661 = ₹0.275` `[AR FY26, Note 41, PDF p232/pr221]`. Any bear reading that this growth is capital-hungry is refuted, and this file makes the opposite argument — the capital is not needed, which is why holding four-fifths of it at 4.42% is a choice rather than a constraint.
DOMAINS: Governance, CashFlow, BalanceSheet, MgmtCommentary, Industry
DISCONFIRM: This finding is itself the disconfirming search, so what is recorded here is the limit of the concessions rather than evidence against them. Three limits: the ₹22,083 crore of repurchase value is a mark to market on the very multiple under dispute and halves if the multiple halves; `DERIVED: 4,497 + 12,300 + 47,620 = 64,417` lakh of the ₹65,837 lakh was spent before the cash arrived and the route is now closed at 2.49% take-up and a price 9.47 times the last offer; and not one CDSL step was discretionary, both sell-downs having been directed by the regulator and the 15% residual being a cap that prevents the stake being increased. The share gain has no such limit and is conceded without one — there is no evidence in the corpus that it has reversed on any measure other than a single secondary-sourced month.
S5 MEANS: A bear case that survives these nine items is necessarily a narrow one, and this is what it is narrowed to: the accounts are reliable in amount, management's conduct is the best in its peer set on every measure that has ever cost money, and the entire dispute is about whether a regulator-allocated position on one weekly expiry day, priced by a volatility ratio, defended by a cost base with negative downside elasticity and funded by a treasury book earning 4.42%, is worth fifty-six times a peak-cycle year.
BASE-RATE: Established in both directions and both halves ship. For the company: zero rupees of realised loss from an accounting channel in ten years, no qualification in nine, no dilution ever, and the lowest realised penalty cost in the peer set. Against it: every rupee that has ever been lost at this company came from a regulator, a counterparty or a capital-allocation decision, and the three largest — the levy re-basing at ₹7,347 lakh, the currency segment at ₹9,734 crore of average daily turnover extinguished, and India International Exchange at ₹20,919 lakh in with nil back — are all live channels rather than closed ones.
S6 IMPLICATION: The correct reading of the evidence is that trust is not the constraint on this name and durability is, so the analytical work that changes a reader's view is not further forensic examination of the accounts but observation of four exogenous series — the expiry calendar, the premium-to-notional ratio, sequential revenue from operations and the FY2027 distribution decision — and the margin of safety should be sized against the volatility of those four rather than against any residual doubt about the reported numbers. Monitorable with a trigger: whether the FY2027 accounts show the share gain of FY2026 held, extended or given back, measured as BSE's share of the two-venue income pool against 21.58%. Next check: the FY2027 annual reports of both venues, and the Q2FY27 quarterly filing.
SEVERITY: High

---

# 8. WHAT W8 INHERITS FROM THIS FILE

**The eleven constraints in `W7_redflags.md` §7 stand unamended and are not restated here.** This file
adds four, all of which are arithmetic rather than judgement:

12. **The strip test must be published, not footnoted.** Carrying the treasury pool at book and CDSL at
    market gives an implied multiple on the operating exchange of
    `DERIVED: 1,30,34,590 / 2,15,055 = 60.61x` against a headline 55.70×. Any sum-of-parts that produces a
    *lower* number than the headline has capitalised a 4.42% pool at more than book and must show why.
13. **The downside case runs revenue reversion against an unchanged cost base.** The ratchet is
    established on three windows and the discretionary lever is worth ₹3.10 per ₹100 against a ₹38.82
    hole. A proportional cost model is not available on this evidence.
14. **The bear driver is the premium/notional ratio and its band is the quarterly one, not the annual
    one.** ±37% inside eight quarters; the already-observed Q2FY26 level costs **₹38,535 lakh**; the
    FY2025 level costs `ESTIMATE: 69,676` lakh. The annual series is a lower bound.
15. **The two shock absorbers must move together in any downside scenario.** FY2019→FY2020 is the
    precedent: PAT attributable −37.0% on flat operating revenue, because investment income fell at the
    same time and through the same cause.

**The five monitorables this file hands forward**, each with a trigger and a next check:

| Monitorable | Trigger | Next check |
|---|---|---|
| The Jun-2026 stall | A second consecutive quarter of sequential revenue-from-operations growth below 2% | September-2026 quarterly filing (~Nov-2026) |
| The premium/notional ratio | Below 0.09% for two consecutive quarters | Q2FY27 investor presentation, Average Daily Lots slide |
| The cost ratchet | Ex-levy cost elasticity to notional above 0.60 for two consecutive quarters (0.159 FY2026 → 0.513 Q1FY27) | Q2FY27 results |
| The capital regime | FY2027 payout below 20% of own-account FCF with capex under ₹600 cr; financial-asset build above 100% of the equity increase | FY2027 annual report, Note 15 and the Board's Report |
| The RBI directions | The first quarter in which legacy bank guarantees have rolled off | Q3FY27 results (~Feb-2027) |

**Four live contradictions this file carries forward rather than resolves** (§10 — nothing deleted, and
W6 §7.4 states that QC fails the report if any is absent from it). Two are already adjudicated in
`W7_redflags.md` and are used here on the adjudicated basis: the guarantee sizing (settled at **2.32×
total equity and 102.5% of total assets at 31-Mar-2025**, §3.2) and the retrospective levy (settled at
**₹7,347 lakh**, §3.1, with ₹22,421 lakh and "21.8%" withdrawn from publication). Two are **not**
adjudicated anywhere and are stated here unresolved: **BSE Institute's consideration exists as ₹1,690
lakh, ₹6,590 lakh, ₹6,191 lakh and a public "₹16.9 crores", with ₹4,900 lakh of the parent's
distributable profit in question**; and **ICCL's FY2026 profit reads ₹16,979 lakh on Form AOC-1 and
₹6,805 lakh on the Schedule III entity table 84 printed pages later, while BSE Technologies reads
+₹1,624 lakh and −₹3,450 lakh in the same pair** — a 149.5% difference and a sign change, with the
eliminations disclosed nowhere. Both are **preparation-quality items rather than bear limbs**, and
neither is used above to carry a mechanism.

**The single highest-severity dated thesis-breaker, restated because it is the one that changes the gate
and not merely the price:** confirmation from **ICCL's own s.136 / MCA-filed FY2026 financial statements**
that the ₹10,60,000 lakh inter-CCP guarantee remains outstanding while the parent's note reads ₹23 lakh.
`W7_redflags.md` §4.1 names it, and if it is found, **RF-008 becomes Critical, the red-flag gate is
re-run, and the terminal state `UNINVESTABLE ON TRUST GROUNDS` returns to the table.** Nothing else in
this file has that consequence.

---

## 8a. Corrections made inside this file before it shipped (§10 — nothing deleted)

Doctrine §4b requires that any computed number carrying a conclusion be recomputed once, independently.
That check was run on all 118 derived figures in this file and caught three of its own, recorded here
rather than quietly fixed, because `W7_redflags.md` §5 makes the same demand of the orchestrator.

| # | The draft error | What replaced it | Why it matters |
|---|---|---|---|
| **1** | Market capitalisation written as **₹13,90,803 lakh** in four places | **₹1,39,08,031 lakh** (`DERIVED: 3,409.80 x 40,78,84,077 / 100000`) | **A factor-of-ten scale error — the identical class as the orchestrator's `RF-047` error, made in the same file that quotes it.** Every ratio built on it (55.70×, 20.47×, 60.61×) was independently correct because they were computed at the right scale, so nothing propagated; but the printed numerator was wrong and would not have reproduced. **This is the argument for the §4b recompute, demonstrated rather than asserted** |
| **2** | The 55.7× row of §4.3 carried an implied FY2036 revenue of ₹14,613 cr, computed on an 11.7% growth rate net of dividend yield, while the same row's stated CAGR was 12.1% | **₹15,164 cr and a required share of 34.0%**, the whole table now struck consistently on the stated CAGRs; the pool at 6.46% is **₹44,622 cr**, not ₹44,790 cr, which was computed at 6.5% | The conclusion strengthens: the least demanding row now requires **34.0%** of the pool rather than 32.6% |
| **3** | `W4_capalloc.md`'s buyback share-count string, quoted forward | Recomputed as **7,93,14,471** against the source's 7,93,13,471 | 0.0013%; no conclusion moves. Both stay on the record (§3.3) |

**None of the three reached a downstream artifact**, because this is the terminal file of wave 7. That is
luck rather than method, and the method is the recompute.

---

**End of W7_bearcase.md.** Doctrine §1c observed: no recommendation, no position sizing, no entry level,
and no target price. Every forward figure is an `ESTIMATE` with its assumptions named, and the falsifiers
of this case are listed in §6 alongside the thesis-breakers of the bull case in §5.
