# -*- coding: utf-8 -*-
"""Step 5 additions: sensitivity scenarios, alternative aggregation rules, and the
Validation sheet. Imported by build_model.py."""

# Ten sensitivity scenarios: each category weight shifted by ten percentage points,
# with the other four rescaled proportionally so the total stays at 100%.
BASE = {"C": 0.30, "G": 0.25, "P": 0.20, "D": 0.10, "A": 0.15}
KEYS = ["C", "G", "P", "D", "A"]
NAMES = {"C": "Customer", "G": "Geography", "P": "Product and service",
         "D": "Delivery channel", "A": "Expected activity"}


def scenarios():
    out = []
    for k in KEYS:
        for d in (-0.10, 0.10):
            w = dict(BASE)
            w[k] = max(0.0, round(BASE[k] + d, 10))
            rest, old = 1 - w[k], 1 - BASE[k]
            for j in KEYS:
                if j != k:
                    w[j] = round(BASE[j] * rest / old, 12)
            out.append(("%s %s10pp" % (NAMES[k], "+" if d > 0 else "-"),
                        "%s at %.0f%%" % (NAMES[k], 100 * w[k]),
                        [w[j] for j in KEYS]))
    return out


SCENARIOS = scenarios()

# Recalibrated band boundaries proposed in Step 5, derived from the observed
# distribution of the population rather than from the midpoint of a 1 to 5 scale.
BAND_B_LOW = 1.60
BAND_B_MED = 2.20

# Severity rule: how many of the 20 factors score 4 or 5.
SEV_MED = 1     # 1 or 2 factors at 4+  -> Medium
SEV_HIGH = 3    # 3 or more             -> High
