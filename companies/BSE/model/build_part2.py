"""BSE model builder — part 2: Segment Revenue Build, Income Statement, Balance Sheet."""
from openpyxl.utils import get_column_letter as gcl
import bse_data as D
import bse_style as S
from build_part1 import (COL_FY, COL_LBL, COL_NOTE, HIST, PROJ, YEARS, colL, aref, A_ROW)

SEG_ROW = {}
IS_ROW = {}
BS_ROW = {}


def _hdr(ws, r, ncols):
    S.label(ws, f"A{r}", "Rs Crore", bold=True)
    S.year_header(ws, r, COL_FY["FY24"], YEARS, hist_count=3)
    S.label(ws, f"H{r}", "Source / formula basis", bold=True)


def _widths(ws):
    ws.column_dimensions["A"].width = 42
    for c in "BCDEFG":
        ws.column_dimensions[c].width = 13
    ws.column_dimensions["H"].width = 50


# =====================================================================
# SEGMENT REVENUE BUILD
# =====================================================================
def build_segment(wb):
    ws = wb.create_sheet("Segment Revenue Build")
    ws.sheet_properties.tabColor = "FF70AD47"
    ncols = 8
    S.title_block(ws, "BSE Ltd — Segment Revenue Build",
                  "Revenue disaggregated by segment. Historical = STANDALONE MD&A split (the only "
                  "disclosed granularity), flagged. Projected = driver formulas referencing Assumptions.",
                  "Units: Rs Crore. Transaction charges = ADTO x trading days x yield(bps)/10000. "
                  "Historical actuals in blue.", ncols)
    _widths(ws)
    r = 5
    _hdr(ws, r, ncols); r += 1

    def segrow(key, lbl, hist_lakh, proj_formulas, note, *, bold=False, indent=1, fmt=S.FMT_CR):
        nonlocal r
        SEG_ROW[key] = r
        S.label(ws, f"A{r}", lbl, bold=bold, indent=indent)
        # historical actuals (blue), converted lakh->crore
        if hist_lakh is not None:
            for i, fy in enumerate(HIST):
                v = hist_lakh[i]
                if v is not None:
                    S.set_cell(ws, f"{colL(fy)}{r}", D.cr(v), fmt=fmt, input_cell=True)
        # projected formulas
        if proj_formulas is not None:
            for i, fy in enumerate(PROJ):
                f = proj_formulas[i]
                if f is not None:
                    S.set_cell(ws, f"{colL(fy)}{r}", f, fmt=fmt)
        if note:
            S.label(ws, f"H{r}", note, italic=True, size=8, color="FF555555")
        r += 1

    S.section(ws, r, "TRANSACTION CHARGES", ncols); r += 1

    # Equity derivatives: ADTO * days * yield/10000, ADTO grown by assumption
    # projected ADTO built inline referencing Assumptions ADTO + growth.
    def deriv_formula(fy, prev_fy):
        # derivative txn = ADTO * trading days * take-rate fraction
        return (f"={aref('adto_deriv', fy)}*{aref('trading_days', fy)}*"
                f"{aref('yld_deriv', fy)}")

    segrow("txn_equity_derivatives", "Equity derivatives txn charges",
           D.SEG_ACTUALS_LAKH["txn_equity_derivatives"],
           [deriv_formula("FY27E", "FY26"), deriv_formula("FY28E", "FY27E"), deriv_formula("FY29E", "FY28E")],
           "= deriv ADTO x days x yield(bps)/10000. ADTO & yield from Assumptions.")

    def cash_formula(fy):
        return (f"={aref('adto_cash', fy)}*{aref('trading_days', fy)}*"
                f"{aref('yld_cash', fy)}")
    segrow("txn_equity_cash", "Equity cash txn charges",
           D.SEG_ACTUALS_LAKH["txn_equity_cash"],
           [cash_formula("FY27E"), cash_formula("FY28E"), cash_formula("FY29E")],
           "= cash ADTO x days x yield(bps)/10000.")

    # Currency derivatives + SLB: not separately disclosed -> reference editable Assumptions inputs
    segrow("txn_currency", "Currency derivatives txn charges",
           [0.0, 0.0, 0.0],
           [f"={aref('currency_txn','FY27E')}", f"={aref('currency_txn','FY28E')}",
            f"={aref('currency_txn','FY29E')}"],
           "NOT-DISCLOSED in MD&A split -> AR audited Note 22. References Assumptions (default 0).")

    segrow("txn_slb", "SLB (securities lending) txn charges",
           [0.0, 0.0, 0.0],
           [f"={aref('slb_txn','FY27E')}", f"={aref('slb_txn','FY28E')}",
            f"={aref('slb_txn','FY29E')}"],
           "NOT-DISCLOSED separately -> AR audited Note 22. References Assumptions (default 0).")

    segrow("txn_starmf", "StAR MF platform fees",
           D.SEG_ACTUALS_LAKH["txn_starmf"], [None, None, None],
           "= prior x (1 + StAR MF growth). MF platform, part of txn charges line.")
    sr = SEG_ROW["txn_starmf"]
    S.set_cell(ws, f"E{sr}", f"=D{sr}*(1+{aref('g_starmf','FY27E')})", fmt=S.FMT_CR)
    S.set_cell(ws, f"F{sr}", f"=E{sr}*(1+{aref('g_starmf','FY28E')})", fmt=S.FMT_CR)
    S.set_cell(ws, f"G{sr}", f"=F{sr}*(1+{aref('g_starmf','FY29E')})", fmt=S.FMT_CR)

    # Transaction charges total = sum of components (same-sheet -> black)
    rows = [SEG_ROW[k] for k in ["txn_equity_derivatives", "txn_equity_cash", "txn_currency",
                                 "txn_slb", "txn_starmf"]]
    SEG_ROW["txn_charges_total"] = r
    S.label(ws, f"A{r}", "Transaction charges — total", bold=True, indent=0)
    # historical actual total (blue) where disclosed
    for i, fy in enumerate(HIST):
        v = D.SEG_ACTUALS_LAKH["txn_charges_total"][i]
        if v is not None:
            # use a SUM formula over components so it recalculates (components are actuals)
            comp = "+".join(f"{colL(fy)}{rr}" for rr in rows)
            S.set_cell(ws, f"{colL(fy)}{r}", f"={comp}", fmt=S.FMT_CR, bold=True)
    for fy in PROJ:
        comp = "+".join(f"{colL(fy)}{rr}" for rr in rows)
        S.set_cell(ws, f"{colL(fy)}{r}", f"={comp}", fmt=S.FMT_CR, bold=True)
    S.label(ws, f"H{r}", "Sum of components (same-sheet).", italic=True, size=8, color="FF555555")
    r += 1

    S.section(ws, r, "NON-TRANSACTION REVENUE", ncols); r += 1

    segrow("listing_fees", "Listing fees (annual + processing)",
           D.SEG_ACTUALS_LAKH["listing_fees"], [None, None, None],
           "= prior x (1 + listing growth). Linked to IPO/listings pipeline.")
    # listing projected chain
    lr = SEG_ROW["listing_fees"]
    S.set_cell(ws, f"E{lr}", f"=D{lr}*(1+{aref('g_listing','FY27E')})", fmt=S.FMT_CR)
    S.set_cell(ws, f"F{lr}", f"=E{lr}*(1+{aref('g_listing','FY28E')})", fmt=S.FMT_CR)
    S.set_cell(ws, f"G{lr}", f"=F{lr}*(1+{aref('g_listing','FY29E')})", fmt=S.FMT_CR)

    segrow("book_building_fees", "Book building / IPO fees",
           D.SEG_ACTUALS_LAKH["book_building_fees"], [None, None, None],
           "= prior x (1 + book-building growth).")
    br = SEG_ROW["book_building_fees"]
    S.set_cell(ws, f"E{br}", f"=D{br}*(1+{aref('g_bookbuild','FY27E')})", fmt=S.FMT_CR)
    S.set_cell(ws, f"F{br}", f"=E{br}*(1+{aref('g_bookbuild','FY28E')})", fmt=S.FMT_CR)
    S.set_cell(ws, f"G{br}", f"=F{br}*(1+{aref('g_bookbuild','FY29E')})", fmt=S.FMT_CR)

    # Data feed & index licensing — seed from colocation actual as proxy for the disclosed data line
    segrow("data_index", "Data feed & index licensing income",
           D.SEG_ACTUALS_LAKH["colocation_income"], [None, None, None],
           "Asia Index/S&P BSE + colocation/data feed. = prior x (1 + data growth).")
    dr = SEG_ROW["data_index"]
    S.set_cell(ws, f"E{dr}", f"=D{dr}*(1+{aref('g_data','FY27E')})", fmt=S.FMT_CR)
    S.set_cell(ws, f"F{dr}", f"=E{dr}*(1+{aref('g_data','FY28E')})", fmt=S.FMT_CR)
    S.set_cell(ws, f"G{dr}", f"=F{dr}*(1+{aref('g_data','FY29E')})", fmt=S.FMT_CR)

    # Other operating income (residual, ex-colocation which we broke into data_index)
    # historical: other_operating_income - colocation
    SEG_ROW["other_operating"] = r
    S.label(ws, f"A{r}", "Other operating income (residual)", indent=1)
    for i, fy in enumerate(HIST):
        oo = D.SEG_ACTUALS_LAKH["other_operating_income"][i]
        co = D.SEG_ACTUALS_LAKH["colocation_income"][i]
        if oo is not None and co is not None:
            S.set_cell(ws, f"{colL(fy)}{r}", D.cr(oo - co), fmt=S.FMT_CR, input_cell=True)
    S.set_cell(ws, f"E{r}", f"=D{r}*(1+{aref('g_other_op','FY27E')})", fmt=S.FMT_CR)
    S.set_cell(ws, f"F{r}", f"=E{r}*(1+{aref('g_other_op','FY28E')})", fmt=S.FMT_CR)
    S.set_cell(ws, f"G{r}", f"=F{r}*(1+{aref('g_other_op','FY29E')})", fmt=S.FMT_CR)
    S.label(ws, f"H{r}", "Other operating income less colocation (moved to data line).",
            italic=True, size=8, color="FF555555")
    r += 1

    S.section(ws, r, "REVENUE FROM OPERATIONS (recomputed)", ncols); r += 1
    # Revenue from operations (standalone-basis build) = txn total + listing + book + data + other
    build_rows = [SEG_ROW[k] for k in ["txn_charges_total", "listing_fees", "book_building_fees",
                                        "data_index", "other_operating"]]
    SEG_ROW["rev_ops_build"] = r
    S.label(ws, f"A{r}", "Revenue from operations (build)", bold=True, indent=0)
    for fy in YEARS:
        comp = "+".join(f"{colL(fy)}{rr}" for rr in build_rows)
        S.set_cell(ws, f"{colL(fy)}{r}", f"={comp}", fmt=S.FMT_CR, bold=True)
    S.label(ws, f"H{r}", "Sum of all segment lines (same-sheet). Feeds Income Statement.",
            italic=True, size=8, color="FF555555")
    r += 1

    # Investment / treasury income = corpus * yield
    S.section(ws, r, "INVESTMENT / TREASURY INCOME", ncols); r += 1
    SEG_ROW["investment_income"] = r
    S.label(ws, f"A{r}", "Investment / treasury income", bold=True, indent=0)
    for i, fy in enumerate(HIST):
        S.set_cell(ws, f"{colL(fy)}{r}", D.cr(D.IS_ACTUALS_LAKH["investment_income"][i]),
                   fmt=S.FMT_CR, input_cell=True)
    for fy in PROJ:
        S.set_cell(ws, f"{colL(fy)}{r}",
                   f"={aref('inv_corpus', fy)}*{aref('inv_yield', fy)}", fmt=S.FMT_CR)
    S.label(ws, f"H{r}", "= investable corpus (incl SGF) x investment yield. From Assumptions.",
            italic=True, size=8, color="FF555555")
    r += 1

    # reconciliation note: consolidated vs standalone-build
    SEG_ROW["consol_scalar"] = r
    S.label(ws, f"A{r}", "Consolidation scalar (consol/standalone)", indent=1, italic=True)
    # FY24 standalone split undisclosed -> no scalar (blank). FY25/FY26 computed.
    for i, fy in enumerate(HIST):
        if fy == "FY24":
            continue
        consol = D.REV_OPS_CONSOL_LAKH[i]
        S.set_cell(ws, f"{colL(fy)}{r}",
                   f"={D.cr(consol)}/{colL(fy)}{SEG_ROW['rev_ops_build']}", fmt=S.FMT_X)
    for fy in PROJ:
        # hold FY26 scalar flat into projection
        S.set_cell(ws, f"{colL(fy)}{r}", f"=$D${r}", fmt=S.FMT_X)
    S.label(ws, f"H{r}", "Consol rev / standalone-build rev. FY24 build undisclosed so scalar blank.",
            italic=True, size=8, color="FF555555")
    r += 1

    SEG_ROW["rev_ops_consol"] = r
    S.label(ws, f"A{r}", "Revenue from operations (consolidated)", bold=True, indent=0)
    for fy in YEARS:
        if fy == "FY24":
            # direct consolidated actual (blue) — standalone split not disclosed for FY24
            S.set_cell(ws, f"{colL(fy)}{r}", D.cr(D.REV_OPS_CONSOL_LAKH[0]),
                       fmt=S.FMT_CR, input_cell=True, bold=True)
        else:
            S.set_cell(ws, f"{colL(fy)}{r}",
                       f"={colL(fy)}{SEG_ROW['rev_ops_build']}*{colL(fy)}{SEG_ROW['consol_scalar']}",
                       fmt=S.FMT_CR, bold=True)
    S.label(ws, f"H{r}", "FY24 = direct consolidated actual (no split disclosed). "
            "FY25-FY29 = build x consolidation scalar. Feeds Income Statement.",
            italic=True, size=8, color="FF555555")
    r += 1

    ws.freeze_panes = "B6"
    SEG_ROW["__end__"] = r
    return ws


