# Generated by Django 3.1.3 on 2020-11-29 17:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='date_placed',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 29, 17, 41, 31, 348223, tzinfo=utc)),
        ),
    ]