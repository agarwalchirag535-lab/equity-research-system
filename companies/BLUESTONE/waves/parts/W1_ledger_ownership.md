# W1_ledger_ownership — evidence ledger: ownership, IPO-proceeds record, governance events

**Company.** BlueStone Jewellery and Lifestyle Limited · NSE `BLUESTONE` · BSE `544484` · ISIN
`INE304W01038` · CIN `L72900KA2011PLC059678` · listed 19-Aug-2025.
**Agent slice (doctrine §7, "one read, many uses").** Transcription with tags. No S1–S6, no chains, no
conclusions. Where two sources disagree both are recorded and the row is marked **DISAGREE**. No ratio is
computed here unless the company or the filing printed it; the four arithmetic checks that *are* shown are
tie-outs of the filing against itself, marked `TIE-OUT`, with the arithmetic inline.
**As-of.** 09-Sep-2026. Compiled from the sources named in `data/source_register.md` Tier 2 and Tier 3 only.

---

## 0. Reading rules for this file — three of them are load-bearing

### 0a. UNIT NOTE — the XBRL percentage scale is NOT constant across the five shareholding filings

| Filing | Percentage fields recorded as | Example: promoter & promoter group share |
|---|---|---|
| `SHP_18AUG2025_new.xml` | **0–100 scale** | literal `16.36` |
| `SHP_30SEP2025_new.xml` | **decimal fraction** | literal `0.1636` |
| `SHP_31DEC2025_new.xml` | **decimal fraction** | literal `0.1636` |
| `SHP_31MAR2026_new.xml` | **decimal fraction** | literal `0.1627` |
| `SHP_30JUN2026_new.xml` | **decimal fraction** | literal `0.1625` |

> **Every percentage printed in §1 of this file is the *percent reading*** — i.e. the XBRL literal for
> 18-Aug-2025 as printed, and the XBRL literal **× 100** for the four later filings. An agent that reads
> the five XML files without applying this rule will be out by a factor of one hundred on four of the five
> quarters. The raw literals for the control rows are reproduced in §1.9 so the conversion can be checked.

### 0b. Share counts are in **numbers of equity shares of face value Re. 1 each** — never in lakhs, crore or millions.
Monetary amounts in §3 (IPO proceeds) are in **Rs. crore**, because that is the unit printed on the face
of every Monitoring Agency Report §4 table. Monetary amounts in §4 (PIT) are in **Rupees** as filed.
Monetary amounts in §6 are in **Rupees** as filed. Each table restates its unit in its own head.

### 0c. Evidence tags used in this file

`[SHP <date>]` — the shareholding-pattern XBRL for that date, e.g. `[SHP 31Mar2026]` ·
`[MAR Q4FY26, p7]` — Monitoring Agency Report, PDF page ·
`[SoD Q3FY26, p2]` — Statement of Deviation, PDF page ·
`[NSE ann <dd-Mmm-yyyy>, <file stem>, p<n>]` — exchange filing, PDF page as marked by
`===== PDF PAGE n =====` in `data/quarterly_text/<stem>.txt` ·
`[PIT NSE pid <n>]` — a row of `data/filings/insider.json` addressed by its `pid` ·
`[NSE IPO detail, <block>]` — `data/ipo/nse_ipo_detail.json` ·
`[IMAGE: data/scanned_pages/<file>.png]` — read visually from the rasterised page, no text layer exists ·
`[SECONDARY: BSE section inventory 09-Sep-2026]` — GAP-003 deal data, secondary, unreconciled.

---

## 1. Shareholding pattern — all five quarters, quarters as columns

Source: the five XBRL instances in `data/filings/`, read directly. Filing dates recorded in the XBRL
`DateOfReport` field are 18-Aug-2025 (with `DateOfListing` 19-Aug-2025 and the instant context dated
**19-Aug-2025**), 30-Sep-2025, 31-Dec-2025, 31-Mar-2026, 30-Jun-2026.

> **Column-header caution.** The first filing is labelled `SHP_18AUG2025` but its instant context — the
> date every number in it is stated *as at* — is **19-Aug-2025**, the listing date. `DateOfReport` is
> 18-Aug-2025. Both dates are on the face of the file `[SHP 18Aug2025, MainI]`. Columns below are headed
> by the filename date; the balance date is 19-Aug-2025.

### 1.1 Control totals — Table I

**Unit: number of equity shares of face value Re. 1 each; percentages are percent readings per §0a.**

| Line (XBRL element, verbatim) | 18-Aug-2025 | 30-Sep-2025 | 31-Dec-2025 | 31-Mar-2026 | 30-Jun-2026 |
|---|---|---|---|---|---|
| **Total shares outstanding** `NumberOfFullyPaidUpEquityShares` (ShareholdingPatternMember) | 151,320,372 | 151,320,372 | 151,320,372 | 152,231,365 | 152,401,781 |
| `NumberOfShares` (same member) | 151,320,372 | 151,320,372 | 151,320,372 | 152,231,365 | 152,401,781 |
| `NumberOfVotingRights` | 151,320,372 | 151,320,372 | 151,320,372 | 152,231,365 | 152,401,781 |
| `NumberOfSharesUnderlyingOutstandingConvertibleSecuritiesWarrantsAndESOP` | 7,567,272 | 7,567,272 | 7,567,272 | 6,433,865 | 6,522,593 |
| `NumberOfSharesOnFullyDilutedBasisIncludingWarrantsESOPAndConvertibleSecurities` | 158,887,644 | 158,887,644 | 158,887,644 | 158,665,230 | 158,924,374 |
| **Total shareholders** `NumberOfShareholders` | 104,021 | 46,553 | 42,074 | 39,697 | 40,653 |
| **Shares in dematerialised form** `NumberOfEquitySharesHeldInDematerializedForm` | 148,239,717 | 148,239,717 | 148,239,717 | 149,150,710 | 149,321,126 |
| Shares NOT in demat (total − demat) `TIE-OUT` | 151,320,372 − 148,239,717 = 3,080,655 | 3,080,655 | 3,080,655 | 152,231,365 − 149,150,710 = 3,080,655 | 152,401,781 − 149,321,126 = 3,080,655 |
| **Total locked-in** `NumberOfTheLockedInShares` | 103,190,124 | 96,485,171 | 89,354,077 | 33,898,807 | 33,898,807 |
| Locked-in as % of total `LockedInSharesAsAPercentageOfTotalNumberOfShares` | 68.19% | 63.76% | 59.05% | 22.27% | 22.24% |
| `NumberOfSharesUnderSubCategoryOne` | 1,232,210 | 1,213,885 | 1,218,914 | 955,400 | 891,673 |
| `NumberOfSharesUnderSubCategoryTwo` | 0 | 0 | 0 | 0 | 0 |
| `NumberOfSharesUnderSubCategoryThree` | 0 | 0 | 0 | 0 | 0 |
| `NumberOfSharesEncumberedUnderNonDisposalUndertaking` (total-company context) | *element absent* | 15,250,000 | 15,250,000 | 15,250,000 | 15,250,000 |

`TIE-OUT` — the **un-dematerialised block is exactly 3,080,655 shares at every one of the five dates**,
unchanged even as the total moves. Every ESOP allotment landed in demat. All five arithmetic lines above
were recomputed independently `[SHP 18Aug2025 / 30Sep2025 / 31Dec2025 / 31Mar2026 / 30Jun2026]`.

**What `SubCategoryOne/Two/Three` mean is NOT DISCLOSED in the XBRL** — the instance carries the values
with no label element -> the SEBI-format shareholding-pattern **PDF/HTML** filed with BSE and NSE for the
same five dates would carry the printed sub-category headings; it is not in this corpus.

### 1.2 Promoter and promoter group — Table II

**Unit: number of equity shares; percent readings per §0a.**

| Line | 18-Aug-2025 | 30-Sep-2025 | 31-Dec-2025 | 31-Mar-2026 | 30-Jun-2026 |
|---|---|---|---|---|---|
| `ShareholdingOfPromoterAndPromoterGroupMember` — shareholders | 2 | 2 | 2 | 2 | 2 |
| — shares | 24,761,977 | 24,761,977 | 24,761,977 | 24,761,977 | 24,761,977 |
| — % of total shares | 16.36% | 16.36% | 16.36% | 16.27% | 16.25% |
| — % of total voting rights | 16.36% | 16.36% | 16.36% | 16.27% | 16.25% |
| — % assuming full conversion of convertibles/warrants/ESOP | 15.58% | 15.58% | 15.58% | 15.61% | 15.58% |
| — locked-in shares | 24,761,977 | 24,761,977 | 24,761,977 | **15,409,076** | **15,409,076** |
| — locked-in as % of the category's own shares | 100.00% | 100% | 100% | 62.23% | 62.23% |
| — shares in demat | 24,761,977 | 24,761,977 | 24,761,977 | 24,761,977 | 24,761,977 |
| — `NumberOfSharesUnderlyingOutstandingConvertibleSecuritiesWarrantsAndESOP` | *absent* (flag `…ForPromoterAndPromoterGroup = false`) | *absent* | *absent* | *absent* | *absent* |
| Of which `IndianMember` — shares | 24,761,977 | 24,761,977 | 24,761,977 | 24,761,977 | 24,761,977 |
| Of which `ForeignMember` — shares | 0 | 0 | 0 | 0 | not reported |

The promoter block **did not move a single share in thirteen months**; the percentage falls only because
the denominator rose on ESOP allotment (§2). Promoter lock-in falls by 24,761,977 − 15,409,076 = **9,352,901
shares** between the 31-Dec-2025 and 31-Mar-2026 filings `TIE-OUT` `[SHP 31Dec2025]` `[SHP 31Mar2026]`.

**A2 — Non-Resident Individuals / Foreign Individuals (promoter group).** `Archana Tomar`, 0 shares, at
18-Aug-2025, 30-Sep-2025, 31-Dec-2025 and 31-Mar-2026; **the whole A2 member is absent from the
30-Jun-2026 instance** `[SHP 30Jun2026]`.

### 1.3 Public shareholding — the category ladder, Table III

**Unit: number of equity shares; percent readings per §0a. `—` = the XBRL member is not present in that
filing; `0` = the member is present and reports zero.**

