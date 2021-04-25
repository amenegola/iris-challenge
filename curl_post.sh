curl -X 'POST' \
  'http://127.0.0.1:8000/api/model/predict' \
  -H 'accept: application/json' \
  -H 'token: 134740f4-1c3c-4dba-ad02-875809d2bf0b' \
  -H 'Content-Type: application/json' \
  -d '{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}'