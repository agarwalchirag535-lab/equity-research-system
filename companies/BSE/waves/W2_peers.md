# W2 — Peer benchmarking: BSE Limited against the Indian MII set

**Wave 2 · peer set · 2026-09-07.** Sector overlay `waves/W1.7_mii_overlay.md` governs which metrics are
admissible; §5 of that overlay disqualifies six standard comparisons and this document computes none of
them. Doctrine §1 governs the output: the tables are evidence, the conclusions above them are the
deliverable.

**Artifact rule.** Per the task instruction this wave writes exactly one file. Doctrine §5a would
normally also emit `records/peer_grid.csv`; it is **not** written here, and the grid below is the
canonical form for this run.

---

## 0. Headline — what the peer set settles

Three questions came into this wave open. All three are now closed.

1. **Does a direct peer publish the audited revenue disaggregation BSE does not?** **Yes — every one of
   them.** All four peers publish the Ind AS 115 timing disaggregation BSE omits, and NSE — the direct
   competitor, running the identical business at an almost identical revenue concentration — splits its
   transaction-charge line into five audited product lines where BSE prints one. RF-003 is upgraded from
   "BSE discloses less than the standard requires" to **"BSE discloses less than every comparable
   institution in its own market."**
2. **How much segment detail do peers give (RF-013)?** NSE publishes a full Ind AS 108 note — segment
   revenue, result, assets, liabilities, capital expenditure and depreciation across Trading, Clearing
   and Others. BSE publishes one segment and no segment P&L since FY2017.
3. **Is BSE's FY2026 margin expansion an operating achievement?** No. The peer set isolates it as the
   arithmetic consequence of one exogenous market-structure ratio, and management describes the
   mechanism in its own words.

---

## 1. The peer set, and why each member is in it

Five market infrastructure institutions, all with 31-March year ends, all FY2026 audited.

| # | Peer | Regulator / statute | Model | Listed | Basis used |
|---|---|---|---|---|---|
| — | **BSE Limited** | SEBI — SECC Regulations 2018 | Exchange + own clearing corporation (ICCL) | NSE-listed | Consolidated |
| 1 | **NSE** (National Stock Exchange) | SEBI — SECC Regulations 2018 | Exchange + own clearing corporation (NCL) | **Unlisted** | Consolidated |
| 2 | **MCX** (Multi Commodity Exchange) | SEBI — SECC Regulations 2018 | Exchange + own clearing corporation (MCXCCL) | BSE-listed | Consolidated |
| 3 | **CDSL** (Central Depository Services) | SEBI — D&P Regulations 2018 | Depository | NSE-listed | Consolidated |
| 4 | **IEX** (Indian Energy Exchange) | **CERC** — Electricity Act 2003 / Power Market Regulations 2021 | Exchange, no clearing corporation | NSE-listed | Consolidated |

### 1.1 Why NSE is the anchor, and why its being unlisted does not disqualify it

NSE is the only entity in India that does what BSE does: an equity cash market and an equity-derivatives
market, under the same SEBI SECC Regulations, priced under the same SEBI fee schedule, cleared through a
wholly-owned clearing corporation, funding a Core Settlement Guarantee Fund on the same SEBI framework,
and interoperating with BSE's own clearing corporation. Its financial statements are audited by Price
Waterhouse & Co Chartered Accountants LLP `[NSE AR FY26, Board's Report, PDF p74]` and are a valid
comparator on every operating, structural and disclosure dimension used here.

**Comparable on:** revenue architecture, transaction-charge economics, the regulatory levy base, cost
structure, clearing-corporation capital, float composition, disclosure quality, board structure,
ownership caps, penalty exposure.
**NOT comparable on:** anything priced by a market — no share price, no market capitalisation, no
multiple, no per-share metric is computed for NSE anywhere in this document. Also not comparable on
scale without saying so: NSE's FY2026 revenue from operations is ₹16,601.31 cr against BSE's ₹4,833.95 cr,
i.e. **3.43×** `= 16,601.31 ÷ 4,833.95` — a share comparison is meaningful, a rupee comparison is not.

### 1.2 Why MCX belongs, and the channel record for obtaining it

**Channel record, per doctrine §1a-iii.** NSE's annual-reports equities API returned zero rows for symbol
MCX on two separate attempts — a fact about one channel. Three further channels were tried:
`api.bseindia.com/BseIndiaAPI/api/AnnualReport_New/w?scripcode=534091` returned **HTTP 200 with fifteen
years of direct PDF links** on the first attempt with browser headers; the `AnnualReport/w` and
`&Type=Y` variants returned the same payload. FY2026 (182pp, filed 26-Aug-2026) and FY2025 (303pp)
were retrieved. **MCX financials are not available via the NSE annual-reports equities API; they are
fully available via BSE's own `AnnualReport_New` endpoint.** The zero-row result was a single-channel
artifact, not a data absence. NSE's own annual report was likewise obtained directly from
`nsearchives.nseindia.com` after cookie priming (bare `curl` returns 403).

**Comparable on:** the exchange-plus-clearing-corporation structure, the SEBI turnover-fee regime, Core
SGF mechanics, statutory-fund contributions, demutualised no-promoter ownership, penalty exposure,
disclosure architecture.
**NOT comparable on:** the underlying. MCX trades commodity derivatives; its participants are hedgers
and its volumes track commodity price volatility, not index option premium. Its FY2026 revenue more than
doubled `(2,302.00 ÷ 1,112.66 = +106.89%)` for reasons that have nothing to do with BSE's growth
driver. MCX also carries a physical-delivery warehouse business (warehouse income ₹10.70 cr) that BSE
has no analogue for.

### 1.3 Why CDSL belongs — and the conflict that has to be stated

CDSL is a **different layer of the value chain**: a depository, not an exchange. It earns nothing on
turnover; it earns on issuer count, market-cap slabs, demat-account count and per-debit charges.

**It is also not an arm's-length peer, and this must be on the record before any comparison is used.**
BSE Limited is **CDSL's promoter**, holding 3,13,50,000 shares = **15.00%**
`[CDSL AR FY26, Note 13/24, PDF p317]`; CDSL's corporate governance report records sitting fees paid to
"the Nominating Institution i.e. BSE Limited (Promoter)" `[CDSL AR FY26, CG Report, PDF p~137]`. CDSL is
an **equity-method associate inside BSE's own consolidated accounts**, contributing to the ₹6,542 lakh
share of associate profit `[AR FY26, Consolidated P&L, PDF p164/pr153]`. And **both companies are audited
by the same firm** — S.R. Batliboi & Co. LLP, FRN 301003E/E300005 `[AR FY26, Consolidated BS, PDF
p163/pr152]`; `[CDSL AR FY26, Consolidated BS, PDF p287]`.

**Comparable on:** cost structure, restricted-versus-distributable equity, disclosure architecture,
MII governance (CDSL is also under a Public Interest Director regime), penalty and financial-disincentive
history, operating leverage to a regulated fee.
**NOT comparable on:** take-rate or realisation — there is no turnover in a depository, so no per-unit
economics bridge exists. Also **not usable as independent corroboration of BSE's disclosure standard**,
because a shared auditor and a promoter relationship mean any similarity in accounting presentation is
not an independent observation. Where CDSL agrees with BSE, that agreement carries less weight than
NSE's, MCX's or IEX's; where CDSL **disagrees** with BSE — as it does on the Ind AS 115 timing split —
the disagreement is *stronger* evidence, because it survives the shared auditor.

### 1.4 Why IEX belongs

IEX runs the same *machine* as BSE — a matching engine that takes a fee on activity it does not own —
over an entirely different underlying and, decisively, **under a different regulator**. It is not a SEBI
entity at all: it is licensed by the Central Electricity Regulatory Commission under the Electricity Act
2003 and the CERC (Power Market) Regulations `[IEX AR FY26, CG Report, PDF p~120]`.

**Comparable on:** the exchange business model, revenue concentration in a single transaction-fee line,
operating leverage to exogenous volume, disclosure of a regulated realisation, cost structure,
restricted equity.
**NOT comparable on:** (a) the regulatory-levy rate — a CERC annual fee is not a SEBI turnover fee and
the two cannot be put on a common rate basis; (b) governance structure — IEX has **no Public Interest
Directors** and **no chair/CEO separation** (Satyanarayan Goel is Chairman *and* Managing Director
`[IEX AR FY26, Note 45, PDF p287]`), so the SECC independence quota has no analogue there; (c) clearing
risk — IEX runs no clearing corporation and no Core SGF of its own.

### 1.5 Peers considered and excluded

**NSDL** — the second depository, listed in 2025. Excluded from this pass because CDSL already occupies
the depository slot and NSDL adds no dimension CDSL does not cover, while costing a full document read.
**Recorded as a decision, not an omission** (doctrine §3): if the depository comparison ever carries a
conclusion on its own, NSDL is the corroborating read to add.
**Global exchanges (CME, HKEX, Deutsche Börse)** — excluded. Different accounting framework, different
regulatory-levy regime, no SEBI turnover fee, and the pricing power question the overlay poses (§6) is
jurisdiction-specific. A comparison would fail the "same definitions" test in §5 below.

---

## 2. Definitional bridges — every difference that had to be crossed

Doctrine requires these stated before the tables, not after.

