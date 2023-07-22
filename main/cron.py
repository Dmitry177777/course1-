from datetime import time

from django.core.mail import EmailMessage
from django.db.models.functions import datetime

from main.models import Client, MailingSetting, Blog, Message, MailingLogs
from django.template.loader import render_to_string

# Задача по времени
def task1():

    try:
        loca_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print('Местное время:' + str(loca_time))

    except Exception as e:
        print('Произошла ошибка, сообщение об ошибке:', e)


def send_email(self, MailingSetting, ):
        # current_site = get_current_site(request)

        for mailS in MailingSetting:

            if mailS.start_time < datetime.now() and datetime.now()< mailS.end_time:

                message = Message.body_message
                email = EmailMessage(
                    MailingSetting.head_message,
                    message,
                    to=[MailingSetting.email],
                )
                email.send()

def my_cron_job():
    # your functionality goes here
    print('1')