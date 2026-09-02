# Customer Risk Assessment Methodology

**Firm:** Northgate Bank UK Limited (fictional)
**Document reference:** HND-CRA-001
**Version:** 0.1 (draft)
**Author:** Saman Barati
**Date:** September 2026
**Review:** on completion of Step 5, or on any material amendment to the Money Laundering Regulations

---

### Author's note

Northgate Bank does not exist. I invented it so the model has a fixed perimeter to sit inside, because a risk methodology written for "a bank" in the abstract can justify any weighting it likes. Everything below is written as a real methodology document would be written, in the third person, because that is the register these documents are actually in.

Two things this document is not. It is not professional compliance advice, and it has not been through the second-line challenge that any real methodology would go through before approval. Section 11 lists the decisions I am least sure about, which is the closest a one-person project can get to a challenge log.

---

## 1. Purpose

1.1 This document sets out how Northgate Bank UK Limited ("the Bank") assigns a money laundering and terrorist financing risk rating to each customer at the point of onboarding, and how that rating is maintained for the life of the relationship.

1.2 The rating drives three decisions: the level of customer due diligence applied, how often the customer file is refreshed, and the sensitivity of ongoing monitoring applied to the account.

1.3 This is the **customer** risk assessment. It sits beneath the firm-wide risk assessment required by regulation 18 of the Money Laundering Regulations 2017 and takes its risk appetite from it. The two are separate documents and this one does not replace the other.

## 2. Scope

2.1 **Customers in scope.** All customers onboarded to:

- personal current accounts, instant-access savings, personal loans and credit cards
- business current accounts and business overdrafts for sole traders, partnerships and UK-incorporated limited companies with annual turnover up to £2 million

2.2 **Not offered by the Bank, and therefore out of scope.** Correspondent banking, trade finance, private banking and wealth management, cryptoasset services, foreign currency accounts, and customers not resident in the United Kingdom at the point of onboarding.

2.3 **Controls that sit outside this document.** Sanctions, PEP and adverse media screening; transaction monitoring rules and alert handling; suspicious activity reporting; and the firm-wide risk assessment. This model *consumes* the output of screening as an input. It does not perform screening, and a screening match is not resolved by a risk score.

## 3. Regulatory basis

| Source | What it drives in this document |
|---|---|
| MLRs 2017, reg. 18 — Risk assessment by relevant persons | The five risk categories in section 4 follow the factors listed at reg. 18(2)(b)(i)-(v) |
| MLRs 2017, reg. 19 and 21 — Policies, controls and procedures; internal controls | Governance, override approval and record-keeping in section 8 |
| MLRs 2017, reg. 27, 28 and 30 — When CDD applies, CDD measures, timing | Band consequences in section 6 |
| MLRs 2017, reg. 31 — Requirement to cease transactions | Prohibited relationships at 5.4 |
| MLRs 2017, reg. 33 — Enhanced customer due diligence | High band treatment and the geography escalator at 5.3 |
| MLRs 2017, reg. 35 — EDD: politically exposed persons | The PEP escalator at 5.3 |
| MLRs 2017, reg. 37 — Simplified customer due diligence | Low band treatment at section 6 |
| JMLSG Guidance, Part I, chapters 4 and 5 | The structure of the risk-based approach and the CDD standards behind each band |
| FCA Financial Crime Guide, FCG 3 | Expectations on customer risk assessment and ongoing monitoring |
| HM Treasury / Home Office National Risk Assessment | Sector and product risk scores in Step 2 |
| FATF public statements (Call for Action; Increased Monitoring) | Country scoring and the geography escalator |
| The Money Laundering and Terrorist Financing (Amendment) Regulations 2026 | The change to jurisdiction-based EDD tested in Step 5 |

## 4. Risk factor framework

4.1 Regulation 18(2)(b) requires a firm to take account of risk factors relating to its customers, the countries or geographic areas it operates in, its products and services, its transactions, and its delivery channels. The model uses those five headings unchanged, so that the mapping between the regulation and the model is direct and can be checked by anyone reading both.

