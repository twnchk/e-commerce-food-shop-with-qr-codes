# Generated by Django 3.1.3 on 2020-12-09 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0031_auto_20201209_1338'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='city_district',
            field=models.CharField(blank=True, max_length=120),
        ),
    ]