| # | Difference | Bridge applied |
|---|---|---|
| 1 | **Reporting unit.** BSE, CDSL and IEX report in ₹ **lakh**; NSE and MCX in ₹ **crore** | Every figure in §3–§4 converted to **₹ crore** (1 crore = 100 lakh). BSE's ₹4,83,395 lakh = ₹4,833.95 cr |
| 2 | **Period** | All five have 31-Mar year ends. FY2026 = year ended 31-Mar-2026 for all five. FY2025 comparatives are taken from each company's **own FY2026 report**, so no figure crosses a restatement boundary |
| 3 | **BSE restatements** | FY2017 revenue was restated −27.76% and FY2024 −1.37% `[records/restatements.md]`. **No multi-year BSE growth rate in this document crosses either boundary** — every BSE growth rate is FY2026 over FY2025 as printed in the FY2026 AR |
| 4 | **BSE consolidated vs standalone** | The audited note is consolidated (₹4,833.95 cr); the product split exists only in standalone MD&A (₹4,469.51 cr). Gap `= 4,833.95 − 4,469.51 = 364.44 cr`, **7.54%** of consolidated revenue. Every BSE product share is stated on the standalone base and labelled |
| 5 | **BSE product figures are unaudited** | Equity derivatives, equity cash and StAR MF come from MD&A `[AR FY26, MD&A, PDF p75/pr64]`, on which no auditor has opined (RF-003). Peer product figures are **audited notes**. Any comparison of the two is a comparison of an unaudited number against an audited one and is flagged at each use |
| 6 | **Core SGF placement** | BSE and NSE charge the Core SGF contribution **below** a subtotal, outside "total expenses"; **MCX charges it inside** "Contribution to statutory funds and regulatory fees" within total expenses. Cost-to-revenue ratios are shown on both bases |
| 7 | **Regulatory-levy line composition** | BSE's "Regulatory contribution" bundles four items; NSE's "Regulatory fees" is a single P&L line allocated wholly to Trading Services `[NSE AR FY26, Note 33(c), PDF p163]`; MCX bundles its SGF contribution into the same line; CDSL and IEX bury theirs inside other expenses. §4.2 isolates the **turnover-linked regulator fee only** for each |
| 8 | **NSE one-off** | NSE FY2026 other expenses include **₹1,431.56 cr of SEBI settlement fees** `[NSE AR FY26, Note 30, PDF p160/pr317]` relating to the colocation and dark-fibre matters. BSE has no comparable item. NSE's cost ratio is shown **both** including and excluding it |
| 9 | **Clearing & settlement expense** | BSE shows ₹280.35 cr on the **consolidated** P&L despite owning ICCL — so it is paid externally (interoperability). NSE shows ₹125.08 cr in other expenses. MCX eliminates it on consolidation (standalone only). IEX and CDSL have none. **Not comparable line-for-line**; used only directionally |
| 10 | **Restricted funds** | Comparisons are made on the **audited balance sheet only**. MCX's IPF corpus is explicitly flagged "Unaudited" and is an unconsolidated trust; NSE's IPF corpus appears only in ESG narrative. Both are excluded from §4.4 |
| 11 | **IEX regulator** | CERC, not SEBI. Its ₹0.555 cr annual fee is a flat charge, not a turnover levy. Used as a **structural contrast**, never as a rate benchmark |
| 12 | **Where I could not bridge** | **Restricted-equity composition for NSE and MCX.** NSE's other-equity note folds General reserve, Capital reserve, Capital Redemption reserve, Staff welfare reserve and Investor compensation reserve *into* retained earnings `[NSE AR FY26, SOCIE, PDF p142]`, so the restricted portion is not separately readable; MCX's was not read in this pass. §4.4 therefore compares BSE only against CDSL and IEX. **NOT DISCLOSED** → *NSE AR FY26 Note 13(b) Other Equity component detail, and MCX AR FY26 Other Equity note* |

---

## 3. Revenue mix and concentration — the comparison the overlay permits

The overlay forbids a variable/fixed cost split and a working-capital cycle here. What it permits is
**activity × realisation**, revenue concentration, and disclosure of both. Concentration first.

### 3.1 The grid (FY2026, consolidated, ₹ crore)

| Metric | **BSE** | NSE | MCX | CDSL | IEX |
|---|---|---|---|---|---|
| Revenue from operations | **4,833.95** | 16,601.31 | 2,302.00 | 1,144.92 | 615.65 |
| Total income | **5,148.10** | 18,713.37 | 2,429.05 | 1,238.50 | 746.95 |
| Largest single audited revenue line | **Transaction charges 3,794.99** | Transaction charges 13,057.01 | Transaction fees 2,090.96 | Annual issuer charges 456.36 | Transaction fees 583.96 |
| — as % of revenue from operations | **78.51%** | **78.65%** | 90.83% | 39.86% | 94.85% |
| **Is that line split by product in the audited note?** | **NO** | **YES — 5 lines** | NO | n/a (18 lines, no dominant line) | **YES — 2 lines** |
| Revenue growth FY26 vs FY25 | **+63.46%** | **−3.15%** | +106.89% | +5.79% | +14.59% |
| Total expenses | 1,837.42 | 5,999.90 | 733.82 | 625.41 | 121.18 |
| Expenses / revenue from ops | 38.01% | 36.14% *(27.52% ex-settlement)* | 31.88% | 54.62% | 19.68% |
| Employee cost / revenue from ops | 6.16% | 4.76% | 7.82% | 13.67% | 7.96% |
| PAT (attributable) | 2,496.98 | 10,302.06 | 1,331.55 | 456.13 | 492.92 |
| Total equity (attributable) | 6,673.01 | 32,113.54 | 2,847.94 | 1,959.78 | 1,364.56 |
| ROE on average attributable equity | **45.00%** | 32.98% | 56.27% | 24.52% | 39.42% |
| Core SGF on balance sheet | **1,246.83** | 13,079.15 | 1,367.29 | none | none (member SGF 25.29) |

Sources: `[AR FY26, Consolidated P&L, PDF p164/pr153]`; `[AR FY26, Consolidated BS, PDF p163/pr152]`;
`[AR FY26, Note 22, PDF p211/pr200]`; `[NSE AR FY26, Consolidated P&L, PDF p140/pr318]`;
`[NSE AR FY26, Note 27, PDF p159-160/pr314-317]`; `[MCX AR FY26, Consolidated P&L, PDF p150/pr266-267]`;
`[MCX AR FY26, Note 24, PDF p165/pr297]`; `[CDSL AR FY26, Consolidated P&L, PDF p288]`;
`[CDSL AR FY26, Note 19, PDF p321]`; `[IEX AR FY26, Consolidated P&L, PDF p241]`;
`[IEX AR FY26, Note 27, PDF p273/pr269]`.

**The conclusion this table exists to support.** BSE and NSE hold *the same proportion* of revenue in a
line called "transaction charges" — **78.51% and 78.65%, a gap of 0.14 percentage points**. They are the
same business at the same concentration. NSE splits that line into Cash Market ₹1,554.64 cr, Futures
₹1,480.10 cr, Options ₹9,997.57 cr, Mutual Fund ₹18.04 cr and Others ₹6.66 cr **inside the audited
note**. BSE prints ₹3,794.99 cr and stops. Concentration is therefore not an explanation for
aggregation, and neither is business model, regulator, statute or auditor — the only two variables that
differ are the two companies' own disclosure choices.

### 3.2 Where each MII's FY2026 growth actually came from — five different answers

| Peer | Growth | The line that produced it | What it says about the driver |
|---|---|---|---|
| **BSE** | +63.46% | Equity derivatives **+121.43%** `(3,134.37 ÷ 1,415.54)` while **equity cash −18%** `[AR FY26, MD&A, PDF p75/pr64]` | One product, activity-driven, unaudited at line level |
| NSE | **−3.15%** | Options **−1.93%**, Futures **−14.31%**, Cash **−7.93%** `[NSE AR FY26, Note 27]` | The same regulatory event that made BSE cost NSE |
| MCX | +106.89% | Transaction fees `2,090.96 ÷ 961.80 = +117.40%` | Commodity options ramp — unrelated cycle |
| CDSL | +5.79% | Annual issuer charges **+40.18%** offsetting transaction charges **−9.93%** and online data charges **−27.88%** | Growth came from a **regulated annual fee**, not activity |
| IEX | +14.59% | Electricity volume 141 BU, **+17%** `[IEX AR FY26, PDF p25/pr20]` at a flat CERC-set rate | Pure volume at a fixed regulated realisation |

**Conclusion.** The overlay's §6 hypothesis — that pricing power sits with the regulator and the
competing exchange, not with the company — is confirmed across all five. **Not one of the five moved a
price it controls.** BSE and MCX gained on a regulator-authored redistribution; NSE lost on the same
event; CDSL grew because SEBI reset an annual fee slab; IEX grew on volume at a CERC-capped rate. The
distinction that matters for BSE is not that it is a price-taker — they all are — but *which* exogenous
variable it is exposed to, and §4.3 shows that its exposure is the narrowest of the five.

### 3.3 Take-rate and realisation — where it can be derived, and where the disclosure forbids it

The overlay makes activity × realisation mandatory for a transaction-charge line. Whether it can be
performed is itself the finding.

| Peer | Realisation derivable from **audited** statements? | FY2026 realisation | Movement |
|---|---|---|---|
| **IEX** | **Yes.** Audited note gives the electricity transaction fee separately | `55,851.37 lakh ÷ 141 BU = ₹396.11 lakh per BU` = **3.96 paise/kWh** | FY25 `47,833.81 ÷ 120.51 = ₹396.93 lakh per BU` → **−0.21%**, i.e. flat at the CERC-capped rate |
| **NSE** | **Yes.** Options transaction charges disclosed separately | ₹9,997.57 cr against disclosed options activity | Options revenue −1.93% |
| **BSE** | **No.** The audited note gives one aggregate. Only an **unaudited MD&A** number permits the calculation | ESTIMATE: realisation index `(3,13,437 ÷ 19,523) ÷ (1,41,554 ÷ 8,978) = 16.055 ÷ 15.767 = 1.0183` → **+1.83%** | **Assumption named:** trading-day count unchanged FY25→FY26, which cancels in the ratio. Sources: charges `[AR FY26, MD&A, PDF p75/pr64]`, premium turnover `[AR FY26, MD&A, PDF p59/pr48]` |
| MCX | No — transaction fees is one line | not derivable | — |
| CDSL | n/a — no turnover exists in a depository | — | — |

