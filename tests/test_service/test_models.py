
import pytest

from app.models.payload import PredictionPayload
from app.models.prediction import PredictionResult
from app.services.models import IrisModel


def test_prediction(test_client) -> None:
    hpp = PredictionPayload.parse_obj({
        "sepal_length": 5.1,
        "sepal_width": 3.5,
        "petal_length": 1.4,
        "petal_width": 0.2})

    hpm = IrisModel()
    result = hpm.predict(hpp)
    assert isinstance(result, PredictionResult)


def test_prediction_no_payload(test_client) -> None:
    hpm = IrisModel()
    with pytest.raises(ValueError):
        result = hpm.predict(None)
        assert isinstance(result, PredictionResult)
