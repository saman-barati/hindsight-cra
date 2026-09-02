# NatWest and Fowler Oldfield

**Document reference:** HND-CRA-007
**Version:** 0.1
**Author:** Saman Barati
**Date:** September 2026

| | |
|---|---|
| **Firm** | National Westminster Bank Plc |
| **Penalty** | £264,772,619.95 |
| **Date** | 13 December 2021 |
| **Basis** | Criminal conviction on FCA prosecution under the Money Laundering Regulations 2007 |
| **Relevant period** | 8 November 2012 to 23 June 2016 |
| **Source** | https://www.fca.org.uk/news/press-releases/natwest-fined-264.8million-anti-money-laundering-failures |

## What happened

Fowler Oldfield was a jewellery business operating from Bradford. When the relationship began, the bank understood that the customer would not be handling cash. Around **£365 million** subsequently passed through the account, of which roughly **£264 million was cash**.

The FCA's case records Scottish banknotes deposited at branches across England, cash arriving in bags with a distinctive smell, and a system error that classified some cash deposits as cheques, which is a lower-risk category. Staff raised concerns. Nothing changed. The sentencing judge described the bank as functionally vital to the laundering.

## The customer at onboarding

Reconstructed from what the bank understood at the start of the relationship, not from what emerged later.

| Factor | Level recorded | Score |
|---|---|---|
| C1 Legal form | UK company, natural owners | 3 |
| C3 Industry or occupation | **Cash-intensive trade** *(reading a)* / **MSB, TCSP or HVD** *(reading b)* | **4 / 5** |
| P1 Product | Business account, basic | 4 |
| P2 Cash functionality | Withdrawal only | 2 |
| A1 Turnover | Over 25k, consistent | 3 |
| A2 Expected cash proportion | **No cash credits** | 1 |
| A5 Plausibility | Consistent | 1 |

Everything else sits at its base level. The full row is on the `Backtest` sheet of `model/customer-risk-model.xlsx`.

**A2 is the line that matters.** The customer declared no cash and the model scores what is declared. A customer intending to launder £264 million in banknotes has every reason to say the account will not see cash, and nothing at onboarding contradicts it.

## What the model says

| | Reading (a): cash-intensive trade | Reading (b): dealer in high-value goods |
|---|---|---|
| Customer category | 2.35 | 2.60 |
| Weighted score | **1.8225** | **1.8975** |
| Band from the arithmetic | Low | Low |
| Mandatory escalator | No | Yes |
| **Final rating** | **Low** | **High** |

Under reading (b) the customer falls inside escalator 5.3(c) — a dealer in high-value goods — and is rated High regardless of the score. Under reading (a) it is not, and the customer is Low.

The arithmetic difference between the two readings is **0.0750**. Neither score comes within 1.6 points of the High band.

## What this teaches the model

1. **The escalator is the whole control.** On this customer the score is irrelevant: it is Low either way. Whether the bank ends up applying enhanced due diligence turns entirely on a list membership question, which is exactly the pattern Step 3 found across 400 customers.

2. **The level definition is ambiguous and that is my fault.** A jewellery business is a plausible dealer in high-value goods and a plausible cash-intensive trade. The library gives an analyst two defensible answers to the same question, and they lead to opposite ratings. Step 5 has to make C3 level 5 turn on a fact that can be checked — whether the customer is registered with HMRC as a high value dealer — rather than on a description of the trade.

3. **Declared cash is worth almost nothing at onboarding.** A2 carries 4.5% of the model and is scored from an unverified statement. Methodology 11.3 already asked whether expected activity belongs in an onboarding model. This is the case that answers it.

---

*Reconstruction, not a finding.* This case file rebuilds a customer from what a published FCA notice records. It is not a claim about what the firm's file actually contained, and it is not a criticism of any individual. The purpose is to test a model, not to re-try a case.
