FROM python:3

ENV PYTHONNUNBUFFERED 1
ENV BINKLEY_DB_NAME dexter
ENV BINKLEY_DB_USERNAME dexter
ENV BINKLEY_DB_PASSWORD dexter

RUN mkdir /code
WORKDIR /code
ADD . /code/
RUN pip install -r requirments.txt