**Conclusion.** BSE's FY2026 revenue growth is **98% activity and 2% realisation**: transaction charges
in equity derivatives grew +121.43% against premium turnover +117.45%, leaving realisation up 1.83%.
That is a clean result — and it rests entirely on a management-authored number in the MD&A. IEX's
equivalent result rests on an audited note. **The same analytical step is audited at the peer and
unaudited at BSE.**

> **Independent corroboration.** W2_industry reached derivatives realisation **+1.8%** for FY2026 by a
> different route (RF-021), against this wave's +1.83% computed from the charge-to-premium ratio. Two
> agents, two methods, the same number to one decimal place. RF-021 also establishes the contrasting
> half this wave could not: equity-cash realisation **fell ~19.5%** on turnover that **rose 2.36%**,
> so the MD&A's "industry-wide reduction in average daily turnover value" explanation is refuted by
> BSE's own document. The realisation story is therefore **up 1.8% in derivatives and down 19.5% in
> cash in the same year** — which is a repricing in one product, not a market condition.

---

## 4. The four structural comparisons the overlay mandates

### 4.1 Disclosure quality — the verdict

This is the load-bearing section. Every cell was read in the source document, not inferred.

| Disclosure | **BSE FY26** | NSE FY26 | MCX FY26 | CDSL FY26 | IEX FY26 |
|---|---|---|---|---|---|
| Audited revenue-from-operations note with line-level split | **YES — 11 components** | YES — 17 lines | YES — 10 lines | YES — 18 lines | YES — 5 lines |
| **Split of the dominant transaction line inside that note** | **NO** | **YES** (Cash / Futures / Options / MF / Others) | NO | n/a | **YES** (Electricity / Certificates) |
| **Ind AS 115 timing split** (point in time vs over time) | **NO** | **YES** 13,456.94 / 3,144.37 | **YES** 2,103.70 / 198.30 | **YES** 67,317.01 / 47,174.86 | **YES** 58,771.57 / 2,793.13 |
| Reconciliation of contracted price to revenue recognised | **NO** | **YES** 15,805.31 → 15,759.62 | **YES** 2,306.99 → 2,302.00 | NO | **YES** 63,167.26 → 61,564.70 |
| Contract-liability balance disclosed | **NO** | **YES**, split current/non-current | **YES** (income received in advance ₹4.99 cr) | NO — policy prose only | **YES**, with a full rollforward |
| Customer concentration statement | **NO** (receivables only) | YES — explicit negative statement | NO | YES — per-entity, per-customer | **YES** — ₹9,862.24 lakh single customer |

*Qualification on the last row, per RF-023.* Ind AS 108.34 requires a major-customer disclosure only where
a customer exceeds 10% of revenue. IEX and CDSL disclose because they **have** such customers; BSE
plausibly does not, so **no trigger arises and no standard is breached**. The residual difference is
narrow but real: NSE, at BSE's scale and concentration, publishes an **explicit negative statement**
("does not have any single customer... more than 10%"), which is information; BSE publishes silence,
which is not. This row is the weakest in the table and is not load-bearing for the verdict.
| Ind AS 108 segment note with revenue **and result** | **NO — one segment** | **YES — 3 segments**, plus assets, liabilities, capex, depreciation | NO — one segment | **YES — 3 segments** | NO — one segment |

Sources: `[AR FY26, Note 22, PDF p211/pr200]`; `[AR FY26, Note 39, PDF p~229]`;
`[NSE AR FY26, Note 27 and 27.1, PDF p159-160/pr314-317]`; `[NSE AR FY26, Note 33, PDF p163-164]`;
`[MCX AR FY26, Note 24, PDF p165/pr297]`; `[CDSL AR FY26, Note 19 and 19.1, PDF p321]`;
`[CDSL AR FY26, Note 35, PDF p339-340]`; `[IEX AR FY26, Note 27 and 24(a), PDF p272-273]`.

**VERDICT — the gap is graded at the maximum severity doctrine §2b allows.**

- On the **Ind AS 115 timing disaggregation**, the peer set is **unanimous: 4 of 4 disclose it, BSE does
  not**. This is not a case of nobody disclosing. It is a case of everybody disclosing except BSE —
  including the peer that shares BSE's auditor and the peer BSE itself promotes.
- On the **product split of the dominant transaction line**, the decisive comparator is NSE, because the
  concentration is identical to two decimal places (78.65% vs 78.51%) and the regulator, statute, product
  and clearing structure are the same. NSE's ₹9,997.57 cr options line is an **audited** figure. BSE's
  ₹3,134.37 cr equity-derivatives figure exists **only in unaudited MD&A**. The single number that
  determines BSE's investment case is attested at the competitor and unattested at BSE.
- On **segment reporting**, RF-013 is settled — and the grade is **split, not unanimous**, which must be
  said plainly because it is the weaker of the two verdicts here. **Two of four peers disclose:** NSE
  gives a Clearing Services segment with revenue ₹1,762.37 cr, result ₹1,105.35 cr, assets ₹46,729.63 cr,
  liabilities ₹46,811.09 cr, capex ₹154.63 cr and depreciation ₹108.51 cr, identifying Core SGF *inside*
  segment assets; CDSL gives three segments with revenue, result, assets and liabilities. **Two of four
  do not:** MCX and IEX each report a single segment, as BSE does. What makes NSE decisive despite the
  split is that it is the only peer with BSE's exact structure — an exchange consolidating its own
  clearing corporation — and it is precisely the clearing arm it chooses to segment.
- **BSE's own within-note asymmetry.** In FY2026 BSE split "Other operating income" — **₹348.51 cr,
  7.21% of revenue** — into six named lines (colocation ₹171.09 cr, data ₹67.63 cr, index ₹36.61 cr,
  software ₹26.64 cr, subscription ₹45.94 cr, auction ₹0.60 cr), while leaving **₹3,794.99 cr, 78.51% of
  revenue** as one line. Granularity was added exactly where it was immaterial and withheld exactly
  where it decides the case.

**Correction to RF-003 — reached independently, and now converged (doctrine §10).** RF-003 originally
stated that BSE has "zero Ind AS 115 disaggregation table". Read against the audited note that is too
strong: `[AR FY26, Note 22, PDF p211/pr200]` **is** a component split, tying exactly to the face of the
P&L. This wave reached that correction from the peer side; W1_ledger reached it from the document side
and has already downgraded RF-003 from High to Medium. **Both waves agree on the substance.** The
precise, defensible statement is: **BSE publishes a component note but no Ind AS 115 *disaggregation* in
the standard's sense — no timing split, no contract-price reconciliation, no contract balances — and the
component note stops immediately above the only component that matters.**

> **One arithmetic disagreement, left open rather than resolved.** W1_ledger describes Note 22 as "a
> four-way service-line split with **twelve** sub-lines"; this wave counts **eleven** named revenue
> components in four service groups — Trading 1 (transaction charges), Listing 3, Treasury 1, Other
> operating 6, so `1 + 3 + 1 + 6 = 11`. Both agree on the four groups and on the tie-out to 4,83,395.
> Neither position is deleted; the count is a QC item for W3_revenue against the printed note.

**The trend is adverse without any accounting change.** Transaction charges as a share of revenue from
operations: **FY2024 41.92%** `(58,271 ÷ 1,39,003)` → **FY2025 68.64%** `(2,02,993 ÷ 2,95,734)` →
**FY2026 78.51%** `(3,79,499 ÷ 4,83,395)` `[AR FY2024, Note 22, PDF p207]`; `[AR FY2025, Note 22, PDF
p195]`; `[AR FY26, Note 22, PDF p211/pr200]`. The share of revenue sitting inside one undecomposed
audited line rose **36.59 percentage points in two years**. The disclosure did not deteriorate; the
business concentrated into the part of the disclosure that was already blank.

### 4.2 Regulatory-contribution burden — the sharpest number in this document

The overlay (§3) sets the test: a levy rising with revenue is expected; rising *faster* is the finding.
The peer set reveals something the single-company view cannot — that BSE's **level** is the anomaly.

| Peer | Turnover-linked regulator fee, FY2026 | % of revenue from ops | Revenue earned per ₹1 of levy |
|---|---|---|---|
| **BSE** | SEBI regulatory fees **₹566.16 cr** | **11.71%** | **₹8.54** |
| NSE | Regulatory fees **₹796.35 cr** | **4.80%** | **₹20.85** |
| MCX | SEBI regulatory fees ₹17.36 cr | 0.75% | ₹132.60 |
| CDSL | Annual SEBI fees ₹9.05 cr | 0.79% | ₹126.51 |
| IEX | CERC regulatory fee ₹0.555 cr | 0.09% | ₹1,109.27 |

Arithmetic shown: BSE `566.16 ÷ 4,833.95 = 11.71%` and `4,833.95 ÷ 566.16 = ₹8.54`; NSE
`796.35 ÷ 16,601.31 = 4.80%` and `16,601.31 ÷ 796.35 = ₹20.85`. Ratio `11.71 ÷ 4.80 = 2.44×`.
Sources: `[AR FY26, Note 27, PDF p213/pr202]`; `[NSE AR FY26, Consolidated P&L, PDF p140/pr318]`;
`[MCX AR FY26, Note 30, PDF p167]`; `[CDSL AR FY26, Note 24, PDF p324]`;
`[IEX AR FY26, Note 32, PDF p275/pr271]`.

