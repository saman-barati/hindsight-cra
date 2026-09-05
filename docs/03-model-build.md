# Building and running the model

**Firm:** Northgate Bank UK Limited (fictional)
**Document reference:** HND-CRA-006
**Version:** 0.5
**Author:** Saman Barati
**Date:** September 2026
**Companion files:** `model/customer-risk-model.xlsx`, `data/synthetic-customers.csv`, `data/generation-notes.md`

---

### Author's note

Step 3 was supposed to be the mechanical step: load the data, apply the library, produce a rating. It turned out to be the step that found the largest problem in the model so far, which is recorded in section 4 below and is the reason there is now an item 11.5 in the methodology.

---

## 1. What the workbook does

1.1 `model/customer-risk-model.xlsx` takes the 400 synthetic customers, converts the level recorded against each of the 20 factors into a score using the Step 2 library, weights and sums those scores, bands the result, and then applies the mandatory escalators from methodology 5.3.

1.2 Six sheets:

| Sheet | Contents |
|---|---|
| `Overview` | What the workbook is, how a rating is produced column by column, and how to refresh the data |
| `Mapping` | The 98 level definitions from the Step 2 library with their scores. The lookup table. |
| `Weights` | The 20 factors with their weight in category and their effective weight, plus a horizontal copy the Scoring sheet reads |
| `Customers` | The imported population, one row per customer |
| `Scoring` | The engine: 400 rows × 20 lookups, then weighting, banding and escalation |
| `Dashboard` | What the population looks like once scored, and how much work each category is doing |
| `Checks` | Nineteen integrity tests |
| `Backtest` | Step 4: six enforcement cases scored through the same library and weights |
| `Validation` | Step 5: weight sensitivity, aggregation rules compared, and the 2026 EDD test |

1.3 The workbook contains 19,546 formulas and no hardcoded results. Every score, weight, band and rating recalculates if the population or a weight changes.

## 2. How a rating is produced

Reading across a row of the `Scoring` sheet:

| Columns | What happens |
|---|---|
| C to V | Each recorded level is converted to a score with `INDEX`/`MATCH` on the key `factor\|level`, so a level that does not exist in the library produces `#N/A` rather than a silent wrong answer |
| W | `SUMPRODUCT` of the 20 scores and the 20 effective weights |
| X | The same figure rounded to two decimal places, as methodology 5.2 requires |
| Y | Band from the arithmetic alone |
| Z | Whether any mandatory escalator in methodology 5.3 applies |
| AA | The final rating: High if Z is Yes, otherwise the band in Y |
| AB to AF | The five category scores, kept so the Dashboard can measure which categories separate customers |

`XLOOKUP` is not used anywhere. `INDEX`/`MATCH` does the same job and works in every version of Excel the reader might have, which matters more here than being modern.

## 3. Refreshing the population with Power Query

3.1 The `Customers` sheet holds the result of the import. To rebuild it from the CSV: **Data → Get Data → From File → From Text/CSV**, choose `data/synthetic-customers.csv`, set the delimiter to comma and the file origin to UTF-8, then **Transform Data**, promote the first row to headers, set every factor column to Text and `onboarded` to Date, remove duplicate `customer_id` values, and **Close & Load To** an existing worksheet at `Customers!$A$1`.

3.2 The query that produces, in M:

```m
let
    Source = Csv.Document(
        File.Contents("C:\Users\<you>\hindsight-cra\data\synthetic-customers.csv"),
        [Delimiter = ",", Columns = 24, Encoding = 65001, QuoteStyle = QuoteStyle.Csv]
    ),
    Promoted = Table.PromoteHeaders(Source, [PromoteAllScalars = true]),
    Typed = Table.TransformColumnTypes(
        Promoted,
        List.Transform(
            List.RemoveItems(Table.ColumnNames(Promoted), {"onboarded"}),
            each {_, type text}
        ) & {{"onboarded", type date}}
    ),
    Deduped = Table.Distinct(Typed, {"customer_id"})
in
    Deduped
```

Change the path on the second line to wherever the repository sits. Everything else is what Excel generates from the steps in 3.1.

3.3 Two deliberate choices in that query. Every factor column is loaded as **text**, not inferred, because a column of level labels must never be guessed into another type. And `Table.Distinct` on `customer_id` runs at import rather than after scoring, so a duplicated customer can never reach the model at all.

## 4. What the first run shows

400 customers, scored.

### 4.1 The headline

| | Customers | Share |
|---|---|---|
| Low | 295 | 73.75% |
| Medium | 62 | 15.50% |
| High | 43 | 10.75% |

**Every one of those 43 High ratings came from a mandatory escalator. Not one customer in 400 reached the High band on the arithmetic.**

Three of the 43 arrive there because of a correction made after external review: escalator 5.3(d) covers nominee shareholders and bearer shares, level 5 of factor C1 covers trusts, nominee arrangements and overseas incorporation, and the model was firing 5.3(d) on factor C2 only. It now fires on C1 level 5 as well. Methodology 11.9a explains why that was applied without approval when nothing else on the recommendation list has been.

The highest overall score anywhere in the population is **2.76**. The High band starts at 3.50.

### 4.2 Why that happens

It is not a coding error, and the workbook's nineteen checks all pass. It is arithmetic. **Nine factors would have to score 5, with every one of the remaining eleven at 1, for a customer to reach exactly 3.50.** The nine heaviest carry 62.5% of the effective weight between them, and 1 + 4 x 0.625 = 3.50 exactly. Nine is the count rather than a unique set: G2, P2 and P3 all carry 5%, so any one of the three fills the ninth place and the other two sit at 1. A weighted average over 20 factors pulls hard towards the middle: a customer has to be simultaneously bad on almost everything before the average moves, and real customers are bad on two or three things at once, not nine.

