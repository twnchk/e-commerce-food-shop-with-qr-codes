# Generated by Django 3.1.3 on 2020-12-03 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20201203_1700'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartline',
            name='total_price',
        ),
    ]
