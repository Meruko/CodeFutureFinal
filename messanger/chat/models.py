from django.db import models
from django.contrib.auth.models import User
import random
import string
from django.urls import reverse_lazy

INVITE_CODE_LENGTH = 20

# Create your models here.
class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Отправитель')
    text = models.TextField(verbose_name='Текст')
    datetime = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='Дата и время')
    is_deleted = models.BooleanField(default=False, null=True, blank=True, verbose_name='Удалено')

    class Meta:
        ordering = ('datetime',)

    def __str__(self):
        return f'{self.sender} ({self.sender.pk}): {self.text}'

class Room(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    invite_code = models.CharField(max_length=INVITE_CODE_LENGTH, null=True, blank=True, verbose_name='Код приглашения', unique=True)
    members = models.ManyToManyField(User, verbose_name='Участники')
    messages = models.ManyToManyField(Message, verbose_name='Сообщения')

    def get_absolute_url(self):
        return reverse_lazy('room', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name