Methodology 10.5 already said that a weighted average dilutes single severe factors by design, and that the escalator list is the compensating control. What Step 3 shows is how complete that dilution is. The escalators are not a compensating control at the margin; on this population they are doing **all** of the work at the top of the scale.

### 4.3 Geography is carrying a quarter of the weight and almost no information

| Category | Weight | Mean | Std dev | Share of customers at the category minimum |
|---|---|---|---|---|
| Customer | 30% | 1.46 | 0.486 | 33.25% |
| Geography | 25% | 1.16 | 0.302 | **69.50%** |
| Product and service | 20% | 2.42 | 0.689 | 1.75% |
| Delivery channel | 10% | 2.67 | 0.538 | 1.00% |
| Expected activity | 15% | 1.76 | 0.531 | 6.50% |

Factor G1, country of residence, takes **one single value across all 400 customers**, because methodology 2.2 puts non-UK residents outside the Bank's perimeter. G1 alone carries 10% of the model's effective weight and separates nobody from anybody.

This is the concern recorded at methodology 11.1, now with a number against it.

### 4.4 Personal customers have no middle

| Segment | Customers | Low | Medium | High |
|---|---|---|---|---|
| Personal | 300 | 280 | 0 | 20 |
| Sole trader | 60 | 15 | 36 | 9 |
| Limited company | 40 | 0 | 26 | 14 |

Not one personal customer was rated Medium. The highest-scoring personal customer who was not escalated scores exactly **2.00**, which is the top of the Low band to the penny. Every personal customer is therefore either Low, or High because an escalator fired. For three quarters of the book the model is not a three-band scale at all; it is a switch.

### 4.5 The boundary is crowded

**37 customers, 9.2% of the population, sit within 0.10 of the Low/Medium boundary.** On a scale where the whole population spans 1.19 to 2.76, a tenth of the book is close enough to the line that a single factor scored one level differently would move it. That is the concern at methodology 11.2, and it points at the boundaries rather than the weights.

### 4.6 The customers nobody catches

Eight customers are in a cash-intensive sector **and** expect more than 30% of their credits in cash, and no escalator applies to any of them. All eight are rated Medium. The highest scores 2.21.

That is the same fact pattern as the worked example at methodology 5.6, which scored 2.07, and it is the question Step 4 answers — though not as cleanly as this sentence originally claimed. See [`backtest/README.md`](../backtest/README.md). Six customers named in FCA notices carrying roughly £480m of penalties between them are rebuilt there; none reaches High on the arithmetic, and none of them could have, because the facts the notices settle pin between 41% and 69% of the model's weight at level 1 before any judgement is made.

## 5. What this does not prove

5.1 The population is synthetic and its factors are drawn independently within a segment (`data/generation-notes.md`, section 6). Real customers correlate, so a real book would have a longer right tail than this one. The compression in 4.2 would be less severe, but it would not disappear: the arithmetic in 4.2 does not depend on the population at all.

5.2 The distributions are my judgement. Change them and the band counts change. What does **not** change with the distributions is that G1 has one value, that nine factors must be at 5 to reach 3.50, and that a weighted average compresses. Those are properties of the model, not of the data.

5.2a **Everything else in section 4 is a property of the population.** Added after external review, which asked for every place this project states a population property as a model property. The list, so it is in one place: "no personal customer is rated Medium" (4.4) follows from the distributions chosen for personal customers in `data/generation-notes.md`, not from the model; so do the band shares in 4.1, the category means and standard deviations in 4.3 apart from G1's single value, the 37 customers near the boundary in 4.5, and the eight uncaught cash-intensive customers in 4.6. Change the distributions and every one of those numbers changes. They are reported because they show what the model does to *a* plausible book, and the README states them more strongly than it should have; that has been corrected too.

5.3 Nothing here says the ratings are wrong. It says the arithmetic is not doing the job the methodology gives it. Whether the ratings are wrong is a question about real customers, and it belongs to Step 4.

## 6. What Step 5 now has to decide

6.1 **Whether to move the band boundaries or the weights.** If the achievable range on a realistic population is roughly 1.2 to 2.8, then a High band starting at 3.50 is decoration and the boundaries should be set from the observed distribution rather than from the midpoint of a theoretical 1 to 5 scale.

6.2 **Whether geography should keep 25%.** The evidence in 4.3 says no. The alternative is to cut it and let escalator 5.3(b) carry country risk on its own, which is what methodology 11.1 predicted.

6.3 **Whether a weighted average is the right aggregation at all.** A maximum-of-categories rule, or a rule that counts how many factors exceed a threshold, would not compress the way an average does. That is a larger change than re-weighting and it needs the Step 4 evidence before it can be argued for.

---

## Version history

| Version | Date | Change |
|---|---|---|
| 0.1 | Sept 2026 | First run of the model on the 400-customer synthetic population. |
| 0.5 | Sept 2026 | After external second-line review. Escalator 5.3(d) corrected to fire on C1 level 5, which moves three customers from Medium to High; every figure in section 4 re-run. The 3.50 arithmetic at 4.2 restated precisely (nine is a count, not a unique set). 5.2a added, listing the findings that are properties of the invented population rather than of the model. |
| 0.4 | Sept 2026 | Validation sheet and the Step 5 scenario columns added; three further integrity checks. Section 4 figures unchanged. |
| 0.3 | Sept 2026 | Backtest sheet added for Step 4, and three further integrity checks. Section 4 figures unchanged. |
| 0.2 | Sept 2026 | Re-run after the pre-Step-4 review corrected the C2 and C3 level 5 definitions. Every figure in section 4 is unchanged, because the correction was to wording rather than to any score. Document reference corrected from HND-CRA-005 to HND-CRA-006. |
