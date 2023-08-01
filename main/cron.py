from datetime import datetime

from django.contrib.sites import requests
from django.core.mail import  send_mail
from django.db.models.functions import datetime
from django.http import request

# from rest_framework import request

from config import settings
from main.models import MailingLogs, MailingSetting, Client, Message
from users.models import User
import pytz

#Задача по времени



def send_mail_():

    for mailSet_m in MailingSetting.objects.all():
        print(mailSet_m.email)

        client_m = Client.objects.get(id=mailSet_m.email_id)
        user_m =User.objects.get(id=client_m.email_id)
        print(f"{user_m.email} - {user_m.password} - {user_m.pk}")
        print(mailSet_m.head_message)
        message_m=Message.objects.get(id=mailSet_m.email_id)
        print(message_m.body_message)

        now_w=datetime.datetime.now().replace(tzinfo=pytz.utc)
        start_time = mailSet_m.start_time.replace(tzinfo=pytz.utc)
        end_time = mailSet_m.end_time.replace(tzinfo=pytz.utc)

        if start_time <= now_w <= end_time:
        response = send_mail(
            mailSet_m.head_message,
            message_m.body_message,
            settings.EMAIL_HOST_USER,
            [mailSet_m.email],
        fail_silently = False,
        )


        log_m = MailingLogs()
        log_m.email = mailSet_m.email
        log_m.head_message = mailSet_m.head_message
        log_m.log_time = datetime.datetime.now()
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



