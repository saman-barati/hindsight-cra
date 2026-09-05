# build

Every file in this repository that contains a number is produced by one of these scripts. Nothing is
typed into a document by hand, which is the only way a project this size stays consistent with itself.

## What each script does

| Script | Produces |
|---|---|
| `data.py` | The source of truth: 20 factors, 98 level definitions, the escalator and prohibition lists, and the worked example. Imported by everything else. |
| `labels.py` | The short label for each level. These are the values that appear in the CSV. |
| `generate.py` | `data/synthetic-customers.csv` — 400 customers from a fixed seed. |
| `build.py` | `model/risk-factor-library.xlsx` |
| `backtest_block.py` | The 13 back-test reconstructions, each traced to a paragraph of a published notice. |
| `validation_block.py` | The Step 5 sensitivity scenarios and the alternative aggregation rules. |
| `build_model.py` | `model/customer-risk-model.xlsx` |
| `write_notes.py` | `data/generation-notes.md` |
| `write_backtest.py` | `backtest/README.md` and the six case files |
| `write_validation.py` | `docs/04-model-validation.md` and `docs/05-edd-policy-note-2026.md` |
| `linkedin.py` | `hindsight-summary.pdf` |
| `review_pack.py` | A single-file bundle of every document plus an appendix of figures read out of the workbooks, for handing to a reviewer. |
| `validate_model.py` | Nothing. It recomputes all 400 ratings independently in Python and fails if the workbook disagrees. |
| `consistency.py` | Nothing. It checks that every figure quoted in the prose matches the workbooks, that no superseded wording survives, and that every internal link resolves. |

`docs/01`, `docs/02`, `docs/03` and the top-level `README.md` are written by hand, which is why
`consistency.py` exists.

## Running it

```
python3 build/generate.py        # the population
python3 build/build.py           # the library workbook
python3 build/build_model.py     # the model workbook
```

Then **recalculate both workbooks** — `openpyxl` writes formulas but does not evaluate them, so the
cached values are empty until something opens the file. Any of LibreOffice, Excel or the `recalc.py`
script from Anthropic's public `xlsx` skill will do it. Then:

```
python3 build/write_notes.py
python3 build/write_backtest.py
python3 build/write_validation.py
python3 build/linkedin.py        # needs playwright and a chromium build
python3 build/validate_model.py  # must print ALL CHECKS PASSED
python3 build/consistency.py     # must print 0 failures
```

`paths.py` works out where the repository is from its own location, so this runs from wherever you
clone it. The only absolute path left anywhere is the one inside `linkedin.py` pointing at a chromium
binary, which you will need to change.

## Reproducibility

The seed is fixed at `20260902` and `generate.py` validates that every probability distribution sums to
1.0 before it writes anything. Re-running it reproduces the same 400 customers, so every count in every
document is checkable rather than merely asserted.