| Category (XBRL member, verbatim) | Field | 18-Aug-2025 | 30-Sep-2025 | 31-Dec-2025 | 31-Mar-2026 | 30-Jun-2026 |
|---|---|---|---|---|---|---|
| **PublicShareholdingMember** | shareholders | 104,019 | 46,551 | 42,072 | 39,695 | 40,651 |
| ↑ | shares | 126,558,395 | 126,558,395 | 126,558,395 | 127,469,388 | 127,639,804 |
| ↑ | % of total | 83.64% | 83.64% | 83.64% | 83.73% | 83.75% |
| ↑ | ESOP/convertibles underlying | 7,567,272 | 7,567,272 | 7,567,272 | 6,433,865 | 6,522,593 |
| ↑ | % on fully diluted | 84.42% | 84.42% | 84.42% | 84.39% | 84.42% |
| ↑ | locked-in | 78,428,147 | 71,723,194 | 64,592,100 | 18,489,731 | 18,489,731 |
| ↑ | locked-in % of category | 61.97% | 56.67% | 51.04% | 14.51% | 14.49% |
| ↑ | demat | 123,477,740 | 123,477,740 | 123,477,740 | 124,388,733 | 124,559,149 |
| **InstitutionsDomesticMember** | shareholders | 45 | 44 | 40 | 42 | 43 |
| ↑ | shares | 47,257,292 | 49,160,311 | 49,193,181 | 51,620,680 | 49,504,996 |
| ↑ | % of total | 31.23% | 32.49% | 32.51% | 33.91% | 32.48% |
| ↑ | locked-in | 17,296,407 | 13,753,116 | 9,783,685 | 9,047,160 | 9,047,160 |
| — `MutualFundsOrUTIMember` | shareholders | 6 | 6 | 4 | 9 | 9 |
| ↑ | shares | 7,206,872 | 8,032,106 | 8,243,000 | 9,306,641 | 13,989,650 |
| ↑ | % of total | 4.76% | 5.31% | 5.45% | 6.11% | 9.18% |
| ↑ | locked-in | 3,656,871 | 1,828,437 | 0 | 0 | 0 |
| — `VentureCapitalFundsMember` | shareholders | 1 | 1 | 1 | 0 | 0 |
| ↑ | shares | 3,126,950 | 3,126,950 | 3,126,950 | 0 | 0 |
| ↑ | % of total | 2.07% | 2.07% | 2.07% | 0% | 0% |
| — `AlternativeInvestmentFundsMember` | shareholders | 35 | 35 | 33 | 31 | 32 |
| ↑ | shares | 32,175,875 | 31,661,961 | 31,775,408 | 34,070,917 | 28,574,002 |
| ↑ | % of total | 21.26% | 20.92% | 21.00% | 22.38% | 18.75% |
| ↑ | locked-in | 10,209,822 | 10,209,822 | 9,783,685 | 9,047,160 | 9,047,160 |
| — `InsuranceCompaniesMember` | shareholders | 2 | 2 | 2 | 2 | 2 |
| ↑ | shares | 4,745,652 | 6,339,294 | 6,047,823 | 8,243,122 | 6,941,344 |
| ↑ | % of total | 3.14% | 4.19% | 4.00% | 5.41% | 4.55% |
| ↑ | locked-in | 3,429,714 | 1,714,857 | 0 | 0 | 0 |
| — `NBFCsRegisteredWithRBIMember` | shareholders | 1 | — | — | — | 0 |
| ↑ | shares | 1,943 | — | — | — | 0 |
| — `BanksMember` | shares | — | — | — | 0 | 0 |
| — `ProvidentFundsOrPensionFundsMember` | shares | — | — | — | — | 0 |
| — `AssetReconstructionCompaniesMember` | shares | — | — | — | — | 0 |
| — `SovereignWealthFundsDomesticMember` | shares | — | — | — | — | 0 |
| — `OtherFinancialInstitutionsMember` | shares | — | — | — | — | 0 |
| — `OtherInstitutionsDomesticMember` | shares | — | — | — | — | 0 |
| **InstitutionsForeignMember** | shareholders | 30 | 39 | 41 | 40 | 67 |
| ↑ | shares | 53,585,259 | 53,330,717 | 52,882,334 | 52,046,844 | 52,857,796 |
| ↑ | % of total | 35.41% | 35.24% | 34.95% | 34.19% | 34.68% |
| ↑ | locked-in | 41,778,788 | 38,617,126 | 35,455,463 | 6,516,161 | 6,516,161 |
| ↑ | demat | 53,431,014 | 53,176,472 | 52,728,089 | 51,892,599 | 52,703,551 |
| — `ForeignDirectInvestmentMember` | shareholders | 16 | 16 | 16 | 16 | 16 |
| ↑ | shares | 42,633,602 | 42,633,602 | 42,633,602 | 42,383,602 | 41,344,858 |
| ↑ | % of total | 28.17% | 28.17% | 28.17% | 27.84% | 27.13% |
| ↑ | locked-in | 35,455,463 | 35,455,463 | 35,455,463 | 6,516,161 | 6,516,161 |
| ↑ | demat | 42,479,357 | 42,479,357 | 42,479,357 | 42,229,357 | 41,190,613 |
| — `InstitutionsForeignPortfolioInvestorCategoryOneMember` | shareholders | 14 | 20 | 23 | 23 | 45 |
| ↑ | shares | 10,951,657 | 10,389,853 | 10,166,446 | 9,602,453 | 11,136,413 |
| ↑ | % of total | 7.24% | 6.87% | 6.72% | 6.31% | 7.31% |
| ↑ | locked-in | 6,323,325 | 3,161,663 | 0 | 0 | 0 |
| — `InstitutionsForeignPortfolioInvestorCategoryTwoMember` | shareholders | — | 3 | 2 | 1 | 6 |
| ↑ | shares | — | 307,262 | 82,286 | 60,789 | 376,525 |
| ↑ | % of total | — | 0.20% | 0.05% | 0.04% | 0.25% |
| — `OtherInstitutionsForeignMember` / `OverseasDepositoriesMember` / `ForeignVentureCapitalInvestorsMember` / `SovereignWealthFundsForeignMember` | shares | — | 0 where present | 0 where present | 0 where present | 0 |
| **Governments** (`CentralGovernmentOrPresidentOfIndia`, `StateGovernmentsOrGovernors`, `ShareholdingByCompaniesOrBodiesCorporateWhereCentralOrStateGovernmentIsPromoter`, `GovernmentsMember`) | shares | — | — | — | — | 0 |
| **NonInstitutionsMember** | shareholders | 103,944 | 46,468 | 41,991 | 39,613 | 40,541 |
| ↑ | shares | 25,715,844 | 24,067,367 | 24,482,880 | 23,801,864 | 25,277,012 |
| ↑ | % of total | 16.99% | 15.90% | 16.18% | 15.64% | 16.59% |
| ↑ | ESOP/convertibles underlying | 7,567,272 | 7,567,272 | 7,567,272 | 6,433,865 | 6,522,593 |
| ↑ | locked-in | 19,352,952 | 19,352,952 | 19,352,952 | 2,926,410 | 2,926,410 |
| ↑ | demat | 22,789,434 | 21,140,957 | 21,556,470 | 20,875,454 | 22,350,602 |
| — `KeyManagerialPersonnelMember` | shareholders | 1 | 1 | 1 | 1 | 1 |
| ↑ | shares | 106,104 | 106,104 | 106,104 | **2,086** | **2,086** |
| ↑ | % of total | 0.07% | 0.07% | 0.07% | 0% | 0% |
| ↑ | ESOP underlying (`NumberOfSharesOutstandingESOPGranted`) | 758,880 | 758,880 | 758,880 | 758,880 | 758,880 |
| ↑ | fully diluted shares | 864,984 | 864,984 | 864,984 | 760,966 | 760,966 |
| ↑ | `NumberOfSharesUnderSubCategoryOne` | 85,104 | 85,104 | 85,104 | 0 | 0 |
| — `ResidentIndividualShareholdersHoldingNominalShareCapitalUpToRsTwoLakhMember` | shareholders | 102,494 | 45,608 | 41,246 | 38,851 | 39,597 |
| ↑ | shares | 6,538,487 | 5,105,879 | 5,111,375 | 5,846,844 | 6,339,591 |
| ↑ | % of total | 4.32% | 3.37% | 3.38% | 3.84% | 4.16% |
| ↑ | ESOP underlying | 1,291,526 | 1,291,526 | 1,291,526 | 742,595 | 891,443 |
| ↑ | locked-in | 1,828,238 | 1,828,238 | 1,828,238 | 0 | 0 |
| — `ResidentIndividualShareholdersHoldingNominalShareCapitalInExcessOfRsTwoLakhMember` | shareholders | 11 | 10 | 10 | 9 | 10 |
| ↑ | shares | 14,086,564 | 13,854,477 | 13,854,477 | 13,388,456 | 14,109,676 |
| ↑ | % of total | 9.31% | 9.16% | 9.16% | 8.79% | 9.26% |
| ↑ | ESOP underlying | 5,516,866 | 5,516,866 | 5,516,866 | 4,932,390 | 4,872,270 |
| ↑ | locked-in | 12,977,404 | 12,977,404 | 12,977,404 | 0 | 0 |
| — `NonResidentIndiansMember` | shareholders | 227 | 257 | 196 | 236 | 302 |
| ↑ | shares | 34,417 | 92,807 | 65,195 | 87,150 | 133,728 |
| ↑ | % of total | 0.02% | 0.06% | 0.04% | 0.06% | 0.09% |
| ↑ | locked-in | 21,280 | 21,280 | 21,280 | 0 | 0 |
| — `BodiesCorporateMember` | shareholders | 39 | 93 | 81 | 80 | 133 |
| ↑ | shares | 1,865,729 | 1,761,629 | 2,354,419 | 1,485,139 | 1,664,965 |
| ↑ | % of total | 1.23% | 1.16% | 1.56% | 0.98% | 1.09% |
| ↑ | locked-in | 1,589,620 | 1,589,620 | 1,589,620 | 0 | 0 |
| — `OtherNonInstitutionsMember` | shareholders | 1,172 | 499 | 457 | 436 | 498 |
| ↑ | shares | 3,084,543 | 3,146,471 | 2,991,310 | 2,992,189 | 3,026,966 |
| ↑ | % of total | 2.04% | 2.08% | 1.98% | 1.97% | 1.99% |
| ↑ | locked-in | 2,936,410 | 2,936,410 | 2,936,410 | 2,926,410 | 2,926,410 |
| ↑ | demat | 158,133 | 220,061 | 64,900 | 65,779 | 100,556 |

**Trusts and Employee Benefit Trust — NOT DISCLOSED.** The XBRL taxonomy in use
(`in-bse-shp 2025-05-31`) carries **no `Trusts` member and no `EmployeeBenefitTrust` member**, and none is
reported in any of the five instances. Any trust holding sits, unlabelled, inside
`OtherNonInstitutionsMember`, whose only named constituent in every quarter is `ACCESS INDIA CAPITAL`
categorised `CategoryOfOtherNonInstitutions = Firm` -> the SEBI-format shareholding-pattern **Table III
"Any Other (specify)" sub-table** as filed in PDF/HTML with BSE and NSE would name the remaining
constituents; it is not in this corpus.

`TIE-OUT` — promoter + public = total at every date: 24,761,977 + 126,558,395 = 151,320,372 (Q1–Q3);
24,761,977 + 127,469,388 = 152,231,365; 24,761,977 + 127,639,804 = 152,401,781. Domestic institutions +
foreign institutions + non-institutions = public at every date (e.g. 30-Jun-2026: 49,504,996 + 52,857,796 +
25,277,012 = 127,639,804). Every sub-category sums to its parent at every date; recomputed independently.

### 1.4 Every shareholder named individually in the XBRL, quarter by quarter — the exit evidence

**This is the primary evidence for W2_exits.** Unit: number of equity shares of face value Re. 1 each.
Percentages are percent readings per §0a. `locked-in` is `NumberOfTheLockedInShares` for that holder.
`not listed` means the holder does not appear in that quarter's instance **at all** — which for the
Table III named-holder tables means the holding fell below the 1% naming threshold, or the name changed,
**not necessarily that the position went to nil**.

Row-matching rule used: names are matched on the first 48 characters, case- and whitespace-insensitive,
trailing full stop ignored. Where the printed name differs between quarters, **every printed variant is
shown in the name cell**, separated by `/`, in quarter order. No two differently-worded fund names have
been merged into one row.

