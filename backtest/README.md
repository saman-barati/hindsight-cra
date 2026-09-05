# Step 4 — the back-test

**Document reference:** HND-CRA-007
**Version:** 0.2
**Author:** Saman Barati
**Date:** September 2026

## The question

Every risk model can be checked for internal consistency. Very few are checked against customers who
are already known to have caused harm. This step takes six customers named in published FCA
enforcement notices, rebuilds each of them as they looked **on the day the bank took them on**, and
runs them through the same library, weights and rules as the 400 synthetic customers.

The six cases carry roughly £480 million of penalties between them. Three things about that number, because it
is the one most likely to be quoted back.

It is arithmetic on the published figures and nothing more: £264,772,619.95 + £107,793,300 +
£44,078,500 + £39,314,700 + £21,091,300 + £3,093,600 = £480,144,019.95.

Those penalties were imposed for control failures across whole customer books over periods of years —
not for these six accounts, and in no case was a single customer the cause of a fine. The customers
are used here because the published material describes them in enough detail to rebuild, which is a
different thing from blaming them for the total.

And the total mixes two kinds of thing. Five are regulatory penalties imposed by the FCA under section
206 of FSMA and set out in final notices. The NatWest figure is a **criminal fine imposed by Southwark
Crown Court** following an FCA prosecution under the Money Laundering Regulations 2007; there is no
final notice for it. Adding them is fair as a measure of scale and wrong as a measure of anything else.

## Ranges, not point estimates

A reconstruction from a published notice involves twenty judgement calls, and the notice settles far
fewer than twenty of them. The first version of this back-test made those calls once and reported a
single score, which gave the reconstruction an authority it had not earned. Every case is now scored
at least twice:

- **the favourable reading** — every factor the notice leaves open, read the way most favourable to the customer;
- **the adverse reading** — every open factor at the worst level a competent analyst could have defended on the same information.

Neither is the answer. The pair is, and the width of the pair is the honest measure of how much of the
result is reconstruction rather than fact. Where the notice settles a factor, both readings carry the
same level. Stunt & Co is the exception: its two rows are not readings but **dates**, eleven days apart.

## The six cases

| Case | Notice | Score range | Ceiling | Final rating |
|---|---|---|---|---|
| [FO](cases/natwest-fowler-oldfield.md) | NatWest, £264.8m, criminal fine, Dec 2021 | 1.82 – 2.26 | 3.34 | Low to High |
| [SAN](cases/santander-translations-company.md) | Santander UK Plc, £107.8m, Dec 2022 | 1.89 – 2.11 | 3.37 | Low to Medium |
| [STU](cases/barclays-stunt-and-co.md) | Barclays Bank Plc, £39.3m, Jul 2025 | 2.14 – 2.29 | 3.28 | High |
| [WTK](cases/barclays-wealthtek.md) | Barclays Bank UK Plc, £3.1m, Jul 2025 | 1.83 – 2.05 | 3.28 | Low to Medium |
| [MON](cases/monzo-landmark-address.md) | Monzo Bank Ltd, £21.1m, Jul 2025 | 1.52 – 1.67 | 2.24 | Low |
| [NAT](cases/nationwide-business-on-personal.md) | Nationwide Building Society, £44.1m, Dec 2025 | 1.50 – 1.60 | 2.27 | Low |

"Ceiling" is the highest score this reconstruction could reach if every factor the notice does not
settle were pushed to 5.

## What the back-test can and cannot show

**It cannot show that these customers should have scored High on the arithmetic.** Read the ceiling
column. The highest ceiling of any of the six is **3.37**, and the High band begins at 3.50. The
facts the notices settle — a UK company, a UK address, branch onboarding, face-to-face documents —
pin between 41% and 69% of the model's weight at level 1 before a single judgement is made. A test
whose answer is fixed by its inputs is not a test. **The finding that no reconstruction reaches the
High band on the arithmetic was guaranteed before the exercise began**, and every conclusion below is
written in that knowledge.

**It can show three things the ceiling does not decide.**

1. Whether a **mandatory escalator** fires. That is a yes/no condition on individual levels and is not
   subject to the ceiling at all.
2. How far apart the favourable and adverse readings sit, which measures how much the model's answer
   depends on the analyst rather than on the file.
3. Whether the **rating changes as the file changes**, which is what the Stunt & Co pair tests.

## What it found

### 1. One case is caught, and only by an escalator

Two of the six cases reaches High in any reading, and it does so through escalator 5.3(c) rather than
through its score. **Not one reconstruction, in any reading, reaches the High band on the arithmetic**
— though for the reasons above, none of them could have.

Stunt & Co scores 2.14 on the application file of 16 January 2015 and is rated High from that day,
because the application records the business as gold refining and trading and level 5 of factor C3
covers a dealer in high-value goods. That is the same level definition the project had already
recommended narrowing, on the ground that it is written as a description of a trade rather than as a
registration status. **The recommendation would have removed the only control that caught this
customer.** It stays in Step 5 as a recommendation, now with that argument recorded against it.

