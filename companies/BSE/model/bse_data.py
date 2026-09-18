"""
BSE Ltd — historical actuals for the financial model.

ALL VALUES IN Rs CRORE (source data is in Rs lakh; 1 crore = 100 lakh, so crore = lakh / 100).
Source: companies/BSE research records (trend_10y.csv, balance_cash_10y.csv,
revenue_disaggregation.md, quarterly_series.csv). CONSOLIDATED basis for IS/BS/CF.
Segment split is STANDALONE MD&A (the only level at which BSE discloses product mix), flagged as such.

These are the ONLY typed-in (blue) numbers permitted in the model besides the Assumptions tab.
"""

L2C = 100.0  # lakh -> crore divisor


def cr(lakh):
    """Convert a lakh figure to crore, rounded to 2 dp. None passes through."""
    return None if lakh is None else round(lakh / L2C, 2)


# ---------------------------------------------------------------------------
# Historical years used as actuals in the model
# ---------------------------------------------------------------------------
HIST_YEARS = ["FY24", "FY25", "FY26"]
PROJ_YEARS = ["FY27E", "FY28E", "FY29E"]
ALL_YEARS = HIST_YEARS + PROJ_YEARS

# ---------------------------------------------------------------------------
# INCOME STATEMENT actuals (CONSOLIDATED), Rs lakh from trend_10y.csv
# key: (FY24, FY25, FY26)
# ---------------------------------------------------------------------------
IS_ACTUALS_LAKH = {
    "revenue_from_operations": (139003, 295734, 483395),
    "investment_income":       (20247, 25470, 29030),
    "other_income":            (2540, 2427, 2385),
    "total_income":            (161790, 323631, 514810),
    "employee_benefits":       (20471, 23662, 29781),
    "technology_expense":      (13744, 16429, 20313),
    "sebi_regulatory_fee":     (16977, 33141, 56616),
    "regulatory_contribution": (None, 41046, 64969),   # SEBI + core SGF grouping shift; FY24 not split
    "clearing_settlement":     (13314, 34805, 28035),
    "depreciation":            (9544, 11298, 15896),
    "other_admin_expenses":    (33884, 20154, 24732),
    "les_expense":             (643, 666, 556),
    "finance_cost":            (1505, 3, 16),
    "total_expenses":          (110082, 148063, 183742),
    "core_sgf_contribution":   (9170, 9000, 7696),
    "associate_profit":        (7182, 8259, 6542),
    "exceptional_items":       (40662, 0, 0),
    "pbt":                     (99552, 174827, 329914),
    "total_tax":               (22386, 43121, 82384),
    "pat_total":               (77166, 132232, 248725),
    "pat_attributable":        (77839, 132589, 249698),
}

# ---------------------------------------------------------------------------
# BALANCE SHEET actuals (CONSOLIDATED), Rs lakh from balance_cash_10y.csv
# ---------------------------------------------------------------------------
BS_ACTUALS_LAKH = {
    "ppe":                       (19841, 22217, 56259),
    "cwip":                      (1113, 4073, 3255),
    "total_noncurrent_assets":   (348032, 299899, 522900),
    "trade_receivables":         (21087, 30967, 55316),
    "total_current_assets":      (596991, 734266, 821714),
    "total_assets":              (945023, 1034165, 1344614),
    "total_equity":              (345466, 457570, 679550),
    "total_noncurrent_liab":     (1363, 1872, 3332),
    "total_current_liabilities": (502698, 461463, 537049),
    "core_sgf_fund_balance":     (95496, 113260, 124683),
}

# ---------------------------------------------------------------------------
# CASH FLOW actuals (CONSOLIDATED), Rs lakh
# ---------------------------------------------------------------------------
CF_ACTUALS_LAKH = {
    "cfo":           (284203, 41015, 310368),
    "cfi":           (-107145, -76723, -273967),
    "cff":           (-14905, -20599, -30370),
    "capex_cash":    (-13132, -15323, -51516),
    "dividend_paid": (-16490, -20599, -31585),
    "tax_paid":      (-17391, -32797, -65541),
    "cash_close":    (207452, 152416, 164642),
}

