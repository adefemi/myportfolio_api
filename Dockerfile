FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /myportfolio

WORKDIR /myportfolio

COPY . /myportfolio/

RUN pip install -r requirements.txt