# Model validation

**Firm:** Northgate Bank UK Limited (fictional)
**Document reference:** HND-CRA-008
**Version:** 0.3
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

1.3 **And that evidence is narrower than it looks.** The facts each FCA notice settles — a UK company, a UK address, branch or app onboarding — pin between 41% and 69% of the model's weight at level 1 before any judgement is made. The highest score any of the six reconstructions could reach, if every remaining factor were pushed to 5, is 3.37, and the High band begins at 3.50. So the back-test's headline finding, that no reconstruction reaches High on the arithmetic, was fixed by its inputs and is not a discovery. What the back-test can still decide is whether an escalator fires, and how far the answer moves when the same file is read two defensible ways. Everything this pack takes from Step 4 is limited to those two things. See [`backtest/README.md`](../backtest/README.md).

## 2. How the population distributes

| Percentile | Overall score |
|---|---|
| 50th | 1.65 |
| 75th | 1.94 |
| 90th | 2.25 |
| 95th | 2.42 |
| Highest | 2.76 |

The High band begins at 3.50. The population never gets there. Under the current bands the book is 295 Low, 62 Medium and 43 High, and every one of those High ratings comes from a mandatory escalator rather than from the score.

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

The right-hand column tests that directly: the same weight changes, applied against boundaries that sit where the population actually is, move between 29 and 100 customers — **between 2.6 and 11.8 times as many, scenario for scenario.** The weights only start to matter once the bands are in the right place.

So the priority order is settled by evidence rather than instinct: fix the boundaries first, then argue about the weights. Section 11.1 of the methodology proposed cutting the geography weight. That is still worth doing for the reason given there — a factor that separates nobody should not carry weight — but it is a second-order change, and this pack says so.

## 4. Aggregation rules compared

Four ways of turning 20 factor scores into a rating, all applied to the same population.

| Rule | Definition | Low | Medium | High | High share |
|---|---|---|---|---|---|
| A  current | Weighted average, bands 1.00 / 2.01 / 3.50 | 295 | 62 | 43 | 10.8% |
| B  rebanded | Weighted average, bands 1.00 / 1.61 / 2.21 | 165 | 161 | 74 | 18.5% |
| C  severity | Count of factors scoring 4 or 5: 0 Low, 1-2 Medium, 3+ High | 120 | 155 | 125 | 31.2% |
| D  higher of B and C | The worse of the two ratings above | 91 | 182 | 127 | 31.8% |

### 4.1 Reading the table

Every rule in the table is a **final rating**, so the mandatory escalators at methodology 5.3 are applied on top of the arithmetic in all four rows. That is worth saying explicitly, because a reader who compares the High column with the score distribution in section 2 will not be able to reconcile them otherwise: 49 customers score above 2.20, 43 are escalated, and 25 of those escalated customers score at or below 2.20, which is how rule B reaches 74.

**Rule A** is the model as built. It uses one of its three bands.

**Rule B** keeps the weighted average and moves the boundaries to 1.60 and 2.20, which fall at the 43rd and 88th percentiles of the population. All three bands are now used, and the High share of 18.5% is a workload a bank could plausibly resource.

**Rule C** ignores the average and counts how many of the 20 factors score 4 or 5: none is Low, one or two is Medium, three or more is High. It is blunt, it is immune to dilution, and it puts 31.2% of the book in High.

**Rule D** takes the worse of B and C. It is the most conservative and the least affordable at 31.8%.

### 4.2 The operational constraint decides it, and the constraint is mine

Rules C and D put 31.2% and 31.8% of the book into High. Rule B puts 18.5% there. I rejected C and D on the ground that a bank cannot apply enhanced due diligence, senior management sign-off and annual refresh to nearly a third of its customers.

**That threshold is not sourced.** There is no published figure for the share of a retail bank's book that can be held at High, and I did not find one. Regulation 33 says when enhanced due diligence is mandatory and regulation 18 requires the assessment to be proportionate to the firm's size and nature; neither gives a number, and neither would, because the answer depends on the firm. What I have is an intuition about cost, dressed as a constraint, and it is doing the decisive work in this section.

Two things follow. The argument is still directionally right: rules C and D put roughly **1.7 times** as many customers into High as rule B does, and an EDD population 1.7 times larger needs something close to 1.7 times the analyst headcount. No firm resources a control by discovering afterwards that it cannot run it. But a reader should treat "rule B is the recommendation" as **the recommendation this analyst reaches given an assumption he cannot evidence**, and the first question a real second line would ask is what the firm's actual EDD capacity is. With that number, this section decides itself. Without it, section 5's priority order rests on a guess.

**Rule B is the recommendation, on that basis and no firmer one.**

## 5. The recommended changes

In priority order, with the evidence for each.

