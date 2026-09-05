# Synthetic population: generation notes

**Firm:** Northgate Bank UK Limited (fictional)  
**Document reference:** HND-CRA-005  
**Version:** 0.1  
**Author:** Saman Barati  
**Date:** September 2026  
**Produced by:** `build/generate.py`, seed `20260902`

---

### Author's note

Methodology 9.2 promises that the generation method and its assumptions are documented. This is that document. It exists because a synthetic population is an argument, not a fact: every percentage below is a claim about what a UK retail bank's customer base looks like, and every one of them is mine. If a reader thinks a number is wrong, this file is where they can say so precisely.

This file is generated from the same code that generates the data, so the two cannot drift apart.

---

## 1. What was produced

`synthetic-customers.csv` holds 400 customers. One row per customer, one column per risk factor, holding the **level recorded at onboarding** rather than a score. Converting a level into a score is the model's job, not the data's, which keeps the population independent of the weights.

| Column | Contents |
|---|---|
| `customer_id` | Reference in the form NG-1xxxx |
| `segment` | Personal, Sole trader, or Limited company |
| `C1` ... `A5` | The level recorded for each of the 20 factors, using the short labels in the model's Mapping sheet |
| `sar_last_12m` | Whether a suspicious activity report was submitted in the preceding twelve months |
| `onboarded` | Date of onboarding, drawn uniformly across 2024 and 2025 |

## 2. Segments

| Segment | Customers | Share |
|---|---|---|
| Personal | 300 | 75% |
| Sole trader | 60 | 15% |
| Limited company | 40 | 10% |
| **Total** | **400** | **100%** |

The mix reflects a retail bank with a small business book rather than a business bank: three quarters personal, and the business quarter weighted towards sole traders. Every customer is UK resident, because methodology 2.2 puts non-UK residents outside the Bank's perimeter.

## 3. Rules applied to every customer

1. **Country of residence is always the United Kingdom.** Not a simplification: it follows from the scope at methodology 2.2. The consequence is that factor G1 has no variance at all in this population, which is deliberate and is one of the things Step 3 set out to measure.
2. **No prohibited relationships appear.** Section 5.4 of the methodology lists customers who are declined rather than rated, so a population of onboarded customers cannot contain them.
3. **Level 5 at C3 means exactly the three business types that trigger escalator 5.3(c)** - money service businesses, trust or company service providers, and dealers in high-value goods. Sectors the National Risk Assessment treats as vulnerable without an automatic escalation, such as accountancy practices, sit at level 4. This was corrected after the Step 3 review; before it, a score of 5 and an automatic escalation did not always mean the same thing.
4. **A SAR was recorded for 1.5% of customers**, drawn independently of every other attribute. That independence is unrealistic, and it is called out in the limitations below.
5. **The draw is deterministic.** Seed 20260902, so re-running the generator reproduces this file byte for byte.

## 4. The distributions

Read across: the probability that a customer in each segment was assigned that level. Blank means the level cannot occur in that segment. Columns sum to 100% within each factor.

