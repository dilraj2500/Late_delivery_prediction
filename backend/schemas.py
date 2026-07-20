from typing import Any, Dict
from pydantic import BaseModel

class PredictionRequest(BaseModel):
    data: Dict[str, Any]