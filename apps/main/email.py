from flask import current_app as app
from flask import render_template
from flask_mail import Message
from apps.main import mail


def send_email(to, subject, template, **kwargs):
    app.logger.info("Sending email to: [{}]".format(to))
    msg = Message("{}: {}".format(app.config['MAIL_SUBJECT'], subject),
                  sender=app.config['MAIL_SENDER'],
                  recipients=[to])
    msg.body = render_template("mail/{}.txt".format(template), **kwargs)
    msg.html = render_template("mail/{}.html".format(template), **kwargs)
    mail.send(msg)
