from django.db import models
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User

MAX_LENGTH_CHAR = 255


class Category(models.Model):
    name = models.CharField(max_length=MAX_LENGTH_CHAR, unique=True, verbose_name='Название')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    def get_absolute_url(self):
        return reverse_lazy('category_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Order(models.Model):
    customer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Заказчик',
        # Данное поле будет заполняться через request.user в views.py приложения basket.py
        null=True,
        blank=True,
    )

    date_create = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания заказа'
    )

    date_finish = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='Дата завершения заказа'
    )

    products = models.ManyToManyField('Product', through='Pos_order')

    def __str__(self):
        return f"{self.pk} {self.customer.username} {self.date_create}"

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class Pos_order(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='Продукт')
    order = models.ForeignKey('Order', on_delete=models.CASCADE, verbose_name='Заказ')
    count = models.PositiveIntegerField(default=1, verbose_name='Количество продукта')

    def sum_pos_order(self):
        return self.product.price * self.count

    def __str__(self):
        return f"{self.pk} {self.product.name} {self.order.customer} ({self.count} шт.)"

    class Meta:
        verbose_name = 'Позиция заказа'
        verbose_name_plural = 'Позиции заказов'


class Parameter(models.Model):
    name = models.CharField(max_length=MAX_LENGTH_CHAR, unique=True, verbose_name='Название характеристики')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Характеристика'
        verbose_name_plural = 'Характеристики'


class Pos_parameter(models.Model):
    product = models.ForeignKey('Product', on_delete=models.PROTECT, verbose_name='Продукт')
    parameter = models.ForeignKey(Parameter, on_delete=models.PROTECT, verbose_name='Характеристика')

    value = models.CharField(max_length=MAX_LENGTH_CHAR, verbose_name='Значение характеристики')

    def __str__(self):
        return f"{self.product.name} {self.parameter.name} {self.value}"

    class Meta:
        verbose_name = 'Позиция характеристики'
        verbose_name_plural = 'Позиции характеристик'


class Product(models.Model):
    name = models.CharField(max_length=MAX_LENGTH_CHAR, verbose_name='Название товара')
    description = models.TextField(blank=True, null=True, verbose_name='Описание товара')
    price = models.FloatField(verbose_name='Цена')
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания записи')
    date_update = models.DateTimeField(auto_now=True, verbose_name='Дата последнего обновления записи')
    photo = models.ImageField(upload_to='image/%Y/%m/%d', null=True, blank=True, verbose_name='Фотография книги')
    exists = models.BooleanField(default=True, verbose_name='Существует ли?')

    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    parameters = models.ManyToManyField(Parameter, through=Pos_parameter)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('product_detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