# =====================================================================
# INCOME STATEMENT
# =====================================================================
def build_income_statement(wb):
    ws = wb.create_sheet("Income Statement")
    ws.sheet_properties.tabColor = "FF4472C4"
    ncols = 8
    S.title_block(ws, "BSE Ltd — Consolidated Income Statement",
                  "FY24-FY26 actuals (blue). FY27E-FY29E projected via Assumptions + Segment build. "
                  "Revenue links (green) from Segment Revenue Build.",
                  "Units: Rs Crore. Consolidated basis.", ncols)
    _widths(ws)
    r = 5
    _hdr(ws, r, ncols); r += 1

    SEG = SEG_ROW

    def isrow(key, lbl, hist_key_lakh, proj_formulas, note, *, bold=False, indent=1,
              fmt=S.FMT_CR, hist_formulas=None):
        nonlocal r
        IS_ROW[key] = r
        S.label(ws, f"A{r}", lbl, bold=bold, indent=indent)
        # historical
        if hist_formulas is not None:
            for i, fy in enumerate(HIST):
                f = hist_formulas[i]
                if f is not None:
                    S.set_cell(ws, f"{colL(fy)}{r}", f, fmt=fmt, bold=bold)
        elif hist_key_lakh is not None:
            vals = D.IS_ACTUALS_LAKH[hist_key_lakh]
            for i, fy in enumerate(HIST):
                if vals[i] is not None:
                    S.set_cell(ws, f"{colL(fy)}{r}", D.cr(vals[i]), fmt=fmt, input_cell=True, bold=bold)
        if proj_formulas is not None:
            for i, fy in enumerate(PROJ):
                f = proj_formulas[i]
                if f is not None:
                    S.set_cell(ws, f"{colL(fy)}{r}", f, fmt=fmt, bold=bold)
        if note:
            S.label(ws, f"H{r}", note, italic=True, size=8, color="FF555555")
        r += 1

    S.section(ws, r, "INCOME", ncols); r += 1

    # Revenue from operations: link (green) to Segment build consolidated line, ALL years
    IS_ROW["revenue"] = r
    S.label(ws, f"A{r}", "Revenue from operations", bold=True, indent=0)
    for fy in YEARS:
        S.set_cell(ws, f"{colL(fy)}{r}",
                   f"='Segment Revenue Build'!{colL(fy)}{SEG['rev_ops_consol']}",
                   fmt=S.FMT_CR, bold=True)
    S.label(ws, f"H{r}", "Link to Segment Revenue Build (consolidated line).",
            italic=True, size=8, color="FF555555")
    r += 1

    # Investment income: link (green) to segment investment line
    IS_ROW["investment_income"] = r
    S.label(ws, f"A{r}", "Investment / treasury income", indent=1)
    for fy in YEARS:
        S.set_cell(ws, f"{colL(fy)}{r}",
                   f"='Segment Revenue Build'!{colL(fy)}{SEG['investment_income']}", fmt=S.FMT_CR)
    S.label(ws, f"H{r}", "Link to Segment Revenue Build investment income.",
            italic=True, size=8, color="FF555555")
    r += 1

    isrow("other_income", "Other income", "other_income",
          [f"=D{r}*(1+{aref('g_other_op','FY27E')})",
           f"=E{r}*(1+{aref('g_other_op','FY28E')})",
           f"=F{r}*(1+{aref('g_other_op','FY29E')})"],
          "Other income grown at other-op growth (Assumptions).")

    IS_ROW["total_income"] = r
    S.label(ws, f"A{r}", "Total income", bold=True, indent=0)
    for fy in YEARS:
        S.set_cell(ws, f"{colL(fy)}{r}",
                   f"={colL(fy)}{IS_ROW['revenue']}+{colL(fy)}{IS_ROW['investment_income']}+{colL(fy)}{IS_ROW['other_income']}",
                   fmt=S.FMT_CR, bold=True)
    S.label(ws, f"H{r}", "Revenue + investment income + other income.", italic=True, size=8, color="FF555555")
    r += 1

    S.section(ws, r, "EXPENSES", ncols); r += 1

    rev = IS_ROW["revenue"]
    txn_ref = f"'Segment Revenue Build'!{{c}}{SEG['txn_charges_total']}"

    isrow("employee", "Employee benefits expense", "employee_benefits",
          [f"=D{r}*(1+{aref('g_emp','FY27E')})",
           f"=E{r}*(1+{aref('g_emp','FY28E')})",
           f"=F{r}*(1+{aref('g_emp','FY29E')})"],
          "Prior x (1 + employee growth).")
    isrow("technology", "Technology & other operating expense", "technology_expense",
          [f"=D{r}*(1+{aref('g_tech','FY27E')})",
           f"=E{r}*(1+{aref('g_tech','FY28E')})",
           f"=F{r}*(1+{aref('g_tech','FY29E')})"],
          "Prior x (1 + technology growth).")
    # SEBI regulatory fee: % of transaction charges (link green to segment txn total)
    isrow("sebi_fee", "SEBI / regulatory fees", "sebi_regulatory_fee",
          [f"='Segment Revenue Build'!E{SEG['txn_charges_total']}*{aref('sebi_fee_pct','FY27E')}",
           f"='Segment Revenue Build'!F{SEG['txn_charges_total']}*{aref('sebi_fee_pct','FY28E')}",
           f"='Segment Revenue Build'!G{SEG['txn_charges_total']}*{aref('sebi_fee_pct','FY29E')}"],
          "% of transaction charges (SEBI turnover fee). Link to Segment build.")
    # Clearing & settlement: % of transaction charges
    isrow("clearing", "Clearing & settlement expense", "clearing_settlement",
          [f"='Segment Revenue Build'!E{SEG['txn_charges_total']}*{aref('clearing_pct','FY27E')}",
           f"='Segment Revenue Build'!F{SEG['txn_charges_total']}*{aref('clearing_pct','FY28E')}",
           f"='Segment Revenue Build'!G{SEG['txn_charges_total']}*{aref('clearing_pct','FY29E')}"],
          "% of transaction charges. Link to Segment build.")
    isrow("core_sgf", "Core SGF contribution", "core_sgf_contribution",
          [f"=D{r}*(1+{aref('g_admin','FY27E')})",
           f"=E{r}*(1+{aref('g_admin','FY28E')})",
           f"=F{r}*(1+{aref('g_admin','FY29E')})"],
          "Grown at admin growth (proxy).")
    isrow("admin", "Other administrative expenses", "other_admin_expenses",
          [f"=D{r}*(1+{aref('g_admin','FY27E')})",
           f"=E{r}*(1+{aref('g_admin','FY28E')})",
           f"=F{r}*(1+{aref('g_admin','FY29E')})"],
          "Prior x (1 + admin growth).")

    # D&A links to BS schedule later; for now compute as % of opening net block via BS.
    # We'll set D&A as a link to Balance Sheet depreciation schedule (green). Placeholder row.
    IS_ROW["depreciation"] = r
    S.label(ws, f"A{r}", "Depreciation & amortisation", indent=1)
    for i, fy in enumerate(HIST):
        S.set_cell(ws, f"{colL(fy)}{r}", D.cr(D.IS_ACTUALS_LAKH["depreciation"][i]),
                   fmt=S.FMT_CR, input_cell=True)
    for fy in PROJ:
        S.set_cell(ws, f"{colL(fy)}{r}", f"='Balance Sheet'!{colL(fy)}{{DA}}", fmt=S.FMT_CR)
    S.label(ws, f"H{r}", "Projected D&A links to Balance Sheet depreciation schedule.",
            italic=True, size=8, color="FF555555")
    r += 1

    # Total expenses = sum of the expense rows above (same-sheet)
    exp_keys = ["employee", "technology", "sebi_fee", "clearing", "core_sgf", "admin", "depreciation"]
    IS_ROW["total_expenses"] = r
    S.label(ws, f"A{r}", "Total expenses", bold=True, indent=0)
    for fy in YEARS:
        comp = "+".join(f"{colL(fy)}{IS_ROW[k]}" for k in exp_keys)
        S.set_cell(ws, f"{colL(fy)}{r}", f"={comp}", fmt=S.FMT_CR, bold=True)
    S.label(ws, f"H{r}", "Sum of expense lines (same-sheet).", italic=True, size=8, color="FF555555")
    r += 1

    S.section(ws, r, "PROFIT", ncols); r += 1

    # EBITDA = total income - (total expenses - depreciation)
    IS_ROW["ebitda"] = r
    S.label(ws, f"A{r}", "EBITDA", bold=True, indent=0)
    for fy in YEARS:
        S.set_cell(ws, f"{colL(fy)}{r}",
                   f"={colL(fy)}{IS_ROW['total_income']}-({colL(fy)}{IS_ROW['total_expenses']}-{colL(fy)}{IS_ROW['depreciation']})",
                   fmt=S.FMT_CR, bold=True)
    S.label(ws, f"H{r}", "Total income - operating expenses ex-D&A.", italic=True, size=8, color="FF555555")
    r += 1

    IS_ROW["ebit"] = r
    S.label(ws, f"A{r}", "EBIT", indent=0, bold=True)
    for fy in YEARS:
        S.set_cell(ws, f"{colL(fy)}{r}",
                   f"={colL(fy)}{IS_ROW['ebitda']}-{colL(fy)}{IS_ROW['depreciation']}",
                   fmt=S.FMT_CR, bold=True)
    S.label(ws, f"H{r}", "EBITDA - D&A.", italic=True, size=8, color="FF555555")
    r += 1

    isrow("finance_cost", "Finance cost", "finance_cost",
          [f"={aref('finance_cost','FY27E')}", f"={aref('finance_cost','FY28E')}",
           f"={aref('finance_cost','FY29E')}"],
          "BSE effectively debt-free; references Assumptions (default 0).", indent=1)
    isrow("associate", "Share of associate profit (CDSL)", "associate_profit",
          [f"=D{r}*(1+{aref('g_admin','FY27E')})",
           f"=E{r}*(1+{aref('g_admin','FY28E')})",
           f"=F{r}*(1+{aref('g_admin','FY29E')})"],
          "Associate (CDSL) equity-method profit; grown modestly.", indent=1)
    isrow("exceptional", "Exceptional items", "exceptional_items",
          [f"={aref('exceptional','FY27E')}", f"={aref('exceptional','FY28E')}",
           f"={aref('exceptional','FY29E')}"],
          "Non-recurring; references Assumptions (default 0).", indent=1)

    IS_ROW["pbt"] = r
    S.label(ws, f"A{r}", "Profit before tax", bold=True, indent=0)
    for fy in YEARS:
        S.set_cell(ws, f"{colL(fy)}{r}",
                   f"={colL(fy)}{IS_ROW['ebit']}-{colL(fy)}{IS_ROW['finance_cost']}+{colL(fy)}{IS_ROW['associate']}+{colL(fy)}{IS_ROW['exceptional']}",
                   fmt=S.FMT_CR, bold=True)
    S.label(ws, f"H{r}", "EBIT - finance cost + associate + exceptional.", italic=True, size=8, color="FF555555")
    r += 1

    isrow("tax", "Tax expense", "total_tax",
          [f"=E{IS_ROW['pbt']}*{aref('tax_rate','FY27E')}",
           f"=F{IS_ROW['pbt']}*{aref('tax_rate','FY28E')}",
           f"=G{IS_ROW['pbt']}*{aref('tax_rate','FY29E')}"],
          "PBT x effective tax rate (Assumptions).", indent=1)

    IS_ROW["pat"] = r
    S.label(ws, f"A{r}", "Profit after tax (total)", bold=True, indent=0)
    for fy in YEARS:
        S.set_cell(ws, f"{colL(fy)}{r}",
                   f"={colL(fy)}{IS_ROW['pbt']}-{colL(fy)}{IS_ROW['tax']}", fmt=S.FMT_CR, bold=True)
    S.label(ws, f"H{r}", "PBT - tax.", italic=True, size=8, color="FF555555")
    r += 1

    # EPS = PAT / shares (link to assumptions shares)
    IS_ROW["eps"] = r
    S.label(ws, f"A{r}", "EPS (Rs)", indent=1)
    for fy in YEARS:
        S.set_cell(ws, f"{colL(fy)}{r}",
                   f"={colL(fy)}{IS_ROW['pat']}/{aref('bse_shares')}", fmt=S.FMT_RS)
    S.label(ws, f"H{r}", "PAT / shares outstanding (Assumptions).", italic=True, size=8, color="FF555555")
    r += 1

    # Dividend = payout * PAT
    IS_ROW["dividend"] = r
    S.label(ws, f"A{r}", "Dividend declared", indent=1)
    for fy in YEARS:
        S.set_cell(ws, f"{colL(fy)}{r}",
                   f"={colL(fy)}{IS_ROW['pat']}*{aref('dividend_payout','FY27E')}", fmt=S.FMT_CR)
    S.label(ws, f"H{r}", "PAT x payout ratio (Assumptions).", italic=True, size=8, color="FF555555")
    r += 1

    # margin ratios
    S.section(ws, r, "MARGINS & CHECKS", ncols); r += 1
    IS_ROW["ebitda_margin"] = r
    S.label(ws, f"A{r}", "EBITDA margin (% of total income)", indent=1, italic=True)
    for fy in YEARS:
        S.set_cell(ws, f"{colL(fy)}{r}",
                   f"={colL(fy)}{IS_ROW['ebitda']}/{colL(fy)}{IS_ROW['total_income']}", fmt=S.FMT_PCT)
    r += 1
    IS_ROW["pat_margin"] = r
    S.label(ws, f"A{r}", "PAT margin (% of total income)", indent=1, italic=True)
    for fy in YEARS:
        S.set_cell(ws, f"{colL(fy)}{r}",
                   f"={colL(fy)}{IS_ROW['pat']}/{colL(fy)}{IS_ROW['total_income']}", fmt=S.FMT_PCT)
    r += 1

    ws.freeze_panes = "B6"
    IS_ROW["__end__"] = r
    # store DA row placeholder resolution happens in build_balance_sheet (needs BS DA row)
    return ws


