from typing import List
from pydantic import BaseModel


class PredictionPayload(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


def payload_to_list(hpp: PredictionPayload) -> List:
    return [
        hpp.sepal_length,
        hpp.sepal_width,
        hpp.petal_length,
        hpp.petal_width]