On the all-in basis (every statutory fund plus the Core SGF contribution): BSE
`(649.69 + 76.96) ÷ 4,833.95 = 15.03%`; NSE `(796.35 + 0.58) ÷ 16,601.31 = 4.80%`; MCX
`163.73 ÷ 2,302.00 = 7.11%`; CDSL `(9.05 + 23.75 + 0.10) ÷ 1,144.92 = 2.87%`; IEX `0.09%`.

**The mechanism, in BSE's own words.** *"The SEBI turnover fee is based on the notional trading, the
clearing expense is based on the number of contracts, and we earn revenue based on premium"*
`[Concall 13May2026, MD & CEO, p14]`. And, on why the gap against NSE exists: *"The premium to notional
ratio of Sensex vis-a-vis comparable indices in the market, the ratio at Sensex is lower"*
`[Concall 13May2026, MD & CEO, p19]`.

**That closes the loop.** The levy is charged on notional; revenue is earned on premium; BSE's
premium-to-notional ratio is structurally below NSE's; therefore BSE pays more levy per rupee of revenue
than NSE does — **2.44× more** — for reasons that are a property of the Sensex options market, not of
BSE's cost discipline. The peer number, the BSE number and the management-stated mechanism agree.

**What the peer number adds to RF-019.** W2_industry has established that SEBI's 26-Apr-2024 letter
re-based the fee to notional option value **retrospective to FY2007 with 15% interest**, costing
₹22,421 lakh across FY2024–FY2025 — 21.8% of FY2024 PAT (RF-019). That establishes the *event*. The peer
comparison establishes the *steady state*: even with the retrospective charge behind it, BSE's ongoing
levy burden is **2.44× the only comparable exchange's**, and the differential is not a one-off
adjustment but a permanent property of the Sensex premium-to-notional ratio. RF-019 and this finding are
the same mechanism measured at two different times, and neither substitutes for the other.

**The levy tracks its base almost exactly, which is the proof the base is notional.** SEBI regulatory
fees `56,616 ÷ 33,141 = +70.83%` against daily-average options notional turnover
`1,87,15,375 ÷ 1,10,66,674 = +69.12%` — a levy-per-unit-of-notional movement of `1.7083 ÷ 1.6912 =
+1.02%`. Over the same year, transaction charges tracked **premium** to within 1.83% (§3.3). Two
different revenue-and-cost bases, each tracking its own driver to within 2%.

### 4.3 Operating leverage to activity — and the ratio that actually produced FY2026's margin

The overlay (§5) replaces the variable/fixed split with leverage to turnover plus the regulated rate.

BSE's FY2026 operating margin before the Core SGF charge rose from `1,75,568 ÷ 3,23,631 = 54.25%` to
`3,31,068 ÷ 5,14,810 = 64.31%` — **+10.06 percentage points** `[AR FY26, Consolidated P&L, PDF
p164/pr153]`.

Decompose it against the two bases:

| Quantity | FY2026 | FY2025 | Change |
|---|---|---|---|
| Daily-avg options **premium** turnover (revenue base) | ₹19,523 cr | ₹8,978 cr | **+117.45%** |
| Daily-avg options **notional** turnover (levy base) | ₹1,87,15,375 cr | ₹1,10,66,674 cr | **+69.12%** |
| **Premium ÷ notional ratio** | **0.10432%** | **0.081126%** | **+28.59%** |

`[AR FY26, MD&A, PDF p59/pr48]`. Arithmetic: `19,523 ÷ 18,715,375 = 0.0010432`;
`8,978 ÷ 11,066,674 = 0.00081126`; `0.0010432 ÷ 0.00081126 = 1.2859`.

**Conclusion.** BSE's revenue base grew 48.33 percentage points faster than its levy base
`= 117.45 − 69.12`, purely because option premium rose relative to notional — which is implied
volatility and moneyness, not an operating decision. Management states it is not forecastable: *"Whether
we can predict this trend, it is, of course, not predictable... the correlation between the clearing and
settlement expenses versus the premium cannot be predicted"* `[Concall 13May2026, MD & CEO, p14]`.

**The peer set is what makes this a finding rather than an observation.** IEX's levy base and revenue
base are the *same physical quantity* (electricity units), and its CERC fee **fell 5.13%**
`(55.50 ÷ 58.50)` while volume rose 17% — zero base mismatch, zero margin exposure to a ratio. CDSL's
fee base and revenue base are both slabs. MCX's SEBI fee is 0.75% of revenue, too small to move margin.
NSE has the same three-base structure as BSE but earns 2.44× more revenue per rupee of levy, so the same
ratio movement moves NSE's margin far less. **BSE is the only member of this peer set whose operating
margin is materially geared to a market-structure ratio it does not control**, and it is geared to it
from the least favourable starting point in the set.

### 4.4 Restricted versus distributable equity, and ROE on the right base

The overlay's mandatory equity rule: state the basis.

**BSE's presentation is a genuine strength and must be said first.** BSE reports Core Settlement
Guarantee Funds of **₹1,246.83 cr as a separate balance-sheet category between equity and liabilities**
`[AR FY26, Consolidated BS, PDF p163/pr152]` — so total equity of ₹6,795.50 cr is *already* clean of
restricted clearing capital. NSE and MCX use the same presentation. This part of the overlay's warning
does not bite at BSE.

**What does bite is inside equity.** BSE carries a **Capital reserve of ₹661.79 cr** created under the
BSE (Corporatisation & Demutualisation) Scheme, 2005, which the note states *"shall not be used for
purposes other than the operations of the Exchange"* `[AR FY26, Note 15.2, PDF p205/pr194]` — a
permanent, non-distributable block. With capital reserve on business combination ₹105.30 cr and the LES
reserve ₹0.09 cr (which the IFSCA circular says *"will not form part of net worth"*):

`661.79 + 105.30 + 0.09 = ₹767.18 cr restricted` → `767.18 ÷ 6,673.01 = 11.50% of attributable equity`.

| Peer | Restricted reserves inside equity | % of attributable equity | ROE on avg total attributable equity | ROE on avg equity ex-restricted |
|---|---|---|---|---|
| **BSE** | ₹767.18 cr — 2005 Demutualisation Scheme capital reserve | **11.50%** | `2,496.98 ÷ 5,548.37 = 45.00%` | `2,496.98 ÷ 4,781.20 = 52.23%` |
| CDSL | **nil** — other equity is retained earnings + OCI; General reserve is zero | **0.00%** | `456.13 ÷ 1,860.06 = 24.52%` | same, 24.52% |
| IEX | ₹19.62 cr — ESOP trust reserve, ESOP outstanding, capital redemption | **1.44%** | `492.92 ÷ 1,250.43 = 39.42%` | `492.92 ÷ 1,231.48 = 40.03%` |

`[AR FY26, Note 15, PDF p205/pr194]`; `[CDSL AR FY26, Note 13, PDF p318]`;
`[IEX AR FY26, SOCIE, PDF p243/pr239]`. NSE and MCX excluded per bridge #12.

**Conclusion, and it runs opposite to the overlay's stated direction.** The overlay warns that ROE on
total equity *overstates* return on shareholders' capital. At BSE the arithmetic runs the other way:
restricted funds sit in the **denominator**, so total-equity ROE **understates** the return on
genuinely distributable capital by **7.23 percentage points** `= 52.23 − 45.00`. BSE is nonetheless the
only member of the comparable set carrying a material permanently-restricted equity block, and the
reason is structural rather than managerial: **BSE is the only one of the five that was ever a mutual
members' association** (founded 1875, demutualised 2005). CDSL, IEX, NSE and MCX were all incorporated as
companies. The reserve is a fossil of that history and it will never be distributed.

**Regulatory capital per ₹1 of revenue — and the disconfirming result.** Overlay §5 replaces capital
intensity with regulatory capital intensity. Core SGF ÷ revenue from operations: **BSE ₹0.258**
`(1,246.83 ÷ 4,833.95)`; **NSE ₹0.788** `(13,079.15 ÷ 16,601.31)`; **MCX ₹0.594**
`(1,367.29 ÷ 2,302.00)`; CDSL nil; IEX ₹0.041 and it is members' money. **BSE is the *least*
regulatory-capital-intensive of the three exchange-plus-clearing groups**, by a factor of three against
NSE. This cuts squarely against a "BSE's growth is capital-hungry" reading and is recorded as such.

**BSE's Core SGF note is, on its own terms, good disclosure.** Note 41 gives a contributor-by-segment
matrix: ICCL ₹608.96 cr, BSE ₹179.52 cr, **NSE ₹265.29 cr**, MSE ₹9.34 cr, Other ₹169.53 cr, total
₹1,232.64 cr `[AR FY26, Note 41, PDF p232/pr221]`, which ties exactly to the balance sheet once India
ICC's IFSC fund is added: `1,232.64 + 14.19 = 1,246.83` ✓ `[AR FY26, Note 42, PDF p232/pr221]`. Two
facts fall out. First, **the BSE group funds 63.97%** of its own clearing guarantee `(608.96 + 179.52) ÷
1,232.64` and **its competitor funds 21.52%** `(265.29 ÷ 1,232.64)` — the consequence of interoperability,
mirrored on the other side where BSE contributes ₹195.05 cr to NSE Clearing's Core SGF
`[NSE AR FY26, Note 41, PDF p169]`. Second, **78.23% of the fund sits in the equity-derivative segment**
`(964.32 ÷ 1,232.64)` against 70.13% of standalone revenue — while the equity **cash** segment holds
17.87% of the fund `(220.32 ÷ 1,232.64)` for 5.60% of revenue `(250.21 ÷ 4,469.51)`. The cash segment is
**3.19× more capital-hungry per rupee of revenue** than the group average; derivatives is 1.12×.

---

## 5. Governance-structural comparison

