#!/bin/zsh
P=~/Desktop/equity-research-system/companies/BSE
until [ "$(ls $P/data/text/*.txt 2>/dev/null | wc -l | tr -d ' ')" -ge 9 ]; do sleep 10; done
echo "=== AR extraction complete (9/9) ==="
python3 "$P"/build_index.py
echo "=== concall text ==="
python3 "$P"/extract_concalls.py
echo "PREP COMPLETE"
