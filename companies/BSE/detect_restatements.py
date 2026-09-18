#!/usr/bin/env python3
"""Every restatement across FY2016-FY2026, found mechanically.

Method: for each AR, the RIGHT column is the prior year as that AR now presents it.
Compare it against the LEFT column of the prior year's own AR (as first reported).
A difference is a restatement, a reclassification, or a disclosure change - always a finding.
Doctrine 4a trigger 3 (exact tie-out) and trigger 4 (same op across 9 documents).
"""
import re, pathlib, json, csv
P = pathlib.Path(__file__).parent
TXT = P/"data/text"
LINES = [
 ("revenue_from_operations", r"^\s*Revenue from operations\s+[\d(]"),
 ("investment_income",       r"^\s*\d?\s*Investment income"),
 ("other_income",            r"^\s*\d?\s*Other income"),
 ("total_income",            r"Total (?:income|revenue) \(1\+2\+3\)"),
 ("employee_benefits",       r"Employee benefits expense"),
 ("total_expenses",          r"^\s*Total expenses"),
 ("pat_attributable",        r"Net [Pp]rofit attributable to the shareholders"),
 ("pat_total_ops",           r"Net profit for the year from total operation"),
]
TOKEN = re.compile(r"\(([\d,]+)\)|(-?[\d][\d,]*)")
def last_two(l):
    t=[]
    for m in TOKEN.finditer(l):
        t.append(-int(m.group(1).replace(",","")) if m.group(1) else int(m.group(2).replace(",","")))
    return t[-2:] if len(t)>=2 else []

def pl_block(fy):
    f = TXT/f"BSE-AR-FY{fy}.txt"
    if not f.exists(): return None, None
    for m in re.finditer(r"===== PDF PAGE (\d+) =====\n(.*?)(?=\n===== PDF PAGE |\Z)", f.read_text(), re.S):
        if re.search(r"Consolidated Statement of Profit and Loss for the year", m.group(2)):
            return int(m.group(1)), m.group(2)
    return None, None

vals = {}   # (fy_reported_in, line) -> [current, prior]
pages = {}
for fy in [2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]:
    pg, blk = pl_block(fy)
    if not blk: continue
    pages[fy] = pg
    for key, pat in LINES:
        rx = re.compile(pat)
        hit = next((l for l in blk.splitlines() if rx.search(l)), None)
        if hit:
            v = last_two(hit)
            if len(v)==2: vals[(fy,key)] = v

out = []
for fy in [2017,2018,2019,2020,2021,2022,2023,2024,2025,2026]:
    prior = fy-1
    # FY2023 AR obtained 2026-09-08 (GAP-001 closed); no year is skipped any more
    for key,_ in LINES:
        a = vals.get((fy,key))          # this AR: [cy, py]
        b = vals.get((prior,key))       # prior AR: [cy, py]
        if not a or not b: continue
        as_restated, as_first = a[1], b[0]
        if as_restated != as_first:
            d = as_restated - as_first
            out.append({"fy_restated": prior, "line": key,
                        "as_first_reported": as_first, "as_restated": as_restated,
                        "delta": d, "pct": round(100.0*d/as_first,2) if as_first else None,
                        "first_src": f"[AR FY{prior}, Consolidated P&L, PDF p{pages.get(prior)}]",
                        "restated_src": f"[AR FY{fy}, Consolidated P&L, PDF p{pages.get(fy)}]"})
json.dump(out, open(P/"records/restatements.json","w"), indent=1)
with open(P/"records/restatements.csv","w",newline="") as fh:
    w=csv.writer(fh); w.writerow(["fy_restated","line","as_first_reported","as_restated","delta","pct"])
    for r in out: w.writerow([r["fy_restated"],r["line"],r["as_first_reported"],r["as_restated"],r["delta"],r["pct"]])
print(f"{len(out)} restatements found\n")
cur=None
for r in out:
    if r["fy_restated"]!=cur: cur=r["fy_restated"]; print(f"FY{cur}:")
    print(f"   {r['line']:<26} {r['as_first_reported']:>10,} -> {r['as_restated']:>10,}  {r['delta']:>+9,}  {r['pct']:>+7.2f}%")
