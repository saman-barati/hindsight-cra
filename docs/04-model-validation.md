# Model validation

**Firm:** Northgate Bank UK Limited (fictional)
**Document reference:** HND-CRA-008
**Version:** 0.1
**Author:** Saman Barati
**Date:** September 2026
**Companion file:** `model/customer-risk-model.xlsx`, sheet `Validation`

---

### Author's note

This is the closest a one-person project can get to second-line challenge: I wrote the model, so I cannot independently validate it. What I can do is test it hard enough that its weaknesses are on the record rather than waiting to be found by someone else.

The largest finding is not one I expected. I spent Step 2 arguing about the weights. Step 5 shows the weights were never the thing that mattered.

---

## 1. What validation can and cannot show

1.1 This pack tests four things: how the population distributes, how much the output depends on each weight, whether a different aggregation rule would work better, and what the 2026 change to jurisdiction-based enhanced due diligence does to the book.

1.2 It cannot show that the ratings are correct. There is no outcome data. Step 4 tested the model against customers whose outcomes are publicly known, and that back-test remains the only evidence in this project about whether the model is *right* rather than merely consistent.

## 2. How the population distributes

| Percentile | Overall score |
|---|---|
| 50th | 1.65 |
| 75th | 1.94 |
| 90th | 2.25 |
| 95th | 2.42 |
| Highest | 2.76 |

The High band begins at 3.50. The population never gets there. Under the current bands the book is 295 Low, 65 Medium and 40 High, and every one of those High ratings comes from a mandatory escalator rather than from the score.

## 3. Weight sensitivity

Each category weight was moved by ten percentage points, with the other four rescaled so the total stays at 100%, and the whole population rescored. The table counts how many of the 400 customers change band.

| Scenario | Weight becomes | Band changes, current bands | Band changes, rebanded |
|---|---|---|---|
| Customer -10pp | 20% | 15 | 54 |
| Customer +10pp | 40% | 4 | 47 |
| Geography -10pp | 15% | 16 | 67 |
| Geography +10pp | 35% | 26 | 68 |
| Product and service -10pp | 10% | 24 | 69 |
| Product and service +10pp | 30% | 20 | 80 |
| Delivery channel -10pp | 0% | 14 | 83 |
| Delivery channel +10pp | 20% | 25 | 100 |
| Expected activity -10pp | 5% | 9 | 29 |
| Expected activity +10pp | 25% | 7 | 36 |

### 3.1 The finding

Under the current bands, **the largest weight change in the table moves 26 customers out of 400**. Removing the delivery channel category entirely — setting it to zero — moves 14.

That is the answer to the question Step 2 spent a document arguing about. Whether geography carries 25% or 15% changes the rating of 26 customers. The weights are not what decides this model's output.

### 3.2 Why, and what actually decides it

Because the population sits far below the band boundaries, a small change to a weighted average of mostly-low scores rarely carries anyone across a line. The boundaries are doing the work, not the weights.

The right-hand column tests that directly: the same weight changes, applied against boundaries that sit where the population actually is, move between 29 and 100 customers. **Between three and six times as many.** The weights only start to matter once the bands are in the right place.

So the priority order is settled by evidence rather than instinct: fix the boundaries first, then argue about the weights. Section 11.1 of the methodology proposed cutting the geography weight. That is still worth doing for the reason given there — a factor that separates nobody should not carry weight — but it is a second-order change, and this pack says so.

## 4. Aggregation rules compared

Four ways of turning 20 factor scores into a rating, all applied to the same population.

| Rule | Definition | Low | Medium | High | High share |
|---|---|---|---|---|---|
| A  current | Weighted average, bands 1.00 / 2.01 / 3.50 | 295 | 65 | 40 | 10.0% |
| B  rebanded | Weighted average, bands 1.00 / 1.61 / 2.21 | 165 | 162 | 73 | 18.2% |
| C  severity | Count of factors scoring 4 or 5: 0 Low, 1-2 Medium, 3+ High | 120 | 155 | 125 | 31.2% |
| D  higher of B and C | The worse of the two ratings above | 91 | 182 | 127 | 31.8% |

### 4.1 Reading the table

**Rule A** is the model as built. It uses one of its three bands.

**Rule B** keeps the weighted average and moves the boundaries to 1.60 and 2.20, which fall at roughly the 42nd and 88th percentiles of the population. All three bands are now used, and the High share of 18.2% is a workload a bank could plausibly resource.

**Rule C** ignores the average and counts how many of the 20 factors score 4 or 5: none is Low, one or two is Medium, three or more is High. It is blunt, it is immune to dilution, and it puts 31.2% of the book in High.

**Rule D** takes the worse of B and C. It is the most conservative and the least affordable at 31.8%.

### 4.2 The operational constraint decides it

A bank cannot apply enhanced due diligence, senior management sign-off and annual refresh to nearly a third of its customers. Rules C and D are unaffordable whatever their analytical merits, and a control that cannot be resourced is not a control. **Rule B is the recommendation.**

That is a real limit on what this exercise can conclude, and it is worth stating plainly: the most risk-sensitive rule tested here is the one no firm could run.

## 5. The recommended changes

In priority order, with the evidence for each.

