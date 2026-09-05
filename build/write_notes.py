# -*- coding: utf-8 -*-
"""Write data/generation-notes.md straight from the generator's own distributions,
so the document cannot drift away from the code that produced the data."""
import os
from paths import REPO
import sys, csv, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate import DIST, SEGMENTS, SEED, SAR_RATE, FACTOR_ORDER, N
from labels import LABELS
from data import FACTORS

NAME = {f[0]: f[2] for f in FACTORS}
CSV = REPO + "/data/synthetic-customers.csv"
OUT = REPO + "/data/generation-notes.md"

rows = list(csv.DictReader(open(CSV, encoding="utf-8")))
actual = {f: collections.Counter(r[f] for r in rows) for f in FACTOR_ORDER}
seg_counts = collections.Counter(r["segment"] for r in rows)
sar = sum(1 for r in rows if r["sar_last_12m"] == "Yes")

L = []
w = L.append
w("# Synthetic population: generation notes")
w("")
w("**Firm:** Northgate Bank UK Limited (fictional)  ")
w("**Document reference:** HND-CRA-005  ")
w("**Version:** 0.1  ")
w("**Author:** Saman Barati  ")
w("**Date:** September 2026  ")
w("**Produced by:** `build/generate.py`, seed `%d`" % SEED)
w("")
w("---")
w("")
w("### Author's note")
w("")
w("Methodology 9.2 promises that the generation method and its assumptions are documented. This is that document. "
  "It exists because a synthetic population is an argument, not a fact: every percentage below is a claim about "
  "what a UK retail bank's customer base looks like, and every one of them is mine. If a reader thinks a number "
  "is wrong, this file is where they can say so precisely.")
w("")
w("This file is generated from the same code that generates the data, so the two cannot drift apart.")
w("")
w("---")
w("")
w("## 1. What was produced")
w("")
w("`synthetic-customers.csv` holds %d customers. One row per customer, one column per risk factor, holding the "
  "**level recorded at onboarding** rather than a score. Converting a level into a score is the model's job, not "
  "the data's, which keeps the population independent of the weights." % len(rows))
w("")
w("| Column | Contents |")
w("|---|---|")
w("| `customer_id` | Reference in the form NG-1xxxx |")
w("| `segment` | Personal, Sole trader, or Limited company |")
w("| `C1` ... `A5` | The level recorded for each of the 20 factors, using the short labels in the model's Mapping sheet |")
w("| `sar_last_12m` | Whether a suspicious activity report was submitted in the preceding twelve months |")
w("| `onboarded` | Date of onboarding, drawn uniformly across 2024 and 2025 |")
w("")
w("## 2. Segments")
w("")
w("| Segment | Customers | Share |")
w("|---|---|---|")
for seg, count in SEGMENTS:
    w("| %s | %d | %.0f%% |" % (seg, count, 100.0 * count / N))
w("| **Total** | **%d** | **100%%** |" % N)
w("")
w("The mix reflects a retail bank with a small business book rather than a business bank: three quarters personal, "
  "and the business quarter weighted towards sole traders. Every customer is UK resident, because methodology 2.2 "
  "puts non-UK residents outside the Bank's perimeter.")
w("")
w("## 3. Rules applied to every customer")
w("")
w("1. **Country of residence is always the United Kingdom.** Not a simplification: it follows from the scope at "
  "methodology 2.2. The consequence is that factor G1 has no variance at all in this population, which is "
  "deliberate and is one of the things Step 3 set out to measure.")
w("2. **No prohibited relationships appear.** Section 5.4 of the methodology lists customers who are declined "
  "rather than rated, so a population of onboarded customers cannot contain them.")
w("3. **Level 5 at C3 means exactly the three business types that trigger escalator 5.3(c)** - money service "
  "businesses, trust or company service providers, and dealers in high-value goods. Sectors the National Risk "
  "Assessment treats as vulnerable without an automatic escalation, such as accountancy practices, sit at level 4. "
  "This was corrected after the Step 3 review; before it, a score of 5 and an automatic escalation did not always "
  "mean the same thing.")
