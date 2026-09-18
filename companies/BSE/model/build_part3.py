"""BSE model builder — part 3: DCF, Comps, Sensitivity, and assembly."""
import openpyxl
from openpyxl.utils import get_column_letter as gcl
import bse_data as D
import bse_style as S
from build_part1 import (COL_FY, HIST, PROJ, YEARS, colL, aref, A_ROW, build_assumptions)
from build_part2 import (SEG_ROW, IS_ROW, BS_ROW, build_segment, build_income_statement,
                         build_balance_sheet, patch_is_depreciation)

DCF_ROW = {}


# =====================================================================
# DCF VALUATION (FCFF)
# =====================================================================
def build_dcf(wb):
    ws = wb.create_sheet("DCF Valuation")
    ws.sheet_properties.tabColor = "FF7030A0"
    ncols = 8
    S.title_block(ws, "BSE Ltd — DCF Valuation (FCFF)",
                  "FCFF discounted at WACC (CAPM cost of equity + after-tax cost of debt). "
                  "Terminal value via Gordon growth. All lines are formula chains referencing "
                  "Assumptions and the Income Statement / Balance Sheet.",
                  "Units: Rs Crore unless marked. BSE is a fee-income business (not a bank) so FCFF DCF applies.",
                  ncols)
    ws.column_dimensions["A"].width = 44
    for c in "BCDEFG":
        ws.column_dimensions[c].width = 13
    ws.column_dimensions["H"].width = 50
    r = 5

    IS, BS = IS_ROW, BS_ROW

    def line(key, lbl, per_year, note, *, bold=False, indent=1, fmt=S.FMT_CR, years=PROJ):
        nonlocal r
        DCF_ROW[key] = r
        S.label(ws, f"A{r}", lbl, bold=bold, indent=indent)
        for fy in years:
            f = per_year(fy)
            if f is not None:
                S.set_cell(ws, f"{colL(fy)}{r}", f, fmt=fmt, bold=bold)
        if note:
            S.label(ws, f"H{r}", note, italic=True, size=8, color="FF555555")
        r += 1

    # ---------------- WACC BUILD-UP ----------------
    S.section(ws, r, "WACC BUILD-UP (CAPM)", ncols); r += 1

    def single(key, lbl, formula, note, fmt=S.FMT_PCT):
        nonlocal r
        DCF_ROW[key] = r
        S.label(ws, f"A{r}", lbl, indent=1)
        S.set_cell(ws, f"E{r}", formula, fmt=fmt)
        if note:
            S.label(ws, f"H{r}", note, italic=True, size=8, color="FF555555")
        r += 1

    single("rf", "Risk-free rate", f"={aref('rf')}", "From Assumptions (green).")
    single("erp", "Equity risk premium", f"={aref('erp')}", "From Assumptions.")
    single("beta", "Beta (levered)", f"={aref('beta')}", "From Assumptions.", fmt=S.FMT_NUM)
    single("coe", "Cost of equity (CAPM)",
           f"=E{DCF_ROW['rf']}+E{DCF_ROW['beta']}*E{DCF_ROW['erp']}",
           "= Rf + beta x ERP (same-sheet).")
    single("cod_pre", "Pre-tax cost of debt", f"={aref('cost_debt')}", "From Assumptions.")
    single("tax", "Tax rate", f"={aref('tax_rate','FY27E')}", "From Assumptions.")
    single("cod_post", "After-tax cost of debt",
           f"=E{DCF_ROW['cod_pre']}*(1-E{DCF_ROW['tax']})", "= Kd x (1 - tax).")
    single("we", "Weight — equity", f"={aref('wt_equity')}", "From Assumptions.")
    single("wd", "Weight — debt", f"={aref('wt_debt')}", "From Assumptions.")
    single("wacc", "WACC",
           f"=E{DCF_ROW['we']}*E{DCF_ROW['coe']}+E{DCF_ROW['wd']}*E{DCF_ROW['cod_post']}",
           "= We x Ke + Wd x Kd(after tax).")
    single("tg", "Terminal growth", f"={aref('term_growth')}", "From Assumptions.")

    # ---------------- FCFF CHAIN ----------------
    S.section(ws, r, "FREE CASH FLOW TO FIRM (FCFF)", ncols); r += 1

    line("ebit", "EBIT",
         lambda fy: f"='Income Statement'!{colL(fy)}{IS['ebit']}",
         "Link to Income Statement EBIT.")
    line("nopat", "NOPAT = EBIT x (1 - tax)",
         lambda fy: f"={colL(fy)}{DCF_ROW['ebit']}*(1-{aref('tax_rate',fy)})",
         "EBIT x (1 - tax rate from Assumptions).")
    line("da", "add: D&A",
         lambda fy: f"='Balance Sheet'!{colL(fy)}{BS['da']}",
         "Link to Balance Sheet D&A schedule.")
    line("capex", "less: Capex",
         lambda fy: f"=-'Balance Sheet'!{colL(fy)}{BS['capex']}",
         "Link to Balance Sheet capex (negative).")
    # change in operating net working capital. For an exchange the large current
    # liabilities are settlement/clearing pass-through float (not operating WC), so
    # operating WC is taken as trade receivables only (the genuine operating item).
    def dnwc(fy):
        j = PROJ.index(fy)
        prev = "D" if j == 0 else colL(PROJ[j-1])
        cc = colL(fy)
        return (f"=-('Balance Sheet'!{cc}{BS['receivables']}"
                f"-'Balance Sheet'!{prev}{BS['receivables']})")
    line("dnwc", "less: Increase in operating working capital", dnwc,
         "Negative change in trade receivables (settlement float excluded). Link to BS.")
    line("fcff", "FCFF", lambda fy:
         f"={colL(fy)}{DCF_ROW['nopat']}+{colL(fy)}{DCF_ROW['da']}+{colL(fy)}{DCF_ROW['capex']}+{colL(fy)}{DCF_ROW['dnwc']}",
         "NOPAT + D&A - Capex - dNWC.", bold=True)

    # ---------------- DISCOUNTING ----------------
    S.section(ws, r, "DISCOUNTING", ncols); r += 1
    line("period", "Discount period (years)",
         lambda fy: f"={PROJ.index(fy)+1}", "1, 2, 3 ...", fmt=S.FMT_NUM)
    line("df", "Discount factor",
         lambda fy: f"=1/(1+$E${DCF_ROW['wacc']})^{colL(fy)}{DCF_ROW['period']}",
         "= 1 / (1 + WACC)^period.", fmt=S.FMT_NUM)
    line("pv_fcff", "PV of FCFF",
         lambda fy: f"={colL(fy)}{DCF_ROW['fcff']}*{colL(fy)}{DCF_ROW['df']}",
         "FCFF x discount factor.", bold=True)

    # ---------------- TERMINAL VALUE ----------------
    S.section(ws, r, "TERMINAL VALUE & ENTERPRISE VALUE", ncols); r += 1
    lastfy = PROJ[-1]
    lastc = colL(lastfy)

    def one(key, lbl, formula, note, fmt=S.FMT_CR, bold=False):
        nonlocal r
        DCF_ROW[key] = r
        S.label(ws, f"A{r}", lbl, indent=1, bold=bold)
        S.set_cell(ws, f"E{r}", formula, fmt=fmt, bold=bold)
        if note:
            S.label(ws, f"H{r}", note, italic=True, size=8, color="FF555555")
        r += 1

    one("tv", "Terminal value (Gordon)",
        f"={lastc}{DCF_ROW['fcff']}*(1+$E${DCF_ROW['tg']})/($E${DCF_ROW['wacc']}-$E${DCF_ROW['tg']})",
        "= FCFF(final) x (1+g) / (WACC - g).")
    one("pv_tv", "PV of terminal value",
        f"=E{DCF_ROW['tv']}*{lastc}{DCF_ROW['df']}",
        "TV x final-year discount factor.")
    one("sum_pv_fcff", "Sum of PV of FCFF (explicit)",
        f"=SUM(E{DCF_ROW['pv_fcff']}:G{DCF_ROW['pv_fcff']})",
        "Sum of discounted explicit-period FCFF.")
    one("ev", "Enterprise value",
        f"=E{DCF_ROW['sum_pv_fcff']}+E{DCF_ROW['pv_tv']}",
        "PV(explicit FCFF) + PV(terminal value).", bold=True)
    one("net_debt", "less: Net debt",
        f"={aref('net_debt')}",
        "Net debt from Assumptions (negative = net cash).")
    one("equity_value", "Equity value",
        f"=E{DCF_ROW['ev']}-E{DCF_ROW['net_debt']}",
        "EV - net debt.", bold=True)
    one("shares", "Shares outstanding (cr)",
        f"={aref('bse_shares')}",
        "From Assumptions.", fmt=S.FMT_NUM)
    one("value_per_share", "Implied value per share (Rs)",
        f"=E{DCF_ROW['equity_value']}/E{DCF_ROW['shares']}",
        "Equity value (Rs cr) / shares (cr) = Rs/share (both in crore units cancel).",
        fmt=S.FMT_RS, bold=True)
    one("mkt_price", "Current market price (Rs)",
        f"={aref('bse_price')}", "From Assumptions.", fmt=S.FMT_RS)
    one("upside", "Implied upside / (downside)",
        f"=E{DCF_ROW['value_per_share']}/E{DCF_ROW['mkt_price']}-1",
        "Value per share / market price - 1.", fmt=S.FMT_PCT, bold=True)

    ws.freeze_panes = "B6"
    DCF_ROW["__end__"] = r
    return ws


