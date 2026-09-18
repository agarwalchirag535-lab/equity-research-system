#!/usr/bin/env python3
"""One text extraction per PDF, reused by every later wave (doctrine s.7 'one read, many uses').
Justified as code by s.4a trigger 4 - same operation across 120+ documents."""
import pathlib, sys
try: from pypdf import PdfReader
except ImportError: from PyPDF2 import PdfReader
P = pathlib.Path(__file__).parent
JOBS = [("data/bronze","data/text"), ("data/ipo","data/text"), ("data/quarterly","data/quarterly_text"), ("data/peers","data/peer_text")]
for src, dst in JOBS:
    s, d = P/src, P/dst; d.mkdir(parents=True, exist_ok=True)
    if not s.exists(): continue
    for f in sorted(s.glob("*.pdf")):
        dest = d/(f.stem + ".txt")
        if dest.exists() and dest.stat().st_size > 4000: print(f"skip {dest.name}", flush=True); continue
        try:
            r = PdfReader(str(f)); npages = len(r.pages)
        except Exception as e: print(f"FAIL {f.name}: {e}", flush=True); continue
        parts=[]
        for i, pg in enumerate(r.pages, 1):
            try: txt = pg.extract_text() or ""
            except Exception as e: txt = f"[extract error: {e}]"
            parts.append(f"\n\n===== PDF PAGE {i} =====\n{txt}")
        dest.write_text("".join(parts))
        print(f"{dest.name}: {npages}p {dest.stat().st_size//1024}KB", flush=True)
print("EXTRACTION DONE", flush=True)