| # | Change | Evidence |
|---|---|---|
| 1 | **Move the band boundaries to 1.60 and 2.20.** | Section 3: the boundaries, not the weights, decide the output. Section 4: rule B is the only tested rule that uses all three bands at a workable High share. |
| 2 | **Move A5 level 5 out of the weighted average and onto the escalator list.** | Step 4: a customer whose stated address is a London landmark scores 1.52 and is rated Low. A declared fact that cannot be true is a failure to identify the customer, not a small increase in risk. |
| 3 | **Tie C3 level 5 to registration as a high value dealer** rather than to a description of the trade. | Step 4: the same jewellery business is Low or High depending on which of two defensible readings an analyst takes. **Contested — see 5.1.** |
| 4 | **Split PEP treatment so domestic PEPs and PEP family members are not automatically High.** | Regulation 35(3A) requires the starting point for a domestic PEP to be a *lower* level of risk than a non-domestic one. Escalator 5.3(a) treats a foreign PEP, a domestic PEP and a PEP's parent identically. |
| 5 | **Add a file-completeness factor.** | Nothing in the library asks how much of the file is evidenced rather than asserted. **The Step 4 evidence for this was withdrawn — see 5.2.** |
| 6 | **Reduce the geography weight.** | Section 3, and methodology 11.1. Genuine, but second-order until change 1 is made. |
| 7 | **Split C1 level 5** into "trust or overseas incorporation, ownership evidenced" and "nominee or bearer". | Escalator 5.3(d) is written as a condition the recorded level cannot evaluate, so it currently fires on the whole level. Methodology 11.9a. |
| 8 | **Add a level to C4 for the family and associates of a foreign PEP**, distinct from those of a domestic PEP. | Regulation 35(3A) requires the domestic starting point to be lower. The library now covers relatives of any PEP at level 3, but still cannot tell the two apart, so change 4 cannot be implemented without this. |

Changes 1 and 2 are implemented in the workbook and tested below. Changes 3 to 8 are specified but not built.

### 5.1 Change 3 is contested by the evidence for it

Tying the high-value-dealer level to registration would resolve the Fowler Oldfield ambiguity. It would also have taken **Stunt & Co from High to Medium**, because a gold refiner and trader that declares no cash would probably not have been a registered high value dealer, and C3 level 5 as currently written is the only thing in the model that catches that customer on the day the account opens.

So the change is not an improvement; it is a trade. It buys consistency on one case and loses the only correct call the back-test produced. It stays on the list because the current wording is genuinely ambiguous, but it cannot be made without a replacement control — the obvious candidate being a level that turns on the *goods* rather than on the registration, which is what the current wording was reaching for and failed to express precisely. Recorded so that nobody applies change 3 on the strength of the Fowler Oldfield finding alone.

### 5.2 The evidence for change 5 was withdrawn

Change 5 was argued from the Stunt & Co reconstruction, on the reading that Barclays had gathered almost nothing and the model therefore rated an empty file Low. That reconstruction was wrong: the Final Notice records what the application form said, and rebuilt from it the customer rates High. The specific claim — that the model cannot rate a file nobody filled in — no longer has that case behind it.

The underlying gap is still real and still unmeasured. The library has no level for "the check was run and nobody read the result" (Stunt & Co, C5) and no factor for the proportion of a file that is evidenced rather than asserted. Change 5 stays, ranked below change 4, with its evidence downgraded from a demonstrated failure to an identified gap. That is a weaker claim than the one it replaces and it is stated as such.

### 5.3 The boundaries in change 1 are fitted to a population I invented

1.60 and 2.20 are the 43rd and 88th percentiles of 400 customers whose distributions I chose in Step 3. Recommending boundaries derived from that population, and then testing them on the same population, is circular, and the circularity is at its worst exactly here — in the recommendation that section 3 says matters more than everything else in the model.

What survives the circularity is the *method*, not the numbers: set boundaries from the observed distribution and check that all three bands are used. What does not survive is any claim that 1.60 and 2.20 are the right numbers for a real book. On a real book they would be different, and the first calibration exercise a firm ran would move them.

## 6. What the recommended package does to the six enforcement cases

Rule B boundaries, plus A5 level 5 as an escalator. The same 13 reconstructions from Step 4 — two or three readings of each of the six cases, so a case counts once for each reading that moves.

| Case | Enforcement case | Score | Rating as built | Rating under the recommendation |
|---|---|---|---|---|
| FO-lo | NatWest / Fowler Oldfield, favourable reading, cash-intensive trade | 1.82 | Low | **Medium** |
| FO-mid | NatWest / Fowler Oldfield, same file, high-value dealer reading | 1.90 | High | **High** |
| FO-hi | NatWest / Fowler Oldfield, adverse reading of the open factors | 2.26 | High | **High** |
| SAN-a | Santander UK / the translations company, the file as recorded | 1.93 | Low | **Medium** |
| SAN-b | Santander UK / the translations company, with the business verified as an MSB | 2.18 | High | **High** |
| STU-a | Barclays / Stunt & Co, the application file of 16 January 2015 | 2.14 | High | **High** |
| STU-b | Barclays / Stunt & Co, the same file after the meeting of 27 January 2015 | 2.29 | High | **High** |
| WTK-lo | Barclays / WealthTek, favourable reading | 1.83 | Low | **Medium** |
| WTK-hi | Barclays / WealthTek, adverse reading | 2.05 | Medium | **Medium** |
| MON-lo | Monzo / the landmark address, favourable reading | 1.52 | Low | **High** |
| MON-hi | Monzo / the landmark address, adverse reading | 1.67 | Low | **High** |
| NAT-lo | Nationwide / the personal account used for business, favourable reading | 1.50 | Low | **Low** |
| NAT-hi | Nationwide / the personal account used for business, adverse reading | 1.60 | Low | **Low** |

