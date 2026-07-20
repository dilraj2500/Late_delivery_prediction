from database.database import SessionLocal
from database.models import PredictionHistory

def save_prediction(prediction: int, probability: float):
    db = SessionLocal()
    try:
        row = PredictionHistory(
            prediction=prediction,
            probability=probability
        )
        db.add(row)
        db.commit()
        db.refresh(row)  # optional: agar saved row return karna ho
        return row
    except Exception as e:
        db.rollback()    # error pe changes undo karo
        raise e
    finally:
        db.close()