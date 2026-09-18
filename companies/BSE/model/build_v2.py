#!/usr/bin/env python3
"""
BSE Ltd financial model — VERSION 2 (advanced).

Fixes the 18 defects in CRITIQUE.md. Key architectural changes vs v1:
  * THREE exogenous driver series (premium ADT / notional ADT / contract count), not one
  * the premium-notional WEDGE is an explicit live driver; the SEBI levy is computed from it
  * DCF values OPERATIONS only (investment income excluded from FCFF); the treasury corpus is
    added ONCE in the bridge -> removes the v1 double-count
  * own-account vs earmarked (clearing float) money separated everywhere
  * Core SGF modelled at announced POLICY (5% of transaction revenue) with a switch
  * an ex-levy COST FLOOR that does not fall with revenue
  * scenario manager (Base / Bear / Bull) resolved through an ACTIVE column
  * Cash Flow tab computing headline CFO vs own-account CFO
  * Checks tab reconciling to EPS 61.22, P/E 55.7x and the disclosed actuals
"""
import json
import openpyxl
from openpyxl.utils import get_column_letter as gcl
from openpyxl.workbook.defined_name import DefinedName

import bse_data as D1          # historical statement actuals (lakh)
import bse_data_v2 as D2       # real driver series (crore)
import bse_style as S

OUT = "BSE_Financial_Model_v2.xlsx"

# ---- Assumptions tab column map ----
A_HIST = {"FY24": 2, "FY25": 3, "FY26": 4}
A_BASE, A_BEAR, A_BULL, A_ACT, A_NOTE = 5, 6, 7, 8, 9
SCEN_CELL = "$C$4"

# ---- Statement tab column map ----
COL = {"FY24": 2, "FY25": 3, "FY26": 4, "FY27E": 5, "FY28E": 6, "FY29E": 7}
HIST = ["FY24", "FY25", "FY26"]
PROJ = ["FY27E", "FY28E", "FY29E"]
YEARS = HIST + PROJ
NOTE_COL = 8


def cl(fy):
    return gcl(COL[fy])


AR = {}     # assumption key -> row on Assumptions
DR = {}     # Drivers tab rows
SG = {}     # Segment rows
IS = {}     # Income Statement rows
BS = {}     # Balance Sheet rows
CF = {}     # Cash Flow rows
DC = {}     # DCF rows
CK = {}     # Checks rows


def act(key):
    """Reference the ACTIVE (scenario-resolved) value of an assumption."""
    return f"Assumptions!${gcl(A_ACT)}${AR[key]}"


def hist_a(key, fy):
    return f"Assumptions!${gcl(A_HIST[fy])}${AR[key]}"


# ===========================================================================
# 1. ASSUMPTIONS
# ===========================================================================
def build_assumptions(wb):
    ws = wb.create_sheet("Assumptions")
    ws.sheet_properties.tabColor = "FFFFC000"
    ncols = 9
    S.title_block(
        ws, "BSE Ltd — Assumptions, Drivers & Scenario Manager",
        "Yellow cells are editable. Base/Bear/Bull are typed inputs; the ACTIVE column resolves the "
        "selected scenario and is the ONLY column downstream tabs reference. "
        "Driver architecture follows management's own statement: revenue on premium, SEBI levy on "
        "notional, clearing on contracts.",
        "Units: Rs Crore. Percentages stored as decimals. Realisation = Rs cr of charges per Rs cr of ADT.",
        ncols)
    ws.column_dimensions["A"].width = 46
    for c in "BCDEFGH":
        ws.column_dimensions[c].width = 13
    ws.column_dimensions["I"].width = 62

    # scenario selector
    S.label(ws, "A4", "SCENARIO  (1 = Base · 2 = Bear · 3 = Bull)", bold=True)
    S.set_cell(ws, SCEN_CELL.replace("$", ""), 1, fmt="0", input_cell=True, bold=True)
    S.label(ws, "E4", "<- change this one cell to switch the whole model", italic=True, size=9,
            color="FFC00000")

    r = 6
    S.label(ws, f"A{r}", "Driver", bold=True)
    for fy, c in A_HIST.items():
        cc = ws.cell(row=r, column=c)
        cc.value = fy
        cc.number_format = "@"
        cc.font = S.Font(name="Calibri", size=10, bold=True, color=S.WHITE)
        cc.fill = S.PatternFill("solid", fgColor="FF375623")
        cc.alignment = S.Alignment(horizontal="center")
    for col, nm, bg in ((A_BASE, "Base", "FF2E75B6"), (A_BEAR, "Bear", "FFC00000"),
                        (A_BULL, "Bull", "FF548235"), (A_ACT, "ACTIVE", "FF7030A0")):
        cc = ws.cell(row=r, column=col)
        cc.value = nm
        cc.font = S.Font(name="Calibri", size=10, bold=True, color=S.WHITE)
        cc.fill = S.PatternFill("solid", fgColor=bg)
        cc.alignment = S.Alignment(horizontal="center")
    S.label(ws, f"I{r}", "Source / basis", bold=True)
    r += 1

    def drv(key, lbl, hist, base, bear, bull, fmt, note, indent=1):
        """One driver row: historical actuals (blue) + 3 scenario inputs + ACTIVE formula."""
        nonlocal r
        AR[key] = r
        S.label(ws, f"A{r}", lbl, indent=indent)
        if hist:
            for fy, v in hist.items():
                if v is not None and fy in A_HIST:
                    S.set_cell(ws, f"{gcl(A_HIST[fy])}{r}", v, fmt=fmt, input_cell=True)
        for col, v in ((A_BASE, base), (A_BEAR, bear), (A_BULL, bull)):
            S.set_cell(ws, f"{gcl(col)}{r}", v, fmt=fmt, input_cell=True)
        # ACTIVE = CHOOSE(scenario, base, bear, bull)  (same-sheet -> black)
        S.set_cell(ws, f"{gcl(A_ACT)}{r}",
                   f"=CHOOSE({SCEN_CELL},{gcl(A_BASE)}{r},{gcl(A_BEAR)}{r},{gcl(A_BULL)}{r})",
                   fmt=fmt, bold=True)
        S.label(ws, f"I{r}", note, italic=True, size=8, color="FF555555")
        r += 1

    # ---------------- DRIVER 1: premium ADT ----------------
    S.section(ws, r, "DRIVER 1 — index-options PREMIUM ADT (revenue rides this)", ncols); r += 1
    drv("padt_g1", "Premium ADT growth — FY27E (%)", None, 0.35, 0.00, 0.60, S.FMT_PCT,
        "Applied to the FY26 AVERAGE of Rs19,523cr. Base +35% -> Rs26,356cr, which is still 11% BELOW "
        "the Q1FY27 actual of Rs29,615cr, so the base is NOT aggressive on this driver. "
        "WARNING on the bear: 0% holds FY27E at the FY26 average, which is a 34% FALL from the "
        "already-printed Q1FY27 run-rate — the bear is a reversion case, not a 'flat' case. "
        "[AR FY26 MD&A p58/pr47; Q1FY27 IP slide 13]")
    drv("padt_g2", "Premium ADT growth — FY28E (%)", None, 0.08, -0.05, 0.35, S.FMT_PCT,
        "Bull = the 34.97%/yr for 3 years the research says the price requires.")
    drv("padt_g3", "Premium ADT growth — FY29E (%)", None, 0.0646, 0.00, 0.35, S.FMT_PCT,
        "Base set EQUAL to two-exchange pool growth (6.46%) so implied market share STOPS rising — "
        "otherwise the base case silently assumes BSE keeps taking share from NSE forever, which "
        "contradicts 'share gains exhaust'. Check the implied FY29E share on the Checks tab.")
    drv("realis_deriv", "Derivatives realisation (Rs cr per Rs cr premium ADT)",
        {"FY25": D2.REALISATION_DERIV["FY25"], "FY26": D2.REALISATION_DERIV["FY26"]},
        0.152520, 0.144492, 0.160547, "0.000000",
        "FY26 = 3,134.37/19,523 = 0.160547 (+1.83% on FY25). Q1FY27 realisation went FLAT then -1.63%. "
        "Base holds it 5% below FY26 per the research's base case.")

    # ---------------- DRIVER 2: the wedge & notional ----------------
    S.section(ws, r, "DRIVER 2 — the premium/notional WEDGE (the levy rides this)", ncols); r += 1
    drv("wedge", "Premium / notional ratio (%)",
        {"FY25": D2.WEDGE["FY25"], "FY26": D2.WEDGE["FY26"]},
        D2.WEDGE["FY26"], D2.WEDGE["Q2FY26"], D2.WEDGE["Q1FY27"], "0.00000%",
        "THE key variable. FY26 0.104315%. Bear = Q2FY26 low 0.091491% ALREADY PRINTED this cycle "
        "(costs Rs385cr of derivatives revenue). Bull = Q1FY27 high 0.124959%. "
        "Management: 'it is, of course, not predictable'.")
    drv("levy_rate", "SEBI levy rate (Rs cr per Rs cr notional ADT)",
        {"FY25": D2.LEVY_RATE_PER_NOTIONAL["FY25"], "FY26": D2.LEVY_RATE_PER_NOTIONAL["FY26"]},
        D2.LEVY_RATE_PER_NOTIONAL["FY26"], D2.LEVY_RATE_PER_NOTIONAL["FY26"],
        D2.LEVY_RATE_PER_NOTIONAL["FY26"], "0.00000000",
        "FY26 566.16/18,715,375 = 0.00003025. Tracked its base to +1.0%. SEBI sets the rate; "
        "a rate change is a separate thesis-breaker, held flat here.")

    # ---------------- DRIVER 3: contracts ----------------
    S.section(ws, r, "DRIVER 3 — CONTRACT COUNT (clearing cost rides this)", ncols); r += 1
    drv("contracts_g", "Contract count growth (%)",
        None, 0.05, -0.10, 0.15, S.FMT_PCT,
        "FY26 contracts FELL 6.53% while revenue rose 63.46% — proof the three series diverge. "
        "Avg daily lots 153mn (Q2FY25) -> 100mn (Q2FY26).")
    drv("clearing_per_unit", "Clearing cost per contract-index unit (Rs cr)",
        {"FY26": D2.TARGETS["clearing_FY26"]},
        280.35, 300.00, 260.00, S.FMT_CR,
        "FY26 clearing 280.35cr at contracts index 1.000. Fell 19.45% while notional rose 69.11% "
        "(81.18% of the fall was an intra-group elimination, per W3_cost).")

    # ---------------- CASH MARKET ----------------
    S.section(ws, r, "EQUITY CASH SEGMENT", ncols); r += 1
    drv("cadt_g", "Cash ADT growth (%)", None, 0.02, -0.10, 0.06, S.FMT_PCT,
        "FY26 cash ADT Rs7,950cr (+2.36%). Three down-years in ten; FY18->FY20 peak-to-trough -39.2%.")
    drv("realis_cash", "Cash realisation (Rs cr per Rs cr cash ADT)",
        {"FY25": D2.REALISATION_CASH["FY25"], "FY26": D2.REALISATION_CASH["FY26"]},
        0.028800, 0.027100, 0.031473, "0.000000",
        "FY26 = 250.21/7,950 = 0.031473, DOWN 19.48% on a RISING volume base (a repricing, "
        "not a volume effect). Q1FY27 a further -13.93%.")

    # ---------------- OTHER REVENUE ----------------
    S.section(ws, r, "OTHER REVENUE LINES (growth on prior year)", ncols); r += 1
    drv("g_starmf", "StAR MF platform fees growth (%)", None, 0.15, 0.00, 0.25, S.FMT_PCT,
        "FY26 +23%. But realisation per order FELL 2.56%, then 6.33% in Q1FY27.")
    drv("g_listing", "Listing fees growth (%)", None, 0.10, 0.04, 0.14, S.FMT_PCT,
        "FY26 +10%. Annual fee per listed company Rs4.273 lakh, +4.01% — the ONLY rising realisation.")
    drv("g_bookbuild", "Book building / IPO fees growth (%)", None, 0.10, -0.10, 0.20, S.FMT_PCT,
        "FY26 +9%. Cyclical with the IPO pipeline.")
    drv("g_data", "Data feed & index licensing growth (%)", None, 0.14, 0.05, 0.22, S.FMT_PCT,
        "Colocation +133% in FY26 off a small base; Asia Index/S&P BSE licensing.")
    drv("g_other_op", "Other operating income growth (%)", None, 0.10, 0.00, 0.15, S.FMT_PCT,
        "Residual other operating income.")
    drv("currency_txn", "Currency derivatives txn charges (Rs cr)", {"FY26": 0.0},
        0.0, 0.0, 0.0, S.FMT_CR,
        "EXTINGUISHED. RBI's 5-Jan-2024 directions took currency-derivatives ADT from Rs9,734cr to NIL. "
        "Two of five derivative segments extinguished in four years. Kept as an explicit line at zero.")
    drv("slb_txn", "SLB (securities lending) txn charges (Rs cr)", {"FY26": 0.0},
        0.0, 0.0, 0.0, S.FMT_CR,
        "NOT-DISCLOSED separately -> AR audited Note 22. Immaterial; explicit zero.")
    drv("other_reg_sundry", "Other regulatory & sundry expense (Rs cr)", {"FY26": 77.97},
        77.97, 85.00, 70.00, S.FMT_CR,
        "RECONCILIATION LINE. Bridges the component build to reported total expenses of Rs1,837.42cr. "
        "Exists because the MD&A 'regulatory contribution' caption (Rs649.69cr) and the audited expense "
        "lines group the SEBI fee and Core SGF differently. Ties FY26 exactly; held flat forward.")
    drv("attrib_factor", "PAT attributable / PAT total (x)", {"FY26": 1.0039},
        1.0039, 1.0039, 1.0039, S.FMT_NUM,
        "FY26 2,496.98/2,487.25 = 1.0039 — non-controlling interests are marginally loss-making.")
    drv("discontinued", "Profit from discontinued operations (Rs cr)", {"FY26": 11.95},
        0.0, 0.0, 0.0, S.FMT_CR,
        "FY26 Rs11.95cr (Rs1,195 lakh). Explains the PBT-less-tax vs reported-PAT gap exactly. "
        "Nil projected — it is by definition non-recurring.")
    drv("txn_audited_uplift", "Audited-vs-MD&A transaction revenue uplift (x)", {"FY26": 1.0342},
        1.0342, 1.0342, 1.0342, S.FMT_NUM,
        "The audited transaction-charges line is Rs3,794.99cr against the MD&A build of Rs3,669.48cr "
        "(3,794.99/3,669.48 = 1.0342). The Core SGF policy rate applies to the AUDITED base, so the "
        "build is grossed up. This gap exists because the product split is unaudited.")

    # ---------------- TREASURY (own vs float) ----------------
    S.section(ws, r, "TREASURY — own corpus vs earmarked float (kept separate)", ncols); r += 1
    drv("own_corpus_g", "Own investible corpus growth (%)", None, 0.15, 0.05, 0.20, S.FMT_PCT,
        "Own corpus closing FY26 Rs6,101.90cr (+66.3%). This is SHAREHOLDERS' money.")
    drv("own_yield", "Own-corpus yield (%)",
        {"FY25": D2.OWN_CORPUS_YIELD["FY25"], "FY26": D2.OWN_CORPUS_YIELD["FY26"]},
        0.05942, 0.05000, 0.06500, S.FMT_PCT,
        "Yield FELL 7.500% -> 5.942%, -156bp/-20.8%. Held at the FY26 realised level in base.")
    drv("float_g", "Earmarked clearing float growth (%)", None, 0.05, -0.10, 0.10, S.FMT_PCT,
        "Clearing/settlement float Rs3,554cr FY26. NOT owner cash — excluded from equity value.")
    drv("float_yield", "Float yield (%)",
        {"FY25": D2.FLOAT_YIELD["FY25"], "FY26": D2.FLOAT_YIELD["FY26"]},
        0.0499, 0.0400, 0.0600, S.FMT_PCT,
        "Treasury on clearing float 6.32% -> 4.99%, -21.0%.")

    # ---------------- COSTS ----------------
    S.section(ws, r, "OPERATING COSTS", ncols); r += 1
    drv("g_emp", "Employee cost growth (%)", None, 0.12, 0.10, 0.14, S.FMT_PCT,
        "FY26 +26% (incl Rs13.01cr non-recurring gratuity past-service cost).")
    drv("g_tech", "Technology cost growth (%)", None, 0.15, 0.12, 0.18, S.FMT_PCT,
        "FY26 +24%. Data-centre and platform build.")
    drv("g_admin", "Other admin cost growth (%)", None, 0.09, 0.08, 0.10, S.FMT_PCT,
        "Other administrative expenses.")
    drv("cost_floor_on", "Cost-floor switch (1 = ON, 0 = OFF)", None, 1, 1, 1, "0",
        "W7_bearcase: the ex-levy cost floor Rs1,187.73cr 'has never contracted in a down year'. "
        "ON means controllable opex cannot fall below the inflated floor however far revenue falls.")
    drv("floor_infl", "Cost-floor inflation (%)", None, 0.06, 0.06, 0.06, S.FMT_PCT,
        "Applied to the Rs1,187.73cr FY26 ex-levy floor.")
    drv("sgf_mode", "Core SGF mode (1 = as charged, 2 = announced policy)", None, 2, 2, 1, "0",
        "Policy = 5% of transaction revenue = Rs189.75cr vs Rs76.96cr charged (2.47x). "
        "Q1FY27 already annualises at Rs103.64cr. Counter-cyclical: rises with volatility.")
    drv("sgf_policy_rate", "Core SGF policy rate (% of txn revenue)", None,
        D2.SGF_POLICY_RATE, D2.SGF_POLICY_RATE, D2.SGF_POLICY_RATE, S.FMT_PCT,
        "Announced 5% monthly, capped 150% of minimum. Source is a CONCALL only — "
        "NOT in the FY26 annual report. [Q2FY26 Concall 17Nov2025, MD]")

    # ---------------- BELOW THE LINE ----------------
    S.section(ws, r, "BELOW-THE-LINE, CAPEX, WORKING CAPITAL, TAX", ncols); r += 1
    drv("associate", "Associate (CDSL) profit (Rs cr)",
        {"FY24": 71.82, "FY25": 82.59, "FY26": 65.42},
        65.42, 55.00, 75.00, S.FMT_CR,
        "FY26 contribution FELL 13.4%. SEBI caps the stake at 15% so it CANNOT be increased — "
        "BSE is a forced holder. Held flat in base, not grown.")
    drv("other_income", "Other income (Rs cr)", {"FY26": 23.85}, 23.85, 20.00, 28.00, S.FMT_CR,
        "Small; held near the FY26 level.")
    drv("finance_cost", "Finance cost (Rs cr)", {"FY26": 0.16}, 0.20, 0.50, 0.10, S.FMT_CR,
        "BSE is effectively debt-free.")
    drv("exceptional", "Exceptional items (Rs cr)", {"FY26": 0.0}, 0.0, 0.0, 0.0, S.FMT_CR,
        "Non-recurring; nil projected. FY24 had Rs406.62cr (CDSL-related).")
    drv("capex_pct", "Capex (% of revenue from operations)", None, 0.07, 0.05, 0.08, S.FMT_PCT,
        "FY26 capex Rs515.16cr = 10.7% of revenue (elevated: data-centre). Normalised lower.")
    drv("da_pct", "D&A (% of opening net block)", None, 0.22, 0.22, 0.22, S.FMT_PCT,
        "FY26 D&A Rs158.96cr on opening net block Rs262.90cr. Forward floor includes "
        "~Rs12.12cr already committed from FY26 additions.")
    drv("recv_days", "Receivable days (on revenue)", None, 42, 55, 38, "0",
        "FY26 receivables Rs553.16cr / revenue Rs4,833.95cr = 41.8 days.")
    drv("payables_pct", "Own payables (% of controllable opex)", None, 0.35, 0.35, 0.35, S.FMT_PCT,
        "Own-account payables driven off cost base, NOT off revenue (v1 error).")
    drv("tax_rate", "Effective tax rate (%)", None, 0.25, 0.25, 0.25, S.FMT_PCT,
        "FY26 823.84/3,299.14 = 24.97%.")
    drv("payout", "Dividend payout (% of PAT attributable)", None, 0.13, 0.13, 0.13, S.FMT_PCT,
        "FY26 dividend Rs315.85cr / PAT attributable Rs2,496.98cr = 12.6%. "
        "NO dividend policy exists in ten annual reports; every listed peer publishes one.")

    # ---------------- VALUATION ----------------
    S.section(ws, r, "VALUATION — WACC, terminal, market data", ncols); r += 1
    drv("rf", "Risk-free rate (%)", None, 0.070, 0.075, 0.065, S.FMT_PCT,
        "SECONDARY: 10Y India G-sec.")
    drv("erp", "Equity risk premium (%)", None, 0.060, 0.070, 0.055, S.FMT_PCT, "SECONDARY: India ERP.")
    drv("beta", "Beta (levered)", None, 0.95, 1.15, 0.85, S.FMT_NUM,
        "SECONDARY. Bear beta raised: revenue is one product on one regulator-allocated expiry slot.")
    drv("cost_debt", "Pre-tax cost of debt (%)", None, 0.080, 0.080, 0.080, S.FMT_PCT,
        "Nominal; BSE carries effectively no debt.")
    drv("wt_equity", "Target weight — equity (%)", None, 1.00, 1.00, 1.00, S.FMT_PCT,
        "~100% equity funded.")
    drv("term_growth", "Terminal growth (%)", None, 0.040, 0.030, 0.050, S.FMT_PCT,
        "LOWERED from v1's 5%: FY26 is peak-cycle (Q1FY27 revenue +0.16% sequential, 110.1% of the "
        "profit increase non-operating) and ~9/10 of FY26 growth was share TRANSFER from NSE, "
        "which cannot compound in perpetuity.")
    drv("tv_method", "Terminal value method (1 = Gordon, 2 = H-model fade)", None, 2, 1, 2, "0",
        "A 3-year explicit window with immediate perpetuity understates a company moving from +63% "
        "growth to maturity. Method 2 fades growth from g_fade to terminal g over the fade period.")
    drv("g_fade", "Growth immediately after explicit period (%)", None, 0.12, 0.04, 0.20, S.FMT_PCT,
        "Starting point of the fade. Base 12% is below FY26's +63% and above the terminal 4%.")
    drv("fade_years", "Fade period (years)", None, 10, 5, 12, "0",
        "H-model half-life = fade_years / 2. Longer fade = more value attributed to the transition.")
    drv("pool_g", "Two-exchange premium pool growth (%)", None, 0.0646, 0.00, 0.12, S.FMT_PCT,
        "FY26 pool grew only 6.46% while BSE's share went 14.44% -> 21.58%. "
        "Used in Checks to print the IMPLIED terminal market share.")
    drv("assoc_value", "CDSL stake MARKET value (Rs cr)", {"FY26": 3509.32},
        3509.32, 3509.32, 3509.32, S.FMT_CR,
        "Rs3,50,932 lakh [AR FY26, Note 8]. EVIDENCED — an earlier draft wrongly called this "
        "unverified. Used ONLY when cdsl_mode = 2.")
    drv("cdsl_mode", "CDSL treatment (1 = equity earnings, 2 = market value)", None, 1, 1, 2, "0",
        "W5 constraint 4: market value OR earnings, NEVER both. Mode 1 keeps the associate profit in "
        "PBT and values the stake at nil. Mode 2 strips the associate profit and adds the market value "
        "in the bridge. Switching modes must never do both.")
    drv("price", "BSE share price (Rs)", {"FY26": D2.PRICE}, D2.PRICE, D2.PRICE, D2.PRICE, S.FMT_RS,
        "NSE Bhavcopy close 4-Sep-2026.")
    drv("shares", "Shares PAID-UP (cr) — for market cap", {"FY26": D2.SHARES_PAID_UP_CR},
        D2.SHARES_PAID_UP_CR, D2.SHARES_PAID_UP_CR, D2.SHARES_PAID_UP_CR, S.FMT_NUM,
        "Paid-up 40,78,84,077. Used for MARKET CAP and for value-per-share.")
    drv("shares_issued", "Shares ISSUED (cr) — for EPS", {"FY26": D2.SHARES_ISSUED_CR},
        D2.SHARES_ISSUED_CR, D2.SHARES_ISSUED_CR, D2.SHARES_ISSUED_CR, S.FMT_NUM,
        "Issued 41,19,79,077. The 40,95,000 difference is 2005 demutualisation shares held in "
        "abeyance. EPS MUST use issued: 2,496.98/41.1979 = Rs60.61 (audited). An earlier draft "
        "divided by paid-up and wrongly printed Rs61.22.")
    drv("inv_recurring_pct", "Recurring share of investment income (%)", None,
        0.6943, 0.6943, 0.6943, S.FMT_PCT,
        "W5: ~30.57% of investment income is MARK-TO-MARKET revaluation, 'not a yield and should not "
        "carry an operating multiple'. Recurring share = 1 - 0.3057 = 69.43%.")
    drv("strip_float", "Strip float income from operating EBIT (1 = yes)", None, 1, 1, 1, "0",
        "Rs171.42cr of FY26 revenue is interest earned on MEMBERS' clearing float at 4.99%, credited "
        "to shareholders as revenue. It is not customer income, so it is removed from the FCFF base "
        "by default.")

    ws.freeze_panes = "B7"
    AR["__end__"] = r
    return ws


