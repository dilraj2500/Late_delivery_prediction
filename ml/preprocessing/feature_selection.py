import pandas as pd

DATA_PATH = "datasets/processed/clean_dataset_v1.csv"
OUTPUT_PATH = "datasets/processed/model_dataset.csv"

LEAKAGE_COLUMNS = [
    "Delivery Status",
    "Days for shipping (real)",
    "Order Status",
]

df = pd.read_csv(DATA_PATH)
df = df.drop(columns=LEAKAGE_COLUMNS)

print(f"Remaining Columns : {df.columns.tolist()}")
print(f"Shape             : {df.shape}")

df.to_csv(OUTPUT_PATH, index=False)
print("\nModel Dataset Saved Successfully!")