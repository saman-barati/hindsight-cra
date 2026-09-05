# Customer Risk Assessment Methodology

**Firm:** Northgate Bank UK Limited (fictional)
**Document reference:** HND-CRA-001
**Version:** 0.8 (draft)
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
| MLRs 2017, reg. 14 — High value dealers, casinos, auction platforms and art market participants | The high value dealer limb of factor C3 level 5 and escalator 5.3(c) |
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

- (a) the customer, a beneficial owner or a person exercising control is a politically exposed person, a family member or a known close associate (reg. 35(1)). **This escalator does not comply with regulation 35(3A)** and is recorded as a defect at 11.13: 35(3A) requires the Bank to start from the position that a domestic PEP presents a *lower* risk than a non-domestic one, and this escalator makes no distinction between a foreign PEP, a domestic PEP and a PEP's parent.
- (b) the customer resides in, has a further tax residence in, or sends money to or receives money from a jurisdiction identified by FATF as a High-Risk Jurisdiction subject to a Call for Action. Regulation 33(1)(b), as amended by SI 2026/621, requires enhanced due diligence where the customer is *established* in such a jurisdiction; the Bank applies the escalator to payment corridors as well, which regulation 33(1) permits because it is a floor and not a ceiling. **The Bank has no factor recording where a beneficial owner is established**, so the beneficial-owner limb of regulation 33(1)(b) is not tested by this model at all (11.14).
- (c) the customer is a money service business, a trust or company service provider, or a dealer in high-value goods
- (d) the ownership structure includes nominee shareholders, bearer shares, or an entity incorporated in a jurisdiction with no accessible beneficial ownership register. Level 5 of factor C1 covers trusts, nominee arrangements and overseas incorporation as one level, so the recorded level cannot tell them apart; the escalator therefore fires on the whole of C1 level 5. That is conservative rather than correct. The proper fix is to split C1 level 5 so the condition can be evaluated, which is change 7 in the validation pack and needs approval; the reason it was applied in this form meanwhile is at 11.9a.
- (e) screening returns a confirmed adverse media match relating to financial crime, fraud, bribery, corruption or tax evasion
- (f) a suspicious activity report has been submitted in respect of the customer in the preceding twelve months

5.4 **Prohibited relationships.** These are not rated. The application is declined, or an existing relationship is referred for exit, under the Bank's exit procedure.

- (a) a confirmed sanctions match — referred immediately to the Sanctions team and handled under the sanctions procedure, not under this document
- (b) shell banks
- (c) a money service business or cryptoasset business operating in the UK without the registration it is required to hold
- (d) the customer does not provide information the Bank needs to complete CDD. Regulation 31 is triggered where the Bank is unable to apply customer due diligence as required by regulation 28, and requires four things: no transaction through a bank account with or on behalf of the customer; no business relationship or transaction otherwise than through a bank account; **termination of any existing business relationship**; and **consideration of whether a disclosure is required** under Part 3 of the Terrorism Act 2000 or Part 7 of the Proceeds of Crime Act 2002. The last two are the limbs firms most often leave out of a policy, so they are written out here.
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

11.5 **Whether the High band can be reached by the arithmetic at all.** Added after Step 3. Scored against the risk factor library, not one of the 400 customers in the synthetic population reached the High band on the weighted average; the highest score anywhere was 2.76 against a threshold of 3.50, and all 43 High ratings came from the mandatory escalators at 5.3. Working down from the heaviest factor, **nine** factors would have to score 5, with every remaining factor at 1, for a customer to reach exactly 3.50 — the nine heaviest carry 62.5% of the effective weight, and 1 + 4 x 0.625 = 3.50 exactly. Nine is the count, not a unique set: G2, P2 and P3 all carry 5% effective weight, and the seven factors above 5% carry 52.5% between them, so **two** of those three have to be at 5 to reach 62.5% and the third sits at 1. With only one of them at 5 the total is 57.5% and the highest reachable score is 3.30. Paragraph 10.5 already says a weighted average dilutes single severe factors and that the escalator list is the compensating control. What Step 3 shows is that on this population the escalators are not compensating at the margin, they are doing all of the work at the top of the scale. Step 5 has to decide whether the answer is to move the boundaries, to re-weight, or to change the aggregation rule itself. The evidence is in `docs/03-model-build.md`, section 4.

