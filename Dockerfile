FROM python:3.10.1-buster

WORKDIR /root/Ruka-Bot

COPY . .

RUN pip install -r requirements.txt

CMD ["python3","-m","RUKA"]
