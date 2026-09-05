# Barclays Bank plc and Stunt & Co

**Document reference:** HND-CRA-007
**Version:** 0.3
**Author:** Saman Barati
**Date:** September 2026

| | |
|---|---|
| **Firm** | Barclays Bank Plc |
| **Penalty** | £39,314,700 (reduced from £56,163,900) |
| **Date** | Final notice 14 July 2025, announced 16 July 2025 |
| **Source** | https://www.fca.org.uk/publication/final-notices/barclays-bank-plc-2025.pdf |

## What happened

**Read this first.** Paragraph 2.7 of the Final Notice records that **on 4 March 2025 James Stunt was
acquitted** of money laundering charges in relation to monies received by Stunt & Co from Fowler
Oldfield, "on the basis that he had no knowledge or suspicion that those monies were criminal
property". Paragraph 4.138 records the same. The FCA's findings in this notice are about **Barclays'
controls**, and nothing in this case file should be read as saying anything else.

The notice records that Stunt & Co received **£46.8 million from Fowler Oldfield** in electronic
transfers between July 2015 and August 2016. The FCA found that Barclays did not gather enough
information at the start of the relationship and did not carry out proper ongoing monitoring.

The case is here for one narrow reason: the notice reproduces enough of the account opening file to
score it. A customer risk rating is a statement about the information on a file on a particular day,
made without knowing how anything turns out. This case makes that unusually clear, and the rating
below is a fact about a form, not about a person.

**This case file has been rebuilt.** The first version treated the relationship as an empty file, on the
reasoning that the FCA's finding was that Barclays had not asked enough questions, and scored every
unasked question at its benign level. That was wrong, and it was wrong in the direction that flattered
the model: the Final Notice records a good deal of what the application form actually said, and reading
it produces a different answer. The earlier version is in the version history below.

## What the notice settles

From the Final Notice of 14 July 2025:

| Paragraph | What the bank held |
|---|---|
| 4.12 | A single director and sole shareholder; the account opened on **16 January 2015** |
| 4.20(a) | The application recorded the business as **"Gold Refining & Trading"** |
| 4.20(b) | An opening investment of **£1,500,000**, paid in from the shareholder's own accounts |
| 4.20(c) | Anticipated turnover of **£500,000, manually amended to £3 million** |
| 4.20(d) | The company **"would not trade outside of the EU"** |
| 4.24 | At a meeting on **27 January 2015**, eleven days after opening: gold sourced from West Africa, principally Ghana and Burkina Faso, sold to high net worth individuals in the Middle East |
| 4.35 | Barclays **classified the customer as low risk**, with no recorded rationale |
| 4.37 | Adverse media checks were run on 15 January 2015; there is **no evidence the results were reviewed** |
| 2.7, 4.138 | The shareholder was **acquitted** of money laundering charges on 4 March 2025 |

## Where the readings differ

The two rows here are not a favourable and an adverse reading. They are the **same file on two dates**,
eleven days apart, and both are things the bank held. Nothing in either row uses information that
emerged later.

| Factor | 16 January 2015 | 27 January 2015 |
|---|---|---|
| G3 Expected counterparty or payment corridor countries | Unlisted countries (2) | **Weaker AML, unlisted (3)** |
| A3 Expected international proportion of value | 10 to 40 percent (3) | **Over 40 percent (4)** |
| A5 Plausibility of the declared profile | Unresolved (4) | **Not credible (5)** |

## What the model says

| | 16 January 2015 | 27 January 2015 |
|---|---|---|
| Weighted score | 2.1425 | 2.2875 |
| Rounded | 2.14 | 2.29 |
| Band from the arithmetic | Medium | Medium |
| Mandatory escalator | Yes | Yes |
| **Final rating** | **High** | **High** |

9 of the 20 factors are settled at level 1 by the notice itself and take that value in every reading. They carry **43.00% of the model's weight**. Even if every one of the remaining 11 factors were pushed to 5, this reconstruction could not score above **3.28**, and the High band begins at 3.50. Nothing this case file says about the arithmetic is a discovery; the ceiling was fixed before any judgement was made.

## What this teaches the model

1. **The application form was enough.** "Gold Refining & Trading" is a dealer in high-value goods on the
   wording of C3 level 5, which fires escalator 5.3(c). The model rates this customer **High on
   16 January 2015**, from the application form alone, with no hindsight and no adverse media. The FCA
   records that Barclays rated it low risk and did not write down why.

2. **The recommendation this project had already made would have removed that.** Step 5 recommends
   tying the high-value-dealer level to *registration* rather than to a description of the trade,
   because the description is what makes the Fowler Oldfield reading ambiguous. Stunt & Co declared no
   cash, so it would probably not have been a registered high value dealer. Applying the recommendation
   would have taken this customer from High to Medium. **A fix that resolves one case breaks another**,
   and the recommendation now carries that argument against it rather than being presented as an
   improvement.

3. **The £500,000 amended to £3 million is the sharpest fact in the notice and the model barely feels
   it.** A six-fold manual amendment with no recorded explanation is an unresolved inconsistency on the
   face of the file on day one. It is recorded at A5, which carries 1.5% of the model and moves the
   score by 0.045. Step 5 recommends moving A5 onto the escalator list; note that the recommendation as
   drafted catches only level 5, and on 16 January this file is at level 4. The recommendation would
   have caught it on 27 January and not before.

4. **Eleven days is not a rating cycle.** Between the two rows the customer's stated trading model went
   from "not outside the EU" to West Africa and the Middle East. The score moves from 2.14 to 2.29 and
   the rating does not move at all, because it was already High. Had the escalator not fired, nothing in
   this model would have re-rated the customer on the new information: a customer risk assessment is
   produced at onboarding and refreshed on a cycle, and the control that is supposed to react in
   eleven days is the event-driven review trigger at methodology 7.2, not the rating.

5. **"Screening was run but nobody read it" has no level.** C5 sits at level 1 in both rows because the
   notice does not record what the unreviewed results contained. The library has no level for a check
   that was performed and not reviewed, which is not the same as a clear result. That is a gap in the
   library, recorded at methodology 11.10.

### Version history of this case file

| Version | Change |
|---|---|
| 0.1 | Reconstructed as a thin file: C3 read as "general trade", A5 as consistent, turnover at the pre-amendment figure. Scored 1.70 and rated **Low**. |
| 0.2 | Rebuilt from the Final Notice after an external review pointed out that paragraphs 4.20, 4.24 and 4.35 record what the file said. C3 is a high-value dealer, A5 is unresolved, and the case is rated **High** on the day the account opened. The earlier version's conclusion — that the model cannot rate a file nobody filled in — was drawn from a file that had in fact been filled in, and has been withdrawn. The underlying gap is real and is now argued from the C5 point at 5 above rather than from this case as a whole. |

---

*Reconstruction, not a finding.* This case file rebuilds a customer from what a published FCA notice
records. It is not a claim about what the firm's file actually contained, and it is not a criticism of
any individual. The purpose is to test a model, not to re-try a case.
