"""
BSE Ltd financial model builder — main.
Produces BSE_Financial_Model.xlsx with 7 tabs, fully formula-driven.

Design rule: every projected cell references an Assumptions cell. Cross-sheet
formulas render green; same-sheet formulas black; typed inputs blue on yellow.
All monetary values in Rs Crore. Historical = FY24/FY25/FY26 (actuals, blue).
Projected = FY27E/FY28E/FY29E (formulas).
"""
import openpyxl
from openpyxl.utils import get_column_letter as gcl
from openpyxl.workbook.defined_name import DefinedName

import bse_data as D
import bse_style as S

# Column layout shared by the statement tabs:
# A = label, B = FY24, C = FY25, D = FY26, E = FY27E, F = FY28E, G = FY29E, H = source/note
COL_LBL = 1
COL_FY = {"FY24": 2, "FY25": 3, "FY26": 4, "FY27E": 5, "FY28E": 6, "FY29E": 7}
COL_NOTE = 8
HIST = ["FY24", "FY25", "FY26"]
PROJ = ["FY27E", "FY28E", "FY29E"]
YEARS = HIST + PROJ


def colL(fy):
    return gcl(COL_FY[fy])


# =====================================================================
# ASSUMPTIONS TAB
# We lay out each driver with one column per projected year (and show the
# implied historical where useful). Row map captured in A_ROW for references.
# =====================================================================
A_ROW = {}  # key -> row number on Assumptions


