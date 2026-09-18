# Analysis doctrine — how this firm reads a financial-statement line

**Location note.** This file lives in the `equity-research-system` project. Every relative path it
cites (`CLAUDE.md`, `src/firm/...`, `docs/...`, `agents/...`, `verify/...`, ADR numbers) refers to the
**implementation repository** at `~/Desktop/equity reserch`, which this project does not modify.

**Status:** standing methodology, owner-directed 2026-09-07. Subordinate to `CLAUDE.md`'s seven laws;
where this file and a law appear to disagree, the law wins and the disagreement is a bug in this file.
Companion documents: `docs/BANK_ANALYSIS_DOCTRINE.md` (the lender overlay and the seven-rung dig
ladder), `docs/FORENSIC_METHODOLOGY.md`, `docs/REPORT_ARCHITECTURE.md`, `CLAUDE.md` §"Source
discovery" (the source-of-record rule this implements).

**Provenance of this document.** It is the general-company counterpart to the bank doctrine, written
from the owner's specification of 2026-09-07. §4 records the one place where it does **not** follow that
specification literally, and why; that deviation is flagged for owner sign-off and is not yet settled.

---

## 1. The objective — interpretation, not reproduction

**The objective is not to collect or reproduce financial information that is already available in the
annual report. The objective is to interpret the evidence and reach investment-relevant conclusions.**

Do not stop at reporting numbers, calculating ratios, or describing individual line items. **Connect
facts across the Business, Income Statement, Balance Sheet, Cash Flow, Notes, Management commentary,
Governance, and Industry context.**

**The analyst's primary job is interpretation, not calculation. Calculations and ratios are evidence;
the conclusion derived from them is the output.**

This is not new to the repo — it is the bank doctrine's *"a fact is not a conclusion"* (Rule 4) and its
*"data print"* standard, promoted out of the lender overlay and made general. It also runs with the
grain of §4: arithmetic is the cheap part and it is not the deliverable. **An agent that spends its
output restating numbers the reader could add up has added nothing.**

### 1a. The six steps

Every important observation is carried through all six, in order:

| Step | Question | Fails when |
|---|---|---|
| **S1** | **What happened?** | Stated as a ratio rather than as an event |
| **S2** | **Why did it happen?** | Answered with a restatement of S1, or with "efficiency", "mix", "growth" — words that are not mechanisms. Also fails on *"the company chose to"* without asking what the rule, incentive or constraint permitted |
| **S3** | **What evidence supports it?** | Evidence is untagged, single-source, not sized in ₹, or **sized but not shaped** (§1a-i) |
| **S4** | **How does it connect with other evidence?** | Fewer than three domains touched (§1b), no disconfirming evidence sought, or a compensating control named without **the class of error it cannot catch** |
| **S5** | **What does it mean?** | A summary of S1–S4 rather than a judgement that goes beyond them, or significance asserted **without the base rate** (§1a-ii) |
| **S6** | **What is the investment implication?** | Absent, or crosses into recommendation (§1c) |

S5 and S6 are distinct and both are required. *"Receivable days rose because the company is funding a
single related distributor"* is S5. *"Reported earnings overstate distributable cash by roughly one
year's PAT, so the multiple the market is paying is on a number that has never converted"* is S6.

**Three requirements absorbed from the retired dig ladder (§1e).** These are not optional colour; each
was load-bearing there and each is now a condition on a step above.

**(i) S3 must be shaped, not only sized — the asymmetry test.** *The shape of a number is usually the
finding.* A share given alone is half an observation; the finding is in the disproportion between two
shares of the same population. The lender example: an unaudited branch set holding **56.92% of deposits
but 25.01% of advances**, and **52.50% of interest expense against 19.32% of interest income** — the
disproportion is what identifies them as deposit-gathering units and moves the loss channel off credit
entirely. Neither share alone says that.

> S3 fails when a proportion is stated without the counter-proportion that reveals its composition.

This is asked **inside one disclosure**, which is what distinguishes it from S4's cross-domain
connection.

