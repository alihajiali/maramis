FROM docker.arvancloud.ir/python:3.12-slim

WORKDIR /app

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python3", "main:app"]