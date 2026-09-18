# Output templates — BSE run

Every artifact uses these blocks verbatim. `verify.py` parses them; free-form prose outside a block is
narrative and is not checked, but **no number may appear outside a block without a tag**.

## Evidence tag
`[AR FY25, Note 24, p187]` · `[AR FY25, Note 24, PDF p187/pr372]` · `[Q3FY26 Concall, CFO]` ·
`[IP Feb-26, slide 14]` · `[SECONDARY: <source>]`

## Chain record (doctrine §2)

```
### CHAIN: <line item> | FY<yy>
L1 REPORTED   <state> | <value> | <tag>
L2 COMPONENTS <state> | <value> | <tag>
L3 DRIVER     <state> | <value> | <tag>
L4 COUNTERPARTY <state> | <value> | <tag>
L5 RECOGNITION  <state> | <value> | <tag>
L6 BALANCE-SHEET <state> | <value> | <tag>
L7 CASH       <state> | <value> | <tag>
L8 SUSTAIN    <state> | <value> | <tag>
CHAIN-STATE: <TRACED|BROKEN at Lx/Ly>
```

States: `TRACED` `NOT-DISCLOSED` `DERIVED` `ESTIMATE` `BROKEN`.
A `DERIVED` value must show its arithmetic inline (contain `=`).
A `NOT-DISCLOSED` must name the document that would answer it, after `->`.

## Finding (doctrine §1)

```
### FINDING: <one-line claim>
S1 WHAT: ...
S2 WHY: ...
S3 EVIDENCE: ...            (sized in Rs; a proportion needs its counter-proportion)
S4 CONNECTS: ...
DOMAINS: Business, IncomeStatement, BalanceSheet, CashFlow, Notes, MgmtCommentary, Governance, Industry
DISCONFIRM: ...             (evidence against, found or recorded absent)
S5 MEANS: ...
BASE-RATE: ...              (realised loss here or in the system, or explicitly none found)
S6 IMPLICATION: ...
SEVERITY: Critical|High|Medium|Watch|None
```

`DOMAINS:` lists >=3, at least one of Business / MgmtCommentary / Governance / Industry.
`S6` must not contain recommendation language.

---

## New-listing additions (BlueStone run)

**Basis tag is mandatory on every pre-listing number.** The RHP/Prospectus carries *Restated Consolidated
Summary Statements* for FY23/FY24/FY25 prepared for the offer document. The FY2025 and FY2026 annual
reports carry *reported* statements. They are different bases and are never joined into one series
without the basis stated on each point.

Tags: `[RHP p<PDF p>, Restated FY24]` · `[Prospectus p<n>, RESTATED]` · `[AR FY26, Note 25, p<n>, REPORTED]`
· `[MAR Q3FY26]` (monitoring agency report) · `[SoD Q3FY26]` (statement of deviation) ·
`[IP Q1FY27, slide n]` · `[Concall Q2FY26, <speaker>]` · `[SHP 31Dec2025]` · `[NSE ann 14Jan2026]`

**Series-basis line** — any table mixing bases carries this immediately under it:

```
BASIS: FY23-FY25 = RHP restated consolidated | FY25-FY26 = AR reported consolidated |
       FY25 appears on both bases: restated <x> vs reported <y>, difference <z> -> <explanation|UNEXPLAINED>
```

## Lock-in / exit record (new-listing overlay)

```
### EXIT: <holder> | <date>
PRE-IPO STAKE   <%> | <tag>
LOCK-IN CLASS   <anchor 30d | anchor 90d | pre-IPO 6m | promoter 18m/3y> | expiry <date> | <tag>
SOLD            <qty> | <price> | <route: bulk/block/open market> | <tag>
POST STAKE      <%> | <tag>
RESIDUAL OVERHANG <qty / % of float still held> | <tag>
```

## IPO proceeds record (replaces multi-year capital allocation for a company with no such history)

```
### OBJECT: <stated object of the issue>
PROMISED    <Rs mn> | <deployment schedule per Prospectus> | <tag>
DEPLOYED    <Rs mn as at latest MAR> | <tag>
UNUTILISED  <Rs mn> | <where parked> | <tag>
DEVIATION   <none | description> | <tag>
STATE: ON-PLAN | BEHIND | DEVIATED | NOT-DISCLOSED
```