| # | Category | Weight | What it captures |
|---|---|---|---|
| C | Customer | 30% | Legal form, ownership and control structure, occupation or sector, PEP status, adverse media, transparency of the beneficial ownership chain |
| G | Geography | 25% | Country of residence or incorporation, country of tax residence, countries of expected counterparties, FATF and HM Treasury listings |
| P | Product and service | 20% | Inherent characteristics of the products taken: cash handling, third-party payments, international payments, anonymity, speed |
| D | Delivery channel | 10% | How the relationship was established and is operated: face-to-face, digital with electronic ID verification, intermediated |
| A | Expected activity | 15% | Turnover, expected cash proportion, expected international exposure and counterparty types, as stated at onboarding |

4.2 The weights above are **provisional**. Step 2 documents the reasoning and the source behind each one; Step 5 tests how much the output moves when each weight is changed. They should not be treated as settled until both are done.

4.3 Each factor within a category is scored on a five-point scale:

| Score | Meaning |
|---|---|
| 1 | Low. No feature that increases risk above the Bank's baseline. |
| 2 | Low to moderate. A feature that increases risk marginally. |
| 3 | Moderate. A recognised risk feature, common in the customer base, manageable with standard controls. |
| 4 | Elevated. A recognised risk feature that materially reduces the Bank's visibility of the customer or the source of funds. |
| 5 | High. A feature identified as high risk by the MLRs, JMLSG, the National Risk Assessment or FATF. |

4.4 Every factor has a written definition of what each score means for that specific factor. Analysts do not exercise judgement on the number; they select the level that matches the evidence on file. This is deliberate. A model where two analysts can defensibly score the same customer differently is not a model.

4.5 Where a customer's declared figure straddles two levels - a range of expected cash deposits that spans a threshold, for example - the higher level applies. This is recorded here rather than left to the analyst, so that two people scoring the same file reach the same number.

## 5. Calculating the rating

5.1 **Category score.** Each category score is the weighted average of the factor scores within it, on the same 1 to 5 scale.

5.2 **Overall score.** The overall score is the sum of each category score multiplied by its category weight, producing a figure between 1.00 and 5.00, rounded to two decimal places.

```
Overall = 0.30·C + 0.25·G + 0.20·P + 0.10·D + 0.15·A
```

**Bands:**

| Band | Score |
|---|---|
| Low | 1.00 – 2.00 |
| Medium | 2.01 – 3.49 |
| High | 3.50 – 5.00 |

5.3 **Mandatory escalators.** The following rate the customer High regardless of the arithmetic. The purpose of this list is to stop a weighted average from diluting a single severe factor.

- (a) the customer, a beneficial owner or a person exercising control is a politically exposed person, a family member or a known close associate (reg. 35)
- (b) the customer or a beneficial owner is established in a jurisdiction identified by FATF as a High-Risk Jurisdiction subject to a Call for Action
- (c) the customer is a money service business, a trust or company service provider, or a dealer in high-value goods
- (d) the ownership structure includes nominee shareholders, bearer shares, or an entity incorporated in a jurisdiction with no accessible beneficial ownership register
- (e) screening returns a confirmed adverse media match relating to financial crime, fraud, bribery, corruption or tax evasion
- (f) a suspicious activity report has been submitted in respect of the customer in the preceding twelve months

5.4 **Prohibited relationships.** These are not rated. The application is declined, or an existing relationship is referred for exit, under the Bank's exit procedure.

- (a) a confirmed sanctions match — referred immediately to the Sanctions team and handled under the sanctions procedure, not under this document
- (b) shell banks
- (c) a money service business or cryptoasset business operating in the UK without the registration it is required to hold
- (d) the customer does not provide information the Bank needs to complete CDD (reg. 31)
- (e) the Bank cannot identify the beneficial owner or is not satisfied it knows who they are

5.5 **Overrides.**