**5 of the 13 rows change rating, all of them upwards** — three rows move from Low to Medium, two rows move from Low to High. The Monzo rows are the Low-to-High moves: the address that could not be true now decides the rating on its own. Rows already rated High by an escalator cannot move, which is 5 of the 13.

### 6.1 What this does not claim

None of these customers becomes High on the arithmetic, and for the reason at 1.3 none of them could have. Fowler Oldfield under the cash-intensive reading is still Medium. The recommendation does not manufacture hindsight and it would not have "caught" these customers in the sense of stopping them.

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

8.2 **The proposed boundaries are fitted to this population, and the aggregation rule is chosen on an unsourced workload limit.** Both admissions used to live here. They have been moved to 5.3 and 4.2, next to the conclusions they undercut, because a caveat filed at the back of a document is not a caveat a reader meets before believing the finding.

8.3 **The challenge is no longer entirely internal, and that changed the pack.** This version follows an external second-line review. Its findings, the ones accepted and the three disputed, are in [`docs/06-review-response.md`](06-review-response.md). Sections 1.3, 4.2, 5.1, 5.2 and 5.3 all exist because of it. That is not the same as independent validation — I still chose which findings to accept — but it is no longer a document that has only ever been read by its author.

8.4 **Fitting to six cases is not validation either.** Six enforcement notices are the six that were published, prosecuted and reported. Firms that failed without being fined are not in the sample, and neither are the customers who looked terrible and turned out fine — which is the false positive side, and this project has no way to see it at all.

## 9. Model change log

| # | Change | Status |
|---|---|---|
| 1 | Band boundaries to 1.60 and 2.20 | Tested; recommended |
| 2 | A5 level 5 onto the escalator list | Tested; recommended |
| 3 | C3 level 5 tied to high value dealer registration | Specified; **contested** (5.1); not built |
| 4 | Domestic PEPs and PEP family members not automatically High | Specified; not built |
| 5 | File-completeness factor | Specified; evidence downgraded (5.2); not built |
| 6 | Reduce the geography weight | Specified; deferred until change 1 |
| 7 | Split C1 level 5 so 5.3(d) can be evaluated | Specified; not built |
| 8 | A C4 level for the relatives of a foreign PEP | Specified; not built |
| — | C4 level 3 reworded to cover the family and known close associates of **any** PEP | **Applied.** A defect fix: regulation 35(1) and escalator 5.3(a) both cover them, and the library's wording covered only the relatives of a domestic PEP, so a foreign PEP's relative had no level to be recorded at. No rating changes on this population. |
| — | Escalator 5.3(b) reworded from "second residence" to "a further tax residence" | **Applied.** Documentation fix: factor G2 records tax residence, and the escalator and the population labels both said "second residence". No rating changes. |
| — | Escalator 5.3(d) now fires on the whole of C1 level 5 | **Applied.** A defect fix, not a calibration change: the library said C1 level 5 triggered 5.3(d) where nominee shareholders or bearer shares were present, and the model never fired it at all. Three customers move to High. The proper fix, splitting C1 level 5 so the condition can be evaluated, is change 7. See methodology 11.9a. |
| — | Escalator 5.3(b) reworded to cover payment corridors | **Applied.** The model always fired on G3 level 5; the written escalator said "established in", which the model does not test. Documentation corrected to match the control. No rating changes. |

---

## Version history

| Version | Date | Change |
|---|---|---|
| 0.3 | Sept 2026 | Second pre-publication review. Percentiles corrected to the 43rd and 88th; the workload ratio at 4.2 corrected from three times to 1.7; changes 7 and 8 added to section 5; two further defect fixes logged in section 9. |
| 0.2 | Sept 2026 | Rewritten after an external second-line review. The back-test ceiling is stated at 1.3 before any conclusion rests on it; the unsourced workload limit is stated at 4.2 where it decides the answer; the circularity of the proposed boundaries is stated at 5.3 where they are recommended. Change 3 is marked contested, change 5's evidence is downgraded, and a PEP change is added at 4 for regulation 35(3A). All figures re-run after escalator 5.3(d) was corrected. |
| 0.1 | Sept 2026 | First validation pack: distribution, sensitivity, aggregation rules, recommended changes. |
