import pandas as pd

DATA_PATH = "datasets/processed/clean_dataset_v1.csv"

df = pd.read_csv(DATA_PATH, encoding="latin1")

print(f"Shape : {df.shape}\n")

print("Dataset Info")
print(df.info())

print("\nTarget Distribution")
print(df["Late_delivery_risk"].value_counts())

print("\nNumerical Summary")
print(df.describe())

print("\nCategorical Summary")
print(df.describe(include="object"))

df["Late_delivery_risk"].value_counts().plot(
    kind="bar", figsize=(6, 5), title="Late Delivery Risk Distribution",
    xlabel="Late Delivery Risk", ylabel="Count"
)
plt.show()