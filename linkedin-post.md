# LinkedIn launch post

Attach `hindsight-summary.pdf` as a **document post** (Add media → Document), not as a link.
Put the repository link in the **first comment**, not in the post body.

---

## Post text

*2993 characters. LinkedIn's limit is 3,000, and the first draft of this post ran to 3,732 —
which is why it is shorter than the repository documents it summarises. Plain text: LinkedIn does not
render markdown, so asterisks would show as asterisks.*

I built a customer risk model, tested it against the customers who actually caused UK banks to be fined, published it — then handed it to an AI and told it to find everything wrong with it.

It found 41 things. Most were right. One inverted a conclusion I had published.

I'm a final-year Accounting and Finance student moving towards financial crime compliance. I wanted to see how a customer risk assessment actually reaches a decision, so I built one — 20 risk factors mapped to regulation 18(2)(b) of the MLRs, every weight with a written rationale and a published source — and rebuilt six customers from FCA notices as they looked on the day each bank took them on.

Three things I would want a compliance team to see.

The reconstruction I got wrong. I had built Barclays' Stunt & Co as an empty file, reasoning that the FCA's finding was that not enough information had been gathered. The reviewer read the Final Notice properly. It records what the application form said — gold refining and trading, turnover of £500,000 manually amended to £3 million, and that the company would not trade outside the EU. Rebuilt from those paragraphs, my model rates it High on the day the account opened.

The fix I had already recommended would have removed that. I had written up a change tying the high-value-dealer level to registration rather than to a description of the trade. A gold trader declaring no cash would not have been registered, so my improvement would have taken the one customer the model caught from High down to Medium. I wrote a fix, tested it on the case that motivated it, and never asked what else it touched.

My headline finding was guaranteed by its inputs. I had reported that none of the six reaches High on the arithmetic. True — and none of them could have. The facts each notice settles pin 41% to 69% of the model's weight at level 1 before any judgement is made, so the highest score any reconstruction could reach is 3.37, against a threshold of 3.50. That is now the first thing the back-test says about its own results.

Three of the 41 findings were wrong, and I have answered those rather than accepted them.

Then I checked every external fact against the primary document rather than against my notes. Nine were wrong. None invented — all nine real facts that had drifted. An interval I had called thirty months was eighteen. A finding I had attributed to the customer was the bank's own assumption about itself. Those are listed with their corrections in the repository, because a project arguing that citations should be checkable ought to show what happened when someone checked them.

Synthetic data, a fictional bank, no professional experience claimed, and no independent validation by a person. It is a learning project, and the point was to find where my own reasoning was wrong.

If you work in financial crime compliance and think I still have something backwards, I would like to hear it.

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
