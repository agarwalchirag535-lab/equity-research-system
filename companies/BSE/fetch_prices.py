#!/usr/bin/env python3
"""Month-end close series for BSE from NSE's static bhavcopy archive.
Uses curl, not urllib: urllib is blocked on this host where curl with browser headers is not
(verified 2026-09-08 - the same URL returns the file via curl and nothing via urllib).
Non-trading days walk back up to 6 days; a month with no file is left absent, never interpolated."""
import csv, io, zipfile, subprocess, datetime, pathlib, calendar, tempfile, os
P = pathlib.Path(__file__).parent
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
URL = "https://nsearchives.nseindia.com/content/cm/BhavCopy_NSE_CM_0_0_0_{}_F_0000.csv.zip"

def fetch(d):
    tmp = tempfile.mktemp(suffix=".zip")
    subprocess.run(["curl","-s","-A",UA,"-H","Referer: https://www.nseindia.com/","-m","45",
                    URL.format(d.strftime("%Y%m%d")),"-o",tmp], capture_output=True)
    try:
        raw = open(tmp,"rb").read()
        if raw[:4] != b"PK\x03\x04": return None
        z = zipfile.ZipFile(io.BytesIO(raw))
        txt = z.read(z.namelist()[0]).decode("utf-8","ignore")
        for r in csv.DictReader(io.StringIO(txt)):
            if r.get("TckrSymb")=="BSE" and r.get("SctySrs")=="EQ": return r
        return None
    finally:
        if os.path.exists(tmp): os.remove(tmp)

out=[]; today=datetime.date(2026,9,4)
months=[]; y,m=2024,9
while (y,m)<=(2026,9):
    months.append((y,m)); m+=1
    if m==13: y,m=y+1,1
for y,m in months:
    last=datetime.date(y,m,calendar.monthrange(y,m)[1])
    if last>today: last=today
    rec=None
    for back in range(7):
        rec=fetch(last-datetime.timedelta(days=back))
        if rec: break
    if rec:
        out.append({"date":rec["TradDt"],"close":float(rec["ClsPric"]),"high":float(rec["HghPric"]),
                    "low":float(rec["LwPric"]),"volume":int(rec["TtlTradgVol"]),
                    "turnover_inr":float(rec["TtlTrfVal"])})
        print(f"  {rec['TradDt']}  {float(rec['ClsPric']):>9,.2f}")
    else:
        print(f"  {y}-{m:02d}  ABSENT (not interpolated)")
with open(P/"records/price_series.csv","w",newline="") as fh:
    w=csv.DictWriter(fh,fieldnames=["date","close","high","low","volume","turnover_inr"])
    w.writeheader(); w.writerows(out)
print(f"\n{len(out)} month-end observations")
