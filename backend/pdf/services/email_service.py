import smtplib
import os
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate

from rest_framework.exceptions import NotFound

from pdf.models import Pdf
from pdf.serializers import GetPdfSerializer


def send_email(send_to, subject, pdf_id):
    pdf = Pdf.objects.filter(id=pdf_id, deleted=False).first()
    if not pdf:
        raise NotFound(detail='PDF not found')
    serializer = GetPdfSerializer(pdf)

    POSTMARK_SENDER_SIGNATURE = "eric@rentapplication.net"
    POSTMARK_SMTP_SERVER_HOST = "smtp.postmarkapp.com"
    POSTMARK_SMTP_SERVER_PORT = 587
    POSTMARK_API_KEY = "EDIT_THIS_ONE"
    # Build message
    message = MIMEMultipart()
    message["From"] = POSTMARK_SENDER_SIGNATURE
    message["To"] = send_to
    message["Date"] = formatdate(localtime=True)
    message['Subject'] = subject
    with open(serializer.data['pdf_src'], "rb") as f:
        attach = MIMEApplication(f.read(), _subtype="pdf")
    attach.add_header('Content-Disposition', 'attachment', filename=str(serializer.data['pdf_src']))
    message.attach(attach)
    message.attach(MIMEText("Body message <TO EDIT IT>"))

    # Build smtp client
    smtp_client = smtplib.SMTP(POSTMARK_SMTP_SERVER_HOST, POSTMARK_SMTP_SERVER_PORT)
    smtp_client.connect(POSTMARK_SMTP_SERVER_HOST, POSTMARK_SMTP_SERVER_PORT)
    smtp_client.ehlo()
    smtp_client.starttls()
    smtp_client.ehlo()
    smtp_client.login(POSTMARK_API_KEY, POSTMARK_API_KEY)
    smtp_client.sendmail(POSTMARK_SENDER_SIGNATURE, send_to, message.as_string())
    smtp_client.close()
