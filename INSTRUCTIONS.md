# EQUITY RESEARCH SYSTEM — MASTER INSTRUCTION FILE

**Version:** 1.0
**Universe:** Indian listed companies (NSE / BSE)
**Method:** Human-language document reading by specialised agents. **No code, no scripts, no parsers, no automated extraction.**
**Output:** Institutional-quality, evidence-linked company analysis.

> **Source note.** This is the owner's specification as written on 2026-09-07, preserved verbatim as the
> statement of intent. Where the working doctrine (`ANALYSIS_DOCTRINE.md`) departs from it — three
> stage-ordering corrections in §7 there — the departure is recorded, not applied silently. This file is
> not edited to match the doctrine; the doctrine explains itself against this file.
>
> **One clarification the owner has since issued, 2026-09-07.** Principle 1 below reads "No code."
> The ruling that governs: *be practical — do not write unnecessary code, because the analyst can do
> arithmetic; write code where it is genuinely required.* Extraction is still never code. Arithmetic is
> the analyst's by default, with code required on the five triggers in `ANALYSIS_DOCTRINE.md` §4a.

---

## 1. PURPOSE

Produce a company analysis that answers three questions in this order:

1. **Business:** What does this company actually do, and how does ₹100 of customer money travel through it?
2. **Numbers:** Is every reported number explainable, traceable to a real economic driver, and backed by cash?
3. **Trust:** Can management's numbers and words be trusted with minority shareholder capital?

Valuation comes last, and only if questions 1–3 are satisfactorily answered.

---

## 2. NON-NEGOTIABLE PRINCIPLES

1. **No code.** Every company's annual report has a different structure, note numbering, segment definition and disclosure depth. Code breaks on this. Agents read documents like an analyst does — with eyes and judgement. *(Clarified 2026-09-07: this binds **extraction** absolutely. For arithmetic, see the source note above and `ANALYSIS_DOCTRINE.md` §4.)*
2. **One agent = one job.** No agent is allowed to do the next agent's work. Each stage ends with a written handoff.
3. **Disclosure-bound.** Never invent a break-up. If the company has not disclosed something, write **`NOT DISCLOSED`** and log it. "Not disclosed" is itself a finding.
4. **Evidence tag on every number.** Format: `[AR FY25, Note 24, p.187]` or `[Q3FY26 Concall, CFO answer]` or `[Investor Presentation Feb-26, slide 14]`. A number without a source tag is rejected by QC.
5. **Estimates must be labelled.** If an agent derives a number, it must be marked `DERIVED` with the formula shown, and `ESTIMATE` if any judgement was used.
6. **Maximum available granularity, not artificial granularity.** Go as deep as disclosure allows. Do not manufacture depth.
7. **Story vs numbers consistency is the core test.** Whatever management claims in presentations/concalls must be verified against financial statements.
8. **Simplicity of process.** Fixed sequence, fixed templates, fixed handoffs. No agent redesigns the process mid-way.
9. **Nothing is deleted.** Contradictions, doubts, unanswered questions all stay in the file.

---

## 3. DATA SOURCES (STAGE 0 SCOPE)

**Primary (mandatory):**
- Annual Reports — last 5 years minimum, 10 years preferred (full report including Notes, MD&A, Board's Report, Corporate Governance Report, Related Party disclosures, Auditor's Report, Secretarial Audit)
- NSE / BSE corporate filings: quarterly results, shareholding pattern (quarter-wise), corporate announcements, board meeting outcomes, RPT disclosures under LODR Reg 23, insider trading (Reg 7) disclosures, pledge disclosures
- Concall transcripts and audio — last 8–12 quarters
- Investor presentations / quarterly earnings decks
- Postal ballot notices, AGM notices, AGM Q&A, voting results
- Subsidiary financials (where separately filed)

**Secondary (supporting):**
- Credit rating rationales (CRISIL / ICRA / CARE / India Ratings) — often disclose debt structure, covenants, group exposure
- Stock exchange clarifications, SEBI orders, NCLT filings, regulatory penalties
- DRHP / RHP / QIP placement documents (excellent business-model detail)
- Industry association data, peer company filings

**Source priority when numbers conflict:** Audited Annual Report > Audited quarterly filing > Unaudited quarterly filing > Concall statement > Investor presentation > Media.

**Rule:** Investor presentations are *marketing documents*. They are used to understand management's claims, never as the final source of a number.

---

## 4. AGENT ROSTER

Each agent below has: **Role → Inputs → Work → Output file → Done-criteria → Forbidden.**