| Factor | Level recorded | Score | Personal | Sole trader | Limited co. |
|---|---|---|---|---|---|
| C1 | Individual | 1 | 78.0% | - | - |
| C1 | Sole trader or joint | 2 | 22.0% | 100.0% | - |
| C1 | UK company, natural owners | 3 | - | - | 62.0% |
| C1 | UK company, corporate owner | 4 | - | - | 30.0% |
| C1 | Trust, nominee or overseas | 5 | - | - | 8.0% |
| C2 | Natural person | 1 | 100.0% | 100.0% | - |
| C2 | One or two UBOs | 2 | - | - | 52.0% |
| C2 | Three to five UBOs | 3 | - | - | 24.0% |
| C2 | Two layers, evidenced | 4 | - | - | 18.0% |
| C2 | Nominee, bearer or unevidenced | 5 | - | - | 6.0% |
| C3 | Employed or pension | 1 | 62.0% | 5.0% | - |
| C3 | Regulated profession | 2 | 14.0% | 14.0% | 20.0% |
| C3 | General trade | 3 | 20.0% | 44.0% | 46.0% |
| C3 | Cash-intensive trade | 4 | 3.5% | 34.0% | 26.0% |
| C3 | MSB, TCSP or HVD | 5 | 0.5% | 3.0% | 8.0% |
| C4 | No match | 1 | 98.5% | 98.5% | 97.5% |
| C4 | PEP family or associate | 3 | 0.8% | 0.8% | 1.2% |
| C4 | Domestic PEP | 4 | 0.5% | 0.5% | 0.8% |
| C4 | Foreign PEP | 5 | 0.2% | 0.2% | 0.5% |
| C5 | No match | 1 | 93.0% | 90.0% | 88.0% |
| C5 | False positive | 2 | 5.5% | 7.0% | 8.0% |
| C5 | Adverse media, non-financial | 3 | 0.8% | 2.0% | 2.2% |
| C5 | Adverse media, unproven | 4 | 0.5% | 0.8% | 1.3% |
| C5 | Adverse media, financial crime | 5 | 0.2% | 0.2% | 0.5% |
| G1 | United Kingdom | 1 | 100.0% | 100.0% | 100.0% |
| G1 | Unlisted country | 2 | - | - | - |
| G1 | Weaker AML, unlisted | 3 | - | - | - |
| G1 | FATF increased monitoring | 4 | - | - | - |
| G1 | FATF call for action | 5 | - | - | - |
| G2 | UK only | 1 | 93.0% | 90.0% | 86.0% |
| G2 | Second residence, unlisted | 2 | 5.5% | 7.5% | 10.0% |
| G2 | Second residence, monitored | 4 | 1.2% | 2.0% | 3.0% |
| G2 | Second residence, call for action | 5 | 0.3% | 0.5% | 1.0% |
| G3 | UK only | 1 | 84.0% | 68.0% | 52.0% |
| G3 | Unlisted countries | 2 | 12.0% | 20.0% | 26.0% |
| G3 | Weaker AML, unlisted | 3 | 3.0% | 8.0% | 14.0% |
| G3 | FATF increased monitoring | 4 | 0.8% | 3.0% | 6.0% |
| G3 | FATF call for action | 5 | 0.2% | 1.0% | 2.0% |
| P1 | Savings only | 1 | 12.0% | - | - |
| P1 | Current account, no overdraft | 2 | 46.0% | - | - |
| P1 | Current account with credit | 3 | 42.0% | - | - |
| P1 | Business account, basic | 4 | - | 72.0% | 45.0% |
| P1 | Business account, cash and international | 5 | - | 28.0% | 55.0% |
| P2 | No cash facility | 1 | 10.0% | 2.0% | 6.0% |
| P2 | Withdrawal only | 2 | 42.0% | 8.0% | 10.0% |
| P2 | Under 2k a month | 3 | 42.0% | 28.0% | 26.0% |
| P2 | 2k to 10k a month | 4 | 5.5% | 42.0% | 36.0% |
| P2 | Over 10k a month | 5 | 0.5% | 20.0% | 22.0% |
| P3 | Not enabled | 1 | 35.0% | 30.0% | 14.0% |
| P3 | Enabled, unused | 2 | 34.0% | 26.0% | 20.0% |
| P3 | Occasional payments | 3 | 24.0% | 28.0% | 30.0% |
| P3 | Regular payments | 4 | 6.0% | 13.0% | 30.0% |
| P3 | Payments to listed country | 5 | 1.0% | 3.0% | 6.0% |
| P4 | Sole party | 1 | 72.0% | 80.0% | 34.0% |
| P4 | Joint, related | 2 | 20.0% | 6.0% | 4.0% |
| P4 | Mandate, evidenced | 3 | 6.0% | 10.0% | 40.0% |
| P4 | Power of attorney | 4 | 1.5% | 3.0% | 17.0% |
| P4 | Unexplained signatories | 5 | 0.5% | 1.0% | 5.0% |
| D1 | Branch | 1 | 10.0% | 14.0% | 20.0% |
| D1 | Telephone and branch | 2 | 5.0% | 5.0% | 6.0% |
| D1 | Digital, own app | 3 | 72.0% | 60.0% | 48.0% |
| D1 | Digital, assisted | 4 | 11.0% | 17.0% | 20.0% |
| D1 | Unsupervised intermediary | 5 | 2.0% | 4.0% | 6.0% |
| D2 | Documents face to face | 1 | 11.0% | 13.0% | 18.0% |
| D2 | Certified copies | 2 | 4.0% | 5.0% | 8.0% |
| D2 | Electronic, two sources | 3 | 66.0% | 58.0% | 50.0% |
| D2 | Electronic, one source | 4 | 17.0% | 21.0% | 20.0% |
| D2 | Uncorroborated documents | 5 | 2.0% | 3.0% | 4.0% |
| D3 | Direct | 1 | 70.0% | 62.0% | 50.0% |
| D3 | Customer referral | 2 | 13.0% | 16.0% | 14.0% |
| D3 | Comparison site | 3 | 14.0% | 12.0% | 8.0% |
| D3 | Register checked | 4 | 2.5% | 8.0% | 24.0% |
| D3 | Register not confirmed | 5 | 0.5% | 2.0% | 4.0% |
| A1 | Under 5k, consistent | 1 | 72.0% | 20.0% | 8.0% |
| A1 | 5k to 25k, consistent | 2 | 23.0% | 50.0% | 36.0% |
| A1 | Over 25k, consistent | 3 | 3.0% | 22.0% | 40.0% |
| A1 | Above sector expectation | 4 | 1.5% | 6.0% | 12.0% |
| A1 | Unexplained | 5 | 0.5% | 2.0% | 4.0% |
| A2 | No cash credits | 1 | 30.0% | 8.0% | 16.0% |
| A2 | Up to 10 percent | 2 | 47.0% | 22.0% | 30.0% |
| A2 | 10 to 30 percent | 3 | 18.0% | 31.0% | 28.0% |
| A2 | 30 to 60 percent | 4 | 4.0% | 28.0% | 18.0% |
| A2 | Over 60 percent | 5 | 1.0% | 11.0% | 8.0% |
| A3 | None | 1 | 66.0% | 56.0% | 34.0% |
| A3 | Up to 10 percent | 2 | 24.0% | 24.0% | 26.0% |
| A3 | 10 to 40 percent | 3 | 7.0% | 13.0% | 24.0% |
| A3 | Over 40 percent | 4 | 2.5% | 5.5% | 12.0% |
| A3 | Over 40 percent, listed country | 5 | 0.5% | 1.5% | 4.0% |
| A4 | Employer and retail | 1 | 74.0% | 10.0% | 6.0% |
| A4 | Named businesses | 2 | 15.0% | 34.0% | 44.0% |
| A4 | Many individuals | 3 | 8.0% | 42.0% | 30.0% |
| A4 | Sector 4 counterparties | 4 | 2.5% | 11.0% | 15.0% |
| A4 | Undescribed or sector 5 | 5 | 0.5% | 3.0% | 5.0% |
| A5 | Consistent | 1 | 86.0% | 78.0% | 74.0% |
| A5 | Minor, explained | 2 | 10.0% | 13.0% | 15.0% |
| A5 | Resolved on follow-up | 3 | 3.0% | 6.0% | 7.0% |
| A5 | Unresolved | 4 | 0.8% | 2.5% | 3.0% |
| A5 | Not credible | 5 | 0.2% | 0.5% | 1.0% |