- An analyst may override a rating **upwards** without approval. The reason is recorded.
- An override **downwards** requires approval from the MLRO or a delegate and a written rationale on the customer file.
- No override may take a customer below Medium where a mandatory escalator at 5.3 applies.
- All overrides are recorded in the override register and reviewed quarterly. If overrides exceed 5% of ratings issued in a quarter, the model is treated as needing recalibration. A high override rate is evidence about the model, not about the analysts.

5.6 **Worked example.**

Customer 4417. Sole trader, UK resident, onboarded through the mobile app with electronic identity verification. Trades in used motor vehicles. Declares turnover of £15,000 to £25,000 a month, of which roughly half is expected in cash. No adverse media, no PEP match, simple ownership.

Scored against the risk factor library built in Step 2 (`model/risk-factor-library.xlsx`, sheet `Example`):

| Category | Score | Weight | Contribution |
|---|---|---|---|
| Customer | 1.95 | 30% | 0.5850 |
| Geography | 1.00 | 25% | 0.2500 |
| Product and service | 3.05 | 20% | 0.6100 |
| Delivery channel | 2.60 | 10% | 0.2600 |
| Expected activity | 2.45 | 15% | 0.3675 |
| **Overall** | | | **2.0725, rounded to 2.07 - Medium** |

2.07 sits one hundredth of a point above the Low boundary. A sole trader in a cash-intensive sector, onboarded without ever being seen, expecting to take half of a five-figure monthly turnover in cash, is rated barely above the Bank's lowest band.

Two things produce that result. The customer category scores 1.95 because four of its five factors are clean and only the sector score is elevated. The geography category scores the minimum possible 1.00 and, at a weight of 25%, holds a quarter of the model at the floor.

Whether that is the right answer is precisely what Step 4 exists to find out. It is also the first evidence for the concerns recorded at 11.1 and 11.2.

## 6. What each band means

| | Low | Medium | High |
|---|---|---|---|
| Due diligence | Simplified CDD where the reg. 37 conditions are met | Standard CDD | Enhanced CDD under reg. 33 |
| Source of funds | Not required at onboarding | Required where activity is inconsistent with the profile | Required at onboarding |
| Source of wealth | Not required | Not required | Required for PEPs and where the profile does not explain the funds |
| Approval to onboard | Automated | Analyst | Senior management |
| File refresh | 5 years | 3 years | 12 months |
| Monitoring | Standard thresholds | Standard thresholds | Reduced thresholds and a named reviewer |

## 7. Keeping the rating current

7.1 A rating produced at onboarding describes the customer on the day they were onboarded. It is at its most accurate on that day and decays from then on. Periodic refresh at the intervals in section 6 is the floor, not the control.

7.2 **Event-driven triggers.** Any of the following causes an immediate re-rating, irrespective of when the file is next due for refresh:

- (a) a screening alert — sanctions, PEP or adverse media
- (b) a change in beneficial ownership or control
- (c) a change of address, registered office or tax residence to a higher-risk country
- (d) business activity identified on a personal account, or personal activity on a business account
- (e) activity materially inconsistent with the expected activity recorded at onboarding
- (f) submission of a suspicious activity report
- (g) the customer takes a product with a higher inherent risk score
- (h) a law enforcement enquiry or production order relating to the customer
- (i) a change by FATF, HM Treasury or the FCA to the status of a country relevant to the customer

7.3 Trigger (d) is included on the basis of published enforcement. The FCA's final notice against Nationwide Building Society of December 2025 records that the society was aware customers were conducting business activity through personal current accounts in breach of its terms, and did not have processes in place to manage the financial crime risk that created. A trigger that fires on the same fact pattern is a direct response to that finding.

## 8. Governance and records

8.1 The MLRO owns this methodology. Changes to weights, bands, escalators or the prohibited list require MLRO approval and are version-controlled in this document.

8.2 For every rating the Bank retains the factor scores, the category scores, the overall score, the band, the date, the analyst, and any override with its rationale. A rating that cannot be reconstructed from the record is treated as not evidenced.

