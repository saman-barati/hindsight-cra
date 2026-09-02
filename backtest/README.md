# Step 4: back-testing the model against enforcement

**Document reference:** HND-CRA-007
**Version:** 0.1
**Author:** Saman Barati
**Date:** September 2026

---

## The question

The model was built in Steps 1 to 3 and behaves sensibly on 400 synthetic customers. That proves it is consistent. It does not prove it is right.

So: take customers who are already known to have caused harm — the ones named in published FCA enforcement notices — rebuild each of them as they looked **on the day the bank took them on**, run them through exactly the same library, weights and rules, and see what rating comes out.

## The rule I set before running it

Reconstruct only from what the bank knew or should have recorded **at onboarding**. No hindsight. If a customer declared no cash, the reconstruction records no cash, even knowing what came later. A back-test that lets the answer leak into the inputs proves nothing.

## The result

| Case | Firm and penalty | Weighted score | Band from the arithmetic | Escalator | Final rating |
|---|---|---|---|---|---|
| [FO-a](cases/natwest-fowler-oldfield.md) | NatWest, £264.8m (2021) — cash-intensive reading | 1.82 | Low | No | **Low** |
| [FO-b](cases/natwest-fowler-oldfield.md) | the same customer, read as a high-value dealer | 1.90 | Low | Yes | **High** |
| [SAN](cases/santander-translations-company.md) | Santander UK, £107.8m (2022) | 1.89 | Low | No | **Low** |
| [STU](cases/barclays-stunt-and-co.md) | Barclays Bank plc, £39.3m (2025) | 1.70 | Low | No | **Low** |
| [WTK](cases/barclays-wealthtek.md) | Barclays Bank UK plc, £3.1m (2025) | 1.83 | Low | No | **Low** |
| [MON](cases/monzo-landmark-address.md) | Monzo, £21.1m (2025) | 1.52 | Low | No | **Low** |
| [NAT](cases/nationwide-business-on-personal.md) | Nationwide, £44.1m (2025) | 1.50 | Low | No | **Low** |

**Six customers. Roughly £480 million of UK enforcement penalties between them. The model's arithmetic rates every single one Low.**

Not one of the seven rows exceeds **1.90** on a scale where High begins at 3.50. The single High rating in the table comes from a mandatory escalator, not from the score — and it appears only under one of two defensible readings of a single factor.

## The four things it found

### 1. One word decides the most serious case in the table

Fowler Oldfield was a Bradford jewellery business. Depending on whether an analyst reads that trade as a **cash-intensive business** (factor C3, level 4) or as a **dealer in high-value goods** (level 5, which triggers escalator 5.3(c)), the same customer is rated Low or High.

The arithmetic barely notices: 1.8225 against 1.8975, a difference of 0.0750. The escalator does all the work. So on the case that produced the FCA's first criminal prosecution of a bank under the Money Laundering Regulations, the difference between the lowest rating the model can give and the highest is one analyst's reading of one level definition.

That is a defect in my level definitions, not in the analyst.

### 2. A customer whose address was a London landmark scores 1.52

Monzo onboarded customers using well-known London landmarks as their home address. The library has a factor for exactly that: A5, plausibility of the declared profile, whose level 5 was written from this case.

A5 carries **1.5% of the model**. I chose that weight in Step 2 and wrote a paragraph defending it. Scored through, a customer with an obviously false address lands at 1.52 — comfortably Low. The factor that saw the problem was too light to change the answer.

### 3. The model cannot rate a file that was never filled in

The FCA's finding against Barclays over Stunt & Co is that the bank "did not gather enough information at the start of the relationship". Reconstruct that file honestly and every unknown sits at its benign default, because that is what an unasked question looks like in a scoring model. The result is 1.70 — the lowest business score in the table.

The model has no factor for *we did not ask*. A missing answer and a reassuring answer produce the same number.

### 4. Two of the six were never onboarding failures at all

Santander's translations company (1.89) and Nationwide's personal customer (1.50) both look ordinary on day one, and both are rated correctly at onboarding. What failed was everything afterwards: nobody compared £5,000 declared with millions received, and nobody noticed a business trading through a personal account.

A customer risk rating is not supposed to catch those. The controls that are supposed to are the event-driven review triggers at methodology 7.2 — including trigger (d), which exists in this project because of the Nationwide notice. The back-test confirms the division of labour rather than breaking it.

## What Step 5 has to do about it

1. **Rebuild the band boundaries from the achievable range**, not from the midpoint of a theoretical 1 to 5 scale. On both the synthetic population and these six real customers, nothing reaches 3.50.
2. **Reweight towards the factors that actually separated these customers** — the sector, the plausibility of the declared profile, the completeness of the file — and away from geography.
3. **Add a completeness factor.** A file with unanswered questions should score worse than a file with benign answers, and at present it does not.
4. **Resolve the C3 ambiguity in the library** so that a jewellery business has one correct level, not two defensible ones.

## Sources

Every case file links to the FCA press release or final notice it is built from. Nothing in this folder relies on reporting that is not traceable to the regulator.
