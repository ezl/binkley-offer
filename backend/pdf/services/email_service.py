import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.utils import formatdate

from rest_framework.exceptions import NotFound

from pdf.models import Pdf
from pdf.serializers import GetPdfSerializer

EMAIL_SENDER = "dummy@email.com"
EMAIL_SENDER_PASSWORD = 'dummy_password'
SMTP_SERVER_HOST = "smtp.gmail.com"
SMTP_SERVER_PORT = 587


def send_email(send_to, subject, pdf_id):
    pdf = Pdf.objects.filter(id=pdf_id, deleted=False).first()
    if not pdf:
        raise NotFound(detail='PDF not found')
    serializer = GetPdfSerializer(pdf)

    # Build message
    message = MIMEMultipart()
    message["From"] = EMAIL_SENDER
    message["To"] = send_to
    message["Date"] = formatdate(localtime=True)
    message['Subject'] = subject
    with open(serializer.data['pdf_src'], "rb") as f:
        attach = MIMEApplication(f.read(), _subtype="pdf")
    attach.add_header('Content-Disposition', 'attachment', filename=str(serializer.data['pdf_src']))
    message.attach(attach)

    # Build smtp client
    smtp_client = smtplib.SMTP(SMTP_SERVER_HOST, SMTP_SERVER_PORT)
    smtp_client.connect(SMTP_SERVER_HOST, SMTP_SERVER_PORT)
    smtp_client.ehlo()
    smtp_client.starttls()
    smtp_client.ehlo()
    smtp_client.login(EMAIL_SENDER, EMAIL_SENDER_PASSWORD)
    smtp_client.sendmail(EMAIL_SENDER, send_to, message.as_string())
    smtp_client.close()
