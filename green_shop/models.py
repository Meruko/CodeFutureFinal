from django.db import models
from django.urls import reverse_lazy
from django.contrib.auth.models import User

MAX_LENGTH_CHAR = 256

# Категория растения
class Category(models.Model):
    name = models.CharField(max_length=MAX_LENGTH_CHAR, unique=True, verbose_name='Название')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

# Тип растения
class Type(models.Model):
    name = models.CharField(max_length=MAX_LENGTH_CHAR, unique=True, verbose_name='Название')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип растения'
        verbose_name_plural = 'Типы растений'

# Позиция типа
class Pos_type(models.Model):
    green = models.ForeignKey('Green', on_delete=models.CASCADE, verbose_name='Растение')
    type = models.ForeignKey(Type, on_delete=models.CASCADE, verbose_name='Тип')
    value = models.CharField(max_length=MAX_LENGTH_CHAR, verbose_name='Значение')

    def __str__(self):
        return f'{self.pk} {self.green.name} {self.type.name} {self.value}'

    class Meta:
        verbose_name = 'Позиция типа'
        verbose_name_plural = 'Позиции типов'

# Растение
class Green(models.Model):
    name = models.CharField(max_length=MAX_LENGTH_CHAR, verbose_name='Название')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.FloatField(verbose_name='Стоимость')
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    date_update = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')
    photo = models.ImageField(upload_to='image/%Y/%m/%d', verbose_name='Фотография')
    exists = models.BooleanField(default=True, verbose_name='Существует')

    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    types = models.ManyToManyField(Type, through=Pos_type, verbose_name='Типы')

    def __str__(self):
        return f'{self.name} {self.category}'

    class Meta:
        verbose_name = 'Растение'
        verbose_name_plural = 'Растения'

# Заказ
class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Заказчик')
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    date_finish = models.DateTimeField(null=True, blank=True, verbose_name='Дата завершения')
    price = models.FloatField(default=0.0, verbose_name='Стоимость')

    greens = models.ManyToManyField(Green, through='Pos_order', verbose_name='Растения')

    def __str__(self):
        return f'{self.pk} {self.customer} {self.date_create}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

# Позиция заказа
class Pos_order(models.Model):
    green = models.ForeignKey(Green, on_delete=models.CASCADE, verbose_name='Растение')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заказ')
    count = models.PositiveIntegerField(default=1, verbose_name='Количество растения')

    def __str__(self):
        return f'{self.pk} {self.green.name} {self.order.customer} ({self.count} шт.)'

    def sum_pos_order(self):
        return self.green.price * self.count

    class Meta:
        verbose_name = 'Позиция заказа'
        verbose_name_plural = 'Позиции заказов'
