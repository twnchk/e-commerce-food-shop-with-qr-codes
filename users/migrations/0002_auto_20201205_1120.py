# Generated by Django 3.1.3 on 2020-12-05 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='qr_code',
            field=models.ImageField(upload_to='qr_codes'),
        ),
    ]