| Fact | **BSE** | NSE | MCX | CDSL | IEX |
|---|---|---|---|---|---|
| Promoter | **None** — *"There are no promoters identified for the Company"* | None disclosed | **None** — *"There are no promoters for the Company"* | **BSE Limited, 15.00%** | **None** — promoter shareholding **Nil** |
| Largest shareholder | LIC 5.57% | LIC 10.72% | Kotak Mahindra Bank >10% | BSE Limited 15.00% | no holder identified as promoter |
| Ownership cap regime | SEBI SECC | SEBI SECC | SEBI SECC | SEBI D&P | CERC Power Market Regulations |
| Regulator-approved directors | **6 of 8 = 75% Public Interest Directors** | SECC regime applies | SECC regime applies | **6 of 11 = 54.54% PID/ID** | **None — ordinary Independent Directors only** |
| Chair / CEO separation | **Mandatory; Chairperson must be a PID** | separate | separate | **Chairperson is a PID** | **NO — Chairman *and* Managing Director are the same person** |
| Statutory auditor | **S.R. Batliboi & Co. LLP** (FRN 301003E/E300005) | Price Waterhouse & Co CA LLP | V. Sankar Aiyar & Co (FRN 109208W) | **S.R. Batliboi & Co. LLP — same firm as BSE** | Walker Chandiok & Co LLP |
| Auditor term / rotation | FY2018→**FY2027, the 10-year statutory maximum**; no successor process disclosed | term ends at the 34th AGM in 2026; **successor already board-approved** (Walker Chandiok & Co LLP) | re-appointed 12-Sep-2025 for FY2026–FY2030 | appointed at the 25th AGM (2023) to the 30th AGM | appointed at the 18th AGM (2024) for 5 years |
| FY2026 monetary regulatory action | SEBI ₹25 lakh (Jun-2025, paid); GST demand ₹7.25 cr (under appeal) | **SEBI settlement provision ₹1,391.21 cr**; ₹40.35 cr and ₹643.05 cr already paid | financial disincentive ₹1.00 cr (glitch); SEBI ₹25 lakh (May-2025) | **financial disincentive ₹3.00 cr** for technical glitches 2021–2024 | **"No Non-Compliance"** across FY24, FY25, FY26 |

Sources: `[AR FY26, Note 45(i), PDF p~231]`; `[AR FY26, CG Report, PDF p78, p94, p95/pr84]`;
`[NSE AR FY26, Note 13(a), PDF p156]`; `[NSE AR FY26, Board's Report, PDF p74]`;
`[NSE AR FY26, Note 30.2 and 36, PDF p166]`; `[MCX AR FY26, Note 45(ix), PDF p144]`;
`[MCX AR FY26, BRSR, PDF p97]`; `[CDSL AR FY26, Note 13, PDF p317]`; `[CDSL AR FY26, BRSR, PDF p185]`;
`[CDSL AR FY26, Board's Report §13, PDF p~85]`; `[IEX AR FY26, Board's Report, PDF p75, p78]`;
`[IEX AR FY26, CG Report, PDF p121/pr117]`.

**Three conclusions.**

1. **On board structure BSE is the strongest in the set, and it is structural, not chosen.** 75% Public
   Interest Directors and a mandatory PID chairperson exceed CDSL's 54.54% and are unavailable to IEX,
   which under CERC has no PID concept at all and combines Chairman and Managing Director in one person.
   For a company with no promoter, the SECC quota is the substitute for a controlling-shareholder
   discipline, and BSE has more of it than any comparator.
2. **On penalty scale, BSE's exposure is the smallest of the two SEBI-regulated exchanges by three
   orders of magnitude.** BSE's FY2026 SEBI penalty was ₹0.25 cr; NSE provided **₹1,391.21 cr** against
   pending settlement applications, which is why NSE's FY2026 PAT fell 15.5% `(10,302.06 ÷ 12,187.69)`.
   Against BSE's FY2026 PAT of ₹2,496.98 cr, the ₹0.25 cr penalty is **0.010%**; NSE's provision is
   **13.5% of its own PAT** `(1,391.21 ÷ 10,302.06)`. This is strong disconfirming evidence against any
   reading that treats BSE's supervision record as an outlier: on money, it is the best in the set.
3. **The CDSL relationship is a structural entanglement that must be carried into W3_group_rpt.** BSE is
   simultaneously CDSL's **promoter** (15.00%), an **equity-method associate holder** consolidating
   CDSL's profit, a **board nominator** receiving a director's sitting fees, and a **co-auditee of the
   same firm**. None of that is a breach — all of it is disclosed — but it means CDSL's numbers are not
   independent evidence about BSE's accounting standard, and it is the single largest related-party
   structure in the group.

---

## 6. Chain record

```
### CHAIN: Transaction charges (consolidated) | FY26
L1 REPORTED   TRACED | Rs 3,79,499 lakh, 78.51% of revenue from operations Rs 4,83,395 lakh | [AR FY26, Note 22, PDF p211/pr200]
L2 COMPONENTS NOT-DISCLOSED | one aggregate line; no equity-derivative / equity-cash / StAR MF split in any audited note FY2024-FY2026 -> AR FY26 audited Note 22 product disaggregation, which does not exist; the direct competitor publishes the equivalent split at [NSE AR FY26, Note 27, PDF p159/pr314]
L3 DRIVER     DERIVED | activity 98% / realisation 2%: charges 3,13,437 / 1,41,554 = +121.43% against daily-avg premium turnover 19,523 / 8,978 = +117.45%; realisation index 2.21434 / 2.17453 = 1.0183 = +1.83% | [AR FY26, MD&A, PDF p75/pr64]
L4 COUNTERPARTY NOT-DISCLOSED | trading members; prop-vs-client and member-concentration split absent, and no >10%-of-revenue customer statement exists -> AR FY26 financial-instruments credit-risk note, which discloses receivable concentration only; peers disclose revenue concentration at [NSE AR FY26, Note "Concentration Risk", PDF p172]
L5 RECOGNITION TRACED | Ind AS 115, recognised at a point in time as the transaction completes; policy unchanged FY2024-FY2026; no timing disaggregation published | [AR FY26, Material accounting policy 2, PDF p~176]
L6 BALANCE-SHEET DERIVED | net trade receivables 55,316 / 30,967 = +78.6% against revenue from operations +63.5%; receivables 11.44% of revenue = 55,316 / 4,83,395 vs 10.47% = 30,967 / 2,95,734. W1_ledger reports +87.1% on a GROSS basis and unbilled +128.3% (RF-026); both are true on their own bases and the gross figure is the more adverse | [AR FY26, Consolidated BS, PDF p163/pr152]
L7 CASH       NOT-DISCLOSED | own-account cash cannot be separated from member and settlement float; clearing-and-settlement liabilities 3,55,423 lakh sit inside the same cash pool -> AR FY26 segment note, which reports one segment; the competitor publishes segment assets and liabilities at [NSE AR FY26, Note 33(d)/(e), PDF p164]
L8 SUSTAIN    ESTIMATE | repeats only while the premium-to-notional ratio holds; it rose 0.081126% to 0.10432% = +28.59% in FY2026, and management states the trend is "not predictable" | [AR FY26, MD&A, PDF p59/pr48]
CHAIN-STATE: BROKEN at L2/L4
```

---

## 7. Findings

### FINDING: Every peer publishes the audited revenue disaggregation BSE omits, and NSE splits the identical line at an identical concentration
S1 WHAT: BSE's audited Note 22 reports "Transaction charges Rs 3,79,499 lakh" as a single undecomposed line, 78.51% of consolidated revenue from operations, with no Ind AS 115 timing split, no contracted-price reconciliation and no contract-liability balance; NSE's audited Note 27 splits its equivalent line into Cash Market, Futures, Options, Mutual Fund and Others, and publishes all three of the disclosures BSE omits.
S2 WHY: Not concentration, not business model, not regulator, not statute and not auditor. NSE holds 78.65% of revenue in the same line against BSE's 78.51% - a gap of 0.14 percentage points - under the same SEBI SECC Regulations, in the same products, with its own clearing corporation. IEX, whose transaction fee is 94.85% of revenue, is *more* concentrated than BSE and still splits it. CDSL, which shares BSE's auditor S.R. Batliboi & Co. LLP, publishes the timing split BSE does not. Every candidate explanation other than BSE's own disclosure choice is eliminated by a peer.
S3 EVIDENCE: BSE transaction charges Rs 3,794.99 cr = 78.51% of revenue from operations Rs 4,833.95 cr [AR FY26, Note 22, PDF p211/pr200]. Counter-proportion within the same note: BSE splits "Other operating income" of Rs 348.51 cr - only 7.21% of revenue - into six named lines, while leaving 78.51% as one. Peer counter-proportion: NSE transaction charges Rs 13,057.01 cr = 78.65% of revenue Rs 16,601.31 cr, split five ways audited, of which Options alone is Rs 9,997.57 cr [NSE AR FY26, Note 27, PDF p159-160/pr314-317]. Ind AS 115 timing split disclosed by NSE 13,456.94/3,144.37, MCX 2,103.70/198.30, CDSL 67,317.01/47,174.86, IEX 58,771.57/2,793.13 - four of four - and by BSE not at all. Trend without any accounting change: the share of revenue inside BSE's one blank line went 41.92% (58,271/1,39,003) in FY2024 to 68.64% (2,02,993/2,95,734) in FY2025 to 78.51% in FY2026, a rise of 36.59 percentage points in two years.
S4 CONNECTS: Note 22 and the P&L face give the aggregate; the MD&A carries the only product split and no auditor has opined on it; the Ind AS 108 note reports one segment so no cost attaches to any line either; NSE's audited note and three-segment note show the same institution type disclosing both; management's own concall explains why the split matters, because revenue, the regulatory levy and the clearing cost each run off a different base.
DOMAINS: IncomeStatement, Notes, MgmtCommentary, Industry, Governance
DISCONFIRM: Sought and partly found, and it moderates the claim. BSE's Note 22 is not empty - it carries eleven named components that tie exactly to the P&L, which is more than RF-003's "zero disaggregation" implies, and that correction is recorded in section 4.1 rather than substituted. MCX also leaves its transaction-fee line undecomposed, so BSE is not unique on that specific point. BSE's Core SGF note 41 is genuinely granular, giving a contributor-by-segment matrix that ties exactly (1,232.64 + 14.19 = 1,246.83), so this is not a company that cannot produce detail. What survives all three is the timing disaggregation, where the peer set is unanimous four to nil against BSE.
S5 MEANS: The single largest input to BSE's investment case - what share of earnings is one three-year-old index-option product - is attested at the direct competitor and unattested at BSE, so a reader must take on management's word the one number that decides the case.
BASE-RATE: No realised loss is attributable to this gap at BSE, and none is claimed. The base rate that exists is a disclosure-asymmetry pattern already on this company's record: RF-002 shows a Rs 5.05 cr ICCL penalty appearing in exactly one document while a penalty twenty times smaller received three slots. In the wider system, SEBI levied a Rs 3.00 cr financial disincentive on CDSL and Rs 1.00 cr on MCX for operational failures in the same window, so the regulator does convert disclosure and control failures into money in this sector - but never yet at BSE on this ground.
S6 IMPLICATION: Any durability judgement on roughly 70% of BSE's revenue rests on an unaudited management schedule, so the margin of safety demanded of that earnings stream should be set against unaudited evidence rather than audited evidence, and the monitorable is whether the FY2027 Note 22 carries a timing disaggregation and a transaction-charge product split; the thesis-breaker is a restatement or reclassification inside the MD&A split that the audited note could not have caught.
SEVERITY: High

