# Generated by Django 3.1.3 on 2020-12-09 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0032_order_city_district'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='city_district',
            field=models.CharField(blank=True, max_length=120, verbose_name='Dzielnica'),
        ),
        migrations.AlterField(
            model_name='order',
            name='date_placed',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Data złożenia zamówienia'),
        ),
        migrations.AlterField(
            model_name='order',
            name='date_updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Data aktualizacji'),
        ),
        migrations.AlterField(
            model_name='order',
            name='flat_number',
            field=models.CharField(blank=True, max_length=60, verbose_name='Nr mieszkania'),
        ),
        migrations.AlterField(
            model_name='order',
            name='house_number',
            field=models.CharField(max_length=60, verbose_name='Nr domu'),
        ),
        migrations.AlterField(
            model_name='order',
            name='qr_code',
            field=models.ImageField(blank=True, upload_to='order_qrcodes', verbose_name='Kod QR'),
        ),
        migrations.AlterField(
            model_name='order',
            name='shipping_address1',
            field=models.CharField(max_length=60, verbose_name='Miasto'),
        ),
        migrations.AlterField(
            model_name='order',
            name='shipping_address2',
            field=models.CharField(max_length=60, verbose_name='Ulica'),
        ),
    ]
