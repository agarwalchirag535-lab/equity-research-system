# Equity Research System

Doctrine and execution design for multi-agent fundamental research on Indian listed companies (NSE/BSE).

**Created:** 2026-09-07.

---

## Files

| File | What it is |
|---|---|
| `INSTRUCTIONS.md` | The owner's master specification, preserved as written. The statement of intent: 22 agents, 20 stages, the 8-step dissection template, the ₹100 map, the 12-point governance frame, the bank overlay. §9 carries the two later directives (the traceability chain, and interpretation-not-reproduction). |
| `ANALYSIS_DOCTRINE.md` | The working doctrine. Takes the spec above and makes it executable: the L1–L8 traceability chain with link states, the S1–S6 interpretation ladder with a checkable cross-domain rule, materiality triggers, wave-based execution, gates, and fixed QC rates. |
| `EXECUTION_PLAN.md` | How to run it fast. Measured bottlenecks in the implementation repo, four ranked changes, and the tracer-bullet sequence. Analysis only — nothing applied. |

Read them in that order: intent → method → execution.

---

## The relationship between the three

`INSTRUCTIONS.md` says **what** to analyse. `ANALYSIS_DOCTRINE.md` says **how**, in a form a checker can
test. `EXECUTION_PLAN.md` says **in what order and how fast**.

The doctrine departs from the spec in four recorded places, each flagged rather than applied silently:

1. **Extraction versus arithmetic** (doctrine §4) — **decided 2026-09-07, closed.** The spec says "no
   code". The owner's ruling: be practical, don't write unnecessary code, write it where genuinely
   required. So extraction is never code, arithmetic is the analyst's by default, and code is required
   only on five named triggers — sums over ~7 operands, multi-year cumulative aggregation, exact
   tie-outs that gate a conclusion, computations repeated across companies, and numbers QC must
   reproduce exactly. The implementation repo's stricter Law 1 binds that repo, not this doctrine.
2. **The 8-point quick screen moves from stage 15 to a wave-1.5 triage gate**, so the pipeline stops
   paying full cost on companies the screen would have killed first.
3. **Promise-vs-delivery moves from stage 14 to wave 2.** It reads only concalls and depends on nothing
   else.
4. **Quantified unit economics moves from stage 4 to wave 4.** Operating leverage cannot be computed
   before the cost engine and balance sheet have run.

**S1–S6 is the single master reasoning framework** (doctrine §1e, decided 2026-09-07). The bank
doctrine's parallel seven-rung ladder is superseded, with its three unique requirements absorbed. Two
frameworks remain and they are orthogonal: the **L1–L8 chain** traces one line item vertically across
statements and produces evidence; **S1–S6** connects many facts horizontally across domains and produces
a finding.

---

## Scope boundary

There is a separate implementation repository at `~/Desktop/equity reserch` — a Python firm-of-agents
pipeline with a compute layer, fact provenance, verifiers and an autonomous harness.

**This project does not modify that repository.** `EXECUTION_PLAN.md` contains findings measured from a
read-only pass over it on 2026-09-07, with `file:line` references. Acting on any of those findings is a
change to that repo, made in that repo's own session, under its own review rules
(`docs/directives/FRESH_CONTEXT_REVIEW_RULE.md`).

---

## Open items

- **Retire `docs/BANK_ANALYSIS_DOCTRINE.md` §2c in the implementation repo.** Doctrine §1e now
  **supersedes** the seven-rung dig ladder: it was checked rung by rung, five rungs mapped cleanly onto
  S1–S6, and the three that did not — asymmetry, base rate, stopping rules — were absorbed as explicit
  conditions (§1a-i, §1a-ii, §1a-iii). The corresponding edit in that repo (replace §2c with a pointer)
  is not made from this project. Until it is, the two documents disagree.
- **`segments` is not ingested** in the implementation repo (roster prerequisite, A44/A45). That blocks
  L2 for revenue — the chain cannot run at full depth on a non-bank until it lands.
- **Sector overlays beyond banks** are unwritten: NBFC/HFC, insurance, real estate, pharma, IT services,
  capital goods, commodities.
