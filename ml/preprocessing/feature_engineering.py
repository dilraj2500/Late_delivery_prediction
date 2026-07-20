import pandas as pd

DATA_PATH = "datasets/processed/model_dataset.csv"
OUTPUT_PATH = "datasets/processed/final_dataset.csv"
DATE_COL = "order date (DateOrders)"

df = pd.read_csv(DATA_PATH)

df[DATE_COL] = pd.to_datetime(df[DATE_COL], errors="coerce")

df["Order_Year"] = df[DATE_COL].dt.year
df["Order_Month"] = df[DATE_COL].dt.month
df["Order_Day"] = df[DATE_COL].dt.day
df["Order_DayOfWeek"] = df[DATE_COL].dt.dayofweek
df["Is_Weekend"] = (df["Order_DayOfWeek"] >= 5).astype(int)

df = df.drop(columns=[DATE_COL])

print(df.head())

df.to_csv(OUTPUT_PATH, index=False)
print("\nFinal Dataset Saved Successfully.")