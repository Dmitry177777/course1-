
from django.conf import settings
from django.core.mail import EmailMessage

from main.forms import MailingSettingForm
from main.models import MailingSetting, Message
from datetime import datetime

from scheduler import job



@job
def test_Job(self):
    now = datetime.now()

    for item in self.cleaned_data:
        if item.start_time > now and item.end_time < now:
            message = Message.body_message
            email = EmailMessage(
                item.head_message,
                message,
                to=[item.email],
            )
            email.send()
            print(f"Письмо по адресу {item.email} отправлено")

            item.status_mailing = True


test_Job.delay()



