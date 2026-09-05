# Nationwide and the personal account used for business

**Document reference:** HND-CRA-007
**Version:** 0.3
**Author:** Saman Barati
**Date:** September 2026

| | |
|---|---|
| **Firm** | Nationwide Building Society |
| **Penalty** | £44,078,500 (reduced from £62,969,297) |
| **Date** | Final notice 11 December 2025, announced 12 December 2025 |
| **Relevant period** | 1 October 2016 to 1 July 2021 |
| **Source** | https://www.fca.org.uk/publication/final-notices/nationwide-building-society-2025.pdf |

## What happened

Nationwide did not keep due diligence and risk assessments up to date across its personal current
account book, and did not adequately monitor transactions. It knew customers were running business
activity through personal accounts in breach of its terms and had no process to manage the financial
crime risk that created.

One customer received **24 fraudulent Covid furlough payments** under the Job Retention Scheme. The
notice records the 24 payments as totalling **£1.35 million over thirteen months**, followed by a
further **£26.01 million over eight days** (2.17). HMRC seized £26.54 million; £820,687 was not
recovered.

## What the notice settles

- An entirely ordinary personal customer at onboarding: a current account, digital onboarding,
  electronic verification, income under £5,000 a month, nothing inconsistent on file.

## Where the readings differ

Very little is open here, and pushing what is open to its worst defensible level moves the score by
about a tenth of a point. Both readings are Low.

| Factor | Favourable reading | Adverse reading |
|---|---|---|
| D2 Identity verification method | Electronic, two sources (3) | **Electronic, one source (4)** |
| A2 Expected cash proportion of credits | Up to 10 percent (2) | **10 to 30 percent (3)** |
| A4 Expected counterparty profile | Employer and retail (1) | **Named businesses (2)** |

## What the model says

| | Favourable reading | Adverse reading |
|---|---|---|
| Weighted score | 1.4950 | 1.5975 |
| Rounded | 1.50 | 1.60 |
| Band from the arithmetic | Low | Low |
| Mandatory escalator | No | No |
| **Final rating** | **Low** | **Low** |

13 of the 20 factors are settled at level 1 by the notice itself and take that value in every reading. They carry **68.25% of the model's weight**. Even if every one of the remaining 7 factors were pushed to 5, this reconstruction could not score above **2.27**, and the High band begins at 3.50. Nothing this case file says about the arithmetic is a discovery; the ceiling was fixed before any judgement was made.

## What this teaches the model

1. **This is the right answer.** The lowest score in the back-test, on a customer who was, at
   onboarding, exactly what the file said. Nothing in a customer risk assessment could have predicted
   a fraud that had not happened yet against a scheme that did not yet exist.

2. **The failure is the refresh, not the rating.** The FCA's finding is that assessments were not kept
   up to date. This model produces a rating at onboarding and refreshes it on the cycle at methodology
   7.1, with event-driven triggers at 7.2. Trigger (d) — business activity on a personal account —
   exists in this project because of this notice.

3. **A back-test that only ever confirmed the model would be worthless.** This case is here because it
   is the one where the model is right and the interesting failure is somewhere else entirely.



---

*Reconstruction, not a finding.* This case file rebuilds a customer from what a published FCA notice
records. It is not a claim about what the firm's file actually contained, and it is not a criticism of
any individual. The purpose is to test a model, not to re-try a case.