11.6 **The C3 level 5 definition is ambiguous and I now know it.** Added after Step 4. Fowler Oldfield was a jewellery business. Read as a cash-intensive trade it scores 4; read as a dealer in high-value goods it scores 5 and triggers escalator 5.3(c). Both readings are defensible on the current wording, and they produce Low and High respectively on the customer behind the FCA's first criminal prosecution of a bank. The obvious fix is to make the level turn on a checkable fact - whether the customer is registered with HMRC as a high value dealer - rather than on a description of the trade. **That fix is contested by the evidence for it.** The rebuilt Stunt & Co reconstruction is rated High on the day the account opened only because C3 level 5 is written as a description: a gold refiner and trader that declares no cash would probably not have been a registered high value dealer, so the fix would take the one customer the back-test catches from High to Medium. The ambiguity is real and the fix as drafted is a trade rather than an improvement. See `backtest/cases/natwest-fowler-oldfield.md` and `docs/04-model-validation.md` section 5.1.

11.7 **A5 is the right factor carrying the wrong weight.** Added after Step 4. Level 5 of A5 was written from the Monzo notice to capture a declared profile that cannot be true, such as an address that is a well-known landmark. Scored through the model, such a customer reaches 1.52 and is rated Low, because A5 carries 1.5% of the effective weight. A fact that cannot be true is not a small increase in risk; it is a failure to identify the customer. Step 5 should move it out of the weighted average and onto the escalator or prohibited list. See `backtest/cases/monzo-landmark-address.md`.

11.8 **Nothing in the library scores how complete the file is.** Added after Step 4; **its evidence has since been withdrawn.** The original argument was that reconstructing Stunt & Co as the FCA describes it - a file where not enough information was gathered - produced the lowest business score in the back-test, because every unasked question sits at its benign level. That reconstruction was wrong. The Final Notice records what the application form said, and rebuilt from it the customer rates High on day one. The claim that the model cannot rate a file nobody filled in no longer has that case behind it, and has been withdrawn. The gap itself remains and is unmeasured: no factor asks what proportion of the file is evidenced rather than asserted, and the library has no level for a check that was run and never reviewed (11.10). See `backtest/cases/barclays-stunt-and-co.md`.

11.9 **The weights were never the thing that mattered.** Added after Step 5. Moving any category weight by ten percentage points changes the band of at most 26 customers out of 400, and setting the delivery channel weight to zero changes 14. Against band boundaries placed where the population actually sits, the same changes move between 29 and 100. The boundaries decide this model's output; the weights barely touch it. Section 4.2 of this document says the weights are provisional pending Step 5. They are now provisional pending a boundary change, which has to come first. The validation pack recommends moving the boundaries to 1.60 and 2.20, moving A5 level 5 onto the escalator list, and four further changes. **None of those changes has been made**, because paragraph 8.1 requires MLRO approval for any change to weights, bands or escalators. They are recorded in `docs/04-model-validation.md` section 9 and await that approval.

11.9a **What "requires approval" does and does not cover.** Added to answer the obvious objection to 11.9, that it is an excuse wearing governance as a costume. The distinction the Bank draws is this. A **calibration change** alters the documented policy - where a boundary sits, what an escalator covers, how the categories are weighted - and needs approval, because someone other than the model's author has to own a change in the firm's risk appetite. A **defect fix** makes the implementation do what the documented policy already says, and does not: leaving a control that is known not to fire as written is not governance. Two defect fixes have therefore been applied without approval and logged in `docs/04-model-validation.md` section 9: escalator 5.3(d) now fires on the whole of C1 level 5, having previously never fired on C1 at all, which moves three customers to High; and escalator 5.3(b) has been reworded to describe the payment corridors the model has always tested, which changes no ratings. Two more have been applied since, on the same principle and logged in the same place: C4 level 3 now covers the family and known close associates of any politically exposed person rather than only a domestic one, and escalator 5.3(b) now says "a further tax residence" because that is what factor G2 records. Everything at 11.6, 11.7, 11.8, 11.11, 11.12, 11.13 and 11.15 is a calibration change and remains unapplied.

