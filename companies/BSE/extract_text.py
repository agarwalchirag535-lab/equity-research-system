#!/usr/bin/env python3
"""One text extraction per AR, reused by every later wave (doctrine sect.7).
Justified as code by sect.4a trigger 4 - same operation across 9 documents."""
import pathlib, sys
try: from pypdf import PdfReader
except ImportError: from PyPDF2 import PdfReader
P = pathlib.Path(__file__).parent
out = P/"data/text"; out.mkdir(exist_ok=True)
for f in sorted((P/"data/bronze").glob("BSE-AR-FY*.pdf")):
    dest = out/(f.stem + ".txt")
    if dest.exists() and dest.stat().st_size > 10000:
        print(f"skip {dest.name}"); continue
    r = PdfReader(str(f)); parts=[]
    for i, pg in enumerate(r.pages, 1):
        try: txt = pg.extract_text() or ""
        except Exception as e: txt = f"[extract error: {e}]"
        parts.append(f"\n\n===== PDF PAGE {i} =====\n{txt}")
    dest.write_text("".join(parts))
    print(f"{dest.name}: {len(r.pages)} pages, {dest.stat().st_size//1024} KB")
print("EXTRACTION DONE")
