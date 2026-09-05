# NatWest and Fowler Oldfield

**Document reference:** HND-CRA-007
**Version:** 0.3
**Author:** Saman Barati
**Date:** September 2026

| | |
|---|---|
| **Firm** | National Westminster Bank Plc |
| **Penalty** | £264,772,619.95 |
| **Date** | Sentenced 13 December 2021, Southwark Crown Court, before Mrs Justice Cockerill |
| **Basis** | Criminal conviction on FCA prosecution, following a guilty plea on 7 October 2021 to offences under regulations 8(1), 8(3) and 14(1) of the Money Laundering Regulations 2007. **This is a criminal fine, not an FCA final notice** — the only one of the six that is. |
| **Relevant period** | 8 November 2012 to 23 June 2016, the outer range across the three offences |
| **Sources** | [FCA press release](https://www.fca.org.uk/news/press-releases/natwest-fined-264.8million-anti-money-laundering-failures) &middot; [Agreed statement of facts](https://www.fca.org.uk/publication/corporate/agreed-statement-facts-fca-national-westminster-bank.pdf) |

## What happened

The FCA describes Fowler Oldfield as "a jewellery business based in Bradford". At the start of the
relationship **NatWest understood that it would not handle cash from the business** — the relationship
manager's note reads "We will not handle any cash for this business" (agreed statement of facts, 80).
Around **£365 million was subsequently deposited with the bank**, of which roughly **£264 million was
in cash**.

The agreed statement of facts records significant amounts of Scottish banknotes deposited throughout
England; notes carrying a prominent musty smell at one cash centre; cash brought into a branch
uncounted in black bin liners at another; and a system error under which cash deposited through cash
centres was read as cheque deposits and subjected to the less stringent rules that apply to cheques.
Staff raised concerns. Nothing changed. In the FCA's press release the sentencing judge, Mrs Justice
Cockerill, is quoted as finding that "the Bank was functionally vital. Without the Bank's failures -
the money could not be effectively laundered".

## What the notice settles

- A UK company with natural-person owners, onboarded in branch with documents seen face to face.
- The business is described three different ways in the FCA's own material: "a jewellery business
  based in Bradford" in the press release; staff recorded as saying "they are not pawnbrokers or
  jewellers but precious metal dealers" (120); and the bank itself having "erroneously described
  Fowler Oldfield as a pawnbroker" (111). The library reads a jeweller and a precious metal dealer
  differently, and that is finding two below.
- **The file recorded that the account would not handle cash.** This is the fact the case turns on, and
  it is settled: A2 sits at level 1 in every reading. Note who said it. The FCA records this as the
  *bank's* understanding, not as a customer declaration.

## Where the readings differ

Three rows are scored. `FO-lo` and `FO-mid` are the **same file** and differ only in how C3 is read —
that comparison is the point of the case, so every other factor is held constant. `FO-hi` then takes
the high-value-dealer reading and pushes every remaining open factor to the worst level the notice
permits.

| Factor | Cash-intensive reading | Adverse reading |
|---|---|---|
| C2 Ownership and control structure | One or two UBOs (2) | **Three to five UBOs (3)** |
| C3 Industry or occupation | Cash-intensive trade (4) | **MSB, TCSP or HVD (5)** |
| G3 Expected counterparty or payment corridor countries | UK only (1) | **Unlisted countries (2)** |
| P2 Cash functionality | Withdrawal only (2) | **Under 2k a month (3)** |
| P3 International payment functionality | Not enabled (1) | **Occasional payments (3)** |
| A3 Expected international proportion of value | None (1) | **Up to 10 percent (2)** |
| A4 Expected counterparty profile | Named businesses (2) | **Many individuals (3)** |

## What the model says

| | Cash-intensive reading | High-value dealer reading | Adverse reading |
|---|---|---|---|
| Weighted score | 1.8225 | 1.8975 | 2.2600 |
| Rounded | 1.82 | 1.90 | 2.26 |
| Band from the arithmetic | Low | Low | Medium |
| Mandatory escalator | No | Yes | Yes |
| **Final rating** | **Low** | **High** | **High** |

9 of the 20 factors are settled at level 1 by the notice itself and take that value in every reading. They carry **41.50% of the model's weight**. Even if every one of the remaining 11 factors were pushed to 5, this reconstruction could not score above **3.34**, and the High band begins at 3.50. Nothing this case file says about the arithmetic is a discovery; the ceiling was fixed before any judgement was made.

## What this teaches the model

1. **The model scores what is on the file, and cannot ask who put it there.** A2 stays at level 1 in all
   three readings. The FCA records "no cash" as the bank's own understanding rather than as something
   the customer stated, and to this model that distinction does not exist: an assumption written into a
   file is scored exactly like a verified fact. Nothing in twenty factors asks where an answer came
   from. No weighting fixes that. What would is a control that compares what the file says with what
   the account does, which is monitoring, not rating.

2. **One word decides the rating, and the FCA's own material supplies three of them.** C3 carries 7.5%
   of the model, so reading the business as a high-value dealer rather than a cash-intensive trade moves
   the score by 0.075 — not enough to change a band. It changes the rating anyway, because level 5 fires
   escalator 5.3(c) and level 4 does not. The escalator is doing the work; the score is decoration. And
   "jeweller", "pawnbroker" and "precious metal dealer" are not synonyms in this library, which is a
   defect in a scale that asks an analyst to pick one word for a business.

3. **The statutory definition does not support the high-value-dealer reading at onboarding.**
   Regulation 14 of the MLRs ("High value dealers, casinos, auction platforms and art market
   participants") defines a high value dealer as a firm or sole trader trading in goods by way of
   business "when the trader makes or receives, in respect of any transaction, a payment or payments in
   cash of at least £10,000 in total" — a threshold redenominated from 10,000 euros to £10,000 by
   regulation 9 of SI 2026/621 with effect from 30 June 2026. The trigger is cash, and this file
   recorded none. So reading (b) is defensible on the wording *this library* uses and not on the wording
   the regulations use — which sharpens the finding rather than weakening it, because the defect is then
   squarely in the level definition. Step 5 recommends tying the level to registration. The Stunt & Co
   case file records the argument against doing so.

---

*Reconstruction, not a finding.* This case file rebuilds a customer from what a published FCA notice
records. It is not a claim about what the firm's file actually contained, and it is not a criticism of
any individual. The purpose is to test a model, not to re-try a case.