| Category | Name(s) exactly as printed in the XBRL | Field | 18-Aug-2025 | 30-Sep-2025 | 31-Dec-2025 | 31-Mar-2026 | 30-Jun-2026 |
|---|---|---|---|---|---|---|---|
| A1 Individuals/HUF — promoter & promoter group | "GAURAV SINGH KUSHWAHA" | shares | 24,465,127 | 24,465,127 | 24,465,127 | 24,465,127 | 24,465,127 |
| ↑ | ↑ | % of total | 16.17% | 16.17% | 16.17% | 16.07% | 16.05% |
| ↑ | ↑ | locked-in | 24,465,127 | 24,465,127 | 24,465,127 | 15,409,076 | 15,409,076 |
| ↑ | "ARPITA TOMAR" | shares | 296,850 | 296,850 | 296,850 | 296,850 | 296,850 |
| ↑ | ↑ | % of total | 0.2% | 0.2% | 0.2% | 0.19% | 0.19% |
| ↑ | ↑ | locked-in | 296,850 | 296,850 | 296,850 | 0 | 0 |
| ↑ | "Shivraj Singh Kushwaha" | shares | 0 | 0 | 0 | 0 | not listed |
| ↑ | ↑ | % of total | 0% | 0% | 0% | 0% | not listed |
| ↑ | ↑ | locked-in | 0 | 0 | 0 | 0 | not listed |
| ↑ | "Prabha Kushwaha" | shares | 0 | 0 | 0 | 0 | not listed |
| ↑ | ↑ | % of total | 0% | 0% | 0% | 0% | not listed |
| ↑ | ↑ | locked-in | 0 | 0 | 0 | 0 | not listed |
| ↑ | "Prashant Singh Kushwaha" | shares | 0 | 0 | 0 | 0 | not listed |
| ↑ | ↑ | % of total | 0% | 0% | 0% | 0% | not listed |
| ↑ | ↑ | locked-in | 0 | 0 | 0 | 0 | not listed |
| ↑ | "Nivaan Singh Kushwaha" | shares | 0 | 0 | 0 | 0 | not listed |
| ↑ | ↑ | % of total | 0% | 0% | 0% | 0% | not listed |
| ↑ | ↑ | locked-in | 0 | 0 | 0 | 0 | not listed |
| ↑ | "Kayna Singh Kushwaha" | shares | 0 | 0 | 0 | 0 | not listed |
| ↑ | ↑ | % of total | 0% | 0% | 0% | 0% | not listed |
| ↑ | ↑ | locked-in | 0 | 0 | 0 | 0 | not listed |
| ↑ | "Arvind Pratap Singh Tomar" | shares | 0 | 0 | 0 | 0 | not listed |
| ↑ | ↑ | % of total | 0% | 0% | 0% | 0% | not listed |
| ↑ | ↑ | locked-in | 0 | 0 | 0 | 0 | not listed |
| ↑ | "Mina Tomar" | shares | 0 | 0 | 0 | 0 | not listed |
| ↑ | ↑ | % of total | 0% | 0% | 0% | 0% | not listed |
| ↑ | ↑ | locked-in | 0 | 0 | 0 | 0 | not listed |
| ↑ | "Anurag Tomar" | shares | 0 | 0 | 0 | 0 | not listed |
| ↑ | ↑ | % of total | 0% | 0% | 0% | 0% | not listed |
| ↑ | ↑ | locked-in | 0 | 0 | 0 | 0 | not listed |
| A2 NRI/Foreign Individuals — promoter group | "Archana Tomar" | shares | 0 | 0 | 0 | 0 | not listed |
| ↑ | ↑ | % of total | 0% | 0% | 0% | 0% | not listed |
| ↑ | ↑ | locked-in | 0 | 0 | 0 | 0 | not listed |
| B1(a) Mutual Funds/UTI | "NIPPON LIFE INDIA TRUSTEE LTD-A/C NIPPON INDIA SMALL CAP FUN" / "NIPPON LIFE INDIA TRUSTEE LTD-A/C NIPPON INDIA SMALL" / "NIPPON LIFE INDIA TRUSTEE LTD-A/C NIPPON INDIA SMA" | shares | 5,186,909 | 5,186,909 | 5,186,909 | not listed | not listed |
| ↑ | ↑ | % of total | 3.43% | 3.43% | 3.43% | not listed | not listed |
| ↑ | ↑ | locked-in | 1,935,431 | 967,716 | 0 | not listed | not listed |
| ↑ | "ADITYA BIRLA SUN LIFE TRUSTEE PRIVATE LIMITED A/C" | shares | not listed | 1,720,403 | 2,536,773 | 2,448,026 | 1,721,152 |
| ↑ | ↑ | % of total | not listed | 1.14% | 1.68% | 1.61% | 1.13% |
| ↑ | ↑ | locked-in | not listed | 333,646 | 0 | 0 | 0 |
| ↑ | "NIPPON LIFE INDIA TRUSTEE LTD-A/C NIPPON INDIA CON" | shares | not listed | not listed | not listed | 6,129,054 | not listed |
| ↑ | ↑ | % of total | not listed | not listed | not listed | 4.03% | not listed |
| ↑ | ↑ | locked-in | not listed | not listed | not listed | 0 | not listed |
| ↑ | "NIPPON LIFE INDIA TRUSTEE LTD-A/C NIPPON INDIA MUL" | shares | not listed | not listed | not listed | not listed | 9,952,140 |
| ↑ | ↑ | % of total | not listed | not listed | not listed | not listed | 6.53% |
| ↑ | ↑ | locked-in | not listed | not listed | not listed | not listed | 0 |
| B1(b) Venture Capital Funds | "VISTRA ITCL (INDIA) LIMITED" | shares | 3,126,950 | 3,126,950 | 3,126,950 | not listed | not listed |
| ↑ | ↑ | % of total | 2.07% | 2.07% | 2.07% | not listed | not listed |
| ↑ | ↑ | locked-in | 0 | 0 | 0 | not listed | not listed |
| B1(c) Alternate Investment Funds | "IVYCAP VENTURES TRUST FUND II" | shares | 2,540,390 | 2,540,390 | 2,540,390 | 2,540,390 | 2,540,390 |
| ↑ | ↑ | % of total | 1.68% | 1.68% | 1.68% | 1.67% | 1.67% |
| ↑ | ↑ | locked-in | 1,502,448 | 1,502,448 | 1,502,448 | 1,502,448 | 1,502,448 |
| ↑ | "IRON PILLAR INDIA FUND I" | shares | 1,568,052 | 1,568,052 | 1,568,052 | 1,568,052 | not listed |
| ↑ | ↑ | % of total | 1.04% | 1.04% | 1.04% | 1.03% | not listed |
| ↑ | ↑ | locked-in | 830,184 | 830,184 | 830,814 | 830,184 | not listed |
| ↑ | "IVYCAP VENTURES TRUST FUND III" | shares | 1,659,376 | 1,659,376 | 1,659,376 | 1,659,376 | 1,659,376 |
| ↑ | ↑ | % of total | 1.1% | 1.1% | 1.1% | 1.09% | 1.09% |
| ↑ | ↑ | locked-in | 981,395 | 981,395 | 981,395 | 981,395 | 981,395 |
| ↑ | "IE VENTURE INVESTMENT FUND II" | shares | 4,112,680 | 4,112,680 | 4,112,680 | 4,112,680 | 4,112,680 |
| ↑ | ↑ | % of total | 2.72% | 2.72% | 2.72% | 2.7% | 2.7% |
| ↑ | ↑ | locked-in | 1,406,946 | 1,406,946 | 1,406,946 | 1,406,946 | 1,406,946 |
| ↑ | "360 ONE SPECIAL OPPORTUNITIES FUND - SERIES 12" | shares | 5,047,169 | 5,047,169 | 5,047,169 | 4,898,848 | 3,843,774 |
| ↑ | ↑ | % of total | 3.34% | 3.34% | 3.34% | 3.22% | 2.52% |
| ↑ | ↑ | locked-in | 0 | 0 | 0 | 0 | 0 |
| ↑ | "360 ONE SPECIAL OPPORTUNITIES FUND - SERIES 11" | shares | 1,659,376 | 1,659,376 | 1,659,376 | 1,639,036 | not listed |
| ↑ | ↑ | % of total | 1.1% | 1.1% | 1.1% | 1.08% | not listed |
| ↑ | ↑ | locked-in | 981,395 | 981,395 | 981,395 | 981,395 | not listed |
| ↑ | "360 ONE LARGE VALUE FUND- SERIES 13" | shares | 2,489,064 | 2,489,064 | 2,489,064 | 2,480,044 | 1,945,913 |
| ↑ | ↑ | % of total | 1.64% | 1.64% | 1.64% | 1.63% | 1.28% |
| ↑ | ↑ | locked-in | 1,472,093 | 1,472,093 | 1,472,093 | 1,472,093 | 1,472,093 |
| ↑ | "IRON PILLAR FUND I LTD" | shares | 2,609,925 | 2,609,925 | 2,609,925 | 2,609,925 | 2,322,746 |
| ↑ | ↑ | % of total | 1.72% | 1.72% | 1.72% | 1.71% | 1.52% |
| ↑ | ↑ | locked-in | 1,382,001 | 1,382,001 | 1,382,001 | 1,382,001 | 1,382,001 |
| ↑ | "PRATITHI GROWTH FUND I" | shares | 2,898,944 | 2,898,944 | 2,898,944 | 2,898,944 | not listed |
| ↑ | ↑ | % of total | 1.92% | 1.92% | 1.92% | 1.9% | not listed |
| ↑ | ↑ | locked-in | 690,000 | 690,000 | 690,000 | 0 | not listed |
| ↑ | "IVYCAP VENTURES TRUST" | shares | not listed | not listed | not listed | 2,618,110 | not listed |
| ↑ | ↑ | % of total | not listed | not listed | not listed | 1.72% | not listed |
| ↑ | ↑ | locked-in | not listed | not listed | not listed | 0 | not listed |
| ↑ | "PRATITHI GROWTH FUND I-LVF" | shares | not listed | not listed | not listed | not listed | 2,898,944 |
| ↑ | ↑ | % of total | not listed | not listed | not listed | not listed | 1.9% |
| ↑ | ↑ | locked-in | not listed | not listed | not listed | not listed | 0 |
| B1(f) Insurance Companies | "SBI LIFE INSURANCE CO. LTD" | shares | 4,078,362 | 5,672,004 | 5,380,632 | 7,611,320 | 6,707,336 |
| ↑ | ↑ | % of total | 2.7% | 3.75% | 3.56% | 5% | 4.4% |
| ↑ | ↑ | locked-in | 2,762,424 | 1,381,212 | 0 | 0 | 0 |
| B2 FPI Category I | "AMANSA HOLDINGS PRIVATE LIMITED" | shares | 4,654,228 | 4,654,228 | 4,806,803 | 4,809,307 | 4,905,077 |
| ↑ | ↑ | % of total | 3.08% | 3.08% | 3.18% | 3.16% | 3.22% |
| ↑ | ↑ | locked-in | 3,272,012 | 1,636,006 | 0 | 0 | 0 |
| ↑ | "GOLDMAN SACHS FUNDS - GOLDMAN SACHS INDIA EQUITY P" | shares | not listed | 1,863,453 | 1,863,453 | 1,863,453 | 1,863,453 |
| ↑ | ↑ | % of total | not listed | 1.23% | 1.23% | 1.22% | 1.22% |
| ↑ | ↑ | locked-in | not listed | 685,183 | 0 | 0 | 0 |
| B2 Foreign Direct Investment | "KALAARI CAPITAL PARTNERS II LLC" | shares | 3,536,990 | 3,536,990 | 3,536,990 | 3,536,990 | 3,536,990 |
| ↑ | ↑ | % of total | 2.34% | 2.34% | 2.34% | 2.32% | 2.32% |
| ↑ | ↑ | locked-in | 3,536,990 | 3,536,990 | 3,536,990 | 0 | 0 |
| ↑ | "RB INVESTMENTS PTE. LTD." | shares | 2,613,955 | 2,613,955 | 2,613,955 | 2,613,955 | 2,613,955 |
| ↑ | ↑ | % of total | 1.73% | 1.73% | 1.73% | 1.72% | 1.72% |
| ↑ | ↑ | locked-in | 2,613,955 | 2,613,955 | 2,613,955 | 0 | 0 |
| ↑ | "ACCEL INDIA III (MAURITIUS) LTD" | shares | 13,540,055 | 13,540,055 | 13,540,055 | 13,290,055 | 12,313,091 |
| ↑ | ↑ | % of total | 8.95% | 8.95% | 8.95% | 8.73% | 8.08% |
| ↑ | ↑ | locked-in | 6,361,916 | 6,361,916 | 6,361,916 | 6,361,916 | 6,361,916 |
| ↑ | "STEADVIEW CAPITAL MAURITIUS LIMITED" | shares | 3,604,943 | 3,604,943 | 3,604,943 | 3,604,943 | 3,543,163 |
| ↑ | ↑ | % of total | 2.38% | 2.38% | 2.38% | 2.37% | 2.32% |
| ↑ | ↑ | locked-in | 3,604,943 | 3,604,943 | 3,604,943 | 0 | 0 |
| ↑ | "MIH INVESTMENTS ONE B.V." | shares | 6,080,439 | 6,080,439 | 6,080,439 | 6,080,439 | 6,080,439 |
| ↑ | ↑ | % of total | 4.02% | 4.02% | 4.02% | 3.99% | 3.99% |
| ↑ | ↑ | locked-in | 6,080,439 | 6,080,439 | 6,080,439 | 0 | 0 |
| ↑ | "ACCEL INDIA VII (MAURITIUS) LIMITED" | shares | 3,767,870 | 3,767,870 | 3,767,870 | 3,767,870 | 3,767,870 |
| ↑ | ↑ | % of total | 2.49% | 2.49% | 2.49% | 2.48% | 2.47% |
| ↑ | ↑ | locked-in | 3,767,870 | 3,767,870 | 3,767,870 | 0 | 0 |
| ↑ | "PEAK XV PARTNERS GROWTH INVESTMENTS IV" | shares | 4,071,580 | 4,071,580 | 4,071,580 | 4,071,580 | 4,071,580 |
| ↑ | ↑ | % of total | 2.69% | 2.69% | 2.69% | 2.67% | 2.67% |
| ↑ | ↑ | locked-in | 4,071,580 | 4,071,580 | 4,071,580 | 0 | 0 |
| B3 Resident individuals > Rs 2 lakh | "GANESH KRISHNAN" | shares | 1,632,390 | 1,632,390 | 1,632,390 | 1,616,070 | 1,616,070 |
| ↑ | ↑ | % of total | 1.08% | 1.08% | 1.08% | 1.06% | 1.06% |
| ↑ | ↑ | locked-in | 1,632,390 | 1,632,390 | 1,632,390 | 0 | 0 |
| ↑ | "SUNIL KANT MUNJAL" | shares | 5,827,570 | 5,827,570 | 5,827,570 | 5,650,000 | 5,565,000 |
| ↑ | ↑ | % of total | 3.85% | 3.85% | 3.85% | 3.71% | 3.65% |
| ↑ | ↑ | locked-in | 5,827,570 | 5,827,570 | 5,827,570 | 0 | 0 |
| ↑ | "NKSQUARED ." / "NKSQUARED" | shares | 1,659,376 | 1,659,376 | 1,659,376 | 1,659,376 | 1,659,376 |
| ↑ | ↑ | % of total | 1.1% | 1.1% | 1.1% | 1.09% | 1.09% |
| ↑ | ↑ | locked-in | 1,659,376 | 1,659,376 | 1,659,376 | 0 | 0 |
| ↑ | "KAMATH ASSOCIATES" | shares | 1,659,376 | 1,659,376 | 1,659,376 | 1,659,376 | 1,659,376 |
| ↑ | ↑ | % of total | 1.1% | 1.1% | 1.1% | 1.09% | 1.09% |
| ↑ | ↑ | locked-in | 1,659,376 | 1,659,376 | 1,659,376 | 0 | 0 |
| B3 Any Other (Other Non-Institutions) | "ACCESS INDIA CAPITAL" | shares | 2,926,410 | 2,926,410 | 2,926,410 | 2,926,410 | 2,926,410 |
| ↑ | ↑ | % of total | 1.93% | 1.93% | 1.93% | 1.92% | 1.92% |
| ↑ | ↑ | locked-in | 2,926,410 | 2,926,410 | 2,926,410 | 2,926,410 | 2,926,410 |

