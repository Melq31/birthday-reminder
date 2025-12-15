import smtplib
from email.message import EmailMessage
import os


def send_email(to_email, subject, body):
msg = EmailMessage()
msg['From'] = os.environ['EMAIL_USER']
msg['To'] = to_email
msg['Subject'] = subject
msg.set_content(body)


with smtplib.SMTP('smtp.office365.com', 587) as smtp:
smtp.starttls()
smtp.login(os.environ['EMAIL_USER'], os.environ['EMAIL_PASSWORD'])
smtp.send_message(msg)