def _yrhdr(ws, r):
    S.label(ws, f"A{r}", "Rs Crore / as marked", bold=True)
    S.year_header(ws, r, COL["FY24"], YEARS, hist_count=3)
    S.label(ws, f"{gcl(NOTE_COL)}{r}", "Source / formula basis", bold=True)


def _w(ws):
    ws.column_dimensions["A"].width = 44
    for c in "BCDEFG":
        ws.column_dimensions[c].width = 14
    ws.column_dimensions[gcl(NOTE_COL)].width = 56


# ===========================================================================
# 2. DRIVERS & HISTORY  — the three exogenous series
# ===========================================================================
def build_drivers(wb):
    ws = wb.create_sheet("Drivers & History")
    ws.sheet_properties.tabColor = "FF00B0F0"
    ncols = NOTE_COL
    S.title_block(
        ws, "BSE Ltd — Driver Series (the three exogenous variables)",
        "Management: 'the SEBI turnover fee is based on the notional trading, the clearing expense is "
        "based on the number of contracts, and we earn revenue based on premium'. Those are three "
        "different series and they diverge — FY26 revenue +63.46%, notional +69.12%, contracts -6.53%.",
        "ADT figures in Rs crore. Historical actuals in blue. Projections reference Assumptions ACTIVE column.",
        ncols)
    _w(ws)
    r = 5
    _yrhdr(ws, r); r += 1

    def row(key, lbl, hist, proj, note, fmt=S.FMT_CR0, bold=False, indent=1):
        nonlocal r
        DR[key] = r
        S.label(ws, f"A{r}", lbl, bold=bold, indent=indent)
        for fy, v in (hist or {}).items():
            if fy in COL and v is not None:
                S.set_cell(ws, f"{cl(fy)}{r}", v, fmt=fmt, input_cell=True, bold=bold)
        for i, fy in enumerate(PROJ):
            f = proj(fy, i) if callable(proj) else None
            if f:
                S.set_cell(ws, f"{cl(fy)}{r}", f, fmt=fmt, bold=bold)
        S.label(ws, f"{gcl(NOTE_COL)}{r}", note, italic=True, size=8, color="FF555555")
        r += 1

    S.section(ws, r, "DRIVER 1 — index-options PREMIUM ADT (revenue base)", ncols); r += 1
    gkeys = ["padt_g1", "padt_g2", "padt_g3"]
    row("premium_adt", "Premium ADT (Rs cr)",
        {"FY25": D2.PREMIUM_ADT["FY25"], "FY26": D2.PREMIUM_ADT["FY26"]},
        lambda fy, i: f"={cl(YEARS[YEARS.index(fy)-1])}{DR['premium_adt']}*(1+{act(gkeys[i])})",
        "FY24 NOT DISCLOSED at this granularity. FY27E-FY29E = prior x (1 + growth) per year.",
        bold=True)

    S.section(ws, r, "DRIVER 2 — the WEDGE and the NOTIONAL base it implies", ncols); r += 1
    row("wedge", "Premium / notional ratio",
        {"FY25": D2.WEDGE["FY25"], "FY26": D2.WEDGE["FY26"]},
        lambda fy, i: f"={act('wedge')}",
        "THE key variable. Quarterly range 0.091491% - 0.124959% = +/-37% inside eight quarters.",
        fmt="0.00000%", bold=True)
    row("notional_adt", "Notional ADT (Rs cr)  = premium / wedge",
        None,
        lambda fy, i: f"={cl(fy)}{DR['premium_adt']}/{cl(fy)}{DR['wedge']}",
        "DERIVED. FY26 19,523/0.104315% = 18,715,429 (actual 18,715,375). "
        "958.6x the base BSE bills on.", bold=True)
    # historical notional as formula from the two series (same-sheet -> black)
    for fy in ("FY25", "FY26"):
        S.set_cell(ws, f"{cl(fy)}{DR['notional_adt']}",
                   f"={cl(fy)}{DR['premium_adt']}/{cl(fy)}{DR['wedge']}", fmt=S.FMT_CR0, bold=True)

    S.section(ws, r, "DRIVER 3 — CONTRACT COUNT (clearing-cost base), indexed FY26 = 1.000", ncols); r += 1
    row("contracts", "Contract count index",
        {"FY25": D2.CONTRACTS_INDEX["FY25"], "FY26": D2.CONTRACTS_INDEX["FY26"]},
        lambda fy, i: f"={cl(YEARS[YEARS.index(fy)-1])}{DR['contracts']}*(1+{act('contracts_g')})",
        "Only the CHANGE is disclosed (-6.53% in FY26), not an audited annual count. "
        "FY25 index = 1/(1-0.0653) = 1.0699.", fmt=S.FMT_NUM, bold=True)

    S.section(ws, r, "EQUITY CASH — average daily turnover", ncols); r += 1
    row("cash_adt", "Cash ADT (Rs cr)",
        {"FY24": D2.CASH_ADT_SERIES["FY24"], "FY25": D2.CASH_ADT_SERIES["FY25"],
         "FY26": D2.CASH_ADT_SERIES["FY26"]},
        lambda fy, i: f"={cl(YEARS[YEARS.index(fy)-1])}{DR['cash_adt']}*(1+{act('cadt_g')})",
        "Eleven-year series on the Drivers reference block below. Three down-years in ten.",
        bold=True)

    S.section(ws, r, "TREASURY — own corpus (shareholders') vs earmarked float (members')", ncols); r += 1
    row("own_corpus", "Own investible corpus — closing (Rs cr)",
        {"FY25": D2.OWN_CORPUS_CLOSING["FY25"], "FY26": D2.OWN_CORPUS_CLOSING["FY26"]},
        lambda fy, i: f"={cl(YEARS[YEARS.index(fy)-1])}{DR['own_corpus']}*(1+{act('own_corpus_g')})",
        "SHAREHOLDERS' money. Closing FY26 Rs6,101.90cr (+66.3%).", bold=True)
    row("own_corpus_avg", "Own corpus — average (Rs cr)",
        None,
        lambda fy, i: f"=AVERAGE({cl(YEARS[YEARS.index(fy)-1])}{DR['own_corpus']},{cl(fy)}{DR['own_corpus']})",
        "Average of opening and closing. Drives investment income.")
    S.set_cell(ws, f"{cl('FY26')}{DR['own_corpus_avg']}", D2.OWN_CORPUS_AVERAGE["FY26"],
               fmt=S.FMT_CR0, input_cell=True)
    S.set_cell(ws, f"{cl('FY25')}{DR['own_corpus_avg']}", D2.OWN_CORPUS_AVERAGE["FY25"],
               fmt=S.FMT_CR0, input_cell=True)
    row("float", "Earmarked clearing/settlement float (Rs cr)",
        D2.EARMARKED_FLOAT,
        lambda fy, i: f"={cl(YEARS[YEARS.index(fy)-1])}{DR['float']}*(1+{act('float_g')})",
        "MEMBERS' money, not shareholders'. Excluded from equity value. "
        "Its movement is what inflates reported CFO.")

    # ---- reference blocks (historical actuals only, blue) ----
    r += 1
    S.section(ws, r, "REFERENCE — eleven-year equity cash ADT (Rs cr)", ncols); r += 1
    S.label(ws, f"A{r}", "FY16 - FY26", indent=1, italic=True)
    for i, (fy, v) in enumerate(D2.CASH_ADT_SERIES.items()):
        c = gcl(2 + i)
        S.set_cell(ws, f"{c}{r}", v, fmt=S.FMT_CR0, input_cell=True)
        lab = ws.cell(row=r - 1, column=2 + i)
        lab.value = fy
        lab.font = S.Font(size=8, bold=True, color="FF375623")
        lab.alignment = S.Alignment(horizontal="center")
    S.label(ws, f"{gcl(13)}{r}", "Three down-years in ten; FY18->FY20 peak-to-trough -39.2%.",
            italic=True, size=8, color="FF555555")
    r += 2

    S.section(ws, r, "REFERENCE — the wedge, quarterly (the band that matters)", ncols); r += 1
    S.label(ws, f"A{r}", "Q1FY26 - Q1FY27", indent=1, italic=True)
    qs = [("Q1FY26", D2.WEDGE["Q1FY26"]), ("Q2FY26", D2.WEDGE["Q2FY26"]), ("Q3FY26", D2.WEDGE["Q3FY26"]),
          ("Q4FY26", D2.WEDGE["Q4FY26"]), ("Q1FY27", D2.WEDGE["Q1FY27"])]
    for i, (q, v) in enumerate(qs):
        c = gcl(2 + i)
        S.set_cell(ws, f"{c}{r}", v, fmt="0.00000%", input_cell=True)
        lab = ws.cell(row=r - 1, column=2 + i)
        lab.value = q
        lab.font = S.Font(size=8, bold=True, color="FF375623")
        lab.alignment = S.Alignment(horizontal="center")
    DR["wedge_q_low"] = r
    S.label(ws, f"{gcl(8)}{r}", "Q2FY26 is the low ALREADY PRINTED -> the bear case.",
            italic=True, size=8, color="FFC00000")
    r += 2

    S.section(ws, r, "REFERENCE — Q1FY27 actuals (the reality check)", ncols); r += 1
    for k, v in D2.Q1FY27.items():
        DR[f"q1_{k}"] = r
        S.label(ws, f"A{r}", f"Q1FY27 {k.replace('_', ' ')}", indent=1)
        S.set_cell(ws, f"B{r}", v, fmt=S.FMT_CR, input_cell=True)
        S.set_cell(ws, f"C{r}", f"=B{r}*4", fmt=S.FMT_CR)
        if r == DR["q1_revenue_ops"]:
            S.label(ws, f"{gcl(NOTE_COL)}{r}",
                    "Revenue grew +0.16% SEQUENTIALLY; 110.1% of the profit increase was non-operating.",
                    italic=True, size=8, color="FFC00000")
        r += 1
    S.label(ws, "B" + str(DR["q1_revenue_ops"] - 1), "Q1FY27", bold=True)
    S.label(ws, "C" + str(DR["q1_revenue_ops"] - 1), "x4 annualised", bold=True)

    ws.freeze_panes = "B6"
    return ws