**Six transcription cautions on the table above, none of them resolved here:**

1. **Fund names are truncated at source.** The XBRL `NameOfTheShareholder` string is cut at roughly 50
   characters in the four post-listing filings. `"NIPPON LIFE INDIA TRUSTEE LTD-A/C NIPPON INDIA SMALL CAP
   FUN"` (18-Aug-2025) becomes `"…NIPPON INDIA SMALL"` and `"…NIPPON INDIA SMA"`, then a *different*
   scheme suffix `"…NIPPON INDIA CON"` (31-Mar-2026) and `"…NIPPON INDIA MUL"` (30-Jun-2026). **These are
   shown as three separate rows because the truncated strings do not establish that they are the same
   scheme.** Whether Nippon's small-cap scheme exited and two other Nippon schemes entered, or the same
   money moved between schemes, **is NOT DISCLOSED in the XBRL** -> the SEBI-format shareholding-pattern
   PDF/HTML, or the fund houses' own scheme portfolio disclosures, would answer it.
2. `"PRATITHI GROWTH FUND I"` (four quarters, 2,898,944 shares) and `"PRATITHI GROWTH FUND I-LVF"`
   (30-Jun-2026, 2,898,944 shares) are separate rows for the same reason. Share count identical.
3. `"IVYCAP VENTURES TRUST"` appears **only** at 31-Mar-2026 with 2,618,110 shares and is a different
   printed name from `"IVYCAP VENTURES TRUST FUND II"` and `"…FUND III"`, both of which are also listed
   that quarter. Three separately-named IvyCap vehicles at 31-Mar-2026; two at 30-Jun-2026.
4. `"GANESH KRISHNAN"` / `"GANESH  KRISHNAN"` (double space, 31-Dec-2025 onward) and `"NKSQUARED ."` /
   `"NKSQUARED"` are the same rows; the punctuation and spacing differ between filings.
5. **`SBI LIFE INSURANCE CO. LTD` crosses 5% at 31-Mar-2026** (7,611,320 shares, 5.00% of total) and falls
   back to 4.40% at 30-Jun-2026 `[SHP 31Mar2026]` `[SHP 30Jun2026]`.
6. **`ACCESS INDIA CAPITAL` holds 2,926,410 shares (1.92–1.93%) at all five dates and its demat holding is
   0 at four of the five dates and 0 at the fifth** — `NumberOfEquitySharesHeldInDematerializedForm = 0`
   throughout, while `NumberOfTheLockedInShares = 2,926,410` (2,926,410 from 31-Mar-2026; 2,936,410 for the
   `OtherNonInstitutions` category as a whole in the first three quarters). It is flagged
   `WhetherACategoryOrMoreThan1PercentageOfShareholding = "More than 1 percentage of shareholding"` and
   `CategoryOfOtherNonInstitutions = "Firm"` `[SHP 18Aug2025 …30Jun2026]`.

### 1.5 The lock-in ladder — total, promoter, public, by date

**Unit: number of equity shares.**

| Locked-in block | 18-Aug-2025 | 30-Sep-2025 | 31-Dec-2025 | 31-Mar-2026 | 30-Jun-2026 |
|---|---|---|---|---|---|
| Total company | 103,190,124 | 96,485,171 | 89,354,077 | 33,898,807 | 33,898,807 |
| — % of total shares | 68.19% | 63.76% | 59.05% | 22.27% | 22.24% |
| Promoter & promoter group | 24,761,977 | 24,761,977 | 24,761,977 | 15,409,076 | 15,409,076 |
| Public — total | 78,428,147 | 71,723,194 | 64,592,100 | 18,489,731 | 18,489,731 |
| Public — domestic institutions | 17,296,407 | 13,753,116 | 9,783,685 | 9,047,160 | 9,047,160 |
| Public — foreign institutions | 41,778,788 | 38,617,126 | 35,455,463 | 6,516,161 | 6,516,161 |
| Public — non-institutions | 19,352,952 | 19,352,952 | 19,352,952 | 2,926,410 | 2,926,410 |
| `WhetherTheListedEntityHasAnySharesInLockedIn` | true | true | true | true | true |

`TIE-OUT` — 24,761,977 + 78,428,147 = 103,190,124 (18-Aug-2025); 15,409,076 + 18,489,731 = 33,898,807
(31-Mar-2026 and 30-Jun-2026). Public sub-blocks: 9,047,160 + 6,516,161 + 2,926,410 = 18,489,731 ✓.
The lock-in release between the 31-Dec-2025 and 31-Mar-2026 filings is 89,354,077 − 33,898,807 =
**55,455,270 shares**, of which 9,352,901 is promoter and 46,102,369 is public `[SHP 31Dec2025]`
`[SHP 31Mar2026]`. **The lock-in class of each block, and the expiry date of each tranche, are NOT
DISCLOSED in the XBRL** -> the Prospectus of 14-Aug-2025 "Capital Structure — details of lock-in" section
carries the class-by-class ladder; it is a Tier-1 document held at `data/ipo/BLUESTONE-PROSPECTUS-2025.pdf`
and is outside this agent's slice.

### 1.6 Encumbrance — and a three-way DISAGREE on what is encumbered

**Unit: number of equity shares. Percentages as printed (percent readings per §0a).**

| Field (XBRL element, verbatim) — promoter & promoter group context | 18-Aug-2025 | 30-Sep-2025 | 31-Dec-2025 | 31-Mar-2026 | 30-Jun-2026 |
|---|---|---|---|---|---|
| `WhetherAnySharesHeldByPromotersAreEncumberedUnderPledged` | **false** | **true** | true | true | true |
| `WhetherAnySharesHeldByPromotersAreEncumberedUnderNonDisposalUndertaking` | **false** | **true** | true | true | true |
| `WhetherAnySharesHeldByPromotersAreEncumberedOtherThanByWayOfPledgeOrNDU` | false | false | false | false | false |
| `NumberOfSharesEncumberedUnderPledged` | *element absent* | 9,215,127 | 9,215,127 | 9,215,127 | 9,215,127 |
| `EncumberedShareUnderPledgedAsPercentageOfTotalNumberOfShares` (of the promoter block) | — | 37.21% | 37.21% | 37.21% | 37.21% |
| `NumberOfSharesEncumberedUnderNonDisposalUndertaking` | *element absent* | 15,250,000 | 15,250,000 | 15,250,000 | 15,250,000 |
| `EncumberedShareUnderNonDisposalUndertakingAsPercentageOfTotalNumberOfShares` (of the promoter block) | — | 61.59% | 61.59% | 61.59% | 61.59% |
| `NumberOfSharesEncumbered` (total) | *element absent* | 24,465,127 | 24,465,127 | 24,465,127 | 24,465,127 |
| `EncumberedSharesHeldAsPercentageOfTotalNumberOfShares` (of the promoter block) | — | 98.80% | 98.80% | 98.80% | 98.80% |
| Same, expressed on the whole company (`ShareholdingPatternMember` context) | — | 16.36% | 16.36% | 16.27% | **16.05%** |

`TIE-OUT` — 9,215,127 + 15,250,000 = 24,465,127, and 24,465,127 / 24,761,977 = 98.80%. The whole of the
promoter's *own* holding (Gaurav Singh Kushwaha's 24,465,127) is reported encumbered; Arpita Tomar's
296,850 is not.

> **DISAGREE — three different statements of the same encumbrance, all on the record.**
>
> **(a) The shareholding-pattern XBRL explanatory note, identical in the 30-Sep-2025, 31-Dec-2025 and
> 31-Mar-2026 instances, verbatim:** *"Please note that under the Non-Disposal Undertaking (NDU), where
> multiple NDUs have been executed with different lenders and varying levels of shareholding, we have
> taken the highest number of shares as part of NDU across the lender stack. Hence the reported number of
> equity shares is 1,52,50,000 (i.e., 2,44,65,127 minus 92,15,127) Equity Shares. **The number of Equity
> shares under NDU is whole of shareholding i.e. 2,44,65,127 Equity shares.** Please note that the
> Non-Disposal Undertakings (NDUs) have not been executed at the Depository level."*
> `[SHP 30Sep2025, DisclosureOfNotesOnShareholdingPatternExplanatoryTextBlock]`
> — i.e. the note says the NDU covers **24,465,127** shares while the field reports **15,250,000**.
>
> **(b) The promoter's own SAST Regulation 31(4) annual declaration, dated 08-Apr-2026, filed 24-Jun-2026,
> verbatim:** *"I hereby confirm and declare that, during the financial year 2025-26, the Promoter of
> Bluestone Jewellery and Lifestyle Limited, ("the Target Company"), have pledged equity shares of the
> Target Company as on March 31, 2026 the total pledged quantity stands at 92,15,127 equity shares of the
> Target Company. Please note that the Non-Disposal Undertaking (NDU), where Multiple NDU have been
> executed with different lenders and varying levels of shareholding. Further, the Promoter have made
> encumbrance, directly or indirectly during the financial year 2025-2026."* and *"Further, the Promoter
> Group along with Person acting in concert, have not created encumbrance or pledged any equity shares of
> the Target Company as on March 31, 2026 and the total pledged quantity stands at Nil equity shares."*
> `[NSE ann 24-Jun-2026, 24-Jun-2026_team_sandeshc_23062026122639_50, p1]`
> `[IMAGE: data/scanned_pages/24-Jun-2026_team_sandeshc_23062026122639_50_p1.png]`
>
> **(c) The 18-Aug-2025 XBRL says there is no encumbrance at all** — all three
> `WhetherAnySharesHeldByPromotersAreEncumbered…` flags are `false` and no encumbrance element exists
> `[SHP 18Aug2025, MainI]`.
>
> **Status: DISAGREE. Not resolved here.** Three numbers are on the record for the same promoter block —
> 9,215,127 "pledged", 15,250,000 "under NDU as reported", 24,465,127 "under NDU in substance" — and a
> fourth statement (nil, at listing) six weeks before the first of them. The identity of the lenders, the
> amount borrowed and the purpose of the borrowing are **NOT DISCLOSED anywhere in the 119 post-listing
> filings** -> the credit-rating rationale of India Ratings & Research dated 07-Aug-2026 (§6, GAP-004) and
> the promoter's personal borrowing arrangements are the documents that would answer it; neither is in
> this corpus.
>
> **The explanatory note is dropped entirely from the 30-Jun-2026 instance** — that filing carries no
> `DisclosureOfNotesOnShareholdingPatternExplanatoryTextBlock` at all, while still reporting the same
> 15,250,000 NDU figure `[SHP 30Jun2026]`.

### 1.7 Other declarations on the face of the XBRL

| Field | 18-Aug-2025 | 30-Sep-2025 | 31-Dec-2025 | 31-Mar-2026 | 30-Jun-2026 |
|---|---|---|---|---|---|
| `WhetherTheListedEntityHasIssuedAnyPartlyPaidUpShares` | false | false | false | false | false |
| `WhetherTheListedEntityHasIssuedAnyConvertibleSecurities` | false | false | false | false | false |
| `WhetherTheListedEntityHasIssuedAnyWarrants` | false | false | false | false | false |
| `WhetherTheListedEntityHasGrantedAnyESOPWhichAreOutstanding` | true | true | true | true | true |
| — for promoter and promoter group | false | false | false | false | false |
| — for public shareholder | true | true | true | true | true |
| `WhetherTheListedEntityHasAnySharesAgainstWhichDepositoryReceiptsAreIssued` | false | false | false | false | false |
| `WhetherCompanyHasEquitySharesWithDifferentialVotingRights` | false | false | false | false | false |
| `WhetherTheListedEntityHasAnySignificantBeneficialOwner` | **false** | **false** | **false** | **false** | **false** |
| `WhetherTheListedEntityIsPublicSectorUndertaking` | false | false | false | false | false |
| `PercentageOfBoardApprovedLimits` (foreign ownership) | 100 (=100%) | 1 (=100%) | 1 (=100%) | 1 (=100%) | 1 (=100%) |
| `PercentageOfLimitsUtilized` (foreign ownership) | 35.42 (=35.42%) | 0.3687 (=36.87%) | 0.3659 (=36.59%) | 0.3433 (=34.33%) | 0.3421 (=34.21%) |
| `ClassOfSecurity` / `TypeOfReport` / `ShareholdingPatternFiledUnder` | `******` | `******` | `******` | `******` | `******` |

