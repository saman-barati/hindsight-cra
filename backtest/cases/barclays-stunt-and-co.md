# Barclays Bank plc and Stunt & Co

**Document reference:** HND-CRA-007
**Version:** 0.1
**Author:** Saman Barati
**Date:** September 2026

| | |
|---|---|
| **Firm** | Barclays Bank Plc |
| **Penalty** | £39,314,700 (reduced from £56,163,900) |
| **Date** | 16 July 2025 |
| **Source** | https://www.fca.org.uk/news/press-releases/fca-fines-barclays-42-million-poor-handling-financial-crime-risks |

## What happened

Barclays provided banking services to Stunt & Co, which received **£46.8 million from Fowler Oldfield** over a little more than a year — the same laundering operation that produced the NatWest prosecution. The FCA found that Barclays did not gather enough information at the start of the relationship and did not carry out proper ongoing monitoring.

## The customer at onboarding

This reconstruction is different from the others. The FCA's finding is not that Barclays recorded the wrong thing; it is that Barclays **did not gather enough information**. So the honest reconstruction is a thin file: every question that was not asked is recorded at the level an unasked question produces, which is the benign one.

| Factor | Level recorded | Score |
|---|---|---|
| C1 Legal form | UK company, natural owners | 3 |
| C2 Ownership | One or two UBOs | 2 |
| C3 Industry or occupation | General trade | 3 |
| P1 Product | Business account, basic | 4 |
| A1 Turnover | 5k to 25k, consistent | 2 |
| A4 Counterparties | Named businesses | 2 |
| A5 Plausibility | Consistent | 1 |

## What the model says

| | |
|---|---|
| Weighted score | **1.7000** |
| Band from the arithmetic | Low |
| Mandatory escalator | No |
| **Final rating** | **Low** |

The lowest business score anywhere in the back-test.

## What this teaches the model

1. **A missing answer and a reassuring answer produce the same number.** This is the sharpest gap the back-test found. Every factor in the library assumes the analyst knows something. None of them asks how much the analyst knows.

2. **The fix is a completeness factor.** Step 5 should add a factor that scores the proportion of the file actually evidenced — not what the answers were, but how many questions have evidenced answers. A file where six of twenty factors rest on the customer's word alone should not be able to land in the same band as a file where all twenty are evidenced.

3. **It also argues for a floor rather than a score.** Regulation 31 already requires a firm to cease transactions where it cannot complete customer due diligence. A model that quietly rates an incomplete file Low is working against that requirement rather than with it.

---

*Reconstruction, not a finding.* This case file rebuilds a customer from what a published FCA notice records. It is not a claim about what the firm's file actually contained, and it is not a criticism of any individual. The purpose is to test a model, not to re-try a case.
