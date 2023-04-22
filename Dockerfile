FROM python:3.10-alpine

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app

EXPOSE 8000

CMD uvicorn main:app --reload --host 0.0.0.0