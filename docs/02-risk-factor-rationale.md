# Risk Factor Rationale

**Firm:** Northgate Bank UK Limited (fictional)
**Document reference:** HND-CRA-003
**Version:** 0.2 (draft)
**Author:** Saman Barati
**Date:** September 2026
**Companion file:** `model/risk-factor-library.xlsx`

---

### Author's note

The workbook holds the library: 20 factors, 98 level definitions, the weights, and a source against each factor. This document explains the decisions behind it, including the two that are most likely to be challenged: how the category weights were set, and what was deliberately left out.

Everything here is judgement unless it cites a source. Where a number is judgement, I say so.

---

## 1. What this document does

1.1 Step 1 set out the framework. Step 2 fills it in. This document records why each weight is what it is, so that anyone reading the workbook can argue with the reasoning rather than only with the number.

1.2 The library contains 20 factors across the five categories required by regulation 18(2)(b)(i)–(v) of the Money Laundering Regulations 2017. Each factor has four or five defined levels, scored 1 to 5.

## 2. Why these five categories

2.1 The categories are not a design choice. Regulation 18(2)(b) requires a firm to take account of risk factors relating to its customers, the countries or geographic areas in which it operates, its products or services, its transactions, and its delivery channels. The model uses those five headings unchanged.

2.2 The one adaptation is that "transactions" is called **Expected activity**, because at onboarding there are no transactions yet. What the Bank has is a statement of intent: how much the customer expects to move, how much of it in cash, to whom, and where. That is what the category scores.

## 3. How the category weights were set

| Category | Weight | Reasoning |
|---|---|---|
| Customer | 30% | The heaviest weight, because who the customer is and what they do is the largest single block of information the Bank holds at onboarding and the one least likely to be wrong. |
| Geography | 25% | Weighted for the risk it *could* carry rather than the risk it usually does. This is the most questionable weight in the model and section 11.1 of the methodology says so. |
| Product and service | 20% | Inherent, verifiable, and independent of anything the customer says. A business current account with cash handling carries risk before a single transaction happens. |
| Delivery channel | 10% | Deliberately small. For a digital-first bank almost every customer arrives the same way, so the category cannot discriminate between them. A factor that gives nearly every customer the same score should not carry weight. |
| Expected activity | 15% | Forward-looking and self-declared, so it earns less weight than the categories built on evidence. It is kept because it is the only part of the file that can later be compared with what the customer actually did. |

3.1 The weights sum to 100%. The workbook checks this and will not read OK if an edit breaks it.

3.2 None of these weights is derived from loss data. No firm publishes the data that would allow that, and a personal project has no access to internal data. They are reasoned judgements, and Step 5 measures how much the model's output actually depends on each one.

## 4. How the factor weights were set within each category

4.1 The rule applied throughout: **a factor earns weight in proportion to how much it separates one customer from another.** A factor where 95% of the customer base scores the same number is not doing work, however serious the risk it names.

4.2 That rule explains most of the shape of the library:

- **C3 Industry or occupation** carries 25% of the customer category, the largest factor weight in it, because sector is the most informative and most varied thing the Bank knows about a business customer on day one.
- **G1 and G3 each carry 40%** of geography, with tax residence at 20%. G3 is the payment corridor. For a bank that only onboards UK residents, the corridor is where country risk actually arrives; the customer's own address is almost always the United Kingdom.
- **D1 Onboarding channel** carries 45% of a category that is itself only worth 10%, so its effective weight across the whole model is 4.5%. That is intentional. The channel matters, but not as much as its prominence in the regulations would suggest for this particular bank.
- **A2 Expected cash proportion** is the heaviest factor in expected activity at 30%, because cash is the mechanism that breaks the audit trail and the declared proportion is the single most testable statement the customer makes.
- **A5 Plausibility** carries the smallest weight in the model at 10% of a 15% category. It has the widest definition and the least weight on purpose: it exists so that an analyst who sees something that does not add up can record it inside the model rather than only in free text.

