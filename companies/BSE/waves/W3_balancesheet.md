# W3 — Balance sheet: BSE Limited (consolidated), FY2024–FY2026

**Agent:** W3_balancesheet. **Date:** 2026-09-08. **Basis:** consolidated unless stated. Unit `₹ lakh`
throughout, matching the annual report's own `(₹ in Lakhs)`. Printed-page offsets from
`W1_docmap.md` §0.1 (FY2026 +11, FY2025 +11, FY2024 +6).

**What this file is for.** Doctrine §2a: the balance sheet is where accrual and cash disagree, and at a
market-infrastructure institution it is also where **other people's money** sits. Overlay §2 says most of
this balance sheet is not the company's. This file classifies every material balance into own /
restricted / members', reconciles every material line opening-to-closing, and states the return on the
capital that is actually the shareholders'.

**Prior work used, not rebuilt.** `records/balance_cash_10y.csv` and `records/trend_10y.csv` (as
corrected by W1_ledger), `waves/W1_ledger.md` §2–§4 (the float separation and seven chain records),
`records/red_flags.md`. **Nothing here overwrites an earlier position**; where I disagree with an earlier
artifact the disagreement is stated with both sides (doctrine §10). Two such disagreements are recorded
in §7.

---

## 1. The owned / restricted / member-money classification (overlay §2)

Every rupee on the funding side of the FY2026 consolidated balance sheet is placed in exactly one of four
classes. The classes tie to the reported total in all three years with **zero residual** — that tie-out is
the control, and it is what makes the percentages below usable rather than asserted.

**Class definitions**

| Class | What it is | Where the company says so |
|---|---|---|
| **OWN** | Total equity plus liabilities arising from the group's own operations — trade payables, employee accruals, tax, provisions, income received in advance, payables for fixed assets | residual of the other three |
| **RESTRICTED (regulatory)** | Core Settlement Guarantee Fund, Note 16 bucket (B) *Earmarked*, the Investors' Services Fund, the IPF contribution payable | `[AR FY26, Note 16, PDF p206/pr195]`, `[AR FY26, Note 19, PDF p208-209/pr197-198]`, `[AR FY26, Notes 41 & 42, PDF p231-232/pr220-221]` |
| **MEMBERS' / SETTLEMENT** | Note 16 bucket (C) *Clearing and settlement*, **plus** the trading-member and other member deposits sitting inside bucket (A) *Owned* | `[AR FY26, Note 16, PDF p206/pr195]` |
| **STATUTORY (held for the government)** | Statutory remittances inside Note 19 — ₹51,478 of it is Securities Transaction Tax collected for the tax authorities | `[AR FY26, Note 19, PDF p208/pr197]` and `[AR FY26, MD&A, PDF p77/pr66]` |

**The table**

| ₹ lakh | FY2024 | FY2025 | FY2026 |
|---|---|---|---|
| Total equity | 3,45,466 | 4,57,570 | 6,79,550 |
| Trade payables | 19,055 | 11,396 | 13,087 |
| Note 16 (A) excluding member deposits | 4,061 | 6,910 | 7,999 |
| Note 16 non-current (employee accruals, lease) | 1,071 | 1,060 | 1,039 |
| Provisions (current + non-current) | 19,132 | 2,806 | 4,282 |
| Current tax liabilities | 1,496 | 8,447 | 20,109 |
| Note 19 own (income in advance, customer advances, other) | 8,090 | 11,171 | 11,687 |
| Liabilities classified as held for sale | – | 1,559 | – |
| **OWN — total** | **3,98,371** | **5,00,919** | **7,37,753** |
| Core SGF (ICCL 1,23,264 + India ICC 1,419) | 95,496 | 1,13,260 | 1,24,683 |
| Note 16 (B) Earmarked | 41,386 | 35,024 | 26,004 |
| Investors' Services Fund (inside Note 19) | 6,632 | 7,523 | 8,926 |
| IPF contribution payable | 39 | 43 | 52 |
| **RESTRICTED — total** | **1,43,553** | **1,55,850** | **1,59,665** |
| Note 16 (C) Clearing and settlement | 3,58,165 | 3,31,172 | 3,55,423 |
| Member deposits inside Note 16 (A) | 16,999 | 16,381 | 16,993 |
| **MEMBERS' — total** | **3,75,164** | **3,47,553** | **3,72,416** |
| **STATUTORY — statutory remittances** | **27,935** | **29,843** | **74,780** |
| **Total equity and liabilities** | **9,45,023** | **10,34,165** | **13,44,614** |

`DERIVED, exact:` FY2026 `7,37,753 + 1,59,665 + 3,72,416 + 74,780 = 13,44,614`; FY2025
`5,00,919 + 1,55,850 + 3,47,553 + 29,843 = 10,34,165`; FY2024
`3,98,371 + 1,43,553 + 3,75,164 + 27,935 = 9,45,023`. All three close to the reported total exactly.

**Shares of the funding side**

| | FY2024 | FY2025 | FY2026 |
|---|---|---|---|
| OWN | 42.2% | 48.4% | **54.9%** |
| RESTRICTED | 15.2% | 15.1% | 11.9% |
| MEMBERS' | 39.7% | 33.6% | 27.7% |
| STATUTORY | 3.0% | 2.9% | 5.6% |
| **NOT the company's money** | **57.8%** | **51.6%** | **45.1%** |

**The conclusion this table supports.** BSE crossed from a balance sheet that was majority other people's
money to one that is majority its own **inside two years**, and it did so without changing anything about
the float: members' money is ₹3,72,416 at FY2026 against ₹3,75,164 at FY2024, essentially flat. The
entire shift is the numerator — equity nearly doubled. **Any ratio computed on total assets for this
company measures the members, not the business**, and the FY2024 denominator was measuring them 58% of
the time. Return on assets is not a usable metric here in any year.

**The asset side ties to the same split.** Notes 11 and 12 label every bank line *Owned*,
*Earmarked – others*, *Earmarked – SGF* or *Earmarked – IPF*, and Note 9 labels every investment *Owned*
or *Earmarked* `[AR FY26, Notes 9, 11 & 12, PDF p190-202/pr179-191]`.

| ₹ lakh | FY2024 | FY2025 | FY2026 |
|---|---|---|---|
| Own-account liquid funds (cash, deposits, accrued interest) | 1,41,528 | 1,67,486 | 3,08,596 |
| Own-account investments (MFs, ETFs, bonds, SDLs, G-Sec) | 1,74,780 | 2,03,588 | 3,05,686 |
| **Own-account financial assets** | **3,16,308** | **3,71,074** | **6,14,282** |
| Earmarked liquid funds | 4,89,249 | 4,68,109 | 5,00,657 |
| Earmarked investments | 18,166 | 30,900 | 24,357 |
| **Earmarked financial assets** | **5,07,415** | **4,99,009** | **5,25,014** |

`DERIVED:` FY2026 owned investments `4,092 + 69,761 + 2,21,094 + 9,528 − 1,398 + 2,609 = 3,05,686`;
earmarked `21,689 + 2,668 = 24,357`; the two sum to Note 9's `95,542 + 2,34,501 = 3,30,043`
`[AR FY26, Note 9, PDF p191-192/pr180-181]`.

**Two-sided test.** Earmarked financial assets 5,25,014 against the liabilities they are earmarked
against — Note 16 (B) 26,004 + (C) 3,55,423 + Core SGF 1,24,683 + ISF 8,926 + IPF 52 = 5,15,088 —
leaves **excess assets of 9,926, i.e. 1.9%** `DERIVED: 5,25,014 − 5,15,088 = 9,926`. The cover is real
and it is disclosed on both sides. **The 16,993 of member deposits inside bucket (A) has no earmarked
asset behind it** — Notes 16.2 and 16.3 earmark assets against buckets (B) and the unpaid-dividend line
only. That is the finding in §5, F6.

**Own-account financial assets are 90.4% of total equity** (`6,14,282 / 6,79,550 = 90.4%`, against
`3,71,074 / 4,57,570 = 81.1%` at FY2025). Shareholders' capital at this company is a securities
portfolio with an exchange attached to it: the operating asset base — PPE, CWIP, intangibles, IAUD — is
68,056, i.e. **10.0% of equity**.

---

## 2. Distributable equity, and ROE on both bases (overlay §2, mandatory equity rule)

**The overlay's premise needs one factual correction before it can be applied.** Overlay §2 says ROE on
total equity "overstates the return on shareholders' capital to the extent restricted funds sit inside
it." **At BSE the Core SGF does not sit inside equity.** The consolidated balance sheet presents it as
its own caption, line 4, *between* "3 Equity" and "Liabilities" — 1,24,683 at FY2026 — and total equity
of 6,79,550 excludes it `[AR FY26, Consolidated Balance Sheet, PDF p163/pr152]`. Policy 2.3.12 confirms
the treatment: contributions are expensed and never reversed, and fund income and member penalties are
credited straight to the fund, never through profit or loss `[AR FY26, Note 2.3.12, PDF p178/pr167]`.
So the largest restricted pool is already outside the equity denominator.

**What *is* locked inside equity is different, and it runs the other way.**

| Restriction inside consolidated equity, FY2026 | ₹ lakh | Source of the restriction |
|---|---|---|
| Non-controlling interest | 12,249 | not the parent shareholders' at all `[AR FY26, Note 44, PDF p236/pr225]` |
| Capital reserve | 66,179 | Demutualisation Scheme 2005 — "shall not be used for purposes other than the operations of the Exchange" `[AR FY26, Note 15.2, PDF p204/pr193]` |
| Capital reserve on business combination | 10,530 | a consolidation reserve, not a realised profit of the parent `[AR FY26, Note 15, PDF p204/pr193]` |
| Foreign currency translation reserve | 4,437 | unrealised; recycles on disposal `[AR FY26, Note 15.5, PDF p205/pr194]` |
| LES reserve | 9 | "will not form part of net worth in accordance with the IFSCA circular" `[AR FY26, Note 15.8, PDF p205/pr194]` |
| General reserve earmarked for abeyance bonus shares | 81 | `[AR FY26, Note 15.1, PDF p204/pr193]` |

`DERIVED: 6,79,550 − 12,249 − 66,179 − 10,530 − 4,437 − 9 − 81 = 5,86,065` distributable equity at
FY2026; `4,42,373 − 66,179 − 10,530 − 4,137 − 8 − 38 = 3,61,481` at FY2025;
`3,30,229 − 66,179 − 10,530 − 3,436 − 9 = 2,50,075` at FY2024.

**Note 15.4 is the legal control:** "the amount that can be distributed by the Parent Company as dividends
to its equity shareholders is determined based on the balance in this reserve" — retained earnings, **at
the parent**. Standalone retained earnings are 4,55,828 at FY2026 `[AR FY26, Standalone Note 15, PDF
p280/pr269]`, i.e. **67.1% of consolidated total equity** (`4,55,828 / 6,79,550`). The consolidated
distributable figure of 5,86,065 is the economic claim; 4,55,828 is the amount the board could legally
declare out of today.

**The other direction — income earned on money that is not the company's.** Revenue from operations
contains a named line, *Treasury income from clearing and settlement funds*, **17,142** at FY2026 against
**21,778** at FY2025 `[AR FY26, Note 22, PDF p211/pr200]`. That is income on members' float, booked
inside the top line and flowing to shareholders. At the FY2026 effective tax rate
(`82,384 / 3,29,914 = 24.97%`) it is `17,142 × 0.7503 = 12,861` of PAT — **5.15% of PAT attributable**
(`12,861 / 2,49,698`), against `21,778 × 0.7534 = 16,406`, **12.37%**, in FY2025. Every other pool's
income is quarantined: Core SGF income goes to the fund (policy 2.3.12), Note 16.4 books income on
earmarked amounts as a liability (8,896 at FY2026), and ISF investment income of 671 is credited to the
fund inside Note 19.