def build_assumptions(wb):
    ws = wb.create_sheet("Assumptions")
    ws.sheet_properties.tabColor = "FFFFC000"
    ncols = 8
    S.title_block(ws,
                  "BSE Ltd — Model Assumptions & Drivers",
                  "Every yellow cell is an editable input. Downstream tabs reference these cells only. "
                  "Sources tagged from BSE research (AR = Annual Report, MD&A, SECONDARY = external).",
                  "Units: Rs Crore unless marked. Percentages stored as decimals (0.15 = 15.0%). "
                  "Bps stored as absolute (e.g. 2.50).",
                  ncols)

    ws.column_dimensions["A"].width = 44
    for c in "BCDEFG":
        ws.column_dimensions[c].width = 12
    ws.column_dimensions["H"].width = 52

    r = 5
    # Column headers
    S.label(ws, f"A{r}", "Driver", bold=True)
    S.year_header(ws, r, COL_FY["FY24"], YEARS, hist_count=3)
    S.label(ws, f"H{r}", "Source / basis", bold=True)
    r += 1

    def driver(key, lbl, hist_vals, proj_vals, fmt, note, indent=0, input_hist=False):
        """Add a driver row. hist_vals/proj_vals are lists (len 3 each) or None.
        Values that are numbers become blue yellow inputs; strings starting '='
        become formulas."""
        nonlocal r
        A_ROW[key] = r
        S.label(ws, f"A{r}", lbl, indent=indent, bold=(indent == 0))
        for i, fy in enumerate(HIST):
            v = None if hist_vals is None else hist_vals[i]
            if v is not None:
                S.set_cell(ws, f"{colL(fy)}{r}", v, fmt=fmt, input_cell=input_hist)
        for i, fy in enumerate(PROJ):
            v = None if proj_vals is None else proj_vals[i]
            if v is not None:
                is_formula = isinstance(v, str) and v.startswith("=")
                S.set_cell(ws, f"{colL(fy)}{r}", v, fmt=fmt, input_cell=(not is_formula))
        if note:
            S.label(ws, f"H{r}", note, italic=True, size=8, color="FF555555")
        r += 1

    # ---------------- VOLUME DRIVERS ----------------
    S.section(ws, r, "1. VOLUME DRIVERS — Average Daily Turnover (ADTO) & market share", ncols); r += 1

    # Equity derivatives premium ADTO (Rs cr) — key swing factor
    driver("adto_deriv", "Equity derivatives premium ADTO (Rs cr)",
           [3200, 6500, 12000], [15600, 19500, 23400], S.FMT_CR0,
           "SECONDARY: BSE monthly volume disclosures; premium turnover. Editable seed.",
           input_hist=True)
    driver("adto_deriv_g", "  ADTO growth — derivatives (%)",
           None, [0.30, 0.25, 0.20], S.FMT_PCT,
           "KEY LEVER. Derivatives is the dominant swing factor (FY25->FY26 premium ADTO ~+85%).")
    driver("adto_cash", "Equity cash ADTO (Rs cr)",
           [6800, 7000, 7165], [7523, 7975, 8454], S.FMT_CR0,
           "SECONDARY: BSE cash-market turnover. FY26 cash turnover rose ~2.4%.",
           input_hist=True)
    driver("adto_cash_g", "  ADTO growth — cash (%)",
           None, [0.05, 0.06, 0.06], S.FMT_PCT,
           "Cash-market ADTO growth. Lower and steadier than derivatives.")
    driver("mkt_share_deriv", "BSE derivatives market share vs NSE (%)",
           [0.06, 0.12, 0.22], [0.26, 0.28, 0.29], S.FMT_PCT,
           "KEY LEVER. BSE has taken derivatives share sharply. Treated as a lever, not a constant.",
           input_hist=True)

    # ---------------- YIELD (take-rate) ----------------
    S.section(ws, r, "2. REALISATION — Take-rate on turnover per segment", ncols); r += 1
    driver("yld_deriv", "Derivatives take-rate (fraction of turnover)",
           None, [0.0010448, 0.0010448, 0.0010448], S.FMT_NUM,
           "= FY26 deriv txn 3134cr / (deriv ADTO 12000 x 250 days). ~0.1045%. SEBI pricing risk.")
    driver("yld_cash", "Cash take-rate (fraction of turnover)",
           None, [0.0001397, 0.0001397, 0.0001397], S.FMT_NUM,
           "= FY26 cash txn 250cr / (cash ADTO 7165 x 250 days). ~0.01397%. Fell ~19.5% in FY26.")
    driver("trading_days", "Trading days per year",
           [250, 250, 250], [250, 250, 250], S.FMT_CR0,
           "Approx NSE/BSE trading days. Editable.", input_hist=True)

    # ---------------- OTHER REVENUE GROWTH ----------------
    S.section(ws, r, "3. OTHER REVENUE DRIVERS (growth on prior year)", ncols); r += 1
    driver("g_starmf", "StAR MF platform fees growth (%)",
           None, [0.20, 0.18, 0.15], S.FMT_PCT, "MF platform fees. FY26 +23%.")
    driver("g_listing", "Listing fees growth (%)",
           None, [0.12, 0.11, 0.10], S.FMT_PCT, "Linked to IPO/listings pipeline. FY26 +10%.")
    driver("g_bookbuild", "Book building / IPO fees growth (%)",
           None, [0.12, 0.10, 0.10], S.FMT_PCT, "IPO processing fees. FY26 +9%.")
    driver("g_data", "Data feed & index licensing growth (%)",
           None, [0.15, 0.14, 0.12], S.FMT_PCT, "Asia Index/S&P BSE + colocation. FY26 colocation +133%.")
    driver("g_other_op", "Other operating income growth (%)",
           None, [0.15, 0.12, 0.10], S.FMT_PCT, "Residual other operating income.")

    # ---------------- INVESTMENT INCOME ----------------
    S.section(ws, r, "4. INVESTMENT / TREASURY INCOME", ncols); r += 1
    driver("inv_corpus", "Investable corpus incl SGF (Rs cr)",
           [4000, 4800, 5200], [5720, 6292, 6921], S.FMT_CR0,
           "SECONDARY: own investable surplus + Core SGF corpus. Editable seed.", input_hist=True)
    driver("inv_corpus_g", "  Corpus growth (%)",
           None, [0.10, 0.10, 0.10], S.FMT_PCT, "Corpus reinvestment growth.")
    driver("inv_yield", "Investment income yield (%)",
           None, [0.056, 0.056, 0.056], S.FMT_PCT,
           "Yield on treasury+SGF. FY26 inv income 290cr / ~5200cr corpus ~5.6%.")

    # ---------------- OPEX ----------------
    S.section(ws, r, "5. OPERATING COST DRIVERS (growth on prior year)", ncols); r += 1
    driver("g_emp", "Employee cost growth (%)",
           None, [0.14, 0.12, 0.11], S.FMT_PCT, "Employee benefits. FY26 +26%.")
    driver("g_tech", "Technology cost growth (%)",
           None, [0.18, 0.15, 0.13], S.FMT_PCT, "Tech/infra cost. FY26 +24%.")
    driver("sebi_fee_pct", "SEBI regulatory fee (% of txn charges)",
           None, [0.12, 0.12, 0.12], S.FMT_PCT,
           "SEBI reg fee scales with turnover/txn charges. FY26 566cr on 3669cr txn ~15%; editable.")
    driver("g_admin", "Other admin cost growth (%)",
           None, [0.10, 0.09, 0.08], S.FMT_PCT, "Other administrative expenses.")
    driver("clearing_pct", "Clearing & settlement (% of txn charges)",
           None, [0.08, 0.08, 0.08], S.FMT_PCT, "ICCL clearing cost, scales with volume.")

    # ---------------- D&A, CAPEX, WC, TAX ----------------
    S.section(ws, r, "6. D&A, CAPEX, WORKING CAPITAL, TAX", ncols); r += 1
    driver("capex_pct", "Capex (% of revenue)",
           None, [0.08, 0.07, 0.06], S.FMT_PCT, "Capex intensity. FY26 elevated (515cr) on data-centre build.")
    driver("da_pct", "D&A (% of opening net block)",
           None, [0.22, 0.22, 0.22], S.FMT_PCT, "Depreciation on PPE. Editable schedule driver.")
    driver("recv_days", "Receivable days (on revenue)",
           None, [42, 42, 42], S.FMT_CR0, "Trade receivable days. FY26 553cr / 4834cr rev ~42d.")
    driver("payable_pct", "Other current liab (% of revenue)",
           None, [1.10, 1.05, 1.00], S.FMT_PCT,
           "Current liabilities incl clearing/settlement float scale with activity.")
    driver("tax_rate", "Effective tax rate (%)",
           None, [0.25, 0.25, 0.25], S.FMT_PCT, "Effective tax. FY26 824cr / 3299cr PBT ~25%.")
    driver("dividend_payout", "Dividend payout (% of PAT)",
           None, [0.13, 0.13, 0.13], S.FMT_PCT, "Payout ratio. FY26 316cr / 2487cr PAT ~13%.")

    # ---------------- WACC / CAPM ----------------
    # Single-input drivers live in column E (FY27E) and are referenced without a year.
    S.section(ws, r, "7. VALUATION — WACC build-up (CAPM) & terminal", ncols); r += 1
    driver("rf", "Risk-free rate (%)", None, [0.070, None, None], S.FMT_PCT,
           "SECONDARY: 10Y India G-sec ~7.0%. Editable single input (col E).")
    driver("erp", "Equity risk premium (%)", None, [0.060, None, None], S.FMT_PCT,
           "SECONDARY: India ERP ~6.0%. Editable single input.")
    driver("beta", "Beta (levered)", None, [0.95, None, None], S.FMT_NUM,
           "SECONDARY: BSE beta vs Nifty ~0.95. Editable single input.")
    driver("cost_debt", "Pre-tax cost of debt (%)", None, [0.080, None, None], S.FMT_PCT,
           "BSE is effectively debt-free; nominal cost of debt for structure.")
    driver("wt_equity", "Target weight — equity (%)", None, [1.00, None, None], S.FMT_PCT,
           "BSE runs ~100% equity funded. Editable target structure.")
    # wt_debt is a formula = 1 - equity weight (same-sheet -> black)
    r_wtE = A_ROW["wt_equity"]
    driver("wt_debt", "Target weight — debt (%)", None,
           [f"=1-E{r_wtE}", None, None], S.FMT_PCT,
           "Target debt weight = 1 - equity weight (same-sheet formula).")
    driver("term_growth", "Terminal growth rate (%)", None, [0.050, None, None], S.FMT_PCT,
           "Long-run growth into perpetuity ~5.0%. Editable; used in Gordon TV.")

    # ---------------- MARKET DATA ----------------
    S.section(ws, r, "8. MARKET DATA (BSE share price & count)", ncols); r += 1
    driver("bse_price", "BSE share price (Rs)", None, [D.BSE_MARKET["price_basis"], None, None], S.FMT_RS,
           "NSE Bhavcopy close 4-Sep-2026 = Rs 3,409.80. Editable.")
    driver("bse_shares", "BSE shares outstanding (cr)", None, [D.BSE_MARKET["shares_paid_up_cr"], None, None], S.FMT_NUM,
           "Paid-up 40,78,84,077 = 40.7884 cr [AR FY26 Note 14].")
    driver("net_debt", "BSE net debt (Rs cr)", None, [-5000.0, None, None], S.FMT_CR0,
           "BSE is net cash (debt-free); negative = net cash. Editable seed for EV bridge.")

    # ---------------- MISC PROJECTED LINE INPUTS (avoid embedded constants) ----------------
    S.section(ws, r, "9. MISC PROJECTED LINE INPUTS (editable, kept explicit)", ncols); r += 1
    driver("currency_txn", "Currency derivatives txn charges (Rs cr)",
           None, [0.0, 0.0, 0.0], S.FMT_CR,
           "NOT-DISCLOSED in MD&A split. Editable; default 0 (immaterial).")
    driver("slb_txn", "SLB txn charges (Rs cr)",
           None, [0.0, 0.0, 0.0], S.FMT_CR,
           "NOT-DISCLOSED separately. Editable; default 0 (immaterial).")
    driver("finance_cost", "Finance cost (Rs cr)",
           None, [0.0, 0.0, 0.0], S.FMT_CR,
           "BSE effectively debt-free. Editable; default 0.")
    driver("exceptional", "Exceptional items (Rs cr)",
           None, [0.0, 0.0, 0.0], S.FMT_CR,
           "Non-recurring; editable; default 0.")

    # store the last-row marker
    A_ROW["__end__"] = r
    ws.freeze_panes = "B6"
    return ws


def aref(key, fy=None, absolute=True):
    """Return an Assumptions reference like Assumptions!$E$42.
    If fy given, pick that year's column; else default to col E (FY27E) for
    single-input drivers."""
    row = A_ROW[key]
    col = COL_FY[fy] if fy else COL_FY["FY27E"]
    cl = gcl(col)
    if absolute:
        return f"Assumptions!${cl}${row}"
    return f"Assumptions!{cl}{row}"
