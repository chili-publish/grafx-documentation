FROM python:3

WORKDIR /usr/grafx-docs

COPY requirements.txt ./

RUN pip install -r requirements.txt