### A0 — RESEARCH MANAGER (Orchestrator)
**Role:** Owns the sequence. Assigns work, receives handoffs, does not analyse.
**Work:** Runs the stage gate — an agent's output is only passed forward when its done-criteria are met. Maintains the master register.
**Output:** `00_Master_Tracker.md` — stage status, open questions, contradictions, pending data.
**Forbidden:** Writing any analytical conclusion.

### A1 — DATA LIBRARIAN
**Role:** Collects and organises every document from NSE/BSE and company site. No reading for meaning.
**Work:** Download, name, and file everything per convention. Flag missing years/quarters.
**Naming:** `COMPANY_DOCTYPE_PERIOD.pdf` → e.g. `PNB_AR_FY25.pdf`, `PNB_Concall_Q2FY26.pdf`
**Output:** `01_Source_Register.md` — table of every document with type, period, URL/filing date, pages, whether audited.
**Done when:** 5 (or 10) years of ARs, 8+ concalls, all shareholding patterns, all RPT filings are listed or explicitly marked unavailable.
**Forbidden:** Interpreting content.

### A2 — DOCUMENT MAPPER
*(this agent solves the "every company is structured differently" problem)*
**Role:** For each annual report, build a personal index of where things actually live in *that* company's report.
**Work:** Read the contents page and note structure, then record: which note number holds revenue break-up, which holds segment data, RPTs, contingent liabilities, employee cost, debt schedule, ageing tables, CWIP, subsidiary list, auditor's key audit matters, etc. Note year-on-year changes in note numbering, restatements, and change in segment/disclosure definitions.
**Output:** `02_Document_Map_FYxx.md` per year + `02_Structure_Change_Log.md`
**Done when:** Any later agent can locate any disclosure in under one minute.
**Forbidden:** Extracting or analysing numbers.

### A3 — BUSINESS UNDERSTANDING AGENT
**Role:** Explain the business **without using any financial number.**
**Work:** Answer: What does the company sell → to whom → what problem does it solve → how does it get paid → how does the product physically/commercially reach the customer → what must go right for the business to work. Map: Company → Product/Service → Customer → Distribution → Payment terms → Revenue recognition point.
**Output:** `03_Business_Understanding.md`
**Done when:** A non-finance reader understands the business in one page, and the 5–10 real business drivers are named.
**Forbidden:** Quoting financials, ratios, or valuation.

### A4 — INDUSTRY & VALUE CHAIN AGENT
**Role:** Place the company in its ecosystem.
**Work:** Map Supplier → Company → Channel → Customer. Assess supplier concentration, customer concentration, competitive intensity, entry barriers, substitutes, pricing power location in the chain, regulation, cyclicality, technology/disruption risk, import-export and duty structure.
**Output:** `04_Industry_Structure.md`
**Done when:** It is clear who in the value chain holds the pricing power, and why.

### A5 — BUSINESS MODEL & UNIT ECONOMICS AGENT
**Role:** Build the ₹100 economic engine and the single-unit economics.
**Work:** ₹100 revenue → cost layers → gross profit → opex → EBITDA → interest/tax → PAT. Then one-unit view: selling price, variable cost per unit, contribution per unit. Then split cost structure into variable vs fixed and state the operating leverage: "revenue +10% → EBITDA +x%; revenue −10% → EBITDA −y%."
**Output:** `05_Business_Model_Unit_Economics.md`
**Done when:** Operating leverage is quantified in both directions, and capital intensity is stated as "₹x of incremental capital employed per ₹1 of incremental revenue" over the last 5 years.

### A6 — REVENUE ENGINE AGENT
**Role:** Dissect revenue to the deepest disclosed level.
**Work:**
- Break-up by product, service line, segment, geography, channel, customer type (retail/enterprise/government), domestic vs export, related vs unrelated party
- Growth decomposition of the YoY change into: volume, price/realisation, mix, new products, acquisition, FX, one-offs. Where the company doesn't disclose split, state `NOT DISCLOSED` and show what *can* be inferred, labelled `DERIVED`.
- Segment-wise growth **and** segment margin — always together, because headline growth can come from the worst-margin segment
- Revenue quality test: Revenue growth % vs Receivables growth % vs Operating cash flow growth %. Any divergence gets escalated.
- Customer concentration and top-5 / top-10 dependence
**Output:** `06_Revenue_Postmortem.md`
**Done when:** Every rupee of revenue growth is attributed to a named driver or explicitly marked unexplained.

