# Generated by Django 3.1.3 on 2020-12-15 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0011_auto_20201210_1814'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='image',
            field=models.ImageField(default='static/restaurants/restaurant-default.png', upload_to='restaurant_logos'),
        ),
    ]
