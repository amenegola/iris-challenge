FROM python:3.7

EXPOSE 8000

ENV PYTHON_VERSION=3.6 \
    PATH=$HOME/.local/bin/:$PATH \
    PYTHONUNBUFFERED=1 \
    PYTHONIOENCODING=UTF-8 \
    LC_ALL=C.UTF-8 \
    LANG=C.UTF-8 \
    PIP_NO_CACHE_DIR=off

ADD requirements.txt .

RUN pip install -r requirements.txt

ADD app/ /app

ADD .env .

CMD ["uvicorn", "--host", "0.0.0.0", "--port", "8000", "app.main:app"]