### FINDING: BSE pays 2.44 times NSE's regulatory levy per rupee of revenue because the levy base is notional and the revenue base is premium
S1 WHAT: BSE's SEBI regulatory fees were Rs 566.16 cr in FY2026, 11.71% of revenue from operations, against NSE's regulatory fees of Rs 796.35 cr, 4.80% of revenue - so BSE earns Rs 8.54 of revenue per rupee of levy where NSE earns Rs 20.85.
S2 WHY: The two exchanges are charged on notional turnover and paid on premium turnover, and BSE's premium-to-notional ratio is structurally lower. Management states both halves: "the SEBI turnover fee is based on the notional trading, the clearing expense is based on the number of contracts, and we earn revenue based on premium", and "the premium to notional ratio of Sensex vis-a-vis comparable indices in the market, the ratio at Sensex is lower", which it attributes to Sensex monthly and longer-dated contracts being undeveloped in a three-year-old product.
S3 EVIDENCE: BSE 566.16 / 4,833.95 = 11.71% and 4,833.95 / 566.16 = Rs 8.54 [AR FY26, Note 27, PDF p213/pr202]. NSE 796.35 / 16,601.31 = 4.80% and 16,601.31 / 796.35 = Rs 20.85 [NSE AR FY26, Consolidated P&L, PDF p140/pr318], with NSE's segment note allocating the whole line to Trading Services so the comparison is like for like [NSE AR FY26, Note 33(c), PDF p163]. Ratio 11.71 / 4.80 = 2.44. Counter-proportion that identifies the base: within BSE's own Note 27, SEBI regulatory fees grew 56,616 / 33,141 = +70.83% while the other three components - investors' service fund, investors' protection fund and contribution to SEBI - grew (5,386+279+2,688) / (5,068+268+2,569) = +5.67%. The fast component tracked notional turnover 1,87,15,375 / 1,10,66,674 = +69.12% to within 1.02%, while revenue tracked premium turnover to within 1.83%. Two components of one note, moving on two different exogenous bases. Peer context: MCX 0.75%, CDSL 0.79%, IEX 0.09% of revenue.
S4 CONNECTS: The regulatory-contribution line in the P&L; the MD&A turnover disclosures that supply both bases; the concall in which management names the mechanism and states it is unpredictable; and the industry structure in which SEBI, not BSE, sets both the rate and the base.
DOMAINS: IncomeStatement, Notes, MgmtCommentary, Industry
DISCONFIRM: Sought and found, in three places. First, BSE's total regulatory contribution as a share of revenue actually fell in FY2026, from 41,046/2,95,734 = 13.88% to 64,969/4,83,395 = 13.44%, because the three near-fixed components were diluted by revenue growth - the burden rose only on the SEBI-fee component. Second, NSE's line is labelled simply "Regulatory fees" and its composition is not broken out, so it may not be a pure turnover fee; that would narrow the 2.44x gap and the number is an upper bound on the differential. Third, the direction was favourable in FY2026: because premium outgrew notional by 48.33 percentage points, the levy grew slower than revenue and expanded margin. The finding is about exposure, not about a realised drag.
S5 MEANS: BSE's operating margin is the residual of two exogenous ratios rather than a pricing or efficiency outcome, and it starts from a structurally worse levy-to-revenue position than the only comparable exchange in its own market.
BASE-RATE: This has already cost money at this company, and RF-019 sizes the realised loss precisely: SEBI's 26-Apr-2024 re-basing of the fee to notional option value, retrospective to FY2007 with 15% interest, put Rs 22,421 lakh through FY2024 and FY2025 - 21.8% of FY2024 PAT - for activity conducted years earlier under a different reading of the rule. The ongoing cost is the same order: BSE's total regulatory contribution rose Rs 236.90 cr to Rs 410.46 cr to Rs 649.69 cr across FY2024 to FY2026, a rise of 649.69 / 236.90 = 2.74x in two years, and at Rs 649.69 cr against PAT of Rs 2,496.98 cr it is 26.02% of PAT. In the wider system NSE carries the same structure and its regulatory fees fell 796.35 / 962.64 = -17.27% in a year its revenue fell 3.15%, showing the levy moves independently of revenue in both directions.
S6 IMPLICATION: The base and bear driver assumptions for BSE must model premium turnover and notional turnover as two separate exogenous series rather than one, because a fall in the premium-to-notional ratio compresses margin with no offsetting revenue movement; the monitorable is the ratio itself, disclosed each year in the MD&A secondary-market section, with the next check at the FY2027 annual report; the thesis-breaker is SEBI changing the fee base or the rate, which is entirely within the regulator's discretion and outside the company's.
SEVERITY: High

### FINDING: FY2026's 10-point margin expansion is a market-structure ratio, and the peer set is what proves it
S1 WHAT: BSE's operating margin before the Core SGF charge rose from 54.25% to 64.31%, a gain of 10.06 percentage points, in a year when its revenue base grew 48.33 percentage points faster than its regulatory-levy base purely because option premium rose relative to notional.
S2 WHY: The premium-to-notional ratio rose from 0.081126% to 0.10432%, up 28.59%. That ratio is implied volatility and moneyness in the Sensex option book - a property of how the market priced options, not of anything BSE did. It expanded the revenue base without expanding the levy base, and management states the relationship cannot be forecast.
S3 EVIDENCE: Margin 3,31,068 / 5,14,810 = 64.31% against 1,75,568 / 3,23,631 = 54.25% [AR FY26, Consolidated P&L, PDF p164/pr153]. Bases: premium turnover 19,523 / 8,978 = +117.45%, notional 1,87,15,375 / 1,10,66,674 = +69.12%, ratio 0.0010432 / 0.00081126 = +28.59% [AR FY26, MD&A, PDF p59/pr48]. Counter-proportion inside the same revenue line: equity derivatives +121.43% while equity cash fell 18%, so the aggregate's growth is one product, not trading activity generally [AR FY26, MD&A, PDF p75/pr64]. Peer counter-proportion, which is what identifies the exposure as specific rather than sectoral: IEX's levy base and revenue base are the same physical quantity, and its CERC fee fell 55.50 / 58.50 = -5.13% while volume rose 17%; CDSL's fee and revenue are both slab-based; MCX's SEBI fee is 0.75% of revenue, too small to move margin; NSE shares the structure but earns 2.44x more revenue per rupee of levy, so the same ratio move shifts its margin far less.
S4 CONNECTS: The P&L margin; the MD&A turnover series that supplies both bases; the concall in which management states the correlation is not predictable; and the industry fact that the October 2024 SEBI derivative measures redistributed volume between the two exchanges, which is why BSE grew 63.46% in the same year NSE's revenue fell 3.15%.
DOMAINS: IncomeStatement, MgmtCommentary, Industry, Notes
DISCONFIRM: Sought, and the strongest candidate has since been falsified by another wave, which is recorded rather than quietly dropped. The obvious counter-argument is that cost discipline, not the ratio, produced the margin - total expenses grew only 1,83,742 / 1,48,063 = +24.10% against revenue +63.46%, and clearing and settlement expense fell 28,035 / 34,805 = -19.45%. RF-025 shows that second limb is not cost discipline at all: the same expense fell only 4.6% on a standalone basis, and 81.2% of the consolidated fall - 5,496 of 6,770 - is the ICCL intra-group charge rising 77.3% and eliminating on consolidation. The underlying cost went up. What genuinely survives as disconfirmation is the first limb, operating leverage on a largely fixed cost base, which is the overlay's expected shape for an exchange - and against even that, BSE's cost-to-revenue of 38.01% remains above NSE's 27.52% excluding NSE's settlement provision, so BSE is not the low-cost operator in the set.
S5 MEANS: The FY2026 margin is a high-water mark produced by a ratio that has no floor and no anchor, so the year is not evidence of a step-change in earning power and should not be treated as a new base level.
BASE-RATE: The ratio has already moved sharply against BSE in the recent past by management's own account: the MD describes a prior state "where that ratio used to be very, very small because most of the volumes were mainly only on the expiry day", under the earlier Friday-expiry regime. In the system, NSE demonstrates the realised loss case directly - options transaction-charge revenue fell 9,997.57 / 10,194.03 = -1.93% and futures fell 14.31% in FY2026 after a regulatory change, so activity-driven exchange revenue at an Indian equity exchange has fallen within the last twelve months.
S6 IMPLICATION: The durability of the FY2026 earnings level depends on a ratio that is neither disclosed as a KPI nor forecast by management, so a base case built on FY2026 margin persisting is a bet on option-market microstructure rather than on the franchise; the monitorable is the premium-to-notional ratio computed from the MD&A secondary-market disclosure each year, next check at the FY2027 annual report; the thesis-breaker is the ratio reverting toward the FY2025 level while notional turnover holds, which would compress margin without any revenue signal.
SEVERITY: High