The last row is **masked in the XBRL as supplied** — the literal value in the file is six asterisks, not a
blank -> the SEBI-format shareholding-pattern PDF/HTML would carry the class of security and the
regulation under which the pattern is filed. `PermanentAccountNumberOfShareholder` and
`TypeOfPromoterShareholding` are masked the same way on every named holder.

**Explanatory note items 1, 3 and 4, verbatim, present in the 30-Sep-2025, 31-Dec-2025 and 31-Mar-2026
instances and absent from 30-Jun-2026** `[SHP 30Sep2025]`:
> *"1. The categorisation of shareholders in the Shareholding Pattern is being disclosed basis the
> categorisation mentioned in the Benpos and reports received from the Registrar and Transfer Agent of the
> Company viz. KFin Technologies Limited. … 3. Under Part B4(i) of Column F, NRI includes total of both
> Repatriable basis and Non - Repatriable basis. 4. Under Annexure B, while calculating limit utilised,
> NRI on a Non- Repatriable Basis are excluded."*

The 18-Aug-2025 instance's note is different and reads, verbatim: *"Table VI - Statement showing foreign
ownership limits - Approved Limit: # Details of sectoral / statutory cap prescribed by Government /
Regulatory Authorities"* `[SHP 18Aug2025]`.

### 1.8 Disclosure depth changed at 30-Jun-2026

| | 18-Aug-2025 | 30-Sep-2025 | 31-Dec-2025 | 31-Mar-2026 | 30-Jun-2026 |
|---|---|---|---|---|---|
| Promoter/promoter-group persons named individually | 11 | 11 | 11 | 11 | **2** |
| Explanatory note block present | yes (different text) | yes | yes | yes | **no** |
| Named public holders listed | 22 | 24 | 24 | 24 | 21 |

The nine promoter-group persons holding nil shares (Shivraj Singh Kushwaha, Prabha Kushwaha, Prashant
Singh Kushwaha, Nivaan Singh Kushwaha, Kayna Singh Kushwaha, Arvind Pratap Singh Tomar, Mina Tomar, Anurag
Tomar, Archana Tomar) are named in the first four instances and **not named in the fifth**
`[SHP 31Mar2026]` `[SHP 30Jun2026]`. All eleven are still named as promoter/promoter group in the
Monitoring Agency Report of 20-Jul-2026, which covers the same quarter
`[MAR Q1FY27, 20260720_BlueStone_Monitoring_Agency_Report_Q1FY27, p4]`, and in the promoter's own SAST
Annexure I as at 31-Mar-2026
`[IMAGE: data/scanned_pages/24-Jun-2026_team_sandeshc_23062026122639_50_p2.png]`. **DISAGREE on the
promoter-group list length between the 30-Jun-2026 shareholding pattern (2) and the 20-Jul-2026
Monitoring Agency Report (11) for the same quarter-end.** Both recorded; not resolved here.

**Spelling variance in the promoter-group names, recorded because it is a name-matching hazard:** the
shareholding pattern prints `Kayna Singh Kushwaha`; every Monitoring Agency Report prints
`Kanya Singh Kushwaha` `[SHP 18Aug2025]` `[MAR Q2FY26, p4]` `[MAR Q3FY26, p4]` `[MAR Q4FY26, p4]`
`[MAR Q1FY27, p4]`.

### 1.9 Raw XBRL literals for the control rows — so §0a can be checked

| Element | 18-Aug-2025 literal | 30-Sep-2025 | 31-Dec-2025 | 31-Mar-2026 | 30-Jun-2026 |
|---|---|---|---|---|---|
| Promoter `ShareholdingAsAPercentageOfTotalNumberOfShares` | `16.36` | `0.1636` | `0.1636` | `0.1627` | `0.1625` |
| Public `ShareholdingAsAPercentageOfTotalNumberOfShares` | `83.64` | `0.8364` | `0.8364` | `0.8373` | `0.8375` |
| Total `LockedInSharesAsAPercentageOfTotalNumberOfShares` | `68.19` | `0.6376` | `0.5905` | `0.2227` | `0.2224` |
| Total `ShareholdingAsAPercentageOfTotalNumberOfShares` | `100.00` | `1` | `1` | `1` | `1` |

**Rounding note, not an error.** At 31-Mar-2026 the promoter aggregate reads 16.27% while its two named
constituents read 16.07% and 0.19%, summing to 16.26%. 24,465,127 / 152,231,365 = 16.0709% and
296,850 / 152,231,365 = 0.1950%, summing to 16.2659% -> 16.27%. The constituents are each rounded down
independently. Same pattern at 30-Jun-2026 (16.05% + 0.19% vs 16.25% aggregate).

---

## 2. Share count movement and the allotment reconciliation

**Unit: number of equity shares of face value Re. 1 each. Paid-up capital in Rupees is numerically equal
to the share count because face value is Re. 1.**

### 2.1 Every allotment announced between the shareholding dates

All nine are allotments of equity shares on exercise of vested options under the **"BlueStone Jewellery and
Lifestyle Limited – Employee Stock Option Plan 2014"**, all at **exercise price Re. 1 per share, premium
NIL**, all ranking pari passu. There were **no other issues of shares of any kind** in the thirteen months
— the XBRL reports no partly-paid shares, no convertibles, no warrants and no depository receipts at any
of the five dates (§1.7).

| # | Date | Board route | Shares allotted | Distinctive numbers (from → to) | Paid-up capital after (shares) | Filing |
|---|---|---|---|---|---|---|
| 1 | 03-Jan-2026 | resolution by circulation | 123,069 | 151,320,373 → 151,443,441 | 151,443,441 | `[NSE ann 03-Jan-2026, 20260103_ESOP_Allotment, p1-p2]` |
| 2 | 22-Jan-2026 | board meeting | 295,857 | 151,443,442 → 151,739,298 | 151,739,298 | `[NSE ann 22-Jan-2026, 20260122_DisclosureunderRegulation30ESOP, p1-p2]` |
| 3 | 16-Feb-2026 | resolution by circulation | 65,494 | 151,739,299 → 151,804,792 | 151,804,792 | `[NSE ann 16-Feb-2026, 20260216_StockExchangedisclosureallotmentofshares, p1-p2]` |
| 4 | 18-Mar-2026 | resolution by circulation | 426,573 | 151,804,793 → 152,231,365 | 152,231,365 | `[NSE ann 18-Mar-2026, 20260318_ESOPExercsieAllotment, p1-p2]` |
| 5 | 23-Apr-2026 | board meeting — **no standalone intimation; item 3 of the 23-page audited-results letter** | 129,573 | 152,231,366 → 152,360,938 | 152,360,938 | `[NSE ann 23-Apr-2026, 20260423_DisclosureunderRegulation30_3, p2 and p4]` |
| 6 | 09-Jun-2026 | resolution by circulation | 40,843 | 152,360,939 → 152,401,781 | 152,401,781 | `[NSE ann 09-Jun-2026, 20260609_DisclosureunderRegulation30, p1-p3]` |
| 7 | 20-Jul-2026 | board meeting | 4,853 | 152,401,782 → 152,406,634 | 152,406,634 | `[NSE ann 20-Jul-2026, 20260720_Allotment_of_Equity_Shares, p1-p3]` |
| 8 | 05-Aug-2026 | circular resolution | 342,766 | 152,406,635 → 152,749,400 | 152,749,400 | `[NSE ann 05-Aug-2026, 20260805_Allotment_of_Equity_Shares, p1-p3]` |
| 9 | 02-Sep-2026 | board meeting | 29,305 | 152,749,401 → 152,778,705 | 152,778,705 | `[NSE ann 02-Sep-2026, 20260902_Allotment_of_Equity_Shares, p1-p3]` (= `20260902_Outcome_of_BM`, Annexure B, p5-p6) |

Each allotment intimation carries, verbatim in field 13 and 14 of the Regulation 10(c) annexure,
`Exercise price per share  Rs.1/- each` (spelt `Re.1/- each` in the 05-Aug-2026 and 02-Sep-2026 filings)
and `Premium per share  NIL`. The ESOP scheme's filing numbers, given on every annexure, are
`NSE : NSE/LIST/51476` and `BSE : DCS/ESOP/IP/NB/3906/2025-26`, filed with NSE on 07-Nov-2025 and with BSE
on 15-Oct-2025 `[NSE ann 20-Jul-2026, 20260720_Allotment_of_Equity_Shares, p2]`.

### 2.2 Opening / additions / closing — the reconciliation

**Unit: number of equity shares.**

| Period | Opening | Additions (allotments in the period) | Closing per the SHP XBRL | Ties? |
|---|---|---|---|---|
| 19-Aug-2025 (listing) → 30-Sep-2025 | 151,320,372 | 0 | 151,320,372 | **TIES** |
| 01-Oct-2025 → 31-Dec-2025 | 151,320,372 | 0 | 151,320,372 | **TIES** |
| 01-Jan-2026 → 31-Mar-2026 | 151,320,372 | 123,069 + 295,857 + 65,494 + 426,573 = 910,993 | 152,231,365 | **TIES** — 151,320,372 + 910,993 = 152,231,365 |
| 01-Apr-2026 → 30-Jun-2026 | 152,231,365 | 129,573 + 40,843 = 170,416 | 152,401,781 | **TIES** — 152,231,365 + 170,416 = 152,401,781 |
| 01-Jul-2026 → 09-Sep-2026 (no SHP yet) | 152,401,781 | 4,853 + 342,766 + 29,305 = 376,924 | 152,778,705 *(per the 02-Sep-2026 allotment intimation, not yet per an SHP)* | **TIES** — 152,401,781 + 376,924 = 152,778,705 |

`TIE-OUT` — sum of the nine allotments = 123,069 + 295,857 + 65,494 + 426,573 + 129,573 + 40,843 + 4,853 +
342,766 + 29,305 = **1,458,333**, and 152,778,705 − 151,320,372 = **1,458,333**. The distinctive-number
ranges are contiguous with no gap from 151,320,373 to 152,778,705, so no allotment is missing from the
sequence. Recomputed independently. **The reconciliation ties at every date; nothing is marked DISAGREE
in this section.**

Dilution over the thirteen months, as arithmetic on the two ends of the series: 1,458,333 / 151,320,372 =
**0.964%** of the listing-date count. Stated here only because it is a two-operand tie-out of the table
above; no interpretation is offered.

### 2.3 The ESOP overhang as the XBRL reports it

**Unit: number of equity shares.**

| Field | 18-Aug-2025 | 30-Sep-2025 | 31-Dec-2025 | 31-Mar-2026 | 30-Jun-2026 |
|---|---|---|---|---|---|
| `NumberOfSharesUnderlyingOutstandingConvertibleSecuritiesWarrantsAndESOP` (whole company) | 7,567,272 | 7,567,272 | 7,567,272 | 6,433,865 | 6,522,593 |
| — of which held by the KMP named in Table III | 758,880 | 758,880 | 758,880 | 758,880 | 758,880 |
| — of which resident individuals up to Rs 2 lakh | 1,291,526 | 1,291,526 | 1,291,526 | 742,595 | 891,443 |
| — of which resident individuals above Rs 2 lakh | 5,516,866 | 5,516,866 | 5,516,866 | 4,932,390 | 4,872,270 |
| Fully diluted share count | 158,887,644 | 158,887,644 | 158,887,644 | 158,665,230 | 158,924,374 |

`TIE-OUT` at 30-Jun-2026: 758,880 + 891,443 + 4,872,270 = 6,522,593 ✓; 152,401,781 + 6,522,593 =
158,924,374 ✓. The outstanding-option figure is **unchanged across the first three filings at 7,567,272
despite no allotments in that window**, and falls to 6,433,865 at 31-Mar-2026 after 910,993 options were
exercised in the quarter — a fall of 1,133,407, which is **larger than the exercises by 222,414**
`[SHP 31Dec2025]` `[SHP 31Mar2026]`. The difference is not explained in the XBRL -> the ESOP disclosure in
the FY2026 annual report (options lapsed / forfeited / cancelled reconciliation) would answer it; that
document is `data/bronze/BLUESTONE-AR-FY2026.pdf` and is outside this agent's slice.

