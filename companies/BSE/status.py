#!/usr/bin/env python3
"""Loop driver. Prints what is runnable now, what is blocked, and on what."""
import json, pathlib, sys
P = pathlib.Path(__file__).parent
u = json.loads((P/"state/progress.json").read_text())
by = {x["unit"]: x for x in u}
done = {x["unit"] for x in u if x["status"] == "verified"}
counts = {}
for x in u: counts[x["status"]] = counts.get(x["status"], 0) + 1

ready, waiting = [], []
for x in u:
    if x["status"] in ("verified", "blocked"): continue
    missing = [d for d in x["deps"] if d not in done]
    (waiting if missing else ready).append((x, missing))

print(f"BSE run — {counts.get('verified',0)}/{len(u)} verified"
      + (f", {counts['blocked']} blocked" if counts.get('blocked') else "")
      + f", {len(ready)} runnable now")
print()
if ready:
    print("RUNNABLE (wave order, parallel within wave):")
    for x, _ in sorted(ready, key=lambda r: (float(str(r[0]['wave']).replace('.', '.') or 0), r[0]['unit'])):
        g = "  [GATE]" if x["gate"] else ""
        print(f"  W{x['wave']:<4} {x['unit']:<22} att={x['attempts']}{g}")
        print(f"        {x['desc']}")
if waiting:
    print("\nWAITING:")
    for x, m in sorted(waiting, key=lambda r: str(r[0]['wave'])):
        print(f"  W{x['wave']:<4} {x['unit']:<22} needs {', '.join(m)}")
blocked = [x for x in u if x["status"] == "blocked"]
if blocked:
    print("\nBLOCKED:")
    for x in blocked: print(f"  {x['unit']}: {x['last_error']}")