### A7 — COST ENGINE AGENT
**Role:** Same treatment for every cost line.
**Work:**
- COGS → raw material, power & fuel, freight, job work, stores & spares, purchase of traded goods; link to commodity prices and volumes
- Employee cost → salaries, bonus, ESOP charge, PF/gratuity; against headcount, cost per employee, senior hiring, attrition. Compare employee cost growth vs headcount growth vs revenue growth.
- Other expenses → advertising, freight outward, rent, professional/consultancy fees, travel, CSR, provisions, "miscellaneous". **Any large or fast-growing "Others" or "professional fees" line is a flag for A11/A13.**
- Finance cost → instrument-wise, rate, lease interest, capitalised interest, forex component
- Other income → interest, dividend, fair-value gains, asset sale gains, forex, government incentives; separate recurring from non-recurring
- Tax → effective rate vs statutory, deferred tax, exceptional tax items
**Output:** `07_Cost_Postmortem.md`
**Done when:** Each cost line is tied to a physical/commercial driver, and margin change is explained by named cost buckets, not by "operational efficiency."

### A8 — P&L LINE-BY-LINE AGENT
**Role:** Apply the standard 8-step dissection to every P&L line in fixed sequence.
**Sequence:** Revenue → COGS → Gross Profit → Employee Cost → Other Operating Expenses → EBITDA → D&A → EBIT → Finance Cost → Other Income → PBT → Tax → PAT → EPS → OCI → Exceptional/discontinued items.
**Output:** `08_PL_Line_Analysis.md`
**Done when:** No line is left as a headline number.

### A9 — BALANCE SHEET AGENT
**Role:** Same 8-step dissection, asset and liability side.
**Work:**
- Receivables → ageing, overdue buckets, provision, customer concentration, subsequent collection, related-party receivables
- Inventory → RM / WIP / FG split, days, ageing, write-downs, valuation policy
- PPE → opening + capex − depreciation − disposals = closing; plus CWIP ageing and long-pending projects
- Intangibles & goodwill → acquisition-wise origin, impairment testing assumptions, capitalised development cost
- Investments → entity-wise, quoted/unquoted, valuation basis, related parties
- Loans & advances given → to whom, rate, security, recoverability
- Debt → lender-wise, secured/unsecured, maturity ladder, rate, currency, covenants, guarantees given
- Payables → days, ageing, supplier financing / bill discounting arrangements
- Other assets/liabilities, contingent liabilities, off-balance-sheet items
**Output:** `09_Balance_Sheet_Analysis.md`
**Done when:** Every material balance is reconciled opening-to-closing, and every unreconciled movement is flagged.

### A10 — CASH FLOW & CASH CONVERSION AGENT
**Role:** Build the full source-to-destination map.
**Work:**
- CFO bridge: PAT → non-cash adjustments → working capital changes (receivables/inventory/payables/other) → tax paid → CFO. Compare CFO vs EBITDA and CFO vs PAT for 5–10 years cumulatively, not just one year.
- Capex: maintenance vs growth, project-wise where disclosed, CWIP movement, actual cash paid vs capex announced
- Financing: new debt, repayment, equity issuance, buyback, dividends, interest paid
- Working capital cycle: inventory days + receivable days − payable days
- Final ₹100 map: `₹100 revenue → costs → operating profit → interest & tax → PAT → working capital → CFO → capex → FCF → debt repayment / dividend / buyback / acquisition / cash balance`
**Output:** `10_Cash_Map.md`
**Done when:** The ₹100 journey is shown end-to-end and cumulative 5–10 year CFO/PAT conversion is stated.

### A11 — NOTES & DISCLOSURE FORENSICS AGENT
**Role:** Hunt in the Notes to Accounts, where the real information hides.
**Work:** Read every note. Focus on accounting policies and any change in them, revenue recognition policy, capitalisation policy, provisioning and impairment assumptions, contingent liabilities, litigation, commitments, guarantees, restatements, prior-period items, ageing tables, unusual disclosures, the Companies (Audit) additional disclosures (loans to promoters/related parties, benami, crypto, undisclosed income, wilful defaulter, funds routed through intermediaries, etc.), and CARO observations.
**Output:** `11_Notes_Forensics.md` + `11_Accounting_Policy_Change_Log.md`
**Done when:** All policy changes across years are logged with quantified P&L/BS impact where disclosed.

