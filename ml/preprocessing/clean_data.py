import pandas as pd
df = pd.read_csv("C:\\Users\\Dilra\\Desktop\\Late_project\\datasets\\DataCoSupplyChainDataset.csv", encoding="latin1")

print(f"Shape: {df.shape}")
print(f"Columns: {df.columns.tolist()}\n")
df.head()