## 5. What is deliberately not a factor

5.1 **Nationality is not a risk factor in this model.** Country of residence, country of incorporation, country of tax residence and the expected payment corridor all are. Nationality is not.

5.2 There are two reasons. The first is that nationality is a protected characteristic under the Equality Act 2010. The second, and the one that matters for the model, is that it carries almost no information the other four geography inputs do not already carry, and it carries it about the person rather than about the money. A UK-resident customer with a UK account paying UK counterparties presents the same laundering risk whatever passport they hold.

5.3 A model that scores nationality produces higher ratings, then more enhanced due diligence, then more account closures, for whole groups of customers on a basis unconnected to the risk it claims to measure. The FCA's published position on de-risking is that the risk-based approach does not permit firms to "deal generically with whole categories of customers", and that there should be relatively few cases where a relationship has to be declined on anti-money laundering grounds alone. A risk model is where blanket de-risking begins, so it is where it has to be prevented.

5.4 Age, gender, and whether the customer receives benefits are excluded for the same reasons.

5.5 This exclusion is a design decision, not an oversight, and it is recorded here so that a reviewer who expects to find nationality in the library can see that it was considered and rejected.

## 6. How the levels were written

6.1 **Levels describe evidence, not judgement.** An analyst selects the level that matches what is on the file. They do not choose a number. A model where two competent analysts can defensibly score the same customer differently is not a model, it is an opinion with arithmetic attached.

6.2 **Where a declared figure straddles two levels, the higher level applies** (methodology 4.5). Without that rule, a customer declaring "£15,000 to £25,000 a month, about half in cash" could be scored two different ways by two people who agree on every fact.

6.3 **C4 has no level 2.** PEP screening returns a match or it does not; there is no state of being slightly a politically exposed person. Inventing a level 2 to make the scale look symmetrical would have made the model less honest, not more complete.

6.4 **A score of 5 and an automatic escalation mean the same thing.** Corrected after the Step 3 review. As first drafted, C2 level 5 covered both an ownership chain of three or more layers *and* the nominee, bearer-share and unevidenced cases, while escalator 5.3(d) covers only the second group. C3 level 5 had the same problem: it listed accountancy practices alongside the three business types in escalator 5.3(c). In both cases a customer could score 5 without meeting the escalator condition, so a model that fires the escalator on the score would have escalated customers it had no basis to escalate.

The fix is definitional rather than mechanical. C2 level 5 is now exactly the 5.3(d) condition, and a deep but fully evidenced ownership chain sits at level 4 however deep it goes, because if the Bank can evidence every layer it can still say who it is dealing with. C3 level 5 is now exactly the three business types in 5.3(c), and sectors the National Risk Assessment treats as vulnerable without an automatic escalation, including accountancy practices and registered cryptoasset businesses, sit at level 4.

6.5 **Some levels point at other factors.** P3 level 5 and A3 level 5 are both defined by reference to the country score at G3. This keeps the model internally consistent: the corridor cannot be low risk in one category and high risk in another.

6.6 **Some levels are drawn straight from enforcement.** A5 level 5 covers a declared profile that is not credible on the information held, "including an address that is a landmark or a non-residential building". That wording comes from the FCA's July 2025 final notice against Monzo, which records customers onboarded using well-known London landmarks as their address. D3 levels 4 and 5 turn on whether the introducing firm's entry on the Financial Services Register was checked, which is the failure the FCA fined Barclays Bank UK for in the same month.

## 7. Where the evidence for each factor sits

7.1 Every row of the `Factors` sheet carries a **Rationale** column and a **Source** column. The source is either a specific provision of the MLRs, a JMLSG chapter, an FCA publication, the National Risk Assessment, a FATF statement, a named final notice, or the words "an assumption of this model".

7.2 That last phrase appears on four factors: the monetary thresholds in P2, the turnover bands in A1, and the percentage bands in A2 and A3. Those numbers have no published source. They are Bank policy in the fiction, and my invention in fact, and they are labelled so that nobody has to guess which is which.

