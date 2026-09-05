# -*- coding: utf-8 -*-
"""Generate the synthetic customer population for Hindsight Step 3.

Deterministic: SEED is fixed, so the same CSV is produced every time.
Every distribution below is reproduced in data/generation-notes.md.
"""
import os
from paths import REPO
import sys, csv, random, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from labels import LABELS

SEED = 20260902
N = 400
FACTOR_ORDER = ["C1","C2","C3","C4","C5","G1","G2","G3","P1","P2",
                "P3","P4","D1","D2","D3","A1","A2","A3","A4","A5"]

SEGMENTS = [("Personal", 300), ("Sole trader", 60), ("Limited company", 40)]

# distributions are {factor: {score: probability}} per segment
DIST = {
"Personal": {
 "C1": {1:.78, 2:.22},
 "C2": {1:1.0},
 "C3": {1:.62, 2:.14, 3:.20, 4:.035, 5:.005},
 "C4": {1:.985, 3:.008, 4:.005, 5:.002},
 "C5": {1:.930, 2:.055, 3:.008, 4:.005, 5:.002},
 "G1": {1:1.0},
 "G2": {1:.930, 2:.055, 4:.012, 5:.003},
 "G3": {1:.840, 2:.120, 3:.030, 4:.008, 5:.002},
 "P1": {1:.12, 2:.46, 3:.42},
 "P2": {1:.100, 2:.420, 3:.420, 4:.055, 5:.005},
 "P3": {1:.35, 2:.34, 3:.24, 4:.06, 5:.01},
 "P4": {1:.720, 2:.200, 3:.060, 4:.015, 5:.005},
 "D1": {1:.10, 2:.05, 3:.72, 4:.11, 5:.02},
 "D2": {1:.11, 2:.04, 3:.66, 4:.17, 5:.02},
 "D3": {1:.700, 2:.130, 3:.140, 4:.025, 5:.005},
 "A1": {1:.720, 2:.230, 3:.030, 4:.015, 5:.005},
 "A2": {1:.30, 2:.47, 3:.18, 4:.04, 5:.01},
 "A3": {1:.660, 2:.240, 3:.070, 4:.025, 5:.005},
 "A4": {1:.740, 2:.150, 3:.080, 4:.025, 5:.005},
 "A5": {1:.860, 2:.100, 3:.030, 4:.008, 5:.002},
},
"Sole trader": {
 "C1": {2:1.0},
 "C2": {1:1.0},
 "C3": {1:.05, 2:.14, 3:.44, 4:.34, 5:.03},
 "C4": {1:.985, 3:.008, 4:.005, 5:.002},
 "C5": {1:.900, 2:.070, 3:.020, 4:.008, 5:.002},
 "G1": {1:1.0},
 "G2": {1:.900, 2:.075, 4:.020, 5:.005},
 "G3": {1:.68, 2:.20, 3:.08, 4:.03, 5:.01},
 "P1": {4:.72, 5:.28},
 "P2": {1:.02, 2:.08, 3:.28, 4:.42, 5:.20},
 "P3": {1:.30, 2:.26, 3:.28, 4:.13, 5:.03},
 "P4": {1:.80, 2:.06, 3:.10, 4:.03, 5:.01},
 "D1": {1:.14, 2:.05, 3:.60, 4:.17, 5:.04},
 "D2": {1:.13, 2:.05, 3:.58, 4:.21, 5:.03},
 "D3": {1:.62, 2:.16, 3:.12, 4:.08, 5:.02},
 "A1": {1:.20, 2:.50, 3:.22, 4:.06, 5:.02},
 "A2": {1:.08, 2:.22, 3:.31, 4:.28, 5:.11},
 "A3": {1:.560, 2:.240, 3:.130, 4:.055, 5:.015},
 "A4": {1:.10, 2:.34, 3:.42, 4:.11, 5:.03},
 "A5": {1:.780, 2:.130, 3:.060, 4:.025, 5:.005},
},
"Limited company": {
 "C1": {3:.62, 4:.30, 5:.08},
 "C2": {2:.52, 3:.24, 4:.18, 5:.06},
 "C3": {2:.20, 3:.46, 4:.26, 5:.08},
 "C4": {1:.975, 3:.012, 4:.008, 5:.005},
 "C5": {1:.880, 2:.080, 3:.022, 4:.013, 5:.005},
 "G1": {1:1.0},
 "G2": {1:.86, 2:.10, 4:.03, 5:.01},
 "G3": {1:.52, 2:.26, 3:.14, 4:.06, 5:.02},
 "P1": {4:.45, 5:.55},
 "P2": {1:.06, 2:.10, 3:.26, 4:.36, 5:.22},
 "P3": {1:.14, 2:.20, 3:.30, 4:.30, 5:.06},
 "P4": {1:.34, 2:.04, 3:.40, 4:.17, 5:.05},
 "D1": {1:.20, 2:.06, 3:.48, 4:.20, 5:.06},
 "D2": {1:.18, 2:.08, 3:.50, 4:.20, 5:.04},
 "D3": {1:.50, 2:.14, 3:.08, 4:.24, 5:.04},
 "A1": {1:.08, 2:.36, 3:.40, 4:.12, 5:.04},
 "A2": {1:.16, 2:.30, 3:.28, 4:.18, 5:.08},
 "A3": {1:.34, 2:.26, 3:.24, 4:.12, 5:.04},
 "A4": {1:.06, 2:.44, 3:.30, 4:.15, 5:.05},
 "A5": {1:.74, 2:.15, 3:.07, 4:.03, 5:.01},
},
}

SAR_RATE = 0.015


def check_distributions():
    problems = []
    for seg, d in DIST.items():
        for f in FACTOR_ORDER:
            if f not in d:
                problems.append("%s missing factor %s" % (seg, f)); continue
            total = round(sum(d[f].values()), 10)
            if total != 1.0:
                problems.append("%s %s sums to %s" % (seg, f, total))
            for s in d[f]:
                if s not in LABELS[f]:
                    problems.append("%s %s has no label for score %d" % (seg, f, s))
    return problems


def draw(rng, dist):
    scores = sorted(dist)
    weights = [dist[s] for s in scores]
    return rng.choices(scores, weights=weights, k=1)[0]


def main():
    problems = check_distributions()
    if problems:
        for p in problems:
            print("DISTRIBUTION ERROR:", p)
        raise SystemExit(1)

    rng = random.Random(SEED)
    start = datetime.date(2024, 1, 1)
    rows = []
    n = 0
    for segment, count in SEGMENTS:
        for _ in range(count):
            n += 1
            d = DIST[segment]
            row = {"customer_id": "NG-%05d" % (10000 + n), "segment": segment}
            for f in FACTOR_ORDER:
                row[f] = LABELS[f][draw(rng, d[f])]
            row["sar_last_12m"] = "Yes" if rng.random() < SAR_RATE else "No"
            row["onboarded"] = (start + datetime.timedelta(days=rng.randrange(0, 730))).isoformat()
            rows.append(row)

    rng.shuffle(rows)

    out = REPO + "/data/synthetic-customers.csv"
    cols = ["customer_id", "segment"] + FACTOR_ORDER + ["sar_last_12m", "onboarded"]
    with open(out, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=cols)
        w.writeheader()
        w.writerows(rows)
    print("wrote", out, len(rows), "rows,", len(cols), "columns")
    print("distributions validated: every factor sums to 1.0 in every segment")


if __name__ == "__main__":
    main()