The same non-tie recurs in the next quarter, in the opposite direction: 6,433,865 opening + 209,319
granted on 16-Apr-2026 − 170,416 exercised in the quarter = 6,472,768, against the 6,522,593 reported at
30-Jun-2026 — **unexplained +49,825** `[SHP 31Mar2026]` `[SHP 30Jun2026]`
`[NSE ann 16-Apr-2026, 20260416_IntimationofGrantFinal, p1]`. Recomputed independently. Marked **DISAGREE**
between the option-movement implied by the allotment and grant intimations and the option balance the
shareholding pattern reports; both sides recorded, neither preferred.

**One grant, not an allotment, in the period:**

| Date | Action | Quantity | Exercise price | Vesting, verbatim | Filing |
|---|---|---|---|---|---|
| 16-Apr-2026 | Grant approved by the Nomination and Remuneration Committee | **209,319 options** | Rs. 1 per option | *"stock options granted to an employee shall vest over a total period of four (4) years from the date of grant. Twenty-five percent (25%) of the granted options shall vest upon completion of one (1) year from the grant date, and the remaining unvested options shall vest proportionately on a monthly basis i.e (on the date of Grant of each month) thereafter, until the completion of the four (4) year vesting period."* | `[NSE ann 16-Apr-2026, 20260416_IntimationofGrantFinal, p1-p2]` |

Same annexure, field 6, verbatim: *"All the option granted under the Bluestone Jewellery and Lifestyle
Limited - Employee Stock Option Plan 2014 shall vest not less than one year and not more than seven years
from the date of grant of such stock options. The Stock Options granted shall be capable of being
exercised within a period of ten years from the date of Vesting of the respective Stock Options."*
`[NSE ann 16-Apr-2026, 20260416_IntimationofGrantFinal, p2]`

**The identity of the grantee(s) of the 209,319 options is NOT DISCLOSED** — the intimation says only
*"granted to employee of the Company"* -> the ESOP disclosure under Regulation 14 of the SEBI (SBEB & SE)
Regulations in the FY2026 annual report and on the company website would name grants to KMP and to
employees receiving 1% or more of the issued capital.

---

## 3. The IPO proceeds record

### 3.0 The issue, as every Monitoring Agency Report states it

**Unit: Rs. crore, exactly as printed on the face of the MAR.**

| Field, verbatim | Value | Tag |
|---|---|---|
| Issue Period | August 11, 2025 to August 13, 2025 | `[MAR Q2FY26, p4]` |
| Type of issue | Public Issue (IPO) | `[MAR Q2FY26, p4]` |
| Type of specified securities | Equity Shares | `[MAR Q2FY26, p4]` |
| IPO Grading, if any | Not Applicable | `[MAR Q2FY26, p4]` |
| Issue size (in crore) | **Rs. 820.00 crore** | `[MAR Q2FY26, p4]` `[MAR Q3FY26, p4]` `[MAR Q4FY26, p4]` `[MAR Q1FY27, p4]` |
| Date of Raising Funds | 14th August, 2025 | `[SoD Q2FY26, p2]` |
| Amount Raised | Rs. 820 Crore | `[SoD Q2FY26, p2]` `[SoD Q3FY26, p2]` `[SoD Q4FY26, p2]` `[SoD Q1FY27, p2]` |
| Monitoring Agency | CARE Ratings Limited | all four MARs and all four SoDs |
| MA authorised signatory | Mr. Raunak Modi, Assistant Director | `[MAR Q2FY26, p3]` `[MAR Q3FY26, p3]` |

**Three stated objects, identical in all four reports, §4(i) "Cost of objects", "Revised Cost" blank and
"Comments of the Monitoring Agency: Nil" in every quarter:**

| Sr. | Item Head, verbatim | Original cost (as per the Offer Document), Rs. crore | Revised cost |
|---|---|---|---|
| 1 | Funding working capital requirements | 750.00 | — |
| 2 | General corporate purposes | 20.75 | — |
| 3 | Issue expenses | 49.25 | — |
| | **Total** | **820.00** | |

`[MAR Q2FY26, p5]` `[MAR Q3FY26, p5]` `[MAR Q4FY26, p5]` `[MAR Q1FY27, p6]`

**Certifier of the CA certificate the MA relies on — it changes after two quarters:**

| Quarter | Certifying firm | FRN | Certificate date | UDIN |
|---|---|---|---|---|
| Q2FY26 | **M S K A & Associates** (the statutory auditor) | 105047W | 02-Nov-2025 | 25159694BMLWKV2425 |
| Q3FY26 | **M/s. Sudit K. Parekh & Co. LLP** | 110512W/W100378 | 15-Jan-2026 | 26137489CYTZYO3877 |
| Q4FY26 | M/s. Sudit K. Parekh & Co. LLP | 110512W/W100378 | 14-Apr-2026 | 26137489PXPMYR3669 |
| Q1FY27 | M/s. Sudit K. Parekh & Co. LLP | 110512W/W100378 | 13-Jul-2026 | 26137489PPPBRT2168 |

`[MAR Q2FY26, p4-p5]` `[MAR Q3FY26, p5]` `[MAR Q4FY26, p5]` `[MAR Q1FY27, p6]`. **M/s. Sudit K. Parekh &
Co. LLP is the firm appointed the Company's internal auditor on 14-Jan-2026** (§6, event 3) — one day
before it signed its first certificate for the Monitoring Agency.

### 3.1 Object-wise utilisation, all four quarters, quarters as columns

**Unit: Rs. crore, as printed in MAR §4(ii) "Progress in the objects". Columns are the quarter the report
covers; each report's own "as at beginning of the quarter / during the quarter / at the end of the
quarter" split is preserved.**

| Object (Item Head, verbatim) | Field | Q2FY26 (30-Sep-2025) | Q3FY26 (31-Dec-2025) | Q4FY26 (31-Mar-2026) | Q1FY27 (30-Jun-2026) |
|---|---|---|---|---|---|
| **Funding working capital requirements** | Amount as proposed in the Offer Document | 750.00 | 750.00 | 750.00 | 750.00 |
| ↑ | utilised as at beginning of quarter | – | 190.65 | 525.65 | 725.65 |
| ↑ | utilised during the quarter | 190.65 | 335.00 | 200.00 | 24.25 |
| ↑ | utilised at end of quarter | 190.65 | 525.65 | 725.65 | 749.90 |
| ↑ | **Total unutilised amount** | **554.35** ⚠ | 224.35 | 24.35 | 0.10 |
| **General corporate purposes** | proposed | 20.75 | 20.75 | 20.75 | 20.75 |
| ↑ | beginning of quarter | – | – | 15.00 | 15.00 |
| ↑ | during the quarter | – | 15.00 | – | 5.75 |
| ↑ | end of quarter | – | 15.00 | 15.00 | 20.75 |
| ↑ | **Total unutilised** | 20.75 | 5.75 | 5.75 | – (nil) |
| **Issue expenses** | proposed | 49.25 | 49.25 | 49.25 | 49.25 |
| ↑ | beginning of quarter | – | – | 10.00 | 22.72 |
| ↑ | during the quarter | – | 10.00 | 12.72 | 0.06 |
| ↑ | end of quarter | – | 10.00 | 22.72 | 22.78 |
| ↑ | **Total unutilised** | 49.25 | 39.25 | 26.53 | 26.47 |
| **Total** | proposed | 820.00 | 820.00 | 820.00 | 820.00 |
| ↑ | beginning of quarter | – | 190.65 | 550.65 | 763.37 |
| ↑ | during the quarter | 190.65 | 360.00 | 212.72 | 30.06 |
| ↑ | end of quarter | 190.65 | 550.65 | 763.37 | 793.43 |
| ↑ | **Total unutilised** | **629.35** | 269.35 | 56.63 | 26.57 |

`[MAR Q2FY26, p5→p6]` `[MAR Q3FY26, p5→p6]` `[MAR Q4FY26, p6→p7]` `[MAR Q1FY27, p6-p7→p8]`

> ⚠ **DISAGREE inside the Q2FY26 report itself.** The "Funding working capital requirements" row prints
> **554.35** as its total unutilised amount. 750.00 − 190.65 = **559.35**, and 554.35 + 20.75 + 49.25 =
> **624.35**, against the Total row's **629.35** (which does tie: 820.00 − 190.65 = 629.35, and the §4(iii)
> deployment schedule also totals 629.35). **The row residual and the Total row cannot both be right; a
> Rs. 5.00 crore difference is unexplained.** This was **read off the PDF, not the text layer**, using
> layout-mode extraction, to eliminate the column-alignment artefact the document map warned of: the PDF
> prints `750.00 | - | 190.65 | 190.65 | 554.35` on one line `[MAR Q2FY26, p5]`. Recorded as printed. Not
> resolved here. Both figures carried forward.
>
> The other three quarters tie in every direction, recomputed independently:
> Q3FY26 750.00 − 525.65 = 224.35 ✓, 20.75 − 15.00 = 5.75 ✓, 49.25 − 10.00 = 39.25 ✓,
> 224.35 + 5.75 + 39.25 = 269.35 ✓, 820.00 − 550.65 = 269.35 ✓.
> Q4FY26 750.00 − 725.65 = 24.35 ✓, 49.25 − 22.72 = 26.53 ✓, 24.35 + 5.75 + 26.53 = 56.63 ✓,
> 820.00 − 763.37 = 56.63 ✓, 550.65 + 212.72 = 763.37 ✓.
> Q1FY27 750.00 − 749.90 = 0.10 ✓, 49.25 − 22.78 = 26.47 ✓, 0.10 + 0 + 26.47 = 26.57 ✓,
> 763.37 + 30.06 = 793.43 ✓, 820.00 − 793.43 = 26.57 ✓.

### 3.2 Where the unutilised money is parked — MAR §4(iii) "Deployment of unutilized proceeds"

**Unit: Rs. crore.**

| Instrument / account, verbatim | Q2FY26 (30-Sep-2025) | Q3FY26 (31-Dec-2025) | Q4FY26 (31-Mar-2026) | Q1FY27 (30-Jun-2026) |
|---|---|---|---|---|
| Fixed Deposits with **Axis Bank** | 505.00 (101 FDs × 5.00) | 125.00 (25 FDs × 5.00) | — | — |
| Fixed Deposits with **AU Small Finance Bank** | 100.00 (10 FDs × 10.00) | 100.00 (10 FDs × 10.00) | 50.00 (5 FDs × 10.00) | 20.00 (2 FDs × 10.00) |
| Fixed Deposit with **Yes Bank** | 5.00 (FD 2240301530480) | 25.00 (FD-002240301533120) | — | — |
| Balance in **Axis Bank Public Offer Account 925020034784826** | 19.35 | 19.35 | **6.63** | **6.57** |
| Balance in **Monitoring Account 925020037164142 with Axis Bank** | — | — | — | 0.00 |
| **Total** | **629.35** | **269.35** | **56.63** | **26.57** |
| Return on Investment (%) printed against the FDs | 6.10 / 6.37 / 5.90 (Axis), 7.05 (AU), 6.15 (Yes) | 6.37 (Axis), 7.05 (AU), 6.60 (Yes) | 7.05 (AU) | 7.05 (AU) |
| "Earning" column | `-` for every line | `-` | `-` | `-` |
| "Market Value as at the end of quarter" column | `-` for every line | `-` | `-` | `-` |

`[MAR Q2FY26, p6-p9]` `[MAR Q3FY26, p7-p8]` `[MAR Q4FY26, p7]` `[MAR Q1FY27, p8]`
`TIE-OUT` — Q2FY26: 505.00 + 100.00 + 5.00 + 19.35 = 629.35 ✓ (111 FD line items counted: 101 Axis + 10 AU).
Q3FY26: 125.00 + 100.00 + 25.00 + 19.35 = 269.35 ✓ (35 FD line items). Q4FY26: 50.00 + 6.63 = 56.63 ✓
(5 FD line items). Q1FY27: 20.00 + 6.57 + 0.00 = 26.57 ✓ (2 FD line items).

**Two footnotes the MA prints against the public-offer-account balance, verbatim:**
> Q4FY26: *"The public issue account has a total balance of Rs. 10.85 crore as on March 31, 2026, of which
> Rs. 6.63 crore pertains to IPO proceeds and the balance Rs. 4.42 crore pertains to OFS proceeds."*
> `[MAR Q4FY26, p7]`
>
> Q1FY27: *"The public issue account has a balance of Rs. 10.73 crore as on June 30, 2026, of which Rs.
> 6.57 crore pertains to IPO proceeds and the balance Rs. 4.26 crore pertains to OFS proceeds."* and
> *"The monitoring account has a total balance of Rs. 0.07 crore as on June 30, 2026, which pertains to
> balance transferred (between January 2026 to June 2026) form public issue account for TDS payable which
> pertains to OFS."* `[MAR Q1FY27, p8]`

