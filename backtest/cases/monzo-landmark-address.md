# Monzo and the landmark address

**Document reference:** HND-CRA-007
**Version:** 0.1
**Author:** Saman Barati
**Date:** September 2026

| | |
|---|---|
| **Firm** | Monzo Bank Ltd |
| **Penalty** | £21,091,300 (reduced from £30,130,475) |
| **Date** | July 2025 |
| **Relevant period** | October 2018 to August 2020, with further breaches to June 2022 |
| **Source** | https://www.fca.org.uk/news/press-releases/fca-fines-monzo-21m-failings-financial-crime-controls |

## What happened

Monzo onboarded customers on the basis of limited and, in some cases, **obviously implausible information — including customers who gave well known London landmarks as their home address**. Its customer risk assessment did not keep pace as the customer base grew roughly tenfold. After the FCA restricted it from opening accounts for high-risk customers in August 2020, it onboarded more than 34,000 of them anyway.

## The customer at onboarding

A personal customer, digitally onboarded, whose stated address is a famous building.

| Factor | Level recorded | Score |
|---|---|---|
| C1 Legal form | Individual | 1 |
| C3 Occupation | Employed or pension | 1 |
| P1 Product | Current account, no overdraft | 2 |
| D1 Onboarding channel | Digital, own app | 3 |
| D2 Identity verification | Electronic, one source | 4 |
| A2 Expected cash | Up to 10 percent | 2 |
| **A5 Plausibility** | **Not credible** | **5** |

A5 level 5 in the library reads: *the declared profile is not credible on the information held, including an address that is a landmark or a non-residential building.* That wording was written from this case, in Step 2, before any of it was scored.

## What the model says

| | |
|---|---|
| Delivery channel category | 2.95 |
| Expected activity category | 1.70 |
| Weighted score | **1.5200** |
| Band from the arithmetic | Low |
| Mandatory escalator | No |
| **Final rating** | **Low** |

## What this teaches the model

1. **I built the right factor and then gave it 1.5% of the model.** A5 carries 10% of a category that itself carries 15%. Scoring the maximum on it moves the overall score by 0.06. A customer whose address is Buckingham Palace is rated Low.

2. **The Step 2 rationale for that weight now reads badly, and it should stay in the repository.** I wrote that A5 was "deliberately given the smallest weight and the widest definition" so an analyst had somewhere to record something that did not add up. The reasoning was sound and the number was wrong. Leaving both the reasoning and the result visible is the point of the exercise.

3. **Some facts should not be scored at all.** An address that cannot be true is not a small increase in risk; it is a failure to identify the customer, which regulation 31 already treats as a reason to stop. Step 5 should move A5 level 5 out of the weighted average and onto the prohibited or escalator list, where a single fact can decide the outcome on its own.

---

*Reconstruction, not a finding.* This case file rebuilds a customer from what a published FCA notice records. It is not a claim about what the firm's file actually contained, and it is not a criticism of any individual. The purpose is to test a model, not to re-try a case.
