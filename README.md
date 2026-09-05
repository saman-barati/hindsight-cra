# Hindsight

**A customer risk rating model, tested against the customers who actually caused UK banks to be fined.**

Most customer risk models are judged on whether the maths works. This one is judged on a harder question: if it had been running on the day these customers were onboarded, would it have rated them High?

To answer that, the project rebuilds the customer profiles described in published FCA material — the final notices against Nationwide, Santander UK, Monzo and two Barclays entities, and the agreed statement of facts in the FCA's criminal prosecution of NatWest — as they would have looked at the point of onboarding, runs them through the model, and compares the result with the control failure the FCA actually identified.

The model is built in Excel and Power Query. There is no machine learning in it, and that is deliberate: a customer risk rating has to be explainable to an auditor, a regulator and the customer, and every score in this model can be traced to a written rationale and a published source.

---

## Why this project exists

I am a final-year Accounting and Finance student moving towards financial crime compliance in London. I wanted to understand how a customer risk assessment actually reaches a decision, rather than read about the risk-based approach in the abstract. Building one and then testing it against real enforcement cases seemed like the most honest way to find out whether I had understood it.

## The five steps

| | Step | Output | Status |
|---|---|---|---|
| 1 | **Methodology** — define the firm, the perimeter, the risk factor framework, the scoring rules, the bands and the governance around them | [`docs/01-methodology.md`](docs/01-methodology.md) | Complete |
| 2 | **Risk factor library** — 20 factors and 98 level definitions, each factor with a weight, a written rationale and a source | [`model/risk-factor-library.xlsx`](model/risk-factor-library.xlsx)<br>[`docs/02-risk-factor-rationale.md`](docs/02-risk-factor-rationale.md) | Complete |
| 3 | **Build and run** — a synthetic population of 400 customers with documented assumptions, loaded in Power Query, scored, banded and escalated | [`model/customer-risk-model.xlsx`](model/customer-risk-model.xlsx)<br>[`data/synthetic-customers.csv`](data/synthetic-customers.csv)<br>[`docs/03-model-build.md`](docs/03-model-build.md) | Complete |
| 4 | **Back-test** — six FCA enforcement cases, each rebuilt as an onboarding profile and run through the model | [`backtest/`](backtest/) | Complete |
| 5 | **Validate and publish** — population distribution, weight sensitivity, alternative aggregation rules, override governance, plus a policy test of the 2026 change to jurisdiction-based EDD | [`docs/04-model-validation.md`](docs/04-model-validation.md)<br>[`docs/05-edd-policy-note-2026.md`](docs/05-edd-policy-note-2026.md) | Complete |
| — | **Review response** — the finished work put through an external second-line review, and what it got wrong | [`docs/06-review-response.md`](docs/06-review-response.md) | Complete |

## What the model has found so far

Six customers named in published FCA enforcement material — NatWest and Fowler Oldfield, Santander UK, both Barclays cases, Monzo and Nationwide — were rebuilt as they looked **on the day each bank took them on**, and run through the same library, weights and rules as the 400 synthetic customers.

The six cases carry roughly £480 million of penalties between them. Two caveats travel with that number and are stated wherever it appears. Those penalties were imposed for control failures across whole customer books over periods of years, not for these six accounts — no single customer caused a fine. And the total mixes five FCA penalties with one **criminal fine imposed by Southwark Crown Court** following an FCA prosecution, which is a different kind of thing. These six are used because the published material describes them in enough detail to rebuild.

Each case is scored at least twice: once with every open factor read the way most favourable to the customer, once with every open factor at the worst level a competent analyst could have defended on the same information. The pair is the result; the width of the pair is how much of it is reconstruction rather than fact.

**Not one of the six reaches the High band on the arithmetic, in any reading.** One is rated High, through a mandatory escalator.

**And none of them could have reached it.** The facts each notice settles — a UK company, a UK address, branch or app onboarding — pin between 41% and 69% of the model's weight at level 1 before a single judgement is made. The highest score any of the six could reach, if every remaining factor went to 5, is 3.37 against a threshold of 3.50. That finding was fixed by the inputs, not discovered by the test, and it is stated here rather than in a limitations section because an earlier version of this README claimed it as a discovery.

What the back-test can still decide is whether an escalator fires, and how far the answer moves between two defensible readings. On that:

- **One word decides the most serious case.** Fowler Oldfield was a jewellery business. Read as a *cash-intensive trade* it is Low; read as a *dealer in high-value goods* it is High. The scores differ by 0.075. The rating differs completely, because one reading fires an escalator and the other does not.
- **Stunt & Co was rated High on the day the account opened**, from the application form alone. The form recorded "Gold Refining & Trading", which is a dealer in high-value goods on the wording of the same level definition Fowler Oldfield exposes as ambiguous. **The fix this project had already recommended — tying that level to registration rather than to a description of the trade — would have taken this customer from High to Medium.** A fix that resolves one case breaks another, and it is now on the list with that argument against it.
- **A customer whose stated address was a London landmark scores 1.52.** The library has a factor written for exactly that, from the Monzo notice. I gave it 1.5% of the model in Step 2 and defended the choice in writing. The back-test says I was wrong, and both the reasoning and the result stay in the repository.
- **Two of the six were never onboarding failures.** Santander's translations company and Nationwide's personal customer were both rated correctly at onboarding. What failed was the monitoring afterwards — which is what the event-driven review triggers exist for, not the rating.

The full evidence, one file per case, is in [`backtest/`](backtest/). The population run that preceded it is in [`docs/03-model-build.md`](docs/03-model-build.md).

## Two more things Step 5 found

