# Generated by Django 3.1.3 on 2020-12-08 23:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0014_auto_20201208_2331'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartline',
            name='total_price',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Całkowita kwota zamówienia'),
        ),
    ]
