# Hindsight

**A customer risk rating model, tested against the customers who actually caused UK banks to be fined.**

Most customer risk models are judged on whether the maths works. This one is judged on a harder question: if it had been running on the day these customers were onboarded, would it have rated them High?

To answer that, the project rebuilds the customer profiles described in published FCA final notices — Nationwide, Barclays, Monzo — as they would have looked at the point of onboarding, runs them through the model, and compares the result with the control failure the FCA actually identified.

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

## What the model has found so far

Six customers named in published FCA enforcement notices — NatWest and Fowler Oldfield, Santander UK, both Barclays cases, Monzo and Nationwide — were rebuilt as they looked **on the day each bank took them on**, and run through the same library, weights and rules as the 400 synthetic customers.

**Between them those customers caused roughly £480 million of UK enforcement penalties. The model's arithmetic rates every single one Low.**

Nothing reaches 1.90 on a scale where High begins at 3.50. The one High rating in the table comes from a mandatory escalator rather than from the score, and only under one of two defensible readings of a single factor.

Four things came out of it:

- **One word decides the most serious case.** Fowler Oldfield was a jewellery business. Read as a *cash-intensive trade* it is Low; read as a *dealer in high-value goods* it is High. The scores differ by 0.075. The rating differs completely.
- **A customer whose stated address was a London landmark scores 1.52.** The library has a factor written for exactly that, from the Monzo notice. I gave it 1.5% of the model in Step 2 and defended the choice in writing. The back-test says I was wrong, and both the reasoning and the result stay in the repository.
- **The model cannot rate a file nobody filled in.** Reconstruct the Stunt & Co relationship as the FCA describes it and every unasked question sits at its benign default. A missing answer and a reassuring answer produce the same number.
- **Two of the six were never onboarding failures.** Santander's translations company and Nationwide's personal customer were both rated correctly at onboarding. What failed was the monitoring afterwards — which is what the event-driven review triggers exist for, not the rating.

The full evidence, one file per case, is in [`backtest/`](backtest/). The population run that preceded it is in [`docs/03-model-build.md`](docs/03-model-build.md).

## Two more things Step 5 found

**The weights were never the thing that mattered.** Moving any category weight by ten percentage points changes the band of at most 26 customers out of 400. Setting the delivery channel weight to zero changes 14. I spent a whole document in Step 2 arguing about those numbers.

Against band boundaries placed where the population actually sits, the same weight changes move between 29 and 100 customers — three to six times as many. The boundaries decide this model's output; the weights barely touch it. That reverses the order of the work: fix the bands first, argue about the weights second.

**The 2026 EDD change removes the only control that was catching a whole population.** The Money Laundering and Terrorist Financing (Amendment) Regulations 2026 narrow mandatory jurisdiction-based enhanced due diligence to the three FATF *Call for Action* countries, rather than those plus the 22 on the *Increased Monitoring* list.

On this book, 16 customers had jurisdiction-based EDD. Under the new rule, 5 do. Of the 11 who lose it, **not one is escalated for any other reason**, and 9 fall to Low.

The model already scores them — a connection to a monitored jurisdiction is level 4 on the geography factors — but as the sensitivity work shows, one factor at level 4 cannot move a customer across a band. The score sees the risk; the rating does not.

The recommendation is a firm-policy floor at Medium rather than a weight change, costing roughly a third of simply keeping the old trigger. The reasoning is in [`docs/05-edd-policy-note-2026.md`](docs/05-edd-policy-note-2026.md), written as the note a compliance analyst would actually put in front of an MLRO.

## What has not been changed

The validation pack recommends five changes to the model. **None of them has been applied.** Paragraph 8.1 of the methodology requires MLRO approval for any change to weights, bands or escalators, so they are recorded in [`docs/04-model-validation.md`](docs/04-model-validation.md) and left there.

That is deliberate. A model whose author quietly rewrites it the moment a test embarrasses him has no version history worth reading.

## Please read this before using anything here

- **Northgate Bank UK Limited is fictional.** It was invented to give the model a defined perimeter.
- **All data is synthetic.** No real customer data is used, held or referenced.
- **This is a self-directed learning project**, built alongside a BA in Accounting and Finance. It is not professional work product and I do not hold a compliance role.
- **It is not compliance advice**, and it has not been through independent validation. The known weaknesses are listed in section 10 of the methodology, and the decisions I am least confident about are in section 11.
- Where I have used AI tools, I say so in the document they relate to.

## Sources

Regulation, guidance and enforcement sources are listed in Appendix A of the methodology document, with links to the primary source in each case.

---

Saman Barati · London · [LinkedIn](https://www.linkedin.com/)