**ROE on four bases**

| Basis | FY2025 | FY2026 |
|---|---|---|
| (a) PAT total / average **total equity** | 32.93% | **43.75%** |
| (b) PAT attributable / average **equity attributable to shareholders** | 34.32% | 45.00% |
| (c) PAT attributable / average **distributable equity** | 43.36% | **52.70%** |
| (d) PAT attributable **ex after-tax float income** / average distributable equity | 38.00% | **49.99%** |
| memo: management's published ROE (standalone, total equity) | 33.77% | 49.07% `[AR FY26, MD&A, PDF p77/pr66]` |

`DERIVED:` average total equity `(6,79,550 + 4,57,570) / 2 = 5,68,560`, `2,48,725 / 5,68,560 = 43.75%`;
average distributable `(5,86,065 + 3,61,481) / 2 = 4,73,773`, `2,49,698 / 4,73,773 = 52.70%`;
ex-float `(2,49,698 − 12,861) / 4,73,773 = 49.99%`.

**By how much does the headline mislead — the quantified answer to overlay §2.** Two errors of opposite
sign sit inside the 43.75%:

- Non-distributable reserves inside the denominator **understate** the return on the capital
  shareholders can claim by **8.95 percentage points** (`52.70 − 43.75`). This is the **opposite sign**
  to the overlay's prediction, because the overlay assumed the Core SGF sat inside equity and it does not.
- Income on members' float inside the numerator **overstates** it by **2.71 percentage points**
  (`52.70 − 49.99`).
- **Net: the reported 43.75% understates the true return on distributable shareholders' capital by 6.24
  percentage points** (`49.99 − 43.75`). The direction is up, not down. In FY2025 the same computation
  gives `38.00 − 32.93 = 5.07pp`, also up.

The overlay's rule stands as a rule — *state which basis is used* — but its stated direction is falsified
here, and the falsification is a fact about BSE's presentation, not about the overlay's logic.

---

## 3. Capital intensity — regulatory, not physical (overlay §5)

| Per ₹1 of revenue from operations | FY2024 | FY2025 | FY2026 |
|---|---|---|---|
| **Core SGF** | ₹0.687 | ₹0.383 | **₹0.258** |
| Physical (PPE + CWIP + intangibles + IAUD) | ₹0.188 | ₹0.107 | ₹0.141 |
| Regulatory ÷ physical | 3.65× | 3.59× | 1.83× |

`DERIVED:` FY2026 `1,24,683 / 4,83,395 = 0.258` and `(56,259 + 3,255 + 4,122 + 4,420) / 4,83,395 = 0.141`;
FY2024 `95,496 / 1,39,003 = 0.687` and `26,168 / 1,39,003 = 0.188`.

Adding the disclosed minimum net-worth floors — ₹100 crore for BSE Limited and ₹100 crore for ICCL under
SECC Regulation 14 `[AR FY26, Note 35, PDF p222/pr211]` — gives `(1,24,683 + 20,000) / 4,83,395 = ₹0.299`
per ₹1 of revenue. The three IFSC floors (USD 3m each for India ICC and India INX, USD 0.5m for India INX
Global Access, ₹1 crore for BSE Index Services) are stated in dollars and not converted by the company.

**The conclusion.** Regulatory capital per rupee of revenue **fell by 62% in two years** while revenue
rose 248% (`4,83,395 / 1,39,003`). That is a direct consequence of the Core SGF being a **stress-test
output, not a turnover function** — Regulation 31(2) of the IFSCA (MII) Regulations 2021 and SEBI's
Minimum Required Contribution methodology both size it off monthly stress-test values
`[AR FY26, Notes 41 & 42, PDF p231-232/pr220-221]`. The binding capital constraint on this business is
still regulatory rather than physical (1.83× at FY2026, 3.65× at FY2024), but **the gap is closing** —
and it is closing because FY2026 was the first year the company spent seriously on physical assets.
Management's own framing of why capital is retained is regulatory, not operating: *"a stronger balance
sheet of an exchange is very essential to showcase to the world that the clearing corporation is strong
enough"* `[Q4FY26 Concall 13May2026, MD & CEO]`.

---

## 4. Chain records

Format per `state/TEMPLATES.md`. Eight links, each in a declared state. `DERIVED` shows its arithmetic
inline; `NOT-DISCLOSED` names the settling document after `->`.

