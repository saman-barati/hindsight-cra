# -*- coding: utf-8 -*-
# Step 4: the Backtest sheet. Imported by build_model.py just before the workbook is saved.
#
# v0.2 (post-review). Two changes of substance.
#
# 1. Every case is now scored twice. The suffix -lo is the reading most favourable to
#    the customer that the published notice permits; -hi is the least favourable reading a
#    competent analyst could have defended on the information the notice records as held at
#    the time. Neither is "the answer". The pair is the answer, and the width of the pair is
#    the honest measure of how much of the earlier result was reconstruction rather than fact.
#    Where a factor is settled by the notice it takes the same value in both rows.
#    Two cases are dated or conditional pairs rather than favourable/adverse brackets, and are
#    labelled -a and -b instead of -lo and -hi: Stunt & Co (two dates) and Santander (the file as
#    recorded, and the file with the verification the FCA found was missing).
#
# 2. Stunt & Co is rebuilt from the Final Notice rather than treated as an empty file, and is
#    scored at two dates: the application file of 16 January 2015, and the same file eleven
#    days later after the meeting of 27 January 2015. See backtest/cases/barclays-stunt-and-co.md.

# The base reading for each case, then the deltas that produce the other rows.
_FO = {
 "C1": "UK company, natural owners", "C2": "One or two UBOs", "C3": "Cash-intensive trade",
 "C4": "No match", "C5": "No match", "G1": "United Kingdom", "G2": "UK tax residence only", "G3": "UK only",
 "P1": "Business account, basic", "P2": "Withdrawal only", "P3": "Not enabled", "P4": "Mandate, evidenced",
 "D1": "Branch", "D2": "Documents face to face", "D3": "Direct",
 "A1": "Over 25k, consistent", "A2": "No cash credits", "A3": "None",
 "A4": "Named businesses", "A5": "Consistent"}

# Santander UK, from the Final Notice of 8 December 2022:
#   4.52  the application form described the business as "Translation service", estimated annual
#         turnover £100,000 and expected monthly deposits to the account of £5,000
#   2.x   Customer A is the largest of six money service business customers, ~£269m of the ~£298m
#   4.x   Santander UK "failed to identify at the time of onboarding that Customer A operated an MSB"
# A1 is level 2, not level 1: £5,000 a month sits on the level 1 / level 2 boundary and methodology
# 4.5 sends a straddling figure to the higher level; £100,000 a year confirms it.
_SAN = {
 "C1": "UK company, natural owners", "C2": "One or two UBOs", "C3": "General trade",
 "C4": "No match", "C5": "No match", "G1": "United Kingdom", "G2": "UK tax residence only", "G3": "Unlisted countries",
 "P1": "Business account, basic", "P2": "Under 2k a month", "P3": "Enabled, unused", "P4": "Sole party",
 "D1": "Branch", "D2": "Documents face to face", "D3": "Direct",
 "A1": "5k to 25k, consistent", "A2": "Up to 10 percent", "A3": "Up to 10 percent",
 "A4": "Named businesses", "A5": "Consistent"}

# Stunt & Co, from the Final Notice of 16 July 2025:
#   4.12    Mr Stunt director and sole shareholder; account opened 16 January 2015
#   4.20(a) application records "Gold Refining & Trading"
#   4.20(b) GBP 1,500,000 opening investment paid in from various accounts of Mr Stunt
#   4.20(c) anticipated turnover of GBP 500,000, manually amended to GBP 3 million
#   4.20(d) the company "would not trade outside of the EU"
#   4.24    meeting of 27 January 2015: gold sourced from West Africa, principally Ghana and
#           Burkina Faso, sold to high net worth individuals in the Middle East
#   4.35    Barclays classified Stunt & Co as low risk with no recorded rationale
#   4.37    adverse media checks run 15 January 2015; no evidence the results were reviewed
_STU = {
 "C1": "UK company, natural owners", "C2": "One or two UBOs", "C3": "MSB, TCSP or HVD",
 "C4": "No match", "C5": "No match", "G1": "United Kingdom", "G2": "UK tax residence only", "G3": "Unlisted countries",
 "P1": "Business account, basic", "P2": "Withdrawal only", "P3": "Occasional payments", "P4": "Sole party",
 "D1": "Branch", "D2": "Documents face to face", "D3": "Direct",
 "A1": "Over 25k, consistent", "A2": "No cash credits", "A3": "10 to 40 percent",
 "A4": "Named businesses", "A5": "Unresolved"}

_WTK = {
 "C1": "UK company, natural owners", "C2": "One or two UBOs", "C3": "Regulated profession",
 "C4": "No match", "C5": "No match", "G1": "United Kingdom", "G2": "UK tax residence only", "G3": "UK only",
 "P1": "Business account, basic", "P2": "No cash facility", "P3": "Regular payments", "P4": "Mandate, evidenced",
 "D1": "Branch", "D2": "Documents face to face", "D3": "Direct",
 "A1": "Over 25k, consistent", "A2": "No cash credits", "A3": "Up to 10 percent",
 "A4": "Many individuals", "A5": "Consistent"}

