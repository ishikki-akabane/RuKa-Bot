FROM python:3.10-slim

WORKDIR /ruka

COPY . .

RUN pip install -r requirements.txt

CMD ["python3","-m","RUKA"]
