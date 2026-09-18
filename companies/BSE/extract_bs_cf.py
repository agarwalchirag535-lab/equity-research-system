#!/usr/bin/env python3
"""Consolidated balance sheet + cash flow series.
Anchored on the consolidated P&L page: the consolidated BS sits just before it and the
consolidated cash flow just after, so standalone statements elsewhere in the AR are never picked up.
Doctrine 4a triggers 2 and 4."""
import re, pathlib, csv, json
P = pathlib.Path(__file__).parent
TOKEN = re.compile(r"\(([\d,]+)\)|(-?[\d][\d,]*)")
def last_two(l):
    t=[]
    for m in TOKEN.finditer(l):
        t.append(-int(m.group(1).replace(",","")) if m.group(1) else int(m.group(2).replace(",","")))
    return t[-2:] if len(t)>=2 else []

BS=[("total_equity",r"^\s*Total equity\b"),("total_assets",r"Total assets"),
    ("total_noncurrent_assets",r"Total non[- ]current assets"),("total_current_assets",r"Total current assets"),
    ("total_current_liabilities",r"Total current liabilities"),("total_noncurrent_liab",r"Total non[- ]current liabilities"),
    ("trade_receivables",r"Trade receivables"),("ppe",r"Property, [Pp]lant and [Ee]quipment"),
    ("cwip",r"Capital work[- ]in[- ]progress"),("goodwill",r"^\s*Goodwill"),
    ("equity_and_liab_total",r"Total equity and liabilities")]
CF=[("cfo",r"Net cash (?:generated|flow|used).{0,30}operating activities"),
    ("cfi",r"Net cash (?:generated|flow|used).{0,30}investing activities"),
    ("cff",r"Net cash (?:generated|flow|used).{0,30}financing activities"),
    ("capex_ppe",r"(?:Purchase|Payments?) (?:of|for) property, plant"),
    ("dividend_paid",r"Dividend paid"),("tax_paid",r"(?:Income[- ])?[Tt]ax(?:es)? paid"),
    ("cash_close",r"Cash and cash equivalents at the end")]

rows, prov, meta = {}, {}, {}
for f in sorted((P/"data/text").glob("BSE-AR-FY*.txt")):
    fy=int(re.search(r"FY(\d{4})",f.stem).group(1))
    pgs={int(m.group(1)):m.group(2) for m in
         re.finditer(r"===== PDF PAGE (\d+) =====\n(.*?)(?=\n===== PDF PAGE |\Z)", f.read_text(), re.S)}
    pl=next((p for p in sorted(pgs) if re.search(r"Consolidated Statement of Profit and Loss for the year",pgs[p])),None)
    if not pl: print(f"FY{fy}: no consolidated P&L anchor"); continue
    # consolidated BS: nearest page in [pl-3, pl] carrying the BS total
    bsp=next((p for p in range(pl,pl-4,-1) if p in pgs and re.search(r"Total equity and liabilities",pgs[p])),None)
    # consolidated CF: window after the P&L
    cfw={p:pgs[p] for p in range(pl,pl+6) if p in pgs}
    cfp=next((p for p in sorted(cfw) if re.search(r"operating activities",cfw[p])),None)
    meta[fy]={"pl":pl,"bs":bsp,"cf":cfp}
    n=0
    if bsp:
        for k,pat in BS:
            rx=re.compile(pat); hit=next((l for l in pgs[bsp].splitlines() if rx.search(l)),None)
            if hit:
                v=last_two(hit)
                if len(v)==2:
                    rows.setdefault(k,{})[fy]=v[0]; rows.setdefault(k,{}).setdefault(fy-1,v[1])
                    prov[f"{k}|FY{fy}"]=f"[AR FY{fy}, Consolidated Balance Sheet, PDF p{bsp}]"; n+=1
    if cfp:
        blob="\n".join(cfw[p] for p in sorted(cfw) if p>=cfp)
        for k,pat in CF:
            rx=re.compile(pat); hit=next((l for l in blob.splitlines() if rx.search(l)),None)
            if hit:
                v=last_two(hit)
                if len(v)==2:
                    rows.setdefault(k,{})[fy]=v[0]; rows.setdefault(k,{}).setdefault(fy-1,v[1])
                    prov[f"{k}|FY{fy}"]=f"[AR FY{fy}, Consolidated Cash Flow, PDF p{cfp}]"; n+=1
    print(f"FY{fy}: P&L p{pl}  BS p{bsp}  CF p{cfp}  -> {n} lines")

years=sorted({y for d in rows.values() for y in d})
with open(P/"records/balance_cash_10y.csv","w",newline="") as fh:
    w=csv.writer(fh); w.writerow(["line_item","unit"]+[f"FY{y}" for y in years])
    for k,_ in BS+CF:
        d=rows.get(k,{})
        if d: w.writerow([k,"INR lakh"]+[d.get(y,"") for y in years])
o=json.load(open(P/"records/trend_provenance.json")); o["provenance"].update(prov)
o["statement_pages"]={str(k):v for k,v in meta.items()}
json.dump(o,open(P/"records/trend_provenance.json","w"),indent=1)
print(f"\n{len(rows)} lines x {len(years)} years")
