#!/usr/bin/env python3
"""mark.py <unit> <verified|pending|in_progress|blocked> [artifact] [error]"""
import json, pathlib, sys
P = pathlib.Path(__file__).parent
f = P/"state/progress.json"
u = json.loads(f.read_text())
unit, st = sys.argv[1], sys.argv[2]
art = sys.argv[3] if len(sys.argv) > 3 else None
err = sys.argv[4] if len(sys.argv) > 4 else None
done = {x["unit"] for x in u if x["status"] == "verified"}
hit = False
for x in u:
    if x["unit"] == unit:
        hit = True
        if st == "in_progress":
            missing = [d for d in x["deps"] if d not in done]
            if missing and "--override" not in sys.argv:
                sys.exit(f"REFUSED: {unit} has unverified deps: {', '.join(missing)}. "
                         f"Re-run with --override <reason> to dispatch anyway (it will be logged).")
            if missing:
                x["dep_override"] = f"dispatched with unverified deps {missing}: " + " ".join(sys.argv[sys.argv.index('--override')+1:])
            x["attempts"] += 1
        x["status"] = st
        if art: x["artifact"] = art
        x["last_error"] = err
        if st == "blocked" and x["attempts"] < 3:
            print(f"warning: blocking {unit} at {x['attempts']} attempts (<3)")
if not hit: sys.exit(f"no such unit: {unit}")
f.write_text(json.dumps(u, indent=2))
print(f"{unit} -> {st}")
