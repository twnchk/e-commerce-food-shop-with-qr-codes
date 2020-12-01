# Generated by Django 3.1.3 on 2020-11-29 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0003_auto_20201127_1652'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='food',
        ),
        migrations.AddField(
            model_name='food',
            name='food',
            field=models.ManyToManyField(blank=True, to='restaurants.Category'),
        ),
    ]