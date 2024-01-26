FROM python:3.11-slim-bullseye

WORKDIR /app

COPY requirements.txt requirements.txt

RUN python3 -m pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . .

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