### FINDING: BSE's own-account cash is recoverable only by reconstructing three notes, and the reconstruction halves cash conversion while the competitor publishes the split directly
S1 WHAT: W1_ledger has now rebuilt BSE's own-account cash flow from Notes 11, 12 and 16, and three-year cumulative own-account CFO to PAT is 0.942 against a headline 1.393 - but no single statement, note or segment in BSE's annual report presents that number, whereas NSE, running the structurally identical exchange-plus-clearing group, publishes a Clearing Services segment with its own revenue, result, assets, liabilities, capital expenditure and depreciation.
S2 WHY: Both groups consolidate a clearing corporation, so both commingle member money with group cash identically. NSE resolved it by treating Clearing Services as a reportable segment under Ind AS 108; BSE asserts the group "operates only in one Operating Segment i.e. Facilitating Trading in Securities and other related ancillary services". BSE does supply the raw material - its notes label every liability and bank balance Owned, Earmarked or Clearing-and-settlement - but it leaves the assembly entirely to the reader, and the reader has to know to do it.
S3 EVIDENCE: Own-account CFO 75,840 / 68,008 / 2,86,117 against reported 2,84,203 / 41,015 / 3,10,368 for FY2024 to FY2026, cumulative 4,29,965 of 6,35,586 = 67.65%, so Rs 2,056.21 cr of three-year reported CFO was member float (RF-005 as resolved by W1_ledger). Headline overstates own-account conversion by 1.393 / 0.942 = 47.9%. Counter-proportion, and it is the sharper half: the contamination is not merely large, it is unstable - FY2024 own-account CFO was 75,840 / 2,84,203 = 26.69% of reported, so 73.31% was float, while FY2026 was 2,86,117 / 3,10,368 = 92.19%, so only 7.81% was float. A bias that moves 65 percentage points in two years destroys the trend, not just the level. Balance-sheet counter-proportion: within Note 16 the owned portion is 24,992 against clearing-and-settlement 3,55,423 and earmarked 26,004, so 87.45% of that note is not the company's money = 3,55,423 / 4,06,419 [AR FY26, Note 16, PDF p207/pr196]. Peer position: NSE Clearing Services segment assets Rs 46,729.63 cr against liabilities Rs 46,811.09 cr, Core SGF of Rs 13,026.78 cr identified inside segment assets, Trading Services assets Rs 8,105.53 cr shown separately [NSE AR FY26, Note 33(d) and 33(e), PDF p164]; CDSL also reports three segments with revenue, result, assets and liabilities [CDSL AR FY26, Note 35, PDF p339-340]; BSE reports one segment and nothing beneath it [AR FY26, Note 39, PDF p~229].
S4 CONNECTS: The balance sheet, where the float sits; the cash flow statement, where the unassembled version overstates conversion; the notes, which carry the labels that make reconstruction possible; the business fact that BSE consolidates a clearing corporation; and the peer disclosure that shows the same standard permits presenting it directly.
DOMAINS: BalanceSheet, CashFlow, Notes, Business, Industry
DISCONFIRM: Sought and found, and it forces this finding to be narrower than RF-005 originally was. RF-005's claim that cash conversion "cannot be measured" is withdrawn - it can be, and W1_ledger has measured it. Notes 11 and 12 label every bank line Owned, Earmarked-others, Earmarked-SGF or Earmarked-IPF, own-account liquid funds tie exactly to the balance sheet in all three years, and Note 16 gives a three-way liability split. That is better note-level disclosure than a bare aggregate and better than this finding would imply if read carelessly. IEX and MCX also report a single segment, so single-segment reporting is not unique to BSE. What survives all of that is the specific comparison to the one peer with the identical structure, which segments anyway.
S5 MEANS: BSE's cash disclosure is adequate at note level and absent at statement level, so a reader who takes the cash flow statement at face value overstates own-account conversion by roughly half and would conclude the business converts earnings to cash when on its own money it has not.
BASE-RATE: This has already produced a wrong number inside this very run, before any external event: the 1.264 ten-year headline conversion previously carried on the record corrects arithmetically to 1.269 and substantively to 0.942 on the own-account basis for the three-year window, a 47.9% overstatement that survived until someone reconstructed three notes by hand. In the wider system, clearing float is where market-infrastructure losses actually occur - the Core SGF exists because member default has cost money in Indian markets, and BSE's own Note 41 records penalties collected from members and transferred into the fund - so the pool being misread is the one that matters.
S6 IMPLICATION: The earnings-quality gate should run on own-account CFO to PAT of 0.942 rather than the headline 1.393, which moves the conversion test from comfortably above one to below it and materially weakens any cash-backed reading of the FY2026 result; the monitorable is whether the FY2027 annual report adds a clearing segment or an own-account cash reconciliation, removing the need for reconstruction; the thesis-breaker is a year in which own-account CFO diverges from PAT for a reason the note labels cannot explain, since that would be an accrual problem rather than a float artefact.
SEVERITY: High

### FINDING: BSE is the only MII in the set carrying a permanently restricted equity block, and it understates rather than overstates return on shareholders' capital
S1 WHAT: Rs 767.18 cr of BSE's Rs 6,673.01 cr attributable equity - 11.50% - is permanently non-distributable, chiefly a Rs 661.79 cr Capital reserve created under the BSE (Corporatisation and Demutualisation) Scheme, 2005 which the note states "shall not be used for purposes other than the operations of the Exchange"; CDSL carries nil restricted reserves and IEX 1.44%.
S2 WHY: BSE is the only one of the five that was ever a mutual members' association. Founded in 1875 and demutualised in 2005, it converted members' contributions, forfeited application money, technology reserve, the exchange building, a library endowment and a charity account into one ring-fenced Capital reserve. NSE, MCX, CDSL and IEX were all incorporated as companies and have no equivalent legacy. This is a fact about corporate history, not about capital allocation.
S3 EVIDENCE: Restricted 661.79 + 105.30 + 0.09 = Rs 767.18 cr; 767.18 / 6,673.01 = 11.50% [AR FY26, Note 15 and 15.2, PDF p205/pr194]. ROE on average attributable equity 2,496.98 / ((6,673.01 + 4,423.73) / 2) = 2,496.98 / 5,548.37 = 45.00%; on average equity excluding restricted reserves 2,496.98 / ((5,905.83 + 3,656.56) / 2) = 2,496.98 / 4,781.20 = 52.23%, a difference of 7.23 percentage points. Counter-proportion: CDSL 0.00% restricted of Rs 1,959.78 cr equity with ROE 24.52% on either basis [CDSL AR FY26, Note 13, PDF p318]; IEX 19.62 / 1,364.56 = 1.44% restricted, ROE 39.42% moving to 40.03% [IEX AR FY26, SOCIE, PDF p243/pr239]. Second counter-proportion, on the regulatory-capital side: Core SGF per rupee of revenue is BSE Rs 0.258 (1,246.83 / 4,833.95) against NSE Rs 0.788 (13,079.15 / 16,601.31) and MCX Rs 0.594 (1,367.29 / 2,302.00), so BSE is the least regulatory-capital-intensive of the three clearing groups even as it is the most equity-restricted.
S4 CONNECTS: The balance sheet and the other-equity note; the 2005 Demutualisation Scheme, which is a governance instrument rather than an accounting one; the business history that distinguishes BSE from every comparator; and the industry framework under which SECC Regulations set net-worth and Core SGF requirements.
DISCONFIRM: Sought and found, and it inverts the overlay's stated direction. The sector overlay warns that ROE on total equity overstates return on shareholders' capital where restricted funds sit inside equity; at BSE the restricted funds sit in the denominator, so total-equity ROE understates the return on distributable capital by 7.23 points rather than overstating it. Further disconfirmation: BSE's presentation of Core SGF as a separate category between equity and liabilities is the correct treatment and means total equity is already clean of the largest restricted pool, so the overlay's principal concern does not arise here at all. The comparison is also incomplete - NSE folds its capital, general and investor-compensation reserves into retained earnings and MCX's equity note was not read, so this ranking is established against CDSL and IEX only.
DOMAINS: BalanceSheet, Notes, Governance, Business
S5 MEANS: BSE's stated return on equity is conservative rather than flattered, but roughly one rupee in nine of its equity is permanently outside shareholders' reach for reasons fixed in 2005 and not reversible by any management decision.
BASE-RATE: No loss has ever arisen from this reserve and none can - it is a presentational ring-fence, not an exposure. The relevant base rate is the opposite one: across ten years the reserve has never been drawn on, never impaired and never reclassified, and BSE's payout has been funded entirely from retained earnings, which stood at Rs 5,406.88 cr at 31 March 2026 against a proposed dividend of Rs 411.98 cr.
S6 IMPLICATION: Any return-on-capital comparison against CDSL, IEX or a non-demutualised exchange must state which equity base it uses, because the 7.23-point difference is larger than the gap between several of the peers themselves; the monitorable is whether the Capital reserve is ever reclassified or drawn, which would signal a change in how the 2005 Scheme is being interpreted; there is no thesis-breaker here, since the reserve is inert.
SEVERITY: Medium

