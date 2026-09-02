# Barclays Bank UK plc and WealthTek

**Document reference:** HND-CRA-007
**Version:** 0.1
**Author:** Saman Barati
**Date:** September 2026

| | |
|---|---|
| **Firm** | Barclays Bank UK Plc |
| **Penalty** | £3,093,600 (reduced from £4,419,500) |
| **Date** | 16 July 2025 |
| **Source** | https://www.fca.org.uk/news/press-releases/fca-fines-barclays-42-million-poor-handling-financial-crime-risks |

## What happened

Barclays opened a client money account for WealthTek without checking the Financial Services Register. Had it looked, it would have seen that **WealthTek was not permitted by the FCA to hold client money**.

The check that was missing is free, takes under a minute, and is public.

## The customer at onboarding

| Factor | Level recorded | Score |
|---|---|---|
| C1 Legal form | UK company, natural owners | 3 |
| C3 Industry or occupation | Regulated profession | 2 |
| P1 Product | Business account, basic | 4 |
| P3 International payments | Regular payments | 4 |
| A1 Turnover | Over 25k, consistent | 3 |
| A4 Counterparties | Many individuals | 3 |

## What the model says

| | |
|---|---|
| Weighted score | **1.8250** |
| Band from the arithmetic | Low |
| Mandatory escalator | No |
| **Final rating** | **Low** |

## What this teaches the model

1. **The model is silent, and silence is the finding.** There is no factor in the library that asks whether a customer holds the permissions its business requires. D3 comes closest, but it asks about the firm that *introduced* the customer, not about the customer itself. WealthTek came direct.

2. **This is a whole class of risk the library misses.** A customer operating without a permission or registration it must hold is not a scoring question at all — regulation 5.4(c) of the methodology already puts unregistered money service businesses and cryptoasset firms on the prohibited list. WealthTek belongs in the same place, and the prohibited list is where Step 5 should put it.

3. **It is the cheapest lesson in the folder.** Every other case in this back-test involves judgement about a customer's story. This one involves reading a public register. A model that spends twenty factors on judgement and none on a checkable fact has its effort in the wrong place.

---

*Reconstruction, not a finding.* This case file rebuilds a customer from what a published FCA notice records. It is not a claim about what the firm's file actually contained, and it is not a criticism of any individual. The purpose is to test a model, not to re-try a case.
