#!/bin/zsh
set -u
P=~/Desktop/equity-research-system/companies/BSE
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
J=/tmp/nse_bse.jar
mkdir -p "$P"/data/filings
curl -s -c $J -A "$UA" "https://www.nseindia.com/companies-listing/corporate-filings-announcements" -o /dev/null -m 30
get () { # name url
  curl -s -b $J -A "$UA" -H "Referer: https://www.nseindia.com/companies-listing/corporate-filings-announcements" \
    -H "Accept: application/json" -m 60 "$2" -o "$P/data/filings/$1.json" -w "$1 http=%{http_code} bytes=%{size_download}\n"
}
get announcements_2026 "https://www.nseindia.com/api/corporate-announcements?index=equities&symbol=BSE&from_date=01-01-2026&to_date=07-09-2026"
get announcements_2025 "https://www.nseindia.com/api/corporate-announcements?index=equities&symbol=BSE&from_date=01-01-2025&to_date=31-12-2025"
get announcements_2024 "https://www.nseindia.com/api/corporate-announcements?index=equities&symbol=BSE&from_date=01-01-2024&to_date=31-12-2024"
get shareholding    "https://www.nseindia.com/api/corporate-share-holdings-master?index=equities&symbol=BSE"
get results         "https://www.nseindia.com/api/corporates-financial-results?index=equities&symbol=BSE&period=Quarterly"
get corp_info       "https://www.nseindia.com/api/quote-equity?symbol=BSE"
echo "FILINGS DONE"