> **ANOMALY, recorded not resolved — the Q2FY26 fixed-deposit maturity dates.** Of the 101 Axis Bank fixed
> deposits listed as holding IPO proceeds at 30-Sep-2025, **53 (Rs. 265.00 crore at Rs. 5.00 crore each)
> carry a printed maturity date of `28-02-2025`** — seven months *before* the quarter end and five and a
> half months *before* the funds were raised on 14-Aug-2025. Two further deposits print `28-02-2026`, ten
> print `27-11-2025` and thirty-six print `29-08-2026`. The 53 anomalous rows carry ROI 6.10%, the same as
> the two dated `28-02-2026`. Counted programmatically off the text layer and cross-checked against the
> PDF. `[MAR Q2FY26, p6-p9]`

### 3.3 Delay in implementation — MAR §4(iv). This is where the record turns

**Verbatim from the "Delay (no. of days/ months)" column.**

| Object | Completion date per offer document | Q2FY26 | Q3FY26 | **Q4FY26** | **Q1FY27** |
|---|---|---|---|---|---|
| Funding working capital requirements | March 31, 2026 | Actual "Ongoing"; delay **Not applicable** | Actual "Ongoing"; delay **Not applicable** | Actual "Ongoing"; **"Delay (exact number of days unascertainable)"** | Actual "Ongoing"; **"Delay (exact number of days unascertainable)"** |
| General corporate purposes | March 31, 2026 | "Ongoing"; **Not applicable** | "Ongoing"; **Not applicable** | "Ongoing"; **"Delay (exact number of days unascertainable)"** | Actual **"June 18, 2026"**; **"Delay (79 days)"** |
| Issue expenses | **Not specified** | Not applicable | Not applicable | Not applicable | Not applicable |

`[MAR Q2FY26, p9]` `[MAR Q3FY26, p8]` `[MAR Q4FY26, p8]` `[MAR Q1FY27, p9]`
Footnote on all four, verbatim: *"The letter of offer does not specify the timeline for utilization of
funds towards issue expenses."*

**The Q4FY26 note under §4(iv), verbatim in full:**
> *"The offer document stipulates the timeline for deployment of net proceeds as March 31, 2026. However,
> IPO proceeds of Rs. 56.63 crore remain unutilized as on March 31, 2026. The offer document further
> specifies that "In the event the estimated utilization of the net proceeds in a scheduled fiscal year is
> not completely met, due to reasons stated, the same shall be utilized in the next fiscal year, as may be
> determined by our Company, in accordance with applicable laws." **The MA has not received any supporting
> approvals for extension of timeline for deployment of net proceeds.**"* `[MAR Q4FY26, p8]`

**The Q1FY27 note under §4(iv), verbatim in full — same paragraph, with one sentence changed:**
> *"The offer document stipulates the timeline for deployment of net proceeds as March 31, 2026. However,
> IPO proceeds of Rs. 26.57 crore remain unutilized as on June 30, 2026. The offer document further
> specifies that "In the event the estimated utilization of the net proceeds in a scheduled fiscal year is
> not completely met, due to reasons stated, the same shall be utilized in the next fiscal year, as may be
> determined by our Company, in accordance with applicable laws." **The MA has received a board resolution
> dated April 23, 2026 for the extension of timeline to utilize the net proceeds till March 31, 2027.**"*
> `[MAR Q1FY27, p9]`

### 3.4 The monitoring agency's own comments and qualifications, verbatim, quarter by quarter

**MAR §3 "Details of the arrangement made to ensure the monitoring of issue proceeds" — the eight
standing questions.** Answers in the "Reply" column, MA comment quoted where it is not "Nil".

| Question, verbatim | Q2FY26 | Q3FY26 | Q4FY26 | Q1FY27 |
|---|---|---|---|---|
| **"Whether all utilization is as per the disclosures in the Offer Document?"** | **Yes** | **Yes** | **No** | **No** |
| "Whether shareholder approval has been obtained in case of material deviations from expenditures disclosed in the Offer Document?" | Not applicable | Not applicable | Not applicable | Not applicable |
| "Whether the means of finance for the disclosed objects of the issue have changed?" | No | No | No | No |
| **"Is there any major deviation observed over the earlier monitoring agency reports?"** | Not applicable | **No** | **Yes** | **Yes** |
| "Whether all Government/statutory approvals related to the object(s) have been obtained?" | Not applicable | Not applicable | Not applicable | Not applicable |
| "Whether all arrangements pertaining to technical assistance/collaboration are in operation?" | Not applicable | Not applicable | Not applicable | Not applicable |
| **"Are there any favorable/unfavorable events affecting the viability of these object(s)?"** | No | No | **Yes** | **Yes** |
| **"Is there any other relevant information that may materially affect the decision making of the investors?"** | **Yes** | **Yes** | **Yes** | **No** |

`[MAR Q2FY26, p4]` `[MAR Q3FY26, p4]` `[MAR Q4FY26, p4-p5]` `[MAR Q1FY27, p4-p5]`

**And the summary declaration on the face of each report, p3:**

| | Q2FY26 | Q3FY26 | Q4FY26 | Q1FY27 |
|---|---|---|---|---|
| "Deviation from the objects" | **No** | **No** | **Nil** | **Nil** |
| "Range of Deviation" | Not applicable | Not applicable | **Nil** | Not Applicable |

`[MAR Q2FY26, p3]` `[MAR Q3FY26, p3]` `[MAR Q4FY26, p3]` `[MAR Q1FY27, p3]`

**The MA's comments in full, in date order:**

**Q2FY26 (04-Nov-2025).**
> *"All funds utilized in Q2 FY26 are as per the disclosures in the offer document."* (utilisation question)
> *"This is the first monitoring agency report for the issue."* (major-deviation question)
> *"The company has reported net losses in the last three financial years (FY23: Rs. -167.24 crore, FY24:
> Rs. -142.24 crore, FY25: Rs. -219.21 crore). The net losses continued in Q1 FY26 at Rs. -34.75 crore."*
> (other relevant information) `[MAR Q2FY26, p4]`
>
> §4(ii) row comment, verbatim: *"During the quarter, the company has utilised Rs. 27.00 crore towards
> purchase of gold and diamonds. Additionally, fixed Deposits worth Rs. 161.93 crore were created and have
> been placed as margin with banks (Axis Bank and HDFC Bank) to avail metal gold loans and Rs. 1.72 crore
> has been placed as mark-to-market margin towards gold metal loans availed from banks. As per the offer
> document, the company also purchases gold bullion from the banks through metal gold loans for which it is
> required to placed fixed deposits as collateral."* `[MAR Q2FY26, p5]`
> — 27.00 + 161.93 + 1.72 = 190.65, which ties to the utilised-during-quarter figure. `TIE-OUT`

**Q3FY26 (22-Jan-2026).**
> *"All funds utilized in Q3 FY26 are as per the disclosures in the offer document. **The MA notes that the
> approval for objects for which the funds have been utilized under general corporate purposes in Q3 FY26
> has been provided post the incurring of expenses.**"* (utilisation question — answered "Yes")
> *"There are no deviations over the previous monitoring agency report."*
> *"The Company has reported net losses in the last three financial years, amounting to Rs. 167.24 crore in
> FY23, Rs. 142.24 crore in FY24, and Rs. 219.21 crore in FY25. The net losses continued in H1 FY26 at Rs.
> 82.00 crore."* `[MAR Q3FY26, p4]`
>
> §4(ii) working-capital row, verbatim: *"During the current quarter, the Company has utilized Rs. 14.02
> crore towards the purchase of gold and diamonds. Additionally, fixed deposits worth Rs. 290.00 crore were
> created and placed as margin with banks (HDFC Bank and Yes Bank) to avail Gold Metal Loans and Rs. 30.98
> crore has been placed as mark-to-market margin towards gold metal loans availed from banks. … The company
> has utilised a total of Rs. 451.93 crore till Dec 31, 2025 to provide FD margin for gold metal loans.
> **The company has transferred funds from MA account to current accounts for utilization of proceeds
> resulting in comingling of funds.**"* `[MAR Q3FY26, p5-p6]`
> — 14.02 + 290.00 + 30.98 = 335.00, ties to utilised-during-quarter. `TIE-OUT`. **The comingling sentence
> first appears here, in Q3FY26, one quarter earlier than the headline "No" answer changes.**
>
> §4(ii) GCP row, verbatim: *"During the current quarter, the company has utilised Rs. 11.00 crore towards
> payment to vendors for marketing services and Rs. 4.00 crore towards repayment of debt. As per the letter
> of offer, allocation or quantum of utilization of funds towards the specific purposes under general
> corporate purpose will be determined by the Board. The board has, vide resolution dated November 04,
> 2025, delegated the above authority to the management defined as CFO and MD, severally. The MA has
> received email confirmation from the CFO authorising the above payments. **However, the approval has been
> provided post the date of incurring of expenses.**"* `[MAR Q3FY26, p6]`
>
> §4(ii) issue-expenses row, verbatim: *"During Q3 FY26, the company has incurred Rs 3.92 crore as issue
> expenses for the fresh issue and another Rs 6.08 crore has been claimed as reimbursement for issue
> expenses incurred earlier."* `[MAR Q3FY26, p6]` — 3.92 + 6.08 = 10.00 `TIE-OUT`

**Q4FY26 (23-Apr-2026) — the report that turns.**
> Utilisation question, answered **"No"**, MA comment verbatim: *"The offer document stipulates the timeline
> for deployment of net proceeds as March 31, 2026. However, **gross IPO proceeds of Rs. 56.63 crore remain
> unutilized as on March 31, 2026. The MA has not received any supporting approvals for extension of
> timeline for deployment of net proceeds.** Refer to detailed note under point iv for more details.
> **The company has transferred funds from MA account to current accounts for utilization of proceeds
> resulting in comingling of funds.** The MA has verified the utilization of funds through bank statements
> and supporting documents."* `[MAR Q4FY26, p4]`
>
> **Comments of the Board of Directors** against that same question, verbatim: *"The Board of Directors of
> the Company has approved the utilization of the unutilized amount from the IPO proceeds in the financial
> year FY 2026–27. The Board has further approved that the unutilized portion of the share issue proceeds
> will be used for general corporate purposes."* `[MAR Q4FY26, p4]`
>
> Major-deviation question, answered **"Yes"**: *"The previous MA report dated January 22, 2026 did not
> specify any delay in implementation of the objects of issue. However, the current MA report specifies a
> delay in implementation of the objects of issue. Refer to Point iv for more details."* `[MAR Q4FY26, p5]`
>
> Viability question, answered **"Yes"**: *"There is a delay in utilization of net proceeds beyond the
> timeline of March 31, 2026 as stipulated in the offer document, which may affect the viability of the
> objects."* `[MAR Q4FY26, p5]`
>
> Other-relevant-information question, answered **"Yes"**: *"The Company has reported net losses amounting
> to Rs. 142.24 crore in FY24, and Rs. 219.21 crore in FY25. The net loss had reduced but stood at ₹18 crore
> in 9M FY26."* `[MAR Q4FY26, p5]`
>
> §4(ii) working-capital row, verbatim: *"During the quarter, the company has utilised ₹30 crore towards
> purchase of gold from vendors. Additionally, fixed deposits worth ₹170 crore were placed as margin with
> banks (HDFC Bank and Yes Bank) to avail Gold Metal Loans, including fixed deposits of ₹25 crore created in
> the previous quarter which were lien marked for gold metal loans in the current quarter. The company has
> transferred funds from MA account to current accounts for utilization of proceeds resulting in comingling
> of funds. The MA has verified the transactions from the bank statements. … The company has utilised a
> total of Rs. 621.93 crore till March 31, 2026 to provide FD margin for gold metal loans."*
> `[MAR Q4FY26, p6]` — 30 + 170 = 200.00, ties to utilised-during-quarter `TIE-OUT`; and
> 451.93 + 170.00 = 621.93 `TIE-OUT` against the Q3FY26 cumulative FD-margin figure.
>
> §4(ii) GCP row: *"The company has not utilised any proceeds towards general corporate purpose in Q4 FY26."*
> §4(ii) issue-expenses row: *"During Q4 FY26, the company has claimed Rs. 12.72 crore as issue expenses for
> the fresh issue. The payment has been made directly from the public issue account."* `[MAR Q4FY26, p6-p7]`
>
> §5 GCP detail table: **"Nil utilization during the quarter"** `[MAR Q4FY26, p8]`