**(ii) S5 must carry the base rate — has it ever cost money?** Before significance is asserted, ask
whether the pattern has ever produced a **realised loss** — at this company or in the system. Fraud by
ticket and type, divergence history, whether the company's own past episode ran through the channel now
being discussed. This is what separates a demonstrated risk from a theoretical one, and it is the house
standard *"state the base rate first"*.

> S5 fails when it asserts that something matters without establishing whether it has ever mattered.

**(iii) Every step has a stopping rule.** S1–S6 previously said nothing about a step that cannot be
answered, which left "unanswerable" and "unasked" looking identical.

- A step answered **"unknown" must name the document that would answer it**, and where that document
  lives. An unnamed unknown is an unasked question.
- A step answered from a news site or aggregator is marked **`SECONDARY`** and **cannot alone carry the
  conclusion**.
- When **two consecutive steps are unanswerable**, the item ships as a **disclosure gap** — a finding in
  its own right at minimum severity **Medium**, routed to the gap register (§9). A gap that prevents
  sizing is a finding about the filing, not an absence of one.

### 1b. The cross-domain rule — the checkable part of S4

The eight domains are: **Business · Income Statement · Balance Sheet · Cash Flow · Notes · Management
commentary · Governance · Industry.**

> **A finding must connect evidence from at least three domains, and at least one of those must be
> non-statement** — Business, Management commentary, Governance, or Industry.

A claim supported inside a single domain is an **observation**, not a finding, and it does not ship as
one. Two statement domains alone is usually just one traceability chain (§2) and is already covered
there; the non-statement requirement is what forces the story-versus-numbers test that the whole method
exists to run. Every finding names the domains it connected — QC checks the count, not the prose.

Disconfirming search is mandatory (`agents/_shared/epistemics.md`): S4 is not complete until evidence
that cuts the other way has been looked for and either found or explicitly recorded as absent.

### 1c. What "investment implication" may and may not say

S6 is mandatory, and it is bounded. `CLAUDE.md` forbids buy/sell/hold output and the firm never emits
"buy this" — but the §6 return-potential question (*can this compound 5–10× over 5–8 years,
self-funded, under honest management?*) is a mandatory section of every report. S6 exists to feed it.

| Permitted | Forbidden |
|---|---|
| What it does to the **durability** of the earnings stream | Buy / sell / hold, in any phrasing |
| What it does to the **value or quality of the asset base** | A target price presented as certainty |
| The **margin of safety** it requires, and why | Position sizing, timing, or entry levels |
| How it moves the **base / bear / bull driver assumptions** | Any implication drawn from a number the earnings-quality gate rated unreliable |
| A **monitorable** with a named trigger and a next-check date | |
| A **thesis-breaker** — the condition under which the case fails | |
| What the **current price is implying**, and whether the evidence supports it | |

### 1d. Reasoning path versus write-up form

S1–S6 is **how the analyst thinks**. The bank doctrine's five parts — exposure, mechanism, size in ₹ and
as % of PAT, mitigant, falsifier — are **how the finding is written**. They are not competing templates:

`exposure` ← S1+S3 · `mechanism` ← S2 · `size` ← S3 · `mitigant` ← S4 · `falsifier` ← S6

Both remain in force. A finding that reasoned through six steps and ships without a size or a falsifier
still does not ship.

### 1e. Two frameworks, not three — the dig ladder is superseded

**Owner decision, 2026-09-07: if the seven-rung dig ladder contains no genuinely unique analytical step,
supersede it and make S1–S6 the single master framework.**

It was checked rung by rung against S1–S6. Five of the eight rungs mapped cleanly and added nothing:

| Rung | Absorbed by |
|---|---|
| 0 — what does the filing say | S1 |
| 1 — why is it so | S2 (with its *"what the rule permits"* sharpening now an S2 failure condition) |
| 2 — how much | S3 |
| 4 — what else looks at it | S4 (with *"what class of error it cannot catch"* now an S4 failure condition) |
| 5 — is this normal | S4, via the Industry and peer domains |
| 7 — so what | S5 + S6 |

**Three did not map, and have been absorbed as explicit conditions rather than lost:** rung 3
(asymmetry) → §1a-i, rung 6 (base rate) → §1a-ii, and the ladder's stopping rules → §1a-iii.