## 8. What the integrity checks prove, and what they do not

8.1 The `Checks` sheet runs thirteen tests: the weights sum correctly at every level, no factor code is duplicated, every level row points at a factor that exists, every factor has at least four levels, no score falls outside 1 to 5, no score is repeated within a factor, and the worked example still produces the number this project has published.

8.2 Two of them are more than arithmetic. Check 11 computes the lowest overall score the model can produce and check 12 the highest. They come out at exactly 1.00 and 5.00, which means every band defined in the methodology is reachable. Had the lowest achievable score been, say, 1.40, the bottom of the Low band would have been decoration.

8.3 What the checks do not prove is that the model is right. They prove it is internally consistent. A model can be perfectly consistent and still rate the wrong customers low, which is the entire reason Step 4 exists.

## 9. What Step 5 will do to these weights

9.1 Three tests, in order.

9.2 **Population distribution.** Score the synthetic population from Step 3 and count how many customers fall in each band. If the great majority land in Medium, the bands are wrong before the weights are.

9.3 **Weight sensitivity.** Change each category weight by ten percentage points in turn and count how many customers change band. A weight that moves nobody is not carrying risk, it is carrying arithmetic. My expectation, recorded now so it can be checked later, is that geography will move almost nobody and that the honest response will be to cut its weight and let the mandatory escalator at 5.3(b) carry country risk on its own.

9.4 **Band boundaries.** The worked example at 2.07 sits one hundredth of a point inside Medium. If a material share of the population clusters that close to a boundary, the boundary is in the wrong place.

---

## Appendix A — Sources

- The Money Laundering, Terrorist Financing and Transfer of Funds (Information on the Payer) Regulations 2017 (SI 2017/692), as amended — https://www.legislation.gov.uk/uksi/2017/692/contents
- JMLSG, *Guidance for the UK financial sector*, Part I, chapters 4 and 5 — https://www.jmlsg.org.uk/guidance/current-guidance/
- FCA, *Financial Crime Guide* — https://www.handbook.fca.org.uk/handbook/FCG/
- FCA, *De-risking: managing money-laundering risk* — https://www.fca.org.uk/firms/financial-crime/money-laundering-terrorist-financing/derisking-managing-risk
- FCA, *FG17/6: The treatment of politically exposed persons for anti-money laundering purposes*, as updated by *FG25/3* (July 2025) — https://www.fca.org.uk/publications/finalised-guidance/fg25-3-treatment-politically-exposed-persons
- HM Treasury and Home Office, *National Risk Assessment of Money Laundering and Terrorist Financing 2025* (July 2025) — https://www.gov.uk/government/collections/money-laundering-and-terrorist-financing-risk-assessments
- FATF, *High-Risk Jurisdictions subject to a Call for Action* and *Jurisdictions under Increased Monitoring*, statements of 19 June 2026 — https://www.fatf-gafi.org/en/countries/black-and-grey-lists.html
- FCA Final Notice, Monzo Bank Ltd, July 2025 — https://www.fca.org.uk/news/press-releases/fca-fines-monzo-21m-failings-financial-crime-controls
- FCA Final Notice, Barclays Bank UK plc, July 2025 — https://www.fca.org.uk/news/press-releases/fca-fines-barclays-42-million-poor-handling-financial-crime-risks
- Equality Act 2010 — https://www.legislation.gov.uk/ukpga/2010/15/contents

## Version history

| Version | Date | Change |
|---|---|---|
| 0.1 | Sept 2026 | First draft, issued with `model/risk-factor-library.xlsx` v0.1. |
| 0.2 | Sept 2026 | Review before Step 4. C2 and C3 level 5 redefined so that a score of 5 matches its escalator exactly (6.4). The unverified claim that the NRA 2025 rates the accountancy sector and TCSPs high risk was removed and replaced with what the NRA actually states. FG17/6 citation updated to note FG25/3 (July 2025). Document reference corrected from HND-CRA-002 to HND-CRA-003. |
