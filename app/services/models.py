import os
import joblib
import tempfile
import numpy as np

from typing import List
from loguru import logger
from google.cloud import storage

from app.core.config import PROJECT, BUCKET_MODEL_ARTIFACTS, MODEL_FILENAME
from app.core.messages import NO_VALID_PAYLOAD
from app.models.payload import (PredictionPayload,
                                payload_to_list)
from app.models.prediction import PredictionResult


class IrisModel():

    def __init__(self):
        self._load_model()

    def _load_model(self):
        storage_client = storage.Client(PROJECT)
        bucket = storage_client.get_bucket(BUCKET_MODEL_ARTIFACTS)
        blob = bucket.blob(MODEL_FILENAME)
        with tempfile.TemporaryDirectory() as tmpdirname:
            local_path = os.path.join(tmpdirname, MODEL_FILENAME)
            blob.download_to_filename(local_path)
            self.model = joblib.load(local_path)

    def _pre_process(self, payload: PredictionPayload) -> List:
        logger.debug("Pre-processing payload.")
        result = np.asarray(payload_to_list(payload)).reshape(1, -1)
        return result

    def _post_process(self, prediction: np.ndarray) -> PredictionResult:
        logger.debug("Post-processing prediction.")
        result = prediction.tolist()
        hpp = PredictionResult(iris_class=result[0])
        return hpp

    def _predict(self, features: List) -> np.ndarray:
        logger.debug("Predicting.")
        prediction_result = self.model.predict(features)
        return prediction_result

    def predict(self, payload: PredictionPayload):
        if payload is None:
            raise ValueError(NO_VALID_PAYLOAD.format(payload))

        pre_processed_payload = self._pre_process(payload)
        prediction = self._predict(pre_processed_payload)
        logger.info(prediction)
        post_processed_result = self._post_process(prediction)

        return post_processed_result