With those absorbed, **the ladder holds nothing S1–S6 does not.** It is retired. Two frameworks remain,
and they are orthogonal — each owns a different object:

| Framework | Object | Motion | Output |
|---|---|---|---|
| **Chain L1–L8** (§2) | One line item | Vertical, across statements | Evidence, with link states |
| **Six steps S1–S6** (§1a) | One observation, many facts | Horizontal, across domains | A finding |

Chains feed findings: a finding's S3 cites chain records, and a `BROKEN` chain (§2c) is the commonest
seed of one.

**S1–S6 now governs lenders too.** The bank overlay keeps everything that is genuinely
sector-specific — the reading order of a bank's annual report, the earnings-engine trace, the danger
ladder, the five-part write-up form of §1d — and loses only its parallel reasoning ladder.

> **Pending edit outside this project.** `docs/BANK_ANALYSIS_DOCTRINE.md` §2c lives in the
> implementation repo at `~/Desktop/equity reserch`, which this project does not modify. Retiring §2c
> there — replacing it with a pointer to §1a here — is an edit for that repo's own session. Until it is
> made, that file still carries the ladder and the two documents disagree.

### 1f. Consequences for the report

- **Sections lead with the conclusion**; evidence is subordinate to it. A section ordered by statement
  sequence buries its own output.
- **Findings are ranked by materiality to the investment case**, never by where they sit in the
  financial statements.
- **A table not followed by the conclusion it supports is a data print** and does not ship. This is the
  bank doctrine's existing standard, applied generally.
- Reproduction of what the annual report already states is permitted only as the evidence line under a
  conclusion — never as a section of its own.

---

## 2. The traceability chain

**Every material financial-statement line must be traced from reported aggregate → disclosed components
→ underlying economic driver → counterparty/product/geography/segment where available → accounting
recognition → balance-sheet consequence → cash consequence → sustainability.**

That sentence is the evidence-gathering method. §1 is what the evidence is *for*. The rest of this
section makes each link testable, so that a chain can be checked by someone other than the analyst who
wrote it.

A line item is not analysed until a chain record exists for it. Eight links, always in this order, each
one individually resolvable and individually falsifiable:

| Link | Name | The question it answers | Fails when |
|---|---|---|---|
| **L1** | Reported aggregate | What exactly did the company print on the face of the statement, in what unit, mapping to which schedule or note? | A number is quoted without its scale (`₹ in lakhs` / `Rs.000's omitted`) or without the note it ties to |
| **L2** | Disclosed components | What is the deepest break-up the company **actually publishes**? Do the components sum to L1? | Components don't tie and the residual is not named |
| **L3** | Economic driver | What physical or commercial quantity moves this? Volume × realisation, headcount × cost per head, average balance × yield, tonnes × spread | The driver is stated as "operational efficiency", "growth", "better mix" or any other word that is not a quantity |
| **L4** | Counterparty / product / geography / segment | Who or what is on the other side, and where does it sit? Related or unrelated party, domestic or export, which segment, which customer tier | Disclosure exists and was not read |
| **L5** | Accounting recognition | Which policy governs when and at what amount this enters the books? How much discretion does it give management? Did the policy change this year? | A policy change is present and unquantified |
| **L6** | Balance-sheet consequence | What asset or liability does this line create, consume, or leave behind? | The line is treated as if it lived only in the P&L |
| **L7** | Cash consequence | Where does this appear in the cash flow statement, and did it convert? | Accrual and cash are not compared over a multi-year window |
| **L8** | Sustainability | Recurring or one-off? What must stay true next year for it to repeat? | Answered as a forecast rather than as a condition |

### 2a. Why L6 is a separate link

The owner's earlier formulation ran accounting treatment straight into cash movement. **L6 is inserted
deliberately between them, and it is the highest-yield link in the chain.** Accrual manipulation does
not hide in the P&L and it does not hide in the cash flow statement; it hides in the balance-sheet
residue between them. Revenue that grew, receivables that grew faster, cash that never arrived is a
three-link reading — L1 up, L6 up more, L7 flat — and no two of those three links alone detect it.

The same shape recurs across the statement: profit with rising inventory, margin with rising CWIP,
other income with rising unquoted investments, cost savings with rising payables. In each case the
finding is the **gap between L6 and L7**, not either one.

