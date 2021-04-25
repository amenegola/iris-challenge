#!/bin/bash -e

docker build -t iris-model .

docker tag iris-model gcr.io/via-varejo-mlops/iris-model

docker push gcr.io/via-varejo-mlops/iris-model