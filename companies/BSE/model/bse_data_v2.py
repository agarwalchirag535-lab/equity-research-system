"""
BSE Ltd — REAL driver data for model v2, extracted from the research evidence base.
All monetary values converted to Rs CRORE (source lakh / 100). ADT values already Rs crore.

Every figure below carries its source. Nothing is invented; where a series does not exist
it is marked None and the model treats it as NOT-DISCLOSED.
"""

# ============================================================================
# DRIVER 1 — index-options PREMIUM average daily turnover (Rs crore)
# Revenue is earned on premium. [AR FY26, MD&A, PDF p58/pr47]
# ============================================================================
PREMIUM_ADT = {"FY25": 8978.0, "FY26": 19523.0, "Q1FY27": 29615.4}

# ============================================================================
# DRIVER 2 — options NOTIONAL average daily turnover (Rs crore)
# The SEBI levy is assessed on notional. [AR FY26, MD&A, PDF p58/pr47]
# ============================================================================
NOTIONAL_ADT = {"FY25": 11066674.0, "FY26": 18715375.0, "Q1FY27": 23700000.0}

# Premium / notional WEDGE (the margin variable). DERIVED from the two series above.
WEDGE = {
    "FY25": 0.00081126,      # 0.081126%
    "FY26": 0.00104315,      # 0.104315%
    "Q1FY26": 0.00115144,
    "Q2FY26": 0.00091491,    # the low already printed inside this cycle -> bear case
    "Q3FY26": 0.00092662,
    "Q4FY26": 0.00118044,
    "Q1FY27": 0.00124959,    # the high -> bull case
}

# ============================================================================
# DRIVER 3 — contract count. Only the CHANGE is disclosed, not a clean annual count.
# FY26 contracts traded fell 6.53%. Average daily lots 153mn (Q2FY25) -> 100mn (Q2FY26).
# Modelled as an INDEX with FY26 = 1.000. [Q1FY27 IP, PDF p14/slide 13]
# ============================================================================
CONTRACTS_INDEX = {"FY25": 1.0699, "FY26": 1.0000}   # FY25 = 1/(1-0.0653)

# ============================================================================
# Equity CASH average daily turnover (Rs crore) — 11-year series
# [REPORT.md line 194; AR FY26 MD&A PDF p58/pr47]
# ============================================================================
CASH_ADT_SERIES = {
    "FY16": 2996.0, "FY17": 4025.0, "FY18": 4402.0, "FY19": 3127.0, "FY20": 2676.0,
    "FY21": 4197.0, "FY22": 5396.0, "FY23": 4132.0, "FY24": 6622.0, "FY25": 7766.0,
    "FY26": 7950.0,
}

# ============================================================================
# REALISATION FACTORS — Rs crore of charges per Rs crore of ADT.
# Defined so no fabricated trading-day count is needed; ties exactly to actuals.
#   deriv:  3134.37 / 19523 = 0.160547   (FY25: 1415.54 / 8978 = 0.157668) -> +1.83%
#   cash :   250.21 /  7950 = 0.031473   (FY25:  303.56 / 7766 = 0.039088) -> -19.48%
# ============================================================================
REALISATION_DERIV = {"FY25": 0.157668, "FY26": 0.160547}
REALISATION_CASH = {"FY25": 0.039088, "FY26": 0.031473}

# SEBI levy rate per Rs crore of NOTIONAL ADT (Rs crore of levy per Rs crore notional)
#   FY26: 566.16 / 18715375 = 0.00003025 ; FY25: 331.41 / 11066674 = 0.00002995 (+1.0%)
LEVY_RATE_PER_NOTIONAL = {"FY25": 0.00002995, "FY26": 0.00003025}

# ============================================================================
# TREASURY — own investible corpus and yields [W8_valuation §1.4]
# ============================================================================
OWN_CORPUS_CLOSING = {"FY25": 3669.77, "FY26": 6101.90}      # Rs cr
OWN_CORPUS_AVERAGE = {"FY25": 3395.97, "FY26": 4885.84}      # Rs cr
OWN_CORPUS_YIELD = {"FY25": 0.07500, "FY26": 0.05942}        # -156bp
FLOAT_YIELD = {"FY25": 0.0632, "FY26": 0.0499}               # treasury on clearing float, -21%

# Earmarked (NOT owner cash) — clearing & settlement current financial liabilities, Rs cr
EARMARKED_FLOAT = {"FY24": 3581.65, "FY25": 3311.72, "FY26": 3554.23}
LIQUID_EARMARKED = {"FY24": 4892.49, "FY25": 4681.09, "FY26": 5006.57}
LIQUID_OWNED = {"FY24": 1415.28, "FY25": 1674.86, "FY26": 3085.96}

