#!/usr/bin/env python3
import pathlib
try: from pypdf import PdfReader
except ImportError: from PyPDF2 import PdfReader
P = pathlib.Path(__file__).parent
out = P/"data/concall_text"; out.mkdir(exist_ok=True)
for f in sorted((P/"data/concalls").glob("*.pdf")):
    d = out/(f.stem + ".txt")
    if d.exists() and d.stat().st_size > 2000: continue
    try:
        r = PdfReader(str(f))
        d.write_text("".join(f"\n\n===== PDF PAGE {i} =====\n{(p.extract_text() or '')}"
                            for i, p in enumerate(r.pages, 1)))
        head = (d.read_text()[:900]).replace("\n"," ")
        kind = "TRANSCRIPT" if "transcript" in head.lower() else ("PRESENTATION" if len(r.pages)>15 else "?")
        print(f"{f.name[:46]:<48} {len(r.pages):>3}p  {kind}")
    except Exception as e:
        print(f"{f.name}: ERROR {e}")
print("CONCALL EXTRACTION DONE")
