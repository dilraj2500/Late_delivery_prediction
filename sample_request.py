import json
import pandas as pd

df = pd.read_csv("datasets/processed/final_dataset.csv")
sample = df.drop(columns=["Late_delivery_risk"]).iloc[0].to_dict()
print(json.dumps({"data": sample}, indent=4, default=str))