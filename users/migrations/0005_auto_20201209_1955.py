# Generated by Django 3.1.3 on 2020-12-09 18:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_address_city_district'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address1',
            field=models.CharField(default='Kraków', editable=False, max_length=60, verbose_name='Miasto'),
        ),
        migrations.AlterField(
            model_name='address',
            name='address2',
            field=models.CharField(max_length=60, verbose_name='Ulica'),
        ),
        migrations.AlterField(
            model_name='address',
            name='flat_number',
            field=models.CharField(blank=True, max_length=60, verbose_name='Nr mieszkania'),
        ),
        migrations.AlterField(
            model_name='address',
            name='house_number',
            field=models.CharField(max_length=60, verbose_name='Nr bloku/domu'),
        ),
        migrations.AlterField(
            model_name='address',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Użytkownik'),
        ),
    ]