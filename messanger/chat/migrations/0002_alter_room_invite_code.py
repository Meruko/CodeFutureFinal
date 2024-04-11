# Generated by Django 5.0.4 on 2024-04-11 06:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("chat", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="room",
            name="invite_code",
            field=models.CharField(
                blank=True,
                default="WWS8PSE5IM1WYES2ULYA",
                max_length=20,
                null=True,
                unique=True,
                verbose_name="Код приглашения",
            ),
        ),
    ]
