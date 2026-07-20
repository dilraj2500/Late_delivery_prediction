import pandas as pd
from pathlib import Path

DATASET = "datasets/DataCoSupplyChainDataset.csv"
OUTPUT_DIR = Path("docs")
OUTPUT_DIR.mkdir(exist_ok=True)

df = pd.read_csv(DATASET, encoding="latin1")

report = pd.DataFrame({
    "Column": df.columns,
    "Data Type": df.dtypes.astype(str).values,
    "Missing Values": df.isnull().sum().values,
    "Missing %": (df.isnull().mean() * 100).round(2).values,
    "Unique Values": df.nunique().values,
})

report.to_csv(OUTPUT_DIR / "data_audit_report.csv", index=False)

print(report)
print("\nAudit Report Saved Successfully.")