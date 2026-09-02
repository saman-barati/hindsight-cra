# Santander UK and the translations company

**Document reference:** HND-CRA-007
**Version:** 0.1
**Author:** Saman Barati
**Date:** September 2026

| | |
|---|---|
| **Firm** | Santander UK Plc |
| **Penalty** | £107,793,300 |
| **Date** | 9 December 2022 |
| **Relevant period** | 31 December 2012 to 18 October 2017 |
| **Source** | https://www.fca.org.uk/news/press-releases/fca-fines-santander-uk-repeated-anti-money-laundering-failures |

## What happened

A small translations company opened a business account and told the bank to expect around **£5,000 a month** in deposits. Within six months the account was receiving millions, which were moved on quickly to other accounts. The bank's own anti-money laundering team recommended closing the account in March 2014. It was closed in September 2015, **thirty months later**.

The FCA found Santander had ineffective systems to verify what customers told it, and did not compare what customers said would go through their accounts with what actually did. More than £298 million passed through problem business accounts.

## The customer at onboarding

| Factor | Level recorded | Score |
|---|---|---|
| C1 Legal form | UK company, natural owners | 3 |
| C3 Industry or occupation | General trade | 3 |
| G3 Payment corridor | Unlisted countries | 2 |
| P1 Product | Business account, basic | 4 |
| P2 Cash functionality | Under 2k a month | 3 |
| A1 Turnover | Under 5k, consistent | 1 |
| A5 Plausibility | Consistent | 1 |

Nothing here is a red flag. A small translations business expecting £5,000 a month is an ordinary customer, and on the day it was onboarded it looked like one.

## What the model says

| | |
|---|---|
| Weighted score | **1.8875** |
| Band from the arithmetic | Low |
| Mandatory escalator | No |
| **Final rating** | **Low** |

## What this teaches the model

1. **The model is right here, and that is the point.** There was nothing at onboarding to catch. Rating this customer Low was the correct answer on the information available.

2. **The failure was the comparison nobody made.** £5,000 declared against millions received is not a scoring problem, it is a monitoring problem — and specifically review trigger 7.2(e), activity materially inconsistent with the expected activity recorded at onboarding.

3. **It shows what the declared-activity factors are actually for.** A1 and A2 are close to worthless as predictors on day one. Their value is as a **baseline to be tested later**. That reframes methodology 11.3: expected activity should perhaps carry no weight at onboarding and considerable weight at the first refresh, when there is something real to compare it against.

4. **Thirty months is the number that should be remembered.** The control that eventually worked, an internal recommendation to exit, was not the model. No risk rating fixes a thirty-month gap between a decision and an action.

---

*Reconstruction, not a finding.* This case file rebuilds a customer from what a published FCA notice records. It is not a claim about what the firm's file actually contained, and it is not a criticism of any individual. The purpose is to test a model, not to re-try a case.
