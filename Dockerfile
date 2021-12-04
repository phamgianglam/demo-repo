FROM python:3.7-slim-buster

RUN apt-get update && apt-get install -y python3-dev build-essential
RUN mkdir -p /usr/src/dvd-api

WORKDIR /usr/src/dvd-api

ENV  DATABASE_URI postgresql://postgres:password@localhost:5432/dvd_api

COPY requirement.txt .
RUN pip3 install -r requirement.txt

COPY . .

EXPOSE 80

CMD ["uvicorn", "--host", "0.0.0.0", "--port", "80", "dvd_apis.app:app"]