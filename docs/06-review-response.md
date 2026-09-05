# Response to the second-line review

**Firm:** Northgate Bank UK Limited (fictional)
**Document reference:** HND-CRA-010
**Version:** 0.3
**Author:** Saman Barati
**Date:** September 2026
**Companion files:** every document and workbook in this repository

---

### Why this document exists

The whole of this project was written by one person, and nobody had ever argued with it. That is the weakness a portfolio piece is least able to fix on its own, because the author cannot find the errors that come from the way he thinks.

So the finished pack — every document, both workbooks and the 400-customer population — was put through a **second-line model validation review** by a system that had not seen any of it before. The instruction was adversarial: assume the work contains errors, find them, name the file and the section for each, and do not praise anything unless the praise is load-bearing for a criticism. The prompt is in the repository history; it ends *"a review that finds nothing has failed, because no model of this kind is error-free."*

It found plenty. This document is what I did about it.

## 1. Whether the review was real

A review from a language model is worth nothing if the model is pattern-matching rather than reading. Three calibration questions were set before it started, with answers I already knew:

| | Question | Correct answer | Result |
|---|---|---|---|
| C1 | The effective weight of factor A5 across the whole model | 1.50% | Correct |
| C2 | The weighted score for back-test row FO-a, to four decimal places | 1.8225 | Correct |
| C3 | How many of the 98 level definitions carry a mandatory escalator reference | 10 | Correct |

The row put to the reviewer as `FO-a` is now labelled `FO-lo`; the file and the score are unchanged.

C2 is the one that matters. It cannot be answered without multiplying twenty scores by twenty weights and adding them up, and it cannot be guessed to four decimal places. Getting it right is evidence that the reviewer read the appendix rather than the prose.

The review returned 41 findings across five categories: factual errors, regulatory errors, analytical and arithmetic errors, over-claims, and presentation problems. I checked the substantive ones against primary sources — the FCA final notices, legislation.gov.uk, the FATF statements — rather than accepting them because they were confidently stated. That check is why three of them are rejected below.

This document is organised **by disposition rather than by the reviewer's numbering**. Several of the 41 were different statements of the same underlying defect — the Stunt & Co reconstruction alone generated findings in three categories — and a number restated weaknesses the validation pack and the generation notes already declared. Grouping them by what happened next is more useful to a reader than reproducing a list.

## 2. How to read the dispositions

| Marking | Meaning |
|---|---|
| **Accepted, fixed** | The finding was right and the work has been changed. The change is named. |
| **Accepted, recorded** | The finding was right, and the fix is a change to a weight, band or escalator. Methodology 8.1 requires MLRO approval for those, so it is written up and not applied. |
| **Accepted, defect fixed** | The finding was right and the fix makes the model do what the documented policy already said. Applied without approval; the distinction is at methodology 11.9a. |
| **Rejected** | I do not accept it, and the reason is given with the arithmetic. |

## 3. The finding that inverted a conclusion

**`backtest/cases/barclays-stunt-and-co.md` — the reconstruction contradicts the Final Notice. Accepted, fixed.**

I had built the Stunt & Co reconstruction as an empty file. The reasoning ran: the FCA's finding is that Barclays did not gather enough information, so the honest reconstruction records every unasked question at the level an unasked question produces, which is the benign one. That produced a score of 1.70, a rating of Low, and a satisfying conclusion — *the model cannot rate a file nobody filled in.*

The reviewer read the Final Notice. I had not, closely enough. It records what the file said:

| Paragraph | What Barclays held |
|---|---|
| 4.20(a) | The application recorded the business as "Gold Refining & Trading" |
| 4.20(c) | Anticipated turnover of £500,000, **manually amended to £3 million** |
| 4.20(d) | The company "would not trade outside of the EU" |
| 4.24 | Eleven days later: gold sourced from Ghana and Burkina Faso, sold to buyers in the Middle East |
| 4.35 | Barclays classified it low risk, with no recorded rationale |

Rebuilt from those paragraphs the customer scores 2.14 and is rated **High on 16 January 2015**, the day the account opened, because a gold refiner and trader is a dealer in high-value goods on the wording of C3 level 5 and that fires escalator 5.3(c).

Three things follow, and the third is the one I would not have found alone.