### 2b. Link states

Every link carries exactly one state. The states are the output, not bookkeeping.

- **`TRACED`** — read from a filing, with an evidence tag (§5).
- **`NOT DISCLOSED`** — the company does not publish it. Never inferred silently, never left blank.
  Goes to the gap register (§9) and generates a question for the next concall. *A disclosure gap is a
  finding about management, and it is graded: a gap the peer set discloses is a stronger finding than a
  gap nobody discloses.*
- **`DERIVED`** — computed from `TRACED` inputs, **with the arithmetic shown inline**, not just the
  result. Who computes it is decided by §4: the analyst by default, code where §4 requires it.
- **`ESTIMATE`** — a `DERIVED` value where judgement entered an assumption. States the assumption and
  the range it moves over.
- **`BROKEN`** — the links contradict each other.

### 2c. A broken chain is the deliverable, not a defect

**When links contradict, the contradiction is the finding.** It is never smoothed over, never averaged,
never resolved by preferring the more flattering link. A `BROKEN` state routes to the red-flag register
at minimum severity **High**, and it is written in the five-part form of §1d.

The four breaks worth naming explicitly, because they recur:

1. **L1 ≠ ΣL2.** Components do not sum to the aggregate. Either a component is undisclosed (→ `NOT
   DISCLOSED`, sized as a residual) or a component is misstated.
2. **L3 contradicts L1.** Management says realisation rose; revenue per unit is flat. Story and numbers
   in conflict — the conflict is the finding, and it is a fact about *management*, not about the
   business (`agents/_shared/epistemics.md`).
3. **L6 outruns L1.** The balance-sheet residue grows faster than the line that created it. Receivable
   days, inventory days, CWIP ageing, capitalised cost.
4. **L7 does not follow L1.** Multi-year cumulative CFO diverges from cumulative PAT. Tested
   cumulatively over 5–10 years, never on a single year, because one year of working-capital swing is
   noise and five years of it is a policy.

### 2d. Worked shape

Real, from the repo's reference reading — a chain that breaks at L2:

> **L1** PNB management deck reports PCR 97.14%. **L2** Note 4.a shows 70.6% of that cover is the
> ₹89,042.50 cr technical write-off pool `[AR PNB FY2026, Note 4.a, p182]`. Both numbers are true;
> only one is an answer. The chain breaks at L2 because the aggregate's components change what the
> aggregate means — and the investor presentation, per `CLAUDE.md`, is a marketing document that
> cannot outrank the note.

Schematic, for the general template — **ILLUSTRATIVE, not a real company, no fact_ids, never to be
quoted in a report:**

> **L1** Revenue ₹1,000cr (+25%). **L2** Product A ₹700cr, Product B ₹250cr, residual ₹50cr `NOT
> DISCLOSED`. **L3** A: volume +5%, realisation +14%; B: volume +40%, realisation −8% `DERIVED`.
> **L4** B is 62% one customer, related party `[Note 38]`. **L5** revenue recognised at dispatch;
> policy unchanged. **L6** receivables +48%, of which related-party receivables +180%. **L7** CFO
> −12% against PAT +22%. **L8** not sustainable — growth sits in the lower-margin product, sold to one
> related counterparty, unconverted to cash. **State: BROKEN at L6/L7. Severity: Critical.**
>
> That is the evidence. The finding built on it runs S1–S6 and connects four domains — Income
> Statement, Balance Sheet, Cash Flow, Governance — reaching S6: *reported growth is not a claim on
> future cash, and the earnings multiple is being paid on a number that has not converted in two years.*

---

## 3. Materiality — when the chain is mandatory

Tracing everything is the same failure as tracing nothing: it exhausts the budget before it reaches the
lines that decide the case. "Maximum available granularity" (owner principle 6) is bounded here.

**The chain is mandatory for any line meeting *any* of these:**