# ===========================================================================
# 3. SEGMENT REVENUE BUILD
# ===========================================================================
def build_segment(wb):
    ws = wb.create_sheet("Segment Revenue Build")
    ws.sheet_properties.tabColor = "FF70AD47"
    ncols = NOTE_COL
    S.title_block(
        ws, "BSE Ltd — Segment Revenue Build",
        "Derivatives = premium ADT x realisation. Cash = cash ADT x realisation. "
        "WARNING: the product split is UNAUDITED — it exists only in the MD&A. The audited Note 22 "
        "stops at one aggregate (78.51% of revenue in a single line). "
        "NOT-DISCLOSED -> Ind AS 115.114 disaggregation note.",
        "Units: Rs Crore. Historical = STANDALONE MD&A split; consolidated via an explicit scalar.",
        ncols)
    _w(ws)
    r = 5
    _yrhdr(ws, r); r += 1

    def seg(key, lbl, hist_lakh, proj, note, bold=False, indent=1):
        nonlocal r
        SG[key] = r
        S.label(ws, f"A{r}", lbl, bold=bold, indent=indent)
        if hist_lakh:
            for i, fy in enumerate(HIST):
                v = hist_lakh[i]
                if v is not None:
                    S.set_cell(ws, f"{cl(fy)}{r}", D1.cr(v), fmt=S.FMT_CR, input_cell=True, bold=bold)
        for i, fy in enumerate(PROJ):
            f = proj(fy, i) if callable(proj) else None
            if f:
                S.set_cell(ws, f"{cl(fy)}{r}", f, fmt=S.FMT_CR, bold=bold)
        S.label(ws, f"{gcl(NOTE_COL)}{r}", note, italic=True, size=8, color="FF555555")
        r += 1

    S.section(ws, r, "TRANSACTION CHARGES", ncols); r += 1

    seg("deriv", "Equity derivatives txn charges",
        D1.SEG_ACTUALS_LAKH["txn_equity_derivatives"],
        lambda fy, i: f"='Drivers & History'!{cl(fy)}{DR['premium_adt']}*{act('realis_deriv')}",
        "= premium ADT x realisation. 64.84% of consolidated revenue — one product, one index, "
        "one regulator-allocated weekly expiry slot.")
    seg("cash", "Equity cash txn charges",
        D1.SEG_ACTUALS_LAKH["txn_equity_cash"],
        lambda fy, i: f"='Drivers & History'!{cl(fy)}{DR['cash_adt']}*{act('realis_cash')}",
        "= cash ADT x realisation. FY26 fell 18% on RISING volume — a repricing.")
    seg("currency", "Currency derivatives txn charges",
        [0.0, 0.0, 0.0],
        lambda fy, i: f"={act('currency_txn')}",
        "EXTINGUISHED by RBI direction (Rs9,734cr ADT -> nil).")
    seg("slb", "SLB txn charges", [0.0, 0.0, 0.0],
        lambda fy, i: f"={act('slb_txn')}", "NOT-DISCLOSED separately; immaterial.")
    seg("starmf", "StAR MF platform fees",
        D1.SEG_ACTUALS_LAKH["txn_starmf"],
        lambda fy, i: f"={cl(YEARS[YEARS.index(fy)-1])}{SG['starmf']}*(1+{act('g_starmf')})",
        "MF distribution platform. Realisation per order is FALLING (-2.56%, then -6.33%).")

    comp = ["deriv", "cash", "currency", "slb", "starmf"]
    SG["txn_total"] = r
    S.label(ws, f"A{r}", "Transaction charges — total", bold=True, indent=0)
    for fy in YEARS:
        expr = "+".join(f"{cl(fy)}{SG[k]}" for k in comp)
        S.set_cell(ws, f"{cl(fy)}{r}", f"={expr}", fmt=S.FMT_CR, bold=True)
    S.label(ws, f"{gcl(NOTE_COL)}{r}", "Sum of components. Drives the Core SGF policy charge.",
            italic=True, size=8, color="FF555555")
    r += 1

    S.section(ws, r, "NON-TRANSACTION REVENUE", ncols); r += 1
    seg("listing", "Listing fees (annual + processing)",
        D1.SEG_ACTUALS_LAKH["listing_fees"],
        lambda fy, i: f"={cl(YEARS[YEARS.index(fy)-1])}{SG['listing']}*(1+{act('g_listing')})",
        "The ONLY line whose realisation rose (+4.01% per listed company).")
    seg("bookbuild", "Book building / IPO fees",
        D1.SEG_ACTUALS_LAKH["book_building_fees"],
        lambda fy, i: f"={cl(YEARS[YEARS.index(fy)-1])}{SG['bookbuild']}*(1+{act('g_bookbuild')})",
        "Cyclical with the IPO pipeline.")
    seg("data", "Data feed & index licensing income",
        D1.SEG_ACTUALS_LAKH["colocation_income"],
        lambda fy, i: f"={cl(YEARS[YEARS.index(fy)-1])}{SG['data']}*(1+{act('g_data')})",
        "Colocation + Asia Index/S&P BSE licensing. FY26 colocation +133% off a small base.")

    SG["other_op"] = r
    S.label(ws, f"A{r}", "Other operating income (residual)", indent=1)
    for i, fy in enumerate(HIST):
        oo = D1.SEG_ACTUALS_LAKH["other_operating_income"][i]
        co = D1.SEG_ACTUALS_LAKH["colocation_income"][i]
        if oo is not None and co is not None:
            S.set_cell(ws, f"{cl(fy)}{r}", D1.cr(oo - co), fmt=S.FMT_CR, input_cell=True)
    for fy in PROJ:
        S.set_cell(ws, f"{cl(fy)}{r}",
                   f"={cl(YEARS[YEARS.index(fy)-1])}{r}*(1+{act('g_other_op')})", fmt=S.FMT_CR)
    S.label(ws, f"{gcl(NOTE_COL)}{r}", "Other operating income less colocation.",
            italic=True, size=8, color="FF555555")
    r += 1

    S.section(ws, r, "REVENUE FROM OPERATIONS", ncols); r += 1
    allrows = [SG[k] for k in ("txn_total", "listing", "bookbuild", "data", "other_op")]
    SG["rev_standalone"] = r
    S.label(ws, f"A{r}", "Revenue from operations — standalone build", bold=True, indent=0)
    for fy in YEARS:
        expr = "+".join(f"{cl(fy)}{rr}" for rr in allrows)
        S.set_cell(ws, f"{cl(fy)}{r}", f"={expr}", fmt=S.FMT_CR, bold=True)
    r += 1

    SG["scalar"] = r
    S.label(ws, f"A{r}", "Consolidation scalar (consol / standalone)", indent=1, italic=True)
    for i, fy in enumerate(HIST):
        if fy == "FY24":
            continue
        S.set_cell(ws, f"{cl(fy)}{r}",
                   f"={D1.cr(D1.REV_OPS_CONSOL_LAKH[i])}/{cl(fy)}{SG['rev_standalone']}", fmt=S.FMT_X)
    for fy in PROJ:
        S.set_cell(ws, f"{cl(fy)}{r}", f"=$D${r}", fmt=S.FMT_X)
    S.label(ws, f"{gcl(NOTE_COL)}{r}",
            "FY26 1.0815 held flat (documented anchor). Subsidiaries ICCL/India INX/BSE Institute/"
            "BSE Technologies supply 7.5% of consolidated revenue.", italic=True, size=8, color="FF555555")
    r += 1

    SG["rev_consol"] = r
    S.label(ws, f"A{r}", "REVENUE FROM OPERATIONS — consolidated", bold=True, indent=0)
    for fy in YEARS:
        if fy == "FY24":
            S.set_cell(ws, f"{cl(fy)}{r}", D1.cr(D1.REV_OPS_CONSOL_LAKH[0]), fmt=S.FMT_CR,
                       input_cell=True, bold=True)
        else:
            S.set_cell(ws, f"{cl(fy)}{r}",
                       f"={cl(fy)}{SG['rev_standalone']}*{cl(fy)}{SG['scalar']}", fmt=S.FMT_CR, bold=True)
    S.label(ws, f"{gcl(NOTE_COL)}{r}", "FY24 = direct actual (no split disclosed). Feeds the Income Statement.",
            italic=True, size=8, color="FF555555")
    r += 1

    S.section(ws, r, "INVESTMENT / TREASURY INCOME (own account only)", ncols); r += 1
    SG["inv_income"] = r
    S.label(ws, f"A{r}", "Investment income (own corpus)", bold=True, indent=0)
    for i, fy in enumerate(HIST):
        S.set_cell(ws, f"{cl(fy)}{r}", D1.cr(D1.IS_ACTUALS_LAKH["investment_income"][i]),
                   fmt=S.FMT_CR, input_cell=True, bold=True)
    for fy in PROJ:
        S.set_cell(ws, f"{cl(fy)}{r}",
                   f"='Drivers & History'!{cl(fy)}{DR['own_corpus_avg']}*{act('own_yield')}",
                   fmt=S.FMT_CR, bold=True)
    S.label(ws, f"{gcl(NOTE_COL)}{r}",
            "= average own corpus x own yield. FY26 4,885.84 x 5.942% = 290.30 (actual 290.30). "
            "EXCLUDED from FCFF — the corpus is added once in the DCF bridge instead.",
            italic=True, size=8, color="FFC00000")
    r += 1

    ws.freeze_panes = "B6"
    return ws


