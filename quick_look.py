"""First look at the Nordhavn sample: monthly revenue, margin and top customers."""
import pandas as pd

sales = pd.read_csv("sales_dk_2025_q1.csv")
cust = pd.read_csv("customers.csv")

monthly = sales.groupby("Period").agg(
    net_eur=("Net invoiced (EUR)", "sum"),
    margin_eur=("Gross margin (EUR)", "sum"),
)
monthly["margin_pct"] = monthly.margin_eur / monthly.net_eur
print(monthly.round(3))

top = (sales.groupby("Customer ID")["Net invoiced (EUR)"].sum()
       .sort_values(ascending=False).head(10).reset_index()
       .merge(cust[["Customer ID", "Customer name", "Segment"]], on="Customer ID"))
print(top)