### 2. One word still decides the most serious case

`FO-lo` and `FO-mid` are the same twenty-factor file. They differ in one reading of one factor: whether
a Bradford jewellery business is a *cash-intensive trade* or a *dealer in high-value goods*.

| Factor | Cash-intensive reading | High-value dealer reading |
|---|---|---|
| C3 Industry or occupation | Cash-intensive trade (4) | **MSB, TCSP or HVD (5)** |

C3 carries 7.5% of the model, so one level of difference moves the score by exactly 0.075 — from
1.82 to 1.90. Neither crosses a band boundary. The rating changes anyway, because level 5 fires
escalator 5.3(c) and level 4 does not. The score is not what decides this case; a definition is.

### 3. The declared profile is the model's blind spot, in both directions

Fowler Oldfield declared no cash and the model scored what was declared: A2 stays at level 1 in every
reading, because nothing at onboarding contradicted it. Around £264 million in cash followed. A model
that scores declarations cannot catch a customer who lies at onboarding, and no weighting fixes that.

Stunt & Co is the mirror image. Its application form carried an anticipated turnover of £500,000
manually amended to £3 million, with no recorded explanation — an inconsistency **on the face of the
file on day one**. The model has a factor for exactly this (A5, plausibility) and gives it 1.5% of the
weight. It moves the score by 0.045.

### 4. Two of the six were never onboarding failures

Santander's translations company and Nationwide's personal customer look ordinary on day one in every
reading, and are rated correctly. What failed was everything afterwards: nobody compared £5,000
declared with millions received, and nobody noticed a business trading through a personal account. A
customer risk rating is not supposed to catch those. The event-driven review triggers at methodology
7.2 are — including trigger (d), which exists in this project because of the Nationwide notice.

### 5. The width of the range is itself a result

The gap between the favourable and adverse readings runs from 0.10 points to 0.44 points across the
six cases. On a scale where the whole synthetic population spans 1.19 to 2.76, a reconstruction spread
of that size means the analyst's reading of an incomplete file moves a customer about as far as most
real differences between customers do.

## Where the reconstructions come from

Every level recorded in the `Backtest` sheet traces to one of these, and nothing else:

| Case | Primary source |
|---|---|
| Fowler Oldfield | [FCA press release](https://www.fca.org.uk/news/press-releases/natwest-fined-264.8million-anti-money-laundering-failures) and the [agreed statement of facts](https://www.fca.org.uk/publication/corporate/agreed-statement-facts-fca-national-westminster-bank.pdf) |
| Santander | [Final notice, 9 December 2022](https://www.fca.org.uk/publication/final-notices/santander-uk-plc-2022.pdf) |
| Stunt & Co | [Barclays Bank Plc final notice, 14 July 2025](https://www.fca.org.uk/publication/final-notices/barclays-bank-plc-2025.pdf) |
| WealthTek | [Barclays Bank UK Plc final notice, 14 July 2025](https://www.fca.org.uk/publication/final-notices/barclays-bank-uk-plc-2025.pdf) |
| Monzo | [Final notice, 8 July 2025](https://www.fca.org.uk/publication/final-notices/monzo-bank-limited.pdf) |
| Nationwide | [Final notice, 11 December 2025](https://www.fca.org.uk/publication/final-notices/nationwide-building-society-2025.pdf) |

Note that the two Barclays matters are **two entities and two separate final notices**: Barclays Bank
Plc for Stunt & Co, Barclays Bank UK Plc for WealthTek. They are announced together in one press
release, which is where the "£42 million" headline figure comes from, and citing one notice for both
is a mistake this project made in an earlier version.

## Reading the workbook

The `Backtest` sheet of `model/customer-risk-model.xlsx` carries all 13 rows: the recorded level for
each of the twenty factors, the score each resolves to, the weighted result, the band, the escalator
test and the final rating. The four integrity checks covering the back-test are on the `Checks` sheet.

## The case files

- [NatWest / Fowler Oldfield](cases/natwest-fowler-oldfield.md) — NatWest, £264.8m, criminal fine, Dec 2021
- [Santander UK / the translations company](cases/santander-translations-company.md) — Santander UK Plc, £107.8m, Dec 2022
- [Barclays / Stunt & Co](cases/barclays-stunt-and-co.md) — Barclays Bank Plc, £39.3m, Jul 2025
- [Barclays / WealthTek](cases/barclays-wealthtek.md) — Barclays Bank UK Plc, £3.1m, Jul 2025
- [Monzo / the landmark address](cases/monzo-landmark-address.md) — Monzo Bank Ltd, £21.1m, Jul 2025
- [Nationwide / the personal account used for business](cases/nationwide-business-on-personal.md) — Nationwide Building Society, £44.1m, Dec 2025

---

*Reconstructions, not findings.* These files rebuild customers from published FCA notices. They are
not claims about what any firm's file actually contained, and not criticism of any individual.