1. The old conclusion is withdrawn. It was drawn from a file that had in fact been filled in.
2. The back-test's headline changes. It is no longer "all six rated Low".
3. **The fix this project had already recommended would have removed the only control that caught this customer.** Step 5 recommends tying C3 level 5 to registration as a high value dealer rather than to a description of the trade, because the description is what makes the Fowler Oldfield reading ambiguous. Stunt & Co declared no cash and would probably not have been registered. The recommendation is now on the list marked contested, with that argument against it (`docs/04-model-validation.md`, 5.1).

I had written a fix, tested it on the case that motivated it, and never tested it on the case it would break. That is the error worth remembering out of all of this.

## 4. Findings accepted and fixed

### 4.1 The back-test could not have produced a different answer

**Accepted, fixed.** The back-test's headline was that no reconstruction reaches High on the arithmetic. The reviewer asked whether any of them could have. They could not, and I checked it myself rather than taking the point on trust:

| Case | Factors the notice settles at level 1 | Share of model weight | Highest score reachable |
|---|---|---|---|
| Fowler Oldfield | 9 | 41.50% | 3.34 |
| Santander | 9 | 40.75% | 3.37 |
| Stunt & Co | 9 | 43.00% | 3.28 |
| WealthTek | 9 | 43.00% | 3.28 |
| Monzo | 13 | 69.00% | 2.24 |
| Nationwide | 13 | 68.25% | 2.27 |

The High band begins at 3.50. Even pushing every remaining factor to 5, no reconstruction reaches it. A finding that is fixed by its inputs is not a finding.

This is now the first thing `backtest/README.md` says about its own results, and it is at `docs/04-model-validation.md` 1.3 before anything in that pack relies on the back-test. What survives is narrower and still worth having: the back-test can decide whether an escalator fires, and it can measure how far the answer moves between two defensible readings of the same file.

### 4.2 Twenty judgement calls, reported as one number

**Accepted, fixed.** Every reconstruction involves twenty decisions and the notices settle far fewer than twenty. Reporting a single score gave those decisions an authority they had not earned.

Every case is now scored at least twice — the reading most favourable to the customer that the notice permits, and the least favourable a competent analyst could have defended on the same information. Thirteen rows, from seven. The width of each pair is reported alongside the score, because it measures how much of the answer is mine rather than the file's.

### 4.3 The £480 million

**Accepted, fixed.** The arithmetic was right: the six notices carry £480,144,019.95 in penalties. The attribution was not. Those penalties were imposed for control failures across whole customer books over periods of years. Nationwide's £44.1m was not caused by one account.

The claim appeared in the README, the back-test summary and the LinkedIn document, and is corrected in all three. The wording is now that the six notices carry roughly £480 million between them, and that these customers are used because the notices describe them in enough detail to rebuild.

### 4.4 The 2026 instrument was cited from commentary

**Accepted, fixed.** `docs/05` rests entirely on what SI 2026/621 changes, and my source for it was a law firm's note on the draft. The note flagged that at 7.2, which is not the same as fixing it.

It now cites the made instrument. Regulation 19 of SI 2026/621 (made 9 June 2026) amends regulation 33(1)(b), (1)(f)(i) and (3)(a) of the 2017 Regulations, substituting "FATF call for action country" for "high-risk third country" and defining it as *"a country named on the list of High-Risk Jurisdictions subject to a Call for Action published by the Financial Action Task Force as such list has effect from time to time"*. Two things reading the instrument added that the commentary had not: the reference to the FATF list is **dynamic**, so the population in scope moves at every plenary with no UK instrument; and regulation 20 inserts a new **regulation 34A** extending mandatory EDD to cryptoasset exchange providers, custodian wallet providers and correspondent relationships from 1 February 2027. The instrument narrows one trigger and adds another, and calling it a relaxation was wrong.

### 4.5 Nationality and the Equality Act

**Accepted, fixed.** `docs/02` at 5.2 said nationality is a protected characteristic under the Equality Act 2010. It is not one of the characteristics listed at section 4. Section 9(1)(b) defines **race** as including colour, nationality and ethnic or national origins, so nationality is protected as an aspect of race.

The conclusion — do not score nationality — is unchanged. The route to it was wrong, and in a document whose argument is that every citation should be checkable, that is not a small thing.

### 4.6 The high-value-dealer reading of Fowler Oldfield

**Accepted, fixed.** Regulation 14 of the MLRs defines a high value dealer as a firm or sole trader trading in goods by way of business "when the trader makes or receives, in respect of any transaction, a payment or payments in cash of at least £10,000 in total". Nothing on the Fowler Oldfield file at onboarding recorded cash. So the reading was never available on the statutory definition.

