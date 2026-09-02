# Nationwide and the personal account used for business

**Document reference:** HND-CRA-007
**Version:** 0.1
**Author:** Saman Barati
**Date:** September 2026

| | |
|---|---|
| **Firm** | Nationwide Building Society |
| **Penalty** | £44,078,500 (reduced from £62,969,297) |
| **Date** | December 2025 |
| **Relevant period** | October 2016 to July 2021 |
| **Source** | https://www.fca.org.uk/news/press-releases/fca-fines-nationwide-44m-failings-financial-crime-controls |

## What happened

Nationwide did not keep due diligence and risk assessments up to date across its personal current account book, and did not adequately monitor transactions. It knew customers were running business activity through personal accounts in breach of its terms and had no process to manage the financial crime risk that created.

One customer received **24 fraudulent Covid furlough payments totalling £27.3 million**. HMRC recovered £26.5 million; around £800,000 was not recovered.

## The customer at onboarding

An entirely ordinary personal customer.

| Factor | Level recorded | Score |
|---|---|---|
| C1 Legal form | Individual | 1 |
| C3 Occupation | Employed or pension | 1 |
| P1 Product | Current account with credit | 3 |
| D1 Onboarding channel | Digital, own app | 3 |
| D2 Identity verification | Electronic, two sources | 3 |
| A1 Turnover | Under 5k, consistent | 1 |
| A5 Plausibility | Consistent | 1 |

## What the model says

| | |
|---|---|
| Weighted score | **1.4950** |
| Band from the arithmetic | Low |
| Mandatory escalator | No |
| **Final rating** | **Low** |

The lowest score in the back-test, and the right answer.

## What this teaches the model

1. **This case is why review trigger 7.2(d) exists.** Methodology 7.2(d) fires a re-rating when business activity is identified on a personal account. It was written into the Step 1 methodology on the basis of this notice, before any scoring was done. The back-test confirms the reason: nothing at onboarding could have found this customer, so the control has to be a trigger.

2. **A Low rating is not a clean bill of health.** Methodology 10.1 says so in one line. This is the case that gives that line its meaning: the customer was correctly Low and went on to receive £27.3 million of fraudulent payments.

3. **It sets the boundary of what Step 5 should try to fix.** Two of the six cases in this back-test are monitoring failures, not rating failures. Reweighting the model would not have caught either. The right response is to leave them alone and be clear about which control owns which risk.

---

*Reconstruction, not a finding.* This case file rebuilds a customer from what a published FCA notice records. It is not a claim about what the firm's file actually contained, and it is not a criticism of any individual. The purpose is to test a model, not to re-try a case.
