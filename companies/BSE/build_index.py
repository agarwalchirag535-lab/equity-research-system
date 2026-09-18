#!/usr/bin/env python3
"""Per-AR section + note index, so later waves jump instead of scanning.
sect.4a trigger 4: same operation across 9 documents."""
import re, pathlib, json
P = pathlib.Path(__file__).parent
TXT = P/"data/text"; OUT = P/"data/index"; OUT.mkdir(exist_ok=True)

SECTIONS = [
 ("auditor_standalone", r"INDEPENDENT AUDITOR'?S REPORT"),
 ("balance_sheet",      r"^\s*BALANCE SHEET AS AT|Balance Sheet as at"),
 ("profit_loss",        r"STATEMENT OF PROFIT AND LOSS|Statement of Profit and Loss for"),
 ("cash_flow",          r"(?:STATEMENT OF )?CASH FLOW STATEMENT|Statement of Cash Flows?"),
 ("equity_changes",     r"STATEMENT OF CHANGES IN EQUITY"),
 ("accounting_policies",r"(?:Significant|Material) [Aa]ccounting [Pp]olic"),
 ("notes_to_accounts",  r"NOTES? (?:TO|FORMING PART OF) THE (?:STANDALONE |CONSOLIDATED )?FINANCIAL"),
 ("segment",            r"[Ss]egment [Rr]eporting|[Oo]perating [Ss]egments"),
 ("related_party",      r"[Rr]elated [Pp]arty (?:[Dd]isclosur|[Tt]ransaction)"),
 ("contingent",         r"[Cc]ontingent [Ll]iabilit"),
 ("board_report",       r"BOARD'?S REPORT|DIRECTORS'? REPORT"),
 ("corp_governance",    r"(?:REPORT ON )?CORPORATE GOVERNANCE"),
 ("mda",                r"MANAGEMENT DISCUSSION AND ANALYSIS"),
 ("remuneration",       r"[Rr]emuneration of (?:[Dd]irectors|[Mm]anagerial)|Section 197"),
 ("csr",                r"(?:ANNUAL REPORT ON )?CSR|Corporate Social Responsib"),
 ("consolidated",       r"CONSOLIDATED FINANCIAL STATEMENT"),
 ("bsr",                r"BUSINESS RESPONSIBILITY"),
 ("subsidiaries_aoc1",  r"\bAOC\s*-?\s*1\b|Salient features of the financial statement of subsidiar"),
]

def pages(txt):
    out=[]
    for m in re.finditer(r"===== PDF PAGE (\d+) =====\n(.*?)(?=\n===== PDF PAGE |\Z)", txt, re.S):
        out.append((int(m.group(1)), m.group(2)))
    return out

for f in sorted(TXT.glob("*.txt")):
    fy = f.stem[9:15]
    pgs = pages(f.read_text())
    idx = {"fy": fy, "pdf_pages": len(pgs), "sections": {}, "notes": {}, "printed_map": None}
    for key, pat in SECTIONS:
        rx = re.compile(pat)
        hits = [p for p, t in pgs if rx.search(t)]
        if hits: idx["sections"][key] = hits[:12]
    # note-number -> title, from the notes region
    noterx = re.compile(r"^\s*(\d{1,2}(?:\.\d)?)\s{1,6}([A-Z][A-Za-z ,&/()\-']{6,60})\s*$", re.M)
    for p, t in pgs:
        for m in noterx.finditer(t):
            n, title = m.group(1), m.group(2).strip()
            if n not in idx["notes"]:
                idx["notes"][n] = {"title": title, "pdf_page": p}
    # printed-page offset: find a page whose text contains a plausible printed number
    for p, t in pgs[10:60]:
        m = re.search(r"\n\s*(\d{1,3})\s*$", t)
        if m:
            pr = int(m.group(1))
            if 1 <= pr <= len(pgs) and abs((p - pr)) <= 12:
                idx["printed_map"] = {"pdf_page": p, "printed": pr, "offset": p - pr}
                break
    (OUT/f"{f.stem}.index.json").write_text(json.dumps(idx, indent=1))
    got = ", ".join(k for k in idx["sections"])
    print(f"FY{fy}: {len(pgs)}p, {len(idx['sections'])} sections, {len(idx['notes'])} notes, offset={idx['printed_map']}")
print("INDEX DONE")
