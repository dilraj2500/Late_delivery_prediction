import pandas as pd

df = pd.read_csv("datasets/processed/model_dataset.csv")

counts = df["Late_delivery_risk"].value_counts()
percentages = (counts / len(df) * 100).round(2)

print(pd.DataFrame({"Count": counts, "Percentage": percentages}))