### A12 — EARNINGS QUALITY AGENT
**Role:** Judge how trustworthy the profit number is.
**Work:** Accrual vs cash profit, revenue recognition aggressiveness, one-off and "exceptional" item frequency, provisioning adequacy and reversals, capitalisation of expenses, depreciation rates and life changes vs peers, other-income dependence, tax rate anomalies, subsidiary vs consolidated profit gap, standalone vs consolidated divergence, related-party contribution to profit.
**Output:** `12_Earnings_Quality.md` with a verdict: **High / Moderate / Low / Cannot be relied upon** — plus the specific reasons.

### A13 — CORPORATE GOVERNANCE AGENT
**Role:** Run the full 12-point governance framework.
**Work:**
1. **Board** — independent director count and genuine independence, Chairman/CEO separation, attendance, tenure, expertise fit, other directorships, resignations and reasons, committee composition, whether the board actually challenges management
2. **Promoter** — holding trend, pledge history, remuneration, other business interests, alignment with minority shareholders
3. **Related Party Transactions** — purchases/sales, loans/advances, guarantees, rent, management/royalty fees, investments, asset transfers; test arm's-length, recurrence and economic logic
4. **Remuneration** — MD/CEO/CFO pay, variable pay, ESOPs, promoter pay vs profit/ROE trend, pay vs peers, pay-for-performance linkage
5. **Auditor** — identity, tenure, rotation, qualified opinion / emphasis of matter / key audit matters, internal control observations, resignation and stated reason, audit vs non-audit fees
6. **Accounting quality** — hand-off from A12
7. **Capital allocation** — hand-off from A15
8. **Subsidiaries & group structure** — count, loss-makers, inter-company loans, guarantees, fund flow direction, unusual investments, step-down layers
9. **Shareholder treatment** — preferential allotments, warrants, dilution, rights issues, buybacks, dividend policy, promoter-favourable terms
10. **Transparency** — disclosure speed for bad news vs good news, concall behaviour on difficult questions, quality of risk factors, guidance withdrawal
11. **Regulatory & legal history** — SEBI/RBI/NCLT/ED/CBI/tax actions, penalties, litigation, fraud allegations, insider trading matters. *One isolated minor penalty ≠ bad governance. Look for pattern.*
12. **Track record** — handed to A16
**Output:** `13_Governance.md`
**Mandatory summary:** the 5-bucket table — Board (who challenges management?), Promoter (aligned with minority?), Transactions (where is the money going?), Accounting/Audit (are the numbers trustworthy?), Track Record (does management do what it says?).
**Mandatory quick screen (the 8):** promoter pledge → RPTs → auditor qualification/resignation → promoter remuneration → board independence → subsidiary transactions → accounting quality → promises vs actual outcomes.
**Standing rule:** "Good governance" ≠ "good investment." The purpose of this stage is only to establish **how much trust the numbers deserve** and **how management behaves with minority capital.**

### A14 — RELATED PARTY & GROUP STRUCTURE AGENT
**Role:** Deep-dive specialist reporting into A13.
**Work:** Build the full group tree (promoter → holdco → subsidiaries → step-downs → associates → JVs → promoter-owned private entities). Tabulate every RPT across 5–10 years by counterparty, nature, amount, and pricing basis. Trace fund flow direction. Identify any entity where money goes in but nothing comes back.
**Output:** `14_Group_Map_and_RPT_Ledger.md`

### A15 — CAPITAL ALLOCATION AGENT
**Role:** Judge what management did with shareholders' money.
**Work:** 5–10 year cumulative sources and uses of cash. Every major capex and acquisition tracked against announced cost, timeline and promised return vs delivered return. Incremental ROCE on incremental capital employed. Dividend/buyback rationale. New business ventures and their outcome.
**Central question:** Did management convert ₹1 into more than ₹1 of value, or destroy it?
**Output:** `15_Capital_Allocation.md`

### A16 — MANAGEMENT CREDIBILITY AGENT (Promise vs Delivery)
**Role:** The concall accountability tracker.
**Work:** From 8–12 quarters of concalls and presentations, extract every specific management claim with date, then mark against actual outcome: **Delivered / Partly delivered / Missed / Quietly dropped.** Cover guidance on revenue and margin, capex amount and commissioning date, debt reduction, ROE/ROCE targets, subsidiary turnaround, "no dilution" statements, new product launches, order book conversion.
**Output:** `16_Promise_vs_Delivery.md` with a hit-rate.
**Also flag:** vocabulary changes, disappearance of previously disclosed metrics, and refusal patterns on specific analyst questions.