# ===========================================================================
# 4. INCOME STATEMENT
# ===========================================================================
def build_is(wb):
    ws = wb.create_sheet("Income Statement")
    ws.sheet_properties.tabColor = "FF4472C4"
    ncols = NOTE_COL
    S.title_block(
        ws, "BSE Ltd — Consolidated Income Statement",
        "SEBI levy computed on NOTIONAL turnover; clearing on CONTRACT COUNT; Core SGF at announced "
        "POLICY. An ex-levy COST FLOOR prevents controllable opex falling with revenue — the research "
        "records that the floor 'has never contracted in a down year'.",
        "Units: Rs Crore, consolidated. Historical actuals blue; projections formula-driven.", ncols)
    _w(ws)
    r = 5
    _yrhdr(ws, r); r += 1

    def row(key, lbl, hist_key, proj, note, bold=False, indent=1, fmt=S.FMT_CR, hist_vals=None):
        nonlocal r
        IS[key] = r
        S.label(ws, f"A{r}", lbl, bold=bold, indent=indent)
        vals = hist_vals if hist_vals is not None else (
            D1.IS_ACTUALS_LAKH[hist_key] if hist_key else None)
        if vals:
            for i, fy in enumerate(HIST):
                v = vals[i]
                if v is not None:
                    val = v if hist_vals is not None else D1.cr(v)
                    S.set_cell(ws, f"{cl(fy)}{r}", val, fmt=fmt, input_cell=True, bold=bold)
        for i, fy in enumerate(PROJ):
            f = proj(fy, i) if callable(proj) else None
            if f:
                S.set_cell(ws, f"{cl(fy)}{r}", f, fmt=fmt, bold=bold)
        S.label(ws, f"{gcl(NOTE_COL)}{r}", note, italic=True, size=8, color="FF555555")
        r += 1

    S.section(ws, r, "INCOME", ncols); r += 1

    IS["revenue"] = r
    S.label(ws, f"A{r}", "Revenue from operations", bold=True, indent=0)
    for fy in YEARS:
        S.set_cell(ws, f"{cl(fy)}{r}", f"='Segment Revenue Build'!{cl(fy)}{SG['rev_consol']}",
                   fmt=S.FMT_CR, bold=True)
    S.label(ws, f"{gcl(NOTE_COL)}{r}", "Link to Segment Revenue Build.", italic=True, size=8,
            color="FF555555")
    r += 1

    IS["inv_income"] = r
    S.label(ws, f"A{r}", "Investment income (own treasury)", indent=1)
    for fy in YEARS:
        S.set_cell(ws, f"{cl(fy)}{r}", f"='Segment Revenue Build'!{cl(fy)}{SG['inv_income']}",
                   fmt=S.FMT_CR)
    S.label(ws, f"{gcl(NOTE_COL)}{r}", "Link to Segment tab. NOT part of operating FCFF.",
            italic=True, size=8, color="FF555555")
    r += 1

    row("other_income", "Other income", "other_income", lambda fy, i: f"={act('other_income')}",
        "From Assumptions.")

    IS["total_income"] = r
    S.label(ws, f"A{r}", "Total income", bold=True, indent=0)
    for fy in YEARS:
        S.set_cell(ws, f"{cl(fy)}{r}",
                   f"={cl(fy)}{IS['revenue']}+{cl(fy)}{IS['inv_income']}+{cl(fy)}{IS['other_income']}",
                   fmt=S.FMT_CR, bold=True)
    r += 1

    # ------------------- CONTROLLABLE OPEX -------------------
    S.section(ws, r, "CONTROLLABLE OPERATING EXPENSES", ncols); r += 1

    row("employee", "Employee benefits expense", "employee_benefits",
        lambda fy, i: f"={cl(YEARS[YEARS.index(fy)-1])}{IS['employee']}*(1+{act('g_emp')})",
        "Prior x (1 + growth).")
    row("tech", "Technology & operating expense", "technology_expense",
        lambda fy, i: f"={cl(YEARS[YEARS.index(fy)-1])}{IS['tech']}*(1+{act('g_tech')})",
        "Prior x (1 + growth).")
    row("clearing", "Clearing & settlement expense", "clearing_settlement",
        lambda fy, i: f"='Drivers & History'!{cl(fy)}{DR['contracts']}*{act('clearing_per_unit')}",
        "= CONTRACT INDEX x cost per unit. FY26 fell 19.45% while notional rose 69.11% — "
        "proof the driver is contracts, not turnover. (v1 wrongly used % of revenue.)")
    row("admin", "Other administrative expenses", "other_admin_expenses",
        lambda fy, i: f"={cl(YEARS[YEARS.index(fy)-1])}{IS['admin']}*(1+{act('g_admin')})",
        "Prior x (1 + growth).")

    IS["da"] = r
    S.label(ws, f"A{r}", "Depreciation & amortisation", indent=1)
    for i, fy in enumerate(HIST):
        S.set_cell(ws, f"{cl(fy)}{r}", D1.cr(D1.IS_ACTUALS_LAKH["depreciation"][i]),
                   fmt=S.FMT_CR, input_cell=True)
    for fy in PROJ:
        S.set_cell(ws, f"{cl(fy)}{r}", f"='Balance Sheet'!{cl(fy)}{{DA}}", fmt=S.FMT_CR)
    S.label(ws, f"{gcl(NOTE_COL)}{r}", "Links to the Balance Sheet capex/D&A schedule.",
            italic=True, size=8, color="FF555555")
    r += 1

    ctrl = ["employee", "tech", "clearing", "admin", "da"]
    IS["ctrl_computed"] = r
    S.label(ws, f"A{r}", "Controllable opex — computed", bold=True, indent=0)
    for fy in YEARS:
        expr = "+".join(f"{cl(fy)}{IS[k]}" for k in ctrl)
        S.set_cell(ws, f"{cl(fy)}{r}", f"={expr}", fmt=S.FMT_CR, bold=True)
    S.label(ws, f"{gcl(NOTE_COL)}{r}", "Sum of the controllable lines above.", italic=True, size=8,
            color="FF555555")
    r += 1

    IS["floor"] = r
    S.label(ws, f"A{r}", "Ex-levy cost FLOOR (inflated)", indent=1, italic=True)
    S.set_cell(ws, f"{cl('FY26')}{r}", D2.COST_FLOOR_EXLEVY_FY26, fmt=S.FMT_CR, input_cell=True)
    for i, fy in enumerate(PROJ):
        S.set_cell(ws, f"{cl(fy)}{r}",
                   f"=$D${r}*(1+{act('floor_infl')})^{i+1}", fmt=S.FMT_CR)
    S.label(ws, f"{gcl(NOTE_COL)}{r}",
            "FY26 ex-levy run rate Rs1,187.73cr. 'That floor has never contracted in a down year.' "
            "[W7_bearcase]", italic=True, size=8, color="FFC00000")
    r += 1

    IS["ctrl_applied"] = r
    S.label(ws, f"A{r}", "Controllable opex — APPLIED (floor enforced)", bold=True, indent=0)
    for fy in HIST:
        S.set_cell(ws, f"{cl(fy)}{r}", f"={cl(fy)}{IS['ctrl_computed']}", fmt=S.FMT_CR, bold=True)
    for fy in PROJ:
        S.set_cell(ws, f"{cl(fy)}{r}",
                   f"=IF({act('cost_floor_on')}=1,MAX({cl(fy)}{IS['ctrl_computed']},{cl(fy)}{IS['floor']}),"
                   f"{cl(fy)}{IS['ctrl_computed']})", fmt=S.FMT_CR, bold=True)
    S.label(ws, f"{gcl(NOTE_COL)}{r}", "MAX(computed, floor) when the switch is ON.",
            italic=True, size=8, color="FF555555")
    r += 1

    IS["floor_uplift"] = r
    S.label(ws, f"A{r}", "  of which: floor uplift (binding when > 0)", indent=2, italic=True)
    for fy in YEARS:
        S.set_cell(ws, f"{cl(fy)}{r}",
                   f"={cl(fy)}{IS['ctrl_applied']}-{cl(fy)}{IS['ctrl_computed']}", fmt=S.FMT_CR)
    S.label(ws, f"{gcl(NOTE_COL)}{r}", "Shows how much cost the floor is holding in place.",
            italic=True, size=8, color="FF555555")
    r += 1

    # ------------------- REGULATORY -------------------
    S.section(ws, r, "REGULATORY COSTS (set by SEBI, not by BSE)", ncols); r += 1

    row("sebi_levy", "SEBI regulatory fee (on NOTIONAL turnover)", "sebi_regulatory_fee",
        lambda fy, i: f"='Drivers & History'!{cl(fy)}{DR['notional_adt']}*{act('levy_rate')}",
        "= NOTIONAL ADT x levy rate. 11.71% of BSE revenue vs NSE's 4.80% = 2.44x, "
        "because BSE bills on premium and pays on notional (958.6x the base).")

    IS["sgf"] = r
    S.label(ws, f"A{r}", "Core SGF contribution", indent=1)
    for i, fy in enumerate(HIST):
        S.set_cell(ws, f"{cl(fy)}{r}", D1.cr(D1.IS_ACTUALS_LAKH["core_sgf_contribution"][i]),
                   fmt=S.FMT_CR, input_cell=True)
    for fy in PROJ:
        prev = cl(YEARS[YEARS.index(fy) - 1])
        S.set_cell(ws, f"{cl(fy)}{r}",
                   f"=IF({act('sgf_mode')}=2,'Segment Revenue Build'!{cl(fy)}{SG['txn_total']}*"
                   f"{act('txn_audited_uplift')}*{act('sgf_policy_rate')},{prev}{r}*(1+{act('g_admin')}))",
                   fmt=S.FMT_CR)
    S.label(ws, f"{gcl(NOTE_COL)}{r}",
            "Mode 2 = announced policy 5% of transaction revenue (Rs189.75cr) vs Rs76.96cr charged "
            "= 2.47x. Permanent cash into a RESTRICTED fund. Counter-cyclical.",
            italic=True, size=8, color="FFC00000")
    r += 1

    row("other_reg", "Other regulatory & sundry expense", None,
        lambda fy, i: f"={act('other_reg_sundry')}",
        "Reconciliation line — bridges the component build to reported total expenses.",
        hist_vals=[None, None, 77.97])

    IS["total_exp"] = r
    S.label(ws, f"A{r}", "TOTAL EXPENSES", bold=True, indent=0)
    for i, fy in enumerate(HIST):
        S.set_cell(ws, f"{cl(fy)}{r}", D1.cr(D1.IS_ACTUALS_LAKH["total_expenses"][i]),
                   fmt=S.FMT_CR, input_cell=True, bold=True)
    for fy in PROJ:
        S.set_cell(ws, f"{cl(fy)}{r}",
                   f"={cl(fy)}{IS['ctrl_applied']}+{cl(fy)}{IS['sebi_levy']}+{cl(fy)}{IS['other_reg']}",
                   fmt=S.FMT_CR, bold=True)
    S.label(ws, f"{gcl(NOTE_COL)}{r}",
            "Projected = controllable applied + SEBI levy + other reg. Core SGF is deducted separately "
            "below, matching the reported PBT identity.", italic=True, size=8, color="FF555555")
    r += 1

    # ------------------- PROFIT -------------------
    S.section(ws, r, "PROFIT", ncols); r += 1

    IS["ebitda"] = r
    S.label(ws, f"A{r}", "EBITDA (incl investment income)", indent=1)
    for fy in YEARS:
        S.set_cell(ws, f"{cl(fy)}{r}",
                   f"={cl(fy)}{IS['total_income']}-{cl(fy)}{IS['total_exp']}+{cl(fy)}{IS['da']}",
                   fmt=S.FMT_CR)
    r += 1

    IS["float_income"] = r
    S.label(ws, f"A{r}", "Memo: float income inside revenue (members' money)", indent=2, italic=True)
    for fy in YEARS:
        S.set_cell(ws, f"{cl(fy)}{r}",
                   f"='Drivers & History'!{cl(fy)}{DR['float']}*{act('float_yield')}", fmt=S.FMT_CR)
    S.label(ws, f"{gcl(NOTE_COL)}{r}",
            "Rs171.42cr in FY26: interest earned on MEMBERS' clearing float at 4.99%, credited to "
            "shareholders as revenue. Not customer income.", italic=True, size=8, color="FFC00000")
    r += 1

    IS["ebit_op"] = r
    S.label(ws, f"A{r}", "OPERATING EBIT (excl investment & other income)", bold=True, indent=0)
    for fy in YEARS:
        S.set_cell(ws, f"{cl(fy)}{r}",
                   f"={cl(fy)}{IS['revenue']}-{cl(fy)}{IS['total_exp']}-{cl(fy)}{IS['sgf']}"
                   f"-IF({act('strip_float')}=1,{cl(fy)}{IS['float_income']},0)",
                   fmt=S.FMT_CR, bold=True)
    S.label(ws, f"{gcl(NOTE_COL)}{r}",
            "THE DCF BASE. Revenue less all operating cost incl SGF, less float income when the strip "
            "switch is on. Excludes treasury income so the corpus is not capitalised twice.",
            italic=True, size=8, color="FFC00000")
    r += 1

    row("finance", "Finance cost", "finance_cost", lambda fy, i: f"={act('finance_cost')}",
        "Effectively debt-free.")
    row("associate", "Share of associate profit (CDSL)", "associate_profit",
        lambda fy, i: f"=IF({act('cdsl_mode')}=1,{act('associate')},0)",
        "Mode 1 = keep the equity earnings here and value the stake at nil. Mode 2 = strip these "
        "earnings and add the stake's MARKET value in the DCF bridge instead. Never both.")
    row("exceptional", "Exceptional items", "exceptional_items",
        lambda fy, i: f"={act('exceptional')}", "Nil projected.")

    IS["pbt"] = r
    S.label(ws, f"A{r}", "Profit before tax", bold=True, indent=0)
    for i, fy in enumerate(HIST):
        S.set_cell(ws, f"{cl(fy)}{r}", D1.cr(D1.IS_ACTUALS_LAKH["pbt"][i]), fmt=S.FMT_CR,
                   input_cell=True, bold=True)
    for fy in PROJ:
        S.set_cell(ws, f"{cl(fy)}{r}",
                   f"={cl(fy)}{IS['ebit_op']}+IF({act('strip_float')}=1,{cl(fy)}{IS['float_income']},0)"
                   f"+{cl(fy)}{IS['inv_income']}+{cl(fy)}{IS['other_income']}"
                   f"-{cl(fy)}{IS['finance']}+{cl(fy)}{IS['associate']}+{cl(fy)}{IS['exceptional']}",
                   fmt=S.FMT_CR, bold=True)
    S.label(ws, f"{gcl(NOTE_COL)}{r}",
            "Float income is added back here because it IS in reported revenue and reported PBT — "
            "it is removed only from the FCFF base.", italic=True, size=8, color="FF555555")
    r += 1

    row("tax", "Tax expense", "total_tax",
        lambda fy, i: f"={cl(fy)}{IS['pbt']}*{act('tax_rate')}", "PBT x effective tax rate.")

    row("discont", "Profit from discontinued operations", None,
        lambda fy, i: f"={act('discontinued')}",
        "FY26 Rs11.95cr — explains the PBT-less-tax vs reported-PAT gap exactly. Nil projected.",
        hist_vals=[None, 5.26, 11.95])

    IS["pat"] = r
    S.label(ws, f"A{r}", "Profit after tax (total)", bold=True, indent=0)
    for fy in YEARS:
        S.set_cell(ws, f"{cl(fy)}{r}",
                   f"={cl(fy)}{IS['pbt']}-{cl(fy)}{IS['tax']}+{cl(fy)}{IS['discont']}",
                   fmt=S.FMT_CR, bold=True)
    r += 1

    IS["pat_attrib"] = r
    S.label(ws, f"A{r}", "PAT attributable to owners", bold=True, indent=0)
    for fy in YEARS:
        S.set_cell(ws, f"{cl(fy)}{r}", f"={cl(fy)}{IS['pat']}*{act('attrib_factor')}",
                   fmt=S.FMT_CR, bold=True)
    S.label(ws, f"{gcl(NOTE_COL)}{r}", "PAT total x attribution factor. This is the EPS numerator.",
            italic=True, size=8, color="FF555555")
    r += 1

    IS["eps"] = r
    S.label(ws, f"A{r}", "EPS (Rs) — on ISSUED shares", bold=True, indent=1)
    for fy in YEARS:
        S.set_cell(ws, f"{cl(fy)}{r}", f"={cl(fy)}{IS['pat_attrib']}/{act('shares_issued')}",
                   fmt=S.FMT_RS, bold=True)
    S.label(ws, f"{gcl(NOTE_COL)}{r}",
            "Audited basis: 2,496.98/41.1979 = Rs60.61 for FY26. Dividing by PAID-UP shares would "
            "print Rs61.22 — that is the wrong denominator for EPS.",
            italic=True, size=8, color="FFC00000")
    r += 1

    IS["mtm"] = r
    S.label(ws, f"A{r}", "Memo: MTM revaluation inside investment income", indent=2, italic=True)
    for fy in YEARS:
        S.set_cell(ws, f"{cl(fy)}{r}",
                   f"={cl(fy)}{IS['inv_income']}*(1-{act('inv_recurring_pct')})", fmt=S.FMT_CR)
    S.label(ws, f"{gcl(NOTE_COL)}{r}",
            "~30.57% of investment income is mark-to-market revaluation — 'not a yield and should not "
            "carry an operating multiple' [W5].", italic=True, size=8, color="FFC00000")
    r += 1

    IS["eps_adj"] = r
    S.label(ws, f"A{r}", "Quality-adjusted EPS (Rs) — MTM removed", bold=True, indent=1)
    for fy in YEARS:
        S.set_cell(ws, f"{cl(fy)}{r}",
                   f"=({cl(fy)}{IS['pat_attrib']}-{cl(fy)}{IS['mtm']}*(1-{act('tax_rate')}))"
                   f"/{act('shares_issued')}", fmt=S.FMT_RS, bold=True)
    S.label(ws, f"{gcl(NOTE_COL)}{r}", "The earnings an operating multiple should be struck on.",
            italic=True, size=8, color="FF555555")
    r += 1

    IS["dividend"] = r
    S.label(ws, f"A{r}", "Dividend declared", indent=1)
    for fy in YEARS:
        S.set_cell(ws, f"{cl(fy)}{r}", f"={cl(fy)}{IS['pat_attrib']}*{act('payout')}", fmt=S.FMT_CR)
    S.label(ws, f"{gcl(NOTE_COL)}{r}", "NO dividend policy exists in ten annual reports.",
            italic=True, size=8, color="FF555555")
    r += 1

    S.section(ws, r, "MARGINS", ncols); r += 1
    for key, lbl, num in (("m_ebitda", "EBITDA margin (% total income)", "ebitda"),
                          ("m_ebit", "Operating EBIT margin (% revenue)", "ebit_op"),
                          ("m_pat", "PAT margin (% total income)", "pat")):
        IS[key] = r
        S.label(ws, f"A{r}", lbl, indent=1, italic=True)
        den = IS["revenue"] if key == "m_ebit" else IS["total_income"]
        for fy in YEARS:
            S.set_cell(ws, f"{cl(fy)}{r}", f"={cl(fy)}{IS[num]}/{cl(fy)}{den}", fmt=S.FMT_PCT)
        r += 1

    ws.freeze_panes = "B6"
    return ws


