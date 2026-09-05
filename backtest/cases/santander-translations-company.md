# Santander UK and the translations company

**Document reference:** HND-CRA-007
**Version:** 0.3
**Author:** Saman Barati
**Date:** September 2026

| | |
|---|---|
| **Firm** | Santander UK Plc |
| **Penalty** | £107,793,300 |
| **Date** | Final notice 8 December 2022 |
| **Source** | https://www.fca.org.uk/publication/final-notices/santander-uk-plc-2022.pdf |

## What happened

A business opened a Santander account on an application form describing its trade as a "Translation
service", with estimated annual turnover of **£100,000** and expected monthly deposits of **£5,000**
(4.52). Within six months the account was receiving millions, swiftly transferred on to separate
accounts. The bank's own anti-money laundering team recommended closing the account in March 2014, the
decision to close was taken in April 2015, and the account was not closed until September 2015 —
**eighteen months** after the recommendation.

Two things in the notice matter more than that story, and an earlier version of this case file missed
both.

**The customer operated a money service business, and Santander did not identify it as one at
onboarding.** The FCA's finding is that the firm failed to verify the nature of the business. That is
not a monitoring failure a rating could never have reached. It is a failure of the input the rating
depends on.

**And this is the large customer.** Roughly £298 million passed through the accounts of six money
service business customers; about **£269 million of it through this one**.

## What the notice settles

- A UK company, a business account, an application form reading "Translation service", estimated
  annual turnover of £100,000 and expected monthly deposits of £5,000 (4.52).
- **The customer operated a money service business**, which the notice records was not identified at
  onboarding.
- A1 is scored at level 2, not level 1. £5,000 a month sits exactly on the level 1 / level 2 boundary
  and methodology 4.5 sends a straddling figure to the higher level; £100,000 a year confirms it.

## Where the readings differ

This pair is not a favourable and an adverse reading. `SAN-a` is the file as Santander recorded it,
with the trade taken from the application form. `SAN-b` is the same file with the one verification the
notice says was missing: the business identified as a money service business, which is level 5 of
factor C3. Three other factors move with it, because a money service business sending occasional
international payments is a different profile from a translation agency.

| Factor | Favourable reading | Adverse reading |
|---|---|---|
| C3 Industry or occupation | General trade (3) | **MSB, TCSP or HVD (5)** |
| P3 International payment functionality | Enabled, unused (2) | **Occasional payments (3)** |
| A3 Expected international proportion of value | Up to 10 percent (2) | **10 to 40 percent (3)** |
| A4 Expected counterparty profile | Named businesses (2) | **Many individuals (3)** |

## What the model says

| | Favourable reading | Adverse reading |
|---|---|---|
| Weighted score | 1.9250 | 2.1775 |
| Rounded | 1.93 | 2.18 |
| Band from the arithmetic | Low | Medium |
| Mandatory escalator | No | Yes |
| **Final rating** | **Low** | **High** |

9 of the 20 factors are settled at level 1 by the notice itself and take that value in every reading. They carry **40.00% of the model's weight**. Even if every one of the remaining 11 factors were pushed to 5, this reconstruction could not score above **3.40**, and the High band begins at 3.50. Nothing this case file says about the arithmetic is a discovery; the ceiling was fixed before any judgement was made.

## What this teaches the model

1. **The model had the control. The file did not have the input.** Verified as a money service
   business the customer is rated **High** on day one, through escalator 5.3(c). Taken from the
   application form at face value it is rated **Low**. The gap between those two rows is not a modelling
   choice or a matter of judgement; it is one verification step that the notice says was not carried
   out.

2. **A risk model is only ever as good as the due diligence feeding it.** This project spends five
   documents arguing about weights, bands and aggregation rules. On a file where the trade has not been
   verified, none of it matters: the model faithfully scores what it is given. Recorded at methodology
   11.15, and it is the single most useful thing the back-test produced.

3. **An earlier version of this case file said the opposite**, and said it confidently: that the
   customer was rated correctly, that this was purely a monitoring failure, and that no customer risk
   rating could reach that far. That was written from the press release and the narrative rather than
   from the notice. It is the same mistake this project already made once with Stunt & Co, caught the
   second time by a pre-publication review rather than by me. It has been withdrawn; see the version
   history below.

4. **The second half of the failure stands.** The declared £5,000 a month sits at A1 and nothing in the
   model ever compares it with what the account received. That comparison belongs to transaction
   monitoring and to the event-driven review triggers at methodology 7.2. The eighteen months between an
   internal recommendation to close and the closure belong to neither.

### Version history of this case file

| Version | Change |
|---|---|
| 0.2 | Reconstructed from the press release: a translation agency expecting £5,000 a month, scored Low, and concluded that the model was right and the failure was entirely in monitoring. |
| 0.3 | Rebuilt from the Final Notice after a pre-publication review. The notice records the customer as a money service business that was not identified as one at onboarding, and as the ~£269m account. The favourable/adverse pair is replaced with a recorded/verified pair, A1 corrected from level 1 to level 2, and the conclusion reversed: verified, this customer is High on day one. |

---

*Reconstruction, not a finding.* This case file rebuilds a customer from what a published FCA notice
records. It is not a claim about what the firm's file actually contained, and it is not a criticism of
any individual. The purpose is to test a model, not to re-try a case.