### FINDING: BSE has the strongest board-independence structure in the peer set and the smallest penalty exposure, while being the promoter and co-auditee of a peer it consolidates
S1 WHAT: Six of BSE's eight directors are Public Interest Directors and the Chairperson must be one, against CDSL's six of eleven and IEX's zero, and BSE's FY2026 SEBI penalty of Rs 0.25 cr is 0.010% of PAT against NSE's Rs 1,391.21 cr settlement provision at 13.5% of its own PAT - yet BSE is simultaneously CDSL's promoter at 15.00%, a board nominator at CDSL, an equity-method consolidator of CDSL's profit, and a client of the same audit firm.
S2 WHY: The independence is structural rather than chosen: with no promoter, the SECC Regulations substitute a regulator-approved director quota and a mandated chair-CEO separation, and BSE sits at the top of that quota. The entanglement is equally structural: BSE was the founding promoter of CDSL in 1999 and SEBI's depository ownership rules capped rather than eliminated that stake, leaving BSE at exactly 15.00%.
S3 EVIDENCE: BSE 6 of 8 PIDs = 75%, Chairperson a PID, no director holds equity [AR FY26, CG Report, PDF p78, p80]. CDSL 54.54% PID/ID of eleven [CDSL AR FY26, Board composition, PDF p48]. IEX four of eight ordinary Independent Directors, no PID concept, and Chairman and Managing Director are the same person [IEX AR FY26, Board's Report, PDF p75]. Counter-proportion on penalties, which is the disproportion that matters: BSE 0.25 / 2,496.98 = 0.010% of PAT [AR FY26, CG Report, PDF p95/pr84]; NSE 1,391.21 / 10,302.06 = 13.50% of PAT [NSE AR FY26, Note 30.2, PDF p166]; CDSL 3.00 / 456.13 = 0.66% [CDSL AR FY26, BRSR, PDF p185]; MCX 1.25 / 1,331.55 = 0.09% [MCX AR FY26, BRSR, PDF p97]; IEX nil across three years [IEX AR FY26, CG Report, PDF p121/pr117]. Auditor tenure counter-proportion: BSE's S.R. Batliboi term runs FY2018 to FY2027, the ten-year statutory maximum, with no successor process disclosed, while NSE's incumbent term ends at the 2026 AGM and its board has already approved Walker Chandiok and Co LLP as successor - the peer facing the same cliff has published its landing and BSE has not.
S4 CONNECTS: The corporate governance report and board composition; the related-party and associate notes that carry the CDSL holding and the Rs 65.42 cr share of associate profit; the auditor signature pages that show one firm signing both sets of accounts; and the industry framework in which SECC and D&P Regulations, not shareholders, set the board.
DOMAINS: Governance, Notes, Industry, Business
DISCONFIRM: Sought and found on both limbs. Against the independence claim, RF-001 records that the SEBI-mandated Executive Directors for all three MII verticals were still unappointed at the FY2026 corporate governance report date and that the Chief Regulatory Officer reports to the MD and CEO - so a high PID count coexists with an unfilled regulatory-function structure, and the quota measures composition rather than effectiveness. Against the CDSL-entanglement concern, everything is disclosed: the 15.00% holding, the promoter designation, the sitting fees routed to BSE as nominating institution, and the auditor identity all appear in both companies' reports, and CDSL contradicts BSE on the Ind AS 115 timing split, which is evidence that the shared auditor is not producing shared presentation.
S5 MEANS: BSE's governance architecture is the strongest available substitute for the promoter discipline it structurally lacks, but the CDSL relationship means one of the four peers cannot serve as independent corroboration of BSE's accounting standard and must be read as a related party first.
BASE-RATE: Regulatory action has cost money in this sector repeatedly and recently - NSE Rs 643.05 cr paid in FY2025 and Rs 40.35 cr in FY2026 with Rs 1,391.21 cr provided, CDSL Rs 3.00 cr, MCX Rs 1.25 cr - so the base rate for Indian MII supervision converting into cash is high. BSE's own realised cost across the three-year window is Rs 8.33 cr including the ICCL order, which is 0.33% of FY2026 PAT and the lowest in the set.
S6 IMPLICATION: The governance structure supports rather than qualifies the durability of the earnings stream, and BSE's supervision record is the best of the five on money, which is disconfirming evidence against treating regulatory risk as the primary hazard here; the monitorables are the three MII Executive Director appointments and the auditor succession process, both due before the 22nd AGM in 2027; the thesis-breaker is a SEBI order of NSE-settlement scale, since the peer set establishes that an order of that size is possible at an Indian exchange within a single year.
SEVERITY: Medium

---

## 8. Handoffs

- **W3_revenue** — the activity-times-realisation decomposition in §3.3 is the input; note that its
  numerator is unaudited. NSE's audited Options line is the external check on BSE's MD&A derivatives
  number, and §3.2 gives the share computation BSE never publishes: BSE's share of the two exchanges'
  equity-derivative transaction-charge revenue went `1,415.54 ÷ 13,336.83 = 10.61%` in FY2025 to
  `3,134.37 ÷ 14,612.04 = 21.45%` in FY2026, **+10.84 percentage points**. Definitional caveat: BSE's
  numerator is standalone unaudited equity derivatives; NSE's is audited Options plus Futures.
- **W3_balancesheet** — Note 16's Owned / Earmarked / Clearing-and-settlement split is the starting
  point, and NSE's Note 33(d)/(e) is the disclosure template that would complete it.
- **W3_cost** — the regulatory-levy comparison in §4.2 supersedes any BSE-only reading of RF-015; the
  levy is not merely presented inconsistently across years, it is structurally 2.44× the competitor's.
- **W3_group_rpt** — the CDSL relationship in §1.3 is the largest related-party structure in the group
  and combines promoter status, board nomination, equity-method consolidation and a shared auditor.
- **W4_cash** — RF-005 is **resolved** by W1_ledger (own-account CFO/PAT 0.942 cumulative against a
  headline 1.393). What remains for this wave to add is that the resolution required a three-note manual
  reconstruction, and that NSE publishes the segment balance sheet that would have supplied it directly.
  Use 0.942, not 1.393, and not 1.264.
- **W4_capalloc** — restricted equity is Rs 767.18 cr, 11.50%; exclude before judging deployment.
- **W5** — the FY2026 margin is decomposed in §4.3 and rests on an exogenous ratio, which bounds every
  forward statement built on it.

## 9. Gap register additions

| Gap | What is missing | Peers disclose? | Question generated |
|---|---|---|---|
| **Ind AS 115 timing disaggregation** | Point-in-time versus over-time revenue split | **Yes — 4 of 4** | Why does BSE not publish the timing disaggregation that NSE, MCX, CDSL and IEX all publish? |
| **Transaction-charge product split, audited** | Equity derivatives / equity cash / StAR MF inside the audited note | **Yes — NSE and IEX** | Will the FY2027 Note 22 carry the split, and will the MD&A figures be reconciled to an audited total? |
| **Contracted-price reconciliation and contract balances** | Contract price to revenue bridge; contract asset and liability | **Yes — NSE, MCX, IEX** | Are there no contract liabilities at BSE, given listing fees are billed annually in advance? |
| **Segment revenue, result, assets and liabilities** | Any split below the group | **Yes — NSE (3), CDSL (3)** | On what basis is a group containing an exchange, a clearing corporation, an IFSC exchange and a technology subsidiary a single operating segment? |
| **Revenue concentration by customer** | Any statement on revenue from a single member | **Yes — NSE, IEX, CDSL** | What share of transaction-charge revenue comes from the largest ten trading members? |
| **NSE and MCX restricted-equity composition** | Component detail inside other equity | not read in this pass | → *NSE AR FY26 Note 13(b); MCX AR FY26 Other Equity note* |

## 10. Corrections recorded, not substituted (doctrine §10)

0. **Concurrency note.** `records/red_flags.md` was updated by W1_ledger, W2_industry and W2_business
   while this wave was running. This document was reconciled against the register **as at the end of
   this wave** and does not silently overwrite any of them. Where a newer artifact falsified something
   written here — RF-025 against the clearing-cost limb of Finding 3, RF-005's resolution against the
   original framing of Finding 4 — the older position is shown against what replaced it, per §10.
1. **RF-003 is narrowed, by two waves independently.** BSE does publish an audited component revenue
   note. This wave and W1_ledger reached that correction separately and agree; the residual disagreement
   is a component count of eleven versus twelve, left open in §4.1. Both positions stand.
1a. **RF-013 is now settled, which was this wave's explicit assignment.** The answer is: NSE discloses
   three segments with revenue, result, assets, liabilities, capex and depreciation, and CDSL discloses
   three with revenue, result, assets and liabilities; MCX and IEX disclose one, as BSE does. The peer
   grading is therefore **split, not unanimous** — which is a weaker grade than §4.1's timing-split
   finding and is stated as such rather than overstated.
2. **`records/trend_10y.csv` row `core_sgf_contribution` is mis-mapped.** The values 60,548 / 1,75,568 /
   3,31,068 for FY2024–FY2026 are **"Profit before contribution to core settlement guarantee fund"**,
   not the contribution. The actual contribution is **7,696 (FY2026) and 9,000 (FY2025)**
   `[AR FY26, Consolidated P&L, PDF p164/pr153]`. Every ratio in this document uses the corrected
   figure. **The CSV is not edited here** — this wave writes one file — and the correction is routed to
   whoever owns the record layer.
3. **MCX availability.** The earlier record that the NSE equities API returns zero rows for MCX stands
   and is correct about that channel. It is superseded as a statement about MCX data, which is fully
   available via `api.bseindia.com/BseIndiaAPI/api/AnnualReport_New/w?scripcode=534091`.
