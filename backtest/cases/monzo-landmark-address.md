# Monzo and the landmark address

**Document reference:** HND-CRA-007
**Version:** 0.3
**Author:** Saman Barati
**Date:** September 2026

| | |
|---|---|
| **Firm** | Monzo Bank Ltd |
| **Penalty** | £21,091,300 (reduced from £30,130,475) |
| **Date** | Final notice 7 July 2025 |
| **Source** | https://www.fca.org.uk/publication/final-notices/monzo-bank-limited.pdf |

## What happened

Monzo onboarded customers on the basis of limited and, in some cases, **obviously implausible
information — including customers who gave well known London landmarks as their home address**. The
final notice names Buckingham Palace and 10 Downing Street (4.50). Its customer risk assessments did
not keep pace as the customer base grew almost tenfold, from around 600,000 in 2018 to over 5.8 million
in 2022. After the FCA restricted it in August 2020 from opening accounts for high-risk customers, it
signed up over 34,000 of them anyway between August 2020 and June 2022.

## What the notice settles

- A personal customer, onboarded digitally through the firm's own app.
- **The stated address is a famous building.** A5 level 5 in the library reads: *the declared profile is
  not credible on the information held, including an address that is a landmark or a non-residential
  building.* That wording was written from this case, in Step 2, before anything was scored. It is
  settled at level 5 in both readings.

## Where the readings differ

The notice settles more of this file than any other case — a personal customer has fewer moving parts —
so the range here is narrow. That is itself informative: the result below is not a reconstruction
artefact.

| Factor | Favourable reading | Adverse reading |
|---|---|---|
| P1 Product type held | Current account, no overdraft (2) | **Current account with credit (3)** |
| D2 Identity verification method | Electronic, one source (4) | **Uncorroborated documents (5)** |
| A2 Expected cash proportion of credits | Up to 10 percent (2) | **10 to 30 percent (3)** |

## What the model says

| | Favourable reading | Adverse reading |
|---|---|---|
| Weighted score | 1.5200 | 1.6700 |
| Rounded | 1.52 | 1.67 |
| Band from the arithmetic | Low | Low |
| Mandatory escalator | No | No |
| **Final rating** | **Low** | **Low** |

13 of the 20 factors are settled at level 1 by the notice itself and take that value in every reading. They carry **69.00% of the model's weight**. Even if every one of the remaining 7 factors were pushed to 5, this reconstruction could not score above **2.24**, and the High band begins at 3.50. Nothing this case file says about the arithmetic is a discovery; the ceiling was fixed before any judgement was made.

## What this teaches the model

1. **The factor that saw the problem was too light to change the answer.** A5 carries 1.5% of the model.
   Moving it from level 1 to level 5 adds 0.06 to the score. The customer lands comfortably in Low in
   both readings, and the argument defending that weight is still in `docs/02-risk-factor-rationale.md`.
   Both the reasoning and the result stay in the repository: deleting the argument that turned out wrong
   would remove the only evidence that the test worked.

2. **Some facts are not scale-shaped.** "This address is a landmark" is not a degree of risk, it is a
   file that should not have been completed. Regulation 31 already requires a firm to cease transactions
   where it cannot complete customer due diligence. Step 5 recommends moving A5 level 5 onto the
   escalator list, and this case is the clearest argument for it.

3. **The delivery channel category, not the plausibility factor, is what raises this customer at all.**
   The category scores 2.95, against 1.70 for expected activity. Digital onboarding with single-source
   electronic verification is doing more work than the landmark address.



---

*Reconstruction, not a finding.* This case file rebuilds a customer from what a published FCA notice
records. It is not a claim about what the firm's file actually contained, and it is not a criticism of
any individual. The purpose is to test a model, not to re-try a case.