11.10 **"Screened but not reviewed" has no level.** Added after Step 4's rebuild. Factor C5 records what adverse media screening returned. It has no level for screening that was performed and whose results nobody looked at, which is the position the FCA records at paragraph 4.37 of the Barclays notice. That is not the same as a clear result and the model treats it as one.

11.11 **Nothing asks whether the customer holds the permissions its business requires.** Added after Step 4. The WealthTek case turns entirely on a check of the Financial Services Register that was never made - free, public, and under a minute. No factor in the library asks for it. Factor D3 mentions the Register, but only for an *introducing* firm, so the one factor that names the Register is the one that could not have caught this case.

11.12 **The C3 scale has no level for a financial-sector customer.** Added after Step 4. Level 2 reads "regulated profession with a named supervisory body outside the financial sector"; levels 3 and 4 are trades; level 5 is MSBs, TCSPs and high-value dealers. A bank's customer that is itself an authorised financial firm has nowhere to sit and is forced into level 2. That is a defect in the scale, not a judgement call.

11.13 **The PEP escalator does not comply with regulation 35(3A).** Added after Step 5. Regulation 35(1) requires enhanced due diligence for a PEP, a family member or a known close associate. Regulation 35(3A), inserted with effect from 10 January 2024, requires that where the person is a **domestic** PEP - entrusted with a prominent public function by the United Kingdom - the starting point is that they present a lower level of risk than a non-domestic PEP, and that where no enhanced risk factors are present the measures applied must be less extensive. Escalator 5.3(a) rates all of them High identically. Requiring EDD for every PEP is not itself wrong, since 35(1) requires it; producing an output that cannot distinguish a foreign PEP from a domestic PEP's parent is, because it makes the differentiation 35(3A) requires impossible to evidence. On the current population this affects 11 customers: 1 foreign PEP, 3 domestic PEPs and 7 family members or associates. Factor C4 cannot make the distinction either, and the defect there turned out to be worse than first recorded: level 3 read "a family member or known close associate **of a domestic PEP**", so a foreign PEP's relative — the case regulation 35(1) is most concerned with — had no level to be recorded at. That wording has been corrected as a defect fix, since 35(1) and escalator 5.3(a) both already covered them. What level 3 still cannot do is separate a domestic PEP's relative from a foreign one's, which is why change 4 in the validation pack needs change 8 alongside it. Recommended as change 4 in the validation pack.

11.14 **No factor records where a beneficial owner is established.** Added after Step 5. Escalator 5.3(b) and regulation 33(1)(b) both refer to the customer *or a beneficial owner*. Factors G1 and G2 record the customer's residence; G3 records payment corridors. A UK-resident customer whose beneficial owner sits in a Call for Action jurisdiction is not caught by anything in this model.

11.15 **A risk model is only as good as the customer due diligence feeding it, and nothing here measures that.** Added after Step 4. Santander's customer was recorded on its application form as a "Translation service" and scores Low. The FCA's finding is that the firm failed to verify the nature of the business, which was a money service business. Verified, the same customer is High on day one through escalator 5.3(c): the control existed and worked, and the input was wrong. Everything this methodology says about weights, bands and aggregation sits downstream of a verification step it does not itself require, measure or record. Section 5 scores what the analyst wrote down and has no way of asking how they came to write it. See `backtest/cases/santander-translations-company.md`.

---

## Appendix A — Sources

