# Generated by Django 3.1.3 on 2020-12-09 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0009_food_description'),
        ('orders', '0019_auto_20201209_1107'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderline',
            name='status',
        ),
        migrations.RemoveField(
            model_name='orderline',
            name='product',
        ),
        migrations.AddField(
            model_name='orderline',
            name='product',
            field=models.ManyToManyField(to='restaurants.Food'),
        ),
    ]