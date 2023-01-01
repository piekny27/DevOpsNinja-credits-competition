FROM python:3.10.5-slim-buster

WORKDIR /credits-competition-view

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD ["python", "app.py"]