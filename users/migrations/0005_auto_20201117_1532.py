# Generated by Django 3.1.3 on 2020-11-17 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20201117_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='qr_code',
            field=models.ImageField(blank=True, max_length=1000, upload_to='qr_codes'),
        ),
    ]