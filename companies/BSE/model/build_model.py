#!/usr/bin/env python3
"""Assemble the BSE financial model workbook."""
import openpyxl
from openpyxl.workbook.defined_name import DefinedName

import bse_data as D
import bse_style as S
from build_part1 import build_assumptions, A_ROW
from build_part2 import (build_segment, build_income_statement, build_balance_sheet,
                         patch_is_depreciation, SEG_ROW, IS_ROW, BS_ROW)
from build_part3 import build_dcf, build_comps, build_sensitivity, DCF_ROW

OUT = "BSE_Financial_Model.xlsx"


def main():
    wb = openpyxl.Workbook()
    # remove default sheet
    wb.remove(wb.active)

    # Build in dependency order (row maps populated as we go)
    build_assumptions(wb)          # 1
    build_segment(wb)              # references Assumptions
    build_income_statement(wb)     # references Segment + Assumptions
    build_balance_sheet(wb)        # references IS + Assumptions
    patch_is_depreciation(wb)      # resolve IS D&A -> BS schedule
    build_dcf(wb)                  # references IS + BS + Assumptions
    build_comps(wb)                # references IS + BS + Assumptions
    build_sensitivity(wb)          # references DCF

    # Enforce final sheet order per spec
    order = ["Assumptions", "Income Statement", "Balance Sheet", "Segment Revenue Build",
             "DCF Valuation", "Comps", "Sensitivity"]
    wb._sheets.sort(key=lambda ws: order.index(ws.title))

    # A couple of workbook-level named ranges for the headline outputs
    def named(name, sheet, cell):
        ref = f"'{sheet}'!{cell}"
        wb.defined_names.add(DefinedName(name, attr_text=ref))

    named("DCF_ValuePerShare", "DCF Valuation", f"$E${DCF_ROW['value_per_share']}")
    named("DCF_WACC", "DCF Valuation", f"$E${DCF_ROW['wacc']}")
    named("DCF_EnterpriseValue", "DCF Valuation", f"$E${DCF_ROW['ev']}")

    wb.save(OUT)
    print(f"Saved {OUT}")
    # emit row maps for the verifier
    import json
    with open("row_maps.json", "w") as fh:
        json.dump({"A_ROW": A_ROW, "SEG_ROW": {k: v for k, v in SEG_ROW.items() if k != 'peers'},
                   "IS_ROW": IS_ROW, "BS_ROW": BS_ROW, "DCF_ROW": DCF_ROW}, fh, indent=2, default=str)
    print("Wrote row_maps.json")


if __name__ == "__main__":
    main()