### CHAIN: Total equity | FY26
L1 REPORTED   TRACED | 6,79,550 against 4,57,570, +48.5% (6,79,550 − 4,57,570 = 2,21,980), of which equity attributable to shareholders 6,67,301 and non-controlling interest 12,249; equity share capital 8,158 and other equity 6,59,143 | [AR FY26, Consolidated Balance Sheet, PDF p163/pr152]
L2 COMPONENTS TRACED | capital reserve 66,179 + capital reserve on business combination 10,530 + securities premium 287 + general reserve 37,013 + retained earnings 5,40,688 + FCTR 4,437 + LES reserve 9 = 6,59,143, zero residual; share capital 8,158 = 40,78,84,077 shares of `2 | [AR FY26, Notes 14 and 15, PDF p203-205/pr192-194]
L3 DRIVER     DERIVED | the year's movement is 89.9% retained profit and 10.1% presentation: profit attributable 2,49,698 / 2,21,980 = 112.5% of the increase, dividends paid (31,585) = −14.2%, OCI +428 remeasurement and +1,935 FCTR, NCI issue +1,215, NCI loss (973), ownership-change transfer +4,529 from NCI to parent, transfer to Core SGF (129). The 2:1 bonus of 27,07,52,718 shares moved 5,414 from general reserve to share capital and changed nothing | [AR FY26, Statement of Changes in Equity, PDF p167-168/pr156-157]
L4 COUNTERPARTY TRACED | no promoter exists — a demutualised exchange. Only one shareholder above 5%: LIC at 2,27,29,500 shares, 5.57% (5.60% at FY2025). Non-controlling interests are the outside holders of India International Exchange (34.73%) and India International Clearing Corporation (39.47%) | [AR FY26, Note 14(e), PDF p204/pr193] and [AR FY26, Standalone Note 7, PDF p267/pr256]
L5 RECOGNITION TRACED | Note 15.2 restricts the capital reserve of 66,179 to "purposes other than the operations of the Exchange" under the Demutualisation Scheme 2005; Note 15.8 excludes the LES reserve from net worth per IFSCA circular F.No.286/IFSCA/PM(CMD-DMIIT)/2021/4; Note 15.4 makes distributable dividends a function of the PARENT's retained earnings, not the group's. Note 35 sets the regulatory floors: `100 crore minimum net worth for BSE Limited and for ICCL under SECC Regulation 14 | [AR FY26, Notes 15.2, 15.4, 15.8 and 35, PDF p204-205, p222/pr193-194, pr211]
L6 BALANCE-SHEET DERIVED | the roll-forward closes exactly on both halves. Attributable: 4,42,373 + 5,451 + 2,49,698 + 428 + 1,935 − 5,414 − 36 − 31,585 − 78 + 4,529 = 6,67,301. NCI: 15,197 + 1,215 − 973 + 193 + 1,188 − 51 − 4,529 + 9 = 12,249. Distributable equity 6,79,550 − 12,249 − 66,179 − 10,530 − 4,437 − 9 − 81 = 5,86,065, i.e. 86.2% of the reported total | [AR FY26, Statement of Changes in Equity, PDF p167-168/pr156-157]
L7 CASH       TRACED | only two lines of equity moved cash: dividends paid (31,585) in financing, and issue of shares by a subsidiary +1,215. The bonus issue, the abeyance allotment and the ownership-change transfer are all non-cash and appear nowhere in the cash flow. Own-account financial assets rose 3,71,074 to 6,14,282, +2,43,208, against the 2,21,980 equity increase | [AR FY26, Consolidated Cash Flow, PDF p165/pr154] and [AR FY26, Notes 9, 11 & 12, PDF p190-202/pr179-191]
L8 SUSTAIN    DERIVED | equity compounds only while payout stays low: dividend 31,585 against profit attributable 2,49,698 = 12.6% payout, and the proposed FY2026 dividend of `10 per share on 41,19,79,077 shares is 41,198, still 16.5%. The condition is that management continues to fund the capex cycle and the clearing corporation's balance-sheet strength from retained profit; management stated both purposes explicitly | [AR FY26, Note 15, PDF p205/pr194] and [Q4FY26 Concall 13May2026, MD & CEO]
CHAIN-STATE: TRACED

### CHAIN: Other financial liabilities (current) — the classification view | FY24-FY26
L1 REPORTED   TRACED | 4,06,419 at FY2026, 3,89,487 at FY2025, 4,20,611 at FY2024. It is 75.7% of total current liabilities and 59.8% of total equity at FY2026, and it was 121.8% of total equity at FY2024 (4,20,611 / 3,45,466) | [AR FY26, Consolidated Balance Sheet, PDF p163/pr152] and [AR FY25, Consolidated Balance Sheet, PDF p155/pr144]
L2 COMPONENTS TRACED | three named buckets in all three years. Owned (A) 21,060 / 23,291 / 24,992; Earmarked (B) 41,386 / 35,024 / 26,004; Clearing and settlement (C) 3,58,165 / 3,31,172 / 3,55,423. Within (A) at FY2026, member money is 10,298 + 5,612 + 1,083 = 16,993 of 24,992 = 68.0%; the genuinely corporate remainder is accrued employee benefits 4,164 + payables on fixed assets 3,341 + unpaid dividends 166 + due to associates 281 + other 47 = 7,999 | [AR FY26, Note 16, PDF p206/pr195] and [AR FY25, Note 16, PDF p192/pr181]
L3 DRIVER     TRACED | two components move on unrelated clocks. Deposit and margins from members: 2,32,583 / 2,24,870 / 2,06,976 — DOWN 11.0% over two years while index-options premium turnover rose 117.4% in FY2026 alone. Settlement obligation payable: 13,724 / 1,594 / 42,357 — purely which settlement cycle is open on March 31 | [AR FY26, Note 16, PDF p206/pr195] and [AR FY26, MD&A, PDF p58/pr47]
L4 COUNTERPARTY TRACED | bucket (C) is clearing members and clearing banks of Indian Clearing Corporation Limited; bucket (B) is issuer money (1%-of-public-issue deposits 6,213, recovery expense fund 5,625), defaulters' liabilities 1,555 and withheld liabilities 2,969, held under SEBI direction; the 16,993 inside (A) is trading-member deposit money. None of it is a related party under Ind AS 24 | [AR FY26, Note 16, PDF p206/pr195] and [AR FY26, Note 36, PDF p223-227/pr212-216]
L5 RECOGNITION TRACED | Notes 16.2 and 16.3 state that bank balances and deposits are earmarked against the (B) liabilities and the unpaid-dividend line; Note 12.1 states the earmarked balances are restricted to specified purposes and "all other cash and bank balances are available for the operating activities of the Group". NOTHING in the note earmarks an asset against the 16,993 of member deposits inside bucket (A) | [AR FY26, Notes 16.2-16.3 and 12.1, PDF p202, p206/pr191, pr195]
L6 BALANCE-SHEET DERIVED | earmarked financial assets 5,25,014 against earmarked liabilities 26,004 + 3,55,423 + 1,24,683 + 8,926 + 52 = 5,15,088, excess 9,926 = 1.9%. On the narrower earmarked-others test the cover is tighter still: 3,82,349 of assets against (B) + (C) = 3,81,427, excess 922 = 0.24%, against 2,439 at FY2025 and 10,258 at FY2024 — the buffer has fallen 91% in two years | [AR FY26, Notes 9, 11, 12 and 16, PDF p190-206/pr179-195]
L7 CASH       BROKEN | the liability moves through OPERATING and the asset that holds the same money moves through INVESTING. Cash-flow footnotes 2 and 3 strip the parent's earmarked pool and the subsidiaries' Core SGF but say nothing about bucket (C) — 87.5% of the liability — which therefore runs inside "Increase / (decrease) in other liabilities and other financial liabilities" +72,767, while the deposits holding it sit in investing as "Investment in fixed deposits (3,29,857)" | [AR FY26, Consolidated Cash Flow, PDF p165-166/pr154-155]
L8 SUSTAIN    NOT-DISCLOSED | whether 3,55,423 is a normal level or a March-31 artefact cannot be established from the annual report: only the year-end point is given, and the settlement-obligation component alone swung 13,724 / 1,594 / 42,357 on three single dates -> AR FY26 discloses no average or peak margin balance; ICCL's monthly SEBI stress-test filings, or a disclosure of average member margin, would answer it
CHAIN-STATE: BROKEN at L6/L7

> This chain **extends** W1_ledger.md §4's FY2026 chain on the same line; it does not replace it. Two
> differences are recorded rather than resolved silently (doctrine §10): (i) W1_ledger's inline
> arithmetic `1,55,712 + 1,93,114 + 1,51,688 = 5,00,657` is 143 short — the earmarked-SGF current
> account of 143 was omitted from the display; the correct decomposition is
> `1,55,855 + 1,93,114 + 1,51,688 = 5,00,657` and **W1_ledger's total was right**. (ii) W1_ledger treated
> bucket (A) as "owned" for the cash-flow estimate; this chain shows 68.0% of (A) is member money with
> no earmarked asset behind it.

### CHAIN: Trade receivables | FY26
L1 REPORTED   TRACED | net 55,316 against 28,778 restated (30,967 as first reported in the FY2025 AR); gross 65,109 against 34,802 restated (36,991 as first reported); impairment allowance 9,793 against 6,024 | [AR FY26, Note 10, PDF p199/pr188] and [AR FY25, Note 10, PDF p186/pr175]
L2 COMPONENTS TRACED | the ageing schedule splits the gross book: unbilled 50,637 + not due 1,836 + under 6 months 3,092 + 6-12 months 520 + 1-2 years 2,922 + 2-3 years 4,228 + over 3 years 1,874 = 65,109, zero residual. Unbilled is 77.8% of the gross book against 63.7% a year earlier. The over-1-year book is 2,922 + 4,228 + 1,874 = 9,024 against 6,461, +39.7%, and is 99.98% provided | [AR FY26, Note 10.5, PDF p199/pr188]
L3 DRIVER     DERIVED | unbilled receivable is the March run-rate, not a collection failure. Q4FY26 consolidated revenue 1,56,351 against Q4FY25 84,664, +84.7%; unbilled / Q4 revenue is 50,637 / 1,56,351 = 32.4% against 22,184 / 84,664 = 26.2%. Billed gross receivables grew only 65,109 − 50,637 = 14,472 against 34,802 − 22,184 = 12,618, +14.7%, well BELOW revenue +63.5%. The entire overrun is unbilled: 28,453 of the 30,307 gross increase, i.e. 93.9% | [AR FY26, Note 10.5, PDF p199/pr188] and [Q4FY26 Results 07May2026, consolidated quarterly statement]
L4 COUNTERPARTY TRACED | not related-party. Note 36 shows total related-party receivables of 133 + 21 + 1 + 0 = 155, i.e. 0.24% of the gross book, plus a CDSL deposit of 5; Note 10.3 confirms no dues from directors or officers. Management names the concentration on the credit side: "there was a provision of about Rs. 40 crores made in our subsidiary clearing company from one of the debtors" — a single ICCL debtor is essentially the whole year's impairment charge | [AR FY26, Note 36, PDF p226/pr215] and [Q1FY27 Concall 10Aug2026, CFO]
L5 RECOGNITION TRACED | Ind AS 109 simplified approach, lifetime expected credit loss by ageing bucket. Note 10.2 gives a credit period of 0-60 days. The loss-rate matrix was RE-ESTIMATED in FY2026 in both directions: under 6 months 39% to 13%, 6-12 months 50% to 72%, 1-2 years 46% to 100%. On FY2025's rates the FY2026 allowance would be 8,914 rather than 9,793, so the re-estimate is net conservative by 879 | [AR FY26, Notes 10.2 and 10.5, PDF p199/pr188] and [AR FY25, Note 10.5, PDF p186/pr175]
L6 BALANCE-SHEET DERIVED | the allowance roll-forward closes exactly: 6,024 + 4,025 − 256 = 9,793. Receivable days on full-year revenue rose 34,802 / 2,95,734 x 365 = 43.0 to 65,109 / 4,83,395 x 365 = 49.2, +6.2 days; but on Q4-annualised revenue they are FLAT — 34,802 / 3,38,656 x 365 = 37.5 against 65,109 / 6,25,404 x 365 = 38.0, +0.5 days. The 6.2-day figure is measuring the intra-year revenue ramp, not the debtors | [AR FY26, Note 10.4, PDF p199/pr188] and [Q4FY26 Results 07May2026, consolidated quarterly statement]
L7 CASH       DERIVED | the cash flow ties to the note to within 32 lakh. Reported "Decrease / (increase) in trade receivables (30,595)"; the note-implied gross build is 65,109 − 34,802 + 256 written off = 30,563; residual 32 = 0.1%. Cross-check on the net line: 28,778 + 30,595 − 4,057 impairment add-back = 55,316, exact | [AR FY26, Consolidated Cash Flow, PDF p165/pr154] and [AR FY26, Note 10.4, PDF p199/pr188]
L8 SUSTAIN    DERIVED | the unbilled balance repeats at about one month of the exit run-rate: 50,637 / (1,56,351 / 3) = 0.97 months against 22,184 / (84,664 / 3) = 0.79 months. The condition for it not to grow further is that the March quarter stops accelerating; the condition for the AGED book is different and worse — 9,024 over one year, 100% provided, growing 39.7% while the book grew 87.1% | [AR FY26, Note 10.5, PDF p199/pr188]
CHAIN-STATE: TRACED, with a BROKEN comparative — see F3

### CHAIN: Investments (other investments, excluding subsidiaries and associates) | FY26
L1 REPORTED   TRACED | 95,542 non-current + 2,34,501 current = 3,30,043 against 82,404 + 1,52,084 = 2,34,488, +40.7% (3,30,043 − 2,34,488 = 95,555) | [AR FY26, Consolidated Balance Sheet, PDF p163/pr152]
L2 COMPONENTS TRACED | Note 9 labels every holding Owned or Earmarked and lists it issuer by issuer across nine pages. Owned 3,05,686 = unquoted equity at FVTPL 4,092 + bonds, NCDs, SDLs and G-Sec at amortised cost 69,761 + mutual funds and ETFs at FVTPL 2,21,094 + current portion of long-term 9,528 − diminution provision 1,398 + accrued interest 2,609. Earmarked 24,357 = G-Sec 21,689 + mutual funds 2,668. Total 3,30,043, zero residual | [AR FY26, Note 9, PDF p190-198/pr179-187]
L3 DRIVER     DERIVED | the corpus is the FY2026 own-account cash build, not a new deployment: owned investments 3,05,686 − 2,03,588 = 1,02,098 and owned liquid funds 3,08,596 − 1,67,486 = 1,41,110, together 1,02,098 + 1,41,110 = 2,43,208 against retained profit of 2,49,698 − 31,585 = 2,18,113. Mix shifted to mutual funds: 2,21,094 / 1,18,110 = 1.872x, +87.2%, while bonds and SDLs were roughly flat at 69,761 against 56,631 | [AR FY26, Note 9, PDF p191-192/pr180-181] and [AR FY25, Note 9, PDF p179-181/pr168-170]
L4 COUNTERPARTY TRACED | no related party. Every bond, NCD, SDL, G-Sec, mutual fund and ETF is named individually in Note 9 and none appears in Note 36. The only unquoted equity of size is Open Network for Digital Commerce at 4,000 (unchanged) and Afrinex Ltd - Mauritius at 92 | [AR FY26, Note 9, PDF p190-198/pr179-187] and [AR FY26, Note 36, PDF p223-227/pr212-216]
L5 RECOGNITION TRACED | policy 2.3.1 and 2.3.4: debt instruments held to collect at amortised cost with effective-interest recognition, mutual funds and ETFs at FVTPL through profit or loss. 8,875 of FY2026 investment income of 29,030 — 30.6% — is fair-value movement rather than contractual yield. Fair-value hierarchy is Level 1 for quoted MFs and ETFs; the Note 34 price-risk sensitivity is stated on 2,21,094 of MFs and ETFs (0.25% = 553) and 77,891 of G-Sec, bonds and debentures (0.25% = 195) | [AR FY26, Notes 2.3.1, 2.3.4 and 34, PDF p173-174, p221-222/pr162-163, pr210-211]
L6 BALANCE-SHEET DERIVED | investments are 3,30,043 / 13,44,614 = 24.5% of total assets and, on the owned part alone, 3,05,686 / 6,79,550 = 45.0% of total equity. Carrying value exceeds market for the quoted book: current 2,35,899 carrying against 2,34,615 market (−1,284) and non-current 91,450 against 91,189 (−261), together −1,545 unrecognised loss on amortised-cost holdings, 0.6% of PBT | [AR FY26, Note 9, PDF p191-192/pr180-181]
L7 CASH       TRACED | investing carries every leg separately: investment in mutual funds (91,484), investment in bonds, NCDs and SDLs (21,520), proceeds from bonds, NCDs and SDLs 22,081, interest received 23,798, dividend received 1. The FVTPL gain of 8,875 and interest income of 20,154 are both stripped out of CFO as non-cash adjustments | [AR FY26, Consolidated Cash Flow, PDF p165/pr154]
L8 SUSTAIN    DERIVED | the yield on the corpus is not repeatable in its current mix: 8,875 / 29,030 = 30.6% of investment income is mark-to-market on a mutual-fund book that grew 87.2% in one year, and Note 34 sizes a 0.25% adverse price move at 553. The condition for the income line to repeat is that the corpus is not distributed — payout is 12.6% — and that debt markets do not reprice | [AR FY26, Note 23, PDF p211/pr200] and [AR FY26, Note 34, PDF p221/pr210]
CHAIN-STATE: TRACED

### CHAIN: Cash and bank balances | FY26
L1 REPORTED   TRACED | cash and cash equivalents 1,67,159 + bank balances other than cash equivalents 3,50,121 = 5,17,280 on the face, against 1,55,100 + 3,63,286 = 5,18,386. Adding the bank deposits and accrued interest inside Note 11 non-current, 2,91,973, gives total liquid funds of 8,09,253 against 6,35,595 | [AR FY26, Consolidated Balance Sheet, PDF p163/pr152] and [AR FY26, Notes 11 and 12, PDF p200-202/pr189-191]
L2 COMPONENTS TRACED | every line is labelled. Owned 3,08,596 = current accounts 6,637 + short deposits 4,667 + deposits under 12 months 1,51,346 + accrued interest 5,661 + deposits over 12 months 1,37,461 + accrued interest 2,824. Earmarked 5,00,657 = others 3,82,349 + SGF 1,18,256 + IPF 52. Sum 3,08,596 + 5,00,657 = 8,09,253, zero residual | [AR FY26, Notes 11 and 12, PDF p200-202/pr189-191]
L3 DRIVER     DERIVED | own-account liquid funds nearly doubled, 1,67,486 to 3,08,596 = +84.3%, while earmarked funds moved 4,68,109 to 5,00,657 = +7.0%. The whole own-account build is the year's retained profit: 2,49,698 attributable less 31,585 dividends = 2,18,113, against a combined own liquid-fund and own-investment build of 2,43,208. Tenor lengthened sharply: owned deposits over 12 months went 16,439 to 1,37,461, +736% | [AR FY26, Notes 11 and 12, PDF p200-202/pr189-191]
L4 COUNTERPARTY NOT-DISCLOSED | the group holds `8,09,253 in bank deposits and current accounts and names not one bank. Note 34's credit-risk paragraph does not give a bank-wise or rating-wise concentration, and there is no counterparty table -> AR FY26 Note 34 (PDF p218-222/pr207-211) gives no deposit counterparty disclosure; a bank-wise concentration schedule, or ICCL's clearing-bank list filed with SEBI, would answer it. The one bank ever named is Punjab & Sindh Bank, as a fully provided 316 receivable in Note 11
L5 RECOGNITION TRACED | Note 12.1: "the above mentioned cash and bank balances are restricted cash and bank balances which are to be used for specified purposes. All other cash and bank balances are available for the operating activities of the Group." That single sentence is what makes the own/earmarked separation a TRACED fact rather than an estimate | [AR FY26, Note 12.1, PDF p202/pr191]
L6 BALANCE-SHEET DERIVED | the earmarked half is matched to its liabilities and the match is disclosed on both sides: earmarked-others 3,82,349 against Note 16 (B) + (C) = 26,004 + 3,55,423 = 3,81,427, excess 3,82,349 - 3,81,427 = 922; earmarked-SGF 1,18,256 plus Note 13 SGF receivable 296 plus roughly 6,131 of prescribed securities against the Core SGF of 1,24,683; earmarked-IPF 52 against the IPF contribution payable of 52, exact | [AR FY26, Notes 11, 12, 13, 16 and 41, PDF p200-208, p231/pr189-197, pr220]
L7 CASH       BROKEN | the cash-flow statement's own definition of cash excludes what the balance sheet includes: closing "cash and cash equivalents" is 1,64,642, reconciled from the balance sheet's 1,67,159 by removing unpaid dividend 1,826, other earmarked current accounts 480, SGF current account 143 and short earmarked deposits 68. But 6,41,919 of deposits — everything in Note 11 non-current and Note 12 "other bank balances" — sits in INVESTING, so the statement's "cash" is 20.3% of the group's actual liquid funds (1,64,642 / 8,09,253) | [AR FY26, Consolidated Cash Flow, PDF p166/pr155]
L8 SUSTAIN    DERIVED | own-account liquidity is now 3,08,596, i.e. 45.4% of total equity and 63.8% of a year's revenue, and it is growing faster than the business can absorb it: capex of 51,516 / (2,49,698 - 31,585) = 23.6% of the year's profit retained after dividend, and 3,08,596 / 6,79,550 = 45.4% and 3,08,596 / 4,83,395 = 63.8%. The condition for it to keep compounding is an unchanged payout; management has stated three intended uses — technology capex it expects to double, colocation capacity, and a possible land purchase in Mumbai | [AR FY26, Notes 11 and 12, PDF p200-202/pr189-191] and [Q4FY26 Concall 13May2026, MD & CEO]
CHAIN-STATE: BROKEN at L1/L7

