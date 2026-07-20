import pandas as pd
from fastapi import APIRouter, HTTPException
from backend.logger import logger
from backend.predictor import predict
from backend.schemas import PredictionRequest
from database.crud import save_prediction

router = APIRouter()

@router.get("/")
def home():
    return {"message": "Late Delivery Risk Prediction API is Running"}

@router.post("/predict")
def make_prediction(request: PredictionRequest):
    try:
        df = pd.DataFrame([request.data])

        prediction, probability = predict(df)

        save_prediction(int(prediction), float(probability))

        logger.info(f"Prediction={prediction}, Probability={probability:.4f}")

        return {
            "prediction": int(prediction),
            "probability": round(float(probability), 4)
        }
    except Exception as e:
        logger.exception("Prediction failed")
        raise HTTPException(status_code=500, detail=str(e))