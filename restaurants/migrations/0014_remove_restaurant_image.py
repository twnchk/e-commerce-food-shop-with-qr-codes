# Generated by Django 3.1.3 on 2020-12-15 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0013_auto_20201215_1634'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='image',
        ),
    ]
