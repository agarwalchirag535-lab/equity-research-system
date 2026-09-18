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
