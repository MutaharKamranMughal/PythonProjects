# Go over to your email account and setup 2 factor authentication.
# generate app password 
# Create a function to send the mail

from email.message import EmailMessage
from app0 import password
import ssl
import smtplib

email_sender = '' # Eneter your email
email_password = password # Go to app0 and enter your password.

email_receiver = ''  # Enter Recievers Email

subject = 'Bachoda'

body = """

""" # Enter Body of email.

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