| # | Trigger |
|---|---|
| 1 | ≥ 5% of revenue, **or** ≥ 5% of PBT, **or** ≥ 2% of total assets |
| 2 | Moved ≥ 20% year-on-year in absolute terms — **regardless of size** |
| 3 | Any accounting-policy change, restatement, or reclassification touches it |
| 4 | Involves a related party — **at any size** |
| 5 | Is an "Other" / "Miscellaneous" / "Sundry" line ≥ 1% of its parent, or growing faster than its parent |
| 6 | The auditor named it — KAM, emphasis of matter, qualification, or CARO observation |
| 7 | Management named it in a concall or presentation — **management attention makes a line material regardless of size** |
| 8 | A peer discloses it and this company does not |

Below every trigger: one line recording the item and why it was not traced. That line is the brake.
A line silently skipped is a QC failure; a line explicitly not traced is a decision on the record.

---

## 4. Extraction and arithmetic — who computes what

**Decided by the owner, 2026-09-07: be practical. Do not write unnecessary code — the analyst is capable
of arithmetic — and write code where it is genuinely required.** This closes the question §4 previously
left open, and it governs this doctrine. (The implementation repo at `~/Desktop/equity reserch` holds a
stricter rule of its own, Law 1; that rule binds that repo, not this doctrine. If the doctrine is ever
adopted there, this section is the divergence to reconcile.)

**Extraction is never code.** Note numbering, segment definitions and disclosure depth differ per
company and per year, so a parser breaks on exactly the companies worth reading. The analyst reads the
PDF and transcribes with a page cite. This was never in question and does not change.

**Arithmetic is the analyst's by default.** Ratios, growth rates, margins, per-unit economics, YoY
deltas, share-of-total, simple two-to-four-operand work — compute it, show it, move on. Writing a
function to divide two numbers is not rigour, it is ceremony.

### 4a. When code is actually required

Not a matter of taste. Any one of these triggers it:

| # | Trigger | Why |
|---|---|---|
| 1 | **More than ~7 operands** in one sum or aggregation — a schedule, an ageing table, a segment roll-up | Long column sums are where silent arithmetic errors live |
| 2 | **Multi-year cumulative aggregation** — 5–10 year CFO vs PAT, cumulative capex, cumulative sources and uses | The test the doctrine leans on hardest, and the easiest to get quietly wrong |
| 3 | **An exact tie-out that gates a conclusion** — `L1 = ΣL2`, `opening + additions − disposals = closing` | A near-miss must be detected as a miss, not rounded away |
| 4 | **The same computation across many companies or periods** — peer tables, 10-year trend lines | Here code is *less* work, not more |
| 5 | **A number QC must reproduce exactly** | If it has to be re-derived identically, it needs a deterministic formula anyway |

Everything else: no code.

### 4b. The safety net, which costs nothing

The failure mode that matters is that **a wrong sum looks exactly like a right one** — there is no error
signal, and confidence is unchanged. Two habits catch nearly all of it without a line of code:

1. **Show the arithmetic inline, not just the result.** `1,247 − 1,032 = 215 (+20.8%)` is checkable by a
   reader; `+20.8%` is not.
2. **Any computed number that carries a conclusion gets recomputed once, independently** — recomputed,
   not re-read. A second pass at the arithmetic catches slips that re-reading the same line never will.

Both are cheaper than writing code, and they apply to every `DERIVED` value whether or not §4a triggered.

### 4c. Consequence

Arithmetic handed to the analyst is fine; arithmetic *presented as the output* is the failure §1 exists
to stop. The point of keeping the calculation cheap is that the effort goes into S1–S6 instead.

---

## 5. Evidence tags

Unchanged from the repo's existing contract: every figure carries `[fact:<id>]` in report prose
(`core/validators/citation.py`), and every fact carries `(doc_id, page/para, published_at,
extractor_version)`.

For chain records, the human-readable tag additionally names the printed page, because the source of
record is the PDF: `[AR FY25, Note 24, PDF p187 / printed pr372]`. The PDF-to-printed mapping is
**derived per document, never assumed** — two-up scans, cover matter and inserted sections all shift it.

Source priority when filings conflict, in force for every link:

> Audited annual report > audited quarterly filing > unaudited quarterly filing > concall statement >
> investor presentation > media.

An investor presentation is used to establish **what management claimed**, which is L3 and L8 input and
a fact about management. It is never the source of an L1.

### 5a. The record layer — where structured data lives

