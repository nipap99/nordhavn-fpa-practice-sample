# Nordhavn FP&A practice data (free sample)

A small, fully synthetic dataset for practising FP&A analysis in Excel, SQL or Python. It comes from the fictional **Nordhavn Commercial Group**, a Nordic HVAC and heat-pump distributor.

This sample covers **one entity (Denmark, DKK) and one quarter (Q1 2025)**: about 1,700 invoice lines, 74 customers, 48 SKUs, a GL P&L extract, FX rates and the chart of accounts. All names, customers and numbers are invented.

## Files

| File | Contents |
|---|---|
| `sales_dk_2025_q1.csv` | Invoice and credit-note lines: quantity, list price, discount, net invoiced (LC and EUR), standard cost, margin |
| `gl_pl_dk_2025_q1.csv` | Monthly P&L by account (EUR, Dr+ / Cr-) |
| `customers.csv`, `products.csv` | Master data |
| `accounts.csv`, `entity.csv`, `fx_rates_dkk.csv` | Chart of accounts, entity, DKK rates |

## Try these

1. Rebuild monthly net revenue and gross margin % from the sales lines. Does it tie to the GL?
2. Which customers have the highest discount leakage versus their standard discount?
3. Split a revenue change between price, volume and mix across the three months.

`quick_look.py` shows a first pass with pandas.

## Want the full case?

The complete Nordhavn case (5 entities, 2024 to 2026, budget, forecast history, balance sheet, accruals, open items with deliberate data issues, plus a brief and answer key) is in the paid case pack. A free interview pricing case is available too:

- Shop: https://payhip.com/FinanceEnthusiast
- Free sample: https://payhip.com/b/jkbBg

Built by [Nik Papadopoulos](https://papadopoulos.dk), Financial Controller.

## Licence

Data and code: MIT. Use it for learning, teaching and interviews. The full case pack is licensed separately.