# ===========================================================================
# 5. BALANCE SHEET  (own-account vs earmarked separated)
# ===========================================================================
def build_bs(wb):
    ws = wb.create_sheet("Balance Sheet")
    ws.sheet_properties.tabColor = "FFED7D31"
    ncols = NOTE_COL
    S.title_block(
        ws, "BSE Ltd — Consolidated Balance Sheet",
        "Own-account money is separated from EARMARKED clearing/settlement balances (members' money). "
        "Only own-account funds belong to shareholders and only they enter equity value.",
        "Units: Rs Crore. Balance check must be 0 in projected years.", ncols)
    _w(ws)
    r = 5
    _yrhdr(ws, r); r += 1

    S.section(ws, r, "CAPEX & DEPRECIATION SCHEDULE", ncols); r += 1

    BS["nb_open"] = r
    S.label(ws, f"A{r}", "Net block — opening", indent=1, italic=True)
    r += 1
    BS["capex"] = r
    S.label(ws, f"A{r}", "Capex", indent=1)
    for i, fy in enumerate(HIST):
        S.set_cell(ws, f"{cl(fy)}{r}", D1.cr(abs(D1.CF_ACTUALS_LAKH["capex_cash"][i])),
                   fmt=S.FMT_CR, input_cell=True)
    for fy in PROJ:
        S.set_cell(ws, f"{cl(fy)}{r}",
                   f"='Income Statement'!{cl(fy)}{IS['revenue']}*{act('capex_pct')}", fmt=S.FMT_CR)
    S.label(ws, f"{gcl(NOTE_COL)}{r}", "Projected = revenue x capex%. FY26 was elevated (data-centre).",
            italic=True, size=8, color="FF555555")
    r += 1
    BS["da"] = r
    S.label(ws, f"A{r}", "Depreciation & amortisation", indent=1)
    for i, fy in enumerate(HIST):
        S.set_cell(ws, f"{cl(fy)}{r}", D1.cr(D1.IS_ACTUALS_LAKH["depreciation"][i]),
                   fmt=S.FMT_CR, input_cell=True)
    for fy in PROJ:
        S.set_cell(ws, f"{cl(fy)}{r}", f"={cl(fy)}{BS['nb_open']}*{act('da_pct')}", fmt=S.FMT_CR)
    r += 1
    BS["nb_close"] = r
    S.label(ws, f"A{r}", "Net block — closing (PPE + CWIP)", bold=True, indent=1)
    for i, fy in enumerate(HIST):
        v = D1.BS_ACTUALS_LAKH["ppe"][i] + D1.BS_ACTUALS_LAKH["cwip"][i]
        S.set_cell(ws, f"{cl(fy)}{r}", D1.cr(v), fmt=S.FMT_CR, input_cell=True, bold=True)
    for fy in PROJ:
        S.set_cell(ws, f"{cl(fy)}{r}",
                   f"={cl(fy)}{BS['nb_open']}+{cl(fy)}{BS['capex']}-{cl(fy)}{BS['da']}",
                   fmt=S.FMT_CR, bold=True)
    r += 1
    # opening chain
    for i, fy in enumerate(PROJ):
        prev = cl(YEARS[YEARS.index(fy) - 1])
        S.set_cell(ws, f"{cl(fy)}{BS['nb_open']}", f"={prev}{BS['nb_close']}", fmt=S.FMT_CR)

    S.section(ws, r, "ASSETS", ncols); r += 1

    BS["own_treasury"] = r
    S.label(ws, f"A{r}", "Own investible corpus (shareholders')", bold=True, indent=1)
    for fy in YEARS:
        if fy == "FY24":
            S.set_cell(ws, f"{cl(fy)}{r}", D2.LIQUID_OWNED["FY24"], fmt=S.FMT_CR, input_cell=True)
        else:
            S.set_cell(ws, f"{cl(fy)}{r}", f"='Drivers & History'!{cl(fy)}{DR['own_corpus']}",
                       fmt=S.FMT_CR, bold=True)
    S.label(ws, f"{gcl(NOTE_COL)}{r}", "Link to Drivers. THIS is what enters equity value.",
            italic=True, size=8, color="FFC00000")
    r += 1

    BS["earmarked"] = r
    S.label(ws, f"A{r}", "Earmarked funds (members' — clearing/settlement)", indent=1)
    for fy in HIST:
        S.set_cell(ws, f"{cl(fy)}{r}", D2.LIQUID_EARMARKED[fy], fmt=S.FMT_CR, input_cell=True)
    for fy in PROJ:
        S.set_cell(ws, f"{cl(fy)}{r}",
                   f"={cl(YEARS[YEARS.index(fy)-1])}{r}*(1+{act('float_g')})", fmt=S.FMT_CR)
    S.label(ws, f"{gcl(NOTE_COL)}{r}", "NOT shareholders' money. Matched by an equal liability.",
            italic=True, size=8, color="FFC00000")
    r += 1

    BS["recv"] = r
    S.label(ws, f"A{r}", "Trade receivables", indent=1)
    for i, fy in enumerate(HIST):
        S.set_cell(ws, f"{cl(fy)}{r}", D1.cr(D1.BS_ACTUALS_LAKH["trade_receivables"][i]),
                   fmt=S.FMT_CR, input_cell=True)
    for fy in PROJ:
        S.set_cell(ws, f"{cl(fy)}{r}",
                   f"='Income Statement'!{cl(fy)}{IS['revenue']}*{act('recv_days')}/365", fmt=S.FMT_CR)
    r += 1

    BS["other_assets"] = r
    S.label(ws, f"A{r}", "Other assets (residual)", indent=1)
    for i, fy in enumerate(HIST):
        ta = D1.BS_ACTUALS_LAKH["total_assets"][i]
        resid = D1.cr(ta) - (D1.cr(D1.BS_ACTUALS_LAKH["ppe"][i] + D1.BS_ACTUALS_LAKH["cwip"][i])
                             + D2.LIQUID_OWNED[fy] + D2.LIQUID_EARMARKED[fy]
                             + D1.cr(D1.BS_ACTUALS_LAKH["trade_receivables"][i]))
        S.set_cell(ws, f"{cl(fy)}{r}", round(resid, 2), fmt=S.FMT_CR, input_cell=True)
    for fy in PROJ:
        S.set_cell(ws, f"{cl(fy)}{r}",
                   f"={cl(YEARS[YEARS.index(fy)-1])}{r}*(1+{act('own_corpus_g')})", fmt=S.FMT_CR)
    S.label(ws, f"{gcl(NOTE_COL)}{r}", "Asset-side residual so historical total ties to the reported figure.",
            italic=True, size=8, color="FF555555")
    r += 1

    BS["total_assets"] = r
    S.label(ws, f"A{r}", "TOTAL ASSETS", bold=True, indent=0)
    for fy in YEARS:
        expr = "+".join(f"{cl(fy)}{BS[k]}" for k in
                        ("nb_close", "own_treasury", "earmarked", "recv", "other_assets"))
        S.set_cell(ws, f"{cl(fy)}{r}", f"={expr}", fmt=S.FMT_CR, bold=True)
    r += 1

    S.section(ws, r, "EQUITY & LIABILITIES", ncols); r += 1

    BS["equity"] = r
    S.label(ws, f"A{r}", "Total equity", bold=True, indent=0)
    for i, fy in enumerate(HIST):
        S.set_cell(ws, f"{cl(fy)}{r}", D1.cr(D1.BS_ACTUALS_LAKH["total_equity"][i]),
                   fmt=S.FMT_CR, input_cell=True, bold=True)
    for fy in PROJ:
        prev = cl(YEARS[YEARS.index(fy) - 1])
        S.set_cell(ws, f"{cl(fy)}{r}",
                   f"={prev}{r}+'Income Statement'!{cl(fy)}{IS['pat_attrib']}"
                   f"-'Income Statement'!{cl(fy)}{IS['dividend']}", fmt=S.FMT_CR, bold=True)
    S.label(ws, f"{gcl(NOTE_COL)}{r}", "Prior + PAT attributable - dividend.", italic=True, size=8,
            color="FF555555")
    r += 1

    BS["float_liab"] = r
    S.label(ws, f"A{r}", "Earmarked liabilities (members' obligations)", indent=1)
    for fy in YEARS:
        S.set_cell(ws, f"{cl(fy)}{r}", f"={cl(fy)}{BS['earmarked']}", fmt=S.FMT_CR)
    S.label(ws, f"{gcl(NOTE_COL)}{r}", "Set equal to earmarked assets — a pass-through, not leverage.",
            italic=True, size=8, color="FF555555")
    r += 1

    BS["own_payables"] = r
    S.label(ws, f"A{r}", "Own payables & provisions", indent=1)
    for fy in PROJ:
        S.set_cell(ws, f"{cl(fy)}{r}",
                   f"='Income Statement'!{cl(fy)}{IS['ctrl_applied']}*{act('payables_pct')}",
                   fmt=S.FMT_CR)
    S.label(ws, f"{gcl(NOTE_COL)}{r}", "Driven off the COST base, not revenue (v1 error B16).",
            italic=True, size=8, color="FF555555")
    r += 1

    BS["other_liab"] = r
    S.label(ws, f"A{r}", "Other liabilities (residual / plug)", indent=1)
    for i, fy in enumerate(HIST):
        ta = D1.cr(D1.BS_ACTUALS_LAKH["total_assets"][i])
        eq = D1.cr(D1.BS_ACTUALS_LAKH["total_equity"][i])
        resid = ta - eq - D2.LIQUID_EARMARKED[fy]
        S.set_cell(ws, f"{cl(fy)}{r}", round(resid, 2), fmt=S.FMT_CR, input_cell=True)
    for fy in PROJ:
        S.set_cell(ws, f"{cl(fy)}{r}",
                   f"={cl(fy)}{BS['total_assets']}-{cl(fy)}{BS['equity']}-{cl(fy)}{BS['float_liab']}"
                   f"-{cl(fy)}{BS['own_payables']}", fmt=S.FMT_CR)
    S.label(ws, f"{gcl(NOTE_COL)}{r}", "Balancing item so the sheet balances identically.",
            italic=True, size=8, color="FF555555")
    r += 1
    # historical own payables blank -> set 0 so totals tie via other_liab
    for fy in HIST:
        S.set_cell(ws, f"{cl(fy)}{BS['own_payables']}", 0.0, fmt=S.FMT_CR, input_cell=True)

    BS["total_le"] = r
    S.label(ws, f"A{r}", "TOTAL EQUITY & LIABILITIES", bold=True, indent=0)
    for fy in YEARS:
        expr = "+".join(f"{cl(fy)}{BS[k]}" for k in
                        ("equity", "float_liab", "own_payables", "other_liab"))
        S.set_cell(ws, f"{cl(fy)}{r}", f"={expr}", fmt=S.FMT_CR, bold=True)
    r += 1

    BS["check"] = r
    S.label(ws, f"A{r}", "BALANCE CHECK (Assets - E&L)", bold=True, indent=0)
    for fy in YEARS:
        S.set_cell(ws, f"{cl(fy)}{r}",
                   f"={cl(fy)}{BS['total_assets']}-{cl(fy)}{BS['total_le']}", fmt=S.FMT_CR,
                   bold=True, force_color=S.BLACK)
    r += 1

    ws.freeze_panes = "B6"
    return ws


