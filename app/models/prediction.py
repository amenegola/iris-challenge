from pydantic import BaseModel


class PredictionResult(BaseModel):
    iris_class: float
