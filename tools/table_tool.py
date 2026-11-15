import sys
import pandas as pd
from rich.console import Console
from rich.table import Table

df = pd.read_csv(sys.argv[1])
result = df[df["os"] == "Ubuntu"]

table = Table(title="Ubuntu servers")
for col in result.columns:
    table.add_column(col)
for _, row in result.iterrows():
    table.add_row(*[str(v) for v in row])

Console().print(table)
result.to_excel("ubuntu_servers.xlsx", index=False)
print("Saved ubuntu_servers.xlsx")