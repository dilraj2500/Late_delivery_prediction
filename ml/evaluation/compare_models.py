import time
from pathlib import Path

import joblib
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from xgboost import XGBClassifier

DATA_PATH = "datasets/processed/final_dataset.csv"
TARGET = "Late_delivery_risk"
LEAKAGE_COLUMNS = ["Delivery Status", "Days for shipping (real)"]

DOCS_DIR = Path("docs")
MODELS_DIR = Path("models")
DOCS_DIR.mkdir(exist_ok=True)
MODELS_DIR.mkdir(exist_ok=True)

df = pd.read_csv(DATA_PATH)
df = df.drop(columns=[c for c in LEAKAGE_COLUMNS if c in df.columns])

X = df.drop(columns=[TARGET])
y = df[TARGET]
print(f"Dataset Shape : {df.shape}")
print(f"Features      : {X.shape[1]}")

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)

numeric_features = X.select_dtypes(include=["number"]).columns
categorical_features = X.select_dtypes(include=["object", "string", "category"]).columns

preprocessor = ColumnTransformer([
    ("num", Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler()),
    ]), numeric_features),
    ("cat", Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(handle_unknown="ignore")),
    ]), categorical_features),
])

print("\nPreprocessing data...")
X_train_processed = preprocessor.fit_transform(X_train)
X_test_processed = preprocessor.transform(X_test)
print("Preprocessing Completed!")

models = {
    "Logistic Regression": LogisticRegression(max_iter=1000, n_jobs=-1, random_state=42),
    "Random Forest": RandomForestClassifier(
        n_estimators=50, max_depth=15, min_samples_split=10,
        min_samples_leaf=5, n_jobs=-1, random_state=42,
    ),
    "XGBoost": XGBClassifier(
        n_estimators=100, max_depth=6, learning_rate=0.1,
        subsample=0.8, colsample_bytree=0.8, tree_method="hist",
        eval_metric="logloss", random_state=42,
    ),
}

results = []
best_model, best_score = None, 0

print("\nMODEL TRAINING")
for name, model in models.items():
    print(f"\nTraining {name}...")
    start = time.time()
    model.fit(X_train_processed, y_train)
    training_time = round(time.time() - start, 2)

    pred = model.predict(X_test_processed)
    prob = model.predict_proba(X_test_processed)[:, 1]
    roc = roc_auc_score(y_test, prob)

    results.append({
        "Model": name,
        "Accuracy": round(accuracy_score(y_test, pred), 4),
        "Precision": round(precision_score(y_test, pred), 4),
        "Recall": round(recall_score(y_test, pred), 4),
        "F1 Score": round(f1_score(y_test, pred), 4),
        "ROC AUC": round(roc, 4),
        "Training Time (sec)": training_time,
    })
    print(f"Completed in {training_time} sec")

    if roc > best_score:
        best_score, best_model = roc, model

results_df = pd.DataFrame(results)
print("\nMODEL COMPARISON")
print(results_df)

results_df.to_csv(DOCS_DIR / "model_comparison.csv", index=False)
joblib.dump({"model": best_model, "preprocessor": preprocessor}, MODELS_DIR / "best_model.pkl")

print("\nBest Model Saved Successfully!")
print(f"Best ROC-AUC : {best_score:.4f}")