def patch_is_da(wb):
    ws = wb["Income Statement"]
    for fy in PROJ:
        ws[f"{cl(fy)}{IS['da']}"].value = f"='Balance Sheet'!{cl(fy)}{BS['da']}"


# ===========================================================================
# 6. CASH FLOW  — headline vs OWN-ACCOUNT (the report's central finding)
# ===========================================================================
def build_cf(wb):
    ws = wb.create_sheet("Cash Flow")
    ws.sheet_properties.tabColor = "FF7F7F7F"
    ncols = NOTE_COL
    S.title_block(
        ws, "BSE Ltd — Cash Flow: headline vs OWN-ACCOUNT",
        "The report's central cash finding: conversion is 1.272 headline and 0.712 own-account — the "
        "printed number is 78.7% too high, because reported CFO absorbs movements in members' clearing "
        "float that are not shareholders' cash. This tab separates the two.",
        "Units: Rs Crore.", ncols)
    _w(ws)
    r = 5
    _yrhdr(ws, r); r += 1

    S.section(ws, r, "OPERATING CASH FLOW", ncols); r += 1

    CF["pat"] = r
    S.label(ws, f"A{r}", "PAT attributable", indent=1)
    for fy in YEARS:
        S.set_cell(ws, f"{cl(fy)}{r}", f"='Income Statement'!{cl(fy)}{IS['pat_attrib']}", fmt=S.FMT_CR)
    r += 1
    CF["da"] = r
    S.label(ws, f"A{r}", "add: D&A", indent=1)
    for fy in YEARS:
        S.set_cell(ws, f"{cl(fy)}{r}", f"='Income Statement'!{cl(fy)}{IS['da']}", fmt=S.FMT_CR)
    r += 1
    CF["drecv"] = r
    S.label(ws, f"A{r}", "less: increase in receivables", indent=1)
    for i, fy in enumerate(YEARS):
        if i == 0:
            continue
        prev = cl(YEARS[i - 1])
        S.set_cell(ws, f"{cl(fy)}{r}",
                   f"=-('Balance Sheet'!{cl(fy)}{BS['recv']}-'Balance Sheet'!{prev}{BS['recv']})",
                   fmt=S.FMT_CR)
    r += 1
    CF["dfloat"] = r
    S.label(ws, f"A{r}", "add: increase in EARMARKED float (members' money)", indent=1)
    for i, fy in enumerate(YEARS):
        if i == 0:
            continue
        prev = cl(YEARS[i - 1])
        S.set_cell(ws, f"{cl(fy)}{r}",
                   f"=('Balance Sheet'!{cl(fy)}{BS['earmarked']}-'Balance Sheet'!{prev}{BS['earmarked']})",
                   fmt=S.FMT_CR)
    S.label(ws, f"{gcl(NOTE_COL)}{r}",
            "THIS is the line that inflates headline CFO. It is not shareholders' cash.",
            italic=True, size=8, color="FFC00000")
    r += 1

    CF["cfo_headline"] = r
    S.label(ws, f"A{r}", "CFO — HEADLINE (as reported basis)", bold=True, indent=0)
    for i, fy in enumerate(YEARS):
        if i == 0:
            continue
        S.set_cell(ws, f"{cl(fy)}{r}",
                   f"={cl(fy)}{CF['pat']}+{cl(fy)}{CF['da']}+{cl(fy)}{CF['drecv']}+{cl(fy)}{CF['dfloat']}",
                   fmt=S.FMT_CR, bold=True)
    r += 1

    CF["cfo_own"] = r
    S.label(ws, f"A{r}", "CFO — OWN ACCOUNT (float movement removed)", bold=True, indent=0)
    for i, fy in enumerate(YEARS):
        if i == 0:
            continue
        S.set_cell(ws, f"{cl(fy)}{r}",
                   f"={cl(fy)}{CF['cfo_headline']}-{cl(fy)}{CF['dfloat']}", fmt=S.FMT_CR, bold=True)
    S.label(ws, f"{gcl(NOTE_COL)}{r}", "The number an owner can spend.", italic=True, size=8,
            color="FFC00000")
    r += 1

    S.section(ws, r, "INVESTING & FREE CASH FLOW", ncols); r += 1
    CF["capex"] = r
    S.label(ws, f"A{r}", "less: capex", indent=1)
    for fy in YEARS:
        S.set_cell(ws, f"{cl(fy)}{r}", f"=-'Balance Sheet'!{cl(fy)}{BS['capex']}", fmt=S.FMT_CR)
    r += 1
    CF["fcf_own"] = r
    S.label(ws, f"A{r}", "OWN-ACCOUNT FREE CASH FLOW", bold=True, indent=0)
    for i, fy in enumerate(YEARS):
        if i == 0:
            continue
        S.set_cell(ws, f"{cl(fy)}{r}",
                   f"={cl(fy)}{CF['cfo_own']}+{cl(fy)}{CF['capex']}", fmt=S.FMT_CR, bold=True)
    r += 1
    CF["dividend"] = r
    S.label(ws, f"A{r}", "less: dividend", indent=1)
    for fy in YEARS:
        S.set_cell(ws, f"{cl(fy)}{r}", f"=-'Income Statement'!{cl(fy)}{IS['dividend']}", fmt=S.FMT_CR)
    r += 1

    S.section(ws, r, "CONVERSION TESTS", ncols); r += 1
    CF["conv_headline"] = r
    S.label(ws, f"A{r}", "Headline CFO / PAT", indent=1, italic=True)
    for i, fy in enumerate(YEARS):
        if i == 0:
            continue
        S.set_cell(ws, f"{cl(fy)}{r}", f"={cl(fy)}{CF['cfo_headline']}/{cl(fy)}{CF['pat']}", fmt=S.FMT_X)
    S.label(ws, f"{gcl(NOTE_COL)}{r}", "Ten-year cumulative reported basis = 1.272.",
            italic=True, size=8, color="FF555555")
    r += 1
    CF["conv_own"] = r
    S.label(ws, f"A{r}", "Own-account CFO / PAT", bold=True, indent=1)
    for i, fy in enumerate(YEARS):
        if i == 0:
            continue
        S.set_cell(ws, f"{cl(fy)}{r}", f"={cl(fy)}{CF['cfo_own']}/{cl(fy)}{CF['pat']}",
                   fmt=S.FMT_X, bold=True)
    S.label(ws, f"{gcl(NOTE_COL)}{r}", "Ten-year cumulative own-account basis = 0.712. "
            "1.272/0.712 = 1.787 -> the printed figure is 78.7% too high.",
            italic=True, size=8, color="FFC00000")
    r += 1

    ws.freeze_panes = "B6"
    return ws


# ===========================================================================
# 7. DCF  — operations only; treasury added ONCE
# ===========================================================================
def build_dcf(wb):
    ws = wb.create_sheet("DCF Valuation")
    ws.sheet_properties.tabColor = "FF7030A0"
    ncols = NOTE_COL
    S.title_block(
        ws, "BSE Ltd — DCF Valuation (FCFF on OPERATIONS ONLY)",
        "FCFF is built from OPERATING EBIT, which excludes investment income. The treasury corpus is "
        "then added ONCE in the bridge. v1 capitalised the treasury twice (income stream + principal) — "
        "that double-count is removed here.",
        "Units: Rs Crore; per-share in Rs. BSE earns fee income (not a bank) so FCFF DCF applies.", ncols)
    _w(ws)
    r = 5

    def one(key, lbl, formula, note, fmt=S.FMT_PCT, bold=False, indent=1):
        nonlocal r
        DC[key] = r
        S.label(ws, f"A{r}", lbl, indent=indent, bold=bold)
        S.set_cell(ws, f"E{r}", formula, fmt=fmt, bold=bold)
        if note:
            S.label(ws, f"{gcl(NOTE_COL)}{r}", note, italic=True, size=8, color="FF555555")
        r += 1

    S.section(ws, r, "WACC BUILD-UP (CAPM)", ncols); r += 1
    one("rf", "Risk-free rate", f"={act('rf')}", "From Assumptions (scenario-resolved).")
    one("erp", "Equity risk premium", f"={act('erp')}", "From Assumptions.")
    one("beta", "Beta (levered)", f"={act('beta')}", "Bear raises beta: one product, one expiry slot.",
        fmt=S.FMT_NUM)
    one("coe", "Cost of equity (CAPM)", f"=E{DC['rf']}+E{DC['beta']}*E{DC['erp']}", "Rf + beta x ERP.")
    one("kd", "Pre-tax cost of debt", f"={act('cost_debt')}", "From Assumptions.")
    one("tax", "Tax rate", f"={act('tax_rate')}", "From Assumptions.")
    one("kd_at", "After-tax cost of debt", f"=E{DC['kd']}*(1-E{DC['tax']})", "Kd x (1 - t).")
    one("we", "Weight — equity", f"={act('wt_equity')}", "From Assumptions.")
    one("wd", "Weight — debt", f"=1-E{DC['we']}", "1 - equity weight.")
    one("wacc", "WACC", f"=E{DC['we']}*E{DC['coe']}+E{DC['wd']}*E{DC['kd_at']}", "We x Ke + Wd x Kd(AT).",
        bold=True)
    one("g", "Terminal growth", f"={act('term_growth')}",
        "Base 4.0% — lowered from v1's 5% because FY26 is peak-cycle and ~9/10 of FY26 growth was "
        "share TRANSFER from NSE, which cannot compound forever.", bold=True)

    S.section(ws, r, "FREE CASH FLOW TO FIRM (operations only)", ncols); r += 1
    _yrhdr(ws, r); r += 1

    def line(key, lbl, proj, note, bold=False, indent=1, fmt=S.FMT_CR):
        nonlocal r
        DC[key] = r
        S.label(ws, f"A{r}", lbl, bold=bold, indent=indent)
        for i, fy in enumerate(PROJ):
            S.set_cell(ws, f"{cl(fy)}{r}", proj(fy, i), fmt=fmt, bold=bold)
        if note:
            S.label(ws, f"{gcl(NOTE_COL)}{r}", note, italic=True, size=8, color="FF555555")
        r += 1

    line("ebit", "Operating EBIT (excl investment income)",
         lambda fy, i: f"='Income Statement'!{cl(fy)}{IS['ebit_op']}",
         "Link to IS operating EBIT. Treasury income deliberately EXCLUDED.", bold=True)
    line("nopat", "NOPAT", lambda fy, i: f"={cl(fy)}{DC['ebit']}*(1-{act('tax_rate')})",
         "EBIT x (1 - tax).")
    line("da", "add: D&A", lambda fy, i: f"='Balance Sheet'!{cl(fy)}{BS['da']}", "Link to BS schedule.")
    line("capex", "less: capex", lambda fy, i: f"=-'Balance Sheet'!{cl(fy)}{BS['capex']}",
         "Link to BS schedule.")
    line("dwc", "less: increase in operating WC",
         lambda fy, i: (f"=-('Balance Sheet'!{cl(fy)}{BS['recv']}-'Balance Sheet'!"
                        f"{cl(YEARS[YEARS.index(fy)-1])}{BS['recv']})"),
         "Receivables only. Earmarked float is members' money and is NOT working capital.")
    line("fcff", "FCFF",
         lambda fy, i: (f"={cl(fy)}{DC['nopat']}+{cl(fy)}{DC['da']}+{cl(fy)}{DC['capex']}"
                        f"+{cl(fy)}{DC['dwc']}"),
         "NOPAT + D&A - capex - dWC.", bold=True)
    line("period", "Discount period", lambda fy, i: f"={i+1}", "1, 2, 3.", fmt=S.FMT_NUM)
    line("df", "Discount factor",
         lambda fy, i: f"=1/(1+$E${DC['wacc']})^{cl(fy)}{DC['period']}", "1/(1+WACC)^n.", fmt=S.FMT_NUM)
    line("pv", "PV of FCFF", lambda fy, i: f"={cl(fy)}{DC['fcff']}*{cl(fy)}{DC['df']}",
         "FCFF x DF.", bold=True)

    S.section(ws, r, "TERMINAL VALUE AND THE BRIDGE TO EQUITY", ncols); r += 1
    last = cl(PROJ[-1])
    one("tv_gordon", "Terminal value — Gordon (single stage)",
        f"={last}{DC['fcff']}*(1+$E${DC['g']})/($E${DC['wacc']}-$E${DC['g']})",
        "FCFF(final) x (1+g) / (WACC - g).", fmt=S.FMT_CR)
    one("tv_hmodel", "Terminal value — H-model (two stage, fading)",
        f"={last}{DC['fcff']}*(1+$E${DC['g']})/($E${DC['wacc']}-$E${DC['g']})"
        f"+{last}{DC['fcff']}*({act('fade_years')}/2)*({act('g_fade')}-$E${DC['g']})"
        f"/($E${DC['wacc']}-$E${DC['g']})",
        "Gordon base + fade premium: FCFF x H x (g_fade - g) / (WACC - g), where H = fade_years/2. "
        "Credits the transition from high growth to maturity instead of assuming it ends instantly.",
        fmt=S.FMT_CR)
    one("tv", "Terminal value — APPLIED",
        f"=IF({act('tv_method')}=1,E{DC['tv_gordon']},E{DC['tv_hmodel']})",
        "Selected by the method switch on Assumptions.", fmt=S.FMT_CR, bold=True)
    one("pv_tv", "PV of terminal value", f"=E{DC['tv']}*{last}{DC['df']}", "TV x final DF.", fmt=S.FMT_CR)
    one("sum_pv", "Sum PV of explicit FCFF",
        f"=SUM({cl(PROJ[0])}{DC['pv']}:{cl(PROJ[-1])}{DC['pv']})", "Explicit period.", fmt=S.FMT_CR)
    one("ev_ops", "Enterprise value — OPERATIONS", f"=E{DC['sum_pv']}+E{DC['pv_tv']}",
        "PV(FCFF) + PV(TV). Operations only.", fmt=S.FMT_CR, bold=True)
    one("treasury", "add: own investible corpus (once)",
        f"='Balance Sheet'!{cl('FY26')}{BS['own_treasury']}",
        "FY26 own corpus Rs6,101.90cr — SHAREHOLDERS' money, added ONCE. "
        "Earmarked float is excluded because it belongs to members.", fmt=S.FMT_CR)
    one("assoc", "add: CDSL stake market value", f"=IF({act('cdsl_mode')}=2,{act('assoc_value')},0)",
        "Rs3,509.32cr [AR FY26, Note 8]. Included ONLY in mode 2, where the associate EARNINGS are "
        "simultaneously stripped from the P&L. Market value OR earnings, never both [W5 constraint 4].",
        fmt=S.FMT_CR)
    one("debt", "less: debt", "=0", "BSE carries effectively no debt.", fmt=S.FMT_CR)
    one("eq_val", "EQUITY VALUE",
        f"=E{DC['ev_ops']}+E{DC['treasury']}+E{DC['assoc']}-E{DC['debt']}",
        "Operations + treasury (once) + associate - debt.", fmt=S.FMT_CR, bold=True)
    one("shares", "Shares outstanding (cr)", f"={act('shares')}", "From Assumptions.", fmt=S.FMT_NUM)
    one("vps", "IMPLIED VALUE PER SHARE (Rs)", f"=E{DC['eq_val']}/E{DC['shares']}",
        "Equity value / shares. Both in crore units, so they cancel to Rs/share.",
        fmt=S.FMT_RS, bold=True)
    one("price", "Market price (Rs)", f"={act('price')}", "NSE bhavcopy 4-Sep-2026.", fmt=S.FMT_RS)
    one("upside", "Implied upside / (downside)", f"=E{DC['vps']}/E{DC['price']}-1",
        "Value / price - 1.", fmt=S.FMT_PCT, bold=True)
    one("implied_pe", "Implied P/E on FY26 EPS",
        f"=E{DC['vps']}/'Income Statement'!{cl('FY26')}{IS['eps']}",
        "What multiple the DCF value represents on FY26 earnings.", fmt=S.FMT_X)

    # ---------------- REVERSE DCF ----------------
    S.section(ws, r, "REVERSE DCF — what does the PRICE require? (the doctrine's question)", ncols)
    r += 1
    S.label(ws, f"A{r}", "This block does not value the company. It inverts the DCF and asks what "
            "the market price must be assuming, so the assumption can be tested against evidence.",
            italic=True, size=9, color="FFC00000")
    r += 1
    one("mkt_cap", "Market capitalisation at current price",
        f"={act('price')}*{act('shares')}",
        "Price x paid-up shares. The company's own basis for market cap.", fmt=S.FMT_CR, bold=True)
    one("implied_ev", "Implied EV of OPERATIONS at market price",
        f"=E{DC['mkt_cap']}-E{DC['treasury']}-E{DC['assoc']}+E{DC['debt']}",
        "Market cap less the treasury the shareholders already own. This is what the price pays "
        "for the operating business alone.", fmt=S.FMT_CR, bold=True)
    one("implied_tv", "Implied terminal value (undiscounted)",
        f"=(E{DC['implied_ev']}-E{DC['sum_pv']})/{last}{DC['df']}",
        "Backs out the terminal value the price requires, after the explicit-period PVs.",
        fmt=S.FMT_CR)
    one("implied_g", "IMPLIED TERMINAL GROWTH at current price",
        f"=(E{DC['implied_tv']}*$E${DC['wacc']}-{last}{DC['fcff']})/(E{DC['implied_tv']}+{last}{DC['fcff']})",
        "Closed form: g = (TV x WACC - FCFF_final) / (TV + FCFF_final). "
        "Compare against WACC — a g at or above WACC is not a growth rate, it is a contradiction.",
        fmt=S.FMT_PCT, bold=True)
    one("g_gap", "  implied g less WACC (must be < 0 to be coherent)",
        f"=E{DC['implied_g']}-$E${DC['wacc']}",
        "If this is >= 0 the Gordon formula has no finite solution: the price cannot be justified by "
        "any perpetual growth rate at this WACC.", fmt=S.FMT_PCT, bold=True)
    one("implied_fcff_mult", "Implied EV / final-year FCFF (x)",
        f"=E{DC['implied_ev']}/{last}{DC['fcff']}",
        "How many years of terminal-year free cash flow the price represents.", fmt=S.FMT_X)
    one("mkt_pe", "Market P/E on FY26 EPS (x)",
        f"={act('price')}/'Income Statement'!{cl('FY26')}{IS['eps']}",
        "Should print 55.7x — the report's figure. FY26 is a PEAK-CYCLE base: Q1FY27 revenue grew "
        "+0.16% sequentially with 110.1% of the profit increase non-operating.", fmt=S.FMT_X, bold=True)
    one("dcf_vs_mkt", "DCF value as % of market price",
        f"=E{DC['vps']}/E{DC['price']}",
        "Read with the reverse-DCF above: the gap is the size of the growth bet embedded in the price, "
        "not a price objective.", fmt=S.FMT_PCT, bold=True)

    ws.freeze_panes = "B6"
    return ws


