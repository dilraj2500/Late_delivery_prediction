from pathlib import Path

import joblib
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay, RocCurveDisplay, classification_report
from sklearn.model_selection import train_test_split

DATA_PATH = "datasets/processed/final_dataset.csv"
MODEL_PATH = "models/best_model.pkl"
TARGET = "Late_delivery_risk"
LEAKAGE_COLUMNS = ["Delivery Status", "Days for shipping (real)"]

if not Path(DATA_PATH).exists():
    raise FileNotFoundError(f"Dataset not found: {DATA_PATH}")
if not Path(MODEL_PATH).exists():
    raise FileNotFoundError(f"Model not found: {MODEL_PATH}")

df = pd.read_csv(DATA_PATH)
X = df.drop(columns=[TARGET])
y = df[TARGET]
X = X.drop(columns=[c for c in LEAKAGE_COLUMNS if c in X.columns])

saved = joblib.load(MODEL_PATH)
model = saved["model"]
preprocessor = saved["preprocessor"]

_, X_test, _, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)
X_test_processed = preprocessor.transform(X_test)
pred = model.predict(X_test_processed)

print(classification_report(y_test, pred))

fig, axes = plt.subplots(1, 2, figsize=(12, 5))
ConfusionMatrixDisplay.from_predictions(y_test, pred, ax=axes[0])
axes[0].set_title("Confusion Matrix")

if hasattr(model, "predict_proba"):
    RocCurveDisplay.from_estimator(model, X_test_processed, y_test, ax=axes[1])
    axes[1].set_title("ROC Curve")
else:
    axes[1].axis("off")
    axes[1].text(0.5, 0.5, "ROC Curve unavailable\n(model has no predict_proba)",
                  ha="center", va="center")

plt.tight_layout()
plt.show()