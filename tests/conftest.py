import pytest
from starlette.config import environ
from starlette.testclient import TestClient

environ["API_KEY"] = "134740f4-1c3c-4dba-ad02-875809d2bf0b"
environ["BUCKET_MODEL_ARTIFACTS"] = "iris-model-artifacts"
environ["MODEL_FILENAME"] = "model.joblib"
environ["PROJECT"] = "via-varejo-mlops"


from app.main import get_app  # noqa: E402


@pytest.fixture()
def test_client():
    app = get_app()
    with TestClient(app) as test_client:
        yield test_client