# ===========================================================================
# 8. COMPS
# ===========================================================================
CM = {}


def build_comps(wb):
    ws = wb.create_sheet("Comps")
    ws.sheet_properties.tabColor = "FF00B0F0"
    ncols = 8
    S.title_block(
        ws, "BSE Ltd — Trading Comparables",
        "HONESTY NOTE: no verified peer market data exists in this research corpus. Peer price / EBITDA "
        "/ PAT / book cells are UNVERIFIED user inputs — refresh them before relying on any output. "
        "The one peer fact that IS evidenced (NSE's SEBI-fee burden) is shown separately as a real anchor.",
        "Units: Rs Crore; price in Rs; multiples in x.", ncols)
    ws.column_dimensions["A"].width = 34
    for c in "BCDEFGH":
        ws.column_dimensions[c].width = 14
    r = 5

    S.label(ws, f"A{r}", "*** PEER MARKET DATA BELOW IS UNVERIFIED — USER MUST REFRESH ***",
            bold=True, color="FFC00000")
    r += 2

    hdr = ["Company", "Price (Rs)", "Shares (cr)", "Mkt cap", "Net debt", "EV", "PAT", "EBITDA"]
    for i, h in enumerate(hdr):
        c = ws.cell(row=r, column=1 + i)
        c.value = h
        c.font = S.Font(name="Calibri", size=10, bold=True, color=S.WHITE)
        c.fill = S.PatternFill("solid", fgColor=S.HDR_BG)
        c.alignment = S.Alignment(horizontal="center")
    r += 1

    CM["peers"] = {}
    seeds = {"MCX": (6500.0, 5.10, -900.0, 560.0, 700.0),
             "CDSL": (1500.0, 20.90, -1200.0, 620.0, 800.0)}
    start = r
    for name, (p, sh, nd, pat, eb) in seeds.items():
        S.label(ws, f"A{r}", name, bold=True)
        S.set_cell(ws, f"B{r}", p, fmt=S.FMT_RS, input_cell=True)
        S.set_cell(ws, f"C{r}", sh, fmt=S.FMT_NUM, input_cell=True)
        S.set_cell(ws, f"D{r}", f"=B{r}*C{r}", fmt=S.FMT_CR)
        S.set_cell(ws, f"E{r}", nd, fmt=S.FMT_CR, input_cell=True)
        S.set_cell(ws, f"F{r}", f"=D{r}+E{r}", fmt=S.FMT_CR)
        S.set_cell(ws, f"G{r}", pat, fmt=S.FMT_CR, input_cell=True)
        S.set_cell(ws, f"H{r}", eb, fmt=S.FMT_CR, input_cell=True)
        CM["peers"][name] = r
        r += 1
    end = r - 1

    # BSE row built from the model (green links)
    S.label(ws, f"A{r}", "BSE (from model)", bold=True)
    S.set_cell(ws, f"B{r}", f"={act('price')}", fmt=S.FMT_RS)
    S.set_cell(ws, f"C{r}", f"={act('shares')}", fmt=S.FMT_NUM)
    S.set_cell(ws, f"D{r}", f"=B{r}*C{r}", fmt=S.FMT_CR)
    S.set_cell(ws, f"E{r}", f"=-'Balance Sheet'!{cl('FY26')}{BS['own_treasury']}", fmt=S.FMT_CR)
    S.set_cell(ws, f"F{r}", f"=D{r}+E{r}", fmt=S.FMT_CR)
    S.set_cell(ws, f"G{r}", f"='Income Statement'!{cl('FY26')}{IS['pat_attrib']}", fmt=S.FMT_CR)
    S.set_cell(ws, f"H{r}", f"='Income Statement'!{cl('FY26')}{IS['ebitda']}", fmt=S.FMT_CR)
    CM["bse"] = r
    r += 2

    S.section(ws, r, "MULTIPLES", ncols); r += 1
    for i, h in enumerate(["Company", "EV/EBITDA", "P/E", "P/B"]):
        c = ws.cell(row=r, column=1 + i)
        c.value = h
        c.font = S.Font(name="Calibri", size=10, bold=True, color=S.WHITE)
        c.fill = S.PatternFill("solid", fgColor=S.HDR_BG)
        c.alignment = S.Alignment(horizontal="center")
    r += 1
    mstart = r
    for name in seeds:
        rr = CM["peers"][name]
        S.label(ws, f"A{r}", name, bold=True)
        S.set_cell(ws, f"B{r}", f"=F{rr}/H{rr}", fmt=S.FMT_X)
        S.set_cell(ws, f"C{r}", f"=D{rr}/G{rr}", fmt=S.FMT_X)
        S.set_cell(ws, f"D{r}", "=NA()", fmt=S.FMT_X)
        r += 1
    mend = r - 1
    S.label(ws, f"A{r}", "Peer average", bold=True, italic=True)
    S.set_cell(ws, f"B{r}", f"=AVERAGE(B{mstart}:B{mend})", fmt=S.FMT_X, bold=True)
    S.set_cell(ws, f"C{r}", f"=AVERAGE(C{mstart}:C{mend})", fmt=S.FMT_X, bold=True)
    CM["avg"] = r
    r += 1
    bse = CM["bse"]
    S.label(ws, f"A{r}", "BSE (model)", bold=True)
    S.set_cell(ws, f"B{r}", f"=F{bse}/H{bse}", fmt=S.FMT_X, bold=True)
    S.set_cell(ws, f"C{r}", f"=D{bse}/G{bse}", fmt=S.FMT_X, bold=True)
    S.set_cell(ws, f"D{r}", f"=D{bse}/'Balance Sheet'!{cl('FY26')}{BS['equity']}", fmt=S.FMT_X, bold=True)
    CM["bse_mult"] = r
    S.label(ws, f"{gcl(6)}{r}", "BSE P/E should print ~55.7x — the report's figure at Rs3,409.80.",
            italic=True, size=8, color="FFC00000")
    r += 2

    S.section(ws, r, "IMPLIED VALUE FOR BSE FROM PEER MULTIPLES", ncols); r += 1
    S.label(ws, f"A{r}", "Implied price/share — EV/EBITDA (Rs)", bold=True, indent=1)
    S.set_cell(ws, f"B{r}",
               f"=(B{CM['avg']}*H{bse}-E{bse})/C{bse}", fmt=S.FMT_RS, bold=True)
    r += 1
    S.label(ws, f"A{r}", "Implied price/share — P/E (Rs)", bold=True, indent=1)
    S.set_cell(ws, f"B{r}", f"=(C{CM['avg']}*G{bse})/C{bse}", fmt=S.FMT_RS, bold=True)
    r += 2

    S.section(ws, r, "THE ONE EVIDENCED PEER FACT — the SEBI-fee burden", ncols); r += 1
    for lbl, v, note in (
        ("NSE FY26 revenue from operations (Rs cr)", D2.NSE_FY26["revenue_ops"],
         "[NSE AR FY26, Consolidated P&L, PDF p140/pr318]"),
        ("NSE FY26 SEBI regulatory fee (Rs cr)", D2.NSE_FY26["sebi_fee"], "same source"),
    ):
        S.label(ws, f"A{r}", lbl, indent=1)
        S.set_cell(ws, f"B{r}", v, fmt=S.FMT_CR, input_cell=True)
        S.label(ws, f"D{r}", note, italic=True, size=8, color="FF555555")
        r += 1
    CM["nse_pct"] = r
    S.label(ws, f"A{r}", "NSE SEBI fee as % of revenue", indent=1, italic=True)
    S.set_cell(ws, f"B{r}", f"=B{r-1}/B{r-2}", fmt=S.FMT_PCT)
    r += 1
    S.label(ws, f"A{r}", "BSE SEBI fee as % of revenue", indent=1, italic=True)
    S.set_cell(ws, f"B{r}",
               f"='Income Statement'!{cl('FY26')}{IS['sebi_levy']}/'Income Statement'!{cl('FY26')}{IS['revenue']}",
               fmt=S.FMT_PCT)
    CM["bse_pct"] = r
    r += 1
    S.label(ws, f"A{r}", "BSE / NSE burden ratio", bold=True, indent=1)
    S.set_cell(ws, f"B{r}", f"=B{CM['bse_pct']}/B{CM['nse_pct']}", fmt=S.FMT_X, bold=True)
    S.label(ws, f"D{r}", "Research figure: 11.71% / 4.80% = 2.44x. BSE bills on premium, pays on notional.",
            italic=True, size=8, color="FFC00000")
    r += 1

    ws.freeze_panes = "B6"
    return ws


