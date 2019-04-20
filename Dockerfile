FROM python:3.6

ENV PYTHONUNBUFFERED 1
RUN mkdir /webapps
WORKDIR /webapps

RUN pip install -U pip setuptools

COPY requirements.txt /webapps/

RUN pip install -r /webapps/requirements.txt

ADD . /webapps/

# Django service
EXPOSE 8000