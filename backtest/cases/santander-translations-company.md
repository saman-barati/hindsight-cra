# Santander UK and the translations company

**Document reference:** HND-CRA-007
**Version:** 0.2
**Author:** Saman Barati
**Date:** September 2026

| | |
|---|---|
| **Firm** | Santander UK Plc |
| **Firm** | Santander UK Plc |
| **Penalty** | £107,793,300 |
| **Date** | Final notice 9 December 2022 |
| **Source** | https://www.fca.org.uk/news/press-releases/fca-fines-santander-uk-repeated-anti-money-laundering-failures |

## What happened

A small translations company opened a business account and told the bank to expect around **£5,000 a
month** in deposits. Within six months the account was receiving millions, which were swiftly
transferred on to separate accounts. The bank's own anti-money laundering team recommended closing the
account in March 2014, the decision to close was taken in April 2015, and the account was not closed
until September 2015 — **eighteen months** after the recommendation.

The FCA found Santander had ineffective systems to verify what customers told it, and did not compare
what customers said would go through their accounts with what actually did. More than £298 million
passed through the accounts of six Money Service Business customers before they were closed, roughly
£269 million of it through a single customer.

## What the notice settles

- A UK company, a business account, and a declared expectation of about £5,000 a month.
- Nothing in the notice suggests anything unusual was recorded at onboarding. That is the point of the
  case: on day one this was an ordinary customer, and it was rated as one.

## Where the readings differ

The notice says almost nothing about ownership, counterparties or payment corridors, so the open
factors here are numerous and the range is correspondingly meaningful.

| Factor | Favourable reading | Adverse reading |
|---|---|---|
| C2 Ownership and control structure | One or two UBOs (2) | **Three to five UBOs (3)** |
| P3 International payment functionality | Enabled, unused (2) | **Occasional payments (3)** |
| P4 Third-party access to the account | Sole party (1) | **Mandate, evidenced (3)** |
| A3 Expected international proportion of value | Up to 10 percent (2) | **10 to 40 percent (3)** |
| A4 Expected counterparty profile | Named businesses (2) | **Many individuals (3)** |

## What the model says

| | Favourable reading | Adverse reading |
|---|---|---|
| Weighted score | 1.8875 | 2.1100 |
| Rounded | 1.89 | 2.11 |
| Band from the arithmetic | Low | Medium |
| Mandatory escalator | No | No |
| **Final rating** | **Low** | **Medium** |

9 of the 20 factors are settled at level 1 by the notice itself and take that value in every reading. They carry **40.75% of the model's weight**. Even if every one of the remaining 11 factors were pushed to 5, this reconstruction could not score above **3.37**, and the High band begins at 3.50. Nothing this case file says about the arithmetic is a discovery; the ceiling was fixed before any judgement was made.

## What this teaches the model

1. **This is not an onboarding failure and the model should not be asked to catch it.** The customer
   was rated correctly. The failure was the eighteen months between an internal recommendation to close
   and the closure, and no customer risk rating reaches that far.

2. **What the model is missing is the comparison, not the score.** The declaration of £5,000 a month is
   recorded at A1. Nothing in the model ever compares it with what the account received. That comparison
   belongs to transaction monitoring and to the event-driven review triggers at methodology 7.2, and the
   back-test's value here is confirming the division of labour rather than breaking it.

3. **The adverse reading still does not reach High**, which is the ceiling problem stated above rather
   than a property of this customer.



---

*Reconstruction, not a finding.* This case file rebuilds a customer from what a published FCA notice
records. It is not a claim about what the firm's file actually contained, and it is not a criticism of
any individual. The purpose is to test a model, not to re-try a case.
