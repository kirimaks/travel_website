from flask import current_app as app
from flask import render_template
# from flask_mail import Message
# from apps.main import mail
# from threading import Thread
from mailjet_rest import Client


'''
def send_async_email(msg):
    from ctrl import app
    with app.app_context():
        mail.send(msg)
'''


def send_email(to, subject, template, **kwargs):
    '''
    app.logger.info("Sending email to: [{}]".format(to))
    msg = Message("{}: {}".format(app.config['MAIL_SUBJECT'], subject),
                  sender=app.config['MAIL_SENDER'],
                  recipients=[to])
    msg.body = render_template("mail/{}.txt".format(template), **kwargs)
    msg.html = render_template("mail/{}.html".format(template), **kwargs)

    thr = Thread(target=send_async_email, args=[msg])
    thr.start()
    return thr
    '''

    api_key = app.config['MJ_APIKEY_PUBLIC']
    api_secret = app.config['MJ_APIKEY_PRIVATE']
    mailjet = Client(auth=(api_key, api_secret))

    data = {
        'FromEmail': app.config['MAIL_SENDER'],
        'FromName': 'Grand-Sochi',
        'Subject': app.config['MAIL_SUBJECT'],
        'Text-part': render_template("mail/{}.txt".format(template), **kwargs),
        'Html-part': render_template("mail/{}.html".format(template), **kwargs),
        'Recipients': [{'Email': to}]
    }
    result = mailjet.send.create(data=data)
    print(result.status_code)
    print(result.json())
