from datetime import datetime

from django.contrib.sites import requests
from django.core.mail import  send_mail
from django.db.models.functions import datetime

from config import settings

#Задача по времени
def task1(MailingSetting):
    for mailS in MailingSetting:

        if mailS.start_time < datetime.now() and datetime.now() < mailS.end_time:
            send_mail(
                "Subject here",
                "Here is the message.",
                settings.EMAIL_HOST_USER,
                [MailingSetting.email],
            fail_silently = False,
            )


def my_scheduled_job():

        token = settings.TG_BOT_TOKEN
        url = f'https://api.telegram.org/bot{token}/sendMessage'
        params = {'chat_id': 216415975, 'text': 'Hello!'}

        response = requests.get(url, params=params)
        if not response.ok:
            raise RuntimeError