(The threshold in regulation 14 was 10,000 euros until regulation 9 of SI 2026/621 redenominated it to £10,000 with effect from 30 June 2026. An earlier version of this response quoted the euro figure without the date, which is the kind of half-right citation the whole exercise is meant to catch.)

That sharpens the finding rather than removing it. The two readings really are both defensible **on the wording I wrote**, and the defect is therefore squarely in my level definition rather than in the analyst reading it. The case file says so now.

### 4.7 The circularity, the workload limit, and the population properties

Three admissions were in the documents already, filed under limitations at the back. The reviewer's point was that a caveat a reader meets after believing the finding is not a caveat. All three have been moved to where the conclusion is drawn.

- **The band boundaries are fitted to a population I invented.** Was `docs/04` 8.2; now 5.3, inside the recommendation itself.
- **"A bank cannot apply EDD to a third of its customers" is an unsourced threshold.** Was 8.3; now 4.2, in the section where it decides the answer. That section now says plainly that the number is an intuition about cost dressed as a constraint, and that the first question a real second line would ask is what the firm's actual EDD capacity is.
- **Findings presented as properties of the model that are properties of the population.** Every one is now listed in a single place at `docs/03` 5.2a: the band shares, the category statistics, "no personal customer is rated Medium", the 37 customers near the boundary, the eight uncaught cash-intensive customers.

### 4.8 An arithmetic error in the sensitivity claim

**Accepted, fixed.** `docs/04` 3.2 said rebanding moves "between three and six times as many" customers. Scenario by scenario the ratio runs from **2.6 to 11.8**. The figure is now computed from the workbook rather than typed, as every other figure in that document already was.

### 4.9 The count of back-test rows that move under the recommendation

**Accepted, fixed.** Section 6 said five rows moved from Low to Medium; four did. The sentence is now generated from the workbook, so it cannot be wrong again. On the current thirteen-row back-test, five rows change rating: three from Low to Medium and two from Low to High.

## 5. Findings accepted and recorded, awaiting approval

### 5.1 The PEP escalator does not comply with regulation 35(3A)

**Accepted, recorded.** Regulation 35(3A), in force from 10 January 2024, requires that where a PEP is entrusted with a prominent public function **by the United Kingdom**, the starting point is that they present a lower level of risk than a non-domestic PEP, and that where no enhanced risk factors are present the measures applied must be less extensive.

Escalator 5.3(a) rates a foreign PEP, a domestic PEP and a PEP's parent High, identically. Requiring EDD for all of them is not the error — regulation 35(1) requires it. The error is producing an output that cannot distinguish them, which makes the differentiation 35(3A) requires impossible to evidence. Factor C4 compounds it by collapsing the family members and associates of foreign and domestic PEPs into one level.

On the current population this affects 11 customers: one foreign PEP, three domestic PEPs and seven family members or associates. Recorded at methodology 11.13, in `docs/02` 6.3a, and as change 4 in the validation pack. Not applied: it is a change to an escalator.

### 5.2 The escalator sweep

The reviewer asked whether every escalator condition matches the level definition that triggers it. Four answers, and they do not all go the same way.

| Condition | Finding | Disposition |
|---|---|---|
| 5.3(d) vs C1 level 5 | The library said C1 level 5 triggers 5.3(d) "only where nominee shareholders or bearer shares are present". C1 level 5 covers trusts, nominee arrangements and overseas incorporation as one level, so the condition cannot be evaluated from the recorded level — and the model was not firing it on C1 at all. | **Accepted, defect fixed.** The escalator now fires on the whole of C1 level 5. Conservative rather than correct; the proper fix is to split the level, which needs approval. Three customers move to High. |
| 5.3(b) vs G3 level 5 | The escalator said "established in", tracking regulation 33(1)(b). The model has always fired on G3, which records payment corridors, not establishment. | **Accepted, defect fixed.** The escalator is reworded to describe what the control does. Firing on corridors is wider than regulation 33(1) requires, which regulation 33(1) permits — it is a floor. No ratings change; the documentation was what was wrong. |
| 5.3(b) vs the beneficial owner | Both the escalator and regulation 33(1)(b) refer to the customer **or a beneficial owner**. No factor records where a beneficial owner is established. | **Accepted, recorded** at methodology 11.14. A UK-resident customer whose beneficial owner sits in a Call for Action jurisdiction is caught by nothing in this model. |
| 5.3(a) vs C4 | See 5.1 above. | Accepted, recorded. |

### 5.3 Gaps the back-test rebuild exposed

