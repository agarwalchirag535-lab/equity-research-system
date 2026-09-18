#!/usr/bin/env python3
"""Subject-line index over 119 filing PDFs. Code justified by doctrine s.4a trigger 4
(same operation across many documents). Extraction of MEANING is not done here - only the
company's own Sub:/Subject: line is lifted verbatim, plus page count."""
import re, glob, os, json
rows=[]
for f in sorted(glob.glob('data/quarterly_text/*.txt')):
    t=open(f).read(); pages=len(re.findall(r'===== PDF PAGE', t))
    flat=re.sub(r'\s+',' ',t[:9000])
    m=re.search(r'\bSub(?:ject)?\s*[:\-–]\s*(.{10,300}?)(?:\s+(?:Dear|Ref\.|Respected|This is |Pursuant|With reference|In terms of|Please|We (?:wish|refer|hereby)|Enclosed))', flat, re.I)
    subj = m.group(1).strip() if m else ''
    if not subj:
        m2=re.search(r'\bSub(?:ject)?\s*[:\-–]\s*(.{10,220})', flat, re.I)
        subj = m2.group(1).strip() if m2 else '[no subject line found]'
    rows.append({"file":os.path.basename(f)[:-4], "date":os.path.basename(f)[:8], "pages":pages, "subject":re.sub(r'\s+',' ',subj)[:230]})
json.dump(rows, open('data/index/filing_index.json','w'), indent=1)
for r in rows: print(f"{r['date']} {r['pages']:3d}p {r['file'][:46]:46s} | {r['subject'][:120]}")
