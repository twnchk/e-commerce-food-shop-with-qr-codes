# Generated by Django 3.1.3 on 2020-12-07 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0005_remove_category_restaurant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodimage',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='food-thumbnails'),
        ),
    ]