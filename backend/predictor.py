import joblib
import pandas as pd
import numpy as np

saved = joblib.load("models/best_model.pkl")

model = saved["model"]
preprocessor = saved["preprocessor"]

def predict(df):
    df = df.astype(object)
    df = df.where(pd.notna(df), other=None)

    X = preprocessor.transform(df)
    prediction = model.predict(X)[0]
    probability = model.predict_proba(X)[0][1]

    return prediction, probability