FROM python:3.7-alpine
WORKDIR /code

ENV FLASK_APP run.py

COPY run.py gunicorn-cfg.py requirements.txt config.py .env ./

ENV FLASK_RUN_HOST 0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["flask", "run"]


EXPOSE 5005
CMD ["gunicorn", "--config", "gunicorn-cfg.py", "run:app"]
