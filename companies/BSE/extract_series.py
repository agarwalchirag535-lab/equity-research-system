#!/usr/bin/env python3
"""10-year headline series from each AR's CONSOLIDATED P&L.
Justified as code by doctrine 4a triggers 2 and 4. Values only, never formulas.
Every value carries the AR and PDF page it was read from (records/trend_provenance.json).
"""
import re, pathlib, csv, json
P = pathlib.Path(__file__).parent
TXT = P/"data/text"

# canonical key -> alternate labels seen across FY2017-FY2026 (structure changes across years)
WANT = [
 ("rev_securities_services", [r"Securities services"]),
 ("rev_services_to_corporates", [r"Services to corporates"]),
 ("rev_data_dissemination", [r"Data dissemination"]),
 ("rev_training_institute", [r"Training institute"]),
 ("rev_software", [r"Sale of Software Licen"]),
 ("revenue_from_operations", [r"^\s*Revenue from operations\s*(?:\d{1,2}\s+)?[\d(]", r"Revenue from operations\s+\d"]),
 ("investment_income",       [r"Investment income"]),
 ("other_income",            [r"^\s*(?:\d\s+)?Other income"]),
 ("total_income",            [r"Total income"]),
 ("employee_benefits",       [r"Employee benefits expense"]),
 ("technology_expense",      [r"(?:Technology expense|Computer Technology Related Expenses)"]),
 ("regulatory_contribution", [r"Regulatory contribution"]),
 ("clearing_settlement",     [r"Clearing and settlement expense"]),
 ("finance_cost",            [r"^\s*Finance costs?\b"]),
 ("depreciation",            [r"Depreciation and amorti[sz]ation expense"]),
 ("other_admin_expenses",    [r"^\s*(?:Administration and other expenses|Other expenses)"]),
 ("total_expenses",          [r"Total expenses"]),
 ("exceptional_items",       [r"Total exceptional items"]),
 ("core_sgf_contribution",   [r"[Cc]ontribution to core settlement guarantee fund"]),
 ("associate_profit",        [r"Share of (?:net )?profits? of associate"]),
 ("pbt",                     [r"^\s*\d{0,2}\s*Profit before tax \(", r"^\s*Profit before tax\s+[\d(]"]),
 ("current_tax",             [r"^\s*Current tax\s+[\d(]"]),
 ("total_tax",               [r"Total tax expenses?"]),
 ("pat_continuing",          [r"Net profit for the year from continuing operation"]),
 ("pat_discontinued",        [r"Net profit for the year from discontinued operation"]),
 ("pat_total",               [r"Net profit for the year from total operation"]),
 ("pat_attributable",        [r"Net [Pp]rofit attributable to the shareholders"]),
 ("total_comprehensive",     [r"Total comprehensive income for the year\s+[\d(]"]),
]

TOKEN = re.compile(r"\(([\d,]+)\)|(-?[\d][\d,]*)")

def last_two(line):
    """The two year-columns are the last two numeric tokens on a statement line."""
    toks = []
    for m in TOKEN.finditer(line):
        if m.group(1) is not None:
            toks.append(-int(m.group(1).replace(",", "")))
        else:
            toks.append(int(m.group(2).replace(",", "")))
    # a bare '-' column means nil
    if re.search(r"\s-\s*$", line): toks.append(0)
    return toks[-2:] if len(toks) >= 2 else []

def pages(txt):
    return [(int(m.group(1)), m.group(2)) for m in
            re.finditer(r"===== PDF PAGE (\d+) =====\n(.*?)(?=\n===== PDF PAGE |\Z)", txt, re.S)]

rows, prov, meta = {}, {}, {}
for f in sorted(TXT.glob("BSE-AR-FY*.txt")):
    fy = int(re.search(r"FY(\d{4})", f.stem).group(1))
    pgs = pages(f.read_text())
    cand = [(p, t) for p, t in pgs if re.search(r"Consolidated Statement of Profit and Loss for the year", t)]
    if not cand:
        print(f"FY{fy}: NO consolidated P&L page"); continue
    pg, blk = cand[0]
    scale = "INR lakh" if re.search(r"in Lakh", blk, re.I) else (
            "INR crore" if re.search(r"in Crore", blk, re.I) else "UNKNOWN")
    meta[fy] = {"pdf_page": pg, "scale": scale}
    got = 0
    for key, pats in WANT:
        for pat in pats:
            rx = re.compile(pat)
            hit = next((l for l in blk.splitlines() if rx.search(l)), None)
            if hit:
                v = last_two(hit)
                if len(v) == 2:
                    rows.setdefault(key, {})[fy] = v[0]
                    rows.setdefault(key, {}).setdefault(fy - 1, v[1])
                    prov[f"{key}|FY{fy}"] = f"[AR FY{fy}, Consolidated P&L, PDF p{pg}]"
                    got += 1
                break
    print(f"FY{fy}: p{pg}  {scale:<10} {got}/{len(WANT)} lines")

years = sorted({y for d in rows.values() for y in d})
with open(P/"records/trend_10y.csv", "w", newline="") as fh:
    w = csv.writer(fh)
    w.writerow(["line_item", "unit"] + [f"FY{y}" for y in years])
    for key, _ in WANT:
        d = rows.get(key, {})
        if d: w.writerow([key, "INR lakh"] + [d.get(y, "") for y in years])
json.dump({"provenance": prov, "statement_meta": {str(k): v for k, v in meta.items()}},
          open(P/"records/trend_provenance.json", "w"), indent=1)
print(f"\nrecords/trend_10y.csv — {len(rows)} line items x {len(years)} years")