w("4. **A SAR was recorded for %.1f%% of customers**, drawn independently of every other attribute. That "
  "independence is unrealistic, and it is called out in the limitations below." % (100 * SAR_RATE))
w("5. **The draw is deterministic.** Seed %d, so re-running the generator reproduces this file byte for byte." % SEED)
w("")
w("## 4. The distributions")
w("")
w("Read across: the probability that a customer in each segment was assigned that level. Blank means the level "
  "cannot occur in that segment. Columns sum to 100% within each factor.")
w("")
w("| Factor | Level recorded | Score | Personal | Sole trader | Limited co. |")
w("|---|---|---|---|---|---|")
for f in FACTOR_ORDER:
    for s in sorted(LABELS[f]):
        cells = []
        for seg, _ in SEGMENTS:
            p = DIST[seg][f].get(s)
            cells.append("-" if p is None else ("%.1f%%" % (100 * p)))
        w("| %s | %s | %d | %s | %s | %s |" % (f, LABELS[f][s], s, cells[0], cells[1], cells[2]))
w("")
w("## 5. What the population actually came out as")
w("")
w("Drawn counts, for the factors where the outcome matters most to the model:")
w("")
w("| Factor | Level recorded | Customers | Share |")
w("|---|---|---|---|")
for f in ["C3", "C4", "G1", "G3", "P2", "A2"]:
    for s in sorted(LABELS[f]):
        lab = LABELS[f][s]
        c = actual[f].get(lab, 0)
        w("| %s %s | %s | %d | %.1f%% |" % (f, NAME[f] if s == min(LABELS[f]) else "", lab, c, 100.0 * c / len(rows)))
w("")
import math as _m
_exp = SAR_RATE * len(rows)
_sd = _m.sqrt(_exp * (1 - SAR_RATE))
w("Suspicious activity reports recorded: **%d of %d customers (%.1f%%)**." % (sar, len(rows), 100.0 * sar / len(rows)))
w("")
w("That is above the %.1f%% parameter at point 4 above, and the gap is the draw rather than a mistake: "
  "with p = %.3f and n = %d the expected count is %.1f with a standard deviation of %.2f, so %d sits %.1f "
  "standard deviations high — the kind of result a single seed produces roughly one time in %d. The seed is "
  "fixed at %d so the figure is reproducible, and it is the realised %.1f%% that every count in this project "
  "is computed from, not the %.1f%% parameter."
  % (100 * SAR_RATE, SAR_RATE, len(rows), _exp, _sd, sar, (sar - _exp) / _sd,
     int(round(1 / (2 * (1 - 0.5 * (1 + _m.erf(((sar - _exp) / _sd) / _m.sqrt(2))))))),
     SEED, 100.0 * sar / len(rows), 100 * SAR_RATE))
w("")
w("## 6. Limitations of this population")
w("")
w("6.1 **The factors are drawn independently within a segment.** In a real book they correlate: a customer who "
  "takes 60% of turnover in cash is more likely to be in a cash-intensive sector, and the generator does not know "
  "that. The effect is to spread the population more evenly across the score range than reality would.")
w("")
w("6.2 **The SAR flag is independent of everything else**, which is the least realistic assumption here. In a real "
  "book, a SAR is the end of a chain that usually starts with something the model can already see.")
w("")
w("6.3 **There is no bad-outcome label.** Nothing in this file records which customers went on to launder money, "
  "because inventing that would let the model be tuned against a fiction. It is the reason Step 4 tests the model "
  "against real published enforcement cases instead of against this population.")
w("")
w("6.4 **The percentages are judgement.** They are shaped by what UK retail banking looks like from the outside, "
  "not by any firm's internal data, which a personal project cannot have.")
w("")
w("6.5 **The population is not a validation set.** It shows how the model behaves across a plausible spread of "
  "customers. It cannot show whether the model is right, only whether it discriminates.")
w("")
open(OUT, "w", encoding="utf-8").write("\n".join(L) + "\n")
print("wrote", OUT, len(L), "lines")
