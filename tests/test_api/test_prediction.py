from app.core import config


def test_prediction(test_client) -> None:
    response = test_client.post(
        "/api/model/predict",
        json={
            "sepal_length": 5.1,
            "sepal_width": 3.5,
            "petal_length": 1.4,
            "petal_width": 0.2},
        headers={"token": str(config.API_KEY)})
    assert response.status_code == 200
    assert "iris_class" in response.json()


def test_prediction_nopayload(test_client) -> None:
    response = test_client.post(
        "/api/model/predict",
        json={},
        headers={"token": str(config.API_KEY)}
    )
    assert response.status_code == 422