8.3 The model is reviewed annually and on any material amendment to the MLRs, any change to the FATF lists that affects a material part of the customer base, or any finding from internal audit or the FCA.

## 9. Data

9.1 Customer risk data is personal data and is processed under the UK GDPR and the Data Protection Act 2018, on the basis of the Bank's legal obligation under the MLRs.

9.2 This project uses **synthetic data only**. No real customer data is used, held or referenced anywhere in this repository. The generation method and its assumptions are documented in `data/generation-notes.md`.

## 10. Known limitations

10.1 This is a rating model. It decides how closely a customer is looked at. It does not detect money laundering, and a Low rating is not a finding that the customer is clean.

10.2 The rating is a point-in-time judgement that decays between refresh points. Between those points the model depends on the trigger list at 7.2 being complete, and it will not be complete.

10.3 Factor scores are ordinal but are treated as cardinal in the weighted average. The distance between a 3 and a 4 is not necessarily the same as the distance between a 1 and a 2. This is a simplification made for tractability and it is a real weakness.

10.4 The weights are judgement, informed by published sources but not derived from loss data, because no loss data is available to a project of this kind.

10.5 A weighted average dilutes single severe factors by design. The escalator list at 5.3 is the compensating control, which means the model is only as good as the judgement about what belongs on that list.

10.6 The model has not been independently validated. The author wrote it, tested it and reviewed it, which is not an arrangement any firm would accept and is the clearest difference between this and a production model.

## 11. Decisions I am least confident about

11.1 **The 25% weight on geography.** Northgate is a UK-only retail bank. Almost every customer will score 1 or 2 here, which means a quarter of the model's weight may be doing nothing except dragging every average downwards and pushing the population into Low. If Step 5 confirms that, the answer is probably to cut the weight and let the escalator at 5.3(b) carry the country risk on its own.

11.2 **The width of the Medium band.** 2.01 to 3.49 is a wide space. If most of the population lands in it, the model is not discriminating between customers, it is just producing a number. The population distribution in Step 5 will show this immediately, and the fix is to move the boundaries rather than the weights.

11.3 **Whether expected activity belongs in an onboarding model at all.** It is self-declared, unverified on the day, and a customer intending to misuse the account has every reason to state something ordinary. It may be more honest to score it at onboarding for the record and give it no weight until the first refresh, when declared activity can be compared with real activity.

11.4 **Cash-intensive sole traders.** The worked example at 5.6 lands at 2.07, one hundredth of a point above Low, and my instinct says it should be High. Instinct is not evidence, which is why Step 4 tests the model against customers already known to have caused harm rather than against my intuition. If the back-test agrees with my instinct, the fix is more likely to be in the category weights at 4.1 than in the level definitions.

11.5 **Whether the High band can be reached by the arithmetic at all.** Added after Step 3. Scored against the risk factor library, not one of the 400 customers in the synthetic population reached the High band on the weighted average; the highest score anywhere was 2.76 against a threshold of 3.50, and all 40 High ratings came from the mandatory escalators at 5.3. Working down from the heaviest factor, the nine heaviest would all have to score 5, with every remaining factor at 1, for a customer to reach exactly 3.50. Paragraph 10.5 already says a weighted average dilutes single severe factors and that the escalator list is the compensating control. What Step 3 shows is that on this population the escalators are not compensating at the margin, they are doing all of the work at the top of the scale. Step 5 has to decide whether the answer is to move the boundaries, to re-weight, or to change the aggregation rule itself. The evidence is in `docs/03-model-build.md`, section 4.

11.6 **The C3 level 5 definition is ambiguous and I now know it.** Added after Step 4. Fowler Oldfield was a jewellery business. Read as a cash-intensive trade it scores 4; read as a dealer in high-value goods it scores 5 and triggers escalator 5.3(c). Both readings are defensible on the current wording, and they produce Low and High respectively on the customer behind the FCA's first criminal prosecution of a bank. The level must turn on a checkable fact - whether the customer is registered with HMRC as a high value dealer - rather than on a description of the trade. See `backtest/cases/natwest-fowler-oldfield.md`.