# =====================================================================
# BALANCE SHEET (with capex/D&A schedule + working capital drivers)
# =====================================================================
def build_balance_sheet(wb):
    ws = wb.create_sheet("Balance Sheet")
    ws.sheet_properties.tabColor = "FFED7D31"
    ncols = 8
    S.title_block(ws, "BSE Ltd — Consolidated Balance Sheet",
                  "FY24-FY26 actuals (blue). FY27E-FY29E projected. Retained earnings link (green) to "
                  "Income Statement PAT & dividend. Capex/D&A schedule drives net block.",
                  "Units: Rs Crore. Consolidated basis. Balance check row must equal 0.", ncols)
    _widths(ws)
    r = 5
    _hdr(ws, r, ncols); r += 1

    IS = IS_ROW

    def bsrow(key, lbl, hist_key_lakh, proj_formulas, note, *, bold=False, indent=1, fmt=S.FMT_CR):
        nonlocal r
        BS_ROW[key] = r
        S.label(ws, f"A{r}", lbl, bold=bold, indent=indent)
        if hist_key_lakh is not None:
            vals = D.BS_ACTUALS_LAKH[hist_key_lakh]
            for i, fy in enumerate(HIST):
                if vals[i] is not None:
                    S.set_cell(ws, f"{colL(fy)}{r}", D.cr(vals[i]), fmt=fmt, input_cell=True, bold=bold)
        if proj_formulas is not None:
            for i, fy in enumerate(PROJ):
                f = proj_formulas[i]
                if f is not None:
                    S.set_cell(ws, f"{colL(fy)}{r}", f, fmt=fmt, bold=bold)
        if note:
            S.label(ws, f"H{r}", note, italic=True, size=8, color="FF555555")
        r += 1

    # ---------- CAPEX / D&A SCHEDULE ----------
    S.section(ws, r, "CAPEX & DEPRECIATION SCHEDULE", ncols); r += 1

    # Net block: opening = prior closing PPE
    BS_ROW["ppe_open"] = r
    S.label(ws, f"A{r}", "Net block — opening", indent=1, italic=True)
    # FY27E opening = FY26 closing PPE (actual). Others chain.
    S.set_cell(ws, f"E{r}", f"=D{{ppe_close}}", fmt=S.FMT_CR)  # patched after ppe_close known
    S.set_cell(ws, f"F{r}", f"=E{{ppe_close}}", fmt=S.FMT_CR)
    S.set_cell(ws, f"G{r}", f"=F{{ppe_close}}", fmt=S.FMT_CR)
    r += 1

    BS_ROW["capex"] = r
    S.label(ws, f"A{r}", "Capex", indent=1)
    for i, fy in enumerate(HIST):
        S.set_cell(ws, f"{colL(fy)}{r}", D.cr(abs(D.CF_ACTUALS_LAKH["capex_cash"][i])),
                   fmt=S.FMT_CR, input_cell=True)
    for fy in PROJ:
        S.set_cell(ws, f"{colL(fy)}{r}",
                   f"='Income Statement'!{colL(fy)}{IS['revenue']}*{aref('capex_pct', fy)}", fmt=S.FMT_CR)
    S.label(ws, f"H{r}", "Projected = revenue x capex% (Assumptions). Hist = cash-flow capex.",
            italic=True, size=8, color="FF555555")
    r += 1

    BS_ROW["da"] = r
    S.label(ws, f"A{r}", "Depreciation & amortisation", indent=1)
    for i, fy in enumerate(HIST):
        S.set_cell(ws, f"{colL(fy)}{r}", D.cr(D.IS_ACTUALS_LAKH["depreciation"][i]),
                   fmt=S.FMT_CR, input_cell=True)
    for fy in PROJ:
        S.set_cell(ws, f"{colL(fy)}{r}",
                   f"={colL(fy)}{BS_ROW['ppe_open']}*{aref('da_pct', fy)}", fmt=S.FMT_CR)
    S.label(ws, f"H{r}", "Projected = opening net block x D&A% (Assumptions).",
            italic=True, size=8, color="FF555555")
    r += 1

    BS_ROW["ppe_close"] = r
    S.label(ws, f"A{r}", "Net block — closing (PPE + CWIP)", bold=True, indent=1)
    for i, fy in enumerate(HIST):
        # actual PPE + CWIP
        val = D.BS_ACTUALS_LAKH["ppe"][i] + D.BS_ACTUALS_LAKH["cwip"][i]
        S.set_cell(ws, f"{colL(fy)}{r}", D.cr(val), fmt=S.FMT_CR, input_cell=True, bold=True)
    for fy in PROJ:
        S.set_cell(ws, f"{colL(fy)}{r}",
                   f"={colL(fy)}{BS_ROW['ppe_open']}+{colL(fy)}{BS_ROW['capex']}-{colL(fy)}{BS_ROW['da']}",
                   fmt=S.FMT_CR, bold=True)
    S.label(ws, f"H{r}", "Opening + capex - D&A. Hist = PPE + CWIP actual.",
            italic=True, size=8, color="FF555555")
    r += 1

    # patch ppe_open formulas now that ppe_close row known
    pc = BS_ROW["ppe_close"]
    ws[f"E{BS_ROW['ppe_open']}"].value = f"=D{pc}"
    ws[f"F{BS_ROW['ppe_open']}"].value = f"=E{pc}"
    ws[f"G{BS_ROW['ppe_open']}"].value = f"=F{pc}"

    # ---------- ASSETS ----------
    S.section(ws, r, "ASSETS", ncols); r += 1

    # Non-current assets ex-net-block held flat-growth; use actual then grow with revenue
    bsrow("other_nca", "Other non-current assets", None,
          [f"=D{r}*(1+{aref('inv_corpus_g','FY27E')})",
           f"=E{r}*(1+{aref('inv_corpus_g','FY28E')})",
           f"=F{r}*(1+{aref('inv_corpus_g','FY29E')})"],
          "Investments/other NCA grown at corpus growth.")
    # historical other_nca = total_noncurrent_assets - (ppe+cwip)
    onr = BS_ROW["other_nca"]
    for i, fy in enumerate(HIST):
        tot = D.BS_ACTUALS_LAKH["total_noncurrent_assets"][i]
        nb = D.BS_ACTUALS_LAKH["ppe"][i] + D.BS_ACTUALS_LAKH["cwip"][i]
        S.set_cell(ws, f"{colL(fy)}{onr}", D.cr(tot - nb), fmt=S.FMT_CR, input_cell=True)

    BS_ROW["total_nca"] = r
    S.label(ws, f"A{r}", "Total non-current assets", bold=True, indent=0)
    for fy in YEARS:
        S.set_cell(ws, f"{colL(fy)}{r}",
                   f"={colL(fy)}{BS_ROW['ppe_close']}+{colL(fy)}{BS_ROW['other_nca']}",
                   fmt=S.FMT_CR, bold=True)
    r += 1

    # Trade receivables = revenue * recv_days/365
    bsrow("receivables", "Trade receivables", "trade_receivables",
          [f"='Income Statement'!E{IS['revenue']}*{aref('recv_days','FY27E')}/365",
           f"='Income Statement'!F{IS['revenue']}*{aref('recv_days','FY28E')}/365",
           f"='Income Statement'!G{IS['revenue']}*{aref('recv_days','FY29E')}/365"],
          "Projected = revenue x receivable days / 365.")

    # Cash & other current assets: plug to make BS balance -> computed as balancing item
    # Other current assets (ex-cash) grow with revenue
    bsrow("other_ca", "Other current assets (ex-cash)", None,
          [f"=D{r}*(1+{aref('inv_corpus_g','FY27E')})",
           f"=E{r}*(1+{aref('inv_corpus_g','FY28E')})",
           f"=F{r}*(1+{aref('inv_corpus_g','FY29E')})"],
          "Other current assets grown at corpus growth.")
    ocr = BS_ROW["other_ca"]
    for i, fy in enumerate(HIST):
        # historical other CA is the asset-side residual so total assets tie to the reported actual
        ta = D.BS_ACTUALS_LAKH["total_assets"][i]
        onca = D.BS_ACTUALS_LAKH["total_noncurrent_assets"][i] - (D.BS_ACTUALS_LAKH["ppe"][i] + D.BS_ACTUALS_LAKH["cwip"][i])
        nb = D.BS_ACTUALS_LAKH["ppe"][i] + D.BS_ACTUALS_LAKH["cwip"][i]
        recv = D.BS_ACTUALS_LAKH["trade_receivables"][i]
        cashc = D.CF_ACTUALS_LAKH["cash_close"][i]
        resid = ta - onca - nb - recv - cashc
        S.set_cell(ws, f"{colL(fy)}{ocr}", D.cr(resid), fmt=S.FMT_CR, input_cell=True)

    # Cash & equivalents: projected as the balancing plug so Assets = E&L exactly.
    # cash = total E&L - (non-current assets + receivables + other current assets)
    BS_ROW["cash"] = r
    S.label(ws, f"A{r}", "Cash & investments (balancing)", indent=1)
    for i, fy in enumerate(HIST):
        S.set_cell(ws, f"{colL(fy)}{r}", D.cr(D.CF_ACTUALS_LAKH["cash_close"][i]),
                   fmt=S.FMT_CR, input_cell=True)
    # projected cash defined after equity/liab rows exist -> patched in _patch_projected_cash
    for fy in PROJ:
        S.set_cell(ws, f"{colL(fy)}{r}", "=0", fmt=S.FMT_CR)  # placeholder, patched below
    S.label(ws, f"H{r}", "Projected = balancing plug: total E&L - non-cash assets (guarantees BS balances).",
            italic=True, size=8, color="FF555555")
    r += 1

    BS_ROW["total_ca"] = r
    S.label(ws, f"A{r}", "Total current assets", bold=True, indent=0)
    for fy in YEARS:
        S.set_cell(ws, f"{colL(fy)}{r}",
                   f"={colL(fy)}{BS_ROW['receivables']}+{colL(fy)}{BS_ROW['other_ca']}+{colL(fy)}{BS_ROW['cash']}",
                   fmt=S.FMT_CR, bold=True)
    r += 1

    BS_ROW["total_assets"] = r
    S.label(ws, f"A{r}", "TOTAL ASSETS", bold=True, indent=0)
    for fy in YEARS:
        S.set_cell(ws, f"{colL(fy)}{r}",
                   f"={colL(fy)}{BS_ROW['total_nca']}+{colL(fy)}{BS_ROW['total_ca']}",
                   fmt=S.FMT_CR, bold=True)
    r += 1

    # ---------- EQUITY & LIABILITIES ----------
    S.section(ws, r, "EQUITY & LIABILITIES", ncols); r += 1

    # Equity: opening + PAT - dividend (retained earnings roll-forward)
    BS_ROW["equity"] = r
    S.label(ws, f"A{r}", "Total equity", bold=True, indent=0)
    for i, fy in enumerate(HIST):
        S.set_cell(ws, f"{colL(fy)}{r}", D.cr(D.BS_ACTUALS_LAKH["total_equity"][i]),
                   fmt=S.FMT_CR, input_cell=True, bold=True)
    for j, fy in enumerate(PROJ):
        prev = "D" if j == 0 else colL(PROJ[j-1])
        cc = colL(fy)
        S.set_cell(ws, f"{cc}{r}",
                   f"={prev}{r}+'Income Statement'!{cc}{IS['pat']}-'Income Statement'!{cc}{IS['dividend']}",
                   fmt=S.FMT_CR, bold=True)
    S.label(ws, f"H{r}", "Prior equity + PAT - dividend (retained earnings roll-forward). Link to IS.",
            italic=True, size=8, color="FF555555")
    r += 1

    bsrow("ncl", "Non-current liabilities", "total_noncurrent_liab",
          [f"=D{r}*(1+{aref('g_admin','FY27E')})",
           f"=E{r}*(1+{aref('g_admin','FY28E')})",
           f"=F{r}*(1+{aref('g_admin','FY29E')})"],
          "Small; grown at admin growth.")

    # Current liabilities = revenue * payable_pct (clearing/settlement float scales with activity)
    bsrow("ccl", "Current liabilities", "total_current_liabilities",
          [f"='Income Statement'!E{IS['revenue']}*{aref('payable_pct','FY27E')}",
           f"='Income Statement'!F{IS['revenue']}*{aref('payable_pct','FY28E')}",
           f"='Income Statement'!G{IS['revenue']}*{aref('payable_pct','FY29E')}"],
          "Projected = revenue x current-liab% (Assumptions). Incl clearing/settlement float.")
    # historical current liabilities = E&L residual so E&L ties to reported total assets
    cclr = BS_ROW["ccl"]
    for i, fy in enumerate(HIST):
        ta = D.BS_ACTUALS_LAKH["total_assets"][i]
        eq = D.BS_ACTUALS_LAKH["total_equity"][i]
        ncl = D.BS_ACTUALS_LAKH["total_noncurrent_liab"][i]
        S.set_cell(ws, f"{colL(fy)}{cclr}", D.cr(ta - eq - ncl), fmt=S.FMT_CR, input_cell=True)

    BS_ROW["total_liab_eq"] = r
    S.label(ws, f"A{r}", "TOTAL EQUITY & LIABILITIES", bold=True, indent=0)
    for fy in YEARS:
        S.set_cell(ws, f"{colL(fy)}{r}",
                   f"={colL(fy)}{BS_ROW['equity']}+{colL(fy)}{BS_ROW['ncl']}+{colL(fy)}{BS_ROW['ccl']}",
                   fmt=S.FMT_CR, bold=True)
    r += 1

    # Balance check
    BS_ROW["check"] = r
    S.label(ws, f"A{r}", "Balance check (Assets - E&L)", bold=True, indent=0)
    for fy in YEARS:
        S.set_cell(ws, f"{colL(fy)}{r}",
                   f"={colL(fy)}{BS_ROW['total_assets']}-{colL(fy)}{BS_ROW['total_liab_eq']}",
                   fmt=S.FMT_CR, bold=True, force_color=S.BLACK)
    S.label(ws, f"H{r}", "Must be ~0 for projected years (plug via cash). Hist may differ (actuals).",
            italic=True, size=8, color="FF555555")
    r += 1

    # Patch projected cash to be the true balancing plug: E&L - non-cash assets.
    # This makes the balance check identically zero for projected years.
    cash_row = BS_ROW["cash"]
    for fy in PROJ:
        cc = colL(fy)
        ws[f"{cc}{cash_row}"].value = (
            f"={cc}{BS_ROW['total_liab_eq']}-{cc}{BS_ROW['total_nca']}"
            f"-{cc}{BS_ROW['receivables']}-{cc}{BS_ROW['other_ca']}")

    ws.freeze_panes = "B6"
    BS_ROW["__end__"] = r
    return ws


def patch_is_depreciation(wb):
    """Resolve the IS depreciation projected formulas to point at the BS D&A schedule row."""
    ws = wb["Income Statement"]
    da_row = BS_ROW["da"]
    for fy in PROJ:
        cc = colL(fy)
        ws[f"{cc}{IS_ROW['depreciation']}"].value = f"='Balance Sheet'!{cc}{da_row}"
