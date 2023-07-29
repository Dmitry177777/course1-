from datetime import datetime

from django.contrib.sites import requests
from django.core.mail import  send_mail
from django.db.models.functions import datetime
from rest_framework import request

from config import settings
from main.models import MailingLogs, MailingSetting, Client
from users.models import User

#Задача по времени



def send_mail_():
    user_m=User.objects.get(pk=1)
    client_m, created=Client.objects.get_or_create(email=user_m)
    print (client_m)
    # log_m = MailingLogs.objects.create(email=client_m[1], log_time=datetime.datetime.now(), status_mailing=False)
    # log_m.save()

    for mailS in MailingSetting.objects.all():
        print(mailS)

        # if mailS.start_time < datetime.now() and datetime.now() < mailS.end_time:
        response = send_mail(
            "Subject here",
            "Here is the message.",
            settings.EMAIL_HOST_USER,
            [mailS.email],
        fail_silently = False,
        )
        log_m.email = MailingSetting.email
        log_m.head_message = "Here is the message."
        log_m.log_time = datetime.now()
        log_m.status_mailing = True
        log_m.get_server_mail = response
        log_m.save()

def my_scheduled_job():

        token = settings.TG_BOT_TOKEN
        url = f'https://api.telegram.org/bot{token}/sendMessage'
        params = {'chat_id': 216415975, 'text': 'Hello!'}

        response = requests.get(url, params=params)
        if not response.ok:
            raise RuntimeError