### A17 — PEER BENCHMARKING AGENT
**Role:** Put every conclusion in relative context.
**Work:** 3–5 closest listed peers. Compare growth, margin, working capital days, capital intensity, ROCE, leverage, tax rate, depreciation policy, disclosure quality, promoter pay, RPT intensity. Same period, same definitions — state definitional differences.
**Output:** `17_Peer_Comparison.md`

### A18 — RED FLAG CONSOLIDATOR / DEVIL'S ADVOCATE
**Role:** Collect every flag raised by every agent and argue the bear case.
**Work:** Single register: flag, source agent, evidence tag, severity (**Critical / High / Medium / Watch**), whether management has explained it, and what would resolve it. Then write the strongest possible bear case and the specific conditions under which the investment thesis breaks.
**Output:** `18_Red_Flag_Register.md` + `18_Bear_Case.md`
**Escalation rule:** Any **Critical** flag — auditor resignation with unexplained reason, unexplained RPTs, repeated CFO/PAT divergence, promoter pledge stress, regulatory fraud action — pauses the process and goes to A0 before valuation begins.

### A19 — VALUATION AGENT
**Role:** Value the business only after trust is established.
**Precondition:** A12 verdict is not "Cannot be relied upon," and no unresolved Critical flag.
**Work:** Value from the drivers already established, not from broker consensus. Show base/bear/bull with the driver assumptions visible. State explicitly what the current market price is implying about growth, margin and capital efficiency, and whether the earlier stages support that.
**Output:** `19_Valuation.md`
**Forbidden:** Any recommendation language, target price presented as certainty, or valuation of numbers that A12 flagged as unreliable.

### A20 — REPORT WRITER
**Role:** Assemble the final document. Adds no new analysis.
**Output:** `20_Final_Report.md` — structure in Section 8 below.

### A21 — QUALITY CONTROL & FACT CHECKER
**Role:** Final gate. Adversarial.
**Work:** Sample-check numbers against source documents. Reject any untagged number, any unlabelled estimate, any conclusion without evidence, any place where an agent stepped outside its role, and any internal contradiction between files.
**Output:** `21_QC_Report.md` — Pass / Rework, with specific rework items.
**Rule:** The report cannot be released without QC pass.

---

## 5. STANDARD 8-STEP DISSECTION TEMPLATE

Every financial line item, in every agent's output, uses exactly this format:

```
LINE ITEM: __________              PERIOD: FY__      SOURCE: [tag]

1. REPORTED NUMBER      What exactly did the company report?
2. BREAK-UP             Which components make up this number? (deepest disclosed level)
3. SOURCE / DRIVER      Where did it come from? Product / customer / geography /
                        segment / asset class / counterparty
4. YoY MOVEMENT         Why did it increase or decrease? Quantify each reason.
5. CROSS-STATEMENT      Where does this show up in P&L, Balance Sheet and Cash Flow?
   LINKAGE              Do the three agree?
6. ACCOUNTING           How much discretion does management have in recognising or
   TREATMENT            measuring this? Which policy applies? Did the policy change?
7. QUALITY /            Recurring or one-off? Cash-backed or accrual? Core business
   SUSTAINABILITY       or peripheral? Can it repeat next year?
8. RED FLAGS &          What looks odd, and exactly which note / filing / concall
   VERIFICATION         answer will confirm or kill the doubt?
```

**Flow to always follow:**
`Financial Statement → Line Item → Sub-line → Economic source → Counterparty/driver → Accounting treatment → Cash movement → Sustainability → Governance implication`

---

## 6. MASTER SEQUENCE (STAGE GATES)

```
Stage 0   A1  Data collection
Stage 1   A2  Document mapping
Stage 2   A3  Business understanding        <- no numbers allowed
Stage 3   A4  Industry & value chain
Stage 4   A5  Business model & unit economics
Stage 5   A6  Revenue engine
Stage 6   A7  Cost engine
Stage 7   A8  P&L line-by-line
Stage 8   A9  Balance sheet
Stage 9   A10 Cash flow & Rs.100 map
Stage 10  A11 Notes forensics
Stage 11  A12 Earnings quality              <- GATE: trust verdict
Stage 12  A14 Group structure & RPT ledger
Stage 13  A15 Capital allocation
Stage 14  A16 Promise vs delivery
Stage 15  A13 Corporate governance          <- consumes A12, A14, A15, A16
Stage 16  A17 Peer benchmarking
Stage 17  A18 Red flags + bear case         <- GATE: critical flags stop here
Stage 18  A19 Valuation
Stage 19  A20 Report writing
Stage 20  A21 QC
```

