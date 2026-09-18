#!/usr/bin/env python3
"""Quarterly consolidated P&L series from the results filings.
Column 0 of each statement line is the current quarter. The column COUNT is derived from the
modal amounts-per-line across the statement itself, never assumed - filings carry 4, 5 or 6
columns depending on whether YTD and prior-FY columns are present.
A line deviating from the mode is recorded DAMAGED with its raw text, never guessed around.
"""
import re, pathlib, csv, collections
P = pathlib.Path(__file__).parent
T = P/"data/quarterly_text"
AMT = re.compile(r"\(?\b\d{1,3}(?:,\d{2,3})+\b\)?|\(?\b\d{1,4}\b\)?")

def tail(line):
    """Amounts live after the label. Two things must be stripped first or they parse as amounts:
    formula/reference groups - (1+2+3), (8+9), (5a to 5f), (refer note 6) - and the leading
    line index. Parenthesised groups that are PURELY numeric are kept: they are negatives."""
    line = re.sub(r"\((?=[^)]*(?:[A-Za-z]|[+]|\s-\s|\bto\b))[^)]*\)", " ", line)
    m = list(re.finditer(r"[A-Za-z]{2,}", line))
    return line[m[-1].end():] if m else line

WANT=[("revenue_ops",r"Revenue from operations"),
      ("investment_income",r"Investment income"),
      ("other_income",r"^\s*\d?\s*Other income"),
      ("total_income",r"Total income \(1\+2\+3\)"),
      ("employee",r"Employee benefits expense"),
      ("technology",r"Technology expense"),
      ("clearing",r"Clearing and settlement expense"),
      ("regulatory",r"Regulatory contribution"),
      ("other_expenses",r"^\s*[a-f]\)\s*Other expenses"),
      ("depreciation",r"Depreciation (?:and amorti[sz]ation )?expense"),
      ("total_expenses",r"Total expenses"),
      ("pbt_pre_sgf",r"Profit before contribution to core settlement"),
      ("core_sgf",r"^\s*\d?\s*Contribution to core settlement"),
      ("pbt",r"Profit before tax(?! and share)"),
      ("pbt_incl_assoc",r"Profit before tax \(|Profit before tax and share"),
      ("pat",r"Net profit for the (?:period|quarter)")]

def amts(l):
    l = tail(l)
    out=[]
    for m in AMT.finditer(l):
        s=m.group(0); neg=s.startswith("(")
        d=re.sub(r"[^\d]","",s)
        if not d: continue
        out.append(-int(d) if neg else int(d))
    return out

rows, damaged = [], []
for f in sorted(T.glob("*.txt")):
    pgs={int(m.group(1)):m.group(2) for m in
         re.finditer(r"===== PDF PAGE (\d+) =====\n(.*?)(?=\n===== PDF PAGE |\Z)", f.read_text(), re.S)}
    cand=[(p,b) for p,b in sorted(pgs.items())
          if re.search(r"Statement of Consolidated Financial Results", b)
          and re.search(r"Revenue from operations", b)]
    if not cand: continue
    p,b=cand[0]
    lines=b.splitlines()
    # modal column count across lines that look like statement rows
    counts=[len(amts(l)) for l in lines if len(amts(l))>=3 and re.search(r"[A-Za-z]{6,}",l)]
    if not counts: continue
    ncols=collections.Counter(counts).most_common(1)[0][0]
    q=re.search(r"quarter\s+ended\s+(\w+)\s+(\d{1,2}),?\s*(\d{4})", b, re.S|re.I)
    rec={"filed":(re.search(r"BSE-Q-(\d{2}\w{3}\d{4})",f.stem) or [None,"?"])[1],
         "quarter_ended":f"{q.group(1)[:3]}-{q.group(3)}" if q else "?",
         "pdf_page":p,"cols":ncols}
    for k,pat in WANT:
        hit=next((l for l in lines if re.search(pat,l)),None)
        if not hit: continue
        v=amts(hit)
        if len(v)==ncols: rec[k]=v[0]
        elif v: damaged.append((rec["filed"],k,len(v),ncols,hit.strip()[:80]))
    rows.append(rec)

# dedupe: same filing date + same revenue = same statement from two attachments
seen=set(); uniq=[]
for r in sorted(rows,key=lambda x:x["filed"]):
    key=(r["filed"],r.get("revenue_ops"))
    if key in seen: continue
    seen.add(key); uniq.append(r)

keys=["filed","quarter_ended","pdf_page","cols"]+[k for k,_ in WANT]
with open(P/"records/quarterly_series.csv","w",newline="") as fh:
    w=csv.DictWriter(fh,fieldnames=keys,extrasaction="ignore"); w.writeheader()
    for r in uniq: w.writerow(r)
print(f"{len(uniq)} distinct consolidated quarterly statements\n")
print(f"{'filed':<11}{'quarter':<10}{'col':>4}{'revenue':>10}{'totinc':>10}{'regulatory':>11}{'clearing':>10}{'PBT':>10}")
for r in uniq:
    g=lambda k: f"{r[k]:,}" if r.get(k) not in (None,"") else "DMG"
    print(f"{r['filed']:<11}{r['quarter_ended']:<10}{r['cols']:>4}{g('revenue_ops'):>10}{g('total_income'):>10}{g('regulatory'):>11}{g('clearing'):>10}{g('pbt'):>10}")
print(f"\n{len(damaged)} damaged lines flagged (not guessed)")
for d in damaged[:6]: print(f"  {d[0]} {d[1]}: {d[2]} amounts vs {d[3]} expected | {d[4]}")
