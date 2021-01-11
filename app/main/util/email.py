import smtplib
from flask_mail import Mail, Message
from flask import current_app
from app.main import mail


# def send_email(to, subject, body):
#     server = smtplib.SMTP_SSL('smtpout.secureserver.net', 465)
#     server.ehlo()
#     server.login("Support@XchangeRate.io", "Support1!")
#     fromaddr = "Support@XchangeRate.io"
#     server.sendmail(fromaddr, to, body)

def send_email(to, subject, body):
    msg = Message(
        subject,
        sender=current_app.config['MAIL_USERNAME'],
        recipients=[to]
    )
    msg.body = body
    mail.send(msg)


def send_email2(to, subject, body):
    msg = Message(
        subject,
        sender='Support@XchangeRate.io ',
        recipients=[to]
    )
    msg.body = body
    mail.send(msg)
