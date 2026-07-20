import joblib
import pandas as pd

MODEL_PATH = "models/best_model.pkl"
OUTPUT_PATH = "docs/logistic_feature_importance.csv"

saved = joblib.load(MODEL_PATH)
model = saved["model"]
preprocessor = saved["preprocessor"]
print("Model Loaded Successfully!")
print(type(model))

importance = pd.DataFrame({
    "Feature": preprocessor.get_feature_names_out(),
    "Coefficient": model.coef_[0],
})
importance["Absolute Coefficient"] = importance["Coefficient"].abs()
importance = importance.sort_values("Absolute Coefficient", ascending=False)

print("\nTop 20 Important Features\n")
print(importance.head(20))

importance.to_csv(OUTPUT_PATH, index=False)
print(f"\nFeature Importance saved to {OUTPUT_PATH}")