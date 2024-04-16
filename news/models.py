from django.db import models
from django.urls import reverse_lazy


class NewsBD(models.Model):
    title = models.CharField('Заголовок',max_length=50)
    anons = models.CharField('Анонос',max_length=250)
    content = models.TextField('Текст')
    date = models.DateTimeField('Дата и время')

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

        permissions = [
            ('qwerty', 'Возможность qwerty'), ('can_smth', 'Возможность can_smth')
        ]

    def get_absolute_url(self):
        return reverse_lazy('one_news', kwargs={'id': self.pk})