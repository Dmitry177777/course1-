from datetime import date
from users.models import User, NULLABLE

from django.db import models
from django.urls import reverse

# from django.utils.text import slugify
from pytils.translit import slugify

# NULLABLE = {'blank':True, 'null': True}

class Client(models.Model):
    objects = None
    email = models.OneToOneField(User, on_delete=models.CASCADE, null=False, unique=True, verbose_name='почта_пользователя')
    client = models.CharField(max_length=150, verbose_name='ФИО')
    client_comment = models.CharField(max_length=350, verbose_name='Комментарий', **NULLABLE)
    is_active = models.BooleanField(default=True, verbose_name='Активный клиент')

    def __str__(self):
        return f'{self.email} : {self.client} : {self.client} '


# функция переопределяет удаление и не удаляет объект а переводит флаг is_active = False
    def delete(self, *args, **kwargs):
        self.is_active = False
        self.save()


    class Meta:
        verbose_name='Клиент сервиса'
        verbose_name_plural='Клиенеты сервиса'
        ordering = ('email', )
        # permissions = [
        #     (
        #         "set_published_status",
        #         "Can publish post",
        #     )
        # ]

class Message(models.Model):
    head_message = models.CharField(max_length=150, unique=True, default='сообщение', verbose_name='Тема сообщения')
    email = models.OneToOneField(Client, on_delete=models.CASCADE, null=False, verbose_name='почта_пользователя')
    body_message = models.TextField(max_length=1000, verbose_name='Текст сообщения', **NULLABLE)



    def __str__(self):
        return f'{self.email} : {self.head_message} '

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

class MailingLogs(models.Model):
    email = models.OneToOneField(Client, on_delete=models.CASCADE, null=False, verbose_name='почта_пользователя')
    head_message = models.OneToOneField(Message, on_delete=models.CASCADE, max_length=150, default='сообщение',
                                        verbose_name='Тема сообщения')
    log_time = models.DateTimeField() # дата и время последней попытки
    status_mailing = models.BooleanField(default=False, verbose_name='Статус попытки')  # завершена, создана, запущена
    get_server_mail = models.CharField(max_length=150, verbose_name='Ответ сервера', **NULLABLE)

    class Meta:
        verbose_name = 'Лог рассылки'
        verbose_name_plural = 'Логи рассылки'

    def __str__(self):
        return f'{self.log_time} : {self.status_mailing}'




class MailingSetting(models.Model):
    email = models.OneToOneField(Client, on_delete=models.CASCADE, null=False,  verbose_name='почта_пользователя')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status_mailing = models.BooleanField(default=False, verbose_name='Статус рассылки') # завершена, создана, запущена
    head_message = models.OneToOneField(Message, on_delete=models.CASCADE, max_length=150,  default='сообщение', verbose_name='Тема сообщения')



    class Meta:
        verbose_name = 'Настройка рассылки'
        verbose_name_plural = 'Настройки рассылки'

    def __str__(self):
        return f'{self.email} : {self.start_time} : {self.end_time} '





class Blog(models.Model):
    slug = models.CharField(max_length=250, null=False, unique=True, verbose_name='slug')
    message_preview = models.ImageField(upload_to='message_preview/', verbose_name='Превью', **NULLABLE)
    message_heading = models.CharField(max_length=250, verbose_name='Заголовок')
    message_content= models.TextField(verbose_name='Контент', **NULLABLE)
    date_of_creation = models.DateField(default=date.today, verbose_name='Дата создания')
    date_of_change = models.DateField(default=date.today, verbose_name='Дата последнего изменения')
    is_publication = models.BooleanField(default=True, verbose_name='Опубликовано')
    views_count = models.IntegerField(default=0,verbose_name='Количество просмотров')
    email = models.OneToOneField(User, on_delete=models.CASCADE, null=False, verbose_name='почта_пользователя')



    def __str__(self):
        return f'{self.message_heading} : {self.message_content}'

        # функция переопределения slug
    def get_absolute_url(self):
        return reverse('blog_item', kwargs={'slug': self.slug})  # new


    def save(self, *args, **kwargs):  # new
        self.slug = slugify(self.message_heading)
        return super().save(*args, **kwargs)




    # функция переопределяет удаление и не удаляет объект а переводит флаг is_publication = False
    def delete(self, *args, **kwargs):
            self.is_publication = False
            self.save()

    class Meta:
        verbose_name='Запись блога'
        verbose_name_plural='Записи блога'
        ordering = ('message_heading', )