**One rule: a CSV exists where code must read it, and nowhere else.** Not for viewing, not for opening
in a spreadsheet, not because the data happens to have rows. A structured file created for human
convenience is a second copy of a number, and a second copy drifts.

**CSV — numeric series only.** Two artifacts qualify:

| File | Shape | Why it must be machine-readable |
|---|---|---|
| `trend_10y.csv` | ~15 metrics × 10 years | §4a triggers 2 and 4 mandate code for multi-year cumulative aggregation. Code needs a parseable input, not a markdown table |
| `peer_grid.csv` | metrics × 3–5 peers, one period basis | Same computation across companies — §4a trigger 4 |

**Markdown with a fixed template — everything else.** Chain records, the red-flag register, the gap
register, promise-vs-delivery, the RPT ledger. These are **prose with attributes**, not tables: L3 is a
decomposition, L5 is policy prose, L8 is a condition. Markdown is canonical for them because it is what
the report consumes directly with no transformation step, it is diffable and reviewable in a fresh
context (§10), and a strict template is parseable enough for QC's structural checks — link states,
domain counts and tag presence are all findable by regex.

**Values, never formulas.** Every cell carries its value *and* its evidence tag. A formula in a cell is a
number whose provenance is invisible — the exact failure §2b exists to prevent. Arithmetic and its
working live in the markdown per §4b; the CSV holds the result and its tag.

**No spreadsheet export.** A `.xlsx` derived from these would be a third place the same number lives.
`trend_10y.csv` already opens in any spreadsheet if the owner wants to pivot it.

---

## 6. The ₹100 map is the chain, aggregated

The source-to-destination map is not a separate exercise. It is L1→L7 run across the whole P&L and
summed into one frame:

```
₹100 revenue → cost layers → operating profit → interest & tax → PAT
             → working-capital absorption → CFO → capex → FCF
             → debt repayment / dividend / buyback / acquisition / cash balance
```

It ships with the cumulative 5–10 year CFO/PAT conversion stated as a single number, and with every
step that lost more than ₹5 of the ₹100 carrying its own chain record. A ₹100 map whose steps have no
chains behind them is a data print, and does not ship. A ₹100 map that has chains but no S5/S6 above it
is evidence without a conclusion, and does not ship either.

---

## 7. Execution order — waves, not a chain of stages

The analysis stages form a dependency graph. Running them serially pays latency the dependencies do not
require. Stages within a wave run concurrently; a wave starts when the prior wave's gate passes.

| Wave | Runs concurrently | Depends on |
|---|---|---|
| 0 | Document collection (parallel per document) | — |
| 1 | Document mapping — **one agent per annual report** | 0 |
| **1.5** | **Triage gate** — 8-point quick screen, CFO/PAT, promoter pledge | 1 |
| 2 | Business understanding ‖ promise-vs-delivery ‖ governance (board / promoter / auditor / regulatory) ‖ industry ‖ peer set | 1.5 |
| 3 | Revenue ‖ cost ‖ balance sheet ‖ notes forensics ‖ group & RPT | 2 |
| 4 | Cash & ₹100 map ‖ unit economics ‖ below-the-line ‖ capital allocation | 3 |
| 5 | **Earnings-quality gate** | 4 |
| 6 | Governance synthesis | 5 |
| 7 | **Red-flag gate** + bear case | 6 |
| 8 | Valuation → report → QC | 7 |

**Waves 2–4 produce evidence; waves 5–8 produce conclusions.** Cross-domain synthesis (§1b) is
structurally impossible before wave 5, because the non-statement domains do not all exist until wave 2
completes and the statement domains until wave 4. An agent in wave 3 that reaches for an investment
implication is working outside its evidence base; it records the observation and the chain state, and
the finding is built later.

Three ordering corrections against the 2026-09-07 specification, each with its reason:

1. **The 8-point quick screen moves from stage 15 to wave 1.5.** As specified it runs after the full
   dissection, so the pipeline pays its full cost on companies the screen would have killed first.
2. **Promise-vs-delivery moves from stage 14 to wave 2.** It reads only concalls and presentations and
   depends on nothing else in the pipeline. There is no reason for it to wait — and it is a
   non-statement domain, so §1b's synthesis requirement needs it early.
