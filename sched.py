from datetime import timedelta
#
from django.core.mail import EmailMessage
from main.models import MailingSetting, Message
# import requests
import schedule
from scheduler import job


# Проверка работы модуля scheduler

#
# def greeting():
#     todos_dict ={
#         '08:00': 'Drink coffe',
#         '11:00': 'Work meeting',
#         '17:00': 'Sleeper'
#     }
#
#     print ("Day's tasks")
#     for i,t in todos_dict.items():
#         print(f'{i} - {t}')
#
#     response = requests.get(url='https://yobit.net/api/3/ticker/btc_usd')
#     data = response.json()
#
#     print(data)
#     btc_price = data.get('btc_usd').get('last')
#     print(btc_price)
#     btc_price_ = f"BTC: {round(btc_price,2)} $"
#     print(btc_price_)
@job
def send_email():

    message = Message.body_message
    email = EmailMessage(
        MailingSetting.head_message,
        message,
        to=[MailingSetting.email],
    )
    email.send()
    print(f"Письмо по адресу {MailingSetting.email} отправлено")

if __name__ == '__send_email__':
    send_email()

#
# def send_email():
#     message = Message.body_message
#     email = EmailMessage(
#         MailingSetting.head_message,
#         message,
#         to=[MailingSetting.email],
#     )
#     email.send()
#     print(f"Письмо по адресу {MailingSetting.email} отправлено")