## 5. What the population actually came out as

Drawn counts, for the factors where the outcome matters most to the model:

| Factor | Level recorded | Customers | Share |
|---|---|---|---|
| C3 Industry or occupation | Employed or pension | 183 | 45.8% |
| C3  | Regulated profession | 55 | 13.8% |
| C3  | General trade | 103 | 25.8% |
| C3  | Cash-intensive trade | 47 | 11.8% |
| C3  | MSB, TCSP or HVD | 12 | 3.0% |
| C4 PEP screening outcome | No match | 389 | 97.2% |
| C4  | PEP family or associate | 7 | 1.8% |
| C4  | Domestic PEP | 3 | 0.8% |
| C4  | Foreign PEP | 1 | 0.2% |
| G1 Country of residence or incorporation | United Kingdom | 400 | 100.0% |
| G1  | Unlisted country | 0 | 0.0% |
| G1  | Weaker AML, unlisted | 0 | 0.0% |
| G1  | FATF increased monitoring | 0 | 0.0% |
| G1  | FATF call for action | 0 | 0.0% |
| G3 Expected counterparty or payment corridor countries | UK only | 307 | 76.8% |
| G3  | Unlisted countries | 65 | 16.2% |
| G3  | Weaker AML, unlisted | 18 | 4.5% |
| G3  | FATF increased monitoring | 6 | 1.5% |
| G3  | FATF call for action | 4 | 1.0% |
| P2 Cash functionality | No cash facility | 36 | 9.0% |
| P2  | Withdrawal only | 147 | 36.8% |
| P2  | Under 2k a month | 144 | 36.0% |
| P2  | 2k to 10k a month | 47 | 11.8% |
| P2  | Over 10k a month | 26 | 6.5% |
| A2 Expected cash proportion of credits | No cash credits | 111 | 27.8% |
| A2  | Up to 10 percent | 162 | 40.5% |
| A2  | 10 to 30 percent | 86 | 21.5% |
| A2  | 30 to 60 percent | 33 | 8.2% |
| A2  | Over 60 percent | 8 | 2.0% |

Suspicious activity reports recorded: **11 of 400 customers (2.8%)**.

That is above the 1.5% parameter at point 4 above, and the gap is the draw rather than a mistake: with p = 0.015 and n = 400 the expected count is 6.0 with a standard deviation of 2.43, so 11 sits 2.1 standard deviations high — the kind of result a single seed produces roughly one time in 25. The seed is fixed at 20260902 so the figure is reproducible, and it is the realised 2.8% that every count in this project is computed from, not the 1.5% parameter. An external reviewer read the two figures as a contradiction, which is fair: the document reported both and explained neither.

## 6. Limitations of this population

6.1 **The factors are drawn independently within a segment.** In a real book they correlate: a customer who takes 60% of turnover in cash is more likely to be in a cash-intensive sector, and the generator does not know that. The effect is to spread the population more evenly across the score range than reality would.

6.2 **The SAR flag is independent of everything else**, which is the least realistic assumption here. In a real book, a SAR is the end of a chain that usually starts with something the model can already see.

6.3 **There is no bad-outcome label.** Nothing in this file records which customers went on to launder money, because inventing that would let the model be tuned against a fiction. It is the reason Step 4 tests the model against real published enforcement cases instead of against this population.

6.4 **The percentages are judgement.** They are shaped by what UK retail banking looks like from the outside, not by any firm's internal data, which a personal project cannot have.

6.5 **The population is not a validation set.** It shows how the model behaves across a plausible spread of customers. It cannot show whether the model is right, only whether it discriminates.

