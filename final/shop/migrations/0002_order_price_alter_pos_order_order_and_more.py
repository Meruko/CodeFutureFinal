# Generated by Django 5.0.4 on 2024-04-12 17:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="price",
            field=models.FloatField(
                blank=True, default=0.0, null=True, verbose_name="Стоимость"
            ),
        ),
        migrations.AlterField(
            model_name="pos_order",
            name="order",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="shop.order",
                verbose_name="Заказ",
            ),
        ),
        migrations.AlterField(
            model_name="pos_order",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="shop.product",
                verbose_name="Продукт",
            ),
        ),
    ]