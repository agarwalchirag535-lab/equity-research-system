#!/usr/bin/env python3
"""Machine-checkable half of ANALYSIS_DOCTRINE.md sect.10, for the BSE run.

Exit 0 = pass. Exit 1 = rework, with reasons. Judgement does not decide done; this does.
"""
import re, sys, pathlib

ROOT = pathlib.Path(__file__).parent
STATES = {"TRACED", "NOT-DISCLOSED", "DERIVED", "ESTIMATE", "BROKEN"}
LINKS = ["L1", "L2", "L3", "L4", "L5", "L6", "L7", "L8"]
STATEMENT = {"IncomeStatement", "BalanceSheet", "CashFlow", "Notes"}
NONSTATEMENT = {"Business", "MgmtCommentary", "Governance", "Industry"}
RECO = re.compile(r"\b(buy|sell|hold|accumulate|target price|price target|overweight|underweight)\b", re.I)
TAG = re.compile(r"\[(AR |Q\d|IP |fact:|SECONDARY:|BSE |NSE |AGM |RA )[^\]]*\]")

def chain_blocks(t):
    return re.findall(r"^### CHAIN: (.+?)$\n(.*?)(?=^###|\Z)", t, re.M | re.S)

def finding_blocks(t):
    return re.findall(r"^### FINDING: (.+?)$\n(.*?)(?=^###|\Z)", t, re.M | re.S)

def check(path):
    errs = []
    t = path.read_text()
    rel = path.relative_to(ROOT)

    for name, body in chain_blocks(t):
        seen = {}
        for ln in body.splitlines():
            m = re.match(r"\s*(L[1-8])\s+\S+\s+(\S+)\s*\|(.*)$", ln)
            if m:
                seen[m.group(1)] = (m.group(2), m.group(3))
        missing = [l for l in LINKS if l not in seen]
        if missing:
            errs.append(f"{rel}: CHAIN '{name}' missing {','.join(missing)}")
        for l, (st, rest) in seen.items():
            if st not in STATES:
                errs.append(f"{rel}: CHAIN '{name}' {l} bad state '{st}'")
            if st == "DERIVED" and "=" not in rest:
                errs.append(f"{rel}: CHAIN '{name}' {l} DERIVED without arithmetic shown")
            if st == "NOT-DISCLOSED" and "->" not in rest:
                errs.append(f"{rel}: CHAIN '{name}' {l} NOT-DISCLOSED must name the document (->)")
            if st in {"TRACED", "DERIVED", "ESTIMATE"} and not TAG.search(rest):
                errs.append(f"{rel}: CHAIN '{name}' {l} {st} without an evidence tag")
        if "CHAIN-STATE:" not in body:
            errs.append(f"{rel}: CHAIN '{name}' missing CHAIN-STATE")

    for name, body in finding_blocks(t):
        for k in ("S1 WHAT:", "S2 WHY:", "S3 EVIDENCE:", "S4 CONNECTS:", "DOMAINS:",
                  "DISCONFIRM:", "S5 MEANS:", "BASE-RATE:", "S6 IMPLICATION:", "SEVERITY:"):
            if k not in body:
                errs.append(f"{rel}: FINDING '{name[:44]}' missing {k}")
        m = re.search(r"^DOMAINS:(.+)$", body, re.M)
        if m:
            ds = {d.strip() for d in m.group(1).split(",") if d.strip()}
            bad = ds - STATEMENT - NONSTATEMENT
            if bad:
                errs.append(f"{rel}: FINDING '{name[:44]}' unknown domain(s) {sorted(bad)}")
            if len(ds) < 3:
                errs.append(f"{rel}: FINDING '{name[:44]}' only {len(ds)} domain(s), need >=3")
            if not (ds & NONSTATEMENT):
                errs.append(f"{rel}: FINDING '{name[:44]}' no non-statement domain")
        m = re.search(r"^S6 IMPLICATION:(.+?)(?=^[A-Z]|\Z)", body, re.M | re.S)
        if m and RECO.search(m.group(1)):
            errs.append(f"{rel}: FINDING '{name[:44]}' S6 contains recommendation language")
        for k in ("S5 MEANS:", "S6 IMPLICATION:"):
            m2 = re.search(rf"^{re.escape(k)}(.*)$", body, re.M)
            if m2 and len(m2.group(1).strip()) < 25:
                errs.append(f"{rel}: FINDING '{name[:44]}' {k} too thin to be a judgement")
    return errs

def main():
    targets = sorted(list((ROOT / "waves").glob("*.md")) + list((ROOT / "records").glob("*.md")))
    if not targets:
        print("verify: no artifacts yet"); return 1
    allerrs, nch, nfi = [], 0, 0
    for p in targets:
        t = p.read_text(); nch += len(chain_blocks(t)); nfi += len(finding_blocks(t))
        allerrs += check(p)
    print(f"verify: {len(targets)} files, {nch} chain records, {nfi} findings")
    if allerrs:
        print(f"\nFAIL ({len(allerrs)}):")
        for e in allerrs[:60]: print("  -", e)
        if len(allerrs) > 60: print(f"  ... +{len(allerrs)-60} more")
        return 1
    print("PASS")
    return 0

sys.exit(main())
