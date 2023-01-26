FROM python:3.10.1-buster

WORKDIR /root/RUKA

COPY . .

RUN pip install -r requirements.txt

CMD ["python3","-m","RUKA"]