Three more, all recorded and none applied, all of them found by rebuilding cases the review made me rebuild:

- **11.10** — factor C5 has no level for screening that was run and never reviewed, which is what paragraph 4.37 of the Barclays notice describes. The model treats it as a clear result.
- **11.11** — nothing in the library asks whether the customer holds the permissions its stated business requires. That is the entire WealthTek case. Factor D3 mentions the Financial Services Register, but only for an *introducing* firm.
- **11.12** — the C3 scale has no level for a customer that is itself an authorised financial firm. Level 2 is explicitly "outside the financial sector". WealthTek is forced into it.

### 5.4 Governance, or an excuse?

The review asked whether "no change applied, because approval is required" is governance or a way of avoiding work. It is a fair question and the honest answer is that the original wording could not tell the difference.

Methodology 11.9a now draws the line. A **calibration change** alters the documented policy and needs someone other than the model's author to own it. A **defect fix** makes the implementation do what the policy already says, and refusing to make one is not governance. Two defect fixes have been applied on that basis and logged; everything else on the list is a calibration change and is still waiting.

## 6. Findings I do not accept

Three, with the working. Where the review was right I changed the work; where I think it is wrong I would rather be argued with than quietly agree.

### 6.1 The Rule B table is not internally contradictory

**Rejected as an error. Accepted as an ambiguity.**

The finding was that `docs/04` cannot be right in both places: 49 customers score above 2.20, but the rule B row reports 74 in High.

Both figures are correct and they measure different things. 49 is the count of customers whose **score** exceeds 2.20. 74 is the **final rating** under rule B, which applies the mandatory escalators on top of the arithmetic, exactly as rule A does. 25 escalated customers score at or below 2.20, and 49 + 25 = 74.

What the reviewer is right about is that the document never said the table was of final ratings. It does now, at 4.1, with the reconciliation spelled out. A figure a reader cannot reconcile is a defect in the document even when the number is correct.

### 6.2 The SAR rate is sampling variance, not a discrepancy

**Rejected.**

The finding was that `data/generation-notes.md` states a SAR rate of 1.5% at point 4 and reports 11 of 400 (2.8%) at section 5.

1.5% is the **parameter** given to the generator. 2.8% is the **realised draw** from one fixed seed. With p = 0.015 and n = 400 the expected count is 6.0 with a standard deviation of 2.43, so 11 sits 2.1 standard deviations high — a result a single seed produces roughly one time in twenty-five. Unremarkable, and reproducible: the seed is fixed at 20260902.

Every count in this project is computed from the realised data, never from the parameter, so nothing downstream is affected. But the document reported both figures and explained neither, which is why a careful reader flagged it, so the explanation is now in the generation notes.

### 6.3 Library checks 11 and 12 are redundant, not vacuous

**Partly accepted.**

The finding was that checks 11 and 12 in the risk factor library — the lowest and highest achievable overall scores — cannot fail, and that presenting them as the two that "matter most" is misleading.

The first half is right. Given check 9 (every factor's lowest level is 1), check 10 (every factor's highest level is 5) and checks 1 to 3 (the weights sum to 100% at every level), a range of 1.00 to 5.00 follows by arithmetic. They add nothing about the level definitions, and the note under the table claimed they did. That note is rewritten.

The second half I do not accept. Checks 11 and 12 evaluate the **aggregation formula itself** — the same weighted sum the Scoring sheet uses — so a mistyped range or a transposed weight vector fails there and nowhere else in that workbook. They test something checks 9 and 10 cannot. They are kept on that ground, described accurately, and `docs/02` 8.2b now makes the general point: a check that restates its own premises is decoration, and counting decorations as assurance measures the wrong thing.

## 7. What the review did not find

Listing this is the point of the exercise, so:

- **The reconstructions are still mine.** Reporting a range is honest about that; it does not remove it. Choosing what counts as "the worst reading a competent analyst could have defended" is itself twenty more judgement calls, made by the same person, in the same direction his instincts run.
- **Six enforcement notices are a survivorship sample.** They are the six that were published, prosecuted and reported. Firms that failed without being fined are not in it, and neither is the false positive side — customers who looked terrible and turned out fine. This project has no way to see that at all, and it is the half of model performance a real validation would spend most of its time on.
- **There is still no human review.** A second language model is not second line. It found errors a person would have found, and it will have missed errors a person would have caught.

## 8. What this cost, and what it was worth