3. **Quantified unit economics moves from stage 4 to wave 4.** Operating leverage and "₹x of capital per
   ₹1 of revenue" cannot be computed before the cost engine and the balance sheet have run. The
   qualitative "how this business makes money" stays in wave 2, where it belongs and where it must
   contain no numbers.

**One read, many uses.** Wave 1 emits a per-document evidence ledger — every number the later waves will
need, transcribed with its tag and its verbatim label, no interpretation. Waves 2–8 read the ledger and
pull specific pages when they need surrounding context. Fourteen agents re-reading the same 1,500 pages
is the pipeline's dominant cost and it buys nothing; the ledger is an analyst's working notes, and it
is what every later wave computes from.

---

## 8. Gates

| Gate | Passes when | On failure |
|---|---|---|
| **Triage** (1.5) | No critical flag on the 8-point screen, or owner overrides | Continue only on owner instruction — never drop the company (ADR-0064: an owner-named company always gets a report) |
| **Earnings quality** (5) | Verdict is not *Cannot be relied upon* | Valuation is skipped. The report ships with the trust verdict as its conclusion |
| **Red flag** (7) | No unresolved Critical flag | Terminal state **`UNINVESTABLE ON TRUST GROUNDS`** — an explicit, publishable ending, not a pause. The report ships |

**Every gate's failure path ends in an artifact.** Per ADR-0064, suspicion, gate failure and opacity are
conclusions to document, never reasons not to research. No gate in this document may terminate a run
without output. A gate failure is itself an S6 — the strongest kind, since it bounds every other
implication in the report.

---

## 9. The gap register

Every `NOT DISCLOSED` link accumulates into one register per company, carrying: the line, the link, what
is missing, whether peers disclose it, and the question it generates for the next concall. This register
is a **section of the final report**, not an internal artifact — what a company declines to disclose is
part of the case, and the reader is entitled to see it assembled.

---

## 10. QC

The report cannot be released without a QC pass. "Sample-check" is not a testable instruction; the rates
are fixed:

- **100%** of numbers appearing in the report's headline conclusions, re-derived from source.
- **100%** of anything tagged `DERIVED` or `ESTIMATE` — arithmetic re-run independently, inputs re-tied.
- **Every `DERIVED` value shows its arithmetic inline** (§4b), and every §4a trigger that fired is
  backed by code rather than by hand.
- **100%** of `BROKEN` links — the contradiction re-verified against both sides.
- **20% random** of everything else.
- **Every** chain record checked for link completeness: eight links present, each in a declared state.

**Interpretation checks — the §1 half, and the one most likely to be skipped:**

- **Every finding carries S1–S6.** A finding missing S5 or S6 is an observation mislabelled.
- **Every finding names ≥ 3 domains, ≥ 1 non-statement** (§1b). QC counts them.
- **Every finding shows its disconfirming search** — evidence against, found or recorded absent.
- **Every S3 proportion carries its counter-proportion** (§1a-i). A share stated alone fails.
- **Every S5 carries the base rate** — realised loss established, or its absence explicitly recorded
  (§1a-ii).
- **Every "unknown" names the document that would answer it** (§1a-iii). An unnamed unknown fails.
- **No `SECONDARY`-sourced step carries a conclusion alone** (§1a-iii).
- **Two consecutive unanswerable steps reached the gap register** at minimum severity Medium, rather
  than being dropped.
- **No S6 crosses into recommendation** (§1c), and no S6 rests on a number the earnings-quality gate
  rated unreliable.
- **Descriptive-content check.** Any section that reproduces annual-report content without a conclusion
  above it fails as a data print, however well cited.

**Contradiction adjudication.** Nothing is deleted (owner principle 9), and a contradiction between two
agents is never resolved by the later agent overwriting the earlier one. Both positions enter the
red-flag register with their evidence tags, and QC **fails the report** if a contradiction present in an
intermediate artifact is absent from the final one. A silently resolved contradiction is the specific
failure this rule exists to catch.

QC runs in a fresh context, per `docs/directives/FRESH_CONTEXT_REVIEW_RULE.md`. It receives the
artifacts and the acceptance criteria, never the producing agents' reasoning traces.
