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
| 2 | **Risk factor library** — around 25 factors, each with defined levels, a score, a weight and a written rationale citing its source | `model/risk-factor-library.xlsx`<br>`docs/02-risk-factor-rationale.md` | Not started |
| 3 | **Build and run** — a synthetic population of 400 customers with documented assumptions, loaded and cleaned in Power Query, scored and banded | `data/synthetic-customers.csv`<br>`model/customer-risk-model.xlsx` | Not started |
| 4 | **Back-test** — six FCA enforcement cases, each rebuilt as an onboarding profile and run through the model | `backtest/` | Not started |
| 5 | **Validate and publish** — population distribution, weight sensitivity, override governance, plus a policy test of the 2026 change to jurisdiction-based EDD | `docs/03-model-validation.md`<br>`docs/04-edd-policy-note-2026.md` | Not started |

## The policy question in Step 5

The Money Laundering and Terrorist Financing (Amendment) Regulations 2026 narrow mandatory jurisdiction-based enhanced due diligence to countries on the FATF *Call for Action* list, rather than the whole FATF monitoring list. Dozens of countries come off the automatic trigger.

Step 5 runs the same customer population under the old rule and the new one, counts how many customers change band, and sets out what a firm would need to change elsewhere to keep the same risk sensitivity. It is a live question for UK compliance teams and I wanted to answer it with a number rather than an opinion.

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
