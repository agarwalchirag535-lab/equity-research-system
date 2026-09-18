#!/bin/zsh
# Downloads BSE Ltd annual reports from NSE. Unzips FY2023-and-earlier ZIPs (format boundary
# documented in the implementation repo: FY2024+ are bare PDF, earlier are ZIP).
set -u
P=~/Desktop/equity-research-system/companies/BSE
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
J=/Users/chiragagarwal/.claude/jobs/4d489f4a/tmp/nse.jar
cd "$P"/data/bronze
python3 - <<'PY' > /tmp/bse_urls.txt
import json
d=json.load(open('/Users/chiragagarwal/.claude/jobs/4d489f4a/tmp/bse_ar.json'))['data']
for r in d:
    fn=r.get('fileName') or ''
    if fn: print(r.get('toYr'), fn)
PY
while read -r yr url; do
  ext="${url##*.}"
  out="BSE-AR-FY${yr}.${ext}"
  [[ -s "$out" ]] && { echo "skip $out"; continue; }
  echo "get FY$yr ($ext) ..."
  curl -s -b "$J" -A "$UA" -H "Referer: https://www.nseindia.com/" -m 300 "$url" -o "$out"
  printf "  %s %s bytes  magic=%s\n" "$out" "$(stat -f%z "$out")" "$(xxd -p -l4 "$out")"
done < /tmp/bse_urls.txt
# unzip the archives
for z in *.zip; do
  [[ -e "$z" ]] || continue
  yr="${z%.zip}"; yr="${yr##*FY}"
  mkdir -p "unz_$yr" && unzip -o -q "$z" -d "unz_$yr" 2>/dev/null
  f=$(find "unz_$yr" -iname "*.pdf" -size +200k | head -1)
  [[ -n "$f" ]] && cp "$f" "BSE-AR-FY${yr}.pdf" && echo "  extracted BSE-AR-FY${yr}.pdf"
done
echo "DONE $(ls -1 BSE-AR-FY*.pdf 2>/dev/null | wc -l) PDFs"