_MON = {
 "C1": "Individual", "C2": "Natural person", "C3": "Employed or pension",
 "C4": "No match", "C5": "No match", "G1": "United Kingdom", "G2": "UK tax residence only", "G3": "UK only",
 "P1": "Current account, no overdraft", "P2": "Under 2k a month", "P3": "Enabled, unused", "P4": "Sole party",
 "D1": "Digital, own app", "D2": "Electronic, one source", "D3": "Direct",
 "A1": "Under 5k, consistent", "A2": "Up to 10 percent", "A3": "None",
 "A4": "Employer and retail", "A5": "Not credible"}

_NAT = {
 "C1": "Individual", "C2": "Natural person", "C3": "Employed or pension",
 "C4": "No match", "C5": "No match", "G1": "United Kingdom", "G2": "UK tax residence only", "G3": "UK only",
 "P1": "Current account with credit", "P2": "Under 2k a month", "P3": "Enabled, unused", "P4": "Sole party",
 "D1": "Digital, own app", "D2": "Electronic, two sources", "D3": "Direct",
 "A1": "Under 5k, consistent", "A2": "Up to 10 percent", "A3": "None",
 "A4": "Employer and retail", "A5": "Consistent"}


def _v(base, **delta):
    d = dict(base)
    d.update(delta)
    return d


BACKTEST = [
 # Fowler Oldfield. FO-lo and FO-mid hold the whole file constant and change one word in the
 # C3 definition, which is the finding. FO-hi adds the adverse reading of the open factors.
 ("FO-lo", "NatWest / Fowler Oldfield, favourable reading, cash-intensive trade", _FO),
 ("FO-mid", "NatWest / Fowler Oldfield, same file, high-value dealer reading",
  _v(_FO, C3="MSB, TCSP or HVD")),
 ("FO-hi", "NatWest / Fowler Oldfield, adverse reading of the open factors",
  _v(_FO, C3="MSB, TCSP or HVD", C2="Three to five UBOs", G3="Unlisted countries",
     P2="Under 2k a month", P3="Occasional payments", A3="Up to 10 percent", A4="Many individuals")),

 # Santander is a pair like Stunt & Co rather than a favourable/adverse bracket: SAN-a is the file
 # as the bank recorded it, SAN-b the same file with the one verification the FCA found was missing.
 ("SAN-a", "Santander UK / the translations company, the file as recorded", _SAN),
 ("SAN-b", "Santander UK / the translations company, with the business verified as an MSB",
  _v(_SAN, C3="MSB, TCSP or HVD", P3="Occasional payments", A3="10 to 40 percent",
     A4="Many individuals")),

 # Stunt & Co is dated rather than bracketed: both rows are things the bank held, eleven days apart.
 ("STU-a", "Barclays / Stunt & Co, the application file of 16 January 2015", _STU),
 ("STU-b", "Barclays / Stunt & Co, the same file after the meeting of 27 January 2015",
  _v(_STU, G3="Weaker AML, unlisted", A3="Over 40 percent", A5="Not credible")),

 ("WTK-lo", "Barclays / WealthTek, favourable reading", _WTK),
 ("WTK-hi", "Barclays / WealthTek, adverse reading",
  _v(_WTK, C2="Three to five UBOs", G3="Unlisted countries", D2="Certified copies",
     A3="10 to 40 percent")),

 ("MON-lo", "Monzo / the landmark address, favourable reading", _MON),
 ("MON-hi", "Monzo / the landmark address, adverse reading",
  _v(_MON, P1="Current account with credit", D2="Uncorroborated documents", A2="10 to 30 percent")),

 ("NAT-lo", "Nationwide / the personal account used for business, favourable reading", _NAT),
 ("NAT-hi", "Nationwide / the personal account used for business, adverse reading",
  _v(_NAT, D2="Electronic, one source", A2="10 to 30 percent", A4="Named businesses")),
]

# Which rows belong to which case, for the documents that report a range per case.
CASES = [
 ("FO",  "NatWest / Fowler Oldfield",                        ["FO-lo", "FO-mid", "FO-hi"]),
 ("SAN", "Santander UK / the translations company",          ["SAN-a", "SAN-b"]),
 ("STU", "Barclays / Stunt & Co",                            ["STU-a", "STU-b"]),
 ("WTK", "Barclays / WealthTek",                             ["WTK-lo", "WTK-hi"]),
 ("MON", "Monzo / the landmark address",                     ["MON-lo", "MON-hi"]),
 ("NAT", "Nationwide / the personal account used for business", ["NAT-lo", "NAT-hi"]),
]