# =====================================================================
# COMPS
# =====================================================================
CMP_ROW = {}


def build_comps(wb):
    ws = wb.create_sheet("Comps")
    ws.sheet_properties.tabColor = "FF00B0F0"
    ncols = 7
    S.title_block(ws, "BSE Ltd — Trading Comparables",
                  "Peer market data in blue (editable). Multiples and BSE-implied values are formulas. "
                  "BSE fundamentals link (green) to Income Statement / DCF.",
                  "Units: Rs Crore for values, Rs for price/share, x for multiples.", ncols)
    ws.column_dimensions["A"].width = 30
    for c in "BCDEFG":
        ws.column_dimensions[c].width = 14
    r = 5

    # header
    cols = ["Company", "Price (Rs)", "Shares (cr)", "Mkt cap", "Net debt", "EV", "PAT"]
    for i, h in enumerate(cols):
        c = ws.cell(row=r, column=1 + i)
        c.value = h
        c.font = S.Font(name="Calibri", size=10, bold=True, color=S.WHITE)
        c.fill = S.PatternFill("solid", fgColor=S.HDR_BG)
        c.alignment = S.Alignment(horizontal="center")
    r += 1

    # peer rows (blue inputs for price/shares/net_debt/ebitda/pat/book; formulas for mktcap/EV)
    peer_start = r
    CMP_ROW["peers"] = {}
    for name, s in D.PEER_SEEDS.items():
        S.label(ws, f"A{r}", name, bold=True)
        S.set_cell(ws, f"B{r}", s["price"], fmt=S.FMT_RS, input_cell=True)
        S.set_cell(ws, f"C{r}", s["shares_cr"], fmt=S.FMT_NUM, input_cell=True)
        S.set_cell(ws, f"D{r}", f"=B{r}*C{r}", fmt=S.FMT_CR)      # mkt cap (Rs cr) = price(Rs) x shares(cr)
        S.set_cell(ws, f"E{r}", s["net_debt_cr"], fmt=S.FMT_CR, input_cell=True)
        S.set_cell(ws, f"F{r}", f"=D{r}+E{r}", fmt=S.FMT_CR)       # EV
        S.set_cell(ws, f"G{r}", s["pat_cr"], fmt=S.FMT_CR, input_cell=True)
        CMP_ROW["peers"][name] = r
        r += 1
    peer_end = r - 1

    # store ebitda/book in adjacent helper columns (I, J) for multiple calc
    ws.cell(row=peer_start - 1, column=9).value = "EBITDA"
    ws.cell(row=peer_start - 1, column=10).value = "Book value"
    ws.cell(row=peer_start - 1, column=9).font = S.Font(bold=True, size=9)
    ws.cell(row=peer_start - 1, column=10).font = S.Font(bold=True, size=9)
    ws.column_dimensions["I"].width = 12
    ws.column_dimensions["J"].width = 12
    for name, s in D.PEER_SEEDS.items():
        rr = CMP_ROW["peers"][name]
        S.set_cell(ws, f"I{rr}", s["ebitda_cr"], fmt=S.FMT_CR, input_cell=True)
        S.set_cell(ws, f"J{rr}", s["book_cr"], fmt=S.FMT_CR, input_cell=True)

    r += 1
    S.section(ws, r, "MULTIPLES (x)", ncols); r += 1
    mhead = ["Company", "EV/EBITDA", "P/E", "P/B"]
    for i, h in enumerate(mhead):
        c = ws.cell(row=r, column=1 + i)
        c.value = h
        c.font = S.Font(name="Calibri", size=10, bold=True, color=S.WHITE)
        c.fill = S.PatternFill("solid", fgColor=S.HDR_BG)
        c.alignment = S.Alignment(horizontal="center")
    r += 1
    mult_start = r
    for name in D.PEER_SEEDS:
        rr = CMP_ROW["peers"][name]
        S.label(ws, f"A{r}", name, bold=True)
        S.set_cell(ws, f"B{r}", f"=F{rr}/I{rr}", fmt=S.FMT_X)       # EV/EBITDA
        S.set_cell(ws, f"C{r}", f"=D{rr}/G{rr}", fmt=S.FMT_X)       # P/E
        S.set_cell(ws, f"D{r}", f"=D{rr}/J{rr}", fmt=S.FMT_X)       # P/B
        r += 1
    mult_end = r - 1

    # peer average multiples
    S.label(ws, f"A{r}", "Peer average", bold=True, italic=True)
    S.set_cell(ws, f"B{r}", f"=AVERAGE(B{mult_start}:B{mult_end})", fmt=S.FMT_X, bold=True)
    S.set_cell(ws, f"C{r}", f"=AVERAGE(C{mult_start}:C{mult_end})", fmt=S.FMT_X, bold=True)
    S.set_cell(ws, f"D{r}", f"=AVERAGE(D{mult_start}:D{mult_end})", fmt=S.FMT_X, bold=True)
    CMP_ROW["avg"] = r
    r += 1

    r += 1
    S.section(ws, r, "BSE — IMPLIED VALUE FROM PEER MULTIPLES", ncols); r += 1
    IS = IS_ROW
    # BSE fundamentals (link green to IS FY26 actual column D)
    S.label(ws, f"A{r}", "BSE EBITDA (FY26)", indent=1)
    S.set_cell(ws, f"B{r}", f"='Income Statement'!D{IS['ebitda']}", fmt=S.FMT_CR)
    CMP_ROW["bse_ebitda"] = r
    r += 1
    S.label(ws, f"A{r}", "BSE PAT (FY26)", indent=1)
    S.set_cell(ws, f"B{r}", f"='Income Statement'!D{IS['pat']}", fmt=S.FMT_CR)
    CMP_ROW["bse_pat"] = r
    r += 1
    S.label(ws, f"A{r}", "BSE book value (equity, FY26)", indent=1)
    S.set_cell(ws, f"B{r}", f"='Balance Sheet'!D{BS_ROW['equity']}", fmt=S.FMT_CR)
    CMP_ROW["bse_book"] = r
    r += 1
    S.label(ws, f"A{r}", "BSE net debt", indent=1)
    S.set_cell(ws, f"B{r}", f"={aref('net_debt')}", fmt=S.FMT_CR)
    CMP_ROW["bse_nd"] = r
    r += 1
    S.label(ws, f"A{r}", "BSE shares (cr)", indent=1)
    S.set_cell(ws, f"B{r}", f"={aref('bse_shares')}", fmt=S.FMT_NUM)
    CMP_ROW["bse_shares"] = r
    r += 1

    avg = CMP_ROW["avg"]
    # implied value per share from EV/EBITDA
    S.label(ws, f"A{r}", "Implied price/share — EV/EBITDA (Rs)", bold=True, indent=1)
    S.set_cell(ws, f"B{r}",
               f"=(B{avg}*B{CMP_ROW['bse_ebitda']}-B{CMP_ROW['bse_nd']})/B{CMP_ROW['bse_shares']}",
               fmt=S.FMT_RS, bold=True)
    r += 1
    S.label(ws, f"A{r}", "Implied price/share — P/E (Rs)", bold=True, indent=1)
    S.set_cell(ws, f"B{r}",
               f"=(C{avg}*B{CMP_ROW['bse_pat']})/B{CMP_ROW['bse_shares']}",
               fmt=S.FMT_RS, bold=True)
    r += 1
    S.label(ws, f"A{r}", "Implied price/share — P/B (Rs)", bold=True, indent=1)
    S.set_cell(ws, f"B{r}",
               f"=(D{avg}*B{CMP_ROW['bse_book']})/B{CMP_ROW['bse_shares']}",
               fmt=S.FMT_RS, bold=True)
    r += 1

    ws.freeze_panes = "B6"
    CMP_ROW["__end__"] = r
    return ws


