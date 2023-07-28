from main.cron import send_mail_
from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        print('Принудительный запуск рассылки')
        send_mail_()
        print('Рассылка завершена')