Six documents changed, two workbooks re-run, one published conclusion withdrawn and one recommendation marked contested by the evidence that produced it.

The finding I would keep out of all 41 is the third-order one at section 3: I wrote a fix, tested it against the case that motivated it, and never asked what else it would touch. Nothing in my own review process would have caught that, because the process was me.

## 9. The pre-publication fact check

The review above was about the model. Before publishing anything, every external fact in the repository
was checked separately against the primary source — each penalty, date, legal entity name, quoted
finding and regulatory citation, against the FCA's own final notices and press releases,
legislation.gov.uk, the FATF statements and gov.uk. Nothing was confirmed from memory.

Nine things were wrong. They are listed here rather than quietly corrected, because a document that
claims its citations are checkable should show what happened when they were checked.

| | What was published | What the source says |
|---|---|---|
| 1 | The Santander account was closed "thirty months" after the internal recommendation to close it | March 2014 to September 2015 is **eighteen months**. The decision to close was taken in April 2015 and not actioned until September. |
| 2 | At the start of the NatWest relationship "the bank understood that the customer would not be handling cash" | The FCA records this as the **bank's** understanding about **itself**: "NatWest initially understood it would not handle cash from the Fowler Oldfield business". Not a customer declaration. This changes what the case shows, and the case file now says so. |
| 3 | Cash arrived "in bags with a distinctive smell" | Two separate findings at two different branches, fused into one. The musty smell attaches to notes at a cash centre; the bin liners are a different account entirely. |
| 4 | £365 million "passed through the account" | The FCA says £365 million was **deposited with the bank**. |
| 5 | The WealthTek case cited the Barclays Bank Plc final notice | WealthTek is **Barclays Bank UK Plc** and has its **own** final notice. Two entities, two notices, one press release. Citing one for both is exactly the error a reader can check in thirty seconds. |
| 6 | £298 million passed through "problem business accounts" at Santander | Six **Money Service Business** customers, roughly £269 million of it a single customer. |
| 7 | A high value dealer accepts cash payments of "€10,000 or more" (regulation 14) | The threshold was redenominated to **£10,000** by regulation 9 of SI 2026/621 with effect from 30 June 2026, and the test is "makes or receives... at least £10,000". |
| 8 | Various "July 2025" and "December 2025" dates | Final notices: both Barclays 14 July 2025 (announced 16 July), Nationwide 11 December 2025 (announced 12 December). **The Monzo and Santander dates given in this row were themselves still wrong when it was written — see 10.3.** |
| 9 | The de-risking passage was part quotation, part paraphrase, presented as one quotation | Both sentences are now quoted in the FCA's own words, from the correct URL, and identified as a webpage rather than finalised guidance. |

Two things survived the check that I had expected to lose. The £480 million total is correct arithmetic
on the published figures — though it mixes a Crown Court criminal fine with five FCA penalties, which
the back-test summary now says out loud. And the FATF counts are right: three jurisdictions subject to
a Call for Action and 22 under Increased Monitoring, both statements dated 19 June 2026 from the
plenary of 17 to 19 June.

The pattern in that table is worth naming. Not one of the nine is an invented fact. All nine are real
facts that drifted — a number rounded into a different number, two findings compressed into one
sentence, a source cited one level too far from the document that actually says it. That is what
happens when you write from notes instead of from the notice, and it is the failure mode a reader can
catch fastest.

## 10. The second review, and what it found in the corrections

Section 9 says nine facts had drifted and that all nine were real facts rather than invented ones. Both
statements were true. What section 9 implied — that the checking was now finished — was not.

The finished repository was reviewed once more before anything was announced. That review found nine
further problems, three of them serious, and they are listed here for the same reason as the first nine.

**10.1 The acquittal.** The Stunt & Co case file described the customer as part of "the same laundering
operation that produced the NatWest prosecution" and never mentioned paragraph 2.7 of the very notice it
cited, which records that **on 4 March 2025 James Stunt was acquitted** of money laundering charges in
relation to those monies, on the basis that he had no knowledge or suspicion that they were criminal
property. A footer saying the file is "not a criticism of any individual" does not cure that; quoting
2.7 does. It is now the first thing that case file says, the gloss is gone, and the reconstruction table
names the company and the role rather than the individual.

It is worth being exact about the class of error, because it is not the class the first review found.
This was not a wrong number. It was a fact I never went looking for, in a document I had already read
for other purposes, about a living person.