# =====================================================================
# SENSITIVITY
# =====================================================================
def build_sensitivity(wb):
    ws = wb.create_sheet("Sensitivity")
    ws.sheet_properties.tabColor = "FFFF0000"
    ncols = 8
    S.title_block(ws, "BSE Ltd — Sensitivity Analysis",
                  "Value per share sensitivity. Each grid cell recomputes value/share from the FCFF "
                  "stream on the DCF sheet using the row/column driver — fully formula-driven, never typed.",
                  "Units: Rs per share. Grid 1: WACC (columns) x terminal growth (rows). "
                  "Grid 2: value vs derivatives ADTO growth.", ncols)
    ws.column_dimensions["A"].width = 22
    for c in "BCDEFGH":
        ws.column_dimensions[c].width = 13
    r = 5

    # DCF references (absolute) for the FCFF stream and bridge items
    f1 = f"'DCF Valuation'!$E${DCF_ROW['fcff']}"
    f2 = f"'DCF Valuation'!$F${DCF_ROW['fcff']}"
    f3 = f"'DCF Valuation'!$G${DCF_ROW['fcff']}"
    nd = f"'DCF Valuation'!$E${DCF_ROW['net_debt']}"
    sh = f"'DCF Valuation'!$E${DCF_ROW['shares']}"

    def vps(wacc_ref, g_ref):
        """Formula string: value per share given a WACC cell ref and growth cell ref.
        EV = f1/(1+w)^1 + f2/(1+w)^2 + f3/(1+w)^3 + [f3*(1+g)/(w-g)]/(1+w)^3 ;
        equity = EV - nd ; per share = equity/shares*100 (Rs)."""
        w = wacc_ref
        g = g_ref
        ev = (f"({f1}/(1+{w})^1+{f2}/(1+{w})^2+{f3}/(1+{w})^3"
              f"+({f3}*(1+{g})/({w}-{g}))/(1+{w})^3)")
        return f"=({ev}-{nd})/{sh}"

    # ---------------- GRID 1: WACC x terminal growth ----------------
    S.section(ws, r, "GRID 1 — Value/share: WACC (columns) x Terminal growth (rows)", ncols); r += 1
    # WACC column headers: base WACC +/- steps around DCF WACC
    base_wacc = f"'DCF Valuation'!$E${DCF_ROW['wacc']}"
    base_g = f"'DCF Valuation'!$E${DCF_ROW['tg']}"
    wacc_offsets = [-0.02, -0.01, 0.0, 0.01, 0.02]
    g_offsets = [-0.02, -0.01, 0.0, 0.01, 0.02]

    corner_row = r
    S.label(ws, f"A{r}", "g \\ WACC", bold=True)
    # WACC header cells (formulas = base + offset)
    wacc_cols = []
    for i, off in enumerate(wacc_offsets):
        cc = gcl(2 + i)
        S.set_cell(ws, f"{cc}{r}", f"={base_wacc}{'+' if off>=0 else ''}{off}", fmt=S.FMT_PCT, bold=True)
        wacc_cols.append(cc)
    r += 1
    grid1_top = r
    for gi, goff in enumerate(g_offsets):
        # row header: g value
        S.set_cell(ws, f"A{r}", f"={base_g}{'+' if goff>=0 else ''}{goff}", fmt=S.FMT_PCT, bold=True)
        for ci, cc in enumerate(wacc_cols):
            w_ref = f"{cc}${corner_row}"      # WACC header in this column (row locked)
            g_ref = f"$A{r}"                  # g header in this row (col locked)
            S.set_cell(ws, f"{cc}{r}", vps(w_ref, g_ref), fmt=S.FMT_RS)
        r += 1
    r += 1

    # ---------------- GRID 2: value vs derivatives ADTO growth ----------------
    S.section(ws, r, "GRID 2 — Value/share vs derivatives ADTO growth (key volume lever)", ncols); r += 1
    S.label(ws, f"A{r}", "Deriv ADTO growth", bold=True)
    S.label(ws, f"B{r}", "Value/share (Rs)", bold=True)
    S.label(ws, f"H{r}", "Note: this grid re-scales FY27E FCFF by the ratio of the sensitised "
            "derivatives revenue to base, holding WACC & g at DCF base.", italic=True, size=8, color="FF555555")
    r += 1

    # base derivatives ADTO growth and its effect: derivatives txn ~ proportional to ADTO growth.
    # We approximate value sensitivity by scaling FCFF1..3 by a revenue-mix factor.
    # deriv share of FY27E revenue:
    deriv_rev = f"'Segment Revenue Build'!$E${SEG_ROW['txn_equity_derivatives']}"
    rev_ops = f"'Segment Revenue Build'!$E${SEG_ROW['rev_ops_build']}"
    base_dg = f"{aref('adto_deriv_g','FY27E')}"

    adto_offsets = [-0.15, -0.10, -0.05, 0.0, 0.05, 0.10, 0.15]
    for off in adto_offsets:
        # sensitised growth
        S.set_cell(ws, f"A{r}", f"={base_dg}{'+' if off>=0 else ''}{off}", fmt=S.FMT_PCT, bold=True)
        # scaling factor k = 1 + deriv_share * (new_g - base_g)/(1+base_g)
        # approximates revenue uplift flowing to FCFF; then value scales EV proportionally on FCFF.
        w = base_wacc
        g = base_g
        k = (f"(1+({deriv_rev}/{rev_ops})*((A{r}-{base_dg})/(1+{base_dg})))")
        ev = (f"({k}*{f1}/(1+{w})^1+{k}*{f2}/(1+{w})^2+{k}*{f3}/(1+{w})^3"
              f"+({k}*{f3}*(1+{g})/({w}-{g}))/(1+{w})^3)")
        S.set_cell(ws, f"B{r}", f"=({ev}-{nd})/{sh}", fmt=S.FMT_RS)
        r += 1

    ws.freeze_panes = "B6"
    return ws