**The weights were never the thing that mattered.** Moving any category weight by ten percentage points changes the band of at most 26 customers out of 400. Setting the delivery channel weight to zero changes 14. I spent a whole document in Step 2 arguing about those numbers.

Against band boundaries placed where the population actually sits, the same weight changes move between 29 and 100 customers — between 2.6 and 11.8 times as many, scenario for scenario. The boundaries decide this model's output; the weights barely touch it. That reverses the order of the work: fix the bands first, argue about the weights second.

**The 2026 EDD change removes the only control that was catching a whole population.** The Money Laundering and Terrorist Financing (Amendment) Regulations 2026 (SI 2026/621, made 9 June 2026) narrow mandatory jurisdiction-based enhanced due diligence to the three FATF *Call for Action* countries, rather than those plus the 22 on the *Increased Monitoring* list. Regulation 19 of the instrument substitutes "FATF call for action country" for "high-risk third country" in regulation 33 of the 2017 Regulations, and defines it by reference to the FATF list as it has effect from time to time.

On this book, 16 customers had jurisdiction-based EDD. Under the new rule, 5 do. Of the 11 who lose it, **not one is escalated for any other reason**, and 9 fall to Low.

The model already scores them — a connection to a monitored jurisdiction is level 4 on the geography factors — but as the sensitivity work shows, one factor at level 4 cannot move a customer across a band. The score sees the risk; the rating does not.

The recommendation is a firm-policy floor at Medium rather than a weight change, costing roughly a third of simply keeping the old trigger. The reasoning is in [`docs/05-edd-policy-note-2026.md`](docs/05-edd-policy-note-2026.md), written as the note a compliance analyst would actually put in front of an MLRO.

## What an external review found

The finished project was put through a second-line model validation review by a system that had not seen it before, given the whole pack and told to find what was wrong with it. It returned 41 findings. Most were right.

The three biggest are already in this README: the Stunt & Co reconstruction had been built from a narrative rather than from the Final Notice and inverted a published conclusion; the back-test's headline was guaranteed by its inputs; and the £480 million was honest arithmetic with a loose attribution. Everything above has been rewritten accordingly, and the workbooks re-run.

Three findings were wrong, and are answered rather than accepted. All 41 dispositions, with the evidence for each, are in [`docs/06-review-response.md`](docs/06-review-response.md).

## What has been changed, and what has not

The validation pack recommends six changes to the model. **None of them has been applied**, because paragraph 8.1 of the methodology requires MLRO approval for any change to weights, bands or escalators.

Two **defect fixes** have been applied, and the difference matters. A calibration change alters the documented policy and needs someone other than the author to own it. A defect fix makes the model do what the policy already says — escalator 5.3(d) was documented as covering nominee and bearer-share structures and was never firing on the factor that records them — and leaving that unfixed would be an excuse wearing governance as a costume. Both are logged in [`docs/04-model-validation.md`](docs/04-model-validation.md) section 9.

A model whose author quietly rewrites it the moment a test embarrasses him has no version history worth reading. A model whose author cites governance to avoid fixing a control that does not work has a worse problem.

## Please read this before using anything here

- **Northgate Bank UK Limited is fictional.** It was invented to give the model a defined perimeter.
- **All data is synthetic.** No real customer data is used, held or referenced.
- **This is a self-directed learning project**, built alongside a BA in Accounting and Finance. It is not professional work product and I do not hold a compliance role.
- **It is not compliance advice**, and it has not been through independent validation by a person. The known weaknesses are listed in section 10 of the methodology, and the decisions I am least confident about are in section 11 — which now runs to fourteen entries.
- **Several findings in this repository are properties of a population I invented**, not of the model. `docs/03-model-build.md` section 5.2a lists every one of them in a single place, because an earlier version of this README stated some of them more strongly than the evidence allows.
- Where I have used AI tools, I say so in the document they relate to.

## Sources

Regulation, guidance and enforcement sources are listed in Appendix A of the methodology document and Appendix A of the risk factor rationale, with a link to the primary source in each case.

Before publication every external fact in this repository — each penalty, date, legal entity name, quoted finding and regulatory citation — was checked against the primary document rather than against notes. Nine things were wrong and are listed, with the corrections, in [`docs/06-review-response.md`](docs/06-review-response.md) section 9. None of them was an invented fact; all nine were real facts that had drifted, which is the failure mode worth watching for in work like this.

The six cases trace to:

- [FCA v National Westminster Bank Plc — agreed statement of facts](https://www.fca.org.uk/publication/corporate/agreed-statement-facts-fca-national-westminster-bank.pdf) and the [press release](https://www.fca.org.uk/news/press-releases/natwest-fined-264.8million-anti-money-laundering-failures)
- [Final Notice, Santander UK Plc, 9 December 2022](https://www.fca.org.uk/publication/final-notices/santander-uk-plc-2022.pdf)
- [Final Notice, Barclays Bank Plc, 14 July 2025](https://www.fca.org.uk/publication/final-notices/barclays-bank-plc-2025.pdf) — Stunt & Co
- [Final Notice, Barclays Bank UK Plc, 14 July 2025](https://www.fca.org.uk/publication/final-notices/barclays-bank-uk-plc-2025.pdf) — WealthTek
- [Final Notice, Monzo Bank Limited, 8 July 2025](https://www.fca.org.uk/publication/final-notices/monzo-bank-limited.pdf)
- [Final Notice, Nationwide Building Society, 11 December 2025](https://www.fca.org.uk/publication/final-notices/nationwide-building-society-2025.pdf)

---

Saman Barati · London · [LinkedIn](https://www.linkedin.com/)