**10.2 Santander was an onboarding failure, and I had concluded it was not.** The case file said the
customer was rated correctly and the failure was entirely in monitoring. The Final Notice records that
the customer operated a **money service business** and that Santander did not identify it as one at
onboarding. Verified, that customer is High on day one through escalator 5.3(c). The case has been
rebuilt, the conclusion reversed, and it has produced the strongest finding in the whole back-test:
methodology 11.15. It is also the same error as the original Stunt & Co mistake — reconstructing from a
press release and a narrative rather than from the notice — repeated on the one case where the earlier
version claimed the model had got it right.

**10.3 Three notice dates were still wrong**, in the document that had just finished congratulating
itself on checking dates. Monzo's notice is dated 7 July 2025 and Santander's 8 December 2022; both had
been given their press release dates. The Barclays Bank Plc notice is dated 14 July 2025, which section
9 states correctly and the source list of this document then contradicted.

**10.4 A broken sentence in the most-read paragraph of the back-test**, left behind by an unfinished
edit: a heading saying one case was caught, over a sentence saying two, ungrammatically. The answer is
three.

**10.5 The reproducibility claim was not true.** `data/generation-notes.md` said the population could be
regenerated from `build/generate.py`, and `build/` was not in the repository. It is now, with every
other script that produces anything here.

**10.6 Five smaller things.** The 24 Nationwide furlough payments totalled £1.35m over thirteen months,
followed by £26.01m over eight days; the file had fused the two figures. Factor G2 records a further
**tax residence**, and the escalator and the population labels both called it a second residence. C4
level 3 covered the relatives of a domestic PEP only, leaving a foreign PEP's relative with nowhere to
be recorded — a worse defect than the one documented at 5.1. The nine-factor arithmetic at `docs/03` 4.2
needs two of the three 5% factors at level 5, not one. And `docs/03` 5.2a, which claims to list every
population property this project states as a model property, was missing the two most quoted numbers in
the document.

**What this round says about the first one.** Two reviews, and the second found a defect worse than
anything in the first. The conclusion is not that the work is now clean. It is that any single reviewer
finds a fraction of what is there, and that the fraction they find is not ordered by seriousness.

---

## Sources checked in preparing this response

- FCA Final Notice, Barclays Bank Plc, 14 July 2025 — https://www.fca.org.uk/publication/final-notices/barclays-bank-plc-2025.pdf
- Regulation 33 of SI 2017/692, as amended — https://www.legislation.gov.uk/uksi/2017/692/regulation/33
- Regulation 35 of SI 2017/692, including paragraph (3A) — https://www.legislation.gov.uk/uksi/2017/692/regulation/35
- The Money Laundering and Terrorist Financing (Amendment) Regulations 2026 (SI 2026/621), as made — https://www.legislation.gov.uk/uksi/2026/621/made
- SI 2026/621, regulation 19 — https://www.legislation.gov.uk/uksi/2026/621/regulation/19/made
- Equality Act 2010, sections 4 and 9 — https://www.legislation.gov.uk/ukpga/2010/15/section/9
- Regulation 14 of SI 2017/692 (high value dealers), and regulation 9 of SI 2026/621 which redenominated its threshold — https://www.legislation.gov.uk/uksi/2017/692/regulation/14
- FCA agreed statement of facts, FCA v National Westminster Bank Plc — https://www.fca.org.uk/publication/corporate/agreed-statement-facts-fca-national-westminster-bank.pdf
- FCA Final Notice, Barclays Bank UK Plc (WealthTek), 14 July 2025 — https://www.fca.org.uk/publication/final-notices/barclays-bank-uk-plc-2025.pdf
- FCA Final Notice, Santander UK Plc, 8 December 2022 — https://www.fca.org.uk/publication/final-notices/santander-uk-plc-2022.pdf
- FCA Final Notice, Monzo Bank Limited, 7 July 2025 — https://www.fca.org.uk/publication/final-notices/monzo-bank-limited.pdf
- FCA Final Notice, Nationwide Building Society, 11 December 2025 — https://www.fca.org.uk/publication/final-notices/nationwide-building-society-2025.pdf

## Version history

| Version | Date | Change |
|---|---|---|
| 0.3 | Sept 2026 | Second pre-publication review, at section 10: the Stunt & Co acquittal, the Santander conclusion reversed, and nine further corrections. |
| 0.2 | Sept 2026 | Pre-publication fact check of every enforcement figure, date, entity name and regulatory citation against the primary source. Nine corrections, listed at section 9. |
| 0.1 | Sept 2026 | First issue, following the external second-line review. |