**Q1FY27 (20-Jul-2026).**
> Utilisation question, answered **"No"**: *"All issue proceeds utilized in Q1 FY27 are towards the objects
> specified in the offer document. The offer document stipulates the timeline for deployment of net
> proceeds as March 31, 2026. However, IPO proceeds of Rs. 26.57 crore remain unutilized as on June 30,
> 2026. **The board has, vide resolution dated April 23, 2026, approved the extension of timeline for
> utilisation of balance net proceeds till March 31, 2027, which is in line with prospectus.** (Refer point
> iv for further details) The company has transferred funds from MA account to other bank accounts for
> utilization of proceeds resulting in comingling of funds. The MA has verified the utilization of funds
> through bank statements and supporting documents."* `[MAR Q1FY27, p4]`
>
> Major-deviation question, answered **"Yes"**: *"The previous monitoring agency report dated April 23,
> 2026 stated that the MA has not received any Board approval for the extension of timeline for utilisation
> of net proceeds. The MA has now received board resolution dated April 23, 2026 for the extension of
> timeline for utilisation of net proceeds till March 31, 2027 (Refer point iv for further details)"*
> `[MAR Q1FY27, p5]`
>
> Viability question, answered **"Yes"**, with the **Board's counter-comment in the adjacent column,
> verbatim**: *"To clarify, this does not affect the viability of the working capital objects — the
> unutilised amount currently stands at only Rs.0.10 cr. As stated elsewhere in this Report, as on June 30,
> 2026, Rs. 749.90 crore of the Rs. 750.00 crore (99.99%) earmarked for working capital objects has been
> utilised."* `[MAR Q1FY27, p5]` — the only quarter in which the Board writes anything other than
> "No Comments" against an MA comment, other than the Q4FY26 utilisation row.
>
> §4(ii) working-capital row: *"During the quarter, fixed deposits worth ₹23.25 crore were placed as margin
> with banks (Rs. 19 crore with Yes Bank and Rs. 4.25 crore with Axis Bank) to avail Gold Metal Loans.
> Additionally, the company has utilised ₹1.00 crore towards purchase of gold from vendors. … The company
> has utilised issue proceeds of Rs. 645.18 crore till June 30, 2026 to provide FD margin for gold metal
> loans."* `[MAR Q1FY27, p6-p7]` — 23.25 + 1.00 = 24.25 `TIE-OUT`; 621.93 + 23.25 = 645.18 `TIE-OUT`.
>
> §4(ii) GCP row and §5: *"During Q1 FY27, the company has utilised ₹5.75 crore towards repayment of
> non-convertible debentures bearing ISIN INE304W07092. The offer document specifies repayment of debt as
> one of the avenues for fund utilisation under general corporate purposes, subject to approval of the
> board. The board has, vide resolution dated November 04, 2025, authorised the MD and CFO to severally
> approve utilisation of funds under general corporate purposes. The MA has received email communication
> dated June 10, 2026 from the CFO confirming that the above utilisation was approved by them."*
> `[MAR Q1FY27, p7-p8]` `[MAR Q1FY27, p9]`. Sources named for the row include a *"No dues certificate from
> debenture trustee dated June 24, 2026"*.

### 3.5 The General Corporate Purposes sub-table — MAR §5, all four quarters

**Unit: Rs. crore.**

| Quarter | Item Head, verbatim | Amount | Approval trail as the MA describes it |
|---|---|---|---|
| Q2FY26 | "Not Applicable" | Not Applicable | Not Applicable |
| Q3FY26 | 1. Marketing services | 11.00 | Board resolution 04-Nov-2025 delegating to MD/CFO severally; CFO e-mail confirmation; *"the approval has been received post the date of incurring expenses"* |
| Q3FY26 | 2. Repayment of loan (*"repayment of a term loan from an NBFC"*) | 4.00 | same delegation; CFO e-mail; *"the approval has been received post the date of incurring expenses"* |
| Q3FY26 | **Total** | **15.00** | |
| Q4FY26 | — | **"Nil utilization during the quarter"** | |
| Q1FY27 | 1. Repayment of Borrowing (*"repayment of non-convertible debentures bearing ISIN INE304W07092"*) | 5.75 | Board resolution 04-Nov-2025; CFO e-mail 10-Jun-2026; no-dues certificate from debenture trustee 24-Jun-2026 |

`[MAR Q2FY26, p9]` `[MAR Q3FY26, p8-p9]` `[MAR Q4FY26, p8]` `[MAR Q1FY27, p9]`
`TIE-OUT` — GCP cumulative 15.00 + 5.75 = 20.75, the whole of the GCP object, fully spent by 18-Jun-2026.

**The offer-document GCP clause the MA reproduces under every §5, quoted here once, verbatim:**
> *"The Net Proceeds will first be utilized towards the Objects, which is ₹207.49 million as set out above.
> Subject to this, our Company intends to deploy any balance Net Proceeds towards general corporate
> purposes as approved by our management, from time to time, subject to such utilization for general
> corporate purposes not exceeding 25% of the gross proceeds of the Fresh Issue, in compliance with the
> SEBI ICDR Regulations. Our Board will have flexibility in utilizing the balance Net Proceeds towards
> general corporate purposes, including but not limited to setting-up of stores, repayment/prepayment of
> loans, strategic initiatives, partnership and joint ventures, acquiring fixed assets including furniture
> and fixtures, repayment of franchisee liability, meeting any expense of our Company, including
> administration, insurance, marketing, repairs and maintenance, payment of taxes and duties, meeting
> expenses incurred in the ordinary course of business and towards any exigencies, and any other purpose as
> may be approved by our Board in accordance with applicable laws. … In the event that we are unable to
> utilize the entire amount that we have currently estimated for use out of Net Proceeds in a Fiscal, we
> will utilize such unutilized amount in the next Fiscal."* `[MAR Q2FY26, p10]` `[MAR Q1FY27, p9-p10]`
> **Unit note: ₹207.49 million = Rs. 20.749 crore = the GCP object of Rs. 20.75 crore.** The Q4FY26 and
> Q1FY27 versions append one further sentence absent from the Q2FY26 and Q3FY26 versions: *"In case of
> variations in the actual utilization of funds designated for the purposes set forth above, increased fund
> requirements for a particular purpose may be financed by surplus funds or through our internal accruals,
> if any, which are not applied to the other purposes set out above."* `[MAR Q4FY26, p8]`

### 3.6 The four Statements of Deviation — the company's own declared answer, verbatim

All four are in the identical SEBI format. Every field is reproduced; the wording is identical in all four
except the quarter and the subject line.

| Field, verbatim | Q2FY26 | Q3FY26 | Q4FY26 | Q1FY27 |
|---|---|---|---|---|
| Filed | 04-Nov-2025 | 22-Jan-2026 | 23-Apr-2026 | 21-Jul-2026 |
| File stem | `20251104_Disclosureunder` | `20260122_StatementofDeviation` | `20260423_StatementofDeviation` | `20260721_BlueStone_Statement_of_Deviation_Q1_FY27` |
| "Mode of Fund Raising" | Public Issue – Initial Public Offer | same | same | same |
| "Date of Raising Funds" | 14th August, 2025 | same | same | same |
| "Amount Raised" | Rs. 820 Crore | same | same | same |
| "Report filed for Quarter ended" | 30th September, 2025 | 31st December, 2025 | 31st March, 2026 | 30th June, 2026 |
| "Monitoring Agency (Applicable/Not Applicable)" | Applicable | Applicable | Applicable | Applicable |
| "Monitoring Agency Name, if applicable" | CARE Ratings Limited. | same | same | same |
| **"Is there a deviation/ variation in use of funds raised?"** | **No** | **No** | **No** | **No** |
| "If yes, whether the same is pursuant to change in terms of a contract or objects, which was approved by the shareholders" | Not Applicable | Not Applicable | Not Applicable | Not Applicable |
| "If Yes, Date of shareholder Approval" | Not Applicable | Not Applicable | Not Applicable | Not Applicable |
| "Explanation for the Deviation/ Variation" | Not Applicable | Not Applicable | Not Applicable | Not Applicable |
| **"Comments of the Audit Committee after review"** | **Nil** | **Nil** | **Nil** | **Nil** |
| **"Comments of the auditors, if any"** | **Nil** | **Nil** | **Nil** | **Nil** |
| Object-wise deviation table (Original object / Modified object / Original allocation / Modified allocation / Funds utilised / Amount of deviation-variation / Remarks) | single entry: **"Not Applicable"** | **"Not Applicable"** | **"Not Applicable"** | **"Not Applicable"** |
| Cover letter signed by | Gaurav Singh Kushwaha, Managing Director, DIN 01674879 | same | same | same |
| Statement signed by | Rumit Dugar, Chief Financial Officer | same | same | same |

`[SoD Q2FY26, p2-p3]` `[SoD Q3FY26, p2-p3]` `[SoD Q4FY26, p2-p3]` `[SoD Q1FY27, p2-p3]`

**The cover-letter sentence, verbatim, identical in all four save the quarter:**
> *"Accordingly, pursuant to Regulation 32(1) of Securities and Exchange Board of India (Listing
> Obligations and Disclosure Requirements) Regulation, 2015, a Statement **confirming no deviation or
> variation** in the utilization of proceeds raised through issuance of equity shares by way of Initial
> Public offer ('IPO') for quarter ended <quarter> is enclosed herein, in the format as prescribed."*

**Locator defect, carried forward as found.** The Q3FY26 statement's cover-letter **subject line** reads
*"Statement of deviation(s) or variation(s) for the quarter ended **September 30, 2025**"* while the body
of the same page says *"for quarter ended December 31, 2025"* and the p2 table says *"Report filed for
Quarter ended 31st December, 2025"*. It is the Q3 statement `[SoD Q3FY26, p1-p2]`.

> **DISAGREE — same day, same board meeting, two documents, opposite postures.** On **23-Apr-2026** the
> company filed the Statement of Deviation answering *"Is there a deviation/ variation in use of funds
> raised? **No**"*, with *"Comments of the Audit Committee after review: **Nil**"* and *"Comments of the
> auditors, if any: **Nil**"* `[SoD Q4FY26, p2]`; and on the same day it filed the Monitoring Agency Report
> in which CARE Ratings answers *"Whether all utilization is as per the disclosures in the Offer Document?
> **No**"*, records that Rs. 56.63 crore remained unutilised past the 31-Mar-2026 deadline, that *"The MA
> has not received any supporting approvals for extension of timeline"*, that funds were comingled, and
> that both monitored objects are in *"Delay (exact number of days unascertainable)"* `[MAR Q4FY26, p4, p5,
> p8]`. **Both positions are on the record. Neither is preferred here, and neither may be silently dropped
> later (doctrine §10 contradiction-adjudication).**

### 3.7 What the IPO record does not disclose

- **The bifurcation of the Rs. 820 crore between fresh issue and offer for sale is NOT DISCLOSED in the
  Monitoring Agency Reports or the Statements of Deviation** — all eight documents treat "Rs. 820 crore"
  as a single number, while the NSE issue page describes the offer as *"Fresh Issue up to Rs. 8,200 million
  and offer for sale of up to 1,39,39,063 Equity Shares"* `[NSE IPO detail, issueInfo "Issue Size"]`. The
  Rs. 820.00 crore the MA monitors is therefore the **fresh issue**, and the OFS proceeds appear only as
  the Rs. 4.42 crore / Rs. 4.26 crore residues footnoted in §3.2 -> the Prospectus "Objects of the Offer"
  section carries the split; it is Tier-1 and outside this slice.
- **The rupee amount of the Rs. 56.63 crore Q4FY26 residue that was gross versus net of issue expenses**
  is stated one way in the MA comment (*"gross IPO proceeds of Rs. 56.63 crore"*, p4) and another in the
  §4(iv) note (*"IPO proceeds of Rs. 56.63 crore"*, p8). Same figure, two labels; recorded as printed.
- **The board resolution of 23-Apr-2026 extending the deployment timeline to 31-Mar-2027 is not itself in
  the corpus** — it is referred to in the Q1FY27 MAR and in the Q4FY26 Board comment, but no Regulation 30
  intimation of it appears among the 142 announcement rows -> the minutes of the 23-Apr-2026 board meeting
  would carry it; the 23-Apr-2026 outcome letter `20260423_DisclosureunderRegulation30_3` does not mention
  it in its item list.
- **The MA's disclaimer, in force on every one of the four reports, verbatim:** *"The Monitoring Agency
  (MA) does not perform an audit and undertakes no independent verification of any information/
  certifications/ statements it receives."* and *"There are certain sections of the report under the title
  'Comments of the Board of Directors', that shall be captured by the Issuer's Management / Audit Committee
  … These sections have not been reviewed by the MA, and the MA takes no responsibility for such comments
  of the issuer's Management/Board."* `[MAR Q2FY26, p3]`

