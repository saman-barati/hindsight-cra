# LinkedIn launch post

Attach `hindsight-summary.pdf` as a **document post** (Add media → Document), not as a link.
Put the repository link in the **first comment**, not in the post body.

---

## Post text

*2705 characters, against LinkedIn's 3,000 limit. Plain text: LinkedIn does not render markdown.
No self-introduction — the headline on the profile already says who I am, and repeating it in a
personal post is the thing that makes a post read as written by someone else.*

I built a customer risk model, tested it on the customers who actually got UK banks fined, published it, and then gave the whole thing to an AI and told it to find everything wrong with it.

41 findings came back. Most of them were right. One turned a conclusion I'd already published upside down.

The model is 20 risk factors mapped to regulation 18(2)(b) of the MLRs, every weight carrying a written rationale and a published source, plus six customers rebuilt from FCA notices as they looked on the day each bank onboarded them.

I'd reconstructed Barclays' Stunt & Co as an almost empty file, on the logic that the FCA's finding was that nobody had asked enough questions. The Final Notice actually records a good deal of what the application form said: gold refining and trading, a turnover figure of £500,000 manually amended to £3 million, and a statement that the company wouldn't trade outside the EU. Rebuild the file from those paragraphs and my model rates the customer High on the day the account opened.

Which is awkward, because I'd already written up a change that would have removed that. I wanted the high-value-dealer level to turn on registration rather than on a description of the trade. A gold trader declaring no cash wouldn't have been registered. So my improvement takes the one customer the model caught and drops it to Medium. I had tested that fix against the case that motivated it and never asked what else it touched.

The third one stung more. I'd reported that none of the six reaches High on the arithmetic. True, but none of them could have. The facts each notice settles pin 41% to 69% of the model's weight at level 1 before anyone makes a judgement call, so the ceiling on any reconstruction is 3.37 against a threshold of 3.50. The test could not have produced another answer. That is now the first thing the back-test says about its own results.

Three of the 41 were wrong and I've argued back rather than accepted them.

Then, before publishing any of it, I went through every external fact against the primary document instead of against my own notes. Nine were off. None invented, all nine real facts that had drifted somewhere between the notice and my draft. An interval I'd called thirty months was eighteen. Something I'd attributed to the customer was the bank's own assumption about itself. Those are in the repository with their corrections. It seemed like the wrong project to quietly fix them in.

Synthetic data, a fictional bank, no professional experience claimed and no independent validation by a person.

If you do this for a living and think I've still got something backwards, tell me.

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