**Governing principle:** Understand the business without numbers → understand the numbers through the business → then test business and numbers against each other for consistency. If management says "premium product, pricing power" but realisation is flat and gross margin is falling, the story and the numbers are in conflict — and that conflict is the finding.

---

## 7. SECTOR OVERLAYS

The standard template is built for an industrial/product company. Some sectors need the revenue engine redefined. The overlay agent is inserted between Stage 4 and Stage 5.

### A6-B — BANK / NBFC OVERLAY (e.g. PNB)
A bank's "revenue" is fundamentally different, so trace the earnings engine instead:

- **Interest income** → advances (segment/product-wise: corporate, MSME, agri, retail, housing, vehicle, gold) + investment book (HTM/AFS/HFT) + RBI and interbank balances → yield on each
- **Cost of funds** → CASA vs term deposits, bulk vs retail, borrowings, refinance → cost of each
- **NII and NIM** → yield minus cost, on average earning assets; disclose whether calculated on average or period-end
- **Fee & other income** → loan processing, guarantees, LC, remittances, cards, third-party distribution (insurance/MF), forex, transaction banking, treasury gains (separate trading gains from core fees)
- **Asset quality** → GNPA/NNPA by segment, slippages, upgrades, recoveries, write-offs (technical vs actual), PCR, restructured book, SMA-0/1/2, security receipts, ARC sales, divergence reported after RBI inspection
- **Provisions** → standard assets, NPA, restructuring, investment depreciation, other contingencies; provision write-backs
- **Capital** → CET1, Tier 1, CRAR, RWA density, capital raise history and dilution
- **Governance additions** — government/PSU ownership dynamics, board appointment process, RBI inspection observations and divergence disclosures, priority sector obligations, employee cost and pension/wage revision provisions

Every major P&L line must be traced back to the balance-sheet asset or liability that generated it.

*(Create similar overlays as needed: NBFC/HFC, insurance, real estate percentage-completion, pharma with USFDA and ANDA pipeline, IT services with headcount/utilisation/billing rates, capital goods with order book and execution, commodities with spreads and realisation.)*

---

## 8. FINAL REPORT STRUCTURE

1. What the company does — one page, no numbers
2. Industry structure and where pricing power sits
3. Business model, ₹100 engine, unit economics, operating leverage
4. Revenue post-mortem — break-up and growth attribution
5. Cost post-mortem and margin explanation
6. P&L line-by-line findings
7. Balance sheet findings
8. Cash flow and the full ₹100 source-to-destination map
9. Earnings quality verdict with reasons
10. Capital allocation scorecard
11. Promise vs delivery scorecard
12. Corporate governance — 12 points, 5-bucket summary, 8-point quick screen
13. Peer comparison
14. Red flag register with severity
15. Bear case and thesis-breakers
16. What is not disclosed (the gap register)
17. Questions to ask management on the next concall
18. Valuation — base/bear/bull with visible assumptions
19. Monitorables — the 5–10 things that must be tracked, and what each would signal

> *Editorial note: item 19 was truncated in the source paste ("Monitorables — the 5–10") and has been
> completed to its evident intent. Correct it if the intent was different.*

---

## 9. LATER OWNER DIRECTIVES (2026-09-07)

Two directives were added after the roster above was written. Both are load-bearing and both are
implemented in `ANALYSIS_DOCTRINE.md`.

**Directive 1 — the traceability chain.** Every material financial-statement line must be traced from
reported aggregate → disclosed components → underlying economic driver → counterparty/product/geography/
segment where available → accounting recognition → balance-sheet consequence → cash consequence →
sustainability.

*(This supersedes the §5 "flow to always follow" by inserting **balance-sheet consequence** as a distinct
step between accounting treatment and cash movement. See `ANALYSIS_DOCTRINE.md` §2a for why.)*

**Directive 2 — interpretation, not reproduction.** The objective is not to collect or reproduce
financial information that is already available in the Annual Report. The objective is to **interpret the
evidence and reach investment-relevant conclusions.**

Do not stop at reporting numbers, calculating ratios, or describing individual line items. **Connect facts
across the Business, Income Statement, Balance Sheet, Cash Flow, Notes, Management commentary, Governance,
and Industry context.**

For every important observation, answer:

**What happened → Why did it happen → What evidence supports it → How does it connect with other evidence
→ What does it mean → What is the investment implication?**

The analyst's primary job is **interpretation, not calculation**. Calculations and ratios are evidence;
**the conclusion derived from them is the output.**