# ===========================================================================
# 9. SENSITIVITY  (adds the WEDGE axis — the key variable)
# ===========================================================================
def build_sens(wb):
    ws = wb.create_sheet("Sensitivity")
    ws.sheet_properties.tabColor = "FFFF0000"
    ncols = 9
    S.title_block(
        ws, "BSE Ltd — Sensitivity",
        "Grid 1: WACC x terminal growth. Grid 2: premium-ADT growth. "
        "Grid 3: THE WEDGE — the premium/notional ratio, which the research identifies as the single "
        "most important exogenous variable and which management says is unforecastable.",
        "Value per share in Rs. Every grid cell is a live formula off the DCF FCFF stream.", ncols)
    ws.column_dimensions["A"].width = 24
    for c in "BCDEFGHI":
        ws.column_dimensions[c].width = 13
    r = 5

    f = [f"'DCF Valuation'!${cl(fy)}${DC['fcff']}" for fy in PROJ]
    trez = f"'DCF Valuation'!$E${DC['treasury']}"
    shr = f"'DCF Valuation'!$E${DC['shares']}"
    wacc0 = f"'DCF Valuation'!$E${DC['wacc']}"
    g0 = f"'DCF Valuation'!$E${DC['g']}"

    def vps(w, g, k="1"):
        ev = (f"({k}*{f[0]}/(1+{w})^1+{k}*{f[1]}/(1+{w})^2+{k}*{f[2]}/(1+{w})^3"
              f"+({k}*{f[2]}*(1+{g})/({w}-{g}))/(1+{w})^3)")
        return f"=({ev}+{trez})/{shr}"

    # ---- GRID 1 ----
    S.section(ws, r, "GRID 1 — value/share: WACC (across) x terminal growth (down)", ncols); r += 1
    hdr_row = r
    S.label(ws, f"A{r}", "g \\ WACC", bold=True)
    wcols = []
    for i, off in enumerate((-0.02, -0.01, 0.0, 0.01, 0.02)):
        c = gcl(2 + i)
        S.set_cell(ws, f"{c}{r}", f"={wacc0}{'+' if off >= 0 else ''}{off}", fmt=S.FMT_PCT, bold=True)
        wcols.append(c)
    r += 1
    for goff in (-0.02, -0.01, 0.0, 0.01, 0.02):
        S.set_cell(ws, f"A{r}", f"={g0}{'+' if goff >= 0 else ''}{goff}", fmt=S.FMT_PCT, bold=True)
        for c in wcols:
            S.set_cell(ws, f"{c}{r}", vps(f"{c}${hdr_row}", f"$A{r}"), fmt=S.FMT_RS)
        r += 1
    r += 1

    # ---- GRID 2: premium ADT growth ----
    S.section(ws, r, "GRID 2 — value/share vs PREMIUM ADT growth (FY27E lever)", ncols); r += 1
    S.label(ws, f"A{r}", "Premium ADT growth", bold=True)
    S.label(ws, f"B{r}", "Value/share (Rs)", bold=True)
    S.label(ws, f"D{r}", "Scales the derivatives share of revenue through to FCFF.",
            italic=True, size=8, color="FF555555")
    r += 1
    dshare = (f"('Segment Revenue Build'!${cl('FY27E')}${SG['deriv']}"
              f"/'Segment Revenue Build'!${cl('FY27E')}${SG['rev_standalone']})")
    base_g1 = act("padt_g1")
    for off in (-0.30, -0.20, -0.10, 0.0, 0.10, 0.20, 0.30):
        S.set_cell(ws, f"A{r}", f"={base_g1}{'+' if off >= 0 else ''}{off}", fmt=S.FMT_PCT, bold=True)
        k = f"(1+{dshare}*((A{r}-{base_g1})/(1+{base_g1})))"
        S.set_cell(ws, f"B{r}", vps(wacc0, g0, k), fmt=S.FMT_RS)
        r += 1
    r += 1

    # ---- GRID 3: THE WEDGE ----
    S.section(ws, r, "GRID 3 — value/share vs THE WEDGE (premium/notional ratio)", ncols); r += 1
    S.label(ws, f"A{r}", "Premium/notional", bold=True)
    S.label(ws, f"B{r}", "Value/share (Rs)", bold=True)
    S.label(ws, f"C{r}", "Levy impact (Rs cr)", bold=True)
    S.label(ws, f"E{r}", "The wedge sets the SEBI levy: notional = premium / wedge. "
            "A LOWER wedge means a BIGGER notional base and a bigger levy for the same revenue.",
            italic=True, size=8, color="FFC00000")
    r += 1
    lev_base = f"'Income Statement'!${cl('FY27E')}${IS['sebi_levy']}"
    padt = f"'Drivers & History'!${cl('FY27E')}${DR['premium_adt']}"
    wedge_act = act("wedge")
    for w in (D2.WEDGE["Q2FY26"], 0.000950, D2.WEDGE["FY26"], 0.000115 * 10, D2.WEDGE["Q1FY27"]):
        S.set_cell(ws, f"A{r}", w, fmt="0.00000%", input_cell=True)
        # levy at this wedge minus levy at active wedge
        dlevy = f"=({padt}/A{r}*{act('levy_rate')})-{lev_base}"
        S.set_cell(ws, f"C{r}", dlevy, fmt=S.FMT_CR)
        # value: FCFF reduced by the after-tax levy delta each year
        k = f"(1-(C{r}*(1-{act('tax_rate')}))/{f[0]})"
        S.set_cell(ws, f"B{r}", vps(wacc0, g0, k), fmt=S.FMT_RS)
        r += 1
    S.label(ws, f"A{r}", "Q2FY26 low = 0.091491% is ALREADY PRINTED inside this cycle.",
            italic=True, size=8, color="FFC00000")
    r += 1

    ws.freeze_panes = "B6"
    return ws


# ===========================================================================
# 10. CHECKS
# ===========================================================================
def build_checks(wb):
    ws = wb.create_sheet("Checks")
    ws.sheet_properties.tabColor = "FF375623"
    ncols = 6
    S.title_block(
        ws, "BSE Ltd — Model Integrity Checks",
        "Every row is a live formula compared against a disclosed actual. A model that cannot reproduce "
        "the audited past should not be used to forecast the future.",
        "Target values are typed (blue) from the research; Model values are formulas.", ncols)
    ws.column_dimensions["A"].width = 52
    for c in "BCD":
        ws.column_dimensions[c].width = 16
    ws.column_dimensions["E"].width = 12
    ws.column_dimensions["F"].width = 46
    r = 5

    for i, h in enumerate(["Check", "Model", "Target", "Diff", "Status", "Note"]):
        c = ws.cell(row=r, column=1 + i)
        c.value = h
        c.font = S.Font(name="Calibri", size=10, bold=True, color=S.WHITE)
        c.fill = S.PatternFill("solid", fgColor=S.HDR_BG)
        c.alignment = S.Alignment(horizontal="center")
    r += 1

    def chk(lbl, model_f, target, tol, note, fmt=S.FMT_CR):
        nonlocal r
        S.label(ws, f"A{r}", lbl, indent=1)
        S.set_cell(ws, f"B{r}", model_f, fmt=fmt)
        S.set_cell(ws, f"C{r}", target, fmt=fmt, input_cell=True)
        S.set_cell(ws, f"D{r}", f"=B{r}-C{r}", fmt=fmt)
        S.set_cell(ws, f"E{r}", f'=IF(ABS(D{r})<={tol},"PASS","REVIEW")', fmt="@", bold=True)
        S.label(ws, f"F{r}", note, italic=True, size=8, color="FF555555")
        r += 1

    S.section(ws, r, "A. DOES THE MODEL REPRODUCE THE AUDITED PAST?", ncols); r += 1
    chk("FY26 revenue from operations", f"='Income Statement'!{cl('FY26')}{IS['revenue']}",
        D2.TARGETS["revenue_ops_FY26"], 2.0, "Audited consolidated [AR FY26 Note 22].")
    chk("FY26 derivatives txn charges",
        f"='Segment Revenue Build'!{cl('FY26')}{SG['deriv']}", D2.TARGETS["deriv_txn_FY26"], 1.0,
        "MD&A split (unaudited). 64.84% of consolidated revenue.")
    chk("FY26 transaction charges total",
        f"='Segment Revenue Build'!{cl('FY26')}{SG['txn_total']}", D2.TARGETS["txn_total_FY26"], 1.0,
        "Sub-components tie exactly in the MD&A.")
    chk("FY26 SEBI regulatory fee", f"='Income Statement'!{cl('FY26')}{IS['sebi_levy']}",
        D2.TARGETS["sebi_fee_FY26"], 2.0, "Computed on NOTIONAL turnover.")
    chk("FY26 investment income", f"='Income Statement'!{cl('FY26')}{IS['inv_income']}",
        290.30, 1.0, "= avg own corpus 4,885.84 x 5.942%.")
    chk("FY26 PAT attributable", f"='Income Statement'!{cl('FY26')}{IS['pat_attrib']}",
        D2.TARGETS["pat_attributable_FY26"], 5.0, "Audited [AR FY26 Consolidated P&L].")
    chk("FY26 EPS (Rs) — issued-share basis", f"='Income Statement'!{cl('FY26')}{IS['eps']}",
        60.61, 0.15, "2,496.98 / 41.1979 issued shares = Rs60.61 [records/capital_structure.md].",
        fmt=S.FMT_RS)
    chk("FY26 P/E at Rs3,409.80 (x)",
        f"={act('price')}/'Income Statement'!{cl('FY26')}{IS['eps']}",
        56.26, 0.20, "3,409.80 / 60.61 = 56.26x — the report's 'reported earnings' multiple.",
        fmt=S.FMT_X)
    chk("CDSL double-count guard (assoc profit x stake value)",
        f"='Income Statement'!{cl('FY27E')}{IS['associate']}*'DCF Valuation'!E{DC['assoc']}",
        0.0, 0.01, "MUST be zero: if both the earnings and the market value are non-zero the stake "
        "is counted twice [W5 constraint 4].")

    S.section(ws, r, "B. INTERNAL CONSISTENCY", ncols); r += 1
    for fy in PROJ:
        chk(f"Balance sheet balances — {fy}", f"='Balance Sheet'!{cl(fy)}{BS['check']}", 0.0, 0.5,
            "Assets - Equity & Liabilities must be zero.")
    chk("Cost floor is binding in FY27E (>0 means yes)",
        f"='Income Statement'!{cl('FY27E')}{IS['floor_uplift']}", 0.0, 100000.0,
        "Informational: shows how much cost the ex-levy floor is holding in place.")

    S.section(ws, r, "C. REALITY TESTS AGAINST Q1FY27 (the latest actual)", ncols); r += 1
    chk("FY27E revenue vs Q1FY27 annualised",
        f"='Income Statement'!{cl('FY27E')}{IS['revenue']}",
        round(D2.Q1FY27["revenue_ops"] * 4, 2), 100000.0,
        "Q1FY27 revenue x4 = Rs6,264cr. If FY27E is far above this, the forecast needs defending: "
        "Q1FY27 revenue grew only +0.16% SEQUENTIALLY.")
    chk("FY27E total income vs Q1FY27 annualised",
        f"='Income Statement'!{cl('FY27E')}{IS['total_income']}",
        round(D2.Q1FY27["total_income"] * 4, 2), 100000.0,
        "110.1% of the Q1FY27 profit increase was NON-OPERATING.")

    S.section(ws, r, "D. IS THE GROWTH ASSUMPTION EVEN POSSIBLE?", ncols); r += 1
    # implied market share in the terminal year
    pool_fy26 = round(D2.POOL_PREMIUM_ADT_FY26, 1)
    S.label(ws, f"A{r}", "Two-exchange premium pool FY26 (Rs cr)", indent=1)
    S.set_cell(ws, f"B{r}", pool_fy26, fmt=S.FMT_CR0, input_cell=True)
    S.label(ws, f"F{r}", "DERIVED: BSE premium ADT 19,523 / share 21.58%.", italic=True, size=8,
            color="FF555555")
    CK["pool26"] = r
    r += 1
    S.label(ws, f"A{r}", "Implied pool FY29E (grown at pool growth)", indent=1)
    S.set_cell(ws, f"B{r}", f"=B{CK['pool26']}*(1+{act('pool_g')})^3", fmt=S.FMT_CR0)
    CK["pool29"] = r
    r += 1
    S.label(ws, f"A{r}", "BSE premium ADT FY29E (model)", indent=1)
    S.set_cell(ws, f"B{r}", f"='Drivers & History'!{cl('FY29E')}{DR['premium_adt']}", fmt=S.FMT_CR0)
    CK["padt29"] = r
    r += 1
    S.label(ws, f"A{r}", "IMPLIED BSE MARKET SHARE IN FY29E", bold=True, indent=0)
    S.set_cell(ws, f"B{r}", f"=B{CK['padt29']}/B{CK['pool29']}", fmt=S.FMT_PCT, bold=True)
    S.set_cell(ws, f"E{r}", f'=IF(B{r}>0.5,"IMPOSSIBLE?",IF(B{r}>0.35,"AGGRESSIVE","PLAUSIBLE"))',
               fmt="@", bold=True)
    S.label(ws, f"F{r}", "FY26 actual share 21.58% (from 14.44%). Share cannot exceed 100% — "
            "if this prints above ~35% the growth assumption is a share-transfer bet, not a market bet.",
            italic=True, size=8, color="FFC00000")
    r += 2

    S.section(ws, r, "E. SIZED RISKS THE MODEL NOW CARRIES", ncols); r += 1
    S.label(ws, f"A{r}", "Wedge reversion to Q2FY26 low — revenue at risk (Rs cr)", indent=1)
    S.set_cell(ws, f"B{r}",
               f"='Segment Revenue Build'!{cl('FY26')}{SG['deriv']}*(1-{D2.WEDGE['Q2FY26']}/{D2.WEDGE['FY26']})",
               fmt=S.FMT_CR)
    S.set_cell(ws, f"C{r}", D2.TARGETS["wedge_reversion_cost"], fmt=S.FMT_CR, input_cell=True)
    S.label(ws, f"F{r}", "Research: Rs385.35cr. A level ALREADY PRINTED inside this cycle.",
            italic=True, size=8, color="FFC00000")
    r += 1
    S.label(ws, f"A{r}", "Core SGF gap: policy vs charged (Rs cr)", indent=1)
    S.set_cell(ws, f"B{r}",
               f"='Segment Revenue Build'!{cl('FY26')}{SG['txn_total']}*{act('txn_audited_uplift')}"
               f"*{act('sgf_policy_rate')}-'Income Statement'!{cl('FY26')}{IS['sgf']}", fmt=S.FMT_CR)
    S.set_cell(ws, f"C{r}", D2.SGF_GAP_FY26, fmt=S.FMT_CR, input_cell=True)
    S.label(ws, f"F{r}", "Rs112.79cr a year of permanent cash into a restricted fund, "
            "sourced only from a concall.", italic=True, size=8, color="FFC00000")
    r += 1

    ws.freeze_panes = "B6"
    return ws


# ===========================================================================
# ASSEMBLY
# ===========================================================================
def main():
    wb = openpyxl.Workbook()
    wb.remove(wb.active)

    build_assumptions(wb)
    build_drivers(wb)
    build_segment(wb)
    build_is(wb)
    build_bs(wb)
    patch_is_da(wb)
    build_cf(wb)
    build_dcf(wb)
    build_comps(wb)
    build_sens(wb)
    build_checks(wb)

    order = ["Assumptions", "Drivers & History", "Income Statement", "Balance Sheet",
             "Cash Flow", "Segment Revenue Build", "DCF Valuation", "Comps", "Sensitivity", "Checks"]
    wb._sheets.sort(key=lambda w: order.index(w.title))

    def named(nm, sheet, cell):
        wb.defined_names.add(DefinedName(nm, attr_text=f"'{sheet}'!{cell}"))
    named("V2_ValuePerShare", "DCF Valuation", f"$E${DC['vps']}")
    named("V2_WACC", "DCF Valuation", f"$E${DC['wacc']}")
    named("V2_Scenario", "Assumptions", SCEN_CELL)

    wb.save(OUT)
    with open("row_maps_v2.json", "w") as fh:
        json.dump({"AR": AR, "DR": DR, "SG": SG, "IS": IS, "BS": BS,
                   "CF": CF, "DC": DC, "CK": CK}, fh, indent=2, default=str)
    print(f"Saved {OUT}")
    print("Wrote row_maps_v2.json")


if __name__ == "__main__":
    main()
