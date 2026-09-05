# LinkedIn launch post

Attach `hindsight-summary.pdf` as a **document post** (Add media → Document), not as a link.
Put the repository link in the **first comment**, not in the post body.

---

## Post text

I built a customer risk model, tested it against the customers who actually caused UK banks to be fined, published the result — and then handed the whole thing to an AI and told it to find everything wrong with it.

It found 41 things. Most of them were right. One of them inverted a conclusion I had already published.

I'm a final-year Accounting and Finance student moving towards financial crime compliance. I wanted to understand how a customer risk assessment actually reaches a decision rather than read about the risk-based approach in the abstract, so I built one — 20 risk factors mapped to regulation 18(2)(b) of the MLRs, every weight carrying a written rationale and a published source — and rebuilt six customers from FCA notices as they looked on the day each bank took them on.

Three things I'd want a compliance team to see.

**The reconstruction I got wrong.** I had built Barclays' Stunt & Co as an empty file, on the reasoning that the FCA's finding was that not enough information was gathered. The reviewer read the Final Notice properly. It records what the application form said: gold refining and trading, turnover of £500,000 manually amended to £3 million, and a statement that the company would not trade outside the EU. Rebuilt from those paragraphs my model rates it High on the day the account opened.

**And the fix I'd already recommended would have removed that.** I had written up a change tying the high-value-dealer level to registration rather than to a description of the trade, because the description is what makes another case ambiguous. A gold trader declaring no cash would not have been registered. So my improvement would have taken the one customer the model caught from High down to Medium. I wrote a fix, tested it on the case that motivated it, and never asked what else it touched.

**My headline finding was guaranteed by its inputs.** I had reported that none of the six reaches High on the arithmetic. True — and none of them could have. The facts each notice settles pin between 41% and 69% of the model's weight at level 1 before any judgement is made, so the highest score any reconstruction could reach is 3.37 against a threshold of 3.50. That is now the first thing the back-test says about its own results.

Three of the 41 findings were wrong, and I've answered those rather than accepted them — including one where two figures looked contradictory and were both right. The full disposition of all 41, with the working, is in the repository.

Then, before publishing, I checked every external fact in it against the primary document — each penalty, date, legal entity, quoted finding and regulation, against the FCA's own notices and legislation.gov.uk rather than against my notes. Nine things were wrong. Not one was invented; all nine were real facts that had drifted. An interval I'd called thirty months was eighteen. A finding I'd attributed to the customer was the bank's own assumption about itself. I'd cited one Barclays final notice for a case that has its own. Those are listed with the corrections in the repository too, because a project whose whole argument is that citations should be checkable ought to show what happened when someone checked them.

Everything is in there: the method, the workbooks, the six case files, the 400-customer synthetic population, the 2026 EDD policy note, and the response document. Synthetic data, a fictional bank, no professional experience claimed. It's a learning project, and the point was to find out where my own reasoning was wrong.

If you work in financial crime compliance and think I still have something backwards, I'd like to hear it.

#AML #FinancialCrime #Compliance #KYC #ModelValidation

---

## First comment

Repository — the methodology, the risk factor library, the 400-customer test population, the six back-tested cases, the 2026 EDD policy note, and the response to the review:

https://github.com/saman-barati/hindsight-cra

---

## Notes on posting

- **Document, not link.** LinkedIn shows link posts to fewer people. The PDF swipes in the feed and keeps people on the platform.
- **Best time:** Tuesday to Thursday, 07:30–09:00 UK time.
- **Reply to every comment in the first two hours.** Reach is decided early.
- **Do not edit the post for the first hour.** Edits reset its distribution.
- **Pin `hindsight-summary.pdf` to the Featured section** of your profile as well. Anyone who opens your profile sees it in the first ten seconds.

## If someone asks about it in an interview

The honest sentence, which is also the strongest one:

> "I have no professional AML experience. I built this to find out how a customer risk model actually reaches a decision, tested it against customers already known to have caused harm, published it, and then had it reviewed adversarially. The review found a reconstruction I'd built from a narrative instead of from the Final Notice, and rebuilding it showed that a fix I'd already recommended would have broken the only case the model got right."

If they press on how careful the work is, the second sentence to have ready:

> "Before publishing I re-checked every enforcement figure and every regulation against the primary source. Nine had drifted. They're listed in the repository with the corrections, because that list is more useful to an employer than a document that claims it got everything right first time."

Then let them pick which part they want to hear about.

## The one thing not to say

Do not describe this as validated. It has been reviewed by a language model, not by a person and not by a second line. If someone asks whether it has been independently validated, the answer is no, and `docs/06-review-response.md` section 7 says so in writing.