# ---------------------------------------------------------------------------
# SEGMENT actuals — STANDALONE MD&A (revenue_disaggregation.md), Rs lakh
# Only FY25 & FY26 disclosed at this granularity. FY24 shown where available.
# Transaction charges sub-components tie: 313437 + 28490 + 25021 = 366948 (FY26).
# ---------------------------------------------------------------------------
SEG_ACTUALS_LAKH = {
    # (FY24, FY25, FY26) ; None where not disclosed at this split
    "txn_equity_derivatives": (None, 141554, 313437),
    "txn_equity_cash":        (None, 30356, 25021),
    "txn_starmf":             (None, 23077, 28490),
    "txn_charges_total":      (None, 194987, 366948),
    "listing_fees":           (None, 35328, 38861),
    "book_building_fees":     (None, 9536, 10412),
    "other_operating_income": (None, 16806, 28110),
    "colocation_income":      (None, 7262, 16899),
    "rev_ops_standalone":     (None, 260643, 446951),
    # currency derivatives and SLB are not separately disclosed in the MD&A split;
    # they sit inside transaction charges / are immaterial. Modelled as driver lines
    # in the build with 0 historical where not disclosed (NOT-DISCLOSED tag).
}

# Consolidated revenue from operations (for the segment tab to reconcile to IS)
REV_OPS_CONSOL_LAKH = (139003, 295734, 483395)

# ---------------------------------------------------------------------------
# Market volume context (for ADTO-driven build) — from research/industry notes.
# BSE equity derivatives premium ADTO and cash ADTO are the volume drivers.
# These are ASSUMPTION-tab seeds (editable), not audited financials, so they live
# in the assumptions with SECONDARY tags. Provided here as starting values.
# Units: Rs crore ADTO (premium turnover for derivatives).
# ---------------------------------------------------------------------------
MARKET_CONTEXT = {
    # Implied realisation seeds derived from FY26 standalone: yield bps computed in-model.
    "note": "ADTO seeds are editable assumptions; yields are computed from actuals in the build.",
}

# ---------------------------------------------------------------------------
# Peer comps seeds (Comps tab blue inputs). Market data as of report basis
# 4-Sep-2026 where used in the BSE report; peer figures are placeholders the user
# can refresh. FY26 fundamentals in Rs crore where known from peer ARs.
# ---------------------------------------------------------------------------
PEER_SEEDS = {
    # name: dict of blue inputs (price, shares_cr, net_debt_cr, ebitda_cr, pat_cr, bookvalue_cr)
    "MCX":  {"price": 6500.0, "shares_cr": 5.10, "net_debt_cr": -900.0, "ebitda_cr": 700.0, "pat_cr": 560.0, "book_cr": 1600.0},
    "CDSL": {"price": 1500.0, "shares_cr": 20.90, "net_debt_cr": -1200.0, "ebitda_cr": 800.0, "pat_cr": 620.0, "book_cr": 2000.0},
}

# BSE share count and market data (blue inputs on Assumptions/Comps)
BSE_MARKET = {
    "price_basis": 3409.80,            # NSE bhavcopy close 4-Sep-2026 [NSE Bhavcopy 2026-09-04]
    "shares_paid_up_cr": 40.7884,      # paid-up 40,78,84,077 [AR FY26 Note 14]
    "shares_issued_cr": 41.1979,       # issued 41,19,79,077 [AR FY26 Note 14]
    "date": "2026-09-04",
}


if __name__ == "__main__":
    # sanity: FY26 transaction-charge tie-out
    fy26 = (SEG_ACTUALS_LAKH["txn_equity_derivatives"][2]
            + SEG_ACTUALS_LAKH["txn_equity_cash"][2]
            + SEG_ACTUALS_LAKH["txn_starmf"][2])
    assert fy26 == SEG_ACTUALS_LAKH["txn_charges_total"][2], fy26
    print("data module OK; FY26 txn tie-out =", fy26, "lakh =", cr(fy26), "cr")