11.7 **A5 is the right factor carrying the wrong weight.** Added after Step 4. Level 5 of A5 was written from the Monzo notice to capture a declared profile that cannot be true, such as an address that is a well-known landmark. Scored through the model, such a customer reaches 1.52 and is rated Low, because A5 carries 1.5% of the effective weight. A fact that cannot be true is not a small increase in risk; it is a failure to identify the customer. Step 5 should move it out of the weighted average and onto the escalator or prohibited list. See `backtest/cases/monzo-landmark-address.md`.

11.8 **Nothing in the library scores how complete the file is.** Added after Step 4. Reconstructing the Stunt & Co relationship as the FCA describes it - a file where not enough information was gathered at the start - produces the lowest business score in the back-test, because every unasked question sits at its benign level. A missing answer and a reassuring answer are indistinguishable to this model. See `backtest/cases/barclays-stunt-and-co.md`.

11.9 **The weights were never the thing that mattered.** Added after Step 5. Moving any category weight by ten percentage points changes the band of at most 26 customers out of 400, and setting the delivery channel weight to zero changes 14. Against band boundaries placed where the population actually sits, the same changes move between 29 and 100. The boundaries decide this model's output; the weights barely touch it. Section 4.2 of this document says the weights are provisional pending Step 5. They are now provisional pending a boundary change, which has to come first. The validation pack recommends moving the boundaries to 1.60 and 2.20, moving A5 level 5 onto the escalator list, and adding a file-completeness factor. **None of those changes has been made to this methodology**, because paragraph 8.1 requires MLRO approval for any change to weights, bands or escalators. They are recorded in `docs/04-model-validation.md` section 9 and await that approval.

---

## Appendix A — Sources

- The Money Laundering, Terrorist Financing and Transfer of Funds (Information on the Payer) Regulations 2017 (SI 2017/692), as amended — https://www.legislation.gov.uk/uksi/2017/692/contents
- The Money Laundering and Terrorist Financing (Amendment) Regulations 2026 — https://www.legislation.gov.uk/ukdsi/2026/9780348281743
- JMLSG, *Prevention of money laundering / combating terrorist financing: Guidance for the UK financial sector*, Part I — https://www.jmlsg.org.uk/guidance/current-guidance/
- FCA, *Financial Crime Guide: A firm's guide to countering financial crime risks* — https://www.handbook.fca.org.uk/handbook/FCG/
- FATF, *High-Risk Jurisdictions subject to a Call for Action* and *Jurisdictions under Increased Monitoring* — https://www.fatf-gafi.org/en/countries/black-and-grey-lists.html
- HM Treasury and Home Office, *National risk assessment of money laundering and terrorist financing* — https://www.gov.uk/government/collections/money-laundering-and-terrorist-financing-risk-assessments
- FCA, *FCA fines Nationwide £44m for failings in financial crime controls*, December 2025 — https://www.fca.org.uk/news/press-releases/fca-fines-nationwide-44m-failings-financial-crime-controls

## Version history

| Version | Date | Change |
|---|---|---|
| 0.1 | Sept 2026 | First draft. Weights provisional pending Step 2 and Step 5. |
| 0.2 | Sept 2026 | Regulation references made precise to reg. 18(2)(b). Scoring rule 4.5 added. Worked example at 5.6 rescored against the Step 2 risk factor library; the result moves from an illustrative 2.93 to a calculated 2.07. Section 11.4 updated accordingly. |
| 0.3 | Sept 2026 | Section 11.5 added after the Step 3 run: the High band was not reached by the arithmetic anywhere in the synthetic population. |
| 0.4 | Sept 2026 | Sections 11.6 to 11.8 added after the Step 4 back-test against six FCA enforcement cases. |
| 0.5 | Sept 2026 | Section 11.9 added after the Step 5 validation pack. No change made to the weights, bands or escalators: the proposed changes are recorded in the validation pack and await approval under paragraph 8.1. |
