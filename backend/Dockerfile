FROM python:3

ENV PYTHONNUNBUFFERED 1
ENV BINKLEY_DB_NAME dexter
ENV BINKLEY_DB_USERNAME dexter
ENV BINKLEY_DB_PASSWORD dexter
ENV POSTMARK_SENDER_SIGNATURE "eric@rentapplication.net"
ENV POSTMARK_SMTP_SERVER_HOST "smtp.postmarkapp.com"
ENV POSTMARK_SMTP_SERVER_PORT "587"
ENV POSTMARK_API_KEY "CHANGE-ME"

RUN mkdir /code
WORKDIR /code
ADD . /code/
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y ghostscript && apt-get update

