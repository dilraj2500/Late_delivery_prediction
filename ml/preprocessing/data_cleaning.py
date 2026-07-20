import pandas as pd
from pathlib import Path

DATA_PATH = "datasets/DataCoSupplyChainDataset.csv"
PROCESSED_DIR = Path("datasets/processed")

DROP_COLUMNS = [
    "Customer Email",
    "Customer Password",
    "Customer Fname",
    "Customer Lname",
    "Customer Street",
    "Product Description",
    "Product Image",
]

# Load
df = pd.read_csv(DATA_PATH, encoding="latin1")
print(f"Original Shape  : {df.shape}")

# Remove duplicates
print(f"Duplicate Rows  : {df.duplicated().sum()}")
df = df.drop_duplicates()

# Drop unnecessary columns
df = df.drop(columns=DROP_COLUMNS)

# Missing value report
missing = pd.DataFrame({
    "Column": df.columns,
    "Missing": df.isnull().sum(),
    "Percentage": (df.isnull().mean() * 100).round(2),
}).sort_values("Percentage", ascending=False)
print("\nMissing Values")
print(missing)

# Save clean dataset
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
df.to_csv(PROCESSED_DIR / "clean_dataset_v1.csv", index=False)

print(f"\nCleaning Completed Successfully — {df.shape}")