| # | Change | Evidence |
|---|---|---|
| 1 | **Move the band boundaries to 1.60 and 2.20.** | Section 3: the boundaries, not the weights, decide the output. Section 4: rule B is the only tested rule that uses all three bands at a workable High share. |
| 2 | **Move A5 level 5 out of the weighted average and onto the escalator list.** | Step 4: a customer whose stated address is a London landmark scores 1.52 and is rated Low. A declared fact that cannot be true is a failure to identify the customer, not a small increase in risk. |
| 3 | **Tie C3 level 5 to registration as a high value dealer** rather than to a description of the trade. | Step 4: the same jewellery business is Low or High depending on which of two defensible readings an analyst takes. |
| 4 | **Add a file-completeness factor.** | Step 4: reconstructing a relationship where the bank did not gather enough information produces the lowest business score in the back-test, because an unasked question and a reassuring answer are indistinguishable. |
| 5 | **Reduce the geography weight.** | Section 3, and methodology 11.1. Genuine, but second-order until change 1 is made. |

Changes 1 to 3 are implemented in the workbook and tested below. Changes 4 and 5 are specified but not built, because change 4 needs a data field the population does not carry and change 5 should not be argued until change 1 has bedded in.

## 6. What the recommended package does to the six enforcement cases

Rule B boundaries, plus A5 level 5 as an escalator. The same seven reconstructions from Step 4.

| Case | Enforcement case | Score | Rating as built | Rating under the recommendation |
|---|---|---|---|---|
| FO-a | NatWest / Fowler Oldfield, cash-intensive reading | 1.82 | Low | **Medium** |
| FO-b | NatWest / Fowler Oldfield, high-value dealer reading | 1.90 | High | **High** |
| SAN | Santander UK / the translations company | 1.89 | Low | **Medium** |
| STU | Barclays Bank plc / Stunt & Co | 1.70 | Low | **Medium** |
| WTK | Barclays Bank UK plc / WealthTek | 1.83 | Low | **Medium** |
| MON | Monzo / the landmark address | 1.52 | Low | **High** |
| NAT | Nationwide / the personal account used for business | 1.50 | Low | **Low** |

**5 of the 7 rows move up.** Five move from Low to Medium; the Monzo reconstruction moves from Low to High, because the address that could not be true now decides the rating on its own.

### 6.1 What this does not claim

None of these customers becomes High on the arithmetic. Fowler Oldfield under the cash-intensive reading is still Medium. The recommendation does not manufacture hindsight and it would not have "caught" these customers in the sense of stopping them.

What it changes is treatment. Medium instead of Low means standard rather than simplified due diligence, source of funds required where activity is inconsistent with the profile, and a three-year rather than five-year refresh. For customers who went on to move hundreds of millions of pounds, that is a material difference, and it is the honest size of the claim.

## 7. Override governance

7.1 Methodology 5.5 sets the rules: an analyst may override upwards freely, downwards only with MLRO approval and a written rationale, never below Medium where a mandatory escalator applies, and the model is treated as needing recalibration if overrides exceed 5% of ratings in a quarter.

7.2 What was missing was the management information that makes the 5% threshold mean anything. The override register should report, quarterly:

- overrides as a percentage of ratings issued, split by direction
- the five factors most often overridden, which is where the level definitions are failing
- overrides by analyst, to separate a model problem from a training problem
- downward overrides that were later followed by a suspicious activity report, which is the only outcome signal this model will ever get

7.3 The third and fourth of those matter most. A high override rate concentrated on one factor is a definition to rewrite. A high override rate spread evenly is a model to recalibrate. Without the split, the 5% threshold cannot tell the two apart.

## 8. Limitations of this validation

8.1 **The population is synthetic and its factors are drawn independently.** Real customers correlate, which would lengthen the right tail. The compression finding in section 3 does not depend on the population — it is a property of averaging 20 factors — but the exact counts do.

8.2 **The proposed boundaries are fitted to this population.** 1.60 and 2.20 come from where these 400 customers sit. On a real book they would be wrong, and the method rather than the numbers is what transfers: set boundaries from the observed distribution and check that all three bands are used.

8.3 **There is still no independent challenge.** I proposed the changes, tested them, and judged them. Section 4.2 rejects rules C and D on an operational argument I made up, using a workload limit no one gave me.

8.4 **Fitting to six cases is not validation either.** Six enforcement notices are the six that were published, prosecuted and reported. Firms that failed without being fined are not in the sample, and neither are the customers who looked terrible and turned out fine — which is the false positive side, and this project has no way to see it at all.

## 9. Model change log

| # | Change | Status |
|---|---|---|
| 1 | Band boundaries to 1.60 and 2.20 | Tested; recommended |
| 2 | A5 level 5 onto the escalator list | Tested; recommended |
| 3 | C3 level 5 tied to high value dealer registration | Specified in Step 4; wording corrected in the library |
| 4 | File-completeness factor | Specified; not built |
| 5 | Reduce the geography weight | Specified; deferred until change 1 |

---

## Version history

| Version | Date | Change |
|---|---|---|
| 0.1 | Sept 2026 | First validation pack: distribution, sensitivity, aggregation rules, recommended changes. |
