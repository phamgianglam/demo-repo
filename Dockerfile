FROM python:3.7-slim-buster

RUN apt-get update && apt-get install -y python3-dev build-essential
RUN mkdir -p /usr/src/dvd-api

WORKDIR /usr/src/dvd-api

ENV  DATABASE_URL postgresql://postgres:password@localhost:5432/dvd_api

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 80

CMD ["uvicorn", "--host", "0.0.0.0", "--port", "80", "dvd_apis.app:app"]