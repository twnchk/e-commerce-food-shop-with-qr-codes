# Generated by Django 3.1.3 on 2020-11-29 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20201129_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='country',
            field=models.CharField(default='Polska', max_length=60),
        ),
    ]