- The Money Laundering, Terrorist Financing and Transfer of Funds (Information on the Payer) Regulations 2017 (SI 2017/692), as amended — https://www.legislation.gov.uk/uksi/2017/692/contents
- The Money Laundering and Terrorist Financing (Amendment) Regulations 2026 (SI 2026/621), as made — made 9 June 2026, in force 30 June 2026 except regulation 20 and regulation 36(b) (1 February 2027) and parts of regulation 37 (25 October 2027) — https://www.legislation.gov.uk/uksi/2026/621/made
- Regulation 14 of SI 2017/692 (high value dealers), whose cash threshold was redenominated from 10,000 euros to £10,000 by regulation 9 of SI 2026/621 with effect from 30 June 2026 — https://www.legislation.gov.uk/uksi/2017/692/regulation/14
- Regulation 31 of SI 2017/692 (requirement to cease transactions etc.) — https://www.legislation.gov.uk/uksi/2017/692/regulation/31
- Regulation 35 of SI 2017/692 (enhanced due diligence: politically exposed persons), including paragraph (3A) — https://www.legislation.gov.uk/uksi/2017/692/regulation/35
- JMLSG, *Prevention of money laundering / combating terrorist financing: Guidance for the UK financial sector*, Part I, June 2023 as updated August 2025 (approved by HM Treasury on 27 August 2025) — https://www.jmlsg.org.uk/guidance/current-guidance/
- FCA, *Financial Crime Guide: A firm's guide to countering financial crime risks* — https://www.handbook.fca.org.uk/handbook/FCG/
- FATF, *High-Risk Jurisdictions subject to a Call for Action* and *Jurisdictions under Increased Monitoring*, both dated 19 June 2026 — https://www.fatf-gafi.org/en/publications/High-risk-and-other-monitored-jurisdictions/call-for-action-june-2026.html and https://www.fatf-gafi.org/en/publications/High-risk-and-other-monitored-jurisdictions/increased-monitoring-june-2026.html
- HM Treasury, *National risk assessment of money laundering and terrorist financing 2025*, published 17 July 2025 — https://www.gov.uk/government/publications/national-risk-assessment-of-money-laundering-and-terrorist-financing-2025
- FCA Final Notice, Nationwide Building Society, 11 December 2025 — https://www.fca.org.uk/publication/final-notices/nationwide-building-society-2025.pdf

## Version history

| Version | Date | Change |
|---|---|---|
| 0.8 | Sept 2026 | Escalator 5.3(b) reworded to "a further tax residence", which is what factor G2 records. C4 level 3 corrected to cover the relatives of any PEP, and 11.13 rewritten. The 3.50 arithmetic at 11.5 corrected: two of the three 5% factors are needed, not one. 11.15 added. |
| 0.7 | Sept 2026 | Pre-publication fact check. Regulation 31 written out in full at 5.4(d), including the termination and disclosure limbs that were missing. Regulation 14 added to the regulatory basis table with the £10,000 threshold as redenominated by SI 2026/621. Source list dated and pointed at primary documents throughout. |
| 0.6 | Sept 2026 | Escalators 5.3(b) and 5.3(d) reworded so that the document describes the control the model actually applies, and 5.3(d) now fires on the whole of C1 level 5. Escalator 5.3(a) marked non-compliant with reg. 35(3A). Section 11.6 records the argument against its own fix; 11.8's evidence is withdrawn; 11.9a states the line between a defect fix and a calibration change; 11.10 to 11.14 added. Figures in 11.5 and 11.9 re-run. Source list corrected to SI 2026/621 as made. |
| 0.5 | Sept 2026 | Section 11.9 added after the Step 5 validation pack. No change made to the weights, bands or escalators: the proposed changes are recorded in the validation pack and await approval under paragraph 8.1. |
| 0.4 | Sept 2026 | Sections 11.6 to 11.8 added after the Step 4 back-test against six FCA enforcement cases. |
| 0.3 | Sept 2026 | Section 11.5 added after the Step 3 run: the High band was not reached by the arithmetic anywhere in the synthetic population. |
| 0.2 | Sept 2026 | Regulation references made precise to reg. 18(2)(b). Scoring rule 4.5 added. Worked example at 5.6 rescored against the Step 2 risk factor library; the result moves from an illustrative 2.93 to a calculated 2.07. Section 11.4 updated accordingly. |
| 0.1 | Sept 2026 | First draft. Weights provisional pending Step 2 and Step 5. |