### CHAIN: Property, plant and equipment (with CWIP and IAUD) | FY26
L1 REPORTED   TRACED | net PPE 56,259 against 22,217, +153.2% (56,259 − 22,217 = 34,042); CWIP 3,255 against 4,073, −20.1%; intangibles 4,122 against 3,893; IAUD 4,420 against 1,339, +230.1%. Combined operating asset base 68,056 against 31,522 | [AR FY26, Consolidated Balance Sheet, PDF p163/pr152]
L2 COMPONENTS TRACED | the increase is two assets. Buildings net 1,778 to 18,585 (+16,807) on gross additions of 18,022, and computers, hardware and networking net 14,360 to 23,347 (+8,987) on gross additions of 18,530; plant and equipment net 1,268 to 7,512 on additions of 7,503. The building is entirely BSE Limited's — standalone buildings additions are also 18,022 | [AR FY26, Note 3, PDF p181/pr170] and [AR FY26, Standalone Note 3, PDF p263/pr252]
L3 DRIVER     TRACED | management states the driver and the amount: "In the last two years, we have built around Rs. 500 crores as gross block, which has gone for capacity increase" — against an actual two-year gross-block build of 1,05,539 − 50,796 = 54,743. Colocation is the named return: "the returns from this capex cycle are already visible in the 133% growth in colocation revenues", on colocation and connectivity revenue of 17,109 | [Q4FY26 Concall 13May2026, MD & CEO] and [AR FY26, MD&A, PDF p76-77/pr65-66] and [AR FY26, Note 22, PDF p211/pr200]
L4 COUNTERPARTY NOT-DISCLOSED | no vendor, contractor or seller is named for the 18,022 building or the 18,530 of hardware; capital commitments are given only as a single figure of 10,029 (17,006 at FY2025), and Note 36 shows no related-party capital transaction -> AR FY26 Note 38 (PDF p227/pr216) gives capital commitments as one number with no counterparty; the standalone title-deeds note 44 (PDF p308/pr297) names properties but not vendors; a fixed-asset addition schedule by counterparty would answer it
L5 RECOGNITION TRACED | Ind AS 16, cost less accumulated depreciation. One estimate change is disclosed and quantified: the useful life of buildings was revised to 25 years effective 1 April 2024 on external valuation advice, "impact of same was Rs. 13", applied prospectively under Ind AS 8. Two properties with a carrying amount of 20 (228 at FY2025) do not have updated property cards at the Land and Revenue Department | [AR FY26, Note 3 notes 2 and 3, PDF p181/pr170]
L6 BALANCE-SHEET DERIVED | the roll-forward closes exactly on both halves. Gross: 63,738 + 47,578 − 6,405 + 101 transferred from investment property + 527 FX = 1,05,539. Accumulated depreciation: 41,521 + 13,720 − 6,373 + 47 + 365 = 49,280. Net 1,05,539 − 49,280 = 56,259, tying to the face. Depreciation also ties to the P&L: PPE 13,720 + investment property 5 + intangible amortisation 2,171 = 15,896 | [AR FY26, Notes 3, 4 and 6, PDF p181-184/pr170-173] and [AR FY26, Consolidated P&L, PDF p164/pr153]
L7 CASH       BROKEN | accrual additions of 47,578 + 2,470 + (3,255 − 4,073) + (4,420 − 1,339) = 52,311; less non-cash FX of 527 + 39, the investment-property transfer of 101 and the 918 increase in payables for fixed assets gives 50,726 against a reported cash line of 51,516 — residual 790, 1.5%. But the bridge only closes because 15,584 of it was ALREADY PAID IN FY2025 as a capital advance that ran through the OPERATING section. Excluding it, true FY2026 investing capex is 50,726 − 15,584 = 35,142 | [AR FY26, Consolidated Cash Flow, PDF p165/pr154] and [AR FY26, Note 13, PDF p202/pr191]
L8 SUSTAIN    DERIVED | this capex cycle is not finished and management says so: technology spend of "around Rs. 300 crores" is "almost going to be doubling", colocation capacity is being increased, and a Mumbai land purchase is under consideration. Capital commitments already contracted are 10,029, and IAUD rose 4,420 - 1,339 = 3,081. Depreciation follows: 15,896 / 11,298 = 1.407x, +40.7%, on a gross block that grew 1,05,539 / 50,796 = 2.08x in two years | [Q4FY26 Concall 13May2026, MD & CEO] and [AR FY26, Note 38, PDF p227/pr216]
CHAIN-STATE: BROKEN at L6/L7

### CHAIN: Core settlement guarantee fund balance | FY26
L1 REPORTED   TRACED | 1,24,683 against 1,13,260, +10.1% (1,24,683 − 1,13,260 = 11,423). Presented as its own caption, line 4, BETWEEN total equity and liabilities — it is neither equity nor a liability on the face of the balance sheet | [AR FY26, Consolidated Balance Sheet, PDF p163/pr152]
L2 COMPONENTS TRACED | ICCL 1,23,264 + India International Clearing Corporation 1,419 = 1,24,683. ICCL's fund splits two ways and both sum exactly: by segment, equity derivative 96,432 + equity 22,032 + commodity derivative 1,762 + currency derivative 1,538 + EGR 1,265 + debt 233 + SLB 2 = 1,23,264; by contributor, ICCL 60,896 + BSE 17,952 + NSE 26,529 + MSE 934 + other 16,953 = 1,23,264 | [AR FY26, Notes 41 and 42, PDF p231-232/pr220-221]
L3 DRIVER     TRACED | SEBI's Minimum Required Contribution, computed from monthly stress-test values — not from turnover. Under IFSCA (MII) Regulations 2021 Regulation 31(2) the India ICC fund must be the greater of the stress-tested minimum corpus or USD 1 million. This is why the fund grew 10.1% in a year revenue grew 63.5% and the P&L charge FELL 14.5% to 7,696 | [AR FY26, Note 2.3.12, PDF p178/pr167] and [AR FY26, Note 42, PDF p232/pr221]
L4 COUNTERPARTY TRACED | the group's own clearing corporations hold the fund, but 22.3% of ICCL's corpus was contributed by competitors that clear through it — NSE 26,529 and MSE 934, together 27,463 of 1,23,264. BSE Limited itself has contributed 17,952, i.e. 14.6%, and ICCL 60,896, i.e. 49.4% | [AR FY26, Note 41, PDF p231-232/pr220-221]
L5 RECOGNITION TRACED | policy 2.3.12: contributions are expensed in the period made and never reversed even if the corpus later exceeds the MRC. Investment income on the fund and fines recovered from members are credited DIRECTLY to the fund and never pass through profit or loss. The presentation as a separate caption is the reason total equity of 6,79,550 does not contain it | [AR FY26, Note 2.3.12, PDF p178/pr167]
L6 BALANCE-SHEET DERIVED | the fund grew 11,423 on a P&L charge of 7,696 and an equity transfer of 129, leaving 11,423 − 7,696 − 129 = 3,598 of fund investment income and member penalties that never appear in profit or loss. Matching assets: earmarked-SGF bank balances 1,18,256 + Note 13 "Others - SGF" 296 + roughly 6,131 held in prescribed securities inside Note 9 = 1,24,683 | [AR FY26, Notes 11, 12, 13 and 41, PDF p200-202, p231/pr189-191, pr220] and [AR FY26, Statement of Changes in Equity, PDF p168/pr157]
L7 CASH       TRACED | cash-flow footnote 3 excludes it entirely: "Movement in Core Settlement Guarantee Fund liabilities and related assets of subsidiary companies are not considered." FY2026 CFO of 3,10,368 is therefore NET of the 7,696 charge, whereas in FY2024 and every year back to FY2017 the contribution was added back as a non-cash adjustment (FY2024 +9,170). The two presentations are not comparable and no note bridges them | [AR FY26, Consolidated Cash Flow, PDF p166/pr155] and [AR FY24, Consolidated Cash Flow, PDF p158/pr152]
L8 SUSTAIN    DERIVED | falling as a claim on the business: 1,24,683 / 4,83,395 = ₹0.258 of fund per ₹1 of revenue against 95,496 / 1,39,003 = ₹0.687 two years earlier, a 62% fall. The condition for it staying small is that ICCL's stress-tested exposure does not step up with derivative open interest; the ten-year P&L charge in trend_10y.csv ranges from 74 to 9,170, so the item is volatile by design | [AR FY26, Notes 41 and 42, PDF p231-232/pr220-221]
CHAIN-STATE: TRACED