# ============================================================================
# COST FLOOR — ex-levy run rate. Total expenses less the regulatory levy.
#   FY26: 1837.42 - 649.69 = 1187.73 Rs cr  [W7_bearcase]
# "that floor has never contracted in a down year"
# ============================================================================
COST_FLOOR_EXLEVY_FY26 = 1187.73

# Core SGF: announced policy = 5% of transaction revenue, vs charged
SGF_POLICY_RATE = 0.05
SGF_CHARGED_FY26 = 76.96          # Rs cr
SGF_POLICY_FY26 = 189.75          # 3794.99 * 5%
SGF_GAP_FY26 = 112.79             # permanent cash into a restricted fund
SGF_Q1FY27_CHARGE = 25.91         # annualises at 103.64 (+34.67%)

# ============================================================================
# MARKET SHARE — two-exchange premium income pool [W8_valuation §1.1]
# ============================================================================
BSE_PREMIUM_SHARE = {"FY25": 0.1444, "FY26": 0.2158}   # +714bp
POOL_GROWTH_FY26 = 0.0646
POOL_PREMIUM_ADT_FY26 = 19523.0 / 0.2158               # ~90,468 Rs cr (DERIVED)

# ============================================================================
# Q1FY27 ACTUALS (the reality check) — Rs cr, from records/quarterly_series.csv
# Revenue grew +0.16% sequentially; 110.1% of the profit increase was non-operating.
# ============================================================================
Q1FY27 = {
    "revenue_ops": 1566.02, "investment_income": 135.18, "other_income": 5.52,
    "total_income": 1706.72, "employee": 87.05, "technology": 60.82,
    "clearing": 90.28, "regulatory": 192.78, "other_expenses": 63.16,
    "depreciation": 42.60, "total_expenses": 536.69, "pbt": 1163.66,
}

# ============================================================================
# VERIFICATION TARGETS — what the model must reproduce
# ============================================================================
TARGETS = {
    "revenue_ops_FY26": 4833.95,
    "eps_consolidated_FY26": 61.22,        # P/E 3409.80 / 61.22 = 55.7x
    "eps_standalone_FY26": 56.27,
    "pe_consolidated": 55.7,
    "pat_attributable_FY26": 2496.98,
    "deriv_txn_FY26": 3134.37,
    "cash_txn_FY26": 250.21,
    "txn_total_FY26": 3669.48,
    "sebi_fee_FY26": 566.16,
    "clearing_FY26": 280.35,
    "wedge_reversion_cost": 385.35,        # Rs cr of derivatives revenue
    "cost_floor_exlevy": 1187.73,
}

# Peer anchor that IS evidenced: NSE FY26 [NSE AR FY26, Consolidated P&L, PDF p140/pr318]
NSE_FY26 = {"revenue_ops": 16601.31, "sebi_fee": 796.35, "sebi_pct": 0.0480}
BSE_SEBI_PCT_FY26 = 0.1171     # 2.44x NSE

# Market data
PRICE = 3409.80          # NSE bhavcopy close 4-Sep-2026
SHARES_PAID_UP_CR = 40.7884
SHARES_ISSUED_CR = 41.1979


if __name__ == "__main__":
    # tie-out proofs
    assert abs(PREMIUM_ADT["FY26"] * REALISATION_DERIV["FY26"] - 3134.37) < 0.5
    assert abs(CASH_ADT_SERIES["FY26"] * REALISATION_CASH["FY26"] - 250.21) < 0.5
    assert abs(NOTIONAL_ADT["FY26"] * LEVY_RATE_PER_NOTIONAL["FY26"] - 566.16) < 1.0
    assert abs(PREMIUM_ADT["FY26"] / WEDGE["FY26"] - NOTIONAL_ADT["FY26"]) < 1000
    print("v2 driver data OK — all tie-outs proved:")
    print("  deriv txn  =", round(PREMIUM_ADT["FY26"] * REALISATION_DERIV["FY26"], 2), "(actual 3134.37)")
    print("  cash txn   =", round(CASH_ADT_SERIES["FY26"] * REALISATION_CASH["FY26"], 2), "(actual 250.21)")
    print("  SEBI levy  =", round(NOTIONAL_ADT["FY26"] * LEVY_RATE_PER_NOTIONAL["FY26"], 2), "(actual 566.16)")
    print("  notional   =", round(PREMIUM_ADT["FY26"] / WEDGE["FY26"], 0), "(actual 18715375)")
    print("  wedge rev. =", round(3134.37 * (1 - WEDGE["Q2FY26"] / WEDGE["FY26"]), 2), "(research 385.35)")
