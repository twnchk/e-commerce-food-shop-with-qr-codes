# Generated by Django 3.1.3 on 2020-12-09 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0023_auto_20201209_1243'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderline',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Całkowita wartość zamówienia'),
        ),
    ]
