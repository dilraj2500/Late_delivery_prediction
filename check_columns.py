import pandas as pd

df = pd.read_csv("datasets/processed/final_dataset.csv")

print("="*60)
print("TOTAL COLUMNS:", len(df.columns))
print("="*60)

for col in df.columns:
    print(col)