### CHAIN: Investment in associate — Central Depository Services (India) Limited | FY26
L1 REPORTED   TRACED | carrying value 44,940 against 41,949, +7.1%, inside total investments in associates of 53,657 against 50,053. 3,13,50,000 shares, 15.00% voting right, unchanged. Standalone carrying value is 3,542, at cost | [AR FY26, Note 8, PDF p188/pr177] and [AR FY26, Standalone Note 8, PDF p268/pr257]
L2 COMPONENTS DERIVED | CDSL is 44,940 / 53,657 = 83.8% of the associates line; the other six associates are India International Bullion Holding 5,870 + Hindustan Power Exchange 1,620 + Countrywide Commodity Repository 1,114 + BSE E-Agricultural Markets 113 + BFSI Sector Skill Council 100 less its own full impairment of 100 = 8,717, together 44,940 + 8,717 = 53,657, zero residual | [AR FY26, Note 8, PDF p187-188/pr176-177]
L3 DRIVER     DERIVED | CDSL's own earnings, not a stake change: share of profit 6,842 against 7,900, −13.4%, on an unchanged 3,13,50,000 shares. CDSL alone is 6,842 / 6,542 = 104.6% of the consolidated associates line, the other six netting to −300. The stake reached 15.00% because BSE divested 5% in FY2024 "to meet the requirement of SEBI directive", realising proceeds of 51,597 and an exceptional gain of 40,662 taxed at 3,910 | [AR FY26, Note 8, PDF p189/pr178] and [AR FY25, Note 52, PDF p211/pr200]
L4 COUNTERPARTY TRACED | a listed related party under Ind AS 24 in which BSE is the largest single shareholder and nominates a director. Trading balances are trivial — payable 38 against 2, plus CDSL Ventures payable 20 and a deposit asset of 5 — and administrative expenditure paid to CDSL was 293 against 183. The two companies also share a statutory auditor, S.R. Batliboi & Co. LLP | [AR FY26, Note 36, PDF p225-227/pr214-216] and [W2_peers method note, records/red_flags.md]
L5 RECOGNITION TRACED | equity method under Ind AS 28: cost plus share of post-acquisition results, with dividends reducing the carrying amount rather than entering income. Fair value is NOT recognised and never enters profit or loss — which is the direct answer to the question an analyst asked and management did not answer. But the market value IS disclosed, in the same note, in both years | [AR FY26, Note 8, PDF p188/pr177]
L6 BALANCE-SHEET DERIVED | the roll-forward closes exactly: 41,949 + 6,842 share of profit + 68 share of OCI − 3,919 dividend received = 44,940. Against that, "aggregate market value of quoted investments" is 3,50,932 (3,82,486 at FY2025), so 3,50,932 − 44,940 = 3,05,992 of value is not on the balance sheet — 45.0% of total equity. Implied CDSL price `3,50,932 lakh / 3,13,50,000 shares = `1,119 per share against `1,220 a year earlier | [AR FY26, Note 8, PDF p188-189/pr177-178]
L7 CASH       BROKEN | the only cash is the 3,919 dividend, and the CONSOLIDATED cash flow does not show it — investing carries "Dividend received 1" and the investing section sums to its stated total of (2,73,967) with no room for it. The STANDALONE does show it: investing carries "Dividend received from subsidiaries, associate and others 10,038", and standalone Note 23 splits that exactly as dividend from subsidiaries 6,118 + dividend income from others 3,919 + mutual-fund dividend 1 = 10,038 | [AR FY26, Standalone Cash Flow, PDF p251/pr240] and [AR FY26, Standalone Note 23, PDF p286/pr275]
L8 SUSTAIN    DERIVED | shrinking as a claim on earnings: 6,542 / 3,29,914 = 2.0% of PBT against 8,259 / 1,74,827 = 4.7%, because the parent's own profit rose 88.7% while the associate's contribution fell 20.8%. The cash yield is the more durable number — 3,919 against 3,449, +13.6% — but it is 3,919 / 3,50,932 = 1.12% on market value. Repetition depends on CDSL's own earnings recovering; the six non-CDSL associates net to −300 and have never contributed positively in aggregate in either year read | [AR FY26, Note 8, PDF p188-189/pr177-178] and [AR FY26, Consolidated P&L, PDF p164/pr153]
CHAIN-STATE: BROKEN at L7 (consolidated presentation), TRACED at the standalone

---

## 5. Findings

### FINDING: The ₹10,60,000 lakh clearing-corporation guarantee did not expire — it was removed from the disclosure and the prior year was restated to match
S1 WHAT: The FY2025 annual report disclosed "Guarantees given by the Group" of 10,60,024 (7,70,006 at FY2024), of which note 3 explained that 10,60,000 was a bank guarantee given by ICCL "towards Inter CCP collateral under Interoperability framework as prescribed by SEBI" `[AR FY25, Note 38, PDF p209-210/pr198-199]`. The FY2026 report shows guarantees of 23 — and shows the FY2025 comparative as **24**, not 10,60,024 `[AR FY26, Note 37, PDF p227/pr216]`.
S2 WHY: If the guarantee had simply matured, the FY2025 comparative would still read 10,60,024 and the FY2026 figure would read 23. Restating the comparative removes the item from both years, which is only consistent with a change in what the group classifies as a disclosable contingent liability. What replaced it is a new unnumbered paragraph under Note 37 describing clearing-member exposure assessed "on a net basis" and concluding that "available collateral is adequate to meet potential obligations arising from Clearing Member defaults" — a management assertion where a rupee number stood.
S3 EVIDENCE: 10,60,000 lakh is 78.8% of FY2026 total assets of 13,44,614 and **1.56x total equity** of 6,79,550. Its counter-proportion inside the same note: every other line in Note 37 GREW — income tax matters 11,170 to 13,496 (+20.8%), indirect tax 2,210 to 5,930 (+168.3%), claims not acknowledged as debts 10,504 to 13,567 (+29.2%), total non-guarantee contingent liabilities 23,884 to 32,993 (+38.1%). The one line that vanished is 32x larger than everything that stayed. The standalone tells the same story from the other side: BSE Limited's own guarantees are 23 at FY2026 and 23 at FY2025 `[AR FY26, Standalone Note 36, PDF p302/pr291]`, so consolidated guarantees of 23 now equal the parent's alone and the clearing subsidiary contributes nothing. The phrase "bank guarantee" does not occur anywhere in the FY2026 annual report.
S4 CONNECTS: The FY2026 secretarial audit report for ICCL discloses that "SEBI issued a Show Cause Notice to the Company for alleged non-compliance with the SEBI Circular on interoperability among clearing corporations", settled by a SEBI order of 15 May 2025 without monetary penalty `[AR FY26, ICCL Secretarial Audit Report, PDF p48/pr37]`. The disappearing disclosure and the regulatory action concern the same framework. Separately, RBI's Amendment Directions on Capital Market Exposure, effective 1 July 2026, act directly on bank guarantees in the capital market, and management stated on the Q1FY27 call that "there are remnant bank guarantees in the system which are of the past because of which we are yet to see the full impact" `[Q1FY27 Concall 10Aug2026, MD & CEO]`. RF-009 already records the loss of the "of which remote" grading in the same note in the same year; that is two gradings and one quantum removed from one note in one year.
DOMAINS: Notes, BalanceSheet, Governance, Industry
DISCONFIRM: Evidence against a concealment reading was looked for and partly found. (i) A guarantee that ceased to exist would legitimately show as nil in the current year — but that does not explain restating the comparative, and the FY2024 comparative in the FY2025 report was 7,70,006, so the company had previously carried the item forward across years. (ii) Note 37 paragraph 3 is a genuine substantive addition, not merely a deletion, and it describes a real risk-management methodology. (iii) The auditor issued an unmodified opinion and CARO raised no clause on this. (iv) The guarantee was an inter-CCP collateral instrument under an interoperability framework, so it may have been replaced by a different collateral form rather than released. **No note anywhere in the FY2026 report explains any of this**, which is the point.
S5 MEANS: A disclosed, quantified exposure of 1.56x equity was replaced, retrospectively and without explanation, by an unquantified statement that collateral is adequate — and the reader now has no way to size the clearing corporation's largest off-balance-sheet obligation in any year.
BASE-RATE: The realised loss on this exposure at BSE is nil — no clearing-member default has been charged against ICCL's Core SGF in any of the nine years read, and the fund has only grown. The systemic base rate is not nil: a clearing corporation's inter-CCP collateral is precisely the instrument that transmits a default across venues, and SEBI's interoperability framework exists because a single-venue default is a system event. The company's own regulator issued a show-cause notice on this framework within the window.
S6 IMPLICATION: The quality of the asset base cannot be assessed at the group's largest single risk concentration, because the number that sized it is no longer published on any basis; the margin of safety required for the clearing subsidiary rises accordingly. Monitorable: whether the FY2027 report restores a quantum for inter-CCP collateral, and what the RBI capital-market-exposure directions do to bank-guarantee availability from 1 July 2026. Thesis-breaker: a clearing-member default that draws on collateral the group can no longer be shown to have.
SEVERITY: High

### FINDING: ₹15,584 lakh of capital expenditure was paid through the operating section in FY2025 and shown as investing capex in FY2026 — inflating FY2026 CFO by 5.0%
S1 WHAT: A "Capital advances" line of 15,584 appears in Note 13 *Other assets (current)* at 31 March 2025 and is nil at 31 March 2024 and at 31 March 2026 `[AR FY26, Note 13, PDF p202/pr191]` and `[AR FY25, Note 13, PDF p188/pr177]`. FY2025's entire reported capex cash line was 15,323 — **smaller than the advance** — so the advance cannot have been paid through FY2025's investing section. It was paid through FY2025's operating working capital, and it converted into the 18,022 building addition in FY2026 while the FY2026 investing line reported it as cash capex of that year.
S2 WHY: Note 13 sits inside the cash-flow line "Decrease / (increase) in other assets and other financial assets". Capital advances are an *other current asset*, so their payment lands in operating unless the preparer reclassifies them; their release lands in operating too. Because the FY2026 investing line is described as "Purchase of property, plant and equipment, intangible assets, capital work-in-progress, intangible assets under development **and capital advances**", the same rupee is presented as an operating source and an investing use in the same year. Total cash is unaffected; the operating/investing split is not.
S3 EVIDENCE: The FY2026 other-current-asset movement reconciles exactly and identifies the amount: capital advances (15,584) + advance to creditors 1,099 + input credit 333 + prepaid 192 − advances recoverable 26 = (13,986), against a reported operating inflow of +13,638 — residual 281, 2.1% `[AR FY26, Note 13, PDF p202/pr191]` and `[AR FY26, Consolidated Cash Flow, PDF p165/pr154]`. On the investing side, accrual additions of 47,578 + 2,470 + (3,255 − 4,073) + (4,420 − 1,339) = 52,311; removing non-cash FX of 566, the investment-property transfer of 101 and the 918 rise in payables for fixed assets gives 50,726 against a reported 51,516 — residual 790, 1.5%. **The bridge closes only if the advance is treated as paid in FY2026.** Counter-proportion: 15,584 is 30.3% of the FY2026 capex line but 101.7% of the FY2025 capex line — the same amount is a third of one year and more than all of the other. The alternative explanation, an unpaid accrual at FY2025, is eliminated: payables for fixed assets in Note 16 were 2,423 at FY2025 against 961 at FY2024, a rise of only 1,462, and no other liability moved by anything approaching 15,584.
S4 CONNECTS: W1_ledger's own-account CFO series is affected. Correcting the classification: FY2026 own-account CFO 2,86,117 − 15,584 = 2,70,533, a conversion of 2,70,533 / 2,47,530 = **1.093 rather than 1.16**; FY2025 68,008 + 15,584 = 83,592, a conversion of **0.635 rather than 0.52**. The three-year cumulative is unchanged at 4,29,965 / 4,56,402 = 0.942, so the correction moves a year, not the total — which is exactly why doctrine §2c tests conversion cumulatively. Management's MD&A quotes a standalone capital-addition figure of 45,753 and a standalone capex cash line of 46,579 without reconciling either to the advance `[AR FY26, MD&A, PDF p76/pr65]`.
DOMAINS: CashFlow, BalanceSheet, Notes, MgmtCommentary
DISCONFIRM: Three tests were run against this reading. (i) If the advance had been paid earlier than FY2025 it would appear at FY2024 — it does not; Note 13 shows nil `[AR FY25, Note 13, PDF p188/pr177]`. (ii) If it had been accrued rather than paid, an offsetting liability of similar size would exist — none does. (iii) If it were not a capital advance at all, the FY2026 building addition of 18,022 would have to be explained some other way — it cannot be; standalone buildings additions are also 18,022 and standalone capital advances were 15,333. What genuinely cuts the other way: **total cash is not misstated in either year**, the auditor is not required to disaggregate a combined caption, and the two errors reverse across the two years. This is a classification finding, not a cash finding.
S5 MEANS: FY2026's headline operating cash flow of 3,10,368 contains 15,584 that is a released capital advance rather than operating cash, and FY2026's capex line contains 15,584 that left the building in the prior year — so neither the CFO nor the capex figure for either year is a clean measure of what it is named after.
BASE-RATE: This has cost nothing and nobody has lost money on it — the amounts reverse and the two-year total is right. But the same caption is where the company's one unexplained cash-flow restatement already lives: RF-027 records an unexplained 19,679 restatement of FY2024 CFO with no stated cause, and this is the second classification defect found in the same statement in the same three-year window. Two defects in one statement is a pattern about preparation quality, not an accident.
S6 IMPLICATION: Single-year cash conversion is not a usable input for this company on the reported presentation, and any model that anchors on FY2026 CFO of 3,10,368 or on FY2026 capex of 51,516 is anchoring on a number that contains a prior-year item. The durable measure is the three-year own-account cumulative of 0.942. Monitorable: whether the FY2027 report presents capital advances inside investing. Next check: FY2027 annual report, consolidated Note 13 and the investing section.
SEVERITY: Medium

### FINDING: RF-026 does not survive contact with the exit run-rate — receivable days are flat; what does not survive is the ₹2,189 lakh restatement that made the base look smaller
S1 WHAT: RF-026 records gross receivables +87.1% and unbilled +128.3% against revenue +63.5%, and grades it High as doctrine §2c break 3. Both percentages are computed off a FY2025 base of 34,802 gross and 22,184 unbilled. The FY2025 annual report reported **36,991 gross and 24,373 unbilled** `[AR FY25, Note 10, PDF p186/pr175]`. On the company's own original numbers the growth rates are **+76.0% and +107.8%**, not +87.1% and +128.3%.
S2 WHY: Two mechanisms, and neither is a collection failure. First, the FY2026 report reclassified exactly 2,189 out of unbilled trade receivables into other current financial assets in the FY2025 comparative — trade receivables 30,967 to 28,778 and other current financial assets 475 to 2,664, an exact offset with total current assets unchanged at 7,34,266 `[AR FY26, Consolidated Balance Sheet, PDF p163/pr152]`. No note explains it. Second, unbilled receivable at an exchange is the un-invoiced portion of the most recent month's transaction charges, so it scales with the **exit** run-rate, not the annual average, and FY2026's exit run-rate was far above its own year.
S3 EVIDENCE: Q4FY26 consolidated revenue was 1,56,351 against Q4FY25 84,664, +84.7% `[Q4FY26 Results 07May2026, consolidated quarterly statement]`. On Q4-annualised revenue, gross receivable days are **38.0 at FY2026 against 37.5 at FY2025 — plus half a day**; on full-year revenue they are 49.2 against 43.0, plus 6.2 days. The counter-proportion inside the book settles which measure is right: unbilled grew 28,453 (+128.3%) while **billed** gross receivables grew only 1,854, from 12,618 to 14,472, **+14.7% against revenue +63.5%** — the invoiced book grew at less than a quarter of revenue. Sizing the residual concern honestly: unbilled as a share of Q4 revenue went 26.2% to 32.4%, so the "excess" unbilled is `50,637 − 0.262 x 1,56,351 = 9,673` on the restated base and 5,628 on the as-first-reported base — 2.0% and 1.2% of revenue respectively. The FY2026 report contradicts itself on which base is right: Note 34's liquidity table still carries **30,967** trade receivables and **475** other financial assets for FY2025, the un-restated figures, while Notes 10 and 11 and the balance sheet carry 28,778 and 2,664 `[AR FY26, Note 34, PDF p220/pr209]`.
S4 CONNECTS: The credit-loss side is concentrated and management named it: "there was a provision of about Rs. 40 crores made in our subsidiary clearing company from one of the debtors" `[Q1FY27 Concall 10Aug2026, CFO]`. That matches the consolidated impairment charge of 4,025 against a standalone impairment **release** of (284) — so the entire charge is in subsidiaries, on subsidiary gross receivables of 65,109 − 52,736 = 12,373, i.e. roughly a third of the clearing group's debtor book provided against one name `[AR FY26, Notes 10 and 10.4, PDF p199/pr188]` and `[AR FY26, Standalone Note 10, PDF p276/pr265]`. Related-party receivables are 155 of 65,109 = 0.24%, so none of the growth is intra-group `[AR FY26, Note 36, PDF p226/pr215]`.
DOMAINS: BalanceSheet, Notes, CashFlow, MgmtCommentary
DISCONFIRM: Evidence against the benign reading was sought and some was found. (i) The over-one-year book grew 6,461 to 9,024, +39.7%, and is 99.98% provided — a real ageing tail, though only 13.9% of the gross book. (ii) The expected-loss rate on the freshest billed bucket was cut from 39% to 13%; had FY2025's rate been kept, the charge would have been 809 higher. (iii) Applying FY2025's full loss matrix to FY2026's buckets gives 8,914 against an actual 9,793, so the re-estimate is **net conservative by 879** — the cut in one bucket is more than offset by taking 1-2 years from 46% to 100%. (iv) The cash flow ties to the note to within 32 lakh on a 30,595 movement, 0.1%, so no receivable has been created without a matching balance-sheet entry.
S5 MEANS: The receivable build is a revenue-timing consequence, not an earnings-quality event, and RF-026's High grade rests on a comparison of an annual flow with a point-in-time stock in a year when the exit run-rate was 29% above the annual average — but the FY2025 base it uses was itself moved by 2,189 with no explanation, and the same annual report disagrees with itself about which base is correct.
BASE-RATE: A realised loss exists and is small and traceable: 256 written off in FY2026, 452 in FY2025, 827 in FY2024, against gross books of 65,109, 36,991 and 23,928 — a write-off rate of 0.39%, 1.22% and 3.46%, falling. The cumulative three-year write-off of 1,535 is 0.6% of one year's PAT. The single-debtor ICCL provision of ~4,000 is the largest credit event in the window and it is provided, not written off.
S6 IMPLICATION: The earnings stream is not being flattered by uncollected revenue, so this line should not be carried into the earnings-quality gate as an accrual-manipulation candidate; what should be carried is the disclosure defect — a comparative moved without a note, and one note inside the same report contradicting two others. Monitorable: whether unbilled receivable stays near one month of the trailing quarter's revenue; a move above 1.3 months would separate timing from collection. Next check: Q2FY27 results, unbilled disclosure if given, otherwise the FY2027 annual report Note 10.5.
SEVERITY: Medium

### FINDING: The ₹3,919 lakh CDSL dividend is real cash and is fully traceable — in the standalone statements; the consolidated cash flow does not present it (RF-028 resolved)
S1 WHAT: Note 8's CDSL roll-forward records "Dividend received during the year (3,919)" reducing the carrying value from 41,949 to 44,940 `[AR FY26, Note 8, PDF p189/pr178]`. The consolidated cash flow shows "Dividend received 1" and "Investments in associates -", and its investing section sums to the reported (2,73,967) exactly, leaving no room for the 3,919 `[AR FY26, Consolidated Cash Flow, PDF p165/pr154]`.
S2 WHY: The dividend is received by BSE Limited, the parent. On consolidation, dividends from subsidiaries are eliminated; a dividend from an equity-accounted associate is not eliminated and should survive as an investing inflow. It has not been carried through — the consolidated statement deducts the full 6,542 share of associate profit from PAT as a non-cash item and then does not add back the cash actually received.
S3 EVIDENCE: The standalone settles it with an exact tie. Standalone investing shows "Dividend received from subsidiaries, associate and others 10,038" (7,350 at FY2025) `[AR FY26, Standalone Cash Flow, PDF p251/pr240]`, and standalone Note 23 splits dividend income as subsidiaries 6,118 + others 3,919 + mutual funds 1 = **10,038, exact** `[AR FY26, Standalone Note 23, PDF p286/pr275]`. The 3,919 is therefore cash, received, in the year, from CDSL. Counter-proportion: at the standalone the item is 39.0% of the dividend line (3,919 / 10,038); at the consolidated it should be 99.97% of it (3,919 / 3,920) once subsidiary dividends are eliminated, and it appears as 0%. The same pattern held in FY2025 — CDSL dividend 3,449, consolidated "Dividend received 1".
S4 CONNECTS: Both consolidated statements tie internally, so the 3,919 has been absorbed into another investing line — most plausibly netted against "Investment in fixed deposits (3,29,857)" or "Interest received 23,798", neither of which is disaggregated. The associates line is also where the group's only FY2026 impairment sits (100 on BFSI Sector Skill Council, fully provided) and where the FY2024 exceptional gain of 40,662 on the SEBI-mandated 5% CDSL divestment arose `[AR FY25, Note 52, PDF p211/pr200]` — a line that has produced a 40,662 gain, a 100 impairment and a lost 3,919 in three years.
DOMAINS: CashFlow, Notes, BalanceSheet, Governance
DISCONFIRM: Alternatives were tested. (i) That the dividend was non-cash or a stock dividend — refuted: standalone Note 23 books it as dividend income and standalone investing shows the cash. (ii) That it was received by a subsidiary and eliminated — refuted: standalone Note 8 shows BSE Limited holds all 3,13,50,000 CDSL shares directly. (iii) That it is inside consolidated "Dividend received 1" — refuted arithmetically; the line is 1. What cuts in favour of the company: the misclassification is between two lines of the same investing section in most readings, and total cash and closing balances are correct in both statements.
S5 MEANS: RF-028 resolves as a consolidated presentation defect rather than a missing cash flow — the money exists, the group received it, and the consolidated statement of cash flows does not show a reader where it went.
BASE-RATE: No loss, realised or otherwise, arises from this — 3,919 is 1.57% of PAT attributable and the cash is in the bank. The base rate that matters is preparation quality, and this is the third defect found in the same statement: the capital-advance split above, RF-027's unexplained 19,679 FY2024 CFO restatement, and this.
S6 IMPLICATION: Cash items in this group have to be verified against the standalone statements before being used, because the consolidated statement of cash flows has now failed three separate tie-out tests in one three-year window; the ₹100 map in W4_cash should be built from both blocks rather than from the consolidated alone. Monitorable: whether the FY2027 consolidated cash flow carries a "dividend received from associate" line. Next check: FY2027 annual report, consolidated investing section.
SEVERITY: Watch

### FINDING: 45.1% of the balance sheet is not the company's money, and the reported ROE understates the return on distributable shareholders' capital by 6.24 percentage points
S1 WHAT: Of FY2026 total equity and liabilities of 13,44,614, the company's own money and own obligations are 7,37,753 — 54.9%. The rest is members' and settlement money 3,72,416 (27.7%), restricted regulatory funds 1,59,665 (11.9%) and statutory amounts collected for the government 74,780 (5.6%). Two years earlier the own share was 42.2%.
S2 WHY: The shift is entirely in the numerator. Members' money is 3,72,416 against 3,75,164 at FY2024 — flat — while total equity rose 3,45,466 to 6,79,550 on retained profit of 2,49,698 in FY2026 alone against dividends of 31,585, a payout of 12.6%. The balance sheet did not become less levered on other people's money because the float shrank; it did so because shareholders' capital nearly doubled beside it.
S3 EVIDENCE: The classification ties exactly in all three years: `7,37,753 + 1,59,665 + 3,72,416 + 74,780 = 13,44,614`. The counter-proportion that makes it a finding rather than a share: **members' money is 27.7% of the funding side but the assets earmarked against it and the other restricted pools are 5,25,014, 39.0% of total assets** — the earmarked asset base is larger than the earmarked liability base by 9,926, 1.9%, and the narrow earmarked-others buffer has fallen from 10,258 at FY2024 to 922 at FY2026, a 91% reduction, on a liability that is essentially unchanged. On the equity side, 93,485 of the reported 6,79,550 is either non-controlling (12,249) or non-distributable by its own note (capital reserves 76,709, FCTR 4,437, LES 9, abeyance-earmarked general reserve 81), leaving distributable equity of 5,86,065.
S4 CONNECTS: ROE on average total equity is 43.75%; on average distributable equity it is 52.70%; stripping the after-tax income earned on members' float — 17,142 of *Treasury income from clearing and settlement funds* inside revenue, `17,142 x 0.7503 = 12,861`, 5.15% of PAT attributable — it is 49.99%. **The reported figure therefore understates the return on distributable shareholders' capital by 6.24pp**, the opposite direction to overlay §2's prediction, because BSE presents the Core SGF as a separate caption between equity and liabilities rather than inside equity `[AR FY26, Consolidated Balance Sheet, PDF p163/pr152]`. Management publishes 49.07% on a standalone total-equity basis `[AR FY26, MD&A, PDF p77/pr66]`, which happens to sit close to the correct consolidated figure for the wrong reason — the standalone excludes the NCI and the clearing subsidiary rather than the restricted reserves. Note 15.4 caps what can actually be declared at the parent's retained earnings of 4,55,828, 67.1% of consolidated equity `[AR FY26, Standalone Note 15, PDF p280/pr269]`.
DOMAINS: BalanceSheet, Notes, IncomeStatement, MgmtCommentary
DISCONFIRM: The strongest evidence against treating the restricted reserves as unavailable is that the capital reserve of 66,179 is restricted to "the operations of the Exchange" rather than being frozen — it funds the business, it simply cannot be distributed, so for a going concern the distinction affects dividend capacity more than economic return. Against the float-income adjustment: the treasury income of 17,142 is genuinely earned by the group's own risk management of the float and SEBI permits its recognition, so removing it entirely is the conservative bound rather than the right answer. And the direction of the net correction is favourable to the company, which is the opposite of what a sceptical prior would predict.
S5 MEANS: Return on assets is meaningless at this company in every year read, return on total equity understates the shareholders' return, and the only defensible equity denominators are distributable equity for economics and the parent's retained earnings for distribution capacity.
BASE-RATE: No loss has ever been charged against the restricted pools at this company — the Core SGF has grown in every one of the ten years in `balance_cash_10y.csv`, from 17,605 to 1,24,683, and no member default has been drawn against it. In the system the base rate is not zero: a settlement guarantee fund exists because clearing defaults have happened, and SEBI sizes it from monthly stress tests precisely because the loss it covers is tail-shaped rather than annual.
S6 IMPLICATION: The economics of this business are better than the reported consolidated ROE suggests and worse than the growth of total assets suggests, and both distortions run through the same disclosure — the float. Any valuation built on book value must use distributable equity of 5,86,065, not 6,79,550; any dividend-capacity assumption must use the parent's 4,55,828. Monitorable: the earmarked-others asset buffer, 922 at FY2026 against 10,258 at FY2024 — a negative reading would mean member obligations exceed the assets set aside for them. Next check: FY2027 annual report, Notes 11, 12 and 16.
SEVERITY: Medium

### FINDING: ₹16,993 lakh of member deposits sit inside the "Owned" bucket of Note 16 with no earmarked asset behind them
S1 WHAT: Note 16 splits current other financial liabilities into *Owned* (A) 24,992, *Earmarked* (B) 26,004 and *Clearing and settlement* (C) 3,55,423. Inside bucket (A), three lines are member money: deposits received from trading members 10,298, other deposits received from members 5,612 and other deposits 1,083 — together 16,993, **68.0% of the bucket the company calls Owned** `[AR FY26, Note 16, PDF p206/pr195]`.
S2 WHY: Notes 16.2 and 16.3 earmark bank balances and deposits against bucket (B) and against the unpaid-dividend line only. Bucket (A) carries no such footnote, so these deposits are funded from the group's general resources and the corresponding cash is inside the *Owned* pool in Notes 11 and 12 that Note 12.1 describes as "available for the operating activities of the Group". Members' refundable deposits are therefore financing the company's own working balances.
S3 EVIDENCE: 16,993 against total equity of 6,79,550 is 2.5%; against own-account liquid funds of 3,08,596 it is 5.5%. The counter-proportion is what makes it visible: bucket (B), at 26,004, is smaller than the member money hidden inside bucket (A) plus its corporate remainder, and (B) is fully asset-earmarked while (A) is not earmarked at all — the company earmarks assets against 26,004 of issuer and defaulter money but not against 16,993 of member money. The balance has been flat for three years — 16,999 / 16,381 / 16,993 — so it behaves as permanent funding rather than as a settlement balance. Management describes it in the same terms: "Other Financial Liabilities include member deposits of ₹14,401 Lakh, which are operational in nature and have remained relatively stable" `[AR FY26, MD&A, PDF p77/pr66]` — the standalone slice of the same item.
S4 CONNECTS: This is the same disclosure asymmetry that RF-003 identifies on the revenue side, where a 60-lakh auction-charge line is disclosed separately while 3,79,499 of transaction charges is one number. Here a 26,004 bucket is footnoted with its asset cover and a 16,993 member balance inside a bucket labelled "Owned" is not. It also matters for W4_capalloc: W1_ledger's own-account CFO estimate treated bucket (A) as owned and noted the sensitivity — stripping the (A) member movement as well moves FY2026 own-account CFO by 1,701, a 0.6% band, so the cash impact is small even though the classification point is not.
DOMAINS: Notes, BalanceSheet, MgmtCommentary, Governance
DISCONFIRM: The company's label is defensible on the substance: trading-member security deposits are long-dated, non-interest-bearing on the evidence available, and function economically as permanent capital for as long as the member remains a member — which is why the balance is flat across three years. There is no regulation cited anywhere in the report requiring these particular deposits to be segregated, unlike the (B) items which are held under specific SEBI direction. And the amount is small: 2.5% of equity. No evidence was found that any member has been unable to recover a deposit.
S5 MEANS: The word "Owned" in Note 16 is doing work the underlying balances do not support, and a reader taking the bucket labels at face value would put 16,993 of refundable third-party money on the company's side of the line.
BASE-RATE: Defaulters' liabilities of 1,555 and withheld liabilities of 2,969 in bucket (B) are the historical record that member money at this exchange does sometimes have to be returned or applied — those balances exist because members have defaulted. No realised loss to the company has arisen from the (A) deposits in any year read.
S6 IMPLICATION: Own-account working capital for this company — the overlay §5 replacement for the standard working-capital cycle — must exclude the 16,993 as well as buckets (B) and (C), which puts own-account current liabilities at 5,37,049 - 3,55,423 - 26,004 - 16,993 = 1,38,629 rather than 5,37,049. The classification does not change the cash conversion materially but it does change what "own-account" means in every later wave. Next check: FY2027 Note 16, whether an earmarking footnote is added to bucket (A).
SEVERITY: Watch

### FINDING: ₹3,05,992 lakh of CDSL value — 45.0% of total equity — is disclosed but never carried, and the disclosure settles a question management declined to answer
S1 WHAT: BSE holds 3,13,50,000 CDSL shares, 15.00%, carried at 44,940 under the equity method. The same note discloses "aggregate market value of quoted investments" of 3,50,932 (3,82,486 at FY2025) `[AR FY26, Note 8, PDF p188/pr177]`. The gap is 3,05,992.
S2 WHY: Ind AS 28 measures an associate at cost plus share of post-acquisition results; fair value never enters the carrying amount or profit or loss. The standalone carries the same holding at cost, 3,542 — so at the parent the unrecognised amount is 3,47,390, and the stake is carried at 1.0% of its market value.
S3 EVIDENCE: 3,05,992 is **45.0% of consolidated total equity** of 6,79,550 and 52.2% of distributable equity of 5,86,065. The counter-proportion is the direction of travel: the unrecognised amount **fell** from 3,40,537 at FY2025 (74.4% of that year's equity of 4,57,570) because CDSL's market value dropped 8.2% — implied `3,50,932 lakh / 3,13,50,000 shares = ₹1,119` per share against ₹1,220 — while BSE's own equity grew 48.5%. The earnings contribution is shrinking on both measures: share of profit 6,842 against 7,900, and as a share of PBT 2.0% against 4.7%. The cash return is the durable part and it is small against value: dividend 3,919, a yield of 8.7% on carrying value but 1.12% on market value.
S4 CONNECTS: W2_promise records this as open item J1 — an analyst asked "CDSL we have a sizable holding. Why it is not showing in the fair valuation gain?" on the Q2FY25 call; the MD did not answer and closed the questioner `[Q2FY25 Concall 19Nov2024]`. W2_promise named the settling document as "BSE FY26 annual report, note on investments in associates (quoted fair value of a listed associate)". **That document discloses it, and disclosed it in FY2025 too** — the answer was in the annual report before the question was asked. The stake reached 15.00% because SEBI directed a 5% divestment in FY2024, realising 51,597 and a 40,662 exceptional gain `[AR FY25, Note 52, PDF p211/pr200]`, so BSE's holding is regulator-capped and cannot be increased. W2_peers separately records that BSE and CDSL share a statutory auditor and that BSE nominates a CDSL director, which is why CDSL is a weak control in the peer set.
DOMAINS: Notes, BalanceSheet, MgmtCommentary, Governance
DISCONFIRM: Evidence against treating this as recoverable value. (i) SEBI caps a stock exchange's holding in a depository at 15%, so the stake cannot be built; whether it can be monetised further without direction is untested — the only precedent is a divestment SEBI required. (ii) Market value is a quoted price on a 15% block and a block of that size would not clear at the screen price. (iii) The value moved against the group in FY2026, falling 31,554 in twelve months, which is a reminder that the unrecognised amount is a two-way number. (iv) The equity-method carrying value is the accounting answer and it is correct; there is no misstatement here.
S5 MEANS: Book value understates the group's asset base by roughly 45% because one listed holding is carried at 12.8% of its market price, and the analyst's original question had a published answer in the annual report that management did not give on the call.
BASE-RATE: This holding has produced one realised gain and no realised loss: the FY2024 divestment of 5% returned 51,597 of cash against a carrying value implying a gain of 40,662, taxed at 3,910 — so the market-versus-carrying gap has been converted to cash once, at a price consistent with the disclosed market value. That is the strongest available evidence that the gap is real rather than notional.
S6 IMPLICATION: Any book-value-based measure for this group needs the CDSL stake restated to market or the group's asset base is understated by roughly 45% of equity; equally, any earnings-based measure should note that the associate contributes 2.0% of PBT and falling, so the value and the earnings tell opposite stories about the same asset. W2_promise item J1 can be closed as **answered by disclosure, unanswered by management**. Monitorable: CDSL's market value at each reporting date, disclosed in Note 8 annually. Next check: FY2027 annual report, Note 8 aggregate market value.
SEVERITY: Watch

### FINDING: The consolidated statements have omitted the CWIP and intangible-development ageing schedules for three consecutive years while the standalone carries both
S1 WHAT: Capital work-in-progress of 3,255 (4,073, 1,113 in the prior two years) and intangible assets under development of 4,420 (1,339, 338) appear on the face of the consolidated balance sheet **with no note reference at all**, and no ageing or completion schedule for either exists anywhere in the consolidated notes for FY2024, FY2025 or FY2026. The standalone carries both — CWIP ageing at Note 3.1 and IAUD ageing and completion at Note 6 `[AR FY26, Standalone Notes 3.1 and 6, PDF p264, p266-267/pr253, pr255-256]`.
S2 WHY: Schedule III to the Companies Act 2013 requires the ageing schedule in both the standalone and the consolidated financial statements. The consolidated block of the FY2026 report contains exactly two ageing schedules — trade receivables at Note 10.5 and trade payables at Note 20.1 — and neither covers capital work in progress `[W1_docmap.md §6 items 6 and 7]`.
S3 EVIDENCE: The gap is a compliance gap rather than an information gap, and the counter-proportion proves it: standalone CWIP is 3,235 of the consolidated 3,255, **99.4%**, and standalone IAUD is 3,922 of the consolidated 4,420, **88.7%** — so 99.4% and 88.7% of the missing schedules can be read in the same document, five pages further on. What the standalone schedules say is benign: all 3,235 of CWIP is under one year (4,051 of 4,073 at FY2025, with 22 in the 1-2 year bucket), 3,917 of 3,922 of IAUD is under one year, and the company states "there is no project whose completion is overdue or has exceeded its cost compared to its original plan" in both years. The residual that genuinely cannot be aged is 20 of CWIP and 498 of IAUD — 518 in total, 0.04% of total assets.
S4 CONNECTS: This is one of ten disclosures W1_docmap recorded as stopped or missing, and it belongs with the group of FY2026 removals: the SEBI regulatory-fee note gone, the buyback note gone, the Liquidity Enhancement Scheme note gone, the "of which remote" contingent-liability grading gone (RF-009), and the ₹10,60,000 inter-CCP guarantee gone (F1 above). The auditor's report is unmodified in all three years and CARO raises no clause on Schedule III presentation; the FY2026 CARO group table flags five entities on clauses 3(i)(c), 3(vii)(b) and 3(xvii), none of them on fixed-asset disclosure `[W1_docmap.md §1.5]`.
DOMAINS: Notes, BalanceSheet, Governance, Business
DISCONFIRM: The strongest evidence against grading this higher is that the information is present, in the same annual report, for 99.4% of the balance — so a reader loses almost nothing and the omission cannot be concealing an aged or stalled project. CWIP also **fell** in FY2026, 4,073 to 3,255, which is the opposite of the doctrine §2c pattern where capitalised cost accumulates; and the amounts are immaterial against total assets at 0.24% and 0.33%. Against the company: this is the third year running, so it is a settled practice rather than an oversight, and it sits inside a year in which four other consolidated disclosures were also withdrawn.
S5 MEANS: A required consolidated disclosure has been omitted three years running with no auditor or CARO remark, in a year the group tripled its capital expenditure — and the omission is only harmless because the reader can substitute the standalone, which is not a substitution the standard permits.
BASE-RATE: No loss and no restatement has arisen from this: the standalone schedules show no overdue or over-budget project in either year, and the PPE roll-forward reconciles exactly. The base rate that matters is the pattern — five consolidated disclosures withdrawn or absent in the FY2026 report, of which one (F1) was worth 1.56x equity.
S6 IMPLICATION: Capital-expenditure discipline can still be assessed here, but only by reading the standalone, and the reader should assume the consolidated block is the weaker of the two disclosure sets in this group. This raises the evidential weight that should be placed on the standalone statements throughout the remaining waves. Monitorable: whether the FY2027 consolidated block restores the two schedules. Next check: FY2027 annual report, consolidated Notes 3 and 6.
SEVERITY: Medium

---

## 6. Reconciliation status of every material balance

Doctrine §3 requires an explicit line for every material balance, traced or not.

| Balance, FY2026 | ₹ lakh | Opening-to-closing status |
|---|---|---|
| Total equity | 6,79,550 | **Reconciled exactly**, both halves — chain 1 L6 |
| Core SGF | 1,24,683 | **Reconciled**, residual 3,598 identified as fund income and penalties credited outside the P&L — chain 7 L6 |
| Other financial liabilities (current) | 4,06,419 | **Reconciled** to three named buckets, zero residual; asset cover ties to 1.9% — chain 2 |
| Trade receivables | 55,316 | **Reconciled**: allowance `6,024 + 4,025 − 256 = 9,793`; cash flow ties to 32 lakh (0.1%) — chain 3 |
| Investments | 3,30,043 | **Reconciled** to owned 3,05,686 + earmarked 24,357, zero residual — chain 4 |
| Cash and bank balances | 8,09,253 | **Reconciled** to owned 3,08,596 + earmarked 5,00,657, zero residual — chain 5 |
| PPE | 56,259 | **Reconciled exactly**, gross and accumulated depreciation — chain 6 L6 |
| CWIP + IAUD | 7,675 | Movements known; **ageing schedule absent from the consolidated** — F8 |
| Investments in associates | 53,657 | **Reconciled exactly**, associate by associate — chain 8 L6 |
| Trade payables | 13,087 | Ageing schedule present (Note 20.1); movement +1,691 ties to the cash flow exactly |
| Deferred tax (net) | 2,371 | **Reconciled**: `1,939 + 476 − 44 = 2,371` `[AR FY26, Note 18, PDF p207/pr196]` |
| Goodwill | 3,814 | **Reconciled**: gross `3,814 + 4 = 3,818` less impairment 4 = 3,814 |
| Other intangible assets | 4,122 | **Reconciled**: gross `18,730 + 2,470 − 12 + 39 = 21,227`; amortisation of 2,171 ties D&A to 15,896 exactly |
| Investment properties | 8 | **Reconciled**: gross `143 − 101 = 42`, depreciation `76 + 5 − 47 = 34` |
| Other liabilities (Note 19) | 95,445 | ISF reconciled (`7,523 + 5,386 + 671 − 4,654 = 8,926`); **statutory remittances of 74,780 have no sub-schedule** -> AR FY26 Note 19 gives one figure; the standalone MD&A identifies 51,478 of it as STT, leaving 23,302 unexplained |

**Unreconciled movements flagged:** (i) the 15,584 capital advance, F2; (ii) the 2,189 trade-receivable
comparative restatement, F3; (iii) the 10,60,000 guarantee, F1; (iv) the 3,919 CDSL dividend at the
consolidated level, F4; (v) the 23,302 residual inside statutory remittances, above.

---

## 7. Handover, and two positions recorded rather than resolved

1. **RF-008 — RESOLVED as a retrospective disclosure-basis change.** The FY2025 comparative was restated
   from 10,60,024 to 24, removing the ₹10,60,000 lakh ICCL inter-CCP collateral bank guarantee from both
   years with no explanatory note. Route to W3_notes and W6_governance; it is not a Watch, it is a High.
2. **RF-028 — RESOLVED.** The 3,919 is cash, disclosed in standalone Note 23 and the standalone cash
   flow (`6,118 + 3,919 + 1 = 10,038`), and absent from the consolidated statement of cash flows. Route
   the presentation defect to W3_notes.
3. **RF-026 — DOWNGRADE PROPOSED, High to Medium.** On Q4-annualised revenue, gross receivable days are
   38.0 against 37.5. The surviving finding is the unexplained 2,189 comparative restatement and the
   Note 34 / Note 10 contradiction inside the same report. **The downgrade is proposed, not applied** —
   RF-026 is W1_ledger's entry and this file does not overwrite it.
4. **RF-005 — one correction to W1_ledger's own-account CFO series, and it is material to single years
   only.** Stripping the misclassified capital advance gives FY2026 2,70,533 (conversion 1.093, not
   1.16) and FY2025 83,592 (0.635, not 0.52). **The three-year cumulative of 0.942 is unchanged.**
   For W4_cash.
5. **Overlay §2's stated direction is falsified for BSE and the overlay should be corrected.** The Core
   SGF sits outside equity, so removing restricted funds from the denominator RAISES ROE. The corrected
   rule: *at BSE, ROE on total equity understates the return on distributable shareholders' capital by
   6.24pp at FY2026 and 5.07pp at FY2025; the overlay's overstatement channel exists but runs only
   through the 17,142 of treasury income on members' float, worth 2.71pp.*
6. **W2_promise item J1 can be closed** — the quoted fair value of the CDSL stake is disclosed in
   consolidated Note 8 in both FY2025 and FY2026 as "aggregate market value of quoted investments",
   3,50,932 and 3,82,486. Management did not answer it on the call; the annual report did.
7. **Two W1_ledger positions are recorded against, not overwritten** (doctrine §10): (i) the inline
   display `1,55,712 + 1,93,114 + 1,51,688 = 5,00,657` omits the earmarked-SGF current account of 143 —
   the total is correct, the displayed decomposition is 143 short; (ii) W1_ledger treats Note 16 bucket
   (A) as owned, this file shows 68.0% of it is member money with no asset earmarked against it. Neither
   changes W1_ledger's conclusions.
8. **New gap-register entries** (doctrine §9): bank-deposit counterparty concentration on ₹8,09,253 of
   deposits (chain 5 L4); capital-expenditure counterparties on a 51,516 line (chain 6 L4); the
   sub-schedule to statutory remittances of 74,780; average or peak member margin (chain 2 L8);
   consolidated CWIP and IAUD ageing (F8).
