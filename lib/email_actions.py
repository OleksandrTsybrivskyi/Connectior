import os
from email.message import EmailMessage
import ssl
import smtplib

import hashlib
import random

import time

def create_activation_code():
    """Hashes a password using the SHA-256 algorithm."""
    hash_object = hashlib.sha256()
    random_number = str(random.randint(0, 999999999)) + "dev" #dev must be replaced with random string
    hash_object.update(random_number.encode('utf-8'))
    return hash_object.hexdigest()


def send_email(email_receiver, subject, body):
    email_sender = "kodova.bryhada@gmail.com"
    # email_password = os.environ.get("EMAIL_PASSWORD")
    email_password = "djfb xumm nfcv mpxl"

    em = EmailMessage()
    em["From"] = email_sender
    em["To"] = email_receiver
    em["Subject"] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())


def send_email_activation_letter(email_receiver):
    activation_code = create_activation_code()

    subject = "Account activation"
    body = f"""
    To activate your Connectior account follow this link:
    http://127.0.0.1:5000/auth/activate?activation_code={activation_code}
    """
    send_email(email_receiver=email_receiver, subject=subject, body=body)

    return activation_code


